# Copyright 2023 The DLRover Authors. All rights reserved.
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

import time
from abc import ABCMeta, abstractmethod

import torch.distributed as dist
from torch.utils.data import Dataset

from dlrover.python.elastic_agent.sharding.client import IndexShardingClient


def get_rank():
    rank = 0
    if dist.is_initialized():
        rank = dist.get_rank()
    return rank


class ElasticDataset(Dataset, metaclass=ABCMeta):
    def __init__(
        self,
        dataset_size,
        batch_size,
        epochs,
        shuffle,
        name=None,
    ):
        """Using ElasticDataset, the node can read samples without
        duplicates with other nodes in an epoch. DLRover master
        will dispatch the index of sample in a dataset to one node.

        Args:
            dataset_size: the number of samples in the dataset.
            batch_size: int, the size of batch samples to compute gradients
                in a trainer process.
            epochs: int, the number of epoch.
            shuffle: bool, whether to shuffle samples in the dataset.
            name: str, the name of dataset.
        """
        self.dataset_size = dataset_size
        if not name:
            name = "dlrover-ds-" + str(time.time())
        self._shard_client = IndexShardingClient(
            dataset_name=name,
            batch_size=batch_size,
            num_epochs=epochs,
            dataset_size=self.dataset_size,
            shuffle=shuffle,
            storage_type="text",
        )

    def __len__(self):
        return self._shard_client.get_total_sample_num()

    def __getitem__(self, _):
        index = self._shard_client.fetch_sample_index()
        return self.read_sample(index)

    def get_epoch(self):
        self._shard_client.get_current_epoch()

    def report_batch_done(self, batch_size=None):
        """After updating models using the samples, the dataset need to
        report the batch completion."""
        self._shard_client.report_batch_done(batch_size)

    def state_dict(self):
        """
        Checkpoint the shards which are not completed from the
        DLRover job master.
        """
        rank = get_rank()
        if rank != 0:
            return
        shards = self._shard_client.get_shard_checkpoint()
        return {"shards": shards}

    def load_state_dict(self, state):
        """
        Restore the uncompleted shards from a checkpoint. The shard
        client will send uncompleted shards to the DLRover job master.
        The master will assign those shards to workers to restore training.
        """
        rank = get_rank()
        if rank == 0:
            self._shard_client.restore_shard_from_checkpoint(state["shards"])
        dist.barrier()  # Wait rank-0 to report checkpoint.
        self._shard_client.set_max_shard_count()

    @abstractmethod
    def read_sample(self, index):
        """Implement to read sample data by the index."""
        pass
