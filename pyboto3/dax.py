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

def create_cluster(ClusterName=None, NodeType=None, Description=None, ReplicationFactor=None, AvailabilityZones=None, SubnetGroupName=None, SecurityGroupIds=None, PreferredMaintenanceWindow=None, NotificationTopicArn=None, IamRoleArn=None, ParameterGroupName=None, Tags=None, SSESpecification=None):
    """
    Creates a DAX cluster. All nodes in the cluster run the same DAX caching software.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_cluster(
        ClusterName='string',
        NodeType='string',
        Description='string',
        ReplicationFactor=123,
        AvailabilityZones=[
            'string',
        ],
        SubnetGroupName='string',
        SecurityGroupIds=[
            'string',
        ],
        PreferredMaintenanceWindow='string',
        NotificationTopicArn='string',
        IamRoleArn='string',
        ParameterGroupName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        SSESpecification={
            'Enabled': True|False
        }
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]\nThe cluster identifier. This parameter is stored as a lowercase string.\n\nConstraints:\n\nA name must contain from 1 to 20 alphanumeric characters or hyphens.\nThe first character must be a letter.\nA name cannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type NodeType: string
    :param NodeType: [REQUIRED]\nThe compute and memory capacity of the nodes in the cluster.\n

    :type Description: string
    :param Description: A description of the cluster.

    :type ReplicationFactor: integer
    :param ReplicationFactor: [REQUIRED]\nThe number of nodes in the DAX cluster. A replication factor of 1 will create a single-node cluster, without any read replicas. For additional fault tolerance, you can create a multiple node cluster with one or more read replicas. To do this, set ReplicationFactor to a number between 3 (one primary and two read replicas) and 10 (one primary and nine read replicas). If the AvailabilityZones parameter is provided, its length must equal the ReplicationFactor .\n\nNote\nAWS recommends that you have at least two read replicas per cluster.\n\n

    :type AvailabilityZones: list
    :param AvailabilityZones: The Availability Zones (AZs) in which the cluster nodes will reside after the cluster has been created or updated. If provided, the length of this list must equal the ReplicationFactor parameter. If you omit this parameter, DAX will spread the nodes across Availability Zones for the highest availability.\n\n(string) --\n\n

    :type SubnetGroupName: string
    :param SubnetGroupName: The name of the subnet group to be used for the replication group.\n\nWarning\nDAX clusters can only run in an Amazon VPC environment. All of the subnets that you specify in a subnet group must exist in the same VPC.\n\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: A list of security group IDs to be assigned to each node in the DAX cluster. (Each of the security group ID is system-generated.)\nIf this parameter is not specified, DAX assigns the default VPC security group to each node.\n\n(string) --\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the DAX cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:\n\nsun\nmon\ntue\nwed\nthu\nfri\nsat\n\nExample: sun:05:00-sun:09:00\n\nNote\nIf you don\'t specify a preferred maintenance window when you create or modify a cache cluster, DAX assigns a 60-minute maintenance window on a randomly selected day of the week.\n\n

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent.\n\nNote\nThe Amazon SNS topic owner must be same as the DAX cluster owner.\n\n

    :type IamRoleArn: string
    :param IamRoleArn: [REQUIRED]\nA valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.\n

    :type ParameterGroupName: string
    :param ParameterGroupName: The parameter group to be associated with the DAX cluster.

    :type Tags: list
    :param Tags: A set of tags to associate with the DAX cluster.\n\n(dict) --A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.\nAWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: .\nYou cannot backdate the application of a tag.\n\nKey (string) --The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.\n\nValue (string) --The value of the tag. Tag values are case-sensitive and can be null.\n\n\n\n\n

    :type SSESpecification: dict
    :param SSESpecification: Represents the settings used to enable server-side encryption on the cluster.\n\nEnabled (boolean) -- [REQUIRED]Indicates whether server-side encryption is enabled (true) or disabled (false) on the cluster.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterName': 'string',
        'Description': 'string',
        'ClusterArn': 'string',
        'TotalNodes': 123,
        'ActiveNodes': 123,
        'NodeType': 'string',
        'Status': 'string',
        'ClusterDiscoveryEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'NodeIdsToRemove': [
            'string',
        ],
        'Nodes': [
            {
                'NodeId': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'NodeCreateTime': datetime(2015, 1, 1),
                'AvailabilityZone': 'string',
                'NodeStatus': 'string',
                'ParameterGroupStatus': 'string'
            },
        ],
        'PreferredMaintenanceWindow': 'string',
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'SubnetGroup': 'string',
        'SecurityGroups': [
            {
                'SecurityGroupIdentifier': 'string',
                'Status': 'string'
            },
        ],
        'IamRoleArn': 'string',
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'NodeIdsToReboot': [
                'string',
            ]
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
A description of the DAX cluster that you have created.

ClusterName (string) --
The name of the DAX cluster.

Description (string) --
The description of the cluster.

ClusterArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the cluster.

TotalNodes (integer) --
The total number of nodes in the cluster.

ActiveNodes (integer) --
The number of nodes in the cluster that are active (i.e., capable of serving requests).

NodeType (string) --
The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)

Status (string) --
The current status of the cluster.

ClusterDiscoveryEndpoint (dict) --
The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeIdsToRemove (list) --
A list of nodes to be removed from the cluster.

(string) --


Nodes (list) --
A list of nodes that are currently in the cluster.

(dict) --
Represents an individual node within a DAX cluster.

NodeId (string) --
A system-generated identifier for the node.

Endpoint (dict) --
The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeCreateTime (datetime) --
The date and time (in UNIX epoch format) when the node was launched.

AvailabilityZone (string) --
The Availability Zone (AZ) in which the node has been deployed.

NodeStatus (string) --
The current status of the node. For example: available .

ParameterGroupStatus (string) --
The status of the parameter group associated with this node. For example, in-sync .





PreferredMaintenanceWindow (string) --
A range of time when maintenance of DAX cluster software will be performed. For example: sun:01:00-sun:09:00 . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



SubnetGroup (string) --
The subnet group where the DAX cluster is running.

SecurityGroups (list) --
A list of security groups, and the status of each, for the nodes in the cluster.

(dict) --
An individual VPC security group and its status.

SecurityGroupIdentifier (string) --
The unique ID for this security group.

Status (string) --
The status of this security group.





IamRoleArn (string) --
A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.

ParameterGroup (dict) --
The parameter group being used by nodes in the cluster.

ParameterGroupName (string) --
The name of the parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

NodeIdsToReboot (list) --
The node IDs of one or more nodes to be rebooted.

(string) --




SSEDescription (dict) --
The description of the server-side encryption status on the specified DAX cluster.

Status (string) --
The current state of server-side encryption:

ENABLING - Server-side encryption is being enabled.
ENABLED - Server-side encryption is enabled.
DISABLING - Server-side encryption is being disabled.
DISABLED - Server-side encryption is disabled.












Exceptions

DAX.Client.exceptions.ClusterAlreadyExistsFault
DAX.Client.exceptions.InvalidClusterStateFault
DAX.Client.exceptions.InsufficientClusterCapacityFault
DAX.Client.exceptions.SubnetGroupNotFoundFault
DAX.Client.exceptions.InvalidParameterGroupStateFault
DAX.Client.exceptions.ParameterGroupNotFoundFault
DAX.Client.exceptions.ClusterQuotaForCustomerExceededFault
DAX.Client.exceptions.NodeQuotaForClusterExceededFault
DAX.Client.exceptions.NodeQuotaForCustomerExceededFault
DAX.Client.exceptions.InvalidVPCNetworkStateFault
DAX.Client.exceptions.TagQuotaPerResourceExceeded
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Cluster': {
            'ClusterName': 'string',
            'Description': 'string',
            'ClusterArn': 'string',
            'TotalNodes': 123,
            'ActiveNodes': 123,
            'NodeType': 'string',
            'Status': 'string',
            'ClusterDiscoveryEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'NodeIdsToRemove': [
                'string',
            ],
            'Nodes': [
                {
                    'NodeId': 'string',
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'NodeCreateTime': datetime(2015, 1, 1),
                    'AvailabilityZone': 'string',
                    'NodeStatus': 'string',
                    'ParameterGroupStatus': 'string'
                },
            ],
            'PreferredMaintenanceWindow': 'string',
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'SubnetGroup': 'string',
            'SecurityGroups': [
                {
                    'SecurityGroupIdentifier': 'string',
                    'Status': 'string'
                },
            ],
            'IamRoleArn': 'string',
            'ParameterGroup': {
                'ParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'NodeIdsToReboot': [
                    'string',
                ]
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_parameter_group(ParameterGroupName=None, Description=None):
    """
    Creates a new parameter group. A parameter group is a collection of parameters that you apply to all of the nodes in a DAX cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_parameter_group(
        ParameterGroupName='string',
        Description='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]\nThe name of the parameter group to apply to all of the clusters in this replication group.\n

    :type Description: string
    :param Description: A description of the parameter group.

    :rtype: dict

ReturnsResponse Syntax
{
    'ParameterGroup': {
        'ParameterGroupName': 'string',
        'Description': 'string'
    }
}


Response Structure

(dict) --

ParameterGroup (dict) --
Represents the output of a CreateParameterGroup action.

ParameterGroupName (string) --
The name of the parameter group.

Description (string) --
A description of the parameter group.









Exceptions

DAX.Client.exceptions.ParameterGroupQuotaExceededFault
DAX.Client.exceptions.ParameterGroupAlreadyExistsFault
DAX.Client.exceptions.InvalidParameterGroupStateFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'Description': 'string'
        }
    }
    
    
    :returns: 
    DAX.Client.exceptions.ParameterGroupQuotaExceededFault
    DAX.Client.exceptions.ParameterGroupAlreadyExistsFault
    DAX.Client.exceptions.InvalidParameterGroupStateFault
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    DAX.Client.exceptions.InvalidParameterValueException
    DAX.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def create_subnet_group(SubnetGroupName=None, Description=None, SubnetIds=None):
    """
    Creates a new subnet group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_subnet_group(
        SubnetGroupName='string',
        Description='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type SubnetGroupName: string
    :param SubnetGroupName: [REQUIRED]\nA name for the subnet group. This value is stored as a lowercase string.\n

    :type Description: string
    :param Description: A description for the subnet group

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nA list of VPC subnet IDs for the subnet group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SubnetGroup': {
        'SubnetGroupName': 'string',
        'Description': 'string',
        'VpcId': 'string',
        'Subnets': [
            {
                'SubnetIdentifier': 'string',
                'SubnetAvailabilityZone': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

SubnetGroup (dict) --
Represents the output of a CreateSubnetGroup operation.

SubnetGroupName (string) --
The name of the subnet group.

Description (string) --
The description of the subnet group.

VpcId (string) --
The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

Subnets (list) --
A list of subnets associated with the subnet group.

(dict) --
Represents the subnet associated with a DAX cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

SubnetIdentifier (string) --
The system-assigned identifier for the subnet.

SubnetAvailabilityZone (string) --
The Availability Zone (AZ) for the subnet.













Exceptions

DAX.Client.exceptions.SubnetGroupAlreadyExistsFault
DAX.Client.exceptions.SubnetGroupQuotaExceededFault
DAX.Client.exceptions.SubnetQuotaExceededFault
DAX.Client.exceptions.InvalidSubnet
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault


    :return: {
        'SubnetGroup': {
            'SubnetGroupName': 'string',
            'Description': 'string',
            'VpcId': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    DAX.Client.exceptions.SubnetGroupAlreadyExistsFault
    DAX.Client.exceptions.SubnetGroupQuotaExceededFault
    DAX.Client.exceptions.SubnetQuotaExceededFault
    DAX.Client.exceptions.InvalidSubnet
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    
    """
    pass

