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


def authorize_cluster_security_group_ingress(ClusterSecurityGroupName=None, CIDRIP=None, EC2SecurityGroupName=None,
                                             EC2SecurityGroupOwnerId=None):
    """
    :param ClusterSecurityGroupName: [REQUIRED]
            The name of the security group to which the ingress rule is added.
            
    :type ClusterSecurityGroupName: string
    :param CIDRIP: The IP range to be added the Amazon Redshift security group.
    :type CIDRIP: string
    :param EC2SecurityGroupName: The EC2 security group to be added the Amazon Redshift security group.
    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupOwnerId: The AWS account number of the owner of the security group specified by the EC2SecurityGroupName parameter. The AWS Access Key ID is not an acceptable value.
            Example: 111122223333
            
    :type EC2SecurityGroupOwnerId: string
    """
    pass


def authorize_snapshot_access(SnapshotIdentifier=None, SnapshotClusterIdentifier=None, AccountWithRestoreAccess=None):
    """
    :param SnapshotIdentifier: [REQUIRED]
            The identifier of the snapshot the account is authorized to restore.
            
    :type SnapshotIdentifier: string
    :param SnapshotClusterIdentifier: The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
    :type SnapshotClusterIdentifier: string
    :param AccountWithRestoreAccess: [REQUIRED]
            The identifier of the AWS customer account authorized to restore the specified snapshot.
            
    :type AccountWithRestoreAccess: string
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


def copy_cluster_snapshot(SourceSnapshotIdentifier=None, SourceSnapshotClusterIdentifier=None,
                          TargetSnapshotIdentifier=None):
    """
    :param SourceSnapshotIdentifier: [REQUIRED]
            The identifier for the source snapshot.
            Constraints:
            Must be the identifier for a valid automated snapshot whose state is available .
            
    :type SourceSnapshotIdentifier: string
    :param SourceSnapshotClusterIdentifier: The identifier of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
            Constraints:
            Must be the identifier for a valid cluster.
            
    :type SourceSnapshotClusterIdentifier: string
    :param TargetSnapshotIdentifier: [REQUIRED]
            The identifier given to the new manual snapshot.
            Constraints:
            Cannot be null, empty, or blank.
            Must contain from 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for the AWS account that is making the request.
            
    :type TargetSnapshotIdentifier: string
    """
    pass


def create_cluster(DBName=None, ClusterIdentifier=None, ClusterType=None, NodeType=None, MasterUsername=None,
                   MasterUserPassword=None, ClusterSecurityGroups=None, VpcSecurityGroupIds=None,
                   ClusterSubnetGroupName=None, AvailabilityZone=None, PreferredMaintenanceWindow=None,
                   ClusterParameterGroupName=None, AutomatedSnapshotRetentionPeriod=None, Port=None,
                   ClusterVersion=None, AllowVersionUpgrade=None, NumberOfNodes=None, PubliclyAccessible=None,
                   Encrypted=None, HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None, ElasticIp=None,
                   Tags=None, KmsKeyId=None, EnhancedVpcRouting=None, AdditionalInfo=None, IamRoles=None):
    """
    :param DBName: The name of the first database to be created when the cluster is created.
            To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to Create a Database in the Amazon Redshift Database Developer Guide.
            Default: dev
            Constraints:
            Must contain 1 to 64 alphanumeric characters.
            Must contain only lowercase letters.
            Cannot be a word that is reserved by the service. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.
            
    :type DBName: string
    :param ClusterIdentifier: [REQUIRED]
            A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            Alphabetic characters must be lowercase.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for all clusters within an AWS account.
            Example: myexamplecluster
            
    :type ClusterIdentifier: string
    :param ClusterType: The type of the cluster. When cluster type is specified as
            single-node , the NumberOfNodes parameter is not required.
            multi-node , the NumberOfNodes parameter is required.
            Valid Values: multi-node | single-node
            Default: multi-node
            
    :type ClusterType: string
    :param NodeType: [REQUIRED]
            The node type to be provisioned for the cluster. For information about node types, go to Working with Clusters in the Amazon Redshift Cluster Management Guide .
            Valid Values: ds1.xlarge | ds1.8xlarge | ds2.xlarge | ds2.8xlarge | dc1.large | dc1.8xlarge .
            
    :type NodeType: string
    :param MasterUsername: [REQUIRED]
            The user name associated with the master user account for the cluster that is being created.
            Constraints:
            Must be 1 - 128 alphanumeric characters.
            First character must be a letter.
            Cannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.
            
    :type MasterUsername: string
    :param MasterUserPassword: [REQUIRED]
            The password associated with the master user account for the cluster that is being created.
            Constraints:
            Must be between 8 and 64 characters in length.
            Must contain at least one uppercase letter.
            Must contain at least one lowercase letter.
            Must contain one number.
            Can be any printable ASCII character (ASCII code 33 to 126) except ' (single quote), ' (double quote), , /, @, or space.
            
    :type MasterUserPassword: string
    :param ClusterSecurityGroups: A list of security groups to be associated with this cluster.
            Default: The default cluster security group for Amazon Redshift.
            (string) --
            
    :type ClusterSecurityGroups: list
    :param VpcSecurityGroupIds: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
            Default: The default VPC security group is associated with the cluster.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param ClusterSubnetGroupName: The name of a cluster subnet group to be associated with this cluster.
            If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
            
    :type ClusterSubnetGroupName: string
    :param AvailabilityZone: The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.
            Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.
            Example: us-east-1d
            Constraint: The specified Availability Zone must be in the same region as the current endpoint.
            
    :type AvailabilityZone: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which automated cluster maintenance can occur.
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see Maintenance Windows in Amazon Redshift Cluster Management Guide.
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Minimum 30-minute window.
            
    :type PreferredMaintenanceWindow: string
    :param ClusterParameterGroupName: The name of the parameter group to be associated with this cluster.
            Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to Working with Amazon Redshift Parameter Groups
            Constraints:
            Must be 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            
    :type ClusterParameterGroupName: string
    :param AutomatedSnapshotRetentionPeriod: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with CreateClusterSnapshot .
            Default: 1
            Constraints: Must be a value from 0 to 35.
            
    :type AutomatedSnapshotRetentionPeriod: integer
    :param Port: The port number on which the cluster accepts incoming connections.
            The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.
            Default: 5439
            Valid Values: 1150-65535
            
    :type Port: integer
    :param ClusterVersion: The version of the Amazon Redshift engine software that you want to deploy on the cluster.
            The version selected runs on all the nodes in the cluster.
            Constraints: Only version 1.0 is currently available.
            Example: 1.0
            
    :type ClusterVersion: string
    :param AllowVersionUpgrade: If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.
            When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.
            Default: true
            
    :type AllowVersionUpgrade: boolean
    :param NumberOfNodes: The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node .
            For information about determining how many nodes you need, go to Working with Clusters in the Amazon Redshift Cluster Management Guide .
            If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.
            Default: 1
            Constraints: Value must be at least 1 and no more than 100.
            
    :type NumberOfNodes: integer
    :param PubliclyAccessible: If true , the cluster can be accessed from a public network.
    :type PubliclyAccessible: boolean
    :param Encrypted: If true , the data in the cluster is encrypted at rest.
            Default: false
            
    :type Encrypted: boolean
    :param HsmClientCertificateIdentifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
    :type HsmClientCertificateIdentifier: string
    :param HsmConfigurationIdentifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    :type HsmConfigurationIdentifier: string
    :param ElasticIp: The Elastic IP (EIP) address for the cluster.
            Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to Supported Platforms to Launch Your Cluster in the Amazon Redshift Cluster Management Guide.
            
    :type ElasticIp: string
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    :param KmsKeyId: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
    :type KmsKeyId: string
    :param EnhancedVpcRouting: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            
    :type EnhancedVpcRouting: boolean
    :param AdditionalInfo: Reserved.
    :type AdditionalInfo: string
    :param IamRoles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM roles in a single request.
            A cluster can have up to 10 IAM roles associated with it at any time.
            (string) --
            
    :type IamRoles: list
    """
    pass


def create_cluster_parameter_group(ParameterGroupName=None, ParameterGroupFamily=None, Description=None, Tags=None):
    """
    :param ParameterGroupName: [REQUIRED]
            The name of the cluster parameter group.
            Constraints:
            Must be 1 to 255 alphanumeric characters or hyphens
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique withing your AWS account.
            Note
            This value is stored as a lower-case string.
            
    :type ParameterGroupName: string
    :param ParameterGroupFamily: [REQUIRED]
            The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.
            To get a list of valid parameter group family names, you can call DescribeClusterParameterGroups . By default, Amazon Redshift returns a list of all the parameter groups that are owned by your AWS account, including the default parameter groups for each Amazon Redshift engine version. The parameter group family names associated with the default parameter groups provide you the valid values. For example, a valid family name is 'redshift-1.0'.
            
    :type ParameterGroupFamily: string
    :param Description: [REQUIRED]
            A description of the parameter group.
            
    :type Description: string
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    """
    pass


def create_cluster_security_group(ClusterSecurityGroupName=None, Description=None, Tags=None):
    """
    :param ClusterSecurityGroupName: [REQUIRED]
            The name for the security group. Amazon Redshift stores the value as a lowercase string.
            Constraints:
            Must contain no more than 255 alphanumeric characters or hyphens.
            Must not be 'Default'.
            Must be unique for all security groups that are created by your AWS account.
            Example: examplesecuritygroup
            
    :type ClusterSecurityGroupName: string
    :param Description: [REQUIRED]
            A description for the security group.
            
    :type Description: string
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    """
    pass


def create_cluster_snapshot(SnapshotIdentifier=None, ClusterIdentifier=None, Tags=None):
    """
    :param SnapshotIdentifier: [REQUIRED]
            A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the AWS account.
            Constraints:
            Cannot be null, empty, or blank
            Must contain from 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-snapshot-id
            
    :type SnapshotIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The cluster identifier for which you want a snapshot.
            
    :type ClusterIdentifier: string
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    """
    pass


def create_cluster_subnet_group(ClusterSubnetGroupName=None, Description=None, SubnetIds=None, Tags=None):
    """
    :param ClusterSubnetGroupName: [REQUIRED]
            The name for the subnet group. Amazon Redshift stores the value as a lowercase string.
            Constraints:
            Must contain no more than 255 alphanumeric characters or hyphens.
            Must not be 'Default'.
            Must be unique for all subnet groups that are created by your AWS account.
            Example: examplesubnetgroup
            
    :type ClusterSubnetGroupName: string
    :param Description: [REQUIRED]
            A description for the subnet group.
            
    :type Description: string
    :param SubnetIds: [REQUIRED]
            An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
            (string) --
            
    :type SubnetIds: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    """
    pass


def create_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, SourceIds=None,
                              EventCategories=None, Severity=None, Enabled=None, Tags=None):
    """
    :param SubscriptionName: [REQUIRED]
            The name of the event subscription to be created.
            Constraints:
            Cannot be null, empty, or blank.
            Must contain from 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            
    :type SubscriptionName: string
    :param SnsTopicArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
            
    :type SnsTopicArn: string
    :param SourceType: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account. You must specify a source type in order to specify source IDs.
            Valid values: cluster, cluster-parameter-group, cluster-security-group, and cluster-snapshot.
            
    :type SourceType: string
    :param SourceIds: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.
            Example: my-cluster-1, my-cluster-2
            Example: my-snapshot-20131010
            (string) --
            
    :type SourceIds: list
    :param EventCategories: Specifies the Amazon Redshift event categories to be published by the event notification subscription.
            Values: Configuration, Management, Monitoring, Security
            (string) --
            
    :type EventCategories: list
    :param Severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription.
            Values: ERROR, INFO
            
    :type Severity: string
    :param Enabled: A Boolean value; set to true to activate the subscription, set to false to create the subscription but not active it.
    :type Enabled: boolean
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    """
    pass


def create_hsm_client_certificate(HsmClientCertificateIdentifier=None, Tags=None):
    """
    :param HsmClientCertificateIdentifier: [REQUIRED]
            The identifier to be assigned to the new HSM client certificate that the cluster will use to connect to the HSM to use the database encryption keys.
            
    :type HsmClientCertificateIdentifier: string
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    """
    pass


def create_hsm_configuration(HsmConfigurationIdentifier=None, Description=None, HsmIpAddress=None,
                             HsmPartitionName=None, HsmPartitionPassword=None, HsmServerPublicCertificate=None,
                             Tags=None):
    """
    :param HsmConfigurationIdentifier: [REQUIRED]
            The identifier to be assigned to the new Amazon Redshift HSM configuration.
            
    :type HsmConfigurationIdentifier: string
    :param Description: [REQUIRED]
            A text description of the HSM configuration to be created.
            
    :type Description: string
    :param HsmIpAddress: [REQUIRED]
            The IP address that the Amazon Redshift cluster must use to access the HSM.
            
    :type HsmIpAddress: string
    :param HsmPartitionName: [REQUIRED]
            The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.
            
    :type HsmPartitionName: string
    :param HsmPartitionPassword: [REQUIRED]
            The password required to access the HSM partition.
            
    :type HsmPartitionPassword: string
    :param HsmServerPublicCertificate: [REQUIRED]
            The HSMs public certificate file. When using Cloud HSM, the file name is server.pem.
            
    :type HsmServerPublicCertificate: string
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    """
    pass


def create_snapshot_copy_grant(SnapshotCopyGrantName=None, KmsKeyId=None, Tags=None):
    """
    :param SnapshotCopyGrantName: [REQUIRED]
            The name of the snapshot copy grant. This name must be unique in the region for the AWS account.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            Alphabetic characters must be lowercase.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for all clusters within an AWS account.
            
    :type SnapshotCopyGrantName: string
    :param KmsKeyId: The unique identifier of the customer master key (CMK) to which to grant Amazon Redshift permission. If no key is specified, the default key is used.
    :type KmsKeyId: string
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    """
    pass


def create_tags(ResourceName=None, Tags=None):
    """
    :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) to which you want to add the tag or tags. For example, arn:aws:redshift:us-east-1:123456789:cluster:t1 .
            
    :type ResourceName: string
    :param Tags: [REQUIRED]
            One or more name/value pairs to add as tags to the specified resource. Each tag name is passed in with the parameter Key and the corresponding value is passed in with the parameter Value . The Key and Value parameters are separated by a comma (,). Separate multiple tags with a space. For example, --tags 'Key'='owner','Value'='admin' 'Key'='environment','Value'='test' 'Key'='version','Value'='1.0' .
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            
    :type Tags: list
    """
    pass


def delete_cluster(ClusterIdentifier=None, SkipFinalClusterSnapshot=None, FinalClusterSnapshotIdentifier=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster to be deleted.
            Constraints:
            Must contain lowercase characters.
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            
    :type ClusterIdentifier: string
    :param SkipFinalClusterSnapshot: Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted.
            Note
            The FinalClusterSnapshotIdentifier parameter must be specified if SkipFinalClusterSnapshot is false .
            Default: false
            
    :type SkipFinalClusterSnapshot: boolean
    :param FinalClusterSnapshotIdentifier: The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, SkipFinalClusterSnapshot must be false .
            Constraints:
            Must be 1 to 255 alphanumeric characters.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            
    :type FinalClusterSnapshotIdentifier: string
    """
    pass


