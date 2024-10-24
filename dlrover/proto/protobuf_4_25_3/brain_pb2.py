# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: brain.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x62rain.proto\x12\x05\x62rain\x1a\x1bgoogle/protobuf/empty.proto\"K\n\x13TrainingHyperParams\x12\x12\n\nbatch_size\x18\x01 \x01(\x03\x12\r\n\x05\x65poch\x18\x02 \x01(\x03\x12\x11\n\tmax_steps\x18\x03 \x01(\x03\"\x97\x01\n\x0fWorkflowFeature\x12\x10\n\x08job_name\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x14\n\x0c\x63ode_address\x18\x03 \x01(\t\x12\x13\n\x0bworkflow_id\x18\x04 \x01(\t\x12\x0f\n\x07node_id\x18\x05 \x01(\t\x12\x14\n\x0codps_project\x18\x06 \x01(\t\x12\x0f\n\x07is_prod\x18\x07 \x01(\x08\"\xfe\x01\n\x12TrainingSetFeature\x12\x14\n\x0c\x64\x61taset_size\x18\x01 \x01(\x03\x12\x14\n\x0c\x64\x61taset_name\x18\x02 \x01(\t\x12\x19\n\x11sparse_item_count\x18\x03 \x01(\x03\x12\x17\n\x0fsparse_features\x18\x04 \x01(\t\x12\x1d\n\x15sparse_feature_groups\x18\x05 \x01(\t\x12\x1d\n\x15sparse_feature_shapes\x18\x06 \x01(\t\x12\x16\n\x0e\x64\x65nse_features\x18\x07 \x01(\t\x12\x1c\n\x14\x64\x65nse_feature_shapes\x18\x08 \x01(\t\x12\x14\n\x0cstorage_size\x18\t \x01(\x03\"\x97\x03\n\x0cModelFeature\x12\x16\n\x0evariable_count\x18\x01 \x01(\x03\x12\x10\n\x08op_count\x18\x02 \x01(\x03\x12\x1b\n\x13\x65mbedding_dimension\x18\x03 \x01(\x03\x12\x1b\n\x13total_variable_size\x18\x04 \x01(\x03\x12\x19\n\x11max_variable_size\x18\x05 \x01(\x03\x12\x17\n\x0fupdate_op_count\x18\x06 \x01(\x03\x12\x15\n\rread_op_count\x18\x07 \x01(\x03\x12\x17\n\x0finput_fetch_dur\x18\x08 \x01(\x03\x12\r\n\x05\x66lops\x18\t \x01(\x03\x12\x15\n\rrecv_op_count\x18\n \x01(\x03\x12\x19\n\x11kv_embedding_dims\x18\x0b \x03(\x03\x12\x45\n\x12tensor_alloc_bytes\x18\x0c \x03(\x0b\x32).brain.ModelFeature.TensorAllocBytesEntry\x1a\x37\n\x15TensorAllocBytesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"k\n\x0bRuntimeInfo\x12\x13\n\x0bglobal_step\x18\x01 \x01(\x03\x12$\n\x0crunning_pods\x18\x02 \x03(\x0b\x32\x0e.brain.PodMeta\x12\x12\n\ntime_stamp\x18\x03 \x01(\x03\x12\r\n\x05speed\x18\x04 \x01(\x02\"\x9a\x01\n\x07PodMeta\x12\x10\n\x08pod_name\x18\x01 \x01(\t\x12\x0e\n\x06pod_ip\x18\x02 \x01(\t\x12\x0f\n\x07node_ip\x18\x03 \x01(\t\x12\x11\n\thost_name\x18\x04 \x01(\t\x12\x11\n\tnamespace\x18\x05 \x01(\t\x12\x10\n\x08is_mixed\x18\x06 \x01(\x08\x12\x11\n\tmem_usage\x18\x07 \x01(\x01\x12\x11\n\tcpu_usage\x18\x08 \x01(\x01\"W\n\x07JobMeta\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x0f\n\x07\x63luster\x18\x04 \x01(\t\x12\x11\n\tnamespace\x18\x05 \x01(\t\"\xa1\x04\n\nJobMetrics\x12\x12\n\ndata_store\x18\x01 \x01(\t\x12 \n\x08job_meta\x18\x02 \x01(\x0b\x32\x0e.brain.JobMeta\x12(\n\x0cmetrics_type\x18\x03 \x01(\x0e\x32\x12.brain.MetricsType\x12;\n\x15training_hyper_params\x18\x04 \x01(\x0b\x32\x1a.brain.TrainingHyperParamsH\x00\x12\x32\n\x10workflow_feature\x18\x05 \x01(\x0b\x32\x16.brain.WorkflowFeatureH\x00\x12\x39\n\x14training_set_feature\x18\x06 \x01(\x0b\x32\x19.brain.TrainingSetFeatureH\x00\x12,\n\rmodel_feature\x18\x07 \x01(\x0b\x32\x13.brain.ModelFeatureH\x00\x12*\n\x0cruntime_info\x18\x08 \x01(\x0b\x32\x12.brain.RuntimeInfoH\x00\x12\x19\n\x0fjob_exit_reason\x18\t \x01(\tH\x00\x12\x14\n\nextra_info\x18\n \x01(\tH\x00\x12\x0e\n\x04type\x18\x0b \x01(\tH\x00\x12\x12\n\x08resource\x18\x0c \x01(\tH\x00\x12\x19\n\x0f\x63ustomized_data\x18\r \x01(\tH\x00\x12\x32\n\x10job_optimization\x18\x0e \x01(\x0b\x32\x16.brain.JobOptimizationH\x00\x42\t\n\x07metrics\"\xe2\x01\n\x0eOptimizeConfig\x12\"\n\x1aoptimizer_config_retriever\x18\x01 \x01(\t\x12\x12\n\ndata_store\x18\x02 \x01(\t\x12\x17\n\x0f\x62rain_processor\x18\x03 \x01(\t\x12\x46\n\x11\x63ustomized_config\x18\x04 \x03(\x0b\x32+.brain.OptimizeConfig.CustomizedConfigEntry\x1a\x37\n\x15\x43ustomizedConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x89\x02\n\x08PodState\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0e\n\x06is_oom\x18\x04 \x01(\x08\x12$\n\x08resource\x18\x05 \x01(\x0b\x32\x12.brain.PodResource\x12)\n\rused_resource\x18\x06 \x01(\x0b\x32\x12.brain.PodResource\x12<\n\x0f\x63ustomized_data\x18\x07 \x03(\x0b\x32#.brain.PodState.CustomizedDataEntry\x1a\x35\n\x13\x43ustomizedDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x88\x02\n\x08JobState\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\'\n\x04pods\x18\x02 \x03(\x0b\x32\x19.brain.JobState.PodsEntry\x12\r\n\x05speed\x18\x03 \x01(\x02\x12<\n\x0f\x63ustomized_data\x18\x04 \x03(\x0b\x32#.brain.JobState.CustomizedDataEntry\x1a<\n\tPodsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.brain.PodState:\x02\x38\x01\x1a\x35\n\x13\x43ustomizedDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"b\n\x0fOptimizeJobMeta\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0f\n\x07\x63luster\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x1e\n\x05state\x18\x04 \x01(\x0b\x32\x0f.brain.JobState\"l\n\x0fOptimizeRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.brain.OptimizeConfig\x12$\n\x04jobs\x18\x03 \x03(\x0b\x32\x16.brain.OptimizeJobMeta\"[\n\x0bPodResource\x12\x0e\n\x06memory\x18\x01 \x01(\x03\x12\x0b\n\x03\x63pu\x18\x02 \x01(\x02\x12\x0b\n\x03gpu\x18\x03 \x01(\x02\x12\x10\n\x08gpu_type\x18\x04 \x01(\t\x12\x10\n\x08priority\x18\x05 \x01(\t\"H\n\x11TaskGroupResource\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12$\n\x08resource\x18\x02 \x01(\x0b\x32\x12.brain.PodResource\"\xb2\x02\n\x0bJobResource\x12H\n\x14task_group_resources\x18\x01 \x03(\x0b\x32*.brain.JobResource.TaskGroupResourcesEntry\x12;\n\rpod_resources\x18\x02 \x03(\x0b\x32$.brain.JobResource.PodResourcesEntry\x1aS\n\x17TaskGroupResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.brain.TaskGroupResource:\x02\x38\x01\x1aG\n\x11PodResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.brain.PodResource:\x02\x38\x01\"o\n\x0fJobOptimizePlan\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12$\n\x08resource\x18\x02 \x01(\x0b\x32\x12.brain.JobResource\x12#\n\x03job\x18\x03 \x01(\x0b\x32\x16.brain.OptimizeJobMeta\"\x96\x01\n\x0fJobOptimization\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.brain.OptimizeConfig\x12$\n\x04plan\x18\x03 \x01(\x0b\x32\x16.brain.JobOptimizePlan\x12#\n\njob_states\x18\x04 \x03(\x0b\x32\x0f.brain.JobState\"+\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06reason\x18\x02 \x01(\t\"i\n\x10OptimizeResponse\x12!\n\x08response\x18\x01 \x01(\x0b\x32\x0f.brain.Response\x12\x32\n\x12job_optimize_plans\x18\x02 \x03(\x0b\x32\x16.brain.JobOptimizePlan\"%\n\x11JobMetricsRequest\x12\x10\n\x08job_uuid\x18\x01 \x01(\t\"L\n\x12JobMetricsResponse\x12!\n\x08response\x18\x01 \x01(\x0b\x32\x0f.brain.Response\x12\x13\n\x0bjob_metrics\x18\x02 \x01(\t*\xea\x01\n\x0bMetricsType\x12\x19\n\x15Training_Hyper_Params\x10\x00\x12\x14\n\x10Workflow_Feature\x10\x01\x12\x18\n\x14Training_Set_Feature\x10\x02\x12\x11\n\rModel_Feature\x10\x03\x12\x10\n\x0cRuntime_Info\x10\x04\x12\x13\n\x0fJob_Exit_Reason\x10\x05\x12\x17\n\x13Optimization_Result\x10\x06\x12\x08\n\x04Type\x10\x07\x12\x0c\n\x08Resource\x10\x08\x12\x13\n\x0f\x43ustomized_Data\x10\t\x12\x10\n\x0cOptimization\x10\n2\xca\x01\n\x05\x42rain\x12<\n\x0fpersist_metrics\x12\x11.brain.JobMetrics\x1a\x16.google.protobuf.Empty\x12;\n\x08optimize\x12\x16.brain.OptimizeRequest\x1a\x17.brain.OptimizeResponse\x12\x46\n\x0fget_job_metrics\x12\x18.brain.JobMetricsRequest\x1a\x19.brain.JobMetricsResponseB\x1cZ\x1a\x64lrover/go/brain/pkg/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'brain_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\032dlrover/go/brain/pkg/proto'
  _MODELFEATURE_TENSORALLOCBYTESENTRY._options = None
  _MODELFEATURE_TENSORALLOCBYTESENTRY._serialized_options = b'8\001'
  _OPTIMIZECONFIG_CUSTOMIZEDCONFIGENTRY._options = None
  _OPTIMIZECONFIG_CUSTOMIZEDCONFIGENTRY._serialized_options = b'8\001'
  _PODSTATE_CUSTOMIZEDDATAENTRY._options = None
  _PODSTATE_CUSTOMIZEDDATAENTRY._serialized_options = b'8\001'
  _JOBSTATE_PODSENTRY._options = None
  _JOBSTATE_PODSENTRY._serialized_options = b'8\001'
  _JOBSTATE_CUSTOMIZEDDATAENTRY._options = None
  _JOBSTATE_CUSTOMIZEDDATAENTRY._serialized_options = b'8\001'
  _JOBRESOURCE_TASKGROUPRESOURCESENTRY._options = None
  _JOBRESOURCE_TASKGROUPRESOURCESENTRY._serialized_options = b'8\001'
  _JOBRESOURCE_PODRESOURCESENTRY._options = None
  _JOBRESOURCE_PODRESOURCESENTRY._serialized_options = b'8\001'
  _globals['_METRICSTYPE']._serialized_start=3838
  _globals['_METRICSTYPE']._serialized_end=4072
  _globals['_TRAININGHYPERPARAMS']._serialized_start=51
  _globals['_TRAININGHYPERPARAMS']._serialized_end=126
  _globals['_WORKFLOWFEATURE']._serialized_start=129
  _globals['_WORKFLOWFEATURE']._serialized_end=280
  _globals['_TRAININGSETFEATURE']._serialized_start=283
  _globals['_TRAININGSETFEATURE']._serialized_end=537
  _globals['_MODELFEATURE']._serialized_start=540
  _globals['_MODELFEATURE']._serialized_end=947
  _globals['_MODELFEATURE_TENSORALLOCBYTESENTRY']._serialized_start=892
  _globals['_MODELFEATURE_TENSORALLOCBYTESENTRY']._serialized_end=947
  _globals['_RUNTIMEINFO']._serialized_start=949
  _globals['_RUNTIMEINFO']._serialized_end=1056
  _globals['_PODMETA']._serialized_start=1059
  _globals['_PODMETA']._serialized_end=1213
  _globals['_JOBMETA']._serialized_start=1215
  _globals['_JOBMETA']._serialized_end=1302
  _globals['_JOBMETRICS']._serialized_start=1305
  _globals['_JOBMETRICS']._serialized_end=1850
  _globals['_OPTIMIZECONFIG']._serialized_start=1853
  _globals['_OPTIMIZECONFIG']._serialized_end=2079
  _globals['_OPTIMIZECONFIG_CUSTOMIZEDCONFIGENTRY']._serialized_start=2024
  _globals['_OPTIMIZECONFIG_CUSTOMIZEDCONFIGENTRY']._serialized_end=2079
  _globals['_PODSTATE']._serialized_start=2082
  _globals['_PODSTATE']._serialized_end=2347
  _globals['_PODSTATE_CUSTOMIZEDDATAENTRY']._serialized_start=2294
  _globals['_PODSTATE_CUSTOMIZEDDATAENTRY']._serialized_end=2347
  _globals['_JOBSTATE']._serialized_start=2350
  _globals['_JOBSTATE']._serialized_end=2614
  _globals['_JOBSTATE_PODSENTRY']._serialized_start=2499
  _globals['_JOBSTATE_PODSENTRY']._serialized_end=2559
  _globals['_JOBSTATE_CUSTOMIZEDDATAENTRY']._serialized_start=2294
  _globals['_JOBSTATE_CUSTOMIZEDDATAENTRY']._serialized_end=2347
  _globals['_OPTIMIZEJOBMETA']._serialized_start=2616
  _globals['_OPTIMIZEJOBMETA']._serialized_end=2714
  _globals['_OPTIMIZEREQUEST']._serialized_start=2716
  _globals['_OPTIMIZEREQUEST']._serialized_end=2824
  _globals['_PODRESOURCE']._serialized_start=2826
  _globals['_PODRESOURCE']._serialized_end=2917
  _globals['_TASKGROUPRESOURCE']._serialized_start=2919
  _globals['_TASKGROUPRESOURCE']._serialized_end=2991
  _globals['_JOBRESOURCE']._serialized_start=2994
  _globals['_JOBRESOURCE']._serialized_end=3300
  _globals['_JOBRESOURCE_TASKGROUPRESOURCESENTRY']._serialized_start=3144
  _globals['_JOBRESOURCE_TASKGROUPRESOURCESENTRY']._serialized_end=3227
  _globals['_JOBRESOURCE_PODRESOURCESENTRY']._serialized_start=3229
  _globals['_JOBRESOURCE_PODRESOURCESENTRY']._serialized_end=3300
  _globals['_JOBOPTIMIZEPLAN']._serialized_start=3302
  _globals['_JOBOPTIMIZEPLAN']._serialized_end=3413
  _globals['_JOBOPTIMIZATION']._serialized_start=3416
  _globals['_JOBOPTIMIZATION']._serialized_end=3566
  _globals['_RESPONSE']._serialized_start=3568
  _globals['_RESPONSE']._serialized_end=3611
  _globals['_OPTIMIZERESPONSE']._serialized_start=3613
  _globals['_OPTIMIZERESPONSE']._serialized_end=3718
  _globals['_JOBMETRICSREQUEST']._serialized_start=3720
  _globals['_JOBMETRICSREQUEST']._serialized_end=3757
  _globals['_JOBMETRICSRESPONSE']._serialized_start=3759
  _globals['_JOBMETRICSRESPONSE']._serialized_end=3835
  _globals['_BRAIN']._serialized_start=4075
  _globals['_BRAIN']._serialized_end=4277
# @@protoc_insertion_point(module_scope)
