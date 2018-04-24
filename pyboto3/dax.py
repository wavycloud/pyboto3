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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def create_cluster(ClusterName=None, NodeType=None, Description=None, ReplicationFactor=None, AvailabilityZones=None, SubnetGroupName=None, SecurityGroupIds=None, PreferredMaintenanceWindow=None, NotificationTopicArn=None, IamRoleArn=None, ParameterGroupName=None, Tags=None):
    """
    Creates a DAX cluster. All nodes in the cluster run the same DAX caching software.
    See also: AWS API Documentation
    
    
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
        ]
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]
            The cluster identifier. This parameter is stored as a lowercase string.
            Constraints:
            A name must contain from 1 to 20 alphanumeric characters or hyphens.
            The first character must be a letter.
            A name cannot end with a hyphen or contain two consecutive hyphens.
            

    :type NodeType: string
    :param NodeType: [REQUIRED]
            The compute and memory capacity of the nodes in the cluster.
            

    :type Description: string
    :param Description: A description of the cluster.

    :type ReplicationFactor: integer
    :param ReplicationFactor: [REQUIRED]
            The number of nodes in the DAX cluster. A replication factor of 1 will create a single-node cluster, without any read replicas. For additional fault tolerance, you can create a multiple node cluster with one or more read replicas. To do this, set ReplicationFactor to 2 or more.
            Note
            AWS recommends that you have at least two read replicas per cluster.
            

    :type AvailabilityZones: list
    :param AvailabilityZones: The Availability Zones (AZs) in which the cluster nodes will be created. All nodes belonging to the cluster are placed in these Availability Zones. Use this parameter if you want to distribute the nodes across multiple AZs.
            (string) --
            

    :type SubnetGroupName: string
    :param SubnetGroupName: The name of the subnet group to be used for the replication group.
            Warning
            DAX clusters can only run in an Amazon VPC environment. All of the subnets that you specify in a subnet group must exist in the same VPC.
            

    :type SecurityGroupIds: list
    :param SecurityGroupIds: A list of security group IDs to be assigned to each node in the DAX cluster. (Each of the security group ID is system-generated.)
            If this parameter is not specified, DAX assigns the default VPC security group to each node.
            (string) --
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the DAX cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:
            sun
            mon
            tue
            wed
            thu
            fri
            sat
            Example: sun:05:00-sun:09:00
            Note
            If you don't specify a preferred maintenance window when you create or modify a cache cluster, DAX assigns a 60-minute maintenance window on a randomly selected day of the week.
            

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent.
            Note
            The Amazon SNS topic owner must be same as the DAX cluster owner.
            

    :type IamRoleArn: string
    :param IamRoleArn: [REQUIRED]
            A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.
            

    :type ParameterGroupName: string
    :param ParameterGroupName: The parameter group to be associated with the DAX cluster.

    :type Tags: list
    :param Tags: A set of tags to associate with the DAX cluster.
            (dict) --A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
            AWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: .
            You cannot backdate the application of a tag.
            Key (string) --The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.
            Value (string) --The value of the tag. Tag values are case-sensitive and can be null.
            
            

    :rtype: dict
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
    
    
    :example: response = client.create_parameter_group(
        ParameterGroupName='string',
        Description='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]
            The name of the parameter group to apply to all of the clusters in this replication group.
            

    :type Description: string
    :param Description: A description of the parameter group.

    :rtype: dict
    :return: {
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def create_subnet_group(SubnetGroupName=None, Description=None, SubnetIds=None):
    """
    Creates a new subnet group.
    See also: AWS API Documentation
    
    
    :example: response = client.create_subnet_group(
        SubnetGroupName='string',
        Description='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type SubnetGroupName: string
    :param SubnetGroupName: [REQUIRED]
            A name for the subnet group. This value is stored as a lowercase string.
            

    :type Description: string
    :param Description: A description for the subnet group

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]
            A list of VPC subnet IDs for the subnet group.
            (string) --
            

    :rtype: dict
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
    
    
    """
    pass

def decrease_replication_factor(ClusterName=None, NewReplicationFactor=None, AvailabilityZones=None, NodeIdsToRemove=None):
    """
    Removes one or more nodes from a DAX cluster.
    See also: AWS API Documentation
    
    
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
    :param ClusterName: [REQUIRED]
            The name of the DAX cluster from which you want to remove nodes.
            

    :type NewReplicationFactor: integer
    :param NewReplicationFactor: [REQUIRED]
            The new number of nodes for the DAX cluster.
            

    :type AvailabilityZones: list
    :param AvailabilityZones: The Availability Zone(s) from which to remove nodes.
            (string) --
            

    :type NodeIdsToRemove: list
    :param NodeIdsToRemove: The unique identifiers of the nodes to be removed from the cluster.
            (string) --
            

    :rtype: dict
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
    
    
    :example: response = client.delete_cluster(
        ClusterName='string'
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]
            The name of the cluster to be deleted.
            

    :rtype: dict
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
    
    
    :example: response = client.delete_parameter_group(
        ParameterGroupName='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]
            The name of the parameter group to delete.
            

    :rtype: dict
    :return: {
        'DeletionMessage': 'string'
    }
    
    
    """
    pass

def delete_subnet_group(SubnetGroupName=None):
    """
    Deletes a subnet group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_subnet_group(
        SubnetGroupName='string'
    )
    
    
    :type SubnetGroupName: string
    :param SubnetGroupName: [REQUIRED]
            The name of the subnet group to delete.
            

    :rtype: dict
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
    
    
    :example: response = client.describe_clusters(
        ClusterNames=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ClusterNames: list
    :param ClusterNames: The names of the DAX clusters being described.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
            The value for MaxResults must be between 20 and 100.
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict
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
    
    
    :example: response = client.describe_default_parameters(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
            The value for MaxResults must be between 20 and 100.
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict
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
    
    
    """
    pass

def describe_events(SourceName=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, MaxResults=None, NextToken=None):
    """
    Returns events related to DAX clusters and parameter groups. You can obtain events specific to a particular DAX cluster or parameter group by providing the name as a parameter.
    By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days' worth of events if necessary.
    See also: AWS API Documentation
    
    
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
    :param Duration: The number of minutes' worth of events to retrieve.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
            The value for MaxResults must be between 20 and 100.
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict
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
    
    
    """
    pass

def describe_parameter_groups(ParameterGroupNames=None, MaxResults=None, NextToken=None):
    """
    Returns a list of parameter group descriptions. If a parameter group name is specified, the list will contain only the descriptions for that group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_parameter_groups(
        ParameterGroupNames=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ParameterGroupNames: list
    :param ParameterGroupNames: The names of the parameter groups.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
            The value for MaxResults must be between 20 and 100.
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'ParameterGroups': [
            {
                'ParameterGroupName': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_parameters(ParameterGroupName=None, Source=None, MaxResults=None, NextToken=None):
    """
    Returns the detailed parameter list for a particular parameter group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_parameters(
        ParameterGroupName='string',
        Source='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]
            The name of the parameter group.
            

    :type Source: string
    :param Source: How the parameter is defined. For example, system denotes a system-defined parameter.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
            The value for MaxResults must be between 20 and 100.
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict
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
    
    
    """
    pass

def describe_subnet_groups(SubnetGroupNames=None, MaxResults=None, NextToken=None):
    """
    Returns a list of subnet group descriptions. If a subnet group name is specified, the list will contain only the description of that group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_subnet_groups(
        SubnetGroupNames=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type SubnetGroupNames: list
    :param SubnetGroupNames: The name of the subnet group.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
            The value for MaxResults must be between 20 and 100.
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults .

    :rtype: dict
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
    :param Params: The parameters normally passed to
            ClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
    """
    pass

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def increase_replication_factor(ClusterName=None, NewReplicationFactor=None, AvailabilityZones=None):
    """
    Adds one or more nodes to a DAX cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.increase_replication_factor(
        ClusterName='string',
        NewReplicationFactor=123,
        AvailabilityZones=[
            'string',
        ]
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]
            The name of the DAX cluster that will receive additional nodes.
            

    :type NewReplicationFactor: integer
    :param NewReplicationFactor: [REQUIRED]
            The new number of nodes for the DAX cluster.
            

    :type AvailabilityZones: list
    :param AvailabilityZones: The Availability Zones (AZs) in which the cluster nodes will be created. All nodes belonging to the cluster are placed in these Availability Zones. Use this parameter if you want to distribute the nodes across multiple AZs.
            (string) --
            

    :rtype: dict
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
    
    
    :example: response = client.list_tags(
        ResourceName='string',
        NextToken='string'
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]
            The name of the DAX resource to which the tags belong.
            

    :type NextToken: string
    :param NextToken: An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token.

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def reboot_node(ClusterName=None, NodeId=None):
    """
    Reboots a single node of a DAX cluster. The reboot action takes place as soon as possible. During the reboot, the node status is set to REBOOTING.
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_node(
        ClusterName='string',
        NodeId='string'
    )
    
    
    :type ClusterName: string
    :param ClusterName: [REQUIRED]
            The name of the DAX cluster containing the node to be rebooted.
            

    :type NodeId: string
    :param NodeId: [REQUIRED]
            The system-assigned ID of the node to be rebooted.
            

    :rtype: dict
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
    :param ResourceName: [REQUIRED]
            The name of the DAX resource to which tags should be added.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags to be assigned to the DAX resource.
            (dict) --A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
            AWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: .
            You cannot backdate the application of a tag.
            Key (string) --The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.
            Value (string) --The value of the tag. Tag values are case-sensitive and can be null.
            
            

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def untag_resource(ResourceName=None, TagKeys=None):
    """
    Removes the association of tags from a DAX resource. You can call UntagResource up to 5 times per second, per account.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        ResourceName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]
            The name of the DAX resource from which the tags should be removed.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            A list of tag keys. If the DAX cluster has any tags with these keys, then the tags are removed from the cluster.
            (string) --
            

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_cluster(ClusterName=None, Description=None, PreferredMaintenanceWindow=None, NotificationTopicArn=None, NotificationTopicStatus=None, ParameterGroupName=None, SecurityGroupIds=None):
    """
    Modifies the settings for a DAX cluster. You can use this action to change one or more cluster configuration parameters by specifying the parameters and the new values.
    See also: AWS API Documentation
    
    
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
    :param ClusterName: [REQUIRED]
            The name of the DAX cluster to be modified.
            

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
    :param SecurityGroupIds: A list of user-specified security group IDs to be assigned to each node in the DAX cluster. If this parameter is not specified, DAX assigns the default VPC security group to each node.
            (string) --
            

    :rtype: dict
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
    :param ParameterGroupName: [REQUIRED]
            The name of the parameter group.
            

    :type ParameterNameValues: list
    :param ParameterNameValues: [REQUIRED]
            An array of name-value pairs for the parameters in the group. Each element in the array represents a single parameter.
            (dict) --An individual DAX parameter.
            ParameterName (string) --The name of the parameter.
            ParameterValue (string) --The value of the parameter.
            
            

    :rtype: dict
    :return: {
        'ParameterGroup': {
            'ParameterGroupName': 'string',
            'Description': 'string'
        }
    }
    
    
    """
    pass

def update_subnet_group(SubnetGroupName=None, Description=None, SubnetIds=None):
    """
    Modifies an existing subnet group.
    See also: AWS API Documentation
    
    
    :example: response = client.update_subnet_group(
        SubnetGroupName='string',
        Description='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type SubnetGroupName: string
    :param SubnetGroupName: [REQUIRED]
            The name of the subnet group.
            

    :type Description: string
    :param Description: A description of the subnet group.

    :type SubnetIds: list
    :param SubnetIds: A list of subnet IDs in the subnet group.
            (string) --
            

    :rtype: dict
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
    
    
    """
    pass

