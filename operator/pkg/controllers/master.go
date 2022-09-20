// Copyright 2022 The EasyDL Authors. All rights reserved.
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package controllers

import (
	"context"
	"fmt"
	elasticv1alpha1 "github.com/intelligent-machine-learning/easydl/operator/api/v1alpha1"
	commonv1 "github.com/kubeflow/common/pkg/apis/common/v1"
	commonutil "github.com/kubeflow/common/pkg/util"
	logger "github.com/sirupsen/logrus"
	corev1 "k8s.io/api/core/v1"
	"k8s.io/apimachinery/pkg/api/errors"
	"k8s.io/apimachinery/pkg/api/resource"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	ctrl "sigs.k8s.io/controller-runtime"
)

const (
	initMasterContainerCPU     = "2"
	initMasterContainerMemory  = "4Gi"
	initMasterContainerStorage = "4Gi"
	masterCommand              = "python -m elasticdl.python.master.main"
	masterImage                = "easydl/easydl-master:v1.0.0"
)

// MasterManager generates a master pod object.
type MasterManager struct {
	PodManager
}

func newMasterManager() *MasterManager {
	return &MasterManager{}
}

func (m *MasterManager) generateEasydlMaster(job *elasticv1alpha1.ElasticJob) *corev1.Pod {
	container := corev1.Container{
		Name:            "main",
		Image:           masterImage,
		ImagePullPolicy: corev1.PullAlways,
		Command:         []string{"/bin/bash", "-c", masterCommand},
		Resources: corev1.ResourceRequirements{
			Requests: corev1.ResourceList{
				corev1.ResourceCPU:              resource.MustParse(initMasterContainerCPU),
				corev1.ResourceMemory:           resource.MustParse(initMasterContainerMemory),
				corev1.ResourceEphemeralStorage: resource.MustParse(initMasterContainerStorage),
			},
			Limits: corev1.ResourceList{
				corev1.ResourceCPU:              resource.MustParse(initMasterContainerCPU),
				corev1.ResourceMemory:           resource.MustParse(initMasterContainerMemory),
				corev1.ResourceEphemeralStorage: resource.MustParse(initMasterContainerStorage),
			},
		},
	}
	podTemplate := &corev1.PodTemplateSpec{
		Spec: corev1.PodSpec{
			Containers:    []corev1.Container{container},
			RestartPolicy: corev1.RestartPolicyNever,
		},
	}
	masterName := m.generatePodName(job)
	pod := m.GeneratePod(job, podTemplate, masterName)
	return pod
}

func (m *MasterManager) createPod(r *ElasticJobReconciler, job *elasticv1alpha1.ElasticJob) error {
	masterPod := m.generateEasydlMaster(job)
	err := r.Create(context.Background(), masterPod)
	if err != nil {
		r.Recorder.Eventf(job, corev1.EventTypeWarning, string(commonv1.JobFailed), "master pod created failed: %v", err)
		return err
	}
	return nil
}

func (m *MasterManager) generatePodName(job *elasticv1alpha1.ElasticJob) string {
	return fmt.Sprintf("%s-%s", job.GetName(), string(ReplicaTypeEasydlMaster))
}

func (m *MasterManager) syncMasterState(r *ElasticJobReconciler, job *elasticv1alpha1.ElasticJob) error {
	master, err := m.getMasterPod(r, job)
	if err != nil {
		logger.Warnf("Failed to get master, error : %v", err)
	}
	if master == nil {
		return nil
	}
	if master.Status.Phase == corev1.PodSucceeded {
		job.Status.ReplicaStatuses[ReplicaTypeEasydlMaster].Succeeded = 1
		msg := fmt.Sprintf("job(%s/%s) successfully completed", job.Namespace, job.Name)
		r.Recorder.Event(job, corev1.EventTypeNormal, string(commonv1.JobSucceeded), msg)
		if job.Status.CompletionTime == nil {
			now := metav1.Now()
			job.Status.CompletionTime = &now
		}
		updateStatus(&job.Status, commonv1.JobSucceeded, commonutil.JobCreatedReason, msg)
	} else if master.Status.Phase == corev1.PodFailed {
		job.Status.ReplicaStatuses[ReplicaTypeEasydlMaster].Failed = 1
		msg := fmt.Sprintf("job(%s/%s) has failed", job.Namespace, job.Name)
		reason := master.Status.Reason
		if reason == "" {
			reason = commonutil.JobFailedReason
		}
		r.Recorder.Event(job, corev1.EventTypeWarning, reason, msg)
		if job.Status.CompletionTime == nil {
			now := metav1.Now()
			job.Status.CompletionTime = &now
		}
		updateStatus(&job.Status, commonv1.JobFailed, reason, msg)
	} else if master.Status.Phase == corev1.PodRunning || master.Status.Phase == corev1.PodPending {
		job.Status.ReplicaStatuses[ReplicaTypeEasydlMaster].Active = 1
		if !isRunning(job.Status) {
			msg := fmt.Sprintf("job(%s/%s) is running.", job.Namespace, job.Name)
			updateStatus(&job.Status, commonv1.JobRunning, commonutil.JobRunningReason, msg)
			r.Recorder.Event(job, corev1.EventTypeNormal, commonutil.JobRunningReason, msg)
		}
	}
	return nil
}

// getMasterPod gets the master pod of a job from a cluster.
func (m *MasterManager) getMasterPod(r *ElasticJobReconciler, job *elasticv1alpha1.ElasticJob) (*corev1.Pod, error) {
	master := &corev1.Pod{}
	name := ctrl.Request{}
	name.NamespacedName.Namespace = job.GetNamespace()
	name.NamespacedName.Name = m.generatePodName(job)
	err := r.Get(context.Background(), name.NamespacedName, master)
	if errors.IsNotFound(err) {
		return nil, err
	}
	return master, nil
}
