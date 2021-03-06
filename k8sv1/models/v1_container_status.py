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
    def __init__(self, name=None, state=None, lastState=None, ready=None, restartCount=None, image=None, imageID=None, containerID=None):
        """
        V1ContainerStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'state': 'V1ContainerState',
            'lastState': 'V1ContainerState',
            'ready': 'bool',
            'restartCount': 'int',
            'image': 'str',
            'imageID': 'str',
            'containerID': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'state': 'state',
            'lastState': 'lastState',
            'ready': 'ready',
            'restartCount': 'restartCount',
            'image': 'image',
            'imageID': 'imageID',
            'containerID': 'containerID'
        }

        self._name = name
        self._state = state
        self._lastState = lastState
        self._ready = ready
        self._restartCount = restartCount
        self._image = image
        self._imageID = imageID
        self._containerID = containerID

    @property
    def name(self):
        """
        Gets the name of this V1ContainerStatus.
        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.

        :return: The name of this V1ContainerStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ContainerStatus.
        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.

        :param name: The name of this V1ContainerStatus.
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """
        Gets the state of this V1ContainerStatus.
        Details about the container's current condition.

        :return: The state of this V1ContainerStatus.
        :rtype: V1ContainerState
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this V1ContainerStatus.
        Details about the container's current condition.

        :param state: The state of this V1ContainerStatus.
        :type: V1ContainerState
        """

        self._state = state

    @property
    def lastState(self):
        """
        Gets the lastState of this V1ContainerStatus.
        Details about the container's last termination condition.

        :return: The lastState of this V1ContainerStatus.
        :rtype: V1ContainerState
        """
        return self._lastState

    @lastState.setter
    def lastState(self, lastState):
        """
        Sets the lastState of this V1ContainerStatus.
        Details about the container's last termination condition.

        :param lastState: The lastState of this V1ContainerStatus.
        :type: V1ContainerState
        """

        self._lastState = lastState

    @property
    def ready(self):
        """
        Gets the ready of this V1ContainerStatus.
        Specifies whether the container has passed its readiness probe.

        :return: The ready of this V1ContainerStatus.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """
        Sets the ready of this V1ContainerStatus.
        Specifies whether the container has passed its readiness probe.

        :param ready: The ready of this V1ContainerStatus.
        :type: bool
        """

        self._ready = ready

    @property
    def restartCount(self):
        """
        Gets the restartCount of this V1ContainerStatus.
        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.

        :return: The restartCount of this V1ContainerStatus.
        :rtype: int
        """
        return self._restartCount

    @restartCount.setter
    def restartCount(self, restartCount):
        """
        Sets the restartCount of this V1ContainerStatus.
        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.

        :param restartCount: The restartCount of this V1ContainerStatus.
        :type: int
        """

        self._restartCount = restartCount

    @property
    def image(self):
        """
        Gets the image of this V1ContainerStatus.
        The image the container is running. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md

        :return: The image of this V1ContainerStatus.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1ContainerStatus.
        The image the container is running. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md

        :param image: The image of this V1ContainerStatus.
        :type: str
        """

        self._image = image

    @property
    def imageID(self):
        """
        Gets the imageID of this V1ContainerStatus.
        ImageID of the container's image.

        :return: The imageID of this V1ContainerStatus.
        :rtype: str
        """
        return self._imageID

    @imageID.setter
    def imageID(self, imageID):
        """
        Sets the imageID of this V1ContainerStatus.
        ImageID of the container's image.

        :param imageID: The imageID of this V1ContainerStatus.
        :type: str
        """

        self._imageID = imageID

    @property
    def containerID(self):
        """
        Gets the containerID of this V1ContainerStatus.
        Container's ID in the format 'docker://<container_id>'. More info: http://releases.k8s.io/HEAD/docs/user-guide/container-environment.md#container-information

        :return: The containerID of this V1ContainerStatus.
        :rtype: str
        """
        return self._containerID

    @containerID.setter
    def containerID(self, containerID):
        """
        Sets the containerID of this V1ContainerStatus.
        Container's ID in the format 'docker://<container_id>'. More info: http://releases.k8s.io/HEAD/docs/user-guide/container-environment.md#container-information

        :param containerID: The containerID of this V1ContainerStatus.
        :type: str
        """

        self._containerID = containerID

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