def decrease_replication_factor(ClusterName=None, NewReplicationFactor=None, AvailabilityZones=None, NodeIdsToRemove=None):
    """
    Removes one or more nodes from a DAX cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.decrease_replication_factor(
        ClusterName='string',
        NewReplicationFactor=123,
        AvailabilityZones=[
            'string',
        ],
        NodeIdsToRemove=[
            'string',
        ]
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]\nThe name of the DAX cluster from which you want to remove nodes.\n

    :type NewReplicationFactor: integer
    :param NewReplicationFactor: [REQUIRED]\nThe new number of nodes for the DAX cluster.\n

    :type AvailabilityZones: list
    :param AvailabilityZones: The Availability Zone(s) from which to remove nodes.\n\n(string) --\n\n

    :type NodeIdsToRemove: list
    :param NodeIdsToRemove: The unique identifiers of the nodes to be removed from the cluster.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterName': 'string',
        'Description': 'string',
        'ClusterArn': 'string',
        'TotalNodes': 123,
        'ActiveNodes': 123,
        'NodeType': 'string',
        'Status': 'string',
        'ClusterDiscoveryEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'NodeIdsToRemove': [
            'string',
        ],
        'Nodes': [
            {
                'NodeId': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'NodeCreateTime': datetime(2015, 1, 1),
                'AvailabilityZone': 'string',
                'NodeStatus': 'string',
                'ParameterGroupStatus': 'string'
            },
        ],
        'PreferredMaintenanceWindow': 'string',
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'SubnetGroup': 'string',
        'SecurityGroups': [
            {
                'SecurityGroupIdentifier': 'string',
                'Status': 'string'
            },
        ],
        'IamRoleArn': 'string',
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'NodeIdsToReboot': [
                'string',
            ]
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
A description of the DAX cluster, after you have decreased its replication factor.

ClusterName (string) --
The name of the DAX cluster.

Description (string) --
The description of the cluster.

ClusterArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the cluster.

TotalNodes (integer) --
The total number of nodes in the cluster.

ActiveNodes (integer) --
The number of nodes in the cluster that are active (i.e., capable of serving requests).

NodeType (string) --
The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)

Status (string) --
The current status of the cluster.

ClusterDiscoveryEndpoint (dict) --
The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeIdsToRemove (list) --
A list of nodes to be removed from the cluster.

(string) --


Nodes (list) --
A list of nodes that are currently in the cluster.

(dict) --
Represents an individual node within a DAX cluster.

NodeId (string) --
A system-generated identifier for the node.

Endpoint (dict) --
The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeCreateTime (datetime) --
The date and time (in UNIX epoch format) when the node was launched.

AvailabilityZone (string) --
The Availability Zone (AZ) in which the node has been deployed.

NodeStatus (string) --
The current status of the node. For example: available .

ParameterGroupStatus (string) --
The status of the parameter group associated with this node. For example, in-sync .





PreferredMaintenanceWindow (string) --
A range of time when maintenance of DAX cluster software will be performed. For example: sun:01:00-sun:09:00 . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



SubnetGroup (string) --
The subnet group where the DAX cluster is running.

SecurityGroups (list) --
A list of security groups, and the status of each, for the nodes in the cluster.

(dict) --
An individual VPC security group and its status.

SecurityGroupIdentifier (string) --
The unique ID for this security group.

Status (string) --
The status of this security group.





IamRoleArn (string) --
A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.

ParameterGroup (dict) --
The parameter group being used by nodes in the cluster.

ParameterGroupName (string) --
The name of the parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

NodeIdsToReboot (list) --
The node IDs of one or more nodes to be rebooted.

(string) --




SSEDescription (dict) --
The description of the server-side encryption status on the specified DAX cluster.

Status (string) --
The current state of server-side encryption:

ENABLING - Server-side encryption is being enabled.
ENABLED - Server-side encryption is enabled.
DISABLING - Server-side encryption is being disabled.
DISABLED - Server-side encryption is disabled.












Exceptions

DAX.Client.exceptions.ClusterNotFoundFault
DAX.Client.exceptions.NodeNotFoundFault
DAX.Client.exceptions.InvalidClusterStateFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Cluster': {
            'ClusterName': 'string',
            'Description': 'string',
            'ClusterArn': 'string',
            'TotalNodes': 123,
            'ActiveNodes': 123,
            'NodeType': 'string',
            'Status': 'string',
            'ClusterDiscoveryEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'NodeIdsToRemove': [
                'string',
            ],
            'Nodes': [
                {
                    'NodeId': 'string',
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'NodeCreateTime': datetime(2015, 1, 1),
                    'AvailabilityZone': 'string',
                    'NodeStatus': 'string',
                    'ParameterGroupStatus': 'string'
                },
            ],
            'PreferredMaintenanceWindow': 'string',
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'SubnetGroup': 'string',
            'SecurityGroups': [
                {
                    'SecurityGroupIdentifier': 'string',
                    'Status': 'string'
                },
            ],
            'IamRoleArn': 'string',
            'ParameterGroup': {
                'ParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'NodeIdsToReboot': [
                    'string',
                ]
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_cluster(ClusterName=None):
    """
    Deletes a previously provisioned DAX cluster. DeleteCluster deletes all associated nodes, node endpoints and the DAX cluster itself. When you receive a successful response from this action, DAX immediately begins deleting the cluster; you cannot cancel or revert this action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cluster(
        ClusterName='string'
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]\nThe name of the cluster to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Cluster': {
        'ClusterName': 'string',
        'Description': 'string',
        'ClusterArn': 'string',
        'TotalNodes': 123,
        'ActiveNodes': 123,
        'NodeType': 'string',
        'Status': 'string',
        'ClusterDiscoveryEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'NodeIdsToRemove': [
            'string',
        ],
        'Nodes': [
            {
                'NodeId': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'NodeCreateTime': datetime(2015, 1, 1),
                'AvailabilityZone': 'string',
                'NodeStatus': 'string',
                'ParameterGroupStatus': 'string'
            },
        ],
        'PreferredMaintenanceWindow': 'string',
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'SubnetGroup': 'string',
        'SecurityGroups': [
            {
                'SecurityGroupIdentifier': 'string',
                'Status': 'string'
            },
        ],
        'IamRoleArn': 'string',
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'NodeIdsToReboot': [
                'string',
            ]
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
        }
    }
}


