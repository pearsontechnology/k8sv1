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


class V1PersistentVolumeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, capacity=None, gcePersistentDisk=None, awsElasticBlockStore=None, hostPath=None, glusterfs=None, nfs=None, rbd=None, iscsi=None, cinder=None, cephfs=None, fc=None, flocker=None, flexVolume=None, azureFile=None, vsphereVolume=None, accessModes=None, claimRef=None, persistentVolumeReclaimPolicy=None):
        """
        V1PersistentVolumeSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'capacity': 'object',
            'gcePersistentDisk': 'V1GCEPersistentDiskVolumeSource',
            'awsElasticBlockStore': 'V1AWSElasticBlockStoreVolumeSource',
            'hostPath': 'V1HostPathVolumeSource',
            'glusterfs': 'V1GlusterfsVolumeSource',
            'nfs': 'V1NFSVolumeSource',
            'rbd': 'V1RBDVolumeSource',
            'iscsi': 'V1ISCSIVolumeSource',
            'cinder': 'V1CinderVolumeSource',
            'cephfs': 'V1CephFSVolumeSource',
            'fc': 'V1FCVolumeSource',
            'flocker': 'V1FlockerVolumeSource',
            'flexVolume': 'V1FlexVolumeSource',
            'azureFile': 'V1AzureFileVolumeSource',
            'vsphereVolume': 'V1VsphereVirtualDiskVolumeSource',
            'accessModes': 'list[V1PersistentVolumeAccessMode]',
            'claimRef': 'V1ObjectReference',
            'persistentVolumeReclaimPolicy': 'str'
        }

        self.attribute_map = {
            'capacity': 'capacity',
            'gcePersistentDisk': 'gcePersistentDisk',
            'awsElasticBlockStore': 'awsElasticBlockStore',
            'hostPath': 'hostPath',
            'glusterfs': 'glusterfs',
            'nfs': 'nfs',
            'rbd': 'rbd',
            'iscsi': 'iscsi',
            'cinder': 'cinder',
            'cephfs': 'cephfs',
            'fc': 'fc',
            'flocker': 'flocker',
            'flexVolume': 'flexVolume',
            'azureFile': 'azureFile',
            'vsphereVolume': 'vsphereVolume',
            'accessModes': 'accessModes',
            'claimRef': 'claimRef',
            'persistentVolumeReclaimPolicy': 'persistentVolumeReclaimPolicy'
        }

        self._capacity = capacity
        self._gcePersistentDisk = gcePersistentDisk
        self._awsElasticBlockStore = awsElasticBlockStore
        self._hostPath = hostPath
        self._glusterfs = glusterfs
        self._nfs = nfs
        self._rbd = rbd
        self._iscsi = iscsi
        self._cinder = cinder
        self._cephfs = cephfs
        self._fc = fc
        self._flocker = flocker
        self._flexVolume = flexVolume
        self._azureFile = azureFile
        self._vsphereVolume = vsphereVolume
        self._accessModes = accessModes
        self._claimRef = claimRef
        self._persistentVolumeReclaimPolicy = persistentVolumeReclaimPolicy

    @property
    def capacity(self):
        """
        Gets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#capacity

        :return: The capacity of this V1PersistentVolumeSpec.
        :rtype: object
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#capacity

        :param capacity: The capacity of this V1PersistentVolumeSpec.
        :type: object
        """

        self._capacity = capacity

    @property
    def gcePersistentDisk(self):
        """
        Gets the gcePersistentDisk of this V1PersistentVolumeSpec.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :return: The gcePersistentDisk of this V1PersistentVolumeSpec.
        :rtype: V1GCEPersistentDiskVolumeSource
        """
        return self._gcePersistentDisk

    @gcePersistentDisk.setter
    def gcePersistentDisk(self, gcePersistentDisk):
        """
        Sets the gcePersistentDisk of this V1PersistentVolumeSpec.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :param gcePersistentDisk: The gcePersistentDisk of this V1PersistentVolumeSpec.
        :type: V1GCEPersistentDiskVolumeSource
        """

        self._gcePersistentDisk = gcePersistentDisk

    @property
    def awsElasticBlockStore(self):
        """
        Gets the awsElasticBlockStore of this V1PersistentVolumeSpec.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#awselasticblockstore

        :return: The awsElasticBlockStore of this V1PersistentVolumeSpec.
        :rtype: V1AWSElasticBlockStoreVolumeSource
        """
        return self._awsElasticBlockStore

    @awsElasticBlockStore.setter
    def awsElasticBlockStore(self, awsElasticBlockStore):
        """
        Sets the awsElasticBlockStore of this V1PersistentVolumeSpec.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#awselasticblockstore

        :param awsElasticBlockStore: The awsElasticBlockStore of this V1PersistentVolumeSpec.
        :type: V1AWSElasticBlockStoreVolumeSource
        """

        self._awsElasticBlockStore = awsElasticBlockStore

    @property
    def hostPath(self):
        """
        Gets the hostPath of this V1PersistentVolumeSpec.
        HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#hostpath

        :return: The hostPath of this V1PersistentVolumeSpec.
        :rtype: V1HostPathVolumeSource
        """
        return self._hostPath

    @hostPath.setter
    def hostPath(self, hostPath):
        """
        Sets the hostPath of this V1PersistentVolumeSpec.
        HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#hostpath

        :param hostPath: The hostPath of this V1PersistentVolumeSpec.
        :type: V1HostPathVolumeSource
        """

        self._hostPath = hostPath

    @property
    def glusterfs(self):
        """
        Gets the glusterfs of this V1PersistentVolumeSpec.
        Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :return: The glusterfs of this V1PersistentVolumeSpec.
        :rtype: V1GlusterfsVolumeSource
        """
        return self._glusterfs

    @glusterfs.setter
    def glusterfs(self, glusterfs):
        """
        Sets the glusterfs of this V1PersistentVolumeSpec.
        Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :param glusterfs: The glusterfs of this V1PersistentVolumeSpec.
        :type: V1GlusterfsVolumeSource
        """

        self._glusterfs = glusterfs

    @property
    def nfs(self):
        """
        Gets the nfs of this V1PersistentVolumeSpec.
        NFS represents an NFS mount on the host. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#nfs

        :return: The nfs of this V1PersistentVolumeSpec.
        :rtype: V1NFSVolumeSource
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """
        Sets the nfs of this V1PersistentVolumeSpec.
        NFS represents an NFS mount on the host. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#nfs

        :param nfs: The nfs of this V1PersistentVolumeSpec.
        :type: V1NFSVolumeSource
        """

        self._nfs = nfs

    @property
    def rbd(self):
        """
        Gets the rbd of this V1PersistentVolumeSpec.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :return: The rbd of this V1PersistentVolumeSpec.
        :rtype: V1RBDVolumeSource
        """
        return self._rbd

    @rbd.setter
    def rbd(self, rbd):
        """
        Sets the rbd of this V1PersistentVolumeSpec.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :param rbd: The rbd of this V1PersistentVolumeSpec.
        :type: V1RBDVolumeSource
        """

        self._rbd = rbd

    @property
    def iscsi(self):
        """
        Gets the iscsi of this V1PersistentVolumeSpec.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.

        :return: The iscsi of this V1PersistentVolumeSpec.
        :rtype: V1ISCSIVolumeSource
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """
        Sets the iscsi of this V1PersistentVolumeSpec.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.

        :param iscsi: The iscsi of this V1PersistentVolumeSpec.
        :type: V1ISCSIVolumeSource
        """

        self._iscsi = iscsi

    @property
    def cinder(self):
        """
        Gets the cinder of this V1PersistentVolumeSpec.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :return: The cinder of this V1PersistentVolumeSpec.
        :rtype: V1CinderVolumeSource
        """
        return self._cinder

    @cinder.setter
    def cinder(self, cinder):
        """
        Sets the cinder of this V1PersistentVolumeSpec.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :param cinder: The cinder of this V1PersistentVolumeSpec.
        :type: V1CinderVolumeSource
        """

        self._cinder = cinder

    @property
    def cephfs(self):
        """
        Gets the cephfs of this V1PersistentVolumeSpec.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :return: The cephfs of this V1PersistentVolumeSpec.
        :rtype: V1CephFSVolumeSource
        """
        return self._cephfs

    @cephfs.setter
    def cephfs(self, cephfs):
        """
        Sets the cephfs of this V1PersistentVolumeSpec.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :param cephfs: The cephfs of this V1PersistentVolumeSpec.
        :type: V1CephFSVolumeSource
        """

        self._cephfs = cephfs

    @property
    def fc(self):
        """
        Gets the fc of this V1PersistentVolumeSpec.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :return: The fc of this V1PersistentVolumeSpec.
        :rtype: V1FCVolumeSource
        """
        return self._fc

    @fc.setter
    def fc(self, fc):
        """
        Sets the fc of this V1PersistentVolumeSpec.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :param fc: The fc of this V1PersistentVolumeSpec.
        :type: V1FCVolumeSource
        """

        self._fc = fc

    @property
    def flocker(self):
        """
        Gets the flocker of this V1PersistentVolumeSpec.
        Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running

        :return: The flocker of this V1PersistentVolumeSpec.
        :rtype: V1FlockerVolumeSource
        """
        return self._flocker

    @flocker.setter
    def flocker(self, flocker):
        """
        Sets the flocker of this V1PersistentVolumeSpec.
        Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running

        :param flocker: The flocker of this V1PersistentVolumeSpec.
        :type: V1FlockerVolumeSource
        """

        self._flocker = flocker

    @property
    def flexVolume(self):
        """
        Gets the flexVolume of this V1PersistentVolumeSpec.
        FlexVolume represents a generic volume resource that is provisioned/attached using a exec based plugin. This is an alpha feature and may change in future.

        :return: The flexVolume of this V1PersistentVolumeSpec.
        :rtype: V1FlexVolumeSource
        """
        return self._flexVolume

    @flexVolume.setter
    def flexVolume(self, flexVolume):
        """
        Sets the flexVolume of this V1PersistentVolumeSpec.
        FlexVolume represents a generic volume resource that is provisioned/attached using a exec based plugin. This is an alpha feature and may change in future.

        :param flexVolume: The flexVolume of this V1PersistentVolumeSpec.
        :type: V1FlexVolumeSource
        """

        self._flexVolume = flexVolume

    @property
    def azureFile(self):
        """
        Gets the azureFile of this V1PersistentVolumeSpec.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :return: The azureFile of this V1PersistentVolumeSpec.
        :rtype: V1AzureFileVolumeSource
        """
        return self._azureFile

    @azureFile.setter
    def azureFile(self, azureFile):
        """
        Sets the azureFile of this V1PersistentVolumeSpec.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :param azureFile: The azureFile of this V1PersistentVolumeSpec.
        :type: V1AzureFileVolumeSource
        """

        self._azureFile = azureFile

    @property
    def vsphereVolume(self):
        """
        Gets the vsphereVolume of this V1PersistentVolumeSpec.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :return: The vsphereVolume of this V1PersistentVolumeSpec.
        :rtype: V1VsphereVirtualDiskVolumeSource
        """
        return self._vsphereVolume

    @vsphereVolume.setter
    def vsphereVolume(self, vsphereVolume):
        """
        Sets the vsphereVolume of this V1PersistentVolumeSpec.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :param vsphereVolume: The vsphereVolume of this V1PersistentVolumeSpec.
        :type: V1VsphereVirtualDiskVolumeSource
        """

        self._vsphereVolume = vsphereVolume

    @property
    def accessModes(self):
        """
        Gets the accessModes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#access-modes

        :return: The accessModes of this V1PersistentVolumeSpec.
        :rtype: list[V1PersistentVolumeAccessMode]
        """
        return self._accessModes

    @accessModes.setter
    def accessModes(self, accessModes):
        """
        Sets the accessModes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#access-modes

        :param accessModes: The accessModes of this V1PersistentVolumeSpec.
        :type: list[V1PersistentVolumeAccessMode]
        """

        self._accessModes = accessModes

    @property
    def claimRef(self):
        """
        Gets the claimRef of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#binding

        :return: The claimRef of this V1PersistentVolumeSpec.
        :rtype: V1ObjectReference
        """
        return self._claimRef

    @claimRef.setter
    def claimRef(self, claimRef):
        """
        Sets the claimRef of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#binding

        :param claimRef: The claimRef of this V1PersistentVolumeSpec.
        :type: V1ObjectReference
        """

        self._claimRef = claimRef

    @property
    def persistentVolumeReclaimPolicy(self):
        """
        Gets the persistentVolumeReclaimPolicy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recyling must be supported by the volume plugin underlying this persistent volume. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#recycling-policy

        :return: The persistentVolumeReclaimPolicy of this V1PersistentVolumeSpec.
        :rtype: str
        """
        return self._persistentVolumeReclaimPolicy

    @persistentVolumeReclaimPolicy.setter
    def persistentVolumeReclaimPolicy(self, persistentVolumeReclaimPolicy):
        """
        Sets the persistentVolumeReclaimPolicy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recyling must be supported by the volume plugin underlying this persistent volume. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#recycling-policy

        :param persistentVolumeReclaimPolicy: The persistentVolumeReclaimPolicy of this V1PersistentVolumeSpec.
        :type: str
        """

        self._persistentVolumeReclaimPolicy = persistentVolumeReclaimPolicy

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
