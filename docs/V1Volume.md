# V1Volume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **str** | Volume&#39;s name. Must be a DNS_LABEL and unique within the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names | 
**HostPath** | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) | HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#hostpath | [optional] 
**EmptyDir** | [**V1EmptyDirVolumeSource**](V1EmptyDirVolumeSource.md) | EmptyDir represents a temporary directory that shares a pod&#39;s lifetime. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#emptydir | [optional] 
**GcePersistentDisk** | [**V1GCEPersistentDiskVolumeSource**](V1GCEPersistentDiskVolumeSource.md) | GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk | [optional] 
**AwsElasticBlockStore** | [**V1AWSElasticBlockStoreVolumeSource**](V1AWSElasticBlockStoreVolumeSource.md) | AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#awselasticblockstore | [optional] 
**GitRepo** | [**V1GitRepoVolumeSource**](V1GitRepoVolumeSource.md) | GitRepo represents a git repository at a particular revision. | [optional] 
**Secret** | [**V1SecretVolumeSource**](V1SecretVolumeSource.md) | Secret represents a secret that should populate this volume. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#secrets | [optional] 
**Nfs** | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) | NFS represents an NFS mount on the host that shares a pod&#39;s lifetime More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#nfs | [optional] 
**Iscsi** | [**V1ISCSIVolumeSource**](V1ISCSIVolumeSource.md) | ISCSI represents an ISCSI Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/examples/volumes/iscsi/README.md | [optional] 
**Glusterfs** | [**V1GlusterfsVolumeSource**](V1GlusterfsVolumeSource.md) | Glusterfs represents a Glusterfs mount on the host that shares a pod&#39;s lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md | [optional] 
**PersistentVolumeClaim** | [**V1PersistentVolumeClaimVolumeSource**](V1PersistentVolumeClaimVolumeSource.md) | PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#persistentvolumeclaims | [optional] 
**Rbd** | [**V1RBDVolumeSource**](V1RBDVolumeSource.md) | RBD represents a Rados Block Device mount on the host that shares a pod&#39;s lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md | [optional] 
**FlexVolume** | [**V1FlexVolumeSource**](V1FlexVolumeSource.md) | FlexVolume represents a generic volume resource that is provisioned/attached using a exec based plugin. This is an alpha feature and may change in future. | [optional] 
**Cinder** | [**V1CinderVolumeSource**](V1CinderVolumeSource.md) | Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md | [optional] 
**Cephfs** | [**V1CephFSVolumeSource**](V1CephFSVolumeSource.md) | CephFS represents a Ceph FS mount on the host that shares a pod&#39;s lifetime | [optional] 
**Flocker** | [**V1FlockerVolumeSource**](V1FlockerVolumeSource.md) | Flocker represents a Flocker volume attached to a kubelet&#39;s host machine. This depends on the Flocker control service being running | [optional] 
**DownwardAPI** | [**V1DownwardAPIVolumeSource**](V1DownwardAPIVolumeSource.md) | DownwardAPI represents downward API about the pod that should populate this volume | [optional] 
**Fc** | [**V1FCVolumeSource**](V1FCVolumeSource.md) | FC represents a Fibre Channel resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. | [optional] 
**AzureFile** | [**V1AzureFileVolumeSource**](V1AzureFileVolumeSource.md) | AzureFile represents an Azure File Service mount on the host and bind mount to the pod. | [optional] 
**ConfigMap** | [**V1ConfigMapVolumeSource**](V1ConfigMapVolumeSource.md) | ConfigMap represents a configMap that should populate this volume | [optional] 
**VsphereVolume** | [**V1VsphereVirtualDiskVolumeSource**](V1VsphereVirtualDiskVolumeSource.md) | VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


