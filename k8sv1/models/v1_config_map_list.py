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


class V1ConfigMapList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Kind=None, ApiVersion=None, Metadata=None, Items=None):
        """
        V1ConfigMapList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Kind': 'str',
            'ApiVersion': 'str',
            'Metadata': 'UnversionedListMeta',
            'Items': 'list[V1ConfigMap]'
        }

        self.attribute_map = {
            'Kind': 'kind',
            'ApiVersion': 'apiVersion',
            'Metadata': 'metadata',
            'Items': 'items'
        }

        self._Kind = Kind
        self._ApiVersion = ApiVersion
        self._Metadata = Metadata
        self._Items = Items

    @property
    def Kind(self):
        """
        Gets the Kind of this V1ConfigMapList.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The Kind of this V1ConfigMapList.
        :rtype: str
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        """
        Sets the Kind of this V1ConfigMapList.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param Kind: The Kind of this V1ConfigMapList.
        :type: str
        """

        self._Kind = Kind

    @property
    def ApiVersion(self):
        """
        Gets the ApiVersion of this V1ConfigMapList.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The ApiVersion of this V1ConfigMapList.
        :rtype: str
        """
        return self._ApiVersion

    @ApiVersion.setter
    def ApiVersion(self, ApiVersion):
        """
        Sets the ApiVersion of this V1ConfigMapList.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param ApiVersion: The ApiVersion of this V1ConfigMapList.
        :type: str
        """

        self._ApiVersion = ApiVersion

    @property
    def Metadata(self):
        """
        Gets the Metadata of this V1ConfigMapList.
        More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The Metadata of this V1ConfigMapList.
        :rtype: UnversionedListMeta
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        """
        Sets the Metadata of this V1ConfigMapList.
        More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param Metadata: The Metadata of this V1ConfigMapList.
        :type: UnversionedListMeta
        """

        self._Metadata = Metadata

    @property
    def Items(self):
        """
        Gets the Items of this V1ConfigMapList.
        Items is the list of ConfigMaps.

        :return: The Items of this V1ConfigMapList.
        :rtype: list[V1ConfigMap]
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        """
        Sets the Items of this V1ConfigMapList.
        Items is the list of ConfigMaps.

        :param Items: The Items of this V1ConfigMapList.
        :type: list[V1ConfigMap]
        """

        self._Items = Items

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
