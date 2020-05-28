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

def add_role_to_db_cluster(DBClusterIdentifier=None, RoleArn=None):
    """
    Associates an Identity and Access Management (IAM) role from an Neptune DB cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_role_to_db_cluster(
        DBClusterIdentifier='string',
        RoleArn='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe name of the DB cluster to associate the IAM role with.\n

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM role to associate with the Neptune DB cluster, for example arn:aws:iam::123456789012:role/NeptuneAccessRole .\n

    :returns: 
    Neptune.Client.exceptions.DBClusterNotFoundFault
    Neptune.Client.exceptions.DBClusterRoleAlreadyExistsFault
    Neptune.Client.exceptions.InvalidDBClusterStateFault
    Neptune.Client.exceptions.DBClusterRoleQuotaExceededFault
    
    """
    pass

def add_source_identifier_to_subscription(SubscriptionName=None, SourceIdentifier=None):
    """
    Adds a source identifier to an existing event notification subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_source_identifier_to_subscription(
        SubscriptionName='string',
        SourceIdentifier='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]\nThe name of the event notification subscription you want to add a source identifier to.\n

    :type SourceIdentifier: string
    :param SourceIdentifier: [REQUIRED]\nThe identifier of the event source to be added.\nConstraints:\n\nIf the source type is a DB instance, then a DBInstanceIdentifier must be supplied.\nIf the source type is a DB security group, a DBSecurityGroupName must be supplied.\nIf the source type is a DB parameter group, a DBParameterGroupName must be supplied.\nIf the source type is a DB snapshot, a DBSnapshotIdentifier must be supplied.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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

EventSubscription (dict) --
Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

CustomerAwsId (string) --
The AWS customer account associated with the event notification subscription.

CustSubscriptionId (string) --
The event notification subscription Id.

SnsTopicArn (string) --
The topic ARN of the event notification subscription.

Status (string) --
The status of the event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that Neptune no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --
The time the event notification subscription was created.

SourceType (string) --
The source type for the event notification subscription.

SourceIdsList (list) --
A list of source IDs for the event notification subscription.

(string) --


EventCategoriesList (list) --
A list of event categories for the event notification subscription.

(string) --


Enabled (boolean) --
A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.

EventSubscriptionArn (string) --
The Amazon Resource Name (ARN) for the event subscription.









Exceptions

Neptune.Client.exceptions.SubscriptionNotFoundFault
Neptune.Client.exceptions.SourceNotFoundFault


    :return: {
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
    
    
    :returns: 
    (string) --
    
    """
    pass

def add_tags_to_resource(ResourceName=None, Tags=None):
    """
    Adds metadata tags to an Amazon Neptune resource. These tags can also be used with cost allocation reporting to track cost associated with Amazon Neptune resources, or used in a Condition statement in an IAM policy for Amazon Neptune.
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
    :param ResourceName: [REQUIRED]\nThe Amazon Neptune resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to be assigned to the Amazon Neptune resource.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :returns: 
    Neptune.Client.exceptions.DBInstanceNotFoundFault
    Neptune.Client.exceptions.DBSnapshotNotFoundFault
    Neptune.Client.exceptions.DBClusterNotFoundFault
    
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
    :param ResourceIdentifier: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .\n

    :type ApplyAction: string
    :param ApplyAction: [REQUIRED]\nThe pending maintenance action to apply to this resource.\nValid values: system-update , db-upgrade\n

    :type OptInType: string
    :param OptInType: [REQUIRED]\nA value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type immediate can\'t be undone.\nValid values:\n\nimmediate - Apply the maintenance action immediately.\nnext-maintenance - Apply the maintenance action during the next maintenance window for the resource.\nundo-opt-in - Cancel any existing next-maintenance opt-in requests.\n\n

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
Describes the pending maintenance actions for a resource.

ResourceIdentifier (string) --
The ARN of the resource that has pending maintenance actions.

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
The effective date when the pending maintenance action is applied to the resource. This date takes into account opt-in requests received from the  ApplyPendingMaintenanceAction API, the AutoAppliedAfterDate , and the ForcedApplyDate . This value is blank if an opt-in request has not been received and nothing has been specified as AutoAppliedAfterDate or ForcedApplyDate .

Description (string) --
A description providing more detail about the maintenance action.













Exceptions

Neptune.Client.exceptions.ResourceNotFoundFault


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
    Neptune.Client.exceptions.ResourceNotFoundFault
    
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
    Copies the specified DB cluster parameter group.
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
    :param SourceDBClusterParameterGroupIdentifier: [REQUIRED]\nThe identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .\nConstraints:\n\nMust specify a valid DB cluster parameter group.\nIf the source DB cluster parameter group is in the same AWS Region as the copy, specify a valid DB parameter group identifier, for example my-db-cluster-param-group , or a valid ARN.\nIf the source DB parameter group is in a different AWS Region than the copy, specify a valid DB cluster parameter group ARN, for example arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1 .\n\n

    :type TargetDBClusterParameterGroupIdentifier: string
    :param TargetDBClusterParameterGroupIdentifier: [REQUIRED]\nThe identifier for the copied DB cluster parameter group.\nConstraints:\n\nCannot be null, empty, or blank\nMust contain from 1 to 255 letters, numbers, or hyphens\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\nExample: my-cluster-param-group1\n

    :type TargetDBClusterParameterGroupDescription: string
    :param TargetDBClusterParameterGroupDescription: [REQUIRED]\nA description for the copied DB cluster parameter group.\n

    :type Tags: list
    :param Tags: The tags to be assigned to the copied DB cluster parameter group.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

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
Contains the details of an Amazon Neptune DB cluster parameter group.
This data type is used as a response element in the  DescribeDBClusterParameterGroups action.

DBClusterParameterGroupName (string) --
Provides the name of the DB cluster parameter group.

DBParameterGroupFamily (string) --
Provides the name of the DB parameter group family that this DB cluster parameter group is compatible with.

Description (string) --
Provides the customer-specified description for this DB cluster parameter group.

DBClusterParameterGroupArn (string) --
The Amazon Resource Name (ARN) for the DB cluster parameter group.









Exceptions

Neptune.Client.exceptions.DBParameterGroupNotFoundFault
Neptune.Client.exceptions.DBParameterGroupQuotaExceededFault
Neptune.Client.exceptions.DBParameterGroupAlreadyExistsFault


    :return: {
        'DBClusterParameterGroup': {
            'DBClusterParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBClusterParameterGroupArn': 'string'
        }
    }
    
    
    :returns: 
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    Neptune.Client.exceptions.DBParameterGroupQuotaExceededFault
    Neptune.Client.exceptions.DBParameterGroupAlreadyExistsFault
    
    """
    pass

def copy_db_cluster_snapshot(SourceDBClusterSnapshotIdentifier=None, TargetDBClusterSnapshotIdentifier=None, KmsKeyId=None, PreSignedUrl=None, CopyTags=None, Tags=None, SourceRegion=None):
    """
    Copies a snapshot of a DB cluster.
    To copy a DB cluster snapshot from a shared manual DB cluster snapshot, SourceDBClusterSnapshotIdentifier must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.copy_db_cluster_snapshot(
        SourceDBClusterSnapshotIdentifier='string',
        TargetDBClusterSnapshotIdentifier='string',
        KmsKeyId='string',
        CopyTags=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        SourceRegion='string'
    )
    
    
    :type SourceDBClusterSnapshotIdentifier: string
    :param SourceDBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier of the DB cluster snapshot to copy. This parameter is not case-sensitive.\nYou can\'t copy from one AWS Region to another.\nConstraints:\n\nMust specify a valid system snapshot in the 'available' state.\nSpecify a valid DB snapshot identifier.\n\nExample: my-cluster-snapshot1\n

    :type TargetDBClusterSnapshotIdentifier: string
    :param TargetDBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case-sensitive.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-cluster-snapshot2\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS AWS KMS key ID for an encrypted DB cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.\nIf you copy an encrypted DB cluster snapshot from your AWS account, you can specify a value for KmsKeyId to encrypt the copy with a new KMS encryption key. If you don\'t specify a value for KmsKeyId , then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot.\nIf you copy an encrypted DB cluster snapshot that is shared from another AWS account, then you must specify a value for KmsKeyId .\nKMS encryption keys are specific to the AWS Region that they are created in, and you can\'t use encryption keys from one AWS Region in another AWS Region.\nYou cannot encrypt an unencrypted DB cluster snapshot when you copy it. If you try to copy an unencrypted DB cluster snapshot and specify a value for the KmsKeyId parameter, an error is returned.\n

    :type PreSignedUrl: string
    :param PreSignedUrl: Not currently supported.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type CopyTags: boolean
    :param CopyTags: True to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot, and otherwise false. The default is false.

    :type Tags: list
    :param Tags: The tags to assign to the new DB cluster snapshot copy.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type SourceRegion: string
    :param SourceRegion: The ID of the region that contains the snapshot to be copied.

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
        'DBClusterSnapshotArn': 'string',
        'SourceDBClusterSnapshotArn': 'string',
        'IAMDatabaseAuthenticationEnabled': True|False
    }
}


Response Structure

(dict) --

DBClusterSnapshot (dict) --
Contains the details for an Amazon Neptune DB cluster snapshot
This data type is used as a response element in the  DescribeDBClusterSnapshots action.

AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

(string) --


DBClusterSnapshotIdentifier (string) --
Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot.
After you restore a DB cluster using a DBClusterSnapshotIdentifier , you must specify the same DBClusterSnapshotIdentifier for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed.
However, if you don\'t specify the DBClusterSnapshotIdentifier , an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the DBClusterSnapshotIdentifier , and the original DB cluster is deleted.

DBClusterIdentifier (string) --
Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.

SnapshotCreateTime (datetime) --
Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

Engine (string) --
Specifies the name of the database engine.

AllocatedStorage (integer) --
Specifies the allocated storage size in gibibytes (GiB).

Status (string) --
Specifies the status of this DB cluster snapshot.

Port (integer) --
Specifies the port that the DB cluster was listening on at the time of the snapshot.

VpcId (string) --
Provides the VPC ID associated with the DB cluster snapshot.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

MasterUsername (string) --
Provides the master username for the DB cluster snapshot.

EngineVersion (string) --
Provides the version of the database engine for this DB cluster snapshot.

LicenseModel (string) --
Provides the license model information for this DB cluster snapshot.

SnapshotType (string) --
Provides the type of the DB cluster snapshot.

PercentProgress (integer) --
Specifies the percentage of the estimated data that has been transferred.

StorageEncrypted (boolean) --
Specifies whether the DB cluster snapshot is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

DBClusterSnapshotArn (string) --
The Amazon Resource Name (ARN) for the DB cluster snapshot.

SourceDBClusterSnapshotArn (string) --
If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.









Exceptions

Neptune.Client.exceptions.DBClusterSnapshotAlreadyExistsFault
Neptune.Client.exceptions.DBClusterSnapshotNotFoundFault
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.InvalidDBClusterSnapshotStateFault
Neptune.Client.exceptions.SnapshotQuotaExceededFault
Neptune.Client.exceptions.KMSKeyNotAccessibleFault


    :return: {
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
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def copy_db_parameter_group(SourceDBParameterGroupIdentifier=None, TargetDBParameterGroupIdentifier=None, TargetDBParameterGroupDescription=None, Tags=None):
    """
    Copies the specified DB parameter group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.copy_db_parameter_group(
        SourceDBParameterGroupIdentifier='string',
        TargetDBParameterGroupIdentifier='string',
        TargetDBParameterGroupDescription='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SourceDBParameterGroupIdentifier: string
    :param SourceDBParameterGroupIdentifier: [REQUIRED]\nThe identifier or ARN for the source DB parameter group. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .\nConstraints:\n\nMust specify a valid DB parameter group.\nMust specify a valid DB parameter group identifier, for example my-db-param-group , or a valid ARN.\n\n

    :type TargetDBParameterGroupIdentifier: string
    :param TargetDBParameterGroupIdentifier: [REQUIRED]\nThe identifier for the copied DB parameter group.\nConstraints:\n\nCannot be null, empty, or blank.\nMust contain from 1 to 255 letters, numbers, or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-db-parameter-group\n

    :type TargetDBParameterGroupDescription: string
    :param TargetDBParameterGroupDescription: [REQUIRED]\nA description for the copied DB parameter group.\n

    :type Tags: list
    :param Tags: The tags to be assigned to the copied DB parameter group.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBParameterGroup': {
        'DBParameterGroupName': 'string',
        'DBParameterGroupFamily': 'string',
        'Description': 'string',
        'DBParameterGroupArn': 'string'
    }
}


Response Structure

(dict) --

DBParameterGroup (dict) --
Contains the details of an Amazon Neptune DB parameter group.
This data type is used as a response element in the  DescribeDBParameterGroups action.

DBParameterGroupName (string) --
Provides the name of the DB parameter group.

DBParameterGroupFamily (string) --
Provides the name of the DB parameter group family that this DB parameter group is compatible with.

Description (string) --
Provides the customer-specified description for this DB parameter group.

DBParameterGroupArn (string) --
The Amazon Resource Name (ARN) for the DB parameter group.









Exceptions