Response Structure

(dict) --
Cluster (dict) --A description of the DAX cluster that is being deleted.

ClusterName (string) --The name of the DAX cluster.

Description (string) --The description of the cluster.

ClusterArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the cluster.

TotalNodes (integer) --The total number of nodes in the cluster.

ActiveNodes (integer) --The number of nodes in the cluster that are active (i.e., capable of serving requests).

NodeType (string) --The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)

Status (string) --The current status of the cluster.

ClusterDiscoveryEndpoint (dict) --The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --The DNS hostname of the endpoint.

Port (integer) --The port number that applications should use to connect to the endpoint.



NodeIdsToRemove (list) --A list of nodes to be removed from the cluster.

(string) --


Nodes (list) --A list of nodes that are currently in the cluster.

(dict) --Represents an individual node within a DAX cluster.

NodeId (string) --A system-generated identifier for the node.

Endpoint (dict) --The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --The DNS hostname of the endpoint.

Port (integer) --The port number that applications should use to connect to the endpoint.



NodeCreateTime (datetime) --The date and time (in UNIX epoch format) when the node was launched.

AvailabilityZone (string) --The Availability Zone (AZ) in which the node has been deployed.

NodeStatus (string) --The current status of the node. For example: available .

ParameterGroupStatus (string) --The status of the parameter group associated with this node. For example, in-sync .





PreferredMaintenanceWindow (string) --A range of time when maintenance of DAX cluster software will be performed. For example: sun:01:00-sun:09:00 . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

NotificationConfiguration (dict) --Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --The current state of the topic.



SubnetGroup (string) --The subnet group where the DAX cluster is running.

SecurityGroups (list) --A list of security groups, and the status of each, for the nodes in the cluster.

(dict) --An individual VPC security group and its status.

SecurityGroupIdentifier (string) --The unique ID for this security group.

Status (string) --The status of this security group.





IamRoleArn (string) --A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.

ParameterGroup (dict) --The parameter group being used by nodes in the cluster.

ParameterGroupName (string) --The name of the parameter group.

ParameterApplyStatus (string) --The status of parameter updates.

NodeIdsToReboot (list) --The node IDs of one or more nodes to be rebooted.

(string) --




SSEDescription (dict) --The description of the server-side encryption status on the specified DAX cluster.

Status (string) --The current state of server-side encryption:

ENABLING - Server-side encryption is being enabled.
ENABLED - Server-side encryption is enabled.
DISABLING - Server-side encryption is being disabled.
DISABLED - Server-side encryption is disabled.











Exceptions

DAX.Client.exceptions.ClusterNotFoundFault
DAX.Client.exceptions.InvalidClusterStateFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Cluster': {
            'ClusterName': 'string',
            'Description': 'string',
            'ClusterArn': 'string',
            'TotalNodes': 123,
            'ActiveNodes': 123,
            'NodeType': 'string',
            'Status': 'string',
            'ClusterDiscoveryEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'NodeIdsToRemove': [
                'string',
            ],
            'Nodes': [
                {
                    'NodeId': 'string',
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'NodeCreateTime': datetime(2015, 1, 1),
                    'AvailabilityZone': 'string',
                    'NodeStatus': 'string',
                    'ParameterGroupStatus': 'string'
                },
            ],
            'PreferredMaintenanceWindow': 'string',
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'SubnetGroup': 'string',
            'SecurityGroups': [
                {
                    'SecurityGroupIdentifier': 'string',
                    'Status': 'string'
                },
            ],
            'IamRoleArn': 'string',
            'ParameterGroup': {
                'ParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'NodeIdsToReboot': [
                    'string',
                ]
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_parameter_group(ParameterGroupName=None):
    """
    Deletes the specified parameter group. You cannot delete a parameter group if it is associated with any DAX clusters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_parameter_group(
        ParameterGroupName='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]\nThe name of the parameter group to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DeletionMessage': 'string'
}


Response Structure

(dict) --
DeletionMessage (string) --A user-specified message for this action (i.e., a reason for deleting the parameter group).






Exceptions

DAX.Client.exceptions.InvalidParameterGroupStateFault
DAX.Client.exceptions.ParameterGroupNotFoundFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'DeletionMessage': 'string'
    }
    
    
    """
    pass

def delete_subnet_group(SubnetGroupName=None):
    """
    Deletes a subnet group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_subnet_group(
        SubnetGroupName='string'
    )
    
    
    :type SubnetGroupName: string
    :param SubnetGroupName: [REQUIRED]\nThe name of the subnet group to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DeletionMessage': 'string'
}


Response Structure

(dict) --
DeletionMessage (string) --A user-specified message for this action (i.e., a reason for deleting the subnet group).






Exceptions

DAX.Client.exceptions.SubnetGroupInUseFault
DAX.Client.exceptions.SubnetGroupNotFoundFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault


    :return: {
        'DeletionMessage': 'string'
    }
    
    
    """
    pass

