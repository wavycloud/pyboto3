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
    :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource to which the tags are to be added, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            

    :type Tags: list
    :param Tags: [REQUIRED]
            A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag. May not be null.
            Value (string) --The tag's value. May be null.
            
            

    :rtype: dict
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

def authorize_cache_security_group_ingress(CacheSecurityGroupName=None, EC2SecurityGroupName=None, EC2SecurityGroupOwnerId=None):
    """
    Allows network ingress to a cache security group. Applications using ElastiCache must be running on Amazon EC2, and Amazon EC2 security groups are used as the authorization mechanism.
    See also: AWS API Documentation
    
    
    :example: response = client.authorize_cache_security_group_ingress(
        CacheSecurityGroupName='string',
        EC2SecurityGroupName='string',
        EC2SecurityGroupOwnerId='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: [REQUIRED]
            The cache security group that allows network ingress.
            

    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: [REQUIRED]
            The Amazon EC2 security group to be authorized for ingress to the cache security group.
            

    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: [REQUIRED]
            The AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.
            

    :rtype: dict
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
            ]
        }
    }
    
    
    :returns: 
    AuthorizeCacheSecurityGroupIngress
    CreateCacheSecurityGroup
    RevokeCacheSecurityGroupIngress
    
    """
    pass

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

def copy_snapshot(SourceSnapshotName=None, TargetSnapshotName=None, TargetBucket=None):
    """
    Makes a copy of an existing snapshot.
    You could receive the following error messages.
    See also: AWS API Documentation
    
    
    :example: response = client.copy_snapshot(
        SourceSnapshotName='string',
        TargetSnapshotName='string',
        TargetBucket='string'
    )
    
    
    :type SourceSnapshotName: string
    :param SourceSnapshotName: [REQUIRED]
            The name of an existing snapshot from which to make a copy.
            

    :type TargetSnapshotName: string
    :param TargetSnapshotName: [REQUIRED]
            A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting.
            

    :type TargetBucket: string
    :param TargetBucket: The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access.
            When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket in the Amazon ElastiCache User Guide .
            For more information, see Exporting a Snapshot in the Amazon ElastiCache User Guide .
            

    :rtype: dict
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
            ]
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
    
    
    """
    pass

def create_cache_cluster(CacheClusterId=None, ReplicationGroupId=None, AZMode=None, PreferredAvailabilityZone=None, PreferredAvailabilityZones=None, NumCacheNodes=None, CacheNodeType=None, Engine=None, EngineVersion=None, CacheParameterGroupName=None, CacheSubnetGroupName=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, Tags=None, SnapshotArns=None, SnapshotName=None, PreferredMaintenanceWindow=None, Port=None, NotificationTopicArn=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None, AuthToken=None):
    """
    Creates a cache cluster. All nodes in the cache cluster run the same protocol-compliant cache engine software, either Memcached or Redis.
    See also: AWS API Documentation
    
    
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
    :param CacheClusterId: [REQUIRED]
            The node group (shard) identifier. This parameter is stored as a lowercase string.
            Constraints:
            A name must contain from 1 to 20 alphanumeric characters or hyphens.
            The first character must be a letter.
            A name cannot end with a hyphen or contain two consecutive hyphens.
            

    :type ReplicationGroupId: string
    :param ReplicationGroupId: 
            Warning
            Due to current limitations on Redis (cluster mode disabled), this operation or parameter is not supported on Redis (cluster mode enabled) replication groups.
            The ID of the replication group to which this cache cluster should belong. If this parameter is specified, the cache cluster is added to the specified replication group as a read replica; otherwise, the cache cluster is a standalone primary that is not part of any replication group.
            If the specified replication group is Multi-AZ enabled and the Availability Zone is not specified, the cache cluster is created in Availability Zones that provide the best spread of read replicas across Availability Zones.
            Note
            This parameter is only valid if the Engine parameter is redis .
            

    :type AZMode: string
    :param AZMode: Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region.
            This parameter is only supported for Memcached cache clusters.
            If the AZMode and PreferredAvailabilityZones are not specified, ElastiCache assumes single-az mode.
            

    :type PreferredAvailabilityZone: string
    :param PreferredAvailabilityZone: The EC2 Availability Zone in which the cache cluster is created.
            All nodes belonging to this Memcached cache cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use PreferredAvailabilityZones .
            Default: System chosen Availability Zone.
            

    :type PreferredAvailabilityZones: list
    :param PreferredAvailabilityZones: A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important.
            This option is only supported on Memcached.
            Note
            If you are creating your cache cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.
            The number of Availability Zones listed must equal the value of NumCacheNodes .
            If you want all the nodes in the same Availability Zone, use PreferredAvailabilityZone instead, or repeat the Availability Zone multiple times in the list.
            Default: System chosen Availability Zones.
            (string) --
            

    :type NumCacheNodes: integer
    :param NumCacheNodes: The initial number of cache nodes that the cache cluster has.
            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
            If you need more than 20 nodes for your Memcached cluster, please fill out the ElastiCache Limit Increase Request form at http://aws.amazon.com/contact-us/elasticache-node-limit-request/ .
            

    :type CacheNodeType: string
    :param CacheNodeType: The compute and memory capacity of the nodes in the node group (shard).
            Valid node types are as follows:
            General purpose:
            Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
            Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
            Compute optimized: cache.c1.xlarge
            Memory optimized:
            Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
            Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
            
            Notes:
            All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).
            Redis backup/restore is not supported for Redis (cluster mode disabled) T1 and T2 instances. Backup/restore is supported on Redis (cluster mode enabled) T2 instances.
            Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.
            For a complete listing of node types and specifications, see Amazon ElastiCache Product Features and Details and either Cache Node Type-Specific Parameters for Memcached or Cache Node Type-Specific Parameters for Redis .
            

    :type Engine: string
    :param Engine: The name of the cache engine to be used for this cache cluster.
            Valid values for this parameter are: memcached | redis
            

    :type EngineVersion: string
    :param EngineVersion: The version number of the cache engine to be used for this cache cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cache cluster or replication group and create it anew with the earlier engine version.
            

    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of the parameter group to associate with this cache cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has cluster-enabled='yes' when creating a cluster.

    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: The name of the subnet group to be used for the cache cluster.
            Use this parameter only when you are creating a cache cluster in an Amazon Virtual Private Cloud (Amazon VPC).
            Warning
            If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see Subnets and Subnet Groups .
            

    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: A list of security group names to associate with this cache cluster.
            Use this parameter only when you are creating a cache cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            

    :type SecurityGroupIds: list
    :param SecurityGroupIds: One or more VPC security groups associated with the cache cluster.
            Use this parameter only when you are creating a cache cluster in an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            

    :type Tags: list
    :param Tags: A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag. May not be null.
            Value (string) --The tag's value. May be null.
            
            

    :type SnapshotArns: list
    :param SnapshotArns: A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Example of an Amazon S3 ARN: arn:aws:s3:::my_bucket/snapshot1.rdb
            (string) --
            

    :type SnapshotName: string
    :param SnapshotName: The name of a Redis snapshot from which to restore data into the new node group (shard). The snapshot status changes to restoring while the new node group (shard) is being created.
            Note
            This parameter is only valid if the Engine parameter is redis .
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cache cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:
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
            

    :type Port: integer
    :param Port: The port number on which each of the cache nodes accepts connections.

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.
            Note
            The Amazon SNS topic owner must be the same as the cache cluster owner.
            

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.

    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot taken today is retained for 5 days before being deleted.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Default: 0 (i.e., automatic backups are disabled for this cache cluster).
            

    :type SnapshotWindow: string
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
            Example: 05:00-09:00
            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
            Note: This parameter is only valid if the Engine parameter is redis .
            

    :type AuthToken: string
    :param AuthToken: 
            Reserved parameter. The password used to access a password protected server.
            Password constraints:
            Must be only printable ASCII characters.
            Must be at least 16 characters and no more than 128 characters in length.
            Cannot contain any of the following characters: '/', ''', or '@'.
            For more information, see AUTH password at Redis.
            

    :rtype: dict
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
                'CacheNodeType': 'string'
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
            'SnapshotWindow': 'string'
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
    """
    pass

