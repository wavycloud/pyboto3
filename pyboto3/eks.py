'''

The MIT License (MIT)

Copyright (c) 2016 WavyCloud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_cluster(name=None, version=None, roleArn=None, resourcesVpcConfig=None, logging=None, clientRequestToken=None, tags=None, encryptionConfig=None):
    """
    Creates an Amazon EKS control plane.
    The Amazon EKS control plane consists of control plane instances that run the Kubernetes software, such as etcd and the API server. The control plane runs in an account managed by AWS, and the Kubernetes API is exposed via the Amazon EKS API server endpoint. Each Amazon EKS cluster control plane is single-tenant and unique and runs on its own set of Amazon EC2 instances.
    The cluster control plane is provisioned across multiple Availability Zones and fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces in your VPC subnets to provide connectivity from the control plane instances to the worker nodes (for example, to support kubectl exec , logs , and proxy data flows).
    Amazon EKS worker nodes run in your AWS account and connect to your cluster\'s control plane via the Kubernetes API server endpoint and a certificate file that is created for your cluster.
    You can use the endpointPublicAccess and endpointPrivateAccess parameters to enable or disable public and private access to your cluster\'s Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .
    You can use the logging parameter to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren\'t exported to CloudWatch Logs. For more information, see Amazon EKS Cluster Control Plane Logs in the * Amazon EKS User Guide * .
    Cluster creation typically takes between 10 and 15 minutes. After you create an Amazon EKS cluster, you must configure your Kubernetes tooling to communicate with the API server and launch worker nodes into your cluster. For more information, see Managing Cluster Authentication and Launching Amazon EKS Worker Nodes in the Amazon EKS User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates an Amazon EKS cluster called prod.
    Expected Output:
    
    :example: response = client.create_cluster(
        name='string',
        version='string',
        roleArn='string',
        resourcesVpcConfig={
            'subnetIds': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ],
            'endpointPublicAccess': True|False,
            'endpointPrivateAccess': True|False,
            'publicAccessCidrs': [
                'string',
            ]
        },
        logging={
            'clusterLogging': [
                {
                    'types': [
                        'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                    ],
                    'enabled': True|False
                },
            ]
        },
        clientRequestToken='string',
        tags={
            'string': 'string'
        },
        encryptionConfig=[
            {
                'resources': [
                    'string',
                ],
                'provider': {
                    'keyArn': 'string'
                }
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe unique name to give to your cluster.\n

    :type version: string
    :param version: The desired Kubernetes version for your cluster. If you don\'t specify a value here, the latest version available in Amazon EKS is used.

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM role that provides permissions for Amazon EKS to make calls to other AWS API operations on your behalf. For more information, see Amazon EKS Service IAM Role in the * Amazon EKS User Guide * .\n

    :type resourcesVpcConfig: dict
    :param resourcesVpcConfig: [REQUIRED]\nThe VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see Cluster VPC Considerations and Cluster Security Group Considerations in the Amazon EKS User Guide . You must specify at least two subnets. You can specify up to five security groups, but we recommend that you use a dedicated security group for your cluster control plane.\n\nsubnetIds (list) --Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.\n\n(string) --\n\n\nsecurityGroupIds (list) --Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane. If you don\'t specify a security group, the default security group for your VPC is used.\n\n(string) --\n\n\nendpointPublicAccess (boolean) --Set this value to false to disable public access to your cluster\'s Kubernetes API server endpoint. If you disable public access, your cluster\'s Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is true , which enables public access for your Kubernetes API server. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .\n\nendpointPrivateAccess (boolean) --Set this value to true to enable private access for your cluster\'s Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster\'s VPC use the private VPC endpoint. The default value for this parameter is false , which disables private access for your Kubernetes API server. If you disable private access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that publicAccessCidrs includes the necessary CIDR blocks for communication with the worker nodes or Fargate pods. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .\n\npublicAccessCidrs (list) --The CIDR blocks that are allowed access to your cluster\'s public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is 0.0.0.0/0 . If you\'ve disabled private endpoint access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that you specify the necessary CIDR blocks. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .\n\n(string) --\n\n\n\n

    :type logging: dict
    :param logging: Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren\'t exported to CloudWatch Logs. For more information, see Amazon EKS Cluster Control Plane Logs in the * Amazon EKS User Guide * .\n\nNote\nCloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see Amazon CloudWatch Pricing .\n\n\nclusterLogging (list) --The cluster control plane logging configuration for your cluster.\n\n(dict) --An object representing the enabled or disabled Kubernetes control plane logs for your cluster.\n\ntypes (list) --The available cluster control plane log types.\n\n(string) --\n\n\nenabled (boolean) --If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs. If a log type isn\'t enabled, that log type doesn\'t export its control plane logs. Each individual log type can be enabled or disabled independently.\n\n\n\n\n\n\n

    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type tags: dict
    :param tags: The metadata to apply to the cluster to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define.\n\n(string) --\n(string) --\n\n\n\n

    :type encryptionConfig: list
    :param encryptionConfig: The encryption configuration for the cluster.\n\n(dict) --The encryption configuration for the cluster.\n\nresources (list) --Specifies the resources to be encrypted. The only supported value is 'secrets'.\n\n(string) --\n\n\nprovider (dict) --AWS Key Management Service (AWS KMS) customer master key (CMK). Either the ARN or the alias can be used.\n\nkeyArn (string) --Amazon Resource Name (ARN) or alias of the customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK. For more information, see Allowing Users in Other Accounts to Use a CMK in the AWS Key Management Service Developer Guide .\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'cluster': {
        'name': 'string',
        'arn': 'string',
        'createdAt': datetime(2015, 1, 1),
        'version': 'string',
        'endpoint': 'string',
        'roleArn': 'string',
        'resourcesVpcConfig': {
            'subnetIds': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ],
            'clusterSecurityGroupId': 'string',
            'vpcId': 'string',
            'endpointPublicAccess': True|False,
            'endpointPrivateAccess': True|False,
            'publicAccessCidrs': [
                'string',
            ]
        },
        'logging': {
            'clusterLogging': [
                {
                    'types': [
                        'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                    ],
                    'enabled': True|False
                },
            ]
        },
        'identity': {
            'oidc': {
                'issuer': 'string'
            }
        },
        'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING',
        'certificateAuthority': {
            'data': 'string'
        },
        'clientRequestToken': 'string',
        'platformVersion': 'string',
        'tags': {
            'string': 'string'
        },
        'encryptionConfig': [
            {
                'resources': [
                    'string',
                ],
                'provider': {
                    'keyArn': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --

cluster (dict) --
The full description of your new cluster.

name (string) --
The name of the cluster.

arn (string) --
The Amazon Resource Name (ARN) of the cluster.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the cluster was created.

version (string) --
The Kubernetes server version for the cluster.

endpoint (string) --
The endpoint for your Kubernetes API server.

roleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.

resourcesVpcConfig (dict) --
The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see Cluster VPC Considerations and Cluster Security Group Considerations in the Amazon EKS User Guide .

subnetIds (list) --
The subnets associated with your cluster.

(string) --


securityGroupIds (list) --
The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your worker nodes and the Kubernetes control plane.

(string) --


clusterSecurityGroupId (string) --
The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control-plane-to-data-plane communication.

vpcId (string) --
The VPC associated with your cluster.

endpointPublicAccess (boolean) --
This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If the Amazon EKS public API server endpoint is disabled, your cluster\'s Kubernetes API server can only receive requests that originate from within the cluster VPC.

endpointPrivateAccess (boolean) --
This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your cluster\'s VPC use the private VPC endpoint instead of traversing the internet. If this value is disabled and you have worker nodes or AWS Fargate pods in the cluster, then ensure that publicAccessCidrs includes the necessary CIDR blocks for communication with the worker nodes or Fargate pods. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .

publicAccessCidrs (list) --
The CIDR blocks that are allowed access to your cluster\'s public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the listed CIDR blocks is denied. The default value is 0.0.0.0/0 . If you\'ve disabled private endpoint access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that the necessary CIDR blocks are listed. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .

(string) --




logging (dict) --
The logging configuration for your cluster.

clusterLogging (list) --
The cluster control plane logging configuration for your cluster.

(dict) --
An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

types (list) --
The available cluster control plane log types.

(string) --


enabled (boolean) --
If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs. If a log type isn\'t enabled, that log type doesn\'t export its control plane logs. Each individual log type can be enabled or disabled independently.







identity (dict) --
The identity provider information for the cluster.

oidc (dict) --
The OpenID Connect identity provider information for the cluster.

issuer (string) --
The issuer URL for the OpenID Connect identity provider.





status (string) --
The current status of the cluster.

certificateAuthority (dict) --
The certificate-authority-data for your cluster.

data (string) --
The Base64-encoded certificate data required to communicate with your cluster. Add this to the certificate-authority-data section of the kubeconfig file for your cluster.



clientRequestToken (string) --
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

platformVersion (string) --
The platform version of your Amazon EKS cluster. For more information, see Platform Versions in the * Amazon EKS User Guide * .

tags (dict) --
The metadata that you apply to the cluster to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Cluster tags do not propagate to any other resources associated with the cluster.

(string) --
(string) --




encryptionConfig (list) --
The encryption configuration for the cluster.

(dict) --
The encryption configuration for the cluster.

resources (list) --
Specifies the resources to be encrypted. The only supported value is "secrets".

(string) --


provider (dict) --
AWS Key Management Service (AWS KMS) customer master key (CMK). Either the ARN or the alias can be used.

keyArn (string) --
Amazon Resource Name (ARN) or alias of the customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK. For more information, see Allowing Users in Other Accounts to Use a CMK in the AWS Key Management Service Developer Guide .















Exceptions

EKS.Client.exceptions.ResourceInUseException
EKS.Client.exceptions.ResourceLimitExceededException
EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ServiceUnavailableException
EKS.Client.exceptions.UnsupportedAvailabilityZoneException

Examples
The following example creates an Amazon EKS cluster called prod.
response = client.create_cluster(
    version='1.10',
    name='prod',
    clientRequestToken='1d2129a1-3d38-460a-9756-e5b91fddb951',
    resourcesVpcConfig={
        'securityGroupIds': [
            'sg-6979fe18',
        ],
        'subnetIds': [
            'subnet-6782e71e',
            'subnet-e7e761ac',
        ],
    },
    roleArn='arn:aws:iam::012345678910:role/eks-service-role-AWSServiceRoleForAmazonEKS-J7ONKE3BQ4PI',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'cluster': {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'version': 'string',
            'endpoint': 'string',
            'roleArn': 'string',
            'resourcesVpcConfig': {
                'subnetIds': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ],
                'clusterSecurityGroupId': 'string',
                'vpcId': 'string',
                'endpointPublicAccess': True|False,
                'endpointPrivateAccess': True|False,
                'publicAccessCidrs': [
                    'string',
                ]
            },
            'logging': {
                'clusterLogging': [
                    {
                        'types': [
                            'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                        ],
                        'enabled': True|False
                    },
                ]
            },
            'identity': {
                'oidc': {
                    'issuer': 'string'
                }
            },
            'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING',
            'certificateAuthority': {
                'data': 'string'
            },
            'clientRequestToken': 'string',
            'platformVersion': 'string',
            'tags': {
                'string': 'string'
            },
            'encryptionConfig': [
                {
                    'resources': [
                        'string',
                    ],
                    'provider': {
                        'keyArn': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_fargate_profile(fargateProfileName=None, clusterName=None, podExecutionRoleArn=None, subnets=None, selectors=None, clientRequestToken=None, tags=None):
    """
    Creates an AWS Fargate profile for your Amazon EKS cluster. You must have at least one Fargate profile in a cluster to be able to run pods on Fargate.
    The Fargate profile allows an administrator to declare which pods run on Fargate and specify which pods run on which Fargate profile. This declaration is done through the profile\xe2\x80\x99s selectors. Each profile can have up to five selectors that contain a namespace and labels. A namespace is required for every selector. The label field consists of multiple optional key-value pairs. Pods that match the selectors are scheduled on Fargate. If a to-be-scheduled pod matches any of the selectors in the Fargate profile, then that pod is run on Fargate.
    When you create a Fargate profile, you must specify a pod execution role to use with the pods that are scheduled with the profile. This role is added to the cluster\'s Kubernetes Role Based Access Control (RBAC) for authorization so that the kubelet that is running on the Fargate infrastructure can register with your Amazon EKS cluster so that it can appear in your cluster as a node. The pod execution role also provides IAM permissions to the Fargate infrastructure to allow read access to Amazon ECR image repositories. For more information, see Pod Execution Role in the Amazon EKS User Guide .
    Fargate profiles are immutable. However, you can create a new updated profile to replace an existing profile and then delete the original after the updated profile has finished creating.
    If any Fargate profiles in a cluster are in the DELETING status, you must wait for that Fargate profile to finish deleting before you can create any other profiles in that cluster.
    For more information, see AWS Fargate Profile in the Amazon EKS User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_fargate_profile(
        fargateProfileName='string',
        clusterName='string',
        podExecutionRoleArn='string',
        subnets=[
            'string',
        ],
        selectors=[
            {
                'namespace': 'string',
                'labels': {
                    'string': 'string'
                }
            },
        ],
        clientRequestToken='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type fargateProfileName: string
    :param fargateProfileName: [REQUIRED]\nThe name of the Fargate profile.\n

    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the Amazon EKS cluster to apply the Fargate profile to.\n

    :type podExecutionRoleArn: string
    :param podExecutionRoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the pod execution role to use for pods that match the selectors in the Fargate profile. The pod execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. For more information, see Pod Execution Role in the Amazon EKS User Guide .\n

    :type subnets: list
    :param subnets: The IDs of subnets to launch your pods into. At this time, pods running on Fargate are not assigned public IP addresses, so only private subnets (with no direct route to an Internet Gateway) are accepted for this parameter.\n\n(string) --\n\n

    :type selectors: list
    :param selectors: The selectors to match for pods to use this Fargate profile. Each selector must have an associated namespace. Optionally, you can also specify labels for a namespace. You may specify up to five selectors in a Fargate profile.\n\n(dict) --An object representing an AWS Fargate profile selector.\n\nnamespace (string) --The Kubernetes namespace that the selector should match.\n\nlabels (dict) --The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type tags: dict
    :param tags: The metadata to apply to the Fargate profile to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Fargate profile tags do not propagate to any other resources associated with the Fargate profile, such as the pods that are scheduled with it.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'fargateProfile': {
        'fargateProfileName': 'string',
        'fargateProfileArn': 'string',
        'clusterName': 'string',
        'createdAt': datetime(2015, 1, 1),
        'podExecutionRoleArn': 'string',
        'subnets': [
            'string',
        ],
        'selectors': [
            {
                'namespace': 'string',
                'labels': {
                    'string': 'string'
                }
            },
        ],
        'status': 'CREATING'|'ACTIVE'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED',
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

fargateProfile (dict) --
The full description of your new Fargate profile.

fargateProfileName (string) --
The name of the Fargate profile.

fargateProfileArn (string) --
The full Amazon Resource Name (ARN) of the Fargate profile.

clusterName (string) --
The name of the Amazon EKS cluster that the Fargate profile belongs to.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the Fargate profile was created.

podExecutionRoleArn (string) --
The Amazon Resource Name (ARN) of the pod execution role to use for pods that match the selectors in the Fargate profile. For more information, see Pod Execution Role in the Amazon EKS User Guide .

subnets (list) --
The IDs of subnets to launch pods into.

(string) --


selectors (list) --
The selectors to match for pods to use this Fargate profile.

(dict) --
An object representing an AWS Fargate profile selector.

namespace (string) --
The Kubernetes namespace that the selector should match.

labels (dict) --
The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match.

(string) --
(string) --








status (string) --
The current status of the Fargate profile.

tags (dict) --
The metadata applied to the Fargate profile to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Fargate profile tags do not propagate to any other resources associated with the Fargate profile, such as the pods that are scheduled with it.

(string) --
(string) --












Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.InvalidRequestException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ResourceLimitExceededException
EKS.Client.exceptions.UnsupportedAvailabilityZoneException


    :return: {
        'fargateProfile': {
            'fargateProfileName': 'string',
            'fargateProfileArn': 'string',
            'clusterName': 'string',
            'createdAt': datetime(2015, 1, 1),
            'podExecutionRoleArn': 'string',
            'subnets': [
                'string',
            ],
            'selectors': [
                {
                    'namespace': 'string',
                    'labels': {
                        'string': 'string'
                    }
                },
            ],
            'status': 'CREATING'|'ACTIVE'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED',
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_nodegroup(clusterName=None, nodegroupName=None, scalingConfig=None, diskSize=None, subnets=None, instanceTypes=None, amiType=None, remoteAccess=None, nodeRole=None, labels=None, tags=None, clientRequestToken=None, version=None, releaseVersion=None):
    """
    Creates a managed worker node group for an Amazon EKS cluster. You can only create a node group for your cluster that is equal to the current Kubernetes version for the cluster. All node groups are created with the latest AMI release version for the respective minor Kubernetes version of the cluster.
    An Amazon EKS managed node group is an Amazon EC2 Auto Scaling group and associated Amazon EC2 instances that are managed by AWS for an Amazon EKS cluster. Each node group uses a version of the Amazon EKS-optimized Amazon Linux 2 AMI. For more information, see Managed Node Groups in the Amazon EKS User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_nodegroup(
        clusterName='string',
        nodegroupName='string',
        scalingConfig={
            'minSize': 123,
            'maxSize': 123,
            'desiredSize': 123
        },
        diskSize=123,
        subnets=[
            'string',
        ],
        instanceTypes=[
            'string',
        ],
        amiType='AL2_x86_64'|'AL2_x86_64_GPU',
        remoteAccess={
            'ec2SshKey': 'string',
            'sourceSecurityGroups': [
                'string',
            ]
        },
        nodeRole='string',
        labels={
            'string': 'string'
        },
        tags={
            'string': 'string'
        },
        clientRequestToken='string',
        version='string',
        releaseVersion='string'
    )
    
    
    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the cluster to create the node group in.\n

    :type nodegroupName: string
    :param nodegroupName: [REQUIRED]\nThe unique name to give your node group.\n

    :type scalingConfig: dict
    :param scalingConfig: The scaling configuration details for the Auto Scaling group that is created for your node group.\n\nminSize (integer) --The minimum number of worker nodes that the managed node group can scale in to. This number must be greater than zero.\n\nmaxSize (integer) --The maximum number of worker nodes that the managed node group can scale out to. Managed node groups can support up to 100 nodes by default.\n\ndesiredSize (integer) --The current number of worker nodes that the managed node group should maintain.\n\n\n

    :type diskSize: integer
    :param diskSize: The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB.

    :type subnets: list
    :param subnets: [REQUIRED]\nThe subnets to use for the Auto Scaling group that is created for your node group. These subnets must have the tag key kubernetes.io/cluster/CLUSTER_NAME with a value of shared , where CLUSTER_NAME is replaced with the name of your cluster.\n\n(string) --\n\n

    :type instanceTypes: list
    :param instanceTypes: The instance type to use for your node group. Currently, you can specify a single instance type for a node group. The default value for this parameter is t3.medium . If you choose a GPU instance type, be sure to specify the AL2_x86_64_GPU with the amiType parameter.\n\n(string) --\n\n

    :type amiType: string
    :param amiType: The AMI type for your node group. GPU instance types should use the AL2_x86_64_GPU AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU support. Non-GPU instances should use the AL2_x86_64 AMI type, which uses the Amazon EKS-optimized Linux AMI.

    :type remoteAccess: dict
    :param remoteAccess: The remote access (SSH) configuration to use with your node group.\n\nec2SshKey (string) --The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes in the managed node group. For more information, see Amazon EC2 Key Pairs in the Amazon Elastic Compute Cloud User Guide for Linux Instances .\n\nsourceSecurityGroups (list) --The security groups that are allowed SSH access (port 22) to the worker nodes. If you specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group, then port 22 on the worker nodes is opened to the internet (0.0.0.0/0). For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .\n\n(string) --\n\n\n\n

    :type nodeRole: string
    :param nodeRole: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM role to associate with your node group. The Amazon EKS worker node kubelet daemon makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch worker nodes and register them into a cluster, you must create an IAM role for those worker nodes to use when they are launched. For more information, see Amazon EKS Worker Node IAM Role in the * Amazon EKS User Guide * .\n

    :type labels: dict
    :param labels: The Kubernetes labels to be applied to the nodes in the node group when they are created.\n\n(string) --\n(string) --\n\n\n\n

    :type tags: dict
    :param tags: The metadata to apply to the node group to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Node group tags do not propagate to any other resources associated with the node group, such as the Amazon EC2 instances or subnets.\n\n(string) --\n(string) --\n\n\n\n

    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type version: string
    :param version: The Kubernetes version to use for your managed nodes. By default, the Kubernetes version of the cluster is used, and this is the only accepted specified value.

    :type releaseVersion: string
    :param releaseVersion: The AMI version of the Amazon EKS-optimized AMI to use with your node group. By default, the latest available AMI version for the node group\'s current Kubernetes version is used. For more information, see Amazon EKS-Optimized Linux AMI Versions in the Amazon EKS User Guide .

    :rtype: dict

ReturnsResponse Syntax
{
    'nodegroup': {
        'nodegroupName': 'string',
        'nodegroupArn': 'string',
        'clusterName': 'string',
        'version': 'string',
        'releaseVersion': 'string',
        'createdAt': datetime(2015, 1, 1),
        'modifiedAt': datetime(2015, 1, 1),
        'status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED'|'DEGRADED',
        'scalingConfig': {
            'minSize': 123,
            'maxSize': 123,
            'desiredSize': 123
        },
        'instanceTypes': [
            'string',
        ],
        'subnets': [
            'string',
        ],
        'remoteAccess': {
            'ec2SshKey': 'string',
            'sourceSecurityGroups': [
                'string',
            ]
        },
        'amiType': 'AL2_x86_64'|'AL2_x86_64_GPU',
        'nodeRole': 'string',
        'labels': {
            'string': 'string'
        },
        'resources': {
            'autoScalingGroups': [
                {
                    'name': 'string'
                },
            ],
            'remoteAccessSecurityGroup': 'string'
        },
        'diskSize': 123,
        'health': {
            'issues': [
                {
                    'code': 'AutoScalingGroupNotFound'|'AutoScalingGroupInvalidConfiguration'|'Ec2SecurityGroupNotFound'|'Ec2SecurityGroupDeletionFailure'|'Ec2LaunchTemplateNotFound'|'Ec2LaunchTemplateVersionMismatch'|'Ec2SubnetNotFound'|'Ec2SubnetInvalidConfiguration'|'IamInstanceProfileNotFound'|'IamLimitExceeded'|'IamNodeRoleNotFound'|'NodeCreationFailure'|'AsgInstanceLaunchFailures'|'InstanceLimitExceeded'|'InsufficientFreeAddresses'|'AccessDenied'|'InternalFailure',
                    'message': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        },
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

nodegroup (dict) --
The full description of your new node group.

nodegroupName (string) --
The name associated with an Amazon EKS managed node group.

nodegroupArn (string) --
The Amazon Resource Name (ARN) associated with the managed node group.

clusterName (string) --
The name of the cluster that the managed node group resides in.

version (string) --
The Kubernetes version of the managed node group.

releaseVersion (string) --
The AMI version of the managed node group. For more information, see Amazon EKS-Optimized Linux AMI Versions in the Amazon EKS User Guide .

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the managed node group was created.

modifiedAt (datetime) --
The Unix epoch timestamp in seconds for when the managed node group was last modified.

status (string) --
The current status of the managed node group.

scalingConfig (dict) --
The scaling configuration details for the Auto Scaling group that is associated with your node group.

minSize (integer) --
The minimum number of worker nodes that the managed node group can scale in to. This number must be greater than zero.

maxSize (integer) --
The maximum number of worker nodes that the managed node group can scale out to. Managed node groups can support up to 100 nodes by default.

desiredSize (integer) --
The current number of worker nodes that the managed node group should maintain.



instanceTypes (list) --
The instance types associated with your node group.

(string) --


subnets (list) --
The subnets allowed for the Auto Scaling group that is associated with your node group. These subnets must have the following tag: kubernetes.io/cluster/CLUSTER_NAME , where CLUSTER_NAME is replaced with the name of your cluster.

(string) --


remoteAccess (dict) --
The remote access (SSH) configuration that is associated with the node group.

ec2SshKey (string) --
The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes in the managed node group. For more information, see Amazon EC2 Key Pairs in the Amazon Elastic Compute Cloud User Guide for Linux Instances .

sourceSecurityGroups (list) --
The security groups that are allowed SSH access (port 22) to the worker nodes. If you specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group, then port 22 on the worker nodes is opened to the internet (0.0.0.0/0). For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .

(string) --




amiType (string) --
The AMI type associated with your node group. GPU instance types should use the AL2_x86_64_GPU AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU support. Non-GPU instances should use the AL2_x86_64 AMI type, which uses the Amazon EKS-optimized Linux AMI.

nodeRole (string) --
The IAM role associated with your node group. The Amazon EKS worker node kubelet daemon makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch worker nodes and register them into a cluster, you must create an IAM role for those worker nodes to use when they are launched. For more information, see Amazon EKS Worker Node IAM Role in the * Amazon EKS User Guide * .

labels (dict) --
The Kubernetes labels applied to the nodes in the node group.

Note
Only labels that are applied with the Amazon EKS API are shown here. There may be other Kubernetes labels applied to the nodes in this group.


(string) --
(string) --




resources (dict) --
The resources associated with the node group, such as Auto Scaling groups and security groups for remote access.

autoScalingGroups (list) --
The Auto Scaling groups associated with the node group.

(dict) --
An Auto Scaling group that is associated with an Amazon EKS managed node group.

name (string) --
The name of the Auto Scaling group associated with an Amazon EKS managed node group.





remoteAccessSecurityGroup (string) --
The remote access security group associated with the node group. This security group controls SSH access to the worker nodes.



diskSize (integer) --
The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB.

health (dict) --
The health status of the node group. If there are issues with your node group\'s health, they are listed here.

issues (list) --
Any issues that are associated with the node group.

(dict) --
An object representing an issue with an Amazon EKS resource.

code (string) --
A brief description of the error.

AutoScalingGroupNotFound : We couldn\'t find the Auto Scaling group associated with the managed node group. You may be able to recreate an Auto Scaling group with the same settings to recover.
Ec2SecurityGroupNotFound : We couldn\'t find the cluster security group for the cluster. You must recreate your cluster.
Ec2SecurityGroupDeletionFailure : We could not delete the remote access security group for your managed node group. Remove any dependencies from the security group.
Ec2LaunchTemplateNotFound : We couldn\'t find the Amazon EC2 launch template for your managed node group. You may be able to recreate a launch template with the same settings to recover.
Ec2LaunchTemplateVersionMismatch : The Amazon EC2 launch template version for your managed node group does not match the version that Amazon EKS created. You may be able to revert to the version that Amazon EKS created to recover.
IamInstanceProfileNotFound : We couldn\'t find the IAM instance profile for your managed node group. You may be able to recreate an instance profile with the same settings to recover.
IamNodeRoleNotFound : We couldn\'t find the IAM role for your managed node group. You may be able to recreate an IAM role with the same settings to recover.
AsgInstanceLaunchFailures : Your Auto Scaling group is experiencing failures while attempting to launch instances.
NodeCreationFailure : Your launched instances are unable to register with your Amazon EKS cluster. Common causes of this failure are insufficient worker node IAM role permissions or lack of outbound internet access for the nodes.
InstanceLimitExceeded : Your AWS account is unable to launch any more instances of the specified instance type. You may be able to request an Amazon EC2 instance limit increase to recover.
InsufficientFreeAddresses : One or more of the subnets associated with your managed node group does not have enough available IP addresses for new nodes.
AccessDenied : Amazon EKS or one or more of your managed nodes is unable to communicate with your cluster API server.
InternalFailure : These errors are usually caused by an Amazon EKS server-side issue.


message (string) --
The error message associated with the issue.

resourceIds (list) --
The AWS resources that are afflicted by this issue.

(string) --








tags (dict) --
The metadata applied to the node group to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Node group tags do not propagate to any other resources associated with the node group, such as the Amazon EC2 instances or subnets.

(string) --
(string) --












Exceptions

EKS.Client.exceptions.ResourceInUseException
EKS.Client.exceptions.ResourceLimitExceededException
EKS.Client.exceptions.InvalidRequestException
EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ServiceUnavailableException


    :return: {
        'nodegroup': {
            'nodegroupName': 'string',
            'nodegroupArn': 'string',
            'clusterName': 'string',
            'version': 'string',
            'releaseVersion': 'string',
            'createdAt': datetime(2015, 1, 1),
            'modifiedAt': datetime(2015, 1, 1),
            'status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED'|'DEGRADED',
            'scalingConfig': {
                'minSize': 123,
                'maxSize': 123,
                'desiredSize': 123
            },
            'instanceTypes': [
                'string',
            ],
            'subnets': [
                'string',
            ],
            'remoteAccess': {
                'ec2SshKey': 'string',
                'sourceSecurityGroups': [
                    'string',
                ]
            },
            'amiType': 'AL2_x86_64'|'AL2_x86_64_GPU',
            'nodeRole': 'string',
            'labels': {
                'string': 'string'
            },
            'resources': {
                'autoScalingGroups': [
                    {
                        'name': 'string'
                    },
                ],
                'remoteAccessSecurityGroup': 'string'
            },
            'diskSize': 123,
            'health': {
                'issues': [
                    {
                        'code': 'AutoScalingGroupNotFound'|'AutoScalingGroupInvalidConfiguration'|'Ec2SecurityGroupNotFound'|'Ec2SecurityGroupDeletionFailure'|'Ec2LaunchTemplateNotFound'|'Ec2LaunchTemplateVersionMismatch'|'Ec2SubnetNotFound'|'Ec2SubnetInvalidConfiguration'|'IamInstanceProfileNotFound'|'IamLimitExceeded'|'IamNodeRoleNotFound'|'NodeCreationFailure'|'AsgInstanceLaunchFailures'|'InstanceLimitExceeded'|'InsufficientFreeAddresses'|'AccessDenied'|'InternalFailure',
                        'message': 'string',
                        'resourceIds': [
                            'string',
                        ]
                    },
                ]
            },
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_cluster(name=None):
    """
    Deletes the Amazon EKS cluster control plane.
    If you have active services in your cluster that are associated with a load balancer, you must delete those services before deleting the cluster so that the load balancers are deleted properly. Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete the VPC. For more information, see Deleting a Cluster in the Amazon EKS User Guide .
    If you have managed node groups or Fargate profiles attached to the cluster, you must delete them first. For more information, see  DeleteNodegroup and  DeleteFargateProfile .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example command deletes a cluster named devel in your default region.
    Expected Output:
    
    :example: response = client.delete_cluster(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the cluster to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'cluster': {
        'name': 'string',
        'arn': 'string',
        'createdAt': datetime(2015, 1, 1),
        'version': 'string',
        'endpoint': 'string',
        'roleArn': 'string',
        'resourcesVpcConfig': {
            'subnetIds': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ],
            'clusterSecurityGroupId': 'string',
            'vpcId': 'string',
            'endpointPublicAccess': True|False,
            'endpointPrivateAccess': True|False,
            'publicAccessCidrs': [
                'string',
            ]
        },
        'logging': {
            'clusterLogging': [
                {
                    'types': [
                        'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                    ],
                    'enabled': True|False
                },
            ]
        },
        'identity': {
            'oidc': {
                'issuer': 'string'
            }
        },
        'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING',
        'certificateAuthority': {
            'data': 'string'
        },
        'clientRequestToken': 'string',
        'platformVersion': 'string',
        'tags': {
            'string': 'string'
        },
        'encryptionConfig': [
            {
                'resources': [
                    'string',
                ],
                'provider': {
                    'keyArn': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --
cluster (dict) --The full description of the cluster to delete.

name (string) --The name of the cluster.

arn (string) --The Amazon Resource Name (ARN) of the cluster.

createdAt (datetime) --The Unix epoch timestamp in seconds for when the cluster was created.

version (string) --The Kubernetes server version for the cluster.

endpoint (string) --The endpoint for your Kubernetes API server.

roleArn (string) --The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.

resourcesVpcConfig (dict) --The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see Cluster VPC Considerations and Cluster Security Group Considerations in the Amazon EKS User Guide .

subnetIds (list) --The subnets associated with your cluster.

(string) --


securityGroupIds (list) --The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your worker nodes and the Kubernetes control plane.

(string) --


clusterSecurityGroupId (string) --The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control-plane-to-data-plane communication.

vpcId (string) --The VPC associated with your cluster.

endpointPublicAccess (boolean) --This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If the Amazon EKS public API server endpoint is disabled, your cluster\'s Kubernetes API server can only receive requests that originate from within the cluster VPC.

endpointPrivateAccess (boolean) --This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your cluster\'s VPC use the private VPC endpoint instead of traversing the internet. If this value is disabled and you have worker nodes or AWS Fargate pods in the cluster, then ensure that publicAccessCidrs includes the necessary CIDR blocks for communication with the worker nodes or Fargate pods. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .

publicAccessCidrs (list) --The CIDR blocks that are allowed access to your cluster\'s public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the listed CIDR blocks is denied. The default value is 0.0.0.0/0 . If you\'ve disabled private endpoint access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that the necessary CIDR blocks are listed. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .

(string) --




logging (dict) --The logging configuration for your cluster.

clusterLogging (list) --The cluster control plane logging configuration for your cluster.

(dict) --An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

types (list) --The available cluster control plane log types.

(string) --


enabled (boolean) --If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs. If a log type isn\'t enabled, that log type doesn\'t export its control plane logs. Each individual log type can be enabled or disabled independently.







identity (dict) --The identity provider information for the cluster.

oidc (dict) --The OpenID Connect identity provider information for the cluster.

issuer (string) --The issuer URL for the OpenID Connect identity provider.





status (string) --The current status of the cluster.

certificateAuthority (dict) --The certificate-authority-data for your cluster.

data (string) --The Base64-encoded certificate data required to communicate with your cluster. Add this to the certificate-authority-data section of the kubeconfig file for your cluster.



clientRequestToken (string) --Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

platformVersion (string) --The platform version of your Amazon EKS cluster. For more information, see Platform Versions in the * Amazon EKS User Guide * .

tags (dict) --The metadata that you apply to the cluster to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Cluster tags do not propagate to any other resources associated with the cluster.

(string) --
(string) --




encryptionConfig (list) --The encryption configuration for the cluster.

(dict) --The encryption configuration for the cluster.

resources (list) --Specifies the resources to be encrypted. The only supported value is "secrets".

(string) --


provider (dict) --AWS Key Management Service (AWS KMS) customer master key (CMK). Either the ARN or the alias can be used.

keyArn (string) --Amazon Resource Name (ARN) or alias of the customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK. For more information, see Allowing Users in Other Accounts to Use a CMK in the AWS Key Management Service Developer Guide .














Exceptions

EKS.Client.exceptions.ResourceInUseException
EKS.Client.exceptions.ResourceNotFoundException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ServiceUnavailableException

Examples
This example command deletes a cluster named devel in your default region.
response = client.delete_cluster(
    name='devel',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'cluster': {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'version': 'string',
            'endpoint': 'string',
            'roleArn': 'string',
            'resourcesVpcConfig': {
                'subnetIds': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ],
                'clusterSecurityGroupId': 'string',
                'vpcId': 'string',
                'endpointPublicAccess': True|False,
                'endpointPrivateAccess': True|False,
                'publicAccessCidrs': [
                    'string',
                ]
            },
            'logging': {
                'clusterLogging': [
                    {
                        'types': [
                            'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                        ],
                        'enabled': True|False
                    },
                ]
            },
            'identity': {
                'oidc': {
                    'issuer': 'string'
                }
            },
            'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING',
            'certificateAuthority': {
                'data': 'string'
            },
            'clientRequestToken': 'string',
            'platformVersion': 'string',
            'tags': {
                'string': 'string'
            },
            'encryptionConfig': [
                {
                    'resources': [
                        'string',
                    ],
                    'provider': {
                        'keyArn': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_fargate_profile(clusterName=None, fargateProfileName=None):
    """
    Deletes an AWS Fargate profile.
    When you delete a Fargate profile, any pods running on Fargate that were created with the profile are deleted. If those pods match another Fargate profile, then they are scheduled on Fargate with that profile. If they no longer match any Fargate profiles, then they are not scheduled on Fargate and they may remain in a pending state.
    Only one Fargate profile in a cluster can be in the DELETING status at a time. You must wait for a Fargate profile to finish deleting before you can delete any other profiles in that cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_fargate_profile(
        clusterName='string',
        fargateProfileName='string'
    )
    
    
    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the Amazon EKS cluster associated with the Fargate profile to delete.\n

    :type fargateProfileName: string
    :param fargateProfileName: [REQUIRED]\nThe name of the Fargate profile to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'fargateProfile': {
        'fargateProfileName': 'string',
        'fargateProfileArn': 'string',
        'clusterName': 'string',
        'createdAt': datetime(2015, 1, 1),
        'podExecutionRoleArn': 'string',
        'subnets': [
            'string',
        ],
        'selectors': [
            {
                'namespace': 'string',
                'labels': {
                    'string': 'string'
                }
            },
        ],
        'status': 'CREATING'|'ACTIVE'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED',
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

fargateProfile (dict) --
The deleted Fargate profile.

fargateProfileName (string) --
The name of the Fargate profile.

fargateProfileArn (string) --
The full Amazon Resource Name (ARN) of the Fargate profile.

clusterName (string) --
The name of the Amazon EKS cluster that the Fargate profile belongs to.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the Fargate profile was created.

podExecutionRoleArn (string) --
The Amazon Resource Name (ARN) of the pod execution role to use for pods that match the selectors in the Fargate profile. For more information, see Pod Execution Role in the Amazon EKS User Guide .

subnets (list) --
The IDs of subnets to launch pods into.

(string) --


selectors (list) --
The selectors to match for pods to use this Fargate profile.

(dict) --
An object representing an AWS Fargate profile selector.

namespace (string) --
The Kubernetes namespace that the selector should match.

labels (dict) --
The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match.

(string) --
(string) --








status (string) --
The current status of the Fargate profile.

tags (dict) --
The metadata applied to the Fargate profile to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Fargate profile tags do not propagate to any other resources associated with the Fargate profile, such as the pods that are scheduled with it.

(string) --
(string) --












Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ResourceNotFoundException


    :return: {
        'fargateProfile': {
            'fargateProfileName': 'string',
            'fargateProfileArn': 'string',
            'clusterName': 'string',
            'createdAt': datetime(2015, 1, 1),
            'podExecutionRoleArn': 'string',
            'subnets': [
                'string',
            ],
            'selectors': [
                {
                    'namespace': 'string',
                    'labels': {
                        'string': 'string'
                    }
                },
            ],
            'status': 'CREATING'|'ACTIVE'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED',
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_nodegroup(clusterName=None, nodegroupName=None):
    """
    Deletes an Amazon EKS node group for a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_nodegroup(
        clusterName='string',
        nodegroupName='string'
    )
    
    
    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the Amazon EKS cluster that is associated with your node group.\n

    :type nodegroupName: string
    :param nodegroupName: [REQUIRED]\nThe name of the node group to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nodegroup': {
        'nodegroupName': 'string',
        'nodegroupArn': 'string',
        'clusterName': 'string',
        'version': 'string',
        'releaseVersion': 'string',
        'createdAt': datetime(2015, 1, 1),
        'modifiedAt': datetime(2015, 1, 1),
        'status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED'|'DEGRADED',
        'scalingConfig': {
            'minSize': 123,
            'maxSize': 123,
            'desiredSize': 123
        },
        'instanceTypes': [
            'string',
        ],
        'subnets': [
            'string',
        ],
        'remoteAccess': {
            'ec2SshKey': 'string',
            'sourceSecurityGroups': [
                'string',
            ]
        },
        'amiType': 'AL2_x86_64'|'AL2_x86_64_GPU',
        'nodeRole': 'string',
        'labels': {
            'string': 'string'
        },
        'resources': {
            'autoScalingGroups': [
                {
                    'name': 'string'
                },
            ],
            'remoteAccessSecurityGroup': 'string'
        },
        'diskSize': 123,
        'health': {
            'issues': [
                {
                    'code': 'AutoScalingGroupNotFound'|'AutoScalingGroupInvalidConfiguration'|'Ec2SecurityGroupNotFound'|'Ec2SecurityGroupDeletionFailure'|'Ec2LaunchTemplateNotFound'|'Ec2LaunchTemplateVersionMismatch'|'Ec2SubnetNotFound'|'Ec2SubnetInvalidConfiguration'|'IamInstanceProfileNotFound'|'IamLimitExceeded'|'IamNodeRoleNotFound'|'NodeCreationFailure'|'AsgInstanceLaunchFailures'|'InstanceLimitExceeded'|'InsufficientFreeAddresses'|'AccessDenied'|'InternalFailure',
                    'message': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        },
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

nodegroup (dict) --
The full description of your deleted node group.

nodegroupName (string) --
The name associated with an Amazon EKS managed node group.

nodegroupArn (string) --
The Amazon Resource Name (ARN) associated with the managed node group.

clusterName (string) --
The name of the cluster that the managed node group resides in.

version (string) --
The Kubernetes version of the managed node group.

releaseVersion (string) --
The AMI version of the managed node group. For more information, see Amazon EKS-Optimized Linux AMI Versions in the Amazon EKS User Guide .

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the managed node group was created.

modifiedAt (datetime) --
The Unix epoch timestamp in seconds for when the managed node group was last modified.

status (string) --
The current status of the managed node group.

scalingConfig (dict) --
The scaling configuration details for the Auto Scaling group that is associated with your node group.

minSize (integer) --
The minimum number of worker nodes that the managed node group can scale in to. This number must be greater than zero.

maxSize (integer) --
The maximum number of worker nodes that the managed node group can scale out to. Managed node groups can support up to 100 nodes by default.

desiredSize (integer) --
The current number of worker nodes that the managed node group should maintain.



instanceTypes (list) --
The instance types associated with your node group.

(string) --


subnets (list) --
The subnets allowed for the Auto Scaling group that is associated with your node group. These subnets must have the following tag: kubernetes.io/cluster/CLUSTER_NAME , where CLUSTER_NAME is replaced with the name of your cluster.

(string) --


remoteAccess (dict) --
The remote access (SSH) configuration that is associated with the node group.

ec2SshKey (string) --
The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes in the managed node group. For more information, see Amazon EC2 Key Pairs in the Amazon Elastic Compute Cloud User Guide for Linux Instances .

sourceSecurityGroups (list) --
The security groups that are allowed SSH access (port 22) to the worker nodes. If you specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group, then port 22 on the worker nodes is opened to the internet (0.0.0.0/0). For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .

(string) --




amiType (string) --
The AMI type associated with your node group. GPU instance types should use the AL2_x86_64_GPU AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU support. Non-GPU instances should use the AL2_x86_64 AMI type, which uses the Amazon EKS-optimized Linux AMI.

nodeRole (string) --
The IAM role associated with your node group. The Amazon EKS worker node kubelet daemon makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch worker nodes and register them into a cluster, you must create an IAM role for those worker nodes to use when they are launched. For more information, see Amazon EKS Worker Node IAM Role in the * Amazon EKS User Guide * .

labels (dict) --
The Kubernetes labels applied to the nodes in the node group.

Note
Only labels that are applied with the Amazon EKS API are shown here. There may be other Kubernetes labels applied to the nodes in this group.


(string) --
(string) --




resources (dict) --
The resources associated with the node group, such as Auto Scaling groups and security groups for remote access.

autoScalingGroups (list) --
The Auto Scaling groups associated with the node group.

(dict) --
An Auto Scaling group that is associated with an Amazon EKS managed node group.

name (string) --
The name of the Auto Scaling group associated with an Amazon EKS managed node group.





remoteAccessSecurityGroup (string) --
The remote access security group associated with the node group. This security group controls SSH access to the worker nodes.



diskSize (integer) --
The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB.

health (dict) --
The health status of the node group. If there are issues with your node group\'s health, they are listed here.

issues (list) --
Any issues that are associated with the node group.

(dict) --
An object representing an issue with an Amazon EKS resource.

code (string) --
A brief description of the error.

AutoScalingGroupNotFound : We couldn\'t find the Auto Scaling group associated with the managed node group. You may be able to recreate an Auto Scaling group with the same settings to recover.
Ec2SecurityGroupNotFound : We couldn\'t find the cluster security group for the cluster. You must recreate your cluster.
Ec2SecurityGroupDeletionFailure : We could not delete the remote access security group for your managed node group. Remove any dependencies from the security group.
Ec2LaunchTemplateNotFound : We couldn\'t find the Amazon EC2 launch template for your managed node group. You may be able to recreate a launch template with the same settings to recover.
Ec2LaunchTemplateVersionMismatch : The Amazon EC2 launch template version for your managed node group does not match the version that Amazon EKS created. You may be able to revert to the version that Amazon EKS created to recover.
IamInstanceProfileNotFound : We couldn\'t find the IAM instance profile for your managed node group. You may be able to recreate an instance profile with the same settings to recover.
IamNodeRoleNotFound : We couldn\'t find the IAM role for your managed node group. You may be able to recreate an IAM role with the same settings to recover.
AsgInstanceLaunchFailures : Your Auto Scaling group is experiencing failures while attempting to launch instances.
NodeCreationFailure : Your launched instances are unable to register with your Amazon EKS cluster. Common causes of this failure are insufficient worker node IAM role permissions or lack of outbound internet access for the nodes.
InstanceLimitExceeded : Your AWS account is unable to launch any more instances of the specified instance type. You may be able to request an Amazon EC2 instance limit increase to recover.
InsufficientFreeAddresses : One or more of the subnets associated with your managed node group does not have enough available IP addresses for new nodes.
AccessDenied : Amazon EKS or one or more of your managed nodes is unable to communicate with your cluster API server.
InternalFailure : These errors are usually caused by an Amazon EKS server-side issue.


message (string) --
The error message associated with the issue.

resourceIds (list) --
The AWS resources that are afflicted by this issue.

(string) --








tags (dict) --
The metadata applied to the node group to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Node group tags do not propagate to any other resources associated with the node group, such as the Amazon EC2 instances or subnets.

(string) --
(string) --












Exceptions

EKS.Client.exceptions.ResourceInUseException
EKS.Client.exceptions.ResourceNotFoundException
EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ServiceUnavailableException


    :return: {
        'nodegroup': {
            'nodegroupName': 'string',
            'nodegroupArn': 'string',
            'clusterName': 'string',
            'version': 'string',
            'releaseVersion': 'string',
            'createdAt': datetime(2015, 1, 1),
            'modifiedAt': datetime(2015, 1, 1),
            'status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED'|'DEGRADED',
            'scalingConfig': {
                'minSize': 123,
                'maxSize': 123,
                'desiredSize': 123
            },
            'instanceTypes': [
                'string',
            ],
            'subnets': [
                'string',
            ],
            'remoteAccess': {
                'ec2SshKey': 'string',
                'sourceSecurityGroups': [
                    'string',
                ]
            },
            'amiType': 'AL2_x86_64'|'AL2_x86_64_GPU',
            'nodeRole': 'string',
            'labels': {
                'string': 'string'
            },
            'resources': {
                'autoScalingGroups': [
                    {
                        'name': 'string'
                    },
                ],
                'remoteAccessSecurityGroup': 'string'
            },
            'diskSize': 123,
            'health': {
                'issues': [
                    {
                        'code': 'AutoScalingGroupNotFound'|'AutoScalingGroupInvalidConfiguration'|'Ec2SecurityGroupNotFound'|'Ec2SecurityGroupDeletionFailure'|'Ec2LaunchTemplateNotFound'|'Ec2LaunchTemplateVersionMismatch'|'Ec2SubnetNotFound'|'Ec2SubnetInvalidConfiguration'|'IamInstanceProfileNotFound'|'IamLimitExceeded'|'IamNodeRoleNotFound'|'NodeCreationFailure'|'AsgInstanceLaunchFailures'|'InstanceLimitExceeded'|'InsufficientFreeAddresses'|'AccessDenied'|'InternalFailure',
                        'message': 'string',
                        'resourceIds': [
                            'string',
                        ]
                    },
                ]
            },
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_cluster(name=None):
    """
    Returns descriptive information about an Amazon EKS cluster.
    The API server endpoint and certificate authority data returned by this operation are required for kubelet and kubectl to communicate with your Kubernetes API server. For more information, see Create a kubeconfig for Amazon EKS .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example command provides a description of the specified cluster in your default region.
    Expected Output:
    
    :example: response = client.describe_cluster(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the cluster to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'cluster': {
        'name': 'string',
        'arn': 'string',
        'createdAt': datetime(2015, 1, 1),
        'version': 'string',
        'endpoint': 'string',
        'roleArn': 'string',
        'resourcesVpcConfig': {
            'subnetIds': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ],
            'clusterSecurityGroupId': 'string',
            'vpcId': 'string',
            'endpointPublicAccess': True|False,
            'endpointPrivateAccess': True|False,
            'publicAccessCidrs': [
                'string',
            ]
        },
        'logging': {
            'clusterLogging': [
                {
                    'types': [
                        'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                    ],
                    'enabled': True|False
                },
            ]
        },
        'identity': {
            'oidc': {
                'issuer': 'string'
            }
        },
        'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING',
        'certificateAuthority': {
            'data': 'string'
        },
        'clientRequestToken': 'string',
        'platformVersion': 'string',
        'tags': {
            'string': 'string'
        },
        'encryptionConfig': [
            {
                'resources': [
                    'string',
                ],
                'provider': {
                    'keyArn': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --
cluster (dict) --The full description of your specified cluster.

name (string) --The name of the cluster.

arn (string) --The Amazon Resource Name (ARN) of the cluster.

createdAt (datetime) --The Unix epoch timestamp in seconds for when the cluster was created.

version (string) --The Kubernetes server version for the cluster.

endpoint (string) --The endpoint for your Kubernetes API server.

roleArn (string) --The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.

resourcesVpcConfig (dict) --The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see Cluster VPC Considerations and Cluster Security Group Considerations in the Amazon EKS User Guide .

subnetIds (list) --The subnets associated with your cluster.

(string) --


securityGroupIds (list) --The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your worker nodes and the Kubernetes control plane.

(string) --


clusterSecurityGroupId (string) --The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control-plane-to-data-plane communication.

vpcId (string) --The VPC associated with your cluster.

endpointPublicAccess (boolean) --This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If the Amazon EKS public API server endpoint is disabled, your cluster\'s Kubernetes API server can only receive requests that originate from within the cluster VPC.

endpointPrivateAccess (boolean) --This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your cluster\'s VPC use the private VPC endpoint instead of traversing the internet. If this value is disabled and you have worker nodes or AWS Fargate pods in the cluster, then ensure that publicAccessCidrs includes the necessary CIDR blocks for communication with the worker nodes or Fargate pods. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .

publicAccessCidrs (list) --The CIDR blocks that are allowed access to your cluster\'s public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the listed CIDR blocks is denied. The default value is 0.0.0.0/0 . If you\'ve disabled private endpoint access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that the necessary CIDR blocks are listed. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .

(string) --




logging (dict) --The logging configuration for your cluster.

clusterLogging (list) --The cluster control plane logging configuration for your cluster.

(dict) --An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

types (list) --The available cluster control plane log types.

(string) --


enabled (boolean) --If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs. If a log type isn\'t enabled, that log type doesn\'t export its control plane logs. Each individual log type can be enabled or disabled independently.







identity (dict) --The identity provider information for the cluster.

oidc (dict) --The OpenID Connect identity provider information for the cluster.

issuer (string) --The issuer URL for the OpenID Connect identity provider.





status (string) --The current status of the cluster.

certificateAuthority (dict) --The certificate-authority-data for your cluster.

data (string) --The Base64-encoded certificate data required to communicate with your cluster. Add this to the certificate-authority-data section of the kubeconfig file for your cluster.



clientRequestToken (string) --Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

platformVersion (string) --The platform version of your Amazon EKS cluster. For more information, see Platform Versions in the * Amazon EKS User Guide * .

tags (dict) --The metadata that you apply to the cluster to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Cluster tags do not propagate to any other resources associated with the cluster.

(string) --
(string) --




encryptionConfig (list) --The encryption configuration for the cluster.

(dict) --The encryption configuration for the cluster.

resources (list) --Specifies the resources to be encrypted. The only supported value is "secrets".

(string) --


provider (dict) --AWS Key Management Service (AWS KMS) customer master key (CMK). Either the ARN or the alias can be used.

keyArn (string) --Amazon Resource Name (ARN) or alias of the customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK. For more information, see Allowing Users in Other Accounts to Use a CMK in the AWS Key Management Service Developer Guide .














Exceptions

EKS.Client.exceptions.ResourceNotFoundException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ServiceUnavailableException

Examples
This example command provides a description of the specified cluster in your default region.
response = client.describe_cluster(
    name='devel',
)

print(response)


Expected Output:
{
    'cluster': {
        'version': '1.10',
        'name': 'devel',
        'arn': 'arn:aws:eks:us-west-2:012345678910:cluster/devel',
        'certificateAuthority': {
            'data': 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRFNE1EVXpNVEl6TVRFek1Wb1hEVEk0TURVeU9ESXpNVEV6TVZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTTZWCjVUaG4rdFcySm9Xa2hQMzRlVUZMNitaRXJOZGIvWVdrTmtDdWNGS2RaaXl2TjlMVmdvUmV2MjlFVFZlN1ZGbSsKUTJ3ZURyRXJiQyt0dVlibkFuN1ZLYmE3ay9hb1BHekZMdmVnb0t6b0M1N2NUdGVwZzRIazRlK2tIWHNaME10MApyb3NzcjhFM1ROeExETnNJTThGL1cwdjhsTGNCbWRPcjQyV2VuTjFHZXJnaDNSZ2wzR3JIazBnNTU0SjFWenJZCm9hTi8zODFUczlOTFF2QTBXb0xIcjBFRlZpTFdSZEoyZ3lXaC9ybDVyOFNDOHZaQXg1YW1BU0hVd01aTFpWRC8KTDBpOW4wRVM0MkpVdzQyQmxHOEdpd3NhTkJWV3lUTHZKclNhRXlDSHFtVVZaUTFDZkFXUjl0L3JleVVOVXM3TApWV1FqM3BFbk9RMitMSWJrc0RzQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFNZ3RsQ1dIQ2U2YzVHMXl2YlFTS0Q4K2hUalkKSm1NSG56L2EvRGt0WG9YUjFVQzIrZUgzT1BZWmVjRVZZZHVaSlZCckNNQ2VWR0ZkeWdBYlNLc1FxWDg0S2RXbAp1MU5QaERDSmEyRHliN2pVMUV6VThTQjFGZUZ5ZFE3a0hNS1E1blpBRVFQOTY4S01hSGUrSm0yQ2x1UFJWbEJVCjF4WlhTS1gzTVZ0K1Q0SU1EV2d6c3JRSjVuQkRjdEtLcUZtM3pKdVVubHo5ZEpVckdscEltMjVJWXJDckxYUFgKWkUwRUtRNWEzMHhkVWNrTHRGQkQrOEtBdFdqSS9yZUZPNzM1YnBMdVoyOTBaNm42QlF3elRrS0p4cnhVc3QvOAppNGsxcnlsaUdWMm5SSjBUYjNORkczNHgrYWdzYTRoSTFPbU90TFM0TmgvRXJxT3lIUXNDc2hEQUtKUT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=',
        },
        'createdAt': 1527807879.988,
        'endpoint': 'https://A0DCCD80A04F01705DD065655C30CC3D.yl4.us-west-2.eks.amazonaws.com',
        'resourcesVpcConfig': {
            'securityGroupIds': [
                'sg-6979fe18',
            ],
            'subnetIds': [
                'subnet-6782e71e',
                'subnet-e7e761ac',
            ],
            'vpcId': 'vpc-950809ec',
        },
        'roleArn': 'arn:aws:iam::012345678910:role/eks-service-role-AWSServiceRoleForAmazonEKS-J7ONKE3BQ4PI',
        'status': 'ACTIVE',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'cluster': {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'version': 'string',
            'endpoint': 'string',
            'roleArn': 'string',
            'resourcesVpcConfig': {
                'subnetIds': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ],
                'clusterSecurityGroupId': 'string',
                'vpcId': 'string',
                'endpointPublicAccess': True|False,
                'endpointPrivateAccess': True|False,
                'publicAccessCidrs': [
                    'string',
                ]
            },
            'logging': {
                'clusterLogging': [
                    {
                        'types': [
                            'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                        ],
                        'enabled': True|False
                    },
                ]
            },
            'identity': {
                'oidc': {
                    'issuer': 'string'
                }
            },
            'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING',
            'certificateAuthority': {
                'data': 'string'
            },
            'clientRequestToken': 'string',
            'platformVersion': 'string',
            'tags': {
                'string': 'string'
            },
            'encryptionConfig': [
                {
                    'resources': [
                        'string',
                    ],
                    'provider': {
                        'keyArn': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_fargate_profile(clusterName=None, fargateProfileName=None):
    """
    Returns descriptive information about an AWS Fargate profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_fargate_profile(
        clusterName='string',
        fargateProfileName='string'
    )
    
    
    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the Amazon EKS cluster associated with the Fargate profile.\n

    :type fargateProfileName: string
    :param fargateProfileName: [REQUIRED]\nThe name of the Fargate profile to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'fargateProfile': {
        'fargateProfileName': 'string',
        'fargateProfileArn': 'string',
        'clusterName': 'string',
        'createdAt': datetime(2015, 1, 1),
        'podExecutionRoleArn': 'string',
        'subnets': [
            'string',
        ],
        'selectors': [
            {
                'namespace': 'string',
                'labels': {
                    'string': 'string'
                }
            },
        ],
        'status': 'CREATING'|'ACTIVE'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED',
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

fargateProfile (dict) --
The full description of your Fargate profile.

fargateProfileName (string) --
The name of the Fargate profile.

fargateProfileArn (string) --
The full Amazon Resource Name (ARN) of the Fargate profile.

clusterName (string) --
The name of the Amazon EKS cluster that the Fargate profile belongs to.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the Fargate profile was created.

podExecutionRoleArn (string) --
The Amazon Resource Name (ARN) of the pod execution role to use for pods that match the selectors in the Fargate profile. For more information, see Pod Execution Role in the Amazon EKS User Guide .

subnets (list) --
The IDs of subnets to launch pods into.

(string) --


selectors (list) --
The selectors to match for pods to use this Fargate profile.

(dict) --
An object representing an AWS Fargate profile selector.

namespace (string) --
The Kubernetes namespace that the selector should match.

labels (dict) --
The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match.

(string) --
(string) --








status (string) --
The current status of the Fargate profile.

tags (dict) --
The metadata applied to the Fargate profile to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Fargate profile tags do not propagate to any other resources associated with the Fargate profile, such as the pods that are scheduled with it.

(string) --
(string) --












Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ResourceNotFoundException


    :return: {
        'fargateProfile': {
            'fargateProfileName': 'string',
            'fargateProfileArn': 'string',
            'clusterName': 'string',
            'createdAt': datetime(2015, 1, 1),
            'podExecutionRoleArn': 'string',
            'subnets': [
                'string',
            ],
            'selectors': [
                {
                    'namespace': 'string',
                    'labels': {
                        'string': 'string'
                    }
                },
            ],
            'status': 'CREATING'|'ACTIVE'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED',
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_nodegroup(clusterName=None, nodegroupName=None):
    """
    Returns descriptive information about an Amazon EKS node group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_nodegroup(
        clusterName='string',
        nodegroupName='string'
    )
    
    
    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the Amazon EKS cluster associated with the node group.\n

    :type nodegroupName: string
    :param nodegroupName: [REQUIRED]\nThe name of the node group to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nodegroup': {
        'nodegroupName': 'string',
        'nodegroupArn': 'string',
        'clusterName': 'string',
        'version': 'string',
        'releaseVersion': 'string',
        'createdAt': datetime(2015, 1, 1),
        'modifiedAt': datetime(2015, 1, 1),
        'status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED'|'DEGRADED',
        'scalingConfig': {
            'minSize': 123,
            'maxSize': 123,
            'desiredSize': 123
        },
        'instanceTypes': [
            'string',
        ],
        'subnets': [
            'string',
        ],
        'remoteAccess': {
            'ec2SshKey': 'string',
            'sourceSecurityGroups': [
                'string',
            ]
        },
        'amiType': 'AL2_x86_64'|'AL2_x86_64_GPU',
        'nodeRole': 'string',
        'labels': {
            'string': 'string'
        },
        'resources': {
            'autoScalingGroups': [
                {
                    'name': 'string'
                },
            ],
            'remoteAccessSecurityGroup': 'string'
        },
        'diskSize': 123,
        'health': {
            'issues': [
                {
                    'code': 'AutoScalingGroupNotFound'|'AutoScalingGroupInvalidConfiguration'|'Ec2SecurityGroupNotFound'|'Ec2SecurityGroupDeletionFailure'|'Ec2LaunchTemplateNotFound'|'Ec2LaunchTemplateVersionMismatch'|'Ec2SubnetNotFound'|'Ec2SubnetInvalidConfiguration'|'IamInstanceProfileNotFound'|'IamLimitExceeded'|'IamNodeRoleNotFound'|'NodeCreationFailure'|'AsgInstanceLaunchFailures'|'InstanceLimitExceeded'|'InsufficientFreeAddresses'|'AccessDenied'|'InternalFailure',
                    'message': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        },
        'tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

nodegroup (dict) --
The full description of your node group.

nodegroupName (string) --
The name associated with an Amazon EKS managed node group.

nodegroupArn (string) --
The Amazon Resource Name (ARN) associated with the managed node group.

clusterName (string) --
The name of the cluster that the managed node group resides in.

version (string) --
The Kubernetes version of the managed node group.

releaseVersion (string) --
The AMI version of the managed node group. For more information, see Amazon EKS-Optimized Linux AMI Versions in the Amazon EKS User Guide .

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the managed node group was created.

modifiedAt (datetime) --
The Unix epoch timestamp in seconds for when the managed node group was last modified.

status (string) --
The current status of the managed node group.

scalingConfig (dict) --
The scaling configuration details for the Auto Scaling group that is associated with your node group.

minSize (integer) --
The minimum number of worker nodes that the managed node group can scale in to. This number must be greater than zero.

maxSize (integer) --
The maximum number of worker nodes that the managed node group can scale out to. Managed node groups can support up to 100 nodes by default.

desiredSize (integer) --
The current number of worker nodes that the managed node group should maintain.



instanceTypes (list) --
The instance types associated with your node group.

(string) --


subnets (list) --
The subnets allowed for the Auto Scaling group that is associated with your node group. These subnets must have the following tag: kubernetes.io/cluster/CLUSTER_NAME , where CLUSTER_NAME is replaced with the name of your cluster.

(string) --


remoteAccess (dict) --
The remote access (SSH) configuration that is associated with the node group.

ec2SshKey (string) --
The Amazon EC2 SSH key that provides access for SSH communication with the worker nodes in the managed node group. For more information, see Amazon EC2 Key Pairs in the Amazon Elastic Compute Cloud User Guide for Linux Instances .

sourceSecurityGroups (list) --
The security groups that are allowed SSH access (port 22) to the worker nodes. If you specify an Amazon EC2 SSH key but do not specify a source security group when you create a managed node group, then port 22 on the worker nodes is opened to the internet (0.0.0.0/0). For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .

(string) --




amiType (string) --
The AMI type associated with your node group. GPU instance types should use the AL2_x86_64_GPU AMI type, which uses the Amazon EKS-optimized Linux AMI with GPU support. Non-GPU instances should use the AL2_x86_64 AMI type, which uses the Amazon EKS-optimized Linux AMI.

nodeRole (string) --
The IAM role associated with your node group. The Amazon EKS worker node kubelet daemon makes calls to AWS APIs on your behalf. Worker nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch worker nodes and register them into a cluster, you must create an IAM role for those worker nodes to use when they are launched. For more information, see Amazon EKS Worker Node IAM Role in the * Amazon EKS User Guide * .

labels (dict) --
The Kubernetes labels applied to the nodes in the node group.

Note
Only labels that are applied with the Amazon EKS API are shown here. There may be other Kubernetes labels applied to the nodes in this group.


(string) --
(string) --




resources (dict) --
The resources associated with the node group, such as Auto Scaling groups and security groups for remote access.

autoScalingGroups (list) --
The Auto Scaling groups associated with the node group.

(dict) --
An Auto Scaling group that is associated with an Amazon EKS managed node group.

name (string) --
The name of the Auto Scaling group associated with an Amazon EKS managed node group.





remoteAccessSecurityGroup (string) --
The remote access security group associated with the node group. This security group controls SSH access to the worker nodes.



diskSize (integer) --
The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB.

health (dict) --
The health status of the node group. If there are issues with your node group\'s health, they are listed here.

issues (list) --
Any issues that are associated with the node group.

(dict) --
An object representing an issue with an Amazon EKS resource.

code (string) --
A brief description of the error.

AutoScalingGroupNotFound : We couldn\'t find the Auto Scaling group associated with the managed node group. You may be able to recreate an Auto Scaling group with the same settings to recover.
Ec2SecurityGroupNotFound : We couldn\'t find the cluster security group for the cluster. You must recreate your cluster.
Ec2SecurityGroupDeletionFailure : We could not delete the remote access security group for your managed node group. Remove any dependencies from the security group.
Ec2LaunchTemplateNotFound : We couldn\'t find the Amazon EC2 launch template for your managed node group. You may be able to recreate a launch template with the same settings to recover.
Ec2LaunchTemplateVersionMismatch : The Amazon EC2 launch template version for your managed node group does not match the version that Amazon EKS created. You may be able to revert to the version that Amazon EKS created to recover.
IamInstanceProfileNotFound : We couldn\'t find the IAM instance profile for your managed node group. You may be able to recreate an instance profile with the same settings to recover.
IamNodeRoleNotFound : We couldn\'t find the IAM role for your managed node group. You may be able to recreate an IAM role with the same settings to recover.
AsgInstanceLaunchFailures : Your Auto Scaling group is experiencing failures while attempting to launch instances.
NodeCreationFailure : Your launched instances are unable to register with your Amazon EKS cluster. Common causes of this failure are insufficient worker node IAM role permissions or lack of outbound internet access for the nodes.
InstanceLimitExceeded : Your AWS account is unable to launch any more instances of the specified instance type. You may be able to request an Amazon EC2 instance limit increase to recover.
InsufficientFreeAddresses : One or more of the subnets associated with your managed node group does not have enough available IP addresses for new nodes.
AccessDenied : Amazon EKS or one or more of your managed nodes is unable to communicate with your cluster API server.
InternalFailure : These errors are usually caused by an Amazon EKS server-side issue.


message (string) --
The error message associated with the issue.

resourceIds (list) --
The AWS resources that are afflicted by this issue.

(string) --








tags (dict) --
The metadata applied to the node group to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Node group tags do not propagate to any other resources associated with the node group, such as the Amazon EC2 instances or subnets.

(string) --
(string) --












Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ResourceNotFoundException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ServiceUnavailableException


    :return: {
        'nodegroup': {
            'nodegroupName': 'string',
            'nodegroupArn': 'string',
            'clusterName': 'string',
            'version': 'string',
            'releaseVersion': 'string',
            'createdAt': datetime(2015, 1, 1),
            'modifiedAt': datetime(2015, 1, 1),
            'status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'CREATE_FAILED'|'DELETE_FAILED'|'DEGRADED',
            'scalingConfig': {
                'minSize': 123,
                'maxSize': 123,
                'desiredSize': 123
            },
            'instanceTypes': [
                'string',
            ],
            'subnets': [
                'string',
            ],
            'remoteAccess': {
                'ec2SshKey': 'string',
                'sourceSecurityGroups': [
                    'string',
                ]
            },
            'amiType': 'AL2_x86_64'|'AL2_x86_64_GPU',
            'nodeRole': 'string',
            'labels': {
                'string': 'string'
            },
            'resources': {
                'autoScalingGroups': [
                    {
                        'name': 'string'
                    },
                ],
                'remoteAccessSecurityGroup': 'string'
            },
            'diskSize': 123,
            'health': {
                'issues': [
                    {
                        'code': 'AutoScalingGroupNotFound'|'AutoScalingGroupInvalidConfiguration'|'Ec2SecurityGroupNotFound'|'Ec2SecurityGroupDeletionFailure'|'Ec2LaunchTemplateNotFound'|'Ec2LaunchTemplateVersionMismatch'|'Ec2SubnetNotFound'|'Ec2SubnetInvalidConfiguration'|'IamInstanceProfileNotFound'|'IamLimitExceeded'|'IamNodeRoleNotFound'|'NodeCreationFailure'|'AsgInstanceLaunchFailures'|'InstanceLimitExceeded'|'InsufficientFreeAddresses'|'AccessDenied'|'InternalFailure',
                        'message': 'string',
                        'resourceIds': [
                            'string',
                        ]
                    },
                ]
            },
            'tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_update(name=None, updateId=None, nodegroupName=None):
    """
    Returns descriptive information about an update against your Amazon EKS cluster or associated managed node group.
    When the status of the update is Succeeded , the update is complete. If an update fails, the status is Failed , and an error detail explains the reason for the failure.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_update(
        name='string',
        updateId='string',
        nodegroupName='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the Amazon EKS cluster associated with the update.\n

    :type updateId: string
    :param updateId: [REQUIRED]\nThe ID of the update to describe.\n

    :type nodegroupName: string
    :param nodegroupName: The name of the Amazon EKS node group associated with the update.

    :rtype: dict

ReturnsResponse Syntax
{
    'update': {
        'id': 'string',
        'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
        'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
        'params': [
            {
                'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                'value': 'string'
            },
        ],
        'createdAt': datetime(2015, 1, 1),
        'errors': [
            {
                'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                'errorMessage': 'string',
                'resourceIds': [
                    'string',
                ]
            },
        ]
    }
}


Response Structure

(dict) --

update (dict) --
The full description of the specified update.

id (string) --
A UUID that is used to track the update.

status (string) --
The current status of the update.

type (string) --
The type of the update.

params (list) --
A key-value map that contains the parameters associated with the update.

(dict) --
An object representing the details of an update request.

type (string) --
The keys associated with an update request.

value (string) --
The value of the keys submitted as part of an update request.





createdAt (datetime) --
The Unix epoch timestamp in seconds for when the update was created.

errors (list) --
Any errors associated with a Failed update.

(dict) --
An object representing an error when an asynchronous operation fails.

errorCode (string) --
A brief description of the error.

SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
EniLimitReached : You have reached the elastic network interface limit for your account.
IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
AccessDenied : You don\'t have permissions to perform the specified operation.
OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.


errorMessage (string) --
A more complete description of the error.

resourceIds (list) --
An optional field that contains the resource IDs associated with the error.

(string) --














Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ResourceNotFoundException


    :return: {
        'update': {
            'id': 'string',
            'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
            'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
            'params': [
                {
                    'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'errors': [
                {
                    'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                    'errorMessage': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
    SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
    EniLimitReached : You have reached the elastic network interface limit for your account.
    IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
    AccessDenied : You don\'t have permissions to perform the specified operation.
    OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
    VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.
    
    """
    pass

def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for

    :type Params: dict
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def list_clusters(maxResults=None, nextToken=None):
    """
    Lists the Amazon EKS clusters in your AWS account in the specified Region.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example command lists all of your available clusters in your default region.
    Expected Output:
    
    :example: response = client.list_clusters(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of cluster results returned by ListClusters in paginated output. When you use this parameter, ListClusters returns only maxResults results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListClusters request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListClusters returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListClusters request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.\n\nNote\nThis token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'clusters': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

clusters (list) --
A list of all of the clusters for your account in the specified Region.

(string) --


nextToken (string) --
The nextToken value to include in a future ListClusters request. When the results of a ListClusters request exceed maxResults , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ServiceUnavailableException

Examples
This example command lists all of your available clusters in your default region.
response = client.list_clusters(
)

print(response)


Expected Output:
{
    'clusters': [
        'devel',
        'prod',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'clusters': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_fargate_profiles(clusterName=None, maxResults=None, nextToken=None):
    """
    Lists the AWS Fargate profiles associated with the specified cluster in your AWS account in the specified Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_fargate_profiles(
        clusterName='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the Amazon EKS cluster that you would like to listFargate profiles in.\n

    :type maxResults: integer
    :param maxResults: The maximum number of Fargate profile results returned by ListFargateProfiles in paginated output. When you use this parameter, ListFargateProfiles returns only maxResults results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListFargateProfiles request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListFargateProfiles returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListFargateProfiles request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'fargateProfileNames': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

fargateProfileNames (list) --
A list of all of the Fargate profiles associated with the specified cluster.

(string) --


nextToken (string) --
The nextToken value to include in a future ListFargateProfiles request. When the results of a ListFargateProfiles request exceed maxResults , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ResourceNotFoundException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException


    :return: {
        'fargateProfileNames': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_nodegroups(clusterName=None, maxResults=None, nextToken=None):
    """
    Lists the Amazon EKS managed node groups associated with the specified cluster in your AWS account in the specified Region. Self-managed node groups are not listed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_nodegroups(
        clusterName='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the Amazon EKS cluster that you would like to list node groups in.\n

    :type maxResults: integer
    :param maxResults: The maximum number of node group results returned by ListNodegroups in paginated output. When you use this parameter, ListNodegroups returns only maxResults results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListNodegroups request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListNodegroups returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListNodegroups request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'nodegroups': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

nodegroups (list) --
A list of all of the node groups associated with the specified cluster.

(string) --


nextToken (string) --
The nextToken value to include in a future ListNodegroups request. When the results of a ListNodegroups request exceed maxResults , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ServiceUnavailableException
EKS.Client.exceptions.ResourceNotFoundException


    :return: {
        'nodegroups': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    List the tags for an Amazon EKS resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are Amazon EKS clusters and managed node groups.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --The tags for the resource.

(string) --
(string) --









Exceptions

EKS.Client.exceptions.BadRequestException
EKS.Client.exceptions.NotFoundException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    EKS.Client.exceptions.BadRequestException
    EKS.Client.exceptions.NotFoundException
    
    """
    pass

def list_updates(name=None, nodegroupName=None, nextToken=None, maxResults=None):
    """
    Lists the updates associated with an Amazon EKS cluster or managed node group in your AWS account, in the specified Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_updates(
        name='string',
        nodegroupName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the Amazon EKS cluster to list updates for.\n

    :type nodegroupName: string
    :param nodegroupName: The name of the Amazon EKS managed node group to list updates for.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListUpdates request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type maxResults: integer
    :param maxResults: The maximum number of update results returned by ListUpdates in paginated output. When you use this parameter, ListUpdates returns only maxResults results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListUpdates request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListUpdates returns up to 100 results and a nextToken value if applicable.

    :rtype: dict

ReturnsResponse Syntax
{
    'updateIds': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

updateIds (list) --
A list of all the updates for the specified cluster and Region.

(string) --


nextToken (string) --
The nextToken value to include in a future ListUpdates request. When the results of a ListUpdates request exceed maxResults , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ResourceNotFoundException


    :return: {
        'updateIds': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Associates the specified tags to a resource with the specified resourceArn . If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well. Tags that you create for Amazon EKS resources do not propagate to any other resources associated with the cluster. For example, if you tag a cluster with this operation, that tag does not automatically propagate to the subnets and worker nodes associated with the cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to which to add tags. Currently, the supported resources are Amazon EKS clusters and managed node groups.\n

    :type tags: dict
    :param tags: [REQUIRED]\nThe tags to add to the resource. A tag is an array of key-value pairs.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

EKS.Client.exceptions.BadRequestException
EKS.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Deletes specified tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource from which to delete tags. Currently, the supported resources are Amazon EKS clusters and managed node groups.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe keys of the tags to be removed.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

EKS.Client.exceptions.BadRequestException
EKS.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_cluster_config(name=None, resourcesVpcConfig=None, logging=None, clientRequestToken=None):
    """
    Updates an Amazon EKS cluster configuration. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the  DescribeUpdate API operation.
    You can use this API operation to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren\'t exported to CloudWatch Logs. For more information, see Amazon EKS Cluster Control Plane Logs in the * Amazon EKS User Guide * .
    You can also use this API operation to enable or disable public and private access to your cluster\'s Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .
    Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to UPDATING (this status transition is eventually consistent). When the update is complete (either Failed or Successful ), the cluster status moves to Active .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_cluster_config(
        name='string',
        resourcesVpcConfig={
            'subnetIds': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ],
            'endpointPublicAccess': True|False,
            'endpointPrivateAccess': True|False,
            'publicAccessCidrs': [
                'string',
            ]
        },
        logging={
            'clusterLogging': [
                {
                    'types': [
                        'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                    ],
                    'enabled': True|False
                },
            ]
        },
        clientRequestToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the Amazon EKS cluster to update.\n

    :type resourcesVpcConfig: dict
    :param resourcesVpcConfig: An object representing the VPC configuration to use for an Amazon EKS cluster.\n\nsubnetIds (list) --Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.\n\n(string) --\n\n\nsecurityGroupIds (list) --Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane. If you don\'t specify a security group, the default security group for your VPC is used.\n\n(string) --\n\n\nendpointPublicAccess (boolean) --Set this value to false to disable public access to your cluster\'s Kubernetes API server endpoint. If you disable public access, your cluster\'s Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is true , which enables public access for your Kubernetes API server. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .\n\nendpointPrivateAccess (boolean) --Set this value to true to enable private access for your cluster\'s Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster\'s VPC use the private VPC endpoint. The default value for this parameter is false , which disables private access for your Kubernetes API server. If you disable private access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that publicAccessCidrs includes the necessary CIDR blocks for communication with the worker nodes or Fargate pods. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .\n\npublicAccessCidrs (list) --The CIDR blocks that are allowed access to your cluster\'s public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is 0.0.0.0/0 . If you\'ve disabled private endpoint access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that you specify the necessary CIDR blocks. For more information, see Amazon EKS Cluster Endpoint Access Control in the * Amazon EKS User Guide * .\n\n(string) --\n\n\n\n

    :type logging: dict
    :param logging: Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren\'t exported to CloudWatch Logs. For more information, see Amazon EKS Cluster Control Plane Logs in the * Amazon EKS User Guide * .\n\nNote\nCloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see Amazon CloudWatch Pricing .\n\n\nclusterLogging (list) --The cluster control plane logging configuration for your cluster.\n\n(dict) --An object representing the enabled or disabled Kubernetes control plane logs for your cluster.\n\ntypes (list) --The available cluster control plane log types.\n\n(string) --\n\n\nenabled (boolean) --If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs. If a log type isn\'t enabled, that log type doesn\'t export its control plane logs. Each individual log type can be enabled or disabled independently.\n\n\n\n\n\n\n

    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'update': {
        'id': 'string',
        'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
        'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
        'params': [
            {
                'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                'value': 'string'
            },
        ],
        'createdAt': datetime(2015, 1, 1),
        'errors': [
            {
                'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                'errorMessage': 'string',
                'resourceIds': [
                    'string',
                ]
            },
        ]
    }
}


Response Structure

(dict) --

update (dict) --
An object representing an asynchronous update.

id (string) --
A UUID that is used to track the update.

status (string) --
The current status of the update.

type (string) --
The type of the update.

params (list) --
A key-value map that contains the parameters associated with the update.

(dict) --
An object representing the details of an update request.

type (string) --
The keys associated with an update request.

value (string) --
The value of the keys submitted as part of an update request.





createdAt (datetime) --
The Unix epoch timestamp in seconds for when the update was created.

errors (list) --
Any errors associated with a Failed update.

(dict) --
An object representing an error when an asynchronous operation fails.

errorCode (string) --
A brief description of the error.

SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
EniLimitReached : You have reached the elastic network interface limit for your account.
IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
AccessDenied : You don\'t have permissions to perform the specified operation.
OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.


errorMessage (string) --
A more complete description of the error.

resourceIds (list) --
An optional field that contains the resource IDs associated with the error.

(string) --














Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ResourceInUseException
EKS.Client.exceptions.ResourceNotFoundException
EKS.Client.exceptions.InvalidRequestException


    :return: {
        'update': {
            'id': 'string',
            'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
            'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
            'params': [
                {
                    'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'errors': [
                {
                    'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                    'errorMessage': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
    SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
    EniLimitReached : You have reached the elastic network interface limit for your account.
    IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
    AccessDenied : You don\'t have permissions to perform the specified operation.
    OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
    VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.
    
    """
    pass

def update_cluster_version(name=None, version=None, clientRequestToken=None):
    """
    Updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the  DescribeUpdate API operation.
    Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to UPDATING (this status transition is eventually consistent). When the update is complete (either Failed or Successful ), the cluster status moves to Active .
    If your cluster has managed node groups attached to it, all of your node groups\xe2\x80\x99 Kubernetes versions must match the cluster\xe2\x80\x99s Kubernetes version in order to update the cluster to a new Kubernetes version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_cluster_version(
        name='string',
        version='string',
        clientRequestToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the Amazon EKS cluster to update.\n

    :type version: string
    :param version: [REQUIRED]\nThe desired Kubernetes version following a successful update.\n

    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'update': {
        'id': 'string',
        'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
        'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
        'params': [
            {
                'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                'value': 'string'
            },
        ],
        'createdAt': datetime(2015, 1, 1),
        'errors': [
            {
                'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                'errorMessage': 'string',
                'resourceIds': [
                    'string',
                ]
            },
        ]
    }
}


Response Structure

(dict) --

update (dict) --
The full description of the specified update

id (string) --
A UUID that is used to track the update.

status (string) --
The current status of the update.

type (string) --
The type of the update.

params (list) --
A key-value map that contains the parameters associated with the update.

(dict) --
An object representing the details of an update request.

type (string) --
The keys associated with an update request.

value (string) --
The value of the keys submitted as part of an update request.





createdAt (datetime) --
The Unix epoch timestamp in seconds for when the update was created.

errors (list) --
Any errors associated with a Failed update.

(dict) --
An object representing an error when an asynchronous operation fails.

errorCode (string) --
A brief description of the error.

SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
EniLimitReached : You have reached the elastic network interface limit for your account.
IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
AccessDenied : You don\'t have permissions to perform the specified operation.
OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.


errorMessage (string) --
A more complete description of the error.

resourceIds (list) --
An optional field that contains the resource IDs associated with the error.

(string) --














Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ResourceInUseException
EKS.Client.exceptions.ResourceNotFoundException
EKS.Client.exceptions.InvalidRequestException


    :return: {
        'update': {
            'id': 'string',
            'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
            'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
            'params': [
                {
                    'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'errors': [
                {
                    'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                    'errorMessage': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
    SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
    EniLimitReached : You have reached the elastic network interface limit for your account.
    IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
    AccessDenied : You don\'t have permissions to perform the specified operation.
    OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
    VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.
    
    """
    pass

def update_nodegroup_config(clusterName=None, nodegroupName=None, labels=None, scalingConfig=None, clientRequestToken=None):
    """
    Updates an Amazon EKS managed node group configuration. Your node group continues to function during the update. The response output includes an update ID that you can use to track the status of your node group update with the  DescribeUpdate API operation. Currently you can update the Kubernetes labels for a node group or the scaling configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_nodegroup_config(
        clusterName='string',
        nodegroupName='string',
        labels={
            'addOrUpdateLabels': {
                'string': 'string'
            },
            'removeLabels': [
                'string',
            ]
        },
        scalingConfig={
            'minSize': 123,
            'maxSize': 123,
            'desiredSize': 123
        },
        clientRequestToken='string'
    )
    
    
    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the Amazon EKS cluster that the managed node group resides in.\n

    :type nodegroupName: string
    :param nodegroupName: [REQUIRED]\nThe name of the managed node group to update.\n

    :type labels: dict
    :param labels: The Kubernetes labels to be applied to the nodes in the node group after the update.\n\naddOrUpdateLabels (dict) --Kubernetes labels to be added or updated.\n\n(string) --\n(string) --\n\n\n\n\nremoveLabels (list) --Kubernetes labels to be removed.\n\n(string) --\n\n\n\n

    :type scalingConfig: dict
    :param scalingConfig: The scaling configuration details for the Auto Scaling group after the update.\n\nminSize (integer) --The minimum number of worker nodes that the managed node group can scale in to. This number must be greater than zero.\n\nmaxSize (integer) --The maximum number of worker nodes that the managed node group can scale out to. Managed node groups can support up to 100 nodes by default.\n\ndesiredSize (integer) --The current number of worker nodes that the managed node group should maintain.\n\n\n

    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'update': {
        'id': 'string',
        'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
        'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
        'params': [
            {
                'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                'value': 'string'
            },
        ],
        'createdAt': datetime(2015, 1, 1),
        'errors': [
            {
                'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                'errorMessage': 'string',
                'resourceIds': [
                    'string',
                ]
            },
        ]
    }
}


Response Structure

(dict) --

update (dict) --
An object representing an asynchronous update.

id (string) --
A UUID that is used to track the update.

status (string) --
The current status of the update.

type (string) --
The type of the update.

params (list) --
A key-value map that contains the parameters associated with the update.

(dict) --
An object representing the details of an update request.

type (string) --
The keys associated with an update request.

value (string) --
The value of the keys submitted as part of an update request.





createdAt (datetime) --
The Unix epoch timestamp in seconds for when the update was created.

errors (list) --
Any errors associated with a Failed update.

(dict) --
An object representing an error when an asynchronous operation fails.

errorCode (string) --
A brief description of the error.

SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
EniLimitReached : You have reached the elastic network interface limit for your account.
IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
AccessDenied : You don\'t have permissions to perform the specified operation.
OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.


errorMessage (string) --
A more complete description of the error.

resourceIds (list) --
An optional field that contains the resource IDs associated with the error.

(string) --














Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ResourceInUseException
EKS.Client.exceptions.ResourceNotFoundException
EKS.Client.exceptions.InvalidRequestException


    :return: {
        'update': {
            'id': 'string',
            'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
            'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
            'params': [
                {
                    'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'errors': [
                {
                    'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                    'errorMessage': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
    SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
    EniLimitReached : You have reached the elastic network interface limit for your account.
    IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
    AccessDenied : You don\'t have permissions to perform the specified operation.
    OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
    VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.
    
    """
    pass

def update_nodegroup_version(clusterName=None, nodegroupName=None, version=None, releaseVersion=None, force=None, clientRequestToken=None):
    """
    Updates the Kubernetes version or AMI version of an Amazon EKS managed node group.
    You can update to the latest available AMI version of a node group\'s current Kubernetes version by not specifying a Kubernetes version in the request. You can update to the latest AMI version of your cluster\'s current Kubernetes version by specifying your cluster\'s Kubernetes version in the request. For more information, see Amazon EKS-Optimized Linux AMI Versions in the Amazon EKS User Guide .
    You cannot roll back a node group to an earlier Kubernetes version or AMI version.
    When a node in a managed node group is terminated due to a scaling action or update, the pods in that node are drained first. Amazon EKS attempts to drain the nodes gracefully and will fail if it is unable to do so. You can force the update if Amazon EKS is unable to drain the nodes as a result of a pod disruption budget issue.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_nodegroup_version(
        clusterName='string',
        nodegroupName='string',
        version='string',
        releaseVersion='string',
        force=True|False,
        clientRequestToken='string'
    )
    
    
    :type clusterName: string
    :param clusterName: [REQUIRED]\nThe name of the Amazon EKS cluster that is associated with the managed node group to update.\n

    :type nodegroupName: string
    :param nodegroupName: [REQUIRED]\nThe name of the managed node group to update.\n

    :type version: string
    :param version: The Kubernetes version to update to. If no version is specified, then the Kubernetes version of the node group does not change. You can specify the Kubernetes version of the cluster to update the node group to the latest AMI version of the cluster\'s Kubernetes version.

    :type releaseVersion: string
    :param releaseVersion: The AMI version of the Amazon EKS-optimized AMI to use for the update. By default, the latest available AMI version for the node group\'s Kubernetes version is used. For more information, see Amazon EKS-Optimized Linux AMI Versions in the Amazon EKS User Guide .

    :type force: boolean
    :param force: Force the update if the existing node group\'s pods are unable to be drained due to a pod disruption budget issue. If an update fails because pods could not be drained, you can force the update after it fails to terminate the old node whether or not any pods are running on the node.

    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'update': {
        'id': 'string',
        'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
        'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
        'params': [
            {
                'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                'value': 'string'
            },
        ],
        'createdAt': datetime(2015, 1, 1),
        'errors': [
            {
                'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                'errorMessage': 'string',
                'resourceIds': [
                    'string',
                ]
            },
        ]
    }
}


Response Structure

(dict) --

update (dict) --
An object representing an asynchronous update.

id (string) --
A UUID that is used to track the update.

status (string) --
The current status of the update.

type (string) --
The type of the update.

params (list) --
A key-value map that contains the parameters associated with the update.

(dict) --
An object representing the details of an update request.

type (string) --
The keys associated with an update request.

value (string) --
The value of the keys submitted as part of an update request.





createdAt (datetime) --
The Unix epoch timestamp in seconds for when the update was created.

errors (list) --
Any errors associated with a Failed update.

(dict) --
An object representing an error when an asynchronous operation fails.

errorCode (string) --
A brief description of the error.

SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
EniLimitReached : You have reached the elastic network interface limit for your account.
IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
AccessDenied : You don\'t have permissions to perform the specified operation.
OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.


errorMessage (string) --
A more complete description of the error.

resourceIds (list) --
An optional field that contains the resource IDs associated with the error.

(string) --














Exceptions

EKS.Client.exceptions.InvalidParameterException
EKS.Client.exceptions.ClientException
EKS.Client.exceptions.ServerException
EKS.Client.exceptions.ResourceInUseException
EKS.Client.exceptions.ResourceNotFoundException
EKS.Client.exceptions.InvalidRequestException


    :return: {
        'update': {
            'id': 'string',
            'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
            'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate'|'ConfigUpdate',
            'params': [
                {
                    'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging'|'DesiredSize'|'LabelsToAdd'|'LabelsToRemove'|'MaxSize'|'MinSize'|'ReleaseVersion'|'PublicAccessCidrs',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'errors': [
                {
                    'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown'|'NodeCreationFailure'|'PodEvictionFailure'|'InsufficientFreeAddresses',
                    'errorMessage': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    SubnetNotFound : We couldn\'t find one of the subnets associated with the cluster.
    SecurityGroupNotFound : We couldn\'t find one of the security groups associated with the cluster.
    EniLimitReached : You have reached the elastic network interface limit for your account.
    IpNotAvailable : A subnet associated with the cluster doesn\'t have any free IP addresses.
    AccessDenied : You don\'t have permissions to perform the specified operation.
    OperationNotPermitted : The service role associated with the cluster doesn\'t have the required access permissions for Amazon EKS.
    VpcIdNotFound : We couldn\'t find the VPC associated with the cluster.
    
    """
    pass

