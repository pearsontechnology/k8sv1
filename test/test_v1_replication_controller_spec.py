# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import k8sv1
from k8sv1.rest import ApiException
from k8sv1.models.v1_replication_controller_spec import V1ReplicationControllerSpec


class TestV1ReplicationControllerSpec(unittest.TestCase):
    """ V1ReplicationControllerSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ReplicationControllerSpec(self):
        """
        Test V1ReplicationControllerSpec
        """
        model = k8sv1.models.v1_replication_controller_spec.V1ReplicationControllerSpec()


if __name__ == '__main__':
    unittest.main()
