# Copyright 2022 The DLRover Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from dlrover.python.common.constants import JobExitReason, NodeStatus, NodeType
from dlrover.python.elastic_agent.master_client import build_master_client
from dlrover.python.master.dist_master import DistributedJobMaster
from dlrover.python.master.shard.dataset_splitter import new_dataset_splitter
from dlrover.python.tests.test_utils import (
    MockK8sPSJobArgs,
    mock_k8s_client,
    start_local_master,
)


class DistributedJobMasterTest(unittest.TestCase):
    def setUp(self) -> None:
        mock_k8s_client()
        params = MockK8sPSJobArgs()
        params.initilize()
        self.master = DistributedJobMaster(2222, params)

    def test_exit_by_workers(self):
        self.master.job_manager._init_nodes()
        job_nodes = self.master.job_manager._job_nodes
        for node in job_nodes[NodeType.WORKER].values():
            node.status = NodeStatus.FINISHED
        for node in job_nodes[NodeType.EVALUATOR].values():
            node.status = NodeStatus.FINISHED
        for node in job_nodes[NodeType.CHIEF].values():
            node.status = NodeStatus.FINISHED
        self.master.run()
        self.assertEqual(self.master._exit_code, 0)
        self.assertEqual(self.master._exit_reason, JobExitReason.SUCCEEDED)

    def test_exit_by_tasks(self):
        self.master.job_manager._init_nodes()
        job_nodes = self.master.job_manager._job_nodes
        for node in job_nodes[NodeType.PS].values():
            node.status = NodeStatus.FINISHED
        for node in job_nodes[NodeType.EVALUATOR].values():
            node.status = NodeStatus.FINISHED
        for node in job_nodes[NodeType.CHIEF].values():
            node.status = NodeStatus.FINISHED

        job_nodes[NodeType.WORKER][0].status = NodeStatus.FINISHED

        splitter = new_dataset_splitter(
            False,
            100,
            10000,
            1,
            "test",
            "table",
        )

        self.master.task_manager.new_dataset(10, 10000, "test", splitter)

        for dataset in self.master.task_manager._datasets.values():
            dataset.todo.clear()
            dataset.doing.clear()
            dataset._dataset_splitter.epoch = 10
        self.master.run()
        self.assertEqual(self.master._exit_code, 0)
        self.assertEqual(self.master._exit_reason, JobExitReason.SUCCEEDED)


class LocalJobMasterTest(unittest.TestCase):
    def setUp(self) -> None:
        self._master, addr = start_local_master()
        self.master_client = build_master_client(addr)

    def addCleanup(self):
        self._master.stop()

    def test_task_manager(self):
        self.master_client.report_dataset_shard_params(
            64, 1, 10000, False, 10, "test-ds"
        )
        succeed, task = self.master_client.get_task("test-ds")
        self.assertTrue(succeed)
        self.assertEqual(task.shard.start, 0)
        self.assertEqual(task.shard.end, 640)
        succeed = self.master_client.report_task_result("test-ds", 0, "")
        self.assertTrue(succeed)

    def test_rdzv_manager(self):
        self.master_client.report_rdzv_params(1, 1, 360, 1)
        self.master_client.join_rendezvous(0, 8, "elastic-training")
        group, world = self.master_client.get_comm_world("elastic-training", 0)
        self.assertEqual(group, 1)
        self.assertEqual(world[0], 8)
