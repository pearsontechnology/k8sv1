# V1PersistentVolumeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Capacity** | **object** | A description of the persistent volume&#39;s resources and capacity. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#capacity | [optional] 
**GcePersistentDisk** | [**V1GCEPersistentDiskVolumeSource**](V1GCEPersistentDiskVolumeSource.md) | GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk | [optional] 
**AwsElasticBlockStore** | [**V1AWSElasticBlockStoreVolumeSource**](V1AWSElasticBlockStoreVolumeSource.md) | AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#awselasticblockstore | [optional] 
**HostPath** | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) | HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#hostpath | [optional] 
**Glusterfs** | [**V1GlusterfsVolumeSource**](V1GlusterfsVolumeSource.md) | Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md | [optional] 
**Nfs** | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) | NFS represents an NFS mount on the host. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#nfs | [optional] 
**Rbd** | [**V1RBDVolumeSource**](V1RBDVolumeSource.md) | RBD represents a Rados Block Device mount on the host that shares a pod&#39;s lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md | [optional] 
**Iscsi** | [**V1ISCSIVolumeSource**](V1ISCSIVolumeSource.md) | ISCSI represents an ISCSI Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. Provisioned by an admin. | [optional] 
**Cinder** | [**V1CinderVolumeSource**](V1CinderVolumeSource.md) | Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md | [optional] 
**Cephfs** | [**V1CephFSVolumeSource**](V1CephFSVolumeSource.md) | CephFS represents a Ceph FS mount on the host that shares a pod&#39;s lifetime | [optional] 
**Fc** | [**V1FCVolumeSource**](V1FCVolumeSource.md) | FC represents a Fibre Channel resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. | [optional] 
**Flocker** | [**V1FlockerVolumeSource**](V1FlockerVolumeSource.md) | Flocker represents a Flocker volume attached to a kubelet&#39;s host machine and exposed to the pod for its usage. This depends on the Flocker control service being running | [optional] 
**FlexVolume** | [**V1FlexVolumeSource**](V1FlexVolumeSource.md) | FlexVolume represents a generic volume resource that is provisioned/attached using a exec based plugin. This is an alpha feature and may change in future. | [optional] 
**AzureFile** | [**V1AzureFileVolumeSource**](V1AzureFileVolumeSource.md) | AzureFile represents an Azure File Service mount on the host and bind mount to the pod. | [optional] 
**VsphereVolume** | [**V1VsphereVirtualDiskVolumeSource**](V1VsphereVirtualDiskVolumeSource.md) | VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine | [optional] 
**AccessModes** | [**list[V1PersistentVolumeAccessMode]**](V1PersistentVolumeAccessMode.md) | AccessModes contains all ways the volume can be mounted. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#access-modes | [optional] 
**ClaimRef** | [**V1ObjectReference**](V1ObjectReference.md) | ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#binding | [optional] 
**PersistentVolumeReclaimPolicy** | **str** | What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recyling must be supported by the volume plugin underlying this persistent volume. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#recycling-policy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


