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


class V1ContainerStateWaiting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Reason=None, Message=None):
        """
        V1ContainerStateWaiting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Reason': 'str',
            'Message': 'str'
        }

        self.attribute_map = {
            'Reason': 'reason',
            'Message': 'message'
        }

        self._Reason = Reason
        self._Message = Message

    @property
    def Reason(self):
        """
        Gets the Reason of this V1ContainerStateWaiting.
        (brief) reason the container is not yet running.

        :return: The Reason of this V1ContainerStateWaiting.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        """
        Sets the Reason of this V1ContainerStateWaiting.
        (brief) reason the container is not yet running.

        :param Reason: The Reason of this V1ContainerStateWaiting.
        :type: str
        """

        self._Reason = Reason

    @property
    def Message(self):
        """
        Gets the Message of this V1ContainerStateWaiting.
        Message regarding why the container is not yet running.

        :return: The Message of this V1ContainerStateWaiting.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        """
        Sets the Message of this V1ContainerStateWaiting.
        Message regarding why the container is not yet running.

        :param Message: The Message of this V1ContainerStateWaiting.
        :type: str
        """

        self._Message = Message

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
