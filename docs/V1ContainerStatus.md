# V1ContainerStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **str** | This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated. | 
**State** | [**V1ContainerState**](V1ContainerState.md) | Details about the container&#39;s current condition. | [optional] 
**LastState** | [**V1ContainerState**](V1ContainerState.md) | Details about the container&#39;s last termination condition. | [optional] 
**Ready** | **bool** | Specifies whether the container has passed its readiness probe. | 
**RestartCount** | **int** | The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC. | 
**Image** | **str** | The image the container is running. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md | 
**ImageID** | **str** | ImageID of the container&#39;s image. | 
**ContainerID** | **str** | Container&#39;s ID in the format &#39;docker://&lt;container_id&gt;&#39;. More info: http://releases.k8s.io/HEAD/docs/user-guide/container-environment.md#container-information | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


