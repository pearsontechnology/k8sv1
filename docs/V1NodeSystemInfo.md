# V1NodeSystemInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machineID** | **str** | MachineID reported by the node. For unique machine identification in the cluster this field is prefered. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html | 
**systemUUID** | **str** | SystemUUID reported by the node. For unique machine identification MachineID is prefered. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-US/Red_Hat_Subscription_Management/1/html/RHSM/getting-system-uuid.html | 
**bootID** | **str** | Boot ID reported by the node. | 
**kernelVersion** | **str** | Kernel Version reported by the node from &#39;uname -r&#39; (e.g. 3.16.0-0.bpo.4-amd64). | 
**osImage** | **str** | OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)). | 
**containerRuntimeVersion** | **str** | ContainerRuntime Version reported by the node through runtime remote API (e.g. docker://1.5.0). | 
**kubeletVersion** | **str** | Kubelet Version reported by the node. | 
**kubeProxyVersion** | **str** | KubeProxy Version reported by the node. | 
**operatingSystem** | **str** | The Operating System reported by the node | 
**architecture** | **str** | The Architecture reported by the node | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


