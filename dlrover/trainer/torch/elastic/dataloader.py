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

import json
import os
import logging

from torch.utils.data import DataLoader
from dlrover.trainer.constants.torch import WorkerEnv

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


class ElasticDataLoader(DataLoader):
    """
    A DataLoader class based on PyTorch's DataLoader that allows dynamic
    adjustment of batch size and optionally loads configuration settings from a
    file.

    This DataLoader inherits from PyTorch's DataLoader and extends its
    functionality by enabling the user to change the batch size during runtime.
    Additionally, it provides an option to load configuration settings from a
    JSON file to initialize the batch size.

    Args:
        constructor. config_file (str, optional): The path to a JSON
        configuration file that specifies
            the initial batch size (default: None).

    Attributes:
        current_batch_size (int): The current batch size used by the
        DataLoader. config_file (str): The path to the configuration file if
        provided.

    Methods:
        load_config(): Load the batch size configuration from the specified
        JSON file. set_batch_size(batch_size): Dynamically set the batch size.

    Usage Example:
        >>> # create a elastic dataloader with config.json
        >>> loader = ElasticDataLoader(dataset, shuffle=True,
        >>> config_file="config.json")
        >>> # Dynamically change the batch size to 64.
        >>> loader.set_batch_size(64)
        >>> for batch in loader:
        ...     # Training loop

    See Also:
        - PyTorch DataLoader:
          https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader
    """

    def __init__(self, *args, config_file=None, **kwargs):
        super(ElasticDataLoader, self).__init__(*args, **kwargs)
        self._config_version = 0
        self.config_file = config_file
        if self.config_file:
            self.config_file = os.getenv(
                WorkerEnv.PARAL_CONFIG_PATH.name,
                WorkerEnv.PARAL_CONFIG_PATH.default,
            )
            self.load_config(self.config_file)

    def load_config(self, config_file=None):
        """
        Load the batch size configuration from a JSON file specified by
        `config_file`.

        If the configuration file contains a 'batch_size' key, it will be used
        to set the initial batch size for the DataLoader.

        Note:
            This method is automatically called during DataLoader
            initialization if `config_file` is provided.
        """
        if not config_file or not os.path.exists(config_file):
            return
        with open(config_file, "r") as f:
            config = json.load(f)
            config_version = config.get("version", 0)
            if config_version > self._config_version:
                self._config_version = config_version
            else:
                return
            if "dataloader" in config:
                dl_config = config["dataloader"]
                batch_size = dl_config.get("batch_size", 0)
                if batch_size > 0:
                    self.batch_sampler.batch_size = batch_size
                    logger.info(
                        f"Update the batch size of dataloader to {batch_size}"
                    )

    def update_params(self):
        """
        Update parameters like batch size, num_workers of the dataloader
        From the parallelism config file.
        """
        self.load_config(self.config_file)
