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

def authorize_cluster_security_group_ingress(ClusterSecurityGroupName=None, CIDRIP=None, EC2SecurityGroupName=None, EC2SecurityGroupOwnerId=None):
    """
    Adds an inbound (ingress) rule to an Amazon Redshift security group. Depending on whether the application accessing your cluster is running on the Internet or an Amazon EC2 instance, you can authorize inbound access to either a Classless Interdomain Routing (CIDR)/Internet Protocol (IP) range or to an Amazon EC2 security group. You can add as many as 20 ingress rules to an Amazon Redshift security group.
    If you authorize access to an Amazon EC2 security group, specify EC2SecurityGroupName and EC2SecurityGroupOwnerId . The Amazon EC2 security group and Amazon Redshift cluster must be in the same AWS region.
    If you authorize access to a CIDR/IP address range, specify CIDRIP . For an overview of CIDR blocks, see the Wikipedia article on Classless Inter-Domain Routing .
    You must also associate the security group with a cluster so that clients running on these IP addresses or the EC2 instance are authorized to connect to the cluster. For information about managing security groups, go to Working with Security Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.authorize_cluster_security_group_ingress(
        ClusterSecurityGroupName='string',
        CIDRIP='string',
        EC2SecurityGroupName='string',
        EC2SecurityGroupOwnerId='string'
    )
    
    
    :type ClusterSecurityGroupName: string
    :param ClusterSecurityGroupName: [REQUIRED]
            The name of the security group to which the ingress rule is added.
            

    :type CIDRIP: string
    :param CIDRIP: The IP range to be added the Amazon Redshift security group.

    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: The EC2 security group to be added the Amazon Redshift security group.

    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: The AWS account number of the owner of the security group specified by the EC2SecurityGroupName parameter. The AWS Access Key ID is not an acceptable value.
            Example: 111122223333
            

    :rtype: dict
    :return: {
        'ClusterSecurityGroup': {
            'ClusterSecurityGroupName': 'string',
            'Description': 'string',
            'EC2SecurityGroups': [
                {
                    'Status': 'string',
                    'EC2SecurityGroupName': 'string',
                    'EC2SecurityGroupOwnerId': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'IPRanges': [
                {
                    'Status': 'string',
                    'CIDRIP': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def authorize_snapshot_access(SnapshotIdentifier=None, SnapshotClusterIdentifier=None, AccountWithRestoreAccess=None):
    """
    Authorizes the specified AWS customer account to restore the specified snapshot.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.authorize_snapshot_access(
        SnapshotIdentifier='string',
        SnapshotClusterIdentifier='string',
        AccountWithRestoreAccess='string'
    )
    
    
    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            The identifier of the snapshot the account is authorized to restore.
            

    :type SnapshotClusterIdentifier: string
    :param SnapshotClusterIdentifier: The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

    :type AccountWithRestoreAccess: string
    :param AccountWithRestoreAccess: [REQUIRED]
            The identifier of the AWS customer account authorized to restore the specified snapshot.
            To share a snapshot with AWS support, specify amazon-redshift-support.
            

    :rtype: dict
    :return: {
        'Snapshot': {
            'SnapshotIdentifier': 'string',
            'ClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Status': 'string',
            'Port': 123,
            'AvailabilityZone': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'ClusterVersion': 'string',
            'SnapshotType': 'string',
            'NodeType': 'string',
            'NumberOfNodes': 123,
            'DBName': 'string',
            'VpcId': 'string',
            'Encrypted': True|False,
            'KmsKeyId': 'string',
            'EncryptedWithHSM': True|False,
            'AccountsWithRestoreAccess': [
                {
                    'AccountId': 'string',
                    'AccountAlias': 'string'
                },
            ],
            'OwnerAccount': 'string',
            'TotalBackupSizeInMegaBytes': 123.0,
            'ActualIncrementalBackupSizeInMegaBytes': 123.0,
            'BackupProgressInMegaBytes': 123.0,
            'CurrentBackupRateInMegaBytesPerSecond': 123.0,
            'EstimatedSecondsToCompletion': 123,
            'ElapsedTimeInSeconds': 123,
            'SourceRegion': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RestorableNodeTypes': [
                'string',
            ],
            'EnhancedVpcRouting': True|False
        }
    }
    
    
    :returns: 
    CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
    DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
    DeleteClusterSnapshot returns status as "deleted".
    
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

def copy_cluster_snapshot(SourceSnapshotIdentifier=None, SourceSnapshotClusterIdentifier=None, TargetSnapshotIdentifier=None):
    """
    Copies the specified automated cluster snapshot to a new manual cluster snapshot. The source must be an automated snapshot and it must be in the available state.
    When you delete a cluster, Amazon Redshift deletes any automated snapshots of the cluster. Also, when the retention period of the snapshot expires, Amazon Redshift automatically deletes it. If you want to keep an automated snapshot for a longer period, you can make a manual copy of the snapshot. Manual snapshots are retained until you delete them.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.copy_cluster_snapshot(
        SourceSnapshotIdentifier='string',
        SourceSnapshotClusterIdentifier='string',
        TargetSnapshotIdentifier='string'
    )
    
    
    :type SourceSnapshotIdentifier: string
    :param SourceSnapshotIdentifier: [REQUIRED]
            The identifier for the source snapshot.
            Constraints:
            Must be the identifier for a valid automated snapshot whose state is available .
            

    :type SourceSnapshotClusterIdentifier: string
    :param SourceSnapshotClusterIdentifier: The identifier of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
            Constraints:
            Must be the identifier for a valid cluster.
            

    :type TargetSnapshotIdentifier: string
    :param TargetSnapshotIdentifier: [REQUIRED]
            The identifier given to the new manual snapshot.
            Constraints:
            Cannot be null, empty, or blank.
            Must contain from 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for the AWS account that is making the request.
            

    :rtype: dict
    :return: {
        'Snapshot': {
            'SnapshotIdentifier': 'string',
            'ClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Status': 'string',
            'Port': 123,
            'AvailabilityZone': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'ClusterVersion': 'string',
            'SnapshotType': 'string',
            'NodeType': 'string',
            'NumberOfNodes': 123,
            'DBName': 'string',
            'VpcId': 'string',
            'Encrypted': True|False,
            'KmsKeyId': 'string',
            'EncryptedWithHSM': True|False,
            'AccountsWithRestoreAccess': [
                {
                    'AccountId': 'string',
                    'AccountAlias': 'string'
                },
            ],
            'OwnerAccount': 'string',
            'TotalBackupSizeInMegaBytes': 123.0,
            'ActualIncrementalBackupSizeInMegaBytes': 123.0,
            'BackupProgressInMegaBytes': 123.0,
            'CurrentBackupRateInMegaBytesPerSecond': 123.0,
            'EstimatedSecondsToCompletion': 123,
            'ElapsedTimeInSeconds': 123,
            'SourceRegion': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RestorableNodeTypes': [
                'string',
            ],
            'EnhancedVpcRouting': True|False
        }
    }
    
    
    :returns: 
    CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
    DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
    DeleteClusterSnapshot returns status as "deleted".
    
    """
    pass

def create_cluster(DBName=None, ClusterIdentifier=None, ClusterType=None, NodeType=None, MasterUsername=None, MasterUserPassword=None, ClusterSecurityGroups=None, VpcSecurityGroupIds=None, ClusterSubnetGroupName=None, AvailabilityZone=None, PreferredMaintenanceWindow=None, ClusterParameterGroupName=None, AutomatedSnapshotRetentionPeriod=None, Port=None, ClusterVersion=None, AllowVersionUpgrade=None, NumberOfNodes=None, PubliclyAccessible=None, Encrypted=None, HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None, ElasticIp=None, Tags=None, KmsKeyId=None, EnhancedVpcRouting=None, AdditionalInfo=None, IamRoles=None):
    """
    Creates a new cluster.
    To create the cluster in Virtual Private Cloud (VPC), you must provide a cluster subnet group name. The cluster subnet group identifies the subnets of your VPC that Amazon Redshift uses when creating the cluster. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_cluster(
        DBName='string',
        ClusterIdentifier='string',
        ClusterType='string',
        NodeType='string',
        MasterUsername='string',
        MasterUserPassword='string',
        ClusterSecurityGroups=[
            'string',
        ],
        VpcSecurityGroupIds=[
            'string',
        ],
        ClusterSubnetGroupName='string',
        AvailabilityZone='string',
        PreferredMaintenanceWindow='string',
        ClusterParameterGroupName='string',
        AutomatedSnapshotRetentionPeriod=123,
        Port=123,
        ClusterVersion='string',
        AllowVersionUpgrade=True|False,
        NumberOfNodes=123,
        PubliclyAccessible=True|False,
        Encrypted=True|False,
        HsmClientCertificateIdentifier='string',
        HsmConfigurationIdentifier='string',
        ElasticIp='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        KmsKeyId='string',
        EnhancedVpcRouting=True|False,
        AdditionalInfo='string',
        IamRoles=[
            'string',
        ]
    )
    
    
    :type DBName: string
    :param DBName: The name of the first database to be created when the cluster is created.
            To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to Create a Database in the Amazon Redshift Database Developer Guide.
            Default: dev
            Constraints:
            Must contain 1 to 64 alphanumeric characters.
            Must contain only lowercase letters.
            Cannot be a word that is reserved by the service. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.
            

    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            Alphabetic characters must be lowercase.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for all clusters within an AWS account.
            Example: myexamplecluster
            

    :type ClusterType: string
    :param ClusterType: The type of the cluster. When cluster type is specified as
            single-node , the NumberOfNodes parameter is not required.
            multi-node , the NumberOfNodes parameter is required.
            Valid Values: multi-node | single-node
            Default: multi-node
            

    :type NodeType: string
    :param NodeType: [REQUIRED]
            The node type to be provisioned for the cluster. For information about node types, go to Working with Clusters in the Amazon Redshift Cluster Management Guide .
            Valid Values: ds1.xlarge | ds1.8xlarge | ds2.xlarge | ds2.8xlarge | dc1.large | dc1.8xlarge .
            

    :type MasterUsername: string
    :param MasterUsername: [REQUIRED]
            The user name associated with the master user account for the cluster that is being created.
            Constraints:
            Must be 1 - 128 alphanumeric characters.
            First character must be a letter.
            Cannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.
            

    :type MasterUserPassword: string
    :param MasterUserPassword: [REQUIRED]
            The password associated with the master user account for the cluster that is being created.
            Constraints:
            Must be between 8 and 64 characters in length.
            Must contain at least one uppercase letter.
            Must contain at least one lowercase letter.
            Must contain one number.
            Can be any printable ASCII character (ASCII code 33 to 126) except ' (single quote), ' (double quote), , /, @, or space.
            

    :type ClusterSecurityGroups: list
    :param ClusterSecurityGroups: A list of security groups to be associated with this cluster.
            Default: The default cluster security group for Amazon Redshift.
            (string) --
            

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
            Default: The default VPC security group is associated with the cluster.
            (string) --
            

    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: The name of a cluster subnet group to be associated with this cluster.
            If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
            

    :type AvailabilityZone: string
    :param AvailabilityZone: The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.
            Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.
            Example: us-east-1d
            Constraint: The specified Availability Zone must be in the same region as the current endpoint.
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which automated cluster maintenance can occur.
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see Maintenance Windows in Amazon Redshift Cluster Management Guide.
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Minimum 30-minute window.
            

    :type ClusterParameterGroupName: string
    :param ClusterParameterGroupName: The name of the parameter group to be associated with this cluster.
            Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to Working with Amazon Redshift Parameter Groups
            Constraints:
            Must be 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            

    :type AutomatedSnapshotRetentionPeriod: integer
    :param AutomatedSnapshotRetentionPeriod: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with CreateClusterSnapshot .
            Default: 1
            Constraints: Must be a value from 0 to 35.
            

    :type Port: integer
    :param Port: The port number on which the cluster accepts incoming connections.
            The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.
            Default: 5439
            Valid Values: 1150-65535
            

    :type ClusterVersion: string
    :param ClusterVersion: The version of the Amazon Redshift engine software that you want to deploy on the cluster.
            The version selected runs on all the nodes in the cluster.
            Constraints: Only version 1.0 is currently available.
            Example: 1.0
            

    :type AllowVersionUpgrade: boolean
    :param AllowVersionUpgrade: If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.
            When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.
            Default: true
            

    :type NumberOfNodes: integer
    :param NumberOfNodes: The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node .
            For information about determining how many nodes you need, go to Working with Clusters in the Amazon Redshift Cluster Management Guide .
            If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.
            Default: 1
            Constraints: Value must be at least 1 and no more than 100.
            

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: If true , the cluster can be accessed from a public network.

    :type Encrypted: boolean
    :param Encrypted: If true , the data in the cluster is encrypted at rest.
            Default: false
            

    :type HsmClientCertificateIdentifier: string
    :param HsmClientCertificateIdentifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

    :type HsmConfigurationIdentifier: string
    :param HsmConfigurationIdentifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

    :type ElasticIp: string
    :param ElasticIp: The Elastic IP (EIP) address for the cluster.
            Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to Supported Platforms to Launch Your Cluster in the Amazon Redshift Cluster Management Guide.
            

    :type Tags: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    :type KmsKeyId: string
    :param KmsKeyId: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.

    :type EnhancedVpcRouting: boolean
    :param EnhancedVpcRouting: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            

    :type AdditionalInfo: string
    :param AdditionalInfo: Reserved.

    :type IamRoles: list
    :param IamRoles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM roles in a single request.
            A cluster can have up to 10 IAM roles associated with it at any time.
            (string) --
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
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
    
    """
    pass

