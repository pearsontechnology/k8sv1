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


class V1OwnerReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, apiVersion=None, kind=None, name=None, uid=None, controller=None):
        """
        V1OwnerReference - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'apiVersion': 'str',
            'kind': 'str',
            'name': 'str',
            'uid': 'str',
            'controller': 'bool'
        }

        self.attribute_map = {
            'apiVersion': 'apiVersion',
            'kind': 'kind',
            'name': 'name',
            'uid': 'uid',
            'controller': 'controller'
        }

        self._apiVersion = apiVersion
        self._kind = kind
        self._name = name
        self._uid = uid
        self._controller = controller

    @property
    def apiVersion(self):
        """
        Gets the apiVersion of this V1OwnerReference.
        API version of the referent.

        :return: The apiVersion of this V1OwnerReference.
        :rtype: str
        """
        return self._apiVersion

    @apiVersion.setter
    def apiVersion(self, apiVersion):
        """
        Sets the apiVersion of this V1OwnerReference.
        API version of the referent.

        :param apiVersion: The apiVersion of this V1OwnerReference.
        :type: str
        """

        self._apiVersion = apiVersion

    @property
    def kind(self):
        """
        Gets the kind of this V1OwnerReference.
        Kind of the referent. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1OwnerReference.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1OwnerReference.
        Kind of the referent. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1OwnerReference.
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1OwnerReference.
        Name of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :return: The name of this V1OwnerReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1OwnerReference.
        Name of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :param name: The name of this V1OwnerReference.
        :type: str
        """

        self._name = name

    @property
    def uid(self):
        """
        Gets the uid of this V1OwnerReference.
        UID of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#uids

        :return: The uid of this V1OwnerReference.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this V1OwnerReference.
        UID of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#uids

        :param uid: The uid of this V1OwnerReference.
        :type: str
        """

        self._uid = uid

    @property
    def controller(self):
        """
        Gets the controller of this V1OwnerReference.
        If true, this reference points to the managing controller.

        :return: The controller of this V1OwnerReference.
        :rtype: bool
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """
        Sets the controller of this V1OwnerReference.
        If true, this reference points to the managing controller.

        :param controller: The controller of this V1OwnerReference.
        :type: bool
        """

        self._controller = controller

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
