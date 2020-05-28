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

def add_tags_to_resource(ResourceName=None, Tags=None):
    """
    Adds up to 50 cost allocation tags to the named resource. A cost allocation tag is a key-value pair where the key and value are case-sensitive. You can use cost allocation tags to categorize and track your AWS costs.
    When you apply tags to your ElastiCache resources, AWS generates a cost allocation report as a comma-separated value (CSV) file with your usage and costs aggregated by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. For more information, see Using Cost Allocation Tags in Amazon ElastiCache in the ElastiCache User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Adds up to 10 tags, key/value pairs, to a cluster or snapshot resource.
    Expected Output:
    
    :example: response = client.add_tags_to_resource(
        ResourceName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to which the tags are to be added, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot . ElastiCache resources are cluster and snapshot .\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.\n\n(dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.\n\nKey (string) --The key for the tag. May not be null.\n\nValue (string) --The tag\'s value. May be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TagList': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output from the AddTagsToResource , ListTagsForResource , and RemoveTagsFromResource operations.

TagList (list) --
A list of cost allocation tags as key-value pairs.

(dict) --
A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

Key (string) --
The key for the tag. May not be null.

Value (string) --
The tag\'s value. May be null.











Exceptions

ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.SnapshotNotFoundFault
ElastiCache.Client.exceptions.TagQuotaPerResourceExceeded
ElastiCache.Client.exceptions.InvalidARNFault

Examples
Adds up to 10 tags, key/value pairs, to a cluster or snapshot resource.
response = client.add_tags_to_resource(
    ResourceName='arn:aws:elasticache:us-east-1:1234567890:cluster:my-mem-cluster',
    Tags=[
        {
            'Key': 'APIVersion',
            'Value': '20150202',
        },
        {
            'Key': 'Service',
            'Value': 'ElastiCache',
        },
    ],
)

print(response)


Expected Output:
{
    'TagList': [
        {
            'Key': 'APIVersion',
            'Value': '20150202',
        },
        {
            'Key': 'Service',
            'Value': 'ElastiCache',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.CacheClusterNotFoundFault
    ElastiCache.Client.exceptions.SnapshotNotFoundFault
    ElastiCache.Client.exceptions.TagQuotaPerResourceExceeded
    ElastiCache.Client.exceptions.InvalidARNFault
    
    """
    pass

def authorize_cache_security_group_ingress(CacheSecurityGroupName=None, EC2SecurityGroupName=None, EC2SecurityGroupOwnerId=None):
    """
    Allows network ingress to a cache security group. Applications using ElastiCache must be running on Amazon EC2, and Amazon EC2 security groups are used as the authorization mechanism.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Allows network ingress to a cache security group. Applications using ElastiCache must be running on Amazon EC2. Amazon EC2 security groups are used as the authorization mechanism.
    Expected Output:
    
    :example: response = client.authorize_cache_security_group_ingress(
        CacheSecurityGroupName='string',
        EC2SecurityGroupName='string',
        EC2SecurityGroupOwnerId='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: [REQUIRED]\nThe cache security group that allows network ingress.\n

    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: [REQUIRED]\nThe Amazon EC2 security group to be authorized for ingress to the cache security group.\n

    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: [REQUIRED]\nThe AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheSecurityGroup': {
        'OwnerId': 'string',
        'CacheSecurityGroupName': 'string',
        'Description': 'string',
        'EC2SecurityGroups': [
            {
                'Status': 'string',
                'EC2SecurityGroupName': 'string',
                'EC2SecurityGroupOwnerId': 'string'
            },
        ],
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheSecurityGroup (dict) --
Represents the output of one of the following operations:

AuthorizeCacheSecurityGroupIngress
CreateCacheSecurityGroup
RevokeCacheSecurityGroupIngress


OwnerId (string) --
The AWS account ID of the cache security group owner.

CacheSecurityGroupName (string) --
The name of the cache security group.

Description (string) --
The description of the cache security group.

EC2SecurityGroups (list) --
A list of Amazon EC2 security groups that are associated with this cache security group.

(dict) --
Provides ownership and status information for an Amazon EC2 security group.

Status (string) --
The status of the Amazon EC2 security group.

EC2SecurityGroupName (string) --
The name of the Amazon EC2 security group.

EC2SecurityGroupOwnerId (string) --
The AWS account ID of the Amazon EC2 security group owner.





ARN (string) --
The ARN (Amazon Resource Name) of the cache security group.









Exceptions

ElastiCache.Client.exceptions.CacheSecurityGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidCacheSecurityGroupStateFault
ElastiCache.Client.exceptions.AuthorizationAlreadyExistsFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Allows network ingress to a cache security group. Applications using ElastiCache must be running on Amazon EC2. Amazon EC2 security groups are used as the authorization mechanism.
response = client.authorize_cache_security_group_ingress(
    CacheSecurityGroupName='my-sec-grp',
    EC2SecurityGroupName='my-ec2-sec-grp',
    EC2SecurityGroupOwnerId='1234567890',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheSecurityGroup': {
            'OwnerId': 'string',
            'CacheSecurityGroupName': 'string',
            'Description': 'string',
            'EC2SecurityGroups': [
                {
                    'Status': 'string',
                    'EC2SecurityGroupName': 'string',
                    'EC2SecurityGroupOwnerId': 'string'
                },
            ],
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    AuthorizeCacheSecurityGroupIngress
    CreateCacheSecurityGroup
    RevokeCacheSecurityGroupIngress
    
    """
    pass

