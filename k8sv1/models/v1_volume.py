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


class V1Volume(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, hostPath=None, emptyDir=None, gcePersistentDisk=None, awsElasticBlockStore=None, gitRepo=None, secret=None, nfs=None, iscsi=None, glusterfs=None, persistentVolumeClaim=None, rbd=None, flexVolume=None, cinder=None, cephfs=None, flocker=None, downwardAPI=None, fc=None, azureFile=None, configMap=None, vsphereVolume=None, quobyte=None, azureDisk=None):
        """
        V1Volume - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'hostPath': 'V1HostPathVolumeSource',
            'emptyDir': 'V1EmptyDirVolumeSource',
            'gcePersistentDisk': 'V1GCEPersistentDiskVolumeSource',
            'awsElasticBlockStore': 'V1AWSElasticBlockStoreVolumeSource',
            'gitRepo': 'V1GitRepoVolumeSource',
            'secret': 'V1SecretVolumeSource',
            'nfs': 'V1NFSVolumeSource',
            'iscsi': 'V1ISCSIVolumeSource',
            'glusterfs': 'V1GlusterfsVolumeSource',
            'persistentVolumeClaim': 'V1PersistentVolumeClaimVolumeSource',
            'rbd': 'V1RBDVolumeSource',
            'flexVolume': 'V1FlexVolumeSource',
            'cinder': 'V1CinderVolumeSource',
            'cephfs': 'V1CephFSVolumeSource',
            'flocker': 'V1FlockerVolumeSource',
            'downwardAPI': 'V1DownwardAPIVolumeSource',
            'fc': 'V1FCVolumeSource',
            'azureFile': 'V1AzureFileVolumeSource',
            'configMap': 'V1ConfigMapVolumeSource',
            'vsphereVolume': 'V1VsphereVirtualDiskVolumeSource',
            'quobyte': 'V1QuobyteVolumeSource',
            'azureDisk': 'V1AzureDiskVolumeSource'
        }

        self.attribute_map = {
            'name': 'name',
            'hostPath': 'hostPath',
            'emptyDir': 'emptyDir',
            'gcePersistentDisk': 'gcePersistentDisk',
            'awsElasticBlockStore': 'awsElasticBlockStore',
            'gitRepo': 'gitRepo',
            'secret': 'secret',
            'nfs': 'nfs',
            'iscsi': 'iscsi',
            'glusterfs': 'glusterfs',
            'persistentVolumeClaim': 'persistentVolumeClaim',
            'rbd': 'rbd',
            'flexVolume': 'flexVolume',
            'cinder': 'cinder',
            'cephfs': 'cephfs',
            'flocker': 'flocker',
            'downwardAPI': 'downwardAPI',
            'fc': 'fc',
            'azureFile': 'azureFile',
            'configMap': 'configMap',
            'vsphereVolume': 'vsphereVolume',
            'quobyte': 'quobyte',
            'azureDisk': 'azureDisk'
        }

        self._name = name
        self._hostPath = hostPath
        self._emptyDir = emptyDir
        self._gcePersistentDisk = gcePersistentDisk
        self._awsElasticBlockStore = awsElasticBlockStore
        self._gitRepo = gitRepo
        self._secret = secret
        self._nfs = nfs
        self._iscsi = iscsi
        self._glusterfs = glusterfs
        self._persistentVolumeClaim = persistentVolumeClaim
        self._rbd = rbd
        self._flexVolume = flexVolume
        self._cinder = cinder
        self._cephfs = cephfs
        self._flocker = flocker
        self._downwardAPI = downwardAPI
        self._fc = fc
        self._azureFile = azureFile
        self._configMap = configMap
        self._vsphereVolume = vsphereVolume
        self._quobyte = quobyte
        self._azureDisk = azureDisk

    @property
    def name(self):
        """
        Gets the name of this V1Volume.
        Volume's name. Must be a DNS_LABEL and unique within the pod. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :return: The name of this V1Volume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Volume.
        Volume's name. Must be a DNS_LABEL and unique within the pod. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :param name: The name of this V1Volume.
        :type: str
        """

        self._name = name

    @property
    def hostPath(self):
        """
        Gets the hostPath of this V1Volume.
        HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath

        :return: The hostPath of this V1Volume.
        :rtype: V1HostPathVolumeSource
        """
        return self._hostPath

    @hostPath.setter
    def hostPath(self, hostPath):
        """
        Sets the hostPath of this V1Volume.
        HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath

        :param hostPath: The hostPath of this V1Volume.
        :type: V1HostPathVolumeSource
        """

        self._hostPath = hostPath

    @property
    def emptyDir(self):
        """
        Gets the emptyDir of this V1Volume.
        EmptyDir represents a temporary directory that shares a pod's lifetime. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir

        :return: The emptyDir of this V1Volume.
        :rtype: V1EmptyDirVolumeSource
        """
        return self._emptyDir

    @emptyDir.setter
    def emptyDir(self, emptyDir):
        """
        Sets the emptyDir of this V1Volume.
        EmptyDir represents a temporary directory that shares a pod's lifetime. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir

        :param emptyDir: The emptyDir of this V1Volume.
        :type: V1EmptyDirVolumeSource
        """

        self._emptyDir = emptyDir

    @property
    def gcePersistentDisk(self):
        """
        Gets the gcePersistentDisk of this V1Volume.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :return: The gcePersistentDisk of this V1Volume.
        :rtype: V1GCEPersistentDiskVolumeSource
        """
        return self._gcePersistentDisk

    @gcePersistentDisk.setter
    def gcePersistentDisk(self, gcePersistentDisk):
        """
        Sets the gcePersistentDisk of this V1Volume.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :param gcePersistentDisk: The gcePersistentDisk of this V1Volume.
        :type: V1GCEPersistentDiskVolumeSource
        """

        self._gcePersistentDisk = gcePersistentDisk

    @property
    def awsElasticBlockStore(self):
        """
        Gets the awsElasticBlockStore of this V1Volume.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        :return: The awsElasticBlockStore of this V1Volume.
        :rtype: V1AWSElasticBlockStoreVolumeSource
        """
        return self._awsElasticBlockStore

    @awsElasticBlockStore.setter
    def awsElasticBlockStore(self, awsElasticBlockStore):
        """
        Sets the awsElasticBlockStore of this V1Volume.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        :param awsElasticBlockStore: The awsElasticBlockStore of this V1Volume.
        :type: V1AWSElasticBlockStoreVolumeSource
        """

        self._awsElasticBlockStore = awsElasticBlockStore

    @property
    def gitRepo(self):
        """
        Gets the gitRepo of this V1Volume.
        GitRepo represents a git repository at a particular revision.

        :return: The gitRepo of this V1Volume.
        :rtype: V1GitRepoVolumeSource
        """
        return self._gitRepo

    @gitRepo.setter
    def gitRepo(self, gitRepo):
        """
        Sets the gitRepo of this V1Volume.
        GitRepo represents a git repository at a particular revision.

        :param gitRepo: The gitRepo of this V1Volume.
        :type: V1GitRepoVolumeSource
        """

        self._gitRepo = gitRepo

    @property
    def secret(self):
        """
        Gets the secret of this V1Volume.
        Secret represents a secret that should populate this volume. More info: http://kubernetes.io/docs/user-guide/volumes#secrets

        :return: The secret of this V1Volume.
        :rtype: V1SecretVolumeSource
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this V1Volume.
        Secret represents a secret that should populate this volume. More info: http://kubernetes.io/docs/user-guide/volumes#secrets

        :param secret: The secret of this V1Volume.
        :type: V1SecretVolumeSource
        """

        self._secret = secret

    @property
    def nfs(self):
        """
        Gets the nfs of this V1Volume.
        NFS represents an NFS mount on the host that shares a pod's lifetime More info: http://kubernetes.io/docs/user-guide/volumes#nfs

        :return: The nfs of this V1Volume.
        :rtype: V1NFSVolumeSource
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """
        Sets the nfs of this V1Volume.
        NFS represents an NFS mount on the host that shares a pod's lifetime More info: http://kubernetes.io/docs/user-guide/volumes#nfs

        :param nfs: The nfs of this V1Volume.
        :type: V1NFSVolumeSource
        """

        self._nfs = nfs

    @property
    def iscsi(self):
        """
        Gets the iscsi of this V1Volume.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/examples/volumes/iscsi/README.md

        :return: The iscsi of this V1Volume.
        :rtype: V1ISCSIVolumeSource
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """
        Sets the iscsi of this V1Volume.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/examples/volumes/iscsi/README.md

        :param iscsi: The iscsi of this V1Volume.
        :type: V1ISCSIVolumeSource
        """

        self._iscsi = iscsi

    @property
    def glusterfs(self):
        """
        Gets the glusterfs of this V1Volume.
        Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :return: The glusterfs of this V1Volume.
        :rtype: V1GlusterfsVolumeSource
        """
        return self._glusterfs

    @glusterfs.setter
    def glusterfs(self, glusterfs):
        """
        Sets the glusterfs of this V1Volume.
        Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :param glusterfs: The glusterfs of this V1Volume.
        :type: V1GlusterfsVolumeSource
        """

        self._glusterfs = glusterfs

    @property
    def persistentVolumeClaim(self):
        """
        Gets the persistentVolumeClaim of this V1Volume.
        PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#persistentvolumeclaims

        :return: The persistentVolumeClaim of this V1Volume.
        :rtype: V1PersistentVolumeClaimVolumeSource
        """
        return self._persistentVolumeClaim

    @persistentVolumeClaim.setter
    def persistentVolumeClaim(self, persistentVolumeClaim):
        """
        Sets the persistentVolumeClaim of this V1Volume.
        PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#persistentvolumeclaims

        :param persistentVolumeClaim: The persistentVolumeClaim of this V1Volume.
        :type: V1PersistentVolumeClaimVolumeSource
        """

        self._persistentVolumeClaim = persistentVolumeClaim

    @property
    def rbd(self):
        """
        Gets the rbd of this V1Volume.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :return: The rbd of this V1Volume.
        :rtype: V1RBDVolumeSource
        """
        return self._rbd

    @rbd.setter
    def rbd(self, rbd):
        """
        Sets the rbd of this V1Volume.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :param rbd: The rbd of this V1Volume.
        :type: V1RBDVolumeSource
        """

        self._rbd = rbd

    @property
    def flexVolume(self):
        """
        Gets the flexVolume of this V1Volume.
        FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. This is an alpha feature and may change in future.

        :return: The flexVolume of this V1Volume.
        :rtype: V1FlexVolumeSource
        """
        return self._flexVolume

    @flexVolume.setter
    def flexVolume(self, flexVolume):
        """
        Sets the flexVolume of this V1Volume.
        FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. This is an alpha feature and may change in future.

        :param flexVolume: The flexVolume of this V1Volume.
        :type: V1FlexVolumeSource
        """

        self._flexVolume = flexVolume

    @property
    def cinder(self):
        """
        Gets the cinder of this V1Volume.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :return: The cinder of this V1Volume.
        :rtype: V1CinderVolumeSource
        """
        return self._cinder

    @cinder.setter
    def cinder(self, cinder):
        """
        Sets the cinder of this V1Volume.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :param cinder: The cinder of this V1Volume.
        :type: V1CinderVolumeSource
        """

        self._cinder = cinder

    @property
    def cephfs(self):
        """
        Gets the cephfs of this V1Volume.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :return: The cephfs of this V1Volume.
        :rtype: V1CephFSVolumeSource
        """
        return self._cephfs

    @cephfs.setter
    def cephfs(self, cephfs):
        """
        Sets the cephfs of this V1Volume.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :param cephfs: The cephfs of this V1Volume.
        :type: V1CephFSVolumeSource
        """

        self._cephfs = cephfs

    @property
    def flocker(self):
        """
        Gets the flocker of this V1Volume.
        Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running

        :return: The flocker of this V1Volume.
        :rtype: V1FlockerVolumeSource
        """
        return self._flocker

    @flocker.setter
    def flocker(self, flocker):
        """
        Sets the flocker of this V1Volume.
        Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running

        :param flocker: The flocker of this V1Volume.
        :type: V1FlockerVolumeSource
        """

        self._flocker = flocker

    @property
    def downwardAPI(self):
        """
        Gets the downwardAPI of this V1Volume.
        DownwardAPI represents downward API about the pod that should populate this volume

        :return: The downwardAPI of this V1Volume.
        :rtype: V1DownwardAPIVolumeSource
        """
        return self._downwardAPI

    @downwardAPI.setter
    def downwardAPI(self, downwardAPI):
        """
        Sets the downwardAPI of this V1Volume.
        DownwardAPI represents downward API about the pod that should populate this volume

        :param downwardAPI: The downwardAPI of this V1Volume.
        :type: V1DownwardAPIVolumeSource
        """

        self._downwardAPI = downwardAPI

    @property
    def fc(self):
        """
        Gets the fc of this V1Volume.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :return: The fc of this V1Volume.
        :rtype: V1FCVolumeSource
        """
        return self._fc

    @fc.setter
    def fc(self, fc):
        """
        Sets the fc of this V1Volume.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :param fc: The fc of this V1Volume.
        :type: V1FCVolumeSource
        """

        self._fc = fc

    @property
    def azureFile(self):
        """
        Gets the azureFile of this V1Volume.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :return: The azureFile of this V1Volume.
        :rtype: V1AzureFileVolumeSource
        """
        return self._azureFile

    @azureFile.setter
    def azureFile(self, azureFile):
        """
        Sets the azureFile of this V1Volume.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :param azureFile: The azureFile of this V1Volume.
        :type: V1AzureFileVolumeSource
        """

        self._azureFile = azureFile

    @property
    def configMap(self):
        """
        Gets the configMap of this V1Volume.
        ConfigMap represents a configMap that should populate this volume

        :return: The configMap of this V1Volume.
        :rtype: V1ConfigMapVolumeSource
        """
        return self._configMap

    @configMap.setter
    def configMap(self, configMap):
        """
        Sets the configMap of this V1Volume.
        ConfigMap represents a configMap that should populate this volume

        :param configMap: The configMap of this V1Volume.
        :type: V1ConfigMapVolumeSource
        """

        self._configMap = configMap

    @property
    def vsphereVolume(self):
        """
        Gets the vsphereVolume of this V1Volume.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :return: The vsphereVolume of this V1Volume.
        :rtype: V1VsphereVirtualDiskVolumeSource
        """
        return self._vsphereVolume

    @vsphereVolume.setter
    def vsphereVolume(self, vsphereVolume):
        """
        Sets the vsphereVolume of this V1Volume.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :param vsphereVolume: The vsphereVolume of this V1Volume.
        :type: V1VsphereVirtualDiskVolumeSource
        """

        self._vsphereVolume = vsphereVolume

    @property
    def quobyte(self):
        """
        Gets the quobyte of this V1Volume.
        Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

        :return: The quobyte of this V1Volume.
        :rtype: V1QuobyteVolumeSource
        """
        return self._quobyte

    @quobyte.setter
    def quobyte(self, quobyte):
        """
        Sets the quobyte of this V1Volume.
        Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

        :param quobyte: The quobyte of this V1Volume.
        :type: V1QuobyteVolumeSource
        """

        self._quobyte = quobyte

    @property
    def azureDisk(self):
        """
        Gets the azureDisk of this V1Volume.
        AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

        :return: The azureDisk of this V1Volume.
        :rtype: V1AzureDiskVolumeSource
        """
        return self._azureDisk

    @azureDisk.setter
    def azureDisk(self, azureDisk):
        """
        Sets the azureDisk of this V1Volume.
        AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

        :param azureDisk: The azureDisk of this V1Volume.
        :type: V1AzureDiskVolumeSource
        """

        self._azureDisk = azureDisk

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
