# V1PodList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**ApiVersion** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**Metadata** | [**UnversionedListMeta**](UnversionedListMeta.md) | Standard list metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**Items** | [**list[V1Pod]**](V1Pod.md) | List of pods. More info: http://releases.k8s.io/HEAD/docs/user-guide/pods.md | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

