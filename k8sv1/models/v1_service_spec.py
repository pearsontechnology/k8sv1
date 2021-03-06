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


class V1ServiceSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ports=None, selector=None, clusterIP=None, type=None, externalIPs=None, deprecatedPublicIPs=None, sessionAffinity=None, loadBalancerIP=None, loadBalancerSourceRanges=None):
        """
        V1ServiceSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ports': 'list[V1ServicePort]',
            'selector': 'object',
            'clusterIP': 'str',
            'type': 'str',
            'externalIPs': 'list[str]',
            'deprecatedPublicIPs': 'list[str]',
            'sessionAffinity': 'str',
            'loadBalancerIP': 'str',
            'loadBalancerSourceRanges': 'list[str]'
        }

        self.attribute_map = {
            'ports': 'ports',
            'selector': 'selector',
            'clusterIP': 'clusterIP',
            'type': 'type',
            'externalIPs': 'externalIPs',
            'deprecatedPublicIPs': 'deprecatedPublicIPs',
            'sessionAffinity': 'sessionAffinity',
            'loadBalancerIP': 'loadBalancerIP',
            'loadBalancerSourceRanges': 'loadBalancerSourceRanges'
        }

        self._ports = ports
        self._selector = selector
        self._clusterIP = clusterIP
        self._type = type
        self._externalIPs = externalIPs
        self._deprecatedPublicIPs = deprecatedPublicIPs
        self._sessionAffinity = sessionAffinity
        self._loadBalancerIP = loadBalancerIP
        self._loadBalancerSourceRanges = loadBalancerSourceRanges

    @property
    def ports(self):
        """
        Gets the ports of this V1ServiceSpec.
        The list of ports that are exposed by this service. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :return: The ports of this V1ServiceSpec.
        :rtype: list[V1ServicePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this V1ServiceSpec.
        The list of ports that are exposed by this service. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :param ports: The ports of this V1ServiceSpec.
        :type: list[V1ServicePort]
        """

        self._ports = ports

    @property
    def selector(self):
        """
        Gets the selector of this V1ServiceSpec.
        This service will route traffic to pods having labels matching this selector. Label keys and values that must match in order to receive traffic for this service. If not specified, endpoints must be manually specified and the system will not automatically manage them. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#overview

        :return: The selector of this V1ServiceSpec.
        :rtype: object
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1ServiceSpec.
        This service will route traffic to pods having labels matching this selector. Label keys and values that must match in order to receive traffic for this service. If not specified, endpoints must be manually specified and the system will not automatically manage them. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#overview

        :param selector: The selector of this V1ServiceSpec.
        :type: object
        """

        self._selector = selector

    @property
    def clusterIP(self):
        """
        Gets the clusterIP of this V1ServiceSpec.
        ClusterIP is usually assigned by the master and is the IP address of the service. If specified, it will be allocated to the service if it is unused or else creation of the service will fail. Valid values are None, empty string (\"\"), or a valid IP address. 'None' can be specified for a headless service when proxying is not required. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :return: The clusterIP of this V1ServiceSpec.
        :rtype: str
        """
        return self._clusterIP

    @clusterIP.setter
    def clusterIP(self, clusterIP):
        """
        Sets the clusterIP of this V1ServiceSpec.
        ClusterIP is usually assigned by the master and is the IP address of the service. If specified, it will be allocated to the service if it is unused or else creation of the service will fail. Valid values are None, empty string (\"\"), or a valid IP address. 'None' can be specified for a headless service when proxying is not required. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :param clusterIP: The clusterIP of this V1ServiceSpec.
        :type: str
        """

        self._clusterIP = clusterIP

    @property
    def type(self):
        """
        Gets the type of this V1ServiceSpec.
        Type of exposed service. Must be ClusterIP, NodePort, or LoadBalancer. Defaults to ClusterIP. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#external-services

        :return: The type of this V1ServiceSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1ServiceSpec.
        Type of exposed service. Must be ClusterIP, NodePort, or LoadBalancer. Defaults to ClusterIP. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#external-services

        :param type: The type of this V1ServiceSpec.
        :type: str
        """

        self._type = type

    @property
    def externalIPs(self):
        """
        Gets the externalIPs of this V1ServiceSpec.
        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.  A previous form of this functionality exists as the deprecatedPublicIPs field.  When using this field, callers should also clear the deprecatedPublicIPs field.

        :return: The externalIPs of this V1ServiceSpec.
        :rtype: list[str]
        """
        return self._externalIPs

    @externalIPs.setter
    def externalIPs(self, externalIPs):
        """
        Sets the externalIPs of this V1ServiceSpec.
        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.  A previous form of this functionality exists as the deprecatedPublicIPs field.  When using this field, callers should also clear the deprecatedPublicIPs field.

        :param externalIPs: The externalIPs of this V1ServiceSpec.
        :type: list[str]
        """

        self._externalIPs = externalIPs

    @property
    def deprecatedPublicIPs(self):
        """
        Gets the deprecatedPublicIPs of this V1ServiceSpec.
        deprecatedPublicIPs is deprecated and replaced by the externalIPs field with almost the exact same semantics.  This field is retained in the v1 API for compatibility until at least 8/20/2016.  It will be removed from any new API revisions.  If both deprecatedPublicIPs *and* externalIPs are set, deprecatedPublicIPs is used.

        :return: The deprecatedPublicIPs of this V1ServiceSpec.
        :rtype: list[str]
        """
        return self._deprecatedPublicIPs

    @deprecatedPublicIPs.setter
    def deprecatedPublicIPs(self, deprecatedPublicIPs):
        """
        Sets the deprecatedPublicIPs of this V1ServiceSpec.
        deprecatedPublicIPs is deprecated and replaced by the externalIPs field with almost the exact same semantics.  This field is retained in the v1 API for compatibility until at least 8/20/2016.  It will be removed from any new API revisions.  If both deprecatedPublicIPs *and* externalIPs are set, deprecatedPublicIPs is used.

        :param deprecatedPublicIPs: The deprecatedPublicIPs of this V1ServiceSpec.
        :type: list[str]
        """

        self._deprecatedPublicIPs = deprecatedPublicIPs

    @property
    def sessionAffinity(self):
        """
        Gets the sessionAffinity of this V1ServiceSpec.
        Supports \"ClientIP\" and \"None\". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :return: The sessionAffinity of this V1ServiceSpec.
        :rtype: str
        """
        return self._sessionAffinity

    @sessionAffinity.setter
    def sessionAffinity(self, sessionAffinity):
        """
        Sets the sessionAffinity of this V1ServiceSpec.
        Supports \"ClientIP\" and \"None\". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: http://releases.k8s.io/HEAD/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :param sessionAffinity: The sessionAffinity of this V1ServiceSpec.
        :type: str
        """

        self._sessionAffinity = sessionAffinity

    @property
    def loadBalancerIP(self):
        """
        Gets the loadBalancerIP of this V1ServiceSpec.
        Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.

        :return: The loadBalancerIP of this V1ServiceSpec.
        :rtype: str
        """
        return self._loadBalancerIP

    @loadBalancerIP.setter
    def loadBalancerIP(self, loadBalancerIP):
        """
        Sets the loadBalancerIP of this V1ServiceSpec.
        Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.

        :param loadBalancerIP: The loadBalancerIP of this V1ServiceSpec.
        :type: str
        """

        self._loadBalancerIP = loadBalancerIP

    @property
    def loadBalancerSourceRanges(self):
        """
        Gets the loadBalancerSourceRanges of this V1ServiceSpec.
        If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature.\" More info: http://releases.k8s.io/HEAD/docs/user-guide/services-firewalls.md

        :return: The loadBalancerSourceRanges of this V1ServiceSpec.
        :rtype: list[str]
        """
        return self._loadBalancerSourceRanges

    @loadBalancerSourceRanges.setter
    def loadBalancerSourceRanges(self, loadBalancerSourceRanges):
        """
        Sets the loadBalancerSourceRanges of this V1ServiceSpec.
        If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature.\" More info: http://releases.k8s.io/HEAD/docs/user-guide/services-firewalls.md

        :param loadBalancerSourceRanges: The loadBalancerSourceRanges of this V1ServiceSpec.
        :type: list[str]
        """

        self._loadBalancerSourceRanges = loadBalancerSourceRanges

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