def delete_cluster_parameter_group(ParameterGroupName=None):
    """
    :param ParameterGroupName: [REQUIRED]
            The name of the parameter group to be deleted.
            Constraints:
            Must be the name of an existing cluster parameter group.
            Cannot delete a default cluster parameter group.
            ReturnsNone
            
    :type ParameterGroupName: string
    """
    pass


def delete_cluster_security_group(ClusterSecurityGroupName=None):
    """
    :param ClusterSecurityGroupName: [REQUIRED]
            The name of the cluster security group to be deleted.
            ReturnsNone
            
    :type ClusterSecurityGroupName: string
    """
    pass


def delete_cluster_snapshot(SnapshotIdentifier=None, SnapshotClusterIdentifier=None):
    """
    :param SnapshotIdentifier: [REQUIRED]
            The unique identifier of the manual snapshot to be deleted.
            Constraints: Must be the name of an existing snapshot that is in the available state.
            
    :type SnapshotIdentifier: string
    :param SnapshotClusterIdentifier: The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
            Constraints: Must be the name of valid cluster.
            
    :type SnapshotClusterIdentifier: string
    """
    pass


def delete_cluster_subnet_group(ClusterSubnetGroupName=None):
    """
    :param ClusterSubnetGroupName: [REQUIRED]
            The name of the cluster subnet group name to be deleted.
            ReturnsNone
            
    :type ClusterSubnetGroupName: string
    """
    pass


def delete_event_subscription(SubscriptionName=None):
    """
    :param SubscriptionName: [REQUIRED]
            The name of the Amazon Redshift event notification subscription to be deleted.
            ReturnsNone
            
    :type SubscriptionName: string
    """
    pass


def delete_hsm_client_certificate(HsmClientCertificateIdentifier=None):
    """
    :param HsmClientCertificateIdentifier: [REQUIRED]
            The identifier of the HSM client certificate to be deleted.
            ReturnsNone
            
    :type HsmClientCertificateIdentifier: string
    """
    pass


def delete_hsm_configuration(HsmConfigurationIdentifier=None):
    """
    :param HsmConfigurationIdentifier: [REQUIRED]
            The identifier of the Amazon Redshift HSM configuration to be deleted.
            ReturnsNone
            
    :type HsmConfigurationIdentifier: string
    """
    pass


def delete_snapshot_copy_grant(SnapshotCopyGrantName=None):
    """
    :param SnapshotCopyGrantName: [REQUIRED]
            The name of the snapshot copy grant to delete.
            ReturnsNone
            
    :type SnapshotCopyGrantName: string
    """
    pass


def delete_tags(ResourceName=None, TagKeys=None):
    """
    :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) from which you want to remove the tag or tags. For example, arn:aws:redshift:us-east-1:123456789:cluster:t1 .
            
    :type ResourceName: string
    :param TagKeys: [REQUIRED]
            The tag key that you want to delete.
            (string) --
            
    :type TagKeys: list
    """
    pass


def describe_cluster_parameter_groups(ParameterGroupName=None, MaxRecords=None, Marker=None, TagKeys=None,
                                      TagValues=None):
    """
    :param ParameterGroupName: The name of a specific parameter group for which to return details. By default, details about all parameter groups and the default parameter group are returned.
    :type ParameterGroupName: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterParameterGroups request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    :param TagKeys: A tag key or keys for which you want to return all matching cluster parameter groups that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag keys associated with them.
            (string) --
            
    :type TagKeys: list
    :param TagValues: A tag value or values for which you want to return all matching cluster parameter groups that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag values associated with them.
            (string) --
            
    :type TagValues: list
    """
    pass


def describe_cluster_parameters(ParameterGroupName=None, Source=None, MaxRecords=None, Marker=None):
    """
    :param ParameterGroupName: [REQUIRED]
            The name of a cluster parameter group for which to return details.
            
    :type ParameterGroupName: string
    :param Source: The parameter types to return. Specify user to show parameters that are different form the default. Similarly, specify engine-default to show parameters that are the same as the default parameter group.
            Default: All parameter types returned.
            Valid Values: user | engine-default
            
    :type Source: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterParameters request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    """
    pass


def describe_cluster_security_groups(ClusterSecurityGroupName=None, MaxRecords=None, Marker=None, TagKeys=None,
                                     TagValues=None):
    """
    :param ClusterSecurityGroupName: The name of a cluster security group for which you are requesting details. You can specify either the Marker parameter or a ClusterSecurityGroupName parameter, but not both.
            Example: securitygroup1
            
    :type ClusterSecurityGroupName: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterSecurityGroups request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
            Constraints: You can specify either the ClusterSecurityGroupName parameter or the Marker parameter, but not both.
            
    :type Marker: string
    :param TagKeys: A tag key or keys for which you want to return all matching cluster security groups that are associated with the specified key or keys. For example, suppose that you have security groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag keys associated with them.
            (string) --
            
    :type TagKeys: list
    :param TagValues: A tag value or values for which you want to return all matching cluster security groups that are associated with the specified tag value or values. For example, suppose that you have security groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag values associated with them.
            (string) --
            
    :type TagValues: list
    """
    pass


