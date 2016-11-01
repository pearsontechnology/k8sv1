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
    def __init__(self, capabilities=None, privileged=None, seLinuxOptions=None, runAsUser=None, runAsNonRoot=None, readOnlyRootFilesystem=None):
        """
        V1SecurityContext - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'capabilities': 'V1Capabilities',
            'privileged': 'bool',
            'seLinuxOptions': 'V1SELinuxOptions',
            'runAsUser': 'int',
            'runAsNonRoot': 'bool',
            'readOnlyRootFilesystem': 'bool'
        }

        self.attribute_map = {
            'capabilities': 'capabilities',
            'privileged': 'privileged',
            'seLinuxOptions': 'seLinuxOptions',
            'runAsUser': 'runAsUser',
            'runAsNonRoot': 'runAsNonRoot',
            'readOnlyRootFilesystem': 'readOnlyRootFilesystem'
        }

        self._capabilities = capabilities
        self._privileged = privileged
        self._seLinuxOptions = seLinuxOptions
        self._runAsUser = runAsUser
        self._runAsNonRoot = runAsNonRoot
        self._readOnlyRootFilesystem = readOnlyRootFilesystem

    @property
    def capabilities(self):
        """
        Gets the capabilities of this V1SecurityContext.
        The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.

        :return: The capabilities of this V1SecurityContext.
        :rtype: V1Capabilities
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """
        Sets the capabilities of this V1SecurityContext.
        The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.

        :param capabilities: The capabilities of this V1SecurityContext.
        :type: V1Capabilities
        """

        self._capabilities = capabilities

    @property
    def privileged(self):
        """
        Gets the privileged of this V1SecurityContext.
        Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.

        :return: The privileged of this V1SecurityContext.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """
        Sets the privileged of this V1SecurityContext.
        Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.

        :param privileged: The privileged of this V1SecurityContext.
        :type: bool
        """

        self._privileged = privileged

    @property
    def seLinuxOptions(self):
        """
        Gets the seLinuxOptions of this V1SecurityContext.
        The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :return: The seLinuxOptions of this V1SecurityContext.
        :rtype: V1SELinuxOptions
        """
        return self._seLinuxOptions

    @seLinuxOptions.setter
    def seLinuxOptions(self, seLinuxOptions):
        """
        Sets the seLinuxOptions of this V1SecurityContext.
        The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :param seLinuxOptions: The seLinuxOptions of this V1SecurityContext.
        :type: V1SELinuxOptions
        """

        self._seLinuxOptions = seLinuxOptions

    @property
    def runAsUser(self):
        """
        Gets the runAsUser of this V1SecurityContext.
        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :return: The runAsUser of this V1SecurityContext.
        :rtype: int
        """
        return self._runAsUser

    @runAsUser.setter
    def runAsUser(self, runAsUser):
        """
        Sets the runAsUser of this V1SecurityContext.
        The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :param runAsUser: The runAsUser of this V1SecurityContext.
        :type: int
        """

        self._runAsUser = runAsUser

    @property
    def runAsNonRoot(self):
        """
        Gets the runAsNonRoot of this V1SecurityContext.
        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :return: The runAsNonRoot of this V1SecurityContext.
        :rtype: bool
        """
        return self._runAsNonRoot

    @runAsNonRoot.setter
    def runAsNonRoot(self, runAsNonRoot):
        """
        Sets the runAsNonRoot of this V1SecurityContext.
        Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

        :param runAsNonRoot: The runAsNonRoot of this V1SecurityContext.
        :type: bool
        """

        self._runAsNonRoot = runAsNonRoot

    @property
    def readOnlyRootFilesystem(self):
        """
        Gets the readOnlyRootFilesystem of this V1SecurityContext.
        Whether this container has a read-only root filesystem. Default is false.

        :return: The readOnlyRootFilesystem of this V1SecurityContext.
        :rtype: bool
        """
        return self._readOnlyRootFilesystem

    @readOnlyRootFilesystem.setter
    def readOnlyRootFilesystem(self, readOnlyRootFilesystem):
        """
        Sets the readOnlyRootFilesystem of this V1SecurityContext.
        Whether this container has a read-only root filesystem. Default is false.

        :param readOnlyRootFilesystem: The readOnlyRootFilesystem of this V1SecurityContext.
        :type: bool
        """

        self._readOnlyRootFilesystem = readOnlyRootFilesystem

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
