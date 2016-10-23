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


def add_role_to_db_cluster(DBClusterIdentifier=None, RoleArn=None):
    """
    :param DBClusterIdentifier: [REQUIRED]
            The name of the DB cluster to associate the IAM role with.
            
    :type DBClusterIdentifier: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role to associate with the Aurora DB cluster, for example arn:aws:iam::123456789012:role/AuroraAccessRole .
            
    :type RoleArn: string
    """
    pass


def add_source_identifier_to_subscription(SubscriptionName=None, SourceIdentifier=None):
    """
    :param SubscriptionName: [REQUIRED]
            The name of the RDS event notification subscription you want to add a source identifier to.
            
    :type SubscriptionName: string
    :param SourceIdentifier: [REQUIRED]
            The identifier of the event source to be added. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it cannot end with a hyphen or contain two consecutive hyphens.
            Constraints:
            If the source type is a DB instance, then a DBInstanceIdentifier must be supplied.
            If the source type is a DB security group, a DBSecurityGroupName must be supplied.
            If the source type is a DB parameter group, a DBParameterGroupName must be supplied.
            If the source type is a DB snapshot, a DBSnapshotIdentifier must be supplied.
            
    :type SourceIdentifier: string
    """
    pass


def add_tags_to_resource(ResourceName=None, Tags=None):
    """
    :param ResourceName: [REQUIRED]
            The Amazon RDS resource the tags will be added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see Constructing an RDS Amazon Resource Name (ARN) .
            
    :type ResourceName: string
    :param Tags: [REQUIRED]
            The tags to be assigned to the Amazon RDS resource.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def apply_pending_maintenance_action(ResourceIdentifier=None, ApplyAction=None, OptInType=None):
    """
    :param ResourceIdentifier: [REQUIRED]
            The RDS Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see Constructing an RDS Amazon Resource Name (ARN) .
            
    :type ResourceIdentifier: string
    :param ApplyAction: [REQUIRED]
            The pending maintenance action to apply to this resource.
            Valid values: system-update , db-upgrade
            
    :type ApplyAction: string
    :param OptInType: [REQUIRED]
            A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type immediate cannot be undone.
            Valid values:
            immediate - Apply the maintenance action immediately.
            next-maintenance - Apply the maintenance action during the next maintenance window for the resource.
            undo-opt-in - Cancel any existing next-maintenance opt-in requests.
            
    :type OptInType: string
    """
    pass


def authorize_db_security_group_ingress(DBSecurityGroupName=None, CIDRIP=None, EC2SecurityGroupName=None,
                                        EC2SecurityGroupId=None, EC2SecurityGroupOwnerId=None):
    """
    :param DBSecurityGroupName: [REQUIRED]
            The name of the DB security group to add authorization to.
            
    :type DBSecurityGroupName: string
    :param CIDRIP: The IP range to authorize.
    :type CIDRIP: string
    :param EC2SecurityGroupName: Name of the EC2 security group to authorize. For VPC DB security groups, EC2SecurityGroupId must be provided. Otherwise, EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId must be provided.
    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupId: Id of the EC2 security group to authorize. For VPC DB security groups, EC2SecurityGroupId must be provided. Otherwise, EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId must be provided.
    :type EC2SecurityGroupId: string
    :param EC2SecurityGroupOwnerId: AWS account number of the owner of the EC2 security group specified in the EC2SecurityGroupName parameter. The AWS Access Key ID is not an acceptable value. For VPC DB security groups, EC2SecurityGroupId must be provided. Otherwise, EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId must be provided.
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


def copy_db_cluster_parameter_group(SourceDBClusterParameterGroupIdentifier=None,
                                    TargetDBClusterParameterGroupIdentifier=None,
                                    TargetDBClusterParameterGroupDescription=None, Tags=None):
    """
    :param SourceDBClusterParameterGroupIdentifier: [REQUIRED]
            The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see Constructing an RDS Amazon Resource Name (ARN) .
            Constraints:
            Must specify a valid DB cluster parameter group.
            If the source DB cluster parameter group is in the same region as the copy, specify a valid DB parameter group identifier, for example my-db-cluster-param-group , or a valid ARN.
            If the source DB parameter group is in a different region than the copy, specify a valid DB cluster parameter group ARN, for example arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1 .
            
    :type SourceDBClusterParameterGroupIdentifier: string
    :param TargetDBClusterParameterGroupIdentifier: [REQUIRED]
            The identifier for the copied DB cluster parameter group.
            Constraints:
            Cannot be null, empty, or blank
            Must contain from 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-cluster-param-group1
            
    :type TargetDBClusterParameterGroupIdentifier: string
    :param TargetDBClusterParameterGroupDescription: [REQUIRED]
            A description for the copied DB cluster parameter group.
            
    :type TargetDBClusterParameterGroupDescription: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def copy_db_cluster_snapshot(SourceDBClusterSnapshotIdentifier=None, TargetDBClusterSnapshotIdentifier=None, Tags=None):
    """
    :param SourceDBClusterSnapshotIdentifier: [REQUIRED]
            The identifier of the DB cluster snapshot to copy. This parameter is not case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster-snapshot1
            
    :type SourceDBClusterSnapshotIdentifier: string
    :param TargetDBClusterSnapshotIdentifier: [REQUIRED]
            The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster-snapshot2
            
    :type TargetDBClusterSnapshotIdentifier: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def copy_db_parameter_group(SourceDBParameterGroupIdentifier=None, TargetDBParameterGroupIdentifier=None,
                            TargetDBParameterGroupDescription=None, Tags=None):
    """
    :param SourceDBParameterGroupIdentifier: [REQUIRED]
            The identifier or ARN for the source DB parameter group. For information about creating an ARN, see Constructing an RDS Amazon Resource Name (ARN) .
            Constraints:
            Must specify a valid DB parameter group.
            Must specify a valid DB parameter group identifier, for example my-db-param-group , or a valid ARN.
            
    :type SourceDBParameterGroupIdentifier: string
    :param TargetDBParameterGroupIdentifier: [REQUIRED]
            The identifier for the copied DB parameter group.
            Constraints:
            Cannot be null, empty, or blank
            Must contain from 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-db-parameter-group
            
    :type TargetDBParameterGroupIdentifier: string
    :param TargetDBParameterGroupDescription: [REQUIRED]
            A description for the copied DB parameter group.
            
    :type TargetDBParameterGroupDescription: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def copy_db_snapshot(SourceDBSnapshotIdentifier=None, TargetDBSnapshotIdentifier=None, KmsKeyId=None, Tags=None,
                     CopyTags=None):
    """
    :param SourceDBSnapshotIdentifier: [REQUIRED]
            The identifier for the source DB snapshot.
            If you are copying from a shared manual DB snapshot, this must be the ARN of the shared DB snapshot.
            Constraints:
            Must specify a valid system snapshot in the 'available' state.
            If the source snapshot is in the same region as the copy, specify a valid DB snapshot identifier.
            If the source snapshot is in a different region than the copy, specify a valid DB snapshot ARN. For more information, go to Copying a DB Snapshot .
            Example: rds:mydb-2012-04-02-00-01
            Example: arn:aws:rds:rr-regn-1:123456789012:snapshot:mysql-instance1-snapshot-20130805
            
    :type SourceDBSnapshotIdentifier: string
    :param TargetDBSnapshotIdentifier: [REQUIRED]
            The identifier for the copied snapshot.
            Constraints:
            Cannot be null, empty, or blank
            Must contain from 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-db-snapshot
            
    :type TargetDBSnapshotIdentifier: string
    :param KmsKeyId: The AWS Key Management Service (AWS KMS) key identifier for an encrypted DB snapshot. The KMS key identifier is the Amazon Resource Name (ARN) or the KMS key alias for the KMS encryption key.
            If you copy an unencrypted DB snapshot and specify a value for the KmsKeyId parameter, Amazon RDS encrypts the target DB snapshot using the specified KMS encryption key.
            If you copy an encrypted DB snapshot from your AWS account, you can specify a value for KmsKeyId to encrypt the copy with a new KMS encryption key. If you don't specify a value for KmsKeyId then the copy of the DB snapshot is encrypted with the same KMS key as the source DB snapshot.
            If you copy an encrypted DB snapshot that is shared from another AWS account, then you must specify a value for KmsKeyId .
            
    :type KmsKeyId: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param CopyTags: True to copy all tags from the source DB snapshot to the target DB snapshot; otherwise false. The default is false.
    :type CopyTags: boolean
    """
    pass


def copy_option_group(SourceOptionGroupIdentifier=None, TargetOptionGroupIdentifier=None,
                      TargetOptionGroupDescription=None, Tags=None):
    """
    :param SourceOptionGroupIdentifier: [REQUIRED]
            The identifier or ARN for the source option group. For information about creating an ARN, see Constructing an RDS Amazon Resource Name (ARN) .
            Constraints:
            Must specify a valid option group.
            If the source option group is in the same region as the copy, specify a valid option group identifier, for example my-option-group , or a valid ARN.
            If the source option group is in a different region than the copy, specify a valid option group ARN, for example arn:aws:rds:us-west-2:123456789012:og:special-options .
            
    :type SourceOptionGroupIdentifier: string
    :param TargetOptionGroupIdentifier: [REQUIRED]
            The identifier for the copied option group.
            Constraints:
            Cannot be null, empty, or blank
            Must contain from 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-option-group
            
    :type TargetOptionGroupIdentifier: string
    :param TargetOptionGroupDescription: [REQUIRED]
            The description for the copied option group.
            
    :type TargetOptionGroupDescription: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def create_db_cluster(AvailabilityZones=None, BackupRetentionPeriod=None, CharacterSetName=None, DatabaseName=None,
                      DBClusterIdentifier=None, DBClusterParameterGroupName=None, VpcSecurityGroupIds=None,
                      DBSubnetGroupName=None, Engine=None, EngineVersion=None, Port=None, MasterUsername=None,
                      MasterUserPassword=None, OptionGroupName=None, PreferredBackupWindow=None,
                      PreferredMaintenanceWindow=None, ReplicationSourceIdentifier=None, Tags=None,
                      StorageEncrypted=None, KmsKeyId=None):
    """
    :param AvailabilityZones: A list of EC2 Availability Zones that instances in the DB cluster can be created in. For information on regions and Availability Zones, see Regions and Availability Zones .
            (string) --
            
    :type AvailabilityZones: list
    :param BackupRetentionPeriod: The number of days for which automated backups are retained. You must specify a minimum value of 1.
            Default: 1
            Constraints:
            Must be a value from 1 to 35
            
    :type BackupRetentionPeriod: integer
    :param CharacterSetName: A value that indicates that the DB cluster should be associated with the specified CharacterSet.
    :type CharacterSetName: string
    :param DatabaseName: The name for your database of up to 8 alpha-numeric characters. If you do not provide a name, Amazon RDS will not create a database in the DB cluster you are creating.
    :type DatabaseName: string
    :param DBClusterIdentifier: [REQUIRED]
            The DB cluster identifier. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster1
            
    :type DBClusterIdentifier: string
    :param DBClusterParameterGroupName: The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted, default.aurora5.6 will be used.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBClusterParameterGroupName: string
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to associate with this DB cluster.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param DBSubnetGroupName: A DB subnet group to associate with this DB cluster.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            
    :type DBSubnetGroupName: string
    :param Engine: [REQUIRED]
            The name of the database engine to be used for this DB cluster.
            Valid Values: aurora
            
    :type Engine: string
    :param EngineVersion: The version number of the database engine to use.
            Aurora
            Example: 5.6.10a
            
    :type EngineVersion: string
    :param Port: The port number on which the instances in the DB cluster accept connections.
            Default: 3306
            
    :type Port: integer
    :param MasterUsername: The name of the master user for the DB cluster.
            Constraints:
            Must be 1 to 16 alphanumeric characters.
            First character must be a letter.
            Cannot be a reserved word for the chosen database engine.
            
    :type MasterUsername: string
    :param MasterUserPassword: The password for the master database user. This password can contain any printable ASCII character except '/', ''', or '@'.
            Constraints: Must contain from 8 to 41 characters.
            
    :type MasterUserPassword: string
    :param OptionGroupName: A value that indicates that the DB cluster should be associated with the specified option group.
            Permanent options cannot be removed from an option group. The option group cannot be removed from a DB cluster once it is associated with a DB cluster.
            
    :type OptionGroupName: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.
            Default: A 30-minute window selected at random from an 8-hour block of time per region. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon RDS User Guide.
            Constraints:
            Must be in the format hh24:mi-hh24:mi .
            Times should be in Universal Coordinated Time (UTC).
            Must not conflict with the preferred maintenance window.
            Must be at least 30 minutes.
            
    :type PreferredBackupWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon RDS User Guide.
            Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
            Constraints: Minimum 30-minute window.
            
    :type PreferredMaintenanceWindow: string
    :param ReplicationSourceIdentifier: The Amazon Resource Name (ARN) of the source DB cluster if this DB cluster is created as a Read Replica.
    :type ReplicationSourceIdentifier: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param StorageEncrypted: Specifies whether the DB cluster is encrypted.
    :type StorageEncrypted: boolean
    :param KmsKeyId: The KMS key identifier for an encrypted DB cluster.
            The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KM encryption key.
            If the StorageEncrypted parameter is true, and you do not specify a value for the KmsKeyId parameter, then Amazon RDS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
            
    :type KmsKeyId: string
    """
    pass