def describe_cluster_snapshots(ClusterIdentifier=None, SnapshotIdentifier=None, SnapshotType=None, StartTime=None,
                               EndTime=None, MaxRecords=None, Marker=None, OwnerAccount=None, TagKeys=None,
                               TagValues=None):
    """
    :param ClusterIdentifier: The identifier of the cluster for which information about snapshots is requested.
    :type ClusterIdentifier: string
    :param SnapshotIdentifier: The snapshot identifier of the snapshot about which to return information.
    :type SnapshotIdentifier: string
    :param SnapshotType: The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.
            Valid Values: automated | manual
            
    :type SnapshotType: string
    :param StartTime: A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2012-07-16T18:00:00Z
            
    :type StartTime: datetime
    :param EndTime: A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2012-07-16T18:00:00Z
            
    :type EndTime: datetime
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterSnapshots request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    :param OwnerAccount: The AWS customer account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your AWS customer account, or do not specify the parameter.
    :type OwnerAccount: string
    :param TagKeys: A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.
            (string) --
            
    :type TagKeys: list
    :param TagValues: A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.
            (string) --
            
    :type TagValues: list
    """
    pass


def describe_cluster_subnet_groups(ClusterSubnetGroupName=None, MaxRecords=None, Marker=None, TagKeys=None,
                                   TagValues=None):
    """
    :param ClusterSubnetGroupName: The name of the cluster subnet group for which information is requested.
    :type ClusterSubnetGroupName: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterSubnetGroups request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    :param TagKeys: A tag key or keys for which you want to return all matching cluster subnet groups that are associated with the specified key or keys. For example, suppose that you have subnet groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag keys associated with them.
            (string) --
            
    :type TagKeys: list
    :param TagValues: A tag value or values for which you want to return all matching cluster subnet groups that are associated with the specified tag value or values. For example, suppose that you have subnet groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag values associated with them.
            (string) --
            
    :type TagValues: list
    """
    pass


def describe_cluster_versions(ClusterVersion=None, ClusterParameterGroupFamily=None, MaxRecords=None, Marker=None):
    """
    :param ClusterVersion: The specific cluster version to return.
            Example: 1.0
            
    :type ClusterVersion: string
    :param ClusterParameterGroupFamily: The name of a specific cluster parameter group family to return details for.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type ClusterParameterGroupFamily: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterVersions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    """
    pass


