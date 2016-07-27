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


class V1SecurityContext(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Capabilities=None, Privileged=None, SeLinuxOptions=None, RunAsUser=None, RunAsNonRoot=None, ReadOnlyRootFilesystem=None):
        """
        V1SecurityContext - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Capabilities': 'V1Capabilities',
            'Privileged': 'bool',
            'SeLinuxOptions': 'V1SELinuxOptions',
            'RunAsUser': 'int',
            'RunAsNonRoot': 'bool',
            'ReadOnlyRootFilesystem': 'bool'
        }

        self.attribute_map = {
            'Capabilities': 'capabilities',
            'Privileged': 'privileged',
            'SeLinuxOptions': 'seLinuxOptions',
            'RunAsUser': 'runAsUser',
            'RunAsNonRoot': 'runAsNonRoot',
            'ReadOnlyRootFilesystem': 'readOnlyRootFilesystem'
        }

        self._Capabilities = Capabilities
        self._Privileged = Privileged
        self._SeLinuxOptions = SeLinuxOptions
        self._RunAsUser = RunAsUser
        self._RunAsNonRoot = RunAsNonRoot
        self._ReadOnlyRootFilesystem = ReadOnlyRootFilesystem

    @property
    def Capabilities(self):
        """
        Gets the Capabilities of this V1SecurityContext.
        The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.

        :return: The Capabilities of this V1SecurityContext.
        :rtype: V1Capabilities
        """
        return self._Capabilities

    @Capabilities.setter
    def Capabilities(self, Capabilities):
        """
        Sets the Capabilities of this V1SecurityContext.
        The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.

        :param Capabilities: The Capabilities of this V1SecurityContext.
        :type: V1Capabilities
        """

        self._Capabilities = Capabilities

    @property
    def Privileged(self):
        """
        Gets the Privileged of this V1SecurityContext.
        Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.

        :return: The Privileged of this V1SecurityContext.
        :rtype: bool
        """
        return self._Privileged

    @Privileged.setter
    def Privileged(self, Privileged):
        """
        Sets the Privileged of this V1SecurityContext.
        Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.

        :param Privileged: The Privileged of this V1SecurityContext.
        :type: bool
        """

        self._Privileged = Privileged

    @property
    def SeLinuxOptions(self):
        """
        Gets the SeLinuxOptions of this V1SecurityContext.
        The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :return: The SeLinuxOptions of this V1SecurityContext.
        :rtype: V1SELinuxOptions
        """
        return self._SeLinuxOptions

    @SeLinuxOptions.setter
    def SeLinuxOptions(self, SeLinuxOptions):
        """
        Sets the SeLinuxOptions of this V1SecurityContext.
        The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :param SeLinuxOptions: The SeLinuxOptions of this V1SecurityContext.
        :type: V1SELinuxOptions
        """

        self._SeLinuxOptions = SeLinuxOptions

    @property
    def RunAsUser(self):
        """
        Gets the RunAsUser of this V1SecurityContext.
        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :return: The RunAsUser of this V1SecurityContext.
        :rtype: int
        """
        return self._RunAsUser

    @RunAsUser.setter
    def RunAsUser(self, RunAsUser):
        """
        Sets the RunAsUser of this V1SecurityContext.
        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :param RunAsUser: The RunAsUser of this V1SecurityContext.
        :type: int
        """

        self._RunAsUser = RunAsUser

    @property
    def RunAsNonRoot(self):
        """
        Gets the RunAsNonRoot of this V1SecurityContext.
        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :return: The RunAsNonRoot of this V1SecurityContext.
        :rtype: bool
        """
        return self._RunAsNonRoot

    @RunAsNonRoot.setter
    def RunAsNonRoot(self, RunAsNonRoot):
        """
        Sets the RunAsNonRoot of this V1SecurityContext.
        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :param RunAsNonRoot: The RunAsNonRoot of this V1SecurityContext.
        :type: bool
        """

        self._RunAsNonRoot = RunAsNonRoot

    @property
    def ReadOnlyRootFilesystem(self):
        """
        Gets the ReadOnlyRootFilesystem of this V1SecurityContext.
        Whether this container has a read-only root filesystem. Default is false.

        :return: The ReadOnlyRootFilesystem of this V1SecurityContext.
        :rtype: bool
        """
        return self._ReadOnlyRootFilesystem

    @ReadOnlyRootFilesystem.setter
    def ReadOnlyRootFilesystem(self, ReadOnlyRootFilesystem):
        """
        Sets the ReadOnlyRootFilesystem of this V1SecurityContext.
        Whether this container has a read-only root filesystem. Default is false.

        :param ReadOnlyRootFilesystem: The ReadOnlyRootFilesystem of this V1SecurityContext.
        :type: bool
        """

        self._ReadOnlyRootFilesystem = ReadOnlyRootFilesystem

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