def create_cache_parameter_group(CacheParameterGroupName=None, CacheParameterGroupFamily=None, Description=None):
    """
    Creates a new Amazon ElastiCache cache parameter group. An ElastiCache cache parameter group is a collection of parameters and their values that are applied to all of the nodes in any cache cluster or replication group using the CacheParameterGroup.
    A newly created CacheParameterGroup is an exact duplicate of the default parameter group for the CacheParameterGroupFamily. To customize the newly created CacheParameterGroup you can change the values of specific parameters. For more information, see:
    See also: AWS API Documentation
    
    
    :example: response = client.create_cache_parameter_group(
        CacheParameterGroupName='string',
        CacheParameterGroupFamily='string',
        Description='string'
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: [REQUIRED]
            A user-specified name for the cache parameter group.
            

    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: [REQUIRED]
            The name of the cache parameter group family that the cache parameter group can be used with.
            Valid values are: memcached1.4 | redis2.6 | redis2.8 | redis3.2
            

    :type Description: string
    :param Description: [REQUIRED]
            A user-specified description for the cache parameter group.
            

    :rtype: dict
    :return: {
        'CacheParameterGroup': {
            'CacheParameterGroupName': 'string',
            'CacheParameterGroupFamily': 'string',
            'Description': 'string'
        }
    }
    
    
    :returns: 
    CacheParameterGroupName (string) -- [REQUIRED]
    A user-specified name for the cache parameter group.
    
    CacheParameterGroupFamily (string) -- [REQUIRED]
    The name of the cache parameter group family that the cache parameter group can be used with.
    Valid values are: memcached1.4 | redis2.6 | redis2.8 | redis3.2
    
    Description (string) -- [REQUIRED]
    A user-specified description for the cache parameter group.
    
    
    """
    pass

def create_cache_security_group(CacheSecurityGroupName=None, Description=None):
    """
    Creates a new cache security group. Use a cache security group to control access to one or more cache clusters.
    Cache security groups are only used when you are creating a cache cluster outside of an Amazon Virtual Private Cloud (Amazon VPC). If you are creating a cache cluster inside of a VPC, use a cache subnet group instead. For more information, see CreateCacheSubnetGroup .
    See also: AWS API Documentation
    
    
    :example: response = client.create_cache_security_group(
        CacheSecurityGroupName='string',
        Description='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: [REQUIRED]
            A name for the cache security group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters. Cannot be the word 'Default'.
            Example: mysecuritygroup
            

    :type Description: string
    :param Description: [REQUIRED]
            A description for the cache security group.
            

    :rtype: dict
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
            ]
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
    
    
    :example: response = client.create_cache_subnet_group(
        CacheSubnetGroupName='string',
        CacheSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: [REQUIRED]
            A name for the cache subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
            Example: mysubnetgroup
            

    :type CacheSubnetGroupDescription: string
    :param CacheSubnetGroupDescription: [REQUIRED]
            A description for the cache subnet group.
            

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]
            A list of VPC subnet IDs for the cache subnet group.
            (string) --
            

    :rtype: dict
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
            ]
        }
    }
    
    
    :returns: 
    CreateCacheSubnetGroup
    ModifyCacheSubnetGroup
    
    """
    pass