def create_db_cluster_parameter_group(DBClusterParameterGroupName=None, DBParameterGroupFamily=None, Description=None,
                                      Tags=None):
    """
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of the DB cluster parameter group.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Note
            This value is stored as a lowercase string.
            
    :type DBClusterParameterGroupName: string
    :param DBParameterGroupFamily: [REQUIRED]
            The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.
            
    :type DBParameterGroupFamily: string
    :param Description: [REQUIRED]
            The description for the DB cluster parameter group.
            
    :type Description: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def create_db_cluster_snapshot(DBClusterSnapshotIdentifier=None, DBClusterIdentifier=None, Tags=None):
    """
    :param DBClusterSnapshotIdentifier: [REQUIRED]
            The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster1-snapshot1
            
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]
            The identifier of the DB cluster to create a snapshot for. This parameter is not case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster1
            
    :type DBClusterIdentifier: string
    :param Tags: The tags to be assigned to the DB cluster snapshot.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def create_db_instance(DBName=None, DBInstanceIdentifier=None, AllocatedStorage=None, DBInstanceClass=None, Engine=None,
                       MasterUsername=None, MasterUserPassword=None, DBSecurityGroups=None, VpcSecurityGroupIds=None,
                       AvailabilityZone=None, DBSubnetGroupName=None, PreferredMaintenanceWindow=None,
                       DBParameterGroupName=None, BackupRetentionPeriod=None, PreferredBackupWindow=None, Port=None,
                       MultiAZ=None, EngineVersion=None, AutoMinorVersionUpgrade=None, LicenseModel=None, Iops=None,
                       OptionGroupName=None, CharacterSetName=None, PubliclyAccessible=None, Tags=None,
                       DBClusterIdentifier=None, StorageType=None, TdeCredentialArn=None, TdeCredentialPassword=None,
                       StorageEncrypted=None, KmsKeyId=None, Domain=None, CopyTagsToSnapshot=None,
                       MonitoringInterval=None, MonitoringRoleArn=None, DomainIAMRoleName=None, PromotionTier=None,
                       Timezone=None):
    """
    :param DBName: The meaning of this parameter differs according to the database engine you use.
            Type: String
            MySQL
            The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance.
            Constraints:
            Must contain 1 to 64 alphanumeric characters
            Cannot be a word reserved by the specified database engine
            MariaDB
            The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance.
            Constraints:
            Must contain 1 to 64 alphanumeric characters
            Cannot be a word reserved by the specified database engine
            PostgreSQL
            The name of the database to create when the DB instance is created. If this parameter is not specified, the default 'postgres' database is created in the DB instance.
            Constraints:
            Must contain 1 to 63 alphanumeric characters
            Must begin with a letter or an underscore. Subsequent characters can be letters, underscores, or digits (0-9).
            Cannot be a word reserved by the specified database engine
            Oracle
            The Oracle System ID (SID) of the created DB instance.
            Default: ORCL
            Constraints:
            Cannot be longer than 8 characters
            SQL Server
            Not applicable. Must be null.
            Amazon Aurora
            The name of the database to create when the primary instance of the DB cluster is created. If this parameter is not specified, no database is created in the DB instance.
            Constraints:
            Must contain 1 to 64 alphanumeric characters
            Cannot be a word reserved by the specified database engine
            
    :type DBName: string
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens (1 to 15 for SQL Server).
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: mydbinstance
            
    :type DBInstanceIdentifier: string
    :param AllocatedStorage: The amount of storage (in gigabytes) to be initially allocated for the database instance.
            Type: Integer
            MySQL
            Constraints: Must be an integer from 5 to 6144.
            MariaDB
            Constraints: Must be an integer from 5 to 6144.
            PostgreSQL
            Constraints: Must be an integer from 5 to 6144.
            Oracle
            Constraints: Must be an integer from 10 to 6144.
            SQL Server
            Constraints: Must be an integer from 200 to 4096 (Standard Edition and Enterprise Edition) or from 20 to 4096 (Express Edition and Web Edition)
            
    :type AllocatedStorage: integer
    :param DBInstanceClass: [REQUIRED]
            The compute and memory capacity of the DB instance.
            Valid Values: db.t1.micro | db.m1.small | db.m1.medium | db.m1.large | db.m1.xlarge | db.m2.xlarge |db.m2.2xlarge | db.m2.4xlarge | db.m3.medium | db.m3.large | db.m3.xlarge | db.m3.2xlarge | db.m4.large | db.m4.xlarge | db.m4.2xlarge | db.m4.4xlarge | db.m4.10xlarge | db.r3.large | db.r3.xlarge | db.r3.2xlarge | db.r3.4xlarge | db.r3.8xlarge | db.t2.micro | db.t2.small | db.t2.medium | db.t2.large
            
    :type DBInstanceClass: string
    :param Engine: [REQUIRED]
            The name of the database engine to be used for this instance.
            Valid Values: mysql | mariadb | oracle-se1 | oracle-se2 | oracle-se | oracle-ee | sqlserver-ee | sqlserver-se | sqlserver-ex | sqlserver-web | postgres | aurora
            Not every database engine is available for every AWS region.
            
    :type Engine: string
    :param MasterUsername: The name of master user for the client DB instance.
            MySQL
            Constraints:
            Must be 1 to 16 alphanumeric characters.
            First character must be a letter.
            Cannot be a reserved word for the chosen database engine.
            MariaDB
            Constraints:
            Must be 1 to 16 alphanumeric characters.
            Cannot be a reserved word for the chosen database engine.
            Type: String
            Oracle
            Constraints:
            Must be 1 to 30 alphanumeric characters.
            First character must be a letter.
            Cannot be a reserved word for the chosen database engine.
            SQL Server
            Constraints:
            Must be 1 to 128 alphanumeric characters.
            First character must be a letter.
            Cannot be a reserved word for the chosen database engine.
            PostgreSQL
            Constraints:
            Must be 1 to 63 alphanumeric characters.
            First character must be a letter.
            Cannot be a reserved word for the chosen database engine.
            
    :type MasterUsername: string
    :param MasterUserPassword: The password for the master database user. Can be any printable ASCII character except '/', ''', or '@'.
            Type: String
            MySQL
            Constraints: Must contain from 8 to 41 characters.
            MariaDB
            Constraints: Must contain from 8 to 41 characters.
            Oracle
            Constraints: Must contain from 8 to 30 characters.
            SQL Server
            Constraints: Must contain from 8 to 128 characters.
            PostgreSQL
            Constraints: Must contain from 8 to 128 characters.
            Amazon Aurora
            Constraints: Must contain from 8 to 41 characters.
            
    :type MasterUserPassword: string
    :param DBSecurityGroups: A list of DB security groups to associate with this DB instance.
            Default: The default DB security group for the database engine.
            (string) --
            
    :type DBSecurityGroups: list
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to associate with this DB instance.
            Default: The default EC2 VPC security group for the DB subnet group's VPC.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param AvailabilityZone: The EC2 Availability Zone that the database instance will be created in. For information on regions and Availability Zones, see Regions and Availability Zones .
            Default: A random, system-chosen Availability Zone in the endpoint's region.
            Example: us-east-1d
            Constraint: The AvailabilityZone parameter cannot be specified if the MultiAZ parameter is set to true . The specified Availability Zone must be in the same region as the current endpoint.
            
    :type AvailabilityZone: string
    :param DBSubnetGroupName: A DB subnet group to associate with this DB instance.
            If there is no DB subnet group, then it is a non-VPC DB instance.
            
    :type DBSubnetGroupName: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). For more information, see DB Instance Maintenance .
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon RDS User Guide.
            Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
            Constraints: Minimum 30-minute window.
            
    :type PreferredMaintenanceWindow: string
    :param DBParameterGroupName: The name of the DB parameter group to associate with this DB instance. If this argument is omitted, the default DBParameterGroup for the specified engine will be used.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBParameterGroupName: string
    :param BackupRetentionPeriod: The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
            Default: 1
            Constraints:
            Must be a value from 0 to 35
            Cannot be set to 0 if the DB instance is a source to Read Replicas
            
    :type BackupRetentionPeriod: integer
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter. For more information, see DB Instance Backups .
            Default: A 30-minute window selected at random from an 8-hour block of time per region. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon RDS User Guide.
            Constraints:
            Must be in the format hh24:mi-hh24:mi .
            Times should be in Universal Coordinated Time (UTC).
            Must not conflict with the preferred maintenance window.
            Must be at least 30 minutes.
            
    :type PreferredBackupWindow: string
    :param Port: The port number on which the database accepts connections.
            MySQL
            Default: 3306
            Valid Values: 1150-65535
            Type: Integer
            MariaDB
            Default: 3306
            Valid Values: 1150-65535
            Type: Integer
            PostgreSQL
            Default: 5432
            Valid Values: 1150-65535
            Type: Integer
            Oracle
            Default: 1521
            Valid Values: 1150-65535
            SQL Server
            Default: 1433
            Valid Values: 1150-65535 except for 1434 , 3389 , 47001 , 49152 , and 49152 through 49156 .
            Amazon Aurora
            Default: 3306
            Valid Values: 1150-65535
            Type: Integer
            
    :type Port: integer
    :param MultiAZ: Specifies if the DB instance is a Multi-AZ deployment. You cannot set the AvailabilityZone parameter if the MultiAZ parameter is set to true.
    :type MultiAZ: boolean
    :param EngineVersion: The version number of the database engine to use.
            The following are the database engines and major and minor versions that are available with Amazon RDS. Not every database engine is available for every AWS region.
            Amazon Aurora
            Version 5.6 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-south-1, ap-southeast-2, eu-west-1, us-east-1, us-west-2): 5.6.10a
            MariaDB
            Version 10.1 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-south-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 10.1.14
            Version 10.0 (available in all AWS regions): 10.0.17 | 10.0.24
            MySQL
            Version 5.7 (available in all AWS regions): 5.7.10 | 5.7.11
            Version 5.6 (available in all AWS regions): 5.6.27 | 5.6.29
            Version 5.6 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 5.6.23
            Version 5.6 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 5.6.19a | 5.6.19b | 5.6.21 | 5.6.21b | 5.6.22
            Version 5.5 (available in all AWS regions): 5.5.46
            Version 5.5 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 5.5.42
            Version 5.5 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 5.5.40b | 5.5.41
            Version 5.5 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 5.5.40 | 5.5.40a
            Oracle Database Enterprise Edition (oracle-ee)
            Version 12.1.0.2 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-south-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 12.1.0.2.v5
            Version 12.1.0.2 (available in all AWS regions): 12.1.0.2.v1 | 12.1.0.2.v2 | 12.1.0.2.v3 | 12.1.0.2.v4
            Version 12.1.0.1 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 12.1.0.1.v6
            Version 12.1.0.1 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 12.1.0.1.v3 | 12.1.0.1.v4 | 12.1.0.1.v5
            Version 12.1.0.1 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-gov-west-1, us-west-1, us-west-2): 12.1.0.1.v1 | 12.1.0.1.v2
            Version 11.2.0.4 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-south-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 11.2.0.4.v6 | 11.2.0.4.v9
            Version 11.2.0.4 (available in all AWS regions): 11.2.0.4.v1 | 11.2.0.4.v3 | 11.2.0.4.v4 | 11.2.0.4.v5 | 11.2.0.4.v7 | 11.2.0.4.v8
            Oracle Database Standard Edition Two (oracle-se2)
            Version 12.1.0.2 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-south-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 12.1.0.2.v5
            Version 12.1.0.2 (available in all AWS regions): 12.1.0.2.v2 | 12.1.0.2.v3 | 12.1.0.2.v4
            Oracle Database Standard Edition One (oracle-se1)
            Version 12.1.0.1 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 12.1.0.1.v6
            Version 12.1.0.1 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 12.1.0.1.v3 | 12.1.0.1.v4 | 12.1.0.1.v5
            Version 12.1.0.1 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-gov-west-1, us-west-1, us-west-2): 12.1.0.1.v1 | 12.1.0.1.v2
            Version 11.2.0.4 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-south-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 11.2.0.4.v6 | 11.2.0.4.v9
            Version 11.2.0.4 (available in all AWS regions): 11.2.0.4.v1 | 11.2.0.4.v3 | 11.2.0.4.v4 | 11.2.0.4.v5 | 11.2.0.4.v7 | 11.2.0.4.v8
            Oracle Database Standard Edition (oracle-se)
            Version 12.1.0.1 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 12.1.0.1.v6
            Version 12.1.0.1 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 12.1.0.1.v3 | 12.1.0.1.v4 | 12.1.0.1.v5
            Version 12.1.0.1 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-gov-west-1, us-west-1, us-west-2): 12.1.0.1.v1 | 12.1.0.1.v2
            Version 11.2.0.4 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-south-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 11.2.0.4.v6 | 11.2.0.4.v9
            Version 11.2.0.4 (available in all AWS regions): 11.2.0.4.v1 | 11.2.0.4.v3 | 11.2.0.4.v4 | 11.2.0.4.v5 | 11.2.0.4.v7 | 11.2.0.4.v8
            PostgreSQL
            Version 9.5 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-south-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 9.5.2 | 9.5.4
            Version 9.4 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-south-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 9.4.7 | 9.4.9
            Version 9.4 (available in all AWS regions): 9.4.5
            Version 9.4 (available in these AWS regions: ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 9.4.1 | 9.4.4
            Version 9.3 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 9.3.10 | 9.3.3 | 9.3.5 | 9.3.6 | 9.3.9
            Version 9.3 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-west-1, sa-east-1, us-east-1, us-gov-west-1, us-west-1, us-west-2): 9.3.1 | 9.3.2
            Version 9.3 (available in these AWS regions: ap-northeast-1, ap-southeast-1, ap-southeast-2, eu-central-1, eu-west-1, sa-east-1, us-east-1, us-west-1, us-west-2): 9.3.12 | 9.3.14
            Microsoft SQL Server Enterprise Edition (sqlserver-ee)
            Version 11.00 (available in all AWS regions): 11.00.2100.60.v1 | 11.00.5058.0.v1 | 11.00.6020.0.v1
            Version 10.50 (available in all AWS regions): 10.50.2789.0.v1 | 10.50.6000.34.v1 | 10.50.6529.0.v1
            Microsoft SQL Server Express Edition (sqlserver-ex)
            Version 12.00 (available in all AWS regions): 12.00.4422.0.v1
            Version 11.00 (available in all AWS regions): 11.00.2100.60.v1 | 11.00.5058.0.v1 | 11.00.6020.0.v1
            Version 10.50 (available in all AWS regions): 10.50.2789.0.v1 | 10.50.6000.34.v1 | 10.50.6529.0.v1
            Microsoft SQL Server Standard Edition (sqlserver-se)
            Version 12.00 (available in all AWS regions): 12.00.4422.0.v1
            Version 11.00 (available in all AWS regions): 11.00.2100.60.v1 | 11.00.5058.0.v1 | 11.00.6020.0.v1
            Version 10.50 (available in all AWS regions): 10.50.2789.0.v1 | 10.50.6000.34.v1 | 10.50.6529.0.v1
            Microsoft SQL Server Web Edition (sqlserver-web)
            Version 12.00 (available in all AWS regions): 12.00.4422.0.v1
            Version 11.00 (available in all AWS regions): 11.00.2100.60.v1 | 11.00.5058.0.v1 | 11.00.6020.0.v1
            Version 10.50 (available in all AWS regions): 10.50.2789.0.v1 | 10.50.6000.34.v1 | 10.50.6529.0.v1
            
    :type EngineVersion: string
    :param AutoMinorVersionUpgrade: Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window.
            Default: true
            
    :type AutoMinorVersionUpgrade: boolean
    :param LicenseModel: License model information for this DB instance.
            Valid values: license-included | bring-your-own-license | general-public-license
            
    :type LicenseModel: string
    :param Iops: The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.
            Constraints: Must be a multiple between 3 and 10 of the storage amount for the DB instance. Must also be an integer multiple of 1000. For example, if the size of your DB instance is 500 GB, then your Iops value can be 2000, 3000, 4000, or 5000.
            
    :type Iops: integer
    :param OptionGroupName: Indicates that the DB instance should be associated with the specified option group.
            Permanent options, such as the TDE option for Oracle Advanced Security TDE, cannot be removed from an option group, and that option group cannot be removed from a DB instance once it is associated with a DB instance
            
    :type OptionGroupName: string
    :param CharacterSetName: For supported engines, indicates that the DB instance should be associated with the specified CharacterSet.
    :type CharacterSetName: string
    :param PubliclyAccessible: Specifies the accessibility options for the DB instance. A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address. A value of false specifies an internal instance with a DNS name that resolves to a private IP address.
            Default: The default behavior varies depending on whether a VPC has been requested or not. The following list shows the default behavior in each case.
            Default VPC: true
            VPC: false
            If no DB subnet group has been specified as part of the request and the PubliclyAccessible value has not been set, the DB instance will be publicly accessible. If a specific DB subnet group has been specified as part of the request and the PubliclyAccessible value has not been set, the DB instance will be private.
            
    :type PubliclyAccessible: boolean
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param DBClusterIdentifier: The identifier of the DB cluster that the instance will belong to.
            For information on creating a DB cluster, see CreateDBCluster .
            Type: String
            
    :type DBClusterIdentifier: string
    :param StorageType: Specifies the storage type to be associated with the DB instance.
            Valid values: standard | gp2 | io1
            If you specify io1 , you must also include a value for the Iops parameter.
            Default: io1 if the Iops parameter is specified; otherwise standard
            
    :type StorageType: string
    :param TdeCredentialArn: The ARN from the Key Store with which to associate the instance for TDE encryption.
    :type TdeCredentialArn: string
    :param TdeCredentialPassword: The password for the given ARN from the Key Store in order to access the device.
    :type TdeCredentialPassword: string
    :param StorageEncrypted: Specifies whether the DB instance is encrypted.
            Default: false
            
    :type StorageEncrypted: boolean
    :param KmsKeyId: The KMS key identifier for an encrypted DB instance.
            The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB instance with the same AWS account that owns the KMS encryption key used to encrypt the new DB instance, then you can use the KMS key alias instead of the ARN for the KM encryption key.
            If the StorageEncrypted parameter is true, and you do not specify a value for the KmsKeyId parameter, then Amazon RDS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
            
    :type KmsKeyId: string
    :param Domain: Specify the Active Directory Domain to create the instance in.
    :type Domain: string
    :param CopyTagsToSnapshot: True to copy all tags from the DB instance to snapshots of the DB instance; otherwise false. The default is false.
    :type CopyTagsToSnapshot: boolean
    :param MonitoringInterval: The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
            If MonitoringRoleArn is specified, then you must also set MonitoringInterval to a value other than 0.
            Valid Values: 0, 1, 5, 10, 15, 30, 60
            
    :type MonitoringInterval: integer
    :param MonitoringRoleArn: The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to CloudWatch Logs. For example, arn:aws:iam:123456789012:role/emaccess . For information on creating a monitoring role, go to To create an IAM role for Amazon RDS Enhanced Monitoring .
            If MonitoringInterval is set to a value other than 0, then you must supply a MonitoringRoleArn value.
            
    :type MonitoringRoleArn: string
    :param DomainIAMRoleName: Specify the name of the IAM role to be used when making API calls to the Directory Service.
    :type DomainIAMRoleName: string
    :param PromotionTier: A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see Fault Tolerance for an Aurora DB Cluster .
            Default: 1
            Valid Values: 0 - 15
            
    :type PromotionTier: integer
    :param Timezone: The time zone of the DB instance. The time zone parameter is currently supported only by Microsoft SQL Server .
    :type Timezone: string
    """
    pass


