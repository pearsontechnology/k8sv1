# V1AzureDiskVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskName** | **str** | The Name of the data disk in the blob storage | 
**diskURI** | **str** | The URI the data disk in the blob storage | 
**cachingMode** | [**V1AzureDataDiskCachingMode**](V1AzureDataDiskCachingMode.md) | Host Caching mode: None, Read Only, Read Write. | [optional] 
**fsType** | **str** | Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**readOnly** | **bool** | Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


