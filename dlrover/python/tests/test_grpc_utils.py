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

from dlrover.python.common.comm import (
    Message,
    addr_connected,
    deserialize_message,
)


class GRPCUtilTest(unittest.TestCase):
    def test_addr_connected(self):
        connected = addr_connected("")
        self.assertFalse(connected)
        connected = addr_connected("localhost:80")
        self.assertFalse(connected)

    def test_deserialize_message(self):
        message = Message()
        message_bytes = message.serialize()
        de_message = deserialize_message(message_bytes)
        self.assertTrue(isinstance(de_message, Message))
        de_message = deserialize_message(b"")
        self.assertIsNone(de_message)


if __name__ == "__main__":
    unittest.main()
