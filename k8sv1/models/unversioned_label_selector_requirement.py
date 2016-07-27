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


class UnversionedLabelSelectorRequirement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Key=None, Operator=None, Values=None):
        """
        UnversionedLabelSelectorRequirement - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Key': 'str',
            'Operator': 'str',
            'Values': 'list[str]'
        }

        self.attribute_map = {
            'Key': 'key',
            'Operator': 'operator',
            'Values': 'values'
        }

        self._Key = Key
        self._Operator = Operator
        self._Values = Values

    @property
    def Key(self):
        """
        Gets the Key of this UnversionedLabelSelectorRequirement.
        key is the label key that the selector applies to.

        :return: The Key of this UnversionedLabelSelectorRequirement.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        """
        Sets the Key of this UnversionedLabelSelectorRequirement.
        key is the label key that the selector applies to.

        :param Key: The Key of this UnversionedLabelSelectorRequirement.
        :type: str
        """

        self._Key = Key

    @property
    def Operator(self):
        """
        Gets the Operator of this UnversionedLabelSelectorRequirement.
        operator represents a key's relationship to a set of values. Valid operators ard In, NotIn, Exists and DoesNotExist.

        :return: The Operator of this UnversionedLabelSelectorRequirement.
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        """
        Sets the Operator of this UnversionedLabelSelectorRequirement.
        operator represents a key's relationship to a set of values. Valid operators ard In, NotIn, Exists and DoesNotExist.

        :param Operator: The Operator of this UnversionedLabelSelectorRequirement.
        :type: str
        """

        self._Operator = Operator

    @property
    def Values(self):
        """
        Gets the Values of this UnversionedLabelSelectorRequirement.
        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :return: The Values of this UnversionedLabelSelectorRequirement.
        :rtype: list[str]
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        """
        Sets the Values of this UnversionedLabelSelectorRequirement.
        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :param Values: The Values of this UnversionedLabelSelectorRequirement.
        :type: list[str]
        """

        self._Values = Values

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