def describe_clusters(ClusterNames=None, MaxResults=None, NextToken=None):
    """
    Returns information about all provisioned DAX clusters if no cluster identifier is specified, or about a specific DAX cluster if a cluster identifier is supplied.
    If the cluster is in the CREATING state, only cluster level information will be displayed until all of the nodes are successfully provisioned.
    If the cluster is in the DELETING state, only cluster level information will be displayed.
    If nodes are currently being added to the DAX cluster, node endpoint information and creation time for the additional nodes will not be displayed until they are completely provisioned. When the DAX cluster state is available , the cluster is ready for use.
    If nodes are currently being removed from the DAX cluster, no endpoint information for the removed nodes is displayed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_clusters(
        ClusterNames=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ClusterNames: list
    :param ClusterNames: The names of the DAX clusters being described.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.\nThe value for MaxResults must be between 20 and 100.\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Clusters': [
        {
            'ClusterName': 'string',
            'Description': 'string',
            'ClusterArn': 'string',
            'TotalNodes': 123,
            'ActiveNodes': 123,
            'NodeType': 'string',
            'Status': 'string',
            'ClusterDiscoveryEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'NodeIdsToRemove': [
                'string',
            ],
            'Nodes': [
                {
                    'NodeId': 'string',
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'NodeCreateTime': datetime(2015, 1, 1),
                    'AvailabilityZone': 'string',
                    'NodeStatus': 'string',
                    'ParameterGroupStatus': 'string'
                },
            ],
            'PreferredMaintenanceWindow': 'string',
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'SubnetGroup': 'string',
            'SecurityGroups': [
                {
                    'SecurityGroupIdentifier': 'string',
                    'Status': 'string'
                },
            ],
            'IamRoleArn': 'string',
            'ParameterGroup': {
                'ParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'NodeIdsToReboot': [
                    'string',
                ]
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
            }
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
Provides an identifier to allow retrieval of paginated results.

Clusters (list) --
The descriptions of your DAX clusters, in response to a DescribeClusters request.

(dict) --
Contains all of the attributes of a specific DAX cluster.

ClusterName (string) --
The name of the DAX cluster.

Description (string) --
The description of the cluster.

ClusterArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the cluster.

TotalNodes (integer) --
The total number of nodes in the cluster.

ActiveNodes (integer) --
The number of nodes in the cluster that are active (i.e., capable of serving requests).

NodeType (string) --
The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)

Status (string) --
The current status of the cluster.

ClusterDiscoveryEndpoint (dict) --
The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeIdsToRemove (list) --
A list of nodes to be removed from the cluster.

(string) --


Nodes (list) --
A list of nodes that are currently in the cluster.

(dict) --
Represents an individual node within a DAX cluster.

NodeId (string) --
A system-generated identifier for the node.

Endpoint (dict) --
The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeCreateTime (datetime) --
The date and time (in UNIX epoch format) when the node was launched.

AvailabilityZone (string) --
The Availability Zone (AZ) in which the node has been deployed.

NodeStatus (string) --
The current status of the node. For example: available .

ParameterGroupStatus (string) --
The status of the parameter group associated with this node. For example, in-sync .





PreferredMaintenanceWindow (string) --
A range of time when maintenance of DAX cluster software will be performed. For example: sun:01:00-sun:09:00 . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



SubnetGroup (string) --
The subnet group where the DAX cluster is running.

SecurityGroups (list) --
A list of security groups, and the status of each, for the nodes in the cluster.

(dict) --
An individual VPC security group and its status.

SecurityGroupIdentifier (string) --
The unique ID for this security group.

Status (string) --
The status of this security group.





IamRoleArn (string) --
A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.

ParameterGroup (dict) --
The parameter group being used by nodes in the cluster.

ParameterGroupName (string) --
The name of the parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

NodeIdsToReboot (list) --
The node IDs of one or more nodes to be rebooted.

(string) --




SSEDescription (dict) --
The description of the server-side encryption status on the specified DAX cluster.

Status (string) --
The current state of server-side encryption:

ENABLING - Server-side encryption is being enabled.
ENABLED - Server-side encryption is enabled.
DISABLING - Server-side encryption is being disabled.
DISABLED - Server-side encryption is disabled.














Exceptions

DAX.Client.exceptions.ClusterNotFoundFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'NextToken': 'string',
        'Clusters': [
            {
                'ClusterName': 'string',
                'Description': 'string',
                'ClusterArn': 'string',
                'TotalNodes': 123,
                'ActiveNodes': 123,
                'NodeType': 'string',
                'Status': 'string',
                'ClusterDiscoveryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'NodeIdsToRemove': [
                    'string',
                ],
                'Nodes': [
                    {
                        'NodeId': 'string',
                        'Endpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'NodeCreateTime': datetime(2015, 1, 1),
                        'AvailabilityZone': 'string',
                        'NodeStatus': 'string',
                        'ParameterGroupStatus': 'string'
                    },
                ],
                'PreferredMaintenanceWindow': 'string',
                'NotificationConfiguration': {
                    'TopicArn': 'string',
                    'TopicStatus': 'string'
                },
                'SubnetGroup': 'string',
                'SecurityGroups': [
                    {
                        'SecurityGroupIdentifier': 'string',
                        'Status': 'string'
                    },
                ],
                'IamRoleArn': 'string',
                'ParameterGroup': {
                    'ParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'NodeIdsToReboot': [
                        'string',
                    ]
                },
                'SSEDescription': {
                    'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_default_parameters(MaxResults=None, NextToken=None):
    """
    Returns the default system parameter information for the DAX caching software.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_default_parameters(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.\nThe value for MaxResults must be between 20 and 100.\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Parameters': [
        {
            'ParameterName': 'string',
            'ParameterType': 'DEFAULT'|'NODE_TYPE_SPECIFIC',
            'ParameterValue': 'string',
            'NodeTypeSpecificValues': [
                {
                    'NodeType': 'string',
                    'Value': 'string'
                },
            ],
            'Description': 'string',
            'Source': 'string',
            'DataType': 'string',
            'AllowedValues': 'string',
            'IsModifiable': 'TRUE'|'FALSE'|'CONDITIONAL',
            'ChangeType': 'IMMEDIATE'|'REQUIRES_REBOOT'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
Provides an identifier to allow retrieval of paginated results.

Parameters (list) --
A list of parameters. Each element in the list represents one parameter.

(dict) --
Describes an individual setting that controls some aspect of DAX behavior.

ParameterName (string) --
The name of the parameter.

ParameterType (string) --
Determines whether the parameter can be applied to any nodes, or only nodes of a particular type.

ParameterValue (string) --
The value for the parameter.

NodeTypeSpecificValues (list) --
A list of node types, and specific parameter values for each node.

(dict) --
Represents a parameter value that is applicable to a particular node type.

NodeType (string) --
A node type to which the parameter value applies.

Value (string) --
The parameter value for this node type.





Description (string) --
A description of the parameter

Source (string) --
How the parameter is defined. For example, system denotes a system-defined parameter.

DataType (string) --
The data type of the parameter. For example, integer :

AllowedValues (string) --
A range of values within which the parameter can be set.

IsModifiable (string) --
Whether the customer is allowed to modify the parameter.

ChangeType (string) --
The conditions under which changes to this parameter can be applied. For example, requires-reboot indicates that a new value for this parameter will only take effect if a node is rebooted.











Exceptions

DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'NextToken': 'string',
        'Parameters': [
            {
                'ParameterName': 'string',
                'ParameterType': 'DEFAULT'|'NODE_TYPE_SPECIFIC',
                'ParameterValue': 'string',
                'NodeTypeSpecificValues': [
                    {
                        'NodeType': 'string',
                        'Value': 'string'
                    },
                ],
                'Description': 'string',
                'Source': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': 'TRUE'|'FALSE'|'CONDITIONAL',
                'ChangeType': 'IMMEDIATE'|'REQUIRES_REBOOT'
            },
        ]
    }
    
    
    :returns: 
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    DAX.Client.exceptions.InvalidParameterValueException
    DAX.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_events(SourceName=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, MaxResults=None, NextToken=None):
    """
    Returns events related to DAX clusters and parameter groups. You can obtain events specific to a particular DAX cluster or parameter group by providing the name as a parameter.
    By default, only the events occurring within the last 24 hours are returned; however, you can retrieve up to 14 days\' worth of events if necessary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_events(
        SourceName='string',
        SourceType='CLUSTER'|'PARAMETER_GROUP'|'SUBNET_GROUP',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Duration=123,
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type SourceName: string
    :param SourceName: The identifier of the event source for which events will be returned. If not specified, then all sources are included in the response.

    :type SourceType: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.

    :type StartTime: datetime
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format.

    :type EndTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format.

    :type Duration: integer
    :param Duration: The number of minutes\' worth of events to retrieve.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.\nThe value for MaxResults must be between 20 and 100.\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Events': [
        {
            'SourceName': 'string',
            'SourceType': 'CLUSTER'|'PARAMETER_GROUP'|'SUBNET_GROUP',
            'Message': 'string',
            'Date': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
Provides an identifier to allow retrieval of paginated results.

Events (list) --
An array of events. Each element in the array represents one event.

(dict) --
Represents a single occurrence of something interesting within the system. Some examples of events are creating a DAX cluster, adding or removing a node, or rebooting a node.

SourceName (string) --
The source of the event. For example, if the event occurred at the node level, the source would be the node ID.

SourceType (string) --
Specifies the origin of this event - a cluster, a parameter group, a node ID, etc.

Message (string) --
A user-defined message associated with the event.

Date (datetime) --
The date and time when the event occurred.











Exceptions

DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'NextToken': 'string',
        'Events': [
            {
                'SourceName': 'string',
                'SourceType': 'CLUSTER'|'PARAMETER_GROUP'|'SUBNET_GROUP',
                'Message': 'string',
                'Date': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    DAX.Client.exceptions.InvalidParameterValueException
    DAX.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_parameter_groups(ParameterGroupNames=None, MaxResults=None, NextToken=None):
    """
    Returns a list of parameter group descriptions. If a parameter group name is specified, the list will contain only the descriptions for that group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_parameter_groups(
        ParameterGroupNames=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ParameterGroupNames: list
    :param ParameterGroupNames: The names of the parameter groups.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.\nThe value for MaxResults must be between 20 and 100.\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'ParameterGroups': [
        {
            'ParameterGroupName': 'string',
            'Description': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
Provides an identifier to allow retrieval of paginated results.

ParameterGroups (list) --
An array of parameter groups. Each element in the array represents one parameter group.

(dict) --
A named set of parameters that are applied to all of the nodes in a DAX cluster.

ParameterGroupName (string) --
The name of the parameter group.

Description (string) --
A description of the parameter group.











Exceptions

DAX.Client.exceptions.ParameterGroupNotFoundFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'NextToken': 'string',
        'ParameterGroups': [
            {
                'ParameterGroupName': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    :returns: 
    DAX.Client.exceptions.ParameterGroupNotFoundFault
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    DAX.Client.exceptions.InvalidParameterValueException
    DAX.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_parameters(ParameterGroupName=None, Source=None, MaxResults=None, NextToken=None):
    """
    Returns the detailed parameter list for a particular parameter group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_parameters(
        ParameterGroupName='string',
        Source='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]\nThe name of the parameter group.\n

    :type Source: string
    :param Source: How the parameter is defined. For example, system denotes a system-defined parameter.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.\nThe value for MaxResults must be between 20 and 100.\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Parameters': [
        {
            'ParameterName': 'string',
            'ParameterType': 'DEFAULT'|'NODE_TYPE_SPECIFIC',
            'ParameterValue': 'string',
            'NodeTypeSpecificValues': [
                {
                    'NodeType': 'string',
                    'Value': 'string'
                },
            ],
            'Description': 'string',
            'Source': 'string',
            'DataType': 'string',
            'AllowedValues': 'string',
            'IsModifiable': 'TRUE'|'FALSE'|'CONDITIONAL',
            'ChangeType': 'IMMEDIATE'|'REQUIRES_REBOOT'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
Provides an identifier to allow retrieval of paginated results.

Parameters (list) --
A list of parameters within a parameter group. Each element in the list represents one parameter.

(dict) --
Describes an individual setting that controls some aspect of DAX behavior.

ParameterName (string) --
The name of the parameter.

ParameterType (string) --
Determines whether the parameter can be applied to any nodes, or only nodes of a particular type.

ParameterValue (string) --
The value for the parameter.

NodeTypeSpecificValues (list) --
A list of node types, and specific parameter values for each node.

(dict) --
Represents a parameter value that is applicable to a particular node type.

NodeType (string) --
A node type to which the parameter value applies.

Value (string) --
The parameter value for this node type.





Description (string) --
A description of the parameter

Source (string) --
How the parameter is defined. For example, system denotes a system-defined parameter.

DataType (string) --
The data type of the parameter. For example, integer :

AllowedValues (string) --
A range of values within which the parameter can be set.

IsModifiable (string) --
Whether the customer is allowed to modify the parameter.

ChangeType (string) --
The conditions under which changes to this parameter can be applied. For example, requires-reboot indicates that a new value for this parameter will only take effect if a node is rebooted.











Exceptions

DAX.Client.exceptions.ParameterGroupNotFoundFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'NextToken': 'string',
        'Parameters': [
            {
                'ParameterName': 'string',
                'ParameterType': 'DEFAULT'|'NODE_TYPE_SPECIFIC',
                'ParameterValue': 'string',
                'NodeTypeSpecificValues': [
                    {
                        'NodeType': 'string',
                        'Value': 'string'
                    },
                ],
                'Description': 'string',
                'Source': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': 'TRUE'|'FALSE'|'CONDITIONAL',
                'ChangeType': 'IMMEDIATE'|'REQUIRES_REBOOT'
            },
        ]
    }
    
    
    :returns: 
    DAX.Client.exceptions.ParameterGroupNotFoundFault
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    DAX.Client.exceptions.InvalidParameterValueException
    DAX.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_subnet_groups(SubnetGroupNames=None, MaxResults=None, NextToken=None):
    """
    Returns a list of subnet group descriptions. If a subnet group name is specified, the list will contain only the description of that group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_subnet_groups(
        SubnetGroupNames=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type SubnetGroupNames: list
    :param SubnetGroupNames: The name of the subnet group.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.\nThe value for MaxResults must be between 20 and 100.\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'SubnetGroups': [
        {
            'SubnetGroupName': 'string',
            'Description': 'string',
            'VpcId': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
Provides an identifier to allow retrieval of paginated results.

SubnetGroups (list) --
An array of subnet groups. Each element in the array represents a single subnet group.

(dict) --
Represents the output of one of the following actions:

CreateSubnetGroup
ModifySubnetGroup


SubnetGroupName (string) --
The name of the subnet group.

Description (string) --
The description of the subnet group.

VpcId (string) --
The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

Subnets (list) --
A list of subnets associated with the subnet group.

(dict) --
Represents the subnet associated with a DAX cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

SubnetIdentifier (string) --
The system-assigned identifier for the subnet.

SubnetAvailabilityZone (string) --
The Availability Zone (AZ) for the subnet.















Exceptions

DAX.Client.exceptions.SubnetGroupNotFoundFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault


    :return: {
        'NextToken': 'string',
        'SubnetGroups': [
            {
                'SubnetGroupName': 'string',
                'Description': 'string',
                'VpcId': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    CreateSubnetGroup
    ModifySubnetGroup
    
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

def increase_replication_factor(ClusterName=None, NewReplicationFactor=None, AvailabilityZones=None):
    """
    Adds one or more nodes to a DAX cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.increase_replication_factor(
        ClusterName='string',
        NewReplicationFactor=123,
        AvailabilityZones=[
            'string',
        ]
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]\nThe name of the DAX cluster that will receive additional nodes.\n

    :type NewReplicationFactor: integer
    :param NewReplicationFactor: [REQUIRED]\nThe new number of nodes for the DAX cluster.\n

    :type AvailabilityZones: list
    :param AvailabilityZones: The Availability Zones (AZs) in which the cluster nodes will be created. All nodes belonging to the cluster are placed in these Availability Zones. Use this parameter if you want to distribute the nodes across multiple AZs.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterName': 'string',
        'Description': 'string',
        'ClusterArn': 'string',
        'TotalNodes': 123,
        'ActiveNodes': 123,
        'NodeType': 'string',
        'Status': 'string',
        'ClusterDiscoveryEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'NodeIdsToRemove': [
            'string',
        ],
        'Nodes': [
            {
                'NodeId': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'NodeCreateTime': datetime(2015, 1, 1),
                'AvailabilityZone': 'string',
                'NodeStatus': 'string',
                'ParameterGroupStatus': 'string'
            },
        ],
        'PreferredMaintenanceWindow': 'string',
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'SubnetGroup': 'string',
        'SecurityGroups': [
            {
                'SecurityGroupIdentifier': 'string',
                'Status': 'string'
            },
        ],
        'IamRoleArn': 'string',
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'NodeIdsToReboot': [
                'string',
            ]
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
A description of the DAX cluster. with its new replication factor.

ClusterName (string) --
The name of the DAX cluster.

Description (string) --
The description of the cluster.

ClusterArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the cluster.

TotalNodes (integer) --
The total number of nodes in the cluster.

ActiveNodes (integer) --
The number of nodes in the cluster that are active (i.e., capable of serving requests).

NodeType (string) --
The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)

Status (string) --
The current status of the cluster.

ClusterDiscoveryEndpoint (dict) --
The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeIdsToRemove (list) --
A list of nodes to be removed from the cluster.

(string) --


Nodes (list) --
A list of nodes that are currently in the cluster.

(dict) --
Represents an individual node within a DAX cluster.

NodeId (string) --
A system-generated identifier for the node.

Endpoint (dict) --
The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeCreateTime (datetime) --
The date and time (in UNIX epoch format) when the node was launched.

AvailabilityZone (string) --
The Availability Zone (AZ) in which the node has been deployed.

NodeStatus (string) --
The current status of the node. For example: available .

ParameterGroupStatus (string) --
The status of the parameter group associated with this node. For example, in-sync .





PreferredMaintenanceWindow (string) --
A range of time when maintenance of DAX cluster software will be performed. For example: sun:01:00-sun:09:00 . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



SubnetGroup (string) --
The subnet group where the DAX cluster is running.

SecurityGroups (list) --
A list of security groups, and the status of each, for the nodes in the cluster.

(dict) --
An individual VPC security group and its status.

SecurityGroupIdentifier (string) --
The unique ID for this security group.

Status (string) --
The status of this security group.





IamRoleArn (string) --
A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.

ParameterGroup (dict) --
The parameter group being used by nodes in the cluster.

ParameterGroupName (string) --
The name of the parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

NodeIdsToReboot (list) --
The node IDs of one or more nodes to be rebooted.

(string) --




SSEDescription (dict) --
The description of the server-side encryption status on the specified DAX cluster.

Status (string) --
The current state of server-side encryption:

ENABLING - Server-side encryption is being enabled.
ENABLED - Server-side encryption is enabled.
DISABLING - Server-side encryption is being disabled.
DISABLED - Server-side encryption is disabled.












Exceptions

DAX.Client.exceptions.ClusterNotFoundFault
DAX.Client.exceptions.InvalidClusterStateFault
DAX.Client.exceptions.InsufficientClusterCapacityFault
DAX.Client.exceptions.InvalidVPCNetworkStateFault
DAX.Client.exceptions.NodeQuotaForClusterExceededFault
DAX.Client.exceptions.NodeQuotaForCustomerExceededFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Cluster': {
            'ClusterName': 'string',
            'Description': 'string',
            'ClusterArn': 'string',
            'TotalNodes': 123,
            'ActiveNodes': 123,
            'NodeType': 'string',
            'Status': 'string',
            'ClusterDiscoveryEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'NodeIdsToRemove': [
                'string',
            ],
            'Nodes': [
                {
                    'NodeId': 'string',
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'NodeCreateTime': datetime(2015, 1, 1),
                    'AvailabilityZone': 'string',
                    'NodeStatus': 'string',
                    'ParameterGroupStatus': 'string'
                },
            ],
            'PreferredMaintenanceWindow': 'string',
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'SubnetGroup': 'string',
            'SecurityGroups': [
                {
                    'SecurityGroupIdentifier': 'string',
                    'Status': 'string'
                },
            ],
            'IamRoleArn': 'string',
            'ParameterGroup': {
                'ParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'NodeIdsToReboot': [
                    'string',
                ]
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags(ResourceName=None, NextToken=None):
    """
    List all of the tags for a DAX cluster. You can call ListTags up to 10 times per second, per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags(
        ResourceName='string',
        NextToken='string'
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe name of the DAX resource to which the tags belong.\n

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
A list of tags currently associated with the DAX cluster.

(dict) --
A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
AWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: .
You cannot backdate the application of a tag.

Key (string) --
The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.

Value (string) --
The value of the tag. Tag values are case-sensitive and can be null.





NextToken (string) --
If this value is present, there are additional results to be displayed. To retrieve them, call ListTags again, with NextToken set to this value.







Exceptions

DAX.Client.exceptions.ClusterNotFoundFault
DAX.Client.exceptions.InvalidARNFault
DAX.Client.exceptions.InvalidClusterStateFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DAX.Client.exceptions.ClusterNotFoundFault
    DAX.Client.exceptions.InvalidARNFault
    DAX.Client.exceptions.InvalidClusterStateFault
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    DAX.Client.exceptions.InvalidParameterValueException
    DAX.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def reboot_node(ClusterName=None, NodeId=None):
    """
    Reboots a single node of a DAX cluster. The reboot action takes place as soon as possible. During the reboot, the node status is set to REBOOTING.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reboot_node(
        ClusterName='string',
        NodeId='string'
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]\nThe name of the DAX cluster containing the node to be rebooted.\n

    :type NodeId: string
    :param NodeId: [REQUIRED]\nThe system-assigned ID of the node to be rebooted.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterName': 'string',
        'Description': 'string',
        'ClusterArn': 'string',
        'TotalNodes': 123,
        'ActiveNodes': 123,
        'NodeType': 'string',
        'Status': 'string',
        'ClusterDiscoveryEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'NodeIdsToRemove': [
            'string',
        ],
        'Nodes': [
            {
                'NodeId': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'NodeCreateTime': datetime(2015, 1, 1),
                'AvailabilityZone': 'string',
                'NodeStatus': 'string',
                'ParameterGroupStatus': 'string'
            },
        ],
        'PreferredMaintenanceWindow': 'string',
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'SubnetGroup': 'string',
        'SecurityGroups': [
            {
                'SecurityGroupIdentifier': 'string',
                'Status': 'string'
            },
        ],
        'IamRoleArn': 'string',
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'NodeIdsToReboot': [
                'string',
            ]
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
A description of the DAX cluster after a node has been rebooted.

ClusterName (string) --
The name of the DAX cluster.

Description (string) --
The description of the cluster.

ClusterArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the cluster.

TotalNodes (integer) --
The total number of nodes in the cluster.

ActiveNodes (integer) --
The number of nodes in the cluster that are active (i.e., capable of serving requests).

NodeType (string) --
The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)

Status (string) --
The current status of the cluster.

ClusterDiscoveryEndpoint (dict) --
The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeIdsToRemove (list) --
A list of nodes to be removed from the cluster.

(string) --


Nodes (list) --
A list of nodes that are currently in the cluster.

(dict) --
Represents an individual node within a DAX cluster.

NodeId (string) --
A system-generated identifier for the node.

Endpoint (dict) --
The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeCreateTime (datetime) --
The date and time (in UNIX epoch format) when the node was launched.

AvailabilityZone (string) --
The Availability Zone (AZ) in which the node has been deployed.

NodeStatus (string) --
The current status of the node. For example: available .

ParameterGroupStatus (string) --
The status of the parameter group associated with this node. For example, in-sync .





PreferredMaintenanceWindow (string) --
A range of time when maintenance of DAX cluster software will be performed. For example: sun:01:00-sun:09:00 . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



SubnetGroup (string) --
The subnet group where the DAX cluster is running.

SecurityGroups (list) --
A list of security groups, and the status of each, for the nodes in the cluster.

(dict) --
An individual VPC security group and its status.

SecurityGroupIdentifier (string) --
The unique ID for this security group.

Status (string) --
The status of this security group.





IamRoleArn (string) --
A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.

ParameterGroup (dict) --
The parameter group being used by nodes in the cluster.

ParameterGroupName (string) --
The name of the parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

NodeIdsToReboot (list) --
The node IDs of one or more nodes to be rebooted.

(string) --




SSEDescription (dict) --
The description of the server-side encryption status on the specified DAX cluster.

Status (string) --
The current state of server-side encryption:

ENABLING - Server-side encryption is being enabled.
ENABLED - Server-side encryption is enabled.
DISABLING - Server-side encryption is being disabled.
DISABLED - Server-side encryption is disabled.












Exceptions

DAX.Client.exceptions.ClusterNotFoundFault
DAX.Client.exceptions.NodeNotFoundFault
DAX.Client.exceptions.InvalidClusterStateFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Cluster': {
            'ClusterName': 'string',
            'Description': 'string',
            'ClusterArn': 'string',
            'TotalNodes': 123,
            'ActiveNodes': 123,
            'NodeType': 'string',
            'Status': 'string',
            'ClusterDiscoveryEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'NodeIdsToRemove': [
                'string',
            ],
            'Nodes': [
                {
                    'NodeId': 'string',
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'NodeCreateTime': datetime(2015, 1, 1),
                    'AvailabilityZone': 'string',
                    'NodeStatus': 'string',
                    'ParameterGroupStatus': 'string'
                },
            ],
            'PreferredMaintenanceWindow': 'string',
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'SubnetGroup': 'string',
            'SecurityGroups': [
                {
                    'SecurityGroupIdentifier': 'string',
                    'Status': 'string'
                },
            ],
            'IamRoleArn': 'string',
            'ParameterGroup': {
                'ParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'NodeIdsToReboot': [
                    'string',
                ]
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def tag_resource(ResourceName=None, Tags=None):
    """
    Associates a set of tags with a DAX resource. You can call TagResource up to 5 times per second, per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe name of the DAX resource to which tags should be added.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to be assigned to the DAX resource.\n\n(dict) --A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.\nAWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: .\nYou cannot backdate the application of a tag.\n\nKey (string) --The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.\n\nValue (string) --The value of the tag. Tag values are case-sensitive and can be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

Tags (list) --
The list of tags that are associated with the DAX resource.

(dict) --
A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
AWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: .
You cannot backdate the application of a tag.

Key (string) --
The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.

Value (string) --
The value of the tag. Tag values are case-sensitive and can be null.











Exceptions

DAX.Client.exceptions.ClusterNotFoundFault
DAX.Client.exceptions.TagQuotaPerResourceExceeded
DAX.Client.exceptions.InvalidARNFault
DAX.Client.exceptions.InvalidClusterStateFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    DAX.Client.exceptions.ClusterNotFoundFault
    DAX.Client.exceptions.TagQuotaPerResourceExceeded
    DAX.Client.exceptions.InvalidARNFault
    DAX.Client.exceptions.InvalidClusterStateFault
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    DAX.Client.exceptions.InvalidParameterValueException
    DAX.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def untag_resource(ResourceName=None, TagKeys=None):
    """
    Removes the association of tags from a DAX resource. You can call UntagResource up to 5 times per second, per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe name of the DAX resource from which the tags should be removed.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of tag keys. If the DAX cluster has any tags with these keys, then the tags are removed from the cluster.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

Tags (list) --
The tag keys that have been removed from the cluster.

(dict) --
A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
AWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: .
You cannot backdate the application of a tag.

Key (string) --
The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.

Value (string) --
The value of the tag. Tag values are case-sensitive and can be null.











Exceptions

DAX.Client.exceptions.ClusterNotFoundFault
DAX.Client.exceptions.InvalidARNFault
DAX.Client.exceptions.TagNotFoundFault
DAX.Client.exceptions.InvalidClusterStateFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    DAX.Client.exceptions.ClusterNotFoundFault
    DAX.Client.exceptions.InvalidARNFault
    DAX.Client.exceptions.TagNotFoundFault
    DAX.Client.exceptions.InvalidClusterStateFault
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    DAX.Client.exceptions.InvalidParameterValueException
    DAX.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def update_cluster(ClusterName=None, Description=None, PreferredMaintenanceWindow=None, NotificationTopicArn=None, NotificationTopicStatus=None, ParameterGroupName=None, SecurityGroupIds=None):
    """
    Modifies the settings for a DAX cluster. You can use this action to change one or more cluster configuration parameters by specifying the parameters and the new values.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_cluster(
        ClusterName='string',
        Description='string',
        PreferredMaintenanceWindow='string',
        NotificationTopicArn='string',
        NotificationTopicStatus='string',
        ParameterGroupName='string',
        SecurityGroupIds=[
            'string',
        ]
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]\nThe name of the DAX cluster to be modified.\n

    :type Description: string
    :param Description: A description of the changes being made to the cluster.

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: A range of time when maintenance of DAX cluster software will be performed. For example: sun:01:00-sun:09:00 . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) that identifies the topic.

    :type NotificationTopicStatus: string
    :param NotificationTopicStatus: The current state of the topic.

    :type ParameterGroupName: string
    :param ParameterGroupName: The name of a parameter group for this cluster.

    :type SecurityGroupIds: list
    :param SecurityGroupIds: A list of user-specified security group IDs to be assigned to each node in the DAX cluster. If this parameter is not specified, DAX assigns the default VPC security group to each node.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterName': 'string',
        'Description': 'string',
        'ClusterArn': 'string',
        'TotalNodes': 123,
        'ActiveNodes': 123,
        'NodeType': 'string',
        'Status': 'string',
        'ClusterDiscoveryEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'NodeIdsToRemove': [
            'string',
        ],
        'Nodes': [
            {
                'NodeId': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'NodeCreateTime': datetime(2015, 1, 1),
                'AvailabilityZone': 'string',
                'NodeStatus': 'string',
                'ParameterGroupStatus': 'string'
            },
        ],
        'PreferredMaintenanceWindow': 'string',
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'SubnetGroup': 'string',
        'SecurityGroups': [
            {
                'SecurityGroupIdentifier': 'string',
                'Status': 'string'
            },
        ],
        'IamRoleArn': 'string',
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'NodeIdsToReboot': [
                'string',
            ]
        },
        'SSEDescription': {
            'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
A description of the DAX cluster, after it has been modified.

ClusterName (string) --
The name of the DAX cluster.

Description (string) --
The description of the cluster.

ClusterArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the cluster.

TotalNodes (integer) --
The total number of nodes in the cluster.

ActiveNodes (integer) --
The number of nodes in the cluster that are active (i.e., capable of serving requests).

NodeType (string) --
The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)

Status (string) --
The current status of the cluster.

ClusterDiscoveryEndpoint (dict) --
The configuration endpoint for this DAX cluster, consisting of a DNS name and a port number. Client applications can specify this endpoint, rather than an individual node endpoint, and allow the DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeIdsToRemove (list) --
A list of nodes to be removed from the cluster.

(string) --


Nodes (list) --
A list of nodes that are currently in the cluster.

(dict) --
Represents an individual node within a DAX cluster.

NodeId (string) --
A system-generated identifier for the node.

Endpoint (dict) --
The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address (string) --
The DNS hostname of the endpoint.

Port (integer) --
The port number that applications should use to connect to the endpoint.



NodeCreateTime (datetime) --
The date and time (in UNIX epoch format) when the node was launched.

AvailabilityZone (string) --
The Availability Zone (AZ) in which the node has been deployed.

NodeStatus (string) --
The current status of the node. For example: available .

ParameterGroupStatus (string) --
The status of the parameter group associated with this node. For example, in-sync .





PreferredMaintenanceWindow (string) --
A range of time when maintenance of DAX cluster software will be performed. For example: sun:01:00-sun:09:00 . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



SubnetGroup (string) --
The subnet group where the DAX cluster is running.

SecurityGroups (list) --
A list of security groups, and the status of each, for the nodes in the cluster.

(dict) --
An individual VPC security group and its status.

SecurityGroupIdentifier (string) --
The unique ID for this security group.

Status (string) --
The status of this security group.





IamRoleArn (string) --
A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role\'s permissions to access DynamoDB on your behalf.

ParameterGroup (dict) --
The parameter group being used by nodes in the cluster.

ParameterGroupName (string) --
The name of the parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

NodeIdsToReboot (list) --
The node IDs of one or more nodes to be rebooted.

(string) --




SSEDescription (dict) --
The description of the server-side encryption status on the specified DAX cluster.

Status (string) --
The current state of server-side encryption:

ENABLING - Server-side encryption is being enabled.
ENABLED - Server-side encryption is enabled.
DISABLING - Server-side encryption is being disabled.
DISABLED - Server-side encryption is disabled.












Exceptions

DAX.Client.exceptions.InvalidClusterStateFault
DAX.Client.exceptions.ClusterNotFoundFault
DAX.Client.exceptions.InvalidParameterGroupStateFault
DAX.Client.exceptions.ParameterGroupNotFoundFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Cluster': {
            'ClusterName': 'string',
            'Description': 'string',
            'ClusterArn': 'string',
            'TotalNodes': 123,
            'ActiveNodes': 123,
            'NodeType': 'string',
            'Status': 'string',
            'ClusterDiscoveryEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'NodeIdsToRemove': [
                'string',
            ],
            'Nodes': [
                {
                    'NodeId': 'string',
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'NodeCreateTime': datetime(2015, 1, 1),
                    'AvailabilityZone': 'string',
                    'NodeStatus': 'string',
                    'ParameterGroupStatus': 'string'
                },
            ],
            'PreferredMaintenanceWindow': 'string',
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'SubnetGroup': 'string',
            'SecurityGroups': [
                {
                    'SecurityGroupIdentifier': 'string',
                    'Status': 'string'
                },
            ],
            'IamRoleArn': 'string',
            'ParameterGroup': {
                'ParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'NodeIdsToReboot': [
                    'string',
                ]
            },
            'SSEDescription': {
                'Status': 'ENABLING'|'ENABLED'|'DISABLING'|'DISABLED'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_parameter_group(ParameterGroupName=None, ParameterNameValues=None):
    """
    Modifies the parameters of a parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_parameter_group(
        ParameterGroupName='string',
        ParameterNameValues=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string'
            },
        ]
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]\nThe name of the parameter group.\n

    :type ParameterNameValues: list
    :param ParameterNameValues: [REQUIRED]\nAn array of name-value pairs for the parameters in the group. Each element in the array represents a single parameter.\n\n(dict) --An individual DAX parameter.\n\nParameterName (string) --The name of the parameter.\n\nParameterValue (string) --The value of the parameter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ParameterGroup': {
        'ParameterGroupName': 'string',
        'Description': 'string'
    }
}


Response Structure

(dict) --

ParameterGroup (dict) --
The parameter group that has been modified.

ParameterGroupName (string) --
The name of the parameter group.

Description (string) --
A description of the parameter group.









Exceptions

DAX.Client.exceptions.InvalidParameterGroupStateFault
DAX.Client.exceptions.ParameterGroupNotFoundFault
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
DAX.Client.exceptions.InvalidParameterValueException
DAX.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'Description': 'string'
        }
    }
    
    
    :returns: 
    DAX.Client.exceptions.InvalidParameterGroupStateFault
    DAX.Client.exceptions.ParameterGroupNotFoundFault
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    DAX.Client.exceptions.InvalidParameterValueException
    DAX.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def update_subnet_group(SubnetGroupName=None, Description=None, SubnetIds=None):
    """
    Modifies an existing subnet group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_subnet_group(
        SubnetGroupName='string',
        Description='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type SubnetGroupName: string
    :param SubnetGroupName: [REQUIRED]\nThe name of the subnet group.\n

    :type Description: string
    :param Description: A description of the subnet group.

    :type SubnetIds: list
    :param SubnetIds: A list of subnet IDs in the subnet group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SubnetGroup': {
        'SubnetGroupName': 'string',
        'Description': 'string',
        'VpcId': 'string',
        'Subnets': [
            {
                'SubnetIdentifier': 'string',
                'SubnetAvailabilityZone': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

SubnetGroup (dict) --
The subnet group that has been modified.

SubnetGroupName (string) --
The name of the subnet group.

Description (string) --
The description of the subnet group.

VpcId (string) --
The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.

Subnets (list) --
A list of subnets associated with the subnet group.

(dict) --
Represents the subnet associated with a DAX cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with DAX.

SubnetIdentifier (string) --
The system-assigned identifier for the subnet.

SubnetAvailabilityZone (string) --
The Availability Zone (AZ) for the subnet.













Exceptions

DAX.Client.exceptions.SubnetGroupNotFoundFault
DAX.Client.exceptions.SubnetQuotaExceededFault
DAX.Client.exceptions.SubnetInUse
DAX.Client.exceptions.InvalidSubnet
DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault


    :return: {
        'SubnetGroup': {
            'SubnetGroupName': 'string',
            'Description': 'string',
            'VpcId': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    DAX.Client.exceptions.SubnetGroupNotFoundFault
    DAX.Client.exceptions.SubnetQuotaExceededFault
    DAX.Client.exceptions.SubnetInUse
    DAX.Client.exceptions.InvalidSubnet
    DAX.Client.exceptions.ServiceLinkedRoleNotFoundFault
    
    """
    pass

