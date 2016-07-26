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


class V1ObjectReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1ObjectReference - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'namespace': 'str',
            'name': 'str',
            'uid': 'str',
            'apiVersion': 'str',
            'resourceVersion': 'str',
            'fieldPath': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'namespace': 'namespace',
            'name': 'name',
            'uid': 'uid',
            'apiVersion': 'apiVersion',
            'resourceVersion': 'resourceVersion',
            'fieldPath': 'fieldPath'
        }


    @property
    def kind(self):
        """
        Gets the kind of this V1ObjectReference.
        Kind of the referent. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ObjectReference.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ObjectReference.
        Kind of the referent. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ObjectReference.
        :type: str
        """

        self._kind = kind

    @property
    def namespace(self):
        """
        Gets the namespace of this V1ObjectReference.
        Namespace of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/namespaces.md

        :return: The namespace of this V1ObjectReference.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this V1ObjectReference.
        Namespace of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/namespaces.md

        :param namespace: The namespace of this V1ObjectReference.
        :type: str
        """

        self._namespace = namespace

    @property
    def name(self):
        """
        Gets the name of this V1ObjectReference.
        Name of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :return: The name of this V1ObjectReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ObjectReference.
        Name of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :param name: The name of this V1ObjectReference.
        :type: str
        """

        self._name = name

    @property
    def uid(self):
        """
        Gets the uid of this V1ObjectReference.
        UID of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#uids

        :return: The uid of this V1ObjectReference.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this V1ObjectReference.
        UID of the referent. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#uids

        :param uid: The uid of this V1ObjectReference.
        :type: str
        """

        self._uid = uid

    @property
    def apiVersion(self):
        """
        Gets the apiVersion of this V1ObjectReference.
        API version of the referent.

        :return: The apiVersion of this V1ObjectReference.
        :rtype: str
        """
        return self._apiVersion

    @apiVersion.setter
    def apiVersion(self, apiVersion):
        """
        Sets the apiVersion of this V1ObjectReference.
        API version of the referent.

        :param apiVersion: The apiVersion of this V1ObjectReference.
        :type: str
        """

        self._apiVersion = apiVersion

    @property
    def resourceVersion(self):
        """
        Gets the resourceVersion of this V1ObjectReference.
        Specific resourceVersion to which this reference is made, if any. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :return: The resourceVersion of this V1ObjectReference.
        :rtype: str
        """
        return self._resourceVersion

    @resourceVersion.setter
    def resourceVersion(self, resourceVersion):
        """
        Sets the resourceVersion of this V1ObjectReference.
        Specific resourceVersion to which this reference is made, if any. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :param resourceVersion: The resourceVersion of this V1ObjectReference.
        :type: str
        """

        self._resourceVersion = resourceVersion

    @property
    def fieldPath(self):
        """
        Gets the fieldPath of this V1ObjectReference.
        If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: \"spec.containers{name}\" (where \"name\" refers to the name of the container that triggered the event) or if no container name is specified \"spec.containers[2]\" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.

        :return: The fieldPath of this V1ObjectReference.
        :rtype: str
        """
        return self._fieldPath

    @fieldPath.setter
    def fieldPath(self, fieldPath):
        """
        Sets the fieldPath of this V1ObjectReference.
        If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: \"spec.containers{name}\" (where \"name\" refers to the name of the container that triggered the event) or if no container name is specified \"spec.containers[2]\" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.

        :param fieldPath: The fieldPath of this V1ObjectReference.
        :type: str
        """

        self._fieldPath = fieldPath

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
