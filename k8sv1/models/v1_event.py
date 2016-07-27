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


class V1Event(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Kind=None, ApiVersion=None, Metadata=None, InvolvedObject=None, Reason=None, Message=None, Source=None, FirstTimestamp=None, LastTimestamp=None, Count=None, Type=None):
        """
        V1Event - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Kind': 'str',
            'ApiVersion': 'str',
            'Metadata': 'V1ObjectMeta',
            'InvolvedObject': 'V1ObjectReference',
            'Reason': 'str',
            'Message': 'str',
            'Source': 'V1EventSource',
            'FirstTimestamp': 'datetime',
            'LastTimestamp': 'datetime',
            'Count': 'int',
            'Type': 'str'
        }

        self.attribute_map = {
            'Kind': 'kind',
            'ApiVersion': 'apiVersion',
            'Metadata': 'metadata',
            'InvolvedObject': 'involvedObject',
            'Reason': 'reason',
            'Message': 'message',
            'Source': 'source',
            'FirstTimestamp': 'firstTimestamp',
            'LastTimestamp': 'lastTimestamp',
            'Count': 'count',
            'Type': 'type'
        }

        self._Kind = Kind
        self._ApiVersion = ApiVersion
        self._Metadata = Metadata
        self._InvolvedObject = InvolvedObject
        self._Reason = Reason
        self._Message = Message
        self._Source = Source
        self._FirstTimestamp = FirstTimestamp
        self._LastTimestamp = LastTimestamp
        self._Count = Count
        self._Type = Type

    @property
    def Kind(self):
        """
        Gets the Kind of this V1Event.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The Kind of this V1Event.
        :rtype: str
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        """
        Sets the Kind of this V1Event.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param Kind: The Kind of this V1Event.
        :type: str
        """

        self._Kind = Kind

    @property
    def ApiVersion(self):
        """
        Gets the ApiVersion of this V1Event.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The ApiVersion of this V1Event.
        :rtype: str
        """
        return self._ApiVersion

    @ApiVersion.setter
    def ApiVersion(self, ApiVersion):
        """
        Sets the ApiVersion of this V1Event.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param ApiVersion: The ApiVersion of this V1Event.
        :type: str
        """

        self._ApiVersion = ApiVersion

    @property
    def Metadata(self):
        """
        Gets the Metadata of this V1Event.
        Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The Metadata of this V1Event.
        :rtype: V1ObjectMeta
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        """
        Sets the Metadata of this V1Event.
        Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param Metadata: The Metadata of this V1Event.
        :type: V1ObjectMeta
        """

        self._Metadata = Metadata

    @property
    def InvolvedObject(self):
        """
        Gets the InvolvedObject of this V1Event.
        The object that this event is about.

        :return: The InvolvedObject of this V1Event.
        :rtype: V1ObjectReference
        """
        return self._InvolvedObject

    @InvolvedObject.setter
    def InvolvedObject(self, InvolvedObject):
        """
        Sets the InvolvedObject of this V1Event.
        The object that this event is about.

        :param InvolvedObject: The InvolvedObject of this V1Event.
        :type: V1ObjectReference
        """

        self._InvolvedObject = InvolvedObject

    @property
    def Reason(self):
        """
        Gets the Reason of this V1Event.
        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.

        :return: The Reason of this V1Event.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        """
        Sets the Reason of this V1Event.
        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.

        :param Reason: The Reason of this V1Event.
        :type: str
        """

        self._Reason = Reason

    @property
    def Message(self):
        """
        Gets the Message of this V1Event.
        A human-readable description of the status of this operation.

        :return: The Message of this V1Event.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        """
        Sets the Message of this V1Event.
        A human-readable description of the status of this operation.

        :param Message: The Message of this V1Event.
        :type: str
        """

        self._Message = Message

    @property
    def Source(self):
        """
        Gets the Source of this V1Event.
        The component reporting this event. Should be a short machine understandable string.

        :return: The Source of this V1Event.
        :rtype: V1EventSource
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        """
        Sets the Source of this V1Event.
        The component reporting this event. Should be a short machine understandable string.

        :param Source: The Source of this V1Event.
        :type: V1EventSource
        """

        self._Source = Source

    @property
    def FirstTimestamp(self):
        """
        Gets the FirstTimestamp of this V1Event.
        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)

        :return: The FirstTimestamp of this V1Event.
        :rtype: datetime
        """
        return self._FirstTimestamp

    @FirstTimestamp.setter
    def FirstTimestamp(self, FirstTimestamp):
        """
        Sets the FirstTimestamp of this V1Event.
        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)

        :param FirstTimestamp: The FirstTimestamp of this V1Event.
        :type: datetime
        """

        self._FirstTimestamp = FirstTimestamp

    @property
    def LastTimestamp(self):
        """
        Gets the LastTimestamp of this V1Event.
        The time at which the most recent occurrence of this event was recorded.

        :return: The LastTimestamp of this V1Event.
        :rtype: datetime
        """
        return self._LastTimestamp

    @LastTimestamp.setter
    def LastTimestamp(self, LastTimestamp):
        """
        Sets the LastTimestamp of this V1Event.
        The time at which the most recent occurrence of this event was recorded.

        :param LastTimestamp: The LastTimestamp of this V1Event.
        :type: datetime
        """

        self._LastTimestamp = LastTimestamp

    @property
    def Count(self):
        """
        Gets the Count of this V1Event.
        The number of times this event has occurred.

        :return: The Count of this V1Event.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        """
        Sets the Count of this V1Event.
        The number of times this event has occurred.

        :param Count: The Count of this V1Event.
        :type: int
        """

        self._Count = Count

    @property
    def Type(self):
        """
        Gets the Type of this V1Event.
        Type of this event (Normal, Warning), new types could be added in the future

        :return: The Type of this V1Event.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        """
        Sets the Type of this V1Event.
        Type of this event (Normal, Warning), new types could be added in the future

        :param Type: The Type of this V1Event.
        :type: str
        """

        self._Type = Type

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