def create_cluster_parameter_group(ParameterGroupName=None, ParameterGroupFamily=None, Description=None, Tags=None):
    """
    Creates an Amazon Redshift parameter group.
    Creating parameter groups is independent of creating clusters. You can associate a cluster with a parameter group when you create the cluster. You can also associate an existing cluster with a parameter group after the cluster is created by using  ModifyCluster .
    Parameters in the parameter group define specific behavior that applies to the databases you create on the cluster. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_cluster_parameter_group(
        ParameterGroupName='string',
        ParameterGroupFamily='string',
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]
            The name of the cluster parameter group.
            Constraints:
            Must be 1 to 255 alphanumeric characters or hyphens
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique withing your AWS account.
            Note
            This value is stored as a lower-case string.
            

    :type ParameterGroupFamily: string
    :param ParameterGroupFamily: [REQUIRED]
            The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.
            To get a list of valid parameter group family names, you can call DescribeClusterParameterGroups . By default, Amazon Redshift returns a list of all the parameter groups that are owned by your AWS account, including the default parameter groups for each Amazon Redshift engine version. The parameter group family names associated with the default parameter groups provide you the valid values. For example, a valid family name is 'redshift-1.0'.
            

    :type Description: string
    :param Description: [REQUIRED]
            A description of the parameter group.
            

    :type Tags: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    :rtype: dict
    :return: {
        'ClusterParameterGroup': {
            'ParameterGroupName': 'string',
            'ParameterGroupFamily': 'string',
            'Description': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_cluster_security_group(ClusterSecurityGroupName=None, Description=None, Tags=None):
    """
    Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.
    For information about managing security groups, go to Amazon Redshift Cluster Security Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_cluster_security_group(
        ClusterSecurityGroupName='string',
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ClusterSecurityGroupName: string
    :param ClusterSecurityGroupName: [REQUIRED]
            The name for the security group. Amazon Redshift stores the value as a lowercase string.
            Constraints:
            Must contain no more than 255 alphanumeric characters or hyphens.
            Must not be 'Default'.
            Must be unique for all security groups that are created by your AWS account.
            Example: examplesecuritygroup
            

    :type Description: string
    :param Description: [REQUIRED]
            A description for the security group.
            

    :type Tags: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    :rtype: dict
    :return: {
        'ClusterSecurityGroup': {
            'ClusterSecurityGroupName': 'string',
            'Description': 'string',
            'EC2SecurityGroups': [
                {
                    'Status': 'string',
                    'EC2SecurityGroupName': 'string',
                    'EC2SecurityGroupOwnerId': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'IPRanges': [
                {
                    'Status': 'string',
                    'CIDRIP': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_cluster_snapshot(SnapshotIdentifier=None, ClusterIdentifier=None, Tags=None):
    """
    Creates a manual snapshot of the specified cluster. The cluster must be in the available state.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_cluster_snapshot(
        SnapshotIdentifier='string',
        ClusterIdentifier='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the AWS account.
            Constraints:
            Cannot be null, empty, or blank
            Must contain from 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-snapshot-id
            

    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The cluster identifier for which you want a snapshot.
            

    :type Tags: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    :rtype: dict
    :return: {
        'Snapshot': {
            'SnapshotIdentifier': 'string',
            'ClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Status': 'string',
            'Port': 123,
            'AvailabilityZone': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'ClusterVersion': 'string',
            'SnapshotType': 'string',
            'NodeType': 'string',
            'NumberOfNodes': 123,
            'DBName': 'string',
            'VpcId': 'string',
            'Encrypted': True|False,
            'KmsKeyId': 'string',
            'EncryptedWithHSM': True|False,
            'AccountsWithRestoreAccess': [
                {
                    'AccountId': 'string',
                    'AccountAlias': 'string'
                },
            ],
            'OwnerAccount': 'string',
            'TotalBackupSizeInMegaBytes': 123.0,
            'ActualIncrementalBackupSizeInMegaBytes': 123.0,
            'BackupProgressInMegaBytes': 123.0,
            'CurrentBackupRateInMegaBytesPerSecond': 123.0,
            'EstimatedSecondsToCompletion': 123,
            'ElapsedTimeInSeconds': 123,
            'SourceRegion': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RestorableNodeTypes': [
                'string',
            ],
            'EnhancedVpcRouting': True|False
        }
    }
    
    
    :returns: 
    CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
    DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
    DeleteClusterSnapshot returns status as "deleted".
    
    """
    pass

def create_cluster_subnet_group(ClusterSubnetGroupName=None, Description=None, SubnetIds=None, Tags=None):
    """
    Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.
    For information about subnet groups, go to Amazon Redshift Cluster Subnet Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_cluster_subnet_group(
        ClusterSubnetGroupName='string',
        Description='string',
        SubnetIds=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: [REQUIRED]
            The name for the subnet group. Amazon Redshift stores the value as a lowercase string.
            Constraints:
            Must contain no more than 255 alphanumeric characters or hyphens.
            Must not be 'Default'.
            Must be unique for all subnet groups that are created by your AWS account.
            Example: examplesubnetgroup
            

    :type Description: string
    :param Description: [REQUIRED]
            A description for the subnet group.
            

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]
            An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
            (string) --
            

    :type Tags: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    :rtype: dict
    :return: {
        'ClusterSubnetGroup': {
            'ClusterSubnetGroupName': 'string',
            'Description': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, SourceIds=None, EventCategories=None, Severity=None, Enabled=None, Tags=None):
    """
    Creates an Amazon Redshift event notification subscription. This action requires an ARN (Amazon Resource Name) of an Amazon SNS topic created by either the Amazon Redshift console, the Amazon SNS console, or the Amazon SNS API. To obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.
    You can specify the source type, and lists of Amazon Redshift source IDs, event categories, and event severities. Notifications will be sent for all events you want that match those criteria. For example, you can specify source type = cluster, source ID = my-cluster-1 and mycluster2, event categories = Availability, Backup, and severity = ERROR. The subscription will only send notifications for those ERROR events in the Availability and Backup categories for the specified clusters.
    If you specify both the source type and source IDs, such as source type = cluster and source identifier = my-cluster-1, notifications will be sent for all the cluster events for my-cluster-1. If you specify a source type but do not specify a source identifier, you will receive notice of the events for the objects of that type in your AWS account. If you do not specify either the SourceType nor the SourceIdentifier, you will be notified of events generated from all Amazon Redshift sources belonging to your AWS account. You must specify a source type if you specify a source ID.
    See also: AWS API Documentation
    
    
    :example: response = client.create_event_subscription(
        SubscriptionName='string',
        SnsTopicArn='string',
        SourceType='string',
        SourceIds=[
            'string',
        ],
        EventCategories=[
            'string',
        ],
        Severity='string',
        Enabled=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]
            The name of the event subscription to be created.
            Constraints:
            Cannot be null, empty, or blank.
            Must contain from 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            

    :type SnsTopicArn: string
    :param SnsTopicArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
            

    :type SourceType: string
    :param SourceType: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account. You must specify a source type in order to specify source IDs.
            Valid values: cluster, cluster-parameter-group, cluster-security-group, and cluster-snapshot.
            

    :type SourceIds: list
    :param SourceIds: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.
            Example: my-cluster-1, my-cluster-2
            Example: my-snapshot-20131010
            (string) --
            

    :type EventCategories: list
    :param EventCategories: Specifies the Amazon Redshift event categories to be published by the event notification subscription.
            Values: Configuration, Management, Monitoring, Security
            (string) --
            

    :type Severity: string
    :param Severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription.
            Values: ERROR, INFO
            

    :type Enabled: boolean
    :param Enabled: A Boolean value; set to true to activate the subscription, set to false to create the subscription but not active it.

    :type Tags: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    :rtype: dict
    :return: {
        'EventSubscription': {
            'CustomerAwsId': 'string',
            'CustSubscriptionId': 'string',
            'SnsTopicArn': 'string',
            'Status': 'string',
            'SubscriptionCreationTime': datetime(2015, 1, 1),
            'SourceType': 'string',
            'SourceIdsList': [
                'string',
            ],
            'EventCategoriesList': [
                'string',
            ],
            'Severity': 'string',
            'Enabled': True|False,
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Can be one of the following: active | no-permission | topic-not-exist
    The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.
    
    """
    pass

def create_hsm_client_certificate(HsmClientCertificateIdentifier=None, Tags=None):
    """
    Creates an HSM client certificate that an Amazon Redshift cluster will use to connect to the client's HSM in order to store and retrieve the keys used to encrypt the cluster databases.
    The command returns a public key, which you must store in the HSM. In addition to creating the HSM certificate, you must create an Amazon Redshift HSM configuration that provides a cluster the information needed to store and use encryption keys in the HSM. For more information, go to Hardware Security Modules in the Amazon Redshift Cluster Management Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.create_hsm_client_certificate(
        HsmClientCertificateIdentifier='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type HsmClientCertificateIdentifier: string
    :param HsmClientCertificateIdentifier: [REQUIRED]
            The identifier to be assigned to the new HSM client certificate that the cluster will use to connect to the HSM to use the database encryption keys.
            

    :type Tags: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    :rtype: dict
    :return: {
        'HsmClientCertificate': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmClientCertificatePublicKey': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_hsm_configuration(HsmConfigurationIdentifier=None, Description=None, HsmIpAddress=None, HsmPartitionName=None, HsmPartitionPassword=None, HsmServerPublicCertificate=None, Tags=None):
    """
    Creates an HSM configuration that contains the information required by an Amazon Redshift cluster to store and use database encryption keys in a Hardware Security Module (HSM). After creating the HSM configuration, you can specify it as a parameter when creating a cluster. The cluster will then store its encryption keys in the HSM.
    In addition to creating an HSM configuration, you must also create an HSM client certificate. For more information, go to Hardware Security Modules in the Amazon Redshift Cluster Management Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.create_hsm_configuration(
        HsmConfigurationIdentifier='string',
        Description='string',
        HsmIpAddress='string',
        HsmPartitionName='string',
        HsmPartitionPassword='string',
        HsmServerPublicCertificate='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type HsmConfigurationIdentifier: string
    :param HsmConfigurationIdentifier: [REQUIRED]
            The identifier to be assigned to the new Amazon Redshift HSM configuration.
            

    :type Description: string
    :param Description: [REQUIRED]
            A text description of the HSM configuration to be created.
            

    :type HsmIpAddress: string
    :param HsmIpAddress: [REQUIRED]
            The IP address that the Amazon Redshift cluster must use to access the HSM.
            

    :type HsmPartitionName: string
    :param HsmPartitionName: [REQUIRED]
            The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.
            

    :type HsmPartitionPassword: string
    :param HsmPartitionPassword: [REQUIRED]
            The password required to access the HSM partition.
            

    :type HsmServerPublicCertificate: string
    :param HsmServerPublicCertificate: [REQUIRED]
            The HSMs public certificate file. When using Cloud HSM, the file name is server.pem.
            

    :type Tags: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    :rtype: dict
    :return: {
        'HsmConfiguration': {
            'HsmConfigurationIdentifier': 'string',
            'Description': 'string',
            'HsmIpAddress': 'string',
            'HsmPartitionName': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_snapshot_copy_grant(SnapshotCopyGrantName=None, KmsKeyId=None, Tags=None):
    """
    Creates a snapshot copy grant that permits Amazon Redshift to use a customer master key (CMK) from AWS Key Management Service (AWS KMS) to encrypt copied snapshots in a destination region.
    For more information about managing snapshot copy grants, go to Amazon Redshift Database Encryption in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_snapshot_copy_grant(
        SnapshotCopyGrantName='string',
        KmsKeyId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SnapshotCopyGrantName: string
    :param SnapshotCopyGrantName: [REQUIRED]
            The name of the snapshot copy grant. This name must be unique in the region for the AWS account.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            Alphabetic characters must be lowercase.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for all clusters within an AWS account.
            

    :type KmsKeyId: string
    :param KmsKeyId: The unique identifier of the customer master key (CMK) to which to grant Amazon Redshift permission. If no key is specified, the default key is used.

    :type Tags: list
    :param Tags: A list of tag instances.
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    :rtype: dict
    :return: {
        'SnapshotCopyGrant': {
            'SnapshotCopyGrantName': 'string',
            'KmsKeyId': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_tags(ResourceName=None, Tags=None):
    """
    Adds one or more tags to a specified resource.
    A resource can have up to 10 tags. If you try to create more than 10 tags for a resource, you will receive an error and the attempt will fail.
    If you specify a key that already exists for the resource, the value for that key will be updated with the new value.
    See also: AWS API Documentation
    
    
    :example: response = client.create_tags(
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
            The Amazon Resource Name (ARN) to which you want to add the tag or tags. For example, arn:aws:redshift:us-east-1:123456789:cluster:t1 .
            

    :type Tags: list
    :param Tags: [REQUIRED]
            One or more name/value pairs to add as tags to the specified resource. Each tag name is passed in with the parameter Key and the corresponding value is passed in with the parameter Value . The Key and Value parameters are separated by a comma (,). Separate multiple tags with a space. For example, --tags 'Key'='owner','Value'='admin' 'Key'='environment','Value'='test' 'Key'='version','Value'='1.0' .
            (dict) --A tag consisting of a name/value pair for a resource.
            Key (string) --The key, or name, for the resource tag.
            Value (string) --The value for the resource tag.
            
            

    """
    pass

def delete_cluster(ClusterIdentifier=None, SkipFinalClusterSnapshot=None, FinalClusterSnapshotIdentifier=None):
    """
    Deletes a previously provisioned cluster. A successful response from the web service indicates that the request was received correctly. Use  DescribeClusters to monitor the status of the deletion. The delete operation cannot be canceled or reverted once submitted. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    If you want to shut down the cluster and retain it for future use, set SkipFinalClusterSnapshot to false and specify a name for FinalClusterSnapshotIdentifier . You can later restore this snapshot to resume using the cluster. If a final cluster snapshot is requested, the status of the cluster will be "final-snapshot" while the snapshot is being taken, then it's "deleting" once Amazon Redshift begins deleting the cluster.
    For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cluster(
        ClusterIdentifier='string',
        SkipFinalClusterSnapshot=True|False,
        FinalClusterSnapshotIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster to be deleted.
            Constraints:
            Must contain lowercase characters.
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            

    :type SkipFinalClusterSnapshot: boolean
    :param SkipFinalClusterSnapshot: Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted.
            Note
            The FinalClusterSnapshotIdentifier parameter must be specified if SkipFinalClusterSnapshot is false .
            Default: false
            

    :type FinalClusterSnapshotIdentifier: string
    :param FinalClusterSnapshotIdentifier: The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, SkipFinalClusterSnapshot must be false .
            Constraints:
            Must be 1 to 255 alphanumeric characters.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
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
    
    """
    pass

def delete_cluster_parameter_group(ParameterGroupName=None):
    """
    Deletes a specified Amazon Redshift parameter group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cluster_parameter_group(
        ParameterGroupName='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]
            The name of the parameter group to be deleted.
            Constraints:
            Must be the name of an existing cluster parameter group.
            Cannot delete a default cluster parameter group.
            

    """
    pass

def delete_cluster_security_group(ClusterSecurityGroupName=None):
    """
    Deletes an Amazon Redshift security group.
    For information about managing security groups, go to Amazon Redshift Cluster Security Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cluster_security_group(
        ClusterSecurityGroupName='string'
    )
    
    
    :type ClusterSecurityGroupName: string
    :param ClusterSecurityGroupName: [REQUIRED]
            The name of the cluster security group to be deleted.
            

    """
    pass

def delete_cluster_snapshot(SnapshotIdentifier=None, SnapshotClusterIdentifier=None):
    """
    Deletes the specified manual snapshot. The snapshot must be in the available state, with no other users authorized to access the snapshot.
    Unlike automated snapshots, manual snapshots are retained even after you delete your cluster. Amazon Redshift does not delete your manual snapshots. You must delete manual snapshot explicitly to avoid getting charged. If other accounts are authorized to access the snapshot, you must revoke all of the authorizations before you can delete the snapshot.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cluster_snapshot(
        SnapshotIdentifier='string',
        SnapshotClusterIdentifier='string'
    )
    
    
    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            The unique identifier of the manual snapshot to be deleted.
            Constraints: Must be the name of an existing snapshot that is in the available state.
            

    :type SnapshotClusterIdentifier: string
    :param SnapshotClusterIdentifier: The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
            Constraints: Must be the name of valid cluster.
            

    :rtype: dict
    :return: {
        'Snapshot': {
            'SnapshotIdentifier': 'string',
            'ClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Status': 'string',
            'Port': 123,
            'AvailabilityZone': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'ClusterVersion': 'string',
            'SnapshotType': 'string',
            'NodeType': 'string',
            'NumberOfNodes': 123,
            'DBName': 'string',
            'VpcId': 'string',
            'Encrypted': True|False,
            'KmsKeyId': 'string',
            'EncryptedWithHSM': True|False,
            'AccountsWithRestoreAccess': [
                {
                    'AccountId': 'string',
                    'AccountAlias': 'string'
                },
            ],
            'OwnerAccount': 'string',
            'TotalBackupSizeInMegaBytes': 123.0,
            'ActualIncrementalBackupSizeInMegaBytes': 123.0,
            'BackupProgressInMegaBytes': 123.0,
            'CurrentBackupRateInMegaBytesPerSecond': 123.0,
            'EstimatedSecondsToCompletion': 123,
            'ElapsedTimeInSeconds': 123,
            'SourceRegion': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RestorableNodeTypes': [
                'string',
            ],
            'EnhancedVpcRouting': True|False
        }
    }
    
    
    :returns: 
    CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
    DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
    DeleteClusterSnapshot returns status as "deleted".
    
    """
    pass

def delete_cluster_subnet_group(ClusterSubnetGroupName=None):
    """
    Deletes the specified cluster subnet group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cluster_subnet_group(
        ClusterSubnetGroupName='string'
    )
    
    
    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: [REQUIRED]
            The name of the cluster subnet group name to be deleted.
            

    """
    pass

def delete_event_subscription(SubscriptionName=None):
    """
    Deletes an Amazon Redshift event notification subscription.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_event_subscription(
        SubscriptionName='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]
            The name of the Amazon Redshift event notification subscription to be deleted.
            

    """
    pass

def delete_hsm_client_certificate(HsmClientCertificateIdentifier=None):
    """
    Deletes the specified HSM client certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_hsm_client_certificate(
        HsmClientCertificateIdentifier='string'
    )
    
    
    :type HsmClientCertificateIdentifier: string
    :param HsmClientCertificateIdentifier: [REQUIRED]
            The identifier of the HSM client certificate to be deleted.
            

    """
    pass

def delete_hsm_configuration(HsmConfigurationIdentifier=None):
    """
    Deletes the specified Amazon Redshift HSM configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_hsm_configuration(
        HsmConfigurationIdentifier='string'
    )
    
    
    :type HsmConfigurationIdentifier: string
    :param HsmConfigurationIdentifier: [REQUIRED]
            The identifier of the Amazon Redshift HSM configuration to be deleted.
            

    """
    pass

def delete_snapshot_copy_grant(SnapshotCopyGrantName=None):
    """
    Deletes the specified snapshot copy grant.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_snapshot_copy_grant(
        SnapshotCopyGrantName='string'
    )
    
    
    :type SnapshotCopyGrantName: string
    :param SnapshotCopyGrantName: [REQUIRED]
            The name of the snapshot copy grant to delete.
            

    """
    pass

def delete_tags(ResourceName=None, TagKeys=None):
    """
    Deletes a tag or tags from a resource. You must provide the ARN of the resource from which you want to delete the tag or tags.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags(
        ResourceName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]
            The Amazon Resource Name (ARN) from which you want to remove the tag or tags. For example, arn:aws:redshift:us-east-1:123456789:cluster:t1 .
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tag key that you want to delete.
            (string) --
            

    """
    pass

def describe_cluster_parameter_groups(ParameterGroupName=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns a list of Amazon Redshift parameter groups, including parameter groups you created and the default parameter group. For each parameter group, the response includes the parameter group name, description, and parameter group family name. You can optionally specify a name to retrieve the description of a specific parameter group.
    For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all parameter groups that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all parameter groups that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, parameter groups are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cluster_parameter_groups(
        ParameterGroupName='string',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: The name of a specific parameter group for which to return details. By default, details about all parameter groups and the default parameter group are returned.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterParameterGroups request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching cluster parameter groups that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag keys associated with them.
            (string) --
            

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching cluster parameter groups that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag values associated with them.
            (string) --
            

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ParameterGroups': [
            {
                'ParameterGroupName': 'string',
                'ParameterGroupFamily': 'string',
                'Description': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_cluster_parameters(ParameterGroupName=None, Source=None, MaxRecords=None, Marker=None):
    """
    Returns a detailed list of parameters contained within the specified Amazon Redshift parameter group. For each parameter the response includes information such as parameter name, description, data type, value, whether the parameter value is modifiable, and so on.
    You can specify source filter to retrieve parameters of only specific type. For example, to retrieve parameters that were modified by a user action such as from  ModifyClusterParameterGroup , you can specify source equal to user .
    For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cluster_parameters(
        ParameterGroupName='string',
        Source='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]
            The name of a cluster parameter group for which to return details.
            

    :type Source: string
    :param Source: The parameter types to return. Specify user to show parameters that are different form the default. Similarly, specify engine-default to show parameters that are the same as the default parameter group.
            Default: All parameter types returned.
            Valid Values: user | engine-default
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterParameters request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict
    :return: {
        'Parameters': [
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'ApplyType': 'static'|'dynamic',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_cluster_security_groups(ClusterSecurityGroupName=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns information about Amazon Redshift security groups. If the name of a security group is specified, the response will contain only information about only that security group.
    For information about managing security groups, go to Amazon Redshift Cluster Security Groups in the Amazon Redshift Cluster Management Guide .
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all security groups that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all security groups that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, security groups are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cluster_security_groups(
        ClusterSecurityGroupName='string',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type ClusterSecurityGroupName: string
    :param ClusterSecurityGroupName: The name of a cluster security group for which you are requesting details. You can specify either the Marker parameter or a ClusterSecurityGroupName parameter, but not both.
            Example: securitygroup1
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterSecurityGroups request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
            Constraints: You can specify either the ClusterSecurityGroupName parameter or the Marker parameter, but not both.
            

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching cluster security groups that are associated with the specified key or keys. For example, suppose that you have security groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag keys associated with them.
            (string) --
            

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching cluster security groups that are associated with the specified tag value or values. For example, suppose that you have security groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag values associated with them.
            (string) --
            

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ClusterSecurityGroups': [
            {
                'ClusterSecurityGroupName': 'string',
                'Description': 'string',
                'EC2SecurityGroups': [
                    {
                        'Status': 'string',
                        'EC2SecurityGroupName': 'string',
                        'EC2SecurityGroupOwnerId': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'IPRanges': [
                    {
                        'Status': 'string',
                        'CIDRIP': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_cluster_snapshots(ClusterIdentifier=None, SnapshotIdentifier=None, SnapshotType=None, StartTime=None, EndTime=None, MaxRecords=None, Marker=None, OwnerAccount=None, TagKeys=None, TagValues=None):
    """
    Returns one or more snapshot objects, which contain metadata about your cluster snapshots. By default, this operation returns information about all snapshots of all clusters that are owned by you AWS customer account. No information is returned for snapshots owned by inactive AWS customer accounts.
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all snapshots that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all snapshots that have any combination of those values are returned. Only snapshots that you own are returned in the response; shared snapshots are not returned with the tag key and tag value request parameters.
    If both tag keys and values are omitted from the request, snapshots are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cluster_snapshots(
        ClusterIdentifier='string',
        SnapshotIdentifier='string',
        SnapshotType='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        MaxRecords=123,
        Marker='string',
        OwnerAccount='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: The identifier of the cluster for which information about snapshots is requested.

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: The snapshot identifier of the snapshot about which to return information.

    :type SnapshotType: string
    :param SnapshotType: The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.
            Valid Values: automated | manual
            

    :type StartTime: datetime
    :param StartTime: A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2012-07-16T18:00:00Z
            

    :type EndTime: datetime
    :param EndTime: A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2012-07-16T18:00:00Z
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterSnapshots request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type OwnerAccount: string
    :param OwnerAccount: The AWS customer account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your AWS customer account, or do not specify the parameter.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.
            (string) --
            

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.
            (string) --
            

    :rtype: dict
    :return: {
        'Marker': 'string',
        'Snapshots': [
            {
                'SnapshotIdentifier': 'string',
                'ClusterIdentifier': 'string',
                'SnapshotCreateTime': datetime(2015, 1, 1),
                'Status': 'string',
                'Port': 123,
                'AvailabilityZone': 'string',
                'ClusterCreateTime': datetime(2015, 1, 1),
                'MasterUsername': 'string',
                'ClusterVersion': 'string',
                'SnapshotType': 'string',
                'NodeType': 'string',
                'NumberOfNodes': 123,
                'DBName': 'string',
                'VpcId': 'string',
                'Encrypted': True|False,
                'KmsKeyId': 'string',
                'EncryptedWithHSM': True|False,
                'AccountsWithRestoreAccess': [
                    {
                        'AccountId': 'string',
                        'AccountAlias': 'string'
                    },
                ],
                'OwnerAccount': 'string',
                'TotalBackupSizeInMegaBytes': 123.0,
                'ActualIncrementalBackupSizeInMegaBytes': 123.0,
                'BackupProgressInMegaBytes': 123.0,
                'CurrentBackupRateInMegaBytesPerSecond': 123.0,
                'EstimatedSecondsToCompletion': 123,
                'ElapsedTimeInSeconds': 123,
                'SourceRegion': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'RestorableNodeTypes': [
                    'string',
                ],
                'EnhancedVpcRouting': True|False
            },
        ]
    }
    
    
    :returns: 
    CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
    DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
    DeleteClusterSnapshot returns status as "deleted".
    
    """
    pass

def describe_cluster_subnet_groups(ClusterSubnetGroupName=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns one or more cluster subnet group objects, which contain metadata about your cluster subnet groups. By default, this operation returns information about all cluster subnet groups that are defined in you AWS account.
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all subnet groups that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all subnet groups that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, subnet groups are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cluster_subnet_groups(
        ClusterSubnetGroupName='string',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: The name of the cluster subnet group for which information is requested.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterSubnetGroups request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching cluster subnet groups that are associated with the specified key or keys. For example, suppose that you have subnet groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag keys associated with them.
            (string) --
            

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching cluster subnet groups that are associated with the specified tag value or values. For example, suppose that you have subnet groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag values associated with them.
            (string) --
            

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ClusterSubnetGroups': [
            {
                'ClusterSubnetGroupName': 'string',
                'Description': 'string',
                'VpcId': 'string',
                'SubnetGroupStatus': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        },
                        'SubnetStatus': 'string'
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_cluster_versions(ClusterVersion=None, ClusterParameterGroupFamily=None, MaxRecords=None, Marker=None):
    """
    Returns descriptions of the available Amazon Redshift cluster versions. You can call this operation even before creating any clusters to learn more about the Amazon Redshift versions. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cluster_versions(
        ClusterVersion='string',
        ClusterParameterGroupFamily='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ClusterVersion: string
    :param ClusterVersion: The specific cluster version to return.
            Example: 1.0
            

    :type ClusterParameterGroupFamily: string
    :param ClusterParameterGroupFamily: The name of a specific cluster parameter group family to return details for.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterVersions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ClusterVersions': [
            {
                'ClusterVersion': 'string',
                'ClusterParameterGroupFamily': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_clusters(ClusterIdentifier=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns properties of provisioned clusters including general cluster properties, cluster database properties, maintenance and backup properties, and security and access properties. This operation supports pagination. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all clusters that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all clusters that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, clusters are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_clusters(
        ClusterIdentifier='string',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.
            The default is that all clusters defined for an account are returned.
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusters request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
            Constraints: You can specify either the ClusterIdentifier parameter or the Marker parameter, but not both.
            

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.
            (string) --
            

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.
            (string) --
            

    :rtype: dict
    :return: {
        'Marker': 'string',
        'Clusters': [
            {
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
            },
        ]
    }
    
    
    :returns: 
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
    
    """
    pass

def describe_default_cluster_parameters(ParameterGroupFamily=None, MaxRecords=None, Marker=None):
    """
    Returns a list of parameter settings for the specified parameter group family.
    For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_default_cluster_parameters(
        ParameterGroupFamily='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ParameterGroupFamily: string
    :param ParameterGroupFamily: [REQUIRED]
            The name of the cluster parameter group family.
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeDefaultClusterParameters request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict
    :return: {
        'DefaultClusterParameters': {
            'ParameterGroupFamily': 'string',
            'Marker': 'string',
            'Parameters': [
                {
                    'ParameterName': 'string',
                    'ParameterValue': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'ApplyType': 'static'|'dynamic',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_event_categories(SourceType=None):
    """
    Displays a list of event categories for all event source types, or for a specified source type. For a list of the event categories and source types, go to Amazon Redshift Event Notifications .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_categories(
        SourceType='string'
    )
    
    
    :type SourceType: string
    :param SourceType: The source type, such as cluster or parameter group, to which the described event categories apply.
            Valid values: cluster, cluster-snapshot, cluster-parameter-group, and cluster-security-group.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_event_subscriptions(SubscriptionName=None, MaxRecords=None, Marker=None):
    """
    Lists descriptions of all the Amazon Redshift event notifications subscription for a customer account. If you specify a subscription name, lists the description for that subscription.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_subscriptions(
        SubscriptionName='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: The name of the Amazon Redshift event notification subscription to be described.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEventSubscriptions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict
    :return: {
        'Marker': 'string',
        'EventSubscriptionsList': [
            {
                'CustomerAwsId': 'string',
                'CustSubscriptionId': 'string',
                'SnsTopicArn': 'string',
                'Status': 'string',
                'SubscriptionCreationTime': datetime(2015, 1, 1),
                'SourceType': 'string',
                'SourceIdsList': [
                    'string',
                ],
                'EventCategoriesList': [
                    'string',
                ],
                'Severity': 'string',
                'Enabled': True|False,
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Can be one of the following: active | no-permission | topic-not-exist
    The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.
    
    """
    pass

def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, MaxRecords=None, Marker=None):
    """
    Returns events related to clusters, security groups, snapshots, and parameter groups for the past 14 days. Events specific to a particular cluster, security group, snapshot or parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_events(
        SourceIdentifier='string',
        SourceType='cluster'|'cluster-parameter-group'|'cluster-security-group'|'cluster-snapshot',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Duration=123,
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type SourceIdentifier: string
    :param SourceIdentifier: The identifier of the event source for which events will be returned. If this parameter is not specified, then all sources are included in the response.
            Constraints:
            If SourceIdentifier is supplied, SourceType must also be provided.
            Specify a cluster identifier when SourceType is cluster .
            Specify a cluster security group name when SourceType is cluster-security-group .
            Specify a cluster parameter group name when SourceType is cluster-parameter-group .
            Specify a cluster snapshot identifier when SourceType is cluster-snapshot .
            

    :type SourceType: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.
            Constraints:
            If SourceType is supplied, SourceIdentifier must also be provided.
            Specify cluster when SourceIdentifier is a cluster identifier.
            Specify cluster-security-group when SourceIdentifier is a cluster security group name.
            Specify cluster-parameter-group when SourceIdentifier is a cluster parameter group name.
            Specify cluster-snapshot when SourceIdentifier is a cluster snapshot identifier.
            

    :type StartTime: datetime
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2009-07-08T18:00Z
            

    :type EndTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2009-07-08T18:00Z
            

    :type Duration: integer
    :param Duration: The number of minutes prior to the time of the request for which to retrieve events. For example, if the request is sent at 18:00 and you specify a duration of 60, then only events which have occurred after 17:00 will be returned.
            Default: 60
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEvents request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict
    :return: {
        'Marker': 'string',
        'Events': [
            {
                'SourceIdentifier': 'string',
                'SourceType': 'cluster'|'cluster-parameter-group'|'cluster-security-group'|'cluster-snapshot',
                'Message': 'string',
                'EventCategories': [
                    'string',
                ],
                'Severity': 'string',
                'Date': datetime(2015, 1, 1),
                'EventId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_hsm_client_certificates(HsmClientCertificateIdentifier=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns information about the specified HSM client certificate. If no certificate ID is specified, returns information about all the HSM certificates owned by your AWS customer account.
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM client certificates that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all HSM client certificates that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, HSM client certificates are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_hsm_client_certificates(
        HsmClientCertificateIdentifier='string',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type HsmClientCertificateIdentifier: string
    :param HsmClientCertificateIdentifier: The identifier of a specific HSM client certificate for which you want information. If no identifier is specified, information is returned for all HSM client certificates owned by your AWS customer account.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeHsmClientCertificates request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching HSM client certificates that are associated with the specified key or keys. For example, suppose that you have HSM client certificates that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag keys associated with them.
            (string) --
            

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching HSM client certificates that are associated with the specified tag value or values. For example, suppose that you have HSM client certificates that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag values associated with them.
            (string) --
            

    :rtype: dict
    :return: {
        'Marker': 'string',
        'HsmClientCertificates': [
            {
                'HsmClientCertificateIdentifier': 'string',
                'HsmClientCertificatePublicKey': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_hsm_configurations(HsmConfigurationIdentifier=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns information about the specified Amazon Redshift HSM configuration. If no configuration ID is specified, returns information about all the HSM configurations owned by your AWS customer account.
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM connections that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all HSM connections that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, HSM connections are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_hsm_configurations(
        HsmConfigurationIdentifier='string',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type HsmConfigurationIdentifier: string
    :param HsmConfigurationIdentifier: The identifier of a specific Amazon Redshift HSM configuration to be described. If no identifier is specified, information is returned for all HSM configurations owned by your AWS customer account.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeHsmConfigurations request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching HSM configurations that are associated with the specified key or keys. For example, suppose that you have HSM configurations that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag keys associated with them.
            (string) --
            

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching HSM configurations that are associated with the specified tag value or values. For example, suppose that you have HSM configurations that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag values associated with them.
            (string) --
            

    :rtype: dict
    :return: {
        'Marker': 'string',
        'HsmConfigurations': [
            {
                'HsmConfigurationIdentifier': 'string',
                'Description': 'string',
                'HsmIpAddress': 'string',
                'HsmPartitionName': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_logging_status(ClusterIdentifier=None):
    """
    Describes whether information, such as queries and connection attempts, is being logged for the specified Amazon Redshift cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_logging_status(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster from which to get the logging status.
            Example: examplecluster
            

    :rtype: dict
    :return: {
        'LoggingEnabled': True|False,
        'BucketName': 'string',
        'S3KeyPrefix': 'string',
        'LastSuccessfulDeliveryTime': datetime(2015, 1, 1),
        'LastFailureTime': datetime(2015, 1, 1),
        'LastFailureMessage': 'string'
    }
    
    
    """
    pass

def describe_orderable_cluster_options(ClusterVersion=None, NodeType=None, MaxRecords=None, Marker=None):
    """
    Returns a list of orderable cluster options. Before you create a new cluster you can use this operation to find what options are available, such as the EC2 Availability Zones (AZ) in the specific AWS region that you can specify, and the node types you can request. The node types differ by available storage, memory, CPU and price. With the cost involved you might want to obtain a list of cluster options in the specific region and specify values when creating a cluster. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_orderable_cluster_options(
        ClusterVersion='string',
        NodeType='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ClusterVersion: string
    :param ClusterVersion: The version filter value. Specify this parameter to show only the available offerings matching the specified version.
            Default: All versions.
            Constraints: Must be one of the version returned from DescribeClusterVersions .
            

    :type NodeType: string
    :param NodeType: The node type filter value. Specify this parameter to show only the available offerings matching the specified node type.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeOrderableClusterOptions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict
    :return: {
        'OrderableClusterOptions': [
            {
                'ClusterVersion': 'string',
                'ClusterType': 'string',
                'NodeType': 'string',
                'AvailabilityZones': [
                    {
                        'Name': 'string'
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_reserved_node_offerings(ReservedNodeOfferingId=None, MaxRecords=None, Marker=None):
    """
    Returns a list of the available reserved node offerings by Amazon Redshift with their descriptions including the node type, the fixed and recurring costs of reserving the node and duration the node will be reserved for you. These descriptions help you determine which reserve node offering you want to purchase. You then use the unique offering ID in you call to  PurchaseReservedNodeOffering to reserve one or more nodes for your Amazon Redshift cluster.
    For more information about reserved node offerings, go to Purchasing Reserved Nodes in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_reserved_node_offerings(
        ReservedNodeOfferingId='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReservedNodeOfferingId: string
    :param ReservedNodeOfferingId: The unique identifier for the offering.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeReservedNodeOfferings request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ReservedNodeOfferings': [
            {
                'ReservedNodeOfferingId': 'string',
                'NodeType': 'string',
                'Duration': 123,
                'FixedPrice': 123.0,
                'UsagePrice': 123.0,
                'CurrencyCode': 'string',
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
    
    
    """
    pass

def describe_reserved_nodes(ReservedNodeId=None, MaxRecords=None, Marker=None):
    """
    Returns the descriptions of the reserved nodes.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_reserved_nodes(
        ReservedNodeId='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReservedNodeId: string
    :param ReservedNodeId: Identifier for the node reservation.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeReservedNodes request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict
    :return: {
        'Marker': 'string',
        'ReservedNodes': [
            {
                'ReservedNodeId': 'string',
                'ReservedNodeOfferingId': 'string',
                'NodeType': 'string',
                'StartTime': datetime(2015, 1, 1),
                'Duration': 123,
                'FixedPrice': 123.0,
                'UsagePrice': 123.0,
                'CurrencyCode': 'string',
                'NodeCount': 123,
                'State': 'string',
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
    pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
    active-This reserved node is owned by the caller and is available for use.
    payment-failed-Payment failed for the purchase attempt.
    
    """
    pass

def describe_resize(ClusterIdentifier=None):
    """
    Returns information about the last resize operation for the specified cluster. If no resize operation has ever been initiated for the specified cluster, a HTTP 404 error is returned. If a resize operation was initiated and completed, the status of the resize remains as SUCCEEDED until the next resize.
    A resize operation can be requested using  ModifyCluster and specifying a different number or type of nodes for the cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_resize(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of a cluster whose resize progress you are requesting. This parameter is case-sensitive.
            By default, resize operations for all clusters defined for an AWS account are returned.
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_snapshot_copy_grants(SnapshotCopyGrantName=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns a list of snapshot copy grants owned by the AWS account in the destination region.
    For more information about managing snapshot copy grants, go to Amazon Redshift Database Encryption in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_snapshot_copy_grants(
        SnapshotCopyGrantName='string',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type SnapshotCopyGrantName: string
    :param SnapshotCopyGrantName: The name of the snapshot copy grant.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
            Default: 100
            Constraints: minimum 20, maximum 100.
            

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeSnapshotCopyGrant request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
            Constraints: You can specify either the SnapshotCopyGrantName parameter or the Marker parameter, but not both.
            

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
            (string) --
            

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
            (string) --
            

    :rtype: dict
    :return: {
        'Marker': 'string',
        'SnapshotCopyGrants': [
            {
                'SnapshotCopyGrantName': 'string',
                'KmsKeyId': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_table_restore_status(ClusterIdentifier=None, TableRestoreRequestId=None, MaxRecords=None, Marker=None):
    """
    Lists the status of one or more table restore requests made using the  RestoreTableFromClusterSnapshot API action. If you don't specify a value for the TableRestoreRequestId parameter, then DescribeTableRestoreStatus returns the status of all table restore requests ordered by the date and time of the request in ascending order. Otherwise DescribeTableRestoreStatus returns the status of the table specified by TableRestoreRequestId .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_table_restore_status(
        ClusterIdentifier='string',
        TableRestoreRequestId='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: The Amazon Redshift cluster that the table is being restored to.

    :type TableRestoreRequestId: string
    :param TableRestoreRequestId: The identifier of the table restore request to return status for. If you don't specify a TableRestoreRequestId value, then DescribeTableRestoreStatus returns the status of all in-progress table restore requests.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeTableRestoreStatus request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the MaxRecords parameter.

    :rtype: dict
    :return: {
        'TableRestoreStatusDetails': [
            {
                'TableRestoreRequestId': 'string',
                'Status': 'PENDING'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'CANCELED',
                'Message': 'string',
                'RequestTime': datetime(2015, 1, 1),
                'ProgressInMegaBytes': 123,
                'TotalDataInMegaBytes': 123,
                'ClusterIdentifier': 'string',
                'SnapshotIdentifier': 'string',
                'SourceDatabaseName': 'string',
                'SourceSchemaName': 'string',
                'SourceTableName': 'string',
                'TargetDatabaseName': 'string',
                'TargetSchemaName': 'string',
                'NewTableName': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_tags(ResourceName=None, ResourceType=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns a list of tags. You can return tags from a specific resource by specifying an ARN, or you can return all tags for a given type of resource, such as clusters, snapshots, and so on.
    The following are limitations for DescribeTags :
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all resources that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all resources that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, resources are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_tags(
        ResourceName='string',
        ResourceType='string',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, arn:aws:redshift:us-east-1:123456789:cluster:t1 .

    :type ResourceType: string
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
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.

    :type Marker: string
    :param Marker: A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the marker parameter and retrying the command. If the marker field is empty, all response records have been retrieved for the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
            (string) --
            

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
            (string) --
            

    :rtype: dict
    :return: {
        'TaggedResources': [
            {
                'Tag': {
                    'Key': 'string',
                    'Value': 'string'
                },
                'ResourceName': 'string',
                'ResourceType': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    ResourceName (string) -- The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, arn:aws:redshift:us-east-1:123456789:cluster:t1 .
    ResourceType (string) -- The type of resource with which you want to view tags. Valid resource types are:
    
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
    
    MaxRecords (integer) -- The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
    Marker (string) -- A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the marker parameter and retrying the command. If the marker field is empty, all response records have been retrieved for the request.
    TagKeys (list) -- A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
    
    (string) --
    
    
    TagValues (list) -- A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
    
    (string) --
    
    
    
    """
    pass

def disable_logging(ClusterIdentifier=None):
    """
    Stops logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_logging(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster on which logging is to be stopped.
            Example: examplecluster
            

    :rtype: dict
    :return: {
        'LoggingEnabled': True|False,
        'BucketName': 'string',
        'S3KeyPrefix': 'string',
        'LastSuccessfulDeliveryTime': datetime(2015, 1, 1),
        'LastFailureTime': datetime(2015, 1, 1),
        'LastFailureMessage': 'string'
    }
    
    
    """
    pass

def disable_snapshot_copy(ClusterIdentifier=None):
    """
    Disables the automatic copying of snapshots from one region to another region for a specified cluster.
    If your cluster and its snapshots are encrypted using a customer master key (CMK) from AWS KMS, use  DeleteSnapshotCopyGrant to delete the grant that grants Amazon Redshift permission to the CMK in the destination region.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_snapshot_copy(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the source cluster that you want to disable copying of snapshots to a destination region.
            Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
    in-sync : The parameter value is in sync with the database.
    pending-reboot : The parameter value will be applied after the cluster reboots.
    applying : The parameter value is being applied to the database.
    invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
    apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
    apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
    unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.
    
    """
    pass

def enable_logging(ClusterIdentifier=None, BucketName=None, S3KeyPrefix=None):
    """
    Starts logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_logging(
        ClusterIdentifier='string',
        BucketName='string',
        S3KeyPrefix='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster on which logging is to be started.
            Example: examplecluster
            

    :type BucketName: string
    :param BucketName: [REQUIRED]
            The name of an existing S3 bucket where the log files are to be stored.
            Constraints:
            Must be in the same region as the cluster
            The cluster must have read bucket and put object permissions
            

    :type S3KeyPrefix: string
    :param S3KeyPrefix: The prefix applied to the log file names.
            Constraints:
            Cannot exceed 512 characters
            Cannot contain spaces( ), double quotes ('), single quotes ('), a backslash (), or control characters. The hexadecimal codes for invalid characters are:
            x00 to x20
            x22
            x27
            x5c
            x7f or larger
            

    :rtype: dict
    :return: {
        'LoggingEnabled': True|False,
        'BucketName': 'string',
        'S3KeyPrefix': 'string',
        'LastSuccessfulDeliveryTime': datetime(2015, 1, 1),
        'LastFailureTime': datetime(2015, 1, 1),
        'LastFailureMessage': 'string'
    }
    
    
    """
    pass

def enable_snapshot_copy(ClusterIdentifier=None, DestinationRegion=None, RetentionPeriod=None, SnapshotCopyGrantName=None):
    """
    Enables the automatic copy of snapshots from one region to another region for a specified cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_snapshot_copy(
        ClusterIdentifier='string',
        DestinationRegion='string',
        RetentionPeriod=123,
        SnapshotCopyGrantName='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the source cluster to copy snapshots from.
            Constraints: Must be the valid name of an existing cluster that does not already have cross-region snapshot copy enabled.
            

    :type DestinationRegion: string
    :param DestinationRegion: [REQUIRED]
            The destination region that you want to copy snapshots to.
            Constraints: Must be the name of a valid region. For more information, see Regions and Endpoints in the Amazon Web Services General Reference.
            

    :type RetentionPeriod: integer
    :param RetentionPeriod: The number of days to retain automated snapshots in the destination region after they are copied from the source region.
            Default: 7.
            Constraints: Must be at least 1 and no more than 35.
            

    :type SnapshotCopyGrantName: string
    :param SnapshotCopyGrantName: The name of the snapshot copy grant to use when snapshots of an AWS KMS-encrypted cluster are copied to the destination region.

    :rtype: dict
    :return: {
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
    
    
    :returns: 
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

def get_cluster_credentials(DbUser=None, DbName=None, ClusterIdentifier=None, DurationSeconds=None, AutoCreate=None, DbGroups=None):
    """
    Returns a database user name and temporary password with temporary authorization to log in to an Amazon Redshift database. The action returns the database user name prefixed with IAM: if AutoCreate is False or IAMA: if AutoCreate is True . You can optionally specify one or more database user groups that the user will join at log in. By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes). For more information, see Generating IAM Database User Credentials in the Amazon Redshift Cluster Management Guide.
    The IAM user or role that executes GetClusterCredentials must have an IAM policy attached that allows the redshift:GetClusterCredentials action with access to the dbuser resource on the cluster. The user name specified for dbuser in the IAM policy and the user name specified for the DbUser parameter must match.
    If the DbGroups parameter is specified, the IAM policy must allow the redshift:JoinGroup action with access to the listed dbgroups .
    In addition, if the AutoCreate parameter is set to True , then the policy must include the redshift:CreateClusterUser privilege.
    If the DbName parameter is specified, the IAM policy must allow access to the resource dbname for the specified database name.
    See also: AWS API Documentation
    
    
    :example: response = client.get_cluster_credentials(
        DbUser='string',
        DbName='string',
        ClusterIdentifier='string',
        DurationSeconds=123,
        AutoCreate=True|False,
        DbGroups=[
            'string',
        ]
    )
    
    
    :type DbUser: string
    :param DbUser: [REQUIRED]
            The name of a database user. If a user name matching DbUser exists in the database, the temporary user credentials have the same permissions as the existing user. If DbUser doesn't exist in the database and Autocreate is True , a new user is created using the value for DbUser with PUBLIC permissions. If a database user matching the value for DbUser doesn't exist and Autocreate is False , then the command succeeds but the connection attempt will fail because the user doesn't exist in the database.
            For more information, see CREATE USER in the Amazon Redshift Database Developer Guide.
            Constraints:
            Must be 1 to 128 alphanumeric characters or hyphens
            Must contain only lowercase letters.
            First character must be a letter.
            Must not contain a colon ( : ) or slash ( / ).
            Cannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.
            

    :type DbName: string
    :param DbName: The name of a database that DbUser is authorized to log on to. If DbName is not specified, DbUser can log in to any existing database.
            Constraints:
            Must be 1 to 64 alphanumeric characters or hyphens
            Must contain only lowercase letters.
            Cannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.
            

    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the cluster that contains the database for which your are requesting credentials. This parameter is case sensitive.
            

    :type DurationSeconds: integer
    :param DurationSeconds: The number of seconds until the returned temporary password expires.
            Constraint: minimum 900, maximum 3600.
            Default: 900
            

    :type AutoCreate: boolean
    :param AutoCreate: Create a database user with the name specified for DbUser if one does not exist.

    :type DbGroups: list
    :param DbGroups: A list of the names of existing database groups that DbUser will join for the current session. If not specified, the new user is added only to PUBLIC.
            (string) --
            

    :rtype: dict
    :return: {
        'DbUser': 'string',
        'DbPassword': 'string',
        'Expiration': datetime(2015, 1, 1)
    }
    
    
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

def modify_cluster(ClusterIdentifier=None, ClusterType=None, NodeType=None, NumberOfNodes=None, ClusterSecurityGroups=None, VpcSecurityGroupIds=None, MasterUserPassword=None, ClusterParameterGroupName=None, AutomatedSnapshotRetentionPeriod=None, PreferredMaintenanceWindow=None, ClusterVersion=None, AllowVersionUpgrade=None, HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None, NewClusterIdentifier=None, PubliclyAccessible=None, ElasticIp=None, EnhancedVpcRouting=None):
    """
    Modifies the settings for a cluster. For example, you can add another security or parameter group, update the preferred maintenance window, or change the master user password. Resetting a cluster password or modifying the security groups associated with a cluster do not need a reboot. However, modifying a parameter group requires a reboot for parameters to take effect. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    You can also change node type and the number of nodes to scale up or down the cluster. When resizing a cluster, you must specify both the number of nodes and the node type even if one of the parameters does not change.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_cluster(
        ClusterIdentifier='string',
        ClusterType='string',
        NodeType='string',
        NumberOfNodes=123,
        ClusterSecurityGroups=[
            'string',
        ],
        VpcSecurityGroupIds=[
            'string',
        ],
        MasterUserPassword='string',
        ClusterParameterGroupName='string',
        AutomatedSnapshotRetentionPeriod=123,
        PreferredMaintenanceWindow='string',
        ClusterVersion='string',
        AllowVersionUpgrade=True|False,
        HsmClientCertificateIdentifier='string',
        HsmConfigurationIdentifier='string',
        NewClusterIdentifier='string',
        PubliclyAccessible=True|False,
        ElasticIp='string',
        EnhancedVpcRouting=True|False
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the cluster to be modified.
            Example: examplecluster
            

    :type ClusterType: string
    :param ClusterType: The new cluster type.
            When you submit your cluster resize request, your existing cluster goes into a read-only mode. After Amazon Redshift provisions a new cluster based on your resize requirements, there will be outage for a period while the old cluster is deleted and your connection is switched to the new cluster. You can use DescribeResize to track the progress of the resize request.
            Valid Values: multi-node | single-node
            

    :type NodeType: string
    :param NodeType: The new node type of the cluster. If you specify a new node type, you must also specify the number of nodes parameter.
            When you submit your request to resize a cluster, Amazon Redshift sets access permissions for the cluster to read-only. After Amazon Redshift provisions a new cluster according to your resize requirements, there will be a temporary outage while the old cluster is deleted and your connection is switched to the new cluster. When the new connection is complete, the original access permissions for the cluster are restored. You can use DescribeResize to track the progress of the resize request.
            Valid Values: ds1.xlarge | ds1.8xlarge | ds2.xlarge | ds2.8xlarge | dc1.large | dc1.8xlarge .
            

    :type NumberOfNodes: integer
    :param NumberOfNodes: The new number of nodes of the cluster. If you specify a new number of nodes, you must also specify the node type parameter.
            When you submit your request to resize a cluster, Amazon Redshift sets access permissions for the cluster to read-only. After Amazon Redshift provisions a new cluster according to your resize requirements, there will be a temporary outage while the old cluster is deleted and your connection is switched to the new cluster. When the new connection is complete, the original access permissions for the cluster are restored. You can use DescribeResize to track the progress of the resize request.
            Valid Values: Integer greater than 0 .
            

    :type ClusterSecurityGroups: list
    :param ClusterSecurityGroups: A list of cluster security groups to be authorized on this cluster. This change is asynchronously applied as soon as possible.
            Security groups currently associated with the cluster, and not in the list of groups to apply, will be revoked from the cluster.
            Constraints:
            Must be 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            (string) --
            

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of virtual private cloud (VPC) security groups to be associated with the cluster.
            (string) --
            

    :type MasterUserPassword: string
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
            

    :type ClusterParameterGroupName: string
    :param ClusterParameterGroupName: The name of the cluster parameter group to apply to this cluster. This change is applied only after the cluster is rebooted. To reboot a cluster use RebootCluster .
            Default: Uses existing setting.
            Constraints: The cluster parameter group must be in the same parameter group family that matches the cluster version.
            

    :type AutomatedSnapshotRetentionPeriod: integer
    :param AutomatedSnapshotRetentionPeriod: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with CreateClusterSnapshot .
            If you decrease the automated snapshot retention period from its current value, existing automated snapshots that fall outside of the new retention period will be immediately deleted.
            Default: Uses existing setting.
            Constraints: Must be a value from 0 to 35.
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, if necessary. If system maintenance is necessary during the window, it may result in an outage.
            This maintenance window change is made immediately. If the new maintenance window indicates the current time, there must be at least 120 minutes between the current time and end of the window in order to ensure that pending changes are applied.
            Default: Uses existing setting.
            Format: ddd:hh24:mi-ddd:hh24:mi, for example wed:07:30-wed:08:00 .
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Must be at least 30 minutes.
            

    :type ClusterVersion: string
    :param ClusterVersion: The new version number of the Amazon Redshift engine to upgrade to.
            For major version upgrades, if a non-default cluster parameter group is currently in use, a new cluster parameter group in the cluster parameter group family for the new version must be specified. The new cluster parameter group can be the default for that cluster parameter group family. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
            Example: 1.0
            

    :type AllowVersionUpgrade: boolean
    :param AllowVersionUpgrade: If true , major version upgrades will be applied automatically to the cluster during the maintenance window.
            Default: false
            

    :type HsmClientCertificateIdentifier: string
    :param HsmClientCertificateIdentifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

    :type HsmConfigurationIdentifier: string
    :param HsmConfigurationIdentifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

    :type NewClusterIdentifier: string
    :param NewClusterIdentifier: The new identifier for the cluster.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            Alphabetic characters must be lowercase.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for all clusters within an AWS account.
            Example: examplecluster
            

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: If true , the cluster can be accessed from a public network. Only clusters in VPCs can be set to be publicly available.

    :type ElasticIp: string
    :param ElasticIp: The Elastic IP (EIP) address for the cluster.
            Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to Supported Platforms to Launch Your Cluster in the Amazon Redshift Cluster Management Guide.
            

    :type EnhancedVpcRouting: boolean
    :param EnhancedVpcRouting: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
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
    
    """
    pass

def modify_cluster_iam_roles(ClusterIdentifier=None, AddIamRoles=None, RemoveIamRoles=None):
    """
    Modifies the list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.
    A cluster can have up to 10 IAM roles associated at any time.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_cluster_iam_roles(
        ClusterIdentifier='string',
        AddIamRoles=[
            'string',
        ],
        RemoveIamRoles=[
            'string',
        ]
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the cluster for which you want to associate or disassociate IAM roles.
            

    :type AddIamRoles: list
    :param AddIamRoles: Zero or more IAM roles to associate with the cluster. The roles must be in their Amazon Resource Name (ARN) format. You can associate up to 10 IAM roles with a single cluster in a single request.
            (string) --
            

    :type RemoveIamRoles: list
    :param RemoveIamRoles: Zero or more IAM roles in ARN format to disassociate from the cluster. You can disassociate up to 10 IAM roles from a single cluster in a single request.
            (string) --
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
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
    
    """
    pass

def modify_cluster_parameter_group(ParameterGroupName=None, Parameters=None):
    """
    Modifies the parameters of a parameter group.
    For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.modify_cluster_parameter_group(
        ParameterGroupName='string',
        Parameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'ApplyType': 'static'|'dynamic',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string'
            },
        ]
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]
            The name of the parameter group to be modified.
            

    :type Parameters: list
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
            
            

    :rtype: dict
    :return: {
        'ParameterGroupName': 'string',
        'ParameterGroupStatus': 'string'
    }
    
    
    """
    pass

def modify_cluster_subnet_group(ClusterSubnetGroupName=None, Description=None, SubnetIds=None):
    """
    Modifies a cluster subnet group to include the specified list of VPC subnets. The operation replaces the existing list of subnets with the new list of subnets.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_cluster_subnet_group(
        ClusterSubnetGroupName='string',
        Description='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: [REQUIRED]
            The name of the subnet group to be modified.
            

    :type Description: string
    :param Description: A text description of the subnet group to be modified.

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]
            An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
            (string) --
            

    :rtype: dict
    :return: {
        'ClusterSubnetGroup': {
            'ClusterSubnetGroupName': 'string',
            'Description': 'string',
            'VpcId': 'string',
            'SubnetGroupStatus': 'string',
            'Subnets': [
                {
                    'SubnetIdentifier': 'string',
                    'SubnetAvailabilityZone': {
                        'Name': 'string'
                    },
                    'SubnetStatus': 'string'
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def modify_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, SourceIds=None, EventCategories=None, Severity=None, Enabled=None):
    """
    Modifies an existing Amazon Redshift event notification subscription.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_event_subscription(
        SubscriptionName='string',
        SnsTopicArn='string',
        SourceType='string',
        SourceIds=[
            'string',
        ],
        EventCategories=[
            'string',
        ],
        Severity='string',
        Enabled=True|False
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]
            The name of the modified Amazon Redshift event notification subscription.
            

    :type SnsTopicArn: string
    :param SnsTopicArn: The Amazon Resource Name (ARN) of the SNS topic to be used by the event notification subscription.

    :type SourceType: string
    :param SourceType: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account. You must specify a source type in order to specify source IDs.
            Valid values: cluster, cluster-parameter-group, cluster-security-group, and cluster-snapshot.
            

    :type SourceIds: list
    :param SourceIds: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.
            Example: my-cluster-1, my-cluster-2
            Example: my-snapshot-20131010
            (string) --
            

    :type EventCategories: list
    :param EventCategories: Specifies the Amazon Redshift event categories to be published by the event notification subscription.
            Values: Configuration, Management, Monitoring, Security
            (string) --
            

    :type Severity: string
    :param Severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription.
            Values: ERROR, INFO
            

    :type Enabled: boolean
    :param Enabled: A Boolean value indicating if the subscription is enabled. true indicates the subscription is enabled

    :rtype: dict
    :return: {
        'EventSubscription': {
            'CustomerAwsId': 'string',
            'CustSubscriptionId': 'string',
            'SnsTopicArn': 'string',
            'Status': 'string',
            'SubscriptionCreationTime': datetime(2015, 1, 1),
            'SourceType': 'string',
            'SourceIdsList': [
                'string',
            ],
            'EventCategoriesList': [
                'string',
            ],
            'Severity': 'string',
            'Enabled': True|False,
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Can be one of the following: active | no-permission | topic-not-exist
    The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.
    
    """
    pass

def modify_snapshot_copy_retention_period(ClusterIdentifier=None, RetentionPeriod=None):
    """
    Modifies the number of days to retain automated snapshots in the destination region after they are copied from the source region.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_snapshot_copy_retention_period(
        ClusterIdentifier='string',
        RetentionPeriod=123
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the cluster for which you want to change the retention period for automated snapshots that are copied to a destination region.
            Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.
            

    :type RetentionPeriod: integer
    :param RetentionPeriod: [REQUIRED]
            The number of days to retain automated snapshots in the destination region after they are copied from the source region.
            If you decrease the retention period for automated snapshots that are copied to a destination region, Amazon Redshift will delete any existing automated snapshots that were copied to the destination region and that fall outside of the new retention period.
            Constraints: Must be at least 1 and no more than 35.
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
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
    
    """
    pass

def purchase_reserved_node_offering(ReservedNodeOfferingId=None, NodeCount=None):
    """
    Allows you to purchase reserved nodes. Amazon Redshift offers a predefined set of reserved node offerings. You can purchase one or more of the offerings. You can call the  DescribeReservedNodeOfferings API to obtain the available reserved node offerings. You can call this API by providing a specific reserved node offering and the number of nodes you want to reserve.
    For more information about reserved node offerings, go to Purchasing Reserved Nodes in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.purchase_reserved_node_offering(
        ReservedNodeOfferingId='string',
        NodeCount=123
    )
    
    
    :type ReservedNodeOfferingId: string
    :param ReservedNodeOfferingId: [REQUIRED]
            The unique identifier of the reserved node offering you want to purchase.
            

    :type NodeCount: integer
    :param NodeCount: The number of reserved nodes that you want to purchase.
            Default: 1
            

    :rtype: dict
    :return: {
        'ReservedNode': {
            'ReservedNodeId': 'string',
            'ReservedNodeOfferingId': 'string',
            'NodeType': 'string',
            'StartTime': datetime(2015, 1, 1),
            'Duration': 123,
            'FixedPrice': 123.0,
            'UsagePrice': 123.0,
            'CurrencyCode': 'string',
            'NodeCount': 123,
            'State': 'string',
            'OfferingType': 'string',
            'RecurringCharges': [
                {
                    'RecurringChargeAmount': 123.0,
                    'RecurringChargeFrequency': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
    active-This reserved node is owned by the caller and is available for use.
    payment-failed-Payment failed for the purchase attempt.
    
    """
    pass

def reboot_cluster(ClusterIdentifier=None):
    """
    Reboots a cluster. This action is taken as soon as possible. It results in a momentary outage to the cluster, during which the cluster status is set to rebooting . A cluster event is created when the reboot is completed. Any pending cluster modifications (see  ModifyCluster ) are applied at this reboot. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_cluster(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The cluster identifier.
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
    in-sync : The parameter value is in sync with the database.
    pending-reboot : The parameter value will be applied after the cluster reboots.
    applying : The parameter value is being applied to the database.
    invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
    apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
    apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
    unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.
    
    """
    pass

def reset_cluster_parameter_group(ParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    Sets one or more parameters of the specified parameter group to their default values and sets the source values of the parameters to "engine-default". To reset the entire parameter group specify the ResetAllParameters parameter. For parameter changes to take effect you must reboot any associated clusters.
    See also: AWS API Documentation
    
    
    :example: response = client.reset_cluster_parameter_group(
        ParameterGroupName='string',
        ResetAllParameters=True|False,
        Parameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'ApplyType': 'static'|'dynamic',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string'
            },
        ]
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]
            The name of the cluster parameter group to be reset.
            

    :type ResetAllParameters: boolean
    :param ResetAllParameters: If true , all parameters in the specified parameter group will be reset to their default values.
            Default: true
            

    :type Parameters: list
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
            
            

    :rtype: dict
    :return: {
        'ParameterGroupName': 'string',
        'ParameterGroupStatus': 'string'
    }
    
    
    """
    pass

def restore_from_cluster_snapshot(ClusterIdentifier=None, SnapshotIdentifier=None, SnapshotClusterIdentifier=None, Port=None, AvailabilityZone=None, AllowVersionUpgrade=None, ClusterSubnetGroupName=None, PubliclyAccessible=None, OwnerAccount=None, HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None, ElasticIp=None, ClusterParameterGroupName=None, ClusterSecurityGroups=None, VpcSecurityGroupIds=None, PreferredMaintenanceWindow=None, AutomatedSnapshotRetentionPeriod=None, KmsKeyId=None, NodeType=None, EnhancedVpcRouting=None, AdditionalInfo=None, IamRoles=None):
    """
    Creates a new cluster from a snapshot. By default, Amazon Redshift creates the resulting cluster with the same configuration as the original cluster from which the snapshot was created, except that the new cluster is created with the default cluster security and parameter groups. After Amazon Redshift creates the cluster, you can use the  ModifyCluster API to associate a different security group and different parameter group with the restored cluster. If you are using a DS node type, you can also choose to change to another DS node type of the same size during restore.
    If you restore a cluster into a VPC, you must provide a cluster subnet group where you want the cluster restored.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.restore_from_cluster_snapshot(
        ClusterIdentifier='string',
        SnapshotIdentifier='string',
        SnapshotClusterIdentifier='string',
        Port=123,
        AvailabilityZone='string',
        AllowVersionUpgrade=True|False,
        ClusterSubnetGroupName='string',
        PubliclyAccessible=True|False,
        OwnerAccount='string',
        HsmClientCertificateIdentifier='string',
        HsmConfigurationIdentifier='string',
        ElasticIp='string',
        ClusterParameterGroupName='string',
        ClusterSecurityGroups=[
            'string',
        ],
        VpcSecurityGroupIds=[
            'string',
        ],
        PreferredMaintenanceWindow='string',
        AutomatedSnapshotRetentionPeriod=123,
        KmsKeyId='string',
        NodeType='string',
        EnhancedVpcRouting=True|False,
        AdditionalInfo='string',
        IamRoles=[
            'string',
        ]
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the cluster that will be created from restoring the snapshot.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            Alphabetic characters must be lowercase.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Must be unique for all clusters within an AWS account.
            

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive.
            Example: my-snapshot-id
            

    :type SnapshotClusterIdentifier: string
    :param SnapshotClusterIdentifier: The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

    :type Port: integer
    :param Port: The port number on which the cluster accepts connections.
            Default: The same port as the original cluster.
            Constraints: Must be between 1115 and 65535 .
            

    :type AvailabilityZone: string
    :param AvailabilityZone: The Amazon EC2 Availability Zone in which to restore the cluster.
            Default: A random, system-chosen Availability Zone.
            Example: us-east-1a
            

    :type AllowVersionUpgrade: boolean
    :param AllowVersionUpgrade: If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.
            Default: true
            

    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: The name of the subnet group where you want to cluster restored.
            A snapshot of cluster in VPC can be restored only in VPC. Therefore, you must provide subnet group name where you want the cluster restored.
            

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: If true , the cluster can be accessed from a public network.

    :type OwnerAccount: string
    :param OwnerAccount: The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

    :type HsmClientCertificateIdentifier: string
    :param HsmClientCertificateIdentifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

    :type HsmConfigurationIdentifier: string
    :param HsmConfigurationIdentifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

    :type ElasticIp: string
    :param ElasticIp: The elastic IP (EIP) address for the cluster.

    :type ClusterParameterGroupName: string
    :param ClusterParameterGroupName: The name of the parameter group to be associated with this cluster.
            Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to Working with Amazon Redshift Parameter Groups .
            Constraints:
            Must be 1 to 255 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            

    :type ClusterSecurityGroups: list
    :param ClusterSecurityGroups: A list of security groups to be associated with this cluster.
            Default: The default cluster security group for Amazon Redshift.
            Cluster security groups only apply to clusters outside of VPCs.
            (string) --
            

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
            Default: The default VPC security group is associated with the cluster.
            VPC security groups only apply to clusters in VPCs.
            (string) --
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which automated cluster maintenance can occur.
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: The value selected for the cluster from which the snapshot was taken. For more information about the time blocks for each region, see Maintenance Windows in Amazon Redshift Cluster Management Guide.
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Minimum 30-minute window.
            

    :type AutomatedSnapshotRetentionPeriod: integer
    :param AutomatedSnapshotRetentionPeriod: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with CreateClusterSnapshot .
            Default: The value selected for the cluster from which the snapshot was taken.
            Constraints: Must be a value from 0 to 35.
            

    :type KmsKeyId: string
    :param KmsKeyId: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster that you restore from a shared snapshot.

    :type NodeType: string
    :param NodeType: The node type that the restored cluster will be provisioned with.
            Default: The node type of the cluster from which the snapshot was taken. You can modify this if you are using any DS node type. In that case, you can choose to restore into another DS node type of the same size. For example, you can restore ds1.8xlarge into ds2.8xlarge, or ds2.xlarge into ds1.xlarge. If you have a DC instance type, you must restore into that same instance type and size. In other words, you can only restore a dc1.large instance type into another dc1.large instance type. For more information about node types, see About Clusters and Nodes in the Amazon Redshift Cluster Management Guide
            

    :type EnhancedVpcRouting: boolean
    :param EnhancedVpcRouting: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
            If this option is true , enhanced VPC routing is enabled.
            Default: false
            

    :type AdditionalInfo: string
    :param AdditionalInfo: Reserved.

    :type IamRoles: list
    :param IamRoles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM roles in a single request.
            A cluster can have up to 10 IAM roles associated at any time.
            (string) --
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
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
    
    """
    pass

def restore_table_from_cluster_snapshot(ClusterIdentifier=None, SnapshotIdentifier=None, SourceDatabaseName=None, SourceSchemaName=None, SourceTableName=None, TargetDatabaseName=None, TargetSchemaName=None, NewTableName=None):
    """
    Creates a new table from a table in an Amazon Redshift cluster snapshot. You must create the new table within the Amazon Redshift cluster that the snapshot was taken from.
    You cannot use RestoreTableFromClusterSnapshot to restore a table with the same name as an existing table in an Amazon Redshift cluster. That is, you cannot overwrite an existing table in a cluster with a restored table. If you want to replace your original table with a new, restored table, then rename or drop your original table before you call RestoreTableFromClusterSnapshot . When you have renamed your original table, then you can pass the original name of the table as the NewTableName parameter value in the call to RestoreTableFromClusterSnapshot . This way, you can replace the original table with the table created from the snapshot.
    See also: AWS API Documentation
    
    
    :example: response = client.restore_table_from_cluster_snapshot(
        ClusterIdentifier='string',
        SnapshotIdentifier='string',
        SourceDatabaseName='string',
        SourceSchemaName='string',
        SourceTableName='string',
        TargetDatabaseName='string',
        TargetSchemaName='string',
        NewTableName='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The identifier of the Amazon Redshift cluster to restore the table to.
            

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            The identifier of the snapshot to restore the table from. This snapshot must have been created from the Amazon Redshift cluster specified by the ClusterIdentifier parameter.
            

    :type SourceDatabaseName: string
    :param SourceDatabaseName: [REQUIRED]
            The name of the source database that contains the table to restore from.
            

    :type SourceSchemaName: string
    :param SourceSchemaName: The name of the source schema that contains the table to restore from. If you do not specify a SourceSchemaName value, the default is public .

    :type SourceTableName: string
    :param SourceTableName: [REQUIRED]
            The name of the source table to restore from.
            

    :type TargetDatabaseName: string
    :param TargetDatabaseName: The name of the database to restore the table to.

    :type TargetSchemaName: string
    :param TargetSchemaName: The name of the schema to restore the table to.

    :type NewTableName: string
    :param NewTableName: [REQUIRED]
            The name of the table to create as a result of the current request.
            

    :rtype: dict
    :return: {
        'TableRestoreStatus': {
            'TableRestoreRequestId': 'string',
            'Status': 'PENDING'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'CANCELED',
            'Message': 'string',
            'RequestTime': datetime(2015, 1, 1),
            'ProgressInMegaBytes': 123,
            'TotalDataInMegaBytes': 123,
            'ClusterIdentifier': 'string',
            'SnapshotIdentifier': 'string',
            'SourceDatabaseName': 'string',
            'SourceSchemaName': 'string',
            'SourceTableName': 'string',
            'TargetDatabaseName': 'string',
            'TargetSchemaName': 'string',
            'NewTableName': 'string'
        }
    }
    
    
    """
    pass

def revoke_cluster_security_group_ingress(ClusterSecurityGroupName=None, CIDRIP=None, EC2SecurityGroupName=None, EC2SecurityGroupOwnerId=None):
    """
    Revokes an ingress rule in an Amazon Redshift security group for a previously authorized IP range or Amazon EC2 security group. To add an ingress rule, see  AuthorizeClusterSecurityGroupIngress . For information about managing security groups, go to Amazon Redshift Cluster Security Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.revoke_cluster_security_group_ingress(
        ClusterSecurityGroupName='string',
        CIDRIP='string',
        EC2SecurityGroupName='string',
        EC2SecurityGroupOwnerId='string'
    )
    
    
    :type ClusterSecurityGroupName: string
    :param ClusterSecurityGroupName: [REQUIRED]
            The name of the security Group from which to revoke the ingress rule.
            

    :type CIDRIP: string
    :param CIDRIP: The IP range for which to revoke access. This range must be a valid Classless Inter-Domain Routing (CIDR) block of IP addresses. If CIDRIP is specified, EC2SecurityGroupName and EC2SecurityGroupOwnerId cannot be provided.

    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: The name of the EC2 Security Group whose access is to be revoked. If EC2SecurityGroupName is specified, EC2SecurityGroupOwnerId must also be provided and CIDRIP cannot be provided.

    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: The AWS account number of the owner of the security group specified in the EC2SecurityGroupName parameter. The AWS access key ID is not an acceptable value. If EC2SecurityGroupOwnerId is specified, EC2SecurityGroupName must also be provided. and CIDRIP cannot be provided.
            Example: 111122223333
            

    :rtype: dict
    :return: {
        'ClusterSecurityGroup': {
            'ClusterSecurityGroupName': 'string',
            'Description': 'string',
            'EC2SecurityGroups': [
                {
                    'Status': 'string',
                    'EC2SecurityGroupName': 'string',
                    'EC2SecurityGroupOwnerId': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'IPRanges': [
                {
                    'Status': 'string',
                    'CIDRIP': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def revoke_snapshot_access(SnapshotIdentifier=None, SnapshotClusterIdentifier=None, AccountWithRestoreAccess=None):
    """
    Removes the ability of the specified AWS customer account to restore the specified snapshot. If the account is currently restoring the snapshot, the restore will run to completion.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.revoke_snapshot_access(
        SnapshotIdentifier='string',
        SnapshotClusterIdentifier='string',
        AccountWithRestoreAccess='string'
    )
    
    
    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            The identifier of the snapshot that the account can no longer access.
            

    :type SnapshotClusterIdentifier: string
    :param SnapshotClusterIdentifier: The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

    :type AccountWithRestoreAccess: string
    :param AccountWithRestoreAccess: [REQUIRED]
            The identifier of the AWS customer account that can no longer restore the specified snapshot.
            

    :rtype: dict
    :return: {
        'Snapshot': {
            'SnapshotIdentifier': 'string',
            'ClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Status': 'string',
            'Port': 123,
            'AvailabilityZone': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'ClusterVersion': 'string',
            'SnapshotType': 'string',
            'NodeType': 'string',
            'NumberOfNodes': 123,
            'DBName': 'string',
            'VpcId': 'string',
            'Encrypted': True|False,
            'KmsKeyId': 'string',
            'EncryptedWithHSM': True|False,
            'AccountsWithRestoreAccess': [
                {
                    'AccountId': 'string',
                    'AccountAlias': 'string'
                },
            ],
            'OwnerAccount': 'string',
            'TotalBackupSizeInMegaBytes': 123.0,
            'ActualIncrementalBackupSizeInMegaBytes': 123.0,
            'BackupProgressInMegaBytes': 123.0,
            'CurrentBackupRateInMegaBytesPerSecond': 123.0,
            'EstimatedSecondsToCompletion': 123,
            'ElapsedTimeInSeconds': 123,
            'SourceRegion': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'RestorableNodeTypes': [
                'string',
            ],
            'EnhancedVpcRouting': True|False
        }
    }
    
    
    :returns: 
    CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
    DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
    DeleteClusterSnapshot returns status as "deleted".
    
    """
    pass

def rotate_encryption_key(ClusterIdentifier=None):
    """
    Rotates the encryption keys for a cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.rotate_encryption_key(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]
            The unique identifier of the cluster that you want to rotate the encryption keys for.
            Constraints: Must be the name of valid cluster that has encryption enabled.
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
    in-sync : The parameter value is in sync with the database.
    pending-reboot : The parameter value will be applied after the cluster reboots.
    applying : The parameter value is being applied to the database.
    invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
    apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
    apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
    unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.
    
    """
    pass

