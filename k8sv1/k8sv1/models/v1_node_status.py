# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class V1NodeStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1NodeStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'capacity': 'object',
            'allocatable': 'object',
            'phase': 'str',
            'conditions': 'list[V1NodeCondition]',
            'addresses': 'list[V1NodeAddress]',
            'daemon_endpoints': 'V1NodeDaemonEndpoints',
            'node_info': 'V1NodeSystemInfo',
            'images': 'list[V1ContainerImage]',
            'volumes_in_use': 'list[V1UniqueVolumeName]',
            'volumes_attached': 'list[V1AttachedVolume]'
        }

        self.attribute_map = {
            'capacity': 'capacity',
            'allocatable': 'allocatable',
            'phase': 'phase',
            'conditions': 'conditions',
            'addresses': 'addresses',
            'daemon_endpoints': 'daemonEndpoints',
            'node_info': 'nodeInfo',
            'images': 'images',
            'volumes_in_use': 'volumesInUse',
            'volumes_attached': 'volumesAttached'
        }

        self._capacity = None
        self._allocatable = None
        self._phase = None
        self._conditions = None
        self._addresses = None
        self._daemon_endpoints = None
        self._node_info = None
        self._images = None
        self._volumes_in_use = None
        self._volumes_attached = None

    @property
    def capacity(self):
        """
        Gets the capacity of this V1NodeStatus.
        Capacity represents the total resources of a node. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#capacity for more details.

        :return: The capacity of this V1NodeStatus.
        :rtype: object
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this V1NodeStatus.
        Capacity represents the total resources of a node. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#capacity for more details.

        :param capacity: The capacity of this V1NodeStatus.
        :type: object
        """
        self._capacity = capacity

    @property
    def allocatable(self):
        """
        Gets the allocatable of this V1NodeStatus.
        Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.

        :return: The allocatable of this V1NodeStatus.
        :rtype: object
        """
        return self._allocatable

    @allocatable.setter
    def allocatable(self, allocatable):
        """
        Sets the allocatable of this V1NodeStatus.
        Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.

        :param allocatable: The allocatable of this V1NodeStatus.
        :type: object
        """
        self._allocatable = allocatable

    @property
    def phase(self):
        """
        Gets the phase of this V1NodeStatus.
        NodePhase is the recently observed lifecycle phase of the node. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#node-phase

        :return: The phase of this V1NodeStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1NodeStatus.
        NodePhase is the recently observed lifecycle phase of the node. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#node-phase

        :param phase: The phase of this V1NodeStatus.
        :type: str
        """
        self._phase = phase

    @property
    def conditions(self):
        """
        Gets the conditions of this V1NodeStatus.
        Conditions is an array of current observed node conditions. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#node-condition

        :return: The conditions of this V1NodeStatus.
        :rtype: list[V1NodeCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1NodeStatus.
        Conditions is an array of current observed node conditions. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#node-condition

        :param conditions: The conditions of this V1NodeStatus.
        :type: list[V1NodeCondition]
        """
        self._conditions = conditions

    @property
    def addresses(self):
        """
        Gets the addresses of this V1NodeStatus.
        List of addresses reachable to the node. Queried from cloud provider, if available. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#node-addresses

        :return: The addresses of this V1NodeStatus.
        :rtype: list[V1NodeAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this V1NodeStatus.
        List of addresses reachable to the node. Queried from cloud provider, if available. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#node-addresses

        :param addresses: The addresses of this V1NodeStatus.
        :type: list[V1NodeAddress]
        """
        self._addresses = addresses

    @property
    def daemon_endpoints(self):
        """
        Gets the daemon_endpoints of this V1NodeStatus.
        Endpoints of daemons running on the Node.

        :return: The daemon_endpoints of this V1NodeStatus.
        :rtype: V1NodeDaemonEndpoints
        """
        return self._daemon_endpoints

    @daemon_endpoints.setter
    def daemon_endpoints(self, daemon_endpoints):
        """
        Sets the daemon_endpoints of this V1NodeStatus.
        Endpoints of daemons running on the Node.

        :param daemon_endpoints: The daemon_endpoints of this V1NodeStatus.
        :type: V1NodeDaemonEndpoints
        """
        self._daemon_endpoints = daemon_endpoints

    @property
    def node_info(self):
        """
        Gets the node_info of this V1NodeStatus.
        Set of ids/uuids to uniquely identify the node. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#node-info

        :return: The node_info of this V1NodeStatus.
        :rtype: V1NodeSystemInfo
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """
        Sets the node_info of this V1NodeStatus.
        Set of ids/uuids to uniquely identify the node. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#node-info

        :param node_info: The node_info of this V1NodeStatus.
        :type: V1NodeSystemInfo
        """
        self._node_info = node_info

    @property
    def images(self):
        """
        Gets the images of this V1NodeStatus.
        List of container images on this node

        :return: The images of this V1NodeStatus.
        :rtype: list[V1ContainerImage]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this V1NodeStatus.
        List of container images on this node

        :param images: The images of this V1NodeStatus.
        :type: list[V1ContainerImage]
        """
        self._images = images

    @property
    def volumes_in_use(self):
        """
        Gets the volumes_in_use of this V1NodeStatus.
        List of attachable volumes in use (mounted) by the node.

        :return: The volumes_in_use of this V1NodeStatus.
        :rtype: list[V1UniqueVolumeName]
        """
        return self._volumes_in_use

    @volumes_in_use.setter
    def volumes_in_use(self, volumes_in_use):
        """
        Sets the volumes_in_use of this V1NodeStatus.
        List of attachable volumes in use (mounted) by the node.

        :param volumes_in_use: The volumes_in_use of this V1NodeStatus.
        :type: list[V1UniqueVolumeName]
        """
        self._volumes_in_use = volumes_in_use

    @property
    def volumes_attached(self):
        """
        Gets the volumes_attached of this V1NodeStatus.
        List of volumes that are attached to the node.

        :return: The volumes_attached of this V1NodeStatus.
        :rtype: list[V1AttachedVolume]
        """
        return self._volumes_attached

    @volumes_attached.setter
    def volumes_attached(self, volumes_attached):
        """
        Sets the volumes_attached of this V1NodeStatus.
        List of volumes that are attached to the node.

        :param volumes_attached: The volumes_attached of this V1NodeStatus.
        :type: list[V1AttachedVolume]
        """
        self._volumes_attached = volumes_attached

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

