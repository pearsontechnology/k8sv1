# UnversionedStatusDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **str** | The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described). | [optional] 
**Group** | **str** | The group attribute of the resource associated with the status StatusReason. | [optional] 
**Kind** | **str** | The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**Causes** | [**list[UnversionedStatusCause]**](UnversionedStatusCause.md) | The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes. | [optional] 
**RetryAfterSeconds** | **int** | If specified, the time in seconds before the operation should be retried. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


