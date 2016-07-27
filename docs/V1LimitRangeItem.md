# V1LimitRangeItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **str** | Type of resource that this limit applies to. | [optional] 
**Max** | **object** | Max usage constraints on this kind by resource name. | [optional] 
**Min** | **object** | Min usage constraints on this kind by resource name. | [optional] 
**Default** | **object** | Default resource requirement limit value by resource name if resource limit is omitted. | [optional] 
**DefaultRequest** | **object** | DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. | [optional] 
**MaxLimitRequestRatio** | **object** | MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


