"""
The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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
"""


def add_tags_to_resource(ResourceName=None, Tags=None):
    """
    :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource to which the tags are to be added, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            
    :type ResourceName: string
    :param Tags: [REQUIRED]
            A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag.
            Value (string) --The tag's value. May not be null.
            
            
    :type Tags: list
    """
    pass


def authorize_cache_security_group_ingress(CacheSecurityGroupName=None, EC2SecurityGroupName=None,
                                           EC2SecurityGroupOwnerId=None):
    """
    :param CacheSecurityGroupName: [REQUIRED]
            The cache security group that allows network ingress.
            
    :type CacheSecurityGroupName: string
    :param EC2SecurityGroupName: [REQUIRED]
            The Amazon EC2 security group to be authorized for ingress to the cache security group.
            
    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupOwnerId: [REQUIRED]
            The AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.
            
    :type EC2SecurityGroupOwnerId: string
    """
    pass


def can_paginate(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
    :type operation_name: string
    """
    pass


def copy_snapshot(SourceSnapshotName=None, TargetSnapshotName=None, TargetBucket=None):
    """
    :param SourceSnapshotName: [REQUIRED]
            The name of an existing snapshot from which to make a copy.
            
    :type SourceSnapshotName: string
    :param TargetSnapshotName: [REQUIRED]
            A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting.
            
    :type TargetSnapshotName: string
    :param TargetBucket: The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access.
            When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket in the Amazon ElastiCache User Guide .
            For more information, see Exporting a Snapshot in the Amazon ElastiCache User Guide .
            
    :type TargetBucket: string
    """
    pass


def create_cache_cluster(CacheClusterId=None, ReplicationGroupId=None, AZMode=None, PreferredAvailabilityZone=None,
                         PreferredAvailabilityZones=None, NumCacheNodes=None, CacheNodeType=None, Engine=None,
                         EngineVersion=None, CacheParameterGroupName=None, CacheSubnetGroupName=None,
                         CacheSecurityGroupNames=None, SecurityGroupIds=None, Tags=None, SnapshotArns=None,
                         SnapshotName=None, PreferredMaintenanceWindow=None, Port=None, NotificationTopicArn=None,
                         AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None):
    """
    :param CacheClusterId: [REQUIRED]
            The node group (shard) identifier. This parameter is stored as a lowercase string.
            Constraints:
            A name must contain from 1 to 20 alphanumeric characters or hyphens.
            The first character must be a letter.
            A name cannot end with a hyphen or contain two consecutive hyphens.
            
    :type CacheClusterId: string
    :param ReplicationGroupId: 
            Warning
            Due to current limitations on Redis (cluster mode disabled), this operation or parameter is not supported on Redis (cluster mode enabled) replication groups.
            The ID of the replication group to which this cache cluster should belong. If this parameter is specified, the cache cluster is added to the specified replication group as a read replica; otherwise, the cache cluster is a standalone primary that is not part of any replication group.
            If the specified replication group is Multi-AZ enabled and the Availability Zone is not specified, the cache cluster is created in Availability Zones that provide the best spread of read replicas across Availability Zones.
            Note
            This parameter is only valid if the Engine parameter is redis .
            
    :type ReplicationGroupId: string
    :param AZMode: Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region.
            This parameter is only supported for Memcached cache clusters.
            If the AZMode and PreferredAvailabilityZones are not specified, ElastiCache assumes single-az mode.
            
    :type AZMode: string
    :param PreferredAvailabilityZone: The EC2 Availability Zone in which the cache cluster is created.
            All nodes belonging to this Memcached cache cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use PreferredAvailabilityZones .
            Default: System chosen Availability Zone.
            
    :type PreferredAvailabilityZone: string
    :param PreferredAvailabilityZones: A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important.
            This option is only supported on Memcached.
            Note
            If you are creating your cache cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.
            The number of Availability Zones listed must equal the value of NumCacheNodes .
            If you want all the nodes in the same Availability Zone, use PreferredAvailabilityZone instead, or repeat the Availability Zone multiple times in the list.
            Default: System chosen Availability Zones.
            (string) --
            
    :type PreferredAvailabilityZones: list
    :param NumCacheNodes: The initial number of cache nodes that the cache cluster has.
            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
            If you need more than 20 nodes for your Memcached cluster, please fill out the ElastiCache Limit Increase Request form at http://aws.amazon.com/contact-us/elasticache-node-limit-request/ .
            
    :type NumCacheNodes: integer
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
            
    :type CacheNodeType: string
    :param Engine: The name of the cache engine to be used for this cache cluster.
            Valid values for this parameter are: memcached | redis
            
    :type Engine: string
    :param EngineVersion: The version number of the cache engine to be used for this cache cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cache cluster or replication group and create it anew with the earlier engine version.
            
    :type EngineVersion: string
    :param CacheParameterGroupName: The name of the parameter group to associate with this cache cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has cluster-enabled='yes' when creating a cluster.
    :type CacheParameterGroupName: string
    :param CacheSubnetGroupName: The name of the subnet group to be used for the cache cluster.
            Use this parameter only when you are creating a cache cluster in an Amazon Virtual Private Cloud (Amazon VPC).
            Warning
            If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see Subnets and Subnet Groups .
            
    :type CacheSubnetGroupName: string
    :param CacheSecurityGroupNames: A list of security group names to associate with this cache cluster.
            Use this parameter only when you are creating a cache cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            
    :type CacheSecurityGroupNames: list
    :param SecurityGroupIds: One or more VPC security groups associated with the cache cluster.
            Use this parameter only when you are creating a cache cluster in an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            
    :type SecurityGroupIds: list
    :param Tags: A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag.
            Value (string) --The tag's value. May not be null.
            
            
    :type Tags: list
    :param SnapshotArns: A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Example of an Amazon S3 ARN: arn:aws:s3:::my_bucket/snapshot1.rdb
            (string) --
            
    :type SnapshotArns: list
    :param SnapshotName: The name of a Redis snapshot from which to restore data into the new node group (shard). The snapshot status changes to restoring while the new node group (shard) is being created.
            Note
            This parameter is only valid if the Engine parameter is redis .
            
    :type SnapshotName: string
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
            
    :type PreferredMaintenanceWindow: string
    :param Port: The port number on which each of the cache nodes accepts connections.
    :type Port: integer
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.
            Note
            The Amazon SNS topic owner must be the same as the cache cluster owner.
            
    :type NotificationTopicArn: string
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.
    :type AutoMinorVersionUpgrade: boolean
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot taken today is retained for 5 days before being deleted.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Default: 0 (i.e., automatic backups are disabled for this cache cluster).
            
    :type SnapshotRetentionLimit: integer
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
            Example: 05:00-09:00
            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
            Note: This parameter is only valid if the Engine parameter is redis .
            
    :type SnapshotWindow: string
    """
    pass


def create_cache_parameter_group(CacheParameterGroupName=None, CacheParameterGroupFamily=None, Description=None):
    """
    :param CacheParameterGroupName: [REQUIRED]
            A user-specified name for the cache parameter group.
            
    :type CacheParameterGroupName: string
    :param CacheParameterGroupFamily: [REQUIRED]
            The name of the cache parameter group family that the cache parameter group can be used with.
            Valid values are: memcached1.4 | redis2.6 | redis2.8 | redis3.2
            
    :type CacheParameterGroupFamily: string
    :param Description: [REQUIRED]
            A user-specified description for the cache parameter group.
            
    :type Description: string
    """
    pass


def create_cache_security_group(CacheSecurityGroupName=None, Description=None):
    """
    :param CacheSecurityGroupName: [REQUIRED]
            A name for the cache security group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters. Cannot be the word 'Default'.
            Example: mysecuritygroup
            
    :type CacheSecurityGroupName: string
    :param Description: [REQUIRED]
            A description for the cache security group.
            
    :type Description: string
    """
    pass


def create_cache_subnet_group(CacheSubnetGroupName=None, CacheSubnetGroupDescription=None, SubnetIds=None):
    """
    :param CacheSubnetGroupName: [REQUIRED]
            A name for the cache subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
            Example: mysubnetgroup
            
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupDescription: [REQUIRED]
            A description for the cache subnet group.
            
    :type CacheSubnetGroupDescription: string
    :param SubnetIds: [REQUIRED]
            A list of VPC subnet IDs for the cache subnet group.
            (string) --
            
    :type SubnetIds: list
    """
    pass


def create_replication_group(ReplicationGroupId=None, ReplicationGroupDescription=None, PrimaryClusterId=None,
                             AutomaticFailoverEnabled=None, NumCacheClusters=None, PreferredCacheClusterAZs=None,
                             NumNodeGroups=None, ReplicasPerNodeGroup=None, NodeGroupConfiguration=None,
                             CacheNodeType=None, Engine=None, EngineVersion=None, CacheParameterGroupName=None,
                             CacheSubnetGroupName=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, Tags=None,
                             SnapshotArns=None, SnapshotName=None, PreferredMaintenanceWindow=None, Port=None,
                             NotificationTopicArn=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None,
                             SnapshotWindow=None):
    """
    :param ReplicationGroupId: [REQUIRED]
            The replication group identifier. This parameter is stored as a lowercase string.
            Constraints:
            A name must contain from 1 to 20 alphanumeric characters or hyphens.
            The first character must be a letter.
            A name cannot end with a hyphen or contain two consecutive hyphens.
            
    :type ReplicationGroupId: string
    :param ReplicationGroupDescription: [REQUIRED]
            A user-created description for the replication group.
            
    :type ReplicationGroupDescription: string
    :param PrimaryClusterId: The identifier of the cache cluster that serves as the primary for this replication group. This cache cluster must already exist and have a status of available .
            This parameter is not required if NumCacheClusters , NumNodeGroups , or ReplicasPerNodeGroup is specified.
            
    :type PrimaryClusterId: string
    :param AutomaticFailoverEnabled: Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.
            If true , Multi-AZ is enabled for this replication group. If false , Multi-AZ is disabled for this replication group.
            AutomaticFailoverEnabled must be enabled for Redis (cluster mode enabled) replication groups.
            Default: false
            Note
            ElastiCache Multi-AZ replication groups is not supported on:
            Redis versions earlier than 2.8.6.
            Redis (cluster mode disabled): T1 and T2 node types. Redis (cluster mode enabled): T2 node types.
            
    :type AutomaticFailoverEnabled: boolean
    :param NumCacheClusters: The number of clusters this replication group initially has.
            This parameter is not used if there is more than one node group (shard). You should use ReplicasPerNodeGroup instead.
            If Multi-AZ is enabled , the value of this parameter must be at least 2.
            The maximum permitted value for NumCacheClusters is 6 (primary plus 5 replicas). If you need to exceed this limit, fill out the ElastiCache Limit Increase Request form at http://aws.amazon.com/contact-us/elasticache-node-limit-request/ .
            
    :type NumCacheClusters: integer
    :param PreferredCacheClusterAZs: A list of EC2 Availability Zones in which the replication group's cache clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list.
            This parameter is not used if there is more than one node group (shard). You should use NodeGroupConfiguration instead.
            Note
            If you are creating your replication group in an Amazon VPC (recommended), you can only locate cache clusters in Availability Zones associated with the subnets in the selected subnet group.
            The number of Availability Zones listed must equal the value of NumCacheClusters .
            Default: system chosen Availability Zones.
            (string) --
            
    :type PreferredCacheClusterAZs: list
    :param NumNodeGroups: An optional parameter that specifies the number of node groups (shards) for this Redis (cluster mode enabled) replication group. For Redis (cluster mode disabled) either omit this parameter or set it to 1.
            Default: 1
            
    :type NumNodeGroups: integer
    :param ReplicasPerNodeGroup: An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.
    :type ReplicasPerNodeGroup: integer
    :param NodeGroupConfiguration: A list of node group (shard) configuration options. Each node group (shard) configuration has the following: Slots, PrimaryAvailabilityZone, ReplicaAvailabilityZones, ReplicaCount.
            If you're creating a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication group, you can use this parameter to configure one node group (shard) or you can omit this parameter.
            (dict) --node group (shard) configuration options. Each node group (shard) configuration has the following: Slots , PrimaryAvailabilityZone , ReplicaAvailabilityZones , ReplicaCount .
            Slots (string) --A string that specifies the keyspaces as a series of comma separated values. Keyspaces are 0 to 16,383. The string is in the format startkey-endkey .
            Example: '0-3999'
            ReplicaCount (integer) --The number of read replica nodes in this node group (shard).
            PrimaryAvailabilityZone (string) --The Availability Zone where the primary node of this node group (shard) is launched.
            ReplicaAvailabilityZones (list) --A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ReplicaCount or ReplicasPerNodeGroup if not specified.
            (string) --
            
            
    :type NodeGroupConfiguration: list
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
            
    :type CacheNodeType: string
    :param Engine: The name of the cache engine to be used for the cache clusters in this replication group.
    :type Engine: string
    :param EngineVersion: The version number of the cache engine to be used for the cache clusters in this replication group. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ) in the ElastiCache User Guide , but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cache cluster or replication group and create it anew with the earlier engine version.
            
    :type EngineVersion: string
    :param CacheParameterGroupName: The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
            If you are running Redis version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name.
            To create a Redis (cluster mode disabled) replication group, use CacheParameterGroupName=default.redis3.2 .
            To create a Redis (cluster mode enabled) replication group, use CacheParameterGroupName=default.redis3.2.cluster.on .
            
    :type CacheParameterGroupName: string
    :param CacheSubnetGroupName: The name of the cache subnet group to be used for the replication group.
            Warning
            If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see Subnets and Subnet Groups .
            
    :type CacheSubnetGroupName: string
    :param CacheSecurityGroupNames: A list of cache security group names to associate with this replication group.
            (string) --
            
    :type CacheSecurityGroupNames: list
    :param SecurityGroupIds: One or more Amazon VPC security groups associated with this replication group.
            Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            
    :type SecurityGroupIds: list
    :param Tags: A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag.
            Value (string) --The tag's value. May not be null.
            
            
    :type Tags: list
    :param SnapshotArns: A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the replication group. The Amazon S3 object name in the ARN cannot contain any commas. The list must match the number of node groups (shards) in the replication group, which means you cannot repartition.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Example of an Amazon S3 ARN: arn:aws:s3:::my_bucket/snapshot1.rdb
            (string) --
            
    :type SnapshotArns: list
    :param SnapshotName: The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to restoring while the new replication group is being created.
            Note
            This parameter is only valid if the Engine parameter is redis .
            
    :type SnapshotName: string
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
            
    :type PreferredMaintenanceWindow: string
    :param Port: The port number on which each member of the replication group accepts connections.
    :type Port: integer
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.
            Note
            The Amazon SNS topic owner must be the same as the cache cluster owner.
            
    :type NotificationTopicArn: string
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.
    :type AutoMinorVersionUpgrade: boolean
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Default: 0 (i.e., automatic backups are disabled for this cache cluster).
            
    :type SnapshotRetentionLimit: integer
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
            Example: 05:00-09:00
            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
            Note
            This parameter is only valid if the Engine parameter is redis .
            
    :type SnapshotWindow: string
    """
    pass


def create_snapshot(ReplicationGroupId=None, CacheClusterId=None, SnapshotName=None):
    """
    :param ReplicationGroupId: The identifier of an existing replication group. The snapshot is created from this replication group.
    :type ReplicationGroupId: string
    :param CacheClusterId: The identifier of an existing cache cluster. The snapshot is created from this cache cluster.
    :type CacheClusterId: string
    :param SnapshotName: [REQUIRED]
            A name for the snapshot being created.
            
    :type SnapshotName: string
    """
    pass


def delete_cache_cluster(CacheClusterId=None, FinalSnapshotIdentifier=None):
    """
    :param CacheClusterId: [REQUIRED]
            The cache cluster identifier for the cluster to be deleted. This parameter is not case sensitive.
            
    :type CacheClusterId: string
    :param FinalSnapshotIdentifier: The user-supplied name of a final cache cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cache cluster immediately afterward.
    :type FinalSnapshotIdentifier: string
    """
    pass


def delete_cache_parameter_group(CacheParameterGroupName=None):
    """
    :param CacheParameterGroupName: [REQUIRED]
            The name of the cache parameter group to delete.
            Note
            The specified cache security group must not be associated with any cache clusters.
            ReturnsNone
            
    :type CacheParameterGroupName: string
    """
    pass


def delete_cache_security_group(CacheSecurityGroupName=None):
    """
    :param CacheSecurityGroupName: [REQUIRED]
            The name of the cache security group to delete.
            Note
            You cannot delete the default security group.
            ReturnsNone
            
    :type CacheSecurityGroupName: string
    """
    pass


def delete_cache_subnet_group(CacheSubnetGroupName=None):
    """
    :param CacheSubnetGroupName: [REQUIRED]
            The name of the cache subnet group to delete.
            Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
            ReturnsNone
            
    :type CacheSubnetGroupName: string
    """
    pass


def delete_replication_group(ReplicationGroupId=None, RetainPrimaryCluster=None, FinalSnapshotIdentifier=None):
    """
    :param ReplicationGroupId: [REQUIRED]
            The identifier for the cluster to be deleted. This parameter is not case sensitive.
            
    :type ReplicationGroupId: string
    :param RetainPrimaryCluster: If set to true , all of the read replicas are deleted, but the primary node is retained.
    :type RetainPrimaryCluster: boolean
    :param FinalSnapshotIdentifier: The name of a final node group (shard) snapshot. ElastiCache creates the snapshot from the primary node in the cluster, rather than one of the replicas; this is to ensure that it captures the freshest data. After the final snapshot is taken, the replication group is immediately deleted.
    :type FinalSnapshotIdentifier: string
    """
    pass


def delete_snapshot(SnapshotName=None):
    """
    :param SnapshotName: [REQUIRED]
            The name of the snapshot to be deleted.
            Return typedict
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
            Response Structure
            (dict) --
            Snapshot (dict) --Represents a copy of an entire Redis cache cluster as of the time when the snapshot was taken.
            SnapshotName (string) --The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.
            ReplicationGroupId (string) --The unique identifier of the source replication group.
            ReplicationGroupDescription (string) --A description of the source replication group.
            CacheClusterId (string) --The user-supplied identifier of the source cache cluster.
            SnapshotStatus (string) --The status of the snapshot. Valid values: creating | available | restoring | copying | deleting .
            SnapshotSource (string) --Indicates whether the snapshot is from an automatic backup (automated ) or was created manually (manual ).
            CacheNodeType (string) --The name of the compute and memory capacity node type for the source cache cluster.
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
            Engine (string) --The name of the cache engine (memcached or redis ) used by the source cache cluster.
            EngineVersion (string) --The version of the cache engine version that is used by the source cache cluster.
            NumCacheNodes (integer) --The number of cache nodes in the source cache cluster.
            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
            PreferredAvailabilityZone (string) --The name of the Availability Zone in which the source cache cluster is located.
            CacheClusterCreateTime (datetime) --The date and time when the source cache cluster was created.
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
            TopicArn (string) --The Amazon Resource Name (ARN) for the topic used by the source cache cluster for publishing notifications.
            Port (integer) --The port number used by each cache nodes in the source cache cluster.
            CacheParameterGroupName (string) --The cache parameter group that is associated with the source cache cluster.
            CacheSubnetGroupName (string) --The name of the cache subnet group associated with the source cache cluster.
            VpcId (string) --The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cache cluster.
            AutoMinorVersionUpgrade (boolean) --This parameter is currently disabled.
            SnapshotRetentionLimit (integer) --For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.
            For manual snapshots, this field reflects the SnapshotRetentionLimit for the source cache cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the DeleteSnapshot operation.
            Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
            SnapshotWindow (string) --The daily time range during which ElastiCache takes daily snapshots of the source cache cluster.
            NumNodeGroups (integer) --The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.
            AutomaticFailover (string) --Indicates the status of Multi-AZ for the source replication group.
            Note
            ElastiCache Multi-AZ replication groups are not supported on:
            Redis versions earlier than 2.8.6.
            Redis (cluster mode disabled):T1 and T2 cache node types. Redis (cluster mode enabled): T1 node types.
            NodeSnapshots (list) --A list of the cache nodes in the source cache cluster.
            (dict) --Represents an individual cache node in a snapshot of a cache cluster.
            CacheClusterId (string) --A unique identifier for the source cache cluster.
            NodeGroupId (string) --A unique identifier for the source node group (shard).
            CacheNodeId (string) --The cache node identifier for the node in the source cache cluster.
            NodeGroupConfiguration (dict) --The configuration for the source node group (shard).
            Slots (string) --A string that specifies the keyspaces as a series of comma separated values. Keyspaces are 0 to 16,383. The string is in the format startkey-endkey .
            Example: '0-3999'
            ReplicaCount (integer) --The number of read replica nodes in this node group (shard).
            PrimaryAvailabilityZone (string) --The Availability Zone where the primary node of this node group (shard) is launched.
            ReplicaAvailabilityZones (list) --A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ReplicaCount or ReplicasPerNodeGroup if not specified.
            (string) --
            
            CacheSize (string) --The size of the cache on the source cache node.
            CacheNodeCreateTime (datetime) --The date and time when the cache node was created in the source cache cluster.
            SnapshotCreateTime (datetime) --The date and time when the source node's metadata and cache data set was obtained for the snapshot.
            
            
            
            
    :type SnapshotName: string
    """
    pass


def describe_cache_clusters(CacheClusterId=None, MaxRecords=None, Marker=None, ShowCacheNodeInfo=None):
    """
    :param CacheClusterId: The user-supplied cluster identifier. If this parameter is specified, only information about that specific cache cluster is returned. This parameter isn't case sensitive.
    :type CacheClusterId: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    :param ShowCacheNodeInfo: An optional flag that can be included in the DescribeCacheCluster request to retrieve information about the individual cache nodes.
    :type ShowCacheNodeInfo: boolean
    """
    pass


def describe_cache_engine_versions(Engine=None, EngineVersion=None, CacheParameterGroupFamily=None, MaxRecords=None,
                                   Marker=None, DefaultOnly=None):
    """
    :param Engine: The cache engine to return. Valid values: memcached | redis
    :type Engine: string
    :param EngineVersion: The cache engine version to return.
            Example: 1.4.14
            
    :type EngineVersion: string
    :param CacheParameterGroupFamily: The name of a specific cache parameter group family to return details for.
            Valid values are: memcached1.4 | redis2.6 | redis2.8 | redis3.2
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type CacheParameterGroupFamily: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    :param DefaultOnly: If true , specifies that only the default version of the specified engine or engine and major version combination is to be returned.
    :type DefaultOnly: boolean
    """
    pass


def describe_cache_parameter_groups(CacheParameterGroupName=None, MaxRecords=None, Marker=None):
    """
    :param CacheParameterGroupName: The name of a specific cache parameter group to return details for.
    :type CacheParameterGroupName: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_cache_parameters(CacheParameterGroupName=None, Source=None, MaxRecords=None, Marker=None):
    """
    :param CacheParameterGroupName: [REQUIRED]
            The name of a specific cache parameter group to return details for.
            
    :type CacheParameterGroupName: string
    :param Source: The parameter types to return.
            Valid values: user | system | engine-default
            
    :type Source: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_cache_security_groups(CacheSecurityGroupName=None, MaxRecords=None, Marker=None):
    """
    :param CacheSecurityGroupName: The name of the cache security group to return details for.
    :type CacheSecurityGroupName: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_cache_subnet_groups(CacheSubnetGroupName=None, MaxRecords=None, Marker=None):
    """
    :param CacheSubnetGroupName: The name of the cache subnet group to return details for.
    :type CacheSubnetGroupName: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_engine_default_parameters(CacheParameterGroupFamily=None, MaxRecords=None, Marker=None):
    """
    :param CacheParameterGroupFamily: [REQUIRED]
            The name of the cache parameter group family.
            Valid values are: memcached1.4 | redis2.6 | redis2.8 | redis3.2
            
    :type CacheParameterGroupFamily: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None,
                    MaxRecords=None, Marker=None):
    """
    :param SourceIdentifier: The identifier of the event source for which events are returned. If not specified, all sources are included in the response.
    :type SourceIdentifier: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.
    :type SourceType: string
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format.
    :type StartTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format.
    :type EndTime: datetime
    :param Duration: The number of minutes' worth of events to retrieve.
    :type Duration: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_replication_groups(ReplicationGroupId=None, MaxRecords=None, Marker=None):
    """
    :param ReplicationGroupId: The identifier for the replication group to be described. This parameter is not case sensitive.
            If you do not specify this parameter, information about all replication groups is returned.
            
    :type ReplicationGroupId: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_reserved_cache_nodes(ReservedCacheNodeId=None, ReservedCacheNodesOfferingId=None, CacheNodeType=None,
                                  Duration=None, ProductDescription=None, OfferingType=None, MaxRecords=None,
                                  Marker=None):
    """
    :param ReservedCacheNodeId: The reserved cache node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.
    :type ReservedCacheNodeId: string
    :param ReservedCacheNodesOfferingId: The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.
    :type ReservedCacheNodesOfferingId: string
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
            
    :type CacheNodeType: string
    :param Duration: The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.
            Valid Values: 1 | 3 | 31536000 | 94608000
            
    :type Duration: string
    :param ProductDescription: The product description filter value. Use this parameter to show only those reservations matching the specified product description.
    :type ProductDescription: string
    :param OfferingType: The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.
            Valid values: 'Light Utilization'|'Medium Utilization'|'Heavy Utilization'
            
    :type OfferingType: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_reserved_cache_nodes_offerings(ReservedCacheNodesOfferingId=None, CacheNodeType=None, Duration=None,
                                            ProductDescription=None, OfferingType=None, MaxRecords=None, Marker=None):
    """
    :param ReservedCacheNodesOfferingId: The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.
            Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
            
    :type ReservedCacheNodesOfferingId: string
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
            
    :type CacheNodeType: string
    :param Duration: Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.
            Valid Values: 1 | 3 | 31536000 | 94608000
            
    :type Duration: string
    :param ProductDescription: The product description filter value. Use this parameter to show only the available offerings matching the specified product description.
    :type ProductDescription: string
    :param OfferingType: The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.
            Valid Values: 'Light Utilization'|'Medium Utilization'|'Heavy Utilization'
            
    :type OfferingType: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_snapshots(ReplicationGroupId=None, CacheClusterId=None, SnapshotName=None, SnapshotSource=None,
                       Marker=None, MaxRecords=None, ShowNodeGroupConfig=None):
    """
    :param ReplicationGroupId: A user-supplied replication group identifier. If this parameter is specified, only snapshots associated with that specific replication group are described.
    :type ReplicationGroupId: string
    :param CacheClusterId: A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cache cluster are described.
    :type CacheClusterId: string
    :param SnapshotName: A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described.
    :type SnapshotName: string
    :param SnapshotSource: If set to system , the output shows snapshots that were automatically created by ElastiCache. If set to user the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.
    :type SnapshotSource: string
    :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 50
            Constraints: minimum 20; maximum 50.
            
    :type MaxRecords: integer
    :param ShowNodeGroupConfig: A boolean value which if true, the node group (shard) configuration is included in the snapshot description.
    :type ShowNodeGroupConfig: boolean
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    :param ClientMethod: The client method to presign for
    :type ClientMethod: string
    :param Params: The parameters normally passed to
            ClientMethod.
    :type Params: dict
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
    :type ExpiresIn: int
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
    :type HttpMethod: string
    """
    pass


