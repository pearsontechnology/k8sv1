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


class V1CinderVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1CinderVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'volumeID': 'str',
            'fsType': 'str',
            'readOnly': 'bool'
        }

        self.attribute_map = {
            'volumeID': 'volumeID',
            'fsType': 'fsType',
            'readOnly': 'readOnly'
        }


    @property
    def volumeID(self):
        """
        Gets the volumeID of this V1CinderVolumeSource.
        volume id used to identify the volume in cinder More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :return: The volumeID of this V1CinderVolumeSource.
        :rtype: str
        """
        return self._volumeID

    @volumeID.setter
    def volumeID(self, volumeID):
        """
        Sets the volumeID of this V1CinderVolumeSource.
        volume id used to identify the volume in cinder More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :param volumeID: The volumeID of this V1CinderVolumeSource.
        :type: str
        """

        self._volumeID = volumeID

    @property
    def fsType(self):
        """
        Gets the fsType of this V1CinderVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :return: The fsType of this V1CinderVolumeSource.
        :rtype: str
        """
        return self._fsType

    @fsType.setter
    def fsType(self, fsType):
        """
        Sets the fsType of this V1CinderVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :param fsType: The fsType of this V1CinderVolumeSource.
        :type: str
        """

        self._fsType = fsType

    @property
    def readOnly(self):
        """
        Gets the readOnly of this V1CinderVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :return: The readOnly of this V1CinderVolumeSource.
        :rtype: bool
        """
        return self._readOnly

    @readOnly.setter
    def readOnly(self, readOnly):
        """
        Sets the readOnly of this V1CinderVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :param readOnly: The readOnly of this V1CinderVolumeSource.
        :type: bool
        """

        self._readOnly = readOnly

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
