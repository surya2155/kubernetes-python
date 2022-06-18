# kubernetes-python
python command line tool for accessing kubernetes API

This tool uses kubernetes API and access the kubernetes cluster

It has two operations:
1. list the deployments of the provided namespace in the table format of Name of the Deployment, Image version of the deployment and Data the deployment was updated.
2. Difference between the deploments of any two provided namespaces and provides the Deployment details if deployments are not existing on both namespaces or if the image vrersions are different.

# 1. List of Deployments:

  To get the list, you need to pass two arguements.

  Arguement 1. Operation name : **list** 
  
  Arguement 2. Namespace: <**name of the namespace**>
  

  example: Python-file    <operation name[i.e. **list**]>   Namespace
  
# 2. Difference of Deployments:
  
  To get the difference between deployments in the 2 namespaces, 3 arguments should be passed.

  Arguement 1. Operation name : **diff** 

  Arguement 2. Namespace1: <**name of the 1st namespace**>

  Arguement 3. Namespace2: <**name of the 2st namespace**>
  
  example: Python-file    <operation name[i.e. **diff**]>     Namespace1     Namespace2
  
  please refer the .jpgs in the repo for the exucution and output on cmd.
