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
    Adds metadata tags to an Amazon DocumentDB resource. You can use these tags with cost allocation reporting to track costs that are associated with Amazon DocumentDB resources. or in a Condition statement in an AWS Identity and Access Management (IAM) policy for Amazon DocumentDB.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ResourceName: [REQUIRED]\nThe Amazon DocumentDB resource that the tags are added to. This value is an Amazon Resource Name (ARN).\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to be assigned to the Amazon DocumentDB resource.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :returns: 
    DocDB.Client.exceptions.DBInstanceNotFoundFault
    DocDB.Client.exceptions.DBSnapshotNotFoundFault
    DocDB.Client.exceptions.DBClusterNotFoundFault
    
    """
    pass

def apply_pending_maintenance_action(ResourceIdentifier=None, ApplyAction=None, OptInType=None):
    """
    Applies a pending maintenance action to a resource (for example, to a DB instance).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.apply_pending_maintenance_action(
        ResourceIdentifier='string',
        ApplyAction='string',
        OptInType='string'
    )
    
    
    :type ResourceIdentifier: string
    :param ResourceIdentifier: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to.\n

    :type ApplyAction: string
    :param ApplyAction: [REQUIRED]\nThe pending maintenance action to apply to this resource.\nValid values: system-update , db-upgrade\n

    :type OptInType: string
    :param OptInType: [REQUIRED]\nA value that specifies the type of opt-in request or undoes an opt-in request. An opt-in request of type immediate can\'t be undone.\nValid values:\n\nimmediate - Apply the maintenance action immediately.\nnext-maintenance - Apply the maintenance action during the next maintenance window for the resource.\nundo-opt-in - Cancel any existing next-maintenance opt-in requests.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourcePendingMaintenanceActions': {
        'ResourceIdentifier': 'string',
        'PendingMaintenanceActionDetails': [
            {
                'Action': 'string',
                'AutoAppliedAfterDate': datetime(2015, 1, 1),
                'ForcedApplyDate': datetime(2015, 1, 1),
                'OptInStatus': 'string',
                'CurrentApplyDate': datetime(2015, 1, 1),
                'Description': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ResourcePendingMaintenanceActions (dict) --
Represents the output of  ApplyPendingMaintenanceAction .

ResourceIdentifier (string) --
The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.

PendingMaintenanceActionDetails (list) --
A list that provides details about the pending maintenance actions for the resource.

(dict) --
Provides information about a pending maintenance action for a resource.

Action (string) --
The type of pending maintenance action that is available for the resource.

AutoAppliedAfterDate (datetime) --
The date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any next-maintenance opt-in requests are ignored.

ForcedApplyDate (datetime) --
The date when the maintenance action is automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any immediate opt-in requests are ignored.

OptInStatus (string) --
Indicates the type of opt-in request that has been received for the resource.

CurrentApplyDate (datetime) --
The effective date when the pending maintenance action is applied to the resource.

Description (string) --
A description providing more detail about the maintenance action.













Exceptions

DocDB.Client.exceptions.ResourceNotFoundFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.InvalidDBInstanceStateFault


    :return: {
        'ResourcePendingMaintenanceActions': {
            'ResourceIdentifier': 'string',
            'PendingMaintenanceActionDetails': [
                {
                    'Action': 'string',
                    'AutoAppliedAfterDate': datetime(2015, 1, 1),
                    'ForcedApplyDate': datetime(2015, 1, 1),
                    'OptInStatus': 'string',
                    'CurrentApplyDate': datetime(2015, 1, 1),
                    'Description': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    DocDB.Client.exceptions.ResourceNotFoundFault
    DocDB.Client.exceptions.InvalidDBClusterStateFault
    DocDB.Client.exceptions.InvalidDBInstanceStateFault
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def copy_db_cluster_parameter_group(SourceDBClusterParameterGroupIdentifier=None, TargetDBClusterParameterGroupIdentifier=None, TargetDBClusterParameterGroupDescription=None, Tags=None):
    """
    Copies the specified cluster parameter group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.copy_db_cluster_parameter_group(
        SourceDBClusterParameterGroupIdentifier='string',
        TargetDBClusterParameterGroupIdentifier='string',
        TargetDBClusterParameterGroupDescription='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SourceDBClusterParameterGroupIdentifier: string
    :param SourceDBClusterParameterGroupIdentifier: [REQUIRED]\nThe identifier or Amazon Resource Name (ARN) for the source cluster parameter group.\nConstraints:\n\nMust specify a valid cluster parameter group.\nIf the source cluster parameter group is in the same AWS Region as the copy, specify a valid parameter group identifier; for example, my-db-cluster-param-group , or a valid ARN.\nIf the source parameter group is in a different AWS Region than the copy, specify a valid cluster parameter group ARN; for example, arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1 .\n\n

    :type TargetDBClusterParameterGroupIdentifier: string
    :param TargetDBClusterParameterGroupIdentifier: [REQUIRED]\nThe identifier for the copied cluster parameter group.\nConstraints:\n\nCannot be null, empty, or blank.\nMust contain from 1 to 255 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-cluster-param-group1\n

    :type TargetDBClusterParameterGroupDescription: string
    :param TargetDBClusterParameterGroupDescription: [REQUIRED]\nA description for the copied cluster parameter group.\n

    :type Tags: list
    :param Tags: The tags that are to be assigned to the parameter group.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBClusterParameterGroup': {
        'DBClusterParameterGroupName': 'string',
        'DBParameterGroupFamily': 'string',
        'Description': 'string',
        'DBClusterParameterGroupArn': 'string'
    }
}


Response Structure

(dict) --

DBClusterParameterGroup (dict) --
Detailed information about a cluster parameter group.

DBClusterParameterGroupName (string) --
Provides the name of the cluster parameter group.

DBParameterGroupFamily (string) --
Provides the name of the parameter group family that this cluster parameter group is compatible with.

Description (string) --
Provides the customer-specified description for this cluster parameter group.

DBClusterParameterGroupArn (string) --
The Amazon Resource Name (ARN) for the cluster parameter group.









Exceptions

DocDB.Client.exceptions.DBParameterGroupNotFoundFault
DocDB.Client.exceptions.DBParameterGroupQuotaExceededFault
DocDB.Client.exceptions.DBParameterGroupAlreadyExistsFault


    :return: {
        'DBClusterParameterGroup': {
            'DBClusterParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBClusterParameterGroupArn': 'string'
        }
    }
    
    
    :returns: 
    DocDB.Client.exceptions.DBParameterGroupNotFoundFault
    DocDB.Client.exceptions.DBParameterGroupQuotaExceededFault
    DocDB.Client.exceptions.DBParameterGroupAlreadyExistsFault
    
    """
    pass

def copy_db_cluster_snapshot(SourceDBClusterSnapshotIdentifier=None, TargetDBClusterSnapshotIdentifier=None, KmsKeyId=None, PreSignedUrl=None, CopyTags=None, Tags=None):
    """
    Copies a snapshot of a cluster.
    To copy a cluster snapshot from a shared manual cluster snapshot, SourceDBClusterSnapshotIdentifier must be the Amazon Resource Name (ARN) of the shared cluster snapshot.
    To cancel the copy operation after it is in progress, delete the target cluster snapshot identified by TargetDBClusterSnapshotIdentifier while that DB cluster snapshot is in the copying status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.copy_db_cluster_snapshot(
        SourceDBClusterSnapshotIdentifier='string',
        TargetDBClusterSnapshotIdentifier='string',
        KmsKeyId='string',
        PreSignedUrl='string',
        CopyTags=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SourceDBClusterSnapshotIdentifier: string
    :param SourceDBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier of the cluster snapshot to copy. This parameter is not case sensitive.\nYou can\'t copy an encrypted, shared cluster snapshot from one AWS Region to another.\nConstraints:\n\nMust specify a valid system snapshot in the 'available' state.\nIf the source snapshot is in the same AWS Region as the copy, specify a valid snapshot identifier.\nIf the source snapshot is in a different AWS Region than the copy, specify a valid cluster snapshot ARN.\n\nExample: my-cluster-snapshot1\n

    :type TargetDBClusterSnapshotIdentifier: string
    :param TargetDBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier of the new cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-cluster-snapshot2\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key ID for an encrypted cluster snapshot. The AWS KMS key ID is the Amazon Resource Name (ARN), AWS KMS key identifier, or the AWS KMS key alias for the AWS KMS encryption key.\nIf you copy an encrypted cluster snapshot from your AWS account, you can specify a value for KmsKeyId to encrypt the copy with a new AWS KMS encryption key. If you don\'t specify a value for KmsKeyId , then the copy of the cluster snapshot is encrypted with the same AWS KMS key as the source cluster snapshot.\nIf you copy an encrypted cluster snapshot that is shared from another AWS account, then you must specify a value for KmsKeyId .\nTo copy an encrypted cluster snapshot to another AWS Region, set KmsKeyId to the AWS KMS key ID that you want to use to encrypt the copy of the cluster snapshot in the destination Region. AWS KMS encryption keys are specific to the AWS Region that they are created in, and you can\'t use encryption keys from one Region in another Region.\nIf you copy an unencrypted cluster snapshot and specify a value for the KmsKeyId parameter, an error is returned.\n

    :type PreSignedUrl: string
    :param PreSignedUrl: The URL that contains a Signature Version 4 signed request for the CopyDBClusterSnapshot API action in the AWS Region that contains the source cluster snapshot to copy. You must use the PreSignedUrl parameter when copying an encrypted cluster snapshot from another AWS Region.\nThe presigned URL must be a valid request for the CopyDBSClusterSnapshot API action that can be executed in the source AWS Region that contains the encrypted DB cluster snapshot to be copied. The presigned URL request must contain the following parameter values:\n\nKmsKeyId - The AWS KMS key identifier for the key to use to encrypt the copy of the cluster snapshot in the destination AWS Region. This is the same identifier for both the CopyDBClusterSnapshot action that is called in the destination AWS Region, and the action contained in the presigned URL.\nDestinationRegion - The name of the AWS Region that the DB cluster snapshot will be created in.\nSourceDBClusterSnapshotIdentifier - The cluster snapshot identifier for the encrypted cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source AWS Region. For example, if you are copying an encrypted cluster snapshot from the us-west-2 AWS Region, then your SourceDBClusterSnapshotIdentifier looks like the following example: arn:aws:rds:us-west-2:123456789012:cluster-snapshot:my-cluster-snapshot-20161115 .\n\n

    :type CopyTags: boolean
    :param CopyTags: Set to true to copy all tags from the source cluster snapshot to the target cluster snapshot, and otherwise false . The default is false .

    :type Tags: list
    :param Tags: The tags to be assigned to the cluster snapshot.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBClusterSnapshot': {
        'AvailabilityZones': [
            'string',
        ],
        'DBClusterSnapshotIdentifier': 'string',
        'DBClusterIdentifier': 'string',
        'SnapshotCreateTime': datetime(2015, 1, 1),
        'Engine': 'string',
        'Status': 'string',
        'Port': 123,
        'VpcId': 'string',
        'ClusterCreateTime': datetime(2015, 1, 1),
        'MasterUsername': 'string',
        'EngineVersion': 'string',
        'SnapshotType': 'string',
        'PercentProgress': 123,
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DBClusterSnapshotArn': 'string',
        'SourceDBClusterSnapshotArn': 'string'
    }
}


Response Structure

(dict) --

DBClusterSnapshot (dict) --
Detailed information about a cluster snapshot.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster snapshot can be restored in.

(string) --


DBClusterSnapshotIdentifier (string) --
Specifies the identifier for the cluster snapshot.

DBClusterIdentifier (string) --
Specifies the cluster identifier of the cluster that this cluster snapshot was created from.

SnapshotCreateTime (datetime) --
Provides the time when the snapshot was taken, in UTC.

Engine (string) --
Specifies the name of the database engine.

Status (string) --
Specifies the status of this cluster snapshot.

Port (integer) --
Specifies the port that the cluster was listening on at the time of the snapshot.

VpcId (string) --
Provides the virtual private cloud (VPC) ID that is associated with the cluster snapshot.

ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

MasterUsername (string) --
Provides the master user name for the cluster snapshot.

EngineVersion (string) --
Provides the version of the database engine for this cluster snapshot.

SnapshotType (string) --
Provides the type of the cluster snapshot.

PercentProgress (integer) --
Specifies the percentage of the estimated data that has been transferred.

StorageEncrypted (boolean) --
Specifies whether the cluster snapshot is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster snapshot.

DBClusterSnapshotArn (string) --
The Amazon Resource Name (ARN) for the cluster snapshot.

SourceDBClusterSnapshotArn (string) --
If the cluster snapshot was copied from a source cluster snapshot, the ARN for the source cluster snapshot; otherwise, a null value.









Exceptions

DocDB.Client.exceptions.DBClusterSnapshotAlreadyExistsFault
DocDB.Client.exceptions.DBClusterSnapshotNotFoundFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.InvalidDBClusterSnapshotStateFault
DocDB.Client.exceptions.SnapshotQuotaExceededFault
DocDB.Client.exceptions.KMSKeyNotAccessibleFault


    :return: {
        'DBClusterSnapshot': {
            'AvailabilityZones': [
                'string',
            ],
            'DBClusterSnapshotIdentifier': 'string',
            'DBClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Engine': 'string',
            'Status': 'string',
            'Port': 123,
            'VpcId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'EngineVersion': 'string',
            'SnapshotType': 'string',
            'PercentProgress': 123,
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_db_cluster(AvailabilityZones=None, BackupRetentionPeriod=None, DBClusterIdentifier=None, DBClusterParameterGroupName=None, VpcSecurityGroupIds=None, DBSubnetGroupName=None, Engine=None, EngineVersion=None, Port=None, MasterUsername=None, MasterUserPassword=None, PreferredBackupWindow=None, PreferredMaintenanceWindow=None, Tags=None, StorageEncrypted=None, KmsKeyId=None, EnableCloudwatchLogsExports=None, DeletionProtection=None):
    """
    Creates a new Amazon DocumentDB cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_db_cluster(
        AvailabilityZones=[
            'string',
        ],
        BackupRetentionPeriod=123,
        DBClusterIdentifier='string',
        DBClusterParameterGroupName='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        DBSubnetGroupName='string',
        Engine='string',
        EngineVersion='string',
        Port=123,
        MasterUsername='string',
        MasterUserPassword='string',
        PreferredBackupWindow='string',
        PreferredMaintenanceWindow='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        StorageEncrypted=True|False,
        KmsKeyId='string',
        EnableCloudwatchLogsExports=[
            'string',
        ],
        DeletionProtection=True|False
    )
    
    
    :type AvailabilityZones: list
    :param AvailabilityZones: A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.\n\n(string) --\n\n

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: The number of days for which automated backups are retained. You must specify a minimum value of 1.\nDefault: 1\nConstraints:\n\nMust be a value from 1 to 35.\n\n

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe cluster identifier. This parameter is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-cluster\n

    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of the cluster parameter group to associate with this cluster.

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to associate with this cluster.\n\n(string) --\n\n

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: A subnet group to associate with this cluster.\nConstraints: Must match the name of an existing DBSubnetGroup . Must not be default.\nExample: mySubnetgroup\n

    :type Engine: string
    :param Engine: [REQUIRED]\nThe name of the database engine to be used for this cluster.\nValid values: docdb\n

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine to use.

    :type Port: integer
    :param Port: The port number on which the instances in the cluster accept connections.

    :type MasterUsername: string
    :param MasterUsername: [REQUIRED]\nThe name of the master user for the cluster.\nConstraints:\n\nMust be from 1 to 63 letters or numbers.\nThe first character must be a letter.\nCannot be a reserved word for the chosen database engine.\n\n

    :type MasterUserPassword: string
    :param MasterUserPassword: [REQUIRED]\nThe password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ('), or the 'at' symbol (@).\nConstraints: Must contain from 8 to 100 characters.\n

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region.\nConstraints:\n\nMust be in the format hh24:mi-hh24:mi .\nMust be in Universal Coordinated Time (UTC).\nMust not conflict with the preferred maintenance window.\nMust be at least 30 minutes.\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).\nFormat: ddd:hh24:mi-ddd:hh24:mi\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.\nValid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun\nConstraints: Minimum 30-minute window.\n

    :type Tags: list
    :param Tags: The tags to be assigned to the cluster.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type StorageEncrypted: boolean
    :param StorageEncrypted: Specifies whether the cluster is encrypted.

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier for an encrypted cluster.\nThe AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are creating a cluster using the same AWS account that owns the AWS KMS encryption key that is used to encrypt the new cluster, you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.\nIf an encryption key is not specified in KmsKeyId :\n\nIf ReplicationSourceIdentifier identifies an encrypted source, then Amazon DocumentDB uses the encryption key that is used to encrypt the source. Otherwise, Amazon DocumentDB uses your default encryption key.\nIf the StorageEncrypted parameter is true and ReplicationSourceIdentifier is not specified, Amazon DocumentDB uses your default encryption key.\n\nAWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.\nIf you create a replica of an encrypted cluster in another AWS Region, you must set KmsKeyId to a KMS key ID that is valid in the destination AWS Region. This key is used to encrypt the replica in that AWS Region.\n

    :type EnableCloudwatchLogsExports: list
    :param EnableCloudwatchLogsExports: A list of log types that need to be enabled for exporting to Amazon CloudWatch Logs.\n\n(string) --\n\n

    :type DeletionProtection: boolean
    :param DeletionProtection: Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.

    :rtype: dict

ReturnsResponse Syntax
{
    'DBCluster': {
        'AvailabilityZones': [
            'string',
        ],
        'BackupRetentionPeriod': 123,
        'DBClusterIdentifier': 'string',
        'DBClusterParameterGroup': 'string',
        'DBSubnetGroup': 'string',
        'Status': 'string',
        'PercentProgress': 'string',
        'EarliestRestorableTime': datetime(2015, 1, 1),
        'Endpoint': 'string',
        'ReaderEndpoint': 'string',
        'MultiAZ': True|False,
        'Engine': 'string',
        'EngineVersion': 'string',
        'LatestRestorableTime': datetime(2015, 1, 1),
        'Port': 123,
        'MasterUsername': 'string',
        'PreferredBackupWindow': 'string',
        'PreferredMaintenanceWindow': 'string',
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
        ],
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBCluster (dict) --
Detailed information about a cluster.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier (string) --
Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup (string) --
Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
The earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint (string) --
The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master user name for the cluster.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

DBClusterMembers (list) --
Provides the list of instances that make up the cluster.

(dict) --
Contains information about an instance that is part of a cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the cluster.

IsClusterWriter (boolean) --
A value that is true if the cluster member is the primary instance for the cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. IAM roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the cluster. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB cluster.
INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.






ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.









Exceptions

DocDB.Client.exceptions.DBClusterAlreadyExistsFault
DocDB.Client.exceptions.InsufficientStorageClusterCapacityFault
DocDB.Client.exceptions.DBClusterQuotaExceededFault
DocDB.Client.exceptions.StorageQuotaExceededFault
DocDB.Client.exceptions.DBSubnetGroupNotFoundFault
DocDB.Client.exceptions.InvalidVPCNetworkStateFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.InvalidDBSubnetGroupStateFault
DocDB.Client.exceptions.InvalidSubnet
DocDB.Client.exceptions.InvalidDBInstanceStateFault
DocDB.Client.exceptions.DBClusterParameterGroupNotFoundFault
DocDB.Client.exceptions.KMSKeyNotAccessibleFault
DocDB.Client.exceptions.DBClusterNotFoundFault
DocDB.Client.exceptions.DBInstanceNotFoundFault
DocDB.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs


    :return: {
        'DBCluster': {
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
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
            ],
            'ClusterCreateTime': datetime(2015, 1, 1),
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_db_cluster_parameter_group(DBClusterParameterGroupName=None, DBParameterGroupFamily=None, Description=None, Tags=None):
    """
    Creates a new cluster parameter group.
    Parameters in a cluster parameter group apply to all of the instances in a DB cluster.
    A cluster parameter group is initially created with the default parameters for the database engine used by instances in the cluster. To provide custom values for any of the parameters, you must modify the group after you create it. After you create a DB cluster parameter group, you must associate it with your cluster. For the new DB cluster parameter group and associated settings to take effect, you must then reboot the instances in the cluster without failover.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_db_cluster_parameter_group(
        DBClusterParameterGroupName='string',
        DBParameterGroupFamily='string',
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of the cluster parameter group.\nConstraints:\n\nMust not match the name of an existing DBClusterParameterGroup .\n\n\nNote\nThis value is stored as a lowercase string.\n\n

    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: [REQUIRED]\nThe cluster parameter group family name.\n

    :type Description: string
    :param Description: [REQUIRED]\nThe description for the cluster parameter group.\n

    :type Tags: list
    :param Tags: The tags to be assigned to the cluster parameter group.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBClusterParameterGroup': {
        'DBClusterParameterGroupName': 'string',
        'DBParameterGroupFamily': 'string',
        'Description': 'string',
        'DBClusterParameterGroupArn': 'string'
    }
}


Response Structure

(dict) --

DBClusterParameterGroup (dict) --
Detailed information about a cluster parameter group.

DBClusterParameterGroupName (string) --
Provides the name of the cluster parameter group.

DBParameterGroupFamily (string) --
Provides the name of the parameter group family that this cluster parameter group is compatible with.

Description (string) --
Provides the customer-specified description for this cluster parameter group.

DBClusterParameterGroupArn (string) --
The Amazon Resource Name (ARN) for the cluster parameter group.









Exceptions

DocDB.Client.exceptions.DBParameterGroupQuotaExceededFault
DocDB.Client.exceptions.DBParameterGroupAlreadyExistsFault


    :return: {
        'DBClusterParameterGroup': {
            'DBClusterParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBClusterParameterGroupArn': 'string'
        }
    }
    
    
    :returns: 
    DocDB.Client.exceptions.DBParameterGroupQuotaExceededFault
    DocDB.Client.exceptions.DBParameterGroupAlreadyExistsFault
    
    """
    pass

def create_db_cluster_snapshot(DBClusterSnapshotIdentifier=None, DBClusterIdentifier=None, Tags=None):
    """
    Creates a snapshot of a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_db_cluster_snapshot(
        DBClusterSnapshotIdentifier='string',
        DBClusterIdentifier='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier of the cluster snapshot. This parameter is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-cluster-snapshot1\n

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe identifier of the cluster to create a snapshot for. This parameter is not case sensitive.\nConstraints:\n\nMust match the identifier of an existing DBCluster .\n\nExample: my-cluster\n

    :type Tags: list
    :param Tags: The tags to be assigned to the cluster snapshot.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBClusterSnapshot': {
        'AvailabilityZones': [
            'string',
        ],
        'DBClusterSnapshotIdentifier': 'string',
        'DBClusterIdentifier': 'string',
        'SnapshotCreateTime': datetime(2015, 1, 1),
        'Engine': 'string',
        'Status': 'string',
        'Port': 123,
        'VpcId': 'string',
        'ClusterCreateTime': datetime(2015, 1, 1),
        'MasterUsername': 'string',
        'EngineVersion': 'string',
        'SnapshotType': 'string',
        'PercentProgress': 123,
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DBClusterSnapshotArn': 'string',
        'SourceDBClusterSnapshotArn': 'string'
    }
}


Response Structure

(dict) --

DBClusterSnapshot (dict) --
Detailed information about a cluster snapshot.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster snapshot can be restored in.

(string) --


DBClusterSnapshotIdentifier (string) --
Specifies the identifier for the cluster snapshot.

DBClusterIdentifier (string) --
Specifies the cluster identifier of the cluster that this cluster snapshot was created from.

SnapshotCreateTime (datetime) --
Provides the time when the snapshot was taken, in UTC.

Engine (string) --
Specifies the name of the database engine.

Status (string) --
Specifies the status of this cluster snapshot.

Port (integer) --
Specifies the port that the cluster was listening on at the time of the snapshot.

VpcId (string) --
Provides the virtual private cloud (VPC) ID that is associated with the cluster snapshot.

ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

MasterUsername (string) --
Provides the master user name for the cluster snapshot.

EngineVersion (string) --
Provides the version of the database engine for this cluster snapshot.

SnapshotType (string) --
Provides the type of the cluster snapshot.

PercentProgress (integer) --
Specifies the percentage of the estimated data that has been transferred.

StorageEncrypted (boolean) --
Specifies whether the cluster snapshot is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster snapshot.

DBClusterSnapshotArn (string) --
The Amazon Resource Name (ARN) for the cluster snapshot.

SourceDBClusterSnapshotArn (string) --
If the cluster snapshot was copied from a source cluster snapshot, the ARN for the source cluster snapshot; otherwise, a null value.









Exceptions

DocDB.Client.exceptions.DBClusterSnapshotAlreadyExistsFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.DBClusterNotFoundFault
DocDB.Client.exceptions.SnapshotQuotaExceededFault
DocDB.Client.exceptions.InvalidDBClusterSnapshotStateFault


    :return: {
        'DBClusterSnapshot': {
            'AvailabilityZones': [
                'string',
            ],
            'DBClusterSnapshotIdentifier': 'string',
            'DBClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Engine': 'string',
            'Status': 'string',
            'Port': 123,
            'VpcId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'EngineVersion': 'string',
            'SnapshotType': 'string',
            'PercentProgress': 123,
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_db_instance(DBInstanceIdentifier=None, DBInstanceClass=None, Engine=None, AvailabilityZone=None, PreferredMaintenanceWindow=None, AutoMinorVersionUpgrade=None, Tags=None, DBClusterIdentifier=None, PromotionTier=None):
    """
    Creates a new instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_db_instance(
        DBInstanceIdentifier='string',
        DBInstanceClass='string',
        Engine='string',
        AvailabilityZone='string',
        PreferredMaintenanceWindow='string',
        AutoMinorVersionUpgrade=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        DBClusterIdentifier='string',
        PromotionTier=123
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]\nThe instance identifier. This parameter is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: mydbinstance\n

    :type DBInstanceClass: string
    :param DBInstanceClass: [REQUIRED]\nThe compute and memory capacity of the instance; for example, db.r5.large .\n

    :type Engine: string
    :param Engine: [REQUIRED]\nThe name of the database engine to be used for this instance.\nValid value: docdb\n

    :type AvailabilityZone: string
    :param AvailabilityZone: The Amazon EC2 Availability Zone that the instance is created in.\nDefault: A random, system-chosen Availability Zone in the endpoint\'s AWS Region.\nExample: us-east-1d\nConstraint: The AvailabilityZone parameter can\'t be specified if the MultiAZ parameter is set to true . The specified Availability Zone must be in the same AWS Region as the current endpoint.\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).\nFormat: ddd:hh24:mi-ddd:hh24:mi\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.\nValid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun\nConstraints: Minimum 30-minute window.\n

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor engine upgrades are applied automatically to the instance during the maintenance window.\nDefault: true\n

    :type Tags: list
    :param Tags: The tags to be assigned to the instance. You can assign up to 10 tags to an instance.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe identifier of the cluster that the instance will belong to.\n

    :type PromotionTier: integer
    :param PromotionTier: A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.\nDefault: 1\nValid values: 0-15\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBInstance': {
        'DBInstanceIdentifier': 'string',
        'DBInstanceClass': 'string',
        'Engine': 'string',
        'DBInstanceStatus': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123,
            'HostedZoneId': 'string'
        },
        'InstanceCreateTime': datetime(2015, 1, 1),
        'PreferredBackupWindow': 'string',
        'BackupRetentionPeriod': 123,
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'AvailabilityZone': 'string',
        'DBSubnetGroup': {
            'DBSubnetGroupName': 'string',
            'DBSubnetGroupDescription': 'string',
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
            'DBSubnetGroupArn': 'string'
        },
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'DBInstanceClass': 'string',
            'AllocatedStorage': 123,
            'MasterUserPassword': 'string',
            'Port': 123,
            'BackupRetentionPeriod': 123,
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'LicenseModel': 'string',
            'Iops': 123,
            'DBInstanceIdentifier': 'string',
            'StorageType': 'string',
            'CACertificateIdentifier': 'string',
            'DBSubnetGroupName': 'string',
            'PendingCloudwatchLogsExports': {
                'LogTypesToEnable': [
                    'string',
                ],
                'LogTypesToDisable': [
                    'string',
                ]
            }
        },
        'LatestRestorableTime': datetime(2015, 1, 1),
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'PubliclyAccessible': True|False,
        'StatusInfos': [
            {
                'StatusType': 'string',
                'Normal': True|False,
                'Status': 'string',
                'Message': 'string'
            },
        ],
        'DBClusterIdentifier': 'string',
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DbiResourceId': 'string',
        'CACertificateIdentifier': 'string',
        'PromotionTier': 123,
        'DBInstanceArn': 'string',
        'EnabledCloudwatchLogsExports': [
            'string',
        ]
    }
}


Response Structure

(dict) --

DBInstance (dict) --
Detailed information about an instance.

DBInstanceIdentifier (string) --
Contains a user-provided database identifier. This identifier is the unique key that identifies an instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the instance.

Engine (string) --
Provides the name of the database engine to be used for this instance.

DBInstanceStatus (string) --
Specifies the current state of this database.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



InstanceCreateTime (datetime) --
Provides the date and time that the instance was created.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

VpcSecurityGroups (list) --
Provides a list of VPC security group elements that the instance belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





AvailabilityZone (string) --
Specifies the name of the Availability Zone that the instance is located in.

DBSubnetGroup (dict) --
Specifies information on the subnet group that is associated with the instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --
The name of the subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the subnet group.

VpcId (string) --
Provides the virtual private cloud (VPC) ID of the subnet group.

SubnetGroupStatus (string) --
Provides the status of the subnet group.

Subnets (list) --
Detailed information about one or more subnets within a subnet group.

(dict) --
Detailed information about a subnet.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the Availability Zone for the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --
Specifies that changes to the instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --
Contains the new DBInstanceClass for the instance that will be applied or is currently being applied.

AllocatedStorage (integer) --
Contains the new AllocatedStorage size for then instance that will be applied or is currently being applied.

MasterUserPassword (string) --
Contains the pending or currently in-progress change of the master credentials for the instance.

Port (integer) --
Specifies the pending port for the instance.

BackupRetentionPeriod (integer) --
Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --
Indicates that the Single-AZ instance is to change to a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

LicenseModel (string) --
The license model for the instance.
Valid values: license-included , bring-your-own-license , general-public-license

Iops (integer) --
Specifies the new Provisioned IOPS value for the instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --
Contains the new DBInstanceIdentifier for the instance that will be applied or is currently being applied.

StorageType (string) --
Specifies the storage type to be associated with the instance.

CACertificateIdentifier (string) --
Specifies the identifier of the certificate authority (CA) certificate for the DB instance.

DBSubnetGroupName (string) --
The new subnet group for the instance.

PendingCloudwatchLogsExports (dict) --
A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.

LogTypesToEnable (list) --
Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --
Log types that are in the process of being enabled. After they are enabled, these log types are exported to Amazon CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

EngineVersion (string) --
Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --
Indicates that minor version patches are applied automatically.

PubliclyAccessible (boolean) --
Not supported. Amazon DocumentDB does not currently support public endpoints. The value of PubliclyAccessible is always false .

StatusInfos (list) --
The status of a read replica. If the instance is not a read replica, this is blank.

(dict) --
Provides a list of status information for an instance.

StatusType (string) --
This value is currently "read replication ."

Normal (boolean) --
A Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --
Status of the instance. For a StatusType of read replica, the values can be replicating , error, stopped , or terminated .

Message (string) --
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





DBClusterIdentifier (string) --
Contains the name of the cluster that the instance is a member of if the instance is a member of a cluster.

StorageEncrypted (boolean) --
Specifies whether or not the instance is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted instance.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the instance is accessed.

CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --
The Amazon Resource Name (ARN) for the instance.

EnabledCloudwatchLogsExports (list) --
A list of log types that this instance is configured to export to Amazon CloudWatch Logs.

(string) --










Exceptions

DocDB.Client.exceptions.DBInstanceAlreadyExistsFault
DocDB.Client.exceptions.InsufficientDBInstanceCapacityFault
DocDB.Client.exceptions.DBParameterGroupNotFoundFault
DocDB.Client.exceptions.DBSecurityGroupNotFoundFault
DocDB.Client.exceptions.InstanceQuotaExceededFault
DocDB.Client.exceptions.StorageQuotaExceededFault
DocDB.Client.exceptions.DBSubnetGroupNotFoundFault
DocDB.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.InvalidSubnet
DocDB.Client.exceptions.InvalidVPCNetworkStateFault
DocDB.Client.exceptions.DBClusterNotFoundFault
DocDB.Client.exceptions.StorageTypeNotSupportedFault
DocDB.Client.exceptions.AuthorizationNotFoundFault
DocDB.Client.exceptions.KMSKeyNotAccessibleFault


    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                'DBSubnetGroupArn': 'string'
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'DBInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MasterUserPassword': 'string',
                'Port': 123,
                'BackupRetentionPeriod': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'Iops': 123,
                'DBInstanceIdentifier': 'string',
                'StorageType': 'string',
                'CACertificateIdentifier': 'string',
                'DBSubnetGroupName': 'string',
                'PendingCloudwatchLogsExports': {
                    'LogTypesToEnable': [
                        'string',
                    ],
                    'LogTypesToDisable': [
                        'string',
                    ]
                }
            },
            'LatestRestorableTime': datetime(2015, 1, 1),
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_db_subnet_group(DBSubnetGroupName=None, DBSubnetGroupDescription=None, SubnetIds=None, Tags=None):
    """
    Creates a new subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the AWS Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_db_subnet_group(
        DBSubnetGroupName='string',
        DBSubnetGroupDescription='string',
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
    
    
    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: [REQUIRED]\nThe name for the subnet group. This value is stored as a lowercase string.\nConstraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.\nExample: mySubnetgroup\n

    :type DBSubnetGroupDescription: string
    :param DBSubnetGroupDescription: [REQUIRED]\nThe description for the subnet group.\n

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nThe Amazon EC2 subnet IDs for the subnet group.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: The tags to be assigned to the subnet group.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBSubnetGroup': {
        'DBSubnetGroupName': 'string',
        'DBSubnetGroupDescription': 'string',
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
        'DBSubnetGroupArn': 'string'
    }
}


Response Structure

(dict) --

DBSubnetGroup (dict) --
Detailed information about a subnet group.

DBSubnetGroupName (string) --
The name of the subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the subnet group.

VpcId (string) --
Provides the virtual private cloud (VPC) ID of the subnet group.

SubnetGroupStatus (string) --
Provides the status of the subnet group.

Subnets (list) --
Detailed information about one or more subnets within a subnet group.

(dict) --
Detailed information about a subnet.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the Availability Zone for the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.









Exceptions

DocDB.Client.exceptions.DBSubnetGroupAlreadyExistsFault
DocDB.Client.exceptions.DBSubnetGroupQuotaExceededFault
DocDB.Client.exceptions.DBSubnetQuotaExceededFault
DocDB.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
DocDB.Client.exceptions.InvalidSubnet


    :return: {
        'DBSubnetGroup': {
            'DBSubnetGroupName': 'string',
            'DBSubnetGroupDescription': 'string',
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
            'DBSubnetGroupArn': 'string'
        }
    }
    
    
    :returns: 
    DocDB.Client.exceptions.DBSubnetGroupAlreadyExistsFault
    DocDB.Client.exceptions.DBSubnetGroupQuotaExceededFault
    DocDB.Client.exceptions.DBSubnetQuotaExceededFault
    DocDB.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
    DocDB.Client.exceptions.InvalidSubnet
    
    """
    pass

def delete_db_cluster(DBClusterIdentifier=None, SkipFinalSnapshot=None, FinalDBSnapshotIdentifier=None):
    """
    Deletes a previously provisioned cluster. When you delete a cluster, all automated backups for that cluster are deleted and can\'t be recovered. Manual DB cluster snapshots of the specified cluster are not deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_cluster(
        DBClusterIdentifier='string',
        SkipFinalSnapshot=True|False,
        FinalDBSnapshotIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe cluster identifier for the cluster to be deleted. This parameter isn\'t case sensitive.\nConstraints:\n\nMust match an existing DBClusterIdentifier .\n\n

    :type SkipFinalSnapshot: boolean
    :param SkipFinalSnapshot: Determines whether a final cluster snapshot is created before the cluster is deleted. If true is specified, no cluster snapshot is created. If false is specified, a cluster snapshot is created before the DB cluster is deleted.\n\nNote\nIf SkipFinalSnapshot is false , you must specify a FinalDBSnapshotIdentifier parameter.\n\nDefault: false\n

    :type FinalDBSnapshotIdentifier: string
    :param FinalDBSnapshotIdentifier: The cluster snapshot identifier of the new cluster snapshot created when SkipFinalSnapshot is set to false .\n\nNote\nSpecifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.\n\nConstraints:\n\nMust be from 1 to 255 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBCluster': {
        'AvailabilityZones': [
            'string',
        ],
        'BackupRetentionPeriod': 123,
        'DBClusterIdentifier': 'string',
        'DBClusterParameterGroup': 'string',
        'DBSubnetGroup': 'string',
        'Status': 'string',
        'PercentProgress': 'string',
        'EarliestRestorableTime': datetime(2015, 1, 1),
        'Endpoint': 'string',
        'ReaderEndpoint': 'string',
        'MultiAZ': True|False,
        'Engine': 'string',
        'EngineVersion': 'string',
        'LatestRestorableTime': datetime(2015, 1, 1),
        'Port': 123,
        'MasterUsername': 'string',
        'PreferredBackupWindow': 'string',
        'PreferredMaintenanceWindow': 'string',
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
        ],
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBCluster (dict) --
Detailed information about a cluster.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier (string) --
Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup (string) --
Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
The earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint (string) --
The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master user name for the cluster.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

DBClusterMembers (list) --
Provides the list of instances that make up the cluster.

(dict) --
Contains information about an instance that is part of a cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the cluster.

IsClusterWriter (boolean) --
A value that is true if the cluster member is the primary instance for the cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. IAM roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the cluster. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB cluster.
INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.






ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.









Exceptions

DocDB.Client.exceptions.DBClusterNotFoundFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.DBClusterSnapshotAlreadyExistsFault
DocDB.Client.exceptions.SnapshotQuotaExceededFault
DocDB.Client.exceptions.InvalidDBClusterSnapshotStateFault


    :return: {
        'DBCluster': {
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
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
            ],
            'ClusterCreateTime': datetime(2015, 1, 1),
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_db_cluster_parameter_group(DBClusterParameterGroupName=None):
    """
    Deletes a specified cluster parameter group. The cluster parameter group to be deleted can\'t be associated with any clusters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_cluster_parameter_group(
        DBClusterParameterGroupName='string'
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of the cluster parameter group.\nConstraints:\n\nMust be the name of an existing cluster parameter group.\nYou can\'t delete a default cluster parameter group.\nCannot be associated with any clusters.\n\n

    :returns: 
    DocDB.Client.exceptions.InvalidDBParameterGroupStateFault
    DocDB.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def delete_db_cluster_snapshot(DBClusterSnapshotIdentifier=None):
    """
    Deletes a cluster snapshot. If the snapshot is being copied, the copy operation is terminated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_cluster_snapshot(
        DBClusterSnapshotIdentifier='string'
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier of the cluster snapshot to delete.\nConstraints: Must be the name of an existing cluster snapshot in the available state.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DBClusterSnapshot': {
        'AvailabilityZones': [
            'string',
        ],
        'DBClusterSnapshotIdentifier': 'string',
        'DBClusterIdentifier': 'string',
        'SnapshotCreateTime': datetime(2015, 1, 1),
        'Engine': 'string',
        'Status': 'string',
        'Port': 123,
        'VpcId': 'string',
        'ClusterCreateTime': datetime(2015, 1, 1),
        'MasterUsername': 'string',
        'EngineVersion': 'string',
        'SnapshotType': 'string',
        'PercentProgress': 123,
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DBClusterSnapshotArn': 'string',
        'SourceDBClusterSnapshotArn': 'string'
    }
}


Response Structure

(dict) --
DBClusterSnapshot (dict) --Detailed information about a cluster snapshot.

AvailabilityZones (list) --Provides the list of Amazon EC2 Availability Zones that instances in the cluster snapshot can be restored in.

(string) --


DBClusterSnapshotIdentifier (string) --Specifies the identifier for the cluster snapshot.

DBClusterIdentifier (string) --Specifies the cluster identifier of the cluster that this cluster snapshot was created from.

SnapshotCreateTime (datetime) --Provides the time when the snapshot was taken, in UTC.

Engine (string) --Specifies the name of the database engine.

Status (string) --Specifies the status of this cluster snapshot.

Port (integer) --Specifies the port that the cluster was listening on at the time of the snapshot.

VpcId (string) --Provides the virtual private cloud (VPC) ID that is associated with the cluster snapshot.

ClusterCreateTime (datetime) --Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

MasterUsername (string) --Provides the master user name for the cluster snapshot.

EngineVersion (string) --Provides the version of the database engine for this cluster snapshot.

SnapshotType (string) --Provides the type of the cluster snapshot.

PercentProgress (integer) --Specifies the percentage of the estimated data that has been transferred.

StorageEncrypted (boolean) --Specifies whether the cluster snapshot is encrypted.

KmsKeyId (string) --If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster snapshot.

DBClusterSnapshotArn (string) --The Amazon Resource Name (ARN) for the cluster snapshot.

SourceDBClusterSnapshotArn (string) --If the cluster snapshot was copied from a source cluster snapshot, the ARN for the source cluster snapshot; otherwise, a null value.








Exceptions

DocDB.Client.exceptions.InvalidDBClusterSnapshotStateFault
DocDB.Client.exceptions.DBClusterSnapshotNotFoundFault


    :return: {
        'DBClusterSnapshot': {
            'AvailabilityZones': [
                'string',
            ],
            'DBClusterSnapshotIdentifier': 'string',
            'DBClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Engine': 'string',
            'Status': 'string',
            'Port': 123,
            'VpcId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'EngineVersion': 'string',
            'SnapshotType': 'string',
            'PercentProgress': 123,
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string'
        }
    }
    
    
    :returns: 
    DocDB.Client.exceptions.InvalidDBClusterSnapshotStateFault
    DocDB.Client.exceptions.DBClusterSnapshotNotFoundFault
    
    """
    pass

def delete_db_instance(DBInstanceIdentifier=None):
    """
    Deletes a previously provisioned instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_instance(
        DBInstanceIdentifier='string'
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]\nThe instance identifier for the instance to be deleted. This parameter isn\'t case sensitive.\nConstraints:\n\nMust match the name of an existing instance.\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'DBInstance': {
        'DBInstanceIdentifier': 'string',
        'DBInstanceClass': 'string',
        'Engine': 'string',
        'DBInstanceStatus': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123,
            'HostedZoneId': 'string'
        },
        'InstanceCreateTime': datetime(2015, 1, 1),
        'PreferredBackupWindow': 'string',
        'BackupRetentionPeriod': 123,
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'AvailabilityZone': 'string',
        'DBSubnetGroup': {
            'DBSubnetGroupName': 'string',
            'DBSubnetGroupDescription': 'string',
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
            'DBSubnetGroupArn': 'string'
        },
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'DBInstanceClass': 'string',
            'AllocatedStorage': 123,
            'MasterUserPassword': 'string',
            'Port': 123,
            'BackupRetentionPeriod': 123,
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'LicenseModel': 'string',
            'Iops': 123,
            'DBInstanceIdentifier': 'string',
            'StorageType': 'string',
            'CACertificateIdentifier': 'string',
            'DBSubnetGroupName': 'string',
            'PendingCloudwatchLogsExports': {
                'LogTypesToEnable': [
                    'string',
                ],
                'LogTypesToDisable': [
                    'string',
                ]
            }
        },
        'LatestRestorableTime': datetime(2015, 1, 1),
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'PubliclyAccessible': True|False,
        'StatusInfos': [
            {
                'StatusType': 'string',
                'Normal': True|False,
                'Status': 'string',
                'Message': 'string'
            },
        ],
        'DBClusterIdentifier': 'string',
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DbiResourceId': 'string',
        'CACertificateIdentifier': 'string',
        'PromotionTier': 123,
        'DBInstanceArn': 'string',
        'EnabledCloudwatchLogsExports': [
            'string',
        ]
    }
}


Response Structure

(dict) --
DBInstance (dict) --Detailed information about an instance.

DBInstanceIdentifier (string) --Contains a user-provided database identifier. This identifier is the unique key that identifies an instance.

DBInstanceClass (string) --Contains the name of the compute and memory capacity class of the instance.

Engine (string) --Provides the name of the database engine to be used for this instance.

DBInstanceStatus (string) --Specifies the current state of this database.

Endpoint (dict) --Specifies the connection endpoint.

Address (string) --Specifies the DNS address of the instance.

Port (integer) --Specifies the port that the database engine is listening on.

HostedZoneId (string) --Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



InstanceCreateTime (datetime) --Provides the date and time that the instance was created.

PreferredBackupWindow (string) --Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --Specifies the number of days for which automatic snapshots are retained.

VpcSecurityGroups (list) --Provides a list of VPC security group elements that the instance belongs to.

(dict) --Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --The name of the VPC security group.

Status (string) --The status of the VPC security group.





AvailabilityZone (string) --Specifies the name of the Availability Zone that the instance is located in.

DBSubnetGroup (dict) --Specifies information on the subnet group that is associated with the instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --The name of the subnet group.

DBSubnetGroupDescription (string) --Provides the description of the subnet group.

VpcId (string) --Provides the virtual private cloud (VPC) ID of the subnet group.

SubnetGroupStatus (string) --Provides the status of the subnet group.

Subnets (list) --Detailed information about one or more subnets within a subnet group.

(dict) --Detailed information about a subnet.

SubnetIdentifier (string) --Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --Specifies the Availability Zone for the subnet.

Name (string) --The name of the Availability Zone.



SubnetStatus (string) --Specifies the status of the subnet.





DBSubnetGroupArn (string) --The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --Specifies that changes to the instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --Contains the new DBInstanceClass for the instance that will be applied or is currently being applied.

AllocatedStorage (integer) --Contains the new AllocatedStorage size for then instance that will be applied or is currently being applied.

MasterUserPassword (string) --Contains the pending or currently in-progress change of the master credentials for the instance.

Port (integer) --Specifies the pending port for the instance.

BackupRetentionPeriod (integer) --Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --Indicates that the Single-AZ instance is to change to a Multi-AZ deployment.

EngineVersion (string) --Indicates the database engine version.

LicenseModel (string) --The license model for the instance.
Valid values: license-included , bring-your-own-license , general-public-license

Iops (integer) --Specifies the new Provisioned IOPS value for the instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --Contains the new DBInstanceIdentifier for the instance that will be applied or is currently being applied.

StorageType (string) --Specifies the storage type to be associated with the instance.

CACertificateIdentifier (string) --Specifies the identifier of the certificate authority (CA) certificate for the DB instance.

DBSubnetGroupName (string) --The new subnet group for the instance.

PendingCloudwatchLogsExports (dict) --A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.

LogTypesToEnable (list) --Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --Log types that are in the process of being enabled. After they are enabled, these log types are exported to Amazon CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --Specifies the latest time to which a database can be restored with point-in-time restore.

EngineVersion (string) --Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --Indicates that minor version patches are applied automatically.

PubliclyAccessible (boolean) --Not supported. Amazon DocumentDB does not currently support public endpoints. The value of PubliclyAccessible is always false .

StatusInfos (list) --The status of a read replica. If the instance is not a read replica, this is blank.

(dict) --Provides a list of status information for an instance.

StatusType (string) --This value is currently "read replication ."

Normal (boolean) --A Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --Status of the instance. For a StatusType of read replica, the values can be replicating , error, stopped , or terminated .

Message (string) --Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





DBClusterIdentifier (string) --Contains the name of the cluster that the instance is a member of if the instance is a member of a cluster.

StorageEncrypted (boolean) --Specifies whether or not the instance is encrypted.

KmsKeyId (string) --If StorageEncrypted is true , the AWS KMS key identifier for the encrypted instance.

DbiResourceId (string) --The AWS Region-unique, immutable identifier for the instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the instance is accessed.

CACertificateIdentifier (string) --The identifier of the CA certificate for this DB instance.

PromotionTier (integer) --A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --The Amazon Resource Name (ARN) for the instance.

EnabledCloudwatchLogsExports (list) --A list of log types that this instance is configured to export to Amazon CloudWatch Logs.

(string) --









Exceptions

DocDB.Client.exceptions.DBInstanceNotFoundFault
DocDB.Client.exceptions.InvalidDBInstanceStateFault
DocDB.Client.exceptions.DBSnapshotAlreadyExistsFault
DocDB.Client.exceptions.SnapshotQuotaExceededFault
DocDB.Client.exceptions.InvalidDBClusterStateFault


    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                'DBSubnetGroupArn': 'string'
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'DBInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MasterUserPassword': 'string',
                'Port': 123,
                'BackupRetentionPeriod': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'Iops': 123,
                'DBInstanceIdentifier': 'string',
                'StorageType': 'string',
                'CACertificateIdentifier': 'string',
                'DBSubnetGroupName': 'string',
                'PendingCloudwatchLogsExports': {
                    'LogTypesToEnable': [
                        'string',
                    ],
                    'LogTypesToDisable': [
                        'string',
                    ]
                }
            },
            'LatestRestorableTime': datetime(2015, 1, 1),
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_db_subnet_group(DBSubnetGroupName=None):
    """
    Deletes a subnet group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_subnet_group(
        DBSubnetGroupName='string'
    )
    
    
    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: [REQUIRED]\nThe name of the database subnet group to delete.\n\nNote\nYou can\'t delete the default subnet group.\n\nConstraints:\nMust match the name of an existing DBSubnetGroup . Must not be default.\nExample: mySubnetgroup\n

    """
    pass

def describe_certificates(CertificateIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of certificate authority (CA) certificates provided by Amazon DocumentDB for this AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_certificates(
        CertificateIdentifier='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type CertificateIdentifier: string
    :param CertificateIdentifier: The user-supplied certificate identifier. If this parameter is specified, information for only the specified certificate is returned. If this parameter is omitted, a list of up to MaxRecords certificates is returned. This parameter is not case sensitive.\nConstraints\n\nMust match an existing CertificateIdentifier .\n\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints:\n\nMinimum: 20\nMaximum: 100\n\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeCertificates request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Certificates': [
        {
            'CertificateIdentifier': 'string',
            'CertificateType': 'string',
            'Thumbprint': 'string',
            'ValidFrom': datetime(2015, 1, 1),
            'ValidTill': datetime(2015, 1, 1),
            'CertificateArn': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

Certificates (list) --
A list of certificates for this AWS account.

(dict) --
A certificate authority (CA) certificate for an AWS account.

CertificateIdentifier (string) --
The unique key that identifies a certificate.
Example: rds-ca-2019

CertificateType (string) --
The type of the certificate.
Example: CA

Thumbprint (string) --
The thumbprint of the certificate.

ValidFrom (datetime) --
The starting date-time from which the certificate is valid.
Example: 2019-07-31T17:57:09Z

ValidTill (datetime) --
The date-time after which the certificate is no longer valid.
Example: 2024-07-31T17:57:09Z

CertificateArn (string) --
The Amazon Resource Name (ARN) for the certificate.
Example: arn:aws:rds:us-east-1::cert:rds-ca-2019





Marker (string) --
An optional pagination token provided if the number of records retrieved is greater than MaxRecords . If this parameter is specified, the marker specifies the next record in the list. Including the value of Marker in the next call to DescribeCertificates results in the next page of certificates.







Exceptions

DocDB.Client.exceptions.CertificateNotFoundFault


    :return: {
        'Certificates': [
            {
                'CertificateIdentifier': 'string',
                'CertificateType': 'string',
                'Thumbprint': 'string',
                'ValidFrom': datetime(2015, 1, 1),
                'ValidTill': datetime(2015, 1, 1),
                'CertificateArn': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    DocDB.Client.exceptions.CertificateNotFoundFault
    
    """
    pass

def describe_db_cluster_parameter_groups(DBClusterParameterGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of DBClusterParameterGroup descriptions. If a DBClusterParameterGroupName parameter is specified, the list contains only the description of the specified cluster parameter group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_cluster_parameter_groups(
        DBClusterParameterGroupName='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of a specific cluster parameter group to return details for.\nConstraints:\n\nIf provided, must match the name of an existing DBClusterParameterGroup .\n\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'DBClusterParameterGroups': [
        {
            'DBClusterParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBClusterParameterGroupArn': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of  DBClusterParameterGroups .

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBClusterParameterGroups (list) --
A list of cluster parameter groups.

(dict) --
Detailed information about a cluster parameter group.

DBClusterParameterGroupName (string) --
Provides the name of the cluster parameter group.

DBParameterGroupFamily (string) --
Provides the name of the parameter group family that this cluster parameter group is compatible with.

Description (string) --
Provides the customer-specified description for this cluster parameter group.

DBClusterParameterGroupArn (string) --
The Amazon Resource Name (ARN) for the cluster parameter group.











Exceptions

DocDB.Client.exceptions.DBParameterGroupNotFoundFault


    :return: {
        'Marker': 'string',
        'DBClusterParameterGroups': [
            {
                'DBClusterParameterGroupName': 'string',
                'DBParameterGroupFamily': 'string',
                'Description': 'string',
                'DBClusterParameterGroupArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    DocDB.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def describe_db_cluster_parameters(DBClusterParameterGroupName=None, Source=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns the detailed parameter list for a particular cluster parameter group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_cluster_parameters(
        DBClusterParameterGroupName='string',
        Source='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of a specific cluster parameter group to return parameter details for.\nConstraints:\n\nIf provided, must match the name of an existing DBClusterParameterGroup .\n\n

    :type Source: string
    :param Source: A value that indicates to return only parameters for a specific source. Parameter sources can be engine , service , or customer .

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Parameters': [
        {
            'ParameterName': 'string',
            'ParameterValue': 'string',
            'Description': 'string',
            'Source': 'string',
            'ApplyType': 'string',
            'DataType': 'string',
            'AllowedValues': 'string',
            'IsModifiable': True|False,
            'MinimumEngineVersion': 'string',
            'ApplyMethod': 'immediate'|'pending-reboot'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
Represents the output of  DBClusterParameterGroup .

Parameters (list) --
Provides a list of parameters for the cluster parameter group.

(dict) --
Detailed information about an individual parameter.

ParameterName (string) --
Specifies the name of the parameter.

ParameterValue (string) --
Specifies the value of the parameter.

Description (string) --
Provides a description of the parameter.

Source (string) --
Indicates the source of the parameter value.

ApplyType (string) --
Specifies the engine-specific parameters type.

DataType (string) --
Specifies the valid data type for the parameter.

AllowedValues (string) --
Specifies the valid range of values for the parameter.

IsModifiable (boolean) --
Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion (string) --
The earliest engine version to which the parameter can apply.

ApplyMethod (string) --
Indicates when to apply parameter updates.





Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .







Exceptions

DocDB.Client.exceptions.DBParameterGroupNotFoundFault


    :return: {
        'Parameters': [
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    DocDB.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def describe_db_cluster_snapshot_attributes(DBClusterSnapshotIdentifier=None):
    """
    Returns a list of cluster snapshot attribute names and values for a manual DB cluster snapshot.
    When you share snapshots with other AWS accounts, DescribeDBClusterSnapshotAttributes returns the restore attribute and a list of IDs for the AWS accounts that are authorized to copy or restore the manual cluster snapshot. If all is included in the list of values for the restore attribute, then the manual cluster snapshot is public and can be copied or restored by all AWS accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_cluster_snapshot_attributes(
        DBClusterSnapshotIdentifier='string'
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier for the cluster snapshot to describe the attributes for.\n

    :rtype: dict
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
DBClusterSnapshotAttributesResult (dict) --Detailed information about the attributes that are associated with a cluster snapshot.

DBClusterSnapshotIdentifier (string) --The identifier of the cluster snapshot that the attributes apply to.

DBClusterSnapshotAttributes (list) --The list of attributes and values for the cluster snapshot.

(dict) --Contains the name and values of a manual cluster snapshot attribute.
Manual cluster snapshot attributes are used to authorize other AWS accounts to restore a manual cluster snapshot.

AttributeName (string) --The name of the manual cluster snapshot attribute.
The attribute named restore refers to the list of AWS accounts that have permission to copy or restore the manual cluster snapshot.

AttributeValues (list) --The values for the manual cluster snapshot attribute.
If the AttributeName field is set to restore , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual cluster snapshot. If a value of all is in the list, then the manual cluster snapshot is public and available for any AWS account to copy or restore.

(string) --













Exceptions

DocDB.Client.exceptions.DBClusterSnapshotNotFoundFault


    :return: {
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
    
    
    :returns: 
    DocDB.Client.exceptions.DBClusterSnapshotNotFoundFault
    
    """
    pass

def describe_db_cluster_snapshots(DBClusterIdentifier=None, DBClusterSnapshotIdentifier=None, SnapshotType=None, Filters=None, MaxRecords=None, Marker=None, IncludeShared=None, IncludePublic=None):
    """
    Returns information about cluster snapshots. This API operation supports pagination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_cluster_snapshots(
        DBClusterIdentifier='string',
        DBClusterSnapshotIdentifier='string',
        SnapshotType='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string',
        IncludeShared=True|False,
        IncludePublic=True|False
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: The ID of the cluster to retrieve the list of cluster snapshots for. This parameter can\'t be used with the DBClusterSnapshotIdentifier parameter. This parameter is not case sensitive.\nConstraints:\n\nIf provided, must match the identifier of an existing DBCluster .\n\n

    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: A specific cluster snapshot identifier to describe. This parameter can\'t be used with the DBClusterIdentifier parameter. This value is stored as a lowercase string.\nConstraints:\n\nIf provided, must match the identifier of an existing DBClusterSnapshot .\nIf this identifier is for an automated snapshot, the SnapshotType parameter must also be specified.\n\n

    :type SnapshotType: string
    :param SnapshotType: The type of cluster snapshots to be returned. You can specify one of the following values:\n\nautomated - Return all cluster snapshots that Amazon DocumentDB has automatically created for your AWS account.\nmanual - Return all cluster snapshots that you have manually created for your AWS account.\nshared - Return all manual cluster snapshots that have been shared to your AWS account.\npublic - Return all cluster snapshots that have been marked as public.\n\nIf you don\'t specify a SnapshotType value, then both automated and manual cluster snapshots are returned. You can include shared cluster snapshots with these results by setting the IncludeShared parameter to true . You can include public cluster snapshots with these results by setting the IncludePublic parameter to true .\nThe IncludeShared and IncludePublic parameters don\'t apply for SnapshotType values of manual or automated . The IncludePublic parameter doesn\'t apply when SnapshotType is set to shared . The IncludeShared parameter doesn\'t apply when SnapshotType is set to public .\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type IncludeShared: boolean
    :param IncludeShared: Set to true to include shared manual cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise false . The default is false .

    :type IncludePublic: boolean
    :param IncludePublic: Set to true to include manual cluster snapshots that are public and can be copied or restored by any AWS account, and otherwise false . The default is false .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'DBClusterSnapshots': [
        {
            'AvailabilityZones': [
                'string',
            ],
            'DBClusterSnapshotIdentifier': 'string',
            'DBClusterIdentifier': 'string',
            'SnapshotCreateTime': datetime(2015, 1, 1),
            'Engine': 'string',
            'Status': 'string',
            'Port': 123,
            'VpcId': 'string',
            'ClusterCreateTime': datetime(2015, 1, 1),
            'MasterUsername': 'string',
            'EngineVersion': 'string',
            'SnapshotType': 'string',
            'PercentProgress': 123,
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of  DescribeDBClusterSnapshots .

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBClusterSnapshots (list) --
Provides a list of cluster snapshots.

(dict) --
Detailed information about a cluster snapshot.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster snapshot can be restored in.

(string) --


DBClusterSnapshotIdentifier (string) --
Specifies the identifier for the cluster snapshot.

DBClusterIdentifier (string) --
Specifies the cluster identifier of the cluster that this cluster snapshot was created from.

SnapshotCreateTime (datetime) --
Provides the time when the snapshot was taken, in UTC.

Engine (string) --
Specifies the name of the database engine.

Status (string) --
Specifies the status of this cluster snapshot.

Port (integer) --
Specifies the port that the cluster was listening on at the time of the snapshot.

VpcId (string) --
Provides the virtual private cloud (VPC) ID that is associated with the cluster snapshot.

ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

MasterUsername (string) --
Provides the master user name for the cluster snapshot.

EngineVersion (string) --
Provides the version of the database engine for this cluster snapshot.

SnapshotType (string) --
Provides the type of the cluster snapshot.

PercentProgress (integer) --
Specifies the percentage of the estimated data that has been transferred.

StorageEncrypted (boolean) --
Specifies whether the cluster snapshot is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster snapshot.

DBClusterSnapshotArn (string) --
The Amazon Resource Name (ARN) for the cluster snapshot.

SourceDBClusterSnapshotArn (string) --
If the cluster snapshot was copied from a source cluster snapshot, the ARN for the source cluster snapshot; otherwise, a null value.











Exceptions

DocDB.Client.exceptions.DBClusterSnapshotNotFoundFault


    :return: {
        'Marker': 'string',
        'DBClusterSnapshots': [
            {
                'AvailabilityZones': [
                    'string',
                ],
                'DBClusterSnapshotIdentifier': 'string',
                'DBClusterIdentifier': 'string',
                'SnapshotCreateTime': datetime(2015, 1, 1),
                'Engine': 'string',
                'Status': 'string',
                'Port': 123,
                'VpcId': 'string',
                'ClusterCreateTime': datetime(2015, 1, 1),
                'MasterUsername': 'string',
                'EngineVersion': 'string',
                'SnapshotType': 'string',
                'PercentProgress': 123,
                'StorageEncrypted': True|False,
                'KmsKeyId': 'string',
                'DBClusterSnapshotArn': 'string',
                'SourceDBClusterSnapshotArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_clusters(DBClusterIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about provisioned Amazon DocumentDB clusters. This API operation supports pagination. For certain management features such as cluster and instance lifecycle management, Amazon DocumentDB leverages operational technology that is shared with Amazon RDS and Amazon Neptune. Use the filterName=engine,Values=docdb filter parameter to return only Amazon DocumentDB clusters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_clusters(
        DBClusterIdentifier='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: The user-provided cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isn\'t case sensitive.\nConstraints:\n\nIf provided, must match an existing DBClusterIdentifier .\n\n

    :type Filters: list
    :param Filters: A filter that specifies one or more clusters to describe.\nSupported filters:\n\ndb-cluster-id - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list only includes information about the clusters identified by these ARNs.\n\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'DBClusters': [
        {
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
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
            ],
            'ClusterCreateTime': datetime(2015, 1, 1),
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        },
    ]
}


Response Structure

(dict) --
Represents the output of  DescribeDBClusters .

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBClusters (list) --
A list of clusters.

(dict) --
Detailed information about a cluster.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier (string) --
Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup (string) --
Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
The earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint (string) --
The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master user name for the cluster.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

DBClusterMembers (list) --
Provides the list of instances that make up the cluster.

(dict) --
Contains information about an instance that is part of a cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the cluster.

IsClusterWriter (boolean) --
A value that is true if the cluster member is the primary instance for the cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. IAM roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the cluster. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB cluster.
INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.






ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.











Exceptions

DocDB.Client.exceptions.DBClusterNotFoundFault


    :return: {
        'Marker': 'string',
        'DBClusters': [
            {
                'AvailabilityZones': [
                    'string',
                ],
                'BackupRetentionPeriod': 123,
                'DBClusterIdentifier': 'string',
                'DBClusterParameterGroup': 'string',
                'DBSubnetGroup': 'string',
                'Status': 'string',
                'PercentProgress': 'string',
                'EarliestRestorableTime': datetime(2015, 1, 1),
                'Endpoint': 'string',
                'ReaderEndpoint': 'string',
                'MultiAZ': True|False,
                'Engine': 'string',
                'EngineVersion': 'string',
                'LatestRestorableTime': datetime(2015, 1, 1),
                'Port': 123,
                'MasterUsername': 'string',
                'PreferredBackupWindow': 'string',
                'PreferredMaintenanceWindow': 'string',
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
                ],
                'ClusterCreateTime': datetime(2015, 1, 1),
                'EnabledCloudwatchLogsExports': [
                    'string',
                ],
                'DeletionProtection': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_engine_versions(Engine=None, EngineVersion=None, DBParameterGroupFamily=None, Filters=None, MaxRecords=None, Marker=None, DefaultOnly=None, ListSupportedCharacterSets=None, ListSupportedTimezones=None):
    """
    Returns a list of the available engines.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_db_engine_versions(
        Engine='string',
        EngineVersion='string',
        DBParameterGroupFamily='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string',
        DefaultOnly=True|False,
        ListSupportedCharacterSets=True|False,
        ListSupportedTimezones=True|False
    )
    
    
    :type Engine: string
    :param Engine: The database engine to return.

    :type EngineVersion: string
    :param EngineVersion: The database engine version to return.\nExample: 5.1.49\n

    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: The name of a specific parameter group family to return details for.\nConstraints:\n\nIf provided, must match an existing DBParameterGroupFamily .\n\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type DefaultOnly: boolean
    :param DefaultOnly: Indicates that only the default version of the specified engine or engine and major version combination is returned.

    :type ListSupportedCharacterSets: boolean
    :param ListSupportedCharacterSets: If this parameter is specified and the requested engine supports the CharacterSetName parameter for CreateDBInstance , the response includes a list of supported character sets for each engine version.

    :type ListSupportedTimezones: boolean
    :param ListSupportedTimezones: If this parameter is specified and the requested engine supports the TimeZone parameter for CreateDBInstance , the response includes a list of supported time zones for each engine version.

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'DBEngineVersions': [
        {
            'Engine': 'string',
            'EngineVersion': 'string',
            'DBParameterGroupFamily': 'string',
            'DBEngineDescription': 'string',
            'DBEngineVersionDescription': 'string',
            'ValidUpgradeTarget': [
                {
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'Description': 'string',
                    'AutoUpgrade': True|False,
                    'IsMajorVersionUpgrade': True|False
                },
            ],
            'ExportableLogTypes': [
                'string',
            ],
            'SupportsLogExportsToCloudwatchLogs': True|False
        },
    ]
}


Response Structure

(dict) --
Represents the output of  DescribeDBEngineVersions .

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBEngineVersions (list) --
Detailed information about one or more engine versions.

(dict) --
Detailed information about an engine version.

Engine (string) --
The name of the database engine.

EngineVersion (string) --
The version number of the database engine.

DBParameterGroupFamily (string) --
The name of the parameter group family for the database engine.

DBEngineDescription (string) --
The description of the database engine.

DBEngineVersionDescription (string) --
The description of the database engine version.

ValidUpgradeTarget (list) --
A list of engine versions that this database engine version can be upgraded to.

(dict) --
The version of the database engine that an instance can be upgraded to.

Engine (string) --
The name of the upgrade target database engine.

EngineVersion (string) --
The version number of the upgrade target database engine.

Description (string) --
The version of the database engine that an instance can be upgraded to.

AutoUpgrade (boolean) --
A value that indicates whether the target version is applied to any source DB instances that have AutoMinorVersionUpgrade set to true .

IsMajorVersionUpgrade (boolean) --
A value that indicates whether a database engine is upgraded to a major version.





ExportableLogTypes (list) --
The types of logs that the database engine has available for export to Amazon CloudWatch Logs.

(string) --


SupportsLogExportsToCloudwatchLogs (boolean) --
A value that indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.












    :return: {
        'Marker': 'string',
        'DBEngineVersions': [
            {
                'Engine': 'string',
                'EngineVersion': 'string',
                'DBParameterGroupFamily': 'string',
                'DBEngineDescription': 'string',
                'DBEngineVersionDescription': 'string',
                'ValidUpgradeTarget': [
                    {
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'Description': 'string',
                        'AutoUpgrade': True|False,
                        'IsMajorVersionUpgrade': True|False
                    },
                ],
                'ExportableLogTypes': [
                    'string',
                ],
                'SupportsLogExportsToCloudwatchLogs': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_instances(DBInstanceIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about provisioned Amazon DocumentDB instances. This API supports pagination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_instances(
        DBInstanceIdentifier='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: The user-provided instance identifier. If this parameter is specified, information from only the specific instance is returned. This parameter isn\'t case sensitive.\nConstraints:\n\nIf provided, must match the identifier of an existing DBInstance .\n\n

    :type Filters: list
    :param Filters: A filter that specifies one or more instances to describe.\nSupported filters:\n\ndb-cluster-id - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list includes only the information about the instances that are associated with the clusters that are identified by these ARNs.\ndb-instance-id - Accepts instance identifiers and instance ARNs. The results list includes only the information about the instances that are identified by these ARNs.\n\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'DBInstances': [
        {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                'DBSubnetGroupArn': 'string'
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'DBInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MasterUserPassword': 'string',
                'Port': 123,
                'BackupRetentionPeriod': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'Iops': 123,
                'DBInstanceIdentifier': 'string',
                'StorageType': 'string',
                'CACertificateIdentifier': 'string',
                'DBSubnetGroupName': 'string',
                'PendingCloudwatchLogsExports': {
                    'LogTypesToEnable': [
                        'string',
                    ],
                    'LogTypesToDisable': [
                        'string',
                    ]
                }
            },
            'LatestRestorableTime': datetime(2015, 1, 1),
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
Represents the output of  DescribeDBInstances .

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBInstances (list) --
Detailed information about one or more instances.

(dict) --
Detailed information about an instance.

DBInstanceIdentifier (string) --
Contains a user-provided database identifier. This identifier is the unique key that identifies an instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the instance.

Engine (string) --
Provides the name of the database engine to be used for this instance.

DBInstanceStatus (string) --
Specifies the current state of this database.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



InstanceCreateTime (datetime) --
Provides the date and time that the instance was created.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

VpcSecurityGroups (list) --
Provides a list of VPC security group elements that the instance belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





AvailabilityZone (string) --
Specifies the name of the Availability Zone that the instance is located in.

DBSubnetGroup (dict) --
Specifies information on the subnet group that is associated with the instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --
The name of the subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the subnet group.

VpcId (string) --
Provides the virtual private cloud (VPC) ID of the subnet group.

SubnetGroupStatus (string) --
Provides the status of the subnet group.

Subnets (list) --
Detailed information about one or more subnets within a subnet group.

(dict) --
Detailed information about a subnet.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the Availability Zone for the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --
Specifies that changes to the instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --
Contains the new DBInstanceClass for the instance that will be applied or is currently being applied.

AllocatedStorage (integer) --
Contains the new AllocatedStorage size for then instance that will be applied or is currently being applied.

MasterUserPassword (string) --
Contains the pending or currently in-progress change of the master credentials for the instance.

Port (integer) --
Specifies the pending port for the instance.

BackupRetentionPeriod (integer) --
Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --
Indicates that the Single-AZ instance is to change to a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

LicenseModel (string) --
The license model for the instance.
Valid values: license-included , bring-your-own-license , general-public-license

Iops (integer) --
Specifies the new Provisioned IOPS value for the instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --
Contains the new DBInstanceIdentifier for the instance that will be applied or is currently being applied.

StorageType (string) --
Specifies the storage type to be associated with the instance.

CACertificateIdentifier (string) --
Specifies the identifier of the certificate authority (CA) certificate for the DB instance.

DBSubnetGroupName (string) --
The new subnet group for the instance.

PendingCloudwatchLogsExports (dict) --
A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.

LogTypesToEnable (list) --
Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --
Log types that are in the process of being enabled. After they are enabled, these log types are exported to Amazon CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

EngineVersion (string) --
Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --
Indicates that minor version patches are applied automatically.

PubliclyAccessible (boolean) --
Not supported. Amazon DocumentDB does not currently support public endpoints. The value of PubliclyAccessible is always false .

StatusInfos (list) --
The status of a read replica. If the instance is not a read replica, this is blank.

(dict) --
Provides a list of status information for an instance.

StatusType (string) --
This value is currently "read replication ."

Normal (boolean) --
A Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --
Status of the instance. For a StatusType of read replica, the values can be replicating , error, stopped , or terminated .

Message (string) --
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





DBClusterIdentifier (string) --
Contains the name of the cluster that the instance is a member of if the instance is a member of a cluster.

StorageEncrypted (boolean) --
Specifies whether or not the instance is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted instance.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the instance is accessed.

CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --
The Amazon Resource Name (ARN) for the instance.

EnabledCloudwatchLogsExports (list) --
A list of log types that this instance is configured to export to Amazon CloudWatch Logs.

(string) --












Exceptions

DocDB.Client.exceptions.DBInstanceNotFoundFault


    :return: {
        'Marker': 'string',
        'DBInstances': [
            {
                'DBInstanceIdentifier': 'string',
                'DBInstanceClass': 'string',
                'Engine': 'string',
                'DBInstanceStatus': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123,
                    'HostedZoneId': 'string'
                },
                'InstanceCreateTime': datetime(2015, 1, 1),
                'PreferredBackupWindow': 'string',
                'BackupRetentionPeriod': 123,
                'VpcSecurityGroups': [
                    {
                        'VpcSecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'AvailabilityZone': 'string',
                'DBSubnetGroup': {
                    'DBSubnetGroupName': 'string',
                    'DBSubnetGroupDescription': 'string',
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
                    'DBSubnetGroupArn': 'string'
                },
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                    'DBInstanceClass': 'string',
                    'AllocatedStorage': 123,
                    'MasterUserPassword': 'string',
                    'Port': 123,
                    'BackupRetentionPeriod': 123,
                    'MultiAZ': True|False,
                    'EngineVersion': 'string',
                    'LicenseModel': 'string',
                    'Iops': 123,
                    'DBInstanceIdentifier': 'string',
                    'StorageType': 'string',
                    'CACertificateIdentifier': 'string',
                    'DBSubnetGroupName': 'string',
                    'PendingCloudwatchLogsExports': {
                        'LogTypesToEnable': [
                            'string',
                        ],
                        'LogTypesToDisable': [
                            'string',
                        ]
                    }
                },
                'LatestRestorableTime': datetime(2015, 1, 1),
                'EngineVersion': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'PubliclyAccessible': True|False,
                'StatusInfos': [
                    {
                        'StatusType': 'string',
                        'Normal': True|False,
                        'Status': 'string',
                        'Message': 'string'
                    },
                ],
                'DBClusterIdentifier': 'string',
                'StorageEncrypted': True|False,
                'KmsKeyId': 'string',
                'DbiResourceId': 'string',
                'CACertificateIdentifier': 'string',
                'PromotionTier': 123,
                'DBInstanceArn': 'string',
                'EnabledCloudwatchLogsExports': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_subnet_groups(DBSubnetGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName is specified, the list will contain only the descriptions of the specified DBSubnetGroup .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_subnet_groups(
        DBSubnetGroupName='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The name of the subnet group to return details for.

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'DBSubnetGroups': [
        {
            'DBSubnetGroupName': 'string',
            'DBSubnetGroupDescription': 'string',
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
            'DBSubnetGroupArn': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of  DescribeDBSubnetGroups .

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBSubnetGroups (list) --
Detailed information about one or more subnet groups.

(dict) --
Detailed information about a subnet group.

DBSubnetGroupName (string) --
The name of the subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the subnet group.

VpcId (string) --
Provides the virtual private cloud (VPC) ID of the subnet group.

SubnetGroupStatus (string) --
Provides the status of the subnet group.

Subnets (list) --
Detailed information about one or more subnets within a subnet group.

(dict) --
Detailed information about a subnet.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the Availability Zone for the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.











Exceptions

DocDB.Client.exceptions.DBSubnetGroupNotFoundFault


    :return: {
        'Marker': 'string',
        'DBSubnetGroups': [
            {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                'DBSubnetGroupArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    DocDB.Client.exceptions.DBSubnetGroupNotFoundFault
    
    """
    pass

def describe_engine_default_cluster_parameters(DBParameterGroupFamily=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns the default engine and system parameter information for the cluster database engine.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_engine_default_cluster_parameters(
        DBParameterGroupFamily='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: [REQUIRED]\nThe name of the cluster parameter group family to return the engine parameter information for.\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'EngineDefaults': {
        'DBParameterGroupFamily': 'string',
        'Marker': 'string',
        'Parameters': [
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ]
    }
}


Response Structure

(dict) --

EngineDefaults (dict) --
Contains the result of a successful invocation of the DescribeEngineDefaultClusterParameters operation.

DBParameterGroupFamily (string) --
The name of the cluster parameter group family to return the engine parameter information for.

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Parameters (list) --
The parameters of a particular cluster parameter group family.

(dict) --
Detailed information about an individual parameter.

ParameterName (string) --
Specifies the name of the parameter.

ParameterValue (string) --
Specifies the value of the parameter.

Description (string) --
Provides a description of the parameter.

Source (string) --
Indicates the source of the parameter value.

ApplyType (string) --
Specifies the engine-specific parameters type.

DataType (string) --
Specifies the valid data type for the parameter.

AllowedValues (string) --
Specifies the valid range of values for the parameter.

IsModifiable (boolean) --
Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion (string) --
The earliest engine version to which the parameter can apply.

ApplyMethod (string) --
Indicates when to apply parameter updates.














    :return: {
        'EngineDefaults': {
            'DBParameterGroupFamily': 'string',
            'Marker': 'string',
            'Parameters': [
                {
                    'ParameterName': 'string',
                    'ParameterValue': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'ApplyType': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string',
                    'ApplyMethod': 'immediate'|'pending-reboot'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_event_categories(SourceType=None, Filters=None):
    """
    Displays a list of categories for all event source types, or, if specified, for a specified source type.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_categories(
        SourceType='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type SourceType: string
    :param SourceType: The type of source that is generating the events.\nValid values: db-instance , db-parameter-group , db-security-group , db-snapshot\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EventCategoriesMapList': [
        {
            'SourceType': 'string',
            'EventCategories': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
Represents the output of  DescribeEventCategories .

EventCategoriesMapList (list) --
A list of event category maps.

(dict) --
An event source type, accompanied by one or more event category names.

SourceType (string) --
The source type that the returned categories belong to.

EventCategories (list) --
The event categories for the specified source type.

(string) --













    :return: {
        'EventCategoriesMapList': [
            {
                'SourceType': 'string',
                'EventCategories': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, EventCategories=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns events related to instances, security groups, snapshots, and DB parameter groups for the past 14 days. You can obtain events specific to a particular DB instance, security group, snapshot, or parameter group by providing the name as a parameter. By default, the events of the past hour are returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_events(
        SourceIdentifier='string',
        SourceType='db-instance'|'db-parameter-group'|'db-security-group'|'db-snapshot'|'db-cluster'|'db-cluster-snapshot',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Duration=123,
        EventCategories=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type SourceIdentifier: string
    :param SourceIdentifier: The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.\nConstraints:\n\nIf SourceIdentifier is provided, SourceType must also be provided.\nIf the source type is DBInstance , a DBInstanceIdentifier must be provided.\nIf the source type is DBSecurityGroup , a DBSecurityGroupName must be provided.\nIf the source type is DBParameterGroup , a DBParameterGroupName must be provided.\nIf the source type is DBSnapshot , a DBSnapshotIdentifier must be provided.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type SourceType: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.

    :type StartTime: datetime
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format.\nExample: 2009-07-08T18:00Z\n

    :type EndTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format.\nExample: 2009-07-08T18:00Z\n

    :type Duration: integer
    :param Duration: The number of minutes to retrieve events for.\nDefault: 60\n

    :type EventCategories: list
    :param EventCategories: A list of event categories that trigger notifications for an event notification subscription.\n\n(string) --\n\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Events': [
        {
            'SourceIdentifier': 'string',
            'SourceType': 'db-instance'|'db-parameter-group'|'db-security-group'|'db-snapshot'|'db-cluster'|'db-cluster-snapshot',
            'Message': 'string',
            'EventCategories': [
                'string',
            ],
            'Date': datetime(2015, 1, 1),
            'SourceArn': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of  DescribeEvents .

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Events (list) --
Detailed information about one or more events.

(dict) --
Detailed information about an event.

SourceIdentifier (string) --
Provides the identifier for the source of the event.

SourceType (string) --
Specifies the source type for this event.

Message (string) --
Provides the text of this event.

EventCategories (list) --
Specifies the category for the event.

(string) --


Date (datetime) --
Specifies the date and time of the event.

SourceArn (string) --
The Amazon Resource Name (ARN) for the event.












    :return: {
        'Marker': 'string',
        'Events': [
            {
                'SourceIdentifier': 'string',
                'SourceType': 'db-instance'|'db-parameter-group'|'db-security-group'|'db-snapshot'|'db-cluster'|'db-cluster-snapshot',
                'Message': 'string',
                'EventCategories': [
                    'string',
                ],
                'Date': datetime(2015, 1, 1),
                'SourceArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_orderable_db_instance_options(Engine=None, EngineVersion=None, DBInstanceClass=None, LicenseModel=None, Vpc=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of orderable instance options for the specified engine.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_orderable_db_instance_options(
        Engine='string',
        EngineVersion='string',
        DBInstanceClass='string',
        LicenseModel='string',
        Vpc=True|False,
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type Engine: string
    :param Engine: [REQUIRED]\nThe name of the engine to retrieve instance options for.\n

    :type EngineVersion: string
    :param EngineVersion: The engine version filter value. Specify this parameter to show only the available offerings that match the specified engine version.

    :type DBInstanceClass: string
    :param DBInstanceClass: The instance class filter value. Specify this parameter to show only the available offerings that match the specified instance class.

    :type LicenseModel: string
    :param LicenseModel: The license model filter value. Specify this parameter to show only the available offerings that match the specified license model.

    :type Vpc: boolean
    :param Vpc: The virtual private cloud (VPC) filter value. Specify this parameter to show only the available VPC or non-VPC offerings.

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'OrderableDBInstanceOptions': [
        {
            'Engine': 'string',
            'EngineVersion': 'string',
            'DBInstanceClass': 'string',
            'LicenseModel': 'string',
            'AvailabilityZones': [
                {
                    'Name': 'string'
                },
            ],
            'Vpc': True|False
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
Represents the output of  DescribeOrderableDBInstanceOptions .

OrderableDBInstanceOptions (list) --
The options that are available for a particular orderable instance.

(dict) --
The options that are available for an instance.

Engine (string) --
The engine type of an instance.

EngineVersion (string) --
The engine version of an instance.

DBInstanceClass (string) --
The instance class for an instance.

LicenseModel (string) --
The license model for an instance.

AvailabilityZones (list) --
A list of Availability Zones for an instance.

(dict) --
Information about an Availability Zone.

Name (string) --
The name of the Availability Zone.





Vpc (boolean) --
Indicates whether an instance is in a virtual private cloud (VPC).





Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .








    :return: {
        'OrderableDBInstanceOptions': [
            {
                'Engine': 'string',
                'EngineVersion': 'string',
                'DBInstanceClass': 'string',
                'LicenseModel': 'string',
                'AvailabilityZones': [
                    {
                        'Name': 'string'
                    },
                ],
                'Vpc': True|False
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_pending_maintenance_actions(ResourceIdentifier=None, Filters=None, Marker=None, MaxRecords=None):
    """
    Returns a list of resources (for example, instances) that have at least one pending maintenance action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_pending_maintenance_actions(
        ResourceIdentifier='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        Marker='string',
        MaxRecords=123
    )
    
    
    :type ResourceIdentifier: string
    :param ResourceIdentifier: The ARN of a resource to return pending maintenance actions for.

    :type Filters: list
    :param Filters: A filter that specifies one or more resources to return pending maintenance actions for.\nSupported filters:\n\ndb-cluster-id - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list includes only pending maintenance actions for the clusters identified by these ARNs.\ndb-instance-id - Accepts instance identifiers and instance ARNs. The results list includes only pending maintenance actions for the DB instances identified by these ARNs.\n\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PendingMaintenanceActions': [
        {
            'ResourceIdentifier': 'string',
            'PendingMaintenanceActionDetails': [
                {
                    'Action': 'string',
                    'AutoAppliedAfterDate': datetime(2015, 1, 1),
                    'ForcedApplyDate': datetime(2015, 1, 1),
                    'OptInStatus': 'string',
                    'CurrentApplyDate': datetime(2015, 1, 1),
                    'Description': 'string'
                },
            ]
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
Represents the output of  DescribePendingMaintenanceActions .

PendingMaintenanceActions (list) --
The maintenance actions to be applied.

(dict) --
Represents the output of  ApplyPendingMaintenanceAction .

ResourceIdentifier (string) --
The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.

PendingMaintenanceActionDetails (list) --
A list that provides details about the pending maintenance actions for the resource.

(dict) --
Provides information about a pending maintenance action for a resource.

Action (string) --
The type of pending maintenance action that is available for the resource.

AutoAppliedAfterDate (datetime) --
The date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any next-maintenance opt-in requests are ignored.

ForcedApplyDate (datetime) --
The date when the maintenance action is automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any immediate opt-in requests are ignored.

OptInStatus (string) --
Indicates the type of opt-in request that has been received for the resource.

CurrentApplyDate (datetime) --
The effective date when the pending maintenance action is applied to the resource.

Description (string) --
A description providing more detail about the maintenance action.









Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .







Exceptions

DocDB.Client.exceptions.ResourceNotFoundFault


    :return: {
        'PendingMaintenanceActions': [
            {
                'ResourceIdentifier': 'string',
                'PendingMaintenanceActionDetails': [
                    {
                        'Action': 'string',
                        'AutoAppliedAfterDate': datetime(2015, 1, 1),
                        'ForcedApplyDate': datetime(2015, 1, 1),
                        'OptInStatus': 'string',
                        'CurrentApplyDate': datetime(2015, 1, 1),
                        'Description': 'string'
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    DocDB.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def failover_db_cluster(DBClusterIdentifier=None, TargetDBInstanceIdentifier=None):
    """
    Forces a failover for a cluster.
    A failover for a cluster promotes one of the Amazon DocumentDB replicas (read-only instances) in the cluster to be the primary instance (the cluster writer).
    If the primary instance fails, Amazon DocumentDB automatically fails over to an Amazon DocumentDB replica, if one exists. You can force a failover when you want to simulate a failure of a primary instance for testing.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.failover_db_cluster(
        DBClusterIdentifier='string',
        TargetDBInstanceIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: A cluster identifier to force a failover for. This parameter is not case sensitive.\nConstraints:\n\nMust match the identifier of an existing DBCluster .\n\n

    :type TargetDBInstanceIdentifier: string
    :param TargetDBInstanceIdentifier: The name of the instance to promote to the primary instance.\nYou must specify the instance identifier for an Amazon DocumentDB replica in the cluster. For example, mydbcluster-replica1 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBCluster': {
        'AvailabilityZones': [
            'string',
        ],
        'BackupRetentionPeriod': 123,
        'DBClusterIdentifier': 'string',
        'DBClusterParameterGroup': 'string',
        'DBSubnetGroup': 'string',
        'Status': 'string',
        'PercentProgress': 'string',
        'EarliestRestorableTime': datetime(2015, 1, 1),
        'Endpoint': 'string',
        'ReaderEndpoint': 'string',
        'MultiAZ': True|False,
        'Engine': 'string',
        'EngineVersion': 'string',
        'LatestRestorableTime': datetime(2015, 1, 1),
        'Port': 123,
        'MasterUsername': 'string',
        'PreferredBackupWindow': 'string',
        'PreferredMaintenanceWindow': 'string',
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
        ],
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBCluster (dict) --
Detailed information about a cluster.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier (string) --
Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup (string) --
Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
The earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint (string) --
The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master user name for the cluster.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

DBClusterMembers (list) --
Provides the list of instances that make up the cluster.

(dict) --
Contains information about an instance that is part of a cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the cluster.

IsClusterWriter (boolean) --
A value that is true if the cluster member is the primary instance for the cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. IAM roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the cluster. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB cluster.
INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.






ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.









Exceptions

DocDB.Client.exceptions.DBClusterNotFoundFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.InvalidDBInstanceStateFault


    :return: {
        'DBCluster': {
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
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
            ],
            'ClusterCreateTime': datetime(2015, 1, 1),
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
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

def list_tags_for_resource(ResourceName=None, Filters=None):
    """
    Lists all tags on an Amazon DocumentDB resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceName='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe Amazon DocumentDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.\nWildcards are not supported in filters.\n\nName (string) -- [REQUIRED]The name of the filter. Filter names are case sensitive.\n\nValues (list) -- [REQUIRED]One or more filter values. Filter values are case sensitive.\n\n(string) --\n\n\n\n\n\n

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
Represents the output of  ListTagsForResource .

TagList (list) --
A list of one or more tags.

(dict) --
Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

Key (string) --
The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with "aws:" or "rds:". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

Value (string) --
The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with "aws:" or "rds:". The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").











Exceptions

DocDB.Client.exceptions.DBInstanceNotFoundFault
DocDB.Client.exceptions.DBSnapshotNotFoundFault
DocDB.Client.exceptions.DBClusterNotFoundFault


    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    DocDB.Client.exceptions.DBInstanceNotFoundFault
    DocDB.Client.exceptions.DBSnapshotNotFoundFault
    DocDB.Client.exceptions.DBClusterNotFoundFault
    
    """
    pass

def modify_db_cluster(DBClusterIdentifier=None, NewDBClusterIdentifier=None, ApplyImmediately=None, BackupRetentionPeriod=None, DBClusterParameterGroupName=None, VpcSecurityGroupIds=None, Port=None, MasterUserPassword=None, PreferredBackupWindow=None, PreferredMaintenanceWindow=None, CloudwatchLogsExportConfiguration=None, EngineVersion=None, DeletionProtection=None):
    """
    Modifies a setting for an Amazon DocumentDB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_db_cluster(
        DBClusterIdentifier='string',
        NewDBClusterIdentifier='string',
        ApplyImmediately=True|False,
        BackupRetentionPeriod=123,
        DBClusterParameterGroupName='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        Port=123,
        MasterUserPassword='string',
        PreferredBackupWindow='string',
        PreferredMaintenanceWindow='string',
        CloudwatchLogsExportConfiguration={
            'EnableLogTypes': [
                'string',
            ],
            'DisableLogTypes': [
                'string',
            ]
        },
        EngineVersion='string',
        DeletionProtection=True|False
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe cluster identifier for the cluster that is being modified. This parameter is not case sensitive.\nConstraints:\n\nMust match the identifier of an existing DBCluster .\n\n

    :type NewDBClusterIdentifier: string
    :param NewDBClusterIdentifier: The new cluster identifier for the cluster when renaming a cluster. This value is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-cluster2\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: A value that specifies whether the changes in this request and any pending changes are asynchronously applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the cluster. If this parameter is set to false , changes to the cluster are applied during the next maintenance window.\nThe ApplyImmediately parameter affects only the NewDBClusterIdentifier and MasterUserPassword values. If you set this parameter value to false , the changes to the NewDBClusterIdentifier and MasterUserPassword values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the ApplyImmediately parameter.\nDefault: false\n

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: The number of days for which automated backups are retained. You must specify a minimum value of 1.\nDefault: 1\nConstraints:\n\nMust be a value from 1 to 35.\n\n

    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of the cluster parameter group to use for the cluster.

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of virtual private cloud (VPC) security groups that the cluster will belong to.\n\n(string) --\n\n

    :type Port: integer
    :param Port: The port number on which the cluster accepts connections.\nConstraints: Must be a value from 1150 to 65535 .\nDefault: The same port as the original cluster.\n

    :type MasterUserPassword: string
    :param MasterUserPassword: The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ('), or the 'at' symbol (@).\nConstraints: Must contain from 8 to 100 characters.\n

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region.\nConstraints:\n\nMust be in the format hh24:mi-hh24:mi .\nMust be in Universal Coordinated Time (UTC).\nMust not conflict with the preferred maintenance window.\nMust be at least 30 minutes.\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).\nFormat: ddd:hh24:mi-ddd:hh24:mi\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.\nValid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun\nConstraints: Minimum 30-minute window.\n

    :type CloudwatchLogsExportConfiguration: dict
    :param CloudwatchLogsExportConfiguration: The configuration setting for the log types to be enabled for export to Amazon CloudWatch Logs for a specific instance or cluster. The EnableLogTypes and DisableLogTypes arrays determine which logs are exported (or not exported) to CloudWatch Logs.\n\nEnableLogTypes (list) --The list of log types to enable.\n\n(string) --\n\n\nDisableLogTypes (list) --The list of log types to disable.\n\n(string) --\n\n\n\n

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true .

    :type DeletionProtection: boolean
    :param DeletionProtection: Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.

    :rtype: dict

ReturnsResponse Syntax
{
    'DBCluster': {
        'AvailabilityZones': [
            'string',
        ],
        'BackupRetentionPeriod': 123,
        'DBClusterIdentifier': 'string',
        'DBClusterParameterGroup': 'string',
        'DBSubnetGroup': 'string',
        'Status': 'string',
        'PercentProgress': 'string',
        'EarliestRestorableTime': datetime(2015, 1, 1),
        'Endpoint': 'string',
        'ReaderEndpoint': 'string',
        'MultiAZ': True|False,
        'Engine': 'string',
        'EngineVersion': 'string',
        'LatestRestorableTime': datetime(2015, 1, 1),
        'Port': 123,
        'MasterUsername': 'string',
        'PreferredBackupWindow': 'string',
        'PreferredMaintenanceWindow': 'string',
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
        ],
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBCluster (dict) --
Detailed information about a cluster.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier (string) --
Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup (string) --
Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
The earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint (string) --
The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master user name for the cluster.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

DBClusterMembers (list) --
Provides the list of instances that make up the cluster.

(dict) --
Contains information about an instance that is part of a cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the cluster.

IsClusterWriter (boolean) --
A value that is true if the cluster member is the primary instance for the cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. IAM roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the cluster. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB cluster.
INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.






ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.









Exceptions

DocDB.Client.exceptions.DBClusterNotFoundFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.StorageQuotaExceededFault
DocDB.Client.exceptions.DBSubnetGroupNotFoundFault
DocDB.Client.exceptions.InvalidVPCNetworkStateFault
DocDB.Client.exceptions.InvalidDBSubnetGroupStateFault
DocDB.Client.exceptions.InvalidSubnet
DocDB.Client.exceptions.DBClusterParameterGroupNotFoundFault
DocDB.Client.exceptions.InvalidDBSecurityGroupStateFault
DocDB.Client.exceptions.InvalidDBInstanceStateFault
DocDB.Client.exceptions.DBClusterAlreadyExistsFault


    :return: {
        'DBCluster': {
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
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
            ],
            'ClusterCreateTime': datetime(2015, 1, 1),
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_db_cluster_parameter_group(DBClusterParameterGroupName=None, Parameters=None):
    """
    Modifies the parameters of a cluster parameter group. To modify more than one parameter, submit a list of the following: ParameterName , ParameterValue , and ApplyMethod . A maximum of 20 parameters can be modified in a single request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_db_cluster_parameter_group(
        DBClusterParameterGroupName='string',
        Parameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ]
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of the cluster parameter group to modify.\n

    :type Parameters: list
    :param Parameters: [REQUIRED]\nA list of parameters in the cluster parameter group to modify.\n\n(dict) --Detailed information about an individual parameter.\n\nParameterName (string) --Specifies the name of the parameter.\n\nParameterValue (string) --Specifies the value of the parameter.\n\nDescription (string) --Provides a description of the parameter.\n\nSource (string) --Indicates the source of the parameter value.\n\nApplyType (string) --Specifies the engine-specific parameters type.\n\nDataType (string) --Specifies the valid data type for the parameter.\n\nAllowedValues (string) --Specifies the valid range of values for the parameter.\n\nIsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.\n\nMinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.\n\nApplyMethod (string) --Indicates when to apply parameter updates.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBClusterParameterGroupName': 'string'
}


Response Structure

(dict) --
Contains the name of a cluster parameter group.

DBClusterParameterGroupName (string) --
The name of a cluster parameter group.
Constraints:

Must be from 1 to 255 letters or numbers.
The first character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.


Note
This value is stored as a lowercase string.








Exceptions

DocDB.Client.exceptions.DBParameterGroupNotFoundFault
DocDB.Client.exceptions.InvalidDBParameterGroupStateFault


    :return: {
        'DBClusterParameterGroupName': 'string'
    }
    
    
    :returns: 
    Must be from 1 to 255 letters or numbers.
    The first character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def modify_db_cluster_snapshot_attribute(DBClusterSnapshotIdentifier=None, AttributeName=None, ValuesToAdd=None, ValuesToRemove=None):
    """
    Adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.
    To share a manual cluster snapshot with other AWS accounts, specify restore as the AttributeName , and use the ValuesToAdd parameter to add a list of IDs of the AWS accounts that are authorized to restore the manual cluster snapshot. Use the value all to make the manual cluster snapshot public, which means that it can be copied or restored by all AWS accounts. Do not add the all value for any manual DB cluster snapshots that contain private information that you don\'t want available to all AWS accounts. If a manual cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized AWS account IDs for the ValuesToAdd parameter. You can\'t use all as a value for that parameter in this case.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_db_cluster_snapshot_attribute(
        DBClusterSnapshotIdentifier='string',
        AttributeName='string',
        ValuesToAdd=[
            'string',
        ],
        ValuesToRemove=[
            'string',
        ]
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier for the cluster snapshot to modify the attributes for.\n

    :type AttributeName: string
    :param AttributeName: [REQUIRED]\nThe name of the cluster snapshot attribute to modify.\nTo manage authorization for other AWS accounts to copy or restore a manual cluster snapshot, set this value to restore .\n

    :type ValuesToAdd: list
    :param ValuesToAdd: A list of cluster snapshot attributes to add to the attribute specified by AttributeName .\nTo authorize other AWS accounts to copy or restore a manual cluster snapshot, set this list to include one or more AWS account IDs. To make the manual cluster snapshot restorable by any AWS account, set it to all . Do not add the all value for any manual cluster snapshots that contain private information that you don\'t want to be available to all AWS accounts.\n\n(string) --\n\n

    :type ValuesToRemove: list
    :param ValuesToRemove: A list of cluster snapshot attributes to remove from the attribute specified by AttributeName .\nTo remove authorization for other AWS accounts to copy or restore a manual cluster snapshot, set this list to include one or more AWS account identifiers. To remove authorization for any AWS account to copy or restore the cluster snapshot, set it to all . If you specify all , an AWS account whose account ID is explicitly added to the restore attribute can still copy or restore a manual cluster snapshot.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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

DBClusterSnapshotAttributesResult (dict) --
Detailed information about the attributes that are associated with a cluster snapshot.

DBClusterSnapshotIdentifier (string) --
The identifier of the cluster snapshot that the attributes apply to.

DBClusterSnapshotAttributes (list) --
The list of attributes and values for the cluster snapshot.

(dict) --
Contains the name and values of a manual cluster snapshot attribute.
Manual cluster snapshot attributes are used to authorize other AWS accounts to restore a manual cluster snapshot.

AttributeName (string) --
The name of the manual cluster snapshot attribute.
The attribute named restore refers to the list of AWS accounts that have permission to copy or restore the manual cluster snapshot.

AttributeValues (list) --
The values for the manual cluster snapshot attribute.
If the AttributeName field is set to restore , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual cluster snapshot. If a value of all is in the list, then the manual cluster snapshot is public and available for any AWS account to copy or restore.

(string) --














Exceptions

DocDB.Client.exceptions.DBClusterSnapshotNotFoundFault
DocDB.Client.exceptions.InvalidDBClusterSnapshotStateFault
DocDB.Client.exceptions.SharedSnapshotQuotaExceededFault


    :return: {
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
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_db_instance(DBInstanceIdentifier=None, DBInstanceClass=None, ApplyImmediately=None, PreferredMaintenanceWindow=None, AutoMinorVersionUpgrade=None, NewDBInstanceIdentifier=None, CACertificateIdentifier=None, PromotionTier=None):
    """
    Modifies settings for an instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_db_instance(
        DBInstanceIdentifier='string',
        DBInstanceClass='string',
        ApplyImmediately=True|False,
        PreferredMaintenanceWindow='string',
        AutoMinorVersionUpgrade=True|False,
        NewDBInstanceIdentifier='string',
        CACertificateIdentifier='string',
        PromotionTier=123
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]\nThe instance identifier. This value is stored as a lowercase string.\nConstraints:\n\nMust match the identifier of an existing DBInstance .\n\n

    :type DBInstanceClass: string
    :param DBInstanceClass: The new compute and memory capacity of the instance; for example, db.r5.large . Not all instance classes are available in all AWS Regions.\nIf you modify the instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless ApplyImmediately is specified as true for this request.\nDefault: Uses existing setting.\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the instance.\nIf this parameter is set to false , changes to the instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next reboot.\nDefault: false\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn\'t result in an outage except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, changing this parameter causes a reboot of the instance. If you are moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure that pending changes are applied.\nDefault: Uses existing setting.\nFormat: ddd:hh24:mi-ddd:hh24:mi\nValid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun\nConstraints: Must be at least 30 minutes.\n

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor version upgrades are applied automatically to the instance during the maintenance window. Changing this parameter doesn\'t result in an outage except in the following case, and the change is asynchronously applied as soon as possible. An outage results if this parameter is set to true during the maintenance window, and a newer minor version is available, and Amazon DocumentDB has enabled automatic patching for that engine version.

    :type NewDBInstanceIdentifier: string
    :param NewDBInstanceIdentifier: The new instance identifier for the instance when renaming an instance. When you change the instance identifier, an instance reboot occurs immediately if you set Apply Immediately to true . It occurs during the next maintenance window if you set Apply Immediately to false . This value is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: mydbinstance\n

    :type CACertificateIdentifier: string
    :param CACertificateIdentifier: Indicates the certificate that needs to be associated with the instance.

    :type PromotionTier: integer
    :param PromotionTier: A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.\nDefault: 1\nValid values: 0-15\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBInstance': {
        'DBInstanceIdentifier': 'string',
        'DBInstanceClass': 'string',
        'Engine': 'string',
        'DBInstanceStatus': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123,
            'HostedZoneId': 'string'
        },
        'InstanceCreateTime': datetime(2015, 1, 1),
        'PreferredBackupWindow': 'string',
        'BackupRetentionPeriod': 123,
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'AvailabilityZone': 'string',
        'DBSubnetGroup': {
            'DBSubnetGroupName': 'string',
            'DBSubnetGroupDescription': 'string',
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
            'DBSubnetGroupArn': 'string'
        },
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'DBInstanceClass': 'string',
            'AllocatedStorage': 123,
            'MasterUserPassword': 'string',
            'Port': 123,
            'BackupRetentionPeriod': 123,
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'LicenseModel': 'string',
            'Iops': 123,
            'DBInstanceIdentifier': 'string',
            'StorageType': 'string',
            'CACertificateIdentifier': 'string',
            'DBSubnetGroupName': 'string',
            'PendingCloudwatchLogsExports': {
                'LogTypesToEnable': [
                    'string',
                ],
                'LogTypesToDisable': [
                    'string',
                ]
            }
        },
        'LatestRestorableTime': datetime(2015, 1, 1),
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'PubliclyAccessible': True|False,
        'StatusInfos': [
            {
                'StatusType': 'string',
                'Normal': True|False,
                'Status': 'string',
                'Message': 'string'
            },
        ],
        'DBClusterIdentifier': 'string',
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DbiResourceId': 'string',
        'CACertificateIdentifier': 'string',
        'PromotionTier': 123,
        'DBInstanceArn': 'string',
        'EnabledCloudwatchLogsExports': [
            'string',
        ]
    }
}


Response Structure

(dict) --

DBInstance (dict) --
Detailed information about an instance.

DBInstanceIdentifier (string) --
Contains a user-provided database identifier. This identifier is the unique key that identifies an instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the instance.

Engine (string) --
Provides the name of the database engine to be used for this instance.

DBInstanceStatus (string) --
Specifies the current state of this database.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



InstanceCreateTime (datetime) --
Provides the date and time that the instance was created.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

VpcSecurityGroups (list) --
Provides a list of VPC security group elements that the instance belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





AvailabilityZone (string) --
Specifies the name of the Availability Zone that the instance is located in.

DBSubnetGroup (dict) --
Specifies information on the subnet group that is associated with the instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --
The name of the subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the subnet group.

VpcId (string) --
Provides the virtual private cloud (VPC) ID of the subnet group.

SubnetGroupStatus (string) --
Provides the status of the subnet group.

Subnets (list) --
Detailed information about one or more subnets within a subnet group.

(dict) --
Detailed information about a subnet.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the Availability Zone for the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --
Specifies that changes to the instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --
Contains the new DBInstanceClass for the instance that will be applied or is currently being applied.

AllocatedStorage (integer) --
Contains the new AllocatedStorage size for then instance that will be applied or is currently being applied.

MasterUserPassword (string) --
Contains the pending or currently in-progress change of the master credentials for the instance.

Port (integer) --
Specifies the pending port for the instance.

BackupRetentionPeriod (integer) --
Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --
Indicates that the Single-AZ instance is to change to a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

LicenseModel (string) --
The license model for the instance.
Valid values: license-included , bring-your-own-license , general-public-license

Iops (integer) --
Specifies the new Provisioned IOPS value for the instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --
Contains the new DBInstanceIdentifier for the instance that will be applied or is currently being applied.

StorageType (string) --
Specifies the storage type to be associated with the instance.

CACertificateIdentifier (string) --
Specifies the identifier of the certificate authority (CA) certificate for the DB instance.

DBSubnetGroupName (string) --
The new subnet group for the instance.

PendingCloudwatchLogsExports (dict) --
A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.

LogTypesToEnable (list) --
Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --
Log types that are in the process of being enabled. After they are enabled, these log types are exported to Amazon CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

EngineVersion (string) --
Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --
Indicates that minor version patches are applied automatically.

PubliclyAccessible (boolean) --
Not supported. Amazon DocumentDB does not currently support public endpoints. The value of PubliclyAccessible is always false .

StatusInfos (list) --
The status of a read replica. If the instance is not a read replica, this is blank.

(dict) --
Provides a list of status information for an instance.

StatusType (string) --
This value is currently "read replication ."

Normal (boolean) --
A Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --
Status of the instance. For a StatusType of read replica, the values can be replicating , error, stopped , or terminated .

Message (string) --
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





DBClusterIdentifier (string) --
Contains the name of the cluster that the instance is a member of if the instance is a member of a cluster.

StorageEncrypted (boolean) --
Specifies whether or not the instance is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted instance.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the instance is accessed.

CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --
The Amazon Resource Name (ARN) for the instance.

EnabledCloudwatchLogsExports (list) --
A list of log types that this instance is configured to export to Amazon CloudWatch Logs.

(string) --










Exceptions

DocDB.Client.exceptions.InvalidDBInstanceStateFault
DocDB.Client.exceptions.InvalidDBSecurityGroupStateFault
DocDB.Client.exceptions.DBInstanceAlreadyExistsFault
DocDB.Client.exceptions.DBInstanceNotFoundFault
DocDB.Client.exceptions.DBSecurityGroupNotFoundFault
DocDB.Client.exceptions.DBParameterGroupNotFoundFault
DocDB.Client.exceptions.InsufficientDBInstanceCapacityFault
DocDB.Client.exceptions.StorageQuotaExceededFault
DocDB.Client.exceptions.InvalidVPCNetworkStateFault
DocDB.Client.exceptions.DBUpgradeDependencyFailureFault
DocDB.Client.exceptions.StorageTypeNotSupportedFault
DocDB.Client.exceptions.AuthorizationNotFoundFault
DocDB.Client.exceptions.CertificateNotFoundFault


    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                'DBSubnetGroupArn': 'string'
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'DBInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MasterUserPassword': 'string',
                'Port': 123,
                'BackupRetentionPeriod': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'Iops': 123,
                'DBInstanceIdentifier': 'string',
                'StorageType': 'string',
                'CACertificateIdentifier': 'string',
                'DBSubnetGroupName': 'string',
                'PendingCloudwatchLogsExports': {
                    'LogTypesToEnable': [
                        'string',
                    ],
                    'LogTypesToDisable': [
                        'string',
                    ]
                }
            },
            'LatestRestorableTime': datetime(2015, 1, 1),
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_db_subnet_group(DBSubnetGroupName=None, DBSubnetGroupDescription=None, SubnetIds=None):
    """
    Modifies an existing subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the AWS Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_db_subnet_group(
        DBSubnetGroupName='string',
        DBSubnetGroupDescription='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: [REQUIRED]\nThe name for the subnet group. This value is stored as a lowercase string. You can\'t modify the default subnet group.\nConstraints: Must match the name of an existing DBSubnetGroup . Must not be default.\nExample: mySubnetgroup\n

    :type DBSubnetGroupDescription: string
    :param DBSubnetGroupDescription: The description for the subnet group.

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nThe Amazon EC2 subnet IDs for the subnet group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBSubnetGroup': {
        'DBSubnetGroupName': 'string',
        'DBSubnetGroupDescription': 'string',
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
        'DBSubnetGroupArn': 'string'
    }
}


Response Structure

(dict) --

DBSubnetGroup (dict) --
Detailed information about a subnet group.

DBSubnetGroupName (string) --
The name of the subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the subnet group.

VpcId (string) --
Provides the virtual private cloud (VPC) ID of the subnet group.

SubnetGroupStatus (string) --
Provides the status of the subnet group.

Subnets (list) --
Detailed information about one or more subnets within a subnet group.

(dict) --
Detailed information about a subnet.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the Availability Zone for the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.









Exceptions

DocDB.Client.exceptions.DBSubnetGroupNotFoundFault
DocDB.Client.exceptions.DBSubnetQuotaExceededFault
DocDB.Client.exceptions.SubnetAlreadyInUse
DocDB.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
DocDB.Client.exceptions.InvalidSubnet


    :return: {
        'DBSubnetGroup': {
            'DBSubnetGroupName': 'string',
            'DBSubnetGroupDescription': 'string',
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
            'DBSubnetGroupArn': 'string'
        }
    }
    
    
    :returns: 
    DocDB.Client.exceptions.DBSubnetGroupNotFoundFault
    DocDB.Client.exceptions.DBSubnetQuotaExceededFault
    DocDB.Client.exceptions.SubnetAlreadyInUse
    DocDB.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
    DocDB.Client.exceptions.InvalidSubnet
    
    """
    pass

def reboot_db_instance(DBInstanceIdentifier=None, ForceFailover=None):
    """
    You might need to reboot your instance, usually for maintenance reasons. For example, if you make certain changes, or if you change the cluster parameter group that is associated with the instance, you must reboot the instance for the changes to take effect.
    Rebooting an instance restarts the database engine service. Rebooting an instance results in a momentary outage, during which the instance status is set to rebooting .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reboot_db_instance(
        DBInstanceIdentifier='string',
        ForceFailover=True|False
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]\nThe instance identifier. This parameter is stored as a lowercase string.\nConstraints:\n\nMust match the identifier of an existing DBInstance .\n\n

    :type ForceFailover: boolean
    :param ForceFailover: When true , the reboot is conducted through a Multi-AZ failover.\nConstraint: You can\'t specify true if the instance is not configured for Multi-AZ.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBInstance': {
        'DBInstanceIdentifier': 'string',
        'DBInstanceClass': 'string',
        'Engine': 'string',
        'DBInstanceStatus': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123,
            'HostedZoneId': 'string'
        },
        'InstanceCreateTime': datetime(2015, 1, 1),
        'PreferredBackupWindow': 'string',
        'BackupRetentionPeriod': 123,
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'AvailabilityZone': 'string',
        'DBSubnetGroup': {
            'DBSubnetGroupName': 'string',
            'DBSubnetGroupDescription': 'string',
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
            'DBSubnetGroupArn': 'string'
        },
        'PreferredMaintenanceWindow': 'string',
        'PendingModifiedValues': {
            'DBInstanceClass': 'string',
            'AllocatedStorage': 123,
            'MasterUserPassword': 'string',
            'Port': 123,
            'BackupRetentionPeriod': 123,
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'LicenseModel': 'string',
            'Iops': 123,
            'DBInstanceIdentifier': 'string',
            'StorageType': 'string',
            'CACertificateIdentifier': 'string',
            'DBSubnetGroupName': 'string',
            'PendingCloudwatchLogsExports': {
                'LogTypesToEnable': [
                    'string',
                ],
                'LogTypesToDisable': [
                    'string',
                ]
            }
        },
        'LatestRestorableTime': datetime(2015, 1, 1),
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'PubliclyAccessible': True|False,
        'StatusInfos': [
            {
                'StatusType': 'string',
                'Normal': True|False,
                'Status': 'string',
                'Message': 'string'
            },
        ],
        'DBClusterIdentifier': 'string',
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DbiResourceId': 'string',
        'CACertificateIdentifier': 'string',
        'PromotionTier': 123,
        'DBInstanceArn': 'string',
        'EnabledCloudwatchLogsExports': [
            'string',
        ]
    }
}


Response Structure

(dict) --

DBInstance (dict) --
Detailed information about an instance.

DBInstanceIdentifier (string) --
Contains a user-provided database identifier. This identifier is the unique key that identifies an instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the instance.

Engine (string) --
Provides the name of the database engine to be used for this instance.

DBInstanceStatus (string) --
Specifies the current state of this database.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



InstanceCreateTime (datetime) --
Provides the date and time that the instance was created.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

VpcSecurityGroups (list) --
Provides a list of VPC security group elements that the instance belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





AvailabilityZone (string) --
Specifies the name of the Availability Zone that the instance is located in.

DBSubnetGroup (dict) --
Specifies information on the subnet group that is associated with the instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --
The name of the subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the subnet group.

VpcId (string) --
Provides the virtual private cloud (VPC) ID of the subnet group.

SubnetGroupStatus (string) --
Provides the status of the subnet group.

Subnets (list) --
Detailed information about one or more subnets within a subnet group.

(dict) --
Detailed information about a subnet.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the Availability Zone for the subnet.

Name (string) --
The name of the Availability Zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --
Specifies that changes to the instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --
Contains the new DBInstanceClass for the instance that will be applied or is currently being applied.

AllocatedStorage (integer) --
Contains the new AllocatedStorage size for then instance that will be applied or is currently being applied.

MasterUserPassword (string) --
Contains the pending or currently in-progress change of the master credentials for the instance.

Port (integer) --
Specifies the pending port for the instance.

BackupRetentionPeriod (integer) --
Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --
Indicates that the Single-AZ instance is to change to a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

LicenseModel (string) --
The license model for the instance.
Valid values: license-included , bring-your-own-license , general-public-license

Iops (integer) --
Specifies the new Provisioned IOPS value for the instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --
Contains the new DBInstanceIdentifier for the instance that will be applied or is currently being applied.

StorageType (string) --
Specifies the storage type to be associated with the instance.

CACertificateIdentifier (string) --
Specifies the identifier of the certificate authority (CA) certificate for the DB instance.

DBSubnetGroupName (string) --
The new subnet group for the instance.

PendingCloudwatchLogsExports (dict) --
A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.

LogTypesToEnable (list) --
Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --
Log types that are in the process of being enabled. After they are enabled, these log types are exported to Amazon CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

EngineVersion (string) --
Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --
Indicates that minor version patches are applied automatically.

PubliclyAccessible (boolean) --
Not supported. Amazon DocumentDB does not currently support public endpoints. The value of PubliclyAccessible is always false .

StatusInfos (list) --
The status of a read replica. If the instance is not a read replica, this is blank.

(dict) --
Provides a list of status information for an instance.

StatusType (string) --
This value is currently "read replication ."

Normal (boolean) --
A Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --
Status of the instance. For a StatusType of read replica, the values can be replicating , error, stopped , or terminated .

Message (string) --
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





DBClusterIdentifier (string) --
Contains the name of the cluster that the instance is a member of if the instance is a member of a cluster.

StorageEncrypted (boolean) --
Specifies whether or not the instance is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted instance.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the instance is accessed.

CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --
The Amazon Resource Name (ARN) for the instance.

EnabledCloudwatchLogsExports (list) --
A list of log types that this instance is configured to export to Amazon CloudWatch Logs.

(string) --










Exceptions

DocDB.Client.exceptions.InvalidDBInstanceStateFault
DocDB.Client.exceptions.DBInstanceNotFoundFault


    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'AvailabilityZone': 'string',
            'DBSubnetGroup': {
                'DBSubnetGroupName': 'string',
                'DBSubnetGroupDescription': 'string',
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
                'DBSubnetGroupArn': 'string'
            },
            'PreferredMaintenanceWindow': 'string',
            'PendingModifiedValues': {
                'DBInstanceClass': 'string',
                'AllocatedStorage': 123,
                'MasterUserPassword': 'string',
                'Port': 123,
                'BackupRetentionPeriod': 123,
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'LicenseModel': 'string',
                'Iops': 123,
                'DBInstanceIdentifier': 'string',
                'StorageType': 'string',
                'CACertificateIdentifier': 'string',
                'DBSubnetGroupName': 'string',
                'PendingCloudwatchLogsExports': {
                    'LogTypesToEnable': [
                        'string',
                    ],
                    'LogTypesToDisable': [
                        'string',
                    ]
                }
            },
            'LatestRestorableTime': datetime(2015, 1, 1),
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def remove_tags_from_resource(ResourceName=None, TagKeys=None):
    """
    Removes metadata tags from an Amazon DocumentDB resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_tags_from_resource(
        ResourceName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe Amazon DocumentDB resource that the tags are removed from. This value is an Amazon Resource Name (ARN).\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag key (name) of the tag to be removed.\n\n(string) --\n\n

    :returns: 
    DocDB.Client.exceptions.DBInstanceNotFoundFault
    DocDB.Client.exceptions.DBSnapshotNotFoundFault
    DocDB.Client.exceptions.DBClusterNotFoundFault
    
    """
    pass

def reset_db_cluster_parameter_group(DBClusterParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    Modifies the parameters of a cluster parameter group to the default value. To reset specific parameters, submit a list of the following: ParameterName and ApplyMethod . To reset the entire cluster parameter group, specify the DBClusterParameterGroupName and ResetAllParameters parameters.
    When you reset the entire group, dynamic parameters are updated immediately and static parameters are set to pending-reboot to take effect on the next DB instance reboot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reset_db_cluster_parameter_group(
        DBClusterParameterGroupName='string',
        ResetAllParameters=True|False,
        Parameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string',
                'Description': 'string',
                'Source': 'string',
                'ApplyType': 'string',
                'DataType': 'string',
                'AllowedValues': 'string',
                'IsModifiable': True|False,
                'MinimumEngineVersion': 'string',
                'ApplyMethod': 'immediate'|'pending-reboot'
            },
        ]
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of the cluster parameter group to reset.\n

    :type ResetAllParameters: boolean
    :param ResetAllParameters: A value that is set to true to reset all parameters in the cluster parameter group to their default values, and false otherwise. You can\'t use this parameter if there is a list of parameter names specified for the Parameters parameter.

    :type Parameters: list
    :param Parameters: A list of parameter names in the cluster parameter group to reset to the default values. You can\'t use this parameter if the ResetAllParameters parameter is set to true .\n\n(dict) --Detailed information about an individual parameter.\n\nParameterName (string) --Specifies the name of the parameter.\n\nParameterValue (string) --Specifies the value of the parameter.\n\nDescription (string) --Provides a description of the parameter.\n\nSource (string) --Indicates the source of the parameter value.\n\nApplyType (string) --Specifies the engine-specific parameters type.\n\nDataType (string) --Specifies the valid data type for the parameter.\n\nAllowedValues (string) --Specifies the valid range of values for the parameter.\n\nIsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.\n\nMinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.\n\nApplyMethod (string) --Indicates when to apply parameter updates.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBClusterParameterGroupName': 'string'
}


Response Structure

(dict) --
Contains the name of a cluster parameter group.

DBClusterParameterGroupName (string) --
The name of a cluster parameter group.
Constraints:

Must be from 1 to 255 letters or numbers.
The first character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.


Note
This value is stored as a lowercase string.








Exceptions

DocDB.Client.exceptions.InvalidDBParameterGroupStateFault
DocDB.Client.exceptions.DBParameterGroupNotFoundFault


    :return: {
        'DBClusterParameterGroupName': 'string'
    }
    
    
    :returns: 
    Must be from 1 to 255 letters or numbers.
    The first character must be a letter.
    Cannot end with a hyphen or contain two consecutive hyphens.
    
    """
    pass

def restore_db_cluster_from_snapshot(AvailabilityZones=None, DBClusterIdentifier=None, SnapshotIdentifier=None, Engine=None, EngineVersion=None, Port=None, DBSubnetGroupName=None, VpcSecurityGroupIds=None, Tags=None, KmsKeyId=None, EnableCloudwatchLogsExports=None, DeletionProtection=None):
    """
    Creates a new cluster from a snapshot or cluster snapshot.
    If a snapshot is specified, the target cluster is created from the source DB snapshot with a default configuration and default security group.
    If a cluster snapshot is specified, the target cluster is created from the source cluster restore point with the same configuration as the original source DB cluster, except that the new cluster is created with the default security group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_db_cluster_from_snapshot(
        AvailabilityZones=[
            'string',
        ],
        DBClusterIdentifier='string',
        SnapshotIdentifier='string',
        Engine='string',
        EngineVersion='string',
        Port=123,
        DBSubnetGroupName='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        KmsKeyId='string',
        EnableCloudwatchLogsExports=[
            'string',
        ],
        DeletionProtection=True|False
    )
    
    
    :type AvailabilityZones: list
    :param AvailabilityZones: Provides the list of Amazon EC2 Availability Zones that instances in the restored DB cluster can be created in.\n\n(string) --\n\n

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe name of the cluster to create from the snapshot or cluster snapshot. This parameter isn\'t case sensitive.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-snapshot-id\n

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]\nThe identifier for the snapshot or cluster snapshot to restore from.\nYou can use either the name or the Amazon Resource Name (ARN) to specify a cluster snapshot. However, you can use only the ARN to specify a snapshot.\nConstraints:\n\nMust match the identifier of an existing snapshot.\n\n

    :type Engine: string
    :param Engine: [REQUIRED]\nThe database engine to use for the new cluster.\nDefault: The same as source.\nConstraint: Must be compatible with the engine of the source.\n

    :type EngineVersion: string
    :param EngineVersion: The version of the database engine to use for the new cluster.

    :type Port: integer
    :param Port: The port number on which the new cluster accepts connections.\nConstraints: Must be a value from 1150 to 65535 .\nDefault: The same port as the original cluster.\n

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The name of the subnet group to use for the new cluster.\nConstraints: If provided, must match the name of an existing DBSubnetGroup .\nExample: mySubnetgroup\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of virtual private cloud (VPC) security groups that the new cluster will belong to.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: The tags to be assigned to the restored cluster.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier to use when restoring an encrypted cluster from a DB snapshot or cluster snapshot.\nThe AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are restoring a cluster with the same AWS account that owns the AWS KMS encryption key used to encrypt the new cluster, then you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.\nIf you do not specify a value for the KmsKeyId parameter, then the following occurs:\n\nIf the snapshot or cluster snapshot in SnapshotIdentifier is encrypted, then the restored cluster is encrypted using the AWS KMS key that was used to encrypt the snapshot or the cluster snapshot.\nIf the snapshot or the cluster snapshot in SnapshotIdentifier is not encrypted, then the restored DB cluster is not encrypted.\n\n

    :type EnableCloudwatchLogsExports: list
    :param EnableCloudwatchLogsExports: A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.\n\n(string) --\n\n

    :type DeletionProtection: boolean
    :param DeletionProtection: Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.

    :rtype: dict

ReturnsResponse Syntax
{
    'DBCluster': {
        'AvailabilityZones': [
            'string',
        ],
        'BackupRetentionPeriod': 123,
        'DBClusterIdentifier': 'string',
        'DBClusterParameterGroup': 'string',
        'DBSubnetGroup': 'string',
        'Status': 'string',
        'PercentProgress': 'string',
        'EarliestRestorableTime': datetime(2015, 1, 1),
        'Endpoint': 'string',
        'ReaderEndpoint': 'string',
        'MultiAZ': True|False,
        'Engine': 'string',
        'EngineVersion': 'string',
        'LatestRestorableTime': datetime(2015, 1, 1),
        'Port': 123,
        'MasterUsername': 'string',
        'PreferredBackupWindow': 'string',
        'PreferredMaintenanceWindow': 'string',
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
        ],
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBCluster (dict) --
Detailed information about a cluster.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier (string) --
Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup (string) --
Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
The earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint (string) --
The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master user name for the cluster.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

DBClusterMembers (list) --
Provides the list of instances that make up the cluster.

(dict) --
Contains information about an instance that is part of a cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the cluster.

IsClusterWriter (boolean) --
A value that is true if the cluster member is the primary instance for the cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. IAM roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the cluster. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB cluster.
INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.






ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.









Exceptions

DocDB.Client.exceptions.DBClusterAlreadyExistsFault
DocDB.Client.exceptions.DBClusterQuotaExceededFault
DocDB.Client.exceptions.StorageQuotaExceededFault
DocDB.Client.exceptions.DBSubnetGroupNotFoundFault
DocDB.Client.exceptions.DBSnapshotNotFoundFault
DocDB.Client.exceptions.DBClusterSnapshotNotFoundFault
DocDB.Client.exceptions.InsufficientDBClusterCapacityFault
DocDB.Client.exceptions.InsufficientStorageClusterCapacityFault
DocDB.Client.exceptions.InvalidDBSnapshotStateFault
DocDB.Client.exceptions.InvalidDBClusterSnapshotStateFault
DocDB.Client.exceptions.StorageQuotaExceededFault
DocDB.Client.exceptions.InvalidVPCNetworkStateFault
DocDB.Client.exceptions.InvalidRestoreFault
DocDB.Client.exceptions.DBSubnetGroupNotFoundFault
DocDB.Client.exceptions.InvalidSubnet
DocDB.Client.exceptions.KMSKeyNotAccessibleFault


    :return: {
        'DBCluster': {
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
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
            ],
            'ClusterCreateTime': datetime(2015, 1, 1),
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def restore_db_cluster_to_point_in_time(DBClusterIdentifier=None, SourceDBClusterIdentifier=None, RestoreToTime=None, UseLatestRestorableTime=None, Port=None, DBSubnetGroupName=None, VpcSecurityGroupIds=None, Tags=None, KmsKeyId=None, EnableCloudwatchLogsExports=None, DeletionProtection=None):
    """
    Restores a cluster to an arbitrary point in time. Users can restore to any point in time before LatestRestorableTime for up to BackupRetentionPeriod days. The target cluster is created from the source cluster with the same configuration as the original cluster, except that the new cluster is created with the default security group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_db_cluster_to_point_in_time(
        DBClusterIdentifier='string',
        SourceDBClusterIdentifier='string',
        RestoreToTime=datetime(2015, 1, 1),
        UseLatestRestorableTime=True|False,
        Port=123,
        DBSubnetGroupName='string',
        VpcSecurityGroupIds=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        KmsKeyId='string',
        EnableCloudwatchLogsExports=[
            'string',
        ],
        DeletionProtection=True|False
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe name of the new cluster to be created.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type SourceDBClusterIdentifier: string
    :param SourceDBClusterIdentifier: [REQUIRED]\nThe identifier of the source cluster from which to restore.\nConstraints:\n\nMust match the identifier of an existing DBCluster .\n\n

    :type RestoreToTime: datetime
    :param RestoreToTime: The date and time to restore the cluster to.\nValid values: A time in Universal Coordinated Time (UTC) format.\nConstraints:\n\nMust be before the latest restorable time for the instance.\nMust be specified if the UseLatestRestorableTime parameter is not provided.\nCannot be specified if the UseLatestRestorableTime parameter is true .\nCannot be specified if the RestoreType parameter is copy-on-write .\n\nExample: 2015-03-07T23:45:00Z\n

    :type UseLatestRestorableTime: boolean
    :param UseLatestRestorableTime: A value that is set to true to restore the cluster to the latest restorable backup time, and false otherwise.\nDefault: false\nConstraints: Cannot be specified if the RestoreToTime parameter is provided.\n

    :type Port: integer
    :param Port: The port number on which the new cluster accepts connections.\nConstraints: Must be a value from 1150 to 65535 .\nDefault: The default port for the engine.\n

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The subnet group name to use for the new cluster.\nConstraints: If provided, must match the name of an existing DBSubnetGroup .\nExample: mySubnetgroup\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of VPC security groups that the new cluster belongs to.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: The tags to be assigned to the restored cluster.\n\n(dict) --Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.\n\nKey (string) --The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can contain only the set of Unicode letters, digits, white space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier to use when restoring an encrypted cluster from an encrypted cluster.\nThe AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are restoring a cluster with the same AWS account that owns the AWS KMS encryption key used to encrypt the new cluster, then you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.\nYou can restore to a new cluster and encrypt the new cluster with an AWS KMS key that is different from the AWS KMS key used to encrypt the source cluster. The new DB cluster is encrypted with the AWS KMS key identified by the KmsKeyId parameter.\nIf you do not specify a value for the KmsKeyId parameter, then the following occurs:\n\nIf the cluster is encrypted, then the restored cluster is encrypted using the AWS KMS key that was used to encrypt the source cluster.\nIf the cluster is not encrypted, then the restored cluster is not encrypted.\n\nIf DBClusterIdentifier refers to a cluster that is not encrypted, then the restore request is rejected.\n

    :type EnableCloudwatchLogsExports: list
    :param EnableCloudwatchLogsExports: A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.\n\n(string) --\n\n

    :type DeletionProtection: boolean
    :param DeletionProtection: Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.

    :rtype: dict

ReturnsResponse Syntax
{
    'DBCluster': {
        'AvailabilityZones': [
            'string',
        ],
        'BackupRetentionPeriod': 123,
        'DBClusterIdentifier': 'string',
        'DBClusterParameterGroup': 'string',
        'DBSubnetGroup': 'string',
        'Status': 'string',
        'PercentProgress': 'string',
        'EarliestRestorableTime': datetime(2015, 1, 1),
        'Endpoint': 'string',
        'ReaderEndpoint': 'string',
        'MultiAZ': True|False,
        'Engine': 'string',
        'EngineVersion': 'string',
        'LatestRestorableTime': datetime(2015, 1, 1),
        'Port': 123,
        'MasterUsername': 'string',
        'PreferredBackupWindow': 'string',
        'PreferredMaintenanceWindow': 'string',
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
        ],
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBCluster (dict) --
Detailed information about a cluster.

AvailabilityZones (list) --
Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier (string) --
Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup (string) --
Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
The earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint (string) --
The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master user name for the cluster.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

DBClusterMembers (list) --
Provides the list of instances that make up the cluster.

(dict) --
Contains information about an instance that is part of a cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the cluster.

IsClusterWriter (boolean) --
A value that is true if the cluster member is the primary instance for the cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(dict) --
Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. IAM roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the cluster. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB cluster.
INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.






ClusterCreateTime (datetime) --
Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.









Exceptions

DocDB.Client.exceptions.DBClusterAlreadyExistsFault
DocDB.Client.exceptions.DBClusterNotFoundFault
DocDB.Client.exceptions.DBClusterQuotaExceededFault
DocDB.Client.exceptions.DBClusterSnapshotNotFoundFault
DocDB.Client.exceptions.DBSubnetGroupNotFoundFault
DocDB.Client.exceptions.InsufficientDBClusterCapacityFault
DocDB.Client.exceptions.InsufficientStorageClusterCapacityFault
DocDB.Client.exceptions.InvalidDBClusterSnapshotStateFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.InvalidDBSnapshotStateFault
DocDB.Client.exceptions.InvalidRestoreFault
DocDB.Client.exceptions.InvalidSubnet
DocDB.Client.exceptions.InvalidVPCNetworkStateFault
DocDB.Client.exceptions.KMSKeyNotAccessibleFault
DocDB.Client.exceptions.StorageQuotaExceededFault


    :return: {
        'DBCluster': {
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
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
            ],
            'ClusterCreateTime': datetime(2015, 1, 1),
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def start_db_cluster(DBClusterIdentifier=None):
    """
    Restarts the stopped cluster that is specified by DBClusterIdentifier . For more information, see Stopping and Starting an Amazon DocumentDB Cluster .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_db_cluster(
        DBClusterIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe identifier of the cluster to restart. Example: docdb-2019-05-28-15-24-52\n

    :rtype: dict
ReturnsResponse Syntax{
    'DBCluster': {
        'AvailabilityZones': [
            'string',
        ],
        'BackupRetentionPeriod': 123,
        'DBClusterIdentifier': 'string',
        'DBClusterParameterGroup': 'string',
        'DBSubnetGroup': 'string',
        'Status': 'string',
        'PercentProgress': 'string',
        'EarliestRestorableTime': datetime(2015, 1, 1),
        'Endpoint': 'string',
        'ReaderEndpoint': 'string',
        'MultiAZ': True|False,
        'Engine': 'string',
        'EngineVersion': 'string',
        'LatestRestorableTime': datetime(2015, 1, 1),
        'Port': 123,
        'MasterUsername': 'string',
        'PreferredBackupWindow': 'string',
        'PreferredMaintenanceWindow': 'string',
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
        ],
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --
DBCluster (dict) --Detailed information about a cluster.

AvailabilityZones (list) --Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier (string) --Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup (string) --Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup (string) --Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status (string) --Specifies the current state of this cluster.

PercentProgress (string) --Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --The earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint (string) --The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --Specifies whether the cluster has instances in multiple Availability Zones.

Engine (string) --Provides the name of the database engine to be used for this cluster.

EngineVersion (string) --Indicates the database engine version.

LatestRestorableTime (datetime) --Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --Specifies the port that the database engine is listening on.

MasterUsername (string) --Contains the master user name for the cluster.

PreferredBackupWindow (string) --Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

DBClusterMembers (list) --Provides the list of instances that make up the cluster.

(dict) --Contains information about an instance that is part of a cluster.

DBInstanceIdentifier (string) --Specifies the instance identifier for this member of the cluster.

IsClusterWriter (boolean) --A value that is true if the cluster member is the primary instance for the cluster and false otherwise.

DBClusterParameterGroupStatus (string) --Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(dict) --Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --The name of the VPC security group.

Status (string) --The status of the VPC security group.





HostedZoneId (string) --Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --Specifies whether the cluster is encrypted.

KmsKeyId (string) --If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster.

DbClusterResourceId (string) --The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.

DBClusterArn (string) --The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles (list) --Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. IAM roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.

(dict) --Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --Describes the state of association between the IAM role and the cluster. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB cluster.
INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.






ClusterCreateTime (datetime) --Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string) --


DeletionProtection (boolean) --Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.








Exceptions

DocDB.Client.exceptions.DBClusterNotFoundFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.InvalidDBInstanceStateFault


    :return: {
        'DBCluster': {
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
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
            ],
            'ClusterCreateTime': datetime(2015, 1, 1),
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
    PENDING - The IAM role ARN is being associated with the DB cluster.
    INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.
    
    """
    pass

def stop_db_cluster(DBClusterIdentifier=None):
    """
    Stops the running cluster that is specified by DBClusterIdentifier . The cluster must be in the available state. For more information, see Stopping and Starting an Amazon DocumentDB Cluster .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_db_cluster(
        DBClusterIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe identifier of the cluster to stop. Example: docdb-2019-05-28-15-24-52\n

    :rtype: dict
ReturnsResponse Syntax{
    'DBCluster': {
        'AvailabilityZones': [
            'string',
        ],
        'BackupRetentionPeriod': 123,
        'DBClusterIdentifier': 'string',
        'DBClusterParameterGroup': 'string',
        'DBSubnetGroup': 'string',
        'Status': 'string',
        'PercentProgress': 'string',
        'EarliestRestorableTime': datetime(2015, 1, 1),
        'Endpoint': 'string',
        'ReaderEndpoint': 'string',
        'MultiAZ': True|False,
        'Engine': 'string',
        'EngineVersion': 'string',
        'LatestRestorableTime': datetime(2015, 1, 1),
        'Port': 123,
        'MasterUsername': 'string',
        'PreferredBackupWindow': 'string',
        'PreferredMaintenanceWindow': 'string',
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
        ],
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --
DBCluster (dict) --Detailed information about a cluster.

AvailabilityZones (list) --Provides the list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --Specifies the number of days for which automatic snapshots are retained.

DBClusterIdentifier (string) --Contains a user-supplied cluster identifier. This identifier is the unique key that identifies a cluster.

DBClusterParameterGroup (string) --Specifies the name of the cluster parameter group for the cluster.

DBSubnetGroup (string) --Specifies information on the subnet group that is associated with the cluster, including the name, description, and subnets in the subnet group.

Status (string) --Specifies the current state of this cluster.

PercentProgress (string) --Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --The earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --Specifies the connection endpoint for the primary instance of the cluster.

ReaderEndpoint (string) --The reader endpoint for the cluster. The reader endpoint for a cluster load balances connections across the Amazon DocumentDB replicas that are available in a cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB distributes the connection requests among the Amazon DocumentDB replicas in the cluster. This functionality can help balance your read workload across multiple Amazon DocumentDB replicas in your cluster.
If a failover occurs, and the Amazon DocumentDB replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --Specifies whether the cluster has instances in multiple Availability Zones.

Engine (string) --Provides the name of the database engine to be used for this cluster.

EngineVersion (string) --Indicates the database engine version.

LatestRestorableTime (datetime) --Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --Specifies the port that the database engine is listening on.

MasterUsername (string) --Contains the master user name for the cluster.

PreferredBackupWindow (string) --Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

DBClusterMembers (list) --Provides the list of instances that make up the cluster.

(dict) --Contains information about an instance that is part of a cluster.

DBInstanceIdentifier (string) --Specifies the instance identifier for this member of the cluster.

IsClusterWriter (boolean) --A value that is true if the cluster member is the primary instance for the cluster and false otherwise.

DBClusterParameterGroupStatus (string) --Specifies the status of the cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --Provides a list of virtual private cloud (VPC) security groups that the cluster belongs to.

(dict) --Used as a response element for queries on virtual private cloud (VPC) security group membership.

VpcSecurityGroupId (string) --The name of the VPC security group.

Status (string) --The status of the VPC security group.





HostedZoneId (string) --Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --Specifies whether the cluster is encrypted.

KmsKeyId (string) --If StorageEncrypted is true , the AWS KMS key identifier for the encrypted cluster.

DbClusterResourceId (string) --The AWS Region-unique, immutable identifier for the cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the cluster is accessed.

DBClusterArn (string) --The Amazon Resource Name (ARN) for the cluster.

AssociatedRoles (list) --Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the cluster. IAM roles that are associated with a cluster grant permission for the cluster to access other AWS services on your behalf.

(dict) --Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --Describes the state of association between the IAM role and the cluster. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB cluster.
INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.






ClusterCreateTime (datetime) --Specifies the time when the cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --A list of log types that this cluster is configured to export to Amazon CloudWatch Logs.

(string) --


DeletionProtection (boolean) --Specifies whether this cluster can be deleted. If DeletionProtection is enabled, the cluster cannot be deleted unless it is modified and DeletionProtection is disabled. DeletionProtection protects clusters from being accidentally deleted.








Exceptions

DocDB.Client.exceptions.DBClusterNotFoundFault
DocDB.Client.exceptions.InvalidDBClusterStateFault
DocDB.Client.exceptions.InvalidDBInstanceStateFault


    :return: {
        'DBCluster': {
            'AvailabilityZones': [
                'string',
            ],
            'BackupRetentionPeriod': 123,
            'DBClusterIdentifier': 'string',
            'DBClusterParameterGroup': 'string',
            'DBSubnetGroup': 'string',
            'Status': 'string',
            'PercentProgress': 'string',
            'EarliestRestorableTime': datetime(2015, 1, 1),
            'Endpoint': 'string',
            'ReaderEndpoint': 'string',
            'MultiAZ': True|False,
            'Engine': 'string',
            'EngineVersion': 'string',
            'LatestRestorableTime': datetime(2015, 1, 1),
            'Port': 123,
            'MasterUsername': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
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
            ],
            'ClusterCreateTime': datetime(2015, 1, 1),
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    ACTIVE - The IAM role ARN is associated with the cluster and can be used to access other AWS services on your behalf.
    PENDING - The IAM role ARN is being associated with the DB cluster.
    INVALID - The IAM role ARN is associated with the cluster, but the cluster cannot assume the IAM role to access other AWS services on your behalf.
    
    """
    pass

