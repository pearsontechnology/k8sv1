# V1FCVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targetWWNs** | **list[str]** | Required: FC target world wide names (WWNs) | 
**lun** | **int** | Required: FC target lun number | 
**fsType** | **str** | Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**readOnly** | **bool** | Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