Neptune.Client.exceptions.DBParameterGroupNotFoundFault
Neptune.Client.exceptions.DBParameterGroupAlreadyExistsFault
Neptune.Client.exceptions.DBParameterGroupQuotaExceededFault


    :return: {
        'DBParameterGroup': {
            'DBParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBParameterGroupArn': 'string'
        }
    }
    
    
    :returns: 
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    Neptune.Client.exceptions.DBParameterGroupAlreadyExistsFault
    Neptune.Client.exceptions.DBParameterGroupQuotaExceededFault
    
    """
    pass

def create_db_cluster(AvailabilityZones=None, BackupRetentionPeriod=None, CharacterSetName=None, DatabaseName=None, DBClusterIdentifier=None, DBClusterParameterGroupName=None, VpcSecurityGroupIds=None, DBSubnetGroupName=None, Engine=None, EngineVersion=None, Port=None, MasterUsername=None, MasterUserPassword=None, OptionGroupName=None, PreferredBackupWindow=None, PreferredMaintenanceWindow=None, ReplicationSourceIdentifier=None, Tags=None, StorageEncrypted=None, KmsKeyId=None, PreSignedUrl=None, EnableIAMDatabaseAuthentication=None, EnableCloudwatchLogsExports=None, DeletionProtection=None, SourceRegion=None):
    """
    Creates a new Amazon Neptune DB cluster.
    You can use the ReplicationSourceIdentifier parameter to create the DB cluster as a Read Replica of another DB cluster or Amazon Neptune DB instance.
    Note that when you create a new cluster using CreateDBCluster directly, deletion protection is disabled by default (when you create a new production cluster in the console, deletion protection is enabled by default). You can only delete a DB cluster if its DeletionProtection field is set to false .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_db_cluster(
        AvailabilityZones=[
            'string',
        ],
        BackupRetentionPeriod=123,
        CharacterSetName='string',
        DatabaseName='string',
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
        OptionGroupName='string',
        PreferredBackupWindow='string',
        PreferredMaintenanceWindow='string',
        ReplicationSourceIdentifier='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        StorageEncrypted=True|False,
        KmsKeyId='string',
        EnableIAMDatabaseAuthentication=True|False,
        EnableCloudwatchLogsExports=[
            'string',
        ],
        DeletionProtection=True|False,
        SourceRegion='string'
    )
    
    
    :type AvailabilityZones: list
    :param AvailabilityZones: A list of EC2 Availability Zones that instances in the DB cluster can be created in.\n\n(string) --\n\n

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: The number of days for which automated backups are retained. You must specify a minimum value of 1.\nDefault: 1\nConstraints:\n\nMust be a value from 1 to 35\n\n

    :type CharacterSetName: string
    :param CharacterSetName: (Not supported by Neptune)

    :type DatabaseName: string
    :param DatabaseName: The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon Neptune will not create a database in the DB cluster you are creating.

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe DB cluster identifier. This parameter is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-cluster1\n

    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted, the default is used.\nConstraints:\n\nIf supplied, must match the name of an existing DBClusterParameterGroup.\n\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to associate with this DB cluster.\n\n(string) --\n\n

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: A DB subnet group to associate with this DB cluster.\nConstraints: Must match the name of an existing DBSubnetGroup. Must not be default.\nExample: mySubnetgroup\n

    :type Engine: string
    :param Engine: [REQUIRED]\nThe name of the database engine to be used for this DB cluster.\nValid Values: neptune\n

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine to use. Currently, setting this parameter has no effect.\nExample: 1.0.1\n

    :type Port: integer
    :param Port: The port number on which the instances in the DB cluster accept connections.\nDefault: 8182\n

    :type MasterUsername: string
    :param MasterUsername: The name of the master user for the DB cluster.\nConstraints:\n\nMust be 1 to 16 letters or numbers.\nFirst character must be a letter.\nCannot be a reserved word for the chosen database engine.\n\n

    :type MasterUserPassword: string
    :param MasterUserPassword: The password for the master database user. This password can contain any printable ASCII character except '/', ''', or '@'.\nConstraints: Must contain from 8 to 41 characters.\n

    :type OptionGroupName: string
    :param OptionGroupName: (Not supported by Neptune)

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon Neptune User Guide.\nConstraints:\n\nMust be in the format hh24:mi-hh24:mi .\nMust be in Universal Coordinated Time (UTC).\nMust not conflict with the preferred maintenance window.\nMust be at least 30 minutes.\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).\nFormat: ddd:hh24:mi-ddd:hh24:mi\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred Maintenance Window in the Amazon Neptune User Guide.\nValid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.\nConstraints: Minimum 30-minute window.\n

    :type ReplicationSourceIdentifier: string
    :param ReplicationSourceIdentifier: The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.

    :type Tags: list
    :param Tags: The tags to assign to the new DB cluster.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type StorageEncrypted: boolean
    :param StorageEncrypted: Specifies whether the DB cluster is encrypted.

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier for an encrypted DB cluster.\nThe KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.\nIf an encryption key is not specified in KmsKeyId :\n\nIf ReplicationSourceIdentifier identifies an encrypted source, then Amazon Neptune will use the encryption key used to encrypt the source. Otherwise, Amazon Neptune will use your default encryption key.\nIf the StorageEncrypted parameter is true and ReplicationSourceIdentifier is not specified, then Amazon Neptune will use your default encryption key.\n\nAWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.\nIf you create a Read Replica of an encrypted DB cluster in another AWS Region, you must set KmsKeyId to a KMS key ID that is valid in the destination AWS Region. This key is used to encrypt the Read Replica in that AWS Region.\n

    :type PreSignedUrl: string
    :param PreSignedUrl: This parameter is not currently supported.\n\nPlease note that this parameter is automatically populated if it is not provided. Including this parameter is not required\n

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.\nDefault: false\n

    :type EnableCloudwatchLogsExports: list
    :param EnableCloudwatchLogsExports: The list of log types that need to be enabled for exporting to CloudWatch Logs.\n\n(string) --\n\n

    :type DeletionProtection: boolean
    :param DeletionProtection: A value that indicates whether the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled. By default, deletion protection is enabled.

    :type SourceRegion: string
    :param SourceRegion: The ID of the region that contains the source for the db cluster.

    :rtype: dict

ReturnsResponse Syntax
{
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
        'MultiAZ': True|False,
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
        ],
        'IAMDatabaseAuthenticationEnabled': True|False,
        'CloneGroupId': 'string',
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
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --

AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.


AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --

(Not supported by Neptune)


DatabaseName (string) --
Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --
Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this DB cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --
The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --
Specifies the name of the DB cluster option group.

Status (string) --
Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --
Not supported by Neptune.

ReadReplicaIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --
Provides the list of instances that make up the DB cluster.

(dict) --
Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --
Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --
Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.









Exceptions

Neptune.Client.exceptions.DBClusterAlreadyExistsFault
Neptune.Client.exceptions.InsufficientStorageClusterCapacityFault
Neptune.Client.exceptions.DBClusterQuotaExceededFault
Neptune.Client.exceptions.StorageQuotaExceededFault
Neptune.Client.exceptions.DBSubnetGroupNotFoundFault
Neptune.Client.exceptions.InvalidVPCNetworkStateFault
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.InvalidDBSubnetGroupStateFault
Neptune.Client.exceptions.InvalidSubnet
Neptune.Client.exceptions.InvalidDBInstanceStateFault
Neptune.Client.exceptions.DBClusterParameterGroupNotFoundFault
Neptune.Client.exceptions.KMSKeyNotAccessibleFault
Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.DBInstanceNotFoundFault
Neptune.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs


    :return: {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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
    Creates a new DB cluster parameter group.
    Parameters in a DB cluster parameter group apply to all of the instances in a DB cluster.
    A DB cluster parameter group is initially created with the default parameters for the database engine used by instances in the DB cluster. To provide custom values for any of the parameters, you must modify the group after creating it using  ModifyDBClusterParameterGroup . Once you\'ve created a DB cluster parameter group, you need to associate it with your DB cluster using  ModifyDBCluster . When you associate a new DB cluster parameter group with a running DB cluster, you need to reboot the DB instances in the DB cluster without failover for the new DB cluster parameter group and associated settings to take effect.
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
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of the DB cluster parameter group.\nConstraints:\n\nMust match the name of an existing DBClusterParameterGroup.\n\n\nNote\nThis value is stored as a lowercase string.\n\n

    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: [REQUIRED]\nThe DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.\n

    :type Description: string
    :param Description: [REQUIRED]\nThe description for the DB cluster parameter group.\n

    :type Tags: list
    :param Tags: The tags to be assigned to the new DB cluster parameter group.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

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
Contains the details of an Amazon Neptune DB cluster parameter group.
This data type is used as a response element in the  DescribeDBClusterParameterGroups action.

DBClusterParameterGroupName (string) --
Provides the name of the DB cluster parameter group.

DBParameterGroupFamily (string) --
Provides the name of the DB parameter group family that this DB cluster parameter group is compatible with.

Description (string) --
Provides the customer-specified description for this DB cluster parameter group.

DBClusterParameterGroupArn (string) --
The Amazon Resource Name (ARN) for the DB cluster parameter group.









Exceptions

Neptune.Client.exceptions.DBParameterGroupQuotaExceededFault
Neptune.Client.exceptions.DBParameterGroupAlreadyExistsFault


    :return: {
        'DBClusterParameterGroup': {
            'DBClusterParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBClusterParameterGroupArn': 'string'
        }
    }
    
    
    :returns: 
    Neptune.Client.exceptions.DBParameterGroupQuotaExceededFault
    Neptune.Client.exceptions.DBParameterGroupAlreadyExistsFault
    
    """
    pass

def create_db_cluster_snapshot(DBClusterSnapshotIdentifier=None, DBClusterIdentifier=None, Tags=None):
    """
    Creates a snapshot of a DB cluster.
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
    :param DBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: my-cluster1-snapshot1\n

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe identifier of the DB cluster to create a snapshot for. This parameter is not case-sensitive.\nConstraints:\n\nMust match the identifier of an existing DBCluster.\n\nExample: my-cluster1\n

    :type Tags: list
    :param Tags: The tags to be assigned to the DB cluster snapshot.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

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
        'DBClusterSnapshotArn': 'string',
        'SourceDBClusterSnapshotArn': 'string',
        'IAMDatabaseAuthenticationEnabled': True|False
    }
}


Response Structure

(dict) --

DBClusterSnapshot (dict) --
Contains the details for an Amazon Neptune DB cluster snapshot
This data type is used as a response element in the  DescribeDBClusterSnapshots action.

AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

(string) --


DBClusterSnapshotIdentifier (string) --
Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot.
After you restore a DB cluster using a DBClusterSnapshotIdentifier , you must specify the same DBClusterSnapshotIdentifier for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed.
However, if you don\'t specify the DBClusterSnapshotIdentifier , an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the DBClusterSnapshotIdentifier , and the original DB cluster is deleted.

DBClusterIdentifier (string) --
Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.

SnapshotCreateTime (datetime) --
Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

Engine (string) --
Specifies the name of the database engine.

AllocatedStorage (integer) --
Specifies the allocated storage size in gibibytes (GiB).

Status (string) --
Specifies the status of this DB cluster snapshot.

Port (integer) --
Specifies the port that the DB cluster was listening on at the time of the snapshot.

VpcId (string) --
Provides the VPC ID associated with the DB cluster snapshot.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

MasterUsername (string) --
Provides the master username for the DB cluster snapshot.

EngineVersion (string) --
Provides the version of the database engine for this DB cluster snapshot.

LicenseModel (string) --
Provides the license model information for this DB cluster snapshot.

SnapshotType (string) --
Provides the type of the DB cluster snapshot.

PercentProgress (integer) --
Specifies the percentage of the estimated data that has been transferred.

StorageEncrypted (boolean) --
Specifies whether the DB cluster snapshot is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

DBClusterSnapshotArn (string) --
The Amazon Resource Name (ARN) for the DB cluster snapshot.

SourceDBClusterSnapshotArn (string) --
If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.









Exceptions

Neptune.Client.exceptions.DBClusterSnapshotAlreadyExistsFault
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.SnapshotQuotaExceededFault
Neptune.Client.exceptions.InvalidDBClusterSnapshotStateFault


    :return: {
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
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_db_instance(DBName=None, DBInstanceIdentifier=None, AllocatedStorage=None, DBInstanceClass=None, Engine=None, MasterUsername=None, MasterUserPassword=None, DBSecurityGroups=None, VpcSecurityGroupIds=None, AvailabilityZone=None, DBSubnetGroupName=None, PreferredMaintenanceWindow=None, DBParameterGroupName=None, BackupRetentionPeriod=None, PreferredBackupWindow=None, Port=None, MultiAZ=None, EngineVersion=None, AutoMinorVersionUpgrade=None, LicenseModel=None, Iops=None, OptionGroupName=None, CharacterSetName=None, PubliclyAccessible=None, Tags=None, DBClusterIdentifier=None, StorageType=None, TdeCredentialArn=None, TdeCredentialPassword=None, StorageEncrypted=None, KmsKeyId=None, Domain=None, CopyTagsToSnapshot=None, MonitoringInterval=None, MonitoringRoleArn=None, DomainIAMRoleName=None, PromotionTier=None, Timezone=None, EnableIAMDatabaseAuthentication=None, EnablePerformanceInsights=None, PerformanceInsightsKMSKeyId=None, EnableCloudwatchLogsExports=None, DeletionProtection=None):
    """
    Creates a new DB instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_db_instance(
        DBName='string',
        DBInstanceIdentifier='string',
        AllocatedStorage=123,
        DBInstanceClass='string',
        Engine='string',
        MasterUsername='string',
        MasterUserPassword='string',
        DBSecurityGroups=[
            'string',
        ],
        VpcSecurityGroupIds=[
            'string',
        ],
        AvailabilityZone='string',
        DBSubnetGroupName='string',
        PreferredMaintenanceWindow='string',
        DBParameterGroupName='string',
        BackupRetentionPeriod=123,
        PreferredBackupWindow='string',
        Port=123,
        MultiAZ=True|False,
        EngineVersion='string',
        AutoMinorVersionUpgrade=True|False,
        LicenseModel='string',
        Iops=123,
        OptionGroupName='string',
        CharacterSetName='string',
        PubliclyAccessible=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        DBClusterIdentifier='string',
        StorageType='string',
        TdeCredentialArn='string',
        TdeCredentialPassword='string',
        StorageEncrypted=True|False,
        KmsKeyId='string',
        Domain='string',
        CopyTagsToSnapshot=True|False,
        MonitoringInterval=123,
        MonitoringRoleArn='string',
        DomainIAMRoleName='string',
        PromotionTier=123,
        Timezone='string',
        EnableIAMDatabaseAuthentication=True|False,
        EnablePerformanceInsights=True|False,
        PerformanceInsightsKMSKeyId='string',
        EnableCloudwatchLogsExports=[
            'string',
        ],
        DeletionProtection=True|False
    )
    
    
    :type DBName: string
    :param DBName: Not supported.

    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]\nThe DB instance identifier. This parameter is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: mydbinstance\n

    :type AllocatedStorage: integer
    :param AllocatedStorage: The amount of storage (in gibibytes) to allocate for the DB instance.\nType: Integer\nNot applicable. Neptune cluster volumes automatically grow as the amount of data in your database increases, though you are only charged for the space that you use in a Neptune cluster volume.\n

    :type DBInstanceClass: string
    :param DBInstanceClass: [REQUIRED]\nThe compute and memory capacity of the DB instance, for example, db.m4.large . Not all DB instance classes are available in all AWS Regions.\n

    :type Engine: string
    :param Engine: [REQUIRED]\nThe name of the database engine to be used for this instance.\nValid Values: neptune\n

    :type MasterUsername: string
    :param MasterUsername: The name for the master user. Not used.

    :type MasterUserPassword: string
    :param MasterUserPassword: The password for the master user. The password can include any printable ASCII character except '/', ''', or '@'.\nNot used.\n

    :type DBSecurityGroups: list
    :param DBSecurityGroups: A list of DB security groups to associate with this DB instance.\nDefault: The default DB security group for the database engine.\n\n(string) --\n\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to associate with this DB instance.\nNot applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see CreateDBCluster .\nDefault: The default EC2 VPC security group for the DB subnet group\'s VPC.\n\n(string) --\n\n

    :type AvailabilityZone: string
    :param AvailabilityZone: The EC2 Availability Zone that the DB instance is created in\nDefault: A random, system-chosen Availability Zone in the endpoint\'s AWS Region.\nExample: us-east-1d\nConstraint: The AvailabilityZone parameter can\'t be specified if the MultiAZ parameter is set to true . The specified Availability Zone must be in the same AWS Region as the current endpoint.\n

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: A DB subnet group to associate with this DB instance.\nIf there is no DB subnet group, then it is a non-VPC DB instance.\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).\nFormat: ddd:hh24:mi-ddd:hh24:mi\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.\nValid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.\nConstraints: Minimum 30-minute window.\n

    :type DBParameterGroupName: string
    :param DBParameterGroupName: The name of the DB parameter group to associate with this DB instance. If this argument is omitted, the default DBParameterGroup for the specified engine is used.\nConstraints:\n\nMust be 1 to 255 letters, numbers, or hyphens.\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\n

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: The number of days for which automated backups are retained.\nNot applicable. The retention period for automated backups is managed by the DB cluster. For more information, see CreateDBCluster .\nDefault: 1\nConstraints:\n\nMust be a value from 0 to 35\nCannot be set to 0 if the DB instance is a source to Read Replicas\n\n

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created.\nNot applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see CreateDBCluster .\n

    :type Port: integer
    :param Port: The port number on which the database accepts connections.\nNot applicable. The port is managed by the DB cluster. For more information, see CreateDBCluster .\nDefault: 8182\nType: Integer\n

    :type MultiAZ: boolean
    :param MultiAZ: Specifies if the DB instance is a Multi-AZ deployment. You can\'t set the AvailabilityZone parameter if the MultiAZ parameter is set to true.

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine to use. Currently, setting this parameter has no effect.

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window.\nDefault: true\n

    :type LicenseModel: string
    :param LicenseModel: License model information for this DB instance.\nValid values: license-included | bring-your-own-license | general-public-license\n

    :type Iops: integer
    :param Iops: The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.

    :type OptionGroupName: string
    :param OptionGroupName: (Not supported by Neptune)

    :type CharacterSetName: string
    :param CharacterSetName: (Not supported by Neptune)

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: This flag should no longer be used.

    :type Tags: list
    :param Tags: The tags to assign to the new instance.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: The identifier of the DB cluster that the instance will belong to.\nFor information on creating a DB cluster, see CreateDBCluster .\nType: String\n

    :type StorageType: string
    :param StorageType: Specifies the storage type to be associated with the DB instance.\nNot applicable. Storage is managed by the DB Cluster.\n

    :type TdeCredentialArn: string
    :param TdeCredentialArn: The ARN from the key store with which to associate the instance for TDE encryption.

    :type TdeCredentialPassword: string
    :param TdeCredentialPassword: The password for the given ARN from the key store in order to access the device.

    :type StorageEncrypted: boolean
    :param StorageEncrypted: Specifies whether the DB instance is encrypted.\nNot applicable. The encryption for DB instances is managed by the DB cluster. For more information, see CreateDBCluster .\nDefault: false\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier for an encrypted DB instance.\nThe KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB instance with the same AWS account that owns the KMS encryption key used to encrypt the new DB instance, then you can use the KMS key alias instead of the ARN for the KM encryption key.\nNot applicable. The KMS key identifier is managed by the DB cluster. For more information, see CreateDBCluster .\nIf the StorageEncrypted parameter is true, and you do not specify a value for the KmsKeyId parameter, then Amazon Neptune will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.\n

    :type Domain: string
    :param Domain: Specify the Active Directory Domain to create the instance in.

    :type CopyTagsToSnapshot: boolean
    :param CopyTagsToSnapshot: True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.

    :type MonitoringInterval: integer
    :param MonitoringInterval: The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.\nIf MonitoringRoleArn is specified, then you must also set MonitoringInterval to a value other than 0.\nValid Values: 0, 1, 5, 10, 15, 30, 60\n

    :type MonitoringRoleArn: string
    :param MonitoringRoleArn: The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, arn:aws:iam:123456789012:role/emaccess .\nIf MonitoringInterval is set to a value other than 0, then you must supply a MonitoringRoleArn value.\n

    :type DomainIAMRoleName: string
    :param DomainIAMRoleName: Specify the name of the IAM role to be used when making API calls to the Directory Service.

    :type PromotionTier: integer
    :param PromotionTier: A value that specifies the order in which an Read Replica is promoted to the primary instance after a failure of the existing primary instance.\nDefault: 1\nValid Values: 0 - 15\n

    :type Timezone: string
    :param Timezone: The time zone of the DB instance.

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable AWS Identity and Access Management (IAM) authentication for Neptune.\nDefault: false\n

    :type EnablePerformanceInsights: boolean
    :param EnablePerformanceInsights: (Not supported by Neptune)

    :type PerformanceInsightsKMSKeyId: string
    :param PerformanceInsightsKMSKeyId: (Not supported by Neptune)

    :type EnableCloudwatchLogsExports: list
    :param EnableCloudwatchLogsExports: The list of log types that need to be enabled for exporting to CloudWatch Logs.\n\n(string) --\n\n

    :type DeletionProtection: boolean
    :param DeletionProtection: A value that indicates whether the DB instance has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled. By default, deletion protection is disabled. See Deleting a DB Instance .\nDB instances in a DB cluster can be deleted even when deletion protection is enabled in their parent DB cluster.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBInstance': {
        'DBInstanceIdentifier': 'string',
        'DBInstanceClass': 'string',
        'Engine': 'string',
        'DBInstanceStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123,
            'HostedZoneId': 'string'
        },
        'AllocatedStorage': 123,
        'InstanceCreateTime': datetime(2015, 1, 1),
        'PreferredBackupWindow': 'string',
        'BackupRetentionPeriod': 123,
        'DBSecurityGroups': [
            {
                'DBSecurityGroupName': 'string',
                'Status': 'string'
            },
        ],
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'DBParameterGroups': [
            {
                'DBParameterGroupName': 'string',
                'ParameterApplyStatus': 'string'
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
        'MultiAZ': True|False,
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'ReadReplicaSourceDBInstanceIdentifier': 'string',
        'ReadReplicaDBInstanceIdentifiers': [
            'string',
        ],
        'ReadReplicaDBClusterIdentifiers': [
            'string',
        ],
        'LicenseModel': 'string',
        'Iops': 123,
        'OptionGroupMemberships': [
            {
                'OptionGroupName': 'string',
                'Status': 'string'
            },
        ],
        'CharacterSetName': 'string',
        'SecondaryAvailabilityZone': 'string',
        'PubliclyAccessible': True|False,
        'StatusInfos': [
            {
                'StatusType': 'string',
                'Normal': True|False,
                'Status': 'string',
                'Message': 'string'
            },
        ],
        'StorageType': 'string',
        'TdeCredentialArn': 'string',
        'DbInstancePort': 123,
        'DBClusterIdentifier': 'string',
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DbiResourceId': 'string',
        'CACertificateIdentifier': 'string',
        'DomainMemberships': [
            {
                'Domain': 'string',
                'Status': 'string',
                'FQDN': 'string',
                'IAMRoleName': 'string'
            },
        ],
        'CopyTagsToSnapshot': True|False,
        'MonitoringInterval': 123,
        'EnhancedMonitoringResourceArn': 'string',
        'MonitoringRoleArn': 'string',
        'PromotionTier': 123,
        'DBInstanceArn': 'string',
        'Timezone': 'string',
        'IAMDatabaseAuthenticationEnabled': True|False,
        'PerformanceInsightsEnabled': True|False,
        'PerformanceInsightsKMSKeyId': 'string',
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBInstance (dict) --
Contains the details of an Amazon Neptune DB instance.
This data type is used as a response element in the  DescribeDBInstances action.

DBInstanceIdentifier (string) --
Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the DB instance.

Engine (string) --
Provides the name of the database engine to be used for this DB instance.

DBInstanceStatus (string) --
Specifies the current state of this database.

MasterUsername (string) --
Contains the master username for the DB instance.

DBName (string) --
The database name.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the DB instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



AllocatedStorage (integer) --
Specifies the allocated storage size specified in gibibytes.

InstanceCreateTime (datetime) --
Provides the date and time the DB instance was created.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

DBSecurityGroups (list) --
Provides List of DB security group elements containing only DBSecurityGroup.Name and DBSecurityGroup.Status subelements.

(dict) --
Specifies membership in a designated DB security group.

DBSecurityGroupName (string) --
The name of the DB security group.

Status (string) --
The status of the DB security group.





VpcSecurityGroups (list) --
Provides a list of VPC security group elements that the DB instance belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





DBParameterGroups (list) --
Provides the list of DB parameter groups applied to this DB instance.

(dict) --
The status of the DB parameter group.
This data type is used as a response element in the following actions:

CreateDBInstance
DeleteDBInstance
ModifyDBInstance
RebootDBInstance


DBParameterGroupName (string) --
The name of the DP parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.





AvailabilityZone (string) --
Specifies the name of the Availability Zone the DB instance is located in.

DBSubnetGroup (dict) --
Specifies information on the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --
The name of the DB subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the DB subnet group.

VpcId (string) --
Provides the VpcId of the DB subnet group.

SubnetGroupStatus (string) --
Provides the status of the DB subnet group.

Subnets (list) --
Contains a list of  Subnet elements.

(dict) --
Specifies a subnet.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the EC2 Availability Zone that the subnet is in.

Name (string) --
The name of the availability zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --
Specifies that changes to the DB instance are pending. This element is only included when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --
Contains the new DBInstanceClass for the DB instance that will be applied or is currently being applied.

AllocatedStorage (integer) --
Contains the new AllocatedStorage size for the DB instance that will be applied or is currently being applied.

MasterUserPassword (string) --
Contains the pending or currently-in-progress change of the master credentials for the DB instance.

Port (integer) --
Specifies the pending port for the DB instance.

BackupRetentionPeriod (integer) --
Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --
Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

LicenseModel (string) --
The license model for the DB instance.
Valid values: license-included | bring-your-own-license | general-public-license

Iops (integer) --
Specifies the new Provisioned IOPS value for the DB instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --
Contains the new DBInstanceIdentifier for the DB instance that will be applied or is currently being applied.

StorageType (string) --
Specifies the storage type to be associated with the DB instance.

CACertificateIdentifier (string) --
Specifies the identifier of the CA certificate for the DB instance.

DBSubnetGroupName (string) --
The new DB subnet group for the DB instance.

PendingCloudwatchLogsExports (dict) --
This PendingCloudwatchLogsExports structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.

LogTypesToEnable (list) --
Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --
Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

MultiAZ (boolean) --
Specifies if the DB instance is a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --
Indicates that minor version patches are applied automatically.

ReadReplicaSourceDBInstanceIdentifier (string) --
Contains the identifier of the source DB instance if this DB instance is a Read Replica.

ReadReplicaDBInstanceIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB instance.

(string) --


ReadReplicaDBClusterIdentifiers (list) --
Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

(string) --


LicenseModel (string) --
License model information for this DB instance.

Iops (integer) --
Specifies the Provisioned IOPS (I/O operations per second) value.

OptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Provides information on the option groups the DB instance is a member of.

OptionGroupName (string) --
The name of the option group that the instance belongs to.

Status (string) --
The status of the DB instance\'s option group membership. Valid values are: in-sync , pending-apply , pending-removal , pending-maintenance-apply , pending-maintenance-removal , applying , removing , and failed .





CharacterSetName (string) --

(Not supported by Neptune)


SecondaryAvailabilityZone (string) --
If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.

PubliclyAccessible (boolean) --
This flag should no longer be used.

StatusInfos (list) --
The status of a Read Replica. If the instance is not a Read Replica, this is blank.

(dict) --
Provides a list of status information for a DB instance.

StatusType (string) --
This value is currently "read replication."

Normal (boolean) --
Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --
Status of the DB instance. For a StatusType of read replica, the values can be replicating, error, stopped, or terminated.

Message (string) --
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





StorageType (string) --
Specifies the storage type associated with DB instance.

TdeCredentialArn (string) --
The ARN from the key store with which the instance is associated for TDE encryption.

DbInstancePort (integer) --
Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.

DBClusterIdentifier (string) --
If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

StorageEncrypted (boolean) --
Not supported: The encryption for DB instances is managed by the DB cluster.

KmsKeyId (string) --
Not supported: The encryption for DB instances is managed by the DB cluster.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

DomainMemberships (list) --
Not supported

(dict) --
An Active Directory Domain membership record associated with a DB instance.

Domain (string) --
The identifier of the Active Directory Domain.

Status (string) --
The status of the DB instance\'s Active Directory Domain membership, such as joined, pending-join, failed etc).

FQDN (string) --
The fully qualified domain name of the Active Directory Domain.

IAMRoleName (string) --
The name of the IAM role to be used when making API calls to the Directory Service.





CopyTagsToSnapshot (boolean) --
Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

MonitoringInterval (integer) --
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.

EnhancedMonitoringResourceArn (string) --
The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.

MonitoringRoleArn (string) --
The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --
The Amazon Resource Name (ARN) for the DB instance.

Timezone (string) --
Not supported.

IAMDatabaseAuthenticationEnabled (boolean) --
True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise false.

PerformanceInsightsEnabled (boolean) --

(Not supported by Neptune)


PerformanceInsightsKMSKeyId (string) --

(Not supported by Neptune)


EnabledCloudwatchLogsExports (list) --
A list of log types that this DB instance is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB instance has deletion protection enabled. The instance can\'t be deleted when deletion protection is enabled. See Deleting a DB Instance .









Exceptions

Neptune.Client.exceptions.DBInstanceAlreadyExistsFault
Neptune.Client.exceptions.InsufficientDBInstanceCapacityFault
Neptune.Client.exceptions.DBParameterGroupNotFoundFault
Neptune.Client.exceptions.DBSecurityGroupNotFoundFault
Neptune.Client.exceptions.InstanceQuotaExceededFault
Neptune.Client.exceptions.StorageQuotaExceededFault
Neptune.Client.exceptions.DBSubnetGroupNotFoundFault
Neptune.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.InvalidSubnet
Neptune.Client.exceptions.InvalidVPCNetworkStateFault
Neptune.Client.exceptions.ProvisionedIopsNotAvailableInAZFault
Neptune.Client.exceptions.OptionGroupNotFoundFault
Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.StorageTypeNotSupportedFault
Neptune.Client.exceptions.AuthorizationNotFoundFault
Neptune.Client.exceptions.KMSKeyNotAccessibleFault
Neptune.Client.exceptions.DomainNotFoundFault


    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'DBSecurityGroups': [
                {
                    'DBSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'DBParameterGroups': [
                {
                    'DBParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string'
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
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'ReadReplicaSourceDBInstanceIdentifier': 'string',
            'ReadReplicaDBInstanceIdentifiers': [
                'string',
            ],
            'ReadReplicaDBClusterIdentifiers': [
                'string',
            ],
            'LicenseModel': 'string',
            'Iops': 123,
            'OptionGroupMemberships': [
                {
                    'OptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CharacterSetName': 'string',
            'SecondaryAvailabilityZone': 'string',
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'StorageType': 'string',
            'TdeCredentialArn': 'string',
            'DbInstancePort': 123,
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'DomainMemberships': [
                {
                    'Domain': 'string',
                    'Status': 'string',
                    'FQDN': 'string',
                    'IAMRoleName': 'string'
                },
            ],
            'CopyTagsToSnapshot': True|False,
            'MonitoringInterval': 123,
            'EnhancedMonitoringResourceArn': 'string',
            'MonitoringRoleArn': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'Timezone': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False,
            'PerformanceInsightsEnabled': True|False,
            'PerformanceInsightsKMSKeyId': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    CreateDBInstance
    DeleteDBInstance
    ModifyDBInstance
    RebootDBInstance
    
    """
    pass

def create_db_parameter_group(DBParameterGroupName=None, DBParameterGroupFamily=None, Description=None, Tags=None):
    """
    Creates a new DB parameter group.
    A DB parameter group is initially created with the default parameters for the database engine used by the DB instance. To provide custom values for any of the parameters, you must modify the group after creating it using ModifyDBParameterGroup . Once you\'ve created a DB parameter group, you need to associate it with your DB instance using ModifyDBInstance . When you associate a new DB parameter group with a running DB instance, you need to reboot the DB instance without failover for the new DB parameter group and associated settings to take effect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_db_parameter_group(
        DBParameterGroupName='string',
        DBParameterGroupFamily='string',
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]\nThe name of the DB parameter group.\nConstraints:\n\nMust be 1 to 255 letters, numbers, or hyphens.\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\n\nNote\nThis value is stored as a lowercase string.\n\n

    :type DBParameterGroupFamily: string
    :param DBParameterGroupFamily: [REQUIRED]\nThe DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.\n

    :type Description: string
    :param Description: [REQUIRED]\nThe description for the DB parameter group.\n

    :type Tags: list
    :param Tags: The tags to be assigned to the new DB parameter group.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBParameterGroup': {
        'DBParameterGroupName': 'string',
        'DBParameterGroupFamily': 'string',
        'Description': 'string',
        'DBParameterGroupArn': 'string'
    }
}


Response Structure

(dict) --

DBParameterGroup (dict) --
Contains the details of an Amazon Neptune DB parameter group.
This data type is used as a response element in the  DescribeDBParameterGroups action.

DBParameterGroupName (string) --
Provides the name of the DB parameter group.

DBParameterGroupFamily (string) --
Provides the name of the DB parameter group family that this DB parameter group is compatible with.

Description (string) --
Provides the customer-specified description for this DB parameter group.

DBParameterGroupArn (string) --
The Amazon Resource Name (ARN) for the DB parameter group.









Exceptions

Neptune.Client.exceptions.DBParameterGroupQuotaExceededFault
Neptune.Client.exceptions.DBParameterGroupAlreadyExistsFault


    :return: {
        'DBParameterGroup': {
            'DBParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBParameterGroupArn': 'string'
        }
    }
    
    
    :returns: 
    Neptune.Client.exceptions.DBParameterGroupQuotaExceededFault
    Neptune.Client.exceptions.DBParameterGroupAlreadyExistsFault
    
    """
    pass

def create_db_subnet_group(DBSubnetGroupName=None, DBSubnetGroupDescription=None, SubnetIds=None, Tags=None):
    """
    Creates a new DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the AWS Region.
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
    :param DBSubnetGroupName: [REQUIRED]\nThe name for the DB subnet group. This value is stored as a lowercase string.\nConstraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.\nExample: mySubnetgroup\n

    :type DBSubnetGroupDescription: string
    :param DBSubnetGroupDescription: [REQUIRED]\nThe description for the DB subnet group.\n

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nThe EC2 Subnet IDs for the DB subnet group.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: The tags to be assigned to the new DB subnet group.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

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
Contains the details of an Amazon Neptune DB subnet group.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

DBSubnetGroupName (string) --
The name of the DB subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the DB subnet group.

VpcId (string) --
Provides the VpcId of the DB subnet group.

SubnetGroupStatus (string) --
Provides the status of the DB subnet group.

Subnets (list) --
Contains a list of  Subnet elements.

(dict) --
Specifies a subnet.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the EC2 Availability Zone that the subnet is in.

Name (string) --
The name of the availability zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.









Exceptions

Neptune.Client.exceptions.DBSubnetGroupAlreadyExistsFault
Neptune.Client.exceptions.DBSubnetGroupQuotaExceededFault
Neptune.Client.exceptions.DBSubnetQuotaExceededFault
Neptune.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
Neptune.Client.exceptions.InvalidSubnet


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
    Neptune.Client.exceptions.DBSubnetGroupAlreadyExistsFault
    Neptune.Client.exceptions.DBSubnetGroupQuotaExceededFault
    Neptune.Client.exceptions.DBSubnetQuotaExceededFault
    Neptune.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
    Neptune.Client.exceptions.InvalidSubnet
    
    """
    pass

def create_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None, SourceIds=None, Enabled=None, Tags=None):
    """
    Creates an event notification subscription. This action requires a topic ARN (Amazon Resource Name) created by either the Neptune console, the SNS console, or the SNS API. To obtain an ARN with SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.
    You can specify the type of source (SourceType) you want to be notified of, provide a list of Neptune sources (SourceIds) that triggers the events, and provide a list of event categories (EventCategories) for events you want to be notified of. For example, you can specify SourceType = db-instance, SourceIds = mydbinstance1, mydbinstance2 and EventCategories = Availability, Backup.
    If you specify both the SourceType and SourceIds, such as SourceType = db-instance and SourceIdentifier = myDBInstance1, you are notified of all the db-instance events for the specified source. If you specify a SourceType but do not specify a SourceIdentifier, you receive notice of the events for that source type for all your Neptune sources. If you do not specify either the SourceType nor the SourceIdentifier, you are notified of events generated from all Neptune sources belonging to your customer account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_event_subscription(
        SubscriptionName='string',
        SnsTopicArn='string',
        SourceType='string',
        EventCategories=[
            'string',
        ],
        SourceIds=[
            'string',
        ],
        Enabled=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]\nThe name of the subscription.\nConstraints: The name must be less than 255 characters.\n

    :type SnsTopicArn: string
    :param SnsTopicArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.\n

    :type SourceType: string
    :param SourceType: The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.\nValid values: db-instance | db-cluster | db-parameter-group | db-security-group | db-snapshot | db-cluster-snapshot\n

    :type EventCategories: list
    :param EventCategories: A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the DescribeEventCategories action.\n\n(string) --\n\n

    :type SourceIds: list
    :param SourceIds: The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can\'t end with a hyphen or contain two consecutive hyphens.\nConstraints:\n\nIf SourceIds are supplied, SourceType must also be provided.\nIf the source type is a DB instance, then a DBInstanceIdentifier must be supplied.\nIf the source type is a DB security group, a DBSecurityGroupName must be supplied.\nIf the source type is a DB parameter group, a DBParameterGroupName must be supplied.\nIf the source type is a DB snapshot, a DBSnapshotIdentifier must be supplied.\n\n\n(string) --\n\n

    :type Enabled: boolean
    :param Enabled: A Boolean value; set to true to activate the subscription, set to false to create the subscription but not active it.

    :type Tags: list
    :param Tags: The tags to be applied to the new event subscription.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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

EventSubscription (dict) --
Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

CustomerAwsId (string) --
The AWS customer account associated with the event notification subscription.

CustSubscriptionId (string) --
The event notification subscription Id.

SnsTopicArn (string) --
The topic ARN of the event notification subscription.

Status (string) --
The status of the event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that Neptune no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --
The time the event notification subscription was created.

SourceType (string) --
The source type for the event notification subscription.

SourceIdsList (list) --
A list of source IDs for the event notification subscription.

(string) --


EventCategoriesList (list) --
A list of event categories for the event notification subscription.

(string) --


Enabled (boolean) --
A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.

EventSubscriptionArn (string) --
The Amazon Resource Name (ARN) for the event subscription.









Exceptions

Neptune.Client.exceptions.EventSubscriptionQuotaExceededFault
Neptune.Client.exceptions.SubscriptionAlreadyExistFault
Neptune.Client.exceptions.SNSInvalidTopicFault
Neptune.Client.exceptions.SNSNoAuthorizationFault
Neptune.Client.exceptions.SNSTopicArnNotFoundFault
Neptune.Client.exceptions.SubscriptionCategoryNotFoundFault
Neptune.Client.exceptions.SourceNotFoundFault


    :return: {
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
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_db_cluster(DBClusterIdentifier=None, SkipFinalSnapshot=None, FinalDBSnapshotIdentifier=None):
    """
    The DeleteDBCluster action deletes a previously provisioned DB cluster. When you delete a DB cluster, all automated backups for that DB cluster are deleted and can\'t be recovered. Manual DB cluster snapshots of the specified DB cluster are not deleted.
    Note that the DB Cluster cannot be deleted if deletion protection is enabled. To delete it, you must first set its DeletionProtection field to False .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_cluster(
        DBClusterIdentifier='string',
        SkipFinalSnapshot=True|False,
        FinalDBSnapshotIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe DB cluster identifier for the DB cluster to be deleted. This parameter isn\'t case-sensitive.\nConstraints:\n\nMust match an existing DBClusterIdentifier.\n\n

    :type SkipFinalSnapshot: boolean
    :param SkipFinalSnapshot: Determines whether a final DB cluster snapshot is created before the DB cluster is deleted. If true is specified, no DB cluster snapshot is created. If false is specified, a DB cluster snapshot is created before the DB cluster is deleted.\n\nNote\nYou must specify a FinalDBSnapshotIdentifier parameter if SkipFinalSnapshot is false .\n\nDefault: false\n

    :type FinalDBSnapshotIdentifier: string
    :param FinalDBSnapshotIdentifier: The DB cluster snapshot identifier of the new DB cluster snapshot created when SkipFinalSnapshot is set to false .\n\nNote\nSpecifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.\n\nConstraints:\n\nMust be 1 to 255 letters, numbers, or hyphens.\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'MultiAZ': True|False,
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
        ],
        'IAMDatabaseAuthenticationEnabled': True|False,
        'CloneGroupId': 'string',
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
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --

AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.


AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --

(Not supported by Neptune)


DatabaseName (string) --
Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --
Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this DB cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --
The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --
Specifies the name of the DB cluster option group.

Status (string) --
Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --
Not supported by Neptune.

ReadReplicaIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --
Provides the list of instances that make up the DB cluster.

(dict) --
Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --
Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --
Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.









Exceptions

Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.DBClusterSnapshotAlreadyExistsFault
Neptune.Client.exceptions.SnapshotQuotaExceededFault
Neptune.Client.exceptions.InvalidDBClusterSnapshotStateFault


    :return: {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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
    Deletes a specified DB cluster parameter group. The DB cluster parameter group to be deleted can\'t be associated with any DB clusters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_cluster_parameter_group(
        DBClusterParameterGroupName='string'
    )
    
    
    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of the DB cluster parameter group.\nConstraints:\n\nMust be the name of an existing DB cluster parameter group.\nYou can\'t delete a default DB cluster parameter group.\nCannot be associated with any DB clusters.\n\n

    :returns: 
    Neptune.Client.exceptions.InvalidDBParameterGroupStateFault
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def delete_db_cluster_snapshot(DBClusterSnapshotIdentifier=None):
    """
    Deletes a DB cluster snapshot. If the snapshot is being copied, the copy operation is terminated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_cluster_snapshot(
        DBClusterSnapshotIdentifier='string'
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier of the DB cluster snapshot to delete.\nConstraints: Must be the name of an existing DB cluster snapshot in the available state.\n

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
        'DBClusterSnapshotArn': 'string',
        'SourceDBClusterSnapshotArn': 'string',
        'IAMDatabaseAuthenticationEnabled': True|False
    }
}


Response Structure

(dict) --
DBClusterSnapshot (dict) --Contains the details for an Amazon Neptune DB cluster snapshot
This data type is used as a response element in the  DescribeDBClusterSnapshots action.

AvailabilityZones (list) --Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

(string) --


DBClusterSnapshotIdentifier (string) --Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot.
After you restore a DB cluster using a DBClusterSnapshotIdentifier , you must specify the same DBClusterSnapshotIdentifier for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed.
However, if you don\'t specify the DBClusterSnapshotIdentifier , an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the DBClusterSnapshotIdentifier , and the original DB cluster is deleted.

DBClusterIdentifier (string) --Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.

SnapshotCreateTime (datetime) --Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

Engine (string) --Specifies the name of the database engine.

AllocatedStorage (integer) --Specifies the allocated storage size in gibibytes (GiB).

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

KmsKeyId (string) --If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

DBClusterSnapshotArn (string) --The Amazon Resource Name (ARN) for the DB cluster snapshot.

SourceDBClusterSnapshotArn (string) --If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

IAMDatabaseAuthenticationEnabled (boolean) --True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.








Exceptions

Neptune.Client.exceptions.InvalidDBClusterSnapshotStateFault
Neptune.Client.exceptions.DBClusterSnapshotNotFoundFault


    :return: {
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
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False
        }
    }
    
    
    :returns: 
    Neptune.Client.exceptions.InvalidDBClusterSnapshotStateFault
    Neptune.Client.exceptions.DBClusterSnapshotNotFoundFault
    
    """
    pass

def delete_db_instance(DBInstanceIdentifier=None, SkipFinalSnapshot=None, FinalDBSnapshotIdentifier=None):
    """
    The DeleteDBInstance action deletes a previously provisioned DB instance. When you delete a DB instance, all automated backups for that instance are deleted and can\'t be recovered. Manual DB snapshots of the DB instance to be deleted by DeleteDBInstance are not deleted.
    If you request a final DB snapshot the status of the Amazon Neptune DB instance is deleting until the DB snapshot is created. The API action DescribeDBInstance is used to monitor the status of this operation. The action can\'t be canceled or reverted once submitted.
    Note that when a DB instance is in a failure state and has a status of failed , incompatible-restore , or incompatible-network , you can only delete it when the SkipFinalSnapshot parameter is set to true .
    You can\'t delete a DB instance if it is the only instance in the DB cluster, or if it has deletion protection enabled.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_instance(
        DBInstanceIdentifier='string',
        SkipFinalSnapshot=True|False,
        FinalDBSnapshotIdentifier='string'
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]\nThe DB instance identifier for the DB instance to be deleted. This parameter isn\'t case-sensitive.\nConstraints:\n\nMust match the name of an existing DB instance.\n\n

    :type SkipFinalSnapshot: boolean
    :param SkipFinalSnapshot: Determines whether a final DB snapshot is created before the DB instance is deleted. If true is specified, no DBSnapshot is created. If false is specified, a DB snapshot is created before the DB instance is deleted.\nNote that when a DB instance is in a failure state and has a status of \'failed\', \'incompatible-restore\', or \'incompatible-network\', it can only be deleted when the SkipFinalSnapshot parameter is set to 'true'.\nSpecify true when deleting a Read Replica.\n\nNote\nThe FinalDBSnapshotIdentifier parameter must be specified if SkipFinalSnapshot is false .\n\nDefault: false\n

    :type FinalDBSnapshotIdentifier: string
    :param FinalDBSnapshotIdentifier: The DBSnapshotIdentifier of the new DBSnapshot created when SkipFinalSnapshot is set to false .\n\nNote\nSpecifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.\n\nConstraints:\n\nMust be 1 to 255 letters or numbers.\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\nCannot be specified when deleting a Read Replica.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBInstance': {
        'DBInstanceIdentifier': 'string',
        'DBInstanceClass': 'string',
        'Engine': 'string',
        'DBInstanceStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123,
            'HostedZoneId': 'string'
        },
        'AllocatedStorage': 123,
        'InstanceCreateTime': datetime(2015, 1, 1),
        'PreferredBackupWindow': 'string',
        'BackupRetentionPeriod': 123,
        'DBSecurityGroups': [
            {
                'DBSecurityGroupName': 'string',
                'Status': 'string'
            },
        ],
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'DBParameterGroups': [
            {
                'DBParameterGroupName': 'string',
                'ParameterApplyStatus': 'string'
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
        'MultiAZ': True|False,
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'ReadReplicaSourceDBInstanceIdentifier': 'string',
        'ReadReplicaDBInstanceIdentifiers': [
            'string',
        ],
        'ReadReplicaDBClusterIdentifiers': [
            'string',
        ],
        'LicenseModel': 'string',
        'Iops': 123,
        'OptionGroupMemberships': [
            {
                'OptionGroupName': 'string',
                'Status': 'string'
            },
        ],
        'CharacterSetName': 'string',
        'SecondaryAvailabilityZone': 'string',
        'PubliclyAccessible': True|False,
        'StatusInfos': [
            {
                'StatusType': 'string',
                'Normal': True|False,
                'Status': 'string',
                'Message': 'string'
            },
        ],
        'StorageType': 'string',
        'TdeCredentialArn': 'string',
        'DbInstancePort': 123,
        'DBClusterIdentifier': 'string',
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DbiResourceId': 'string',
        'CACertificateIdentifier': 'string',
        'DomainMemberships': [
            {
                'Domain': 'string',
                'Status': 'string',
                'FQDN': 'string',
                'IAMRoleName': 'string'
            },
        ],
        'CopyTagsToSnapshot': True|False,
        'MonitoringInterval': 123,
        'EnhancedMonitoringResourceArn': 'string',
        'MonitoringRoleArn': 'string',
        'PromotionTier': 123,
        'DBInstanceArn': 'string',
        'Timezone': 'string',
        'IAMDatabaseAuthenticationEnabled': True|False,
        'PerformanceInsightsEnabled': True|False,
        'PerformanceInsightsKMSKeyId': 'string',
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBInstance (dict) --
Contains the details of an Amazon Neptune DB instance.
This data type is used as a response element in the  DescribeDBInstances action.

DBInstanceIdentifier (string) --
Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the DB instance.

Engine (string) --
Provides the name of the database engine to be used for this DB instance.

DBInstanceStatus (string) --
Specifies the current state of this database.

MasterUsername (string) --
Contains the master username for the DB instance.

DBName (string) --
The database name.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the DB instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



AllocatedStorage (integer) --
Specifies the allocated storage size specified in gibibytes.

InstanceCreateTime (datetime) --
Provides the date and time the DB instance was created.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

DBSecurityGroups (list) --
Provides List of DB security group elements containing only DBSecurityGroup.Name and DBSecurityGroup.Status subelements.

(dict) --
Specifies membership in a designated DB security group.

DBSecurityGroupName (string) --
The name of the DB security group.

Status (string) --
The status of the DB security group.





VpcSecurityGroups (list) --
Provides a list of VPC security group elements that the DB instance belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





DBParameterGroups (list) --
Provides the list of DB parameter groups applied to this DB instance.

(dict) --
The status of the DB parameter group.
This data type is used as a response element in the following actions:

CreateDBInstance
DeleteDBInstance
ModifyDBInstance
RebootDBInstance


DBParameterGroupName (string) --
The name of the DP parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.





AvailabilityZone (string) --
Specifies the name of the Availability Zone the DB instance is located in.

DBSubnetGroup (dict) --
Specifies information on the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --
The name of the DB subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the DB subnet group.

VpcId (string) --
Provides the VpcId of the DB subnet group.

SubnetGroupStatus (string) --
Provides the status of the DB subnet group.

Subnets (list) --
Contains a list of  Subnet elements.

(dict) --
Specifies a subnet.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the EC2 Availability Zone that the subnet is in.

Name (string) --
The name of the availability zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --
Specifies that changes to the DB instance are pending. This element is only included when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --
Contains the new DBInstanceClass for the DB instance that will be applied or is currently being applied.

AllocatedStorage (integer) --
Contains the new AllocatedStorage size for the DB instance that will be applied or is currently being applied.

MasterUserPassword (string) --
Contains the pending or currently-in-progress change of the master credentials for the DB instance.

Port (integer) --
Specifies the pending port for the DB instance.

BackupRetentionPeriod (integer) --
Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --
Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

LicenseModel (string) --
The license model for the DB instance.
Valid values: license-included | bring-your-own-license | general-public-license

Iops (integer) --
Specifies the new Provisioned IOPS value for the DB instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --
Contains the new DBInstanceIdentifier for the DB instance that will be applied or is currently being applied.

StorageType (string) --
Specifies the storage type to be associated with the DB instance.

CACertificateIdentifier (string) --
Specifies the identifier of the CA certificate for the DB instance.

DBSubnetGroupName (string) --
The new DB subnet group for the DB instance.

PendingCloudwatchLogsExports (dict) --
This PendingCloudwatchLogsExports structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.

LogTypesToEnable (list) --
Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --
Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

MultiAZ (boolean) --
Specifies if the DB instance is a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --
Indicates that minor version patches are applied automatically.

ReadReplicaSourceDBInstanceIdentifier (string) --
Contains the identifier of the source DB instance if this DB instance is a Read Replica.

ReadReplicaDBInstanceIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB instance.

(string) --


ReadReplicaDBClusterIdentifiers (list) --
Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

(string) --


LicenseModel (string) --
License model information for this DB instance.

Iops (integer) --
Specifies the Provisioned IOPS (I/O operations per second) value.

OptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Provides information on the option groups the DB instance is a member of.

OptionGroupName (string) --
The name of the option group that the instance belongs to.

Status (string) --
The status of the DB instance\'s option group membership. Valid values are: in-sync , pending-apply , pending-removal , pending-maintenance-apply , pending-maintenance-removal , applying , removing , and failed .





CharacterSetName (string) --

(Not supported by Neptune)


SecondaryAvailabilityZone (string) --
If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.

PubliclyAccessible (boolean) --
This flag should no longer be used.

StatusInfos (list) --
The status of a Read Replica. If the instance is not a Read Replica, this is blank.

(dict) --
Provides a list of status information for a DB instance.

StatusType (string) --
This value is currently "read replication."

Normal (boolean) --
Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --
Status of the DB instance. For a StatusType of read replica, the values can be replicating, error, stopped, or terminated.

Message (string) --
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





StorageType (string) --
Specifies the storage type associated with DB instance.

TdeCredentialArn (string) --
The ARN from the key store with which the instance is associated for TDE encryption.

DbInstancePort (integer) --
Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.

DBClusterIdentifier (string) --
If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

StorageEncrypted (boolean) --
Not supported: The encryption for DB instances is managed by the DB cluster.

KmsKeyId (string) --
Not supported: The encryption for DB instances is managed by the DB cluster.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

DomainMemberships (list) --
Not supported

(dict) --
An Active Directory Domain membership record associated with a DB instance.

Domain (string) --
The identifier of the Active Directory Domain.

Status (string) --
The status of the DB instance\'s Active Directory Domain membership, such as joined, pending-join, failed etc).

FQDN (string) --
The fully qualified domain name of the Active Directory Domain.

IAMRoleName (string) --
The name of the IAM role to be used when making API calls to the Directory Service.





CopyTagsToSnapshot (boolean) --
Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

MonitoringInterval (integer) --
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.

EnhancedMonitoringResourceArn (string) --
The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.

MonitoringRoleArn (string) --
The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --
The Amazon Resource Name (ARN) for the DB instance.

Timezone (string) --
Not supported.

IAMDatabaseAuthenticationEnabled (boolean) --
True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise false.

PerformanceInsightsEnabled (boolean) --

(Not supported by Neptune)


PerformanceInsightsKMSKeyId (string) --

(Not supported by Neptune)


EnabledCloudwatchLogsExports (list) --
A list of log types that this DB instance is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB instance has deletion protection enabled. The instance can\'t be deleted when deletion protection is enabled. See Deleting a DB Instance .









Exceptions

Neptune.Client.exceptions.DBInstanceNotFoundFault
Neptune.Client.exceptions.InvalidDBInstanceStateFault
Neptune.Client.exceptions.DBSnapshotAlreadyExistsFault
Neptune.Client.exceptions.SnapshotQuotaExceededFault
Neptune.Client.exceptions.InvalidDBClusterStateFault


    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'DBSecurityGroups': [
                {
                    'DBSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'DBParameterGroups': [
                {
                    'DBParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string'
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
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'ReadReplicaSourceDBInstanceIdentifier': 'string',
            'ReadReplicaDBInstanceIdentifiers': [
                'string',
            ],
            'ReadReplicaDBClusterIdentifiers': [
                'string',
            ],
            'LicenseModel': 'string',
            'Iops': 123,
            'OptionGroupMemberships': [
                {
                    'OptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CharacterSetName': 'string',
            'SecondaryAvailabilityZone': 'string',
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'StorageType': 'string',
            'TdeCredentialArn': 'string',
            'DbInstancePort': 123,
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'DomainMemberships': [
                {
                    'Domain': 'string',
                    'Status': 'string',
                    'FQDN': 'string',
                    'IAMRoleName': 'string'
                },
            ],
            'CopyTagsToSnapshot': True|False,
            'MonitoringInterval': 123,
            'EnhancedMonitoringResourceArn': 'string',
            'MonitoringRoleArn': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'Timezone': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False,
            'PerformanceInsightsEnabled': True|False,
            'PerformanceInsightsKMSKeyId': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    CreateDBInstance
    DeleteDBInstance
    ModifyDBInstance
    RebootDBInstance
    
    """
    pass

def delete_db_parameter_group(DBParameterGroupName=None):
    """
    Deletes a specified DBParameterGroup. The DBParameterGroup to be deleted can\'t be associated with any DB instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_parameter_group(
        DBParameterGroupName='string'
    )
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]\nThe name of the DB parameter group.\nConstraints:\n\nMust be the name of an existing DB parameter group\nYou can\'t delete a default DB parameter group\nCannot be associated with any DB instances\n\n

    :returns: 
    Neptune.Client.exceptions.InvalidDBParameterGroupStateFault
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def delete_db_subnet_group(DBSubnetGroupName=None):
    """
    Deletes a DB subnet group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_db_subnet_group(
        DBSubnetGroupName='string'
    )
    
    
    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: [REQUIRED]\nThe name of the database subnet group to delete.\n\nNote\nYou can\'t delete the default subnet group.\n\nConstraints:\nConstraints: Must match the name of an existing DBSubnetGroup. Must not be default.\nExample: mySubnetgroup\n

    """
    pass

def delete_event_subscription(SubscriptionName=None):
    """
    Deletes an event notification subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_event_subscription(
        SubscriptionName='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]\nThe name of the event notification subscription you want to delete.\n

    :rtype: dict
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
EventSubscription (dict) --Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

CustomerAwsId (string) --The AWS customer account associated with the event notification subscription.

CustSubscriptionId (string) --The event notification subscription Id.

SnsTopicArn (string) --The topic ARN of the event notification subscription.

Status (string) --The status of the event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that Neptune no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --The time the event notification subscription was created.

SourceType (string) --The source type for the event notification subscription.

SourceIdsList (list) --A list of source IDs for the event notification subscription.

(string) --


EventCategoriesList (list) --A list of event categories for the event notification subscription.

(string) --


Enabled (boolean) --A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.

EventSubscriptionArn (string) --The Amazon Resource Name (ARN) for the event subscription.








Exceptions

Neptune.Client.exceptions.SubscriptionNotFoundFault
Neptune.Client.exceptions.InvalidEventSubscriptionStateFault


    :return: {
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
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_cluster_parameter_groups(DBClusterParameterGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of DBClusterParameterGroup descriptions. If a DBClusterParameterGroupName parameter is specified, the list will contain only the description of the specified DB cluster parameter group.
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
    :param DBClusterParameterGroupName: The name of a specific DB cluster parameter group to return details for.\nConstraints:\n\nIf supplied, must match the name of an existing DBClusterParameterGroup.\n\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBClusterParameterGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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

Marker (string) --
An optional pagination token provided by a previous DescribeDBClusterParameterGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBClusterParameterGroups (list) --
A list of DB cluster parameter groups.

(dict) --
Contains the details of an Amazon Neptune DB cluster parameter group.
This data type is used as a response element in the  DescribeDBClusterParameterGroups action.

DBClusterParameterGroupName (string) --
Provides the name of the DB cluster parameter group.

DBParameterGroupFamily (string) --
Provides the name of the DB parameter group family that this DB cluster parameter group is compatible with.

Description (string) --
Provides the customer-specified description for this DB cluster parameter group.

DBClusterParameterGroupArn (string) --
The Amazon Resource Name (ARN) for the DB cluster parameter group.











Exceptions

Neptune.Client.exceptions.DBParameterGroupNotFoundFault


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
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def describe_db_cluster_parameters(DBClusterParameterGroupName=None, Source=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns the detailed parameter list for a particular DB cluster parameter group.
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
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of a specific DB cluster parameter group to return parameter details for.\nConstraints:\n\nIf supplied, must match the name of an existing DBClusterParameterGroup.\n\n

    :type Source: string
    :param Source: A value that indicates to return only parameters for a specific source. Parameter sources can be engine , service , or customer .

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBClusterParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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

Parameters (list) --
Provides a list of parameters for the DB cluster parameter group.

(dict) --
Specifies a parameter.

ParameterName (string) --
Specifies the name of the parameter.

ParameterValue (string) --
Specifies the value of the parameter.

Description (string) --
Provides a description of the parameter.

Source (string) --
Indicates the source of the parameter value.

ApplyType (string) --
Specifies the engine specific parameters type.

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
An optional pagination token provided by a previous DescribeDBClusterParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .







Exceptions

Neptune.Client.exceptions.DBParameterGroupNotFoundFault


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
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def describe_db_cluster_snapshot_attributes(DBClusterSnapshotIdentifier=None):
    """
    Returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.
    When sharing snapshots with other AWS accounts, DescribeDBClusterSnapshotAttributes returns the restore attribute and a list of IDs for the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If all is included in the list of values for the restore attribute, then the manual DB cluster snapshot is public and can be copied or restored by all AWS accounts.
    To add or remove access for an AWS account to copy or restore a manual DB cluster snapshot, or to make the manual DB cluster snapshot public or private, use the  ModifyDBClusterSnapshotAttribute API action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_cluster_snapshot_attributes(
        DBClusterSnapshotIdentifier='string'
    )
    
    
    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier for the DB cluster snapshot to describe the attributes for.\n

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
DBClusterSnapshotAttributesResult (dict) --Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API action.
Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.

DBClusterSnapshotIdentifier (string) --The identifier of the manual DB cluster snapshot that the attributes apply to.

DBClusterSnapshotAttributes (list) --The list of attributes and values for the manual DB cluster snapshot.

(dict) --Contains the name and values of a manual DB cluster snapshot attribute.
Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore a manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.

AttributeName (string) --The name of the manual DB cluster snapshot attribute.
The attribute named restore refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.

AttributeValues (list) --The value(s) for the manual DB cluster snapshot attribute.
If the AttributeName field is set to restore , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of all is in the list, then the manual DB cluster snapshot is public and available for any AWS account to copy or restore.

(string) --













Exceptions

Neptune.Client.exceptions.DBClusterSnapshotNotFoundFault


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
    Neptune.Client.exceptions.DBClusterSnapshotNotFoundFault
    
    """
    pass

def describe_db_cluster_snapshots(DBClusterIdentifier=None, DBClusterSnapshotIdentifier=None, SnapshotType=None, Filters=None, MaxRecords=None, Marker=None, IncludeShared=None, IncludePublic=None):
    """
    Returns information about DB cluster snapshots. This API action supports pagination.
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
    :param DBClusterIdentifier: The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can\'t be used in conjunction with the DBClusterSnapshotIdentifier parameter. This parameter is not case-sensitive.\nConstraints:\n\nIf supplied, must match the identifier of an existing DBCluster.\n\n

    :type DBClusterSnapshotIdentifier: string
    :param DBClusterSnapshotIdentifier: A specific DB cluster snapshot identifier to describe. This parameter can\'t be used in conjunction with the DBClusterIdentifier parameter. This value is stored as a lowercase string.\nConstraints:\n\nIf supplied, must match the identifier of an existing DBClusterSnapshot.\nIf this identifier is for an automated snapshot, the SnapshotType parameter must also be specified.\n\n

    :type SnapshotType: string
    :param SnapshotType: The type of DB cluster snapshots to be returned. You can specify one of the following values:\n\nautomated - Return all DB cluster snapshots that have been automatically taken by Amazon Neptune for my AWS account.\nmanual - Return all DB cluster snapshots that have been taken by my AWS account.\nshared - Return all manual DB cluster snapshots that have been shared to my AWS account.\npublic - Return all DB cluster snapshots that have been marked as public.\n\nIf you don\'t specify a SnapshotType value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the IncludeShared parameter to true . You can include public DB cluster snapshots with these results by setting the IncludePublic parameter to true .\nThe IncludeShared and IncludePublic parameters don\'t apply for SnapshotType values of manual or automated . The IncludePublic parameter doesn\'t apply when SnapshotType is set to shared . The IncludeShared parameter doesn\'t apply when SnapshotType is set to public .\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBClusterSnapshots request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :type IncludeShared: boolean
    :param IncludeShared: True to include shared manual DB cluster snapshots from other AWS accounts that this AWS account has been given permission to copy or restore, and otherwise false. The default is false .\nYou can give an AWS account permission to restore a manual DB cluster snapshot from another AWS account by the ModifyDBClusterSnapshotAttribute API action.\n

    :type IncludePublic: boolean
    :param IncludePublic: True to include manual DB cluster snapshots that are public and can be copied or restored by any AWS account, and otherwise false. The default is false . The default is false.\nYou can share a manual DB cluster snapshot as public by using the ModifyDBClusterSnapshotAttribute API action.\n

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
            'DBClusterSnapshotArn': 'string',
            'SourceDBClusterSnapshotArn': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous  DescribeDBClusterSnapshots request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBClusterSnapshots (list) --
Provides a list of DB cluster snapshots for the user.

(dict) --
Contains the details for an Amazon Neptune DB cluster snapshot
This data type is used as a response element in the  DescribeDBClusterSnapshots action.

AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.

(string) --


DBClusterSnapshotIdentifier (string) --
Specifies the identifier for a DB cluster snapshot. Must match the identifier of an existing snapshot.
After you restore a DB cluster using a DBClusterSnapshotIdentifier , you must specify the same DBClusterSnapshotIdentifier for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed.
However, if you don\'t specify the DBClusterSnapshotIdentifier , an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the snapshot specified by the DBClusterSnapshotIdentifier , and the original DB cluster is deleted.

DBClusterIdentifier (string) --
Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was created from.

SnapshotCreateTime (datetime) --
Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

Engine (string) --
Specifies the name of the database engine.

AllocatedStorage (integer) --
Specifies the allocated storage size in gibibytes (GiB).

Status (string) --
Specifies the status of this DB cluster snapshot.

Port (integer) --
Specifies the port that the DB cluster was listening on at the time of the snapshot.

VpcId (string) --
Provides the VPC ID associated with the DB cluster snapshot.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

MasterUsername (string) --
Provides the master username for the DB cluster snapshot.

EngineVersion (string) --
Provides the version of the database engine for this DB cluster snapshot.

LicenseModel (string) --
Provides the license model information for this DB cluster snapshot.

SnapshotType (string) --
Provides the type of the DB cluster snapshot.

PercentProgress (integer) --
Specifies the percentage of the estimated data that has been transferred.

StorageEncrypted (boolean) --
Specifies whether the DB cluster snapshot is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.

DBClusterSnapshotArn (string) --
The Amazon Resource Name (ARN) for the DB cluster snapshot.

SourceDBClusterSnapshotArn (string) --
If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.











Exceptions

Neptune.Client.exceptions.DBClusterSnapshotNotFoundFault


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
                'DBClusterSnapshotArn': 'string',
                'SourceDBClusterSnapshotArn': 'string',
                'IAMDatabaseAuthenticationEnabled': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_clusters(DBClusterIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about provisioned DB clusters, and supports pagination.
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
    :param DBClusterIdentifier: The user-supplied DB cluster identifier. If this parameter is specified, information from only the specific DB cluster is returned. This parameter isn\'t case-sensitive.\nConstraints:\n\nIf supplied, must match an existing DBClusterIdentifier.\n\n

    :type Filters: list
    :param Filters: A filter that specifies one or more DB clusters to describe.\nSupported filters:\n\ndb-cluster-id - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB clusters identified by these ARNs.\nengine - Accepts an engine name (such as neptune ), and restricts the results list to DB clusters created by that engine.\n\nFor example, to invoke this API from the AWS CLI and filter so that only Neptune DB clusters are returned, you could use the following command:\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBClusters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'DBClusters': [
        {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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

Marker (string) --
A pagination token that can be used in a subsequent DescribeDBClusters request.

DBClusters (list) --
Contains a list of DB clusters for the user.

(dict) --
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --

AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.


AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --

(Not supported by Neptune)


DatabaseName (string) --
Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --
Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this DB cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --
The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --
Specifies the name of the DB cluster option group.

Status (string) --
Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --
Not supported by Neptune.

ReadReplicaIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --
Provides the list of instances that make up the DB cluster.

(dict) --
Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --
Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --
Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.











Exceptions

Neptune.Client.exceptions.DBClusterNotFoundFault


    :return: {
        'Marker': 'string',
        'DBClusters': [
            {
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
                'MultiAZ': True|False,
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
                ],
                'IAMDatabaseAuthenticationEnabled': True|False,
                'CloneGroupId': 'string',
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
    Returns a list of the available DB engines.
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
    :param DBParameterGroupFamily: The name of a specific DB parameter group family to return details for.\nConstraints:\n\nIf supplied, must match an existing DBParameterGroupFamily.\n\n

    :type Filters: list
    :param Filters: Not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more than the MaxRecords value is available, a pagination token called a marker is included in the response so that the following results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

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
            'DefaultCharacterSet': {
                'CharacterSetName': 'string',
                'CharacterSetDescription': 'string'
            },
            'SupportedCharacterSets': [
                {
                    'CharacterSetName': 'string',
                    'CharacterSetDescription': 'string'
                },
            ],
            'ValidUpgradeTarget': [
                {
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'Description': 'string',
                    'AutoUpgrade': True|False,
                    'IsMajorVersionUpgrade': True|False
                },
            ],
            'SupportedTimezones': [
                {
                    'TimezoneName': 'string'
                },
            ],
            'ExportableLogTypes': [
                'string',
            ],
            'SupportsLogExportsToCloudwatchLogs': True|False,
            'SupportsReadReplica': True|False
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBEngineVersions (list) --
A list of DBEngineVersion elements.

(dict) --
This data type is used as a response element in the action  DescribeDBEngineVersions .

Engine (string) --
The name of the database engine.

EngineVersion (string) --
The version number of the database engine.

DBParameterGroupFamily (string) --
The name of the DB parameter group family for the database engine.

DBEngineDescription (string) --
The description of the database engine.

DBEngineVersionDescription (string) --
The description of the database engine version.

DefaultCharacterSet (dict) --

(Not supported by Neptune)


CharacterSetName (string) --
The name of the character set.

CharacterSetDescription (string) --
The description of the character set.



SupportedCharacterSets (list) --

(Not supported by Neptune)


(dict) --
Specifies a character set.

CharacterSetName (string) --
The name of the character set.

CharacterSetDescription (string) --
The description of the character set.





ValidUpgradeTarget (list) --
A list of engine versions that this database engine version can be upgraded to.

(dict) --
The version of the database engine that a DB instance can be upgraded to.

Engine (string) --
The name of the upgrade target database engine.

EngineVersion (string) --
The version number of the upgrade target database engine.

Description (string) --
The version of the database engine that a DB instance can be upgraded to.

AutoUpgrade (boolean) --
A value that indicates whether the target version is applied to any source DB instances that have AutoMinorVersionUpgrade set to true.

IsMajorVersionUpgrade (boolean) --
A value that indicates whether a database engine is upgraded to a major version.





SupportedTimezones (list) --
A list of the time zones supported by this engine for the Timezone parameter of the CreateDBInstance action.

(dict) --
A time zone associated with a  DBInstance .

TimezoneName (string) --
The name of the time zone.





ExportableLogTypes (list) --
The types of logs that the database engine has available for export to CloudWatch Logs.

(string) --


SupportsLogExportsToCloudwatchLogs (boolean) --
A value that indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.

SupportsReadReplica (boolean) --
Indicates whether the database engine version supports read replicas.












    :return: {
        'Marker': 'string',
        'DBEngineVersions': [
            {
                'Engine': 'string',
                'EngineVersion': 'string',
                'DBParameterGroupFamily': 'string',
                'DBEngineDescription': 'string',
                'DBEngineVersionDescription': 'string',
                'DefaultCharacterSet': {
                    'CharacterSetName': 'string',
                    'CharacterSetDescription': 'string'
                },
                'SupportedCharacterSets': [
                    {
                        'CharacterSetName': 'string',
                        'CharacterSetDescription': 'string'
                    },
                ],
                'ValidUpgradeTarget': [
                    {
                        'Engine': 'string',
                        'EngineVersion': 'string',
                        'Description': 'string',
                        'AutoUpgrade': True|False,
                        'IsMajorVersionUpgrade': True|False
                    },
                ],
                'SupportedTimezones': [
                    {
                        'TimezoneName': 'string'
                    },
                ],
                'ExportableLogTypes': [
                    'string',
                ],
                'SupportsLogExportsToCloudwatchLogs': True|False,
                'SupportsReadReplica': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_db_instances(DBInstanceIdentifier=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns information about provisioned instances, and supports pagination.
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
    :param DBInstanceIdentifier: The user-supplied instance identifier. If this parameter is specified, information from only the specific DB instance is returned. This parameter isn\'t case-sensitive.\nConstraints:\n\nIf supplied, must match the identifier of an existing DBInstance.\n\n

    :type Filters: list
    :param Filters: A filter that specifies one or more DB instances to describe.\nSupported filters:\n\ndb-cluster-id - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB instances associated with the DB clusters identified by these ARNs.\nengine - Accepts an engine name (such as neptune ), and restricts the results list to DB instances created by that engine.\n\nFor example, to invoke this API from the AWS CLI and filter so that only Neptune DB instances are returned, you could use the following command:\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBInstances request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'DBSecurityGroups': [
                {
                    'DBSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'DBParameterGroups': [
                {
                    'DBParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string'
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
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'ReadReplicaSourceDBInstanceIdentifier': 'string',
            'ReadReplicaDBInstanceIdentifiers': [
                'string',
            ],
            'ReadReplicaDBClusterIdentifiers': [
                'string',
            ],
            'LicenseModel': 'string',
            'Iops': 123,
            'OptionGroupMemberships': [
                {
                    'OptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CharacterSetName': 'string',
            'SecondaryAvailabilityZone': 'string',
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'StorageType': 'string',
            'TdeCredentialArn': 'string',
            'DbInstancePort': 123,
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'DomainMemberships': [
                {
                    'Domain': 'string',
                    'Status': 'string',
                    'FQDN': 'string',
                    'IAMRoleName': 'string'
                },
            ],
            'CopyTagsToSnapshot': True|False,
            'MonitoringInterval': 123,
            'EnhancedMonitoringResourceArn': 'string',
            'MonitoringRoleArn': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'Timezone': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False,
            'PerformanceInsightsEnabled': True|False,
            'PerformanceInsightsKMSKeyId': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBInstances (list) --
A list of  DBInstance instances.

(dict) --
Contains the details of an Amazon Neptune DB instance.
This data type is used as a response element in the  DescribeDBInstances action.

DBInstanceIdentifier (string) --
Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the DB instance.

Engine (string) --
Provides the name of the database engine to be used for this DB instance.

DBInstanceStatus (string) --
Specifies the current state of this database.

MasterUsername (string) --
Contains the master username for the DB instance.

DBName (string) --
The database name.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the DB instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



AllocatedStorage (integer) --
Specifies the allocated storage size specified in gibibytes.

InstanceCreateTime (datetime) --
Provides the date and time the DB instance was created.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

DBSecurityGroups (list) --
Provides List of DB security group elements containing only DBSecurityGroup.Name and DBSecurityGroup.Status subelements.

(dict) --
Specifies membership in a designated DB security group.

DBSecurityGroupName (string) --
The name of the DB security group.

Status (string) --
The status of the DB security group.





VpcSecurityGroups (list) --
Provides a list of VPC security group elements that the DB instance belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





DBParameterGroups (list) --
Provides the list of DB parameter groups applied to this DB instance.

(dict) --
The status of the DB parameter group.
This data type is used as a response element in the following actions:

CreateDBInstance
DeleteDBInstance
ModifyDBInstance
RebootDBInstance


DBParameterGroupName (string) --
The name of the DP parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.





AvailabilityZone (string) --
Specifies the name of the Availability Zone the DB instance is located in.

DBSubnetGroup (dict) --
Specifies information on the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --
The name of the DB subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the DB subnet group.

VpcId (string) --
Provides the VpcId of the DB subnet group.

SubnetGroupStatus (string) --
Provides the status of the DB subnet group.

Subnets (list) --
Contains a list of  Subnet elements.

(dict) --
Specifies a subnet.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the EC2 Availability Zone that the subnet is in.

Name (string) --
The name of the availability zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --
Specifies that changes to the DB instance are pending. This element is only included when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --
Contains the new DBInstanceClass for the DB instance that will be applied or is currently being applied.

AllocatedStorage (integer) --
Contains the new AllocatedStorage size for the DB instance that will be applied or is currently being applied.

MasterUserPassword (string) --
Contains the pending or currently-in-progress change of the master credentials for the DB instance.

Port (integer) --
Specifies the pending port for the DB instance.

BackupRetentionPeriod (integer) --
Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --
Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

LicenseModel (string) --
The license model for the DB instance.
Valid values: license-included | bring-your-own-license | general-public-license

Iops (integer) --
Specifies the new Provisioned IOPS value for the DB instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --
Contains the new DBInstanceIdentifier for the DB instance that will be applied or is currently being applied.

StorageType (string) --
Specifies the storage type to be associated with the DB instance.

CACertificateIdentifier (string) --
Specifies the identifier of the CA certificate for the DB instance.

DBSubnetGroupName (string) --
The new DB subnet group for the DB instance.

PendingCloudwatchLogsExports (dict) --
This PendingCloudwatchLogsExports structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.

LogTypesToEnable (list) --
Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --
Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

MultiAZ (boolean) --
Specifies if the DB instance is a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --
Indicates that minor version patches are applied automatically.

ReadReplicaSourceDBInstanceIdentifier (string) --
Contains the identifier of the source DB instance if this DB instance is a Read Replica.

ReadReplicaDBInstanceIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB instance.

(string) --


ReadReplicaDBClusterIdentifiers (list) --
Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

(string) --


LicenseModel (string) --
License model information for this DB instance.

Iops (integer) --
Specifies the Provisioned IOPS (I/O operations per second) value.

OptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Provides information on the option groups the DB instance is a member of.

OptionGroupName (string) --
The name of the option group that the instance belongs to.

Status (string) --
The status of the DB instance\'s option group membership. Valid values are: in-sync , pending-apply , pending-removal , pending-maintenance-apply , pending-maintenance-removal , applying , removing , and failed .





CharacterSetName (string) --

(Not supported by Neptune)


SecondaryAvailabilityZone (string) --
If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.

PubliclyAccessible (boolean) --
This flag should no longer be used.

StatusInfos (list) --
The status of a Read Replica. If the instance is not a Read Replica, this is blank.

(dict) --
Provides a list of status information for a DB instance.

StatusType (string) --
This value is currently "read replication."

Normal (boolean) --
Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --
Status of the DB instance. For a StatusType of read replica, the values can be replicating, error, stopped, or terminated.

Message (string) --
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





StorageType (string) --
Specifies the storage type associated with DB instance.

TdeCredentialArn (string) --
The ARN from the key store with which the instance is associated for TDE encryption.

DbInstancePort (integer) --
Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.

DBClusterIdentifier (string) --
If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

StorageEncrypted (boolean) --
Not supported: The encryption for DB instances is managed by the DB cluster.

KmsKeyId (string) --
Not supported: The encryption for DB instances is managed by the DB cluster.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

DomainMemberships (list) --
Not supported

(dict) --
An Active Directory Domain membership record associated with a DB instance.

Domain (string) --
The identifier of the Active Directory Domain.

Status (string) --
The status of the DB instance\'s Active Directory Domain membership, such as joined, pending-join, failed etc).

FQDN (string) --
The fully qualified domain name of the Active Directory Domain.

IAMRoleName (string) --
The name of the IAM role to be used when making API calls to the Directory Service.





CopyTagsToSnapshot (boolean) --
Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

MonitoringInterval (integer) --
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.

EnhancedMonitoringResourceArn (string) --
The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.

MonitoringRoleArn (string) --
The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --
The Amazon Resource Name (ARN) for the DB instance.

Timezone (string) --
Not supported.

IAMDatabaseAuthenticationEnabled (boolean) --
True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise false.

PerformanceInsightsEnabled (boolean) --

(Not supported by Neptune)


PerformanceInsightsKMSKeyId (string) --

(Not supported by Neptune)


EnabledCloudwatchLogsExports (list) --
A list of log types that this DB instance is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB instance has deletion protection enabled. The instance can\'t be deleted when deletion protection is enabled. See Deleting a DB Instance .











Exceptions

Neptune.Client.exceptions.DBInstanceNotFoundFault


    :return: {
        'Marker': 'string',
        'DBInstances': [
            {
                'DBInstanceIdentifier': 'string',
                'DBInstanceClass': 'string',
                'Engine': 'string',
                'DBInstanceStatus': 'string',
                'MasterUsername': 'string',
                'DBName': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123,
                    'HostedZoneId': 'string'
                },
                'AllocatedStorage': 123,
                'InstanceCreateTime': datetime(2015, 1, 1),
                'PreferredBackupWindow': 'string',
                'BackupRetentionPeriod': 123,
                'DBSecurityGroups': [
                    {
                        'DBSecurityGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'VpcSecurityGroups': [
                    {
                        'VpcSecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'DBParameterGroups': [
                    {
                        'DBParameterGroupName': 'string',
                        'ParameterApplyStatus': 'string'
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
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'ReadReplicaSourceDBInstanceIdentifier': 'string',
                'ReadReplicaDBInstanceIdentifiers': [
                    'string',
                ],
                'ReadReplicaDBClusterIdentifiers': [
                    'string',
                ],
                'LicenseModel': 'string',
                'Iops': 123,
                'OptionGroupMemberships': [
                    {
                        'OptionGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'CharacterSetName': 'string',
                'SecondaryAvailabilityZone': 'string',
                'PubliclyAccessible': True|False,
                'StatusInfos': [
                    {
                        'StatusType': 'string',
                        'Normal': True|False,
                        'Status': 'string',
                        'Message': 'string'
                    },
                ],
                'StorageType': 'string',
                'TdeCredentialArn': 'string',
                'DbInstancePort': 123,
                'DBClusterIdentifier': 'string',
                'StorageEncrypted': True|False,
                'KmsKeyId': 'string',
                'DbiResourceId': 'string',
                'CACertificateIdentifier': 'string',
                'DomainMemberships': [
                    {
                        'Domain': 'string',
                        'Status': 'string',
                        'FQDN': 'string',
                        'IAMRoleName': 'string'
                    },
                ],
                'CopyTagsToSnapshot': True|False,
                'MonitoringInterval': 123,
                'EnhancedMonitoringResourceArn': 'string',
                'MonitoringRoleArn': 'string',
                'PromotionTier': 123,
                'DBInstanceArn': 'string',
                'Timezone': 'string',
                'IAMDatabaseAuthenticationEnabled': True|False,
                'PerformanceInsightsEnabled': True|False,
                'PerformanceInsightsKMSKeyId': 'string',
                'EnabledCloudwatchLogsExports': [
                    'string',
                ],
                'DeletionProtection': True|False
            },
        ]
    }
    
    
    :returns: 
    CreateDBInstance
    DeleteDBInstance
    ModifyDBInstance
    RebootDBInstance
    
    """
    pass

def describe_db_parameter_groups(DBParameterGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of DBParameterGroup descriptions. If a DBParameterGroupName is specified, the list will contain only the description of the specified DB parameter group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_parameter_groups(
        DBParameterGroupName='string',
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
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: The name of a specific DB parameter group to return details for.\nConstraints:\n\nIf supplied, must match the name of an existing DBClusterParameterGroup.\n\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBParameterGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'DBParameterGroups': [
        {
            'DBParameterGroupName': 'string',
            'DBParameterGroupFamily': 'string',
            'Description': 'string',
            'DBParameterGroupArn': 'string'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBParameterGroups (list) --
A list of  DBParameterGroup instances.

(dict) --
Contains the details of an Amazon Neptune DB parameter group.
This data type is used as a response element in the  DescribeDBParameterGroups action.

DBParameterGroupName (string) --
Provides the name of the DB parameter group.

DBParameterGroupFamily (string) --
Provides the name of the DB parameter group family that this DB parameter group is compatible with.

Description (string) --
Provides the customer-specified description for this DB parameter group.

DBParameterGroupArn (string) --
The Amazon Resource Name (ARN) for the DB parameter group.











Exceptions

Neptune.Client.exceptions.DBParameterGroupNotFoundFault


    :return: {
        'Marker': 'string',
        'DBParameterGroups': [
            {
                'DBParameterGroupName': 'string',
                'DBParameterGroupFamily': 'string',
                'Description': 'string',
                'DBParameterGroupArn': 'string'
            },
        ]
    }
    
    
    :returns: 
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def describe_db_parameters(DBParameterGroupName=None, Source=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns the detailed parameter list for a particular DB parameter group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_db_parameters(
        DBParameterGroupName='string',
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
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]\nThe name of a specific DB parameter group to return details for.\nConstraints:\n\nIf supplied, must match the name of an existing DBParameterGroup.\n\n

    :type Source: string
    :param Source: The parameter types to return.\nDefault: All parameter types returned\nValid Values: user | system | engine-default\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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

Parameters (list) --
A list of  Parameter values.

(dict) --
Specifies a parameter.

ParameterName (string) --
Specifies the name of the parameter.

ParameterValue (string) --
Specifies the value of the parameter.

Description (string) --
Provides a description of the parameter.

Source (string) --
Indicates the source of the parameter value.

ApplyType (string) --
Specifies the engine specific parameters type.

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

Neptune.Client.exceptions.DBParameterGroupNotFoundFault


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
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def describe_db_subnet_groups(DBSubnetGroupName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName is specified, the list will contain only the descriptions of the specified DBSubnetGroup.
    For an overview of CIDR ranges, go to the Wikipedia Tutorial .
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
    :param DBSubnetGroupName: The name of the DB subnet group to return details for.

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeDBSubnetGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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

Marker (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

DBSubnetGroups (list) --
A list of  DBSubnetGroup instances.

(dict) --
Contains the details of an Amazon Neptune DB subnet group.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

DBSubnetGroupName (string) --
The name of the DB subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the DB subnet group.

VpcId (string) --
Provides the VpcId of the DB subnet group.

SubnetGroupStatus (string) --
Provides the status of the DB subnet group.

Subnets (list) --
Contains a list of  Subnet elements.

(dict) --
Specifies a subnet.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the EC2 Availability Zone that the subnet is in.

Name (string) --
The name of the availability zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.











Exceptions

Neptune.Client.exceptions.DBSubnetGroupNotFoundFault


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
    Neptune.Client.exceptions.DBSubnetGroupNotFoundFault
    
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
    :param DBParameterGroupFamily: [REQUIRED]\nThe name of the DB cluster parameter group family to return engine parameter information for.\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeEngineDefaultClusterParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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
Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.

DBParameterGroupFamily (string) --
Specifies the name of the DB parameter group family that the engine default parameters apply to.

Marker (string) --
An optional pagination token provided by a previous EngineDefaults request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Parameters (list) --
Contains a list of engine default parameters.

(dict) --
Specifies a parameter.

ParameterName (string) --
Specifies the name of the parameter.

ParameterValue (string) --
Specifies the value of the parameter.

Description (string) --
Provides a description of the parameter.

Source (string) --
Indicates the source of the parameter value.

ApplyType (string) --
Specifies the engine specific parameters type.

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

def describe_engine_default_parameters(DBParameterGroupFamily=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns the default engine and system parameter information for the specified database engine.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_engine_default_parameters(
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
    :param DBParameterGroupFamily: [REQUIRED]\nThe name of the DB parameter group family.\n

    :type Filters: list
    :param Filters: Not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeEngineDefaultParameters request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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
Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.

DBParameterGroupFamily (string) --
Specifies the name of the DB parameter group family that the engine default parameters apply to.

Marker (string) --
An optional pagination token provided by a previous EngineDefaults request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Parameters (list) --
Contains a list of engine default parameters.

(dict) --
Specifies a parameter.

ParameterName (string) --
Specifies the name of the parameter.

ParameterValue (string) --
Specifies the value of the parameter.

Description (string) --
Provides a description of the parameter.

Source (string) --
Indicates the source of the parameter value.

ApplyType (string) --
Specifies the engine specific parameters type.

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
    :param SourceType: The type of source that is generating the events.\nValid values: db-instance | db-parameter-group | db-security-group | db-snapshot\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

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

EventCategoriesMapList (list) --
A list of EventCategoriesMap data types.

(dict) --
Contains the results of a successful invocation of the  DescribeEventCategories action.

SourceType (string) --
The source type that the returned categories belong to

EventCategories (list) --
The event categories for the specified source type

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

def describe_event_subscriptions(SubscriptionName=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Lists all the subscription descriptions for a customer account. The description for a subscription includes SubscriptionName, SNSTopicARN, CustomerID, SourceType, SourceID, CreationTime, and Status.
    If you specify a SubscriptionName, lists the description for that subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_subscriptions(
        SubscriptionName='string',
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
    
    
    :type SubscriptionName: string
    :param SubscriptionName: The name of the event notification subscription you want to describe.

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'EventSubscriptionsList': [
        {
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
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

EventSubscriptionsList (list) --
A list of EventSubscriptions data types.

(dict) --
Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

CustomerAwsId (string) --
The AWS customer account associated with the event notification subscription.

CustSubscriptionId (string) --
The event notification subscription Id.

SnsTopicArn (string) --
The topic ARN of the event notification subscription.

Status (string) --
The status of the event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that Neptune no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --
The time the event notification subscription was created.

SourceType (string) --
The source type for the event notification subscription.

SourceIdsList (list) --
A list of source IDs for the event notification subscription.

(string) --


EventCategoriesList (list) --
A list of event categories for the event notification subscription.

(string) --


Enabled (boolean) --
A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.

EventSubscriptionArn (string) --
The Amazon Resource Name (ARN) for the event subscription.











Exceptions

Neptune.Client.exceptions.SubscriptionNotFoundFault


    :return: {
        'Marker': 'string',
        'EventSubscriptionsList': [
            {
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
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_events(SourceIdentifier=None, SourceType=None, StartTime=None, EndTime=None, Duration=None, EventCategories=None, Filters=None, MaxRecords=None, Marker=None):
    """
    Returns events related to DB instances, DB security groups, DB snapshots, and DB parameter groups for the past 14 days. Events specific to a particular DB instance, DB security group, database snapshot, or DB parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.
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
    :param SourceIdentifier: The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.\nConstraints:\n\nIf SourceIdentifier is supplied, SourceType must also be provided.\nIf the source type is DBInstance , then a DBInstanceIdentifier must be supplied.\nIf the source type is DBSecurityGroup , a DBSecurityGroupName must be supplied.\nIf the source type is DBParameterGroup , a DBParameterGroupName must be supplied.\nIf the source type is DBSnapshot , a DBSnapshotIdentifier must be supplied.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type SourceType: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.

    :type StartTime: datetime
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.\nExample: 2009-07-08T18:00Z\n

    :type EndTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.\nExample: 2009-07-08T18:00Z\n

    :type Duration: integer
    :param Duration: The number of minutes to retrieve events for.\nDefault: 60\n

    :type EventCategories: list
    :param EventCategories: A list of event categories that trigger notifications for a event notification subscription.\n\n(string) --\n\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeEvents request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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

Marker (string) --
An optional pagination token provided by a previous Events request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

Events (list) --
A list of  Event instances.

(dict) --
This data type is used as a response element in the  DescribeEvents action.

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
    Returns a list of orderable DB instance options for the specified engine.
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
    :param Engine: [REQUIRED]\nThe name of the engine to retrieve DB instance options for.\n

    :type EngineVersion: string
    :param EngineVersion: The engine version filter value. Specify this parameter to show only the available offerings matching the specified engine version.

    :type DBInstanceClass: string
    :param DBInstanceClass: The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.

    :type LicenseModel: string
    :param LicenseModel: The license model filter value. Specify this parameter to show only the available offerings matching the specified license model.

    :type Vpc: boolean
    :param Vpc: The VPC filter value. Specify this parameter to show only the available VPC or non-VPC offerings.

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .

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
            'MultiAZCapable': True|False,
            'ReadReplicaCapable': True|False,
            'Vpc': True|False,
            'SupportsStorageEncryption': True|False,
            'StorageType': 'string',
            'SupportsIops': True|False,
            'SupportsEnhancedMonitoring': True|False,
            'SupportsIAMDatabaseAuthentication': True|False,
            'SupportsPerformanceInsights': True|False,
            'MinStorageSize': 123,
            'MaxStorageSize': 123,
            'MinIopsPerDbInstance': 123,
            'MaxIopsPerDbInstance': 123,
            'MinIopsPerGib': 123.0,
            'MaxIopsPerGib': 123.0
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

OrderableDBInstanceOptions (list) --
An  OrderableDBInstanceOption structure containing information about orderable options for the DB instance.

(dict) --
Contains a list of available options for a DB instance.
This data type is used as a response element in the  DescribeOrderableDBInstanceOptions action.

Engine (string) --
The engine type of a DB instance.

EngineVersion (string) --
The engine version of a DB instance.

DBInstanceClass (string) --
The DB instance class for a DB instance.

LicenseModel (string) --
The license model for a DB instance.

AvailabilityZones (list) --
A list of Availability Zones for a DB instance.

(dict) --
Specifies an Availability Zone.

Name (string) --
The name of the availability zone.





MultiAZCapable (boolean) --
Indicates whether a DB instance is Multi-AZ capable.

ReadReplicaCapable (boolean) --
Indicates whether a DB instance can have a Read Replica.

Vpc (boolean) --
Indicates whether a DB instance is in a VPC.

SupportsStorageEncryption (boolean) --
Indicates whether a DB instance supports encrypted storage.

StorageType (string) --
Indicates the storage type for a DB instance.

SupportsIops (boolean) --
Indicates whether a DB instance supports provisioned IOPS.

SupportsEnhancedMonitoring (boolean) --
Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.

SupportsIAMDatabaseAuthentication (boolean) --
Indicates whether a DB instance supports IAM database authentication.

SupportsPerformanceInsights (boolean) --

(Not supported by Neptune)


MinStorageSize (integer) --
Minimum storage size for a DB instance.

MaxStorageSize (integer) --
Maximum storage size for a DB instance.

MinIopsPerDbInstance (integer) --
Minimum total provisioned IOPS for a DB instance.

MaxIopsPerDbInstance (integer) --
Maximum total provisioned IOPS for a DB instance.

MinIopsPerGib (float) --
Minimum provisioned IOPS per GiB for a DB instance.

MaxIopsPerGib (float) --
Maximum provisioned IOPS per GiB for a DB instance.





Marker (string) --
An optional pagination token provided by a previous OrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .








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
                'MultiAZCapable': True|False,
                'ReadReplicaCapable': True|False,
                'Vpc': True|False,
                'SupportsStorageEncryption': True|False,
                'StorageType': 'string',
                'SupportsIops': True|False,
                'SupportsEnhancedMonitoring': True|False,
                'SupportsIAMDatabaseAuthentication': True|False,
                'SupportsPerformanceInsights': True|False,
                'MinStorageSize': 123,
                'MaxStorageSize': 123,
                'MinIopsPerDbInstance': 123,
                'MaxIopsPerDbInstance': 123,
                'MinIopsPerGib': 123.0,
                'MaxIopsPerGib': 123.0
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_pending_maintenance_actions(ResourceIdentifier=None, Filters=None, Marker=None, MaxRecords=None):
    """
    Returns a list of resources (for example, DB instances) that have at least one pending maintenance action.
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
    :param Filters: A filter that specifies one or more resources to return pending maintenance actions for.\nSupported filters:\n\ndb-cluster-id - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include pending maintenance actions for the DB clusters identified by these ARNs.\ndb-instance-id - Accepts DB instance identifiers and DB instance ARNs. The results list will only include pending maintenance actions for the DB instances identified by these ARNs.\n\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribePendingMaintenanceActions request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by MaxRecords .

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.\nDefault: 100\nConstraints: Minimum 20, maximum 100.\n

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

PendingMaintenanceActions (list) --
A list of the pending maintenance actions for the resource.

(dict) --
Describes the pending maintenance actions for a resource.

ResourceIdentifier (string) --
The ARN of the resource that has pending maintenance actions.

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
The effective date when the pending maintenance action is applied to the resource. This date takes into account opt-in requests received from the  ApplyPendingMaintenanceAction API, the AutoAppliedAfterDate , and the ForcedApplyDate . This value is blank if an opt-in request has not been received and nothing has been specified as AutoAppliedAfterDate or ForcedApplyDate .

Description (string) --
A description providing more detail about the maintenance action.









Marker (string) --
An optional pagination token provided by a previous DescribePendingMaintenanceActions request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by MaxRecords .







Exceptions

Neptune.Client.exceptions.ResourceNotFoundFault


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
    Neptune.Client.exceptions.ResourceNotFoundFault
    
    """
    pass

def describe_valid_db_instance_modifications(DBInstanceIdentifier=None):
    """
    You can call  DescribeValidDBInstanceModifications to learn what modifications you can make to your DB instance. You can use this information when you call  ModifyDBInstance .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_valid_db_instance_modifications(
        DBInstanceIdentifier='string'
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]\nThe customer identifier or the ARN of your DB instance.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ValidDBInstanceModificationsMessage': {
        'Storage': [
            {
                'StorageType': 'string',
                'StorageSize': [
                    {
                        'From': 123,
                        'To': 123,
                        'Step': 123
                    },
                ],
                'ProvisionedIops': [
                    {
                        'From': 123,
                        'To': 123,
                        'Step': 123
                    },
                ],
                'IopsToStorageRatio': [
                    {
                        'From': 123.0,
                        'To': 123.0
                    },
                ]
            },
        ]
    }
}


Response Structure

(dict) --
ValidDBInstanceModificationsMessage (dict) --Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the  DescribeValidDBInstanceModifications action. You can use this information when you call  ModifyDBInstance .

Storage (list) --Valid storage options for your DB instance.

(dict) --Information about valid modifications that you can make to your DB instance.
Contains the result of a successful call to the  DescribeValidDBInstanceModifications action.

StorageType (string) --The valid storage types for your DB instance. For example, gp2, io1.

StorageSize (list) --The valid range of storage in gibibytes. For example, 100 to 16384.

(dict) --A range of integer values.

From (integer) --The minimum value in the range.

To (integer) --The maximum value in the range.

Step (integer) --The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isn\'t a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000...





ProvisionedIops (list) --The valid range of provisioned IOPS. For example, 1000-20000.

(dict) --A range of integer values.

From (integer) --The minimum value in the range.

To (integer) --The maximum value in the range.

Step (integer) --The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isn\'t a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000...





IopsToStorageRatio (list) --The valid range of Provisioned IOPS to gibibytes of storage multiplier. For example, 3-10, which means that provisioned IOPS can be between 3 and 10 times storage.

(dict) --A range of double values.

From (float) --The minimum value in the range.

To (float) --The maximum value in the range.
















Exceptions

Neptune.Client.exceptions.DBInstanceNotFoundFault
Neptune.Client.exceptions.InvalidDBInstanceStateFault


    :return: {
        'ValidDBInstanceModificationsMessage': {
            'Storage': [
                {
                    'StorageType': 'string',
                    'StorageSize': [
                        {
                            'From': 123,
                            'To': 123,
                            'Step': 123
                        },
                    ],
                    'ProvisionedIops': [
                        {
                            'From': 123,
                            'To': 123,
                            'Step': 123
                        },
                    ],
                    'IopsToStorageRatio': [
                        {
                            'From': 123.0,
                            'To': 123.0
                        },
                    ]
                },
            ]
        }
    }
    
    
    """
    pass

def failover_db_cluster(DBClusterIdentifier=None, TargetDBInstanceIdentifier=None):
    """
    Forces a failover for a DB cluster.
    A failover for a DB cluster promotes one of the Read Replicas (read-only instances) in the DB cluster to be the primary instance (the cluster writer).
    Amazon Neptune will automatically fail over to a Read Replica, if one exists, when the primary instance fails. You can force a failover when you want to simulate a failure of a primary instance for testing. Because each instance in a DB cluster has its own endpoint address, you will need to clean up and re-establish any existing connections that use those endpoint addresses when the failover is complete.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.failover_db_cluster(
        DBClusterIdentifier='string',
        TargetDBInstanceIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: A DB cluster identifier to force a failover for. This parameter is not case-sensitive.\nConstraints:\n\nMust match the identifier of an existing DBCluster.\n\n

    :type TargetDBInstanceIdentifier: string
    :param TargetDBInstanceIdentifier: The name of the instance to promote to the primary instance.\nYou must specify the instance identifier for an Read Replica in the DB cluster. For example, mydbcluster-replica1 .\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'MultiAZ': True|False,
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
        ],
        'IAMDatabaseAuthenticationEnabled': True|False,
        'CloneGroupId': 'string',
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
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --

AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.


AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --

(Not supported by Neptune)


DatabaseName (string) --
Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --
Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this DB cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --
The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --
Specifies the name of the DB cluster option group.

Status (string) --
Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --
Not supported by Neptune.

ReadReplicaIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --
Provides the list of instances that make up the DB cluster.

(dict) --
Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --
Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --
Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.









Exceptions

Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.InvalidDBInstanceStateFault


    :return: {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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
    Lists all tags on an Amazon Neptune resource.
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
    :param ResourceName: [REQUIRED]\nThe Amazon Neptune resource with tags to be listed. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .\n

    :type Filters: list
    :param Filters: This parameter is not currently supported.\n\n(dict) --This type is not currently supported.\n\nName (string) -- [REQUIRED]This parameter is not currently supported.\n\nValues (list) -- [REQUIRED]This parameter is not currently supported.\n\n(string) --\n\n\n\n\n\n

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

TagList (list) --
List of tags returned by the ListTagsForResource operation.

(dict) --
Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

Key (string) --
A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with "aws:" or "rds:". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

Value (string) --
A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with "aws:" or "rds:". The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").











Exceptions

Neptune.Client.exceptions.DBInstanceNotFoundFault
Neptune.Client.exceptions.DBSnapshotNotFoundFault
Neptune.Client.exceptions.DBClusterNotFoundFault


    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    Neptune.Client.exceptions.DBInstanceNotFoundFault
    Neptune.Client.exceptions.DBSnapshotNotFoundFault
    Neptune.Client.exceptions.DBClusterNotFoundFault
    
    """
    pass

def modify_db_cluster(DBClusterIdentifier=None, NewDBClusterIdentifier=None, ApplyImmediately=None, BackupRetentionPeriod=None, DBClusterParameterGroupName=None, VpcSecurityGroupIds=None, Port=None, MasterUserPassword=None, OptionGroupName=None, PreferredBackupWindow=None, PreferredMaintenanceWindow=None, EnableIAMDatabaseAuthentication=None, CloudwatchLogsExportConfiguration=None, EngineVersion=None, DeletionProtection=None):
    """
    Modify a setting for a DB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.
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
        OptionGroupName='string',
        PreferredBackupWindow='string',
        PreferredMaintenanceWindow='string',
        EnableIAMDatabaseAuthentication=True|False,
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
    :param DBClusterIdentifier: [REQUIRED]\nThe DB cluster identifier for the cluster being modified. This parameter is not case-sensitive.\nConstraints:\n\nMust match the identifier of an existing DBCluster.\n\n

    :type NewDBClusterIdentifier: string
    :param NewDBClusterIdentifier: The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens\nThe first character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\nExample: my-cluster2\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: A value that specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the DB cluster. If this parameter is set to false , changes to the DB cluster are applied during the next maintenance window.\nThe ApplyImmediately parameter only affects the NewDBClusterIdentifier and MasterUserPassword values. If you set the ApplyImmediately parameter value to false, then changes to the NewDBClusterIdentifier and MasterUserPassword values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the ApplyImmediately parameter.\nDefault: false\n

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: The number of days for which automated backups are retained. You must specify a minimum value of 1.\nDefault: 1\nConstraints:\n\nMust be a value from 1 to 35\n\n

    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of the DB cluster parameter group to use for the DB cluster.

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of VPC security groups that the DB cluster will belong to.\n\n(string) --\n\n

    :type Port: integer
    :param Port: The port number on which the DB cluster accepts connections.\nConstraints: Value must be 1150-65535\nDefault: The same port as the original DB cluster.\n

    :type MasterUserPassword: string
    :param MasterUserPassword: The new password for the master database user. This password can contain any printable ASCII character except '/', ''', or '@'.\nConstraints: Must contain from 8 to 41 characters.\n

    :type OptionGroupName: string
    :param OptionGroupName: (Not supported by Neptune)

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region.\nConstraints:\n\nMust be in the format hh24:mi-hh24:mi .\nMust be in Universal Coordinated Time (UTC).\nMust not conflict with the preferred maintenance window.\nMust be at least 30 minutes.\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).\nFormat: ddd:hh24:mi-ddd:hh24:mi\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.\nValid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.\nConstraints: Minimum 30-minute window.\n

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.\nDefault: false\n

    :type CloudwatchLogsExportConfiguration: dict
    :param CloudwatchLogsExportConfiguration: The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB cluster.\n\nEnableLogTypes (list) --The list of log types to enable.\n\n(string) --\n\n\nDisableLogTypes (list) --The list of log types to disable.\n\n(string) --\n\n\n\n

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine. Currently, setting this parameter has no effect. To upgrade your database engine to the most recent release, use the ApplyPendingMaintenanceAction API.\nFor a list of valid engine versions, see CreateDBInstance , or call DescribeDBEngineVersions .\n

    :type DeletionProtection: boolean
    :param DeletionProtection: A value that indicates whether the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled. By default, deletion protection is disabled.

    :rtype: dict

ReturnsResponse Syntax
{
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
        'MultiAZ': True|False,
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
        ],
        'IAMDatabaseAuthenticationEnabled': True|False,
        'CloneGroupId': 'string',
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
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --

AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.


AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --

(Not supported by Neptune)


DatabaseName (string) --
Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --
Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this DB cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --
The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --
Specifies the name of the DB cluster option group.

Status (string) --
Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --
Not supported by Neptune.

ReadReplicaIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --
Provides the list of instances that make up the DB cluster.

(dict) --
Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --
Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --
Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.









Exceptions

Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.StorageQuotaExceededFault
Neptune.Client.exceptions.DBSubnetGroupNotFoundFault
Neptune.Client.exceptions.InvalidVPCNetworkStateFault
Neptune.Client.exceptions.InvalidDBSubnetGroupStateFault
Neptune.Client.exceptions.InvalidSubnet
Neptune.Client.exceptions.DBClusterParameterGroupNotFoundFault
Neptune.Client.exceptions.InvalidDBSecurityGroupStateFault
Neptune.Client.exceptions.InvalidDBInstanceStateFault
Neptune.Client.exceptions.DBClusterAlreadyExistsFault


    :return: {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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
    Modifies the parameters of a DB cluster parameter group. To modify more than one parameter, submit a list of the following: ParameterName , ParameterValue , and ApplyMethod . A maximum of 20 parameters can be modified in a single request.
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
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of the DB cluster parameter group to modify.\n

    :type Parameters: list
    :param Parameters: [REQUIRED]\nA list of parameters in the DB cluster parameter group to modify.\n\n(dict) --Specifies a parameter.\n\nParameterName (string) --Specifies the name of the parameter.\n\nParameterValue (string) --Specifies the value of the parameter.\n\nDescription (string) --Provides a description of the parameter.\n\nSource (string) --Indicates the source of the parameter value.\n\nApplyType (string) --Specifies the engine specific parameters type.\n\nDataType (string) --Specifies the valid data type for the parameter.\n\nAllowedValues (string) --Specifies the valid range of values for the parameter.\n\nIsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.\n\nMinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.\n\nApplyMethod (string) --Indicates when to apply parameter updates.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBClusterParameterGroupName': 'string'
}


Response Structure

(dict) --

DBClusterParameterGroupName (string) --
The name of the DB cluster parameter group.
Constraints:

Must be 1 to 255 letters or numbers.
First character must be a letter
Cannot end with a hyphen or contain two consecutive hyphens


Note
This value is stored as a lowercase string.








Exceptions

Neptune.Client.exceptions.DBParameterGroupNotFoundFault
Neptune.Client.exceptions.InvalidDBParameterGroupStateFault


    :return: {
        'DBClusterParameterGroupName': 'string'
    }
    
    
    :returns: 
    Must be 1 to 255 letters or numbers.
    First character must be a letter
    Cannot end with a hyphen or contain two consecutive hyphens
    
    """
    pass

def modify_db_cluster_snapshot_attribute(DBClusterSnapshotIdentifier=None, AttributeName=None, ValuesToAdd=None, ValuesToRemove=None):
    """
    Adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.
    To share a manual DB cluster snapshot with other AWS accounts, specify restore as the AttributeName and use the ValuesToAdd parameter to add a list of IDs of the AWS accounts that are authorized to restore the manual DB cluster snapshot. Use the value all to make the manual DB cluster snapshot public, which means that it can be copied or restored by all AWS accounts. Do not add the all value for any manual DB cluster snapshots that contain private information that you don\'t want available to all AWS accounts. If a manual DB cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized AWS account IDs for the ValuesToAdd parameter. You can\'t use all as a value for that parameter in this case.
    To view which AWS accounts have access to copy or restore a manual DB cluster snapshot, or whether a manual DB cluster snapshot public or private, use the  DescribeDBClusterSnapshotAttributes API action.
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
    :param DBClusterSnapshotIdentifier: [REQUIRED]\nThe identifier for the DB cluster snapshot to modify the attributes for.\n

    :type AttributeName: string
    :param AttributeName: [REQUIRED]\nThe name of the DB cluster snapshot attribute to modify.\nTo manage authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this value to restore .\n

    :type ValuesToAdd: list
    :param ValuesToAdd: A list of DB cluster snapshot attributes to add to the attribute specified by AttributeName .\nTo authorize other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account IDs, or all to make the manual DB cluster snapshot restorable by any AWS account. Do not add the all value for any manual DB cluster snapshots that contain private information that you don\'t want available to all AWS accounts.\n\n(string) --\n\n

    :type ValuesToRemove: list
    :param ValuesToRemove: A list of DB cluster snapshot attributes to remove from the attribute specified by AttributeName .\nTo remove authorization for other AWS accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more AWS account identifiers, or all to remove authorization for any AWS account to copy or restore the DB cluster snapshot. If you specify all , an AWS account whose account ID is explicitly added to the restore attribute can still copy or restore a manual DB cluster snapshot.\n\n(string) --\n\n

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
Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API action.
Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.

DBClusterSnapshotIdentifier (string) --
The identifier of the manual DB cluster snapshot that the attributes apply to.

DBClusterSnapshotAttributes (list) --
The list of attributes and values for the manual DB cluster snapshot.

(dict) --
Contains the name and values of a manual DB cluster snapshot attribute.
Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore a manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.

AttributeName (string) --
The name of the manual DB cluster snapshot attribute.
The attribute named restore refers to the list of AWS accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the  ModifyDBClusterSnapshotAttribute API action.

AttributeValues (list) --
The value(s) for the manual DB cluster snapshot attribute.
If the AttributeName field is set to restore , then this element returns a list of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of all is in the list, then the manual DB cluster snapshot is public and available for any AWS account to copy or restore.

(string) --














Exceptions

Neptune.Client.exceptions.DBClusterSnapshotNotFoundFault
Neptune.Client.exceptions.InvalidDBClusterSnapshotStateFault
Neptune.Client.exceptions.SharedSnapshotQuotaExceededFault


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

def modify_db_instance(DBInstanceIdentifier=None, AllocatedStorage=None, DBInstanceClass=None, DBSubnetGroupName=None, DBSecurityGroups=None, VpcSecurityGroupIds=None, ApplyImmediately=None, MasterUserPassword=None, DBParameterGroupName=None, BackupRetentionPeriod=None, PreferredBackupWindow=None, PreferredMaintenanceWindow=None, MultiAZ=None, EngineVersion=None, AllowMajorVersionUpgrade=None, AutoMinorVersionUpgrade=None, LicenseModel=None, Iops=None, OptionGroupName=None, NewDBInstanceIdentifier=None, StorageType=None, TdeCredentialArn=None, TdeCredentialPassword=None, CACertificateIdentifier=None, Domain=None, CopyTagsToSnapshot=None, MonitoringInterval=None, DBPortNumber=None, PubliclyAccessible=None, MonitoringRoleArn=None, DomainIAMRoleName=None, PromotionTier=None, EnableIAMDatabaseAuthentication=None, EnablePerformanceInsights=None, PerformanceInsightsKMSKeyId=None, CloudwatchLogsExportConfiguration=None, DeletionProtection=None):
    """
    Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. To learn what modifications you can make to your DB instance, call  DescribeValidDBInstanceModifications before you call  ModifyDBInstance .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_db_instance(
        DBInstanceIdentifier='string',
        AllocatedStorage=123,
        DBInstanceClass='string',
        DBSubnetGroupName='string',
        DBSecurityGroups=[
            'string',
        ],
        VpcSecurityGroupIds=[
            'string',
        ],
        ApplyImmediately=True|False,
        MasterUserPassword='string',
        DBParameterGroupName='string',
        BackupRetentionPeriod=123,
        PreferredBackupWindow='string',
        PreferredMaintenanceWindow='string',
        MultiAZ=True|False,
        EngineVersion='string',
        AllowMajorVersionUpgrade=True|False,
        AutoMinorVersionUpgrade=True|False,
        LicenseModel='string',
        Iops=123,
        OptionGroupName='string',
        NewDBInstanceIdentifier='string',
        StorageType='string',
        TdeCredentialArn='string',
        TdeCredentialPassword='string',
        CACertificateIdentifier='string',
        Domain='string',
        CopyTagsToSnapshot=True|False,
        MonitoringInterval=123,
        DBPortNumber=123,
        PubliclyAccessible=True|False,
        MonitoringRoleArn='string',
        DomainIAMRoleName='string',
        PromotionTier=123,
        EnableIAMDatabaseAuthentication=True|False,
        EnablePerformanceInsights=True|False,
        PerformanceInsightsKMSKeyId='string',
        CloudwatchLogsExportConfiguration={
            'EnableLogTypes': [
                'string',
            ],
            'DisableLogTypes': [
                'string',
            ]
        },
        DeletionProtection=True|False
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]\nThe DB instance identifier. This value is stored as a lowercase string.\nConstraints:\n\nMust match the identifier of an existing DBInstance.\n\n

    :type AllocatedStorage: integer
    :param AllocatedStorage: The new amount of storage (in gibibytes) to allocate for the DB instance.\nNot applicable. Storage is managed by the DB Cluster.\n

    :type DBInstanceClass: string
    :param DBInstanceClass: The new compute and memory capacity of the DB instance, for example, db.m4.large . Not all DB instance classes are available in all AWS Regions.\nIf you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless ApplyImmediately is specified as true for this request.\nDefault: Uses existing setting\n

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC.\nChanging the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you specify true for the ApplyImmediately parameter.\nConstraints: If supplied, must match the name of an existing DBSubnetGroup.\nExample: mySubnetGroup\n

    :type DBSecurityGroups: list
    :param DBSecurityGroups: A list of DB security groups to authorize on this DB instance. Changing this setting doesn\'t result in an outage and the change is asynchronously applied as soon as possible.\nConstraints:\n\nIf supplied, must match existing DBSecurityGroups.\n\n\n(string) --\n\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of EC2 VPC security groups to authorize on this DB instance. This change is asynchronously applied as soon as possible.\nNot applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see ModifyDBCluster .\nConstraints:\n\nIf supplied, must match existing VpcSecurityGroupIds.\n\n\n(string) --\n\n

    :type ApplyImmediately: boolean
    :param ApplyImmediately: Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the DB instance.\nIf this parameter is set to false , changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to RebootDBInstance , or the next failure reboot.\nDefault: false\n

    :type MasterUserPassword: string
    :param MasterUserPassword: Not applicable.

    :type DBParameterGroupName: string
    :param DBParameterGroupName: The name of the DB parameter group to apply to the DB instance. Changing this setting doesn\'t result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. The db instance will NOT be rebooted automatically and the parameter changes will NOT be applied during the next maintenance window.\nDefault: Uses existing setting\nConstraints: The DB parameter group must be in the same DB parameter group family as this DB instance.\n

    :type BackupRetentionPeriod: integer
    :param BackupRetentionPeriod: Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see ModifyDBCluster .\nDefault: Uses existing setting\n

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The daily time range during which automated backups are created if automated backups are enabled.\nNot applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see ModifyDBCluster .\nConstraints:\n\nMust be in the format hh24:mi-hh24:mi\nMust be in Universal Time Coordinated (UTC)\nMust not conflict with the preferred maintenance window\nMust be at least 30 minutes\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn\'t result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter will cause a reboot of the DB instance. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.\nDefault: Uses existing setting\nFormat: ddd:hh24:mi-ddd:hh24:mi\nValid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun\nConstraints: Must be at least 30 minutes\n

    :type MultiAZ: boolean
    :param MultiAZ: Specifies if the DB instance is a Multi-AZ deployment. Changing this parameter doesn\'t result in an outage and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request.

    :type EngineVersion: string
    :param EngineVersion: The version number of the database engine to upgrade to. Currently, setting this parameter has no effect. To upgrade your database engine to the most recent release, use the ApplyPendingMaintenanceAction API.

    :type AllowMajorVersionUpgrade: boolean
    :param AllowMajorVersionUpgrade: Indicates that major version upgrades are allowed. Changing this parameter doesn\'t result in an outage and the change is asynchronously applied as soon as possible.

    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor version upgrades are applied automatically to the DB instance during the maintenance window. Changing this parameter doesn\'t result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to true during the maintenance window, and a newer minor version is available, and Neptune has enabled auto patching for that engine version.

    :type LicenseModel: string
    :param LicenseModel: Not supported.

    :type Iops: integer
    :param Iops: The new Provisioned IOPS (I/O operations per second) value for the instance.\nChanging this setting doesn\'t result in an outage and the change is applied during the next maintenance window unless the ApplyImmediately parameter is set to true for this request.\nDefault: Uses existing setting\n

    :type OptionGroupName: string
    :param OptionGroupName: (Not supported by Neptune)

    :type NewDBInstanceIdentifier: string
    :param NewDBInstanceIdentifier: The new DB instance identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot will occur immediately if you set Apply Immediately to true, or will occur during the next maintenance window if Apply Immediately to false. This value is stored as a lowercase string.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens.\nThe first character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\nExample: mydbinstance\n

    :type StorageType: string
    :param StorageType: Not supported.

    :type TdeCredentialArn: string
    :param TdeCredentialArn: The ARN from the key store with which to associate the instance for TDE encryption.

    :type TdeCredentialPassword: string
    :param TdeCredentialPassword: The password for the given ARN from the key store in order to access the device.

    :type CACertificateIdentifier: string
    :param CACertificateIdentifier: Indicates the certificate that needs to be associated with the instance.

    :type Domain: string
    :param Domain: Not supported.

    :type CopyTagsToSnapshot: boolean
    :param CopyTagsToSnapshot: True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.

    :type MonitoringInterval: integer
    :param MonitoringInterval: The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.\nIf MonitoringRoleArn is specified, then you must also set MonitoringInterval to a value other than 0.\nValid Values: 0, 1, 5, 10, 15, 30, 60\n

    :type DBPortNumber: integer
    :param DBPortNumber: The port number on which the database accepts connections.\nThe value of the DBPortNumber parameter must not match any of the port values specified for options in the option group for the DB instance.\nYour database will restart when you change the DBPortNumber value regardless of the value of the ApplyImmediately parameter.\nDefault: 8182\n

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: This flag should no longer be used.

    :type MonitoringRoleArn: string
    :param MonitoringRoleArn: The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, arn:aws:iam:123456789012:role/emaccess .\nIf MonitoringInterval is set to a value other than 0, then you must supply a MonitoringRoleArn value.\n

    :type DomainIAMRoleName: string
    :param DomainIAMRoleName: Not supported

    :type PromotionTier: integer
    :param PromotionTier: A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.\nDefault: 1\nValid Values: 0 - 15\n

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.\nYou can enable IAM database authentication for the following database engines\nNot applicable. Mapping AWS IAM accounts to database accounts is managed by the DB cluster. For more information, see ModifyDBCluster .\nDefault: false\n

    :type EnablePerformanceInsights: boolean
    :param EnablePerformanceInsights: (Not supported by Neptune)

    :type PerformanceInsightsKMSKeyId: string
    :param PerformanceInsightsKMSKeyId: (Not supported by Neptune)

    :type CloudwatchLogsExportConfiguration: dict
    :param CloudwatchLogsExportConfiguration: The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB instance or DB cluster.\n\nEnableLogTypes (list) --The list of log types to enable.\n\n(string) --\n\n\nDisableLogTypes (list) --The list of log types to disable.\n\n(string) --\n\n\n\n

    :type DeletionProtection: boolean
    :param DeletionProtection: A value that indicates whether the DB instance has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled. By default, deletion protection is disabled. See Deleting a DB Instance .

    :rtype: dict

ReturnsResponse Syntax
{
    'DBInstance': {
        'DBInstanceIdentifier': 'string',
        'DBInstanceClass': 'string',
        'Engine': 'string',
        'DBInstanceStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123,
            'HostedZoneId': 'string'
        },
        'AllocatedStorage': 123,
        'InstanceCreateTime': datetime(2015, 1, 1),
        'PreferredBackupWindow': 'string',
        'BackupRetentionPeriod': 123,
        'DBSecurityGroups': [
            {
                'DBSecurityGroupName': 'string',
                'Status': 'string'
            },
        ],
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'DBParameterGroups': [
            {
                'DBParameterGroupName': 'string',
                'ParameterApplyStatus': 'string'
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
        'MultiAZ': True|False,
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'ReadReplicaSourceDBInstanceIdentifier': 'string',
        'ReadReplicaDBInstanceIdentifiers': [
            'string',
        ],
        'ReadReplicaDBClusterIdentifiers': [
            'string',
        ],
        'LicenseModel': 'string',
        'Iops': 123,
        'OptionGroupMemberships': [
            {
                'OptionGroupName': 'string',
                'Status': 'string'
            },
        ],
        'CharacterSetName': 'string',
        'SecondaryAvailabilityZone': 'string',
        'PubliclyAccessible': True|False,
        'StatusInfos': [
            {
                'StatusType': 'string',
                'Normal': True|False,
                'Status': 'string',
                'Message': 'string'
            },
        ],
        'StorageType': 'string',
        'TdeCredentialArn': 'string',
        'DbInstancePort': 123,
        'DBClusterIdentifier': 'string',
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DbiResourceId': 'string',
        'CACertificateIdentifier': 'string',
        'DomainMemberships': [
            {
                'Domain': 'string',
                'Status': 'string',
                'FQDN': 'string',
                'IAMRoleName': 'string'
            },
        ],
        'CopyTagsToSnapshot': True|False,
        'MonitoringInterval': 123,
        'EnhancedMonitoringResourceArn': 'string',
        'MonitoringRoleArn': 'string',
        'PromotionTier': 123,
        'DBInstanceArn': 'string',
        'Timezone': 'string',
        'IAMDatabaseAuthenticationEnabled': True|False,
        'PerformanceInsightsEnabled': True|False,
        'PerformanceInsightsKMSKeyId': 'string',
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBInstance (dict) --
Contains the details of an Amazon Neptune DB instance.
This data type is used as a response element in the  DescribeDBInstances action.

DBInstanceIdentifier (string) --
Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the DB instance.

Engine (string) --
Provides the name of the database engine to be used for this DB instance.

DBInstanceStatus (string) --
Specifies the current state of this database.

MasterUsername (string) --
Contains the master username for the DB instance.

DBName (string) --
The database name.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the DB instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



AllocatedStorage (integer) --
Specifies the allocated storage size specified in gibibytes.

InstanceCreateTime (datetime) --
Provides the date and time the DB instance was created.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

DBSecurityGroups (list) --
Provides List of DB security group elements containing only DBSecurityGroup.Name and DBSecurityGroup.Status subelements.

(dict) --
Specifies membership in a designated DB security group.

DBSecurityGroupName (string) --
The name of the DB security group.

Status (string) --
The status of the DB security group.





VpcSecurityGroups (list) --
Provides a list of VPC security group elements that the DB instance belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





DBParameterGroups (list) --
Provides the list of DB parameter groups applied to this DB instance.

(dict) --
The status of the DB parameter group.
This data type is used as a response element in the following actions:

CreateDBInstance
DeleteDBInstance
ModifyDBInstance
RebootDBInstance


DBParameterGroupName (string) --
The name of the DP parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.





AvailabilityZone (string) --
Specifies the name of the Availability Zone the DB instance is located in.

DBSubnetGroup (dict) --
Specifies information on the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --
The name of the DB subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the DB subnet group.

VpcId (string) --
Provides the VpcId of the DB subnet group.

SubnetGroupStatus (string) --
Provides the status of the DB subnet group.

Subnets (list) --
Contains a list of  Subnet elements.

(dict) --
Specifies a subnet.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the EC2 Availability Zone that the subnet is in.

Name (string) --
The name of the availability zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --
Specifies that changes to the DB instance are pending. This element is only included when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --
Contains the new DBInstanceClass for the DB instance that will be applied or is currently being applied.

AllocatedStorage (integer) --
Contains the new AllocatedStorage size for the DB instance that will be applied or is currently being applied.

MasterUserPassword (string) --
Contains the pending or currently-in-progress change of the master credentials for the DB instance.

Port (integer) --
Specifies the pending port for the DB instance.

BackupRetentionPeriod (integer) --
Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --
Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

LicenseModel (string) --
The license model for the DB instance.
Valid values: license-included | bring-your-own-license | general-public-license

Iops (integer) --
Specifies the new Provisioned IOPS value for the DB instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --
Contains the new DBInstanceIdentifier for the DB instance that will be applied or is currently being applied.

StorageType (string) --
Specifies the storage type to be associated with the DB instance.

CACertificateIdentifier (string) --
Specifies the identifier of the CA certificate for the DB instance.

DBSubnetGroupName (string) --
The new DB subnet group for the DB instance.

PendingCloudwatchLogsExports (dict) --
This PendingCloudwatchLogsExports structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.

LogTypesToEnable (list) --
Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --
Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

MultiAZ (boolean) --
Specifies if the DB instance is a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --
Indicates that minor version patches are applied automatically.

ReadReplicaSourceDBInstanceIdentifier (string) --
Contains the identifier of the source DB instance if this DB instance is a Read Replica.

ReadReplicaDBInstanceIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB instance.

(string) --


ReadReplicaDBClusterIdentifiers (list) --
Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

(string) --


LicenseModel (string) --
License model information for this DB instance.

Iops (integer) --
Specifies the Provisioned IOPS (I/O operations per second) value.

OptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Provides information on the option groups the DB instance is a member of.

OptionGroupName (string) --
The name of the option group that the instance belongs to.

Status (string) --
The status of the DB instance\'s option group membership. Valid values are: in-sync , pending-apply , pending-removal , pending-maintenance-apply , pending-maintenance-removal , applying , removing , and failed .





CharacterSetName (string) --

(Not supported by Neptune)


SecondaryAvailabilityZone (string) --
If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.

PubliclyAccessible (boolean) --
This flag should no longer be used.

StatusInfos (list) --
The status of a Read Replica. If the instance is not a Read Replica, this is blank.

(dict) --
Provides a list of status information for a DB instance.

StatusType (string) --
This value is currently "read replication."

Normal (boolean) --
Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --
Status of the DB instance. For a StatusType of read replica, the values can be replicating, error, stopped, or terminated.

Message (string) --
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





StorageType (string) --
Specifies the storage type associated with DB instance.

TdeCredentialArn (string) --
The ARN from the key store with which the instance is associated for TDE encryption.

DbInstancePort (integer) --
Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.

DBClusterIdentifier (string) --
If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

StorageEncrypted (boolean) --
Not supported: The encryption for DB instances is managed by the DB cluster.

KmsKeyId (string) --
Not supported: The encryption for DB instances is managed by the DB cluster.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

DomainMemberships (list) --
Not supported

(dict) --
An Active Directory Domain membership record associated with a DB instance.

Domain (string) --
The identifier of the Active Directory Domain.

Status (string) --
The status of the DB instance\'s Active Directory Domain membership, such as joined, pending-join, failed etc).

FQDN (string) --
The fully qualified domain name of the Active Directory Domain.

IAMRoleName (string) --
The name of the IAM role to be used when making API calls to the Directory Service.





CopyTagsToSnapshot (boolean) --
Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

MonitoringInterval (integer) --
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.

EnhancedMonitoringResourceArn (string) --
The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.

MonitoringRoleArn (string) --
The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --
The Amazon Resource Name (ARN) for the DB instance.

Timezone (string) --
Not supported.

IAMDatabaseAuthenticationEnabled (boolean) --
True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise false.

PerformanceInsightsEnabled (boolean) --

(Not supported by Neptune)


PerformanceInsightsKMSKeyId (string) --

(Not supported by Neptune)


EnabledCloudwatchLogsExports (list) --
A list of log types that this DB instance is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB instance has deletion protection enabled. The instance can\'t be deleted when deletion protection is enabled. See Deleting a DB Instance .









Exceptions

Neptune.Client.exceptions.InvalidDBInstanceStateFault
Neptune.Client.exceptions.InvalidDBSecurityGroupStateFault
Neptune.Client.exceptions.DBInstanceAlreadyExistsFault
Neptune.Client.exceptions.DBInstanceNotFoundFault
Neptune.Client.exceptions.DBSecurityGroupNotFoundFault
Neptune.Client.exceptions.DBParameterGroupNotFoundFault
Neptune.Client.exceptions.InsufficientDBInstanceCapacityFault
Neptune.Client.exceptions.StorageQuotaExceededFault
Neptune.Client.exceptions.InvalidVPCNetworkStateFault
Neptune.Client.exceptions.ProvisionedIopsNotAvailableInAZFault
Neptune.Client.exceptions.OptionGroupNotFoundFault
Neptune.Client.exceptions.DBUpgradeDependencyFailureFault
Neptune.Client.exceptions.StorageTypeNotSupportedFault
Neptune.Client.exceptions.AuthorizationNotFoundFault
Neptune.Client.exceptions.CertificateNotFoundFault
Neptune.Client.exceptions.DomainNotFoundFault


    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'DBSecurityGroups': [
                {
                    'DBSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'DBParameterGroups': [
                {
                    'DBParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string'
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
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'ReadReplicaSourceDBInstanceIdentifier': 'string',
            'ReadReplicaDBInstanceIdentifiers': [
                'string',
            ],
            'ReadReplicaDBClusterIdentifiers': [
                'string',
            ],
            'LicenseModel': 'string',
            'Iops': 123,
            'OptionGroupMemberships': [
                {
                    'OptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CharacterSetName': 'string',
            'SecondaryAvailabilityZone': 'string',
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'StorageType': 'string',
            'TdeCredentialArn': 'string',
            'DbInstancePort': 123,
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'DomainMemberships': [
                {
                    'Domain': 'string',
                    'Status': 'string',
                    'FQDN': 'string',
                    'IAMRoleName': 'string'
                },
            ],
            'CopyTagsToSnapshot': True|False,
            'MonitoringInterval': 123,
            'EnhancedMonitoringResourceArn': 'string',
            'MonitoringRoleArn': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'Timezone': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False,
            'PerformanceInsightsEnabled': True|False,
            'PerformanceInsightsKMSKeyId': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    CreateDBInstance
    DeleteDBInstance
    ModifyDBInstance
    RebootDBInstance
    
    """
    pass

def modify_db_parameter_group(DBParameterGroupName=None, Parameters=None):
    """
    Modifies the parameters of a DB parameter group. To modify more than one parameter, submit a list of the following: ParameterName , ParameterValue , and ApplyMethod . A maximum of 20 parameters can be modified in a single request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_db_parameter_group(
        DBParameterGroupName='string',
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
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]\nThe name of the DB parameter group.\nConstraints:\n\nIf supplied, must match the name of an existing DBParameterGroup.\n\n

    :type Parameters: list
    :param Parameters: [REQUIRED]\nAn array of parameter names, values, and the apply method for the parameter update. At least one parameter name, value, and apply method must be supplied; subsequent arguments are optional. A maximum of 20 parameters can be modified in a single request.\nValid Values (for the application method): immediate | pending-reboot\n\nNote\nYou can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when you reboot the DB instance without failover.\n\n\n(dict) --Specifies a parameter.\n\nParameterName (string) --Specifies the name of the parameter.\n\nParameterValue (string) --Specifies the value of the parameter.\n\nDescription (string) --Provides a description of the parameter.\n\nSource (string) --Indicates the source of the parameter value.\n\nApplyType (string) --Specifies the engine specific parameters type.\n\nDataType (string) --Specifies the valid data type for the parameter.\n\nAllowedValues (string) --Specifies the valid range of values for the parameter.\n\nIsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.\n\nMinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.\n\nApplyMethod (string) --Indicates when to apply parameter updates.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBParameterGroupName': 'string'
}


Response Structure

(dict) --

DBParameterGroupName (string) --
Provides the name of the DB parameter group.







Exceptions

Neptune.Client.exceptions.DBParameterGroupNotFoundFault
Neptune.Client.exceptions.InvalidDBParameterGroupStateFault


    :return: {
        'DBParameterGroupName': 'string'
    }
    
    
    :returns: 
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    Neptune.Client.exceptions.InvalidDBParameterGroupStateFault
    
    """
    pass

def modify_db_subnet_group(DBSubnetGroupName=None, DBSubnetGroupDescription=None, SubnetIds=None):
    """
    Modifies an existing DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the AWS Region.
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
    :param DBSubnetGroupName: [REQUIRED]\nThe name for the DB subnet group. This value is stored as a lowercase string. You can\'t modify the default subnet group.\nConstraints: Must match the name of an existing DBSubnetGroup. Must not be default.\nExample: mySubnetgroup\n

    :type DBSubnetGroupDescription: string
    :param DBSubnetGroupDescription: The description for the DB subnet group.

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nThe EC2 subnet IDs for the DB subnet group.\n\n(string) --\n\n

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
Contains the details of an Amazon Neptune DB subnet group.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

DBSubnetGroupName (string) --
The name of the DB subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the DB subnet group.

VpcId (string) --
Provides the VpcId of the DB subnet group.

SubnetGroupStatus (string) --
Provides the status of the DB subnet group.

Subnets (list) --
Contains a list of  Subnet elements.

(dict) --
Specifies a subnet.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the EC2 Availability Zone that the subnet is in.

Name (string) --
The name of the availability zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.









Exceptions

Neptune.Client.exceptions.DBSubnetGroupNotFoundFault
Neptune.Client.exceptions.DBSubnetQuotaExceededFault
Neptune.Client.exceptions.SubnetAlreadyInUse
Neptune.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
Neptune.Client.exceptions.InvalidSubnet


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
    Neptune.Client.exceptions.DBSubnetGroupNotFoundFault
    Neptune.Client.exceptions.DBSubnetQuotaExceededFault
    Neptune.Client.exceptions.SubnetAlreadyInUse
    Neptune.Client.exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
    Neptune.Client.exceptions.InvalidSubnet
    
    """
    pass

def modify_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, EventCategories=None, Enabled=None):
    """
    Modifies an existing event notification subscription. Note that you can\'t modify the source identifiers using this call; to change source identifiers for a subscription, use the  AddSourceIdentifierToSubscription and  RemoveSourceIdentifierFromSubscription calls.
    You can see a list of the event categories for a given SourceType by using the DescribeEventCategories action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_event_subscription(
        SubscriptionName='string',
        SnsTopicArn='string',
        SourceType='string',
        EventCategories=[
            'string',
        ],
        Enabled=True|False
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]\nThe name of the event notification subscription.\n

    :type SnsTopicArn: string
    :param SnsTopicArn: The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.

    :type SourceType: string
    :param SourceType: The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.\nValid values: db-instance | db-parameter-group | db-security-group | db-snapshot\n

    :type EventCategories: list
    :param EventCategories: A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the DescribeEventCategories action.\n\n(string) --\n\n

    :type Enabled: boolean
    :param Enabled: A Boolean value; set to true to activate the subscription.

    :rtype: dict

ReturnsResponse Syntax
{
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

EventSubscription (dict) --
Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

CustomerAwsId (string) --
The AWS customer account associated with the event notification subscription.

CustSubscriptionId (string) --
The event notification subscription Id.

SnsTopicArn (string) --
The topic ARN of the event notification subscription.

Status (string) --
The status of the event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that Neptune no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --
The time the event notification subscription was created.

SourceType (string) --
The source type for the event notification subscription.

SourceIdsList (list) --
A list of source IDs for the event notification subscription.

(string) --


EventCategoriesList (list) --
A list of event categories for the event notification subscription.

(string) --


Enabled (boolean) --
A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.

EventSubscriptionArn (string) --
The Amazon Resource Name (ARN) for the event subscription.









Exceptions

Neptune.Client.exceptions.EventSubscriptionQuotaExceededFault
Neptune.Client.exceptions.SubscriptionNotFoundFault
Neptune.Client.exceptions.SNSInvalidTopicFault
Neptune.Client.exceptions.SNSNoAuthorizationFault
Neptune.Client.exceptions.SNSTopicArnNotFoundFault
Neptune.Client.exceptions.SubscriptionCategoryNotFoundFault


    :return: {
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
    
    
    :returns: 
    (string) --
    
    """
    pass

def promote_read_replica_db_cluster(DBClusterIdentifier=None):
    """
    Not supported.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.promote_read_replica_db_cluster(
        DBClusterIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nNot supported.\n

    :rtype: dict
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
        'MultiAZ': True|False,
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
        ],
        'IAMDatabaseAuthenticationEnabled': True|False,
        'CloneGroupId': 'string',
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --
DBCluster (dict) --Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --
AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.

AvailabilityZones (list) --Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --
(Not supported by Neptune)

DatabaseName (string) --Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --Specifies the current state of this DB cluster.

PercentProgress (string) --Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --Indicates the database engine version.

LatestRestorableTime (datetime) --Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --Specifies the port that the database engine is listening on.

MasterUsername (string) --Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --
(Not supported by Neptune)

(dict) --Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --Specifies the name of the DB cluster option group.

Status (string) --Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --Not supported by Neptune.

ReadReplicaIdentifiers (list) --Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --Provides the list of instances that make up the DB cluster.

(dict) --Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --The name of the VPC security group.

Status (string) --The status of the VPC security group.





HostedZoneId (string) --Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.








Exceptions

Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.InvalidDBClusterStateFault


    :return: {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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

def reboot_db_instance(DBInstanceIdentifier=None, ForceFailover=None):
    """
    You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB parameter group associated with the DB instance, you must reboot the instance for the changes to take effect.
    Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reboot_db_instance(
        DBInstanceIdentifier='string',
        ForceFailover=True|False
    )
    
    
    :type DBInstanceIdentifier: string
    :param DBInstanceIdentifier: [REQUIRED]\nThe DB instance identifier. This parameter is stored as a lowercase string.\nConstraints:\n\nMust match the identifier of an existing DBInstance.\n\n

    :type ForceFailover: boolean
    :param ForceFailover: When true , the reboot is conducted through a MultiAZ failover.\nConstraint: You can\'t specify true if the instance is not configured for MultiAZ.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBInstance': {
        'DBInstanceIdentifier': 'string',
        'DBInstanceClass': 'string',
        'Engine': 'string',
        'DBInstanceStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123,
            'HostedZoneId': 'string'
        },
        'AllocatedStorage': 123,
        'InstanceCreateTime': datetime(2015, 1, 1),
        'PreferredBackupWindow': 'string',
        'BackupRetentionPeriod': 123,
        'DBSecurityGroups': [
            {
                'DBSecurityGroupName': 'string',
                'Status': 'string'
            },
        ],
        'VpcSecurityGroups': [
            {
                'VpcSecurityGroupId': 'string',
                'Status': 'string'
            },
        ],
        'DBParameterGroups': [
            {
                'DBParameterGroupName': 'string',
                'ParameterApplyStatus': 'string'
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
        'MultiAZ': True|False,
        'EngineVersion': 'string',
        'AutoMinorVersionUpgrade': True|False,
        'ReadReplicaSourceDBInstanceIdentifier': 'string',
        'ReadReplicaDBInstanceIdentifiers': [
            'string',
        ],
        'ReadReplicaDBClusterIdentifiers': [
            'string',
        ],
        'LicenseModel': 'string',
        'Iops': 123,
        'OptionGroupMemberships': [
            {
                'OptionGroupName': 'string',
                'Status': 'string'
            },
        ],
        'CharacterSetName': 'string',
        'SecondaryAvailabilityZone': 'string',
        'PubliclyAccessible': True|False,
        'StatusInfos': [
            {
                'StatusType': 'string',
                'Normal': True|False,
                'Status': 'string',
                'Message': 'string'
            },
        ],
        'StorageType': 'string',
        'TdeCredentialArn': 'string',
        'DbInstancePort': 123,
        'DBClusterIdentifier': 'string',
        'StorageEncrypted': True|False,
        'KmsKeyId': 'string',
        'DbiResourceId': 'string',
        'CACertificateIdentifier': 'string',
        'DomainMemberships': [
            {
                'Domain': 'string',
                'Status': 'string',
                'FQDN': 'string',
                'IAMRoleName': 'string'
            },
        ],
        'CopyTagsToSnapshot': True|False,
        'MonitoringInterval': 123,
        'EnhancedMonitoringResourceArn': 'string',
        'MonitoringRoleArn': 'string',
        'PromotionTier': 123,
        'DBInstanceArn': 'string',
        'Timezone': 'string',
        'IAMDatabaseAuthenticationEnabled': True|False,
        'PerformanceInsightsEnabled': True|False,
        'PerformanceInsightsKMSKeyId': 'string',
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --

DBInstance (dict) --
Contains the details of an Amazon Neptune DB instance.
This data type is used as a response element in the  DescribeDBInstances action.

DBInstanceIdentifier (string) --
Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the DB instance.

Engine (string) --
Provides the name of the database engine to be used for this DB instance.

DBInstanceStatus (string) --
Specifies the current state of this database.

MasterUsername (string) --
Contains the master username for the DB instance.

DBName (string) --
The database name.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the DB instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



AllocatedStorage (integer) --
Specifies the allocated storage size specified in gibibytes.

InstanceCreateTime (datetime) --
Provides the date and time the DB instance was created.

PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

DBSecurityGroups (list) --
Provides List of DB security group elements containing only DBSecurityGroup.Name and DBSecurityGroup.Status subelements.

(dict) --
Specifies membership in a designated DB security group.

DBSecurityGroupName (string) --
The name of the DB security group.

Status (string) --
The status of the DB security group.





VpcSecurityGroups (list) --
Provides a list of VPC security group elements that the DB instance belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





DBParameterGroups (list) --
Provides the list of DB parameter groups applied to this DB instance.

(dict) --
The status of the DB parameter group.
This data type is used as a response element in the following actions:

CreateDBInstance
DeleteDBInstance
ModifyDBInstance
RebootDBInstance


DBParameterGroupName (string) --
The name of the DP parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.





AvailabilityZone (string) --
Specifies the name of the Availability Zone the DB instance is located in.

DBSubnetGroup (dict) --
Specifies information on the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.

DBSubnetGroupName (string) --
The name of the DB subnet group.

DBSubnetGroupDescription (string) --
Provides the description of the DB subnet group.

VpcId (string) --
Provides the VpcId of the DB subnet group.

SubnetGroupStatus (string) --
Provides the status of the DB subnet group.

Subnets (list) --
Contains a list of  Subnet elements.

(dict) --
Specifies a subnet.
This data type is used as a response element in the  DescribeDBSubnetGroups action.

SubnetIdentifier (string) --
Specifies the identifier of the subnet.

SubnetAvailabilityZone (dict) --
Specifies the EC2 Availability Zone that the subnet is in.

Name (string) --
The name of the availability zone.



SubnetStatus (string) --
Specifies the status of the subnet.





DBSubnetGroupArn (string) --
The Amazon Resource Name (ARN) for the DB subnet group.



PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

PendingModifiedValues (dict) --
Specifies that changes to the DB instance are pending. This element is only included when changes are pending. Specific changes are identified by subelements.

DBInstanceClass (string) --
Contains the new DBInstanceClass for the DB instance that will be applied or is currently being applied.

AllocatedStorage (integer) --
Contains the new AllocatedStorage size for the DB instance that will be applied or is currently being applied.

MasterUserPassword (string) --
Contains the pending or currently-in-progress change of the master credentials for the DB instance.

Port (integer) --
Specifies the pending port for the DB instance.

BackupRetentionPeriod (integer) --
Specifies the pending number of days for which automated backups are retained.

MultiAZ (boolean) --
Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

LicenseModel (string) --
The license model for the DB instance.
Valid values: license-included | bring-your-own-license | general-public-license

Iops (integer) --
Specifies the new Provisioned IOPS value for the DB instance that will be applied or is currently being applied.

DBInstanceIdentifier (string) --
Contains the new DBInstanceIdentifier for the DB instance that will be applied or is currently being applied.

StorageType (string) --
Specifies the storage type to be associated with the DB instance.

CACertificateIdentifier (string) --
Specifies the identifier of the CA certificate for the DB instance.

DBSubnetGroupName (string) --
The new DB subnet group for the DB instance.

PendingCloudwatchLogsExports (dict) --
This PendingCloudwatchLogsExports structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.

LogTypesToEnable (list) --
Log types that are in the process of being deactivated. After they are deactivated, these log types aren\'t exported to CloudWatch Logs.

(string) --


LogTypesToDisable (list) --
Log types that are in the process of being enabled. After they are enabled, these log types are exported to CloudWatch Logs.

(string) --






LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

MultiAZ (boolean) --
Specifies if the DB instance is a Multi-AZ deployment.

EngineVersion (string) --
Indicates the database engine version.

AutoMinorVersionUpgrade (boolean) --
Indicates that minor version patches are applied automatically.

ReadReplicaSourceDBInstanceIdentifier (string) --
Contains the identifier of the source DB instance if this DB instance is a Read Replica.

ReadReplicaDBInstanceIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB instance.

(string) --


ReadReplicaDBClusterIdentifiers (list) --
Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

(string) --


LicenseModel (string) --
License model information for this DB instance.

Iops (integer) --
Specifies the Provisioned IOPS (I/O operations per second) value.

OptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Provides information on the option groups the DB instance is a member of.

OptionGroupName (string) --
The name of the option group that the instance belongs to.

Status (string) --
The status of the DB instance\'s option group membership. Valid values are: in-sync , pending-apply , pending-removal , pending-maintenance-apply , pending-maintenance-removal , applying , removing , and failed .





CharacterSetName (string) --

(Not supported by Neptune)


SecondaryAvailabilityZone (string) --
If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.

PubliclyAccessible (boolean) --
This flag should no longer be used.

StatusInfos (list) --
The status of a Read Replica. If the instance is not a Read Replica, this is blank.

(dict) --
Provides a list of status information for a DB instance.

StatusType (string) --
This value is currently "read replication."

Normal (boolean) --
Boolean value that is true if the instance is operating normally, or false if the instance is in an error state.

Status (string) --
Status of the DB instance. For a StatusType of read replica, the values can be replicating, error, stopped, or terminated.

Message (string) --
Details of the error if there is an error for the instance. If the instance is not in an error state, this value is blank.





StorageType (string) --
Specifies the storage type associated with DB instance.

TdeCredentialArn (string) --
The ARN from the key store with which the instance is associated for TDE encryption.

DbInstancePort (integer) --
Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.

DBClusterIdentifier (string) --
If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

StorageEncrypted (boolean) --
Not supported: The encryption for DB instances is managed by the DB cluster.

KmsKeyId (string) --
Not supported: The encryption for DB instances is managed by the DB cluster.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

DomainMemberships (list) --
Not supported

(dict) --
An Active Directory Domain membership record associated with a DB instance.

Domain (string) --
The identifier of the Active Directory Domain.

Status (string) --
The status of the DB instance\'s Active Directory Domain membership, such as joined, pending-join, failed etc).

FQDN (string) --
The fully qualified domain name of the Active Directory Domain.

IAMRoleName (string) --
The name of the IAM role to be used when making API calls to the Directory Service.





CopyTagsToSnapshot (boolean) --
Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

MonitoringInterval (integer) --
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.

EnhancedMonitoringResourceArn (string) --
The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.

MonitoringRoleArn (string) --
The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.

DBInstanceArn (string) --
The Amazon Resource Name (ARN) for the DB instance.

Timezone (string) --
Not supported.

IAMDatabaseAuthenticationEnabled (boolean) --
True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise false.

PerformanceInsightsEnabled (boolean) --

(Not supported by Neptune)


PerformanceInsightsKMSKeyId (string) --

(Not supported by Neptune)


EnabledCloudwatchLogsExports (list) --
A list of log types that this DB instance is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB instance has deletion protection enabled. The instance can\'t be deleted when deletion protection is enabled. See Deleting a DB Instance .









Exceptions

Neptune.Client.exceptions.InvalidDBInstanceStateFault
Neptune.Client.exceptions.DBInstanceNotFoundFault


    :return: {
        'DBInstance': {
            'DBInstanceIdentifier': 'string',
            'DBInstanceClass': 'string',
            'Engine': 'string',
            'DBInstanceStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123,
                'HostedZoneId': 'string'
            },
            'AllocatedStorage': 123,
            'InstanceCreateTime': datetime(2015, 1, 1),
            'PreferredBackupWindow': 'string',
            'BackupRetentionPeriod': 123,
            'DBSecurityGroups': [
                {
                    'DBSecurityGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'VpcSecurityGroups': [
                {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                },
            ],
            'DBParameterGroups': [
                {
                    'DBParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string'
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
            'MultiAZ': True|False,
            'EngineVersion': 'string',
            'AutoMinorVersionUpgrade': True|False,
            'ReadReplicaSourceDBInstanceIdentifier': 'string',
            'ReadReplicaDBInstanceIdentifiers': [
                'string',
            ],
            'ReadReplicaDBClusterIdentifiers': [
                'string',
            ],
            'LicenseModel': 'string',
            'Iops': 123,
            'OptionGroupMemberships': [
                {
                    'OptionGroupName': 'string',
                    'Status': 'string'
                },
            ],
            'CharacterSetName': 'string',
            'SecondaryAvailabilityZone': 'string',
            'PubliclyAccessible': True|False,
            'StatusInfos': [
                {
                    'StatusType': 'string',
                    'Normal': True|False,
                    'Status': 'string',
                    'Message': 'string'
                },
            ],
            'StorageType': 'string',
            'TdeCredentialArn': 'string',
            'DbInstancePort': 123,
            'DBClusterIdentifier': 'string',
            'StorageEncrypted': True|False,
            'KmsKeyId': 'string',
            'DbiResourceId': 'string',
            'CACertificateIdentifier': 'string',
            'DomainMemberships': [
                {
                    'Domain': 'string',
                    'Status': 'string',
                    'FQDN': 'string',
                    'IAMRoleName': 'string'
                },
            ],
            'CopyTagsToSnapshot': True|False,
            'MonitoringInterval': 123,
            'EnhancedMonitoringResourceArn': 'string',
            'MonitoringRoleArn': 'string',
            'PromotionTier': 123,
            'DBInstanceArn': 'string',
            'Timezone': 'string',
            'IAMDatabaseAuthenticationEnabled': True|False,
            'PerformanceInsightsEnabled': True|False,
            'PerformanceInsightsKMSKeyId': 'string',
            'EnabledCloudwatchLogsExports': [
                'string',
            ],
            'DeletionProtection': True|False
        }
    }
    
    
    :returns: 
    CreateDBInstance
    DeleteDBInstance
    ModifyDBInstance
    RebootDBInstance
    
    """
    pass

def remove_role_from_db_cluster(DBClusterIdentifier=None, RoleArn=None):
    """
    Disassociates an Identity and Access Management (IAM) role from a DB cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_role_from_db_cluster(
        DBClusterIdentifier='string',
        RoleArn='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe name of the DB cluster to disassociate the IAM role from.\n

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM role to disassociate from the DB cluster, for example arn:aws:iam::123456789012:role/NeptuneAccessRole .\n

    :returns: 
    Neptune.Client.exceptions.DBClusterNotFoundFault
    Neptune.Client.exceptions.DBClusterRoleNotFoundFault
    Neptune.Client.exceptions.InvalidDBClusterStateFault
    
    """
    pass

def remove_source_identifier_from_subscription(SubscriptionName=None, SourceIdentifier=None):
    """
    Removes a source identifier from an existing event notification subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_source_identifier_from_subscription(
        SubscriptionName='string',
        SourceIdentifier='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]\nThe name of the event notification subscription you want to remove a source identifier from.\n

    :type SourceIdentifier: string
    :param SourceIdentifier: [REQUIRED]\nThe source identifier to be removed from the subscription, such as the DB instance identifier for a DB instance or the name of a security group.\n

    :rtype: dict

ReturnsResponse Syntax
{
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

EventSubscription (dict) --
Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

CustomerAwsId (string) --
The AWS customer account associated with the event notification subscription.

CustSubscriptionId (string) --
The event notification subscription Id.

SnsTopicArn (string) --
The topic ARN of the event notification subscription.

Status (string) --
The status of the event notification subscription.
Constraints:
Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist
The status "no-permission" indicates that Neptune no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

SubscriptionCreationTime (string) --
The time the event notification subscription was created.

SourceType (string) --
The source type for the event notification subscription.

SourceIdsList (list) --
A list of source IDs for the event notification subscription.

(string) --


EventCategoriesList (list) --
A list of event categories for the event notification subscription.

(string) --


Enabled (boolean) --
A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.

EventSubscriptionArn (string) --
The Amazon Resource Name (ARN) for the event subscription.









Exceptions

Neptune.Client.exceptions.SubscriptionNotFoundFault
Neptune.Client.exceptions.SourceNotFoundFault


    :return: {
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
    
    
    :returns: 
    (string) --
    
    """
    pass

def remove_tags_from_resource(ResourceName=None, TagKeys=None):
    """
    Removes metadata tags from an Amazon Neptune resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_tags_from_resource(
        ResourceName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe Amazon Neptune resource that the tags are removed from. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag key (name) of the tag to be removed.\n\n(string) --\n\n

    :returns: 
    Neptune.Client.exceptions.DBInstanceNotFoundFault
    Neptune.Client.exceptions.DBSnapshotNotFoundFault
    Neptune.Client.exceptions.DBClusterNotFoundFault
    
    """
    pass

def reset_db_cluster_parameter_group(DBClusterParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    Modifies the parameters of a DB cluster parameter group to the default value. To reset specific parameters submit a list of the following: ParameterName and ApplyMethod . To reset the entire DB cluster parameter group, specify the DBClusterParameterGroupName and ResetAllParameters parameters.
    When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to pending-reboot to take effect on the next DB instance restart or  RebootDBInstance request. You must call  RebootDBInstance for every DB instance in your DB cluster that you want the updated static parameter to apply to.
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
    :param DBClusterParameterGroupName: [REQUIRED]\nThe name of the DB cluster parameter group to reset.\n

    :type ResetAllParameters: boolean
    :param ResetAllParameters: A value that is set to true to reset all parameters in the DB cluster parameter group to their default values, and false otherwise. You can\'t use this parameter if there is a list of parameter names specified for the Parameters parameter.

    :type Parameters: list
    :param Parameters: A list of parameter names in the DB cluster parameter group to reset to the default values. You can\'t use this parameter if the ResetAllParameters parameter is set to true .\n\n(dict) --Specifies a parameter.\n\nParameterName (string) --Specifies the name of the parameter.\n\nParameterValue (string) --Specifies the value of the parameter.\n\nDescription (string) --Provides a description of the parameter.\n\nSource (string) --Indicates the source of the parameter value.\n\nApplyType (string) --Specifies the engine specific parameters type.\n\nDataType (string) --Specifies the valid data type for the parameter.\n\nAllowedValues (string) --Specifies the valid range of values for the parameter.\n\nIsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.\n\nMinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.\n\nApplyMethod (string) --Indicates when to apply parameter updates.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBClusterParameterGroupName': 'string'
}


Response Structure

(dict) --

DBClusterParameterGroupName (string) --
The name of the DB cluster parameter group.
Constraints:

Must be 1 to 255 letters or numbers.
First character must be a letter
Cannot end with a hyphen or contain two consecutive hyphens


Note
This value is stored as a lowercase string.








Exceptions

Neptune.Client.exceptions.InvalidDBParameterGroupStateFault
Neptune.Client.exceptions.DBParameterGroupNotFoundFault


    :return: {
        'DBClusterParameterGroupName': 'string'
    }
    
    
    :returns: 
    Must be 1 to 255 letters or numbers.
    First character must be a letter
    Cannot end with a hyphen or contain two consecutive hyphens
    
    """
    pass

def reset_db_parameter_group(DBParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    Modifies the parameters of a DB parameter group to the engine/system default value. To reset specific parameters, provide a list of the following: ParameterName and ApplyMethod . To reset the entire DB parameter group, specify the DBParameterGroup name and ResetAllParameters parameters. When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to pending-reboot to take effect on the next DB instance restart or RebootDBInstance request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reset_db_parameter_group(
        DBParameterGroupName='string',
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
    
    
    :type DBParameterGroupName: string
    :param DBParameterGroupName: [REQUIRED]\nThe name of the DB parameter group.\nConstraints:\n\nMust match the name of an existing DBParameterGroup.\n\n

    :type ResetAllParameters: boolean
    :param ResetAllParameters: Specifies whether (true ) or not (false ) to reset all parameters in the DB parameter group to default values.\nDefault: true\n

    :type Parameters: list
    :param Parameters: To reset the entire DB parameter group, specify the DBParameterGroup name and ResetAllParameters parameters. To reset specific parameters, provide a list of the following: ParameterName and ApplyMethod . A maximum of 20 parameters can be modified in a single request.\nValid Values (for Apply method): pending-reboot\n\n(dict) --Specifies a parameter.\n\nParameterName (string) --Specifies the name of the parameter.\n\nParameterValue (string) --Specifies the value of the parameter.\n\nDescription (string) --Provides a description of the parameter.\n\nSource (string) --Indicates the source of the parameter value.\n\nApplyType (string) --Specifies the engine specific parameters type.\n\nDataType (string) --Specifies the valid data type for the parameter.\n\nAllowedValues (string) --Specifies the valid range of values for the parameter.\n\nIsModifiable (boolean) --Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.\n\nMinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.\n\nApplyMethod (string) --Indicates when to apply parameter updates.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DBParameterGroupName': 'string'
}


Response Structure

(dict) --

DBParameterGroupName (string) --
Provides the name of the DB parameter group.







Exceptions

Neptune.Client.exceptions.InvalidDBParameterGroupStateFault
Neptune.Client.exceptions.DBParameterGroupNotFoundFault


    :return: {
        'DBParameterGroupName': 'string'
    }
    
    
    :returns: 
    Neptune.Client.exceptions.InvalidDBParameterGroupStateFault
    Neptune.Client.exceptions.DBParameterGroupNotFoundFault
    
    """
    pass

def restore_db_cluster_from_snapshot(AvailabilityZones=None, DBClusterIdentifier=None, SnapshotIdentifier=None, Engine=None, EngineVersion=None, Port=None, DBSubnetGroupName=None, DatabaseName=None, OptionGroupName=None, VpcSecurityGroupIds=None, Tags=None, KmsKeyId=None, EnableIAMDatabaseAuthentication=None, EnableCloudwatchLogsExports=None, DBClusterParameterGroupName=None, DeletionProtection=None):
    """
    Creates a new DB cluster from a DB snapshot or DB cluster snapshot.
    If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.
    If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.
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
        DatabaseName='string',
        OptionGroupName='string',
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
        EnableIAMDatabaseAuthentication=True|False,
        EnableCloudwatchLogsExports=[
            'string',
        ],
        DBClusterParameterGroupName='string',
        DeletionProtection=True|False
    )
    
    
    :type AvailabilityZones: list
    :param AvailabilityZones: Provides the list of EC2 Availability Zones that instances in the restored DB cluster can be created in.\n\n(string) --\n\n

    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe name of the DB cluster to create from the DB snapshot or DB cluster snapshot. This parameter isn\'t case-sensitive.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\nExample: my-snapshot-id\n

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]\nThe identifier for the DB snapshot or DB cluster snapshot to restore from.\nYou can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.\nConstraints:\n\nMust match the identifier of an existing Snapshot.\n\n

    :type Engine: string
    :param Engine: [REQUIRED]\nThe database engine to use for the new DB cluster.\nDefault: The same as source\nConstraint: Must be compatible with the engine of the source\n

    :type EngineVersion: string
    :param EngineVersion: The version of the database engine to use for the new DB cluster.

    :type Port: integer
    :param Port: The port number on which the new DB cluster accepts connections.\nConstraints: Value must be 1150-65535\nDefault: The same port as the original DB cluster.\n

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The name of the DB subnet group to use for the new DB cluster.\nConstraints: If supplied, must match the name of an existing DBSubnetGroup.\nExample: mySubnetgroup\n

    :type DatabaseName: string
    :param DatabaseName: Not supported.

    :type OptionGroupName: string
    :param OptionGroupName: (Not supported by Neptune)

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of VPC security groups that the new DB cluster will belong to.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: The tags to be assigned to the restored DB cluster.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier to use when restoring an encrypted DB cluster from a DB snapshot or DB cluster snapshot.\nThe KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.\nIf you do not specify a value for the KmsKeyId parameter, then the following will occur:\n\nIf the DB snapshot or DB cluster snapshot in SnapshotIdentifier is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB snapshot or DB cluster snapshot.\nIf the DB snapshot or DB cluster snapshot in SnapshotIdentifier is not encrypted, then the restored DB cluster is not encrypted.\n\n

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.\nDefault: false\n

    :type EnableCloudwatchLogsExports: list
    :param EnableCloudwatchLogsExports: The list of logs that the restored DB cluster is to export to Amazon CloudWatch Logs.\n\n(string) --\n\n

    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of the DB cluster parameter group to associate with the new DB cluster.\nConstraints:\n\nIf supplied, must match the name of an existing DBClusterParameterGroup.\n\n

    :type DeletionProtection: boolean
    :param DeletionProtection: A value that indicates whether the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled. By default, deletion protection is disabled.

    :rtype: dict

ReturnsResponse Syntax
{
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
        'MultiAZ': True|False,
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
        ],
        'IAMDatabaseAuthenticationEnabled': True|False,
        'CloneGroupId': 'string',
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
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --

AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.


AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --

(Not supported by Neptune)


DatabaseName (string) --
Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --
Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this DB cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --
The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --
Specifies the name of the DB cluster option group.

Status (string) --
Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --
Not supported by Neptune.

ReadReplicaIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --
Provides the list of instances that make up the DB cluster.

(dict) --
Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --
Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --
Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.









Exceptions

Neptune.Client.exceptions.DBClusterAlreadyExistsFault
Neptune.Client.exceptions.DBClusterQuotaExceededFault
Neptune.Client.exceptions.StorageQuotaExceededFault
Neptune.Client.exceptions.DBSubnetGroupNotFoundFault
Neptune.Client.exceptions.DBSnapshotNotFoundFault
Neptune.Client.exceptions.DBClusterSnapshotNotFoundFault
Neptune.Client.exceptions.InsufficientDBClusterCapacityFault
Neptune.Client.exceptions.InsufficientStorageClusterCapacityFault
Neptune.Client.exceptions.InvalidDBSnapshotStateFault
Neptune.Client.exceptions.InvalidDBClusterSnapshotStateFault
Neptune.Client.exceptions.StorageQuotaExceededFault
Neptune.Client.exceptions.InvalidVPCNetworkStateFault
Neptune.Client.exceptions.InvalidRestoreFault
Neptune.Client.exceptions.DBSubnetGroupNotFoundFault
Neptune.Client.exceptions.InvalidSubnet
Neptune.Client.exceptions.OptionGroupNotFoundFault
Neptune.Client.exceptions.KMSKeyNotAccessibleFault
Neptune.Client.exceptions.DBClusterParameterGroupNotFoundFault


    :return: {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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

def restore_db_cluster_to_point_in_time(DBClusterIdentifier=None, RestoreType=None, SourceDBClusterIdentifier=None, RestoreToTime=None, UseLatestRestorableTime=None, Port=None, DBSubnetGroupName=None, OptionGroupName=None, VpcSecurityGroupIds=None, Tags=None, KmsKeyId=None, EnableIAMDatabaseAuthentication=None, EnableCloudwatchLogsExports=None, DBClusterParameterGroupName=None, DeletionProtection=None):
    """
    Restores a DB cluster to an arbitrary point in time. Users can restore to any point in time before LatestRestorableTime for up to BackupRetentionPeriod days. The target DB cluster is created from the source DB cluster with the same configuration as the original DB cluster, except that the new DB cluster is created with the default DB security group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_db_cluster_to_point_in_time(
        DBClusterIdentifier='string',
        RestoreType='string',
        SourceDBClusterIdentifier='string',
        RestoreToTime=datetime(2015, 1, 1),
        UseLatestRestorableTime=True|False,
        Port=123,
        DBSubnetGroupName='string',
        OptionGroupName='string',
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
        EnableIAMDatabaseAuthentication=True|False,
        EnableCloudwatchLogsExports=[
            'string',
        ],
        DBClusterParameterGroupName='string',
        DeletionProtection=True|False
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe name of the new DB cluster to be created.\nConstraints:\n\nMust contain from 1 to 63 letters, numbers, or hyphens\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\n

    :type RestoreType: string
    :param RestoreType: The type of restore to be performed. You can specify one of the following values:\n\nfull-copy - The new DB cluster is restored as a full copy of the source DB cluster.\ncopy-on-write - The new DB cluster is restored as a clone of the source DB cluster.\n\nIf you don\'t specify a RestoreType value, then the new DB cluster is restored as a full copy of the source DB cluster.\n

    :type SourceDBClusterIdentifier: string
    :param SourceDBClusterIdentifier: [REQUIRED]\nThe identifier of the source DB cluster from which to restore.\nConstraints:\n\nMust match the identifier of an existing DBCluster.\n\n

    :type RestoreToTime: datetime
    :param RestoreToTime: The date and time to restore the DB cluster to.\nValid Values: Value must be a time in Universal Coordinated Time (UTC) format\nConstraints:\n\nMust be before the latest restorable time for the DB instance\nMust be specified if UseLatestRestorableTime parameter is not provided\nCannot be specified if UseLatestRestorableTime parameter is true\nCannot be specified if RestoreType parameter is copy-on-write\n\nExample: 2015-03-07T23:45:00Z\n

    :type UseLatestRestorableTime: boolean
    :param UseLatestRestorableTime: A value that is set to true to restore the DB cluster to the latest restorable backup time, and false otherwise.\nDefault: false\nConstraints: Cannot be specified if RestoreToTime parameter is provided.\n

    :type Port: integer
    :param Port: The port number on which the new DB cluster accepts connections.\nConstraints: Value must be 1150-65535\nDefault: The same port as the original DB cluster.\n

    :type DBSubnetGroupName: string
    :param DBSubnetGroupName: The DB subnet group name to use for the new DB cluster.\nConstraints: If supplied, must match the name of an existing DBSubnetGroup.\nExample: mySubnetgroup\n

    :type OptionGroupName: string
    :param OptionGroupName: (Not supported by Neptune)

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of VPC security groups that the new DB cluster belongs to.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: The tags to be applied to the restored DB cluster.\n\n(dict) --Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.\n\nKey (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can\'t be prefixed with 'aws:' or 'rds:'. The string can only contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS KMS key identifier to use when restoring an encrypted DB cluster from an encrypted DB cluster.\nThe KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same AWS account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.\nYou can restore to a new DB cluster and encrypt the new DB cluster with a KMS key that is different than the KMS key used to encrypt the source DB cluster. The new DB cluster is encrypted with the KMS key identified by the KmsKeyId parameter.\nIf you do not specify a value for the KmsKeyId parameter, then the following will occur:\n\nIf the DB cluster is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the source DB cluster.\nIf the DB cluster is not encrypted, then the restored DB cluster is not encrypted.\n\nIf DBClusterIdentifier refers to a DB cluster that is not encrypted, then the restore request is rejected.\n

    :type EnableIAMDatabaseAuthentication: boolean
    :param EnableIAMDatabaseAuthentication: True to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts, and otherwise false.\nDefault: false\n

    :type EnableCloudwatchLogsExports: list
    :param EnableCloudwatchLogsExports: The list of logs that the restored DB cluster is to export to CloudWatch Logs.\n\n(string) --\n\n

    :type DBClusterParameterGroupName: string
    :param DBClusterParameterGroupName: The name of the DB cluster parameter group to associate with the new DB cluster.\nConstraints:\n\nIf supplied, must match the name of an existing DBClusterParameterGroup.\n\n

    :type DeletionProtection: boolean
    :param DeletionProtection: A value that indicates whether the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled. By default, deletion protection is disabled.

    :rtype: dict

ReturnsResponse Syntax
{
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
        'MultiAZ': True|False,
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
        ],
        'IAMDatabaseAuthenticationEnabled': True|False,
        'CloneGroupId': 'string',
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
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --

AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.


AvailabilityZones (list) --
Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --
Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --

(Not supported by Neptune)


DatabaseName (string) --
Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --
Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --
Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --
Specifies the current state of this DB cluster.

PercentProgress (string) --
Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --
Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --
Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --
The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --
Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --
Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --
Indicates the database engine version.

LatestRestorableTime (datetime) --
Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --
Specifies the port that the database engine is listening on.

MasterUsername (string) --
Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --

(Not supported by Neptune)


(dict) --
Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --
Specifies the name of the DB cluster option group.

Status (string) --
Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --
Not supported by Neptune.

ReadReplicaIdentifiers (list) --
Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --
Provides the list of instances that make up the DB cluster.

(dict) --
Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --
Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --
Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --
Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --
Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --
This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.





HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --
Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --
The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --
The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --
Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --
Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --
Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --
Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --
A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --
Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.









Exceptions

Neptune.Client.exceptions.DBClusterAlreadyExistsFault
Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.DBClusterQuotaExceededFault
Neptune.Client.exceptions.DBClusterSnapshotNotFoundFault
Neptune.Client.exceptions.DBSubnetGroupNotFoundFault
Neptune.Client.exceptions.InsufficientDBClusterCapacityFault
Neptune.Client.exceptions.InsufficientStorageClusterCapacityFault
Neptune.Client.exceptions.InvalidDBClusterSnapshotStateFault
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.InvalidDBSnapshotStateFault
Neptune.Client.exceptions.InvalidRestoreFault
Neptune.Client.exceptions.InvalidSubnet
Neptune.Client.exceptions.InvalidVPCNetworkStateFault
Neptune.Client.exceptions.KMSKeyNotAccessibleFault
Neptune.Client.exceptions.OptionGroupNotFoundFault
Neptune.Client.exceptions.StorageQuotaExceededFault
Neptune.Client.exceptions.DBClusterParameterGroupNotFoundFault


    :return: {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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
    Starts an Amazon Neptune DB cluster that was stopped using the AWS console, the AWS CLI stop-db-cluster command, or the StopDBCluster API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_db_cluster(
        DBClusterIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe DB cluster identifier of the Neptune DB cluster to be started. This parameter is stored as a lowercase string.\n

    :rtype: dict
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
        'MultiAZ': True|False,
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
        ],
        'IAMDatabaseAuthenticationEnabled': True|False,
        'CloneGroupId': 'string',
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --
DBCluster (dict) --Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --
AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.

AvailabilityZones (list) --Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --
(Not supported by Neptune)

DatabaseName (string) --Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --Specifies the current state of this DB cluster.

PercentProgress (string) --Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --Indicates the database engine version.

LatestRestorableTime (datetime) --Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --Specifies the port that the database engine is listening on.

MasterUsername (string) --Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --
(Not supported by Neptune)

(dict) --Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --Specifies the name of the DB cluster option group.

Status (string) --Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --Not supported by Neptune.

ReadReplicaIdentifiers (list) --Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --Provides the list of instances that make up the DB cluster.

(dict) --Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --The name of the VPC security group.

Status (string) --The status of the VPC security group.





HostedZoneId (string) --Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.








Exceptions

Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.InvalidDBInstanceStateFault


    :return: {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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

def stop_db_cluster(DBClusterIdentifier=None):
    """
    Stops an Amazon Neptune DB cluster. When you stop a DB cluster, Neptune retains the DB cluster\'s metadata, including its endpoints and DB parameter groups.
    Neptune also retains the transaction logs so you can do a point-in-time restore if necessary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_db_cluster(
        DBClusterIdentifier='string'
    )
    
    
    :type DBClusterIdentifier: string
    :param DBClusterIdentifier: [REQUIRED]\nThe DB cluster identifier of the Neptune DB cluster to be stopped. This parameter is stored as a lowercase string.\n

    :rtype: dict
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
        'MultiAZ': True|False,
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
        ],
        'IAMDatabaseAuthenticationEnabled': True|False,
        'CloneGroupId': 'string',
        'ClusterCreateTime': datetime(2015, 1, 1),
        'EnabledCloudwatchLogsExports': [
            'string',
        ],
        'DeletionProtection': True|False
    }
}


Response Structure

(dict) --
DBCluster (dict) --Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the  DescribeDBClusters action.

AllocatedStorage (integer) --
AllocatedStorage always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.

AvailabilityZones (list) --Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.

(string) --


BackupRetentionPeriod (integer) --Specifies the number of days for which automatic DB snapshots are retained.

CharacterSetName (string) --
(Not supported by Neptune)

DatabaseName (string) --Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.

DBClusterIdentifier (string) --Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.

DBClusterParameterGroup (string) --Specifies the name of the DB cluster parameter group for the DB cluster.

DBSubnetGroup (string) --Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.

Status (string) --Specifies the current state of this DB cluster.

PercentProgress (string) --Specifies the progress of the operation as a percentage.

EarliestRestorableTime (datetime) --Specifies the earliest time to which a database can be restored with point-in-time restore.

Endpoint (string) --Specifies the connection endpoint for the primary instance of the DB cluster.

ReaderEndpoint (string) --The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

MultiAZ (boolean) --Specifies whether the DB cluster has instances in multiple Availability Zones.

Engine (string) --Provides the name of the database engine to be used for this DB cluster.

EngineVersion (string) --Indicates the database engine version.

LatestRestorableTime (datetime) --Specifies the latest time to which a database can be restored with point-in-time restore.

Port (integer) --Specifies the port that the database engine is listening on.

MasterUsername (string) --Contains the master username for the DB cluster.

DBClusterOptionGroupMemberships (list) --
(Not supported by Neptune)

(dict) --Contains status information for a DB cluster option group.

DBClusterOptionGroupName (string) --Specifies the name of the DB cluster option group.

Status (string) --Specifies the status of the DB cluster option group.





PreferredBackupWindow (string) --Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod .

PreferredMaintenanceWindow (string) --Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

ReplicationSourceIdentifier (string) --Not supported by Neptune.

ReadReplicaIdentifiers (list) --Contains one or more identifiers of the Read Replicas associated with this DB cluster.

(string) --


DBClusterMembers (list) --Provides the list of instances that make up the DB cluster.

(dict) --Contains information about an instance that is part of a DB cluster.

DBInstanceIdentifier (string) --Specifies the instance identifier for this member of the DB cluster.

IsClusterWriter (boolean) --Value that is true if the cluster member is the primary instance for the DB cluster and false otherwise.

DBClusterParameterGroupStatus (string) --Specifies the status of the DB cluster parameter group for this member of the DB cluster.

PromotionTier (integer) --A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.





VpcSecurityGroups (list) --Provides a list of VPC security groups that the DB cluster belongs to.

(dict) --This data type is used as a response element for queries on VPC security group membership.

VpcSecurityGroupId (string) --The name of the VPC security group.

Status (string) --The status of the VPC security group.





HostedZoneId (string) --Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

StorageEncrypted (boolean) --Specifies whether the DB cluster is encrypted.

KmsKeyId (string) --If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB cluster.

DbClusterResourceId (string) --The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

DBClusterArn (string) --The Amazon Resource Name (ARN) for the DB cluster.

AssociatedRoles (list) --Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.

(dict) --Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

Status (string) --Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:

ACTIVE - the IAM role ARN is associated with the DB cluster and can be used to access other AWS services on your behalf.
PENDING - the IAM role ARN is being associated with the DB cluster.
INVALID - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other AWS services on your behalf.






IAMDatabaseAuthenticationEnabled (boolean) --True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.

CloneGroupId (string) --Identifies the clone group to which the DB cluster is associated.

ClusterCreateTime (datetime) --Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

EnabledCloudwatchLogsExports (list) --A list of log types that this DB cluster is configured to export to CloudWatch Logs.

(string) --


DeletionProtection (boolean) --Indicates whether or not the DB cluster has deletion protection enabled. The database can\'t be deleted when deletion protection is enabled.








Exceptions

Neptune.Client.exceptions.DBClusterNotFoundFault
Neptune.Client.exceptions.InvalidDBClusterStateFault
Neptune.Client.exceptions.InvalidDBInstanceStateFault


    :return: {
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
            'MultiAZ': True|False,
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
            ],
            'IAMDatabaseAuthenticationEnabled': True|False,
            'CloneGroupId': 'string',
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

