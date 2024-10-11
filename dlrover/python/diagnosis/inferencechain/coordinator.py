# Copyright 2024 The DLRover Authors. All rights reserved.
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

from typing import List

from dlrover.python.diagnosis.common.constants import (
    DiagnosisAction as DiagnosisActionConstant,
)
from dlrover.python.diagnosis.common.diagnose_action import DiagnoseAction
from dlrover.python.diagnosis.common.inference_chain import Inference


def coordinate_inferences(observations: List[Inference]) -> DiagnoseAction:
    action = DiagnoseAction()
    if len(observations) == 0:
        action.add_action(DiagnosisActionConstant.NO_ACTION)
    return action
