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


class UnversionedStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UnversionedStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'apiVersion': 'str',
            'metadata': 'UnversionedListMeta',
            'status': 'str',
            'message': 'str',
            'reason': 'str',
            'details': 'UnversionedStatusDetails',
            'code': 'int'
        }

        self.attribute_map = {
            'kind': 'kind',
            'apiVersion': 'apiVersion',
            'metadata': 'metadata',
            'status': 'status',
            'message': 'message',
            'reason': 'reason',
            'details': 'details',
            'code': 'code'
        }


    @property
    def kind(self):
        """
        Gets the kind of this UnversionedStatus.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this UnversionedStatus.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this UnversionedStatus.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this UnversionedStatus.
        :type: str
        """

        self._kind = kind

    @property
    def apiVersion(self):
        """
        Gets the apiVersion of this UnversionedStatus.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The apiVersion of this UnversionedStatus.
        :rtype: str
        """
        return self._apiVersion

    @apiVersion.setter
    def apiVersion(self, apiVersion):
        """
        Sets the apiVersion of this UnversionedStatus.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param apiVersion: The apiVersion of this UnversionedStatus.
        :type: str
        """

        self._apiVersion = apiVersion

    @property
    def metadata(self):
        """
        Gets the metadata of this UnversionedStatus.
        Standard list metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The metadata of this UnversionedStatus.
        :rtype: UnversionedListMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UnversionedStatus.
        Standard list metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param metadata: The metadata of this UnversionedStatus.
        :type: UnversionedListMeta
        """

        self._metadata = metadata

    @property
    def status(self):
        """
        Gets the status of this UnversionedStatus.
        Status of the operation. One of: \"Success\" or \"Failure\". More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status

        :return: The status of this UnversionedStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UnversionedStatus.
        Status of the operation. One of: \"Success\" or \"Failure\". More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status

        :param status: The status of this UnversionedStatus.
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """
        Gets the message of this UnversionedStatus.
        A human-readable description of the status of this operation.

        :return: The message of this UnversionedStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this UnversionedStatus.
        A human-readable description of the status of this operation.

        :param message: The message of this UnversionedStatus.
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """
        Gets the reason of this UnversionedStatus.
        A machine-readable description of why this operation is in the \"Failure\" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it.

        :return: The reason of this UnversionedStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this UnversionedStatus.
        A machine-readable description of why this operation is in the \"Failure\" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it.

        :param reason: The reason of this UnversionedStatus.
        :type: str
        """

        self._reason = reason

    @property
    def details(self):
        """
        Gets the details of this UnversionedStatus.
        Extended data associated with the reason.  Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type.

        :return: The details of this UnversionedStatus.
        :rtype: UnversionedStatusDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this UnversionedStatus.
        Extended data associated with the reason.  Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type.

        :param details: The details of this UnversionedStatus.
        :type: UnversionedStatusDetails
        """

        self._details = details

    @property
    def code(self):
        """
        Gets the code of this UnversionedStatus.
        Suggested HTTP return code for this status, 0 if not set.

        :return: The code of this UnversionedStatus.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this UnversionedStatus.
        Suggested HTTP return code for this status, 0 if not set.

        :param code: The code of this UnversionedStatus.
        :type: int
        """

        self._code = code

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