def create_db_instance_read_replica(DBInstanceIdentifier=None, SourceDBInstanceIdentifier=None, DBInstanceClass=None,
                                    AvailabilityZone=None, Port=None, AutoMinorVersionUpgrade=None, Iops=None,
                                    OptionGroupName=None, PubliclyAccessible=None, Tags=None, DBSubnetGroupName=None,
                                    StorageType=None, CopyTagsToSnapshot=None, MonitoringInterval=None,
                                    MonitoringRoleArn=None):
    """
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier of the Read Replica. This identifier is the unique key that identifies a DB instance. This parameter is stored as a lowercase string.
            
    :type DBInstanceIdentifier: string
    :param SourceDBInstanceIdentifier: [REQUIRED]
            The identifier of the DB instance that will act as the source for the Read Replica. Each DB instance can have up to five Read Replicas.
            Constraints:
            Must be the identifier of an existing MySQL, MariaDB, or PostgreSQL DB instance.
            Can specify a DB instance that is a MySQL Read Replica only if the source is running MySQL 5.6.
            Can specify a DB instance that is a PostgreSQL Read Replica only if the source is running PostgreSQL 9.3.5.
            The specified DB instance must have automatic backups enabled, its backup retention period must be greater than 0.
            If the source DB instance is in the same region as the Read Replica, specify a valid DB instance identifier.
            If the source DB instance is in a different region than the Read Replica, specify a valid DB instance ARN. For more information, go to Constructing a Amazon RDS Amazon Resource Name (ARN) .
            
    :type SourceDBInstanceIdentifier: string
    :param DBInstanceClass: The compute and memory capacity of the Read Replica.
            Valid Values: db.m1.small | db.m1.medium | db.m1.large | db.m1.xlarge | db.m2.xlarge |db.m2.2xlarge | db.m2.4xlarge | db.m3.medium | db.m3.large | db.m3.xlarge | db.m3.2xlarge | db.m4.large | db.m4.xlarge | db.m4.2xlarge | db.m4.4xlarge | db.m4.10xlarge | db.r3.large | db.r3.xlarge | db.r3.2xlarge | db.r3.4xlarge | db.r3.8xlarge | db.t2.micro | db.t2.small | db.t2.medium | db.t2.large
            Default: Inherits from the source DB instance.
            
    :type DBInstanceClass: string
    :param AvailabilityZone: The Amazon EC2 Availability Zone that the Read Replica will be created in.
            Default: A random, system-chosen Availability Zone in the endpoint's region.
            Example: us-east-1d
            
    :type AvailabilityZone: string
    :param Port: The port number that the DB instance uses for connections.
            Default: Inherits from the source DB instance
            Valid Values: 1150-65535
            
    :type Port: integer
    :param AutoMinorVersionUpgrade: Indicates that minor engine upgrades will be applied automatically to the Read Replica during the maintenance window.
            Default: Inherits from the source DB instance
            
    :type AutoMinorVersionUpgrade: boolean
    :param Iops: The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.
    :type Iops: integer
    :param OptionGroupName: The option group the DB instance will be associated with. If omitted, the default option group for the engine specified will be used.
    :type OptionGroupName: string
    :param PubliclyAccessible: Specifies the accessibility options for the DB instance. A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address. A value of false specifies an internal instance with a DNS name that resolves to a private IP address.
            Default: The default behavior varies depending on whether a VPC has been requested or not. The following list shows the default behavior in each case.
            Default VPC: true
            VPC: false
            If no DB subnet group has been specified as part of the request and the PubliclyAccessible value has not been set, the DB instance will be publicly accessible. If a specific DB subnet group has been specified as part of the request and the PubliclyAccessible value has not been set, the DB instance will be private.
            
    :type PubliclyAccessible: boolean
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param DBSubnetGroupName: Specifies a DB subnet group for the DB instance. The new DB instance will be created in the VPC associated with the DB subnet group. If no DB subnet group is specified, then the new DB instance is not created in a VPC.
            Constraints:
            Can only be specified if the source DB instance identifier specifies a DB instance in another region.
            The specified DB subnet group must be in the same region in which the operation is running.
            All Read Replicas in one region that are created from the same source DB instance must either:
            Specify DB subnet groups from the same VPC. All these Read Replicas will be created in the same VPC.
            Not specify a DB subnet group. All these Read Replicas will be created outside of any VPC.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            
    :type DBSubnetGroupName: string
    :param StorageType: Specifies the storage type to be associated with the Read Replica.
            Valid values: standard | gp2 | io1
            If you specify io1 , you must also include a value for the Iops parameter.
            Default: io1 if the Iops parameter is specified; otherwise standard
            
    :type StorageType: string
    :param CopyTagsToSnapshot: True to copy all tags from the Read Replica to snapshots of the Read Replica; otherwise false. The default is false.
    :type CopyTagsToSnapshot: boolean
    :param MonitoringInterval: The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the Read Replica. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
            If MonitoringRoleArn is specified, then you must also set MonitoringInterval to a value other than 0.
            Valid Values: 0, 1, 5, 10, 15, 30, 60
            
    :type MonitoringInterval: integer
    :param MonitoringRoleArn: The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to CloudWatch Logs. For example, arn:aws:iam:123456789012:role/emaccess . For information on creating a monitoring role, go to To create an IAM role for Amazon RDS Enhanced Monitoring .
            If MonitoringInterval is set to a value other than 0, then you must supply a MonitoringRoleArn value.
            
    :type MonitoringRoleArn: string
    """
    pass


def create_db_parameter_group(DBParameterGroupName=None, DBParameterGroupFamily=None, Description=None, Tags=None):
    """
    :param DBParameterGroupName: [REQUIRED]
            The name of the DB parameter group.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Note
            This value is stored as a lowercase string.
            
    :type DBParameterGroupName: string
    :param DBParameterGroupFamily: [REQUIRED]
            The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.
            
    :type DBParameterGroupFamily: string
    :param Description: [REQUIRED]
            The description for the DB parameter group.
            
    :type Description: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def create_db_security_group(DBSecurityGroupName=None, DBSecurityGroupDescription=None, Tags=None):
    """
    :param DBSecurityGroupName: [REQUIRED]
            The name for the DB security group. This value is stored as a lowercase string.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Must not be 'Default'
            Example: mysecuritygroup
            
    :type DBSecurityGroupName: string
    :param DBSecurityGroupDescription: [REQUIRED]
            The description for the DB security group.
            
    :type DBSecurityGroupDescription: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def create_db_snapshot(DBSnapshotIdentifier=None, DBInstanceIdentifier=None, Tags=None):
    """
    :param DBSnapshotIdentifier: [REQUIRED]
            The identifier for the DB snapshot.
            Constraints:
            Cannot be null, empty, or blank
            Must contain from 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-snapshot-id
            
    :type DBSnapshotIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier. This is the unique key that identifies a DB instance.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBInstanceIdentifier: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def create_db_subnet_group(DBSubnetGroupName=None, DBSubnetGroupDescription=None, SubnetIds=None, Tags=None):
    """
    :param DBSubnetGroupName: [REQUIRED]
            The name for the DB subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            
    :type DBSubnetGroupName: string
    :param DBSubnetGroupDescription: [REQUIRED]
            The description for the DB subnet group.
            
    :type DBSubnetGroupDescription: string
    :param SubnetIds: [REQUIRED]
            The EC2 Subnet IDs for the DB subnet group.
            (string) --
            
    :type SubnetIds: list
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def create_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None,
                              SourceIds=None, Enabled=None, Tags=None):
    """
    :param SubscriptionName: [REQUIRED]
            The name of the subscription.
            Constraints: The name must be less than 255 characters.
            
    :type SubscriptionName: string
    :param SnsTopicArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
            
    :type SnsTopicArn: string
    :param SourceType: The type of source that will be generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.
            Valid values: db-instance | db-cluster | db-parameter-group | db-security-group | db-snapshot | db-cluster-snapshot
            
    :type SourceType: string
    :param EventCategories: A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType in the Events topic in the Amazon RDS User Guide or by using the DescribeEventCategories action.
            (string) --
            
    :type EventCategories: list
    :param SourceIds: The list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it cannot end with a hyphen or contain two consecutive hyphens.
            Constraints:
            If SourceIds are supplied, SourceType must also be provided.
            If the source type is a DB instance, then a DBInstanceIdentifier must be supplied.
            If the source type is a DB security group, a DBSecurityGroupName must be supplied.
            If the source type is a DB parameter group, a DBParameterGroupName must be supplied.
            If the source type is a DB snapshot, a DBSnapshotIdentifier must be supplied.
            (string) --
            
    :type SourceIds: list
    :param Enabled: A Boolean value; set to true to activate the subscription, set to false to create the subscription but not active it.
    :type Enabled: boolean
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def create_option_group(OptionGroupName=None, EngineName=None, MajorEngineVersion=None, OptionGroupDescription=None,
                        Tags=None):
    """
    :param OptionGroupName: [REQUIRED]
            Specifies the name of the option group to be created.
            Constraints:
            Must be 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: myoptiongroup
            
    :type OptionGroupName: string
    :param EngineName: [REQUIRED]
            Specifies the name of the engine that this option group should be associated with.
            
    :type EngineName: string
    :param MajorEngineVersion: [REQUIRED]
            Specifies the major version of the engine that this option group should be associated with.
            
    :type MajorEngineVersion: string
    :param OptionGroupDescription: [REQUIRED]
            The description of the option group.
            
    :type OptionGroupDescription: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def delete_db_cluster(DBClusterIdentifier=None, SkipFinalSnapshot=None, FinalDBSnapshotIdentifier=None):
    """
    :param DBClusterIdentifier: [REQUIRED]
            The DB cluster identifier for the DB cluster to be deleted. This parameter isn't case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBClusterIdentifier: string
    :param SkipFinalSnapshot: Determines whether a final DB cluster snapshot is created before the DB cluster is deleted. If true is specified, no DB cluster snapshot is created. If false is specified, a DB cluster snapshot is created before the DB cluster is deleted.
            Note
            You must specify a FinalDBSnapshotIdentifier parameter if SkipFinalSnapshot is false .
            Default: false
            
    :type SkipFinalSnapshot: boolean
    :param FinalDBSnapshotIdentifier: The DB cluster snapshot identifier of the new DB cluster snapshot created when SkipFinalSnapshot is set to false .
            Note
            Specifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type FinalDBSnapshotIdentifier: string
    """
    pass


def delete_db_cluster_parameter_group(DBClusterParameterGroupName=None):
    """
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of the DB cluster parameter group.
            Constraints:
            Must be the name of an existing DB cluster parameter group.
            You cannot delete a default DB cluster parameter group.
            Cannot be associated with any DB clusters.
            ReturnsNone
            
    :type DBClusterParameterGroupName: string
    """
    pass


def delete_db_cluster_snapshot(DBClusterSnapshotIdentifier=None):
    """
    :param DBClusterSnapshotIdentifier: [REQUIRED]
            The identifier of the DB cluster snapshot to delete.
            Constraints: Must be the name of an existing DB cluster snapshot in the available state.
            Return typedict
            ReturnsResponse Syntax{
              'DBClusterSnapshot': {
                'AvailabilityZones': [
                  'string',
                ],
                'DBClusterSnapshotIdentifier': 'string',
                'DBClusterIdentifier': 'string',
                'SnapshotCreateTime': datetime(2015, 1, 1),
                'Engine': 'string',
                'AllocatedStorage': 123,
                'Status': 'string',
                'Port': 123,
                'VpcId': 'string',
                'ClusterCreateTime': datetime(2015, 1, 1),
                'MasterUsername': 'string',
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'SnapshotType': 'string',
                'PercentProgress': 123,
                'StorageEncrypted': True|False,
                'KmsKeyId': 'string',
                'DBClusterSnapshotArn': 'string'
              }
            }
            Response Structure
            (dict) --
            DBClusterSnapshot (dict) --Contains the result of a successful invocation of the following actions:
            CreateDBClusterSnapshot
            DeleteDBClusterSnapshot
            This data type is used as a response element in the DescribeDBClusterSnapshots action.
            AvailabilityZones (list) --Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
            (string) --
            DBClusterSnapshotIdentifier (string) --Specifies the identifier for the DB cluster snapshot.
            DBClusterIdentifier (string) --Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.
            SnapshotCreateTime (datetime) --Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).
            Engine (string) --Specifies the name of the database engine.
            AllocatedStorage (integer) --Specifies the allocated storage size in gigabytes (GB).
            Status (string) --Specifies the status of this DB cluster snapshot.
            Port (integer) --Specifies the port that the DB cluster was listening on at the time of the snapshot.
            VpcId (string) --Provides the VPC ID associated with the DB cluster snapshot.
            ClusterCreateTime (datetime) --Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
            MasterUsername (string) --Provides the master username for the DB cluster snapshot.
            EngineVersion (string) --Provides the version of the database engine for this DB cluster snapshot.
            LicenseModel (string) --Provides the license model information for this DB cluster snapshot.
            SnapshotType (string) --Provides the type of the DB cluster snapshot.
            PercentProgress (integer) --Specifies the percentage of the estimated data that has been transferred.
            StorageEncrypted (boolean) --Specifies whether the DB cluster snapshot is encrypted.
            KmsKeyId (string) --If StorageEncrypted is true, the KMS key identifier for the encrypted DB cluster snapshot.
            DBClusterSnapshotArn (string) --The Amazon Resource Name (ARN) for the DB cluster snapshot.
            
            
            
    :type DBClusterSnapshotIdentifier: string
    """
    pass


def delete_db_instance(DBInstanceIdentifier=None, SkipFinalSnapshot=None, FinalDBSnapshotIdentifier=None):
    """
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier for the DB instance to be deleted. This parameter isn't case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBInstanceIdentifier: string
    :param SkipFinalSnapshot: Determines whether a final DB snapshot is created before the DB instance is deleted. If true is specified, no DBSnapshot is created. If false is specified, a DB snapshot is created before the DB instance is deleted.
            Note that when a DB instance is in a failure state and has a status of 'failed', 'incompatible-restore', or 'incompatible-network', it can only be deleted when the SkipFinalSnapshot parameter is set to 'true'.
            Specify true when deleting a Read Replica.
            Note
            The FinalDBSnapshotIdentifier parameter must be specified if SkipFinalSnapshot is false .
            Default: false
            
    :type SkipFinalSnapshot: boolean
    :param FinalDBSnapshotIdentifier: The DBSnapshotIdentifier of the new DBSnapshot created when SkipFinalSnapshot is set to false .
            Note
            Specifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Cannot be specified when deleting a Read Replica.
            
    :type FinalDBSnapshotIdentifier: string
    """
    pass


def delete_db_parameter_group(DBParameterGroupName=None):
    """
    :param DBParameterGroupName: [REQUIRED]
            The name of the DB parameter group.
            Constraints:
            Must be the name of an existing DB parameter group
            You cannot delete a default DB parameter group
            Cannot be associated with any DB instances
            ReturnsNone
            
    :type DBParameterGroupName: string
    """
    pass


def delete_db_security_group(DBSecurityGroupName=None):
    """
    :param DBSecurityGroupName: [REQUIRED]
            The name of the DB security group to delete.
            Note
            You cannot delete the default DB security group.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Must not be 'Default'
            ReturnsNone
            
    :type DBSecurityGroupName: string
    """
    pass


def delete_db_snapshot(DBSnapshotIdentifier=None):
    """
    :param DBSnapshotIdentifier: [REQUIRED]
            The DBSnapshot identifier.
            Constraints: Must be the name of an existing DB snapshot in the available state.
            Return typedict
            ReturnsResponse Syntax{
              'DBSnapshot': {
                'DBSnapshotIdentifier': 'string',
                'DBInstanceIdentifier': 'string',
                'SnapshotCreateTime': datetime(2015, 1, 1),
                'Engine': 'string',
                'AllocatedStorage': 123,
                'Status': 'string',
                'Port': 123,
                'AvailabilityZone': 'string',
                'VpcId': 'string',
                'InstanceCreateTime': datetime(2015, 1, 1),
                'MasterUsername': 'string',
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'SnapshotType': 'string',
                'Iops': 123,
                'OptionGroupName': 'string',
                'PercentProgress': 123,
                'SourceRegion': 'string',
                'SourceDBSnapshotIdentifier': 'string',
                'StorageType': 'string',
                'TdeCredentialArn': 'string',
                'Encrypted': True|False,
                'KmsKeyId': 'string',
                'DBSnapshotArn': 'string',
                'Timezone': 'string'
              }
            }
            Response Structure
            (dict) --
            DBSnapshot (dict) --Contains the result of a successful invocation of the following actions:
            CreateDBSnapshot
            DeleteDBSnapshot
            This data type is used as a response element in the DescribeDBSnapshots action.
            DBSnapshotIdentifier (string) --Specifies the identifier for the DB snapshot.
            DBInstanceIdentifier (string) --Specifies the DB instance identifier of the DB instance this DB snapshot was created from.
            SnapshotCreateTime (datetime) --Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).
            Engine (string) --Specifies the name of the database engine.
            AllocatedStorage (integer) --Specifies the allocated storage size in gigabytes (GB).
            Status (string) --Specifies the status of this DB snapshot.
            Port (integer) --Specifies the port that the database engine was listening on at the time of the snapshot.
            AvailabilityZone (string) --Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
            VpcId (string) --Provides the VPC ID associated with the DB snapshot.
            InstanceCreateTime (datetime) --Specifies the time when the snapshot was taken, in Universal Coordinated Time (UTC).
            MasterUsername (string) --Provides the master username for the DB snapshot.
            EngineVersion (string) --Specifies the version of the database engine.
            LicenseModel (string) --License model information for the restored DB instance.
            SnapshotType (string) --Provides the type of the DB snapshot.
            Iops (integer) --Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
            OptionGroupName (string) --Provides the option group name for the DB snapshot.
            PercentProgress (integer) --The percentage of the estimated data that has been transferred.
            SourceRegion (string) --The region that the DB snapshot was created in or copied from.
            SourceDBSnapshotIdentifier (string) --The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
            StorageType (string) --Specifies the storage type associated with DB snapshot.
            TdeCredentialArn (string) --The ARN from the key store with which to associate the instance for TDE encryption.
            Encrypted (boolean) --Specifies whether the DB snapshot is encrypted.
            KmsKeyId (string) --If Encrypted is true, the KMS key identifier for the encrypted DB snapshot.
            DBSnapshotArn (string) --The Amazon Resource Name (ARN) for the DB snapshot.
            Timezone (string) --The time zone of the DB snapshot. In most cases, the Timezone element is empty. Timezone content appears only for snapshots taken from Microsoft SQL Server DB instances that were created with a time zone specified.
            
            
            
    :type DBSnapshotIdentifier: string
    """
    pass


