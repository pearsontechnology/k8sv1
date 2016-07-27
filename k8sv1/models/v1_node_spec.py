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

from pprint import pformat
from six import iteritems
import re


class V1NodeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, PodCIDR=None, ExternalID=None, ProviderID=None, Unschedulable=None):
        """
        V1NodeSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'PodCIDR': 'str',
            'ExternalID': 'str',
            'ProviderID': 'str',
            'Unschedulable': 'bool'
        }

        self.attribute_map = {
            'PodCIDR': 'podCIDR',
            'ExternalID': 'externalID',
            'ProviderID': 'providerID',
            'Unschedulable': 'unschedulable'
        }

        self._PodCIDR = PodCIDR
        self._ExternalID = ExternalID
        self._ProviderID = ProviderID
        self._Unschedulable = Unschedulable

    @property
    def PodCIDR(self):
        """
        Gets the PodCIDR of this V1NodeSpec.
        PodCIDR represents the pod IP range assigned to the node.

        :return: The PodCIDR of this V1NodeSpec.
        :rtype: str
        """
        return self._PodCIDR

    @PodCIDR.setter
    def PodCIDR(self, PodCIDR):
        """
        Sets the PodCIDR of this V1NodeSpec.
        PodCIDR represents the pod IP range assigned to the node.

        :param PodCIDR: The PodCIDR of this V1NodeSpec.
        :type: str
        """

        self._PodCIDR = PodCIDR

    @property
    def ExternalID(self):
        """
        Gets the ExternalID of this V1NodeSpec.
        External ID of the node assigned by some machine database (e.g. a cloud provider). Deprecated.

        :return: The ExternalID of this V1NodeSpec.
        :rtype: str
        """
        return self._ExternalID

    @ExternalID.setter
    def ExternalID(self, ExternalID):
        """
        Sets the ExternalID of this V1NodeSpec.
        External ID of the node assigned by some machine database (e.g. a cloud provider). Deprecated.

        :param ExternalID: The ExternalID of this V1NodeSpec.
        :type: str
        """

        self._ExternalID = ExternalID

    @property
    def ProviderID(self):
        """
        Gets the ProviderID of this V1NodeSpec.
        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>

        :return: The ProviderID of this V1NodeSpec.
        :rtype: str
        """
        return self._ProviderID

    @ProviderID.setter
    def ProviderID(self, ProviderID):
        """
        Sets the ProviderID of this V1NodeSpec.
        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>

        :param ProviderID: The ProviderID of this V1NodeSpec.
        :type: str
        """

        self._ProviderID = ProviderID

    @property
    def Unschedulable(self):
        """
        Gets the Unschedulable of this V1NodeSpec.
        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#manual-node-administration\"`

        :return: The Unschedulable of this V1NodeSpec.
        :rtype: bool
        """
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        """
        Sets the Unschedulable of this V1NodeSpec.
        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#manual-node-administration\"`

        :param Unschedulable: The Unschedulable of this V1NodeSpec.
        :type: bool
        """

        self._Unschedulable = Unschedulable

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
