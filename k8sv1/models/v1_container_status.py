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


class V1ContainerStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Name=None, State=None, LastState=None, Ready=None, RestartCount=None, Image=None, ImageID=None, ContainerID=None):
        """
        V1ContainerStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Name': 'str',
            'State': 'V1ContainerState',
            'LastState': 'V1ContainerState',
            'Ready': 'bool',
            'RestartCount': 'int',
            'Image': 'str',
            'ImageID': 'str',
            'ContainerID': 'str'
        }

        self.attribute_map = {
            'Name': 'name',
            'State': 'state',
            'LastState': 'lastState',
            'Ready': 'ready',
            'RestartCount': 'restartCount',
            'Image': 'image',
            'ImageID': 'imageID',
            'ContainerID': 'containerID'
        }

        self._Name = Name
        self._State = State
        self._LastState = LastState
        self._Ready = Ready
        self._RestartCount = RestartCount
        self._Image = Image
        self._ImageID = ImageID
        self._ContainerID = ContainerID

    @property
    def Name(self):
        """
        Gets the Name of this V1ContainerStatus.
        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.

        :return: The Name of this V1ContainerStatus.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        """
        Sets the Name of this V1ContainerStatus.
        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.

        :param Name: The Name of this V1ContainerStatus.
        :type: str
        """

        self._Name = Name

    @property
    def State(self):
        """
        Gets the State of this V1ContainerStatus.
        Details about the container's current condition.

        :return: The State of this V1ContainerStatus.
        :rtype: V1ContainerState
        """
        return self._State

    @State.setter
    def State(self, State):
        """
        Sets the State of this V1ContainerStatus.
        Details about the container's current condition.

        :param State: The State of this V1ContainerStatus.
        :type: V1ContainerState
        """

        self._State = State

    @property
    def LastState(self):
        """
        Gets the LastState of this V1ContainerStatus.
        Details about the container's last termination condition.

        :return: The LastState of this V1ContainerStatus.
        :rtype: V1ContainerState
        """
        return self._LastState

    @LastState.setter
    def LastState(self, LastState):
        """
        Sets the LastState of this V1ContainerStatus.
        Details about the container's last termination condition.

        :param LastState: The LastState of this V1ContainerStatus.
        :type: V1ContainerState
        """

        self._LastState = LastState

    @property
    def Ready(self):
        """
        Gets the Ready of this V1ContainerStatus.
        Specifies whether the container has passed its readiness probe.

        :return: The Ready of this V1ContainerStatus.
        :rtype: bool
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        """
        Sets the Ready of this V1ContainerStatus.
        Specifies whether the container has passed its readiness probe.

        :param Ready: The Ready of this V1ContainerStatus.
        :type: bool
        """

        self._Ready = Ready

    @property
    def RestartCount(self):
        """
        Gets the RestartCount of this V1ContainerStatus.
        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.

        :return: The RestartCount of this V1ContainerStatus.
        :rtype: int
        """
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        """
        Sets the RestartCount of this V1ContainerStatus.
        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.

        :param RestartCount: The RestartCount of this V1ContainerStatus.
        :type: int
        """

        self._RestartCount = RestartCount

    @property
    def Image(self):
        """
        Gets the Image of this V1ContainerStatus.
        The image the container is running. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md

        :return: The Image of this V1ContainerStatus.
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        """
        Sets the Image of this V1ContainerStatus.
        The image the container is running. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md

        :param Image: The Image of this V1ContainerStatus.
        :type: str
        """

        self._Image = Image

    @property
    def ImageID(self):
        """
        Gets the ImageID of this V1ContainerStatus.
        ImageID of the container's image.

        :return: The ImageID of this V1ContainerStatus.
        :rtype: str
        """
        return self._ImageID

    @ImageID.setter
    def ImageID(self, ImageID):
        """
        Sets the ImageID of this V1ContainerStatus.
        ImageID of the container's image.

        :param ImageID: The ImageID of this V1ContainerStatus.
        :type: str
        """

        self._ImageID = ImageID

    @property
    def ContainerID(self):
        """
        Gets the ContainerID of this V1ContainerStatus.
        Container's ID in the format 'docker://<container_id>'. More info: http://releases.k8s.io/HEAD/docs/user-guide/container-environment.md#container-information

        :return: The ContainerID of this V1ContainerStatus.
        :rtype: str
        """
        return self._ContainerID

    @ContainerID.setter
    def ContainerID(self, ContainerID):
        """
        Sets the ContainerID of this V1ContainerStatus.
        Container's ID in the format 'docker://<container_id>'. More info: http://releases.k8s.io/HEAD/docs/user-guide/container-environment.md#container-information

        :param ContainerID: The ContainerID of this V1ContainerStatus.
        :type: str
        """

        self._ContainerID = ContainerID

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
