# V1SecretVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SecretName** | **str** | Name of the secret in the pod&#39;s namespace to use. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#secrets | [optional] 
**Items** | [**list[V1KeyToPath]**](V1KeyToPath.md) | If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error. Paths must be relative and may not contain the &#39;..&#39; path or start with &#39;..&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


