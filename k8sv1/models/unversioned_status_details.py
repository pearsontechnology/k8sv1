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


class UnversionedStatusDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UnversionedStatusDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'group': 'str',
            'kind': 'str',
            'causes': 'list[UnversionedStatusCause]',
            'retryAfterSeconds': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'group': 'group',
            'kind': 'kind',
            'causes': 'causes',
            'retryAfterSeconds': 'retryAfterSeconds'
        }


    @property
    def name(self):
        """
        Gets the name of this UnversionedStatusDetails.
        The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).

        :return: The name of this UnversionedStatusDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UnversionedStatusDetails.
        The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).

        :param name: The name of this UnversionedStatusDetails.
        :type: str
        """

        self._name = name

    @property
    def group(self):
        """
        Gets the group of this UnversionedStatusDetails.
        The group attribute of the resource associated with the status StatusReason.

        :return: The group of this UnversionedStatusDetails.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this UnversionedStatusDetails.
        The group attribute of the resource associated with the status StatusReason.

        :param group: The group of this UnversionedStatusDetails.
        :type: str
        """

        self._group = group

    @property
    def kind(self):
        """
        Gets the kind of this UnversionedStatusDetails.
        The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this UnversionedStatusDetails.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this UnversionedStatusDetails.
        The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this UnversionedStatusDetails.
        :type: str
        """

        self._kind = kind

    @property
    def causes(self):
        """
        Gets the causes of this UnversionedStatusDetails.
        The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.

        :return: The causes of this UnversionedStatusDetails.
        :rtype: list[UnversionedStatusCause]
        """
        return self._causes

    @causes.setter
    def causes(self, causes):
        """
        Sets the causes of this UnversionedStatusDetails.
        The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.

        :param causes: The causes of this UnversionedStatusDetails.
        :type: list[UnversionedStatusCause]
        """

        self._causes = causes

    @property
    def retryAfterSeconds(self):
        """
        Gets the retryAfterSeconds of this UnversionedStatusDetails.
        If specified, the time in seconds before the operation should be retried.

        :return: The retryAfterSeconds of this UnversionedStatusDetails.
        :rtype: int
        """
        return self._retryAfterSeconds

    @retryAfterSeconds.setter
    def retryAfterSeconds(self, retryAfterSeconds):
        """
        Sets the retryAfterSeconds of this UnversionedStatusDetails.
        If specified, the time in seconds before the operation should be retried.

        :param retryAfterSeconds: The retryAfterSeconds of this UnversionedStatusDetails.
        :type: int
        """

        self._retryAfterSeconds = retryAfterSeconds

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
