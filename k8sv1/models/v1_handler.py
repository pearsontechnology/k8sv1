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


class V1Handler(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Exec=None, HttpGet=None, TcpSocket=None):
        """
        V1Handler - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Exec': 'V1ExecAction',
            'HttpGet': 'V1HTTPGetAction',
            'TcpSocket': 'V1TCPSocketAction'
        }

        self.attribute_map = {
            'Exec': 'exec',
            'HttpGet': 'httpGet',
            'TcpSocket': 'tcpSocket'
        }

        self._Exec = Exec
        self._HttpGet = HttpGet
        self._TcpSocket = TcpSocket

    @property
    def Exec(self):
        """
        Gets the Exec of this V1Handler.
        One and only one of the following should be specified. Exec specifies the action to take.

        :return: The Exec of this V1Handler.
        :rtype: V1ExecAction
        """
        return self._Exec

    @Exec.setter
    def Exec(self, Exec):
        """
        Sets the Exec of this V1Handler.
        One and only one of the following should be specified. Exec specifies the action to take.

        :param Exec: The Exec of this V1Handler.
        :type: V1ExecAction
        """

        self._Exec = Exec

    @property
    def HttpGet(self):
        """
        Gets the HttpGet of this V1Handler.
        HTTPGet specifies the http request to perform.

        :return: The HttpGet of this V1Handler.
        :rtype: V1HTTPGetAction
        """
        return self._HttpGet

    @HttpGet.setter
    def HttpGet(self, HttpGet):
        """
        Sets the HttpGet of this V1Handler.
        HTTPGet specifies the http request to perform.

        :param HttpGet: The HttpGet of this V1Handler.
        :type: V1HTTPGetAction
        """

        self._HttpGet = HttpGet

    @property
    def TcpSocket(self):
        """
        Gets the TcpSocket of this V1Handler.
        TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

        :return: The TcpSocket of this V1Handler.
        :rtype: V1TCPSocketAction
        """
        return self._TcpSocket

    @TcpSocket.setter
    def TcpSocket(self, TcpSocket):
        """
        Sets the TcpSocket of this V1Handler.
        TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

        :param TcpSocket: The TcpSocket of this V1Handler.
        :type: V1TCPSocketAction
        """

        self._TcpSocket = TcpSocket

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