def describe_clusters(ClusterIdentifier=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    :param ClusterIdentifier: The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.
            The default is that all clusters defined for an account are returned.
            
    :type ClusterIdentifier: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusters request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
            Constraints: You can specify either the ClusterIdentifier parameter or the Marker parameter, but not both.
            
    :type Marker: string
    :param TagKeys: A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.
            (string) --
            
    :type TagKeys: list
    :param TagValues: A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.
            (string) --
            
    :type TagValues: list
    """
    pass


def describe_default_cluster_parameters(ParameterGroupFamily=None, MaxRecords=None, Marker=None):
    """
    :param ParameterGroupFamily: [REQUIRED]
            The name of the cluster parameter group family.
            
    :type ParameterGroupFamily: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeDefaultClusterParameters request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    """
    pass


def describe_event_categories(SourceType=None):
    """
    :param SourceType: The source type, such as cluster or parameter group, to which the described event categories apply.
            Valid values: cluster, cluster-snapshot, cluster-parameter-group, and cluster-security-group.
            Return typedict
            ReturnsResponse Syntax{
              'EventCategoriesMapList': [
                {
                  'SourceType': 'string',
                  'Events': [
                    {
                      'EventId': 'string',
                      'EventCategories': [
                        'string',
                      ],
                      'EventDescription': 'string',
                      'Severity': 'string'
                    },
                  ]
                },
              ]
            }
            Response Structure
            (dict) --
            EventCategoriesMapList (list) --A list of event categories descriptions.
            (dict) --Describes event categories.
            SourceType (string) --The source type, such as cluster or cluster-snapshot, that the returned categories belong to.
            Events (list) --The events in the event category.
            (dict) --Describes event information.
            EventId (string) --The identifier of an Amazon Redshift event.
            EventCategories (list) --The category of an Amazon Redshift event.
            (string) --
            EventDescription (string) --The description of an Amazon Redshift event.
            Severity (string) --The severity of the event.
            Values: ERROR, INFO
            
            
            
            
    :type SourceType: string
    """
    pass


def describe_event_subscriptions(SubscriptionName=None, MaxRecords=None, Marker=None):
    """
    :param SubscriptionName: The name of the Amazon Redshift event notification subscription to be described.
    :type SubscriptionName: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEventSubscriptions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    """
    pass


def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None,
                    MaxRecords=None, Marker=None):
    """
    :param SourceIdentifier: The identifier of the event source for which events will be returned. If this parameter is not specified, then all sources are included in the response.
            Constraints:
            If SourceIdentifier is supplied, SourceType must also be provided.
            Specify a cluster identifier when SourceType is cluster .
            Specify a cluster security group name when SourceType is cluster-security-group .
            Specify a cluster parameter group name when SourceType is cluster-parameter-group .
            Specify a cluster snapshot identifier when SourceType is cluster-snapshot .
            
    :type SourceIdentifier: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.
            Constraints:
            If SourceType is supplied, SourceIdentifier must also be provided.
            Specify cluster when SourceIdentifier is a cluster identifier.
            Specify cluster-security-group when SourceIdentifier is a cluster security group name.
            Specify cluster-parameter-group when SourceIdentifier is a cluster parameter group name.
            Specify cluster-snapshot when SourceIdentifier is a cluster snapshot identifier.
            
    :type SourceType: string
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2009-07-08T18:00Z
            
    :type StartTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2009-07-08T18:00Z
            
    :type EndTime: datetime
    :param Duration: The number of minutes prior to the time of the request for which to retrieve events. For example, if the request is sent at 18:00 and you specify a duration of 60, then only events which have occurred after 17:00 will be returned.
            Default: 60
            
    :type Duration: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEvents request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    """
    pass


def describe_hsm_client_certificates(HsmClientCertificateIdentifier=None, MaxRecords=None, Marker=None, TagKeys=None,
                                     TagValues=None):
    """
    :param HsmClientCertificateIdentifier: The identifier of a specific HSM client certificate for which you want information. If no identifier is specified, information is returned for all HSM client certificates owned by your AWS customer account.
    :type HsmClientCertificateIdentifier: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeHsmClientCertificates request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    :param TagKeys: A tag key or keys for which you want to return all matching HSM client certificates that are associated with the specified key or keys. For example, suppose that you have HSM client certificates that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag keys associated with them.
            (string) --
            
    :type TagKeys: list
    :param TagValues: A tag value or values for which you want to return all matching HSM client certificates that are associated with the specified tag value or values. For example, suppose that you have HSM client certificates that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag values associated with them.
            (string) --
            
    :type TagValues: list
    """
    pass


def describe_hsm_configurations(HsmConfigurationIdentifier=None, MaxRecords=None, Marker=None, TagKeys=None,
                                TagValues=None):
    """
    :param HsmConfigurationIdentifier: The identifier of a specific Amazon Redshift HSM configuration to be described. If no identifier is specified, information is returned for all HSM configurations owned by your AWS customer account.
    :type HsmConfigurationIdentifier: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeHsmConfigurations request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    :param TagKeys: A tag key or keys for which you want to return all matching HSM configurations that are associated with the specified key or keys. For example, suppose that you have HSM configurations that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag keys associated with them.
            (string) --
            
    :type TagKeys: list
    :param TagValues: A tag value or values for which you want to return all matching HSM configurations that are associated with the specified tag value or values. For example, suppose that you have HSM configurations that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag values associated with them.
            (string) --
            
    :type TagValues: list
    """
    pass


def describe_logging_status(ClusterIdentifier=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster from which to get the logging status.
            Example: examplecluster
            Return typedict
            ReturnsResponse Syntax{
              'LoggingEnabled': True|False,
              'BucketName': 'string',
              'S3KeyPrefix': 'string',
              'LastSuccessfulDeliveryTime': datetime(2015, 1, 1),
              'LastFailureTime': datetime(2015, 1, 1),
              'LastFailureMessage': 'string'
            }
            Response Structure
            (dict) --Describes the status of logging for a cluster.
            LoggingEnabled (boolean) --
            true if logging is on, false if logging is off.
            BucketName (string) --The name of the S3 bucket where the log files are stored.
            S3KeyPrefix (string) --The prefix applied to the log file names.
            LastSuccessfulDeliveryTime (datetime) --The last time that logs were delivered.
            LastFailureTime (datetime) --The last time when logs failed to be delivered.
            LastFailureMessage (string) --The message indicating that logs failed to be delivered.
            
            
    :type ClusterIdentifier: string
    """
    pass


def describe_orderable_cluster_options(ClusterVersion=None, NodeType=None, MaxRecords=None, Marker=None):
    """
    :param ClusterVersion: The version filter value. Specify this parameter to show only the available offerings matching the specified version.
            Default: All versions.
            Constraints: Must be one of the version returned from DescribeClusterVersions .
            
    :type ClusterVersion: string
    :param NodeType: The node type filter value. Specify this parameter to show only the available offerings matching the specified node type.
    :type NodeType: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeOrderableClusterOptions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    """
    pass


def describe_reserved_node_offerings(ReservedNodeOfferingId=None, MaxRecords=None, Marker=None):
    """
    :param ReservedNodeOfferingId: The unique identifier for the offering.
    :type ReservedNodeOfferingId: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeReservedNodeOfferings request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    """
    pass


def describe_reserved_nodes(ReservedNodeId=None, MaxRecords=None, Marker=None):
    """
    :param ReservedNodeId: Identifier for the node reservation.
    :type ReservedNodeId: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeReservedNodes request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    :type Marker: string
    """
    pass


def describe_resize(ClusterIdentifier=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of a cluster whose resize progress you are requesting. This parameter is case-sensitive.
            By default, resize operations for all clusters defined for an AWS account are returned.
            Return typedict
            ReturnsResponse Syntax{
              'TargetNodeType': 'string',
              'TargetNumberOfNodes': 123,
              'TargetClusterType': 'string',
              'Status': 'string',
              'ImportTablesCompleted': [
                'string',
              ],
              'ImportTablesInProgress': [
                'string',
              ],
              'ImportTablesNotStarted': [
                'string',
              ],
              'AvgResizeRateInMegaBytesPerSecond': 123.0,
              'TotalResizeDataInMegaBytes': 123,
              'ProgressInMegaBytes': 123,
              'ElapsedTimeInSeconds': 123,
              'EstimatedTimeToCompletionInSeconds': 123
            }
            Response Structure
            (dict) --Describes the result of a cluster resize operation.
            TargetNodeType (string) --The node type that the cluster will have after the resize operation is complete.
            TargetNumberOfNodes (integer) --The number of nodes that the cluster will have after the resize operation is complete.
            TargetClusterType (string) --The cluster type after the resize operation is complete.
            Valid Values: multi-node | single-node
            Status (string) --The status of the resize operation.
            Valid Values: NONE | IN_PROGRESS | FAILED | SUCCEEDED
            ImportTablesCompleted (list) --The names of tables that have been completely imported .
            Valid Values: List of table names.
            (string) --
            ImportTablesInProgress (list) --The names of tables that are being currently imported.
            Valid Values: List of table names.
            (string) --
            ImportTablesNotStarted (list) --The names of tables that have not been yet imported.
            Valid Values: List of table names
            (string) --
            AvgResizeRateInMegaBytesPerSecond (float) --The average rate of the resize operation over the last few minutes, measured in megabytes per second. After the resize operation completes, this value shows the average rate of the entire resize operation.
            TotalResizeDataInMegaBytes (integer) --The estimated total amount of data, in megabytes, on the cluster before the resize operation began.
            ProgressInMegaBytes (integer) --While the resize operation is in progress, this value shows the current amount of data, in megabytes, that has been processed so far. When the resize operation is complete, this value shows the total amount of data, in megabytes, on the cluster, which may be more or less than TotalResizeDataInMegaBytes (the estimated total amount of data before resize).
            ElapsedTimeInSeconds (integer) --The amount of seconds that have elapsed since the resize operation began. After the resize operation completes, this value shows the total actual time, in seconds, for the resize operation.
            EstimatedTimeToCompletionInSeconds (integer) --The estimated time remaining, in seconds, until the resize operation is complete. This value is calculated based on the average resize rate and the estimated amount of data remaining to be processed. Once the resize operation is complete, this value will be 0.
            
            
    :type ClusterIdentifier: string
    """
    pass


def describe_snapshot_copy_grants(SnapshotCopyGrantName=None, MaxRecords=None, Marker=None, TagKeys=None,
                                  TagValues=None):
    """
    :param SnapshotCopyGrantName: The name of the snapshot copy grant.
    :type SnapshotCopyGrantName: string
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeSnapshotCopyGrant request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
            Constraints: You can specify either the SnapshotCopyGrantName parameter or the Marker parameter, but not both.
            
    :type Marker: string
    :param TagKeys: A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
            (string) --
            
    :type TagKeys: list
    :param TagValues: A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
            (string) --
            
    :type TagValues: list
    """
    pass


def describe_table_restore_status(ClusterIdentifier=None, TableRestoreRequestId=None, MaxRecords=None, Marker=None):
    """
    :param ClusterIdentifier: The Amazon Redshift cluster that the table is being restored to.
    :type ClusterIdentifier: string
    :param TableRestoreRequestId: The identifier of the table restore request to return status for. If you don't specify a TableRestoreRequestId value, then DescribeTableRestoreStatus returns the status of all in-progress table restore requests.
    :type TableRestoreRequestId: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeTableRestoreStatus request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the MaxRecords parameter.
    :type Marker: string
    """
    pass


def describe_tags(ResourceName=None, ResourceType=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    :param ResourceName: The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, arn:aws:redshift:us-east-1:123456789:cluster:t1 .
    :type ResourceName: string
    :param ResourceType: The type of resource with which you want to view tags. Valid resource types are:
            Cluster
            CIDR/IP
            EC2 security group
            Snapshot
            Cluster security group
            Subnet group
            HSM connection
            HSM certificate
            Parameter group
            Snapshot copy grant
            For more information about Amazon Redshift resource types and constructing ARNs, go to Constructing an Amazon Redshift Amazon Resource Name (ARN) in the Amazon Redshift Cluster Management Guide.
            
    :type ResourceType: string
    :param MaxRecords: The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
    :type MaxRecords: integer
    :param Marker: A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the marker parameter and retrying the command. If the marker field is empty, all response records have been retrieved for the request.
    :type Marker: string
    :param TagKeys: A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
            (string) --
            
    :type TagKeys: list
    :param TagValues: A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
            (string) --
            
    :type TagValues: list
    """
    pass


def disable_logging(ClusterIdentifier=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster on which logging is to be stopped.
            Example: examplecluster
            Return typedict
            ReturnsResponse Syntax{
              'LoggingEnabled': True|False,
              'BucketName': 'string',
              'S3KeyPrefix': 'string',
              'LastSuccessfulDeliveryTime': datetime(2015, 1, 1),
              'LastFailureTime': datetime(2015, 1, 1),
              'LastFailureMessage': 'string'
            }
            Response Structure
            (dict) --Describes the status of logging for a cluster.
            LoggingEnabled (boolean) --
            true if logging is on, false if logging is off.
            BucketName (string) --The name of the S3 bucket where the log files are stored.
            S3KeyPrefix (string) --The prefix applied to the log file names.
            LastSuccessfulDeliveryTime (datetime) --The last time that logs were delivered.
            LastFailureTime (datetime) --The last time when logs failed to be delivered.
            LastFailureMessage (string) --The message indicating that logs failed to be delivered.
            
            
    :type ClusterIdentifier: string
    """
    pass


def disable_snapshot_copy(ClusterIdentifier=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the source cluster that you want to disable copying of snapshots to a destination region.
            Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.
            Return typedict
            ReturnsResponse Syntax{
              'Cluster': {
                'ClusterIdentifier': 'string',
                'NodeType': 'string',
                'ClusterStatus': 'string',
                'ModifyStatus': 'string',
                'MasterUsername': 'string',
                'DBName': 'string',
                'Endpoint': {
                  'Address': 'string',
                  'Port': 123
                },
                'ClusterCreateTime': datetime(2015, 1, 1),
                'AutomatedSnapshotRetentionPeriod': 123,
                'ClusterSecurityGroups': [
                  {
                    'ClusterSecurityGroupName': 'string',
                    'Status': 'string'
                  },
                ],
                'VpcSecurityGroups': [
                  {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                  },
                ],
                'ClusterParameterGroups': [
                  {
                    'ParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'ClusterParameterStatusList': [
                      {
                        'ParameterName': 'string',
                        'ParameterApplyStatus': 'string',
                        'ParameterApplyErrorDescription': 'string'
                      },
                    ]
                  },
                ],
                'ClusterSubnetGroupName': 'string',
                'VpcId': 'string',
                'AvailabilityZone': 'string',
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                  'MasterUserPassword': 'string',
                  'NodeType': 'string',
                  'NumberOfNodes': 123,
                  'ClusterType': 'string',
                  'ClusterVersion': 'string',
                  'AutomatedSnapshotRetentionPeriod': 123,
                  'ClusterIdentifier': 'string',
                  'PubliclyAccessible': True|False,
                  'EnhancedVpcRouting': True|False
                },
                'ClusterVersion': 'string',
                'AllowVersionUpgrade': True|False,
                'NumberOfNodes': 123,
                'PubliclyAccessible': True|False,
                'Encrypted': True|False,
                'RestoreStatus': {
                  'Status': 'string',
                  'CurrentRestoreRateInMegaBytesPerSecond': 123.0,
                  'SnapshotSizeInMegaBytes': 123,
                  'ProgressInMegaBytes': 123,
                  'ElapsedTimeInSeconds': 123,
                  'EstimatedTimeToCompletionInSeconds': 123
                },
                'HsmStatus': {
                  'HsmClientCertificateIdentifier': 'string',
                  'HsmConfigurationIdentifier': 'string',
                  'Status': 'string'
                },
                'ClusterSnapshotCopyStatus': {
                  'DestinationRegion': 'string',
                  'RetentionPeriod': 123,
                  'SnapshotCopyGrantName': 'string'
                },
                'ClusterPublicKey': 'string',
                'ClusterNodes': [
                  {
                    'NodeRole': 'string',
                    'PrivateIPAddress': 'string',
                    'PublicIPAddress': 'string'
                  },
                ],
                'ElasticIpStatus': {
                  'ElasticIp': 'string',
                  'Status': 'string'
                },
                'ClusterRevisionNumber': 'string',
                'Tags': [
                  {
                    'Key': 'string',
                    'Value': 'string'
                  },
                ],
                'KmsKeyId': 'string',
                'EnhancedVpcRouting': True|False,
                'IamRoles': [
                  {
                    'IamRoleArn': 'string',
                    'ApplyStatus': 'string'
                  },
                ]
              }
            }
            Response Structure
            (dict) --
            Cluster (dict) --Describes a cluster.
            ClusterIdentifier (string) --The unique identifier of the cluster.
            NodeType (string) --The node type for the nodes in the cluster.
            ClusterStatus (string) --The current state of the cluster. Possible values are the following:
            available
            creating
            deleting
            final-snapshot
            hardware-failure
            incompatible-hsm
            incompatible-network
            incompatible-parameters
            incompatible-restore
            modifying
            rebooting
            renaming
            resizing
            rotating-keys
            storage-full
            updating-hsm
            ModifyStatus (string) --The status of a modify operation, if any, initiated for the cluster.
            MasterUsername (string) --The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.
            DBName (string) --The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.
            Endpoint (dict) --The connection endpoint.
            Address (string) --The DNS address of the Cluster.
            Port (integer) --The port that the database engine is listening on.
            ClusterCreateTime (datetime) --The date and time that the cluster was created.
            AutomatedSnapshotRetentionPeriod (integer) --The number of days that automatic cluster snapshots are retained.
            ClusterSecurityGroups (list) --A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
            Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.
            (dict) --Describes a cluster security group.
            ClusterSecurityGroupName (string) --The name of the cluster security group.
            Status (string) --The status of the cluster security group.
            
            VpcSecurityGroups (list) --A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
            (dict) --Describes the members of a VPC security group.
            VpcSecurityGroupId (string) --The identifier of the VPC security group.
            Status (string) --The status of the VPC security group.
            
            ClusterParameterGroups (list) --The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
            (dict) --Describes the status of a parameter group.
            ParameterGroupName (string) --The name of the cluster parameter group.
            ParameterApplyStatus (string) --The status of parameter updates.
            ClusterParameterStatusList (list) --The list of parameter statuses.
            For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
            (dict) --Describes the status of a parameter group.
            ParameterName (string) --The name of the parameter.
            ParameterApplyStatus (string) --The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
            The following are possible statuses and descriptions.
            in-sync : The parameter value is in sync with the database.
            pending-reboot : The parameter value will be applied after the cluster reboots.
            applying : The parameter value is being applied to the database.
            invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
            apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
            apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
            unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.
            ParameterApplyErrorDescription (string) --The error that prevented the parameter from being applied to the database.
            
            
            ClusterSubnetGroupName (string) --The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
            VpcId (string) --The identifier of the VPC the cluster is in, if the cluster is in a VPC.
            AvailabilityZone (string) --The name of the Availability Zone in which the cluster is located.
            PreferredMaintenanceWindow (string) --The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
            PendingModifiedValues (dict) --A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
            MasterUserPassword (string) --The pending or in-progress change of the master user password for the cluster.
            NodeType (string) --The pending or in-progress change of the cluster's node type.
            NumberOfNodes (integer) --The pending or in-progress change of the number of nodes in the cluster.
            ClusterType (string) --The pending or in-progress change of the cluster type.
            ClusterVersion (string) --The pending or in-progress change of the service version.
            AutomatedSnapshotRetentionPeriod (integer) --The pending or in-progress change of the automated snapshot retention period.
            ClusterIdentifier (string) --The pending or in-progress change of the new identifier for the cluster.
            PubliclyAccessible (boolean) --The pending or in-progress change of the ability to connect to the cluster from the public network.
            EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            ClusterVersion (string) --The version ID of the Amazon Redshift engine that is running on the cluster.
            AllowVersionUpgrade (boolean) --A Boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.
            NumberOfNodes (integer) --The number of compute nodes in the cluster.
            PubliclyAccessible (boolean) --A Boolean value that, if true , indicates that the cluster can be accessed from a public network.
            Encrypted (boolean) --A Boolean value that, if true , indicates that data in the cluster is encrypted at rest.
            RestoreStatus (dict) --A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
            Status (string) --The status of the restore action. Returns starting, restoring, completed, or failed.
            CurrentRestoreRateInMegaBytesPerSecond (float) --The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
            SnapshotSizeInMegaBytes (integer) --The size of the set of snapshot data used to restore the cluster.
            ProgressInMegaBytes (integer) --The number of megabytes that have been transferred from snapshot storage.
            ElapsedTimeInSeconds (integer) --The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
            EstimatedTimeToCompletionInSeconds (integer) --The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
            HsmStatus (dict) --A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
            Values: active, applying
            HsmClientCertificateIdentifier (string) --Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
            HsmConfigurationIdentifier (string) --Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
            Status (string) --Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
            Values: active, applying
            ClusterSnapshotCopyStatus (dict) --A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
            DestinationRegion (string) --The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
            RetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
            SnapshotCopyGrantName (string) --The name of the snapshot copy grant.
            ClusterPublicKey (string) --The public key for the cluster.
            ClusterNodes (list) --The nodes in the cluster.
            (dict) --The identifier of a node in a cluster.
            NodeRole (string) --Whether the node is a leader node or a compute node.
            PrivateIPAddress (string) --The private IP address of a node within a cluster.
            PublicIPAddress (string) --The public IP address of a node within a cluster.
            
            ElasticIpStatus (dict) --The status of the elastic IP (EIP) address.
            ElasticIp (string) --The elastic IP (EIP) address for the cluster.
            Status (string) --The status of the elastic IP (EIP) address.
            ClusterRevisionNumber (string) --The specific revision number of the database in the cluster.
            Tags (list) --The list of tags for the cluster.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
            EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            IamRoles (list) --A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
            (dict) --An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
            IamRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .
            ApplyStatus (string) --A value that describes the status of the IAM role's association with an Amazon Redshift cluster.
            The following are possible statuses and descriptions.
            in-sync : The role is available for use by the cluster.
            adding : The role is in the process of being associated with the cluster.
            removing : The role is in the process of being disassociated with the cluster.
            
            
            
            
    :type ClusterIdentifier: string
    """
    pass


def enable_logging(ClusterIdentifier=None, BucketName=None, S3KeyPrefix=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster on which logging is to be started.
            Example: examplecluster
            
    :type ClusterIdentifier: string
    :param BucketName: [REQUIRED]
            The name of an existing S3 bucket where the log files are to be stored.
            Constraints:
            Must be in the same region as the cluster
            The cluster must have read bucket and put object permissions
            
    :type BucketName: string
    :param S3KeyPrefix: The prefix applied to the log file names.
            Constraints:
            Cannot exceed 512 characters
            Cannot contain spaces( ), double quotes ('), single quotes ('), a backslash (), or control characters. The hexadecimal codes for invalid characters are:
            x00 to x20
            x22
            x27
            x5c
            x7f or larger
            
    :type S3KeyPrefix: string
    """
    pass


def enable_snapshot_copy(ClusterIdentifier=None, DestinationRegion=None, RetentionPeriod=None,
                         SnapshotCopyGrantName=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the source cluster to copy snapshots from.
            Constraints: Must be the valid name of an existing cluster that does not already have cross-region snapshot copy enabled.
            
    :type ClusterIdentifier: string
    :param DestinationRegion: [REQUIRED]
            The destination region that you want to copy snapshots to.
            Constraints: Must be the name of a valid region. For more information, see Regions and Endpoints in the Amazon Web Services General Reference.
            
    :type DestinationRegion: string
    :param RetentionPeriod: The number of days to retain automated snapshots in the destination region after they are copied from the source region.
            Default: 7.
            Constraints: Must be at least 1 and no more than 35.
            
    :type RetentionPeriod: integer
    :param SnapshotCopyGrantName: The name of the snapshot copy grant to use when snapshots of an AWS KMS-encrypted cluster are copied to the destination region.
    :type SnapshotCopyGrantName: string
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


def modify_cluster(ClusterIdentifier=None, ClusterType=None, NodeType=None, NumberOfNodes=None,
                   ClusterSecurityGroups=None, VpcSecurityGroupIds=None, MasterUserPassword=None,
                   ClusterParameterGroupName=None, AutomatedSnapshotRetentionPeriod=None,
                   PreferredMaintenanceWindow=None, ClusterVersion=None, AllowVersionUpgrade=None,
                   HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None, NewClusterIdentifier=None,
                   PubliclyAccessible=None, ElasticIp=None, EnhancedVpcRouting=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the cluster to be modified.
            Example: examplecluster
            
    :type ClusterIdentifier: string
    :param ClusterType: The new cluster type.
            When you submit your cluster resize request, your existing cluster goes into a read-only mode. After Amazon Redshift provisions a new cluster based on your resize requirements, there will be outage for a period while the old cluster is deleted and your connection is switched to the new cluster. You can use DescribeResize to track the progress of the resize request.
            Valid Values: multi-node | single-node
            
    :type ClusterType: string
    :param NodeType: The new node type of the cluster. If you specify a new node type, you must also specify the number of nodes parameter.
            When you submit your request to resize a cluster, Amazon Redshift sets access permissions for the cluster to read-only. After Amazon Redshift provisions a new cluster according to your resize requirements, there will be a temporary outage while the old cluster is deleted and your connection is switched to the new cluster. When the new connection is complete, the original access permissions for the cluster are restored. You can use DescribeResize to track the progress of the resize request.
            Valid Values: ds1.xlarge | ds1.8xlarge | ds2.xlarge | ds2.8xlarge | dc1.large | dc1.8xlarge .
            
    :type NodeType: string
    :param NumberOfNodes: The new number of nodes of the cluster. If you specify a new number of nodes, you must also specify the node type parameter.
            When you submit your request to resize a cluster, Amazon Redshift sets access permissions for the cluster to read-only. After Amazon Redshift provisions a new cluster according to your resize requirements, there will be a temporary outage while the old cluster is deleted and your connection is switched to the new cluster. When the new connection is complete, the original access permissions for the cluster are restored. You can use DescribeResize to track the progress of the resize request.
            Valid Values: Integer greater than 0 .
            
    :type NumberOfNodes: integer
    :param ClusterSecurityGroups: A list of cluster security groups to be authorized on this cluster. This change is asynchronously applied as soon as possible.
            Security groups currently associated with the cluster, and not in the list of groups to apply, will be revoked from the cluster.
            Constraints:
            Must be 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            (string) --
            
    :type ClusterSecurityGroups: list
    :param VpcSecurityGroupIds: A list of virtual private cloud (VPC) security groups to be associated with the cluster.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param MasterUserPassword: The new password for the cluster master user. This change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the MasterUserPassword element exists in the PendingModifiedValues element of the operation response.
            Note
            Operations never return the password, so this operation provides a way to regain access to the master user account for a cluster if the password is lost.
            Default: Uses existing setting.
            Constraints:
            Must be between 8 and 64 characters in length.
            Must contain at least one uppercase letter.
            Must contain at least one lowercase letter.
            Must contain one number.
            Can be any printable ASCII character (ASCII code 33 to 126) except ' (single quote), ' (double quote), , /, @, or space.
            
    :type MasterUserPassword: string
    :param ClusterParameterGroupName: The name of the cluster parameter group to apply to this cluster. This change is applied only after the cluster is rebooted. To reboot a cluster use RebootCluster .
            Default: Uses existing setting.
            Constraints: The cluster parameter group must be in the same parameter group family that matches the cluster version.
            
    :type ClusterParameterGroupName: string
    :param AutomatedSnapshotRetentionPeriod: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with CreateClusterSnapshot .
            If you decrease the automated snapshot retention period from its current value, existing automated snapshots that fall outside of the new retention period will be immediately deleted.
            Default: Uses existing setting.
            Constraints: Must be a value from 0 to 35.
            
    :type AutomatedSnapshotRetentionPeriod: integer
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, if necessary. If system maintenance is necessary during the window, it may result in an outage.
            This maintenance window change is made immediately. If the new maintenance window indicates the current time, there must be at least 120 minutes between the current time and end of the window in order to ensure that pending changes are applied.
            Default: Uses existing setting.
            Format: ddd:hh24:mi-ddd:hh24:mi, for example wed:07:30-wed:08:00 .
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Must be at least 30 minutes.
            
    :type PreferredMaintenanceWindow: string
    :param ClusterVersion: The new version number of the Amazon Redshift engine to upgrade to.
            For major version upgrades, if a non-default cluster parameter group is currently in use, a new cluster parameter group in the cluster parameter group family for the new version must be specified. The new cluster parameter group can be the default for that cluster parameter group family. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
            Example: 1.0
            
    :type ClusterVersion: string
    :param AllowVersionUpgrade: If true , major version upgrades will be applied automatically to the cluster during the maintenance window.
            Default: false
            
    :type AllowVersionUpgrade: boolean
    :param HsmClientCertificateIdentifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
    :type HsmClientCertificateIdentifier: string
    :param HsmConfigurationIdentifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    :type HsmConfigurationIdentifier: string
    :param NewClusterIdentifier: The new identifier for the cluster.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            Alphabetic characters must be lowercase.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for all clusters within an AWS account.
            Example: examplecluster
            
    :type NewClusterIdentifier: string
    :param PubliclyAccessible: If true , the cluster can be accessed from a public network. Only clusters in VPCs can be set to be publicly available.
    :type PubliclyAccessible: boolean
    :param ElasticIp: The Elastic IP (EIP) address for the cluster.
            Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to Supported Platforms to Launch Your Cluster in the Amazon Redshift Cluster Management Guide.
            
    :type ElasticIp: string
    :param EnhancedVpcRouting: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            
    :type EnhancedVpcRouting: boolean
    """
    pass


def modify_cluster_iam_roles(ClusterIdentifier=None, AddIamRoles=None, RemoveIamRoles=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the cluster for which you want to associate or disassociate IAM roles.
            
    :type ClusterIdentifier: string
    :param AddIamRoles: Zero or more IAM roles to associate with the cluster. The roles must be in their Amazon Resource Name (ARN) format. You can associate up to 10 IAM roles with a single cluster in a single request.
            (string) --
            
    :type AddIamRoles: list
    :param RemoveIamRoles: Zero or more IAM roles in ARN format to disassociate from the cluster. You can disassociate up to 10 IAM roles from a single cluster in a single request.
            (string) --
            
    :type RemoveIamRoles: list
    """
    pass


def modify_cluster_parameter_group(ParameterGroupName=None, Parameters=None):
    """
    :param ParameterGroupName: [REQUIRED]
            The name of the parameter group to be modified.
            
    :type ParameterGroupName: string
    :param Parameters: [REQUIRED]
            An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
            For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.
            For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.
            (dict) --Describes a parameter in a cluster parameter group.
            ParameterName (string) --The name of the parameter.
            ParameterValue (string) --The value of the parameter.
            Description (string) --A description of the parameter.
            Source (string) --The source of the parameter value, such as 'engine-default' or 'user'.
            DataType (string) --The data type of the parameter.
            AllowedValues (string) --The valid range of values for the parameter.
            ApplyType (string) --Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
            IsModifiable (boolean) --If true , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            
            
    :type Parameters: list
    """
    pass


def modify_cluster_subnet_group(ClusterSubnetGroupName=None, Description=None, SubnetIds=None):
    """
    :param ClusterSubnetGroupName: [REQUIRED]
            The name of the subnet group to be modified.
            
    :type ClusterSubnetGroupName: string
    :param Description: A text description of the subnet group to be modified.
    :type Description: string
    :param SubnetIds: [REQUIRED]
            An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
            (string) --
            
    :type SubnetIds: list
    """
    pass


def modify_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, SourceIds=None,
                              EventCategories=None, Severity=None, Enabled=None):
    """
    :param SubscriptionName: [REQUIRED]
            The name of the modified Amazon Redshift event notification subscription.
            
    :type SubscriptionName: string
    :param SnsTopicArn: The Amazon Resource Name (ARN) of the SNS topic to be used by the event notification subscription.
    :type SnsTopicArn: string
    :param SourceType: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account. You must specify a source type in order to specify source IDs.
            Valid values: cluster, cluster-parameter-group, cluster-security-group, and cluster-snapshot.
            
    :type SourceType: string
    :param SourceIds: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.
            Example: my-cluster-1, my-cluster-2
            Example: my-snapshot-20131010
            (string) --
            
    :type SourceIds: list
    :param EventCategories: Specifies the Amazon Redshift event categories to be published by the event notification subscription.
            Values: Configuration, Management, Monitoring, Security
            (string) --
            
    :type EventCategories: list
    :param Severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription.
            Values: ERROR, INFO
            
    :type Severity: string
    :param Enabled: A Boolean value indicating if the subscription is enabled. true indicates the subscription is enabled
    :type Enabled: boolean
    """
    pass


def modify_snapshot_copy_retention_period(ClusterIdentifier=None, RetentionPeriod=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the cluster for which you want to change the retention period for automated snapshots that are copied to a destination region.
            Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.
            
    :type ClusterIdentifier: string
    :param RetentionPeriod: [REQUIRED]
            The number of days to retain automated snapshots in the destination region after they are copied from the source region.
            If you decrease the retention period for automated snapshots that are copied to a destination region, Amazon Redshift will delete any existing automated snapshots that were copied to the destination region and that fall outside of the new retention period.
            Constraints: Must be at least 1 and no more than 35.
            
    :type RetentionPeriod: integer
    """
    pass


def purchase_reserved_node_offering(ReservedNodeOfferingId=None, NodeCount=None):
    """
    :param ReservedNodeOfferingId: [REQUIRED]
            The unique identifier of the reserved node offering you want to purchase.
            
    :type ReservedNodeOfferingId: string
    :param NodeCount: The number of reserved nodes that you want to purchase.
            Default: 1
            
    :type NodeCount: integer
    """
    pass


def reboot_cluster(ClusterIdentifier=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The cluster identifier.
            Return typedict
            ReturnsResponse Syntax{
              'Cluster': {
                'ClusterIdentifier': 'string',
                'NodeType': 'string',
                'ClusterStatus': 'string',
                'ModifyStatus': 'string',
                'MasterUsername': 'string',
                'DBName': 'string',
                'Endpoint': {
                  'Address': 'string',
                  'Port': 123
                },
                'ClusterCreateTime': datetime(2015, 1, 1),
                'AutomatedSnapshotRetentionPeriod': 123,
                'ClusterSecurityGroups': [
                  {
                    'ClusterSecurityGroupName': 'string',
                    'Status': 'string'
                  },
                ],
                'VpcSecurityGroups': [
                  {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                  },
                ],
                'ClusterParameterGroups': [
                  {
                    'ParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'ClusterParameterStatusList': [
                      {
                        'ParameterName': 'string',
                        'ParameterApplyStatus': 'string',
                        'ParameterApplyErrorDescription': 'string'
                      },
                    ]
                  },
                ],
                'ClusterSubnetGroupName': 'string',
                'VpcId': 'string',
                'AvailabilityZone': 'string',
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                  'MasterUserPassword': 'string',
                  'NodeType': 'string',
                  'NumberOfNodes': 123,
                  'ClusterType': 'string',
                  'ClusterVersion': 'string',
                  'AutomatedSnapshotRetentionPeriod': 123,
                  'ClusterIdentifier': 'string',
                  'PubliclyAccessible': True|False,
                  'EnhancedVpcRouting': True|False
                },
                'ClusterVersion': 'string',
                'AllowVersionUpgrade': True|False,
                'NumberOfNodes': 123,
                'PubliclyAccessible': True|False,
                'Encrypted': True|False,
                'RestoreStatus': {
                  'Status': 'string',
                  'CurrentRestoreRateInMegaBytesPerSecond': 123.0,
                  'SnapshotSizeInMegaBytes': 123,
                  'ProgressInMegaBytes': 123,
                  'ElapsedTimeInSeconds': 123,
                  'EstimatedTimeToCompletionInSeconds': 123
                },
                'HsmStatus': {
                  'HsmClientCertificateIdentifier': 'string',
                  'HsmConfigurationIdentifier': 'string',
                  'Status': 'string'
                },
                'ClusterSnapshotCopyStatus': {
                  'DestinationRegion': 'string',
                  'RetentionPeriod': 123,
                  'SnapshotCopyGrantName': 'string'
                },
                'ClusterPublicKey': 'string',
                'ClusterNodes': [
                  {
                    'NodeRole': 'string',
                    'PrivateIPAddress': 'string',
                    'PublicIPAddress': 'string'
                  },
                ],
                'ElasticIpStatus': {
                  'ElasticIp': 'string',
                  'Status': 'string'
                },
                'ClusterRevisionNumber': 'string',
                'Tags': [
                  {
                    'Key': 'string',
                    'Value': 'string'
                  },
                ],
                'KmsKeyId': 'string',
                'EnhancedVpcRouting': True|False,
                'IamRoles': [
                  {
                    'IamRoleArn': 'string',
                    'ApplyStatus': 'string'
                  },
                ]
              }
            }
            Response Structure
            (dict) --
            Cluster (dict) --Describes a cluster.
            ClusterIdentifier (string) --The unique identifier of the cluster.
            NodeType (string) --The node type for the nodes in the cluster.
            ClusterStatus (string) --The current state of the cluster. Possible values are the following:
            available
            creating
            deleting
            final-snapshot
            hardware-failure
            incompatible-hsm
            incompatible-network
            incompatible-parameters
            incompatible-restore
            modifying
            rebooting
            renaming
            resizing
            rotating-keys
            storage-full
            updating-hsm
            ModifyStatus (string) --The status of a modify operation, if any, initiated for the cluster.
            MasterUsername (string) --The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.
            DBName (string) --The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.
            Endpoint (dict) --The connection endpoint.
            Address (string) --The DNS address of the Cluster.
            Port (integer) --The port that the database engine is listening on.
            ClusterCreateTime (datetime) --The date and time that the cluster was created.
            AutomatedSnapshotRetentionPeriod (integer) --The number of days that automatic cluster snapshots are retained.
            ClusterSecurityGroups (list) --A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
            Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.
            (dict) --Describes a cluster security group.
            ClusterSecurityGroupName (string) --The name of the cluster security group.
            Status (string) --The status of the cluster security group.
            
            VpcSecurityGroups (list) --A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
            (dict) --Describes the members of a VPC security group.
            VpcSecurityGroupId (string) --The identifier of the VPC security group.
            Status (string) --The status of the VPC security group.
            
            ClusterParameterGroups (list) --The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
            (dict) --Describes the status of a parameter group.
            ParameterGroupName (string) --The name of the cluster parameter group.
            ParameterApplyStatus (string) --The status of parameter updates.
            ClusterParameterStatusList (list) --The list of parameter statuses.
            For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
            (dict) --Describes the status of a parameter group.
            ParameterName (string) --The name of the parameter.
            ParameterApplyStatus (string) --The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
            The following are possible statuses and descriptions.
            in-sync : The parameter value is in sync with the database.
            pending-reboot : The parameter value will be applied after the cluster reboots.
            applying : The parameter value is being applied to the database.
            invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
            apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
            apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
            unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.
            ParameterApplyErrorDescription (string) --The error that prevented the parameter from being applied to the database.
            
            
            ClusterSubnetGroupName (string) --The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
            VpcId (string) --The identifier of the VPC the cluster is in, if the cluster is in a VPC.
            AvailabilityZone (string) --The name of the Availability Zone in which the cluster is located.
            PreferredMaintenanceWindow (string) --The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
            PendingModifiedValues (dict) --A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
            MasterUserPassword (string) --The pending or in-progress change of the master user password for the cluster.
            NodeType (string) --The pending or in-progress change of the cluster's node type.
            NumberOfNodes (integer) --The pending or in-progress change of the number of nodes in the cluster.
            ClusterType (string) --The pending or in-progress change of the cluster type.
            ClusterVersion (string) --The pending or in-progress change of the service version.
            AutomatedSnapshotRetentionPeriod (integer) --The pending or in-progress change of the automated snapshot retention period.
            ClusterIdentifier (string) --The pending or in-progress change of the new identifier for the cluster.
            PubliclyAccessible (boolean) --The pending or in-progress change of the ability to connect to the cluster from the public network.
            EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            ClusterVersion (string) --The version ID of the Amazon Redshift engine that is running on the cluster.
            AllowVersionUpgrade (boolean) --A Boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.
            NumberOfNodes (integer) --The number of compute nodes in the cluster.
            PubliclyAccessible (boolean) --A Boolean value that, if true , indicates that the cluster can be accessed from a public network.
            Encrypted (boolean) --A Boolean value that, if true , indicates that data in the cluster is encrypted at rest.
            RestoreStatus (dict) --A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
            Status (string) --The status of the restore action. Returns starting, restoring, completed, or failed.
            CurrentRestoreRateInMegaBytesPerSecond (float) --The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
            SnapshotSizeInMegaBytes (integer) --The size of the set of snapshot data used to restore the cluster.
            ProgressInMegaBytes (integer) --The number of megabytes that have been transferred from snapshot storage.
            ElapsedTimeInSeconds (integer) --The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
            EstimatedTimeToCompletionInSeconds (integer) --The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
            HsmStatus (dict) --A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
            Values: active, applying
            HsmClientCertificateIdentifier (string) --Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
            HsmConfigurationIdentifier (string) --Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
            Status (string) --Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
            Values: active, applying
            ClusterSnapshotCopyStatus (dict) --A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
            DestinationRegion (string) --The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
            RetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
            SnapshotCopyGrantName (string) --The name of the snapshot copy grant.
            ClusterPublicKey (string) --The public key for the cluster.
            ClusterNodes (list) --The nodes in the cluster.
            (dict) --The identifier of a node in a cluster.
            NodeRole (string) --Whether the node is a leader node or a compute node.
            PrivateIPAddress (string) --The private IP address of a node within a cluster.
            PublicIPAddress (string) --The public IP address of a node within a cluster.
            
            ElasticIpStatus (dict) --The status of the elastic IP (EIP) address.
            ElasticIp (string) --The elastic IP (EIP) address for the cluster.
            Status (string) --The status of the elastic IP (EIP) address.
            ClusterRevisionNumber (string) --The specific revision number of the database in the cluster.
            Tags (list) --The list of tags for the cluster.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
            EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            IamRoles (list) --A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
            (dict) --An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
            IamRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .
            ApplyStatus (string) --A value that describes the status of the IAM role's association with an Amazon Redshift cluster.
            The following are possible statuses and descriptions.
            in-sync : The role is available for use by the cluster.
            adding : The role is in the process of being associated with the cluster.
            removing : The role is in the process of being disassociated with the cluster.
            
            
            
            
    :type ClusterIdentifier: string
    """
    pass


def reset_cluster_parameter_group(ParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    :param ParameterGroupName: [REQUIRED]
            The name of the cluster parameter group to be reset.
            
    :type ParameterGroupName: string
    :param ResetAllParameters: If true , all parameters in the specified parameter group will be reset to their default values.
            Default: true
            
    :type ResetAllParameters: boolean
    :param Parameters: An array of names of parameters to be reset. If ResetAllParameters option is not used, then at least one parameter name must be supplied.
            Constraints: A maximum of 20 parameters can be reset in a single request.
            (dict) --Describes a parameter in a cluster parameter group.
            ParameterName (string) --The name of the parameter.
            ParameterValue (string) --The value of the parameter.
            Description (string) --A description of the parameter.
            Source (string) --The source of the parameter value, such as 'engine-default' or 'user'.
            DataType (string) --The data type of the parameter.
            AllowedValues (string) --The valid range of values for the parameter.
            ApplyType (string) --Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
            IsModifiable (boolean) --If true , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            
            
    :type Parameters: list
    """
    pass


def restore_from_cluster_snapshot(ClusterIdentifier=None, SnapshotIdentifier=None, SnapshotClusterIdentifier=None,
                                  Port=None, AvailabilityZone=None, AllowVersionUpgrade=None,
                                  ClusterSubnetGroupName=None, PubliclyAccessible=None, OwnerAccount=None,
                                  HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None, ElasticIp=None,
                                  ClusterParameterGroupName=None, ClusterSecurityGroups=None, VpcSecurityGroupIds=None,
                                  PreferredMaintenanceWindow=None, AutomatedSnapshotRetentionPeriod=None, KmsKeyId=None,
                                  NodeType=None, EnhancedVpcRouting=None, AdditionalInfo=None, IamRoles=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster that will be created from restoring the snapshot.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            Alphabetic characters must be lowercase.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for all clusters within an AWS account.
            
    :type ClusterIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive.
            Example: my-snapshot-id
            
    :type SnapshotIdentifier: string
    :param SnapshotClusterIdentifier: The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
    :type SnapshotClusterIdentifier: string
    :param Port: The port number on which the cluster accepts connections.
            Default: The same port as the original cluster.
            Constraints: Must be between 1115 and 65535 .
            
    :type Port: integer
    :param AvailabilityZone: The Amazon EC2 Availability Zone in which to restore the cluster.
            Default: A random, system-chosen Availability Zone.
            Example: us-east-1a
            
    :type AvailabilityZone: string
    :param AllowVersionUpgrade: If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.
            Default: true
            
    :type AllowVersionUpgrade: boolean
    :param ClusterSubnetGroupName: The name of the subnet group where you want to cluster restored.
            A snapshot of cluster in VPC can be restored only in VPC. Therefore, you must provide subnet group name where you want the cluster restored.
            
    :type ClusterSubnetGroupName: string
    :param PubliclyAccessible: If true , the cluster can be accessed from a public network.
    :type PubliclyAccessible: boolean
    :param OwnerAccount: The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
    :type OwnerAccount: string
    :param HsmClientCertificateIdentifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
    :type HsmClientCertificateIdentifier: string
    :param HsmConfigurationIdentifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    :type HsmConfigurationIdentifier: string
    :param ElasticIp: The elastic IP (EIP) address for the cluster.
    :type ElasticIp: string
    :param ClusterParameterGroupName: The name of the parameter group to be associated with this cluster.
            Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to Working with Amazon Redshift Parameter Groups .
            Constraints:
            Must be 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            
    :type ClusterParameterGroupName: string
    :param ClusterSecurityGroups: A list of security groups to be associated with this cluster.
            Default: The default cluster security group for Amazon Redshift.
            Cluster security groups only apply to clusters outside of VPCs.
            (string) --
            
    :type ClusterSecurityGroups: list
    :param VpcSecurityGroupIds: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
            Default: The default VPC security group is associated with the cluster.
            VPC security groups only apply to clusters in VPCs.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which automated cluster maintenance can occur.
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: The value selected for the cluster from which the snapshot was taken. For more information about the time blocks for each region, see Maintenance Windows in Amazon Redshift Cluster Management Guide.
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Minimum 30-minute window.
            
    :type PreferredMaintenanceWindow: string
    :param AutomatedSnapshotRetentionPeriod: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with CreateClusterSnapshot .
            Default: The value selected for the cluster from which the snapshot was taken.
            Constraints: Must be a value from 0 to 35.
            
    :type AutomatedSnapshotRetentionPeriod: integer
    :param KmsKeyId: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster that you restore from a shared snapshot.
    :type KmsKeyId: string
    :param NodeType: The node type that the restored cluster will be provisioned with.
            Default: The node type of the cluster from which the snapshot was taken. You can modify this if you are using any DS node type. In that case, you can choose to restore into another DS node type of the same size. For example, you can restore ds1.8xlarge into ds2.8xlarge, or ds2.xlarge into ds1.xlarge. If you have a DC instance type, you must restore into that same instance type and size. In other words, you can only restore a dc1.large instance type into another dc1.large instance type. For more information about node types, see About Clusters and Nodes in the Amazon Redshift Cluster Management Guide
            
    :type NodeType: string
    :param EnhancedVpcRouting: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            
    :type EnhancedVpcRouting: boolean
    :param AdditionalInfo: Reserved.
    :type AdditionalInfo: string
    :param IamRoles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM roles in a single request.
            A cluster can have up to 10 IAM roles associated at any time.
            (string) --
            
    :type IamRoles: list
    """
    pass


def restore_table_from_cluster_snapshot(ClusterIdentifier=None, SnapshotIdentifier=None, SourceDatabaseName=None,
                                        SourceSchemaName=None, SourceTableName=None, TargetDatabaseName=None,
                                        TargetSchemaName=None, NewTableName=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the Amazon Redshift cluster to restore the table to.
            
    :type ClusterIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            The identifier of the snapshot to restore the table from. This snapshot must have been created from the Amazon Redshift cluster specified by the ClusterIdentifier parameter.
            
    :type SnapshotIdentifier: string
    :param SourceDatabaseName: [REQUIRED]
            The name of the source database that contains the table to restore from.
            
    :type SourceDatabaseName: string
    :param SourceSchemaName: The name of the source schema that contains the table to restore from. If you do not specify a SourceSchemaName value, the default is public .
    :type SourceSchemaName: string
    :param SourceTableName: [REQUIRED]
            The name of the source table to restore from.
            
    :type SourceTableName: string
    :param TargetDatabaseName: The name of the database to restore the table to.
    :type TargetDatabaseName: string
    :param TargetSchemaName: The name of the schema to restore the table to.
    :type TargetSchemaName: string
    :param NewTableName: [REQUIRED]
            The name of the table to create as a result of the current request.
            
    :type NewTableName: string
    """
    pass


def revoke_cluster_security_group_ingress(ClusterSecurityGroupName=None, CIDRIP=None, EC2SecurityGroupName=None,
                                          EC2SecurityGroupOwnerId=None):
    """
    :param ClusterSecurityGroupName: [REQUIRED]
            The name of the security Group from which to revoke the ingress rule.
            
    :type ClusterSecurityGroupName: string
    :param CIDRIP: The IP range for which to revoke access. This range must be a valid Classless Inter-Domain Routing (CIDR) block of IP addresses. If CIDRIP is specified, EC2SecurityGroupName and EC2SecurityGroupOwnerId cannot be provided.
    :type CIDRIP: string
    :param EC2SecurityGroupName: The name of the EC2 Security Group whose access is to be revoked. If EC2SecurityGroupName is specified, EC2SecurityGroupOwnerId must also be provided and CIDRIP cannot be provided.
    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupOwnerId: The AWS account number of the owner of the security group specified in the EC2SecurityGroupName parameter. The AWS access key ID is not an acceptable value. If EC2SecurityGroupOwnerId is specified, EC2SecurityGroupName must also be provided. and CIDRIP cannot be provided.
            Example: 111122223333
            
    :type EC2SecurityGroupOwnerId: string
    """
    pass


def revoke_snapshot_access(SnapshotIdentifier=None, SnapshotClusterIdentifier=None, AccountWithRestoreAccess=None):
    """
    :param SnapshotIdentifier: [REQUIRED]
            The identifier of the snapshot that the account can no longer access.
            
    :type SnapshotIdentifier: string
    :param SnapshotClusterIdentifier: The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
    :type SnapshotClusterIdentifier: string
    :param AccountWithRestoreAccess: [REQUIRED]
            The identifier of the AWS customer account that can no longer restore the specified snapshot.
            
    :type AccountWithRestoreAccess: string
    """
    pass


def rotate_encryption_key(ClusterIdentifier=None):
    """
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the cluster that you want to rotate the encryption keys for.
            Constraints: Must be the name of valid cluster that has encryption enabled.
            Return typedict
            ReturnsResponse Syntax{
              'Cluster': {
                'ClusterIdentifier': 'string',
                'NodeType': 'string',
                'ClusterStatus': 'string',
                'ModifyStatus': 'string',
                'MasterUsername': 'string',
                'DBName': 'string',
                'Endpoint': {
                  'Address': 'string',
                  'Port': 123
                },
                'ClusterCreateTime': datetime(2015, 1, 1),
                'AutomatedSnapshotRetentionPeriod': 123,
                'ClusterSecurityGroups': [
                  {
                    'ClusterSecurityGroupName': 'string',
                    'Status': 'string'
                  },
                ],
                'VpcSecurityGroups': [
                  {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                  },
                ],
                'ClusterParameterGroups': [
                  {
                    'ParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'ClusterParameterStatusList': [
                      {
                        'ParameterName': 'string',
                        'ParameterApplyStatus': 'string',
                        'ParameterApplyErrorDescription': 'string'
                      },
                    ]
                  },
                ],
                'ClusterSubnetGroupName': 'string',
                'VpcId': 'string',
                'AvailabilityZone': 'string',
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                  'MasterUserPassword': 'string',
                  'NodeType': 'string',
                  'NumberOfNodes': 123,
                  'ClusterType': 'string',
                  'ClusterVersion': 'string',
                  'AutomatedSnapshotRetentionPeriod': 123,
                  'ClusterIdentifier': 'string',
                  'PubliclyAccessible': True|False,
                  'EnhancedVpcRouting': True|False
                },
                'ClusterVersion': 'string',
                'AllowVersionUpgrade': True|False,
                'NumberOfNodes': 123,
                'PubliclyAccessible': True|False,
                'Encrypted': True|False,
                'RestoreStatus': {
                  'Status': 'string',
                  'CurrentRestoreRateInMegaBytesPerSecond': 123.0,
                  'SnapshotSizeInMegaBytes': 123,
                  'ProgressInMegaBytes': 123,
                  'ElapsedTimeInSeconds': 123,
                  'EstimatedTimeToCompletionInSeconds': 123
                },
                'HsmStatus': {
                  'HsmClientCertificateIdentifier': 'string',
                  'HsmConfigurationIdentifier': 'string',
                  'Status': 'string'
                },
                'ClusterSnapshotCopyStatus': {
                  'DestinationRegion': 'string',
                  'RetentionPeriod': 123,
                  'SnapshotCopyGrantName': 'string'
                },
                'ClusterPublicKey': 'string',
                'ClusterNodes': [
                  {
                    'NodeRole': 'string',
                    'PrivateIPAddress': 'string',
                    'PublicIPAddress': 'string'
                  },
                ],
                'ElasticIpStatus': {
                  'ElasticIp': 'string',
                  'Status': 'string'
                },
                'ClusterRevisionNumber': 'string',
                'Tags': [
                  {
                    'Key': 'string',
                    'Value': 'string'
                  },
                ],
                'KmsKeyId': 'string',
                'EnhancedVpcRouting': True|False,
                'IamRoles': [
                  {
                    'IamRoleArn': 'string',
                    'ApplyStatus': 'string'
                  },
                ]
              }
            }
            Response Structure
            (dict) --
            Cluster (dict) --Describes a cluster.
            ClusterIdentifier (string) --The unique identifier of the cluster.
            NodeType (string) --The node type for the nodes in the cluster.
            ClusterStatus (string) --The current state of the cluster. Possible values are the following:
            available
            creating
            deleting
            final-snapshot
            hardware-failure
            incompatible-hsm
            incompatible-network
            incompatible-parameters
            incompatible-restore
            modifying
            rebooting
            renaming
            resizing
            rotating-keys
            storage-full
            updating-hsm
            ModifyStatus (string) --The status of a modify operation, if any, initiated for the cluster.
            MasterUsername (string) --The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.
            DBName (string) --The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.
            Endpoint (dict) --The connection endpoint.
            Address (string) --The DNS address of the Cluster.
            Port (integer) --The port that the database engine is listening on.
            ClusterCreateTime (datetime) --The date and time that the cluster was created.
            AutomatedSnapshotRetentionPeriod (integer) --The number of days that automatic cluster snapshots are retained.
            ClusterSecurityGroups (list) --A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
            Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.
            (dict) --Describes a cluster security group.
            ClusterSecurityGroupName (string) --The name of the cluster security group.
            Status (string) --The status of the cluster security group.
            
            VpcSecurityGroups (list) --A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.
            (dict) --Describes the members of a VPC security group.
            VpcSecurityGroupId (string) --The identifier of the VPC security group.
            Status (string) --The status of the VPC security group.
            
            ClusterParameterGroups (list) --The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.
            (dict) --Describes the status of a parameter group.
            ParameterGroupName (string) --The name of the cluster parameter group.
            ParameterApplyStatus (string) --The status of parameter updates.
            ClusterParameterStatusList (list) --The list of parameter statuses.
            For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
            (dict) --Describes the status of a parameter group.
            ParameterName (string) --The name of the parameter.
            ParameterApplyStatus (string) --The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
            The following are possible statuses and descriptions.
            in-sync : The parameter value is in sync with the database.
            pending-reboot : The parameter value will be applied after the cluster reboots.
            applying : The parameter value is being applied to the database.
            invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
            apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
            apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
            unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.
            ParameterApplyErrorDescription (string) --The error that prevented the parameter from being applied to the database.
            
            
            ClusterSubnetGroupName (string) --The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
            VpcId (string) --The identifier of the VPC the cluster is in, if the cluster is in a VPC.
            AvailabilityZone (string) --The name of the Availability Zone in which the cluster is located.
            PreferredMaintenanceWindow (string) --The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
            PendingModifiedValues (dict) --A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.
            MasterUserPassword (string) --The pending or in-progress change of the master user password for the cluster.
            NodeType (string) --The pending or in-progress change of the cluster's node type.
            NumberOfNodes (integer) --The pending or in-progress change of the number of nodes in the cluster.
            ClusterType (string) --The pending or in-progress change of the cluster type.
            ClusterVersion (string) --The pending or in-progress change of the service version.
            AutomatedSnapshotRetentionPeriod (integer) --The pending or in-progress change of the automated snapshot retention period.
            ClusterIdentifier (string) --The pending or in-progress change of the new identifier for the cluster.
            PubliclyAccessible (boolean) --The pending or in-progress change of the ability to connect to the cluster from the public network.
            EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            ClusterVersion (string) --The version ID of the Amazon Redshift engine that is running on the cluster.
            AllowVersionUpgrade (boolean) --A Boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.
            NumberOfNodes (integer) --The number of compute nodes in the cluster.
            PubliclyAccessible (boolean) --A Boolean value that, if true , indicates that the cluster can be accessed from a public network.
            Encrypted (boolean) --A Boolean value that, if true , indicates that data in the cluster is encrypted at rest.
            RestoreStatus (dict) --A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.
            Status (string) --The status of the restore action. Returns starting, restoring, completed, or failed.
            CurrentRestoreRateInMegaBytesPerSecond (float) --The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
            SnapshotSizeInMegaBytes (integer) --The size of the set of snapshot data used to restore the cluster.
            ProgressInMegaBytes (integer) --The number of megabytes that have been transferred from snapshot storage.
            ElapsedTimeInSeconds (integer) --The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
            EstimatedTimeToCompletionInSeconds (integer) --The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore.
            HsmStatus (dict) --A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
            Values: active, applying
            HsmClientCertificateIdentifier (string) --Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
            HsmConfigurationIdentifier (string) --Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
            Status (string) --Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
            Values: active, applying
            ClusterSnapshotCopyStatus (dict) --A value that returns the destination region and retention period that are configured for cross-region snapshot copy.
            DestinationRegion (string) --The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
            RetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
            SnapshotCopyGrantName (string) --The name of the snapshot copy grant.
            ClusterPublicKey (string) --The public key for the cluster.
            ClusterNodes (list) --The nodes in the cluster.
            (dict) --The identifier of a node in a cluster.
            NodeRole (string) --Whether the node is a leader node or a compute node.
            PrivateIPAddress (string) --The private IP address of a node within a cluster.
            PublicIPAddress (string) --The public IP address of a node within a cluster.
            
            ElasticIpStatus (dict) --The status of the elastic IP (EIP) address.
            ElasticIp (string) --The elastic IP (EIP) address for the cluster.
            Status (string) --The status of the elastic IP (EIP) address.
            ClusterRevisionNumber (string) --The specific revision number of the database in the cluster.
            Tags (list) --The list of tags for the cluster.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.
            EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            IamRoles (list) --A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
            (dict) --An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.
            IamRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .
            ApplyStatus (string) --A value that describes the status of the IAM role's association with an Amazon Redshift cluster.
            The following are possible statuses and descriptions.
            in-sync : The role is available for use by the cluster.
            adding : The role is in the process of being associated with the cluster.
            removing : The role is in the process of being disassociated with the cluster.
            
            
            
            
    :type ClusterIdentifier: string
    """
    pass