def batch_apply_update_action(ReplicationGroupIds=None, CacheClusterIds=None, ServiceUpdateName=None):
    """
    Apply the service update. For more information on service updates and applying them, see Applying Service Updates .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_apply_update_action(
        ReplicationGroupIds=[
            'string',
        ],
        CacheClusterIds=[
            'string',
        ],
        ServiceUpdateName='string'
    )
    
    
    :type ReplicationGroupIds: list
    :param ReplicationGroupIds: The replication group IDs\n\n(string) --\n\n

    :type CacheClusterIds: list
    :param CacheClusterIds: The cache cluster IDs\n\n(string) --\n\n

    :type ServiceUpdateName: string
    :param ServiceUpdateName: [REQUIRED]\nThe unique ID of the service update\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProcessedUpdateActions': [
        {
            'ReplicationGroupId': 'string',
            'CacheClusterId': 'string',
            'ServiceUpdateName': 'string',
            'UpdateActionStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete'|'scheduling'|'scheduled'|'not-applicable'
        },
    ],
    'UnprocessedUpdateActions': [
        {
            'ReplicationGroupId': 'string',
            'CacheClusterId': 'string',
            'ServiceUpdateName': 'string',
            'ErrorType': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

ProcessedUpdateActions (list) --
Update actions that have been processed successfully

(dict) --
Update action that has been processed for the corresponding apply/stop request

ReplicationGroupId (string) --
The ID of the replication group

CacheClusterId (string) --
The ID of the cache cluster

ServiceUpdateName (string) --
The unique ID of the service update

UpdateActionStatus (string) --
The status of the update action on the Redis cluster





UnprocessedUpdateActions (list) --
Update actions that haven\'t been processed successfully

(dict) --
Update action that has failed to be processed for the corresponding apply/stop request

ReplicationGroupId (string) --
The replication group ID

CacheClusterId (string) --
The ID of the cache cluster

ServiceUpdateName (string) --
The unique ID of the service update

ErrorType (string) --
The error type for requests that are not processed

ErrorMessage (string) --
The error message that describes the reason the request was not processed











Exceptions

ElastiCache.Client.exceptions.ServiceUpdateNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException


    :return: {
        'ProcessedUpdateActions': [
            {
                'ReplicationGroupId': 'string',
                'CacheClusterId': 'string',
                'ServiceUpdateName': 'string',
                'UpdateActionStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete'|'scheduling'|'scheduled'|'not-applicable'
            },
        ],
        'UnprocessedUpdateActions': [
            {
                'ReplicationGroupId': 'string',
                'CacheClusterId': 'string',
                'ServiceUpdateName': 'string',
                'ErrorType': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.ServiceUpdateNotFoundFault
    ElastiCache.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def batch_stop_update_action(ReplicationGroupIds=None, CacheClusterIds=None, ServiceUpdateName=None):
    """
    Stop the service update. For more information on service updates and stopping them, see Stopping Service Updates .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_stop_update_action(
        ReplicationGroupIds=[
            'string',
        ],
        CacheClusterIds=[
            'string',
        ],
        ServiceUpdateName='string'
    )
    
    
    :type ReplicationGroupIds: list
    :param ReplicationGroupIds: The replication group IDs\n\n(string) --\n\n

    :type CacheClusterIds: list
    :param CacheClusterIds: The cache cluster IDs\n\n(string) --\n\n

    :type ServiceUpdateName: string
    :param ServiceUpdateName: [REQUIRED]\nThe unique ID of the service update\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProcessedUpdateActions': [
        {
            'ReplicationGroupId': 'string',
            'CacheClusterId': 'string',
            'ServiceUpdateName': 'string',
            'UpdateActionStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete'|'scheduling'|'scheduled'|'not-applicable'
        },
    ],
    'UnprocessedUpdateActions': [
        {
            'ReplicationGroupId': 'string',
            'CacheClusterId': 'string',
            'ServiceUpdateName': 'string',
            'ErrorType': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

ProcessedUpdateActions (list) --
Update actions that have been processed successfully

(dict) --
Update action that has been processed for the corresponding apply/stop request

ReplicationGroupId (string) --
The ID of the replication group

CacheClusterId (string) --
The ID of the cache cluster

ServiceUpdateName (string) --
The unique ID of the service update

UpdateActionStatus (string) --
The status of the update action on the Redis cluster





UnprocessedUpdateActions (list) --
Update actions that haven\'t been processed successfully

(dict) --
Update action that has failed to be processed for the corresponding apply/stop request

ReplicationGroupId (string) --
The replication group ID

CacheClusterId (string) --
The ID of the cache cluster

ServiceUpdateName (string) --
The unique ID of the service update

ErrorType (string) --
The error type for requests that are not processed

ErrorMessage (string) --
The error message that describes the reason the request was not processed











Exceptions

ElastiCache.Client.exceptions.ServiceUpdateNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException


    :return: {
        'ProcessedUpdateActions': [
            {
                'ReplicationGroupId': 'string',
                'CacheClusterId': 'string',
                'ServiceUpdateName': 'string',
                'UpdateActionStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete'|'scheduling'|'scheduled'|'not-applicable'
            },
        ],
        'UnprocessedUpdateActions': [
            {
                'ReplicationGroupId': 'string',
                'CacheClusterId': 'string',
                'ServiceUpdateName': 'string',
                'ErrorType': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.ServiceUpdateNotFoundFault
    ElastiCache.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def complete_migration(ReplicationGroupId=None, Force=None):
    """
    Complete the migration of data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.complete_migration(
        ReplicationGroupId='string',
        Force=True|False
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe ID of the replication group to which data is being migrated.\n

    :type Force: boolean
    :param Force: Forces the migration to stop without ensuring that data is in sync. It is recommended to use this option only to abort the migration and not recommended when application wants to continue migration to ElastiCache.

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationGroup': {
        'ReplicationGroupId': 'string',
        'Description': 'string',
        'GlobalReplicationGroupInfo': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupMemberRole': 'string'
        },
        'Status': 'string',
        'PendingModifiedValues': {
            'PrimaryClusterId': 'string',
            'AutomaticFailoverStatus': 'enabled'|'disabled',
            'Resharding': {
                'SlotMigration': {
                    'ProgressPercentage': 123.0
                }
            },
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'MemberClusters': [
            'string',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': 'string',
                'Status': 'string',
                'PrimaryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ReaderEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'Slots': 'string',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'string',
                        'CacheNodeId': 'string',
                        'ReadEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'PreferredAvailabilityZone': 'string',
                        'CurrentRole': 'string'
                    },
                ]
            },
        ],
        'SnapshottingClusterId': 'string',
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'ClusterEnabled': True|False,
        'CacheNodeType': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

ReplicationGroup (dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.









Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.ReplicationGroupNotUnderMigrationFault


    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled): T1 node types.
    Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def copy_snapshot(SourceSnapshotName=None, TargetSnapshotName=None, TargetBucket=None, KmsKeyId=None):
    """
    Makes a copy of an existing snapshot.
    You could receive the following error messages.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Copies a snapshot to a specified name.
    Expected Output:
    
    :example: response = client.copy_snapshot(
        SourceSnapshotName='string',
        TargetSnapshotName='string',
        TargetBucket='string',
        KmsKeyId='string'
    )
    
    
    :type SourceSnapshotName: string
    :param SourceSnapshotName: [REQUIRED]\nThe name of an existing snapshot from which to make a copy.\n

    :type TargetSnapshotName: string
    :param TargetSnapshotName: [REQUIRED]\nA name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting.\n

    :type TargetBucket: string
    :param TargetBucket: The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access.\nWhen using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket in the Amazon ElastiCache User Guide .\nFor more information, see Exporting a Snapshot in the Amazon ElastiCache User Guide .\n

    :type KmsKeyId: string
    :param KmsKeyId: The ID of the KMS key used to encrypt the target snapshot.

    :rtype: dict

ReturnsResponse Syntax
{
    'Snapshot': {
        'SnapshotName': 'string',
        'ReplicationGroupId': 'string',
        'ReplicationGroupDescription': 'string',
        'CacheClusterId': 'string',
        'SnapshotStatus': 'string',
        'SnapshotSource': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'NumCacheNodes': 123,
        'PreferredAvailabilityZone': 'string',
        'CacheClusterCreateTime': datetime(2015, 1, 1),
        'PreferredMaintenanceWindow': 'string',
        'TopicArn': 'string',
        'Port': 123,
        'CacheParameterGroupName': 'string',
        'CacheSubnetGroupName': 'string',
        'VpcId': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'NumNodeGroups': 123,
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'NodeSnapshots': [
            {
                'CacheClusterId': 'string',
                'NodeGroupId': 'string',
                'CacheNodeId': 'string',
                'NodeGroupConfiguration': {
                    'NodeGroupId': 'string',
                    'Slots': 'string',
                    'ReplicaCount': 123,
                    'PrimaryAvailabilityZone': 'string',
                    'ReplicaAvailabilityZones': [
                        'string',
                    ]
                },
                'CacheSize': 'string',
                'CacheNodeCreateTime': datetime(2015, 1, 1),
                'SnapshotCreateTime': datetime(2015, 1, 1)
            },
        ],
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

Snapshot (dict) --
Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

SnapshotName (string) --
The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

ReplicationGroupId (string) --
The unique identifier of the source replication group.

ReplicationGroupDescription (string) --
A description of the source replication group.

CacheClusterId (string) --
The user-supplied identifier of the source cluster.

SnapshotStatus (string) --
The status of the snapshot. Valid values: creating | available | restoring | copying | deleting .

SnapshotSource (string) --
Indicates whether the snapshot is from an automatic backup (automated ) or was created manually (manual ).

CacheNodeType (string) --
The name of the compute and memory capacity node type for the source cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Engine (string) --
The name of the cache engine (memcached or redis ) used by the source cluster.

EngineVersion (string) --
The version of the cache engine version that is used by the source cluster.

NumCacheNodes (integer) --
The number of cache nodes in the source cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the source cluster is located.

CacheClusterCreateTime (datetime) --
The date and time when the source cluster was created.

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for ddd are:

sun
mon
tue
wed
thu
fri
sat

Example: sun:23:00-mon:01:30

TopicArn (string) --
The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

Port (integer) --
The port number used by each cache nodes in the source cluster.

CacheParameterGroupName (string) --
The cache parameter group that is associated with the source cluster.

CacheSubnetGroupName (string) --
The name of the cache subnet group associated with the source cluster.

VpcId (string) --
The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

AutoMinorVersionUpgrade (boolean) --
This parameter is currently disabled.

SnapshotRetentionLimit (integer) --
For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.
For manual snapshots, this field reflects the SnapshotRetentionLimit for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the DeleteSnapshot operation.

Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range during which ElastiCache takes daily snapshots of the source cluster.

NumNodeGroups (integer) --
The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


NodeSnapshots (list) --
A list of the cache nodes in the source cluster.

(dict) --
Represents an individual cache node in a snapshot of a cluster.

CacheClusterId (string) --
A unique identifier for the source cluster.

NodeGroupId (string) --
A unique identifier for the source node group (shard).

CacheNodeId (string) --
The cache node identifier for the node in the source cluster.

NodeGroupConfiguration (dict) --
The configuration for the source node group (shard).

NodeGroupId (string) --
Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.

Slots (string) --
A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format startkey-endkey .
Example: "0-3999"

ReplicaCount (integer) --
The number of read replica nodes in this node group (shard).

PrimaryAvailabilityZone (string) --
The Availability Zone where the primary node of this node group (shard) is launched.

ReplicaAvailabilityZones (list) --
A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ReplicaCount or ReplicasPerNodeGroup if not specified.

(string) --




CacheSize (string) --
The size of the cache on the source cache node.

CacheNodeCreateTime (datetime) --
The date and time when the cache node was created in the source cluster.

SnapshotCreateTime (datetime) --
The date and time when the source node\'s metadata and cache data set was obtained for the snapshot.





KmsKeyId (string) --
The ID of the KMS key used to encrypt the snapshot.

ARN (string) --
The ARN (Amazon Resource Name) of the snapshot.









Exceptions

ElastiCache.Client.exceptions.SnapshotAlreadyExistsFault
ElastiCache.Client.exceptions.SnapshotNotFoundFault
ElastiCache.Client.exceptions.SnapshotQuotaExceededFault
ElastiCache.Client.exceptions.InvalidSnapshotStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Copies a snapshot to a specified name.
response = client.copy_snapshot(
    SourceSnapshotName='my-snapshot',
    TargetBucket='',
    TargetSnapshotName='my-snapshot-copy',
)

print(response)


Expected Output:
{
    'Snapshot': {
        'AutoMinorVersionUpgrade': True,
        'CacheClusterCreateTime': datetime(2016, 12, 21, 22, 24, 4, 2, 356, 0),
        'CacheClusterId': 'my-redis4',
        'CacheNodeType': 'cache.m3.large',
        'CacheParameterGroupName': 'default.redis3.2',
        'CacheSubnetGroupName': 'default',
        'Engine': 'redis',
        'EngineVersion': '3.2.4',
        'NodeSnapshots': [
            {
                'CacheNodeCreateTime': datetime(2016, 12, 21, 22, 24, 4, 2, 356, 0),
                'CacheNodeId': '0001',
                'CacheSize': '3 MB',
                'SnapshotCreateTime': datetime(2016, 12, 28, 7, 0, 52, 2, 363, 0),
            },
        ],
        'NumCacheNodes': 1,
        'Port': 6379,
        'PreferredAvailabilityZone': 'us-east-1c',
        'PreferredMaintenanceWindow': 'tue:09:30-tue:10:30',
        'SnapshotName': 'my-snapshot-copy',
        'SnapshotRetentionLimit': 7,
        'SnapshotSource': 'manual',
        'SnapshotStatus': 'creating',
        'SnapshotWindow': '07:00-08:00',
        'VpcId': 'vpc-3820329f3',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Snapshot': {
            'SnapshotName': 'string',
            'ReplicationGroupId': 'string',
            'ReplicationGroupDescription': 'string',
            'CacheClusterId': 'string',
            'SnapshotStatus': 'string',
            'SnapshotSource': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'NumCacheNodes': 123,
            'PreferredAvailabilityZone': 'string',
            'CacheClusterCreateTime': datetime(2015, 1, 1),
            'PreferredMaintenanceWindow': 'string',
            'TopicArn': 'string',
            'Port': 123,
            'CacheParameterGroupName': 'string',
            'CacheSubnetGroupName': 'string',
            'VpcId': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'NumNodeGroups': 123,
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'NodeSnapshots': [
                {
                    'CacheClusterId': 'string',
                    'NodeGroupId': 'string',
                    'CacheNodeId': 'string',
                    'NodeGroupConfiguration': {
                        'NodeGroupId': 'string',
                        'Slots': 'string',
                        'ReplicaCount': 123,
                        'PrimaryAvailabilityZone': 'string',
                        'ReplicaAvailabilityZones': [
                            'string',
                        ]
                    },
                    'CacheSize': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'SnapshotCreateTime': datetime(2015, 1, 1)
                },
            ],
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    SourceSnapshotName (string) -- [REQUIRED]
    The name of an existing snapshot from which to make a copy.
    
    TargetSnapshotName (string) -- [REQUIRED]
    A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting.
    
    TargetBucket (string) -- The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access.
    When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket in the Amazon ElastiCache User Guide .
    For more information, see Exporting a Snapshot in the Amazon ElastiCache User Guide .
    
    KmsKeyId (string) -- The ID of the KMS key used to encrypt the target snapshot.
    
    """
    pass

def create_cache_cluster(CacheClusterId=None, ReplicationGroupId=None, AZMode=None, PreferredAvailabilityZone=None, PreferredAvailabilityZones=None, NumCacheNodes=None, CacheNodeType=None, Engine=None, EngineVersion=None, CacheParameterGroupName=None, CacheSubnetGroupName=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, Tags=None, SnapshotArns=None, SnapshotName=None, PreferredMaintenanceWindow=None, Port=None, NotificationTopicArn=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None, AuthToken=None):
    """
    Creates a cluster. All nodes in the cluster run the same protocol-compliant cache engine software, either Memcached or Redis.
    This operation is not supported for Redis (cluster mode enabled) clusters.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a Redis cluster with 1 node.
    Expected Output:
    
    :example: response = client.create_cache_cluster(
        CacheClusterId='string',
        ReplicationGroupId='string',
        AZMode='single-az'|'cross-az',
        PreferredAvailabilityZone='string',
        PreferredAvailabilityZones=[
            'string',
        ],
        NumCacheNodes=123,
        CacheNodeType='string',
        Engine='string',
        EngineVersion='string',
        CacheParameterGroupName='string',
        CacheSubnetGroupName='string',
        CacheSecurityGroupNames=[
            'string',
        ],
        SecurityGroupIds=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        SnapshotArns=[
            'string',
        ],
        SnapshotName='string',
        PreferredMaintenanceWindow='string',
        Port=123,
        NotificationTopicArn='string',
        AutoMinorVersionUpgrade=True|False,
        SnapshotRetentionLimit=123,
        SnapshotWindow='string',
        AuthToken='string'
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: [REQUIRED]\nThe node group (shard) identifier. This parameter is stored as a lowercase string.\n\nConstraints:\n\nA name must contain from 1 to 50 alphanumeric characters or hyphens.\nThe first character must be a letter.\nA name cannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type ReplicationGroupId: string
    :param ReplicationGroupId: The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.\nIf the specified replication group is Multi-AZ enabled and the Availability Zone is not specified, the cluster is created in Availability Zones that provide the best spread of read replicas across Availability Zones.\n\nNote\nThis parameter is only valid if the Engine parameter is redis .\n\n

    :type AZMode: string
    :param AZMode: Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster\'s region.\nThis parameter is only supported for Memcached clusters.\nIf the AZMode and PreferredAvailabilityZones are not specified, ElastiCache assumes single-az mode.\n

    :type PreferredAvailabilityZone: string
    :param PreferredAvailabilityZone: The EC2 Availability Zone in which the cluster is created.\nAll nodes belonging to this Memcached cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use PreferredAvailabilityZones .\nDefault: System chosen Availability Zone.\n

    :type PreferredAvailabilityZones: list
    :param PreferredAvailabilityZones: A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important.\nThis option is only supported on Memcached.\n\nNote\nIf you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.\nThe number of Availability Zones listed must equal the value of NumCacheNodes .\n\nIf you want all the nodes in the same Availability Zone, use PreferredAvailabilityZone instead, or repeat the Availability Zone multiple times in the list.\nDefault: System chosen Availability Zones.\n\n(string) --\n\n

    :type NumCacheNodes: integer
    :param NumCacheNodes: The initial number of cache nodes that the cluster has.\nFor clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.\nIf you need more than 20 nodes for your Memcached cluster, please fill out the ElastiCache Limit Increase Request form at http://aws.amazon.com/contact-us/elasticache-node-limit-request/ .\n

    :type CacheNodeType: string
    :param CacheNodeType: The compute and memory capacity of the nodes in the node group (shard).\nThe following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.\n\nGeneral purpose:\nCurrent generation:  M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium\nPrevious generation: (not recommended) T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge\n\n\nCompute optimized:\nPrevious generation: (not recommended) C1 node types: cache.c1.xlarge\n\n\nMemory optimized:\nCurrent generation:  R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge\nPrevious generation: (not recommended) M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge\n\n\n\n\nAdditional node type info\n\nAll current generation instance types are created in Amazon VPC by default.\nRedis append-only files (AOF) are not supported for T1 or T2 instances.\nRedis Multi-AZ with automatic failover is not supported on T1 instances.\nRedis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.\n\n

    :type Engine: string
    :param Engine: The name of the cache engine to be used for this cluster.\nValid values for this parameter are: memcached | redis\n

    :type EngineVersion: string
    :param EngineVersion: The version number of the cache engine to be used for this cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.\n\nImportant: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.\n

    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of the parameter group to associate with this cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has cluster-enabled=\'yes\' when creating a cluster.

    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: The name of the subnet group to be used for the cluster.\nUse this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).\n\nWarning\nIf you\'re going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see Subnets and Subnet Groups .\n\n

    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: A list of security group names to associate with this cluster.\nUse this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).\n\n(string) --\n\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: One or more VPC security groups associated with the cluster.\nUse this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).\n\n(string) --\n\n

    :type Tags: list
    :param Tags: A list of cost allocation tags to be added to this resource.\n\n(dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.\n\nKey (string) --The key for the tag. May not be null.\n\nValue (string) --The tag\'s value. May be null.\n\n\n\n\n

    :type SnapshotArns: list
    :param SnapshotArns: A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas.\n\nNote\nThis parameter is only valid if the Engine parameter is redis .\n\nExample of an Amazon S3 ARN: arn:aws:s3:::my_bucket/snapshot1.rdb\n\n(string) --\n\n

    :type SnapshotName: string
    :param SnapshotName: The name of a Redis snapshot from which to restore data into the new node group (shard). The snapshot status changes to restoring while the new node group (shard) is being created.\n\nNote\nThis parameter is only valid if the Engine parameter is redis .\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:\nSpecifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.\nValid values for ddd are:\n\nsun\nmon\ntue\nwed\nthu\nfri\nsat\n\nExample: sun:23:00-mon:01:30\n

    :type Port: integer
    :param Port: The port number on which each of the cache nodes accepts connections.

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.\n\nNote\nThe Amazon SNS topic owner must be the same as the cluster owner.\n\n

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.

    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot taken today is retained for 5 days before being deleted.\n\nNote\nThis parameter is only valid if the Engine parameter is redis .\n\nDefault: 0 (i.e., automatic backups are disabled for this cache cluster).\n

    :type SnapshotWindow: string
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).\nExample: 05:00-09:00\nIf you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.\n\nNote\nThis parameter is only valid if the Engine parameter is redis .\n\n

    :type AuthToken: string
    :param AuthToken: \nReserved parameter. The password used to access a password protected server.\nPassword constraints:\n\nMust be only printable ASCII characters.\nMust be at least 16 characters and no more than 128 characters in length.\nThe only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable special characters cannot be used in the AUTH token.\n\nFor more information, see AUTH password at http://redis.io/commands/AUTH.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheCluster': {
        'CacheClusterId': 'string',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClientDownloadLandingPage': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'CacheClusterStatus': 'string',
        'NumCacheNodes': 123,
        'PreferredAvailabilityZone': 'string',
        'CacheClusterCreateTime': datetime(2015, 1, 1),
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'NumCacheNodes': 123,
            'CacheNodeIdsToRemove': [
                'string',
            ],
            'EngineVersion': 'string',
            'CacheNodeType': 'string',
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'CacheSecurityGroups': [
            {
                'CacheSecurityGroupName': 'string',
                'Status': 'string'
            },
        ],
        'CacheParameterGroup': {
            'CacheParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'CacheNodeIdsToReboot': [
                'string',
            ]
        },
        'CacheSubnetGroupName': 'string',
        'CacheNodes': [
            {
                'CacheNodeId': 'string',
                'CacheNodeStatus': 'string',
                'CacheNodeCreateTime': datetime(2015, 1, 1),
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ParameterGroupStatus': 'string',
                'SourceCacheNodeId': 'string',
                'CustomerAvailabilityZone': 'string'
            },
        ],
        'AutoMinorVersionUpgrade': True|False,
        'SecurityGroups': [
            {
                'SecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'ReplicationGroupId': 'string',
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheCluster (dict) --
Contains all of the attributes of a specific cluster.

CacheClusterId (string) --
The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

ConfigurationEndpoint (dict) --
Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have .cfg in it.
Example: mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ClientDownloadLandingPage (string) --
The URL of the web page where you can download the latest ElastiCache client library.

CacheNodeType (string) --
The name of the compute and memory capacity node type for the cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Engine (string) --
The name of the cache engine (memcached or redis ) to be used for this cluster.

EngineVersion (string) --
The version of the cache engine that is used in this cluster.

CacheClusterStatus (string) --
The current state of this cluster, one of the following values: available , creating , deleted , deleting , incompatible-network , modifying , rebooting cluster nodes , restore-failed , or snapshotting .

NumCacheNodes (integer) --
The number of cache nodes in the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

CacheClusterCreateTime (datetime) --
The date and time when the cluster was created.

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for ddd are:

sun
mon
tue
wed
thu
fri
sat

Example: sun:23:00-mon:01:30

PendingModifiedValues (dict) --
A group of settings that are applied to the cluster in the future, or that are currently being applied.

NumCacheNodes (integer) --
The new number of cache nodes for the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

CacheNodeIdsToRemove (list) --
A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

(string) --


EngineVersion (string) --
The new cache engine version that the cluster runs.

CacheNodeType (string) --
The cache node type that this cluster or replication group is scaled to.

AuthTokenStatus (string) --
The auth token status



NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



CacheSecurityGroups (list) --
A list of cache security group elements, composed of name and status sub-elements.

(dict) --
Represents a cluster\'s status within a particular cache security group.

CacheSecurityGroupName (string) --
The name of the cache security group.

Status (string) --
The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





CacheParameterGroup (dict) --
Status of the cache parameter group.

CacheParameterGroupName (string) --
The name of the cache parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

CacheNodeIdsToReboot (list) --
A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

(string) --




CacheSubnetGroupName (string) --
The name of the cache subnet group associated with the cluster.

CacheNodes (list) --
A list of cache nodes that are members of the cluster.

(dict) --
Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster\'s protocol-compliant caching software - either Memcached or Redis.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


CacheNodeId (string) --
The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer\'s AWS account.

CacheNodeStatus (string) --
The current state of this cache node, one of the following values: available , creating , rebooting , or deleting .

CacheNodeCreateTime (datetime) --
The date and time when the cache node was created.

Endpoint (dict) --
The hostname for connecting to this cache node.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ParameterGroupStatus (string) --
The status of the parameter group applied to this cache node.

SourceCacheNodeId (string) --
The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

CustomerAvailabilityZone (string) --
The Availability Zone where this node was created and now resides.





AutoMinorVersionUpgrade (boolean) --
This parameter is currently disabled.

SecurityGroups (list) --
A list of VPC Security Groups associated with the cluster.

(dict) --
Represents a single cache security group and its status.

SecurityGroupId (string) --
The identifier of the cache security group.

Status (string) --
The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





ReplicationGroupId (string) --
The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.
Example: 05:00-09:00

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable at-rest encryption on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

ARN (string) --
The ARN (Amazon Resource Name) of the cache cluster.









Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.CacheClusterAlreadyExistsFault
ElastiCache.Client.exceptions.InsufficientCacheClusterCapacityFault
ElastiCache.Client.exceptions.CacheSecurityGroupNotFoundFault
ElastiCache.Client.exceptions.CacheSubnetGroupNotFoundFault
ElastiCache.Client.exceptions.ClusterQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.NodeQuotaForClusterExceededFault
ElastiCache.Client.exceptions.NodeQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidVPCNetworkStateFault
ElastiCache.Client.exceptions.TagQuotaPerResourceExceeded
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Creates a Redis cluster with 1 node.
response = client.create_cache_cluster(
    AutoMinorVersionUpgrade=True,
    CacheClusterId='my-redis',
    CacheNodeType='cache.r3.larage',
    CacheSubnetGroupName='default',
    Engine='redis',
    EngineVersion='3.2.4',
    NumCacheNodes=1,
    Port=6379,
    PreferredAvailabilityZone='us-east-1c',
    SnapshotRetentionLimit=7,
)

print(response)


Expected Output:
{
    'CacheCluster': {
        'AutoMinorVersionUpgrade': True,
        'CacheClusterId': 'my-redis',
        'CacheClusterStatus': 'creating',
        'CacheNodeType': 'cache.m3.large',
        'CacheParameterGroup': {
            'CacheNodeIdsToReboot': [
            ],
            'CacheParameterGroupName': 'default.redis3.2',
            'ParameterApplyStatus': 'in-sync',
        },
        'CacheSecurityGroups': [
        ],
        'CacheSubnetGroupName': 'default',
        'ClientDownloadLandingPage': 'https: //console.aws.amazon.com/elasticache/home#client-download: ',
        'Engine': 'redis',
        'EngineVersion': '3.2.4',
        'NumCacheNodes': 1,
        'PendingModifiedValues': {
        },
        'PreferredAvailabilityZone': 'us-east-1c',
        'PreferredMaintenanceWindow': 'fri: 05: 30-fri: 06: 30',
        'SnapshotRetentionLimit': 7,
        'SnapshotWindow': '10: 00-11: 00',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheCluster': {
            'CacheClusterId': 'string',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClientDownloadLandingPage': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'CacheClusterStatus': 'string',
            'NumCacheNodes': 123,
            'PreferredAvailabilityZone': 'string',
            'CacheClusterCreateTime': datetime(2015, 1, 1),
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'NumCacheNodes': 123,
                'CacheNodeIdsToRemove': [
                    'string',
                ],
                'EngineVersion': 'string',
                'CacheNodeType': 'string',
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'CacheSecurityGroups': [
                {
                    'CacheSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CacheParameterGroup': {
                'CacheParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'CacheNodeIdsToReboot': [
                    'string',
                ]
            },
            'CacheSubnetGroupName': 'string',
            'CacheNodes': [
                {
                    'CacheNodeId': 'string',
                    'CacheNodeStatus': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ParameterGroupStatus': 'string',
                    'SourceCacheNodeId': 'string',
                    'CustomerAvailabilityZone': 'string'
                },
            ],
            'AutoMinorVersionUpgrade': True|False,
            'SecurityGroups': [
                {
                    'SecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'ReplicationGroupId': 'string',
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
    Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
    
    
    Compute optimized:
    Previous generation: (not recommended)  C1 node types: cache.c1.xlarge
    
    
    Memory optimized:
    Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
    Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    
    
    
    """
    pass

def create_cache_parameter_group(CacheParameterGroupName=None, CacheParameterGroupFamily=None, Description=None):
    """
    Creates a new Amazon ElastiCache cache parameter group. An ElastiCache cache parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster or replication group using the CacheParameterGroup.
    A newly created CacheParameterGroup is an exact duplicate of the default parameter group for the CacheParameterGroupFamily. To customize the newly created CacheParameterGroup you can change the values of specific parameters. For more information, see:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates the Amazon ElastiCache parameter group custom-redis2-8.
    Expected Output:
    
    :example: response = client.create_cache_parameter_group(
        CacheParameterGroupName='string',
        CacheParameterGroupFamily='string',
        Description='string'
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: [REQUIRED]\nA user-specified name for the cache parameter group.\n

    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: [REQUIRED]\nThe name of the cache parameter group family that the cache parameter group can be used with.\nValid values are: memcached1.4 | memcached1.5 | redis2.6 | redis2.8 | redis3.2 | redis4.0 | redis5.0 |\n

    :type Description: string
    :param Description: [REQUIRED]\nA user-specified description for the cache parameter group.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheParameterGroup': {
        'CacheParameterGroupName': 'string',
        'CacheParameterGroupFamily': 'string',
        'Description': 'string',
        'IsGlobal': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheParameterGroup (dict) --
Represents the output of a CreateCacheParameterGroup operation.

CacheParameterGroupName (string) --
The name of the cache parameter group.

CacheParameterGroupFamily (string) --
The name of the cache parameter group family that this cache parameter group is compatible with.
Valid values are: memcached1.4 | memcached1.5 | redis2.6 | redis2.8 | redis3.2 | redis4.0 | redis5.0 |

Description (string) --
The description for this cache parameter group.

IsGlobal (boolean) --
Indicates whether the parameter group is associated with a Global Datastore

ARN (string) --
The ARN (Amazon Resource Name) of the cache parameter group.









Exceptions

ElastiCache.Client.exceptions.CacheParameterGroupQuotaExceededFault
ElastiCache.Client.exceptions.CacheParameterGroupAlreadyExistsFault
ElastiCache.Client.exceptions.InvalidCacheParameterGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Creates the Amazon ElastiCache parameter group custom-redis2-8.
response = client.create_cache_parameter_group(
    CacheParameterGroupFamily='redis2.8',
    CacheParameterGroupName='custom-redis2-8',
    Description='Custom Redis 2.8 parameter group.',
)

print(response)


Expected Output:
{
    'CacheParameterGroup': {
        'CacheParameterGroupFamily': 'redis2.8',
        'CacheParameterGroupName': 'custom-redis2-8',
        'Description': 'Custom Redis 2.8 parameter group.',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheParameterGroup': {
            'CacheParameterGroupName': 'string',
            'CacheParameterGroupFamily': 'string',
            'Description': 'string',
            'IsGlobal': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    CacheParameterGroupName (string) -- [REQUIRED]
    A user-specified name for the cache parameter group.
    
    CacheParameterGroupFamily (string) -- [REQUIRED]
    The name of the cache parameter group family that the cache parameter group can be used with.
    Valid values are: memcached1.4 | memcached1.5 | redis2.6 | redis2.8 | redis3.2 | redis4.0 | redis5.0 |
    
    Description (string) -- [REQUIRED]
    A user-specified description for the cache parameter group.
    
    
    """
    pass

def create_cache_security_group(CacheSecurityGroupName=None, Description=None):
    """
    Creates a new cache security group. Use a cache security group to control access to one or more clusters.
    Cache security groups are only used when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC). If you are creating a cluster inside of a VPC, use a cache subnet group instead. For more information, see CreateCacheSubnetGroup .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates an ElastiCache security group. ElastiCache security groups are only for clusters not running in an AWS VPC.
    Expected Output:
    
    :example: response = client.create_cache_security_group(
        CacheSecurityGroupName='string',
        Description='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: [REQUIRED]\nA name for the cache security group. This value is stored as a lowercase string.\nConstraints: Must contain no more than 255 alphanumeric characters. Cannot be the word 'Default'.\nExample: mysecuritygroup\n

    :type Description: string
    :param Description: [REQUIRED]\nA description for the cache security group.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheSecurityGroup': {
        'OwnerId': 'string',
        'CacheSecurityGroupName': 'string',
        'Description': 'string',
        'EC2SecurityGroups': [
            {
                'Status': 'string',
                'EC2SecurityGroupName': 'string',
                'EC2SecurityGroupOwnerId': 'string'
            },
        ],
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheSecurityGroup (dict) --
Represents the output of one of the following operations:

AuthorizeCacheSecurityGroupIngress
CreateCacheSecurityGroup
RevokeCacheSecurityGroupIngress


OwnerId (string) --
The AWS account ID of the cache security group owner.

CacheSecurityGroupName (string) --
The name of the cache security group.

Description (string) --
The description of the cache security group.

EC2SecurityGroups (list) --
A list of Amazon EC2 security groups that are associated with this cache security group.

(dict) --
Provides ownership and status information for an Amazon EC2 security group.

Status (string) --
The status of the Amazon EC2 security group.

EC2SecurityGroupName (string) --
The name of the Amazon EC2 security group.

EC2SecurityGroupOwnerId (string) --
The AWS account ID of the Amazon EC2 security group owner.





ARN (string) --
The ARN (Amazon Resource Name) of the cache security group.









Exceptions

ElastiCache.Client.exceptions.CacheSecurityGroupAlreadyExistsFault
ElastiCache.Client.exceptions.CacheSecurityGroupQuotaExceededFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Creates an ElastiCache security group. ElastiCache security groups are only for clusters not running in an AWS VPC.
response = client.create_cache_security_group(
    CacheSecurityGroupName='my-cache-sec-grp',
    Description='Example ElastiCache security group.',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheSecurityGroup': {
            'OwnerId': 'string',
            'CacheSecurityGroupName': 'string',
            'Description': 'string',
            'EC2SecurityGroups': [
                {
                    'Status': 'string',
                    'EC2SecurityGroupName': 'string',
                    'EC2SecurityGroupOwnerId': 'string'
                },
            ],
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    AuthorizeCacheSecurityGroupIngress
    CreateCacheSecurityGroup
    RevokeCacheSecurityGroupIngress
    
    """
    pass

def create_cache_subnet_group(CacheSubnetGroupName=None, CacheSubnetGroupDescription=None, SubnetIds=None):
    """
    Creates a new cache subnet group.
    Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a new cache subnet group.
    Expected Output:
    
    :example: response = client.create_cache_subnet_group(
        CacheSubnetGroupName='string',
        CacheSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: [REQUIRED]\nA name for the cache subnet group. This value is stored as a lowercase string.\nConstraints: Must contain no more than 255 alphanumeric characters or hyphens.\nExample: mysubnetgroup\n

    :type CacheSubnetGroupDescription: string
    :param CacheSubnetGroupDescription: [REQUIRED]\nA description for the cache subnet group.\n

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nA list of VPC subnet IDs for the cache subnet group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheSubnetGroup': {
        'CacheSubnetGroupName': 'string',
        'CacheSubnetGroupDescription': 'string',
        'VpcId': 'string',
        'Subnets': [
            {
                'SubnetIdentifier': 'string',
                'SubnetAvailabilityZone': {
                    'Name': 'string'
                }
            },
        ],
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheSubnetGroup (dict) --
Represents the output of one of the following operations:

CreateCacheSubnetGroup
ModifyCacheSubnetGroup


CacheSubnetGroupName (string) --
The name of the cache subnet group.

CacheSubnetGroupDescription (string) --
The description of the cache subnet group.

VpcId (string) --
The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

Subnets (list) --
A list of subnets associated with the cache subnet group.

(dict) --
Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

SubnetIdentifier (string) --
The unique identifier for the subnet.

SubnetAvailabilityZone (dict) --
The Availability Zone associated with the subnet.

Name (string) --
The name of the Availability Zone.







ARN (string) --
The ARN (Amazon Resource Name) of the cache subnet group.









Exceptions

ElastiCache.Client.exceptions.CacheSubnetGroupAlreadyExistsFault
ElastiCache.Client.exceptions.CacheSubnetGroupQuotaExceededFault
ElastiCache.Client.exceptions.CacheSubnetQuotaExceededFault
ElastiCache.Client.exceptions.InvalidSubnet

Examples
Creates a new cache subnet group.
response = client.create_cache_subnet_group(
    CacheSubnetGroupDescription='Sample subnet group',
    CacheSubnetGroupName='my-sn-grp2',
    SubnetIds=[
        'subnet-6f28c982',
        'subnet-bcd382f3',
        'subnet-845b3e7c0',
    ],
)

print(response)


Expected Output:
{
    'CacheSubnetGroup': {
        'CacheSubnetGroupDescription': 'My subnet group.',
        'CacheSubnetGroupName': 'my-sn-grp',
        'Subnets': [
            {
                'SubnetAvailabilityZone': {
                    'Name': 'us-east-1a',
                },
                'SubnetIdentifier': 'subnet-6f28c982',
            },
            {
                'SubnetAvailabilityZone': {
                    'Name': 'us-east-1c',
                },
                'SubnetIdentifier': 'subnet-bcd382f3',
            },
            {
                'SubnetAvailabilityZone': {
                    'Name': 'us-east-1b',
                },
                'SubnetIdentifier': 'subnet-845b3e7c0',
            },
        ],
        'VpcId': 'vpc-91280df6',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheSubnetGroup': {
            'CacheSubnetGroupName': 'string',
            'CacheSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    }
                },
            ],
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    CreateCacheSubnetGroup
    ModifyCacheSubnetGroup
    
    """
    pass

def create_global_replication_group(GlobalReplicationGroupIdSuffix=None, GlobalReplicationGroupDescription=None, PrimaryReplicationGroupId=None):
    """
    Global Datastore for Redis offers fully managed, fast, reliable and secure cross-region replication. Using Global Datastore for Redis, you can create cross-region read replica clusters for ElastiCache for Redis to enable low-latency reads and disaster recovery across regions. For more information, see Replication Across Regions Using Global Datastore .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_global_replication_group(
        GlobalReplicationGroupIdSuffix='string',
        GlobalReplicationGroupDescription='string',
        PrimaryReplicationGroupId='string'
    )
    
    
    :type GlobalReplicationGroupIdSuffix: string
    :param GlobalReplicationGroupIdSuffix: [REQUIRED]\nThe suffix name of a Global Datastore. The suffix guarantees uniqueness of the Global Datastore name across multiple regions.\n

    :type GlobalReplicationGroupDescription: string
    :param GlobalReplicationGroupDescription: Provides details of the Global Datastore

    :type PrimaryReplicationGroupId: string
    :param PrimaryReplicationGroupId: [REQUIRED]\nThe name of the primary cluster that accepts writes and will replicate updates to the secondary cluster.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalReplicationGroup': {
        'GlobalReplicationGroupId': 'string',
        'GlobalReplicationGroupDescription': 'string',
        'Status': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'Members': [
            {
                'ReplicationGroupId': 'string',
                'ReplicationGroupRegion': 'string',
                'Role': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'Status': 'string'
            },
        ],
        'ClusterEnabled': True|False,
        'GlobalNodeGroups': [
            {
                'GlobalNodeGroupId': 'string',
                'Slots': 'string'
            },
        ],
        'AuthTokenEnabled': True|False,
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

GlobalReplicationGroup (dict) --
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different AWS region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.


GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupDescription (string) --
The optional description of the Global Datastore

Status (string) --
The status of the Global Datastore

CacheNodeType (string) --
The cache node type of the Global Datastore

Engine (string) --
The Elasticache engine. For Redis only.

EngineVersion (string) --
The Elasticache Redis engine version. For preview, it is Redis version 5.0.5 only.

Members (list) --
The replication groups that comprise the Global Datastore.

(dict) --
A member of a Global Datastore. It contains the Replication Group Id, the AWS region and the role of the replication group.

ReplicationGroupId (string) --
The replication group id of the Global Datastore member.

ReplicationGroupRegion (string) --
The AWS region of the Global Datastore member.

Role (string) --
Indicates the role of the replication group, primary or secondary.

AutomaticFailover (string) --
Indicates whether automatic failover is enabled for the replication group.

Status (string) --
The status of the membership of the replication group.





ClusterEnabled (boolean) --
A flag that indicates whether the Global Datastore is cluster enabled.

GlobalNodeGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId (string) --
The name of the global node group

Slots (string) --
The keyspace for this node group





AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true. You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.


ARN (string) --
The ARN (Amazon Resource Name) of the global replication group.









Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.GlobalReplicationGroupAlreadyExistsFault
ElastiCache.Client.exceptions.ServiceLinkedRoleNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException


    :return: {
        'GlobalReplicationGroup': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupDescription': 'string',
            'Status': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'Members': [
                {
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupRegion': 'string',
                    'Role': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'Status': 'string'
                },
            ],
            'ClusterEnabled': True|False,
            'GlobalNodeGroups': [
                {
                    'GlobalNodeGroupId': 'string',
                    'Slots': 'string'
                },
            ],
            'AuthTokenEnabled': True|False,
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    GlobalReplicationGroupIdSuffix (string) -- [REQUIRED]
    The suffix name of a Global Datastore. The suffix guarantees uniqueness of the Global Datastore name across multiple regions.
    
    GlobalReplicationGroupDescription (string) -- Provides details of the Global Datastore
    PrimaryReplicationGroupId (string) -- [REQUIRED]
    The name of the primary cluster that accepts writes and will replicate updates to the secondary cluster.
    
    
    """
    pass

def create_replication_group(ReplicationGroupId=None, ReplicationGroupDescription=None, GlobalReplicationGroupId=None, PrimaryClusterId=None, AutomaticFailoverEnabled=None, NumCacheClusters=None, PreferredCacheClusterAZs=None, NumNodeGroups=None, ReplicasPerNodeGroup=None, NodeGroupConfiguration=None, CacheNodeType=None, Engine=None, EngineVersion=None, CacheParameterGroupName=None, CacheSubnetGroupName=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, Tags=None, SnapshotArns=None, SnapshotName=None, PreferredMaintenanceWindow=None, Port=None, NotificationTopicArn=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None, AuthToken=None, TransitEncryptionEnabled=None, AtRestEncryptionEnabled=None, KmsKeyId=None):
    """
    Creates a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication group.
    This API can be used to create a standalone regional replication group or a secondary replication group associated with a Global Datastore.
    A Redis (cluster mode disabled) replication group is a collection of clusters, where one of the clusters is a read/write primary and the others are read-only replicas. Writes to the primary are asynchronously propagated to the replicas.
    A Redis (cluster mode enabled) replication group is a collection of 1 to 90 node groups (shards). Each node group (shard) has one read/write primary node and up to 5 read-only replica nodes. Writes to the primary are asynchronously propagated to the replicas. Redis (cluster mode enabled) replication groups partition the data across node groups (shards).
    When a Redis (cluster mode disabled) replication group has been successfully created, you can add one or more read replicas to it, up to a total of 5 read replicas. You cannot alter a Redis (cluster mode enabled) replication group after it has been created. However, if you need to increase or decrease the number of node groups (console: shards), you can avail yourself of ElastiCache for Redis\' enhanced backup and restore. For more information, see Restoring From a Backup with Cluster Resizing in the ElastiCache User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a Redis replication group with 3 nodes.
    Expected Output:
    Creates a Redis (cluster mode enabled) replication group with two shards. One shard has one read replica node and the other shard has two read replicas.
    Expected Output:
    
    :example: response = client.create_replication_group(
        ReplicationGroupId='string',
        ReplicationGroupDescription='string',
        GlobalReplicationGroupId='string',
        PrimaryClusterId='string',
        AutomaticFailoverEnabled=True|False,
        NumCacheClusters=123,
        PreferredCacheClusterAZs=[
            'string',
        ],
        NumNodeGroups=123,
        ReplicasPerNodeGroup=123,
        NodeGroupConfiguration=[
            {
                'NodeGroupId': 'string',
                'Slots': 'string',
                'ReplicaCount': 123,
                'PrimaryAvailabilityZone': 'string',
                'ReplicaAvailabilityZones': [
                    'string',
                ]
            },
        ],
        CacheNodeType='string',
        Engine='string',
        EngineVersion='string',
        CacheParameterGroupName='string',
        CacheSubnetGroupName='string',
        CacheSecurityGroupNames=[
            'string',
        ],
        SecurityGroupIds=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        SnapshotArns=[
            'string',
        ],
        SnapshotName='string',
        PreferredMaintenanceWindow='string',
        Port=123,
        NotificationTopicArn='string',
        AutoMinorVersionUpgrade=True|False,
        SnapshotRetentionLimit=123,
        SnapshotWindow='string',
        AuthToken='string',
        TransitEncryptionEnabled=True|False,
        AtRestEncryptionEnabled=True|False,
        KmsKeyId='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe replication group identifier. This parameter is stored as a lowercase string.\nConstraints:\n\nA name must contain from 1 to 40 alphanumeric characters or hyphens.\nThe first character must be a letter.\nA name cannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type ReplicationGroupDescription: string
    :param ReplicationGroupDescription: [REQUIRED]\nA user-created description for the replication group.\n

    :type GlobalReplicationGroupId: string
    :param GlobalReplicationGroupId: The name of the Global Datastore

    :type PrimaryClusterId: string
    :param PrimaryClusterId: The identifier of the cluster that serves as the primary for this replication group. This cluster must already exist and have a status of available .\nThis parameter is not required if NumCacheClusters , NumNodeGroups , or ReplicasPerNodeGroup is specified.\n

    :type AutomaticFailoverEnabled: boolean
    :param AutomaticFailoverEnabled: Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.\nIf true , Multi-AZ is enabled for this replication group. If false , Multi-AZ is disabled for this replication group.\n\nAutomaticFailoverEnabled must be enabled for Redis (cluster mode enabled) replication groups.\nDefault: false\nAmazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:\n\nRedis versions earlier than 2.8.6.\nRedis (cluster mode disabled): T1 node types.\nRedis (cluster mode enabled): T1 node types.\n\n

    :type NumCacheClusters: integer
    :param NumCacheClusters: The number of nodes in the cluster.\nThis parameter is not used if there is more than one node group (shard). You should use ReplicasPerNodeGroup instead.\nIf AutomaticFailoverEnabled is true , the value of this parameter must be at least 2. If AutomaticFailoverEnabled is false you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6.\nThe maximum permitted value for NumCacheClusters is 6 (1 primary plus 5 replicas).\n

    :type PreferredCacheClusterAZs: list
    :param PreferredCacheClusterAZs: A list of EC2 Availability Zones in which the replication group\'s clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list.\nThis parameter is not used if there is more than one node group (shard). You should use NodeGroupConfiguration instead.\n\nNote\nIf you are creating your replication group in an Amazon VPC (recommended), you can only locate clusters in Availability Zones associated with the subnets in the selected subnet group.\nThe number of Availability Zones listed must equal the value of NumCacheClusters .\n\nDefault: system chosen Availability Zones.\n\n(string) --\n\n

    :type NumNodeGroups: integer
    :param NumNodeGroups: An optional parameter that specifies the number of node groups (shards) for this Redis (cluster mode enabled) replication group. For Redis (cluster mode disabled) either omit this parameter or set it to 1.\nDefault: 1\n

    :type ReplicasPerNodeGroup: integer
    :param ReplicasPerNodeGroup: An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.

    :type NodeGroupConfiguration: list
    :param NodeGroupConfiguration: A list of node group (shard) configuration options. Each node group (shard) configuration has the following members: PrimaryAvailabilityZone , ReplicaAvailabilityZones , ReplicaCount , and Slots .\nIf you\'re creating a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication group, you can use this parameter to individually configure each node group (shard), or you can omit this parameter. However, it is required when seeding a Redis (cluster mode enabled) cluster from a S3 rdb file. You must configure each node group (shard) using this parameter because you must specify the slots for each node group.\n\n(dict) --Node group (shard) configuration options. Each node group (shard) configuration has the following: Slots , PrimaryAvailabilityZone , ReplicaAvailabilityZones , ReplicaCount .\n\nNodeGroupId (string) --Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.\n\nSlots (string) --A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format startkey-endkey .\nExample: '0-3999'\n\nReplicaCount (integer) --The number of read replica nodes in this node group (shard).\n\nPrimaryAvailabilityZone (string) --The Availability Zone where the primary node of this node group (shard) is launched.\n\nReplicaAvailabilityZones (list) --A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ReplicaCount or ReplicasPerNodeGroup if not specified.\n\n(string) --\n\n\n\n\n\n

    :type CacheNodeType: string
    :param CacheNodeType: The compute and memory capacity of the nodes in the node group (shard).\nThe following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.\n\nGeneral purpose:\nCurrent generation:  M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium\nPrevious generation: (not recommended) T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge\n\n\nCompute optimized:\nPrevious generation: (not recommended) C1 node types: cache.c1.xlarge\n\n\nMemory optimized:\nCurrent generation:  R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge\nPrevious generation: (not recommended) M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge\n\n\n\n\nAdditional node type info\n\nAll current generation instance types are created in Amazon VPC by default.\nRedis append-only files (AOF) are not supported for T1 or T2 instances.\nRedis Multi-AZ with automatic failover is not supported on T1 instances.\nRedis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.\n\n

    :type Engine: string
    :param Engine: The name of the cache engine to be used for the clusters in this replication group.

    :type EngineVersion: string
    :param EngineVersion: The version number of the cache engine to be used for the clusters in this replication group. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.\n\nImportant: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ) in the ElastiCache User Guide , but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.\n

    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.\n\nNote\nIf you are restoring to an engine version that is different than the original, you must specify the default version of that version. For example, CacheParameterGroupName=default.redis4.0 .\n\nIf you are running Redis version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name.\n\nTo create a Redis (cluster mode disabled) replication group, use CacheParameterGroupName=default.redis3.2 .\nTo create a Redis (cluster mode enabled) replication group, use CacheParameterGroupName=default.redis3.2.cluster.on .\n\n

    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: The name of the cache subnet group to be used for the replication group.\n\nWarning\nIf you\'re going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see Subnets and Subnet Groups .\n\n

    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: A list of cache security group names to associate with this replication group.\n\n(string) --\n\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: One or more Amazon VPC security groups associated with this replication group.\nUse this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).\n\n(string) --\n\n

    :type Tags: list
    :param Tags: A list of cost allocation tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=``myKey`` , Value=``myKeyValue`` . You can include multiple tags as shown following: Key=``myKey`` , Value=``myKeyValue`` Key=``mySecondKey`` , Value=``mySecondKeyValue`` .\n\n(dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.\n\nKey (string) --The key for the tag. May not be null.\n\nValue (string) --The tag\'s value. May be null.\n\n\n\n\n

    :type SnapshotArns: list
    :param SnapshotArns: A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter NumNodeGroups or the number of node groups configured by NodeGroupConfiguration regardless of the number of ARNs specified here.\nExample of an Amazon S3 ARN: arn:aws:s3:::my_bucket/snapshot1.rdb\n\n(string) --\n\n

    :type SnapshotName: string
    :param SnapshotName: The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to restoring while the new replication group is being created.

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:\nSpecifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.\nValid values for ddd are:\n\nsun\nmon\ntue\nwed\nthu\nfri\nsat\n\nExample: sun:23:00-mon:01:30\n

    :type Port: integer
    :param Port: The port number on which each member of the replication group accepts connections.

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.\n\nNote\nThe Amazon SNS topic owner must be the same as the cluster owner.\n\n

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.

    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.\nDefault: 0 (i.e., automatic backups are disabled for this cluster).\n

    :type SnapshotWindow: string
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).\nExample: 05:00-09:00\nIf you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.\n

    :type AuthToken: string
    :param AuthToken: \nReserved parameter. The password used to access a password protected server.AuthToken can be specified only on replication groups where TransitEncryptionEnabled is true .\n\n\nWarning\nFor HIPAA compliance, you must specify TransitEncryptionEnabled as true , an AuthToken , and a CacheSubnetGroup .\n\nPassword constraints:\n\nMust be only printable ASCII characters.\nMust be at least 16 characters and no more than 128 characters in length.\nThe only permitted printable special characters are !, &, #, $, ^, <, >, and -. Other printable special characters cannot be used in the AUTH token.\n\nFor more information, see AUTH password at http://redis.io/commands/AUTH.\n

    :type TransitEncryptionEnabled: boolean
    :param TransitEncryptionEnabled: A flag that enables in-transit encryption when set to true .\nYou cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.\nThis parameter is valid only if the Engine parameter is redis , the EngineVersion parameter is 3.2.6 , 4.x or later, and the cluster is being created in an Amazon VPC.\nIf you enable in-transit encryption, you must also specify a value for CacheSubnetGroup .\n\nRequired: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.\nDefault: false\n\nWarning\nFor HIPAA compliance, you must specify TransitEncryptionEnabled as true , an AuthToken , and a CacheSubnetGroup .\n\n

    :type AtRestEncryptionEnabled: boolean
    :param AtRestEncryptionEnabled: A flag that enables encryption at rest when set to true .\nYou cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.\n\nRequired: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.\nDefault: false\n

    :type KmsKeyId: string
    :param KmsKeyId: The ID of the KMS key used to encrypt the disk in the cluster.

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationGroup': {
        'ReplicationGroupId': 'string',
        'Description': 'string',
        'GlobalReplicationGroupInfo': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupMemberRole': 'string'
        },
        'Status': 'string',
        'PendingModifiedValues': {
            'PrimaryClusterId': 'string',
            'AutomaticFailoverStatus': 'enabled'|'disabled',
            'Resharding': {
                'SlotMigration': {
                    'ProgressPercentage': 123.0
                }
            },
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'MemberClusters': [
            'string',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': 'string',
                'Status': 'string',
                'PrimaryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ReaderEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'Slots': 'string',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'string',
                        'CacheNodeId': 'string',
                        'ReadEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'PreferredAvailabilityZone': 'string',
                        'CurrentRole': 'string'
                    },
                ]
            },
        ],
        'SnapshottingClusterId': 'string',
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'ClusterEnabled': True|False,
        'CacheNodeType': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

ReplicationGroup (dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.









Exceptions

ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.ReplicationGroupAlreadyExistsFault
ElastiCache.Client.exceptions.InsufficientCacheClusterCapacityFault
ElastiCache.Client.exceptions.CacheSecurityGroupNotFoundFault
ElastiCache.Client.exceptions.CacheSubnetGroupNotFoundFault
ElastiCache.Client.exceptions.ClusterQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.NodeQuotaForClusterExceededFault
ElastiCache.Client.exceptions.NodeQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidVPCNetworkStateFault
ElastiCache.Client.exceptions.TagQuotaPerResourceExceeded
ElastiCache.Client.exceptions.NodeGroupsPerReplicationGroupQuotaExceededFault
ElastiCache.Client.exceptions.GlobalReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Creates a Redis replication group with 3 nodes.
response = client.create_replication_group(
    AutomaticFailoverEnabled=True,
    CacheNodeType='cache.m3.medium',
    Engine='redis',
    EngineVersion='2.8.24',
    NumCacheClusters=3,
    ReplicationGroupDescription='A Redis replication group.',
    ReplicationGroupId='my-redis-rg',
    SnapshotRetentionLimit=30,
)

print(response)


Expected Output:
{
    'ReplicationGroup': {
        'AutomaticFailover': 'enabling',
        'Description': 'A Redis replication group.',
        'MemberClusters': [
            'my-redis-rg-001',
            'my-redis-rg-002',
            'my-redis-rg-003',
        ],
        'PendingModifiedValues': {
        },
        'ReplicationGroupId': 'my-redis-rg',
        'SnapshottingClusterId': 'my-redis-rg-002',
        'Status': 'creating',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


Creates a Redis (cluster mode enabled) replication group with two shards. One shard has one read replica node and the other shard has two read replicas.
response = client.create_replication_group(
    AutoMinorVersionUpgrade=True,
    CacheNodeType='cache.m3.medium',
    CacheParameterGroupName='default.redis3.2.cluster.on',
    Engine='redis',
    EngineVersion='3.2.4',
    NodeGroupConfiguration=[
        {
            'PrimaryAvailabilityZone': 'us-east-1c',
            'ReplicaAvailabilityZones': [
                'us-east-1b',
            ],
            'ReplicaCount': 1,
            'Slots': '0-8999',
        },
        {
            'PrimaryAvailabilityZone': 'us-east-1a',
            'ReplicaAvailabilityZones': [
                'us-east-1a',
                'us-east-1c',
            ],
            'ReplicaCount': 2,
            'Slots': '9000-16383',
        },
    ],
    NumNodeGroups=2,
    ReplicationGroupDescription='A multi-sharded replication group',
    ReplicationGroupId='clustered-redis-rg',
    SnapshotRetentionLimit=8,
)

print(response)


Expected Output:
{
    'ReplicationGroup': {
        'AutomaticFailover': 'enabled',
        'Description': 'Sharded replication group',
        'MemberClusters': [
            'rc-rg3-0001-001',
            'rc-rg3-0001-002',
            'rc-rg3-0002-001',
            'rc-rg3-0002-002',
            'rc-rg3-0002-003',
        ],
        'PendingModifiedValues': {
        },
        'ReplicationGroupId': 'clustered-redis-rg',
        'SnapshotRetentionLimit': 8,
        'SnapshotWindow': '05:30-06:30',
        'Status': 'creating',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled): T1 node types.
    Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def create_snapshot(ReplicationGroupId=None, CacheClusterId=None, SnapshotName=None, KmsKeyId=None):
    """
    Creates a copy of an entire cluster or replication group at a specific moment in time.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a snapshot of a non-clustered Redis cluster that has only three nodes, primary and two read-replicas. CacheClusterId must be a specific node in the cluster.
    Expected Output:
    Creates a snapshot of a clustered Redis cluster that has 2 shards, each with a primary and 4 read-replicas.
    Expected Output:
    
    :example: response = client.create_snapshot(
        ReplicationGroupId='string',
        CacheClusterId='string',
        SnapshotName='string',
        KmsKeyId='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: The identifier of an existing replication group. The snapshot is created from this replication group.

    :type CacheClusterId: string
    :param CacheClusterId: The identifier of an existing cluster. The snapshot is created from this cluster.

    :type SnapshotName: string
    :param SnapshotName: [REQUIRED]\nA name for the snapshot being created.\n

    :type KmsKeyId: string
    :param KmsKeyId: The ID of the KMS key used to encrypt the snapshot.

    :rtype: dict

ReturnsResponse Syntax
{
    'Snapshot': {
        'SnapshotName': 'string',
        'ReplicationGroupId': 'string',
        'ReplicationGroupDescription': 'string',
        'CacheClusterId': 'string',
        'SnapshotStatus': 'string',
        'SnapshotSource': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'NumCacheNodes': 123,
        'PreferredAvailabilityZone': 'string',
        'CacheClusterCreateTime': datetime(2015, 1, 1),
        'PreferredMaintenanceWindow': 'string',
        'TopicArn': 'string',
        'Port': 123,
        'CacheParameterGroupName': 'string',
        'CacheSubnetGroupName': 'string',
        'VpcId': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'NumNodeGroups': 123,
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'NodeSnapshots': [
            {
                'CacheClusterId': 'string',
                'NodeGroupId': 'string',
                'CacheNodeId': 'string',
                'NodeGroupConfiguration': {
                    'NodeGroupId': 'string',
                    'Slots': 'string',
                    'ReplicaCount': 123,
                    'PrimaryAvailabilityZone': 'string',
                    'ReplicaAvailabilityZones': [
                        'string',
                    ]
                },
                'CacheSize': 'string',
                'CacheNodeCreateTime': datetime(2015, 1, 1),
                'SnapshotCreateTime': datetime(2015, 1, 1)
            },
        ],
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

Snapshot (dict) --
Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

SnapshotName (string) --
The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

ReplicationGroupId (string) --
The unique identifier of the source replication group.

ReplicationGroupDescription (string) --
A description of the source replication group.

CacheClusterId (string) --
The user-supplied identifier of the source cluster.

SnapshotStatus (string) --
The status of the snapshot. Valid values: creating | available | restoring | copying | deleting .

SnapshotSource (string) --
Indicates whether the snapshot is from an automatic backup (automated ) or was created manually (manual ).

CacheNodeType (string) --
The name of the compute and memory capacity node type for the source cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Engine (string) --
The name of the cache engine (memcached or redis ) used by the source cluster.

EngineVersion (string) --
The version of the cache engine version that is used by the source cluster.

NumCacheNodes (integer) --
The number of cache nodes in the source cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the source cluster is located.

CacheClusterCreateTime (datetime) --
The date and time when the source cluster was created.

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for ddd are:

sun
mon
tue
wed
thu
fri
sat

Example: sun:23:00-mon:01:30

TopicArn (string) --
The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

Port (integer) --
The port number used by each cache nodes in the source cluster.

CacheParameterGroupName (string) --
The cache parameter group that is associated with the source cluster.

CacheSubnetGroupName (string) --
The name of the cache subnet group associated with the source cluster.

VpcId (string) --
The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

AutoMinorVersionUpgrade (boolean) --
This parameter is currently disabled.

SnapshotRetentionLimit (integer) --
For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.
For manual snapshots, this field reflects the SnapshotRetentionLimit for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the DeleteSnapshot operation.

Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range during which ElastiCache takes daily snapshots of the source cluster.

NumNodeGroups (integer) --
The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


NodeSnapshots (list) --
A list of the cache nodes in the source cluster.

(dict) --
Represents an individual cache node in a snapshot of a cluster.

CacheClusterId (string) --
A unique identifier for the source cluster.

NodeGroupId (string) --
A unique identifier for the source node group (shard).

CacheNodeId (string) --
The cache node identifier for the node in the source cluster.

NodeGroupConfiguration (dict) --
The configuration for the source node group (shard).

NodeGroupId (string) --
Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.

Slots (string) --
A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format startkey-endkey .
Example: "0-3999"

ReplicaCount (integer) --
The number of read replica nodes in this node group (shard).

PrimaryAvailabilityZone (string) --
The Availability Zone where the primary node of this node group (shard) is launched.

ReplicaAvailabilityZones (list) --
A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ReplicaCount or ReplicasPerNodeGroup if not specified.

(string) --




CacheSize (string) --
The size of the cache on the source cache node.

CacheNodeCreateTime (datetime) --
The date and time when the cache node was created in the source cluster.

SnapshotCreateTime (datetime) --
The date and time when the source node\'s metadata and cache data set was obtained for the snapshot.





KmsKeyId (string) --
The ID of the KMS key used to encrypt the snapshot.

ARN (string) --
The ARN (Amazon Resource Name) of the snapshot.









Exceptions

ElastiCache.Client.exceptions.SnapshotAlreadyExistsFault
ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.SnapshotQuotaExceededFault
ElastiCache.Client.exceptions.SnapshotFeatureNotSupportedFault
ElastiCache.Client.exceptions.InvalidParameterCombinationException
ElastiCache.Client.exceptions.InvalidParameterValueException

Examples
Creates a snapshot of a non-clustered Redis cluster that has only three nodes, primary and two read-replicas. CacheClusterId must be a specific node in the cluster.
response = client.create_snapshot(
    CacheClusterId='threenoderedis-001',
    SnapshotName='snapshot-2',
)

print(response)


Expected Output:
{
    'Snapshot': {
        'AutoMinorVersionUpgrade': True,
        'CacheClusterCreateTime': datetime(2017, 2, 3, 15, 43, 36, 4, 34, 0),
        'CacheClusterId': 'threenoderedis-001',
        'CacheNodeType': 'cache.m3.medium',
        'CacheParameterGroupName': 'default.redis3.2',
        'CacheSubnetGroupName': 'default',
        'Engine': 'redis',
        'EngineVersion': '3.2.4',
        'NodeSnapshots': [
            {
                'CacheNodeCreateTime': datetime(2017, 2, 3, 15, 43, 36, 4, 34, 0),
                'CacheNodeId': '0001',
                'CacheSize': '',
            },
        ],
        'NumCacheNodes': 1,
        'Port': 6379,
        'PreferredAvailabilityZone': 'us-west-2c',
        'PreferredMaintenanceWindow': 'sat:08:00-sat:09:00',
        'SnapshotName': 'snapshot-2',
        'SnapshotRetentionLimit': 1,
        'SnapshotSource': 'manual',
        'SnapshotStatus': 'creating',
        'SnapshotWindow': '00:00-01:00',
        'VpcId': 'vpc-73c3cd17',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}


Creates a snapshot of a clustered Redis cluster that has 2 shards, each with a primary and 4 read-replicas.
response = client.create_snapshot(
    ReplicationGroupId='clusteredredis',
    SnapshotName='snapshot-2x5',
)

print(response)


Expected Output:
{
    'Snapshot': {
        'AutoMinorVersionUpgrade': True,
        'AutomaticFailover': 'enabled',
        'CacheNodeType': 'cache.m3.medium',
        'CacheParameterGroupName': 'default.redis3.2.cluster.on',
        'CacheSubnetGroupName': 'default',
        'Engine': 'redis',
        'EngineVersion': '3.2.4',
        'NodeSnapshots': [
            {
                'CacheSize': '',
                'NodeGroupId': '0001',
            },
            {
                'CacheSize': '',
                'NodeGroupId': '0002',
            },
        ],
        'NumNodeGroups': 2,
        'Port': 6379,
        'PreferredMaintenanceWindow': 'mon:09:30-mon:10:30',
        'ReplicationGroupDescription': 'Redis cluster with 2 shards.',
        'ReplicationGroupId': 'clusteredredis',
        'SnapshotName': 'snapshot-2x5',
        'SnapshotRetentionLimit': 1,
        'SnapshotSource': 'manual',
        'SnapshotStatus': 'creating',
        'SnapshotWindow': '12:00-13:00',
        'VpcId': 'vpc-73c3cd17',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Snapshot': {
            'SnapshotName': 'string',
            'ReplicationGroupId': 'string',
            'ReplicationGroupDescription': 'string',
            'CacheClusterId': 'string',
            'SnapshotStatus': 'string',
            'SnapshotSource': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'NumCacheNodes': 123,
            'PreferredAvailabilityZone': 'string',
            'CacheClusterCreateTime': datetime(2015, 1, 1),
            'PreferredMaintenanceWindow': 'string',
            'TopicArn': 'string',
            'Port': 123,
            'CacheParameterGroupName': 'string',
            'CacheSubnetGroupName': 'string',
            'VpcId': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'NumNodeGroups': 123,
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'NodeSnapshots': [
                {
                    'CacheClusterId': 'string',
                    'NodeGroupId': 'string',
                    'CacheNodeId': 'string',
                    'NodeGroupConfiguration': {
                        'NodeGroupId': 'string',
                        'Slots': 'string',
                        'ReplicaCount': 123,
                        'PrimaryAvailabilityZone': 'string',
                        'ReplicaAvailabilityZones': [
                            'string',
                        ]
                    },
                    'CacheSize': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'SnapshotCreateTime': datetime(2015, 1, 1)
                },
            ],
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
    Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
    
    
    Compute optimized:
    Previous generation: (not recommended)  C1 node types: cache.c1.xlarge
    
    
    Memory optimized:
    Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
    Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    
    
    
    """
    pass

def decrease_node_groups_in_global_replication_group(GlobalReplicationGroupId=None, NodeGroupCount=None, GlobalNodeGroupsToRemove=None, GlobalNodeGroupsToRetain=None, ApplyImmediately=None):
    """
    Decreases the number of node groups in a Global Datastore
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.decrease_node_groups_in_global_replication_group(
        GlobalReplicationGroupId='string',
        NodeGroupCount=123,
        GlobalNodeGroupsToRemove=[
            'string',
        ],
        GlobalNodeGroupsToRetain=[
            'string',
        ],
        ApplyImmediately=True|False
    )
    
    
    :type GlobalReplicationGroupId: string
    :param GlobalReplicationGroupId: [REQUIRED]\nThe name of the Global Datastore\n

    :type NodeGroupCount: integer
    :param NodeGroupCount: [REQUIRED]\nThe number of node groups (shards) that results from the modification of the shard configuration\n

    :type GlobalNodeGroupsToRemove: list
    :param GlobalNodeGroupsToRemove: If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. NodeGroupsToRemove is a list of NodeGroupIds to remove from the cluster. ElastiCache for Redis will attempt to remove all node groups listed by NodeGroupsToRemove from the cluster.\n\n(string) --\n\n

    :type GlobalNodeGroupsToRetain: list
    :param GlobalNodeGroupsToRetain: If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. NodeGroupsToRemove is a list of NodeGroupIds to remove from the cluster. ElastiCache for Redis will attempt to remove all node groups listed by NodeGroupsToRemove from the cluster.\n\n(string) --\n\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: [REQUIRED]\nIndicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is true.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalReplicationGroup': {
        'GlobalReplicationGroupId': 'string',
        'GlobalReplicationGroupDescription': 'string',
        'Status': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'Members': [
            {
                'ReplicationGroupId': 'string',
                'ReplicationGroupRegion': 'string',
                'Role': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'Status': 'string'
            },
        ],
        'ClusterEnabled': True|False,
        'GlobalNodeGroups': [
            {
                'GlobalNodeGroupId': 'string',
                'Slots': 'string'
            },
        ],
        'AuthTokenEnabled': True|False,
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

GlobalReplicationGroup (dict) --
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different AWS region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.


GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupDescription (string) --
The optional description of the Global Datastore

Status (string) --
The status of the Global Datastore

CacheNodeType (string) --
The cache node type of the Global Datastore

Engine (string) --
The Elasticache engine. For Redis only.

EngineVersion (string) --
The Elasticache Redis engine version. For preview, it is Redis version 5.0.5 only.

Members (list) --
The replication groups that comprise the Global Datastore.

(dict) --
A member of a Global Datastore. It contains the Replication Group Id, the AWS region and the role of the replication group.

ReplicationGroupId (string) --
The replication group id of the Global Datastore member.

ReplicationGroupRegion (string) --
The AWS region of the Global Datastore member.

Role (string) --
Indicates the role of the replication group, primary or secondary.

AutomaticFailover (string) --
Indicates whether automatic failover is enabled for the replication group.

Status (string) --
The status of the membership of the replication group.





ClusterEnabled (boolean) --
A flag that indicates whether the Global Datastore is cluster enabled.

GlobalNodeGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId (string) --
The name of the global node group

Slots (string) --
The keyspace for this node group





AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true. You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.


ARN (string) --
The ARN (Amazon Resource Name) of the global replication group.









Exceptions

ElastiCache.Client.exceptions.GlobalReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'GlobalReplicationGroup': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupDescription': 'string',
            'Status': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'Members': [
                {
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupRegion': 'string',
                    'Role': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'Status': 'string'
                },
            ],
            'ClusterEnabled': True|False,
            'GlobalNodeGroups': [
                {
                    'GlobalNodeGroupId': 'string',
                    'Slots': 'string'
                },
            ],
            'AuthTokenEnabled': True|False,
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.
    
    """
    pass

def decrease_replica_count(ReplicationGroupId=None, NewReplicaCount=None, ReplicaConfiguration=None, ReplicasToRemove=None, ApplyImmediately=None):
    """
    Dynamically decreases the number of replicas in a Redis (cluster mode disabled) replication group or the number of replica nodes in one or more node groups (shards) of a Redis (cluster mode enabled) replication group. This operation is performed with no cluster down time.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.decrease_replica_count(
        ReplicationGroupId='string',
        NewReplicaCount=123,
        ReplicaConfiguration=[
            {
                'NodeGroupId': 'string',
                'NewReplicaCount': 123,
                'PreferredAvailabilityZones': [
                    'string',
                ]
            },
        ],
        ReplicasToRemove=[
            'string',
        ],
        ApplyImmediately=True|False
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe id of the replication group from which you want to remove replica nodes.\n

    :type NewReplicaCount: integer
    :param NewReplicaCount: The number of read replica nodes you want at the completion of this operation. For Redis (cluster mode disabled) replication groups, this is the number of replica nodes in the replication group. For Redis (cluster mode enabled) replication groups, this is the number of replica nodes in each of the replication group\'s node groups.\nThe minimum number of replicas in a shard or replication group is:\n\nRedis (cluster mode disabled)\nIf Multi-AZ with Automatic Failover is enabled: 1\nIf Multi-AZ with Automatic Failover is not enabled: 0\n\n\nRedis (cluster mode enabled): 0 (though you will not be able to failover to a replica if your primary node fails)\n\n

    :type ReplicaConfiguration: list
    :param ReplicaConfiguration: A list of ConfigureShard objects that can be used to configure each shard in a Redis (cluster mode enabled) replication group. The ConfigureShard has three members: NewReplicaCount , NodeGroupId , and PreferredAvailabilityZones .\n\n(dict) --Node group (shard) configuration options when adding or removing replicas. Each node group (shard) configuration has the following members: NodeGroupId, NewReplicaCount, and PreferredAvailabilityZones.\n\nNodeGroupId (string) -- [REQUIRED]The 4-digit id for the node group you are configuring. For Redis (cluster mode disabled) replication groups, the node group id is always 0001. To find a Redis (cluster mode enabled)\'s node group\'s (shard\'s) id, see Finding a Shard\'s Id .\n\nNewReplicaCount (integer) -- [REQUIRED]The number of replicas you want in this node group at the end of this operation. The maximum value for NewReplicaCount is 5. The minimum value depends upon the type of Redis replication group you are working with.\nThe minimum number of replicas in a shard or replication group is:\n\nRedis (cluster mode disabled)\nIf Multi-AZ with Automatic Failover is enabled: 1\nIf Multi-AZ with Automatic Failover is not enable: 0\n\n\nRedis (cluster mode enabled): 0 (though you will not be able to failover to a replica if your primary node fails)\n\n\nPreferredAvailabilityZones (list) --A list of PreferredAvailabilityZone strings that specify which availability zones the replication group\'s nodes are to be in. The nummber of PreferredAvailabilityZone values must equal the value of NewReplicaCount plus 1 to account for the primary node. If this member of ReplicaConfiguration is omitted, ElastiCache for Redis selects the availability zone for each of the replicas.\n\n(string) --\n\n\n\n\n\n

    :type ReplicasToRemove: list
    :param ReplicasToRemove: A list of the node ids to remove from the replication group or node group (shard).\n\n(string) --\n\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: [REQUIRED]\nIf True , the number of replica nodes is decreased immediately. ApplyImmediately=False is not currently supported.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationGroup': {
        'ReplicationGroupId': 'string',
        'Description': 'string',
        'GlobalReplicationGroupInfo': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupMemberRole': 'string'
        },
        'Status': 'string',
        'PendingModifiedValues': {
            'PrimaryClusterId': 'string',
            'AutomaticFailoverStatus': 'enabled'|'disabled',
            'Resharding': {
                'SlotMigration': {
                    'ProgressPercentage': 123.0
                }
            },
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'MemberClusters': [
            'string',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': 'string',
                'Status': 'string',
                'PrimaryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ReaderEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'Slots': 'string',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'string',
                        'CacheNodeId': 'string',
                        'ReadEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'PreferredAvailabilityZone': 'string',
                        'CurrentRole': 'string'
                    },
                ]
            },
        ],
        'SnapshottingClusterId': 'string',
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'ClusterEnabled': True|False,
        'CacheNodeType': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

ReplicationGroup (dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.









Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.InvalidVPCNetworkStateFault
ElastiCache.Client.exceptions.InsufficientCacheClusterCapacityFault
ElastiCache.Client.exceptions.ClusterQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.NodeGroupsPerReplicationGroupQuotaExceededFault
ElastiCache.Client.exceptions.NodeQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.ServiceLinkedRoleNotFoundFault
ElastiCache.Client.exceptions.NoOperationFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled): T1 node types.
    Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def delete_cache_cluster(CacheClusterId=None, FinalSnapshotIdentifier=None):
    """
    Deletes a previously provisioned cluster. DeleteCacheCluster deletes all associated cache nodes, node endpoints and the cluster itself. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the cluster; you cannot cancel or revert this operation.
    This operation is not valid for:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes an Amazon ElastiCache cluster.
    Expected Output:
    
    :example: response = client.delete_cache_cluster(
        CacheClusterId='string',
        FinalSnapshotIdentifier='string'
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: [REQUIRED]\nThe cluster identifier for the cluster to be deleted. This parameter is not case sensitive.\n

    :type FinalSnapshotIdentifier: string
    :param FinalSnapshotIdentifier: The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cluster immediately afterward.

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheCluster': {
        'CacheClusterId': 'string',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClientDownloadLandingPage': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'CacheClusterStatus': 'string',
        'NumCacheNodes': 123,
        'PreferredAvailabilityZone': 'string',
        'CacheClusterCreateTime': datetime(2015, 1, 1),
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'NumCacheNodes': 123,
            'CacheNodeIdsToRemove': [
                'string',
            ],
            'EngineVersion': 'string',
            'CacheNodeType': 'string',
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'CacheSecurityGroups': [
            {
                'CacheSecurityGroupName': 'string',
                'Status': 'string'
            },
        ],
        'CacheParameterGroup': {
            'CacheParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'CacheNodeIdsToReboot': [
                'string',
            ]
        },
        'CacheSubnetGroupName': 'string',
        'CacheNodes': [
            {
                'CacheNodeId': 'string',
                'CacheNodeStatus': 'string',
                'CacheNodeCreateTime': datetime(2015, 1, 1),
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ParameterGroupStatus': 'string',
                'SourceCacheNodeId': 'string',
                'CustomerAvailabilityZone': 'string'
            },
        ],
        'AutoMinorVersionUpgrade': True|False,
        'SecurityGroups': [
            {
                'SecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'ReplicationGroupId': 'string',
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheCluster (dict) --
Contains all of the attributes of a specific cluster.

CacheClusterId (string) --
The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

ConfigurationEndpoint (dict) --
Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have .cfg in it.
Example: mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ClientDownloadLandingPage (string) --
The URL of the web page where you can download the latest ElastiCache client library.

CacheNodeType (string) --
The name of the compute and memory capacity node type for the cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Engine (string) --
The name of the cache engine (memcached or redis ) to be used for this cluster.

EngineVersion (string) --
The version of the cache engine that is used in this cluster.

CacheClusterStatus (string) --
The current state of this cluster, one of the following values: available , creating , deleted , deleting , incompatible-network , modifying , rebooting cluster nodes , restore-failed , or snapshotting .

NumCacheNodes (integer) --
The number of cache nodes in the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

CacheClusterCreateTime (datetime) --
The date and time when the cluster was created.

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for ddd are:

sun
mon
tue
wed
thu
fri
sat

Example: sun:23:00-mon:01:30

PendingModifiedValues (dict) --
A group of settings that are applied to the cluster in the future, or that are currently being applied.

NumCacheNodes (integer) --
The new number of cache nodes for the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

CacheNodeIdsToRemove (list) --
A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

(string) --


EngineVersion (string) --
The new cache engine version that the cluster runs.

CacheNodeType (string) --
The cache node type that this cluster or replication group is scaled to.

AuthTokenStatus (string) --
The auth token status



NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



CacheSecurityGroups (list) --
A list of cache security group elements, composed of name and status sub-elements.

(dict) --
Represents a cluster\'s status within a particular cache security group.

CacheSecurityGroupName (string) --
The name of the cache security group.

Status (string) --
The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





CacheParameterGroup (dict) --
Status of the cache parameter group.

CacheParameterGroupName (string) --
The name of the cache parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

CacheNodeIdsToReboot (list) --
A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

(string) --




CacheSubnetGroupName (string) --
The name of the cache subnet group associated with the cluster.

CacheNodes (list) --
A list of cache nodes that are members of the cluster.

(dict) --
Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster\'s protocol-compliant caching software - either Memcached or Redis.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


CacheNodeId (string) --
The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer\'s AWS account.

CacheNodeStatus (string) --
The current state of this cache node, one of the following values: available , creating , rebooting , or deleting .

CacheNodeCreateTime (datetime) --
The date and time when the cache node was created.

Endpoint (dict) --
The hostname for connecting to this cache node.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ParameterGroupStatus (string) --
The status of the parameter group applied to this cache node.

SourceCacheNodeId (string) --
The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

CustomerAvailabilityZone (string) --
The Availability Zone where this node was created and now resides.





AutoMinorVersionUpgrade (boolean) --
This parameter is currently disabled.

SecurityGroups (list) --
A list of VPC Security Groups associated with the cluster.

(dict) --
Represents a single cache security group and its status.

SecurityGroupId (string) --
The identifier of the cache security group.

Status (string) --
The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





ReplicationGroupId (string) --
The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.
Example: 05:00-09:00

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable at-rest encryption on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

ARN (string) --
The ARN (Amazon Resource Name) of the cache cluster.









Exceptions

ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.SnapshotAlreadyExistsFault
ElastiCache.Client.exceptions.SnapshotFeatureNotSupportedFault
ElastiCache.Client.exceptions.SnapshotQuotaExceededFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Deletes an Amazon ElastiCache cluster.
response = client.delete_cache_cluster(
    CacheClusterId='my-memcached',
)

print(response)


Expected Output:
{
    'CacheCluster': {
        'AutoMinorVersionUpgrade': True,
        'CacheClusterCreateTime': datetime(2016, 12, 22, 16, 5, 17, 3, 357, 0),
        'CacheClusterId': 'my-memcached',
        'CacheClusterStatus': 'deleting',
        'CacheNodeType': 'cache.r3.large',
        'CacheParameterGroup': {
            'CacheNodeIdsToReboot': [
            ],
            'CacheParameterGroupName': 'default.memcached1.4',
            'ParameterApplyStatus': 'in-sync',
        },
        'CacheSecurityGroups': [
        ],
        'CacheSubnetGroupName': 'default',
        'ClientDownloadLandingPage': 'https://console.aws.amazon.com/elasticache/home#client-download:',
        'ConfigurationEndpoint': {
            'Address': 'my-memcached2.ameaqx.cfg.use1.cache.amazonaws.com',
            'Port': 11211,
        },
        'Engine': 'memcached',
        'EngineVersion': '1.4.24',
        'NumCacheNodes': 2,
        'PendingModifiedValues': {
        },
        'PreferredAvailabilityZone': 'Multiple',
        'PreferredMaintenanceWindow': 'tue:07:30-tue:08:30',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheCluster': {
            'CacheClusterId': 'string',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClientDownloadLandingPage': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'CacheClusterStatus': 'string',
            'NumCacheNodes': 123,
            'PreferredAvailabilityZone': 'string',
            'CacheClusterCreateTime': datetime(2015, 1, 1),
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'NumCacheNodes': 123,
                'CacheNodeIdsToRemove': [
                    'string',
                ],
                'EngineVersion': 'string',
                'CacheNodeType': 'string',
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'CacheSecurityGroups': [
                {
                    'CacheSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CacheParameterGroup': {
                'CacheParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'CacheNodeIdsToReboot': [
                    'string',
                ]
            },
            'CacheSubnetGroupName': 'string',
            'CacheNodes': [
                {
                    'CacheNodeId': 'string',
                    'CacheNodeStatus': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ParameterGroupStatus': 'string',
                    'SourceCacheNodeId': 'string',
                    'CustomerAvailabilityZone': 'string'
                },
            ],
            'AutoMinorVersionUpgrade': True|False,
            'SecurityGroups': [
                {
                    'SecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'ReplicationGroupId': 'string',
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    CacheClusterId (string) -- [REQUIRED]
    The cluster identifier for the cluster to be deleted. This parameter is not case sensitive.
    
    FinalSnapshotIdentifier (string) -- The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cluster immediately afterward.
    
    """
    pass

def delete_cache_parameter_group(CacheParameterGroupName=None):
    """
    Deletes the specified cache parameter group. You cannot delete a cache parameter group if it is associated with any cache clusters.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the Amazon ElastiCache parameter group custom-mem1-4.
    Expected Output:
    
    :example: response = client.delete_cache_parameter_group(
        CacheParameterGroupName='string'
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: [REQUIRED]\nThe name of the cache parameter group to delete.\n\nNote\nThe specified cache security group must not be associated with any clusters.\n\n

    :return: response = client.delete_cache_parameter_group(
        CacheParameterGroupName='custom-mem1-4',
    )
    
    print(response)
    
    
    """
    pass

def delete_cache_security_group(CacheSecurityGroupName=None):
    """
    Deletes a cache security group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes a cache security group.
    Expected Output:
    
    :example: response = client.delete_cache_security_group(
        CacheSecurityGroupName='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: [REQUIRED]\nThe name of the cache security group to delete.\n\nNote\nYou cannot delete the default security group.\n\n

    :return: response = client.delete_cache_security_group(
        CacheSecurityGroupName='my-sec-group',
    )
    
    print(response)
    
    
    """
    pass

def delete_cache_subnet_group(CacheSubnetGroupName=None):
    """
    Deletes a cache subnet group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the Amazon ElastiCache subnet group my-subnet-group.
    Expected Output:
    
    :example: response = client.delete_cache_subnet_group(
        CacheSubnetGroupName='string'
    )
    
    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: [REQUIRED]\nThe name of the cache subnet group to delete.\nConstraints: Must contain no more than 255 alphanumeric characters or hyphens.\n

    :return: response = client.delete_cache_subnet_group(
        CacheSubnetGroupName='my-subnet-group',
    )
    
    print(response)
    
    
    """
    pass

def delete_global_replication_group(GlobalReplicationGroupId=None, RetainPrimaryReplicationGroup=None):
    """
    Deleting a Global Datastore is a two-step process:
    Since the Global Datastore has only a primary cluster, you can delete the Global Datastore while retaining the primary by setting RetainPrimaryCluster=true .
    When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_global_replication_group(
        GlobalReplicationGroupId='string',
        RetainPrimaryReplicationGroup=True|False
    )
    
    
    :type GlobalReplicationGroupId: string
    :param GlobalReplicationGroupId: [REQUIRED]\nThe name of the Global Datastore\n

    :type RetainPrimaryReplicationGroup: boolean
    :param RetainPrimaryReplicationGroup: [REQUIRED]\nThe primary replication group is retained as a standalone replication group.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalReplicationGroup': {
        'GlobalReplicationGroupId': 'string',
        'GlobalReplicationGroupDescription': 'string',
        'Status': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'Members': [
            {
                'ReplicationGroupId': 'string',
                'ReplicationGroupRegion': 'string',
                'Role': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'Status': 'string'
            },
        ],
        'ClusterEnabled': True|False,
        'GlobalNodeGroups': [
            {
                'GlobalNodeGroupId': 'string',
                'Slots': 'string'
            },
        ],
        'AuthTokenEnabled': True|False,
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

GlobalReplicationGroup (dict) --
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different AWS region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.


GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupDescription (string) --
The optional description of the Global Datastore

Status (string) --
The status of the Global Datastore

CacheNodeType (string) --
The cache node type of the Global Datastore

Engine (string) --
The Elasticache engine. For Redis only.

EngineVersion (string) --
The Elasticache Redis engine version. For preview, it is Redis version 5.0.5 only.

Members (list) --
The replication groups that comprise the Global Datastore.

(dict) --
A member of a Global Datastore. It contains the Replication Group Id, the AWS region and the role of the replication group.

ReplicationGroupId (string) --
The replication group id of the Global Datastore member.

ReplicationGroupRegion (string) --
The AWS region of the Global Datastore member.

Role (string) --
Indicates the role of the replication group, primary or secondary.

AutomaticFailover (string) --
Indicates whether automatic failover is enabled for the replication group.

Status (string) --
The status of the membership of the replication group.





ClusterEnabled (boolean) --
A flag that indicates whether the Global Datastore is cluster enabled.

GlobalNodeGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId (string) --
The name of the global node group

Slots (string) --
The keyspace for this node group





AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true. You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.


ARN (string) --
The ARN (Amazon Resource Name) of the global replication group.









Exceptions

ElastiCache.Client.exceptions.GlobalReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException


    :return: {
        'GlobalReplicationGroup': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupDescription': 'string',
            'Status': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'Members': [
                {
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupRegion': 'string',
                    'Role': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'Status': 'string'
                },
            ],
            'ClusterEnabled': True|False,
            'GlobalNodeGroups': [
                {
                    'GlobalNodeGroupId': 'string',
                    'Slots': 'string'
                },
            ],
            'AuthTokenEnabled': True|False,
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    GlobalReplicationGroupId (string) -- [REQUIRED]
    The name of the Global Datastore
    
    RetainPrimaryReplicationGroup (boolean) -- [REQUIRED]
    The primary replication group is retained as a standalone replication group.
    
    
    """
    pass

def delete_replication_group(ReplicationGroupId=None, RetainPrimaryCluster=None, FinalSnapshotIdentifier=None):
    """
    Deletes an existing replication group. By default, this operation deletes the entire replication group, including the primary/primaries and all of the read replicas. If the replication group has only one primary, you can optionally delete only the read replicas, while retaining the primary by setting RetainPrimaryCluster=true .
    When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the Amazon ElastiCache replication group my-redis-rg.
    Expected Output:
    
    :example: response = client.delete_replication_group(
        ReplicationGroupId='string',
        RetainPrimaryCluster=True|False,
        FinalSnapshotIdentifier='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe identifier for the cluster to be deleted. This parameter is not case sensitive.\n

    :type RetainPrimaryCluster: boolean
    :param RetainPrimaryCluster: If set to true , all of the read replicas are deleted, but the primary node is retained.

    :type FinalSnapshotIdentifier: string
    :param FinalSnapshotIdentifier: The name of a final node group (shard) snapshot. ElastiCache creates the snapshot from the primary node in the cluster, rather than one of the replicas; this is to ensure that it captures the freshest data. After the final snapshot is taken, the replication group is immediately deleted.

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationGroup': {
        'ReplicationGroupId': 'string',
        'Description': 'string',
        'GlobalReplicationGroupInfo': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupMemberRole': 'string'
        },
        'Status': 'string',
        'PendingModifiedValues': {
            'PrimaryClusterId': 'string',
            'AutomaticFailoverStatus': 'enabled'|'disabled',
            'Resharding': {
                'SlotMigration': {
                    'ProgressPercentage': 123.0
                }
            },
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'MemberClusters': [
            'string',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': 'string',
                'Status': 'string',
                'PrimaryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ReaderEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'Slots': 'string',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'string',
                        'CacheNodeId': 'string',
                        'ReadEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'PreferredAvailabilityZone': 'string',
                        'CurrentRole': 'string'
                    },
                ]
            },
        ],
        'SnapshottingClusterId': 'string',
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'ClusterEnabled': True|False,
        'CacheNodeType': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

ReplicationGroup (dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.









Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.SnapshotAlreadyExistsFault
ElastiCache.Client.exceptions.SnapshotFeatureNotSupportedFault
ElastiCache.Client.exceptions.SnapshotQuotaExceededFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Deletes the Amazon ElastiCache replication group my-redis-rg.
response = client.delete_replication_group(
    ReplicationGroupId='my-redis-rg',
    RetainPrimaryCluster=False,
)

print(response)


Expected Output:
{
    'ReplicationGroup': {
        'AutomaticFailover': 'disabled',
        'Description': 'simple redis cluster',
        'PendingModifiedValues': {
        },
        'ReplicationGroupId': 'my-redis-rg',
        'Status': 'deleting',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled): T1 node types.
    Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def delete_snapshot(SnapshotName=None):
    """
    Deletes an existing snapshot. When you receive a successful response from this operation, ElastiCache immediately begins deleting the snapshot; you cannot cancel or revert this operation.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the Redis snapshot snapshot-20160822.
    Expected Output:
    
    :example: response = client.delete_snapshot(
        SnapshotName='string'
    )
    
    
    :type SnapshotName: string
    :param SnapshotName: [REQUIRED]\nThe name of the snapshot to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Snapshot': {
        'SnapshotName': 'string',
        'ReplicationGroupId': 'string',
        'ReplicationGroupDescription': 'string',
        'CacheClusterId': 'string',
        'SnapshotStatus': 'string',
        'SnapshotSource': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'NumCacheNodes': 123,
        'PreferredAvailabilityZone': 'string',
        'CacheClusterCreateTime': datetime(2015, 1, 1),
        'PreferredMaintenanceWindow': 'string',
        'TopicArn': 'string',
        'Port': 123,
        'CacheParameterGroupName': 'string',
        'CacheSubnetGroupName': 'string',
        'VpcId': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'NumNodeGroups': 123,
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'NodeSnapshots': [
            {
                'CacheClusterId': 'string',
                'NodeGroupId': 'string',
                'CacheNodeId': 'string',
                'NodeGroupConfiguration': {
                    'NodeGroupId': 'string',
                    'Slots': 'string',
                    'ReplicaCount': 123,
                    'PrimaryAvailabilityZone': 'string',
                    'ReplicaAvailabilityZones': [
                        'string',
                    ]
                },
                'CacheSize': 'string',
                'CacheNodeCreateTime': datetime(2015, 1, 1),
                'SnapshotCreateTime': datetime(2015, 1, 1)
            },
        ],
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --
Snapshot (dict) --Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

SnapshotName (string) --The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

ReplicationGroupId (string) --The unique identifier of the source replication group.

ReplicationGroupDescription (string) --A description of the source replication group.

CacheClusterId (string) --The user-supplied identifier of the source cluster.

SnapshotStatus (string) --The status of the snapshot. Valid values: creating | available | restoring | copying | deleting .

SnapshotSource (string) --Indicates whether the snapshot is from an automatic backup (automated ) or was created manually (manual ).

CacheNodeType (string) --The name of the compute and memory capacity node type for the source cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info

All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Engine (string) --The name of the cache engine (memcached or redis ) used by the source cluster.

EngineVersion (string) --The version of the cache engine version that is used by the source cluster.

NumCacheNodes (integer) --The number of cache nodes in the source cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

PreferredAvailabilityZone (string) --The name of the Availability Zone in which the source cluster is located.

CacheClusterCreateTime (datetime) --The date and time when the source cluster was created.

PreferredMaintenanceWindow (string) --Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for ddd are:

sun
mon
tue
wed
thu
fri
sat

Example: sun:23:00-mon:01:30

TopicArn (string) --The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

Port (integer) --The port number used by each cache nodes in the source cluster.

CacheParameterGroupName (string) --The cache parameter group that is associated with the source cluster.

CacheSubnetGroupName (string) --The name of the cache subnet group associated with the source cluster.

VpcId (string) --The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

AutoMinorVersionUpgrade (boolean) --This parameter is currently disabled.

SnapshotRetentionLimit (integer) --For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.
For manual snapshots, this field reflects the SnapshotRetentionLimit for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the DeleteSnapshot operation.

Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

SnapshotWindow (string) --The daily time range during which ElastiCache takes daily snapshots of the source cluster.

NumNodeGroups (integer) --The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

AutomaticFailover (string) --Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


NodeSnapshots (list) --A list of the cache nodes in the source cluster.

(dict) --Represents an individual cache node in a snapshot of a cluster.

CacheClusterId (string) --A unique identifier for the source cluster.

NodeGroupId (string) --A unique identifier for the source node group (shard).

CacheNodeId (string) --The cache node identifier for the node in the source cluster.

NodeGroupConfiguration (dict) --The configuration for the source node group (shard).

NodeGroupId (string) --Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.

Slots (string) --A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format startkey-endkey .
Example: "0-3999"

ReplicaCount (integer) --The number of read replica nodes in this node group (shard).

PrimaryAvailabilityZone (string) --The Availability Zone where the primary node of this node group (shard) is launched.

ReplicaAvailabilityZones (list) --A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ReplicaCount or ReplicasPerNodeGroup if not specified.

(string) --




CacheSize (string) --The size of the cache on the source cache node.

CacheNodeCreateTime (datetime) --The date and time when the cache node was created in the source cluster.

SnapshotCreateTime (datetime) --The date and time when the source node\'s metadata and cache data set was obtained for the snapshot.





KmsKeyId (string) --The ID of the KMS key used to encrypt the snapshot.

ARN (string) --The ARN (Amazon Resource Name) of the snapshot.








Exceptions

ElastiCache.Client.exceptions.SnapshotNotFoundFault
ElastiCache.Client.exceptions.InvalidSnapshotStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Deletes the Redis snapshot snapshot-20160822.
response = client.delete_snapshot(
    SnapshotName='snapshot-20161212',
)

print(response)


Expected Output:
{
    'Snapshot': {
        'AutoMinorVersionUpgrade': True,
        'CacheClusterCreateTime': datetime(2016, 12, 21, 22, 27, 12, 2, 356, 0),
        'CacheClusterId': 'my-redis5',
        'CacheNodeType': 'cache.m3.large',
        'CacheParameterGroupName': 'default.redis3.2',
        'CacheSubnetGroupName': 'default',
        'Engine': 'redis',
        'EngineVersion': '3.2.4',
        'NodeSnapshots': [
            {
                'CacheNodeCreateTime': datetime(2016, 12, 21, 22, 27, 12, 2, 356, 0),
                'CacheNodeId': '0001',
                'CacheSize': '3 MB',
                'SnapshotCreateTime': datetime(2016, 12, 21, 22, 30, 26, 2, 356, 0),
            },
        ],
        'NumCacheNodes': 1,
        'Port': 6379,
        'PreferredAvailabilityZone': 'us-east-1c',
        'PreferredMaintenanceWindow': 'fri:05:30-fri:06:30',
        'SnapshotName': 'snapshot-20161212',
        'SnapshotRetentionLimit': 7,
        'SnapshotSource': 'manual',
        'SnapshotStatus': 'deleting',
        'SnapshotWindow': '10:00-11:00',
        'VpcId': 'vpc-91280df6',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Snapshot': {
            'SnapshotName': 'string',
            'ReplicationGroupId': 'string',
            'ReplicationGroupDescription': 'string',
            'CacheClusterId': 'string',
            'SnapshotStatus': 'string',
            'SnapshotSource': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'NumCacheNodes': 123,
            'PreferredAvailabilityZone': 'string',
            'CacheClusterCreateTime': datetime(2015, 1, 1),
            'PreferredMaintenanceWindow': 'string',
            'TopicArn': 'string',
            'Port': 123,
            'CacheParameterGroupName': 'string',
            'CacheSubnetGroupName': 'string',
            'VpcId': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'NumNodeGroups': 123,
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'NodeSnapshots': [
                {
                    'CacheClusterId': 'string',
                    'NodeGroupId': 'string',
                    'CacheNodeId': 'string',
                    'NodeGroupConfiguration': {
                        'NodeGroupId': 'string',
                        'Slots': 'string',
                        'ReplicaCount': 123,
                        'PrimaryAvailabilityZone': 'string',
                        'ReplicaAvailabilityZones': [
                            'string',
                        ]
                    },
                    'CacheSize': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'SnapshotCreateTime': datetime(2015, 1, 1)
                },
            ],
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    All current generation instance types are created in Amazon VPC by default.
    Redis append-only files (AOF) are not supported for T1 or T2 instances.
    Redis Multi-AZ with automatic failover is not supported on T1 instances.
    Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.
    
    """
    pass

def describe_cache_clusters(CacheClusterId=None, MaxRecords=None, Marker=None, ShowCacheNodeInfo=None, ShowCacheClustersNotInReplicationGroups=None):
    """
    Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cache cluster if a cluster identifier is supplied.
    By default, abbreviated information about the clusters is returned. You can use the optional ShowCacheNodeInfo flag to retrieve detailed information about the cache nodes associated with the clusters. These details include the DNS address and port for the cache node endpoint.
    If the cluster is in the creating state, only cluster-level information is displayed until all of the nodes are successfully provisioned.
    If the cluster is in the deleting state, only cluster-level information is displayed.
    If cache nodes are currently being added to the cluster, node endpoint information and creation time for the additional nodes are not displayed until they are completely provisioned. When the cluster state is available , the cluster is ready for use.
    If cache nodes are currently being removed from the cluster, no endpoint information for the removed nodes is displayed.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists the details for the cache cluster my-mem-cluster.
    Expected Output:
    
    :example: response = client.describe_cache_clusters(
        CacheClusterId='string',
        MaxRecords=123,
        Marker='string',
        ShowCacheNodeInfo=True|False,
        ShowCacheClustersNotInReplicationGroups=True|False
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn\'t case sensitive.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type ShowCacheNodeInfo: boolean
    :param ShowCacheNodeInfo: An optional flag that can be included in the DescribeCacheCluster request to retrieve information about the individual cache nodes.

    :type ShowCacheClustersNotInReplicationGroups: boolean
    :param ShowCacheClustersNotInReplicationGroups: An optional flag that can be included in the DescribeCacheCluster request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this mean Memcached and single node Redis clusters.

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'CacheClusters': [
        {
            'CacheClusterId': 'string',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClientDownloadLandingPage': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'CacheClusterStatus': 'string',
            'NumCacheNodes': 123,
            'PreferredAvailabilityZone': 'string',
            'CacheClusterCreateTime': datetime(2015, 1, 1),
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'NumCacheNodes': 123,
                'CacheNodeIdsToRemove': [
                    'string',
                ],
                'EngineVersion': 'string',
                'CacheNodeType': 'string',
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'CacheSecurityGroups': [
                {
                    'CacheSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CacheParameterGroup': {
                'CacheParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'CacheNodeIdsToReboot': [
                    'string',
                ]
            },
            'CacheSubnetGroupName': 'string',
            'CacheNodes': [
                {
                    'CacheNodeId': 'string',
                    'CacheNodeStatus': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ParameterGroupStatus': 'string',
                    'SourceCacheNodeId': 'string',
                    'CustomerAvailabilityZone': 'string'
                },
            ],
            'AutoMinorVersionUpgrade': True|False,
            'SecurityGroups': [
                {
                    'SecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'ReplicationGroupId': 'string',
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeCacheClusters operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

CacheClusters (list) --
A list of clusters. Each item in the list contains detailed information about one cluster.

(dict) --
Contains all of the attributes of a specific cluster.

CacheClusterId (string) --
The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

ConfigurationEndpoint (dict) --
Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have .cfg in it.
Example: mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ClientDownloadLandingPage (string) --
The URL of the web page where you can download the latest ElastiCache client library.

CacheNodeType (string) --
The name of the compute and memory capacity node type for the cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Engine (string) --
The name of the cache engine (memcached or redis ) to be used for this cluster.

EngineVersion (string) --
The version of the cache engine that is used in this cluster.

CacheClusterStatus (string) --
The current state of this cluster, one of the following values: available , creating , deleted , deleting , incompatible-network , modifying , rebooting cluster nodes , restore-failed , or snapshotting .

NumCacheNodes (integer) --
The number of cache nodes in the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

CacheClusterCreateTime (datetime) --
The date and time when the cluster was created.

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for ddd are:

sun
mon
tue
wed
thu
fri
sat

Example: sun:23:00-mon:01:30

PendingModifiedValues (dict) --
A group of settings that are applied to the cluster in the future, or that are currently being applied.

NumCacheNodes (integer) --
The new number of cache nodes for the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

CacheNodeIdsToRemove (list) --
A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

(string) --


EngineVersion (string) --
The new cache engine version that the cluster runs.

CacheNodeType (string) --
The cache node type that this cluster or replication group is scaled to.

AuthTokenStatus (string) --
The auth token status



NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



CacheSecurityGroups (list) --
A list of cache security group elements, composed of name and status sub-elements.

(dict) --
Represents a cluster\'s status within a particular cache security group.

CacheSecurityGroupName (string) --
The name of the cache security group.

Status (string) --
The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





CacheParameterGroup (dict) --
Status of the cache parameter group.

CacheParameterGroupName (string) --
The name of the cache parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

CacheNodeIdsToReboot (list) --
A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

(string) --




CacheSubnetGroupName (string) --
The name of the cache subnet group associated with the cluster.

CacheNodes (list) --
A list of cache nodes that are members of the cluster.

(dict) --
Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster\'s protocol-compliant caching software - either Memcached or Redis.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


CacheNodeId (string) --
The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer\'s AWS account.

CacheNodeStatus (string) --
The current state of this cache node, one of the following values: available , creating , rebooting , or deleting .

CacheNodeCreateTime (datetime) --
The date and time when the cache node was created.

Endpoint (dict) --
The hostname for connecting to this cache node.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ParameterGroupStatus (string) --
The status of the parameter group applied to this cache node.

SourceCacheNodeId (string) --
The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

CustomerAvailabilityZone (string) --
The Availability Zone where this node was created and now resides.





AutoMinorVersionUpgrade (boolean) --
This parameter is currently disabled.

SecurityGroups (list) --
A list of VPC Security Groups associated with the cluster.

(dict) --
Represents a single cache security group and its status.

SecurityGroupId (string) --
The identifier of the cache security group.

Status (string) --
The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





ReplicationGroupId (string) --
The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.
Example: 05:00-09:00

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable at-rest encryption on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

ARN (string) --
The ARN (Amazon Resource Name) of the cache cluster.











Exceptions

ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Lists the details for the cache cluster my-mem-cluster.
response = client.describe_cache_clusters(
    CacheClusterId='my-mem-cluster',
    ShowCacheNodeInfo=True,
)

print(response)


Expected Output:
{
    'CacheClusters': [
        {
            'AutoMinorVersionUpgrade': True,
            'CacheClusterCreateTime': datetime(2016, 12, 21, 21, 59, 43, 2, 356, 0),
            'CacheClusterId': 'my-mem-cluster',
            'CacheClusterStatus': 'available',
            'CacheNodeType': 'cache.t2.medium',
            'CacheNodes': [
                {
                    'CacheNodeCreateTime': datetime(2016, 12, 21, 21, 59, 43, 2, 356, 0),
                    'CacheNodeId': '0001',
                    'CacheNodeStatus': 'available',
                    'CustomerAvailabilityZone': 'us-east-1b',
                    'Endpoint': {
                        'Address': 'my-mem-cluster.ameaqx.0001.use1.cache.amazonaws.com',
                        'Port': 11211,
                    },
                    'ParameterGroupStatus': 'in-sync',
                },
                {
                    'CacheNodeCreateTime': datetime(2016, 12, 21, 21, 59, 43, 2, 356, 0),
                    'CacheNodeId': '0002',
                    'CacheNodeStatus': 'available',
                    'CustomerAvailabilityZone': 'us-east-1a',
                    'Endpoint': {
                        'Address': 'my-mem-cluster.ameaqx.0002.use1.cache.amazonaws.com',
                        'Port': 11211,
                    },
                    'ParameterGroupStatus': 'in-sync',
                },
            ],
            'CacheParameterGroup': {
                'CacheNodeIdsToReboot': [
                ],
                'CacheParameterGroupName': 'default.memcached1.4',
                'ParameterApplyStatus': 'in-sync',
            },
            'CacheSecurityGroups': [
            ],
            'CacheSubnetGroupName': 'default',
            'ClientDownloadLandingPage': 'https://console.aws.amazon.com/elasticache/home#client-download:',
            'ConfigurationEndpoint': {
                'Address': 'my-mem-cluster.ameaqx.cfg.use1.cache.amazonaws.com',
                'Port': 11211,
            },
            'Engine': 'memcached',
            'EngineVersion': '1.4.24',
            'NumCacheNodes': 2,
            'PendingModifiedValues': {
            },
            'PreferredAvailabilityZone': 'Multiple',
            'PreferredMaintenanceWindow': 'wed:06:00-wed:07:00',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'CacheClusters': [
            {
                'CacheClusterId': 'string',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ClientDownloadLandingPage': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'CacheClusterStatus': 'string',
                'NumCacheNodes': 123,
                'PreferredAvailabilityZone': 'string',
                'CacheClusterCreateTime': datetime(2015, 1, 1),
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                    'NumCacheNodes': 123,
                    'CacheNodeIdsToRemove': [
                        'string',
                    ],
                    'EngineVersion': 'string',
                    'CacheNodeType': 'string',
                    'AuthTokenStatus': 'SETTING'|'ROTATING'
                },
                'NotificationConfiguration': {
                    'TopicArn': 'string',
                    'TopicStatus': 'string'
                },
                'CacheSecurityGroups': [
                    {
                        'CacheSecurityGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'CacheParameterGroup': {
                    'CacheParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'CacheNodeIdsToReboot': [
                        'string',
                    ]
                },
                'CacheSubnetGroupName': 'string',
                'CacheNodes': [
                    {
                        'CacheNodeId': 'string',
                        'CacheNodeStatus': 'string',
                        'CacheNodeCreateTime': datetime(2015, 1, 1),
                        'Endpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'ParameterGroupStatus': 'string',
                        'SourceCacheNodeId': 'string',
                        'CustomerAvailabilityZone': 'string'
                    },
                ],
                'AutoMinorVersionUpgrade': True|False,
                'SecurityGroups': [
                    {
                        'SecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'ReplicationGroupId': 'string',
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'AuthTokenEnabled': True|False,
                'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False,
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    General purpose:
    Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
    Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
    
    
    Compute optimized:
    Previous generation: (not recommended)  C1 node types: cache.c1.xlarge
    
    
    Memory optimized:
    Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
    Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    
    
    
    """
    pass

def describe_cache_engine_versions(Engine=None, EngineVersion=None, CacheParameterGroupFamily=None, MaxRecords=None, Marker=None, DefaultOnly=None):
    """
    Returns a list of the available cache engines and their versions.
    See also: AWS API Documentation
    
    Examples
    Lists the details for up to 50 Redis cache engine versions.
    Expected Output:
    
    :example: response = client.describe_cache_engine_versions(
        Engine='string',
        EngineVersion='string',
        CacheParameterGroupFamily='string',
        MaxRecords=123,
        Marker='string',
        DefaultOnly=True|False
    )
    
    
    :type Engine: string
    :param Engine: The cache engine to return. Valid values: memcached | redis

    :type EngineVersion: string
    :param EngineVersion: The cache engine version to return.\nExample: 1.4.14\n

    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: The name of a specific cache parameter group family to return details for.\nValid values are: memcached1.4 | memcached1.5 | redis2.6 | redis2.8 | redis3.2 | redis4.0 | redis5.0 |\nConstraints:\n\nMust be 1 to 255 alphanumeric characters\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type DefaultOnly: boolean
    :param DefaultOnly: If true , specifies that only the default version of the specified engine or engine and major version combination is to be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'CacheEngineVersions': [
        {
            'Engine': 'string',
            'EngineVersion': 'string',
            'CacheParameterGroupFamily': 'string',
            'CacheEngineDescription': 'string',
            'CacheEngineVersionDescription': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a  DescribeCacheEngineVersions operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

CacheEngineVersions (list) --
A list of cache engine version details. Each element in the list contains detailed information about one cache engine version.

(dict) --
Provides all of the details about a particular cache engine version.

Engine (string) --
The name of the cache engine.

EngineVersion (string) --
The version number of the cache engine.

CacheParameterGroupFamily (string) --
The name of the cache parameter group family associated with this cache engine.
Valid values are: memcached1.4 | memcached1.5 | redis2.6 | redis2.8 | redis3.2 | redis4.0 | redis5.0 |

CacheEngineDescription (string) --
The description of the cache engine.

CacheEngineVersionDescription (string) --
The description of the cache engine version.











Examples
Lists the details for up to 50 Redis cache engine versions.
response = client.describe_cache_engine_versions(
    DefaultOnly=False,
    Engine='redis',
    MaxRecords=50,
)

print(response)


Expected Output:
{
    'CacheEngineVersions': [
        {
            'CacheEngineDescription': 'Redis',
            'CacheEngineVersionDescription': 'redis version 2.6.13',
            'CacheParameterGroupFamily': 'redis2.6',
            'Engine': 'redis',
            'EngineVersion': '2.6.13',
        },
        {
            'CacheEngineDescription': 'Redis',
            'CacheEngineVersionDescription': 'redis version 2.8.19',
            'CacheParameterGroupFamily': 'redis2.8',
            'Engine': 'redis',
            'EngineVersion': '2.8.19',
        },
        {
            'CacheEngineDescription': 'Redis',
            'CacheEngineVersionDescription': 'redis version 2.8.21',
            'CacheParameterGroupFamily': 'redis2.8',
            'Engine': 'redis',
            'EngineVersion': '2.8.21',
        },
        {
            'CacheEngineDescription': 'Redis',
            'CacheEngineVersionDescription': 'redis version 2.8.22 R5',
            'CacheParameterGroupFamily': 'redis2.8',
            'Engine': 'redis',
            'EngineVersion': '2.8.22',
        },
        {
            'CacheEngineDescription': 'Redis',
            'CacheEngineVersionDescription': 'redis version 2.8.23 R4',
            'CacheParameterGroupFamily': 'redis2.8',
            'Engine': 'redis',
            'EngineVersion': '2.8.23',
        },
        {
            'CacheEngineDescription': 'Redis',
            'CacheEngineVersionDescription': 'redis version 2.8.24 R3',
            'CacheParameterGroupFamily': 'redis2.8',
            'Engine': 'redis',
            'EngineVersion': '2.8.24',
        },
        {
            'CacheEngineDescription': 'Redis',
            'CacheEngineVersionDescription': 'redis version 2.8.6',
            'CacheParameterGroupFamily': 'redis2.8',
            'Engine': 'redis',
            'EngineVersion': '2.8.6',
        },
        {
            'CacheEngineDescription': 'Redis',
            'CacheEngineVersionDescription': 'redis version 3.2.4',
            'CacheParameterGroupFamily': 'redis3.2',
            'Engine': 'redis',
            'EngineVersion': '3.2.4',
        },
    ],
    'Marker': '',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'CacheEngineVersions': [
            {
                'Engine': 'string',
                'EngineVersion': 'string',
                'CacheParameterGroupFamily': 'string',
                'CacheEngineDescription': 'string',
                'CacheEngineVersionDescription': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_cache_parameter_groups(CacheParameterGroupName=None, MaxRecords=None, Marker=None):
    """
    Returns a list of cache parameter group descriptions. If a cache parameter group name is specified, the list contains only the descriptions for that group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a list of cache parameter group descriptions. If a cache parameter group name is specified, the list contains only the descriptions for that group.
    Expected Output:
    
    :example: response = client.describe_cache_parameter_groups(
        CacheParameterGroupName='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of a specific cache parameter group to return details for.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'CacheParameterGroups': [
        {
            'CacheParameterGroupName': 'string',
            'CacheParameterGroupFamily': 'string',
            'Description': 'string',
            'IsGlobal': True|False,
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeCacheParameterGroups operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

CacheParameterGroups (list) --
A list of cache parameter groups. Each element in the list contains detailed information about one cache parameter group.

(dict) --
Represents the output of a CreateCacheParameterGroup operation.

CacheParameterGroupName (string) --
The name of the cache parameter group.

CacheParameterGroupFamily (string) --
The name of the cache parameter group family that this cache parameter group is compatible with.
Valid values are: memcached1.4 | memcached1.5 | redis2.6 | redis2.8 | redis3.2 | redis4.0 | redis5.0 |

Description (string) --
The description for this cache parameter group.

IsGlobal (boolean) --
Indicates whether the parameter group is associated with a Global Datastore

ARN (string) --
The ARN (Amazon Resource Name) of the cache parameter group.











Exceptions

ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Returns a list of cache parameter group descriptions. If a cache parameter group name is specified, the list contains only the descriptions for that group.
response = client.describe_cache_parameter_groups(
    CacheParameterGroupName='custom-mem1-4',
)

print(response)


Expected Output:
{
    'CacheParameterGroups': [
        {
            'CacheParameterGroupFamily': 'memcached1.4',
            'CacheParameterGroupName': 'custom-mem1-4',
            'Description': 'Custom memcache param group',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'CacheParameterGroups': [
            {
                'CacheParameterGroupName': 'string',
                'CacheParameterGroupFamily': 'string',
                'Description': 'string',
                'IsGlobal': True|False,
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
    ElastiCache.Client.exceptions.InvalidParameterValueException
    ElastiCache.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_cache_parameters(CacheParameterGroupName=None, Source=None, MaxRecords=None, Marker=None):
    """
    Returns the detailed parameter list for a particular cache parameter group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists up to 100 user parameter values for the parameter group custom.redis2.8.
    Expected Output:
    
    :example: response = client.describe_cache_parameters(
        CacheParameterGroupName='string',
        Source='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: [REQUIRED]\nThe name of a specific cache parameter group to return details for.\n

    :type Source: string
    :param Source: The parameter types to return.\nValid values: user | system | engine-default\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Parameters': [
        {
            'ParameterName': 'string',
            'ParameterValue': 'string',
            'Description': 'string',
            'Source': 'string',
            'DataType': 'string',
            'AllowedValues': 'string',
            'IsModifiable': True|False,
            'MinimumEngineVersion': 'string',
            'ChangeType': 'immediate'|'requires-reboot'
        },
    ],
    'CacheNodeTypeSpecificParameters': [
        {
            'ParameterName': 'string',
            'Description': 'string',
            'Source': 'string',
            'DataType': 'string',
            'AllowedValues': 'string',
            'IsModifiable': True|False,
            'MinimumEngineVersion': 'string',
            'CacheNodeTypeSpecificValues': [
                {
                    'CacheNodeType': 'string',
                    'Value': 'string'
                },
            ],
            'ChangeType': 'immediate'|'requires-reboot'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeCacheParameters operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

Parameters (list) --
A list of  Parameter instances.

(dict) --
Describes an individual setting that controls some aspect of ElastiCache behavior.

ParameterName (string) --
The name of the parameter.

ParameterValue (string) --
The value of the parameter.

Description (string) --
A description of the parameter.

Source (string) --
The source of the parameter.

DataType (string) --
The valid data type for the parameter.

AllowedValues (string) --
The valid range of values for the parameter.

IsModifiable (boolean) --
Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion (string) --
The earliest cache engine version to which the parameter can apply.

ChangeType (string) --
Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window\'s reboot. For more information, see Rebooting a Cluster .





CacheNodeTypeSpecificParameters (list) --
A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.

(dict) --
A parameter that has a different value for each cache node type it is applied to. For example, in a Redis cluster, a cache.m1.large cache node type would have a larger maxmemory value than a cache.m1.small type.

ParameterName (string) --
The name of the parameter.

Description (string) --
A description of the parameter.

Source (string) --
The source of the parameter value.

DataType (string) --
The valid data type for the parameter.

AllowedValues (string) --
The valid range of values for the parameter.

IsModifiable (boolean) --
Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion (string) --
The earliest cache engine version to which the parameter can apply.

CacheNodeTypeSpecificValues (list) --
A list of cache node types and their corresponding values for this parameter.

(dict) --
A value that applies only to a certain cache node type.

CacheNodeType (string) --
The cache node type for which this value applies.

Value (string) --
The value for the cache node type.





ChangeType (string) --
Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window\'s reboot. For more information, see Rebooting a Cluster .











Exceptions

ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Lists up to 100 user parameter values for the parameter group custom.redis2.8.
response = client.describe_cache_parameters(
    CacheParameterGroupName='custom-redis2-8',
    MaxRecords=100,
    Source='user',
)

print(response)


Expected Output:
{
    'Marker': '',
    'Parameters': [
        {
            'AllowedValues': 'yes,no',
            'ChangeType': 'requires-reboot',
            'DataType': 'string',
            'Description': 'Apply rehashing or not.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'activerehashing',
            'ParameterValue': 'yes',
            'Source': 'system',
        },
        {
            'AllowedValues': 'always,everysec,no',
            'ChangeType': 'immediate',
            'DataType': 'string',
            'Description': 'fsync policy for AOF persistence',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'appendfsync',
            'ParameterValue': 'everysec',
            'Source': 'system',
        },
        {
            'AllowedValues': 'yes,no',
            'ChangeType': 'immediate',
            'DataType': 'string',
            'Description': 'Enable Redis persistence.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'appendonly',
            'ParameterValue': 'no',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Normal client output buffer hard limit in bytes.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'client-output-buffer-limit-normal-hard-limit',
            'ParameterValue': '0',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Normal client output buffer soft limit in bytes.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'client-output-buffer-limit-normal-soft-limit',
            'ParameterValue': '0',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Normal client output buffer soft limit in seconds.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'client-output-buffer-limit-normal-soft-seconds',
            'ParameterValue': '0',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Pubsub client output buffer hard limit in bytes.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'client-output-buffer-limit-pubsub-hard-limit',
            'ParameterValue': '33554432',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Pubsub client output buffer soft limit in bytes.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'client-output-buffer-limit-pubsub-soft-limit',
            'ParameterValue': '8388608',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Pubsub client output buffer soft limit in seconds.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'client-output-buffer-limit-pubsub-soft-seconds',
            'ParameterValue': '60',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Slave client output buffer soft limit in seconds.',
            'IsModifiable': False,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'client-output-buffer-limit-slave-soft-seconds',
            'ParameterValue': '60',
            'Source': 'system',
        },
        {
            'AllowedValues': 'yes,no',
            'ChangeType': 'immediate',
            'DataType': 'string',
            'Description': 'If enabled, clients who attempt to write to a read-only slave will be disconnected. Applicable to 2.8.23 and higher.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.23',
            'ParameterName': 'close-on-slave-write',
            'ParameterValue': 'yes',
            'Source': 'system',
        },
        {
            'AllowedValues': '1-1200000',
            'ChangeType': 'requires-reboot',
            'DataType': 'integer',
            'Description': 'Set the number of databases.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'databases',
            'ParameterValue': '16',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The maximum number of hash entries in order for the dataset to be compressed.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'hash-max-ziplist-entries',
            'ParameterValue': '512',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The threshold of biggest hash entries in order for the dataset to be compressed.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'hash-max-ziplist-value',
            'ParameterValue': '64',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The maximum number of list entries in order for the dataset to be compressed.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'list-max-ziplist-entries',
            'ParameterValue': '512',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The threshold of biggest list entries in order for the dataset to be compressed.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'list-max-ziplist-value',
            'ParameterValue': '64',
            'Source': 'system',
        },
        {
            'AllowedValues': '5000',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Max execution time of a Lua script in milliseconds. 0 for unlimited execution without warnings.',
            'IsModifiable': False,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'lua-time-limit',
            'ParameterValue': '5000',
            'Source': 'system',
        },
        {
            'AllowedValues': '1-65000',
            'ChangeType': 'requires-reboot',
            'DataType': 'integer',
            'Description': 'The maximum number of Redis clients.',
            'IsModifiable': False,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'maxclients',
            'ParameterValue': '65000',
            'Source': 'system',
        },
        {
            'AllowedValues': 'volatile-lru,allkeys-lru,volatile-random,allkeys-random,volatile-ttl,noeviction',
            'ChangeType': 'immediate',
            'DataType': 'string',
            'Description': 'Max memory policy.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'maxmemory-policy',
            'ParameterValue': 'volatile-lru',
            'Source': 'system',
        },
        {
            'AllowedValues': '1-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Max memory samples.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'maxmemory-samples',
            'ParameterValue': '3',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Maximum number of seconds within which the master must receive a ping from a slave to take writes. Use this parameter together with min-slaves-to-write to regulate when the master stops accepting writes. Setting this value to 0 means the master always takes writes.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'min-slaves-max-lag',
            'ParameterValue': '10',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Number of slaves that must be connected in order for master to take writes. Use this parameter together with min-slaves-max-lag to regulate when the master stops accepting writes. Setting this to 0 means the master always takes writes.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'min-slaves-to-write',
            'ParameterValue': '0',
            'Source': 'system',
        },
        {
            'ChangeType': 'immediate',
            'DataType': 'string',
            'Description': 'The keyspace events for Redis to notify Pub/Sub clients about. By default all notifications are disabled',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'notify-keyspace-events',
            'Source': 'system',
        },
        {
            'AllowedValues': '16384-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The replication backlog size in bytes for PSYNC. This is the size of the buffer which accumulates slave data when slave is disconnected for some time, so that when slave reconnects again, only transfer the portion of data which the slave missed. Minimum value is 16K.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'repl-backlog-size',
            'ParameterValue': '1048576',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The amount of time in seconds after the master no longer have any slaves connected for the master to free the replication backlog. A value of 0 means to never release the backlog.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'repl-backlog-ttl',
            'ParameterValue': '3600',
            'Source': 'system',
        },
        {
            'AllowedValues': '11-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The timeout in seconds for bulk transfer I/O during sync and master timeout from the perspective of the slave, and slave timeout from the perspective of the master.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'repl-timeout',
            'ParameterValue': '60',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The amount of memory reserved for non-cache memory usage, in bytes. You may want to increase this parameter for nodes with read replicas, AOF enabled, etc, to reduce swap usage.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'reserved-memory',
            'ParameterValue': '0',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The limit in the size of the set in order for the dataset to be compressed.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'set-max-intset-entries',
            'ParameterValue': '512',
            'Source': 'system',
        },
        {
            'AllowedValues': 'yes,no',
            'ChangeType': 'immediate',
            'DataType': 'string',
            'Description': 'Configures if chaining of slaves is allowed',
            'IsModifiable': False,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'slave-allow-chaining',
            'ParameterValue': 'no',
            'Source': 'system',
        },
        {
            'AllowedValues': '-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The execution time, in microseconds, to exceed in order for the command to get logged. Note that a negative number disables the slow log, while a value of zero forces the logging of every command.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'slowlog-log-slower-than',
            'ParameterValue': '10000',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The length of the slow log. There is no limit to this length. Just be aware that it will consume memory. You can reclaim memory used by the slow log with SLOWLOG RESET.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'slowlog-max-len',
            'ParameterValue': '128',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'If non-zero, send ACKs every given number of seconds.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'tcp-keepalive',
            'ParameterValue': '0',
            'Source': 'system',
        },
        {
            'AllowedValues': '0,20-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'Close connection if client is idle for a given number of seconds, or never if 0.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'timeout',
            'ParameterValue': '0',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The maximum number of sorted set entries in order for the dataset to be compressed.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'zset-max-ziplist-entries',
            'ParameterValue': '128',
            'Source': 'system',
        },
        {
            'AllowedValues': '0-',
            'ChangeType': 'immediate',
            'DataType': 'integer',
            'Description': 'The threshold of biggest sorted set entries in order for the dataset to be compressed.',
            'IsModifiable': True,
            'MinimumEngineVersion': '2.8.6',
            'ParameterName': 'zset-max-ziplist-value',
            'ParameterValue': '64',
            'Source': 'system',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'Parameters': [
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ChangeType': 'immediate'|'requires-reboot'
            },
        ],
        'CacheNodeTypeSpecificParameters': [
            {
                'ParameterName': 'string',
                'Description': 'string',
                'Source': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'CacheNodeTypeSpecificValues': [
                    {
                        'CacheNodeType': 'string',
                        'Value': 'string'
                    },
                ],
                'ChangeType': 'immediate'|'requires-reboot'
            },
        ]
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
    ElastiCache.Client.exceptions.InvalidParameterValueException
    ElastiCache.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_cache_security_groups(CacheSecurityGroupName=None, MaxRecords=None, Marker=None):
    """
    Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group. This applicable only when you have ElastiCache in Classic setup
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group.
    Expected Output:
    
    :example: response = client.describe_cache_security_groups(
        CacheSecurityGroupName='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: The name of the cache security group to return details for.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'CacheSecurityGroups': [
        {
            'OwnerId': 'string',
            'CacheSecurityGroupName': 'string',
            'Description': 'string',
            'EC2SecurityGroups': [
                {
                    'Status': 'string',
                    'EC2SecurityGroupName': 'string',
                    'EC2SecurityGroupOwnerId': 'string'
                },
            ],
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeCacheSecurityGroups operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

CacheSecurityGroups (list) --
A list of cache security groups. Each element in the list contains detailed information about one group.

(dict) --
Represents the output of one of the following operations:

AuthorizeCacheSecurityGroupIngress
CreateCacheSecurityGroup
RevokeCacheSecurityGroupIngress


OwnerId (string) --
The AWS account ID of the cache security group owner.

CacheSecurityGroupName (string) --
The name of the cache security group.

Description (string) --
The description of the cache security group.

EC2SecurityGroups (list) --
A list of Amazon EC2 security groups that are associated with this cache security group.

(dict) --
Provides ownership and status information for an Amazon EC2 security group.

Status (string) --
The status of the Amazon EC2 security group.

EC2SecurityGroupName (string) --
The name of the Amazon EC2 security group.

EC2SecurityGroupOwnerId (string) --
The AWS account ID of the Amazon EC2 security group owner.





ARN (string) --
The ARN (Amazon Resource Name) of the cache security group.











Exceptions

ElastiCache.Client.exceptions.CacheSecurityGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group.
response = client.describe_cache_security_groups(
    CacheSecurityGroupName='my-sec-group',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'CacheSecurityGroups': [
            {
                'OwnerId': 'string',
                'CacheSecurityGroupName': 'string',
                'Description': 'string',
                'EC2SecurityGroups': [
                    {
                        'Status': 'string',
                        'EC2SecurityGroupName': 'string',
                        'EC2SecurityGroupOwnerId': 'string'
                    },
                ],
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    AuthorizeCacheSecurityGroupIngress
    CreateCacheSecurityGroup
    RevokeCacheSecurityGroupIngress
    
    """
    pass

def describe_cache_subnet_groups(CacheSubnetGroupName=None, MaxRecords=None, Marker=None):
    """
    Returns a list of cache subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group. This is applicable only when you have ElastiCache in VPC setup. All ElastiCache clusters now launch in VPC by default.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes up to 25 cache subnet groups.
    Expected Output:
    
    :example: response = client.describe_cache_subnet_groups(
        CacheSubnetGroupName='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: The name of the cache subnet group to return details for.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'CacheSubnetGroups': [
        {
            'CacheSubnetGroupName': 'string',
            'CacheSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    }
                },
            ],
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeCacheSubnetGroups operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

CacheSubnetGroups (list) --
A list of cache subnet groups. Each element in the list contains detailed information about one group.

(dict) --
Represents the output of one of the following operations:

CreateCacheSubnetGroup
ModifyCacheSubnetGroup


CacheSubnetGroupName (string) --
The name of the cache subnet group.

CacheSubnetGroupDescription (string) --
The description of the cache subnet group.

VpcId (string) --
The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

Subnets (list) --
A list of subnets associated with the cache subnet group.

(dict) --
Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

SubnetIdentifier (string) --
The unique identifier for the subnet.

SubnetAvailabilityZone (dict) --
The Availability Zone associated with the subnet.

Name (string) --
The name of the Availability Zone.







ARN (string) --
The ARN (Amazon Resource Name) of the cache subnet group.











Exceptions

ElastiCache.Client.exceptions.CacheSubnetGroupNotFoundFault

Examples
Describes up to 25 cache subnet groups.
response = client.describe_cache_subnet_groups(
    MaxRecords=25,
)

print(response)


Expected Output:
{
    'CacheSubnetGroups': [
        {
            'CacheSubnetGroupDescription': 'Default CacheSubnetGroup',
            'CacheSubnetGroupName': 'default',
            'Subnets': [
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1a',
                    },
                    'SubnetIdentifier': 'subnet-1a2b3c4d',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1c',
                    },
                    'SubnetIdentifier': 'subnet-a1b2c3d4',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1e',
                    },
                    'SubnetIdentifier': 'subnet-abcd1234',
                },
                {
                    'SubnetAvailabilityZone': {
                        'Name': 'us-east-1b',
                    },
                    'SubnetIdentifier': 'subnet-1234abcd',
                },
            ],
            'VpcId': 'vpc-91280df6',
        },
    ],
    'Marker': '',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'CacheSubnetGroups': [
            {
                'CacheSubnetGroupName': 'string',
                'CacheSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        }
                    },
                ],
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    CreateCacheSubnetGroup
    ModifyCacheSubnetGroup
    
    """
    pass

def describe_engine_default_parameters(CacheParameterGroupFamily=None, MaxRecords=None, Marker=None):
    """
    Returns the default engine and system parameter information for the specified cache engine.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns the default engine and system parameter information for the specified cache engine.
    Expected Output:
    
    :example: response = client.describe_engine_default_parameters(
        CacheParameterGroupFamily='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: [REQUIRED]\nThe name of the cache parameter group family.\nValid values are: memcached1.4 | memcached1.5 | redis2.6 | redis2.8 | redis3.2 | redis4.0 | redis5.0 |\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'EngineDefaults': {
        'CacheParameterGroupFamily': 'string',
        'Marker': 'string',
        'Parameters': [
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ChangeType': 'immediate'|'requires-reboot'
            },
        ],
        'CacheNodeTypeSpecificParameters': [
            {
                'ParameterName': 'string',
                'Description': 'string',
                'Source': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'CacheNodeTypeSpecificValues': [
                    {
                        'CacheNodeType': 'string',
                        'Value': 'string'
                    },
                ],
                'ChangeType': 'immediate'|'requires-reboot'
            },
        ]
    }
}


Response Structure

(dict) --

EngineDefaults (dict) --
Represents the output of a DescribeEngineDefaultParameters operation.

CacheParameterGroupFamily (string) --
Specifies the name of the cache parameter group family to which the engine default parameters apply.
Valid values are: memcached1.4 | memcached1.5 | redis2.6 | redis2.8 | redis3.2 | redis4.0 | redis5.0 |

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

Parameters (list) --
Contains a list of engine default parameters.

(dict) --
Describes an individual setting that controls some aspect of ElastiCache behavior.

ParameterName (string) --
The name of the parameter.

ParameterValue (string) --
The value of the parameter.

Description (string) --
A description of the parameter.

Source (string) --
The source of the parameter.

DataType (string) --
The valid data type for the parameter.

AllowedValues (string) --
The valid range of values for the parameter.

IsModifiable (boolean) --
Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion (string) --
The earliest cache engine version to which the parameter can apply.

ChangeType (string) --
Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window\'s reboot. For more information, see Rebooting a Cluster .





CacheNodeTypeSpecificParameters (list) --
A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.

(dict) --
A parameter that has a different value for each cache node type it is applied to. For example, in a Redis cluster, a cache.m1.large cache node type would have a larger maxmemory value than a cache.m1.small type.

ParameterName (string) --
The name of the parameter.

Description (string) --
A description of the parameter.

Source (string) --
The source of the parameter value.

DataType (string) --
The valid data type for the parameter.

AllowedValues (string) --
The valid range of values for the parameter.

IsModifiable (boolean) --
Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion (string) --
The earliest cache engine version to which the parameter can apply.

CacheNodeTypeSpecificValues (list) --
A list of cache node types and their corresponding values for this parameter.

(dict) --
A value that applies only to a certain cache node type.

CacheNodeType (string) --
The cache node type for which this value applies.

Value (string) --
The value for the cache node type.





ChangeType (string) --
Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window\'s reboot. For more information, see Rebooting a Cluster .













Exceptions

ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Returns the default engine and system parameter information for the specified cache engine.
response = client.describe_engine_default_parameters(
    CacheParameterGroupFamily='redis2.8',
    MaxRecords=25,
)

print(response)


Expected Output:
{
    'EngineDefaults': {
        'CacheNodeTypeSpecificParameters': [
            {
                'AllowedValues': '0-',
                'CacheNodeTypeSpecificValues': [
                    {
                        'CacheNodeType': 'cache.c1.xlarge',
                        'Value': '650117120',
                    },
                    {
                        'CacheNodeType': 'cache.m1.large',
                        'Value': '702545920',
                    },
                    {
                        'CacheNodeType': 'cache.m1.medium',
                        'Value': '309329920',
                    },
                    {
                        'CacheNodeType': 'cache.m1.small',
                        'Value': '94371840',
                    },
                    {
                        'CacheNodeType': 'cache.m1.xlarge',
                        'Value': '1488977920',
                    },
                    {
                        'CacheNodeType': 'cache.m2.2xlarge',
                        'Value': '3502243840',
                    },
                    {
                        'CacheNodeType': 'cache.m2.4xlarge',
                        'Value': '7088373760',
                    },
                    {
                        'CacheNodeType': 'cache.m2.xlarge',
                        'Value': '1709178880',
                    },
                    {
                        'CacheNodeType': 'cache.m3.2xlarge',
                        'Value': '2998927360',
                    },
                    {
                        'CacheNodeType': 'cache.m3.large',
                        'Value': '650117120',
                    },
                    {
                        'CacheNodeType': 'cache.m3.medium',
                        'Value': '309329920',
                    },
                    {
                        'CacheNodeType': 'cache.m3.xlarge',
                        'Value': '1426063360',
                    },
                    {
                        'CacheNodeType': 'cache.m4.10xlarge',
                        'Value': '16604761424',
                    },
                    {
                        'CacheNodeType': 'cache.m4.2xlarge',
                        'Value': '3188912636',
                    },
                    {
                        'CacheNodeType': 'cache.m4.4xlarge',
                        'Value': '6525729063',
                    },
                    {
                        'CacheNodeType': 'cache.m4.large',
                        'Value': '689259315',
                    },
                    {
                        'CacheNodeType': 'cache.m4.xlarge',
                        'Value': '1532850176',
                    },
                    {
                        'CacheNodeType': 'cache.r3.2xlarge',
                        'Value': '6081740800',
                    },
                    {
                        'CacheNodeType': 'cache.r3.4xlarge',
                        'Value': '12268339200',
                    },
                    {
                        'CacheNodeType': 'cache.r3.8xlarge',
                        'Value': '24536678400',
                    },
                    {
                        'CacheNodeType': 'cache.r3.large',
                        'Value': '1468006400',
                    },
                    {
                        'CacheNodeType': 'cache.r3.xlarge',
                        'Value': '3040870400',
                    },
                    {
                        'CacheNodeType': 'cache.t1.micro',
                        'Value': '14260633',
                    },
                    {
                        'CacheNodeType': 'cache.t2.medium',
                        'Value': '346134937',
                    },
                    {
                        'CacheNodeType': 'cache.t2.micro',
                        'Value': '58195968',
                    },
                    {
                        'CacheNodeType': 'cache.t2.small',
                        'Value': '166513868',
                    },
                ],
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Slave client output buffer hard limit in bytes.',
                'IsModifiable': False,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'client-output-buffer-limit-slave-hard-limit',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'CacheNodeTypeSpecificValues': [
                    {
                        'CacheNodeType': 'cache.c1.xlarge',
                        'Value': '650117120',
                    },
                    {
                        'CacheNodeType': 'cache.m1.large',
                        'Value': '702545920',
                    },
                    {
                        'CacheNodeType': 'cache.m1.medium',
                        'Value': '309329920',
                    },
                    {
                        'CacheNodeType': 'cache.m1.small',
                        'Value': '94371840',
                    },
                    {
                        'CacheNodeType': 'cache.m1.xlarge',
                        'Value': '1488977920',
                    },
                    {
                        'CacheNodeType': 'cache.m2.2xlarge',
                        'Value': '3502243840',
                    },
                    {
                        'CacheNodeType': 'cache.m2.4xlarge',
                        'Value': '7088373760',
                    },
                    {
                        'CacheNodeType': 'cache.m2.xlarge',
                        'Value': '1709178880',
                    },
                    {
                        'CacheNodeType': 'cache.m3.2xlarge',
                        'Value': '2998927360',
                    },
                    {
                        'CacheNodeType': 'cache.m3.large',
                        'Value': '650117120',
                    },
                    {
                        'CacheNodeType': 'cache.m3.medium',
                        'Value': '309329920',
                    },
                    {
                        'CacheNodeType': 'cache.m3.xlarge',
                        'Value': '1426063360',
                    },
                    {
                        'CacheNodeType': 'cache.m4.10xlarge',
                        'Value': '16604761424',
                    },
                    {
                        'CacheNodeType': 'cache.m4.2xlarge',
                        'Value': '3188912636',
                    },
                    {
                        'CacheNodeType': 'cache.m4.4xlarge',
                        'Value': '6525729063',
                    },
                    {
                        'CacheNodeType': 'cache.m4.large',
                        'Value': '689259315',
                    },
                    {
                        'CacheNodeType': 'cache.m4.xlarge',
                        'Value': '1532850176',
                    },
                    {
                        'CacheNodeType': 'cache.r3.2xlarge',
                        'Value': '6081740800',
                    },
                    {
                        'CacheNodeType': 'cache.r3.4xlarge',
                        'Value': '12268339200',
                    },
                    {
                        'CacheNodeType': 'cache.r3.8xlarge',
                        'Value': '24536678400',
                    },
                    {
                        'CacheNodeType': 'cache.r3.large',
                        'Value': '1468006400',
                    },
                    {
                        'CacheNodeType': 'cache.r3.xlarge',
                        'Value': '3040870400',
                    },
                    {
                        'CacheNodeType': 'cache.t1.micro',
                        'Value': '14260633',
                    },
                    {
                        'CacheNodeType': 'cache.t2.medium',
                        'Value': '346134937',
                    },
                    {
                        'CacheNodeType': 'cache.t2.micro',
                        'Value': '58195968',
                    },
                    {
                        'CacheNodeType': 'cache.t2.small',
                        'Value': '166513868',
                    },
                ],
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Slave client output buffer soft limit in bytes.',
                'IsModifiable': False,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'client-output-buffer-limit-slave-soft-limit',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'CacheNodeTypeSpecificValues': [
                    {
                        'CacheNodeType': 'cache.c1.xlarge',
                        'Value': '6501171200',
                    },
                    {
                        'CacheNodeType': 'cache.m1.large',
                        'Value': '7025459200',
                    },
                    {
                        'CacheNodeType': 'cache.m1.medium',
                        'Value': '3093299200',
                    },
                    {
                        'CacheNodeType': 'cache.m1.small',
                        'Value': '943718400',
                    },
                    {
                        'CacheNodeType': 'cache.m1.xlarge',
                        'Value': '14889779200',
                    },
                    {
                        'CacheNodeType': 'cache.m2.2xlarge',
                        'Value': '35022438400',
                    },
                    {
                        'CacheNodeType': 'cache.m2.4xlarge',
                        'Value': '70883737600',
                    },
                    {
                        'CacheNodeType': 'cache.m2.xlarge',
                        'Value': '17091788800',
                    },
                    {
                        'CacheNodeType': 'cache.m3.2xlarge',
                        'Value': '29989273600',
                    },
                    {
                        'CacheNodeType': 'cache.m3.large',
                        'Value': '6501171200',
                    },
                    {
                        'CacheNodeType': 'cache.m3.medium',
                        'Value': '2988441600',
                    },
                    {
                        'CacheNodeType': 'cache.m3.xlarge',
                        'Value': '14260633600',
                    },
                    {
                        'CacheNodeType': 'cache.m4.10xlarge',
                        'Value': '166047614239',
                    },
                    {
                        'CacheNodeType': 'cache.m4.2xlarge',
                        'Value': '31889126359',
                    },
                    {
                        'CacheNodeType': 'cache.m4.4xlarge',
                        'Value': '65257290629',
                    },
                    {
                        'CacheNodeType': 'cache.m4.large',
                        'Value': '6892593152',
                    },
                    {
                        'CacheNodeType': 'cache.m4.xlarge',
                        'Value': '15328501760',
                    },
                    {
                        'CacheNodeType': 'cache.r3.2xlarge',
                        'Value': '62495129600',
                    },
                    {
                        'CacheNodeType': 'cache.r3.4xlarge',
                        'Value': '126458265600',
                    },
                    {
                        'CacheNodeType': 'cache.r3.8xlarge',
                        'Value': '254384537600',
                    },
                    {
                        'CacheNodeType': 'cache.r3.large',
                        'Value': '14470348800',
                    },
                    {
                        'CacheNodeType': 'cache.r3.xlarge',
                        'Value': '30513561600',
                    },
                    {
                        'CacheNodeType': 'cache.t1.micro',
                        'Value': '142606336',
                    },
                    {
                        'CacheNodeType': 'cache.t2.medium',
                        'Value': '3461349376',
                    },
                    {
                        'CacheNodeType': 'cache.t2.micro',
                        'Value': '581959680',
                    },
                    {
                        'CacheNodeType': 'cache.t2.small',
                        'Value': '1665138688',
                    },
                ],
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'The maximum configurable amount of memory to use to store items, in bytes.',
                'IsModifiable': False,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'maxmemory',
                'Source': 'system',
            },
        ],
        'CacheParameterGroupFamily': 'redis2.8',
        'Marker': 'bWluLXNsYXZlcy10by13cml0ZQ==',
        'Parameters': [
            {
                'AllowedValues': 'yes,no',
                'ChangeType': 'requires-reboot',
                'DataType': 'string',
                'Description': 'Apply rehashing or not.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'activerehashing',
                'ParameterValue': 'yes',
                'Source': 'system',
            },
            {
                'AllowedValues': 'always,everysec,no',
                'ChangeType': 'immediate',
                'DataType': 'string',
                'Description': 'fsync policy for AOF persistence',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'appendfsync',
                'ParameterValue': 'everysec',
                'Source': 'system',
            },
            {
                'AllowedValues': 'yes,no',
                'ChangeType': 'immediate',
                'DataType': 'string',
                'Description': 'Enable Redis persistence.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'appendonly',
                'ParameterValue': 'no',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Normal client output buffer hard limit in bytes.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'client-output-buffer-limit-normal-hard-limit',
                'ParameterValue': '0',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Normal client output buffer soft limit in bytes.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'client-output-buffer-limit-normal-soft-limit',
                'ParameterValue': '0',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Normal client output buffer soft limit in seconds.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'client-output-buffer-limit-normal-soft-seconds',
                'ParameterValue': '0',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Pubsub client output buffer hard limit in bytes.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'client-output-buffer-limit-pubsub-hard-limit',
                'ParameterValue': '33554432',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Pubsub client output buffer soft limit in bytes.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'client-output-buffer-limit-pubsub-soft-limit',
                'ParameterValue': '8388608',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Pubsub client output buffer soft limit in seconds.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'client-output-buffer-limit-pubsub-soft-seconds',
                'ParameterValue': '60',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Slave client output buffer soft limit in seconds.',
                'IsModifiable': False,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'client-output-buffer-limit-slave-soft-seconds',
                'ParameterValue': '60',
                'Source': 'system',
            },
            {
                'AllowedValues': 'yes,no',
                'ChangeType': 'immediate',
                'DataType': 'string',
                'Description': 'If enabled, clients who attempt to write to a read-only slave will be disconnected. Applicable to 2.8.23 and higher.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.23',
                'ParameterName': 'close-on-slave-write',
                'ParameterValue': 'yes',
                'Source': 'system',
            },
            {
                'AllowedValues': '1-1200000',
                'ChangeType': 'requires-reboot',
                'DataType': 'integer',
                'Description': 'Set the number of databases.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'databases',
                'ParameterValue': '16',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'The maximum number of hash entries in order for the dataset to be compressed.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'hash-max-ziplist-entries',
                'ParameterValue': '512',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'The threshold of biggest hash entries in order for the dataset to be compressed.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'hash-max-ziplist-value',
                'ParameterValue': '64',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'The maximum number of list entries in order for the dataset to be compressed.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'list-max-ziplist-entries',
                'ParameterValue': '512',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'The threshold of biggest list entries in order for the dataset to be compressed.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'list-max-ziplist-value',
                'ParameterValue': '64',
                'Source': 'system',
            },
            {
                'AllowedValues': '5000',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Max execution time of a Lua script in milliseconds. 0 for unlimited execution without warnings.',
                'IsModifiable': False,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'lua-time-limit',
                'ParameterValue': '5000',
                'Source': 'system',
            },
            {
                'AllowedValues': '1-65000',
                'ChangeType': 'requires-reboot',
                'DataType': 'integer',
                'Description': 'The maximum number of Redis clients.',
                'IsModifiable': False,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'maxclients',
                'ParameterValue': '65000',
                'Source': 'system',
            },
            {
                'AllowedValues': 'volatile-lru,allkeys-lru,volatile-random,allkeys-random,volatile-ttl,noeviction',
                'ChangeType': 'immediate',
                'DataType': 'string',
                'Description': 'Max memory policy.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'maxmemory-policy',
                'ParameterValue': 'volatile-lru',
                'Source': 'system',
            },
            {
                'AllowedValues': '1-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Max memory samples.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'maxmemory-samples',
                'ParameterValue': '3',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Maximum number of seconds within which the master must receive a ping from a slave to take writes. Use this parameter together with min-slaves-to-write to regulate when the master stops accepting writes. Setting this value to 0 means the master always takes writes.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'min-slaves-max-lag',
                'ParameterValue': '10',
                'Source': 'system',
            },
            {
                'AllowedValues': '0-',
                'ChangeType': 'immediate',
                'DataType': 'integer',
                'Description': 'Number of slaves that must be connected in order for master to take writes. Use this parameter together with min-slaves-max-lag to regulate when the master stops accepting writes. Setting this to 0 means the master always takes writes.',
                'IsModifiable': True,
                'MinimumEngineVersion': '2.8.6',
                'ParameterName': 'min-slaves-to-write',
                'ParameterValue': '0',
                'Source': 'system',
            },
        ],
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'EngineDefaults': {
            'CacheParameterGroupFamily': 'string',
            'Marker': 'string',
            'Parameters': [
                {
                    'ParameterName': 'string',
                    'ParameterValue': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string',
                    'ChangeType': 'immediate'|'requires-reboot'
                },
            ],
            'CacheNodeTypeSpecificParameters': [
                {
                    'ParameterName': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string',
                    'CacheNodeTypeSpecificValues': [
                        {
                            'CacheNodeType': 'string',
                            'Value': 'string'
                        },
                    ],
                    'ChangeType': 'immediate'|'requires-reboot'
                },
            ]
        }
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.InvalidParameterValueException
    ElastiCache.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, MaxRecords=None, Marker=None):
    """
    Returns events related to clusters, cache security groups, and cache parameter groups. You can obtain events specific to a particular cluster, cache security group, or cache parameter group by providing the name as a parameter.
    By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days\' worth of events if necessary.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes all the replication-group events from 3:00P to 5:00P on November 11, 2016.
    Expected Output:
    
    :example: response = client.describe_events(
        SourceIdentifier='string',
        SourceType='cache-cluster'|'cache-parameter-group'|'cache-security-group'|'cache-subnet-group'|'replication-group',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Duration=123,
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type SourceIdentifier: string
    :param SourceIdentifier: The identifier of the event source for which events are returned. If not specified, all sources are included in the response.

    :type SourceType: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.

    :type StartTime: datetime
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format.\n\nExample: 2017-03-30T07:03:49.555Z\n

    :type EndTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format.\n\nExample: 2017-03-30T07:03:49.555Z\n

    :type Duration: integer
    :param Duration: The number of minutes worth of events to retrieve.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Events': [
        {
            'SourceIdentifier': 'string',
            'SourceType': 'cache-cluster'|'cache-parameter-group'|'cache-security-group'|'cache-subnet-group'|'replication-group',
            'Message': 'string',
            'Date': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeEvents operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

Events (list) --
A list of events. Each element in the list contains detailed information about one event.

(dict) --
Represents a single occurrence of something interesting within the system. Some examples of events are creating a cluster, adding or removing a cache node, or rebooting a node.

SourceIdentifier (string) --
The identifier for the source of the event. For example, if the event occurred at the cluster level, the identifier would be the name of the cluster.

SourceType (string) --
Specifies the origin of this event - a cluster, a parameter group, a security group, etc.

Message (string) --
The text of the event.

Date (datetime) --
The date and time when the event occurred.











Exceptions

ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Describes all the replication-group events from 3:00P to 5:00P on November 11, 2016.
response = client.describe_events(
    StartTime=datetime(2016, 12, 22, 15, 0, 0, 3, 357, 0),
)

print(response)


Expected Output:
{
    'Events': [
        {
            'Date': datetime(2016, 12, 22, 21, 35, 46, 3, 357, 0),
            'Message': 'Snapshot succeeded for snapshot with ID 'cr-bkup' of replication group with ID 'clustered-redis'',
            'SourceIdentifier': 'clustered-redis-0001-001',
            'SourceType': 'cache-cluster',
        },
        {
            'Date': datetime(2016, 12, 22, 16, 27, 56, 3, 357, 0),
            'Message': 'Added cache node 0001 in availability zone us-east-1e',
            'SourceIdentifier': 'redis-cluster',
            'SourceType': 'cache-cluster',
        },
        {
            'Date': datetime(2016, 12, 22, 16, 27, 56, 3, 357, 0),
            'Message': 'Cache cluster created',
            'SourceIdentifier': 'redis-cluster',
            'SourceType': 'cache-cluster',
        },
        {
            'Date': datetime(2016, 12, 22, 16, 5, 17, 3, 357, 0),
            'Message': 'Added cache node 0002 in availability zone us-east-1c',
            'SourceIdentifier': 'my-memcached2',
            'SourceType': 'cache-cluster',
        },
        {
            'Date': datetime(2016, 12, 22, 16, 5, 17, 3, 357, 0),
            'Message': 'Added cache node 0001 in availability zone us-east-1e',
            'SourceIdentifier': 'my-memcached2',
            'SourceType': 'cache-cluster',
        },
        {
            'Date': datetime(2016, 12, 22, 16, 5, 17, 3, 357, 0),
            'Message': 'Cache cluster created',
            'SourceIdentifier': 'my-memcached2',
            'SourceType': 'cache-cluster',
        },
    ],
    'Marker': '',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'Events': [
            {
                'SourceIdentifier': 'string',
                'SourceType': 'cache-cluster'|'cache-parameter-group'|'cache-security-group'|'cache-subnet-group'|'replication-group',
                'Message': 'string',
                'Date': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.InvalidParameterValueException
    ElastiCache.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_global_replication_groups(GlobalReplicationGroupId=None, MaxRecords=None, Marker=None, ShowMemberInfo=None):
    """
    Returns information about a particular global replication group. If no identifier is specified, returns information about all Global Datastores.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_global_replication_groups(
        GlobalReplicationGroupId='string',
        MaxRecords=123,
        Marker='string',
        ShowMemberInfo=True|False
    )
    
    
    :type GlobalReplicationGroupId: string
    :param GlobalReplicationGroupId: The name of the Global Datastore

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type ShowMemberInfo: boolean
    :param ShowMemberInfo: Returns the list of members that comprise the Global Datastore.

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'GlobalReplicationGroups': [
        {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupDescription': 'string',
            'Status': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'Members': [
                {
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupRegion': 'string',
                    'Role': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'Status': 'string'
                },
            ],
            'ClusterEnabled': True|False,
            'GlobalNodeGroups': [
                {
                    'GlobalNodeGroupId': 'string',
                    'Slots': 'string'
                },
            ],
            'AuthTokenEnabled': True|False,
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. >

GlobalReplicationGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different AWS region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.


GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupDescription (string) --
The optional description of the Global Datastore

Status (string) --
The status of the Global Datastore

CacheNodeType (string) --
The cache node type of the Global Datastore

Engine (string) --
The Elasticache engine. For Redis only.

EngineVersion (string) --
The Elasticache Redis engine version. For preview, it is Redis version 5.0.5 only.

Members (list) --
The replication groups that comprise the Global Datastore.

(dict) --
A member of a Global Datastore. It contains the Replication Group Id, the AWS region and the role of the replication group.

ReplicationGroupId (string) --
The replication group id of the Global Datastore member.

ReplicationGroupRegion (string) --
The AWS region of the Global Datastore member.

Role (string) --
Indicates the role of the replication group, primary or secondary.

AutomaticFailover (string) --
Indicates whether automatic failover is enabled for the replication group.

Status (string) --
The status of the membership of the replication group.





ClusterEnabled (boolean) --
A flag that indicates whether the Global Datastore is cluster enabled.

GlobalNodeGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId (string) --
The name of the global node group

Slots (string) --
The keyspace for this node group





AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true. You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.


ARN (string) --
The ARN (Amazon Resource Name) of the global replication group.











Exceptions

ElastiCache.Client.exceptions.GlobalReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Marker': 'string',
        'GlobalReplicationGroups': [
            {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupDescription': 'string',
                'Status': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'Members': [
                    {
                        'ReplicationGroupId': 'string',
                        'ReplicationGroupRegion': 'string',
                        'Role': 'string',
                        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                        'Status': 'string'
                    },
                ],
                'ClusterEnabled': True|False,
                'GlobalNodeGroups': [
                    {
                        'GlobalNodeGroupId': 'string',
                        'Slots': 'string'
                    },
                ],
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False,
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.
    
    """
    pass

def describe_replication_groups(ReplicationGroupId=None, MaxRecords=None, Marker=None):
    """
    Returns information about a particular replication group. If no identifier is specified, DescribeReplicationGroups returns information about all replication groups.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about the replication group myreplgroup.
    Expected Output:
    
    :example: response = client.describe_replication_groups(
        ReplicationGroupId='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: The identifier for the replication group to be described. This parameter is not case sensitive.\nIf you do not specify this parameter, information about all replication groups is returned.\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ReplicationGroups': [
        {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeReplicationGroups operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

ReplicationGroups (list) --
A list of replication groups. Each item in the list contains detailed information about one replication group.

(dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.











Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Returns information about the replication group myreplgroup.
response = client.describe_replication_groups(
)

print(response)


Expected Output:
{
    'Marker': '',
    'ReplicationGroups': [
        {
            'AutomaticFailover': 'enabled',
            'Description': 'Test cluster',
            'MemberClusters': [
                'clustered-redis-0001-001',
                'clustered-redis-0001-002',
                'clustered-redis-0002-001',
                'clustered-redis-0002-002',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': '0001',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'clustered-redis-0001-001',
                            'CacheNodeId': '0001',
                            'PreferredAvailabilityZone': 'us-east-1e',
                        },
                        {
                            'CacheClusterId': 'clustered-redis-0001-002',
                            'CacheNodeId': '0001',
                            'PreferredAvailabilityZone': 'us-east-1c',
                        },
                    ],
                    'Status': 'available',
                },
                {
                    'NodeGroupId': '0002',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'clustered-redis-0002-001',
                            'CacheNodeId': '0001',
                            'PreferredAvailabilityZone': 'us-east-1c',
                        },
                        {
                            'CacheClusterId': 'clustered-redis-0002-002',
                            'CacheNodeId': '0001',
                            'PreferredAvailabilityZone': 'us-east-1b',
                        },
                    ],
                    'Status': 'available',
                },
            ],
            'PendingModifiedValues': {
            },
            'ReplicationGroupId': 'clustered-redis',
            'Status': 'available',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'ReplicationGroups': [
            {
                'ReplicationGroupId': 'string',
                'Description': 'string',
                'GlobalReplicationGroupInfo': {
                    'GlobalReplicationGroupId': 'string',
                    'GlobalReplicationGroupMemberRole': 'string'
                },
                'Status': 'string',
                'PendingModifiedValues': {
                    'PrimaryClusterId': 'string',
                    'AutomaticFailoverStatus': 'enabled'|'disabled',
                    'Resharding': {
                        'SlotMigration': {
                            'ProgressPercentage': 123.0
                        }
                    },
                    'AuthTokenStatus': 'SETTING'|'ROTATING'
                },
                'MemberClusters': [
                    'string',
                ],
                'NodeGroups': [
                    {
                        'NodeGroupId': 'string',
                        'Status': 'string',
                        'PrimaryEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'ReaderEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'Slots': 'string',
                        'NodeGroupMembers': [
                            {
                                'CacheClusterId': 'string',
                                'CacheNodeId': 'string',
                                'ReadEndpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'PreferredAvailabilityZone': 'string',
                                'CurrentRole': 'string'
                            },
                        ]
                    },
                ],
                'SnapshottingClusterId': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'ClusterEnabled': True|False,
                'CacheNodeType': 'string',
                'AuthTokenEnabled': True|False,
                'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False,
                'KmsKeyId': 'string',
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled): T1 node types.
    Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def describe_reserved_cache_nodes(ReservedCacheNodeId=None, ReservedCacheNodesOfferingId=None, CacheNodeType=None, Duration=None, ProductDescription=None, OfferingType=None, MaxRecords=None, Marker=None):
    """
    Returns information about reserved cache nodes for this account, or about a specified reserved cache node.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about reserved cache nodes for this account, or about a specified reserved cache node. If the account has no reserved cache nodes, the operation returns an empty list, as shown here.
    Expected Output:
    
    :example: response = client.describe_reserved_cache_nodes(
        ReservedCacheNodeId='string',
        ReservedCacheNodesOfferingId='string',
        CacheNodeType='string',
        Duration='string',
        ProductDescription='string',
        OfferingType='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReservedCacheNodeId: string
    :param ReservedCacheNodeId: The reserved cache node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.

    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodesOfferingId: The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.

    :type CacheNodeType: string
    :param CacheNodeType: The cache node type filter value. Use this parameter to show only those reservations matching the specified cache node type.\nThe following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.\n\nGeneral purpose:\nCurrent generation:  M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium\nPrevious generation: (not recommended) T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge\n\n\nCompute optimized:\nPrevious generation: (not recommended) C1 node types: cache.c1.xlarge\n\n\nMemory optimized:\nCurrent generation:  R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge\nPrevious generation: (not recommended) M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge\n\n\n\n\nAdditional node type info\n\nAll current generation instance types are created in Amazon VPC by default.\nRedis append-only files (AOF) are not supported for T1 or T2 instances.\nRedis Multi-AZ with automatic failover is not supported on T1 instances.\nRedis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.\n\n

    :type Duration: string
    :param Duration: The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.\nValid Values: 1 | 3 | 31536000 | 94608000\n

    :type ProductDescription: string
    :param ProductDescription: The product description filter value. Use this parameter to show only those reservations matching the specified product description.

    :type OfferingType: string
    :param OfferingType: The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.\nValid values: 'Light Utilization'|'Medium Utilization'|'Heavy Utilization'\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ReservedCacheNodes': [
        {
            'ReservedCacheNodeId': 'string',
            'ReservedCacheNodesOfferingId': 'string',
            'CacheNodeType': 'string',
            'StartTime': datetime(2015, 1, 1),
            'Duration': 123,
            'FixedPrice': 123.0,
            'UsagePrice': 123.0,
            'CacheNodeCount': 123,
            'ProductDescription': 'string',
            'OfferingType': 'string',
            'State': 'string',
            'RecurringCharges': [
                {
                    'RecurringChargeAmount': 123.0,
                    'RecurringChargeFrequency': 'string'
                },
            ],
            'ReservationARN': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeReservedCacheNodes operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

ReservedCacheNodes (list) --
A list of reserved cache nodes. Each element in the list contains detailed information about one node.

(dict) --
Represents the output of a PurchaseReservedCacheNodesOffering operation.

ReservedCacheNodeId (string) --
The unique identifier for the reservation.

ReservedCacheNodesOfferingId (string) --
The offering identifier.

CacheNodeType (string) --
The cache node type for the reserved cache nodes.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


StartTime (datetime) --
The time the reservation started.

Duration (integer) --
The duration of the reservation in seconds.

FixedPrice (float) --
The fixed price charged for this reserved cache node.

UsagePrice (float) --
The hourly price charged for this reserved cache node.

CacheNodeCount (integer) --
The number of cache nodes that have been reserved.

ProductDescription (string) --
The description of the reserved cache node.

OfferingType (string) --
The offering type of this reserved cache node.

State (string) --
The state of the reserved cache node.

RecurringCharges (list) --
The recurring price charged to run this reserved cache node.

(dict) --
Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

RecurringChargeAmount (float) --
The monetary amount of the recurring charge.

RecurringChargeFrequency (string) --
The frequency of the recurring charge.





ReservationARN (string) --
The Amazon Resource Name (ARN) of the reserved cache node.
Example: arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582











Exceptions

ElastiCache.Client.exceptions.ReservedCacheNodeNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Returns information about reserved cache nodes for this account, or about a specified reserved cache node. If the account has no reserved cache nodes, the operation returns an empty list, as shown here.
response = client.describe_reserved_cache_nodes(
    MaxRecords=25,
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'ReservedCacheNodes': [
            {
                'ReservedCacheNodeId': 'string',
                'ReservedCacheNodesOfferingId': 'string',
                'CacheNodeType': 'string',
                'StartTime': datetime(2015, 1, 1),
                'Duration': 123,
                'FixedPrice': 123.0,
                'UsagePrice': 123.0,
                'CacheNodeCount': 123,
                'ProductDescription': 'string',
                'OfferingType': 'string',
                'State': 'string',
                'RecurringCharges': [
                    {
                        'RecurringChargeAmount': 123.0,
                        'RecurringChargeFrequency': 'string'
                    },
                ],
                'ReservationARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    General purpose:
    Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
    Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
    
    
    Compute optimized:
    Previous generation: (not recommended)  C1 node types: cache.c1.xlarge
    
    
    Memory optimized:
    Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
    Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    
    
    
    """
    pass

def describe_reserved_cache_nodes_offerings(ReservedCacheNodesOfferingId=None, CacheNodeType=None, Duration=None, ProductDescription=None, OfferingType=None, MaxRecords=None, Marker=None):
    """
    Lists available reserved cache node offerings.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists available reserved cache node offerings.
    Expected Output:
    
    :example: response = client.describe_reserved_cache_nodes_offerings(
        ReservedCacheNodesOfferingId='string',
        CacheNodeType='string',
        Duration='string',
        ProductDescription='string',
        OfferingType='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodesOfferingId: The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.\nExample: 438012d3-4052-4cc7-b2e3-8d3372e0e706\n

    :type CacheNodeType: string
    :param CacheNodeType: The cache node type filter value. Use this parameter to show only the available offerings matching the specified cache node type.\nThe following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.\n\nGeneral purpose:\nCurrent generation:  M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium\nPrevious generation: (not recommended) T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge\n\n\nCompute optimized:\nPrevious generation: (not recommended) C1 node types: cache.c1.xlarge\n\n\nMemory optimized:\nCurrent generation:  R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge\nPrevious generation: (not recommended) M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge\n\n\n\n\nAdditional node type info\n\nAll current generation instance types are created in Amazon VPC by default.\nRedis append-only files (AOF) are not supported for T1 or T2 instances.\nRedis Multi-AZ with automatic failover is not supported on T1 instances.\nRedis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.\n\n

    :type Duration: string
    :param Duration: Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.\nValid Values: 1 | 3 | 31536000 | 94608000\n

    :type ProductDescription: string
    :param ProductDescription: The product description filter value. Use this parameter to show only the available offerings matching the specified product description.

    :type OfferingType: string
    :param OfferingType: The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.\nValid Values: 'Light Utilization'|'Medium Utilization'|'Heavy Utilization'\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: minimum 20; maximum 100.\n

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ReservedCacheNodesOfferings': [
        {
            'ReservedCacheNodesOfferingId': 'string',
            'CacheNodeType': 'string',
            'Duration': 123,
            'FixedPrice': 123.0,
            'UsagePrice': 123.0,
            'ProductDescription': 'string',
            'OfferingType': 'string',
            'RecurringCharges': [
                {
                    'RecurringChargeAmount': 123.0,
                    'RecurringChargeFrequency': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeReservedCacheNodesOfferings operation.

Marker (string) --
Provides an identifier to allow retrieval of paginated results.

ReservedCacheNodesOfferings (list) --
A list of reserved cache node offerings. Each element in the list contains detailed information about one offering.

(dict) --
Describes all of the attributes of a reserved cache node offering.

ReservedCacheNodesOfferingId (string) --
A unique identifier for the reserved cache node offering.

CacheNodeType (string) --
The cache node type for the reserved cache node.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Duration (integer) --
The duration of the offering. in seconds.

FixedPrice (float) --
The fixed price charged for this offering.

UsagePrice (float) --
The hourly price charged for this offering.

ProductDescription (string) --
The cache engine used by the offering.

OfferingType (string) --
The offering type.

RecurringCharges (list) --
The recurring price charged to run this reserved cache node.

(dict) --
Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

RecurringChargeAmount (float) --
The monetary amount of the recurring charge.

RecurringChargeFrequency (string) --
The frequency of the recurring charge.















Exceptions

ElastiCache.Client.exceptions.ReservedCacheNodesOfferingNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Lists available reserved cache node offerings.
response = client.describe_reserved_cache_nodes_offerings(
    CacheNodeType='',
    Duration='',
    Marker='',
    MaxRecords=25,
    OfferingType='',
    ProductDescription='',
    ReservedCacheNodesOfferingId='438012d3-4052-4cc7-b2e3-8d3372e0e706',
)

print(response)


Expected Output:
{
    'Marker': '',
    'ReservedCacheNodesOfferings': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'ReservedCacheNodesOfferings': [
            {
                'ReservedCacheNodesOfferingId': 'string',
                'CacheNodeType': 'string',
                'Duration': 123,
                'FixedPrice': 123.0,
                'UsagePrice': 123.0,
                'ProductDescription': 'string',
                'OfferingType': 'string',
                'RecurringCharges': [
                    {
                        'RecurringChargeAmount': 123.0,
                        'RecurringChargeFrequency': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    General purpose:
    Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
    Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
    
    
    Compute optimized:
    Previous generation: (not recommended)  C1 node types: cache.c1.xlarge
    
    
    Memory optimized:
    Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
    Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    
    
    
    """
    pass

def describe_service_updates(ServiceUpdateName=None, ServiceUpdateStatus=None, MaxRecords=None, Marker=None):
    """
    Returns details of the service updates
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_service_updates(
        ServiceUpdateName='string',
        ServiceUpdateStatus=[
            'available'|'cancelled'|'expired',
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ServiceUpdateName: string
    :param ServiceUpdateName: The unique ID of the service update

    :type ServiceUpdateStatus: list
    :param ServiceUpdateStatus: The status of the service update\n\n(string) --\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ServiceUpdates': [
        {
            'ServiceUpdateName': 'string',
            'ServiceUpdateReleaseDate': datetime(2015, 1, 1),
            'ServiceUpdateEndDate': datetime(2015, 1, 1),
            'ServiceUpdateSeverity': 'critical'|'important'|'medium'|'low',
            'ServiceUpdateRecommendedApplyByDate': datetime(2015, 1, 1),
            'ServiceUpdateStatus': 'available'|'cancelled'|'expired',
            'ServiceUpdateDescription': 'string',
            'ServiceUpdateType': 'security-update',
            'Engine': 'string',
            'EngineVersion': 'string',
            'AutoUpdateAfterRecommendedApplyByDate': True|False,
            'EstimatedUpdateTime': 'string'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

ServiceUpdates (list) --
A list of service updates

(dict) --
An update that you can apply to your Redis clusters.

ServiceUpdateName (string) --
The unique ID of the service update

ServiceUpdateReleaseDate (datetime) --
The date when the service update is initially available

ServiceUpdateEndDate (datetime) --
The date after which the service update is no longer available

ServiceUpdateSeverity (string) --
The severity of the service update

ServiceUpdateRecommendedApplyByDate (datetime) --
The recommendend date to apply the service update in order to ensure compliance. For information on compliance, see Self-Service Security Updates for Compliance .

ServiceUpdateStatus (string) --
The status of the service update

ServiceUpdateDescription (string) --
Provides details of the service update

ServiceUpdateType (string) --
Reflects the nature of the service update

Engine (string) --
The Elasticache engine to which the update applies. Either Redis or Memcached

EngineVersion (string) --
The Elasticache engine version to which the update applies. Either Redis or Memcached engine version

AutoUpdateAfterRecommendedApplyByDate (boolean) --
Indicates whether the service update will be automatically applied once the recommended apply-by date has expired.

EstimatedUpdateTime (string) --
The estimated length of time the service update will take











Exceptions

ElastiCache.Client.exceptions.ServiceUpdateNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Marker': 'string',
        'ServiceUpdates': [
            {
                'ServiceUpdateName': 'string',
                'ServiceUpdateReleaseDate': datetime(2015, 1, 1),
                'ServiceUpdateEndDate': datetime(2015, 1, 1),
                'ServiceUpdateSeverity': 'critical'|'important'|'medium'|'low',
                'ServiceUpdateRecommendedApplyByDate': datetime(2015, 1, 1),
                'ServiceUpdateStatus': 'available'|'cancelled'|'expired',
                'ServiceUpdateDescription': 'string',
                'ServiceUpdateType': 'security-update',
                'Engine': 'string',
                'EngineVersion': 'string',
                'AutoUpdateAfterRecommendedApplyByDate': True|False,
                'EstimatedUpdateTime': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.ServiceUpdateNotFoundFault
    ElastiCache.Client.exceptions.InvalidParameterValueException
    ElastiCache.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_snapshots(ReplicationGroupId=None, CacheClusterId=None, SnapshotName=None, SnapshotSource=None, Marker=None, MaxRecords=None, ShowNodeGroupConfig=None):
    """
    Returns information about cluster or replication group snapshots. By default, DescribeSnapshots lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cache cluster.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about the snapshot mysnapshot. By default.
    Expected Output:
    
    :example: response = client.describe_snapshots(
        ReplicationGroupId='string',
        CacheClusterId='string',
        SnapshotName='string',
        SnapshotSource='string',
        Marker='string',
        MaxRecords=123,
        ShowNodeGroupConfig=True|False
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: A user-supplied replication group identifier. If this parameter is specified, only snapshots associated with that specific replication group are described.

    :type CacheClusterId: string
    :param CacheClusterId: A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.

    :type SnapshotName: string
    :param SnapshotName: A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described.

    :type SnapshotSource: string
    :param SnapshotSource: If set to system , the output shows snapshots that were automatically created by ElastiCache. If set to user the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.\nDefault: 50\nConstraints: minimum 20; maximum 50.\n

    :type ShowNodeGroupConfig: boolean
    :param ShowNodeGroupConfig: A Boolean value which if true, the node group (shard) configuration is included in the snapshot description.

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Snapshots': [
        {
            'SnapshotName': 'string',
            'ReplicationGroupId': 'string',
            'ReplicationGroupDescription': 'string',
            'CacheClusterId': 'string',
            'SnapshotStatus': 'string',
            'SnapshotSource': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'NumCacheNodes': 123,
            'PreferredAvailabilityZone': 'string',
            'CacheClusterCreateTime': datetime(2015, 1, 1),
            'PreferredMaintenanceWindow': 'string',
            'TopicArn': 'string',
            'Port': 123,
            'CacheParameterGroupName': 'string',
            'CacheSubnetGroupName': 'string',
            'VpcId': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'NumNodeGroups': 123,
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'NodeSnapshots': [
                {
                    'CacheClusterId': 'string',
                    'NodeGroupId': 'string',
                    'CacheNodeId': 'string',
                    'NodeGroupConfiguration': {
                        'NodeGroupId': 'string',
                        'Slots': 'string',
                        'ReplicaCount': 123,
                        'PrimaryAvailabilityZone': 'string',
                        'ReplicaAvailabilityZones': [
                            'string',
                        ]
                    },
                    'CacheSize': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'SnapshotCreateTime': datetime(2015, 1, 1)
                },
            ],
            'KmsKeyId': 'string',
            'ARN': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DescribeSnapshots operation.

Marker (string) --
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Snapshots (list) --
A list of snapshots. Each item in the list contains detailed information about one snapshot.

(dict) --
Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

SnapshotName (string) --
The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

ReplicationGroupId (string) --
The unique identifier of the source replication group.

ReplicationGroupDescription (string) --
A description of the source replication group.

CacheClusterId (string) --
The user-supplied identifier of the source cluster.

SnapshotStatus (string) --
The status of the snapshot. Valid values: creating | available | restoring | copying | deleting .

SnapshotSource (string) --
Indicates whether the snapshot is from an automatic backup (automated ) or was created manually (manual ).

CacheNodeType (string) --
The name of the compute and memory capacity node type for the source cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Engine (string) --
The name of the cache engine (memcached or redis ) used by the source cluster.

EngineVersion (string) --
The version of the cache engine version that is used by the source cluster.

NumCacheNodes (integer) --
The number of cache nodes in the source cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the source cluster is located.

CacheClusterCreateTime (datetime) --
The date and time when the source cluster was created.

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for ddd are:

sun
mon
tue
wed
thu
fri
sat

Example: sun:23:00-mon:01:30

TopicArn (string) --
The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

Port (integer) --
The port number used by each cache nodes in the source cluster.

CacheParameterGroupName (string) --
The cache parameter group that is associated with the source cluster.

CacheSubnetGroupName (string) --
The name of the cache subnet group associated with the source cluster.

VpcId (string) --
The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

AutoMinorVersionUpgrade (boolean) --
This parameter is currently disabled.

SnapshotRetentionLimit (integer) --
For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.
For manual snapshots, this field reflects the SnapshotRetentionLimit for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the DeleteSnapshot operation.

Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range during which ElastiCache takes daily snapshots of the source cluster.

NumNodeGroups (integer) --
The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


NodeSnapshots (list) --
A list of the cache nodes in the source cluster.

(dict) --
Represents an individual cache node in a snapshot of a cluster.

CacheClusterId (string) --
A unique identifier for the source cluster.

NodeGroupId (string) --
A unique identifier for the source node group (shard).

CacheNodeId (string) --
The cache node identifier for the node in the source cluster.

NodeGroupConfiguration (dict) --
The configuration for the source node group (shard).

NodeGroupId (string) --
Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.

Slots (string) --
A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format startkey-endkey .
Example: "0-3999"

ReplicaCount (integer) --
The number of read replica nodes in this node group (shard).

PrimaryAvailabilityZone (string) --
The Availability Zone where the primary node of this node group (shard) is launched.

ReplicaAvailabilityZones (list) --
A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ReplicaCount or ReplicasPerNodeGroup if not specified.

(string) --




CacheSize (string) --
The size of the cache on the source cache node.

CacheNodeCreateTime (datetime) --
The date and time when the cache node was created in the source cluster.

SnapshotCreateTime (datetime) --
The date and time when the source node\'s metadata and cache data set was obtained for the snapshot.





KmsKeyId (string) --
The ID of the KMS key used to encrypt the snapshot.

ARN (string) --
The ARN (Amazon Resource Name) of the snapshot.











Exceptions

ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.SnapshotNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Returns information about the snapshot mysnapshot. By default.
response = client.describe_snapshots(
    SnapshotName='snapshot-20161212',
)

print(response)


Expected Output:
{
    'Marker': '',
    'Snapshots': [
        {
            'AutoMinorVersionUpgrade': True,
            'CacheClusterCreateTime': datetime(2016, 12, 21, 22, 27, 12, 2, 356, 0),
            'CacheClusterId': 'my-redis5',
            'CacheNodeType': 'cache.m3.large',
            'CacheParameterGroupName': 'default.redis3.2',
            'CacheSubnetGroupName': 'default',
            'Engine': 'redis',
            'EngineVersion': '3.2.4',
            'NodeSnapshots': [
                {
                    'CacheNodeCreateTime': datetime(2016, 12, 21, 22, 27, 12, 2, 356, 0),
                    'CacheNodeId': '0001',
                    'CacheSize': '3 MB',
                    'SnapshotCreateTime': datetime(2016, 12, 21, 22, 30, 26, 2, 356, 0),
                },
            ],
            'NumCacheNodes': 1,
            'Port': 6379,
            'PreferredAvailabilityZone': 'us-east-1c',
            'PreferredMaintenanceWindow': 'fri:05:30-fri:06:30',
            'SnapshotName': 'snapshot-20161212',
            'SnapshotRetentionLimit': 7,
            'SnapshotSource': 'manual',
            'SnapshotStatus': 'available',
            'SnapshotWindow': '10:00-11:00',
            'VpcId': 'vpc-91280df6',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'Snapshots': [
            {
                'SnapshotName': 'string',
                'ReplicationGroupId': 'string',
                'ReplicationGroupDescription': 'string',
                'CacheClusterId': 'string',
                'SnapshotStatus': 'string',
                'SnapshotSource': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'NumCacheNodes': 123,
                'PreferredAvailabilityZone': 'string',
                'CacheClusterCreateTime': datetime(2015, 1, 1),
                'PreferredMaintenanceWindow': 'string',
                'TopicArn': 'string',
                'Port': 123,
                'CacheParameterGroupName': 'string',
                'CacheSubnetGroupName': 'string',
                'VpcId': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'NumNodeGroups': 123,
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'NodeSnapshots': [
                    {
                        'CacheClusterId': 'string',
                        'NodeGroupId': 'string',
                        'CacheNodeId': 'string',
                        'NodeGroupConfiguration': {
                            'NodeGroupId': 'string',
                            'Slots': 'string',
                            'ReplicaCount': 123,
                            'PrimaryAvailabilityZone': 'string',
                            'ReplicaAvailabilityZones': [
                                'string',
                            ]
                        },
                        'CacheSize': 'string',
                        'CacheNodeCreateTime': datetime(2015, 1, 1),
                        'SnapshotCreateTime': datetime(2015, 1, 1)
                    },
                ],
                'KmsKeyId': 'string',
                'ARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    General purpose:
    Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
    Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
    
    
    Compute optimized:
    Previous generation: (not recommended)  C1 node types: cache.c1.xlarge
    
    
    Memory optimized:
    Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
    Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    
    
    
    """
    pass

def describe_update_actions(ServiceUpdateName=None, ReplicationGroupIds=None, CacheClusterIds=None, Engine=None, ServiceUpdateStatus=None, ServiceUpdateTimeRange=None, UpdateActionStatus=None, ShowNodeLevelUpdateStatus=None, MaxRecords=None, Marker=None):
    """
    Returns details of the update actions
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_update_actions(
        ServiceUpdateName='string',
        ReplicationGroupIds=[
            'string',
        ],
        CacheClusterIds=[
            'string',
        ],
        Engine='string',
        ServiceUpdateStatus=[
            'available'|'cancelled'|'expired',
        ],
        ServiceUpdateTimeRange={
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1)
        },
        UpdateActionStatus=[
            'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete'|'scheduling'|'scheduled'|'not-applicable',
        ],
        ShowNodeLevelUpdateStatus=True|False,
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ServiceUpdateName: string
    :param ServiceUpdateName: The unique ID of the service update

    :type ReplicationGroupIds: list
    :param ReplicationGroupIds: The replication group IDs\n\n(string) --\n\n

    :type CacheClusterIds: list
    :param CacheClusterIds: The cache cluster IDs\n\n(string) --\n\n

    :type Engine: string
    :param Engine: The Elasticache engine to which the update applies. Either Redis or Memcached

    :type ServiceUpdateStatus: list
    :param ServiceUpdateStatus: The status of the service update\n\n(string) --\n\n

    :type ServiceUpdateTimeRange: dict
    :param ServiceUpdateTimeRange: The range of time specified to search for service updates that are in available status\n\nStartTime (datetime) --The start time of the time range filter\n\nEndTime (datetime) --The end time of the time range filter\n\n\n

    :type UpdateActionStatus: list
    :param UpdateActionStatus: The status of the update action.\n\n(string) --\n\n

    :type ShowNodeLevelUpdateStatus: boolean
    :param ShowNodeLevelUpdateStatus: Dictates whether to include node level update status in the response

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'UpdateActions': [
        {
            'ReplicationGroupId': 'string',
            'CacheClusterId': 'string',
            'ServiceUpdateName': 'string',
            'ServiceUpdateReleaseDate': datetime(2015, 1, 1),
            'ServiceUpdateSeverity': 'critical'|'important'|'medium'|'low',
            'ServiceUpdateStatus': 'available'|'cancelled'|'expired',
            'ServiceUpdateRecommendedApplyByDate': datetime(2015, 1, 1),
            'ServiceUpdateType': 'security-update',
            'UpdateActionAvailableDate': datetime(2015, 1, 1),
            'UpdateActionStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete'|'scheduling'|'scheduled'|'not-applicable',
            'NodesUpdated': 'string',
            'UpdateActionStatusModifiedDate': datetime(2015, 1, 1),
            'SlaMet': 'yes'|'no'|'n/a',
            'NodeGroupUpdateStatus': [
                {
                    'NodeGroupId': 'string',
                    'NodeGroupMemberUpdateStatus': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'NodeUpdateStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete',
                            'NodeDeletionDate': datetime(2015, 1, 1),
                            'NodeUpdateStartDate': datetime(2015, 1, 1),
                            'NodeUpdateEndDate': datetime(2015, 1, 1),
                            'NodeUpdateInitiatedBy': 'system'|'customer',
                            'NodeUpdateInitiatedDate': datetime(2015, 1, 1),
                            'NodeUpdateStatusModifiedDate': datetime(2015, 1, 1)
                        },
                    ]
                },
            ],
            'CacheNodeUpdateStatus': [
                {
                    'CacheNodeId': 'string',
                    'NodeUpdateStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete',
                    'NodeDeletionDate': datetime(2015, 1, 1),
                    'NodeUpdateStartDate': datetime(2015, 1, 1),
                    'NodeUpdateEndDate': datetime(2015, 1, 1),
                    'NodeUpdateInitiatedBy': 'system'|'customer',
                    'NodeUpdateInitiatedDate': datetime(2015, 1, 1),
                    'NodeUpdateStatusModifiedDate': datetime(2015, 1, 1)
                },
            ],
            'EstimatedUpdateTime': 'string',
            'Engine': 'string'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

UpdateActions (list) --
Returns a list of update actions

(dict) --
The status of the service update for a specific replication group

ReplicationGroupId (string) --
The ID of the replication group

CacheClusterId (string) --
The ID of the cache cluster

ServiceUpdateName (string) --
The unique ID of the service update

ServiceUpdateReleaseDate (datetime) --
The date the update is first available

ServiceUpdateSeverity (string) --
The severity of the service update

ServiceUpdateStatus (string) --
The status of the service update

ServiceUpdateRecommendedApplyByDate (datetime) --
The recommended date to apply the service update to ensure compliance. For information on compliance, see Self-Service Security Updates for Compliance .

ServiceUpdateType (string) --
Reflects the nature of the service update

UpdateActionAvailableDate (datetime) --
The date that the service update is available to a replication group

UpdateActionStatus (string) --
The status of the update action

NodesUpdated (string) --
The progress of the service update on the replication group

UpdateActionStatusModifiedDate (datetime) --
The date when the UpdateActionStatus was last modified

SlaMet (string) --
If yes, all nodes in the replication group have been updated by the recommended apply-by date. If no, at least one node in the replication group have not been updated by the recommended apply-by date. If N/A, the replication group was created after the recommended apply-by date.

NodeGroupUpdateStatus (list) --
The status of the service update on the node group

(dict) --
The status of the service update on the node group

NodeGroupId (string) --
The ID of the node group

NodeGroupMemberUpdateStatus (list) --
The status of the service update on the node group member

(dict) --
The status of the service update on the node group member

CacheClusterId (string) --
The cache cluster ID

CacheNodeId (string) --
The node ID of the cache cluster

NodeUpdateStatus (string) --
The update status of the node

NodeDeletionDate (datetime) --
The deletion date of the node

NodeUpdateStartDate (datetime) --
The start date of the update for a node

NodeUpdateEndDate (datetime) --
The end date of the update for a node

NodeUpdateInitiatedBy (string) --
Reflects whether the update was initiated by the customer or automatically applied

NodeUpdateInitiatedDate (datetime) --
The date when the update is triggered

NodeUpdateStatusModifiedDate (datetime) --
The date when the NodeUpdateStatus was last modified









CacheNodeUpdateStatus (list) --
The status of the service update on the cache node

(dict) --
The status of the service update on the cache node

CacheNodeId (string) --
The node ID of the cache cluster

NodeUpdateStatus (string) --
The update status of the node

NodeDeletionDate (datetime) --
The deletion date of the node

NodeUpdateStartDate (datetime) --
The start date of the update for a node

NodeUpdateEndDate (datetime) --
The end date of the update for a node

NodeUpdateInitiatedBy (string) --
Reflects whether the update was initiated by the customer or automatically applied

NodeUpdateInitiatedDate (datetime) --
The date when the update is triggered

NodeUpdateStatusModifiedDate (datetime) --
The date when the NodeUpdateStatus was last modified>





EstimatedUpdateTime (string) --
The estimated length of time for the update to complete

Engine (string) --
The Elasticache engine to which the update applies. Either Redis or Memcached











Exceptions

ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Marker': 'string',
        'UpdateActions': [
            {
                'ReplicationGroupId': 'string',
                'CacheClusterId': 'string',
                'ServiceUpdateName': 'string',
                'ServiceUpdateReleaseDate': datetime(2015, 1, 1),
                'ServiceUpdateSeverity': 'critical'|'important'|'medium'|'low',
                'ServiceUpdateStatus': 'available'|'cancelled'|'expired',
                'ServiceUpdateRecommendedApplyByDate': datetime(2015, 1, 1),
                'ServiceUpdateType': 'security-update',
                'UpdateActionAvailableDate': datetime(2015, 1, 1),
                'UpdateActionStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete'|'scheduling'|'scheduled'|'not-applicable',
                'NodesUpdated': 'string',
                'UpdateActionStatusModifiedDate': datetime(2015, 1, 1),
                'SlaMet': 'yes'|'no'|'n/a',
                'NodeGroupUpdateStatus': [
                    {
                        'NodeGroupId': 'string',
                        'NodeGroupMemberUpdateStatus': [
                            {
                                'CacheClusterId': 'string',
                                'CacheNodeId': 'string',
                                'NodeUpdateStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete',
                                'NodeDeletionDate': datetime(2015, 1, 1),
                                'NodeUpdateStartDate': datetime(2015, 1, 1),
                                'NodeUpdateEndDate': datetime(2015, 1, 1),
                                'NodeUpdateInitiatedBy': 'system'|'customer',
                                'NodeUpdateInitiatedDate': datetime(2015, 1, 1),
                                'NodeUpdateStatusModifiedDate': datetime(2015, 1, 1)
                            },
                        ]
                    },
                ],
                'CacheNodeUpdateStatus': [
                    {
                        'CacheNodeId': 'string',
                        'NodeUpdateStatus': 'not-applied'|'waiting-to-start'|'in-progress'|'stopping'|'stopped'|'complete',
                        'NodeDeletionDate': datetime(2015, 1, 1),
                        'NodeUpdateStartDate': datetime(2015, 1, 1),
                        'NodeUpdateEndDate': datetime(2015, 1, 1),
                        'NodeUpdateInitiatedBy': 'system'|'customer',
                        'NodeUpdateInitiatedDate': datetime(2015, 1, 1),
                        'NodeUpdateStatusModifiedDate': datetime(2015, 1, 1)
                    },
                ],
                'EstimatedUpdateTime': 'string',
                'Engine': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.InvalidParameterValueException
    ElastiCache.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def disassociate_global_replication_group(GlobalReplicationGroupId=None, ReplicationGroupId=None, ReplicationGroupRegion=None):
    """
    Remove a secondary cluster from the Global Datastore using the Global Datastore name. The secondary cluster will no longer receive updates from the primary cluster, but will remain as a standalone cluster in that AWS region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_global_replication_group(
        GlobalReplicationGroupId='string',
        ReplicationGroupId='string',
        ReplicationGroupRegion='string'
    )
    
    
    :type GlobalReplicationGroupId: string
    :param GlobalReplicationGroupId: [REQUIRED]\nThe name of the Global Datastore\n

    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe name of the secondary cluster you wish to remove from the Global Datastore\n

    :type ReplicationGroupRegion: string
    :param ReplicationGroupRegion: [REQUIRED]\nThe AWS region of secondary cluster you wish to remove from the Global Datastore\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalReplicationGroup': {
        'GlobalReplicationGroupId': 'string',
        'GlobalReplicationGroupDescription': 'string',
        'Status': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'Members': [
            {
                'ReplicationGroupId': 'string',
                'ReplicationGroupRegion': 'string',
                'Role': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'Status': 'string'
            },
        ],
        'ClusterEnabled': True|False,
        'GlobalNodeGroups': [
            {
                'GlobalNodeGroupId': 'string',
                'Slots': 'string'
            },
        ],
        'AuthTokenEnabled': True|False,
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

GlobalReplicationGroup (dict) --
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different AWS region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.


GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupDescription (string) --
The optional description of the Global Datastore

Status (string) --
The status of the Global Datastore

CacheNodeType (string) --
The cache node type of the Global Datastore

Engine (string) --
The Elasticache engine. For Redis only.

EngineVersion (string) --
The Elasticache Redis engine version. For preview, it is Redis version 5.0.5 only.

Members (list) --
The replication groups that comprise the Global Datastore.

(dict) --
A member of a Global Datastore. It contains the Replication Group Id, the AWS region and the role of the replication group.

ReplicationGroupId (string) --
The replication group id of the Global Datastore member.

ReplicationGroupRegion (string) --
The AWS region of the Global Datastore member.

Role (string) --
Indicates the role of the replication group, primary or secondary.

AutomaticFailover (string) --
Indicates whether automatic failover is enabled for the replication group.

Status (string) --
The status of the membership of the replication group.





ClusterEnabled (boolean) --
A flag that indicates whether the Global Datastore is cluster enabled.

GlobalNodeGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId (string) --
The name of the global node group

Slots (string) --
The keyspace for this node group





AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true. You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.


ARN (string) --
The ARN (Amazon Resource Name) of the global replication group.









Exceptions

ElastiCache.Client.exceptions.GlobalReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'GlobalReplicationGroup': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupDescription': 'string',
            'Status': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'Members': [
                {
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupRegion': 'string',
                    'Role': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'Status': 'string'
                },
            ],
            'ClusterEnabled': True|False,
            'GlobalNodeGroups': [
                {
                    'GlobalNodeGroupId': 'string',
                    'Slots': 'string'
                },
            ],
            'AuthTokenEnabled': True|False,
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.
    
    """
    pass

def failover_global_replication_group(GlobalReplicationGroupId=None, PrimaryRegion=None, PrimaryReplicationGroupId=None):
    """
    Used to failover the primary region to a selected secondary region. The selected secondary region will be come primary, and all other clusters will become secondary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.failover_global_replication_group(
        GlobalReplicationGroupId='string',
        PrimaryRegion='string',
        PrimaryReplicationGroupId='string'
    )
    
    
    :type GlobalReplicationGroupId: string
    :param GlobalReplicationGroupId: [REQUIRED]\nThe name of the Global Datastore\n

    :type PrimaryRegion: string
    :param PrimaryRegion: [REQUIRED]\nThe AWS region of the primary cluster of the Global Datastore\n

    :type PrimaryReplicationGroupId: string
    :param PrimaryReplicationGroupId: [REQUIRED]\nThe name of the primary replication group\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalReplicationGroup': {
        'GlobalReplicationGroupId': 'string',
        'GlobalReplicationGroupDescription': 'string',
        'Status': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'Members': [
            {
                'ReplicationGroupId': 'string',
                'ReplicationGroupRegion': 'string',
                'Role': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'Status': 'string'
            },
        ],
        'ClusterEnabled': True|False,
        'GlobalNodeGroups': [
            {
                'GlobalNodeGroupId': 'string',
                'Slots': 'string'
            },
        ],
        'AuthTokenEnabled': True|False,
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

GlobalReplicationGroup (dict) --
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different AWS region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.


GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupDescription (string) --
The optional description of the Global Datastore

Status (string) --
The status of the Global Datastore

CacheNodeType (string) --
The cache node type of the Global Datastore

Engine (string) --
The Elasticache engine. For Redis only.

EngineVersion (string) --
The Elasticache Redis engine version. For preview, it is Redis version 5.0.5 only.

Members (list) --
The replication groups that comprise the Global Datastore.

(dict) --
A member of a Global Datastore. It contains the Replication Group Id, the AWS region and the role of the replication group.

ReplicationGroupId (string) --
The replication group id of the Global Datastore member.

ReplicationGroupRegion (string) --
The AWS region of the Global Datastore member.

Role (string) --
Indicates the role of the replication group, primary or secondary.

AutomaticFailover (string) --
Indicates whether automatic failover is enabled for the replication group.

Status (string) --
The status of the membership of the replication group.





ClusterEnabled (boolean) --
A flag that indicates whether the Global Datastore is cluster enabled.

GlobalNodeGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId (string) --
The name of the global node group

Slots (string) --
The keyspace for this node group





AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true. You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.


ARN (string) --
The ARN (Amazon Resource Name) of the global replication group.









Exceptions

ElastiCache.Client.exceptions.GlobalReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'GlobalReplicationGroup': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupDescription': 'string',
            'Status': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'Members': [
                {
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupRegion': 'string',
                    'Role': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'Status': 'string'
                },
            ],
            'ClusterEnabled': True|False,
            'GlobalNodeGroups': [
                {
                    'GlobalNodeGroupId': 'string',
                    'Slots': 'string'
                },
            ],
            'AuthTokenEnabled': True|False,
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.
    
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

def increase_node_groups_in_global_replication_group(GlobalReplicationGroupId=None, NodeGroupCount=None, RegionalConfigurations=None, ApplyImmediately=None):
    """
    Increase the number of node groups in the Global Datastore
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.increase_node_groups_in_global_replication_group(
        GlobalReplicationGroupId='string',
        NodeGroupCount=123,
        RegionalConfigurations=[
            {
                'ReplicationGroupId': 'string',
                'ReplicationGroupRegion': 'string',
                'ReshardingConfiguration': [
                    {
                        'NodeGroupId': 'string',
                        'PreferredAvailabilityZones': [
                            'string',
                        ]
                    },
                ]
            },
        ],
        ApplyImmediately=True|False
    )
    
    
    :type GlobalReplicationGroupId: string
    :param GlobalReplicationGroupId: [REQUIRED]\nThe name of the Global Datastore\n

    :type NodeGroupCount: integer
    :param NodeGroupCount: [REQUIRED]\nThe number of node groups you wish to add\n

    :type RegionalConfigurations: list
    :param RegionalConfigurations: Describes the replication group IDs, the AWS regions where they are stored and the shard configuration for each that comprise the Global Datastore\n\n(dict) --A list of the replication groups\n\nReplicationGroupId (string) -- [REQUIRED]The name of the secondary cluster\n\nReplicationGroupRegion (string) -- [REQUIRED]The AWS region where the cluster is stored\n\nReshardingConfiguration (list) -- [REQUIRED]A list of PreferredAvailabilityZones objects that specifies the configuration of a node group in the resharded cluster.\n\n(dict) --A list of PreferredAvailabilityZones objects that specifies the configuration of a node group in the resharded cluster.\n\nNodeGroupId (string) --Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.\n\nPreferredAvailabilityZones (list) --A list of preferred availability zones for the nodes in this cluster.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: [REQUIRED]\nIndicates that the process begins immediately. At present, the only permitted value for this parameter is true.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalReplicationGroup': {
        'GlobalReplicationGroupId': 'string',
        'GlobalReplicationGroupDescription': 'string',
        'Status': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'Members': [
            {
                'ReplicationGroupId': 'string',
                'ReplicationGroupRegion': 'string',
                'Role': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'Status': 'string'
            },
        ],
        'ClusterEnabled': True|False,
        'GlobalNodeGroups': [
            {
                'GlobalNodeGroupId': 'string',
                'Slots': 'string'
            },
        ],
        'AuthTokenEnabled': True|False,
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

GlobalReplicationGroup (dict) --
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different AWS region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.


GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupDescription (string) --
The optional description of the Global Datastore

Status (string) --
The status of the Global Datastore

CacheNodeType (string) --
The cache node type of the Global Datastore

Engine (string) --
The Elasticache engine. For Redis only.

EngineVersion (string) --
The Elasticache Redis engine version. For preview, it is Redis version 5.0.5 only.

Members (list) --
The replication groups that comprise the Global Datastore.

(dict) --
A member of a Global Datastore. It contains the Replication Group Id, the AWS region and the role of the replication group.

ReplicationGroupId (string) --
The replication group id of the Global Datastore member.

ReplicationGroupRegion (string) --
The AWS region of the Global Datastore member.

Role (string) --
Indicates the role of the replication group, primary or secondary.

AutomaticFailover (string) --
Indicates whether automatic failover is enabled for the replication group.

Status (string) --
The status of the membership of the replication group.





ClusterEnabled (boolean) --
A flag that indicates whether the Global Datastore is cluster enabled.

GlobalNodeGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId (string) --
The name of the global node group

Slots (string) --
The keyspace for this node group





AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true. You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.


ARN (string) --
The ARN (Amazon Resource Name) of the global replication group.









Exceptions

ElastiCache.Client.exceptions.GlobalReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException


    :return: {
        'GlobalReplicationGroup': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupDescription': 'string',
            'Status': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'Members': [
                {
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupRegion': 'string',
                    'Role': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'Status': 'string'
                },
            ],
            'ClusterEnabled': True|False,
            'GlobalNodeGroups': [
                {
                    'GlobalNodeGroupId': 'string',
                    'Slots': 'string'
                },
            ],
            'AuthTokenEnabled': True|False,
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.
    
    """
    pass

def increase_replica_count(ReplicationGroupId=None, NewReplicaCount=None, ReplicaConfiguration=None, ApplyImmediately=None):
    """
    Dynamically increases the number of replics in a Redis (cluster mode disabled) replication group or the number of replica nodes in one or more node groups (shards) of a Redis (cluster mode enabled) replication group. This operation is performed with no cluster down time.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.increase_replica_count(
        ReplicationGroupId='string',
        NewReplicaCount=123,
        ReplicaConfiguration=[
            {
                'NodeGroupId': 'string',
                'NewReplicaCount': 123,
                'PreferredAvailabilityZones': [
                    'string',
                ]
            },
        ],
        ApplyImmediately=True|False
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe id of the replication group to which you want to add replica nodes.\n

    :type NewReplicaCount: integer
    :param NewReplicaCount: The number of read replica nodes you want at the completion of this operation. For Redis (cluster mode disabled) replication groups, this is the number of replica nodes in the replication group. For Redis (cluster mode enabled) replication groups, this is the number of replica nodes in each of the replication group\'s node groups.

    :type ReplicaConfiguration: list
    :param ReplicaConfiguration: A list of ConfigureShard objects that can be used to configure each shard in a Redis (cluster mode enabled) replication group. The ConfigureShard has three members: NewReplicaCount , NodeGroupId , and PreferredAvailabilityZones .\n\n(dict) --Node group (shard) configuration options when adding or removing replicas. Each node group (shard) configuration has the following members: NodeGroupId, NewReplicaCount, and PreferredAvailabilityZones.\n\nNodeGroupId (string) -- [REQUIRED]The 4-digit id for the node group you are configuring. For Redis (cluster mode disabled) replication groups, the node group id is always 0001. To find a Redis (cluster mode enabled)\'s node group\'s (shard\'s) id, see Finding a Shard\'s Id .\n\nNewReplicaCount (integer) -- [REQUIRED]The number of replicas you want in this node group at the end of this operation. The maximum value for NewReplicaCount is 5. The minimum value depends upon the type of Redis replication group you are working with.\nThe minimum number of replicas in a shard or replication group is:\n\nRedis (cluster mode disabled)\nIf Multi-AZ with Automatic Failover is enabled: 1\nIf Multi-AZ with Automatic Failover is not enable: 0\n\n\nRedis (cluster mode enabled): 0 (though you will not be able to failover to a replica if your primary node fails)\n\n\nPreferredAvailabilityZones (list) --A list of PreferredAvailabilityZone strings that specify which availability zones the replication group\'s nodes are to be in. The nummber of PreferredAvailabilityZone values must equal the value of NewReplicaCount plus 1 to account for the primary node. If this member of ReplicaConfiguration is omitted, ElastiCache for Redis selects the availability zone for each of the replicas.\n\n(string) --\n\n\n\n\n\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: [REQUIRED]\nIf True , the number of replica nodes is increased immediately. ApplyImmediately=False is not currently supported.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationGroup': {
        'ReplicationGroupId': 'string',
        'Description': 'string',
        'GlobalReplicationGroupInfo': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupMemberRole': 'string'
        },
        'Status': 'string',
        'PendingModifiedValues': {
            'PrimaryClusterId': 'string',
            'AutomaticFailoverStatus': 'enabled'|'disabled',
            'Resharding': {
                'SlotMigration': {
                    'ProgressPercentage': 123.0
                }
            },
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'MemberClusters': [
            'string',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': 'string',
                'Status': 'string',
                'PrimaryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ReaderEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'Slots': 'string',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'string',
                        'CacheNodeId': 'string',
                        'ReadEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'PreferredAvailabilityZone': 'string',
                        'CurrentRole': 'string'
                    },
                ]
            },
        ],
        'SnapshottingClusterId': 'string',
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'ClusterEnabled': True|False,
        'CacheNodeType': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

ReplicationGroup (dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.









Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.InvalidVPCNetworkStateFault
ElastiCache.Client.exceptions.InsufficientCacheClusterCapacityFault
ElastiCache.Client.exceptions.ClusterQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.NodeGroupsPerReplicationGroupQuotaExceededFault
ElastiCache.Client.exceptions.NodeQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.NoOperationFault
ElastiCache.Client.exceptions.InvalidKMSKeyFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled): T1 node types.
    Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def list_allowed_node_type_modifications(CacheClusterId=None, ReplicationGroupId=None):
    """
    Lists all available node types that you can scale your Redis cluster\'s or replication group\'s current node type.
    When you use the ModifyCacheCluster or ModifyReplicationGroup operations to scale your cluster or replication group, the value of the CacheNodeType parameter must be one of the node types returned by this operation.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists all available node types that you can scale your Redis cluster\'s or replication group\'s current node type up to.
    Expected Output:
    
    :example: response = client.list_allowed_node_type_modifications(
        CacheClusterId='string',
        ReplicationGroupId='string'
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: The name of the cluster you want to scale up to a larger node instanced type. ElastiCache uses the cluster id to identify the current node type of this cluster and from that to create a list of node types you can scale up to.\n\nWarning\nYou must provide a value for either the CacheClusterId or the ReplicationGroupId .\n\n

    :type ReplicationGroupId: string
    :param ReplicationGroupId: The name of the replication group want to scale up to a larger node type. ElastiCache uses the replication group id to identify the current node type being used by this replication group, and from that to create a list of node types you can scale up to.\n\nWarning\nYou must provide a value for either the CacheClusterId or the ReplicationGroupId .\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ScaleUpModifications': [
        'string',
    ],
    'ScaleDownModifications': [
        'string',
    ]
}


Response Structure

(dict) --
Represents the allowed node types you can use to modify your cluster or replication group.

ScaleUpModifications (list) --
A string list, each element of which specifies a cache node type which you can use to scale your cluster or replication group.
When scaling up a Redis cluster or replication group using ModifyCacheCluster or ModifyReplicationGroup , use a value from this list for the CacheNodeType parameter.

(string) --


ScaleDownModifications (list) --
A string list, each element of which specifies a cache node type which you can use to scale your cluster or replication group. When scaling down a Redis cluster or replication group using ModifyCacheCluster or ModifyReplicationGroup, use a value from this list for the CacheNodeType parameter.

(string) --








Exceptions

ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterCombinationException
ElastiCache.Client.exceptions.InvalidParameterValueException

Examples
Lists all available node types that you can scale your Redis cluster\'s or replication group\'s current node type up to.
response = client.list_allowed_node_type_modifications(
    CacheClusterId='mycluster',
)

print(response)


Expected Output:
{
    'ScaleUpModifications': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ScaleUpModifications': [
            'string',
        ],
        'ScaleDownModifications': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(ResourceName=None):
    """
    Lists all cost allocation tags currently on the named resource. A cost allocation tag is a key-value pair where the key is case-sensitive and the value is optional. You can use cost allocation tags to categorize and track your AWS costs.
    If the cluster is not in the available state, ListTagsForResource returns an error.
    You can have a maximum of 50 cost allocation tags on an ElastiCache resource. For more information, see Monitoring Costs with Tags .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists all cost allocation tags currently on the named resource. A cost allocation tag is a key-value pair where the key is case-sensitive and the value is optional. You can use cost allocation tags to categorize and track your AWS costs.
    Expected Output:
    
    :example: response = client.list_tags_for_resource(
        ResourceName='string'
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource for which you want the list of tags, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :rtype: dict
ReturnsResponse Syntax{
    'TagList': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --Represents the output from the AddTagsToResource , ListTagsForResource , and RemoveTagsFromResource operations.

TagList (list) --A list of cost allocation tags as key-value pairs.

(dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

Key (string) --The key for the tag. May not be null.

Value (string) --The tag\'s value. May be null.










Exceptions

ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.SnapshotNotFoundFault
ElastiCache.Client.exceptions.InvalidARNFault

Examples
Lists all cost allocation tags currently on the named resource. A cost allocation tag is a key-value pair where the key is case-sensitive and the value is optional. You can use cost allocation tags to categorize and track your AWS costs.
response = client.list_tags_for_resource(
    ResourceName='arn:aws:elasticache:us-west-2:<my-account-id>:cluster:mycluster',
)

print(response)


Expected Output:
{
    'TagList': [
        {
            'Key': 'APIVersion',
            'Value': '20150202',
        },
        {
            'Key': 'Service',
            'Value': 'ElastiCache',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def modify_cache_cluster(CacheClusterId=None, NumCacheNodes=None, CacheNodeIdsToRemove=None, AZMode=None, NewAvailabilityZones=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, PreferredMaintenanceWindow=None, NotificationTopicArn=None, CacheParameterGroupName=None, NotificationTopicStatus=None, ApplyImmediately=None, EngineVersion=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None, CacheNodeType=None, AuthToken=None, AuthTokenUpdateStrategy=None):
    """
    Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration parameters by specifying the parameters and the new values.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Copies a snapshot to a specified name.
    Expected Output:
    
    :example: response = client.modify_cache_cluster(
        CacheClusterId='string',
        NumCacheNodes=123,
        CacheNodeIdsToRemove=[
            'string',
        ],
        AZMode='single-az'|'cross-az',
        NewAvailabilityZones=[
            'string',
        ],
        CacheSecurityGroupNames=[
            'string',
        ],
        SecurityGroupIds=[
            'string',
        ],
        PreferredMaintenanceWindow='string',
        NotificationTopicArn='string',
        CacheParameterGroupName='string',
        NotificationTopicStatus='string',
        ApplyImmediately=True|False,
        EngineVersion='string',
        AutoMinorVersionUpgrade=True|False,
        SnapshotRetentionLimit=123,
        SnapshotWindow='string',
        CacheNodeType='string',
        AuthToken='string',
        AuthTokenUpdateStrategy='SET'|'ROTATE'
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: [REQUIRED]\nThe cluster identifier. This value is stored as a lowercase string.\n

    :type NumCacheNodes: integer
    :param NumCacheNodes: The number of cache nodes that the cluster should have. If the value for NumCacheNodes is greater than the sum of the number of current cache nodes and the number of cache nodes pending creation (which may be zero), more nodes are added. If the value is less than the number of existing cache nodes, nodes are removed. If the value is equal to the number of current cache nodes, any pending add or remove requests are canceled.\nIf you are removing cache nodes, you must use the CacheNodeIdsToRemove parameter to provide the IDs of the specific cache nodes to remove.\nFor clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.\n\nNote\nAdding or removing Memcached cache nodes can be applied immediately or as a pending operation (see ApplyImmediately ).\nA pending operation to modify the number of cache nodes in a cluster during its maintenance window, whether by adding or removing nodes in accordance with the scale out architecture, is not queued. The customer\'s latest request to add or remove nodes to the cluster overrides any previous pending operations to modify the number of cache nodes in the cluster. For example, a request to remove 2 nodes would override a previous pending operation to remove 3 nodes. Similarly, a request to add 2 nodes would override a previous pending operation to remove 3 nodes and vice versa. As Memcached cache nodes may now be provisioned in different Availability Zones with flexible cache node placement, a request to add nodes does not automatically override a previous pending operation to add nodes. The customer can modify the previous pending operation to add more nodes or explicitly cancel the pending request and retry the new request. To cancel pending operations to modify the number of cache nodes in a cluster, use the ModifyCacheCluster request and set NumCacheNodes equal to the number of cache nodes currently in the cluster.\n\n

    :type CacheNodeIdsToRemove: list
    :param CacheNodeIdsToRemove: A list of cache node IDs to be removed. A node ID is a numeric identifier (0001, 0002, etc.). This parameter is only valid when NumCacheNodes is less than the existing number of cache nodes. The number of cache node IDs supplied in this parameter must match the difference between the existing number of cache nodes in the cluster or pending cache nodes, whichever is greater, and the value of NumCacheNodes in the request.\nFor example: If you have 3 active cache nodes, 7 pending cache nodes, and the number of cache nodes in this ModifyCacheCluster call is 5, you must list 2 (7 - 5) cache node IDs to remove.\n\n(string) --\n\n

    :type AZMode: string
    :param AZMode: Specifies whether the new nodes in this Memcached cluster are all created in a single Availability Zone or created across multiple Availability Zones.\nValid values: single-az | cross-az .\nThis option is only supported for Memcached clusters.\n\nNote\nYou cannot specify single-az if the Memcached cluster already has cache nodes in different Availability Zones. If cross-az is specified, existing Memcached nodes remain in their current Availability Zone.\nOnly newly created nodes are located in different Availability Zones.\n\n

    :type NewAvailabilityZones: list
    :param NewAvailabilityZones: The list of Availability Zones where the new Memcached cache nodes are created.\nThis parameter is only valid when NumCacheNodes in the request is greater than the sum of the number of active cache nodes and the number of cache nodes pending creation (which may be zero). The number of Availability Zones supplied in this list must match the cache nodes being added in this request.\nThis option is only supported on Memcached clusters.\nScenarios:\n\nScenario 1: You have 3 active nodes and wish to add 2 nodes. Specify NumCacheNodes=5 (3 + 2) and optionally specify two Availability Zones for the two new nodes.\nScenario 2: You have 3 active nodes and 2 nodes pending creation (from the scenario 1 call) and want to add 1 more node. Specify NumCacheNodes=6 ((3 + 2) + 1) and optionally specify an Availability Zone for the new node.\nScenario 3: You want to cancel all pending operations. Specify NumCacheNodes=3 to cancel all pending operations.\n\nThe Availability Zone placement of nodes pending creation cannot be modified. If you wish to cancel any nodes pending creation, add 0 nodes by setting NumCacheNodes to the number of current nodes.\nIf cross-az is specified, existing Memcached nodes remain in their current Availability Zone. Only newly created nodes can be located in different Availability Zones. For guidance on how to move existing Memcached nodes to different Availability Zones, see the Availability Zone Considerations section of Cache Node Considerations for Memcached .\n\nImpact of new add/remove requests upon pending requests\n\nScenario-1\nPending Action: Delete\nNew Request: Delete\nResult: The new delete, pending or immediate, replaces the pending delete.\n\n\nScenario-2\nPending Action: Delete\nNew Request: Create\nResult: The new create, pending or immediate, replaces the pending delete.\n\n\nScenario-3\nPending Action: Create\nNew Request: Delete\nResult: The new delete, pending or immediate, replaces the pending create.\n\n\nScenario-4\nPending Action: Create\nNew Request: Create\nResult: The new create is added to the pending create.\n\n\nWarning\nImportant: If the new create request is Apply Immediately - Yes , all creates are performed immediately. If the new create request is Apply Immediately - No , all creates are pending.\n\n\n\n\n(string) --\n\n

    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: A list of cache security group names to authorize on this cluster. This change is asynchronously applied as soon as possible.\nYou can use this parameter only with clusters that are created outside of an Amazon Virtual Private Cloud (Amazon VPC).\nConstraints: Must contain no more than 255 alphanumeric characters. Must not be 'Default'.\n\n(string) --\n\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: Specifies the VPC Security Groups associated with the cluster.\nThis parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud (Amazon VPC).\n\n(string) --\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.\nValid values for ddd are:\n\nsun\nmon\ntue\nwed\nthu\nfri\nsat\n\nExample: sun:23:00-mon:01:30\n

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.\n\nNote\nThe Amazon SNS topic owner must be same as the cluster owner.\n\n

    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of the cache parameter group to apply to this cluster. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for this request.

    :type NotificationTopicStatus: string
    :param NotificationTopicStatus: The status of the Amazon SNS notification topic. Notifications are sent only if the status is active .\nValid values: active | inactive\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: If true , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow setting for the cluster.\nIf false , changes to the cluster are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.\n\nWarning\nIf you perform a ModifyCacheCluster before a pending modification is applied, the pending modification is replaced by the newer modification.\n\nValid values: true | false\nDefault: false\n

    :type EngineVersion: string
    :param EngineVersion: The upgraded version of the cache engine to be run on the cache nodes.\n\nImportant: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster and create it anew with the earlier engine version.\n

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.

    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.\n\nNote\nIf the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.\n\n

    :type SnapshotWindow: string
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.

    :type CacheNodeType: string
    :param CacheNodeType: A valid cache node type that you want to scale this cluster up to.

    :type AuthToken: string
    :param AuthToken: Reserved parameter. The password used to access a password protected server. This parameter must be specified with the auth-token-update parameter. Password constraints:\n\nMust be only printable ASCII characters\nMust be at least 16 characters and no more than 128 characters in length\nCannot contain any of the following characters: \'/\', \''\', or \'@\', \'%\'\n\nFor more information, see AUTH password at AUTH .\n

    :type AuthTokenUpdateStrategy: string
    :param AuthTokenUpdateStrategy: Specifies the strategy to use to update the AUTH token. This parameter must be specified with the auth-token parameter. Possible values:\n\nRotate\nSet\n\nFor more information, see Authenticating Users with Redis AUTH\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheCluster': {
        'CacheClusterId': 'string',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClientDownloadLandingPage': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'CacheClusterStatus': 'string',
        'NumCacheNodes': 123,
        'PreferredAvailabilityZone': 'string',
        'CacheClusterCreateTime': datetime(2015, 1, 1),
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'NumCacheNodes': 123,
            'CacheNodeIdsToRemove': [
                'string',
            ],
            'EngineVersion': 'string',
            'CacheNodeType': 'string',
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'CacheSecurityGroups': [
            {
                'CacheSecurityGroupName': 'string',
                'Status': 'string'
            },
        ],
        'CacheParameterGroup': {
            'CacheParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'CacheNodeIdsToReboot': [
                'string',
            ]
        },
        'CacheSubnetGroupName': 'string',
        'CacheNodes': [
            {
                'CacheNodeId': 'string',
                'CacheNodeStatus': 'string',
                'CacheNodeCreateTime': datetime(2015, 1, 1),
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ParameterGroupStatus': 'string',
                'SourceCacheNodeId': 'string',
                'CustomerAvailabilityZone': 'string'
            },
        ],
        'AutoMinorVersionUpgrade': True|False,
        'SecurityGroups': [
            {
                'SecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'ReplicationGroupId': 'string',
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheCluster (dict) --
Contains all of the attributes of a specific cluster.

CacheClusterId (string) --
The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

ConfigurationEndpoint (dict) --
Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have .cfg in it.
Example: mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ClientDownloadLandingPage (string) --
The URL of the web page where you can download the latest ElastiCache client library.

CacheNodeType (string) --
The name of the compute and memory capacity node type for the cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Engine (string) --
The name of the cache engine (memcached or redis ) to be used for this cluster.

EngineVersion (string) --
The version of the cache engine that is used in this cluster.

CacheClusterStatus (string) --
The current state of this cluster, one of the following values: available , creating , deleted , deleting , incompatible-network , modifying , rebooting cluster nodes , restore-failed , or snapshotting .

NumCacheNodes (integer) --
The number of cache nodes in the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

CacheClusterCreateTime (datetime) --
The date and time when the cluster was created.

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for ddd are:

sun
mon
tue
wed
thu
fri
sat

Example: sun:23:00-mon:01:30

PendingModifiedValues (dict) --
A group of settings that are applied to the cluster in the future, or that are currently being applied.

NumCacheNodes (integer) --
The new number of cache nodes for the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

CacheNodeIdsToRemove (list) --
A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

(string) --


EngineVersion (string) --
The new cache engine version that the cluster runs.

CacheNodeType (string) --
The cache node type that this cluster or replication group is scaled to.

AuthTokenStatus (string) --
The auth token status



NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



CacheSecurityGroups (list) --
A list of cache security group elements, composed of name and status sub-elements.

(dict) --
Represents a cluster\'s status within a particular cache security group.

CacheSecurityGroupName (string) --
The name of the cache security group.

Status (string) --
The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





CacheParameterGroup (dict) --
Status of the cache parameter group.

CacheParameterGroupName (string) --
The name of the cache parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

CacheNodeIdsToReboot (list) --
A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

(string) --




CacheSubnetGroupName (string) --
The name of the cache subnet group associated with the cluster.

CacheNodes (list) --
A list of cache nodes that are members of the cluster.

(dict) --
Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster\'s protocol-compliant caching software - either Memcached or Redis.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


CacheNodeId (string) --
The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer\'s AWS account.

CacheNodeStatus (string) --
The current state of this cache node, one of the following values: available , creating , rebooting , or deleting .

CacheNodeCreateTime (datetime) --
The date and time when the cache node was created.

Endpoint (dict) --
The hostname for connecting to this cache node.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ParameterGroupStatus (string) --
The status of the parameter group applied to this cache node.

SourceCacheNodeId (string) --
The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

CustomerAvailabilityZone (string) --
The Availability Zone where this node was created and now resides.





AutoMinorVersionUpgrade (boolean) --
This parameter is currently disabled.

SecurityGroups (list) --
A list of VPC Security Groups associated with the cluster.

(dict) --
Represents a single cache security group and its status.

SecurityGroupId (string) --
The identifier of the cache security group.

Status (string) --
The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





ReplicationGroupId (string) --
The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.
Example: 05:00-09:00

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable at-rest encryption on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

ARN (string) --
The ARN (Amazon Resource Name) of the cache cluster.









Exceptions

ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.InvalidCacheSecurityGroupStateFault
ElastiCache.Client.exceptions.InsufficientCacheClusterCapacityFault
ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.NodeQuotaForClusterExceededFault
ElastiCache.Client.exceptions.NodeQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.CacheSecurityGroupNotFoundFault
ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidVPCNetworkStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Copies a snapshot to a specified name.
response = client.modify_cache_cluster(
    ApplyImmediately=True,
    CacheClusterId='redis-cluster',
    SnapshotRetentionLimit=14,
)

print(response)


Expected Output:
{
    'CacheCluster': {
        'AutoMinorVersionUpgrade': True,
        'CacheClusterCreateTime': datetime(2016, 12, 22, 16, 27, 56, 3, 357, 0),
        'CacheClusterId': 'redis-cluster',
        'CacheClusterStatus': 'available',
        'CacheNodeType': 'cache.r3.large',
        'CacheParameterGroup': {
            'CacheNodeIdsToReboot': [
            ],
            'CacheParameterGroupName': 'default.redis3.2',
            'ParameterApplyStatus': 'in-sync',
        },
        'CacheSecurityGroups': [
        ],
        'CacheSubnetGroupName': 'default',
        'ClientDownloadLandingPage': 'https://console.aws.amazon.com/elasticache/home#client-download:',
        'Engine': 'redis',
        'EngineVersion': '3.2.4',
        'NumCacheNodes': 1,
        'PendingModifiedValues': {
        },
        'PreferredAvailabilityZone': 'us-east-1e',
        'PreferredMaintenanceWindow': 'fri:09:00-fri:10:00',
        'SnapshotRetentionLimit': 14,
        'SnapshotWindow': '07:00-08:00',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheCluster': {
            'CacheClusterId': 'string',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClientDownloadLandingPage': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'CacheClusterStatus': 'string',
            'NumCacheNodes': 123,
            'PreferredAvailabilityZone': 'string',
            'CacheClusterCreateTime': datetime(2015, 1, 1),
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'NumCacheNodes': 123,
                'CacheNodeIdsToRemove': [
                    'string',
                ],
                'EngineVersion': 'string',
                'CacheNodeType': 'string',
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'CacheSecurityGroups': [
                {
                    'CacheSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CacheParameterGroup': {
                'CacheParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'CacheNodeIdsToReboot': [
                    'string',
                ]
            },
            'CacheSubnetGroupName': 'string',
            'CacheNodes': [
                {
                    'CacheNodeId': 'string',
                    'CacheNodeStatus': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ParameterGroupStatus': 'string',
                    'SourceCacheNodeId': 'string',
                    'CustomerAvailabilityZone': 'string'
                },
            ],
            'AutoMinorVersionUpgrade': True|False,
            'SecurityGroups': [
                {
                    'SecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'ReplicationGroupId': 'string',
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
    Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
    
    
    Compute optimized:
    Previous generation: (not recommended)  C1 node types: cache.c1.xlarge
    
    
    Memory optimized:
    Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
    Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    
    
    
    """
    pass

def modify_cache_parameter_group(CacheParameterGroupName=None, ParameterNameValues=None):
    """
    Modifies the parameters of a cache parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Modifies one or more parameter values in the specified parameter group. You cannot modify any default parameter group.
    Expected Output:
    
    :example: response = client.modify_cache_parameter_group(
        CacheParameterGroupName='string',
        ParameterNameValues=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string'
            },
        ]
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: [REQUIRED]\nThe name of the cache parameter group to modify.\n

    :type ParameterNameValues: list
    :param ParameterNameValues: [REQUIRED]\nAn array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be modified per request.\n\n(dict) --Describes a name-value pair that is used to update the value of a parameter.\n\nParameterName (string) --The name of the parameter.\n\nParameterValue (string) --The value of the parameter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheParameterGroupName': 'string'
}


Response Structure

(dict) --
Represents the output of one of the following operations:

ModifyCacheParameterGroup
ResetCacheParameterGroup


CacheParameterGroupName (string) --
The name of the cache parameter group.







Exceptions

ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidCacheParameterGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault

Examples
Modifies one or more parameter values in the specified parameter group. You cannot modify any default parameter group.
response = client.modify_cache_parameter_group(
    CacheParameterGroupName='custom-mem1-4',
    ParameterNameValues=[
        {
            'ParameterName': 'binding_protocol',
            'ParameterValue': 'ascii',
        },
        {
            'ParameterName': 'chunk_size',
            'ParameterValue': '96',
        },
    ],
)

print(response)


Expected Output:
{
    'CacheParameterGroupName': 'custom-mem1-4',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheParameterGroupName': 'string'
    }
    
    
    :returns: 
    ModifyCacheParameterGroup
    ResetCacheParameterGroup
    
    """
    pass

def modify_cache_subnet_group(CacheSubnetGroupName=None, CacheSubnetGroupDescription=None, SubnetIds=None):
    """
    Modifies an existing cache subnet group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Modifies an existing ElastiCache subnet group.
    Expected Output:
    
    :example: response = client.modify_cache_subnet_group(
        CacheSubnetGroupName='string',
        CacheSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: [REQUIRED]\nThe name for the cache subnet group. This value is stored as a lowercase string.\nConstraints: Must contain no more than 255 alphanumeric characters or hyphens.\nExample: mysubnetgroup\n

    :type CacheSubnetGroupDescription: string
    :param CacheSubnetGroupDescription: A description of the cache subnet group.

    :type SubnetIds: list
    :param SubnetIds: The EC2 subnet IDs for the cache subnet group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheSubnetGroup': {
        'CacheSubnetGroupName': 'string',
        'CacheSubnetGroupDescription': 'string',
        'VpcId': 'string',
        'Subnets': [
            {
                'SubnetIdentifier': 'string',
                'SubnetAvailabilityZone': {
                    'Name': 'string'
                }
            },
        ],
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheSubnetGroup (dict) --
Represents the output of one of the following operations:

CreateCacheSubnetGroup
ModifyCacheSubnetGroup


CacheSubnetGroupName (string) --
The name of the cache subnet group.

CacheSubnetGroupDescription (string) --
The description of the cache subnet group.

VpcId (string) --
The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

Subnets (list) --
A list of subnets associated with the cache subnet group.

(dict) --
Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

SubnetIdentifier (string) --
The unique identifier for the subnet.

SubnetAvailabilityZone (dict) --
The Availability Zone associated with the subnet.

Name (string) --
The name of the Availability Zone.







ARN (string) --
The ARN (Amazon Resource Name) of the cache subnet group.









Exceptions

ElastiCache.Client.exceptions.CacheSubnetGroupNotFoundFault
ElastiCache.Client.exceptions.CacheSubnetQuotaExceededFault
ElastiCache.Client.exceptions.SubnetInUse
ElastiCache.Client.exceptions.InvalidSubnet

Examples
Modifies an existing ElastiCache subnet group.
response = client.modify_cache_subnet_group(
    CacheSubnetGroupName='my-sn-grp',
    SubnetIds=[
        'subnet-bcde2345',
    ],
)

print(response)


Expected Output:
{
    'CacheSubnetGroup': {
        'CacheSubnetGroupDescription': 'My subnet group.',
        'CacheSubnetGroupName': 'my-sn-grp',
        'Subnets': [
            {
                'SubnetAvailabilityZone': {
                    'Name': 'us-east-1c',
                },
                'SubnetIdentifier': 'subnet-a1b2c3d4',
            },
            {
                'SubnetAvailabilityZone': {
                    'Name': 'us-east-1e',
                },
                'SubnetIdentifier': 'subnet-1a2b3c4d',
            },
            {
                'SubnetAvailabilityZone': {
                    'Name': 'us-east-1e',
                },
                'SubnetIdentifier': 'subnet-bcde2345',
            },
            {
                'SubnetAvailabilityZone': {
                    'Name': 'us-east-1c',
                },
                'SubnetIdentifier': 'subnet-1234abcd',
            },
            {
                'SubnetAvailabilityZone': {
                    'Name': 'us-east-1b',
                },
                'SubnetIdentifier': 'subnet-abcd1234',
            },
        ],
        'VpcId': 'vpc-91280df6',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheSubnetGroup': {
            'CacheSubnetGroupName': 'string',
            'CacheSubnetGroupDescription': 'string',
            'VpcId': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    }
                },
            ],
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    CreateCacheSubnetGroup
    ModifyCacheSubnetGroup
    
    """
    pass

def modify_global_replication_group(GlobalReplicationGroupId=None, ApplyImmediately=None, CacheNodeType=None, EngineVersion=None, GlobalReplicationGroupDescription=None, AutomaticFailoverEnabled=None):
    """
    Modifies the settings for a Global Datastore.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_global_replication_group(
        GlobalReplicationGroupId='string',
        ApplyImmediately=True|False,
        CacheNodeType='string',
        EngineVersion='string',
        GlobalReplicationGroupDescription='string',
        AutomaticFailoverEnabled=True|False
    )
    
    
    :type GlobalReplicationGroupId: string
    :param GlobalReplicationGroupId: [REQUIRED]\nThe name of the Global Datastore\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: [REQUIRED]\nThis parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible. Modifications to Global Replication Groups cannot be requested to be applied in PreferredMaintenceWindow.\n

    :type CacheNodeType: string
    :param CacheNodeType: A valid cache node type that you want to scale this Global Datastore to.

    :type EngineVersion: string
    :param EngineVersion: The upgraded version of the cache engine to be run on the clusters in the Global Datastore.

    :type GlobalReplicationGroupDescription: string
    :param GlobalReplicationGroupDescription: A description of the Global Datastore

    :type AutomaticFailoverEnabled: boolean
    :param AutomaticFailoverEnabled: Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure.

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalReplicationGroup': {
        'GlobalReplicationGroupId': 'string',
        'GlobalReplicationGroupDescription': 'string',
        'Status': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'Members': [
            {
                'ReplicationGroupId': 'string',
                'ReplicationGroupRegion': 'string',
                'Role': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'Status': 'string'
            },
        ],
        'ClusterEnabled': True|False,
        'GlobalNodeGroups': [
            {
                'GlobalNodeGroupId': 'string',
                'Slots': 'string'
            },
        ],
        'AuthTokenEnabled': True|False,
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

GlobalReplicationGroup (dict) --
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different AWS region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.


GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupDescription (string) --
The optional description of the Global Datastore

Status (string) --
The status of the Global Datastore

CacheNodeType (string) --
The cache node type of the Global Datastore

Engine (string) --
The Elasticache engine. For Redis only.

EngineVersion (string) --
The Elasticache Redis engine version. For preview, it is Redis version 5.0.5 only.

Members (list) --
The replication groups that comprise the Global Datastore.

(dict) --
A member of a Global Datastore. It contains the Replication Group Id, the AWS region and the role of the replication group.

ReplicationGroupId (string) --
The replication group id of the Global Datastore member.

ReplicationGroupRegion (string) --
The AWS region of the Global Datastore member.

Role (string) --
Indicates the role of the replication group, primary or secondary.

AutomaticFailover (string) --
Indicates whether automatic failover is enabled for the replication group.

Status (string) --
The status of the membership of the replication group.





ClusterEnabled (boolean) --
A flag that indicates whether the Global Datastore is cluster enabled.

GlobalNodeGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId (string) --
The name of the global node group

Slots (string) --
The keyspace for this node group





AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true. You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.


ARN (string) --
The ARN (Amazon Resource Name) of the global replication group.









Exceptions

ElastiCache.Client.exceptions.GlobalReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException


    :return: {
        'GlobalReplicationGroup': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupDescription': 'string',
            'Status': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'Members': [
                {
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupRegion': 'string',
                    'Role': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'Status': 'string'
                },
            ],
            'ClusterEnabled': True|False,
            'GlobalNodeGroups': [
                {
                    'GlobalNodeGroupId': 'string',
                    'Slots': 'string'
                },
            ],
            'AuthTokenEnabled': True|False,
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.
    
    """
    pass

def modify_replication_group(ReplicationGroupId=None, ReplicationGroupDescription=None, PrimaryClusterId=None, SnapshottingClusterId=None, AutomaticFailoverEnabled=None, NodeGroupId=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, PreferredMaintenanceWindow=None, NotificationTopicArn=None, CacheParameterGroupName=None, NotificationTopicStatus=None, ApplyImmediately=None, EngineVersion=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None, CacheNodeType=None, AuthToken=None, AuthTokenUpdateStrategy=None):
    """
    Modifies the settings for a replication group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.modify_replication_group(
        ReplicationGroupId='string',
        ReplicationGroupDescription='string',
        PrimaryClusterId='string',
        SnapshottingClusterId='string',
        AutomaticFailoverEnabled=True|False,
        NodeGroupId='string',
        CacheSecurityGroupNames=[
            'string',
        ],
        SecurityGroupIds=[
            'string',
        ],
        PreferredMaintenanceWindow='string',
        NotificationTopicArn='string',
        CacheParameterGroupName='string',
        NotificationTopicStatus='string',
        ApplyImmediately=True|False,
        EngineVersion='string',
        AutoMinorVersionUpgrade=True|False,
        SnapshotRetentionLimit=123,
        SnapshotWindow='string',
        CacheNodeType='string',
        AuthToken='string',
        AuthTokenUpdateStrategy='SET'|'ROTATE'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe identifier of the replication group to modify.\n

    :type ReplicationGroupDescription: string
    :param ReplicationGroupDescription: A description for the replication group. Maximum length is 255 characters.

    :type PrimaryClusterId: string
    :param PrimaryClusterId: For replication groups with a single primary, if this parameter is specified, ElastiCache promotes the specified cluster in the specified replication group to the primary role. The nodes of all other clusters in the replication group are read replicas.

    :type SnapshottingClusterId: string
    :param SnapshottingClusterId: The cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Redis (cluster mode enabled) replication groups.

    :type AutomaticFailoverEnabled: boolean
    :param AutomaticFailoverEnabled: Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure.\nValid values: true | false\nAmazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:\n\nRedis versions earlier than 2.8.6.\nRedis (cluster mode disabled): T1 node types.\nRedis (cluster mode enabled): T1 node types.\n\n

    :type NodeGroupId: string
    :param NodeGroupId: Deprecated. This parameter is not used.

    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: A list of cache security group names to authorize for the clusters in this replication group. This change is asynchronously applied as soon as possible.\nThis parameter can be used only with replication group containing clusters running outside of an Amazon Virtual Private Cloud (Amazon VPC).\nConstraints: Must contain no more than 255 alphanumeric characters. Must not be Default .\n\n(string) --\n\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: Specifies the VPC Security Groups associated with the clusters in the replication group.\nThis parameter can be used only with replication group containing clusters running in an Amazon Virtual Private Cloud (Amazon VPC).\n\n(string) --\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.\nValid values for ddd are:\n\nsun\nmon\ntue\nwed\nthu\nfri\nsat\n\nExample: sun:23:00-mon:01:30\n

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.\n\nNote\nThe Amazon SNS topic owner must be same as the replication group owner.\n\n

    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of the cache parameter group to apply to all of the clusters in this replication group. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for this request.

    :type NotificationTopicStatus: string
    :param NotificationTopicStatus: The status of the Amazon SNS notification topic for the replication group. Notifications are sent only if the status is active .\nValid values: active | inactive\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: If true , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow setting for the replication group.\nIf false , changes to the nodes in the replication group are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.\nValid values: true | false\nDefault: false\n

    :type EngineVersion: string
    :param EngineVersion: The upgraded version of the cache engine to be run on the clusters in the replication group.\n\nImportant: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing replication group and create it anew with the earlier engine version.\n

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.

    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic node group (shard) snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.\n\nImportant If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.\n

    :type SnapshotWindow: string
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node group (shard) specified by SnapshottingClusterId .\nExample: 05:00-09:00\nIf you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.\n

    :type CacheNodeType: string
    :param CacheNodeType: A valid cache node type that you want to scale this replication group to.

    :type AuthToken: string
    :param AuthToken: Reserved parameter. The password used to access a password protected server. This parameter must be specified with the auth-token-update-strategy parameter. Password constraints:\n\nMust be only printable ASCII characters\nMust be at least 16 characters and no more than 128 characters in length\nCannot contain any of the following characters: \'/\', \''\', or \'@\', \'%\'\n\nFor more information, see AUTH password at AUTH .\n

    :type AuthTokenUpdateStrategy: string
    :param AuthTokenUpdateStrategy: Specifies the strategy to use to update the AUTH token. This parameter must be specified with the auth-token parameter. Possible values:\n\nRotate\nSet\n\nFor more information, see Authenticating Users with Redis AUTH\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationGroup': {
        'ReplicationGroupId': 'string',
        'Description': 'string',
        'GlobalReplicationGroupInfo': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupMemberRole': 'string'
        },
        'Status': 'string',
        'PendingModifiedValues': {
            'PrimaryClusterId': 'string',
            'AutomaticFailoverStatus': 'enabled'|'disabled',
            'Resharding': {
                'SlotMigration': {
                    'ProgressPercentage': 123.0
                }
            },
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'MemberClusters': [
            'string',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': 'string',
                'Status': 'string',
                'PrimaryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ReaderEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'Slots': 'string',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'string',
                        'CacheNodeId': 'string',
                        'ReadEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'PreferredAvailabilityZone': 'string',
                        'CurrentRole': 'string'
                    },
                ]
            },
        ],
        'SnapshottingClusterId': 'string',
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'ClusterEnabled': True|False,
        'CacheNodeType': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

ReplicationGroup (dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.









Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.InvalidCacheSecurityGroupStateFault
ElastiCache.Client.exceptions.InsufficientCacheClusterCapacityFault
ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.NodeQuotaForClusterExceededFault
ElastiCache.Client.exceptions.NodeQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.CacheSecurityGroupNotFoundFault
ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidVPCNetworkStateFault
ElastiCache.Client.exceptions.InvalidKMSKeyFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
response = client.modify_replication_group(
    ApplyImmediately=True,
    ReplicationGroupDescription='Modified replication group',
    ReplicationGroupId='my-redis-rg',
    SnapshotRetentionLimit=30,
    SnapshottingClusterId='my-redis-rg-001',
)

print(response)


Expected Output:
{
    'ReplicationGroup': {
        'AutomaticFailover': 'enabled',
        'Description': 'Modified replication group',
        'MemberClusters': [
            'my-redis-rg-001',
            'my-redis-rg-002',
            'my-redis-rg-003',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': '0001',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'my-redis-rg-001',
                        'CacheNodeId': '0001',
                        'CurrentRole': 'primary',
                        'PreferredAvailabilityZone': 'us-east-1b',
                        'ReadEndpoint': {
                            'Address': 'my-redis-rg-001.abcdef.0001.use1.cache.amazonaws.com',
                            'Port': 6379,
                        },
                    },
                    {
                        'CacheClusterId': 'my-redis-rg-002',
                        'CacheNodeId': '0001',
                        'CurrentRole': 'replica',
                        'PreferredAvailabilityZone': 'us-east-1a',
                        'ReadEndpoint': {
                            'Address': 'my-redis-rg-002.abcdef.0001.use1.cache.amazonaws.com',
                            'Port': 6379,
                        },
                    },
                    {
                        'CacheClusterId': 'my-redis-rg-003',
                        'CacheNodeId': '0001',
                        'CurrentRole': 'replica',
                        'PreferredAvailabilityZone': 'us-east-1c',
                        'ReadEndpoint': {
                            'Address': 'my-redis-rg-003.abcdef.0001.use1.cache.amazonaws.com',
                            'Port': 6379,
                        },
                    },
                ],
                'PrimaryEndpoint': {
                    'Address': 'my-redis-rg.abcdef.ng.0001.use1.cache.amazonaws.com',
                    'Port': 6379,
                },
                'Status': 'available',
            },
        ],
        'PendingModifiedValues': {
        },
        'ReplicationGroupId': 'my-redis-rg',
        'SnapshottingClusterId': 'my-redis-rg-002',
        'Status': 'available',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    ReplicationGroupId (string) -- [REQUIRED]
    The identifier of the replication group to modify.
    
    ReplicationGroupDescription (string) -- A description for the replication group. Maximum length is 255 characters.
    PrimaryClusterId (string) -- For replication groups with a single primary, if this parameter is specified, ElastiCache promotes the specified cluster in the specified replication group to the primary role. The nodes of all other clusters in the replication group are read replicas.
    SnapshottingClusterId (string) -- The cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Redis (cluster mode enabled) replication groups.
    AutomaticFailoverEnabled (boolean) -- Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure.
    Valid values: true | false
    Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:
    
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled): T1 node types.
    Redis (cluster mode enabled): T1 node types.
    
    
    NodeGroupId (string) -- Deprecated. This parameter is not used.
    CacheSecurityGroupNames (list) -- A list of cache security group names to authorize for the clusters in this replication group. This change is asynchronously applied as soon as possible.
    This parameter can be used only with replication group containing clusters running outside of an Amazon Virtual Private Cloud (Amazon VPC).
    Constraints: Must contain no more than 255 alphanumeric characters. Must not be Default .
    
    (string) --
    
    
    SecurityGroupIds (list) -- Specifies the VPC Security Groups associated with the clusters in the replication group.
    This parameter can be used only with replication group containing clusters running in an Amazon Virtual Private Cloud (Amazon VPC).
    
    (string) --
    
    
    PreferredMaintenanceWindow (string) -- Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
    Valid values for ddd are:
    
    sun
    mon
    tue
    wed
    thu
    fri
    sat
    
    Example: sun:23:00-mon:01:30
    
    NotificationTopicArn (string) -- The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.
    
    Note
    The Amazon SNS topic owner must be same as the replication group owner.
    
    
    CacheParameterGroupName (string) -- The name of the cache parameter group to apply to all of the clusters in this replication group. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for this request.
    NotificationTopicStatus (string) -- The status of the Amazon SNS notification topic for the replication group. Notifications are sent only if the status is active .
    Valid values: active | inactive
    
    ApplyImmediately (boolean) -- If true , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow setting for the replication group.
    If false , changes to the nodes in the replication group are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.
    Valid values: true | false
    Default: false
    
    EngineVersion (string) -- The upgraded version of the cache engine to be run on the clusters in the replication group.
    
    Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing replication group and create it anew with the earlier engine version.
    
    AutoMinorVersionUpgrade (boolean) -- This parameter is currently disabled.
    SnapshotRetentionLimit (integer) -- The number of days for which ElastiCache retains automatic node group (shard) snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
    
    Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
    
    SnapshotWindow (string) -- The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node group (shard) specified by SnapshottingClusterId .
    Example: 05:00-09:00
    If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
    
    CacheNodeType (string) -- A valid cache node type that you want to scale this replication group to.
    AuthToken (string) -- Reserved parameter. The password used to access a password protected server. This parameter must be specified with the auth-token-update-strategy parameter. Password constraints:
    
    Must be only printable ASCII characters
    Must be at least 16 characters and no more than 128 characters in length
    Cannot contain any of the following characters: \'/\', \'"\', or \'@\', \'%\'
    
    For more information, see AUTH password at AUTH .
    
    AuthTokenUpdateStrategy (string) -- Specifies the strategy to use to update the AUTH token. This parameter must be specified with the auth-token parameter. Possible values:
    
    Rotate
    Set
    
    For more information, see Authenticating Users with Redis AUTH
    
    
    """
    pass

def modify_replication_group_shard_configuration(ReplicationGroupId=None, NodeGroupCount=None, ApplyImmediately=None, ReshardingConfiguration=None, NodeGroupsToRemove=None, NodeGroupsToRetain=None):
    """
    Modifies a replication group\'s shards (node groups) by allowing you to add shards, remove shards, or rebalance the keyspaces among exisiting shards.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_replication_group_shard_configuration(
        ReplicationGroupId='string',
        NodeGroupCount=123,
        ApplyImmediately=True|False,
        ReshardingConfiguration=[
            {
                'NodeGroupId': 'string',
                'PreferredAvailabilityZones': [
                    'string',
                ]
            },
        ],
        NodeGroupsToRemove=[
            'string',
        ],
        NodeGroupsToRetain=[
            'string',
        ]
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe name of the Redis (cluster mode enabled) cluster (replication group) on which the shards are to be configured.\n

    :type NodeGroupCount: integer
    :param NodeGroupCount: [REQUIRED]\nThe number of node groups (shards) that results from the modification of the shard configuration.\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: [REQUIRED]\nIndicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is true .\nValue: true\n

    :type ReshardingConfiguration: list
    :param ReshardingConfiguration: Specifies the preferred availability zones for each node group in the cluster. If the value of NodeGroupCount is greater than the current number of node groups (shards), you can use this parameter to specify the preferred availability zones of the cluster\'s shards. If you omit this parameter ElastiCache selects availability zones for you.\nYou can specify this parameter only if the value of NodeGroupCount is greater than the current number of node groups (shards).\n\n(dict) --A list of PreferredAvailabilityZones objects that specifies the configuration of a node group in the resharded cluster.\n\nNodeGroupId (string) --Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group these configuration values apply to.\n\nPreferredAvailabilityZones (list) --A list of preferred availability zones for the nodes in this cluster.\n\n(string) --\n\n\n\n\n\n

    :type NodeGroupsToRemove: list
    :param NodeGroupsToRemove: If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. NodeGroupsToRemove is a list of NodeGroupId s to remove from the cluster.\nElastiCache for Redis will attempt to remove all node groups listed by NodeGroupsToRemove from the cluster.\n\n(string) --\n\n

    :type NodeGroupsToRetain: list
    :param NodeGroupsToRetain: If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. NodeGroupsToRetain is a list of NodeGroupId s to retain in the cluster.\nElastiCache for Redis will attempt to remove all node groups except those listed by NodeGroupsToRetain from the cluster.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationGroup': {
        'ReplicationGroupId': 'string',
        'Description': 'string',
        'GlobalReplicationGroupInfo': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupMemberRole': 'string'
        },
        'Status': 'string',
        'PendingModifiedValues': {
            'PrimaryClusterId': 'string',
            'AutomaticFailoverStatus': 'enabled'|'disabled',
            'Resharding': {
                'SlotMigration': {
                    'ProgressPercentage': 123.0
                }
            },
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'MemberClusters': [
            'string',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': 'string',
                'Status': 'string',
                'PrimaryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ReaderEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'Slots': 'string',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'string',
                        'CacheNodeId': 'string',
                        'ReadEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'PreferredAvailabilityZone': 'string',
                        'CurrentRole': 'string'
                    },
                ]
            },
        ],
        'SnapshottingClusterId': 'string',
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'ClusterEnabled': True|False,
        'CacheNodeType': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

ReplicationGroup (dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.









Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.InvalidVPCNetworkStateFault
ElastiCache.Client.exceptions.InsufficientCacheClusterCapacityFault
ElastiCache.Client.exceptions.NodeGroupsPerReplicationGroupQuotaExceededFault
ElastiCache.Client.exceptions.NodeQuotaForCustomerExceededFault
ElastiCache.Client.exceptions.InvalidKMSKeyFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled): T1 node types.
    Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def purchase_reserved_cache_nodes_offering(ReservedCacheNodesOfferingId=None, ReservedCacheNodeId=None, CacheNodeCount=None):
    """
    Allows you to purchase a reserved cache node offering.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Allows you to purchase a reserved cache node offering.
    Expected Output:
    
    :example: response = client.purchase_reserved_cache_nodes_offering(
        ReservedCacheNodesOfferingId='string',
        ReservedCacheNodeId='string',
        CacheNodeCount=123
    )
    
    
    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodesOfferingId: [REQUIRED]\nThe ID of the reserved cache node offering to purchase.\nExample: 438012d3-4052-4cc7-b2e3-8d3372e0e706\n

    :type ReservedCacheNodeId: string
    :param ReservedCacheNodeId: A customer-specified identifier to track this reservation.\n\nNote\nThe Reserved Cache Node ID is an unique customer-specified identifier to track this reservation. If this parameter is not specified, ElastiCache automatically generates an identifier for the reservation.\n\nExample: myreservationID\n

    :type CacheNodeCount: integer
    :param CacheNodeCount: The number of cache node instances to reserve.\nDefault: 1\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReservedCacheNode': {
        'ReservedCacheNodeId': 'string',
        'ReservedCacheNodesOfferingId': 'string',
        'CacheNodeType': 'string',
        'StartTime': datetime(2015, 1, 1),
        'Duration': 123,
        'FixedPrice': 123.0,
        'UsagePrice': 123.0,
        'CacheNodeCount': 123,
        'ProductDescription': 'string',
        'OfferingType': 'string',
        'State': 'string',
        'RecurringCharges': [
            {
                'RecurringChargeAmount': 123.0,
                'RecurringChargeFrequency': 'string'
            },
        ],
        'ReservationARN': 'string'
    }
}


Response Structure

(dict) --

ReservedCacheNode (dict) --
Represents the output of a PurchaseReservedCacheNodesOffering operation.

ReservedCacheNodeId (string) --
The unique identifier for the reservation.

ReservedCacheNodesOfferingId (string) --
The offering identifier.

CacheNodeType (string) --
The cache node type for the reserved cache nodes.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


StartTime (datetime) --
The time the reservation started.

Duration (integer) --
The duration of the reservation in seconds.

FixedPrice (float) --
The fixed price charged for this reserved cache node.

UsagePrice (float) --
The hourly price charged for this reserved cache node.

CacheNodeCount (integer) --
The number of cache nodes that have been reserved.

ProductDescription (string) --
The description of the reserved cache node.

OfferingType (string) --
The offering type of this reserved cache node.

State (string) --
The state of the reserved cache node.

RecurringCharges (list) --
The recurring price charged to run this reserved cache node.

(dict) --
Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

RecurringChargeAmount (float) --
The monetary amount of the recurring charge.

RecurringChargeFrequency (string) --
The frequency of the recurring charge.





ReservationARN (string) --
The Amazon Resource Name (ARN) of the reserved cache node.
Example: arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582









Exceptions

ElastiCache.Client.exceptions.ReservedCacheNodesOfferingNotFoundFault
ElastiCache.Client.exceptions.ReservedCacheNodeAlreadyExistsFault
ElastiCache.Client.exceptions.ReservedCacheNodeQuotaExceededFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Allows you to purchase a reserved cache node offering.
response = client.purchase_reserved_cache_nodes_offering(
    ReservedCacheNodesOfferingId='1ef01f5b-94ff-433f-a530-61a56bfc8e7a',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ReservedCacheNode': {
            'ReservedCacheNodeId': 'string',
            'ReservedCacheNodesOfferingId': 'string',
            'CacheNodeType': 'string',
            'StartTime': datetime(2015, 1, 1),
            'Duration': 123,
            'FixedPrice': 123.0,
            'UsagePrice': 123.0,
            'CacheNodeCount': 123,
            'ProductDescription': 'string',
            'OfferingType': 'string',
            'State': 'string',
            'RecurringCharges': [
                {
                    'RecurringChargeAmount': 123.0,
                    'RecurringChargeFrequency': 'string'
                },
            ],
            'ReservationARN': 'string'
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
    Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
    
    
    Compute optimized:
    Previous generation: (not recommended)  C1 node types: cache.c1.xlarge
    
    
    Memory optimized:
    Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
    Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    
    
    
    """
    pass

def rebalance_slots_in_global_replication_group(GlobalReplicationGroupId=None, ApplyImmediately=None):
    """
    Redistribute slots to ensure uniform distribution across existing shards in the cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.rebalance_slots_in_global_replication_group(
        GlobalReplicationGroupId='string',
        ApplyImmediately=True|False
    )
    
    
    :type GlobalReplicationGroupId: string
    :param GlobalReplicationGroupId: [REQUIRED]\nThe name of the Global Datastore\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: [REQUIRED]\nIf True , redistribution is applied immediately.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GlobalReplicationGroup': {
        'GlobalReplicationGroupId': 'string',
        'GlobalReplicationGroupDescription': 'string',
        'Status': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'Members': [
            {
                'ReplicationGroupId': 'string',
                'ReplicationGroupRegion': 'string',
                'Role': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'Status': 'string'
            },
        ],
        'ClusterEnabled': True|False,
        'GlobalNodeGroups': [
            {
                'GlobalNodeGroupId': 'string',
                'Slots': 'string'
            },
        ],
        'AuthTokenEnabled': True|False,
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

GlobalReplicationGroup (dict) --
Consists of a primary cluster that accepts writes and an associated secondary cluster that resides in a different AWS region. The secondary cluster accepts only reads. The primary cluster automatically replicates updates to the secondary cluster.

The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.


GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupDescription (string) --
The optional description of the Global Datastore

Status (string) --
The status of the Global Datastore

CacheNodeType (string) --
The cache node type of the Global Datastore

Engine (string) --
The Elasticache engine. For Redis only.

EngineVersion (string) --
The Elasticache Redis engine version. For preview, it is Redis version 5.0.5 only.

Members (list) --
The replication groups that comprise the Global Datastore.

(dict) --
A member of a Global Datastore. It contains the Replication Group Id, the AWS region and the role of the replication group.

ReplicationGroupId (string) --
The replication group id of the Global Datastore member.

ReplicationGroupRegion (string) --
The AWS region of the Global Datastore member.

Role (string) --
Indicates the role of the replication group, primary or secondary.

AutomaticFailover (string) --
Indicates whether automatic failover is enabled for the replication group.

Status (string) --
The status of the membership of the replication group.





ClusterEnabled (boolean) --
A flag that indicates whether the Global Datastore is cluster enabled.

GlobalNodeGroups (list) --
Indicates the slot configuration and global identifier for each slice group.

(dict) --
Indicates the slot configuration and global identifier for a slice group.

GlobalNodeGroupId (string) --
The name of the global node group

Slots (string) --
The keyspace for this node group





AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true. You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication group you must set AtRestEncryptionEnabled to true when you create the replication group.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.


ARN (string) --
The ARN (Amazon Resource Name) of the global replication group.









Exceptions

ElastiCache.Client.exceptions.GlobalReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException


    :return: {
        'GlobalReplicationGroup': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupDescription': 'string',
            'Status': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'Members': [
                {
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupRegion': 'string',
                    'Role': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'Status': 'string'
                },
            ],
            'ClusterEnabled': True|False,
            'GlobalNodeGroups': [
                {
                    'GlobalNodeGroupId': 'string',
                    'Slots': 'string'
                },
            ],
            'AuthTokenEnabled': True|False,
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    The GlobalReplicationGroupIdSuffix represents the name of the Global Datastore, which is what you use to associate a secondary cluster.
    
    """
    pass

def reboot_cache_cluster(CacheClusterId=None, CacheNodeIdsToReboot=None):
    """
    Reboots some, or all, of the cache nodes within a provisioned cluster. This operation applies any modified cache parameter groups to the cluster. The reboot operation takes place as soon as possible, and results in a momentary outage to the cluster. During the reboot, the cluster status is set to REBOOTING.
    The reboot causes the contents of the cache (for each cache node being rebooted) to be lost.
    When the reboot is complete, a cluster event is created.
    Rebooting a cluster is currently supported on Memcached and Redis (cluster mode disabled) clusters. Rebooting is not supported on Redis (cluster mode enabled) clusters.
    If you make changes to parameters that require a Redis (cluster mode enabled) cluster reboot for the changes to be applied, see Rebooting a Cluster for an alternate process.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Reboots the specified nodes in the names cluster.
    Expected Output:
    
    :example: response = client.reboot_cache_cluster(
        CacheClusterId='string',
        CacheNodeIdsToReboot=[
            'string',
        ]
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: [REQUIRED]\nThe cluster identifier. This parameter is stored as a lowercase string.\n

    :type CacheNodeIdsToReboot: list
    :param CacheNodeIdsToReboot: [REQUIRED]\nA list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cluster, specify all of the cache node IDs.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheCluster': {
        'CacheClusterId': 'string',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClientDownloadLandingPage': 'string',
        'CacheNodeType': 'string',
        'Engine': 'string',
        'EngineVersion': 'string',
        'CacheClusterStatus': 'string',
        'NumCacheNodes': 123,
        'PreferredAvailabilityZone': 'string',
        'CacheClusterCreateTime': datetime(2015, 1, 1),
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'NumCacheNodes': 123,
            'CacheNodeIdsToRemove': [
                'string',
            ],
            'EngineVersion': 'string',
            'CacheNodeType': 'string',
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'NotificationConfiguration': {
            'TopicArn': 'string',
            'TopicStatus': 'string'
        },
        'CacheSecurityGroups': [
            {
                'CacheSecurityGroupName': 'string',
                'Status': 'string'
            },
        ],
        'CacheParameterGroup': {
            'CacheParameterGroupName': 'string',
            'ParameterApplyStatus': 'string',
            'CacheNodeIdsToReboot': [
                'string',
            ]
        },
        'CacheSubnetGroupName': 'string',
        'CacheNodes': [
            {
                'CacheNodeId': 'string',
                'CacheNodeStatus': 'string',
                'CacheNodeCreateTime': datetime(2015, 1, 1),
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ParameterGroupStatus': 'string',
                'SourceCacheNodeId': 'string',
                'CustomerAvailabilityZone': 'string'
            },
        ],
        'AutoMinorVersionUpgrade': True|False,
        'SecurityGroups': [
            {
                'SecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'ReplicationGroupId': 'string',
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheCluster (dict) --
Contains all of the attributes of a specific cluster.

CacheClusterId (string) --
The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

ConfigurationEndpoint (dict) --
Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have .cfg in it.
Example: mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ClientDownloadLandingPage (string) --
The URL of the web page where you can download the latest ElastiCache client library.

CacheNodeType (string) --
The name of the compute and memory capacity node type for the cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


Engine (string) --
The name of the cache engine (memcached or redis ) to be used for this cluster.

EngineVersion (string) --
The version of the cache engine that is used in this cluster.

CacheClusterStatus (string) --
The current state of this cluster, one of the following values: available , creating , deleted , deleting , incompatible-network , modifying , rebooting cluster nodes , restore-failed , or snapshotting .

NumCacheNodes (integer) --
The number of cache nodes in the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

CacheClusterCreateTime (datetime) --
The date and time when the cluster was created.

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for ddd are:

sun
mon
tue
wed
thu
fri
sat

Example: sun:23:00-mon:01:30

PendingModifiedValues (dict) --
A group of settings that are applied to the cluster in the future, or that are currently being applied.

NumCacheNodes (integer) --
The new number of cache nodes for the cluster.
For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

CacheNodeIdsToRemove (list) --
A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

(string) --


EngineVersion (string) --
The new cache engine version that the cluster runs.

CacheNodeType (string) --
The cache node type that this cluster or replication group is scaled to.

AuthTokenStatus (string) --
The auth token status



NotificationConfiguration (dict) --
Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn (string) --
The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus (string) --
The current state of the topic.



CacheSecurityGroups (list) --
A list of cache security group elements, composed of name and status sub-elements.

(dict) --
Represents a cluster\'s status within a particular cache security group.

CacheSecurityGroupName (string) --
The name of the cache security group.

Status (string) --
The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





CacheParameterGroup (dict) --
Status of the cache parameter group.

CacheParameterGroupName (string) --
The name of the cache parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

CacheNodeIdsToReboot (list) --
A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

(string) --




CacheSubnetGroupName (string) --
The name of the cache subnet group associated with the cluster.

CacheNodes (list) --
A list of cache nodes that are members of the cluster.

(dict) --
Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster\'s protocol-compliant caching software - either Memcached or Redis.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

General purpose:
Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge


Compute optimized:
Previous generation: (not recommended)  C1 node types: cache.c1.xlarge


Memory optimized:
Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge




Additional node type info


All current generation instance types are created in Amazon VPC by default.
Redis append-only files (AOF) are not supported for T1 or T2 instances.
Redis Multi-AZ with automatic failover is not supported on T1 instances.
Redis configuration variables appendonly and appendfsync are not supported on Redis version 2.8.22 and later.


CacheNodeId (string) --
The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer\'s AWS account.

CacheNodeStatus (string) --
The current state of this cache node, one of the following values: available , creating , rebooting , or deleting .

CacheNodeCreateTime (datetime) --
The date and time when the cache node was created.

Endpoint (dict) --
The hostname for connecting to this cache node.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ParameterGroupStatus (string) --
The status of the parameter group applied to this cache node.

SourceCacheNodeId (string) --
The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

CustomerAvailabilityZone (string) --
The Availability Zone where this node was created and now resides.





AutoMinorVersionUpgrade (boolean) --
This parameter is currently disabled.

SecurityGroups (list) --
A list of VPC Security Groups associated with the cluster.

(dict) --
Represents a single cache security group and its status.

SecurityGroupId (string) --
The identifier of the cache security group.

Status (string) --
The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.





ReplicationGroupId (string) --
The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.
Example: 05:00-09:00

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable at-rest encryption on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

ARN (string) --
The ARN (Amazon Resource Name) of the cache cluster.









Exceptions

ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.CacheClusterNotFoundFault

Examples
Reboots the specified nodes in the names cluster.
response = client.reboot_cache_cluster(
    CacheClusterId='custom-mem1-4  ',
    CacheNodeIdsToReboot=[
        '0001',
        '0002',
    ],
)

print(response)


Expected Output:
{
    'CacheCluster': {
        'AutoMinorVersionUpgrade': True,
        'CacheClusterCreateTime': datetime(2016, 12, 21, 21, 59, 43, 2, 356, 0),
        'CacheClusterId': 'my-mem-cluster',
        'CacheClusterStatus': 'rebooting cache cluster nodes',
        'CacheNodeType': 'cache.t2.medium',
        'CacheParameterGroup': {
            'CacheNodeIdsToReboot': [
            ],
            'CacheParameterGroupName': 'default.memcached1.4',
            'ParameterApplyStatus': 'in-sync',
        },
        'CacheSecurityGroups': [
        ],
        'CacheSubnetGroupName': 'default',
        'ClientDownloadLandingPage': 'https://console.aws.amazon.com/elasticache/home#client-download:',
        'ConfigurationEndpoint': {
            'Address': 'my-mem-cluster.abcdef.cfg.use1.cache.amazonaws.com',
            'Port': 11211,
        },
        'Engine': 'memcached',
        'EngineVersion': '1.4.24',
        'NumCacheNodes': 2,
        'PendingModifiedValues': {
        },
        'PreferredAvailabilityZone': 'Multiple',
        'PreferredMaintenanceWindow': 'wed:06:00-wed:07:00',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheCluster': {
            'CacheClusterId': 'string',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClientDownloadLandingPage': 'string',
            'CacheNodeType': 'string',
            'Engine': 'string',
            'EngineVersion': 'string',
            'CacheClusterStatus': 'string',
            'NumCacheNodes': 123,
            'PreferredAvailabilityZone': 'string',
            'CacheClusterCreateTime': datetime(2015, 1, 1),
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'NumCacheNodes': 123,
                'CacheNodeIdsToRemove': [
                    'string',
                ],
                'EngineVersion': 'string',
                'CacheNodeType': 'string',
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'NotificationConfiguration': {
                'TopicArn': 'string',
                'TopicStatus': 'string'
            },
            'CacheSecurityGroups': [
                {
                    'CacheSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CacheParameterGroup': {
                'CacheParameterGroupName': 'string',
                'ParameterApplyStatus': 'string',
                'CacheNodeIdsToReboot': [
                    'string',
                ]
            },
            'CacheSubnetGroupName': 'string',
            'CacheNodes': [
                {
                    'CacheNodeId': 'string',
                    'CacheNodeStatus': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'Endpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ParameterGroupStatus': 'string',
                    'SourceCacheNodeId': 'string',
                    'CustomerAvailabilityZone': 'string'
                },
            ],
            'AutoMinorVersionUpgrade': True|False,
            'SecurityGroups': [
                {
                    'SecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'ReplicationGroupId': 'string',
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation:   M5 node types: cache.m5.large , cache.m5.xlarge , cache.m5.2xlarge , cache.m5.4xlarge , cache.m5.12xlarge , cache.m5.24xlarge M4 node types: cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge T3 node types: cache.t3.micro , cache.t3.small , cache.t3.medium T2 node types: cache.t2.micro , cache.t2.small , cache.t2.medium
    Previous generation: (not recommended)  T1 node types: cache.t1.micro M1 node types: cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge M3 node types: cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
    
    
    Compute optimized:
    Previous generation: (not recommended)  C1 node types: cache.c1.xlarge
    
    
    Memory optimized:
    Current generation:   R5 node types: cache.r5.large , cache.r5.xlarge , cache.r5.2xlarge , cache.r5.4xlarge , cache.r5.12xlarge , cache.r5.24xlarge R4 node types: cache.r4.large , cache.r4.xlarge , cache.r4.2xlarge , cache.r4.4xlarge , cache.r4.8xlarge , cache.r4.16xlarge
    Previous generation: (not recommended)  M2 node types: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge R3 node types: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    
    
    
    """
    pass

def remove_tags_from_resource(ResourceName=None, TagKeys=None):
    """
    Removes the tags identified by the TagKeys list from the named resource.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Removes tags identified by a list of tag keys from the list of tags on the specified resource.
    Expected Output:
    
    :example: response = client.remove_tags_from_resource(
        ResourceName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .\nFor more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of TagKeys identifying the tags you want removed from the named resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TagList': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output from the AddTagsToResource , ListTagsForResource , and RemoveTagsFromResource operations.

TagList (list) --
A list of cost allocation tags as key-value pairs.

(dict) --
A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

Key (string) --
The key for the tag. May not be null.

Value (string) --
The tag\'s value. May be null.











Exceptions

ElastiCache.Client.exceptions.CacheClusterNotFoundFault
ElastiCache.Client.exceptions.SnapshotNotFoundFault
ElastiCache.Client.exceptions.InvalidARNFault
ElastiCache.Client.exceptions.TagNotFoundFault

Examples
Removes tags identified by a list of tag keys from the list of tags on the specified resource.
response = client.remove_tags_from_resource(
    ResourceName='arn:aws:elasticache:us-east-1:1234567890:cluster:my-mem-cluster',
    TagKeys=[
        'A',
        'C',
        'E',
    ],
)

print(response)


Expected Output:
{
    'TagList': [
        {
            'Key': 'B',
            'Value': 'Banana',
        },
        {
            'Key': 'D',
            'Value': 'Dog',
        },
        {
            'Key': 'F',
            'Value': 'Fox',
        },
        {
            'Key': 'I',
            'Value': '',
        },
        {
            'Key': 'K',
            'Value': 'Kite',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    ElastiCache.Client.exceptions.CacheClusterNotFoundFault
    ElastiCache.Client.exceptions.SnapshotNotFoundFault
    ElastiCache.Client.exceptions.InvalidARNFault
    ElastiCache.Client.exceptions.TagNotFoundFault
    
    """
    pass

def reset_cache_parameter_group(CacheParameterGroupName=None, ResetAllParameters=None, ParameterNameValues=None):
    """
    Modifies the parameters of a cache parameter group to the engine or system default value. You can reset specific parameters by submitting a list of parameter names. To reset the entire cache parameter group, specify the ResetAllParameters and CacheParameterGroupName parameters.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Modifies the parameters of a cache parameter group to the engine or system default value.
    Expected Output:
    
    :example: response = client.reset_cache_parameter_group(
        CacheParameterGroupName='string',
        ResetAllParameters=True|False,
        ParameterNameValues=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string'
            },
        ]
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: [REQUIRED]\nThe name of the cache parameter group to reset.\n

    :type ResetAllParameters: boolean
    :param ResetAllParameters: If true , all parameters in the cache parameter group are reset to their default values. If false , only the parameters listed by ParameterNameValues are reset to their default values.\nValid values: true | false\n

    :type ParameterNameValues: list
    :param ParameterNameValues: An array of parameter names to reset to their default values. If ResetAllParameters is true , do not use ParameterNameValues . If ResetAllParameters is false , you must specify the name of at least one parameter to reset.\n\n(dict) --Describes a name-value pair that is used to update the value of a parameter.\n\nParameterName (string) --The name of the parameter.\n\nParameterValue (string) --The value of the parameter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheParameterGroupName': 'string'
}


Response Structure

(dict) --
Represents the output of one of the following operations:

ModifyCacheParameterGroup
ResetCacheParameterGroup


CacheParameterGroupName (string) --
The name of the cache parameter group.







Exceptions

ElastiCache.Client.exceptions.InvalidCacheParameterGroupStateFault
ElastiCache.Client.exceptions.CacheParameterGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException
ElastiCache.Client.exceptions.InvalidGlobalReplicationGroupStateFault

Examples
Modifies the parameters of a cache parameter group to the engine or system default value.
response = client.reset_cache_parameter_group(
    CacheParameterGroupName='custom-mem1-4',
    ResetAllParameters=True,
)

print(response)


Expected Output:
{
    'CacheParameterGroupName': 'custom-mem1-4',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheParameterGroupName': 'string'
    }
    
    
    :returns: 
    ModifyCacheParameterGroup
    ResetCacheParameterGroup
    
    """
    pass

def revoke_cache_security_group_ingress(CacheSecurityGroupName=None, EC2SecurityGroupName=None, EC2SecurityGroupOwnerId=None):
    """
    Revokes ingress from a cache security group. Use this operation to disallow access from an Amazon EC2 security group that had been previously authorized.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group.
    Expected Output:
    
    :example: response = client.revoke_cache_security_group_ingress(
        CacheSecurityGroupName='string',
        EC2SecurityGroupName='string',
        EC2SecurityGroupOwnerId='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: [REQUIRED]\nThe name of the cache security group to revoke ingress from.\n

    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: [REQUIRED]\nThe name of the Amazon EC2 security group to revoke access from.\n

    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: [REQUIRED]\nThe AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CacheSecurityGroup': {
        'OwnerId': 'string',
        'CacheSecurityGroupName': 'string',
        'Description': 'string',
        'EC2SecurityGroups': [
            {
                'Status': 'string',
                'EC2SecurityGroupName': 'string',
                'EC2SecurityGroupOwnerId': 'string'
            },
        ],
        'ARN': 'string'
    }
}


Response Structure

(dict) --

CacheSecurityGroup (dict) --
Represents the output of one of the following operations:

AuthorizeCacheSecurityGroupIngress
CreateCacheSecurityGroup
RevokeCacheSecurityGroupIngress


OwnerId (string) --
The AWS account ID of the cache security group owner.

CacheSecurityGroupName (string) --
The name of the cache security group.

Description (string) --
The description of the cache security group.

EC2SecurityGroups (list) --
A list of Amazon EC2 security groups that are associated with this cache security group.

(dict) --
Provides ownership and status information for an Amazon EC2 security group.

Status (string) --
The status of the Amazon EC2 security group.

EC2SecurityGroupName (string) --
The name of the Amazon EC2 security group.

EC2SecurityGroupOwnerId (string) --
The AWS account ID of the Amazon EC2 security group owner.





ARN (string) --
The ARN (Amazon Resource Name) of the cache security group.









Exceptions

ElastiCache.Client.exceptions.CacheSecurityGroupNotFoundFault
ElastiCache.Client.exceptions.AuthorizationNotFoundFault
ElastiCache.Client.exceptions.InvalidCacheSecurityGroupStateFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException

Examples
Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group.
response = client.revoke_cache_security_group_ingress(
    CacheSecurityGroupName='my-sec-grp',
    EC2SecurityGroupName='my-ec2-sec-grp',
    EC2SecurityGroupOwnerId='1234567890',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CacheSecurityGroup': {
            'OwnerId': 'string',
            'CacheSecurityGroupName': 'string',
            'Description': 'string',
            'EC2SecurityGroups': [
                {
                    'Status': 'string',
                    'EC2SecurityGroupName': 'string',
                    'EC2SecurityGroupOwnerId': 'string'
                },
            ],
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    AuthorizeCacheSecurityGroupIngress
    CreateCacheSecurityGroup
    RevokeCacheSecurityGroupIngress
    
    """
    pass

def start_migration(ReplicationGroupId=None, CustomerNodeEndpointList=None):
    """
    Start the migration of data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_migration(
        ReplicationGroupId='string',
        CustomerNodeEndpointList=[
            {
                'Address': 'string',
                'Port': 123
            },
        ]
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe ID of the replication group to which data should be migrated.\n

    :type CustomerNodeEndpointList: list
    :param CustomerNodeEndpointList: [REQUIRED]\nList of endpoints from which data should be migrated. For Redis (cluster mode disabled), list should have only one element.\n\n(dict) --The endpoint from which data should be migrated.\n\nAddress (string) --The address of the node endpoint\n\nPort (integer) --The port of the node endpoint\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationGroup': {
        'ReplicationGroupId': 'string',
        'Description': 'string',
        'GlobalReplicationGroupInfo': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupMemberRole': 'string'
        },
        'Status': 'string',
        'PendingModifiedValues': {
            'PrimaryClusterId': 'string',
            'AutomaticFailoverStatus': 'enabled'|'disabled',
            'Resharding': {
                'SlotMigration': {
                    'ProgressPercentage': 123.0
                }
            },
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'MemberClusters': [
            'string',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': 'string',
                'Status': 'string',
                'PrimaryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ReaderEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'Slots': 'string',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'string',
                        'CacheNodeId': 'string',
                        'ReadEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'PreferredAvailabilityZone': 'string',
                        'CurrentRole': 'string'
                    },
                ]
            },
        ],
        'SnapshottingClusterId': 'string',
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'ClusterEnabled': True|False,
        'CacheNodeType': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

ReplicationGroup (dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.









Exceptions

ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.ReplicationGroupAlreadyUnderMigrationFault
ElastiCache.Client.exceptions.InvalidParameterValueException


    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled): T1 node types.
    Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def test_failover(ReplicationGroupId=None, NodeGroupId=None):
    """
    Represents the input of a TestFailover operation which test automatic failover on a specified node group (called shard in the console) in a replication group (called cluster in the console).
    For more information see:
    Also see, Testing Multi-AZ with Automatic Failover in the ElastiCache User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.test_failover(
        ReplicationGroupId='string',
        NodeGroupId='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]\nThe name of the replication group (console: cluster) whose automatic failover is being tested by this operation.\n

    :type NodeGroupId: string
    :param NodeGroupId: [REQUIRED]\nThe name of the node group (called shard in the console) in this replication group on which automatic failover is to be tested. You may test automatic failover on up to 5 node groups in any rolling 24-hour period.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReplicationGroup': {
        'ReplicationGroupId': 'string',
        'Description': 'string',
        'GlobalReplicationGroupInfo': {
            'GlobalReplicationGroupId': 'string',
            'GlobalReplicationGroupMemberRole': 'string'
        },
        'Status': 'string',
        'PendingModifiedValues': {
            'PrimaryClusterId': 'string',
            'AutomaticFailoverStatus': 'enabled'|'disabled',
            'Resharding': {
                'SlotMigration': {
                    'ProgressPercentage': 123.0
                }
            },
            'AuthTokenStatus': 'SETTING'|'ROTATING'
        },
        'MemberClusters': [
            'string',
        ],
        'NodeGroups': [
            {
                'NodeGroupId': 'string',
                'Status': 'string',
                'PrimaryEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ReaderEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'Slots': 'string',
                'NodeGroupMembers': [
                    {
                        'CacheClusterId': 'string',
                        'CacheNodeId': 'string',
                        'ReadEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'PreferredAvailabilityZone': 'string',
                        'CurrentRole': 'string'
                    },
                ]
            },
        ],
        'SnapshottingClusterId': 'string',
        'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
        'ConfigurationEndpoint': {
            'Address': 'string',
            'Port': 123
        },
        'SnapshotRetentionLimit': 123,
        'SnapshotWindow': 'string',
        'ClusterEnabled': True|False,
        'CacheNodeType': 'string',
        'AuthTokenEnabled': True|False,
        'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
        'TransitEncryptionEnabled': True|False,
        'AtRestEncryptionEnabled': True|False,
        'KmsKeyId': 'string',
        'ARN': 'string'
    }
}


Response Structure

(dict) --

ReplicationGroup (dict) --
Contains all of the attributes of a specific Redis replication group.

ReplicationGroupId (string) --
The identifier for the replication group.

Description (string) --
The user supplied description of the replication group.

GlobalReplicationGroupInfo (dict) --
The name of the Global Datastore and role of this replication group in the Global Datastore.

GlobalReplicationGroupId (string) --
The name of the Global Datastore

GlobalReplicationGroupMemberRole (string) --
The role of the replication group in a Global Datastore. Can be primary or secondary.



Status (string) --
The current state of this replication group - creating , available , modifying , deleting , create-failed , snapshotting .

PendingModifiedValues (dict) --
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

PrimaryClusterId (string) --
The primary cluster ID that is applied immediately (if --apply-immediately was specified), or during the next maintenance window.

AutomaticFailoverStatus (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


Resharding (dict) --
The status of an online resharding operation.

SlotMigration (dict) --
Represents the progress of an online resharding operation.

ProgressPercentage (float) --
The percentage of the slot migration that is complete.





AuthTokenStatus (string) --
The auth token status



MemberClusters (list) --
The names of all the cache clusters that are part of this replication group.

(string) --


NodeGroups (list) --
A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

(dict) --
Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

NodeGroupId (string) --
The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.

Status (string) --
The current state of this replication group - creating , available , etc.

PrimaryEndpoint (dict) --
The endpoint of the primary node in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



ReaderEndpoint (dict) --
The endpoint of the replica nodes in this node group (shard).

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



Slots (string) --
The keyspace for this node group (shard).

NodeGroupMembers (list) --
A list containing information about individual nodes within the node group (shard).

(dict) --
Represents a single node within a node group (shard).

CacheClusterId (string) --
The ID of the cluster to which the node belongs.

CacheNodeId (string) --
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

ReadEndpoint (dict) --
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Redis (cluster mode disabled) clusters.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



PreferredAvailabilityZone (string) --
The name of the Availability Zone in which the node is located.

CurrentRole (string) --
The role that is currently assigned to the node - primary or replica . This member is only applicable for Redis (cluster mode disabled) replication groups.









SnapshottingClusterId (string) --
The cluster ID that is used as the daily snapshot source for the replication group.

AutomaticFailover (string) --
Indicates the status of Multi-AZ with automatic failover for this Redis replication group.
Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

Redis versions earlier than 2.8.6.
Redis (cluster mode disabled): T1 node types.
Redis (cluster mode enabled): T1 node types.


ConfigurationEndpoint (dict) --
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

Address (string) --
The DNS hostname of the cache node.

Port (integer) --
The port number that the cache engine is listening on.



SnapshotRetentionLimit (integer) --
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.

Warning
If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.


SnapshotWindow (string) --
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: 05:00-09:00
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

Note
This parameter is only valid if the Engine parameter is redis .


ClusterEnabled (boolean) --
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: true | false

CacheNodeType (string) --
The name of the compute and memory capacity node type for each node in the replication group.

AuthTokenEnabled (boolean) --
A flag that enables using an AuthToken (password) when issuing Redis commands.
Default: false

AuthTokenLastModifiedDate (datetime) --
The date the auth token was last modified

TransitEncryptionEnabled (boolean) --
A flag that enables in-transit encryption when set to true .
You cannot modify the value of TransitEncryptionEnabled after the cluster is created. To enable in-transit encryption on a cluster you must set TransitEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

AtRestEncryptionEnabled (boolean) --
A flag that enables encryption at-rest when set to true .
You cannot modify the value of AtRestEncryptionEnabled after the cluster is created. To enable encryption at-rest on a cluster you must set AtRestEncryptionEnabled to true when you create a cluster.

Required: Only available when creating a replication group in an Amazon VPC using redis version 3.2.6 , 4.x or later.

Default: false

KmsKeyId (string) --
The ID of the KMS key used to encrypt the disk in the cluster.

ARN (string) --
The ARN (Amazon Resource Name) of the replication group.









Exceptions

ElastiCache.Client.exceptions.APICallRateForCustomerExceededFault
ElastiCache.Client.exceptions.InvalidCacheClusterStateFault
ElastiCache.Client.exceptions.InvalidReplicationGroupStateFault
ElastiCache.Client.exceptions.NodeGroupNotFoundFault
ElastiCache.Client.exceptions.ReplicationGroupNotFoundFault
ElastiCache.Client.exceptions.TestFailoverNotAvailableFault
ElastiCache.Client.exceptions.InvalidKMSKeyFault
ElastiCache.Client.exceptions.InvalidParameterValueException
ElastiCache.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'GlobalReplicationGroupInfo': {
                'GlobalReplicationGroupId': 'string',
                'GlobalReplicationGroupMemberRole': 'string'
            },
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled',
                'Resharding': {
                    'SlotMigration': {
                        'ProgressPercentage': 123.0
                    }
                },
                'AuthTokenStatus': 'SETTING'|'ROTATING'
            },
            'MemberClusters': [
                'string',
            ],
            'NodeGroups': [
                {
                    'NodeGroupId': 'string',
                    'Status': 'string',
                    'PrimaryEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ReaderEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'Slots': 'string',
                    'NodeGroupMembers': [
                        {
                            'CacheClusterId': 'string',
                            'CacheNodeId': 'string',
                            'ReadEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'PreferredAvailabilityZone': 'string',
                            'CurrentRole': 'string'
                        },
                    ]
                },
            ],
            'SnapshottingClusterId': 'string',
            'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
            'ConfigurationEndpoint': {
                'Address': 'string',
                'Port': 123
            },
            'SnapshotRetentionLimit': 123,
            'SnapshotWindow': 'string',
            'ClusterEnabled': True|False,
            'CacheNodeType': 'string',
            'AuthTokenEnabled': True|False,
            'AuthTokenLastModifiedDate': datetime(2015, 1, 1),
            'TransitEncryptionEnabled': True|False,
            'AtRestEncryptionEnabled': True|False,
            'KmsKeyId': 'string',
            'ARN': 'string'
        }
    }
    
    
    :returns: 
    Viewing ElastiCache Events in the ElastiCache User Guide
    DescribeEvents in the ElastiCache API Reference
    
    """
    pass

