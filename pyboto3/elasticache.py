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

import boto3


class Elasticache(object):
    def __init__(self):
        self.client = boto3.client('Elasticache')

    def add_tags_to_resource(self, ResourceName=None, Tags=None):
        """
        :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource to which the tags are to be added, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .
            For more information on ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces .
            
        :type ResourceName: string
        :param Tags: [REQUIRED]
            A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag.
            Value (string) --The tag's value. May not be null.
            
            
        :type Tags: list
        """
        self.client.add_tags_to_resource(ResourceName=ResourceName, Tags=Tags)

    def authorize_cache_security_group_ingress(self, CacheSecurityGroupName=None, EC2SecurityGroupName=None,
                                               EC2SecurityGroupOwnerId=None):
        """
        :param CacheSecurityGroupName: [REQUIRED]
            The cache security group which will allow network ingress.
            
        :type CacheSecurityGroupName: string
        :param EC2SecurityGroupName: [REQUIRED]
            The Amazon EC2 security group to be authorized for ingress to the cache security group.
            
        :type EC2SecurityGroupName: string
        :param EC2SecurityGroupOwnerId: [REQUIRED]
            The AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.
            
        :type EC2SecurityGroupOwnerId: string
        """
        self.client.authorize_cache_security_group_ingress(CacheSecurityGroupName=CacheSecurityGroupName,
                                                           EC2SecurityGroupName=EC2SecurityGroupName,
                                                           EC2SecurityGroupOwnerId=EC2SecurityGroupOwnerId)

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def copy_snapshot(self, SourceSnapshotName=None, TargetSnapshotName=None, TargetBucket=None):
        """
        :param SourceSnapshotName: [REQUIRED]
            The name of an existing snapshot from which to make a copy.
            
        :type SourceSnapshotName: string
        :param TargetSnapshotName: [REQUIRED]
            A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting.
            Error Message
            Error Message: The S3 bucket %s already contains an object with key %s. Solution: Give the TargetSnapshotName a new and unique value. If exporting a snapshot, you could alternatively create a new Amazon S3 bucket and use this same value for TargetSnapshotName .
            
        :type TargetSnapshotName: string
        :param TargetBucket: The Amazon S3 bucket to which the snapshot will be exported. This parameter is used only when exporting a snapshot for external access.
            When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket in the Amazon ElastiCache User Guide .
            Error Messages:
            You could receive one of the following error messages.
            Erorr Messages
            Error Message: ElastiCache has not been granted READ permissions %s on the S3 Bucket. Solution: Add List and Read permissions on the bucket.
            Error Message: ElastiCache has not been granted WRITE permissions %s on the S3 Bucket. Solution: Add Upload/Delete permissions on the bucket.
            Error Message: ElastiCache has not been granted READ_ACP permissions %s on the S3 Bucket. Solution: Add View Permissions permissions on the bucket.
            Error Message: The S3 bucket %s is outside of the region. Solution: Before exporting your snapshot, create a new Amazon S3 bucket in the same region as your snapshot. For more information, see Step 1: Create an Amazon S3 Bucket .
            Error Message: The S3 bucket %s does not exist. Solution: Create an Amazon S3 bucket in the same region as your snapshot. For more information, see Step 1: Create an Amazon S3 Bucket .
            Error Message: The S3 bucket %s is not owned by the authenticated user. Solution: Create an Amazon S3 bucket in the same region as your snapshot. For more information, see Step 1: Create an Amazon S3 Bucket .
            Error Message: The authenticated user does not have sufficient permissions to perform the desired activity. Solution: Contact your system administrator to get the needed permissions.
            For more information, see Exporting a Snapshot in the Amazon ElastiCache User Guide .
            
        :type TargetBucket: string
        """
        self.client.copy_snapshot(SourceSnapshotName=SourceSnapshotName, TargetSnapshotName=TargetSnapshotName,
                                  TargetBucket=TargetBucket)

    def create_cache_cluster(self, CacheClusterId=None, ReplicationGroupId=None, AZMode=None,
                             PreferredAvailabilityZone=None, PreferredAvailabilityZones=None, NumCacheNodes=None,
                             CacheNodeType=None, Engine=None, EngineVersion=None, CacheParameterGroupName=None,
                             CacheSubnetGroupName=None, CacheSecurityGroupNames=None, SecurityGroupIds=None, Tags=None,
                             SnapshotArns=None, SnapshotName=None, PreferredMaintenanceWindow=None, Port=None,
                             NotificationTopicArn=None, AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None,
                             SnapshotWindow=None):
        """
        :param CacheClusterId: [REQUIRED]
            The node group identifier. This parameter is stored as a lowercase string.
            Constraints:
            A name must contain from 1 to 20 alphanumeric characters or hyphens.
            The first character must be a letter.
            A name cannot end with a hyphen or contain two consecutive hyphens.
            
        :type CacheClusterId: string
        :param ReplicationGroupId: The ID of the replication group to which this cache cluster should belong. If this parameter is specified, the cache cluster will be added to the specified replication group as a read replica; otherwise, the cache cluster will be a standalone primary that is not part of any replication group.
            If the specified replication group is Multi-AZ enabled and the availability zone is not specified, the cache cluster will be created in availability zones that provide the best spread of read replicas across availability zones.
            Note
            This parameter is only valid if the Engine parameter is redis .
            
        :type ReplicationGroupId: string
        :param AZMode: Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region.
            This parameter is only supported for Memcached cache clusters.
            If the AZMode and PreferredAvailabilityZones are not specified, ElastiCache assumes single-az mode.
            
        :type AZMode: string
        :param PreferredAvailabilityZone: The EC2 Availability Zone in which the cache cluster will be created.
            All nodes belonging to this Memcached cache cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use PreferredAvailabilityZones .
            Default: System chosen Availability Zone.
            
        :type PreferredAvailabilityZone: string
        :param PreferredAvailabilityZones: A list of the Availability Zones in which cache nodes will be created. The order of the zones in the list is not important.
            This option is only supported on Memcached.
            Note
            If you are creating your cache cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.
            The number of Availability Zones listed must equal the value of NumCacheNodes .
            If you want all the nodes in the same Availability Zone, use PreferredAvailabilityZone instead, or repeat the Availability Zone multiple times in the list.
            Default: System chosen Availability Zones.
            Example: One Memcached node in each of three different Availability Zones: PreferredAvailabilityZones.member.1=us-west-2aamp;PreferredAvailabilityZones.member.2=us-west-2bamp;PreferredAvailabilityZones.member.3=us-west-2c
            Example: All three Memcached nodes in one Availability Zone: PreferredAvailabilityZones.member.1=us-west-2aamp;PreferredAvailabilityZones.member.2=us-west-2aamp;PreferredAvailabilityZones.member.3=us-west-2a
            (string) --
            
        :type PreferredAvailabilityZones: list
        :param NumCacheNodes: The initial number of cache nodes that the cache cluster will have.
            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
            If you need more than 20 nodes for your Memcached cluster, please fill out the ElastiCache Limit Increase Request form at http://aws.amazon.com/contact-us/elasticache-node-limit-request/ .
            
        :type NumCacheNodes: integer
        :param CacheNodeType: The compute and memory capacity of the nodes in the node group.
            Valid node types are as follows:
            General purpose:
            Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
            Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
            Compute optimized: cache.c1.xlarge
            Memory optimized:
            Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
            Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
            
            Notes:
            All t2 instances are created in an Amazon Virtual Private Cloud (VPC).
            Redis backup/restore is not supported for t2 instances.
            Redis Append-only files (AOF) functionality is not supported for t1 or t2 instances.
            For a complete listing of cache node types and specifications, see Amazon ElastiCache Product Features and Details and Cache Node Type-Specific Parameters for Memcached or Cache Node Type-Specific Parameters for Redis .
            
        :type CacheNodeType: string
        :param Engine: The name of the cache engine to be used for this cache cluster.
            Valid values for this parameter are:
            memcached | redis
            
        :type Engine: string
        :param EngineVersion: The version number of the cache engine to be used for this cache cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions action.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cache cluster or replication group and create it anew with the earlier engine version.
            
        :type EngineVersion: string
        :param CacheParameterGroupName: The name of the parameter group to associate with this cache cluster. If this argument is omitted, the default parameter group for the specified engine is used.
        :type CacheParameterGroupName: string
        :param CacheSubnetGroupName: The name of the subnet group to be used for the cache cluster.
            Use this parameter only when you are creating a cache cluster in an Amazon Virtual Private Cloud (VPC).
            
        :type CacheSubnetGroupName: string
        :param CacheSecurityGroupNames: A list of security group names to associate with this cache cluster.
            Use this parameter only when you are creating a cache cluster outside of an Amazon Virtual Private Cloud (VPC).
            (string) --
            
        :type CacheSecurityGroupNames: list
        :param SecurityGroupIds: One or more VPC security groups associated with the cache cluster.
            Use this parameter only when you are creating a cache cluster in an Amazon Virtual Private Cloud (VPC).
            (string) --
            
        :type SecurityGroupIds: list
        :param Tags: A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag.
            Value (string) --The tag's value. May not be null.
            
            
        :type Tags: list
        :param SnapshotArns: A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3. The snapshot file will be used to populate the node group. The Amazon S3 object name in the ARN cannot contain any commas.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Example of an Amazon S3 ARN: arn:aws:s3:::my_bucket/snapshot1.rdb
            (string) --
            
        :type SnapshotArns: list
        :param SnapshotName: The name of a snapshot from which to restore data into the new node group. The snapshot status changes to restoring while the new node group is being created.
            Note
            This parameter is only valid if the Engine parameter is redis .
            
        :type SnapshotName: string
        :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cache cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:
            sun
            mon
            tue
            wed
            thu
            fri
            sat
            Example: sun:05:00-sun:09:00
            
        :type PreferredMaintenanceWindow: string
        :param Port: The port number on which each of the cache nodes will accept connections.
        :type Port: integer
        :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications will be sent.
            Note
            The Amazon SNS topic owner must be the same as the cache cluster owner.
            
        :type NotificationTopicArn: string
        :param AutoMinorVersionUpgrade: This parameter is currently disabled.
        :type AutoMinorVersionUpgrade: boolean
        :param SnapshotRetentionLimit: The number of days for which ElastiCache will retain automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days before being deleted.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Default: 0 (i.e., automatic backups are disabled for this cache cluster).
            
        :type SnapshotRetentionLimit: integer
        :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache will begin taking a daily snapshot of your node group.
            Example: 05:00-09:00
            If you do not specify this parameter, then ElastiCache will automatically choose an appropriate time range.
            Note: This parameter is only valid if the Engine parameter is redis .
            
        :type SnapshotWindow: string
        """
        self.client.create_cache_cluster(CacheClusterId=CacheClusterId, ReplicationGroupId=ReplicationGroupId,
                                         AZMode=AZMode, PreferredAvailabilityZone=PreferredAvailabilityZone,
                                         PreferredAvailabilityZones=PreferredAvailabilityZones,
                                         NumCacheNodes=NumCacheNodes, CacheNodeType=CacheNodeType, Engine=Engine,
                                         EngineVersion=EngineVersion, CacheParameterGroupName=CacheParameterGroupName,
                                         CacheSubnetGroupName=CacheSubnetGroupName,
                                         CacheSecurityGroupNames=CacheSecurityGroupNames,
                                         SecurityGroupIds=SecurityGroupIds, Tags=Tags, SnapshotArns=SnapshotArns,
                                         SnapshotName=SnapshotName,
                                         PreferredMaintenanceWindow=PreferredMaintenanceWindow, Port=Port,
                                         NotificationTopicArn=NotificationTopicArn,
                                         AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
                                         SnapshotRetentionLimit=SnapshotRetentionLimit, SnapshotWindow=SnapshotWindow)

    def create_cache_parameter_group(self, CacheParameterGroupName=None, CacheParameterGroupFamily=None,
                                     Description=None):
        """
        :param CacheParameterGroupName: [REQUIRED]
            A user-specified name for the cache parameter group.
            
        :type CacheParameterGroupName: string
        :param CacheParameterGroupFamily: [REQUIRED]
            The name of the cache parameter group family the cache parameter group can be used with.
            Valid values are: memcached1.4 | redis2.6 | redis2.8
            
        :type CacheParameterGroupFamily: string
        :param Description: [REQUIRED]
            A user-specified description for the cache parameter group.
            
        :type Description: string
        """
        self.client.create_cache_parameter_group(CacheParameterGroupName=CacheParameterGroupName,
                                                 CacheParameterGroupFamily=CacheParameterGroupFamily,
                                                 Description=Description)

    def create_cache_security_group(self, CacheSecurityGroupName=None, Description=None):
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
        self.client.create_cache_security_group(CacheSecurityGroupName=CacheSecurityGroupName, Description=Description)

    def create_cache_subnet_group(self, CacheSubnetGroupName=None, CacheSubnetGroupDescription=None, SubnetIds=None):
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
        self.client.create_cache_subnet_group(CacheSubnetGroupName=CacheSubnetGroupName,
                                              CacheSubnetGroupDescription=CacheSubnetGroupDescription,
                                              SubnetIds=SubnetIds)

    def create_replication_group(self, ReplicationGroupId=None, ReplicationGroupDescription=None, PrimaryClusterId=None,
                                 AutomaticFailoverEnabled=None, NumCacheClusters=None, PreferredCacheClusterAZs=None,
                                 CacheNodeType=None, Engine=None, EngineVersion=None, CacheParameterGroupName=None,
                                 CacheSubnetGroupName=None, CacheSecurityGroupNames=None, SecurityGroupIds=None,
                                 Tags=None, SnapshotArns=None, SnapshotName=None, PreferredMaintenanceWindow=None,
                                 Port=None, NotificationTopicArn=None, AutoMinorVersionUpgrade=None,
                                 SnapshotRetentionLimit=None, SnapshotWindow=None):
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
        :param PrimaryClusterId: The identifier of the cache cluster that will serve as the primary for this replication group. This cache cluster must already exist and have a status of available .
            This parameter is not required if NumCacheClusters is specified.
            
        :type PrimaryClusterId: string
        :param AutomaticFailoverEnabled: Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails.
            If true , Multi-AZ is enabled for this replication group. If false , Multi-AZ is disabled for this replication group.
            Default: false
            Note
            ElastiCache Multi-AZ replication groups is not supported on:
            Redis versions earlier than 2.8.6.
            T1 and T2 cache node types.
            
        :type AutomaticFailoverEnabled: boolean
        :param NumCacheClusters: The number of cache clusters this replication group will initially have.
            If Multi-AZ is enabled , the value of this parameter must be at least 2.
            The maximum permitted value for NumCacheClusters is 6 (primary plus 5 replicas). If you need to exceed this limit, please fill out the ElastiCache Limit Increase Request form at http://aws.amazon.com/contact-us/elasticache-node-limit-request .
            
        :type NumCacheClusters: integer
        :param PreferredCacheClusterAZs: A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.
            Note
            If you are creating your replication group in an Amazon VPC (recommended), you can only locate cache clusters in availability zones associated with the subnets in the selected subnet group.
            The number of availability zones listed must equal the value of NumCacheClusters .
            Default: system chosen availability zones.
            Example: One Redis cache cluster in each of three availability zones.
            PreferredAvailabilityZones.member.1=us-west-2a PreferredAvailabilityZones.member.2=us-west-2c PreferredAvailabilityZones.member.3=us-west-2c
            (string) --
            
        :type PreferredCacheClusterAZs: list
        :param CacheNodeType: The compute and memory capacity of the nodes in the node group.
            Valid node types are as follows:
            General purpose:
            Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
            Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
            Compute optimized: cache.c1.xlarge
            Memory optimized:
            Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
            Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
            
            Notes:
            All t2 instances are created in an Amazon Virtual Private Cloud (VPC).
            Redis backup/restore is not supported for t2 instances.
            Redis Append-only files (AOF) functionality is not supported for t1 or t2 instances.
            For a complete listing of cache node types and specifications, see Amazon ElastiCache Product Features and Details and Cache Node Type-Specific Parameters for Memcached or Cache Node Type-Specific Parameters for Redis .
            
        :type CacheNodeType: string
        :param Engine: The name of the cache engine to be used for the cache clusters in this replication group.
            Default: redis
            
        :type Engine: string
        :param EngineVersion: The version number of the cache engine to be used for the cache clusters in this replication group. To view the supported cache engine versions, use the DescribeCacheEngineVersions action.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ) in the ElastiCache User Guide , but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cache cluster or replication group and create it anew with the earlier engine version.
            
        :type EngineVersion: string
        :param CacheParameterGroupName: The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
        :type CacheParameterGroupName: string
        :param CacheSubnetGroupName: The name of the cache subnet group to be used for the replication group.
        :type CacheSubnetGroupName: string
        :param CacheSecurityGroupNames: A list of cache security group names to associate with this replication group.
            (string) --
            
        :type CacheSecurityGroupNames: list
        :param SecurityGroupIds: One or more Amazon VPC security groups associated with this replication group.
            Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (VPC).
            (string) --
            
        :type SecurityGroupIds: list
        :param Tags: A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag.
            Value (string) --The tag's value. May not be null.
            
            
        :type Tags: list
        :param SnapshotArns: A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3. The snapshot file will be used to populate the node group. The Amazon S3 object name in the ARN cannot contain any commas.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Example of an Amazon S3 ARN: arn:aws:s3:::my_bucket/snapshot1.rdb
            (string) --
            
        :type SnapshotArns: list
        :param SnapshotName: The name of a snapshot from which to restore data into the new node group. The snapshot status changes to restoring while the new node group is being created.
            Note
            This parameter is only valid if the Engine parameter is redis .
            
        :type SnapshotName: string
        :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cache cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:
            sun
            mon
            tue
            wed
            thu
            fri
            sat
            Example: sun:05:00-sun:09:00
            
        :type PreferredMaintenanceWindow: string
        :param Port: The port number on which each member of the replication group will accept connections.
        :type Port: integer
        :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications will be sent.
            Note
            The Amazon SNS topic owner must be the same as the cache cluster owner.
            
        :type NotificationTopicArn: string
        :param AutoMinorVersionUpgrade: This parameter is currently disabled.
        :type AutoMinorVersionUpgrade: boolean
        :param SnapshotRetentionLimit: The number of days for which ElastiCache will retain automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days before being deleted.
            Note
            This parameter is only valid if the Engine parameter is redis .
            Default: 0 (i.e., automatic backups are disabled for this cache cluster).
            
        :type SnapshotRetentionLimit: integer
        :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache will begin taking a daily snapshot of your node group.
            Example: 05:00-09:00
            If you do not specify this parameter, then ElastiCache will automatically choose an appropriate time range.
            Note
            This parameter is only valid if the Engine parameter is redis .
            
        :type SnapshotWindow: string
        """
        self.client.create_replication_group(ReplicationGroupId=ReplicationGroupId,
                                             ReplicationGroupDescription=ReplicationGroupDescription,
                                             PrimaryClusterId=PrimaryClusterId,
                                             AutomaticFailoverEnabled=AutomaticFailoverEnabled,
                                             NumCacheClusters=NumCacheClusters,
                                             PreferredCacheClusterAZs=PreferredCacheClusterAZs,
                                             CacheNodeType=CacheNodeType, Engine=Engine, EngineVersion=EngineVersion,
                                             CacheParameterGroupName=CacheParameterGroupName,
                                             CacheSubnetGroupName=CacheSubnetGroupName,
                                             CacheSecurityGroupNames=CacheSecurityGroupNames,
                                             SecurityGroupIds=SecurityGroupIds, Tags=Tags, SnapshotArns=SnapshotArns,
                                             SnapshotName=SnapshotName,
                                             PreferredMaintenanceWindow=PreferredMaintenanceWindow, Port=Port,
                                             NotificationTopicArn=NotificationTopicArn,
                                             AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
                                             SnapshotRetentionLimit=SnapshotRetentionLimit,
                                             SnapshotWindow=SnapshotWindow)

    def create_snapshot(self, CacheClusterId=None, SnapshotName=None):
        """
        :param CacheClusterId: [REQUIRED]
            The identifier of an existing cache cluster. The snapshot will be created from this cache cluster.
            
        :type CacheClusterId: string
        :param SnapshotName: [REQUIRED]
            A name for the snapshot being created.
            
        :type SnapshotName: string
        """
        self.client.create_snapshot(CacheClusterId=CacheClusterId, SnapshotName=SnapshotName)

    def delete_cache_cluster(self, CacheClusterId=None, FinalSnapshotIdentifier=None):
        """
        :param CacheClusterId: [REQUIRED]
            The cache cluster identifier for the cluster to be deleted. This parameter is not case sensitive.
            
        :type CacheClusterId: string
        :param FinalSnapshotIdentifier: The user-supplied name of a final cache cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cache cluster immediately afterward.
        :type FinalSnapshotIdentifier: string
        """
        self.client.delete_cache_cluster(CacheClusterId=CacheClusterId, FinalSnapshotIdentifier=FinalSnapshotIdentifier)

    def delete_cache_parameter_group(self, CacheParameterGroupName=None):
        """
        :param CacheParameterGroupName: [REQUIRED]
            The name of the cache parameter group to delete.
            Note
            The specified cache security group must not be associated with any cache clusters.
            ReturnsNone
            
        :type CacheParameterGroupName: string
        """
        self.client.delete_cache_parameter_group(CacheParameterGroupName=CacheParameterGroupName)

    def delete_cache_security_group(self, CacheSecurityGroupName=None):
        """
        :param CacheSecurityGroupName: [REQUIRED]
            The name of the cache security group to delete.
            Note
            You cannot delete the default security group.
            ReturnsNone
            
        :type CacheSecurityGroupName: string
        """
        self.client.delete_cache_security_group(CacheSecurityGroupName=CacheSecurityGroupName)

    def delete_cache_subnet_group(self, CacheSubnetGroupName=None):
        """
        :param CacheSubnetGroupName: [REQUIRED]
            The name of the cache subnet group to delete.
            Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
            ReturnsNone
            
        :type CacheSubnetGroupName: string
        """
        self.client.delete_cache_subnet_group(CacheSubnetGroupName=CacheSubnetGroupName)

    def delete_replication_group(self, ReplicationGroupId=None, RetainPrimaryCluster=None,
                                 FinalSnapshotIdentifier=None):
        """
        :param ReplicationGroupId: [REQUIRED]
            The identifier for the cluster to be deleted. This parameter is not case sensitive.
            
        :type ReplicationGroupId: string
        :param RetainPrimaryCluster: If set to true , all of the read replicas will be deleted, but the primary node will be retained.
        :type RetainPrimaryCluster: boolean
        :param FinalSnapshotIdentifier: The name of a final node group snapshot. ElastiCache creates the snapshot from the primary node in the cluster, rather than one of the replicas; this is to ensure that it captures the freshest data. After the final snapshot is taken, the cluster is immediately deleted.
        :type FinalSnapshotIdentifier: string
        """
        self.client.delete_replication_group(ReplicationGroupId=ReplicationGroupId,
                                             RetainPrimaryCluster=RetainPrimaryCluster,
                                             FinalSnapshotIdentifier=FinalSnapshotIdentifier)

    def delete_snapshot(self, SnapshotName=None):
        """
        :param SnapshotName: [REQUIRED]
            The name of the snapshot to be deleted.
            Return typedict
            ReturnsResponse Syntax{
              'Snapshot': {
                'SnapshotName': 'string',
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
                'NodeSnapshots': [
                  {
                    'CacheNodeId': 'string',
                    'CacheSize': 'string',
                    'CacheNodeCreateTime': datetime(2015, 1, 1),
                    'SnapshotCreateTime': datetime(2015, 1, 1)
                  },
                ]
              }
            }
            Response Structure
            (dict) --
            Snapshot (dict) --Represents a copy of an entire cache cluster as of the time when the snapshot was taken.
            SnapshotName (string) --The name of a snapshot. For an automatic snapshot, the name is system-generated; for a manual snapshot, this is the user-provided name.
            CacheClusterId (string) --The user-supplied identifier of the source cache cluster.
            SnapshotStatus (string) --The status of the snapshot. Valid values: creating | available | restoring | copying | deleting .
            SnapshotSource (string) --Indicates whether the snapshot is from an automatic backup (automated ) or was created manually (manual ).
            CacheNodeType (string) --The name of the compute and memory capacity node type for the source cache cluster.
            Valid node types are as follows:
            General purpose:
            Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
            Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
            Compute optimized: cache.c1.xlarge
            Memory optimized:
            Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
            Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
            
            Notes:
            All t2 instances are created in an Amazon Virtual Private Cloud (VPC).
            Redis backup/restore is not supported for t2 instances.
            Redis Append-only files (AOF) functionality is not supported for t1 or t2 instances.
            For a complete listing of cache node types and specifications, see Amazon ElastiCache Product Features and Details and Cache Node Type-Specific Parameters for Memcached or Cache Node Type-Specific Parameters for Redis .
            Engine (string) --The name of the cache engine (memcached or redis ) used by the source cache cluster.
            EngineVersion (string) --The version of the cache engine version that is used by the source cache cluster.
            NumCacheNodes (integer) --The number of cache nodes in the source cache cluster.
            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
            PreferredAvailabilityZone (string) --The name of the Availability Zone in which the source cache cluster is located.
            CacheClusterCreateTime (datetime) --The date and time when the source cache cluster was created.
            PreferredMaintenanceWindow (string) --Specifies the weekly time range during which maintenance on the cache cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:
            sun
            mon
            tue
            wed
            thu
            fri
            sat
            Example: sun:05:00-sun:09:00
            TopicArn (string) --The Amazon Resource Name (ARN) for the topic used by the source cache cluster for publishing notifications.
            Port (integer) --The port number used by each cache nodes in the source cache cluster.
            CacheParameterGroupName (string) --The cache parameter group that is associated with the source cache cluster.
            CacheSubnetGroupName (string) --The name of the cache subnet group associated with the source cache cluster.
            VpcId (string) --The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cache cluster.
            AutoMinorVersionUpgrade (boolean) --This parameter is currently disabled.
            SnapshotRetentionLimit (integer) --For an automatic snapshot, the number of days for which ElastiCache will retain the snapshot before deleting it.
            For manual snapshots, this field reflects the SnapshotRetentionLimit for the source cache cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the DeleteSnapshot action.
            Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
            SnapshotWindow (string) --The daily time range during which ElastiCache takes daily snapshots of the source cache cluster.
            NodeSnapshots (list) --A list of the cache nodes in the source cache cluster.
            (dict) --Represents an individual cache node in a snapshot of a cache cluster.
            CacheNodeId (string) --The cache node identifier for the node in the source cache cluster.
            CacheSize (string) --The size of the cache on the source cache node.
            CacheNodeCreateTime (datetime) --The date and time when the cache node was created in the source cache cluster.
            SnapshotCreateTime (datetime) --The date and time when the source node's metadata and cache data set was obtained for the snapshot.
            
            
            
            
        :type SnapshotName: string
        """
        self.client.delete_snapshot(SnapshotName=SnapshotName)

    def describe_cache_clusters(self, CacheClusterId=None, MaxRecords=None, Marker=None, ShowCacheNodeInfo=None):
        """
        :param CacheClusterId: The user-supplied cluster identifier. If this parameter is specified, only information about that specific cache cluster is returned. This parameter isn't case sensitive.
        :type CacheClusterId: string
        :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
        :type MaxRecords: integer
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        :param ShowCacheNodeInfo: An optional flag that can be included in the DescribeCacheCluster request to retrieve information about the individual cache nodes.
        :type ShowCacheNodeInfo: boolean
        """
        self.client.describe_cache_clusters(CacheClusterId=CacheClusterId, MaxRecords=MaxRecords, Marker=Marker,
                                            ShowCacheNodeInfo=ShowCacheNodeInfo)

    def describe_cache_engine_versions(self, Engine=None, EngineVersion=None, CacheParameterGroupFamily=None,
                                       MaxRecords=None, Marker=None, DefaultOnly=None):
        """
        :param Engine: The cache engine to return. Valid values: memcached | redis
        :type Engine: string
        :param EngineVersion: The cache engine version to return.
            Example: 1.4.14
            
        :type EngineVersion: string
        :param CacheParameterGroupFamily: The name of a specific cache parameter group family to return details for.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
        :type CacheParameterGroupFamily: string
        :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
        :type MaxRecords: integer
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        :param DefaultOnly: If true , specifies that only the default version of the specified engine or engine and major version combination is to be returned.
        :type DefaultOnly: boolean
        """
        self.client.describe_cache_engine_versions(Engine=Engine, EngineVersion=EngineVersion,
                                                   CacheParameterGroupFamily=CacheParameterGroupFamily,
                                                   MaxRecords=MaxRecords, Marker=Marker, DefaultOnly=DefaultOnly)

    def describe_cache_parameter_groups(self, CacheParameterGroupName=None, MaxRecords=None, Marker=None):
        """
        :param CacheParameterGroupName: The name of a specific cache parameter group to return details for.
        :type CacheParameterGroupName: string
        :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
        :type MaxRecords: integer
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        """
        self.client.describe_cache_parameter_groups(CacheParameterGroupName=CacheParameterGroupName,
                                                    MaxRecords=MaxRecords, Marker=Marker)

    def describe_cache_parameters(self, CacheParameterGroupName=None, Source=None, MaxRecords=None, Marker=None):
        """
        :param CacheParameterGroupName: [REQUIRED]
            The name of a specific cache parameter group to return details for.
            
        :type CacheParameterGroupName: string
        :param Source: The parameter types to return.
            Valid values: user | system | engine-default
            
        :type Source: string
        :param MaxRecords: The maximum number of brecords to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
        :type MaxRecords: integer
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        """
        self.client.describe_cache_parameters(CacheParameterGroupName=CacheParameterGroupName, Source=Source,
                                              MaxRecords=MaxRecords, Marker=Marker)

    def describe_cache_security_groups(self, CacheSecurityGroupName=None, MaxRecords=None, Marker=None):
        """
        :param CacheSecurityGroupName: The name of the cache security group to return details for.
        :type CacheSecurityGroupName: string
        :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
        :type MaxRecords: integer
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        """
        self.client.describe_cache_security_groups(CacheSecurityGroupName=CacheSecurityGroupName, MaxRecords=MaxRecords,
                                                   Marker=Marker)

    def describe_cache_subnet_groups(self, CacheSubnetGroupName=None, MaxRecords=None, Marker=None):
        """
        :param CacheSubnetGroupName: The name of the cache subnet group to return details for.
        :type CacheSubnetGroupName: string
        :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
        :type MaxRecords: integer
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        """
        self.client.describe_cache_subnet_groups(CacheSubnetGroupName=CacheSubnetGroupName, MaxRecords=MaxRecords,
                                                 Marker=Marker)

    def describe_engine_default_parameters(self, CacheParameterGroupFamily=None, MaxRecords=None, Marker=None):
        """
        :param CacheParameterGroupFamily: [REQUIRED]
            The name of the cache parameter group family. Valid values are: memcached1.4 | redis2.6 | redis2.8
            
        :type CacheParameterGroupFamily: string
        :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
        :type MaxRecords: integer
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        """
        self.client.describe_engine_default_parameters(CacheParameterGroupFamily=CacheParameterGroupFamily,
                                                       MaxRecords=MaxRecords, Marker=Marker)

    def describe_events(self, SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None,
                        MaxRecords=None, Marker=None):
        """
        :param SourceIdentifier: The identifier of the event source for which events will be returned. If not specified, then all sources are included in the response.
        :type SourceIdentifier: string
        :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.
            Valid values are: cache-cluster | cache-parameter-group | cache-security-group | cache-subnet-group
            
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
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        """
        self.client.describe_events(SourceIdentifier=SourceIdentifier, SourceType=SourceType, StartTime=StartTime,
                                    EndTime=EndTime, Duration=Duration, MaxRecords=MaxRecords, Marker=Marker)

    def describe_replication_groups(self, ReplicationGroupId=None, MaxRecords=None, Marker=None):
        """
        :param ReplicationGroupId: The identifier for the replication group to be described. This parameter is not case sensitive.
            If you do not specify this parameter, information about all replication groups is returned.
            
        :type ReplicationGroupId: string
        :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: minimum 20; maximum 100.
            
        :type MaxRecords: integer
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        """
        self.client.describe_replication_groups(ReplicationGroupId=ReplicationGroupId, MaxRecords=MaxRecords,
                                                Marker=Marker)

    def describe_reserved_cache_nodes(self, ReservedCacheNodeId=None, ReservedCacheNodesOfferingId=None,
                                      CacheNodeType=None, Duration=None, ProductDescription=None, OfferingType=None,
                                      MaxRecords=None, Marker=None):
        """
        :param ReservedCacheNodeId: The reserved cache node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.
        :type ReservedCacheNodeId: string
        :param ReservedCacheNodesOfferingId: The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.
        :type ReservedCacheNodesOfferingId: string
        :param CacheNodeType: The cache node type filter value. Use this parameter to show only those reservations matching the specified cache node type.
            Valid node types are as follows:
            General purpose:
            Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
            Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
            Compute optimized: cache.c1.xlarge
            Memory optimized:
            Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
            Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
            
            Notes:
            All t2 instances are created in an Amazon Virtual Private Cloud (VPC).
            Redis backup/restore is not supported for t2 instances.
            Redis Append-only files (AOF) functionality is not supported for t1 or t2 instances.
            For a complete listing of cache node types and specifications, see Amazon ElastiCache Product Features and Details and Cache Node Type-Specific Parameters for Memcached or Cache Node Type-Specific Parameters for Redis .
            
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
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        """
        self.client.describe_reserved_cache_nodes(ReservedCacheNodeId=ReservedCacheNodeId,
                                                  ReservedCacheNodesOfferingId=ReservedCacheNodesOfferingId,
                                                  CacheNodeType=CacheNodeType, Duration=Duration,
                                                  ProductDescription=ProductDescription, OfferingType=OfferingType,
                                                  MaxRecords=MaxRecords, Marker=Marker)

    def describe_reserved_cache_nodes_offerings(self, ReservedCacheNodesOfferingId=None, CacheNodeType=None,
                                                Duration=None, ProductDescription=None, OfferingType=None,
                                                MaxRecords=None, Marker=None):
        """
        :param ReservedCacheNodesOfferingId: The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.
            Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
            
        :type ReservedCacheNodesOfferingId: string
        :param CacheNodeType: The cache node type filter value. Use this parameter to show only the available offerings matching the specified cache node type.
            Valid node types are as follows:
            General purpose:
            Current generation: cache.t2.micro , cache.t2.small , cache.t2.medium , cache.m3.medium , cache.m3.large , cache.m3.xlarge , cache.m3.2xlarge
            Previous generation: cache.t1.micro , cache.m1.small , cache.m1.medium , cache.m1.large , cache.m1.xlarge
            Compute optimized: cache.c1.xlarge
            Memory optimized:
            Current generation: cache.r3.large , cache.r3.xlarge , cache.r3.2xlarge , cache.r3.4xlarge , cache.r3.8xlarge
            Previous generation: cache.m2.xlarge , cache.m2.2xlarge , cache.m2.4xlarge
            
            Notes:
            All t2 instances are created in an Amazon Virtual Private Cloud (VPC).
            Redis backup/restore is not supported for t2 instances.
            Redis Append-only files (AOF) functionality is not supported for t1 or t2 instances.
            For a complete listing of cache node types and specifications, see Amazon ElastiCache Product Features and Details and Cache Node Type-Specific Parameters for Memcached or Cache Node Type-Specific Parameters for Redis .
            
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
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        """
        self.client.describe_reserved_cache_nodes_offerings(ReservedCacheNodesOfferingId=ReservedCacheNodesOfferingId,
                                                            CacheNodeType=CacheNodeType, Duration=Duration,
                                                            ProductDescription=ProductDescription,
                                                            OfferingType=OfferingType, MaxRecords=MaxRecords,
                                                            Marker=Marker)

    def describe_snapshots(self, CacheClusterId=None, SnapshotName=None, SnapshotSource=None, Marker=None,
                           MaxRecords=None):
        """
        :param CacheClusterId: A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cache cluster will be described.
        :type CacheClusterId: string
        :param SnapshotName: A user-supplied name of the snapshot. If this parameter is specified, only this snapshot will be described.
        :type SnapshotName: string
        :param SnapshotSource: If set to system , the output shows snapshots that were automatically created by ElastiCache. If set to user the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.
        :type SnapshotSource: string
        :param Marker: An optional marker returned from a prior request. Use this marker for pagination of results from this action. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
        :type Marker: string
        :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
            Default: 50
            Constraints: minimum 20; maximum 50.
            
        :type MaxRecords: integer
        """
        self.client.describe_snapshots(CacheClusterId=CacheClusterId, SnapshotName=SnapshotName,
                                       SnapshotSource=SnapshotSource, Marker=Marker, MaxRecords=MaxRecords)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def list_allowed_node_type_modifications(self, CacheClusterId=None, ReplicationGroupId=None):
        """
        :param CacheClusterId: The name of the cache cluster you want to scale up to a larger node instanced type. ElastiCache uses the cluster id to identify the current node type of this cluster and from that to to create a list of node types you can scale up to.
            Warning
            You must provide a value for either the CacheClusterId or the ReplicationGroupId .
            
        :type CacheClusterId: string
        :param ReplicationGroupId: The name of the replication group want to scale up to a larger node type. ElastiCache uses the replication group id to identify the current node type being used by this replication group, and from that to create a list of node types you can scale up to.
            Warning
            You must provide a value for either the CacheClusterId or the ReplicationGroupId .
            
        :type ReplicationGroupId: string
        """
        self.client.list_allowed_node_type_modifications(CacheClusterId=CacheClusterId,
                                                         ReplicationGroupId=ReplicationGroupId)

    def list_tags_for_resource(self, ResourceName=None):
        """
        :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource for which you want the list of tags, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .
            For more information on ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces .
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
            (dict) --Represents the output from the AddTagsToResource , ListTagsOnResource , and RemoveTagsFromResource actions.
            TagList (list) --A list of cost allocation tags as key-value pairs.
            (dict) --A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.
            Key (string) --The key for the tag.
            Value (string) --The tag's value. May not be null.
            
            
            
        :type ResourceName: string
        """
        self.client.list_tags_for_resource(ResourceName=ResourceName)

    def modify_cache_cluster(self, CacheClusterId=None, NumCacheNodes=None, CacheNodeIdsToRemove=None, AZMode=None,
                             NewAvailabilityZones=None, CacheSecurityGroupNames=None, SecurityGroupIds=None,
                             PreferredMaintenanceWindow=None, NotificationTopicArn=None, CacheParameterGroupName=None,
                             NotificationTopicStatus=None, ApplyImmediately=None, EngineVersion=None,
                             AutoMinorVersionUpgrade=None, SnapshotRetentionLimit=None, SnapshotWindow=None,
                             CacheNodeType=None):
        """
        :param CacheClusterId: [REQUIRED]
            The cache cluster identifier. This value is stored as a lowercase string.
            
        :type CacheClusterId: string
        :param NumCacheNodes: The number of cache nodes that the cache cluster should have. If the value for NumCacheNodes is greater than the sum of the number of current cache nodes and the number of cache nodes pending creation (which may be zero), then more nodes will be added. If the value is less than the number of existing cache nodes, then nodes will be removed. If the value is equal to the number of current cache nodes, then any pending add or remove requests are canceled.
            If you are removing cache nodes, you must use the CacheNodeIdsToRemove parameter to provide the IDs of the specific cache nodes to remove.
            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.
            Note
            Adding or removing Memcached cache nodes can be applied immediately or as a pending action. See ApplyImmediately .
            A pending action to modify the number of cache nodes in a cluster during its maintenance window, whether by adding or removing nodes in accordance with the scale out architecture, is not queued. The customer's latest request to add or remove nodes to the cluster overrides any previous pending actions to modify the number of cache nodes in the cluster. For example, a request to remove 2 nodes would override a previous pending action to remove 3 nodes. Similarly, a request to add 2 nodes would override a previous pending action to remove 3 nodes and vice versa. As Memcached cache nodes may now be provisioned in different Availability Zones with flexible cache node placement, a request to add nodes does not automatically override a previous pending action to add nodes. The customer can modify the previous pending action to add more nodes or explicitly cancel the pending request and retry the new request. To cancel pending actions to modify the number of cache nodes in a cluster, use the ModifyCacheCluster request and set NumCacheNodes equal to the number of cache nodes currently in the cache cluster.
            
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
            Only newly created nodes will be located in different Availability Zones. For instructions on how to move existing Memcached nodes to different Availability Zones, see the Availability Zone Considerations section of Cache Node Considerations for Memcached .
            
        :type AZMode: string
        :param NewAvailabilityZones: The list of Availability Zones where the new Memcached cache nodes will be created.
            This parameter is only valid when NumCacheNodes in the request is greater than the sum of the number of active cache nodes and the number of cache nodes pending creation (which may be zero). The number of Availability Zones supplied in this list must match the cache nodes being added in this request.
            This option is only supported on Memcached clusters.
            Scenarios:
            Scenario 1: You have 3 active nodes and wish to add 2 nodes. Specify NumCacheNodes=5 (3 + 2) and optionally specify two Availability Zones for the two new nodes.
            Scenario 2: You have 3 active nodes and 2 nodes pending creation (from the scenario 1 call) and want to add 1 more node. Specify NumCacheNodes=6 ((3 + 2) + 1) and optionally specify an Availability Zone for the new node.
            Scenario 3: You want to cancel all pending actions. Specify NumCacheNodes=3 to cancel all pending actions.
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
            Example:
            NewAvailabilityZones.member.1=us-west-2aamp;NewAvailabilityZones.member.2=us-west-2bamp;NewAvailabilityZones.member.3=us-west-2c
            (string) --
            
        :type NewAvailabilityZones: list
        :param CacheSecurityGroupNames: A list of cache security group names to authorize on this cache cluster. This change is asynchronously applied as soon as possible.
            This parameter can be used only with clusters that are created outside of an Amazon Virtual Private Cloud (VPC).
            Constraints: Must contain no more than 255 alphanumeric characters. Must not be 'Default'.
            (string) --
            
        :type CacheSecurityGroupNames: list
        :param SecurityGroupIds: Specifies the VPC Security Groups associated with the cache cluster.
            This parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud (VPC).
            (string) --
            
        :type SecurityGroupIds: list
        :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cache cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:
            sun
            mon
            tue
            wed
            thu
            fri
            sat
            Example: sun:05:00-sun:09:00
            
        :type PreferredMaintenanceWindow: string
        :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent.
            Note
            The Amazon SNS topic owner must be same as the cache cluster owner.
            
        :type NotificationTopicArn: string
        :param CacheParameterGroupName: The name of the cache parameter group to apply to this cache cluster. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for this request.
        :type CacheParameterGroupName: string
        :param NotificationTopicStatus: The status of the Amazon SNS notification topic. Notifications are sent only if the status is active .
            Valid values: active | inactive
            
        :type NotificationTopicStatus: string
        :param ApplyImmediately: If true , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow setting for the cache cluster.
            If false , then changes to the cache cluster are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.
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
        :param SnapshotRetentionLimit: The number of days for which ElastiCache will retain automatic cache cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days before being deleted.
            Note
            If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
            
        :type SnapshotRetentionLimit: integer
        :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache will begin taking a daily snapshot of your cache cluster.
        :type SnapshotWindow: string
        :param CacheNodeType: A valid cache node type that you want to scale this cache cluster to. The value of this parameter must be one of the ScaleUpModifications values returned by the ListAllowedCacheNodeTypeModification action.
        :type CacheNodeType: string
        """
        self.client.modify_cache_cluster(CacheClusterId=CacheClusterId, NumCacheNodes=NumCacheNodes,
                                         CacheNodeIdsToRemove=CacheNodeIdsToRemove, AZMode=AZMode,
                                         NewAvailabilityZones=NewAvailabilityZones,
                                         CacheSecurityGroupNames=CacheSecurityGroupNames,
                                         SecurityGroupIds=SecurityGroupIds,
                                         PreferredMaintenanceWindow=PreferredMaintenanceWindow,
                                         NotificationTopicArn=NotificationTopicArn,
                                         CacheParameterGroupName=CacheParameterGroupName,
                                         NotificationTopicStatus=NotificationTopicStatus,
                                         ApplyImmediately=ApplyImmediately, EngineVersion=EngineVersion,
                                         AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
                                         SnapshotRetentionLimit=SnapshotRetentionLimit, SnapshotWindow=SnapshotWindow,
                                         CacheNodeType=CacheNodeType)

    def modify_cache_parameter_group(self, CacheParameterGroupName=None, ParameterNameValues=None):
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
        self.client.modify_cache_parameter_group(CacheParameterGroupName=CacheParameterGroupName,
                                                 ParameterNameValues=ParameterNameValues)

    def modify_cache_subnet_group(self, CacheSubnetGroupName=None, CacheSubnetGroupDescription=None, SubnetIds=None):
        """
        :param CacheSubnetGroupName: [REQUIRED]
            The name for the cache subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters or hyphens.
            Example: mysubnetgroup
            
        :type CacheSubnetGroupName: string
        :param CacheSubnetGroupDescription: A description for the cache subnet group.
        :type CacheSubnetGroupDescription: string
        :param SubnetIds: The EC2 subnet IDs for the cache subnet group.
            (string) --
            
        :type SubnetIds: list
        """
        self.client.modify_cache_subnet_group(CacheSubnetGroupName=CacheSubnetGroupName,
                                              CacheSubnetGroupDescription=CacheSubnetGroupDescription,
                                              SubnetIds=SubnetIds)

    def modify_replication_group(self, ReplicationGroupId=None, ReplicationGroupDescription=None, PrimaryClusterId=None,
                                 SnapshottingClusterId=None, AutomaticFailoverEnabled=None,
                                 CacheSecurityGroupNames=None, SecurityGroupIds=None, PreferredMaintenanceWindow=None,
                                 NotificationTopicArn=None, CacheParameterGroupName=None, NotificationTopicStatus=None,
                                 ApplyImmediately=None, EngineVersion=None, AutoMinorVersionUpgrade=None,
                                 SnapshotRetentionLimit=None, SnapshotWindow=None, CacheNodeType=None):
        """
        :param ReplicationGroupId: [REQUIRED]
            The identifier of the replication group to modify.
            
        :type ReplicationGroupId: string
        :param ReplicationGroupDescription: A description for the replication group. Maximum length is 255 characters.
        :type ReplicationGroupDescription: string
        :param PrimaryClusterId: If this parameter is specified, ElastiCache will promote the specified cluster in the specified replication group to the primary role. The nodes of all other clusters in the replication group will be read replicas.
        :type PrimaryClusterId: string
        :param SnapshottingClusterId: The cache cluster ID that will be used as the daily snapshot source for the replication group.
        :type SnapshottingClusterId: string
        :param AutomaticFailoverEnabled: Whether a read replica will be automatically promoted to read/write primary if the existing primary encounters a failure.
            Valid values: true | false
            Note
            ElastiCache Multi-AZ replication groups are not supported on:
            Redis versions earlier than 2.8.6.
            T1 and T2 cache node types.
            
        :type AutomaticFailoverEnabled: boolean
        :param CacheSecurityGroupNames: A list of cache security group names to authorize for the clusters in this replication group. This change is asynchronously applied as soon as possible.
            This parameter can be used only with replication group containing cache clusters running outside of an Amazon Virtual Private Cloud (VPC).
            Constraints: Must contain no more than 255 alphanumeric characters. Must not be 'Default'.
            (string) --
            
        :type CacheSecurityGroupNames: list
        :param SecurityGroupIds: Specifies the VPC Security Groups associated with the cache clusters in the replication group.
            This parameter can be used only with replication group containing cache clusters running in an Amazon Virtual Private Cloud (VPC).
            (string) --
            
        :type SecurityGroupIds: list
        :param PreferredMaintenanceWindow: Specifies the weekly time range during which maintenance on the cache cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ddd are:
            sun
            mon
            tue
            wed
            thu
            fri
            sat
            Example: sun:05:00-sun:09:00
            
        :type PreferredMaintenanceWindow: string
        :param NotificationTopicArn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent.
            Note
            The Amazon SNS topic owner must be same as the replication group owner.
            
        :type NotificationTopicArn: string
        :param CacheParameterGroupName: The name of the cache parameter group to apply to all of the clusters in this replication group. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for this request.
        :type CacheParameterGroupName: string
        :param NotificationTopicStatus: The status of the Amazon SNS notification topic for the replication group. Notifications are sent only if the status is active .
            Valid values: active | inactive
            
        :type NotificationTopicStatus: string
        :param ApplyImmediately: If true , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow setting for the replication group.
            If false , then changes to the nodes in the replication group are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.
            Valid values: true | false
            Default: false
            
        :type ApplyImmediately: boolean
        :param EngineVersion: The upgraded version of the cache engine to be run on the cache clusters in the replication group.
            Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing replication group and create it anew with the earlier engine version.
            
        :type EngineVersion: string
        :param AutoMinorVersionUpgrade: This parameter is currently disabled.
        :type AutoMinorVersionUpgrade: boolean
        :param SnapshotRetentionLimit: The number of days for which ElastiCache will retain automatic node group snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days before being deleted.
            Important If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
            
        :type SnapshotRetentionLimit: integer
        :param SnapshotWindow: The daily time range (in UTC) during which ElastiCache will begin taking a daily snapshot of the node group specified by SnapshottingClusterId .
            Example: 05:00-09:00
            If you do not specify this parameter, then ElastiCache will automatically choose an appropriate time range.
            
        :type SnapshotWindow: string
        :param CacheNodeType: A valid cache node type that you want to scale this replication group to. The value of this parameter must be one of the ScaleUpModifications values returned by the ListAllowedCacheNodeTypeModification action.
        :type CacheNodeType: string
        """
        self.client.modify_replication_group(ReplicationGroupId=ReplicationGroupId,
                                             ReplicationGroupDescription=ReplicationGroupDescription,
                                             PrimaryClusterId=PrimaryClusterId,
                                             SnapshottingClusterId=SnapshottingClusterId,
                                             AutomaticFailoverEnabled=AutomaticFailoverEnabled,
                                             CacheSecurityGroupNames=CacheSecurityGroupNames,
                                             SecurityGroupIds=SecurityGroupIds,
                                             PreferredMaintenanceWindow=PreferredMaintenanceWindow,
                                             NotificationTopicArn=NotificationTopicArn,
                                             CacheParameterGroupName=CacheParameterGroupName,
                                             NotificationTopicStatus=NotificationTopicStatus,
                                             ApplyImmediately=ApplyImmediately, EngineVersion=EngineVersion,
                                             AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
                                             SnapshotRetentionLimit=SnapshotRetentionLimit,
                                             SnapshotWindow=SnapshotWindow, CacheNodeType=CacheNodeType)

    def purchase_reserved_cache_nodes_offering(self, ReservedCacheNodesOfferingId=None, ReservedCacheNodeId=None,
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
        self.client.purchase_reserved_cache_nodes_offering(ReservedCacheNodesOfferingId=ReservedCacheNodesOfferingId,
                                                           ReservedCacheNodeId=ReservedCacheNodeId,
                                                           CacheNodeCount=CacheNodeCount)

    def reboot_cache_cluster(self, CacheClusterId=None, CacheNodeIdsToReboot=None):
        """
        :param CacheClusterId: [REQUIRED]
            The cache cluster identifier. This parameter is stored as a lowercase string.
            
        :type CacheClusterId: string
        :param CacheNodeIdsToReboot: [REQUIRED]
            A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cache cluster, specify all of the cache node IDs.
            (string) --
            
        :type CacheNodeIdsToReboot: list
        """
        self.client.reboot_cache_cluster(CacheClusterId=CacheClusterId, CacheNodeIdsToReboot=CacheNodeIdsToReboot)

    def remove_tags_from_resource(self, ResourceName=None, TagKeys=None):
        """
        :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot .
            For more information on ARNs, go to Amazon Resource Names (ARNs) and AWS Service Namespaces .
            
        :type ResourceName: string
        :param TagKeys: [REQUIRED]
            A list of TagKeys identifying the tags you want removed from the named resource. For example, TagKeys.member.1=Region removes the cost allocation tag with the key name Region from the resource named by the ResourceName parameter.
            (string) --
            
        :type TagKeys: list
        """
        self.client.remove_tags_from_resource(ResourceName=ResourceName, TagKeys=TagKeys)

    def reset_cache_parameter_group(self, CacheParameterGroupName=None, ResetAllParameters=None,
                                    ParameterNameValues=None):
        """
        :param CacheParameterGroupName: [REQUIRED]
            The name of the cache parameter group to reset.
            
        :type CacheParameterGroupName: string
        :param ResetAllParameters: If true , all parameters in the cache parameter group will be reset to their default values. If false , only the parameters listed by ParameterNameValues are reset to their default values.
            Valid values: true | false
            
        :type ResetAllParameters: boolean
        :param ParameterNameValues: An array of parameter names to reset to their default values. If ResetAllParameters is false , you must specify the name of at least one parameter to reset.
            (dict) --Describes a name-value pair that is used to update the value of a parameter.
            ParameterName (string) --The name of the parameter.
            ParameterValue (string) --The value of the parameter.
            
            
        :type ParameterNameValues: list
        """
        self.client.reset_cache_parameter_group(CacheParameterGroupName=CacheParameterGroupName,
                                                ResetAllParameters=ResetAllParameters,
                                                ParameterNameValues=ParameterNameValues)

    def revoke_cache_security_group_ingress(self, CacheSecurityGroupName=None, EC2SecurityGroupName=None,
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
        self.client.revoke_cache_security_group_ingress(CacheSecurityGroupName=CacheSecurityGroupName,
                                                        EC2SecurityGroupName=EC2SecurityGroupName,
                                                        EC2SecurityGroupOwnerId=EC2SecurityGroupOwnerId)