def create_replication_group(ReplicationGroupId=None, ReplicationGroupDescription=None, PrimaryClusterId=None, AutomaticFailoverEnabled=None, NumCacheClusters=None, PreferredCacheClusterAZs=None, NumNodeGroups=None, ReplicasPerNodeGroup=None, NodeGroupConfiguration=None, CacheNodeType=None, Engine=None, EngineVersion=None, CacheParameterGroupName=None, CacheSubnetGroupName=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, Tags=None, SnapshotArns=None, SnapshotName=None, PreferredMaintenanceWindow=None, Port=None, NotificationTopicArn=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None, AuthToken=None):
    """
    Creates a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication group.
    A Redis (cluster mode disabled) replication group is a collection of cache clusters, where one of the cache clusters is a read/write primary and the others are read-only replicas. Writes to the primary are asynchronously propagated to the replicas.
    A Redis (cluster mode enabled) replication group is a collection of 1 to 15 node groups (shards). Each node group (shard) has one read/write primary node and up to 5 read-only replica nodes. Writes to the primary are asynchronously propagated to the replicas. Redis (cluster mode enabled) replication groups partition the data across node groups (shards).
    When a Redis (cluster mode disabled) replication group has been successfully created, you can add one or more read replicas to it, up to a total of 5 read replicas. You cannot alter a Redis (cluster mode enabled) replication group after it has been created. However, if you need to increase or decrease the number of node groups (console: shards), you can avail yourself of ElastiCache for Redis' enhanced backup and restore. For more information, see Restoring From a Backup with Cluster Resizing in the ElastiCache User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_replication_group(
        ReplicationGroupId='string',
        ReplicationGroupDescription='string',
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
        AuthToken='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]
            The replication group identifier. This parameter is stored as a lowercase string.
            Constraints:
            A name must contain from 1 to 20 alphanumeric characters or hyphens.
            The first character must be a letter.
            A name cannot end with a hyphen or contain two consecutive hyphens.
            

    :type ReplicationGroupDescription: string
    :param ReplicationGroupDescription: [REQUIRED]
            A user-created description for the replication group.
            

    :type PrimaryClusterId: string
    :param PrimaryClusterId: The identifier of the cache cluster that serves as the primary for this replication group. This cache cluster must already exist and have a status of available .
            This parameter is not required if NumCacheClusters , NumNodeGroups , or ReplicasPerNodeGroup is specified.
            

    :type AutomaticFailoverEnabled: boolean
    :param AutomaticFailoverEnabled: Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.
            If true , Multi-AZ is enabled for this replication group. If false , Multi-AZ is disabled for this replication group.
            AutomaticFailoverEnabled must be enabled for Redis (cluster mode enabled) replication groups.
            Default: false
            Note
            ElastiCache Multi-AZ replication groups is not supported on:
            Redis versions earlier than 2.8.6.
            Redis (cluster mode disabled): T1 and T2 node types. Redis (cluster mode enabled): T2 node types.
            

    :type NumCacheClusters: integer
    :param NumCacheClusters: The number of clusters this replication group initially has.
            This parameter is not used if there is more than one node group (shard). You should use ReplicasPerNodeGroup instead.
            If AutomaticFailoverEnabled is true , the value of this parameter must be at least 2. If AutomaticFailoverEnabled is false you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6.
            The maximum permitted value for NumCacheClusters is 6 (primary plus 5 replicas).
            

    :type PreferredCacheClusterAZs: list
    :param PreferredCacheClusterAZs: A list of EC2 Availability Zones in which the replication group's cache clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list.
            This parameter is not used if there is more than one node group (shard). You should use NodeGroupConfiguration instead.
            Note
            If you are creating your replication group in an Amazon VPC (recommended), you can only locate cache clusters in Availability Zones associated with the subnets in the selected subnet group.
            The number of Availability Zones listed must equal the value of NumCacheClusters .
            Default: system chosen Availability Zones.
            (string) --
            

    :type NumNodeGroups: integer
    :param NumNodeGroups: An optional parameter that specifies the number of node groups (shards) for this Redis (cluster mode enabled) replication group. For Redis (cluster mode disabled) either omit this parameter or set it to 1.
            Default: 1
            

    :type ReplicasPerNodeGroup: integer
    :param ReplicasPerNodeGroup: An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.

    :type NodeGroupConfiguration: list
    :param NodeGroupConfiguration: A list of node group (shard) configuration options. Each node group (shard) configuration has the following: Slots, PrimaryAvailabilityZone, ReplicaAvailabilityZones, ReplicaCount.
            If you're creating a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication group, you can use this parameter to individually configure each node group (shard), or you can omit this parameter.
            (dict) --node group (shard) configuration options. Each node group (shard) configuration has the following: Slots , PrimaryAvailabilityZone , ReplicaAvailabilityZones , ReplicaCount .
            Slots (string) --A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format startkey-endkey .
            Example: '0-3999'
            ReplicaCount (integer) --The number of read replica nodes in this node group (shard).
            PrimaryAvailabilityZone (string) --The Availability Zone where the primary node of this node group (shard) is launched.
            ReplicaAvailabilityZones (list) --A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ReplicaCount or ReplicasPerNodeGroup if not specified.
            (string) --
            
            

    :type CacheNodeType: string
    :param CacheNodeType: The compute and memory capacity of the nodes in the node group (shard).
            Valid node types are as follows:
            General purpose:
            Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
            Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
            Compute optimized: cache.c1.xlarge
            Memory optimized:
            Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
            Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
            
            Notes:
            All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).
            Redis backup/restore is not supported for Redis (cluster mode disabled) T1 and T2 instances. Backup/restore is supported on Redis (cluster mode enabled) T2 instances.
            Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.
            For a complete listing of node types and specifications, see Amazon ElastiCache Product Features and Details and either Cache Node Type-Specific Parameters for Memcached or Cache Node Type-Specific Parameters for Redis .
            

    :type Engine: string
    :param Engine: The name of the cache engine to be used for the cache clusters in this replication group.

    :type EngineVersion: string
    :param EngineVersion: The version number of the cache engine to be used for the cache clusters in this replication group. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ) in the ElastiCache User Guide , but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cache cluster or replication group and create it anew with the earlier engine version.
            

    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
            If you are running Redis version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name.
            To create a Redis (cluster mode disabled) replication group, use CacheParameterGroupName=default.redis3.2 .
            To create a Redis (cluster mode enabled) replication group, use CacheParameterGroupName=default.redis3.2.cluster.on .
            

    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: The name of the cache subnet group to be used for the replication group.
            Warning
            If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see Subnets and Subnet Groups .
            

    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: A list of cache security group names to associate with this replication group.
            (string) --
            

    :type SecurityGroupIds: list
    :param SecurityGroupIds: One or more Amazon VPC security groups associated with this replication group.
            Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            

    :type Tags: list
    :param Tags: A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag. May not be null.
            Value (string) --The tag's value. May be null.
            
            

    :type SnapshotArns: list
    :param SnapshotArns: A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter NumNodeGroups or the number of node groups configured by NodeGroupConfiguration regardless of the number of ARNs specified here.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Example of an Amazon S3 ARN: arn:aws:s3:::my_bucket/snapshot1.rdb
            (string) --
            

    :type SnapshotName: string
    :param SnapshotName: The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to restoring while the new replication group is being created.
            Note
            This parameter is only valid if the Engine parameter is redis .
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cache cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:
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
            

    :type Port: integer
    :param Port: The port number on which each member of the replication group accepts connections.

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.
            Note
            The Amazon SNS topic owner must be the same as the cache cluster owner.
            

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.

    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Default: 0 (i.e., automatic backups are disabled for this cache cluster).
            

    :type SnapshotWindow: string
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
            Example: 05:00-09:00
            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
            Note
            This parameter is only valid if the Engine parameter is redis .
            

    :type AuthToken: string
    :param AuthToken: 
            Reserved parameter. The password used to access a password protected server.
            Password constraints:
            Must be only printable ASCII characters.
            Must be at least 16 characters and no more than 128 characters in length.
            Cannot contain any of the following characters: '/', ''', or '@'.
            For more information, see AUTH password at Redis.
            

    :rtype: dict
    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled'
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
            'CacheNodeType': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled):T1 and T2 cache node types. Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def create_snapshot(ReplicationGroupId=None, CacheClusterId=None, SnapshotName=None):
    """
    Creates a copy of an entire cache cluster or replication group at a specific moment in time.
    See also: AWS API Documentation
    
    
    :example: response = client.create_snapshot(
        ReplicationGroupId='string',
        CacheClusterId='string',
        SnapshotName='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: The identifier of an existing replication group. The snapshot is created from this replication group.

    :type CacheClusterId: string
    :param CacheClusterId: The identifier of an existing cache cluster. The snapshot is created from this cache cluster.

    :type SnapshotName: string
    :param SnapshotName: [REQUIRED]
            A name for the snapshot being created.
            

    :rtype: dict
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
            ]
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
    """
    pass

def delete_cache_cluster(CacheClusterId=None, FinalSnapshotIdentifier=None):
    """
    Deletes a previously provisioned cache cluster. DeleteCacheCluster deletes all associated cache nodes, node endpoints and the cache cluster itself. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the cache cluster; you cannot cancel or revert this operation.
    This operation cannot be used to delete a cache cluster that is the last read replica of a replication group or node group (shard) that has Multi-AZ mode enabled or a cache cluster from a Redis (cluster mode enabled) replication group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cache_cluster(
        CacheClusterId='string',
        FinalSnapshotIdentifier='string'
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: [REQUIRED]
            The cache cluster identifier for the cluster to be deleted. This parameter is not case sensitive.
            

    :type FinalSnapshotIdentifier: string
    :param FinalSnapshotIdentifier: The user-supplied name of a final cache cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cache cluster immediately afterward.

    :rtype: dict
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
                'CacheNodeType': 'string'
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
            'SnapshotWindow': 'string'
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
    """
    pass

def delete_cache_parameter_group(CacheParameterGroupName=None):
    """
    Deletes the specified cache parameter group. You cannot delete a cache parameter group if it is associated with any cache clusters.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cache_parameter_group(
        CacheParameterGroupName='string'
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: [REQUIRED]
            The name of the cache parameter group to delete.
            Note
            The specified cache security group must not be associated with any cache clusters.
            

    """
    pass

def delete_cache_security_group(CacheSecurityGroupName=None):
    """
    Deletes a cache security group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cache_security_group(
        CacheSecurityGroupName='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: [REQUIRED]
            The name of the cache security group to delete.
            Note
            You cannot delete the default security group.
            

    """
    pass

def delete_cache_subnet_group(CacheSubnetGroupName=None):
    """
    Deletes a cache subnet group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cache_subnet_group(
        CacheSubnetGroupName='string'
    )
    
    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: [REQUIRED]
            The name of the cache subnet group to delete.
            Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
            

    """
    pass

def delete_replication_group(ReplicationGroupId=None, RetainPrimaryCluster=None, FinalSnapshotIdentifier=None):
    """
    Deletes an existing replication group. By default, this operation deletes the entire replication group, including the primary/primaries and all of the read replicas. If the replication group has only one primary, you can optionally delete only the read replicas, while retaining the primary by setting RetainPrimaryCluster=true .
    When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_replication_group(
        ReplicationGroupId='string',
        RetainPrimaryCluster=True|False,
        FinalSnapshotIdentifier='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]
            The identifier for the cluster to be deleted. This parameter is not case sensitive.
            

    :type RetainPrimaryCluster: boolean
    :param RetainPrimaryCluster: If set to true , all of the read replicas are deleted, but the primary node is retained.

    :type FinalSnapshotIdentifier: string
    :param FinalSnapshotIdentifier: The name of a final node group (shard) snapshot. ElastiCache creates the snapshot from the primary node in the cluster, rather than one of the replicas; this is to ensure that it captures the freshest data. After the final snapshot is taken, the replication group is immediately deleted.

    :rtype: dict
    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled'
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
            'CacheNodeType': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled):T1 and T2 cache node types. Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def delete_snapshot(SnapshotName=None):
    """
    Deletes an existing snapshot. When you receive a successful response from this operation, ElastiCache immediately begins deleting the snapshot; you cannot cancel or revert this operation.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_snapshot(
        SnapshotName='string'
    )
    
    
    :type SnapshotName: string
    :param SnapshotName: [REQUIRED]
            The name of the snapshot to be deleted.
            

    :rtype: dict
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
            ]
        }
    }
    
    
    :returns: 
    All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).
    Redis backup/restore is not supported for Redis (cluster mode disabled) T1 and T2 instances. Backup/restore is supported on Redis (cluster mode enabled) T2 instances.
    Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.
    
    """
    pass

def describe_cache_clusters(CacheClusterId=None, MaxRecords=None, Marker=None, ShowCacheNodeInfo=None, ShowCacheClustersNotInReplicationGroups=None):
    """
    Returns information about all provisioned cache clusters if no cache cluster identifier is specified, or about a specific cache cluster if a cache cluster identifier is supplied.
    By default, abbreviated information about the cache clusters is returned. You can use the optional ShowCacheNodeInfo flag to retrieve detailed information about the cache nodes associated with the cache clusters. These details include the DNS address and port for the cache node endpoint.
    If the cluster is in the creating state, only cluster-level information is displayed until all of the nodes are successfully provisioned.
    If the cluster is in the deleting state, only cluster-level information is displayed.
    If cache nodes are currently being added to the cache cluster, node endpoint information and creation time for the additional nodes are not displayed until they are completely provisioned. When the cache cluster state is available , the cluster is ready for use.
    If cache nodes are currently being removed from the cache cluster, no endpoint information for the removed nodes is displayed.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cache_clusters(
        CacheClusterId='string',
        MaxRecords=123,
        Marker='string',
        ShowCacheNodeInfo=True|False,
        ShowCacheClustersNotInReplicationGroups=True|False
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: The user-supplied cluster identifier. If this parameter is specified, only information about that specific cache cluster is returned. This parameter isn't case sensitive.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type ShowCacheNodeInfo: boolean
    :param ShowCacheNodeInfo: An optional flag that can be included in the DescribeCacheCluster request to retrieve information about the individual cache nodes.

    :type ShowCacheClustersNotInReplicationGroups: boolean
    :param ShowCacheClustersNotInReplicationGroups: An optional flag that can be included in the DescribeCacheCluster request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this mean Memcached and single node Redis clusters.

    :rtype: dict
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
                    'CacheNodeType': 'string'
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
                'SnapshotWindow': 'string'
            },
        ]
    }
    
    
    :returns: 
    General purpose:
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
    """
    pass

def describe_cache_engine_versions(Engine=None, EngineVersion=None, CacheParameterGroupFamily=None, MaxRecords=None, Marker=None, DefaultOnly=None):
    """
    Returns a list of the available cache engines and their versions.
    See also: AWS API Documentation
    
    
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
    :param EngineVersion: The cache engine version to return.
            Example: 1.4.14
            

    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: The name of a specific cache parameter group family to return details for.
            Valid values are: memcached1.4 | redis2.6 | redis2.8 | redis3.2
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type DefaultOnly: boolean
    :param DefaultOnly: If true , specifies that only the default version of the specified engine or engine and major version combination is to be returned.

    :rtype: dict
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
    
    
    :example: response = client.describe_cache_parameter_groups(
        CacheParameterGroupName='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of a specific cache parameter group to return details for.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'CacheParameterGroups': [
            {
                'CacheParameterGroupName': 'string',
                'CacheParameterGroupFamily': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_cache_parameters(CacheParameterGroupName=None, Source=None, MaxRecords=None, Marker=None):
    """
    Returns the detailed parameter list for a particular cache parameter group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cache_parameters(
        CacheParameterGroupName='string',
        Source='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: [REQUIRED]
            The name of a specific cache parameter group to return details for.
            

    :type Source: string
    :param Source: The parameter types to return.
            Valid values: user | system | engine-default
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
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
    
    
    """
    pass

def describe_cache_security_groups(CacheSecurityGroupName=None, MaxRecords=None, Marker=None):
    """
    Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cache_security_groups(
        CacheSecurityGroupName='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: The name of the cache security group to return details for.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
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
                ]
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
    Returns a list of cache subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cache_subnet_groups(
        CacheSubnetGroupName='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: The name of the cache subnet group to return details for.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
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
                ]
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
    
    
    :example: response = client.describe_engine_default_parameters(
        CacheParameterGroupFamily='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: [REQUIRED]
            The name of the cache parameter group family.
            Valid values are: memcached1.4 | redis2.6 | redis2.8 | redis3.2
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
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
    
    
    """
    pass

def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, MaxRecords=None, Marker=None):
    """
    Returns events related to cache clusters, cache security groups, and cache parameter groups. You can obtain events specific to a particular cache cluster, cache security group, or cache parameter group by providing the name as a parameter.
    By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days' worth of events if necessary.
    See also: AWS API Documentation
    
    
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
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format.
            Example: 2017-03-30T07:03:49.555Z
            

    :type EndTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format.
            Example: 2017-03-30T07:03:49.555Z
            

    :type Duration: integer
    :param Duration: The number of minutes worth of events to retrieve.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
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
    
    
    """
    pass

def describe_replication_groups(ReplicationGroupId=None, MaxRecords=None, Marker=None):
    """
    Returns information about a particular replication group. If no identifier is specified, DescribeReplicationGroups returns information about all replication groups.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_replication_groups(
        ReplicationGroupId='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: The identifier for the replication group to be described. This parameter is not case sensitive.
            If you do not specify this parameter, information about all replication groups is returned.
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ReplicationGroups': [
            {
                'ReplicationGroupId': 'string',
                'Description': 'string',
                'Status': 'string',
                'PendingModifiedValues': {
                    'PrimaryClusterId': 'string',
                    'AutomaticFailoverStatus': 'enabled'|'disabled'
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
                'CacheNodeType': 'string'
            },
        ]
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled):T1 and T2 cache node types. Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def describe_reserved_cache_nodes(ReservedCacheNodeId=None, ReservedCacheNodesOfferingId=None, CacheNodeType=None, Duration=None, ProductDescription=None, OfferingType=None, MaxRecords=None, Marker=None):
    """
    Returns information about reserved cache nodes for this account, or about a specified reserved cache node.
    See also: AWS API Documentation
    
    
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
    :param CacheNodeType: The cache node type filter value. Use this parameter to show only those reservations matching the specified cache node type.
            Valid node types are as follows:
            General purpose:
            Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
            Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
            Compute optimized: cache.c1.xlarge
            Memory optimized:
            Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
            Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
            
            Notes:
            All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).
            Redis backup/restore is not supported for Redis (cluster mode disabled) T1 and T2 instances. Backup/restore is supported on Redis (cluster mode enabled) T2 instances.
            Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.
            For a complete listing of node types and specifications, see Amazon ElastiCache Product Features and Details and either Cache Node Type-Specific Parameters for Memcached or Cache Node Type-Specific Parameters for Redis .
            

    :type Duration: string
    :param Duration: The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.
            Valid Values: 1 | 3 | 31536000 | 94608000
            

    :type ProductDescription: string
    :param ProductDescription: The product description filter value. Use this parameter to show only those reservations matching the specified product description.

    :type OfferingType: string
    :param OfferingType: The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.
            Valid values: 'Light Utilization'|'Medium Utilization'|'Heavy Utilization'
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
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
                ]
            },
        ]
    }
    
    
    :returns: 
    General purpose:
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
    """
    pass

def describe_reserved_cache_nodes_offerings(ReservedCacheNodesOfferingId=None, CacheNodeType=None, Duration=None, ProductDescription=None, OfferingType=None, MaxRecords=None, Marker=None):
    """
    Lists available reserved cache node offerings.
    See also: AWS API Documentation
    
    
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
    :param ReservedCacheNodesOfferingId: The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.
            Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
            

    :type CacheNodeType: string
    :param CacheNodeType: The cache node type filter value. Use this parameter to show only the available offerings matching the specified cache node type.
            Valid node types are as follows:
            General purpose:
            Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
            Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
            Compute optimized: cache.c1.xlarge
            Memory optimized:
            Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
            Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
            
            Notes:
            All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).
            Redis backup/restore is not supported for Redis (cluster mode disabled) T1 and T2 instances. Backup/restore is supported on Redis (cluster mode enabled) T2 instances.
            Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances.
            For a complete listing of node types and specifications, see Amazon ElastiCache Product Features and Details and either Cache Node Type-Specific Parameters for Memcached or Cache Node Type-Specific Parameters for Redis .
            

    :type Duration: string
    :param Duration: Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.
            Valid Values: 1 | 3 | 31536000 | 94608000
            

    :type ProductDescription: string
    :param ProductDescription: The product description filter value. Use this parameter to show only the available offerings matching the specified product description.

    :type OfferingType: string
    :param OfferingType: The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.
            Valid Values: 'Light Utilization'|'Medium Utilization'|'Heavy Utilization'
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict
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
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
    """
    pass

def describe_snapshots(ReplicationGroupId=None, CacheClusterId=None, SnapshotName=None, SnapshotSource=None, Marker=None, MaxRecords=None, ShowNodeGroupConfig=None):
    """
    Returns information about cache cluster or replication group snapshots. By default, DescribeSnapshots lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cache cluster.
    See also: AWS API Documentation
    
    
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
    :param CacheClusterId: A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cache cluster are described.

    :type SnapshotName: string
    :param SnapshotName: A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described.

    :type SnapshotSource: string
    :param SnapshotSource: If set to system , the output shows snapshots that were automatically created by ElastiCache. If set to user the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.

    :type Marker: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 50
            Constraints: minimum 20; maximum 50.
            

    :type ShowNodeGroupConfig: boolean
    :param ShowNodeGroupConfig: A Boolean value which if true, the node group (shard) configuration is included in the snapshot description.

    :rtype: dict
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
                ]
            },
        ]
    }
    
    
    :returns: 
    General purpose:
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
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

def get_waiter():
    """
    
    """
    pass

def list_allowed_node_type_modifications(CacheClusterId=None, ReplicationGroupId=None):
    """
    Lists all available node types that you can scale your Redis cluster's or replication group's current node type up to.
    When you use the ModifyCacheCluster or ModifyReplicationGroup operations to scale up your cluster or replication group, the value of the CacheNodeType parameter must be one of the node types returned by this operation.
    See also: AWS API Documentation
    
    
    :example: response = client.list_allowed_node_type_modifications(
        CacheClusterId='string',
        ReplicationGroupId='string'
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: The name of the cache cluster you want to scale up to a larger node instanced type. ElastiCache uses the cluster id to identify the current node type of this cluster and from that to create a list of node types you can scale up to.
            Warning
            You must provide a value for either the CacheClusterId or the ReplicationGroupId .
            

    :type ReplicationGroupId: string
    :param ReplicationGroupId: The name of the replication group want to scale up to a larger node type. ElastiCache uses the replication group id to identify the current node type being used by this replication group, and from that to create a list of node types you can scale up to.
            Warning
            You must provide a value for either the CacheClusterId or the ReplicationGroupId .
            

    :rtype: dict
    :return: {
        'ScaleUpModifications': [
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
    You can have a maximum of 50 cost allocation tags on an ElastiCache resource. For more information, see Using Cost Allocation Tags in Amazon ElastiCache .
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceName='string'
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource for which you want the list of tags, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            

    :rtype: dict
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

def modify_cache_cluster(CacheClusterId=None, NumCacheNodes=None, CacheNodeIdsToRemove=None, AZMode=None, NewAvailabilityZones=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, PreferredMaintenanceWindow=None, NotificationTopicArn=None, CacheParameterGroupName=None, NotificationTopicStatus=None, ApplyImmediately=None, EngineVersion=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None, CacheNodeType=None):
    """
    Modifies the settings for a cache cluster. You can use this operation to change one or more cluster configuration parameters by specifying the parameters and the new values.
    See also: AWS API Documentation
    
    
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
        CacheNodeType='string'
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: [REQUIRED]
            The cache cluster identifier. This value is stored as a lowercase string.
            

    :type NumCacheNodes: integer
    :param NumCacheNodes: The number of cache nodes that the cache cluster should have. If the value for NumCacheNodes is greater than the sum of the number of current cache nodes and the number of cache nodes pending creation (which may be zero), more nodes are added. If the value is less than the number of existing cache nodes, nodes are removed. If the value is equal to the number of current cache nodes, any pending add or remove requests are canceled.
            If you are removing cache nodes, you must use the CacheNodeIdsToRemove parameter to provide the IDs of the specific cache nodes to remove.
            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
            Note
            Adding or removing Memcached cache nodes can be applied immediately or as a pending operation (see ApplyImmediately ).
            A pending operation to modify the number of cache nodes in a cluster during its maintenance window, whether by adding or removing nodes in accordance with the scale out architecture, is not queued. The customer's latest request to add or remove nodes to the cluster overrides any previous pending operations to modify the number of cache nodes in the cluster. For example, a request to remove 2 nodes would override a previous pending operation to remove 3 nodes. Similarly, a request to add 2 nodes would override a previous pending operation to remove 3 nodes and vice versa. As Memcached cache nodes may now be provisioned in different Availability Zones with flexible cache node placement, a request to add nodes does not automatically override a previous pending operation to add nodes. The customer can modify the previous pending operation to add more nodes or explicitly cancel the pending request and retry the new request. To cancel pending operations to modify the number of cache nodes in a cluster, use the ModifyCacheCluster request and set NumCacheNodes equal to the number of cache nodes currently in the cache cluster.
            

    :type CacheNodeIdsToRemove: list
    :param CacheNodeIdsToRemove: A list of cache node IDs to be removed. A node ID is a numeric identifier (0001, 0002, etc.). This parameter is only valid when NumCacheNodes is less than the existing number of cache nodes. The number of cache node IDs supplied in this parameter must match the difference between the existing number of cache nodes in the cluster or pending cache nodes, whichever is greater, and the value of NumCacheNodes in the request.
            For example: If you have 3 active cache nodes, 7 pending cache nodes, and the number of cache nodes in this ModifyCacheCluser call is 5, you must list 2 (7 - 5) cache node IDs to remove.
            (string) --
            

    :type AZMode: string
    :param AZMode: Specifies whether the new nodes in this Memcached cache cluster are all created in a single Availability Zone or created across multiple Availability Zones.
            Valid values: single-az | cross-az .
            This option is only supported for Memcached cache clusters.
            Note
            You cannot specify single-az if the Memcached cache cluster already has cache nodes in different Availability Zones. If cross-az is specified, existing Memcached nodes remain in their current Availability Zone.
            Only newly created nodes are located in different Availability Zones. For instructions on how to move existing Memcached nodes to different Availability Zones, see the Availability Zone Considerations section of Cache Node Considerations for Memcached .
            

    :type NewAvailabilityZones: list
    :param NewAvailabilityZones: The list of Availability Zones where the new Memcached cache nodes are created.
            This parameter is only valid when NumCacheNodes in the request is greater than the sum of the number of active cache nodes and the number of cache nodes pending creation (which may be zero). The number of Availability Zones supplied in this list must match the cache nodes being added in this request.
            This option is only supported on Memcached clusters.
            Scenarios:
            Scenario 1: You have 3 active nodes and wish to add 2 nodes. Specify NumCacheNodes=5 (3 + 2) and optionally specify two Availability Zones for the two new nodes.
            Scenario 2: You have 3 active nodes and 2 nodes pending creation (from the scenario 1 call) and want to add 1 more node. Specify NumCacheNodes=6 ((3 + 2) + 1) and optionally specify an Availability Zone for the new node.
            Scenario 3: You want to cancel all pending operations. Specify NumCacheNodes=3 to cancel all pending operations.
            The Availability Zone placement of nodes pending creation cannot be modified. If you wish to cancel any nodes pending creation, add 0 nodes by setting NumCacheNodes to the number of current nodes.
            If cross-az is specified, existing Memcached nodes remain in their current Availability Zone. Only newly created nodes can be located in different Availability Zones. For guidance on how to move existing Memcached nodes to different Availability Zones, see the Availability Zone Considerations section of Cache Node Considerations for Memcached .
            Impact of new add/remove requests upon pending requests
            Scenario-1
            Pending Action: Delete
            New Request: Delete
            Result: The new delete, pending or immediate, replaces the pending delete.
            Scenario-2
            Pending Action: Delete
            New Request: Create
            Result: The new create, pending or immediate, replaces the pending delete.
            Scenario-3
            Pending Action: Create
            New Request: Delete
            Result: The new delete, pending or immediate, replaces the pending create.
            Scenario-4
            Pending Action: Create
            New Request: Create
            Result: The new create is added to the pending create.
            Warning
            Important: If the new create request is Apply Immediately - Yes , all creates are performed immediately. If the new create request is Apply Immediately - No , all creates are pending.
            
            (string) --
            

    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: A list of cache security group names to authorize on this cache cluster. This change is asynchronously applied as soon as possible.
            You can use this parameter only with clusters that are created outside of an Amazon Virtual Private Cloud (Amazon VPC).
            Constraints: Must contain no more than 255 alphanumeric characters. Must not be 'Default'.
            (string) --
            

    :type SecurityGroupIds: list
    :param SecurityGroupIds: Specifies the VPC Security Groups associated with the cache cluster.
            This parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
            Valid values for ddd are:
            sun
            mon
            tue
            wed
            thu
            fri
            sat
            Example: sun:23:00-mon:01:30
            

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.
            Note
            The Amazon SNS topic owner must be same as the cache cluster owner.
            

    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of the cache parameter group to apply to this cache cluster. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for this request.

    :type NotificationTopicStatus: string
    :param NotificationTopicStatus: The status of the Amazon SNS notification topic. Notifications are sent only if the status is active .
            Valid values: active | inactive
            

    :type ApplyImmediately: boolean
    :param ApplyImmediately: If true , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow setting for the cache cluster.
            If false , changes to the cache cluster are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.
            Warning
            If you perform a ModifyCacheCluster before a pending modification is applied, the pending modification is replaced by the newer modification.
            Valid values: true | false
            Default: false
            

    :type EngineVersion: string
    :param EngineVersion: The upgraded version of the cache engine to be run on the cache nodes.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cache cluster and create it anew with the earlier engine version.
            

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.

    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic cache cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
            Note
            If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
            

    :type SnapshotWindow: string
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cache cluster.

    :type CacheNodeType: string
    :param CacheNodeType: A valid cache node type that you want to scale this cache cluster up to.

    :rtype: dict
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
                'CacheNodeType': 'string'
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
            'SnapshotWindow': 'string'
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
    """
    pass

def modify_cache_parameter_group(CacheParameterGroupName=None, ParameterNameValues=None):
    """
    Modifies the parameters of a cache parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.
    See also: AWS API Documentation
    
    
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
    :param CacheParameterGroupName: [REQUIRED]
            The name of the cache parameter group to modify.
            

    :type ParameterNameValues: list
    :param ParameterNameValues: [REQUIRED]
            An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be modified per request.
            (dict) --Describes a name-value pair that is used to update the value of a parameter.
            ParameterName (string) --The name of the parameter.
            ParameterValue (string) --The value of the parameter.
            
            

    :rtype: dict
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
    
    
    :example: response = client.modify_cache_subnet_group(
        CacheSubnetGroupName='string',
        CacheSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: [REQUIRED]
            The name for the cache subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
            Example: mysubnetgroup
            

    :type CacheSubnetGroupDescription: string
    :param CacheSubnetGroupDescription: A description of the cache subnet group.

    :type SubnetIds: list
    :param SubnetIds: The EC2 subnet IDs for the cache subnet group.
            (string) --
            

    :rtype: dict
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
            ]
        }
    }
    
    
    :returns: 
    CreateCacheSubnetGroup
    ModifyCacheSubnetGroup
    
    """
    pass

def modify_replication_group(ReplicationGroupId=None, ReplicationGroupDescription=None, PrimaryClusterId=None, SnapshottingClusterId=None, AutomaticFailoverEnabled=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, PreferredMaintenanceWindow=None, NotificationTopicArn=None, CacheParameterGroupName=None, NotificationTopicStatus=None, ApplyImmediately=None, EngineVersion=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None, CacheNodeType=None, NodeGroupId=None):
    """
    Modifies the settings for a replication group.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_replication_group(
        ReplicationGroupId='string',
        ReplicationGroupDescription='string',
        PrimaryClusterId='string',
        SnapshottingClusterId='string',
        AutomaticFailoverEnabled=True|False,
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
        NodeGroupId='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]
            The identifier of the replication group to modify.
            

    :type ReplicationGroupDescription: string
    :param ReplicationGroupDescription: A description for the replication group. Maximum length is 255 characters.

    :type PrimaryClusterId: string
    :param PrimaryClusterId: For replication groups with a single primary, if this parameter is specified, ElastiCache promotes the specified cluster in the specified replication group to the primary role. The nodes of all other clusters in the replication group are read replicas.

    :type SnapshottingClusterId: string
    :param SnapshottingClusterId: The cache cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Redis (cluster mode enabled) replication groups.

    :type AutomaticFailoverEnabled: boolean
    :param AutomaticFailoverEnabled: Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure.
            Valid values: true | false
            Note
            ElastiCache Multi-AZ replication groups are not supported on:
            Redis versions earlier than 2.8.6.
            Redis (cluster mode disabled):T1 and T2 cache node types. Redis (cluster mode enabled): T1 node types.
            

    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: A list of cache security group names to authorize for the clusters in this replication group. This change is asynchronously applied as soon as possible.
            This parameter can be used only with replication group containing cache clusters running outside of an Amazon Virtual Private Cloud (Amazon VPC).
            Constraints: Must contain no more than 255 alphanumeric characters. Must not be Default .
            (string) --
            

    :type SecurityGroupIds: list
    :param SecurityGroupIds: Specifies the VPC Security Groups associated with the cache clusters in the replication group.
            This parameter can be used only with replication group containing cache clusters running in an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
            Valid values for ddd are:
            sun
            mon
            tue
            wed
            thu
            fri
            sat
            Example: sun:23:00-mon:01:30
            

    :type NotificationTopicArn: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.
            Note
            The Amazon SNS topic owner must be same as the replication group owner.
            

    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: The name of the cache parameter group to apply to all of the clusters in this replication group. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for this request.

    :type NotificationTopicStatus: string
    :param NotificationTopicStatus: The status of the Amazon SNS notification topic for the replication group. Notifications are sent only if the status is active .
            Valid values: active | inactive
            

    :type ApplyImmediately: boolean
    :param ApplyImmediately: If true , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow setting for the replication group.
            If false , changes to the nodes in the replication group are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.
            Valid values: true | false
            Default: false
            

    :type EngineVersion: string
    :param EngineVersion: The upgraded version of the cache engine to be run on the cache clusters in the replication group.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing replication group and create it anew with the earlier engine version.
            

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.

    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic node group (shard) snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
            Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
            

    :type SnapshotWindow: string
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node group (shard) specified by SnapshottingClusterId .
            Example: 05:00-09:00
            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
            

    :type CacheNodeType: string
    :param CacheNodeType: A valid cache node type that you want to scale this replication group to.

    :type NodeGroupId: string
    :param NodeGroupId: The name of the Node Group (called shard in the console).

    :rtype: dict
    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled'
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
            'CacheNodeType': 'string'
        }
    }
    
    
    :returns: 
    Redis versions earlier than 2.8.6.
    Redis (cluster mode disabled):T1 and T2 cache node types. Redis (cluster mode enabled): T1 node types.
    
    """
    pass

def purchase_reserved_cache_nodes_offering(ReservedCacheNodesOfferingId=None, ReservedCacheNodeId=None, CacheNodeCount=None):
    """
    Allows you to purchase a reserved cache node offering.
    See also: AWS API Documentation
    
    
    :example: response = client.purchase_reserved_cache_nodes_offering(
        ReservedCacheNodesOfferingId='string',
        ReservedCacheNodeId='string',
        CacheNodeCount=123
    )
    
    
    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodesOfferingId: [REQUIRED]
            The ID of the reserved cache node offering to purchase.
            Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
            

    :type ReservedCacheNodeId: string
    :param ReservedCacheNodeId: A customer-specified identifier to track this reservation.
            Note
            The Reserved Cache Node ID is an unique customer-specified identifier to track this reservation. If this parameter is not specified, ElastiCache automatically generates an identifier for the reservation.
            Example: myreservationID
            

    :type CacheNodeCount: integer
    :param CacheNodeCount: The number of cache node instances to reserve.
            Default: 1
            

    :rtype: dict
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
            ]
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
    """
    pass

def reboot_cache_cluster(CacheClusterId=None, CacheNodeIdsToReboot=None):
    """
    Reboots some, or all, of the cache nodes within a provisioned cache cluster. This operation applies any modified cache parameter groups to the cache cluster. The reboot operation takes place as soon as possible, and results in a momentary outage to the cache cluster. During the reboot, the cache cluster status is set to REBOOTING.
    The reboot causes the contents of the cache (for each cache node being rebooted) to be lost.
    When the reboot is complete, a cache cluster event is created.
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_cache_cluster(
        CacheClusterId='string',
        CacheNodeIdsToReboot=[
            'string',
        ]
    )
    
    
    :type CacheClusterId: string
    :param CacheClusterId: [REQUIRED]
            The cache cluster identifier. This parameter is stored as a lowercase string.
            

    :type CacheNodeIdsToReboot: list
    :param CacheNodeIdsToReboot: [REQUIRED]
            A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cache cluster, specify all of the cache node IDs.
            (string) --
            

    :rtype: dict
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
                'CacheNodeType': 'string'
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
            'SnapshotWindow': 'string'
        }
    }
    
    
    :returns: 
    General purpose:
    Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge , cache.m4.large , cache.m4.xlarge , cache.m4.2xlarge , cache.m4.4xlarge , cache.m4.10xlarge
    Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
    
    
    Compute optimized: cache.c1.xlarge
    Memory optimized:
    Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
    Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
    
    
    
    """
    pass

def remove_tags_from_resource(ResourceName=None, TagKeys=None):
    """
    Removes the tags identified by the TagKeys list from the named resource.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags_from_resource(
        ResourceName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            A list of TagKeys identifying the tags you want removed from the named resource.
            (string) --
            

    :rtype: dict
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

def reset_cache_parameter_group(CacheParameterGroupName=None, ResetAllParameters=None, ParameterNameValues=None):
    """
    Modifies the parameters of a cache parameter group to the engine or system default value. You can reset specific parameters by submitting a list of parameter names. To reset the entire cache parameter group, specify the ResetAllParameters and CacheParameterGroupName parameters.
    See also: AWS API Documentation
    
    
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
    :param CacheParameterGroupName: [REQUIRED]
            The name of the cache parameter group to reset.
            

    :type ResetAllParameters: boolean
    :param ResetAllParameters: If true , all parameters in the cache parameter group are reset to their default values. If false , only the parameters listed by ParameterNameValues are reset to their default values.
            Valid values: true | false
            

    :type ParameterNameValues: list
    :param ParameterNameValues: An array of parameter names to reset to their default values. If ResetAllParameters is true , do not use ParameterNameValues . If ResetAllParameters is false , you must specify the name of at least one parameter to reset.
            (dict) --Describes a name-value pair that is used to update the value of a parameter.
            ParameterName (string) --The name of the parameter.
            ParameterValue (string) --The value of the parameter.
            
            

    :rtype: dict
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
    
    
    :example: response = client.revoke_cache_security_group_ingress(
        CacheSecurityGroupName='string',
        EC2SecurityGroupName='string',
        EC2SecurityGroupOwnerId='string'
    )
    
    
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: [REQUIRED]
            The name of the cache security group to revoke ingress from.
            

    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: [REQUIRED]
            The name of the Amazon EC2 security group to revoke access from.
            

    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: [REQUIRED]
            The AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.
            

    :rtype: dict
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
            ]
        }
    }
    
    
    :returns: 
    AuthorizeCacheSecurityGroupIngress
    CreateCacheSecurityGroup
    RevokeCacheSecurityGroupIngress
    
    """
    pass

def test_failover(ReplicationGroupId=None, NodeGroupId=None):
    """
    Represents the input of a TestFailover operation which test automatic failover on a specified node group (called shard in the console) in a replication group (called cluster in the console).
    For more information see:
    Also see, Testing Multi-AZ with Automatic Failover in the ElastiCache User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.test_failover(
        ReplicationGroupId='string',
        NodeGroupId='string'
    )
    
    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: [REQUIRED]
            The name of the replication group (console: cluster) whose automatic failover is being tested by this operation.
            

    :type NodeGroupId: string
    :param NodeGroupId: [REQUIRED]
            The name of the node group (called shard in the console) in this replication group on which automatic failover is to be tested. You may test automatic failover on up to 5 node groups in any rolling 24-hour period.
            

    :rtype: dict
    :return: {
        'ReplicationGroup': {
            'ReplicationGroupId': 'string',
            'Description': 'string',
            'Status': 'string',
            'PendingModifiedValues': {
                'PrimaryClusterId': 'string',
                'AutomaticFailoverStatus': 'enabled'|'disabled'
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
            'CacheNodeType': 'string'
        }
    }
    
    
    :returns: 
    Viewing ElastiCache Events in the ElastiCache User Guide
    DescribeEvents in the ElastiCache API Reference
    
    """
    pass

