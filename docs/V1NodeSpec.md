# V1NodeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PodCIDR** | **str** | PodCIDR represents the pod IP range assigned to the node. | [optional] 
**ExternalID** | **str** | External ID of the node assigned by some machine database (e.g. a cloud provider). Deprecated. | [optional] 
**ProviderID** | **str** | ID of the node assigned by the cloud provider in the format: &lt;ProviderName&gt;://&lt;ProviderSpecificNodeID&gt; | [optional] 
**Unschedulable** | **bool** | Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: http://releases.k8s.io/HEAD/docs/admin/node.md#manual-node-administration\&quot;&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


