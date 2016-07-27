# V1GCEPersistentDiskVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PdName** | **str** | Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk | 
**FsType** | **str** | Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk | [optional] 
**Partition** | **int** | The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \&quot;1\&quot;. Similarly, the volume partition for /dev/sda is \&quot;0\&quot; (or you can leave the property empty). More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk | [optional] 
**ReadOnly** | **bool** | ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

