# coding: utf-8

"""


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


class V1PersistentVolumeClaimSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1PersistentVolumeClaimSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'accessModes': 'list[V1PersistentVolumeAccessMode]',
            'selector': 'UnversionedLabelSelector',
            'resources': 'V1ResourceRequirements',
            'volumeName': 'str'
        }

        self.attribute_map = {
            'accessModes': 'accessModes',
            'selector': 'selector',
            'resources': 'resources',
            'volumeName': 'volumeName'
        }


    @property
    def access_modes(self):
        """
        Gets the access_modes of this V1PersistentVolumeClaimSpec.
        AccessModes contains the desired access modes the volume should have. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#access-modes-1

        :return: The access_modes of this V1PersistentVolumeClaimSpec.
        :rtype: list[V1PersistentVolumeAccessMode]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """
        Sets the access_modes of this V1PersistentVolumeClaimSpec.
        AccessModes contains the desired access modes the volume should have. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#access-modes-1

        :param access_modes: The access_modes of this V1PersistentVolumeClaimSpec.
        :type: list[V1PersistentVolumeAccessMode]
        """

        self._access_modes = access_modes

    @property
    def selector(self):
        """
        Gets the selector of this V1PersistentVolumeClaimSpec.
        A label query over volumes to consider for binding.

        :return: The selector of this V1PersistentVolumeClaimSpec.
        :rtype: UnversionedLabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1PersistentVolumeClaimSpec.
        A label query over volumes to consider for binding.

        :param selector: The selector of this V1PersistentVolumeClaimSpec.
        :type: UnversionedLabelSelector
        """

        self._selector = selector

    @property
    def resources(self):
        """
        Gets the resources of this V1PersistentVolumeClaimSpec.
        Resources represents the minimum resources the volume should have. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#resources

        :return: The resources of this V1PersistentVolumeClaimSpec.
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1PersistentVolumeClaimSpec.
        Resources represents the minimum resources the volume should have. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#resources

        :param resources: The resources of this V1PersistentVolumeClaimSpec.
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def volume_name(self):
        """
        Gets the volume_name of this V1PersistentVolumeClaimSpec.
        VolumeName is the binding reference to the PersistentVolume backing this claim.

        :return: The volume_name of this V1PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """
        Sets the volume_name of this V1PersistentVolumeClaimSpec.
        VolumeName is the binding reference to the PersistentVolume backing this claim.

        :param volume_name: The volume_name of this V1PersistentVolumeClaimSpec.
        :type: str
        """

        self._volume_name = volume_name

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
