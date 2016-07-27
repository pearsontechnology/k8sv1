# V1PodCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **str** | Type is the type of the condition. Currently only Ready. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#pod-conditions | 
**Status** | **str** | Status is the status of the condition. Can be True, False, Unknown. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#pod-conditions | 
**LastProbeTime** | **datetime** | Last time we probed the condition. | [optional] 
**LastTransitionTime** | **datetime** | Last time the condition transitioned from one status to another. | [optional] 
**Reason** | **str** | Unique, one-word, CamelCase reason for the condition&#39;s last transition. | [optional] 
**Message** | **str** | Human-readable message indicating details about last transition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