def delete_db_subnet_group(DBSubnetGroupName=None):
    """
    :param DBSubnetGroupName: [REQUIRED]
            The name of the database subnet group to delete.
            Note
            You cannot delete the default subnet group.
            Constraints:
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            ReturnsNone
            
    :type DBSubnetGroupName: string
    """
    pass


def delete_event_subscription(SubscriptionName=None):
    """
    :param SubscriptionName: [REQUIRED]
            The name of the RDS event notification subscription you want to delete.
            Return typedict
            ReturnsResponse Syntax{
              'EventSubscription': {
                'CustomerAwsId': 'string',
                'CustSubscriptionId': 'string',
                'SnsTopicArn': 'string',
                'Status': 'string',
                'SubscriptionCreationTime': 'string',
                'SourceType': 'string',
                'SourceIdsList': [
                  'string',
                ],
                'EventCategoriesList': [
                  'string',
                ],
                'Enabled': True|False,
                'EventSubscriptionArn': 'string'
              }
            }
            Response Structure
            (dict) --
            EventSubscription (dict) --Contains the results of a successful invocation of the DescribeEventSubscriptions action.
            CustomerAwsId (string) --The AWS customer account associated with the RDS event notification subscription.
            CustSubscriptionId (string) --The RDS event notification subscription Id.
            SnsTopicArn (string) --The topic ARN of the RDS event notification subscription.
            Status (string) --The status of the RDS event notification subscription.
            Constraints:
            Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
            The status 'no-permission' indicates that RDS no longer has permission to post to the SNS topic. The status 'topic-not-exist' indicates that the topic was deleted after the subscription was created.
            SubscriptionCreationTime (string) --The time the RDS event notification subscription was created.
            SourceType (string) --The source type for the RDS event notification subscription.
            SourceIdsList (list) --A list of source IDs for the RDS event notification subscription.
            (string) --
            EventCategoriesList (list) --A list of event categories for the RDS event notification subscription.
            (string) --
            Enabled (boolean) --A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.
            EventSubscriptionArn (string) --The Amazon Resource Name (ARN) for the event subscription.
            
            
            
    :type SubscriptionName: string
    """
    pass


def delete_option_group(OptionGroupName=None):
    """
    :param OptionGroupName: [REQUIRED]
            The name of the option group to be deleted.
            Note
            You cannot delete default option groups.
            ReturnsNone
            
    :type OptionGroupName: string
    """
    pass


def describe_account_attributes():
    """
    """
    pass


def describe_certificates(CertificateIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param CertificateIdentifier: The user-supplied certificate identifier. If this parameter is specified, information for only the identified certificate is returned. This parameter isn't case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type CertificateIdentifier: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeCertificates request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_db_cluster_parameter_groups(DBClusterParameterGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBClusterParameterGroupName: The name of a specific DB cluster parameter group to return details for.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBClusterParameterGroupName: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBClusterParameterGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_db_cluster_parameters(DBClusterParameterGroupName=None, Source=None, Filters=None, MaxRecords=None,
                                   Marker=None):
    """
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of a specific DB cluster parameter group to return parameter details for.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBClusterParameterGroupName: string
    :param Source: A value that indicates to return only parameters for a specific source. Parameter sources can be engine , service , or customer .
    :type Source: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBClusterParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_db_cluster_snapshot_attributes(DBClusterSnapshotIdentifier=None):
    """
    :param DBClusterSnapshotIdentifier: [REQUIRED]
            The identifier for the DB cluster snapshot to describe the attributes for.
            Return typedict
            ReturnsResponse Syntax{
              'DBClusterSnapshotAttributesResult': {
                'DBClusterSnapshotIdentifier': 'string',
                'DBClusterSnapshotAttributes': [
                  {
                    'AttributeName': 'string',
                    'AttributeValues': [
                      'string',
                    ]
                  },
                ]
              }
            }
            Response Structure
            (dict) --
            DBClusterSnapshotAttributesResult (dict) --Contains the results of a successful call to the DescribeDBClusterSnapshotAttributes API action.
            Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB cluster snapshot. For more information, see the ModifyDBClusterSnapshotAttribute API action.
            DBClusterSnapshotIdentifier (string) --The identifier of the manual DB cluster snapshot that the attributes apply to.
            DBClusterSnapshotAttributes (list) --The list of attributes and values for the manual DB cluster snapshot.
            (dict) --Contains the name and values of a manual DB cluster snapshot attribute.
            Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore a manual DB cluster snapshot. For more information, see the ModifyDBClusterSnapshotAttribute API action.
            AttributeName (string) --The name of the manual DB cluster snapshot attribute.
            The attribute named restore refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the ModifyDBClusterSnapshotAttribute API action.
            AttributeValues (list) --The value(s) for the manual DB cluster snapshot attribute.
            If the AttributeName field is set to restore , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of all is in the list, then the manual DB cluster snapshot is public and available for any AWS account to copy or restore.
            (string) --
            
            
            
            
    :type DBClusterSnapshotIdentifier: string
    """
    pass


def describe_db_cluster_snapshots(DBClusterIdentifier=None, DBClusterSnapshotIdentifier=None, SnapshotType=None,
                                  Filters=None, MaxRecords=None, Marker=None, IncludeShared=None, IncludePublic=None):
    """
    :param DBClusterIdentifier: The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter cannot be used in conjunction with the DBClusterSnapshotIdentifier parameter. This parameter is not case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBClusterIdentifier: string
    :param DBClusterSnapshotIdentifier: A specific DB cluster snapshot identifier to describe. This parameter cannot be used in conjunction with the DBClusterIdentifier parameter. This value is stored as a lowercase string.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            If this identifier is for an automated snapshot, the SnapshotType parameter must also be specified.
            
    :type DBClusterSnapshotIdentifier: string
    :param SnapshotType: The type of DB cluster snapshots to be returned. You can specify one of the following values:
            automated - Return all DB cluster snapshots that have been automatically taken by Amazon RDS for my AWS account.
            manual - Return all DB cluster snapshots that have been taken by my AWS account.
            shared - Return all manual DB cluster snapshots that have been shared to my AWS account.
            public - Return all DB cluster snapshots that have been marked as public.
            If you don't specify a SnapshotType value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the IncludeShared parameter to true . You can include public DB cluster snapshots with these results by setting the IncludePublic parameter to true .
            The IncludeShared and IncludePublic parameters don't apply for SnapshotType values of manual or automated . The IncludePublic parameter doesn't apply when SnapshotType is set to shared . The IncludeShared parameter doesn't apply when SnapshotType is set to public .
            
    :type SnapshotType: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBClusterSnapshots request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    :param IncludeShared: Set this value to true to include shared manual DB cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, otherwise set this value to false . The default is false .
            You can give an AWS account permission to restore a manual DB cluster snapshot from another AWS account by the ModifyDBClusterSnapshotAttribute API action.
            
    :type IncludeShared: boolean
    :param IncludePublic: Set this value to true to include manual DB cluster snapshots that are public and can be copied or restored by any AWS account, otherwise set this value to false . The default is false . The default is false.
            You can share a manual DB cluster snapshot as public by using the ModifyDBClusterSnapshotAttribute API action.
            
    :type IncludePublic: boolean
    """
    pass


def describe_db_clusters(DBClusterIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBClusterIdentifier: The user-supplied DB cluster identifier. If this parameter is specified, information from only the specific DB cluster is returned. This parameter isn't case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBClusterIdentifier: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBClusters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_db_engine_versions(Engine=None, EngineVersion=None, DBParameterGroupFamily=None, Filters=None,
                                MaxRecords=None, Marker=None, DefaultOnly=None, ListSupportedCharacterSets=None,
                                ListSupportedTimezones=None):
    """
    :param Engine: The database engine to return.
    :type Engine: string
    :param EngineVersion: The database engine version to return.
            Example: 5.1.49
            
    :type EngineVersion: string
    :param DBParameterGroupFamily: The name of a specific DB parameter group family to return details for.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBParameterGroupFamily: string
    :param Filters: Not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more than the MaxRecords value is available, a pagination token called a marker is included in the response so that the following results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    :param DefaultOnly: Indicates that only the default version of the specified engine or engine and major version combination is returned.
    :type DefaultOnly: boolean
    :param ListSupportedCharacterSets: If this parameter is specified and the requested engine supports the CharacterSetName parameter for CreateDBInstance , the response includes a list of supported character sets for each engine version.
    :type ListSupportedCharacterSets: boolean
    :param ListSupportedTimezones: If this parameter is specified and the requested engine supports the TimeZone parameter for CreateDBInstance , the response includes a list of supported time zones for each engine version.
    :type ListSupportedTimezones: boolean
    """
    pass


def describe_db_instances(DBInstanceIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBInstanceIdentifier: The user-supplied instance identifier. If this parameter is specified, information from only the specific DB instance is returned. This parameter isn't case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBInstanceIdentifier: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBInstances request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_db_log_files(DBInstanceIdentifier=None, FilenameContains=None, FileLastWritten=None, FileSize=None,
                          Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBInstanceIdentifier: [REQUIRED]
            The customer-assigned name of the DB instance that contains the log files you want to list.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBInstanceIdentifier: string
    :param FilenameContains: Filters the available log files for log file names that contain the specified string.
    :type FilenameContains: string
    :param FileLastWritten: Filters the available log files for files written since the specified date, in POSIX timestamp format with milliseconds.
    :type FileLastWritten: integer
    :param FileSize: Filters the available log files for files larger than the specified size.
    :type FileSize: integer
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
    :type MaxRecords: integer
    :param Marker: The pagination token provided in the previous request. If this parameter is specified the response includes only records beyond the marker, up to MaxRecords.
    :type Marker: string
    """
    pass


