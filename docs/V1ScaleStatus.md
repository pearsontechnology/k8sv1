# V1ScaleStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Replicas** | **int** | actual number of observed instances of the scaled object. | 
**Selector** | **str** | label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: http://releases.k8s.io/HEAD/docs/user-guide/labels.md#label-selectors | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


