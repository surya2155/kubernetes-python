from kubernetes import client, config
import sys
config.load_kube_config()

operation = sys.argv[1]
namespace1 = sys.argv[2]


v1 = client.AppsV1Api()



deploy_namespace1 = v1.list_namespaced_deployment(namespace1)


if( "list" in operation.lower() ):
    
    for item in deploy_namespace1.items :
        print("%s " "| " " %s " "|" " %s" % ( item.metadata.name, item.spec.template.spec.containers[0].image, item.metadata.creation_timestamp ))


if( "diff" in operation.lower() ):
    
    namespace2 = sys.argv[3]
    
    list_deployment_name1 = []
    list_deployment_name2 = []

    list_deployment_image1 = []
    list_deployment_image2 = []
    
    deploy_namespace2 = v1.list_namespaced_deployment(namespace2)

    for item in deploy_namespace1.items :
        list_deployment_name1.append(item.metadata.name)
        list_deployment_image1.append(item.spec.template.spec.containers[0].image)

    
    for item in deploy_namespace2.items :
        list_deployment_name2.append(item.metadata.name)
        list_deployment_image2.append(item.spec.template.spec.containers[0].image)


    print("Missing deployments in first namespace:", list(sorted(set(list_deployment_name2) - set(list_deployment_name1))))    
    print("Missing deployments in second namespace:", list(sorted(set(list_deployment_name1) - set(list_deployment_name2))))


    print("deployments with diff image in both namespaces are:", list(sorted(set(list_deployment_image2) - set(list_deployment_image1))))    