def describe_db_parameter_groups(DBParameterGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBParameterGroupName: The name of a specific DB parameter group to return details for.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBParameterGroupName: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBParameterGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_db_parameters(DBParameterGroupName=None, Source=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBParameterGroupName: [REQUIRED]
            The name of a specific DB parameter group to return details for.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBParameterGroupName: string
    :param Source: The parameter types to return.
            Default: All parameter types returned
            Valid Values: user | system | engine-default
            
    :type Source: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_db_security_groups(DBSecurityGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBSecurityGroupName: The name of the DB security group to return details for.
    :type DBSecurityGroupName: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBSecurityGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_db_snapshot_attributes(DBSnapshotIdentifier=None):
    """
    :param DBSnapshotIdentifier: [REQUIRED]
            The identifier for the DB snapshot to describe the attributes for.
            Return typedict
            ReturnsResponse Syntax{
              'DBSnapshotAttributesResult': {
                'DBSnapshotIdentifier': 'string',
                'DBSnapshotAttributes': [
                  {
                    'AttributeName': 'string',
                    'AttributeValues': [
                      'string',
                    ]
                  },
                ]
              }
            }
            Response Structure
            (dict) --
            DBSnapshotAttributesResult (dict) --Contains the results of a successful call to the DescribeDBSnapshotAttributes API action.
            Manual DB snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB snapshot. For more information, see the ModifyDBSnapshotAttribute API action.
            DBSnapshotIdentifier (string) --The identifier of the manual DB snapshot that the attributes apply to.
            DBSnapshotAttributes (list) --The list of attributes and values for the manual DB snapshot.
            (dict) --Contains the name and values of a manual DB snapshot attribute
            Manual DB snapshot attributes are used to authorize other AWS accounts to restore a manual DB snapshot. For more information, see the ModifyDBSnapshotAttribute API.
            AttributeName (string) --The name of the manual DB snapshot attribute.
            The attribute named restore refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the ModifyDBSnapshotAttribute API action.
            AttributeValues (list) --The value or values for the manual DB snapshot attribute.
            If the AttributeName field is set to restore , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB snapshot. If a value of all is in the list, then the manual DB snapshot is public and available for any AWS account to copy or restore.
            (string) --
            
            
            
            
    :type DBSnapshotIdentifier: string
    """
    pass


def describe_db_snapshots(DBInstanceIdentifier=None, DBSnapshotIdentifier=None, SnapshotType=None, Filters=None,
                          MaxRecords=None, Marker=None, IncludeShared=None, IncludePublic=None):
    """
    :param DBInstanceIdentifier: The ID of the DB instance to retrieve the list of DB snapshots for. This parameter cannot be used in conjunction with DBSnapshotIdentifier . This parameter is not case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBInstanceIdentifier: string
    :param DBSnapshotIdentifier: A specific DB snapshot identifier to describe. This parameter cannot be used in conjunction with DBInstanceIdentifier . This value is stored as a lowercase string.
            Constraints:
            Must be 1 to 255 alphanumeric characters.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            If this identifier is for an automated snapshot, the SnapshotType parameter must also be specified.
            
    :type DBSnapshotIdentifier: string
    :param SnapshotType: The type of snapshots to be returned. You can specify one of the following values:
            automated - Return all DB snapshots that have been automatically taken by Amazon RDS for my AWS account.
            manual - Return all DB snapshots that have been taken by my AWS account.
            shared - Return all manual DB snapshots that have been shared to my AWS account.
            public - Return all DB snapshots that have been marked as public.
            If you don't specify a SnapshotType value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not included in the returned results by default. You can include shared snapshots with these results by setting the IncludeShared parameter to true . You can include public snapshots with these results by setting the IncludePublic parameter to true .
            The IncludeShared and IncludePublic parameters don't apply for SnapshotType values of manual or automated . The IncludePublic parameter doesn't apply when SnapshotType is set to shared . The IncludeShared parameter doesn't apply when SnapshotType is set to public .
            
    :type SnapshotType: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBSnapshots request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    :param IncludeShared: Set this value to true to include shared manual DB snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, otherwise set this value to false . The default is false .
            You can give an AWS account permission to restore a manual DB snapshot from another AWS account by using the ModifyDBSnapshotAttribute API action.
            
    :type IncludeShared: boolean
    :param IncludePublic: Set this value to true to include manual DB snapshots that are public and can be copied or restored by any AWS account, otherwise set this value to false . The default is false .
            You can share a manual DB snapshot as public by using the ModifyDBSnapshotAttribute API.
            
    :type IncludePublic: boolean
    """
    pass


def describe_db_subnet_groups(DBSubnetGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBSubnetGroupName: The name of the DB subnet group to return details for.
    :type DBSubnetGroupName: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeDBSubnetGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_engine_default_cluster_parameters(DBParameterGroupFamily=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBParameterGroupFamily: [REQUIRED]
            The name of the DB cluster parameter group family to return engine parameter information for.
            
    :type DBParameterGroupFamily: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeEngineDefaultClusterParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_engine_default_parameters(DBParameterGroupFamily=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param DBParameterGroupFamily: [REQUIRED]
            The name of the DB parameter group family.
            
    :type DBParameterGroupFamily: string
    :param Filters: Not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeEngineDefaultParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_event_categories(SourceType=None, Filters=None):
    """
    :param SourceType: The type of source that will be generating the events.
            Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot
            
    :type SourceType: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_event_subscriptions(SubscriptionName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param SubscriptionName: The name of the RDS event notification subscription you want to describe.
    :type SubscriptionName: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None,
                    EventCategories=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param SourceIdentifier: The identifier of the event source for which events will be returned. If not specified, then all sources are included in the response.
            Constraints:
            If SourceIdentifier is supplied, SourceType must also be provided.
            If the source type is DBInstance , then a DBInstanceIdentifier must be supplied.
            If the source type is DBSecurityGroup , a DBSecurityGroupName must be supplied.
            If the source type is DBParameterGroup , a DBParameterGroupName must be supplied.
            If the source type is DBSnapshot , a DBSnapshotIdentifier must be supplied.
            Cannot end with a hyphen or contain two consecutive hyphens.
            
    :type SourceIdentifier: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.
    :type SourceType: string
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2009-07-08T18:00Z
            
    :type StartTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.
            Example: 2009-07-08T18:00Z
            
    :type EndTime: datetime
    :param Duration: The number of minutes to retrieve events for.
            Default: 60
            
    :type Duration: integer
    :param EventCategories: A list of event categories that trigger notifications for a event notification subscription.
            (string) --
            
    :type EventCategories: list
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeEvents request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_option_group_options(EngineName=None, MajorEngineVersion=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param EngineName: [REQUIRED]
            A required parameter. Options available for the given engine name will be described.
            
    :type EngineName: string
    :param MajorEngineVersion: If specified, filters the results to include only options for the specified major engine version.
    :type MajorEngineVersion: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_option_groups(OptionGroupName=None, Filters=None, Marker=None, MaxRecords=None, EngineName=None,
                           MajorEngineVersion=None):
    """
    :param OptionGroupName: The name of the option group to describe. Cannot be supplied together with EngineName or MajorEngineVersion.
    :type OptionGroupName: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param Marker: An optional pagination token provided by a previous DescribeOptionGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param EngineName: Filters the list of option groups to only include groups associated with a specific database engine.
    :type EngineName: string
    :param MajorEngineVersion: Filters the list of option groups to only include groups associated with a specific database engine version. If specified, then EngineName must also be specified.
    :type MajorEngineVersion: string
    """
    pass


def describe_orderable_db_instance_options(Engine=None, EngineVersion=None, DBInstanceClass=None, LicenseModel=None,
                                           Vpc=None, Filters=None, MaxRecords=None, Marker=None):
    """
    :param Engine: [REQUIRED]
            The name of the engine to retrieve DB instance options for.
            
    :type Engine: string
    :param EngineVersion: The engine version filter value. Specify this parameter to show only the available offerings matching the specified engine version.
    :type EngineVersion: string
    :param DBInstanceClass: The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.
    :type DBInstanceClass: string
    :param LicenseModel: The license model filter value. Specify this parameter to show only the available offerings matching the specified license model.
    :type LicenseModel: string
    :param Vpc: The VPC filter value. Specify this parameter to show only the available VPC or non-VPC offerings.
    :type Vpc: boolean
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_pending_maintenance_actions(ResourceIdentifier=None, Filters=None, Marker=None, MaxRecords=None):
    """
    :param ResourceIdentifier: The ARN of a resource to return pending maintenance actions for.
    :type ResourceIdentifier: string
    :param Filters: A filter that specifies one or more resources to return pending maintenance actions for.
            Supported filters:
            db-instance-id - Accepts DB instance identifiers and DB instance Amazon Resource Names (ARNs). The results list will only include pending maintenance actions for the DB instances identified by these ARNs.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param Marker: An optional pagination token provided by a previous DescribePendingMaintenanceActions request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by MaxRecords .
    :type Marker: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    """
    pass


def describe_reserved_db_instances(ReservedDBInstanceId=None, ReservedDBInstancesOfferingId=None, DBInstanceClass=None,
                                   Duration=None, ProductDescription=None, OfferingType=None, MultiAZ=None,
                                   Filters=None, MaxRecords=None, Marker=None):
    """
    :param ReservedDBInstanceId: The reserved DB instance identifier filter value. Specify this parameter to show only the reservation that matches the specified reservation ID.
    :type ReservedDBInstanceId: string
    :param ReservedDBInstancesOfferingId: The offering identifier filter value. Specify this parameter to show only purchased reservations matching the specified offering identifier.
    :type ReservedDBInstancesOfferingId: string
    :param DBInstanceClass: The DB instance class filter value. Specify this parameter to show only those reservations matching the specified DB instances class.
    :type DBInstanceClass: string
    :param Duration: The duration filter value, specified in years or seconds. Specify this parameter to show only reservations for this duration.
            Valid Values: 1 | 3 | 31536000 | 94608000
            
    :type Duration: string
    :param ProductDescription: The product description filter value. Specify this parameter to show only those reservations matching the specified product description.
    :type ProductDescription: string
    :param OfferingType: The offering type filter value. Specify this parameter to show only the available offerings matching the specified offering type.
            Valid Values: 'Partial Upfront' | 'All Upfront' | 'No Upfront'
            
    :type OfferingType: string
    :param MultiAZ: The Multi-AZ filter value. Specify this parameter to show only those reservations matching the specified Multi-AZ parameter.
    :type MultiAZ: boolean
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more than the MaxRecords value is available, a pagination token called a marker is included in the response so that the following results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_reserved_db_instances_offerings(ReservedDBInstancesOfferingId=None, DBInstanceClass=None, Duration=None,
                                             ProductDescription=None, OfferingType=None, MultiAZ=None, Filters=None,
                                             MaxRecords=None, Marker=None):
    """
    :param ReservedDBInstancesOfferingId: The offering identifier filter value. Specify this parameter to show only the available offering that matches the specified reservation identifier.
            Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
            
    :type ReservedDBInstancesOfferingId: string
    :param DBInstanceClass: The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.
    :type DBInstanceClass: string
    :param Duration: Duration filter value, specified in years or seconds. Specify this parameter to show only reservations for this duration.
            Valid Values: 1 | 3 | 31536000 | 94608000
            
    :type Duration: string
    :param ProductDescription: Product description filter value. Specify this parameter to show only the available offerings matching the specified product description.
    :type ProductDescription: string
    :param OfferingType: The offering type filter value. Specify this parameter to show only the available offerings matching the specified offering type.
            Valid Values: 'Partial Upfront' | 'All Upfront' | 'No Upfront'
            
    :type OfferingType: string
    :param MultiAZ: The Multi-AZ filter value. Specify this parameter to show only the available offerings matching the specified Multi-AZ parameter.
    :type MultiAZ: boolean
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more than the MaxRecords value is available, a pagination token called a marker is included in the response so that the following results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_source_regions(RegionName=None, MaxRecords=None, Marker=None, Filters=None):
    """
    :param RegionName: The source region name. For example, us-east-1 .
            Constraints:
            Must specify a valid AWS Region name.
            
    :type RegionName: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous DescribeSourceRegions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    """
    pass


def download_db_log_file_portion(DBInstanceIdentifier=None, LogFileName=None, Marker=None, NumberOfLines=None):
    """
    :param DBInstanceIdentifier: [REQUIRED]
            The customer-assigned name of the DB instance that contains the log files you want to list.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBInstanceIdentifier: string
    :param LogFileName: [REQUIRED]
            The name of the log file to be downloaded.
            
    :type LogFileName: string
    :param Marker: The pagination token provided in the previous request or '0'. If the Marker parameter is specified the response includes only records beyond the marker until the end of the file or up to NumberOfLines.
    :type Marker: string
    :param NumberOfLines: The number of lines to download. If the number of lines specified results in a file over 1 MB in size, the file will be truncated at 1 MB in size.
            If the NumberOfLines parameter is specified, then the block of lines returned can be from the beginning or the end of the log file, depending on the value of the Marker parameter.
            If neither Marker or NumberOfLines are specified, the entire log file is returned up to a maximum of 10000 lines, starting with the most recent log entries first.
            If NumberOfLines is specified and Marker is not specified, then the most recent lines from the end of the log file are returned.
            If Marker is specified as '0', then the specified number of lines from the beginning of the log file are returned.
            You can download the log file in blocks of lines by specifying the size of the block using the NumberOfLines parameter, and by specifying a value of '0' for the Marker parameter in your first request. Include the Marker value returned in the response as the Marker value for the next request, continuing until the AdditionalDataPending response element returns false.
            
    :type NumberOfLines: integer
    """
    pass


def failover_db_cluster(DBClusterIdentifier=None, TargetDBInstanceIdentifier=None):
    """
    :param DBClusterIdentifier: A DB cluster identifier to force a failover for. This parameter is not case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBClusterIdentifier: string
    :param TargetDBInstanceIdentifier: The name of the instance to promote to the primary instance.
            You must specify the instance identifier for an Aurora Replica in the DB cluster. For example, mydbcluster-replica1 .
            
    :type TargetDBInstanceIdentifier: string
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


def list_tags_for_resource(ResourceName=None, Filters=None):
    """
    :param ResourceName: [REQUIRED]
            The Amazon RDS resource with tags to be listed. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see Constructing an RDS Amazon Resource Name (ARN) .
            
    :type ResourceName: string
    :param Filters: This parameter is not currently supported.
            (dict) --This type is not currently supported.
            Name (string) -- [REQUIRED]This parameter is not currently supported.
            Values (list) -- [REQUIRED]This parameter is not currently supported.
            (string) --
            
            
    :type Filters: list
    """
    pass


def modify_db_cluster(DBClusterIdentifier=None, NewDBClusterIdentifier=None, ApplyImmediately=None,
                      BackupRetentionPeriod=None, DBClusterParameterGroupName=None, VpcSecurityGroupIds=None, Port=None,
                      MasterUserPassword=None, OptionGroupName=None, PreferredBackupWindow=None,
                      PreferredMaintenanceWindow=None):
    """
    :param DBClusterIdentifier: [REQUIRED]
            The DB cluster identifier for the cluster being modified. This parameter is not case-sensitive.
            Constraints:
            Must be the identifier for an existing DB cluster.
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            
    :type DBClusterIdentifier: string
    :param NewDBClusterIdentifier: The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-cluster2
            
    :type NewDBClusterIdentifier: string
    :param ApplyImmediately: A value that specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the DB cluster. If this parameter is set to false , changes to the DB cluster are applied during the next maintenance window.
            The ApplyImmediately parameter only affects the NewDBClusterIdentifier and MasterUserPassword values. If you set the ApplyImmediately parameter value to false, then changes to the NewDBClusterIdentifier and MasterUserPassword values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the ApplyImmediately parameter.
            Default: false
            
    :type ApplyImmediately: boolean
    :param BackupRetentionPeriod: The number of days for which automated backups are retained. You must specify a minimum value of 1.
            Default: 1
            Constraints:
            Must be a value from 1 to 35
            
    :type BackupRetentionPeriod: integer
    :param DBClusterParameterGroupName: The name of the DB cluster parameter group to use for the DB cluster.
    :type DBClusterParameterGroupName: string
    :param VpcSecurityGroupIds: A lst of VPC security groups that the DB cluster will belong to.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param Port: The port number on which the DB cluster accepts connections.
            Constraints: Value must be 1150-65535
            Default: The same port as the original DB cluster.
            
    :type Port: integer
    :param MasterUserPassword: The new password for the master database user. This password can contain any printable ASCII character except '/', ''', or '@'.
            Constraints: Must contain from 8 to 41 characters.
            
    :type MasterUserPassword: string
    :param OptionGroupName: A value that indicates that the DB cluster should be associated with the specified option group. Changing this parameter does not result in an outage except in the following case, and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request. If the parameter change results in an option group that enables OEM, this change can cause a brief (sub-second) period during which new connections are rejected but existing connections are not interrupted.
            Permanent options cannot be removed from an option group. The option group cannot be removed from a DB cluster once it is associated with a DB cluster.
            
    :type OptionGroupName: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
            Default: A 30-minute window selected at random from an 8-hour block of time per region. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon RDS User Guide.
            Constraints:
            Must be in the format hh24:mi-hh24:mi .
            Times should be in Universal Coordinated Time (UTC).
            Must not conflict with the preferred maintenance window.
            Must be at least 30 minutes.
            
    :type PreferredBackupWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon RDS User Guide.
            Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
            Constraints: Minimum 30-minute window.
            
    :type PreferredMaintenanceWindow: string
    """
    pass


def modify_db_cluster_parameter_group(DBClusterParameterGroupName=None, Parameters=None):
    """
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of the DB cluster parameter group to modify.
            
    :type DBClusterParameterGroupName: string
    :param Parameters: [REQUIRED]
            A list of parameters in the DB cluster parameter group to modify.
            (dict) --This data type is used as a request parameter in the ModifyDBParameterGroup and ResetDBParameterGroup actions.
            This data type is used as a response element in the DescribeEngineDefaultParameters and DescribeDBParameters actions.
            ParameterName (string) --Specifies the name of the parameter.
            ParameterValue (string) --Specifies the value of the parameter.
            Description (string) --Provides a description of the parameter.
            Source (string) --Indicates the source of the parameter value.
            ApplyType (string) --Specifies the engine specific parameters type.
            DataType (string) --Specifies the valid data type for the parameter.
            AllowedValues (string) --Specifies the valid range of values for the parameter.
            IsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            ApplyMethod (string) --Indicates when to apply parameter updates.
            
            
    :type Parameters: list
    """
    pass


def modify_db_cluster_snapshot_attribute(DBClusterSnapshotIdentifier=None, AttributeName=None, ValuesToAdd=None,
                                         ValuesToRemove=None):
    """
    :param DBClusterSnapshotIdentifier: [REQUIRED]
            The identifier for the DB cluster snapshot to modify the attributes for.
            
    :type DBClusterSnapshotIdentifier: string
    :param AttributeName: [REQUIRED]
            The name of the DB cluster snapshot attribute to modify.
            To manage authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this value to restore .
            
    :type AttributeName: string
    :param ValuesToAdd: A list of DB cluster snapshot attributes to add to the attribute specified by AttributeName .
            To authorize other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account IDs, or all to make the manual DB cluster snapshot restorable by any AWS account. Do not add the all value for any manual DB cluster snapshots that contain private information that you don't want available to all AWS accounts.
            (string) --
            
    :type ValuesToAdd: list
    :param ValuesToRemove: A list of DB cluster snapshot attributes to remove from the attribute specified by AttributeName .
            To remove authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account identifiers, or all to remove authorization for any AWS account to copy or restore the DB cluster snapshot. If you specify all , an AWS account whose account ID is explicitly added to the restore attribute can still copy or restore a manual DB cluster snapshot.
            (string) --
            
    :type ValuesToRemove: list
    """
    pass


def modify_db_instance(DBInstanceIdentifier=None, AllocatedStorage=None, DBInstanceClass=None, DBSubnetGroupName=None,
                       DBSecurityGroups=None, VpcSecurityGroupIds=None, ApplyImmediately=None, MasterUserPassword=None,
                       DBParameterGroupName=None, BackupRetentionPeriod=None, PreferredBackupWindow=None,
                       PreferredMaintenanceWindow=None, MultiAZ=None, EngineVersion=None, AllowMajorVersionUpgrade=None,
                       AutoMinorVersionUpgrade=None, LicenseModel=None, Iops=None, OptionGroupName=None,
                       NewDBInstanceIdentifier=None, StorageType=None, TdeCredentialArn=None,
                       TdeCredentialPassword=None, CACertificateIdentifier=None, Domain=None, CopyTagsToSnapshot=None,
                       MonitoringInterval=None, DBPortNumber=None, PubliclyAccessible=None, MonitoringRoleArn=None,
                       DomainIAMRoleName=None, PromotionTier=None):
    """
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier. This value is stored as a lowercase string.
            Constraints:
            Must be the identifier for an existing DB instance
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBInstanceIdentifier: string
    :param AllocatedStorage: The new storage capacity of the RDS instance. Changing this setting does not result in an outage and the change is applied during the next maintenance window unless ApplyImmediately is set to true for this request.
            MySQL
            Default: Uses existing setting
            Valid Values: 5-6144
            Constraints: Value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.
            Type: Integer
            MariaDB
            Default: Uses existing setting
            Valid Values: 5-6144
            Constraints: Value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.
            Type: Integer
            PostgreSQL
            Default: Uses existing setting
            Valid Values: 5-6144
            Constraints: Value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.
            Type: Integer
            Oracle
            Default: Uses existing setting
            Valid Values: 10-6144
            Constraints: Value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.
            SQL Server
            Cannot be modified.
            If you choose to migrate your DB instance from using standard storage to using Provisioned IOPS, or from using Provisioned IOPS to using standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance will be available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance will be suspended. No other Amazon RDS operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a Read Replica for the instance, and creating a DB snapshot of the instance.
            
    :type AllocatedStorage: integer
    :param DBInstanceClass: The new compute and memory capacity of the DB instance. To determine the instance classes that are available for a particular DB engine, use the DescribeOrderableDBInstanceOptions action.
            Passing a value for this setting causes an outage during the change and is applied during the next maintenance window, unless ApplyImmediately is specified as true for this request.
            Default: Uses existing setting
            Valid Values: db.t1.micro | db.m1.small | db.m1.medium | db.m1.large | db.m1.xlarge | db.m2.xlarge | db.m2.2xlarge | db.m2.4xlarge | db.m3.medium | db.m3.large | db.m3.xlarge | db.m3.2xlarge | db.m4.large | db.m4.xlarge | db.m4.2xlarge | db.m4.4xlarge | db.m4.10xlarge | db.r3.large | db.r3.xlarge | db.r3.2xlarge | db.r3.4xlarge | db.r3.8xlarge | db.t2.micro | db.t2.small | db.t2.medium | db.t2.large
            
    :type DBInstanceClass: string
    :param DBSubnetGroupName: The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC. If your DB instance is not in a VPC, you can also use this parameter to move your DB instance into a VPC. For more information, see Updating the VPC for a DB Instance .
            Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you specify true for the ApplyImmediately parameter.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens.
            Example: mySubnetGroup
            
    :type DBSubnetGroupName: string
    :param DBSecurityGroups: A list of DB security groups to authorize on this DB instance. Changing this setting does not result in an outage and the change is asynchronously applied as soon as possible.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            (string) --
            
    :type DBSecurityGroups: list
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to authorize on this DB instance. This change is asynchronously applied as soon as possible.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param ApplyImmediately: Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the DB instance.
            If this parameter is set to false , changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and will be applied on the next call to RebootDBInstance , or the next failure reboot. Review the table of parameters in Modifying a DB Instance and Using the Apply Immediately Parameter to see the impact that setting ApplyImmediately to true or false has for each modified parameter and to determine when the changes will be applied.
            Default: false
            
    :type ApplyImmediately: boolean
    :param MasterUserPassword: The new password for the DB instance master user. Can be any printable ASCII character except '/', ''', or '@'.
            Changing this parameter does not result in an outage and the change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the MasterUserPassword element exists in the PendingModifiedValues element of the operation response.
            Default: Uses existing setting
            Constraints: Must be 8 to 41 alphanumeric characters (MySQL, MariaDB, and Amazon Aurora), 8 to 30 alphanumeric characters (Oracle), or 8 to 128 alphanumeric characters (SQL Server).
            Note
            Amazon RDS API actions never return the password, so this action provides a way to regain access to a primary instance user if the password is lost. This includes restoring privileges that might have been accidentally revoked.
            
    :type MasterUserPassword: string
    :param DBParameterGroupName: The name of the DB parameter group to apply to the DB instance. Changing this setting does not result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. The db instance will NOT be rebooted automatically and the parameter changes will NOT be applied during the next maintenance window.
            Default: Uses existing setting
            Constraints: The DB parameter group must be in the same DB parameter group family as this DB instance.
            
    :type DBParameterGroupName: string
    :param BackupRetentionPeriod: The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
            Changing this parameter can result in an outage if you change from 0 to a non-zero value or from a non-zero value to 0. These changes are applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request. If you change the parameter from one non-zero value to another non-zero value, the change is asynchronously applied as soon as possible.
            Default: Uses existing setting
            Constraints:
            Must be a value from 0 to 35
            Can be specified for a MySQL Read Replica only if the source is running MySQL 5.6
            Can be specified for a PostgreSQL Read Replica only if the source is running PostgreSQL 9.3.5
            Cannot be set to 0 if the DB instance is a source to Read Replicas
            
    :type BackupRetentionPeriod: integer
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod parameter. Changing this parameter does not result in an outage and the change is asynchronously applied as soon as possible.
            Constraints:
            Must be in the format hh24:mi-hh24:mi
            Times should be in Universal Time Coordinated (UTC)
            Must not conflict with the preferred maintenance window
            Must be at least 30 minutes
            
    :type PreferredBackupWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter does not result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter will cause a reboot of the DB instance. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.
            Default: Uses existing setting
            Format: ddd:hh24:mi-ddd:hh24:mi
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Must be at least 30 minutes
            
    :type PreferredMaintenanceWindow: string
    :param MultiAZ: Specifies if the DB instance is a Multi-AZ deployment. Changing this parameter does not result in an outage and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request.
            Constraints: Cannot be specified if the DB instance is a Read Replica.
            
    :type MultiAZ: boolean
    :param EngineVersion: The version number of the database engine to upgrade to. Changing this parameter results in an outage and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request.
            For major version upgrades, if a non-default DB parameter group is currently in use, a new DB parameter group in the DB parameter group family for the new engine version must be specified. The new DB parameter group can be the default for that DB parameter group family.
            For a list of valid engine versions, see CreateDBInstance .
            
    :type EngineVersion: string
    :param AllowMajorVersionUpgrade: Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage and the change is asynchronously applied as soon as possible.
            Constraints: This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the DB instance's current version.
            
    :type AllowMajorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor version upgrades will be applied automatically to the DB instance during the maintenance window. Changing this parameter does not result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to true during the maintenance window, and a newer minor version is available, and RDS has enabled auto patching for that engine version.
    :type AutoMinorVersionUpgrade: boolean
    :param LicenseModel: The license model for the DB instance.
            Valid values: license-included | bring-your-own-license | general-public-license
            
    :type LicenseModel: string
    :param Iops: The new Provisioned IOPS (I/O operations per second) value for the RDS instance. Changing this setting does not result in an outage and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request.
            Default: Uses existing setting
            Constraints: Value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value. If you are migrating from Provisioned IOPS to standard storage, set this value to 0. The DB instance will require a reboot for the change in storage type to take effect.
            SQL Server
            Setting the IOPS value for the SQL Server database engine is not supported.
            Type: Integer
            If you choose to migrate your DB instance from using standard storage to using Provisioned IOPS, or from using Provisioned IOPS to using standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance will be available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance will be suspended. No other Amazon RDS operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a Read Replica for the instance, and creating a DB snapshot of the instance.
            
    :type Iops: integer
    :param OptionGroupName: Indicates that the DB instance should be associated with the specified option group. Changing this parameter does not result in an outage except in the following case and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request. If the parameter change results in an option group that enables OEM, this change can cause a brief (sub-second) period during which new connections are rejected but existing connections are not interrupted.
            Permanent options, such as the TDE option for Oracle Advanced Security TDE, cannot be removed from an option group, and that option group cannot be removed from a DB instance once it is associated with a DB instance
            
    :type OptionGroupName: string
    :param NewDBInstanceIdentifier: The new DB instance identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot will occur immediately if you set Apply Immediately to true, or will occur during the next maintenance window if Apply Immediately to false. This value is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type NewDBInstanceIdentifier: string
    :param StorageType: Specifies the storage type to be associated with the DB instance.
            Valid values: standard | gp2 | io1
            If you specify io1 , you must also include a value for the Iops parameter.
            Default: io1 if the Iops parameter is specified; otherwise standard
            
    :type StorageType: string
    :param TdeCredentialArn: The ARN from the Key Store with which to associate the instance for TDE encryption.
    :type TdeCredentialArn: string
    :param TdeCredentialPassword: The password for the given ARN from the Key Store in order to access the device.
    :type TdeCredentialPassword: string
    :param CACertificateIdentifier: Indicates the certificate that needs to be associated with the instance.
    :type CACertificateIdentifier: string
    :param Domain: The Active Directory Domain to move the instance to. Specify none to remove the instance from its current domain. The domain must be created prior to this operation. Currently only a Microsoft SQL Server instance can be created in a Active Directory Domain.
    :type Domain: string
    :param CopyTagsToSnapshot: True to copy all tags from the DB instance to snapshots of the DB instance; otherwise false. The default is false.
    :type CopyTagsToSnapshot: boolean
    :param MonitoringInterval: The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
            If MonitoringRoleArn is specified, then you must also set MonitoringInterval to a value other than 0.
            Valid Values: 0, 1, 5, 10, 15, 30, 60
            
    :type MonitoringInterval: integer
    :param DBPortNumber: The port number on which the database accepts connections.
            The value of the DBPortNumber parameter must not match any of the port values specified for options in the option group for the DB instance.
            Your database will restart when you change the DBPortNumber value regardless of the value of the ApplyImmediately parameter.
            MySQL
            Default: 3306
            Valid Values: 1150-65535
            MariaDB
            Default: 3306
            Valid Values: 1150-65535
            PostgreSQL
            Default: 5432
            Valid Values: 1150-65535
            Type: Integer
            Oracle
            Default: 1521
            Valid Values: 1150-65535
            SQL Server
            Default: 1433
            Valid Values: 1150-65535 except for 1434 , 3389 , 47001 , 49152 , and 49152 through 49156 .
            Amazon Aurora
            Default: 3306
            Valid Values: 1150-65535
            
    :type DBPortNumber: integer
    :param PubliclyAccessible: Boolean value that indicates if the DB instance has a publicly resolvable DNS name. Set to True to make the DB instance Internet-facing with a publicly resolvable DNS name, which resolves to a public IP address. Set to False to make the DB instance internal with a DNS name that resolves to a private IP address.
            PubliclyAccessible only applies to DB instances in a VPC. The DB instance must be part of a public subnet and PubliclyAccessible must be true in order for it to be publicly accessible.
            Changes to the PubliclyAccessible parameter are applied immediately regardless of the value of the ApplyImmediately parameter.
            Default: false
            
    :type PubliclyAccessible: boolean
    :param MonitoringRoleArn: The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to CloudWatch Logs. For example, arn:aws:iam:123456789012:role/emaccess . For information on creating a monitoring role, go to To create an IAM role for Amazon RDS Enhanced Monitoring .
            If MonitoringInterval is set to a value other than 0, then you must supply a MonitoringRoleArn value.
            
    :type MonitoringRoleArn: string
    :param DomainIAMRoleName: The name of the IAM role to use when making API calls to the Directory Service.
    :type DomainIAMRoleName: string
    :param PromotionTier: A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see Fault Tolerance for an Aurora DB Cluster .
            Default: 1
            Valid Values: 0 - 15
            
    :type PromotionTier: integer
    """
    pass


def modify_db_parameter_group(DBParameterGroupName=None, Parameters=None):
    """
    :param DBParameterGroupName: [REQUIRED]
            The name of the DB parameter group.
            Constraints:
            Must be the name of an existing DB parameter group
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBParameterGroupName: string
    :param Parameters: [REQUIRED]
            An array of parameter names, values, and the apply method for the parameter update. At least one parameter name, value, and apply method must be supplied; subsequent arguments are optional. A maximum of 20 parameters can be modified in a single request.
            Valid Values (for the application method): immediate | pending-reboot
            Note
            You can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when you reboot the DB instance without failover.
            (dict) --This data type is used as a request parameter in the ModifyDBParameterGroup and ResetDBParameterGroup actions.
            This data type is used as a response element in the DescribeEngineDefaultParameters and DescribeDBParameters actions.
            ParameterName (string) --Specifies the name of the parameter.
            ParameterValue (string) --Specifies the value of the parameter.
            Description (string) --Provides a description of the parameter.
            Source (string) --Indicates the source of the parameter value.
            ApplyType (string) --Specifies the engine specific parameters type.
            DataType (string) --Specifies the valid data type for the parameter.
            AllowedValues (string) --Specifies the valid range of values for the parameter.
            IsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            ApplyMethod (string) --Indicates when to apply parameter updates.
            
            
    :type Parameters: list
    """
    pass


def modify_db_snapshot_attribute(DBSnapshotIdentifier=None, AttributeName=None, ValuesToAdd=None, ValuesToRemove=None):
    """
    :param DBSnapshotIdentifier: [REQUIRED]
            The identifier for the DB snapshot to modify the attributes for.
            
    :type DBSnapshotIdentifier: string
    :param AttributeName: [REQUIRED]
            The name of the DB snapshot attribute to modify.
            To manage authorization for other AWS accounts to copy or restore a manual DB snapshot, set this value to restore .
            
    :type AttributeName: string
    :param ValuesToAdd: A list of DB snapshot attributes to add to the attribute specified by AttributeName .
            To authorize other AWS accounts to copy or restore a manual snapshot, set this list to include one or more AWS account IDs, or all to make the manual DB snapshot restorable by any AWS account. Do not add the all value for any manual DB snapshots that contain private information that you don't want available to all AWS accounts.
            (string) --
            
    :type ValuesToAdd: list
    :param ValuesToRemove: A list of DB snapshot attributes to remove from the attribute specified by AttributeName .
            To remove authorization for other AWS accounts to copy or restore a manual snapshot, set this list to include one or more AWS account identifiers, or all to remove authorization for any AWS account to copy or restore the DB snapshot. If you specify all , an AWS account whose account ID is explicitly added to the restore attribute can still copy or restore the manual DB snapshot.
            (string) --
            
    :type ValuesToRemove: list
    """
    pass


def modify_db_subnet_group(DBSubnetGroupName=None, DBSubnetGroupDescription=None, SubnetIds=None):
    """
    :param DBSubnetGroupName: [REQUIRED]
            The name for the DB subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            
    :type DBSubnetGroupName: string
    :param DBSubnetGroupDescription: The description for the DB subnet group.
    :type DBSubnetGroupDescription: string
    :param SubnetIds: [REQUIRED]
            The EC2 subnet IDs for the DB subnet group.
            (string) --
            
    :type SubnetIds: list
    """
    pass


def modify_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None,
                              Enabled=None):
    """
    :param SubscriptionName: [REQUIRED]
            The name of the RDS event notification subscription.
            
    :type SubscriptionName: string
    :param SnsTopicArn: The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
    :type SnsTopicArn: string
    :param SourceType: The type of source that will be generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.
            Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot
            
    :type SourceType: string
    :param EventCategories: A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType in the Events topic in the Amazon RDS User Guide or by using the DescribeEventCategories action.
            (string) --
            
    :type EventCategories: list
    :param Enabled: A Boolean value; set to true to activate the subscription.
    :type Enabled: boolean
    """
    pass


def modify_option_group(OptionGroupName=None, OptionsToInclude=None, OptionsToRemove=None, ApplyImmediately=None):
    """
    :param OptionGroupName: [REQUIRED]
            The name of the option group to be modified.
            Permanent options, such as the TDE option for Oracle Advanced Security TDE, cannot be removed from an option group, and that option group cannot be removed from a DB instance once it is associated with a DB instance
            
    :type OptionGroupName: string
    :param OptionsToInclude: Options in this list are added to the option group or, if already present, the specified configuration is used to update the existing configuration.
            (dict) --A list of all available options
            OptionName (string) -- [REQUIRED]The configuration of options to include in a group.
            Port (integer) --The optional port for the option.
            OptionVersion (string) --The version for the option.
            DBSecurityGroupMemberships (list) --A list of DBSecurityGroupMemebrship name strings used for this option.
            (string) --
            VpcSecurityGroupMemberships (list) --A list of VpcSecurityGroupMemebrship name strings used for this option.
            (string) --
            OptionSettings (list) --The option settings to include in an option group.
            (dict) --Option settings are the actual settings being applied or configured for that option. It is used when you modify an option group or describe option groups. For example, the NATIVE_NETWORK_ENCRYPTION option has a setting called SQLNET.ENCRYPTION_SERVER that can have several different values.
            Name (string) --The name of the option that has settings that you can set.
            Value (string) --The current value of the option setting.
            DefaultValue (string) --The default value of the option setting.
            Description (string) --The description of the option setting.
            ApplyType (string) --The DB engine specific parameter type.
            DataType (string) --The data type of the option setting.
            AllowedValues (string) --The allowed values of the option setting.
            IsModifiable (boolean) --A Boolean value that, when true, indicates the option setting can be modified from the default.
            IsCollection (boolean) --Indicates if the option setting is part of a collection.
            
            
            
    :type OptionsToInclude: list
    :param OptionsToRemove: Options in this list are removed from the option group.
            (string) --
            
    :type OptionsToRemove: list
    :param ApplyImmediately: Indicates whether the changes should be applied immediately, or during the next maintenance window for each instance associated with the option group.
    :type ApplyImmediately: boolean
    """
    pass


def promote_read_replica(DBInstanceIdentifier=None, BackupRetentionPeriod=None, PreferredBackupWindow=None):
    """
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier. This value is stored as a lowercase string.
            Constraints:
            Must be the identifier for an existing Read Replica DB instance
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: mydbinstance
            
    :type DBInstanceIdentifier: string
    :param BackupRetentionPeriod: The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
            Default: 1
            Constraints:
            Must be a value from 0 to 8
            
    :type BackupRetentionPeriod: integer
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
            Default: A 30-minute window selected at random from an 8-hour block of time per region. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon RDS User Guide.
            Constraints:
            Must be in the format hh24:mi-hh24:mi .
            Times should be in Universal Coordinated Time (UTC).
            Must not conflict with the preferred maintenance window.
            Must be at least 30 minutes.
            
    :type PreferredBackupWindow: string
    """
    pass


def promote_read_replica_db_cluster(DBClusterIdentifier=None):
    """
    :param DBClusterIdentifier: [REQUIRED]
            The identifier of the DB cluster Read Replica to promote. This parameter is not case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster-replica1
            Return typedict
            ReturnsResponse Syntax{
              'DBCluster': {
                'AllocatedStorage': 123,
                'AvailabilityZones': [
                  'string',
                ],
                'BackupRetentionPeriod': 123,
                'CharacterSetName': 'string',
                'DatabaseName': 'string',
                'DBClusterIdentifier': 'string',
                'DBClusterParameterGroup': 'string',
                'DBSubnetGroup': 'string',
                'Status': 'string',
                'PercentProgress': 'string',
                'EarliestRestorableTime': datetime(2015, 1, 1),
                'Endpoint': 'string',
                'ReaderEndpoint': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'LatestRestorableTime': datetime(2015, 1, 1),
                'Port': 123,
                'MasterUsername': 'string',
                'DBClusterOptionGroupMemberships': [
                  {
                    'DBClusterOptionGroupName': 'string',
                    'Status': 'string'
                  },
                ],
                'PreferredBackupWindow': 'string',
                'PreferredMaintenanceWindow': 'string',
                'ReplicationSourceIdentifier': 'string',
                'ReadReplicaIdentifiers': [
                  'string',
                ],
                'DBClusterMembers': [
                  {
                    'DBInstanceIdentifier': 'string',
                    'IsClusterWriter': True|False,
                    'DBClusterParameterGroupStatus': 'string',
                    'PromotionTier': 123
                  },
                ],
                'VpcSecurityGroups': [
                  {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                  },
                ],
                'HostedZoneId': 'string',
                'StorageEncrypted': True|False,
                'KmsKeyId': 'string',
                'DbClusterResourceId': 'string',
                'DBClusterArn': 'string',
                'AssociatedRoles': [
                  {
                    'RoleArn': 'string',
                    'Status': 'string'
                  },
                ]
              }
            }
            Response Structure
            (dict) --
            DBCluster (dict) --Contains the result of a successful invocation of the following actions:
            CreateDBCluster
            DeleteDBCluster
            FailoverDBCluster
            ModifyDBCluster
            RestoreDBClusterFromSnapshot
            RestoreDBClusterToPointInTime
            This data type is used as a response element in the DescribeDBClusters action.
            AllocatedStorage (integer) --Specifies the allocated storage size in gigabytes (GB).
            AvailabilityZones (list) --Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.
            (string) --
            BackupRetentionPeriod (integer) --Specifies the number of days for which automatic DB snapshots are retained.
            CharacterSetName (string) --If present, specifies the name of the character set that this cluster is associated with.
            DatabaseName (string) --Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.
            DBClusterIdentifier (string) --Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.
            DBClusterParameterGroup (string) --Specifies the name of the DB cluster parameter group for the DB cluster.
            DBSubnetGroup (string) --Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.
            Status (string) --Specifies the current state of this DB cluster.
            PercentProgress (string) --Specifies the progress of the operation as a percentage.
            EarliestRestorableTime (datetime) --Specifies the earliest time to which a database can be restored with point-in-time restore.
            Endpoint (string) --Specifies the connection endpoint for the primary instance of the DB cluster.
            ReaderEndpoint (string) --The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Aurora Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Aurora distributes the connection requests among the Aurora Replicas in the DB cluster. This functionality can help balance your read workload across multiple Aurora Replicas in your DB cluster.
            If a failover occurs, and the Aurora Replica that you are connected to is promoted to be the primary instance, your connection will be dropped. To continue sending your read workload to other Aurora Replicas in the cluster, you can then recoonect to the reader endpoint.
            Engine (string) --Provides the name of the database engine to be used for this DB cluster.
            EngineVersion (string) --Indicates the database engine version.
            LatestRestorableTime (datetime) --Specifies the latest time to which a database can be restored with point-in-time restore.
            Port (integer) --Specifies the port that the database engine is listening on.
            MasterUsername (string) --Contains the master username for the DB cluster.
            DBClusterOptionGroupMemberships (list) --Provides the list of option group memberships for this DB cluster.
            (dict) --Contains status information for a DB cluster option group.
            DBClusterOptionGroupName (string) --Specifies the name of the DB cluster option group.
            Status (string) --Specifies the status of the DB cluster option group.
            
            PreferredBackupWindow (string) --Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .
            PreferredMaintenanceWindow (string) --Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
            ReplicationSourceIdentifier (string) --Contains the identifier of the source DB cluster if this DB cluster is a Read Replica.
            ReadReplicaIdentifiers (list) --Contains one or more identifiers of the Read Replicas associated with this DB cluster.
            (string) --
            DBClusterMembers (list) --Provides the list of instances that make up the DB cluster.
            (dict) --Contains information about an instance that is part of a DB cluster.
            DBInstanceIdentifier (string) --Specifies the instance identifier for this member of the DB cluster.
            IsClusterWriter (boolean) --Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.
            DBClusterParameterGroupStatus (string) --Specifies the status of the DB cluster parameter group for this member of the DB cluster.
            PromotionTier (integer) --A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see Fault Tolerance for an Aurora DB Cluster .
            
            VpcSecurityGroups (list) --Provides a list of VPC security groups that the DB cluster belongs to.
            (dict) --This data type is used as a response element for queries on VPC security group membership.
            VpcSecurityGroupId (string) --The name of the VPC security group.
            Status (string) --The status of the VPC security group.
            
            HostedZoneId (string) --Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
            StorageEncrypted (boolean) --Specifies whether the DB cluster is encrypted.
            KmsKeyId (string) --If StorageEncrypted is true, the KMS key identifier for the encrypted DB cluster.
            DbClusterResourceId (string) --The region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the KMS key for the DB cluster is accessed.
            DBClusterArn (string) --The Amazon Resource Name (ARN) for the DB cluster.
            AssociatedRoles (list) --Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
            (dict) --Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.
            RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.
            Status (string) --Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:
            ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
            PENDING - the IAM role ARN is being associated with the DB cluster.
            INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.
            
            
            
            
    :type DBClusterIdentifier: string
    """
    pass


def purchase_reserved_db_instances_offering(ReservedDBInstancesOfferingId=None, ReservedDBInstanceId=None,
                                            DBInstanceCount=None, Tags=None):
    """
    :param ReservedDBInstancesOfferingId: [REQUIRED]
            The ID of the Reserved DB instance offering to purchase.
            Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
            
    :type ReservedDBInstancesOfferingId: string
    :param ReservedDBInstanceId: Customer-specified identifier to track this reservation.
            Example: myreservationID
            
    :type ReservedDBInstanceId: string
    :param DBInstanceCount: The number of instances to reserve.
            Default: 1
            
    :type DBInstanceCount: integer
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def reboot_db_instance(DBInstanceIdentifier=None, ForceFailover=None):
    """
    :param DBInstanceIdentifier: [REQUIRED]
            The DB instance identifier. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBInstanceIdentifier: string
    :param ForceFailover: When true , the reboot will be conducted through a MultiAZ failover.
            Constraint: You cannot specify true if the instance is not configured for MultiAZ.
            
    :type ForceFailover: boolean
    """
    pass


def remove_role_from_db_cluster(DBClusterIdentifier=None, RoleArn=None):
    """
    :param DBClusterIdentifier: [REQUIRED]
            The name of the DB cluster to disassociate the IAM role rom.
            
    :type DBClusterIdentifier: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role to disassociate from the Aurora DB cluster, for example arn:aws:iam::123456789012:role/AuroraAccessRole .
            
    :type RoleArn: string
    """
    pass


def remove_source_identifier_from_subscription(SubscriptionName=None, SourceIdentifier=None):
    """
    :param SubscriptionName: [REQUIRED]
            The name of the RDS event notification subscription you want to remove a source identifier from.
            
    :type SubscriptionName: string
    :param SourceIdentifier: [REQUIRED]
            The source identifier to be removed from the subscription, such as the DB instance identifier for a DB instance or the name of a security group.
            
    :type SourceIdentifier: string
    """
    pass


def remove_tags_from_resource(ResourceName=None, TagKeys=None):
    """
    :param ResourceName: [REQUIRED]
            The Amazon RDS resource the tags will be removed from. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see Constructing an RDS Amazon Resource Name (ARN) .
            
    :type ResourceName: string
    :param TagKeys: [REQUIRED]
            The tag key (name) of the tag to be removed.
            (string) --
            
    :type TagKeys: list
    """
    pass


def reset_db_cluster_parameter_group(DBClusterParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    :param DBClusterParameterGroupName: [REQUIRED]
            The name of the DB cluster parameter group to reset.
            
    :type DBClusterParameterGroupName: string
    :param ResetAllParameters: A value that is set to true to reset all parameters in the DB cluster parameter group to their default values, and false otherwise. You cannot use this parameter if there is a list of parameter names specified for the Parameters parameter.
    :type ResetAllParameters: boolean
    :param Parameters: A list of parameter names in the DB cluster parameter group to reset to the default values. You cannot use this parameter if the ResetAllParameters parameter is set to true .
            (dict) --This data type is used as a request parameter in the ModifyDBParameterGroup and ResetDBParameterGroup actions.
            This data type is used as a response element in the DescribeEngineDefaultParameters and DescribeDBParameters actions.
            ParameterName (string) --Specifies the name of the parameter.
            ParameterValue (string) --Specifies the value of the parameter.
            Description (string) --Provides a description of the parameter.
            Source (string) --Indicates the source of the parameter value.
            ApplyType (string) --Specifies the engine specific parameters type.
            DataType (string) --Specifies the valid data type for the parameter.
            AllowedValues (string) --Specifies the valid range of values for the parameter.
            IsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            ApplyMethod (string) --Indicates when to apply parameter updates.
            
            
    :type Parameters: list
    """
    pass


def reset_db_parameter_group(DBParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    :param DBParameterGroupName: [REQUIRED]
            The name of the DB parameter group.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBParameterGroupName: string
    :param ResetAllParameters: Specifies whether (true ) or not (false ) to reset all parameters in the DB parameter group to default values.
            Default: true
            
    :type ResetAllParameters: boolean
    :param Parameters: An array of parameter names, values, and the apply method for the parameter update. At least one parameter name, value, and apply method must be supplied; subsequent arguments are optional. A maximum of 20 parameters can be modified in a single request.
            MySQL
            Valid Values (for Apply method): immediate | pending-reboot
            You can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when DB instance reboots.
            MariaDB
            Valid Values (for Apply method): immediate | pending-reboot
            You can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when DB instance reboots.
            Oracle
            Valid Values (for Apply method): pending-reboot
            (dict) --This data type is used as a request parameter in the ModifyDBParameterGroup and ResetDBParameterGroup actions.
            This data type is used as a response element in the DescribeEngineDefaultParameters and DescribeDBParameters actions.
            ParameterName (string) --Specifies the name of the parameter.
            ParameterValue (string) --Specifies the value of the parameter.
            Description (string) --Provides a description of the parameter.
            Source (string) --Indicates the source of the parameter value.
            ApplyType (string) --Specifies the engine specific parameters type.
            DataType (string) --Specifies the valid data type for the parameter.
            AllowedValues (string) --Specifies the valid range of values for the parameter.
            IsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.
            MinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.
            ApplyMethod (string) --Indicates when to apply parameter updates.
            
            
    :type Parameters: list
    """
    pass


def restore_db_cluster_from_s3(AvailabilityZones=None, BackupRetentionPeriod=None, CharacterSetName=None,
                               DatabaseName=None, DBClusterIdentifier=None, DBClusterParameterGroupName=None,
                               VpcSecurityGroupIds=None, DBSubnetGroupName=None, Engine=None, EngineVersion=None,
                               Port=None, MasterUsername=None, MasterUserPassword=None, OptionGroupName=None,
                               PreferredBackupWindow=None, PreferredMaintenanceWindow=None, Tags=None,
                               StorageEncrypted=None, KmsKeyId=None, SourceEngine=None, SourceEngineVersion=None,
                               S3BucketName=None, S3Prefix=None, S3IngestionRoleArn=None):
    """
    :param AvailabilityZones: A list of EC2 Availability Zones that instances in the restored DB cluster can be created in.
            (string) --
            
    :type AvailabilityZones: list
    :param BackupRetentionPeriod: The number of days for which automated backups of the restored DB cluster are retained. You must specify a minimum value of 1.
            Default: 1
            Constraints:
            Must be a value from 1 to 35
            
    :type BackupRetentionPeriod: integer
    :param CharacterSetName: A value that indicates that the restored DB cluster should be associated with the specified CharacterSet.
    :type CharacterSetName: string
    :param DatabaseName: The database name for the restored DB cluster.
    :type DatabaseName: string
    :param DBClusterIdentifier: [REQUIRED]
            The name of the DB cluster to create from the source data in the S3 bucket. This parameter is isn't case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: my-cluster1
            
    :type DBClusterIdentifier: string
    :param DBClusterParameterGroupName: The name of the DB cluster parameter group to associate with the restored DB cluster. If this argument is omitted, default.aurora5.6 will be used.
            Constraints:
            Must be 1 to 255 alphanumeric characters
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBClusterParameterGroupName: string
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to associate with the restored DB cluster.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param DBSubnetGroupName: A DB subnet group to associate with the restored DB cluster.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            
    :type DBSubnetGroupName: string
    :param Engine: [REQUIRED]
            The name of the database engine to be used for the restored DB cluster.
            Valid Values: aurora
            
    :type Engine: string
    :param EngineVersion: The version number of the database engine to use.
            Aurora
            Example: 5.6.10a
            
    :type EngineVersion: string
    :param Port: The port number on which the instances in the restored DB cluster accept connections.
            Default: 3306
            
    :type Port: integer
    :param MasterUsername: [REQUIRED]
            The name of the master user for the restored DB cluster.
            Constraints:
            Must be 1 to 16 alphanumeric characters.
            First character must be a letter.
            Cannot be a reserved word for the chosen database engine.
            
    :type MasterUsername: string
    :param MasterUserPassword: [REQUIRED]
            The password for the master database user. This password can contain any printable ASCII character except '/', ''', or '@'.
            Constraints: Must contain from 8 to 41 characters.
            
    :type MasterUserPassword: string
    :param OptionGroupName: A value that indicates that the restored DB cluster should be associated with the specified option group.
            Permanent options cannot be removed from an option group. An option group cannot be removed from a DB cluster once it is associated with a DB cluster.
            
    :type OptionGroupName: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.
            Default: A 30-minute window selected at random from an 8-hour block of time per region. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon RDS User Guide.
            Constraints:
            Must be in the format hh24:mi-hh24:mi .
            Times should be in Universal Coordinated Time (UTC).
            Must not conflict with the preferred maintenance window.
            Must be at least 30 minutes.
            
    :type PreferredBackupWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon RDS User Guide.
            Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
            Constraints: Minimum 30-minute window.
            
    :type PreferredMaintenanceWindow: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param StorageEncrypted: Specifies whether the restored DB cluster is encrypted.
    :type StorageEncrypted: boolean
    :param KmsKeyId: The KMS key identifier for an encrypted DB cluster.
            The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KM encryption key.
            If the StorageEncrypted parameter is true, and you do not specify a value for the KmsKeyId parameter, then Amazon RDS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
            
    :type KmsKeyId: string
    :param SourceEngine: [REQUIRED]
            The identifier for the database engine that was backed up to create the files stored in the Amazon S3 bucket.
            Valid values: mysql
            
    :type SourceEngine: string
    :param SourceEngineVersion: [REQUIRED]
            The version of the database that the backup files were created from.
            MySQL version 5.5 and 5.6 are supported.
            Example: 5.6.22
            
    :type SourceEngineVersion: string
    :param S3BucketName: [REQUIRED]
            The name of the Amazon S3 bucket that contains the data used to create the Amazon Aurora DB cluster.
            
    :type S3BucketName: string
    :param S3Prefix: The prefix for all of the file names that contain the data used to create the Amazon Aurora DB cluster. If you do not specify a SourceS3Prefix value, then the Amazon Aurora DB cluster is created by using all of the files in the Amazon S3 bucket.
    :type S3Prefix: string
    :param S3IngestionRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon RDS to access the Amazon S3 bucket on your behalf.
            
    :type S3IngestionRoleArn: string
    """
    pass


def restore_db_cluster_from_snapshot(AvailabilityZones=None, DBClusterIdentifier=None, SnapshotIdentifier=None,
                                     Engine=None, EngineVersion=None, Port=None, DBSubnetGroupName=None,
                                     DatabaseName=None, OptionGroupName=None, VpcSecurityGroupIds=None, Tags=None,
                                     KmsKeyId=None):
    """
    :param AvailabilityZones: Provides the list of EC2 Availability Zones that instances in the restored DB cluster can be created in.
            (string) --
            
    :type AvailabilityZones: list
    :param DBClusterIdentifier: [REQUIRED]
            The name of the DB cluster to create from the DB cluster snapshot. This parameter isn't case-sensitive.
            Constraints:
            Must contain from 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-snapshot-id
            
    :type DBClusterIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]
            The identifier for the DB cluster snapshot to restore from.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type SnapshotIdentifier: string
    :param Engine: [REQUIRED]
            The database engine to use for the new DB cluster.
            Default: The same as source
            Constraint: Must be compatible with the engine of the source
            
    :type Engine: string
    :param EngineVersion: The version of the database engine to use for the new DB cluster.
    :type EngineVersion: string
    :param Port: The port number on which the new DB cluster accepts connections.
            Constraints: Value must be 1150-65535
            Default: The same port as the original DB cluster.
            
    :type Port: integer
    :param DBSubnetGroupName: The name of the DB subnet group to use for the new DB cluster.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            
    :type DBSubnetGroupName: string
    :param DatabaseName: The database name for the restored DB cluster.
    :type DatabaseName: string
    :param OptionGroupName: The name of the option group to use for the restored DB cluster.
    :type OptionGroupName: string
    :param VpcSecurityGroupIds: A list of VPC security groups that the new DB cluster will belong to.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param Tags: The tags to be assigned to the restored DB cluster.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param KmsKeyId: The KMS key identifier to use when restoring an encrypted DB cluster from a DB cluster snapshot.
            The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.
            If you do not specify a value for the KmsKeyId parameter, then the following will occur:
            If the DB cluster snapshot is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB cluster snapshot.
            If the DB cluster snapshot is not encrypted, then the restored DB cluster is encrypted using the specified encryption key.
            
    :type KmsKeyId: string
    """
    pass


def restore_db_cluster_to_point_in_time(DBClusterIdentifier=None, SourceDBClusterIdentifier=None, RestoreToTime=None,
                                        UseLatestRestorableTime=None, Port=None, DBSubnetGroupName=None,
                                        OptionGroupName=None, VpcSecurityGroupIds=None, Tags=None, KmsKeyId=None):
    """
    :param DBClusterIdentifier: [REQUIRED]
            The name of the new DB cluster to be created.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type DBClusterIdentifier: string
    :param SourceDBClusterIdentifier: [REQUIRED]
            The identifier of the source DB cluster from which to restore.
            Constraints:
            Must be the identifier of an existing database instance
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type SourceDBClusterIdentifier: string
    :param RestoreToTime: The date and time to restore the DB cluster to.
            Valid Values: Value must be a time in Universal Coordinated Time (UTC) format
            Constraints:
            Must be before the latest restorable time for the DB instance
            Cannot be specified if UseLatestRestorableTime parameter is true
            Example: 2015-03-07T23:45:00Z
            
    :type RestoreToTime: datetime
    :param UseLatestRestorableTime: A value that is set to true to restore the DB cluster to the latest restorable backup time, and false otherwise.
            Default: false
            Constraints: Cannot be specified if RestoreToTime parameter is provided.
            
    :type UseLatestRestorableTime: boolean
    :param Port: The port number on which the new DB cluster accepts connections.
            Constraints: Value must be 1150-65535
            Default: The same port as the original DB cluster.
            
    :type Port: integer
    :param DBSubnetGroupName: The DB subnet group name to use for the new DB cluster.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            
    :type DBSubnetGroupName: string
    :param OptionGroupName: The name of the option group for the new DB cluster.
    :type OptionGroupName: string
    :param VpcSecurityGroupIds: A lst of VPC security groups that the new DB cluster belongs to.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param KmsKeyId: The KMS key identifier to use when restoring an encrypted DB cluster from an encrypted DB cluster.
            The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.
            You can restore to a new DB cluster and encrypt the new DB cluster with a KMS key that is different than the KMS key used to encrypt the source DB cluster. The new DB cluster will be encrypted with the KMS key identified by the KmsKeyId parameter.
            If you do not specify a value for the KmsKeyId parameter, then the following will occur:
            If the DB cluster is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the source DB cluster.
            If the DB cluster is not encrypted, then the restored DB cluster is not encrypted.
            If DBClusterIdentifier refers to a DB cluster that is note encrypted, then the restore request is rejected.
            
    :type KmsKeyId: string
    """
    pass


def restore_db_instance_from_db_snapshot(DBInstanceIdentifier=None, DBSnapshotIdentifier=None, DBInstanceClass=None,
                                         Port=None, AvailabilityZone=None, DBSubnetGroupName=None, MultiAZ=None,
                                         PubliclyAccessible=None, AutoMinorVersionUpgrade=None, LicenseModel=None,
                                         DBName=None, Engine=None, Iops=None, OptionGroupName=None, Tags=None,
                                         StorageType=None, TdeCredentialArn=None, TdeCredentialPassword=None,
                                         Domain=None, CopyTagsToSnapshot=None, DomainIAMRoleName=None):
    """
    :param DBInstanceIdentifier: [REQUIRED]
            Name of the DB instance to create from the DB snapshot. This parameter isn't case-sensitive.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens (1 to 15 for SQL Server)
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            Example: my-snapshot-id
            
    :type DBInstanceIdentifier: string
    :param DBSnapshotIdentifier: [REQUIRED]
            The identifier for the DB snapshot to restore from.
            Constraints:
            Must contain from 1 to 255 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            If you are restoring from a shared manual DB snapshot, the DBSnapshotIdentifier must be the ARN of the shared DB snapshot.
            
    :type DBSnapshotIdentifier: string
    :param DBInstanceClass: The compute and memory capacity of the Amazon RDS DB instance.
            Valid Values: db.t1.micro | db.m1.small | db.m1.medium | db.m1.large | db.m1.xlarge | db.m2.2xlarge | db.m2.4xlarge | db.m3.medium | db.m3.large | db.m3.xlarge | db.m3.2xlarge | db.m4.large | db.m4.xlarge | db.m4.2xlarge | db.m4.4xlarge | db.m4.10xlarge | db.r3.large | db.r3.xlarge | db.r3.2xlarge | db.r3.4xlarge | db.r3.8xlarge | db.t2.micro | db.t2.small | db.t2.medium | db.t2.large
            
    :type DBInstanceClass: string
    :param Port: The port number on which the database accepts connections.
            Default: The same port as the original DB instance
            Constraints: Value must be 1150-65535
            
    :type Port: integer
    :param AvailabilityZone: The EC2 Availability Zone that the database instance will be created in.
            Default: A random, system-chosen Availability Zone.
            Constraint: You cannot specify the AvailabilityZone parameter if the MultiAZ parameter is set to true .
            Example: us-east-1a
            
    :type AvailabilityZone: string
    :param DBSubnetGroupName: The DB subnet group name to use for the new instance.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            
    :type DBSubnetGroupName: string
    :param MultiAZ: Specifies if the DB instance is a Multi-AZ deployment.
            Constraint: You cannot specify the AvailabilityZone parameter if the MultiAZ parameter is set to true .
            
    :type MultiAZ: boolean
    :param PubliclyAccessible: Specifies the accessibility options for the DB instance. A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address. A value of false specifies an internal instance with a DNS name that resolves to a private IP address.
            Default: The default behavior varies depending on whether a VPC has been requested or not. The following list shows the default behavior in each case.
            Default VPC: true
            VPC: false
            If no DB subnet group has been specified as part of the request and the PubliclyAccessible value has not been set, the DB instance will be publicly accessible. If a specific DB subnet group has been specified as part of the request and the PubliclyAccessible value has not been set, the DB instance will be private.
            
    :type PubliclyAccessible: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor version upgrades will be applied automatically to the DB instance during the maintenance window.
    :type AutoMinorVersionUpgrade: boolean
    :param LicenseModel: License model information for the restored DB instance.
            Default: Same as source.
            Valid values: license-included | bring-your-own-license | general-public-license
            
    :type LicenseModel: string
    :param DBName: The database name for the restored DB instance.
            Note
            This parameter doesn't apply to the MySQL, PostgreSQL, or MariaDB engines.
            
    :type DBName: string
    :param Engine: The database engine to use for the new instance.
            Default: The same as source
            Constraint: Must be compatible with the engine of the source
            Valid Values: MySQL | mariadb | oracle-se1 | oracle-se | oracle-ee | sqlserver-ee | sqlserver-se | sqlserver-ex | sqlserver-web | postgres | aurora
            
    :type Engine: string
    :param Iops: Specifies the amount of provisioned IOPS for the DB instance, expressed in I/O operations per second. If this parameter is not specified, the IOPS value will be taken from the backup. If this parameter is set to 0, the new instance will be converted to a non-PIOPS instance, which will take additional time, though your DB instance will be available for connections before the conversion starts.
            Constraints: Must be an integer greater than 1000.
            SQL Server
            Setting the IOPS value for the SQL Server database engine is not supported.
            
    :type Iops: integer
    :param OptionGroupName: The name of the option group to be used for the restored DB instance.
            Permanent options, such as the TDE option for Oracle Advanced Security TDE, cannot be removed from an option group, and that option group cannot be removed from a DB instance once it is associated with a DB instance
            
    :type OptionGroupName: string
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param StorageType: Specifies the storage type to be associated with the DB instance.
            Valid values: standard | gp2 | io1
            If you specify io1 , you must also include a value for the Iops parameter.
            Default: io1 if the Iops parameter is specified; otherwise standard
            
    :type StorageType: string
    :param TdeCredentialArn: The ARN from the Key Store with which to associate the instance for TDE encryption.
    :type TdeCredentialArn: string
    :param TdeCredentialPassword: The password for the given ARN from the Key Store in order to access the device.
    :type TdeCredentialPassword: string
    :param Domain: Specify the Active Directory Domain to restore the instance in.
    :type Domain: string
    :param CopyTagsToSnapshot: True to copy all tags from the restored DB instance to snapshots of the DB instance; otherwise false. The default is false.
    :type CopyTagsToSnapshot: boolean
    :param DomainIAMRoleName: Specify the name of the IAM role to be used when making API calls to the Directory Service.
    :type DomainIAMRoleName: string
    """
    pass


def restore_db_instance_to_point_in_time(SourceDBInstanceIdentifier=None, TargetDBInstanceIdentifier=None,
                                         RestoreTime=None, UseLatestRestorableTime=None, DBInstanceClass=None,
                                         Port=None, AvailabilityZone=None, DBSubnetGroupName=None, MultiAZ=None,
                                         PubliclyAccessible=None, AutoMinorVersionUpgrade=None, LicenseModel=None,
                                         DBName=None, Engine=None, Iops=None, OptionGroupName=None,
                                         CopyTagsToSnapshot=None, Tags=None, StorageType=None, TdeCredentialArn=None,
                                         TdeCredentialPassword=None, Domain=None, DomainIAMRoleName=None):
    """
    :param SourceDBInstanceIdentifier: [REQUIRED]
            The identifier of the source DB instance from which to restore.
            Constraints:
            Must be the identifier of an existing database instance
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type SourceDBInstanceIdentifier: string
    :param TargetDBInstanceIdentifier: [REQUIRED]
            The name of the new database instance to be created.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens
            First character must be a letter
            Cannot end with a hyphen or contain two consecutive hyphens
            
    :type TargetDBInstanceIdentifier: string
    :param RestoreTime: The date and time to restore from.
            Valid Values: Value must be a time in Universal Coordinated Time (UTC) format
            Constraints:
            Must be before the latest restorable time for the DB instance
            Cannot be specified if UseLatestRestorableTime parameter is true
            Example: 2009-09-07T23:45:00Z
            
    :type RestoreTime: datetime
    :param UseLatestRestorableTime: Specifies whether (true ) or not (false ) the DB instance is restored from the latest backup time.
            Default: false
            Constraints: Cannot be specified if RestoreTime parameter is provided.
            
    :type UseLatestRestorableTime: boolean
    :param DBInstanceClass: The compute and memory capacity of the Amazon RDS DB instance.
            Valid Values: db.t1.micro | db.m1.small | db.m1.medium | db.m1.large | db.m1.xlarge | db.m2.2xlarge | db.m2.4xlarge | db.m3.medium | db.m3.large | db.m3.xlarge | db.m3.2xlarge | db.m4.large | db.m4.xlarge | db.m4.2xlarge | db.m4.4xlarge | db.m4.10xlarge | db.r3.large | db.r3.xlarge | db.r3.2xlarge | db.r3.4xlarge | db.r3.8xlarge | db.t2.micro | db.t2.small | db.t2.medium | db.t2.large
            Default: The same DBInstanceClass as the original DB instance.
            
    :type DBInstanceClass: string
    :param Port: The port number on which the database accepts connections.
            Constraints: Value must be 1150-65535
            Default: The same port as the original DB instance.
            
    :type Port: integer
    :param AvailabilityZone: The EC2 Availability Zone that the database instance will be created in.
            Default: A random, system-chosen Availability Zone.
            Constraint: You cannot specify the AvailabilityZone parameter if the MultiAZ parameter is set to true.
            Example: us-east-1a
            
    :type AvailabilityZone: string
    :param DBSubnetGroupName: The DB subnet group name to use for the new instance.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, spaces, or hyphens. Must not be default.
            Example: mySubnetgroup
            
    :type DBSubnetGroupName: string
    :param MultiAZ: Specifies if the DB instance is a Multi-AZ deployment.
            Constraint: You cannot specify the AvailabilityZone parameter if the MultiAZ parameter is set to true .
            
    :type MultiAZ: boolean
    :param PubliclyAccessible: Specifies the accessibility options for the DB instance. A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address. A value of false specifies an internal instance with a DNS name that resolves to a private IP address.
            Default: The default behavior varies depending on whether a VPC has been requested or not. The following list shows the default behavior in each case.
            Default VPC: true
            VPC: false
            If no DB subnet group has been specified as part of the request and the PubliclyAccessible value has not been set, the DB instance will be publicly accessible. If a specific DB subnet group has been specified as part of the request and the PubliclyAccessible value has not been set, the DB instance will be private.
            
    :type PubliclyAccessible: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor version upgrades will be applied automatically to the DB instance during the maintenance window.
    :type AutoMinorVersionUpgrade: boolean
    :param LicenseModel: License model information for the restored DB instance.
            Default: Same as source.
            Valid values: license-included | bring-your-own-license | general-public-license
            
    :type LicenseModel: string
    :param DBName: The database name for the restored DB instance.
            Note
            This parameter is not used for the MySQL or MariaDB engines.
            
    :type DBName: string
    :param Engine: The database engine to use for the new instance.
            Default: The same as source
            Constraint: Must be compatible with the engine of the source
            Valid Values: MySQL | mariadb | oracle-se1 | oracle-se | oracle-ee | sqlserver-ee | sqlserver-se | sqlserver-ex | sqlserver-web | postgres | aurora
            
    :type Engine: string
    :param Iops: The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.
            Constraints: Must be an integer greater than 1000.
            SQL Server
            Setting the IOPS value for the SQL Server database engine is not supported.
            
    :type Iops: integer
    :param OptionGroupName: The name of the option group to be used for the restored DB instance.
            Permanent options, such as the TDE option for Oracle Advanced Security TDE, cannot be removed from an option group, and that option group cannot be removed from a DB instance once it is associated with a DB instance
            
    :type OptionGroupName: string
    :param CopyTagsToSnapshot: True to copy all tags from the restored DB instance to snapshots of the DB instance; otherwise false. The default is false.
    :type CopyTagsToSnapshot: boolean
    :param Tags: A list of tags.
            (dict) --Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param StorageType: Specifies the storage type to be associated with the DB instance.
            Valid values: standard | gp2 | io1
            If you specify io1 , you must also include a value for the Iops parameter.
            Default: io1 if the Iops parameter is specified; otherwise standard
            
    :type StorageType: string
    :param TdeCredentialArn: The ARN from the Key Store with which to associate the instance for TDE encryption.
    :type TdeCredentialArn: string
    :param TdeCredentialPassword: The password for the given ARN from the Key Store in order to access the device.
    :type TdeCredentialPassword: string
    :param Domain: Specify the Active Directory Domain to restore the instance in.
    :type Domain: string
    :param DomainIAMRoleName: Specify the name of the IAM role to be used when making API calls to the Directory Service.
    :type DomainIAMRoleName: string
    """
    pass


def revoke_db_security_group_ingress(DBSecurityGroupName=None, CIDRIP=None, EC2SecurityGroupName=None,
                                     EC2SecurityGroupId=None, EC2SecurityGroupOwnerId=None):
    """
    :param DBSecurityGroupName: [REQUIRED]
            The name of the DB security group to revoke ingress from.
            
    :type DBSecurityGroupName: string
    :param CIDRIP: The IP range to revoke access from. Must be a valid CIDR range. If CIDRIP is specified, EC2SecurityGroupName , EC2SecurityGroupId and EC2SecurityGroupOwnerId cannot be provided.
    :type CIDRIP: string
    :param EC2SecurityGroupName: The name of the EC2 security group to revoke access from. For VPC DB security groups, EC2SecurityGroupId must be provided. Otherwise, EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId must be provided.
    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupId: The id of the EC2 security group to revoke access from. For VPC DB security groups, EC2SecurityGroupId must be provided. Otherwise, EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId must be provided.
    :type EC2SecurityGroupId: string
    :param EC2SecurityGroupOwnerId: The AWS Account Number of the owner of the EC2 security group specified in the EC2SecurityGroupName parameter. The AWS Access Key ID is not an acceptable value. For VPC DB security groups, EC2SecurityGroupId must be provided. Otherwise, EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId must be provided.
    :type EC2SecurityGroupOwnerId: string
    """
    pass
