# V1PodStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Phase** | **str** | Current condition of the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#pod-phase | [optional] 
**Conditions** | [**list[V1PodCondition]**](V1PodCondition.md) | Current service state of pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#pod-conditions | [optional] 
**Message** | **str** | A human readable message indicating details about why the pod is in this condition. | [optional] 
**Reason** | **str** | A brief CamelCase message indicating details about why the pod is in this state. e.g. &#39;OutOfDisk&#39; | [optional] 
**HostIP** | **str** | IP address of the host to which the pod is assigned. Empty if not yet scheduled. | [optional] 
**PodIP** | **str** | IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated. | [optional] 
**StartTime** | **datetime** | RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod. | [optional] 
**ContainerStatuses** | [**list[V1ContainerStatus]**](V1ContainerStatus.md) | The list has one entry per container in the manifest. Each entry is currently the output of &#x60;docker inspect&#x60;. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#container-statuses | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


