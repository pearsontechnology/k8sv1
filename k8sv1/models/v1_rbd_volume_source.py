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


class V1RBDVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, monitors=None, image=None, fsType=None, pool=None, user=None, keyring=None, secretRef=None, readOnly=None):
        """
        V1RBDVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'monitors': 'list[str]',
            'image': 'str',
            'fsType': 'str',
            'pool': 'str',
            'user': 'str',
            'keyring': 'str',
            'secretRef': 'V1LocalObjectReference',
            'readOnly': 'bool'
        }

        self.attribute_map = {
            'monitors': 'monitors',
            'image': 'image',
            'fsType': 'fsType',
            'pool': 'pool',
            'user': 'user',
            'keyring': 'keyring',
            'secretRef': 'secretRef',
            'readOnly': 'readOnly'
        }

        self._monitors = monitors
        self._image = image
        self._fsType = fsType
        self._pool = pool
        self._user = user
        self._keyring = keyring
        self._secretRef = secretRef
        self._readOnly = readOnly

    @property
    def monitors(self):
        """
        Gets the monitors of this V1RBDVolumeSource.
        A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The monitors of this V1RBDVolumeSource.
        :rtype: list[str]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """
        Sets the monitors of this V1RBDVolumeSource.
        A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param monitors: The monitors of this V1RBDVolumeSource.
        :type: list[str]
        """

        self._monitors = monitors

    @property
    def image(self):
        """
        Gets the image of this V1RBDVolumeSource.
        The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The image of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1RBDVolumeSource.
        The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param image: The image of this V1RBDVolumeSource.
        :type: str
        """

        self._image = image

    @property
    def fsType(self):
        """
        Gets the fsType of this V1RBDVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#rbd

        :return: The fsType of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._fsType

    @fsType.setter
    def fsType(self, fsType):
        """
        Sets the fsType of this V1RBDVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#rbd

        :param fsType: The fsType of this V1RBDVolumeSource.
        :type: str
        """

        self._fsType = fsType

    @property
    def pool(self):
        """
        Gets the pool of this V1RBDVolumeSource.
        The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        :return: The pool of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """
        Sets the pool of this V1RBDVolumeSource.
        The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        :param pool: The pool of this V1RBDVolumeSource.
        :type: str
        """

        self._pool = pool

    @property
    def user(self):
        """
        Gets the user of this V1RBDVolumeSource.
        The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The user of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1RBDVolumeSource.
        The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param user: The user of this V1RBDVolumeSource.
        :type: str
        """

        self._user = user

    @property
    def keyring(self):
        """
        Gets the keyring of this V1RBDVolumeSource.
        Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The keyring of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._keyring

    @keyring.setter
    def keyring(self, keyring):
        """
        Sets the keyring of this V1RBDVolumeSource.
        Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param keyring: The keyring of this V1RBDVolumeSource.
        :type: str
        """

        self._keyring = keyring

    @property
    def secretRef(self):
        """
        Gets the secretRef of this V1RBDVolumeSource.
        SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The secretRef of this V1RBDVolumeSource.
        :rtype: V1LocalObjectReference
        """
        return self._secretRef

    @secretRef.setter
    def secretRef(self, secretRef):
        """
        Sets the secretRef of this V1RBDVolumeSource.
        SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param secretRef: The secretRef of this V1RBDVolumeSource.
        :type: V1LocalObjectReference
        """

        self._secretRef = secretRef

    @property
    def readOnly(self):
        """
        Gets the readOnly of this V1RBDVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The readOnly of this V1RBDVolumeSource.
        :rtype: bool
        """
        return self._readOnly

    @readOnly.setter
    def readOnly(self, readOnly):
        """
        Sets the readOnly of this V1RBDVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param readOnly: The readOnly of this V1RBDVolumeSource.
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
