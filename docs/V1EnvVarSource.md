# V1EnvVarSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldRef** | [**V1ObjectFieldSelector**](V1ObjectFieldSelector.md) | Selects a field of the pod; only name and namespace are supported. | [optional] 
**resourceFieldRef** | [**V1ResourceFieldSelector**](V1ResourceFieldSelector.md) | Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported. | [optional] 
**configMapKeyRef** | [**V1ConfigMapKeySelector**](V1ConfigMapKeySelector.md) | Selects a key of a ConfigMap. | [optional] 
**secretKeyRef** | [**V1SecretKeySelector**](V1SecretKeySelector.md) | Selects a key of a secret in the pod&#39;s namespace | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


