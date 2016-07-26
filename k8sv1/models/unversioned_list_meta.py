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


class UnversionedListMeta(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UnversionedListMeta - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'selfLink': 'str',
            'resourceVersion': 'str'
        }

        self.attribute_map = {
            'selfLink': 'selfLink',
            'resourceVersion': 'resourceVersion'
        }


    @property
    def selfLink(self):
        """
        Gets the selfLink of this UnversionedListMeta.
        SelfLink is a URL representing this object. Populated by the system. Read-only.

        :return: The selfLink of this UnversionedListMeta.
        :rtype: str
        """
        return self._selfLink

    @selfLink.setter
    def selfLink(self, selfLink):
        """
        Sets the selfLink of this UnversionedListMeta.
        SelfLink is a URL representing this object. Populated by the system. Read-only.

        :param selfLink: The selfLink of this UnversionedListMeta.
        :type: str
        """

        self._selfLink = selfLink

    @property
    def resourceVersion(self):
        """
        Gets the resourceVersion of this UnversionedListMeta.
        String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :return: The resourceVersion of this UnversionedListMeta.
        :rtype: str
        """
        return self._resourceVersion

    @resourceVersion.setter
    def resourceVersion(self, resourceVersion):
        """
        Sets the resourceVersion of this UnversionedListMeta.
        String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :param resourceVersion: The resourceVersion of this UnversionedListMeta.
        :type: str
        """

        self._resourceVersion = resourceVersion

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