def get_paginator(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
    :type operation_name: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_allowed_node_type_modifications(CacheClusterId=None, ReplicationGroupId=None):
    """
    :param CacheClusterId: The name of the cache cluster you want to scale up to a larger node instanced type. ElastiCache uses the cluster id to identify the current node type of this cluster and from that to create a list of node types you can scale up to.
            Warning
            You must provide a value for either the CacheClusterId or the ReplicationGroupId .
            
    :type CacheClusterId: string
    :param ReplicationGroupId: The name of the replication group want to scale up to a larger node type. ElastiCache uses the replication group id to identify the current node type being used by this replication group, and from that to create a list of node types you can scale up to.
            Warning
            You must provide a value for either the CacheClusterId or the ReplicationGroupId .
            
    :type ReplicationGroupId: string
    """
    pass


def list_tags_for_resource(ResourceName=None):
    """
    :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource for which you want the list of tags, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            Return typedict
            ReturnsResponse Syntax{
              'TagList': [
                {
                  'Key': 'string',
                  'Value': 'string'
                },
              ]
            }
            Response Structure
            (dict) --Represents the output from the AddTagsToResource , ListTagsOnResource , and RemoveTagsFromResource operations.
            TagList (list) --A list of cost allocation tags as key-value pairs.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag.
            Value (string) --The tag's value. May not be null.
            
            
            
    :type ResourceName: string
    """
    pass


def modify_cache_cluster(CacheClusterId=None, NumCacheNodes=None, CacheNodeIdsToRemove=None, AZMode=None,
                         NewAvailabilityZones=None, CacheSecurityGroupNames=None, SecurityGroupIds=None,
                         PreferredMaintenanceWindow=None, NotificationTopicArn=None, CacheParameterGroupName=None,
                         NotificationTopicStatus=None, ApplyImmediately=None, EngineVersion=None,
                         AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None,
                         CacheNodeType=None):
    """
    :param CacheClusterId: [REQUIRED]
            The cache cluster identifier. This value is stored as a lowercase string.
            
    :type CacheClusterId: string
    :param NumCacheNodes: The number of cache nodes that the cache cluster should have. If the value for NumCacheNodes is greater than the sum of the number of current cache nodes and the number of cache nodes pending creation (which may be zero), more nodes are added. If the value is less than the number of existing cache nodes, nodes are removed. If the value is equal to the number of current cache nodes, any pending add or remove requests are canceled.
            If you are removing cache nodes, you must use the CacheNodeIdsToRemove parameter to provide the IDs of the specific cache nodes to remove.
            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
            Note
            Adding or removing Memcached cache nodes can be applied immediately or as a pending operation (see ApplyImmediately ).
            A pending operation to modify the number of cache nodes in a cluster during its maintenance window, whether by adding or removing nodes in accordance with the scale out architecture, is not queued. The customer's latest request to add or remove nodes to the cluster overrides any previous pending operations to modify the number of cache nodes in the cluster. For example, a request to remove 2 nodes would override a previous pending operation to remove 3 nodes. Similarly, a request to add 2 nodes would override a previous pending operation to remove 3 nodes and vice versa. As Memcached cache nodes may now be provisioned in different Availability Zones with flexible cache node placement, a request to add nodes does not automatically override a previous pending operation to add nodes. The customer can modify the previous pending operation to add more nodes or explicitly cancel the pending request and retry the new request. To cancel pending operations to modify the number of cache nodes in a cluster, use the ModifyCacheCluster request and set NumCacheNodes equal to the number of cache nodes currently in the cache cluster.
            
    :type NumCacheNodes: integer
    :param CacheNodeIdsToRemove: A list of cache node IDs to be removed. A node ID is a numeric identifier (0001, 0002, etc.). This parameter is only valid when NumCacheNodes is less than the existing number of cache nodes. The number of cache node IDs supplied in this parameter must match the difference between the existing number of cache nodes in the cluster or pending cache nodes, whichever is greater, and the value of NumCacheNodes in the request.
            For example: If you have 3 active cache nodes, 7 pending cache nodes, and the number of cache nodes in this ModifyCacheCluser call is 5, you must list 2 (7 - 5) cache node IDs to remove.
            (string) --
            
    :type CacheNodeIdsToRemove: list
    :param AZMode: Specifies whether the new nodes in this Memcached cache cluster are all created in a single Availability Zone or created across multiple Availability Zones.
            Valid values: single-az | cross-az .
            This option is only supported for Memcached cache clusters.
            Note
            You cannot specify single-az if the Memcached cache cluster already has cache nodes in different Availability Zones. If cross-az is specified, existing Memcached nodes remain in their current Availability Zone.
            Only newly created nodes are located in different Availability Zones. For instructions on how to move existing Memcached nodes to different Availability Zones, see the Availability Zone Considerations section of Cache Node Considerations for Memcached .
            
    :type AZMode: string
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
            
    :type NewAvailabilityZones: list
    :param CacheSecurityGroupNames: A list of cache security group names to authorize on this cache cluster. This change is asynchronously applied as soon as possible.
            You can use this parameter only with clusters that are created outside of an Amazon Virtual Private Cloud (Amazon VPC).
            Constraints: Must contain no more than 255 alphanumeric characters. Must not be 'Default'.
            (string) --
            
    :type CacheSecurityGroupNames: list
    :param SecurityGroupIds: Specifies the VPC Security Groups associated with the cache cluster.
            This parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            
    :type SecurityGroupIds: list
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
            
    :type PreferredMaintenanceWindow: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.
            Note
            The Amazon SNS topic owner must be same as the cache cluster owner.
            
    :type NotificationTopicArn: string
    :param CacheParameterGroupName: The name of the cache parameter group to apply to this cache cluster. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for this request.
    :type CacheParameterGroupName: string
    :param NotificationTopicStatus: The status of the Amazon SNS notification topic. Notifications are sent only if the status is active .
            Valid values: active | inactive
            
    :type NotificationTopicStatus: string
    :param ApplyImmediately: If true , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow setting for the cache cluster.
            If false , changes to the cache cluster are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.
            Warning
            If you perform a ModifyCacheCluster before a pending modification is applied, the pending modification is replaced by the newer modification.
            Valid values: true | false
            Default: false
            
    :type ApplyImmediately: boolean
    :param EngineVersion: The upgraded version of the cache engine to be run on the cache nodes.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cache cluster and create it anew with the earlier engine version.
            
    :type EngineVersion: string
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.
    :type AutoMinorVersionUpgrade: boolean
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic cache cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
            Note
            If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
            
    :type SnapshotRetentionLimit: integer
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cache cluster.
    :type SnapshotWindow: string
    :param CacheNodeType: A valid cache node type that you want to scale this cache cluster up to.
    :type CacheNodeType: string
    """
    pass


def modify_cache_parameter_group(CacheParameterGroupName=None, ParameterNameValues=None):
    """
    :param CacheParameterGroupName: [REQUIRED]
            The name of the cache parameter group to modify.
            
    :type CacheParameterGroupName: string
    :param ParameterNameValues: [REQUIRED]
            An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be modified per request.
            (dict) --Describes a name-value pair that is used to update the value of a parameter.
            ParameterName (string) --The name of the parameter.
            ParameterValue (string) --The value of the parameter.
            
            
    :type ParameterNameValues: list
    """
    pass


def modify_cache_subnet_group(CacheSubnetGroupName=None, CacheSubnetGroupDescription=None, SubnetIds=None):
    """
    :param CacheSubnetGroupName: [REQUIRED]
            The name for the cache subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
            Example: mysubnetgroup
            
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupDescription: A description of the cache subnet group.
    :type CacheSubnetGroupDescription: string
    :param SubnetIds: The EC2 subnet IDs for the cache subnet group.
            (string) --
            
    :type SubnetIds: list
    """
    pass


def modify_replication_group(ReplicationGroupId=None, ReplicationGroupDescription=None, PrimaryClusterId=None,
                             SnapshottingClusterId=None, AutomaticFailoverEnabled=None, CacheSecurityGroupNames=None,
                             SecurityGroupIds=None, PreferredMaintenanceWindow=None, NotificationTopicArn=None,
                             CacheParameterGroupName=None, NotificationTopicStatus=None, ApplyImmediately=None,
                             EngineVersion=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None,
                             SnapshotWindow=None, CacheNodeType=None):
    """
    :param ReplicationGroupId: [REQUIRED]
            The identifier of the replication group to modify.
            
    :type ReplicationGroupId: string
    :param ReplicationGroupDescription: A description for the replication group. Maximum length is 255 characters.
    :type ReplicationGroupDescription: string
    :param PrimaryClusterId: For replication groups with a single primary, if this parameter is specified, ElastiCache promotes the specified cluster in the specified replication group to the primary role. The nodes of all other clusters in the replication group are read replicas.
    :type PrimaryClusterId: string
    :param SnapshottingClusterId: The cache cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Redis (cluster mode enabled) replication groups.
    :type SnapshottingClusterId: string
    :param AutomaticFailoverEnabled: Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure.
            Valid values: true | false
            Note
            ElastiCache Multi-AZ replication groups are not supported on:
            Redis versions earlier than 2.8.6.
            Redis (cluster mode disabled):T1 and T2 cache node types. Redis (cluster mode enabled): T1 node types.
            
    :type AutomaticFailoverEnabled: boolean
    :param CacheSecurityGroupNames: A list of cache security group names to authorize for the clusters in this replication group. This change is asynchronously applied as soon as possible.
            This parameter can be used only with replication group containing cache clusters running outside of an Amazon Virtual Private Cloud (Amazon VPC).
            Constraints: Must contain no more than 255 alphanumeric characters. Must not be Default .
            (string) --
            
    :type CacheSecurityGroupNames: list
    :param SecurityGroupIds: Specifies the VPC Security Groups associated with the cache clusters in the replication group.
            This parameter can be used only with replication group containing cache clusters running in an Amazon Virtual Private Cloud (Amazon VPC).
            (string) --
            
    :type SecurityGroupIds: list
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
            
    :type PreferredMaintenanceWindow: string
    :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.
            Note
            The Amazon SNS topic owner must be same as the replication group owner.
            
    :type NotificationTopicArn: string
    :param CacheParameterGroupName: The name of the cache parameter group to apply to all of the clusters in this replication group. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for this request.
    :type CacheParameterGroupName: string
    :param NotificationTopicStatus: The status of the Amazon SNS notification topic for the replication group. Notifications are sent only if the status is active .
            Valid values: active | inactive
            
    :type NotificationTopicStatus: string
    :param ApplyImmediately: If true , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow setting for the replication group.
            If false , changes to the nodes in the replication group are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.
            Valid values: true | false
            Default: false
            
    :type ApplyImmediately: boolean
    :param EngineVersion: The upgraded version of the cache engine to be run on the cache clusters in the replication group.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing replication group and create it anew with the earlier engine version.
            
    :type EngineVersion: string
    :param AutoMinorVersionUpgrade: This parameter is currently disabled.
    :type AutoMinorVersionUpgrade: boolean
    :param SnapshotRetentionLimit: The number of days for which ElastiCache retains automatic node group (shard) snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
            Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
            
    :type SnapshotRetentionLimit: integer
    :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node group (shard) specified by SnapshottingClusterId .
            Example: 05:00-09:00
            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
            
    :type SnapshotWindow: string
    :param CacheNodeType: A valid cache node type that you want to scale this replication group to.
    :type CacheNodeType: string
    """
    pass


def purchase_reserved_cache_nodes_offering(ReservedCacheNodesOfferingId=None, ReservedCacheNodeId=None,
                                           CacheNodeCount=None):
    """
    :param ReservedCacheNodesOfferingId: [REQUIRED]
            The ID of the reserved cache node offering to purchase.
            Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
            
    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodeId: A customer-specified identifier to track this reservation.
            Note
            The Reserved Cache Node ID is an unique customer-specified identifier to track this reservation. If this parameter is not specified, ElastiCache automatically generates an identifier for the reservation.
            Example: myreservationID
            
    :type ReservedCacheNodeId: string
    :param CacheNodeCount: The number of cache node instances to reserve.
            Default: 1
            
    :type CacheNodeCount: integer
    """
    pass


def reboot_cache_cluster(CacheClusterId=None, CacheNodeIdsToReboot=None):
    """
    :param CacheClusterId: [REQUIRED]
            The cache cluster identifier. This parameter is stored as a lowercase string.
            
    :type CacheClusterId: string
    :param CacheNodeIdsToReboot: [REQUIRED]
            A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cache cluster, specify all of the cache node IDs.
            (string) --
            
    :type CacheNodeIdsToReboot: list
    """
    pass


def remove_tags_from_resource(ResourceName=None, TagKeys=None):
    """
    :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .
            For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
            
    :type ResourceName: string
    :param TagKeys: [REQUIRED]
            A list of TagKeys identifying the tags you want removed from the named resource.
            (string) --
            
    :type TagKeys: list
    """
    pass


def reset_cache_parameter_group(CacheParameterGroupName=None, ResetAllParameters=None, ParameterNameValues=None):
    """
    :param CacheParameterGroupName: [REQUIRED]
            The name of the cache parameter group to reset.
            
    :type CacheParameterGroupName: string
    :param ResetAllParameters: If true , all parameters in the cache parameter group are reset to their default values. If false , only the parameters listed by ParameterNameValues are reset to their default values.
            Valid values: true | false
            
    :type ResetAllParameters: boolean
    :param ParameterNameValues: An array of parameter names to reset to their default values. If ResetAllParameters is true , do not use ParameterNameValues . If ResetAllParameters is false , you must specify the name of at least one parameter to reset.
            (dict) --Describes a name-value pair that is used to update the value of a parameter.
            ParameterName (string) --The name of the parameter.
            ParameterValue (string) --The value of the parameter.
            
            
    :type ParameterNameValues: list
    """
    pass


def revoke_cache_security_group_ingress(CacheSecurityGroupName=None, EC2SecurityGroupName=None,
                                        EC2SecurityGroupOwnerId=None):
    """
    :param CacheSecurityGroupName: [REQUIRED]
            The name of the cache security group to revoke ingress from.
            
    :type CacheSecurityGroupName: string
    :param EC2SecurityGroupName: [REQUIRED]
            The name of the Amazon EC2 security group to revoke access from.
            
    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupOwnerId: [REQUIRED]
            The AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.
            
    :type EC2SecurityGroupOwnerId: string
    """
    pass
