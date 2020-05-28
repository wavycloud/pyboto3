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

def accept_reserved_node_exchange(ReservedNodeId=None, TargetReservedNodeOfferingId=None):
    """
    Exchanges a DC1 Reserved Node for a DC2 Reserved Node with no changes to the configuration (term, payment type, or number of nodes) and no additional costs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_reserved_node_exchange(
        ReservedNodeId='string',
        TargetReservedNodeOfferingId='string'
    )
    
    
    :type ReservedNodeId: string
    :param ReservedNodeId: [REQUIRED]\nA string representing the node identifier of the DC1 Reserved Node to be exchanged.\n

    :type TargetReservedNodeOfferingId: string
    :param TargetReservedNodeOfferingId: [REQUIRED]\nThe unique identifier of the DC2 Reserved Node offering to be used for the exchange. You can obtain the value for the parameter by calling GetReservedNodeExchangeOfferings\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ExchangedReservedNode': {
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
        ],
        'ReservedNodeOfferingType': 'Regular'|'Upgradable'
    }
}


Response Structure

(dict) --

ExchangedReservedNode (dict) --

ReservedNodeId (string) --
The unique identifier for the reservation.

ReservedNodeOfferingId (string) --
The identifier for the reserved node offering.

NodeType (string) --
The node type of the reserved node.

StartTime (datetime) --
The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.

Duration (integer) --
The duration of the node reservation in seconds.

FixedPrice (float) --
The fixed cost Amazon Redshift charges you for this reserved node.

UsagePrice (float) --
The hourly rate Amazon Redshift charges you for this reserved node.

CurrencyCode (string) --
The currency code for the reserved cluster.

NodeCount (integer) --
The number of reserved compute nodes.

State (string) --
The state of the reserved compute node.
Possible Values:

pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
active-This reserved node is owned by the caller and is available for use.
payment-failed-Payment failed for the purchase attempt.
retired-The reserved node is no longer available.
exchanging-The owner is exchanging the reserved node for another reserved node.


OfferingType (string) --
The anticipated utilization of the reserved node, as defined in the reserved node offering.

RecurringCharges (list) --
The recurring charges for the reserved node.

(dict) --
Describes a recurring charge.

RecurringChargeAmount (float) --
The amount charged per the period of time specified by the recurring charge frequency.

RecurringChargeFrequency (string) --
The frequency at which the recurring charge amount is applied.





ReservedNodeOfferingType (string) --









Exceptions

Redshift.Client.exceptions.ReservedNodeNotFoundFault
Redshift.Client.exceptions.InvalidReservedNodeStateFault
Redshift.Client.exceptions.ReservedNodeAlreadyMigratedFault
Redshift.Client.exceptions.ReservedNodeOfferingNotFoundFault
Redshift.Client.exceptions.UnsupportedOperationFault
Redshift.Client.exceptions.DependentServiceUnavailableFault
Redshift.Client.exceptions.ReservedNodeAlreadyExistsFault


    :return: {
        'ExchangedReservedNode': {
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
            ],
            'ReservedNodeOfferingType': 'Regular'|'Upgradable'
        }
    }
    
    
    :returns: 
    pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
    active-This reserved node is owned by the caller and is available for use.
    payment-failed-Payment failed for the purchase attempt.
    retired-The reserved node is no longer available.
    exchanging-The owner is exchanging the reserved node for another reserved node.
    
    """
    pass

def authorize_cluster_security_group_ingress(ClusterSecurityGroupName=None, CIDRIP=None, EC2SecurityGroupName=None, EC2SecurityGroupOwnerId=None):
    """
    Adds an inbound (ingress) rule to an Amazon Redshift security group. Depending on whether the application accessing your cluster is running on the Internet or an Amazon EC2 instance, you can authorize inbound access to either a Classless Interdomain Routing (CIDR)/Internet Protocol (IP) range or to an Amazon EC2 security group. You can add as many as 20 ingress rules to an Amazon Redshift security group.
    If you authorize access to an Amazon EC2 security group, specify EC2SecurityGroupName and EC2SecurityGroupOwnerId . The Amazon EC2 security group and Amazon Redshift cluster must be in the same AWS Region.
    If you authorize access to a CIDR/IP address range, specify CIDRIP . For an overview of CIDR blocks, see the Wikipedia article on Classless Inter-Domain Routing .
    You must also associate the security group with a cluster so that clients running on these IP addresses or the EC2 instance are authorized to connect to the cluster. For information about managing security groups, go to Working with Security Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.authorize_cluster_security_group_ingress(
        ClusterSecurityGroupName='string',
        CIDRIP='string',
        EC2SecurityGroupName='string',
        EC2SecurityGroupOwnerId='string'
    )
    
    
    :type ClusterSecurityGroupName: string
    :param ClusterSecurityGroupName: [REQUIRED]\nThe name of the security group to which the ingress rule is added.\n

    :type CIDRIP: string
    :param CIDRIP: The IP range to be added the Amazon Redshift security group.

    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: The EC2 security group to be added the Amazon Redshift security group.

    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: The AWS account number of the owner of the security group specified by the EC2SecurityGroupName parameter. The AWS Access Key ID is not an acceptable value.\nExample: 111122223333\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ClusterSecurityGroup (dict) --
Describes a security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group to which the operation was applied.

Description (string) --
A description of the security group.

EC2SecurityGroups (list) --
A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.

(dict) --
Describes an Amazon EC2 security group.

Status (string) --
The status of the EC2 security group.

EC2SecurityGroupName (string) --
The name of the EC2 Security Group.

EC2SecurityGroupOwnerId (string) --
The AWS ID of the owner of the EC2 security group specified in the EC2SecurityGroupName field.

Tags (list) --
The list of tags for the EC2 security group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.









IPRanges (list) --
A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.

(dict) --
Describes an IP range used in a security group.

Status (string) --
The status of the IP range, for example, "authorized".

CIDRIP (string) --
The IP range in Classless Inter-Domain Routing (CIDR) notation.

Tags (list) --
The list of tags for the IP range.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.









Tags (list) --
The list of tags for the cluster security group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.ClusterSecurityGroupNotFoundFault
Redshift.Client.exceptions.InvalidClusterSecurityGroupStateFault
Redshift.Client.exceptions.AuthorizationAlreadyExistsFault
Redshift.Client.exceptions.AuthorizationQuotaExceededFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterSecurityGroupNotFoundFault
    Redshift.Client.exceptions.InvalidClusterSecurityGroupStateFault
    Redshift.Client.exceptions.AuthorizationAlreadyExistsFault
    Redshift.Client.exceptions.AuthorizationQuotaExceededFault
    
    """
    pass

def authorize_snapshot_access(SnapshotIdentifier=None, SnapshotClusterIdentifier=None, AccountWithRestoreAccess=None):
    """
    Authorizes the specified AWS customer account to restore the specified snapshot.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.authorize_snapshot_access(
        SnapshotIdentifier='string',
        SnapshotClusterIdentifier='string',
        AccountWithRestoreAccess='string'
    )
    
    
    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]\nThe identifier of the snapshot the account is authorized to restore.\n

    :type SnapshotClusterIdentifier: string
    :param SnapshotClusterIdentifier: The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

    :type AccountWithRestoreAccess: string
    :param AccountWithRestoreAccess: [REQUIRED]\nThe identifier of the AWS customer account authorized to restore the specified snapshot.\nTo share a snapshot with AWS support, specify amazon-redshift-support.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'EnhancedVpcRouting': True|False,
        'MaintenanceTrackName': 'string',
        'ManualSnapshotRetentionPeriod': 123,
        'ManualSnapshotRemainingDays': 123,
        'SnapshotRetentionStartTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Snapshot (dict) --
Describes a snapshot.

SnapshotIdentifier (string) --
The snapshot identifier that is provided in the request.

ClusterIdentifier (string) --
The identifier of the cluster for which the snapshot was taken.

SnapshotCreateTime (datetime) --
The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.

Status (string) --
The snapshot status. The value of the status depends on the API operation used:

CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
DeleteClusterSnapshot returns status as "deleted".


Port (integer) --
The port that the cluster is listening on.

AvailabilityZone (string) --
The Availability Zone in which the cluster was created.

ClusterCreateTime (datetime) --
The time (UTC) when the cluster was originally created.

MasterUsername (string) --
The master user name for the cluster.

ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

SnapshotType (string) --
The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot are of type "manual".

NodeType (string) --
The node type of the nodes in the cluster.

NumberOfNodes (integer) --
The number of nodes in the cluster.

DBName (string) --
The name of the database that was created when the cluster was created.

VpcId (string) --
The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.

Encrypted (boolean) --
If true , the data in the snapshot is encrypted at rest.

KmsKeyId (string) --
The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.

EncryptedWithHSM (boolean) --
A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. true indicates that the data is encrypted using HSM keys.

AccountsWithRestoreAccess (list) --
A list of the AWS customer accounts authorized to restore the snapshot. Returns null if no accounts are authorized. Visible only to the snapshot owner.

(dict) --
Describes an AWS customer account authorized to restore a snapshot.

AccountId (string) --
The identifier of an AWS customer account authorized to restore a snapshot.

AccountAlias (string) --
The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is amazon-redshift-support .





OwnerAccount (string) --
For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.

TotalBackupSizeInMegaBytes (float) --
The size of the complete set of backup data that would be used to restore the cluster.

ActualIncrementalBackupSizeInMegaBytes (float) --
The size of the incremental backup.

BackupProgressInMegaBytes (float) --
The number of megabytes that have been transferred to the snapshot backup.

CurrentBackupRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred to the snapshot backup. Returns 0 for a completed backup.

EstimatedSecondsToCompletion (integer) --
The estimate of the time remaining before the snapshot backup will complete. Returns 0 for a completed backup.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.

SourceRegion (string) --
The source region from which the snapshot was copied.

Tags (list) --
The list of tags for the cluster snapshot.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





RestorableNodeTypes (list) --
The list of node types that this cluster snapshot is able to restore into.

(string) --


EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track for the snapshot.

ManualSnapshotRetentionPeriod (integer) --
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

ManualSnapshotRemainingDays (integer) --
The number of days until a manual snapshot will pass its retention period.

SnapshotRetentionStartTime (datetime) --
A timestamp representing the start of the retention period for the snapshot.









Exceptions

Redshift.Client.exceptions.ClusterSnapshotNotFoundFault
Redshift.Client.exceptions.AuthorizationAlreadyExistsFault
Redshift.Client.exceptions.AuthorizationQuotaExceededFault
Redshift.Client.exceptions.DependentServiceRequestThrottlingFault
Redshift.Client.exceptions.InvalidClusterSnapshotStateFault
Redshift.Client.exceptions.LimitExceededFault


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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'ManualSnapshotRetentionPeriod': 123,
            'ManualSnapshotRemainingDays': 123,
            'SnapshotRetentionStartTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
    DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
    DeleteClusterSnapshot returns status as "deleted".
    
    """
    pass

def batch_delete_cluster_snapshots(Identifiers=None):
    """
    Deletes a set of cluster snapshots.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_delete_cluster_snapshots(
        Identifiers=[
            {
                'SnapshotIdentifier': 'string',
                'SnapshotClusterIdentifier': 'string'
            },
        ]
    )
    
    
    :type Identifiers: list
    :param Identifiers: [REQUIRED]\nA list of identifiers for the snapshots that you want to delete.\n\n(dict) --\nSnapshotIdentifier (string) -- [REQUIRED]The unique identifier of the manual snapshot to be deleted.\nConstraints: Must be the name of an existing snapshot that is in the available , failed , or cancelled state.\n\nSnapshotClusterIdentifier (string) --The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.\nConstraints: Must be the name of valid cluster.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Resources': [
        'string',
    ],
    'Errors': [
        {
            'SnapshotIdentifier': 'string',
            'SnapshotClusterIdentifier': 'string',
            'FailureCode': 'string',
            'FailureReason': 'string'
        },
    ]
}


Response Structure

(dict) --
Resources (list) --A list of the snapshot identifiers that were deleted.

(string) --


Errors (list) --A list of any errors returned.

(dict) --Describes the errors returned by a snapshot.

SnapshotIdentifier (string) --A unique identifier for the snapshot returning the error.

SnapshotClusterIdentifier (string) --A unique identifier for the cluster.

FailureCode (string) --The failure code for the error.

FailureReason (string) --The text message describing the error.










Exceptions

Redshift.Client.exceptions.BatchDeleteRequestSizeExceededFault


    :return: {
        'Resources': [
            'string',
        ],
        'Errors': [
            {
                'SnapshotIdentifier': 'string',
                'SnapshotClusterIdentifier': 'string',
                'FailureCode': 'string',
                'FailureReason': 'string'
            },
        ]
    }
    
    
    :returns: 
    Redshift.Client.exceptions.BatchDeleteRequestSizeExceededFault
    
    """
    pass

def batch_modify_cluster_snapshots(SnapshotIdentifierList=None, ManualSnapshotRetentionPeriod=None, Force=None):
    """
    Modifies the settings for a set of cluster snapshots.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_modify_cluster_snapshots(
        SnapshotIdentifierList=[
            'string',
        ],
        ManualSnapshotRetentionPeriod=123,
        Force=True|False
    )
    
    
    :type SnapshotIdentifierList: list
    :param SnapshotIdentifierList: [REQUIRED]\nA list of snapshot identifiers you want to modify.\n\n(string) --\n\n

    :type ManualSnapshotRetentionPeriod: integer
    :param ManualSnapshotRetentionPeriod: The number of days that a manual snapshot is retained. If you specify the value -1, the manual snapshot is retained indefinitely.\nThe number must be either -1 or an integer between 1 and 3,653.\nIf you decrease the manual snapshot retention period from its current value, existing manual snapshots that fall outside of the new retention period will return an error. If you want to suppress the errors and delete the snapshots, use the force option.\n

    :type Force: boolean
    :param Force: A boolean value indicating whether to override an exception if the retention period has passed.

    :rtype: dict

ReturnsResponse Syntax
{
    'Resources': [
        'string',
    ],
    'Errors': [
        {
            'SnapshotIdentifier': 'string',
            'SnapshotClusterIdentifier': 'string',
            'FailureCode': 'string',
            'FailureReason': 'string'
        },
    ]
}


Response Structure

(dict) --

Resources (list) --
A list of the snapshots that were modified.

(string) --


Errors (list) --
A list of any errors returned.

(dict) --
Describes the errors returned by a snapshot.

SnapshotIdentifier (string) --
A unique identifier for the snapshot returning the error.

SnapshotClusterIdentifier (string) --
A unique identifier for the cluster.

FailureCode (string) --
The failure code for the error.

FailureReason (string) --
The text message describing the error.











Exceptions

Redshift.Client.exceptions.InvalidRetentionPeriodFault
Redshift.Client.exceptions.BatchModifyClusterSnapshotsLimitExceededFault


    :return: {
        'Resources': [
            'string',
        ],
        'Errors': [
            {
                'SnapshotIdentifier': 'string',
                'SnapshotClusterIdentifier': 'string',
                'FailureCode': 'string',
                'FailureReason': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_resize(ClusterIdentifier=None):
    """
    Cancels a resize operation for a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_resize(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier for the cluster that you want to cancel a resize operation for.\n

    :rtype: dict
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
    'EstimatedTimeToCompletionInSeconds': 123,
    'ResizeType': 'string',
    'Message': 'string',
    'TargetEncryptionType': 'string',
    'DataTransferProgressPercent': 123.0
}


Response Structure

(dict) --Describes the result of a cluster resize operation.

TargetNodeType (string) --The node type that the cluster will have after the resize operation is complete.

TargetNumberOfNodes (integer) --The number of nodes that the cluster will have after the resize operation is complete.

TargetClusterType (string) --The cluster type after the resize operation is complete.
Valid Values: multi-node | single-node

Status (string) --The status of the resize operation.
Valid Values: NONE | IN_PROGRESS | FAILED | SUCCEEDED | CANCELLING

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

ResizeType (string) --An enum with possible values of ClassicResize and ElasticResize . These values describe the type of resize operation being performed.

Message (string) --An optional string to provide additional details about the resize action.

TargetEncryptionType (string) --The type of encryption for the cluster after the resize is complete.
Possible values are KMS and None . In the China region possible values are: Legacy and None .

DataTransferProgressPercent (float) --The percent of data transferred from source cluster to target cluster.






Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.ResizeNotFoundFault
Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.UnsupportedOperationFault


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
        'EstimatedTimeToCompletionInSeconds': 123,
        'ResizeType': 'string',
        'Message': 'string',
        'TargetEncryptionType': 'string',
        'DataTransferProgressPercent': 123.0
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def copy_cluster_snapshot(SourceSnapshotIdentifier=None, SourceSnapshotClusterIdentifier=None, TargetSnapshotIdentifier=None, ManualSnapshotRetentionPeriod=None):
    """
    Copies the specified automated cluster snapshot to a new manual cluster snapshot. The source must be an automated snapshot and it must be in the available state.
    When you delete a cluster, Amazon Redshift deletes any automated snapshots of the cluster. Also, when the retention period of the snapshot expires, Amazon Redshift automatically deletes it. If you want to keep an automated snapshot for a longer period, you can make a manual copy of the snapshot. Manual snapshots are retained until you delete them.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.copy_cluster_snapshot(
        SourceSnapshotIdentifier='string',
        SourceSnapshotClusterIdentifier='string',
        TargetSnapshotIdentifier='string',
        ManualSnapshotRetentionPeriod=123
    )
    
    
    :type SourceSnapshotIdentifier: string
    :param SourceSnapshotIdentifier: [REQUIRED]\nThe identifier for the source snapshot.\nConstraints:\n\nMust be the identifier for a valid automated snapshot whose state is available .\n\n

    :type SourceSnapshotClusterIdentifier: string
    :param SourceSnapshotClusterIdentifier: The identifier of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.\nConstraints:\n\nMust be the identifier for a valid cluster.\n\n

    :type TargetSnapshotIdentifier: string
    :param TargetSnapshotIdentifier: [REQUIRED]\nThe identifier given to the new manual snapshot.\nConstraints:\n\nCannot be null, empty, or blank.\nMust contain from 1 to 255 alphanumeric characters or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\nMust be unique for the AWS account that is making the request.\n\n

    :type ManualSnapshotRetentionPeriod: integer
    :param ManualSnapshotRetentionPeriod: The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.\nThe value must be either -1 or an integer between 1 and 3,653.\nThe default value is -1.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'EnhancedVpcRouting': True|False,
        'MaintenanceTrackName': 'string',
        'ManualSnapshotRetentionPeriod': 123,
        'ManualSnapshotRemainingDays': 123,
        'SnapshotRetentionStartTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Snapshot (dict) --
Describes a snapshot.

SnapshotIdentifier (string) --
The snapshot identifier that is provided in the request.

ClusterIdentifier (string) --
The identifier of the cluster for which the snapshot was taken.

SnapshotCreateTime (datetime) --
The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.

Status (string) --
The snapshot status. The value of the status depends on the API operation used:

CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
DeleteClusterSnapshot returns status as "deleted".


Port (integer) --
The port that the cluster is listening on.

AvailabilityZone (string) --
The Availability Zone in which the cluster was created.

ClusterCreateTime (datetime) --
The time (UTC) when the cluster was originally created.

MasterUsername (string) --
The master user name for the cluster.

ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

SnapshotType (string) --
The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot are of type "manual".

NodeType (string) --
The node type of the nodes in the cluster.

NumberOfNodes (integer) --
The number of nodes in the cluster.

DBName (string) --
The name of the database that was created when the cluster was created.

VpcId (string) --
The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.

Encrypted (boolean) --
If true , the data in the snapshot is encrypted at rest.

KmsKeyId (string) --
The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.

EncryptedWithHSM (boolean) --
A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. true indicates that the data is encrypted using HSM keys.

AccountsWithRestoreAccess (list) --
A list of the AWS customer accounts authorized to restore the snapshot. Returns null if no accounts are authorized. Visible only to the snapshot owner.

(dict) --
Describes an AWS customer account authorized to restore a snapshot.

AccountId (string) --
The identifier of an AWS customer account authorized to restore a snapshot.

AccountAlias (string) --
The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is amazon-redshift-support .





OwnerAccount (string) --
For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.

TotalBackupSizeInMegaBytes (float) --
The size of the complete set of backup data that would be used to restore the cluster.

ActualIncrementalBackupSizeInMegaBytes (float) --
The size of the incremental backup.

BackupProgressInMegaBytes (float) --
The number of megabytes that have been transferred to the snapshot backup.

CurrentBackupRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred to the snapshot backup. Returns 0 for a completed backup.

EstimatedSecondsToCompletion (integer) --
The estimate of the time remaining before the snapshot backup will complete. Returns 0 for a completed backup.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.

SourceRegion (string) --
The source region from which the snapshot was copied.

Tags (list) --
The list of tags for the cluster snapshot.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





RestorableNodeTypes (list) --
The list of node types that this cluster snapshot is able to restore into.

(string) --


EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track for the snapshot.

ManualSnapshotRetentionPeriod (integer) --
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

ManualSnapshotRemainingDays (integer) --
The number of days until a manual snapshot will pass its retention period.

SnapshotRetentionStartTime (datetime) --
A timestamp representing the start of the retention period for the snapshot.









Exceptions

Redshift.Client.exceptions.ClusterSnapshotAlreadyExistsFault
Redshift.Client.exceptions.ClusterSnapshotNotFoundFault
Redshift.Client.exceptions.InvalidClusterSnapshotStateFault
Redshift.Client.exceptions.ClusterSnapshotQuotaExceededFault
Redshift.Client.exceptions.InvalidRetentionPeriodFault


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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'ManualSnapshotRetentionPeriod': 123,
            'ManualSnapshotRemainingDays': 123,
            'SnapshotRetentionStartTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
    DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
    DeleteClusterSnapshot returns status as "deleted".
    
    """
    pass

def create_cluster(DBName=None, ClusterIdentifier=None, ClusterType=None, NodeType=None, MasterUsername=None, MasterUserPassword=None, ClusterSecurityGroups=None, VpcSecurityGroupIds=None, ClusterSubnetGroupName=None, AvailabilityZone=None, PreferredMaintenanceWindow=None, ClusterParameterGroupName=None, AutomatedSnapshotRetentionPeriod=None, ManualSnapshotRetentionPeriod=None, Port=None, ClusterVersion=None, AllowVersionUpgrade=None, NumberOfNodes=None, PubliclyAccessible=None, Encrypted=None, HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None, ElasticIp=None, Tags=None, KmsKeyId=None, EnhancedVpcRouting=None, AdditionalInfo=None, IamRoles=None, MaintenanceTrackName=None, SnapshotScheduleIdentifier=None):
    """
    Creates a new cluster with the specified parameters.
    To create a cluster in Virtual Private Cloud (VPC), you must provide a cluster subnet group name. The cluster subnet group identifies the subnets of your VPC that Amazon Redshift uses when creating the cluster. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
        ManualSnapshotRetentionPeriod=123,
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
        ],
        MaintenanceTrackName='string',
        SnapshotScheduleIdentifier='string'
    )
    
    
    :type DBName: string
    :param DBName: The name of the first database to be created when the cluster is created.\nTo create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to Create a Database in the Amazon Redshift Database Developer Guide.\nDefault: dev\nConstraints:\n\nMust contain 1 to 64 alphanumeric characters.\nMust contain only lowercase letters.\nCannot be a word that is reserved by the service. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.\n\n

    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nA unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.\nConstraints:\n\nMust contain from 1 to 63 alphanumeric characters or hyphens.\nAlphabetic characters must be lowercase.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\nMust be unique for all clusters within an AWS account.\n\nExample: myexamplecluster\n

    :type ClusterType: string
    :param ClusterType: The type of the cluster. When cluster type is specified as\n\nsingle-node , the NumberOfNodes parameter is not required.\nmulti-node , the NumberOfNodes parameter is required.\n\nValid Values: multi-node | single-node\nDefault: multi-node\n

    :type NodeType: string
    :param NodeType: [REQUIRED]\nThe node type to be provisioned for the cluster. For information about node types, go to Working with Clusters in the Amazon Redshift Cluster Management Guide .\nValid Values: ds2.xlarge | ds2.8xlarge | dc1.large | dc1.8xlarge | dc2.large | dc2.8xlarge | ra3.4xlarge | ra3.16xlarge\n

    :type MasterUsername: string
    :param MasterUsername: [REQUIRED]\nThe user name associated with the master user account for the cluster that is being created.\nConstraints:\n\nMust be 1 - 128 alphanumeric characters. The user name can\'t be PUBLIC .\nFirst character must be a letter.\nCannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.\n\n

    :type MasterUserPassword: string
    :param MasterUserPassword: [REQUIRED]\nThe password associated with the master user account for the cluster that is being created.\nConstraints:\n\nMust be between 8 and 64 characters in length.\nMust contain at least one uppercase letter.\nMust contain at least one lowercase letter.\nMust contain one number.\nCan be any printable ASCII character (ASCII code 33 to 126) except \' (single quote), ' (double quote), , /, @, or space.\n\n

    :type ClusterSecurityGroups: list
    :param ClusterSecurityGroups: A list of security groups to be associated with this cluster.\nDefault: The default cluster security group for Amazon Redshift.\n\n(string) --\n\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.\nDefault: The default VPC security group is associated with the cluster.\n\n(string) --\n\n

    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: The name of a cluster subnet group to be associated with this cluster.\nIf this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).\n

    :type AvailabilityZone: string
    :param AvailabilityZone: The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.\nDefault: A random, system-chosen Availability Zone in the region that is specified by the endpoint.\nExample: us-east-2d\nConstraint: The specified Availability Zone must be in the same region as the current endpoint.\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which automated cluster maintenance can occur.\nFormat: ddd:hh24:mi-ddd:hh24:mi\nDefault: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see Maintenance Windows in Amazon Redshift Cluster Management Guide.\nValid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun\nConstraints: Minimum 30-minute window.\n

    :type ClusterParameterGroupName: string
    :param ClusterParameterGroupName: The name of the parameter group to be associated with this cluster.\nDefault: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to Working with Amazon Redshift Parameter Groups\nConstraints:\n\nMust be 1 to 255 alphanumeric characters or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type AutomatedSnapshotRetentionPeriod: integer
    :param AutomatedSnapshotRetentionPeriod: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with CreateClusterSnapshot .\nDefault: 1\nConstraints: Must be a value from 0 to 35.\n

    :type ManualSnapshotRetentionPeriod: integer
    :param ManualSnapshotRetentionPeriod: The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.\nThe value must be either -1 or an integer between 1 and 3,653.\n

    :type Port: integer
    :param Port: The port number on which the cluster accepts incoming connections.\nThe cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.\nDefault: 5439\nValid Values: 1150-65535\n

    :type ClusterVersion: string
    :param ClusterVersion: The version of the Amazon Redshift engine software that you want to deploy on the cluster.\nThe version selected runs on all the nodes in the cluster.\nConstraints: Only version 1.0 is currently available.\nExample: 1.0\n

    :type AllowVersionUpgrade: boolean
    :param AllowVersionUpgrade: If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.\nWhen a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.\nDefault: true\n

    :type NumberOfNodes: integer
    :param NumberOfNodes: The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node .\nFor information about determining how many nodes you need, go to Working with Clusters in the Amazon Redshift Cluster Management Guide .\nIf you don\'t specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.\nDefault: 1\nConstraints: Value must be at least 1 and no more than 100.\n

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: If true , the cluster can be accessed from a public network.

    :type Encrypted: boolean
    :param Encrypted: If true , the data in the cluster is encrypted at rest.\nDefault: false\n

    :type HsmClientCertificateIdentifier: string
    :param HsmClientCertificateIdentifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

    :type HsmConfigurationIdentifier: string
    :param HsmConfigurationIdentifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

    :type ElasticIp: string
    :param ElasticIp: The Elastic IP (EIP) address for the cluster.\nConstraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to Supported Platforms to Launch Your Cluster in the Amazon Redshift Cluster Management Guide.\n

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.

    :type EnhancedVpcRouting: boolean
    :param EnhancedVpcRouting: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.\nIf this option is true , enhanced VPC routing is enabled.\nDefault: false\n

    :type AdditionalInfo: string
    :param AdditionalInfo: Reserved.

    :type IamRoles: list
    :param IamRoles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM roles in a single request.\nA cluster can have up to 10 IAM roles associated with it at any time.\n\n(string) --\n\n

    :type MaintenanceTrackName: string
    :param MaintenanceTrackName: An optional parameter for the name of the maintenance track for the cluster. If you don\'t provide a maintenance track name, the cluster is assigned to the current track.

    :type SnapshotScheduleIdentifier: string
    :param SnapshotScheduleIdentifier: A unique identifier for the snapshot schedule.

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.ClusterAlreadyExistsFault
Redshift.Client.exceptions.InsufficientClusterCapacityFault
Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
Redshift.Client.exceptions.ClusterSecurityGroupNotFoundFault
Redshift.Client.exceptions.ClusterQuotaExceededFault
Redshift.Client.exceptions.NumberOfNodesQuotaExceededFault
Redshift.Client.exceptions.NumberOfNodesPerClusterLimitExceededFault
Redshift.Client.exceptions.ClusterSubnetGroupNotFoundFault
Redshift.Client.exceptions.InvalidVPCNetworkStateFault
Redshift.Client.exceptions.InvalidClusterSubnetGroupStateFault
Redshift.Client.exceptions.InvalidSubnet
Redshift.Client.exceptions.UnauthorizedOperation
Redshift.Client.exceptions.HsmClientCertificateNotFoundFault
Redshift.Client.exceptions.HsmConfigurationNotFoundFault
Redshift.Client.exceptions.InvalidElasticIpFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault
Redshift.Client.exceptions.LimitExceededFault
Redshift.Client.exceptions.DependentServiceRequestThrottlingFault
Redshift.Client.exceptions.InvalidClusterTrackFault
Redshift.Client.exceptions.SnapshotScheduleNotFoundFault
Redshift.Client.exceptions.InvalidRetentionPeriodFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
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
    
    Exceptions
    
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
    :param ParameterGroupName: [REQUIRED]\nThe name of the cluster parameter group.\nConstraints:\n\nMust be 1 to 255 alphanumeric characters or hyphens\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\nMust be unique withing your AWS account.\n\n\nNote\nThis value is stored as a lower-case string.\n\n

    :type ParameterGroupFamily: string
    :param ParameterGroupFamily: [REQUIRED]\nThe Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.\nTo get a list of valid parameter group family names, you can call DescribeClusterParameterGroups . By default, Amazon Redshift returns a list of all the parameter groups that are owned by your AWS account, including the default parameter groups for each Amazon Redshift engine version. The parameter group family names associated with the default parameter groups provide you the valid values. For example, a valid family name is 'redshift-1.0'.\n

    :type Description: string
    :param Description: [REQUIRED]\nA description of the parameter group.\n

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ClusterParameterGroup (dict) --
Describes a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterGroupFamily (string) --
The name of the cluster parameter group family that this cluster parameter group is compatible with.

Description (string) --
The description of the parameter group.

Tags (list) --
The list of tags for the cluster parameter group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.ClusterParameterGroupQuotaExceededFault
Redshift.Client.exceptions.ClusterParameterGroupAlreadyExistsFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterParameterGroupQuotaExceededFault
    Redshift.Client.exceptions.ClusterParameterGroupAlreadyExistsFault
    Redshift.Client.exceptions.TagLimitExceededFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def create_cluster_security_group(ClusterSecurityGroupName=None, Description=None, Tags=None):
    """
    Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.
    For information about managing security groups, go to Amazon Redshift Cluster Security Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ClusterSecurityGroupName: [REQUIRED]\nThe name for the security group. Amazon Redshift stores the value as a lowercase string.\nConstraints:\n\nMust contain no more than 255 alphanumeric characters or hyphens.\nMust not be 'Default'.\nMust be unique for all security groups that are created by your AWS account.\n\nExample: examplesecuritygroup\n

    :type Description: string
    :param Description: [REQUIRED]\nA description for the security group.\n

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ClusterSecurityGroup (dict) --
Describes a security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group to which the operation was applied.

Description (string) --
A description of the security group.

EC2SecurityGroups (list) --
A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.

(dict) --
Describes an Amazon EC2 security group.

Status (string) --
The status of the EC2 security group.

EC2SecurityGroupName (string) --
The name of the EC2 Security Group.

EC2SecurityGroupOwnerId (string) --
The AWS ID of the owner of the EC2 security group specified in the EC2SecurityGroupName field.

Tags (list) --
The list of tags for the EC2 security group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.









IPRanges (list) --
A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.

(dict) --
Describes an IP range used in a security group.

Status (string) --
The status of the IP range, for example, "authorized".

CIDRIP (string) --
The IP range in Classless Inter-Domain Routing (CIDR) notation.

Tags (list) --
The list of tags for the IP range.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.









Tags (list) --
The list of tags for the cluster security group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.ClusterSecurityGroupAlreadyExistsFault
Redshift.Client.exceptions.ClusterSecurityGroupQuotaExceededFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterSecurityGroupAlreadyExistsFault
    Redshift.Client.exceptions.ClusterSecurityGroupQuotaExceededFault
    Redshift.Client.exceptions.TagLimitExceededFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def create_cluster_snapshot(SnapshotIdentifier=None, ClusterIdentifier=None, ManualSnapshotRetentionPeriod=None, Tags=None):
    """
    Creates a manual snapshot of the specified cluster. The cluster must be in the available state.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_cluster_snapshot(
        SnapshotIdentifier='string',
        ClusterIdentifier='string',
        ManualSnapshotRetentionPeriod=123,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]\nA unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the AWS account.\nConstraints:\n\nCannot be null, empty, or blank\nMust contain from 1 to 255 alphanumeric characters or hyphens\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\nExample: my-snapshot-id\n

    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe cluster identifier for which you want a snapshot.\n

    :type ManualSnapshotRetentionPeriod: integer
    :param ManualSnapshotRetentionPeriod: The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.\nThe value must be either -1 or an integer between 1 and 3,653.\nThe default value is -1.\n

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'EnhancedVpcRouting': True|False,
        'MaintenanceTrackName': 'string',
        'ManualSnapshotRetentionPeriod': 123,
        'ManualSnapshotRemainingDays': 123,
        'SnapshotRetentionStartTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Snapshot (dict) --
Describes a snapshot.

SnapshotIdentifier (string) --
The snapshot identifier that is provided in the request.

ClusterIdentifier (string) --
The identifier of the cluster for which the snapshot was taken.

SnapshotCreateTime (datetime) --
The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.

Status (string) --
The snapshot status. The value of the status depends on the API operation used:

CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
DeleteClusterSnapshot returns status as "deleted".


Port (integer) --
The port that the cluster is listening on.

AvailabilityZone (string) --
The Availability Zone in which the cluster was created.

ClusterCreateTime (datetime) --
The time (UTC) when the cluster was originally created.

MasterUsername (string) --
The master user name for the cluster.

ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

SnapshotType (string) --
The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot are of type "manual".

NodeType (string) --
The node type of the nodes in the cluster.

NumberOfNodes (integer) --
The number of nodes in the cluster.

DBName (string) --
The name of the database that was created when the cluster was created.

VpcId (string) --
The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.

Encrypted (boolean) --
If true , the data in the snapshot is encrypted at rest.

KmsKeyId (string) --
The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.

EncryptedWithHSM (boolean) --
A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. true indicates that the data is encrypted using HSM keys.

AccountsWithRestoreAccess (list) --
A list of the AWS customer accounts authorized to restore the snapshot. Returns null if no accounts are authorized. Visible only to the snapshot owner.

(dict) --
Describes an AWS customer account authorized to restore a snapshot.

AccountId (string) --
The identifier of an AWS customer account authorized to restore a snapshot.

AccountAlias (string) --
The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is amazon-redshift-support .





OwnerAccount (string) --
For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.

TotalBackupSizeInMegaBytes (float) --
The size of the complete set of backup data that would be used to restore the cluster.

ActualIncrementalBackupSizeInMegaBytes (float) --
The size of the incremental backup.

BackupProgressInMegaBytes (float) --
The number of megabytes that have been transferred to the snapshot backup.

CurrentBackupRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred to the snapshot backup. Returns 0 for a completed backup.

EstimatedSecondsToCompletion (integer) --
The estimate of the time remaining before the snapshot backup will complete. Returns 0 for a completed backup.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.

SourceRegion (string) --
The source region from which the snapshot was copied.

Tags (list) --
The list of tags for the cluster snapshot.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





RestorableNodeTypes (list) --
The list of node types that this cluster snapshot is able to restore into.

(string) --


EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track for the snapshot.

ManualSnapshotRetentionPeriod (integer) --
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

ManualSnapshotRemainingDays (integer) --
The number of days until a manual snapshot will pass its retention period.

SnapshotRetentionStartTime (datetime) --
A timestamp representing the start of the retention period for the snapshot.









Exceptions

Redshift.Client.exceptions.ClusterSnapshotAlreadyExistsFault
Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.ClusterSnapshotQuotaExceededFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault
Redshift.Client.exceptions.InvalidRetentionPeriodFault


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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'ManualSnapshotRetentionPeriod': 123,
            'ManualSnapshotRemainingDays': 123,
            'SnapshotRetentionStartTime': datetime(2015, 1, 1)
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
    
    Exceptions
    
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
    :param ClusterSubnetGroupName: [REQUIRED]\nThe name for the subnet group. Amazon Redshift stores the value as a lowercase string.\nConstraints:\n\nMust contain no more than 255 alphanumeric characters or hyphens.\nMust not be 'Default'.\nMust be unique for all subnet groups that are created by your AWS account.\n\nExample: examplesubnetgroup\n

    :type Description: string
    :param Description: [REQUIRED]\nA description for the subnet group.\n

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nAn array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterSubnetGroup': {
        'ClusterSubnetGroupName': 'string',
        'Description': 'string',
        'VpcId': 'string',
        'SubnetGroupStatus': 'string',
        'Subnets': [
            {
                'SubnetIdentifier': 'string',
                'SubnetAvailabilityZone': {
                    'Name': 'string',
                    'SupportedPlatforms': [
                        {
                            'Name': 'string'
                        },
                    ]
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


Response Structure

(dict) --

ClusterSubnetGroup (dict) --
Describes a subnet group.

ClusterSubnetGroupName (string) --
The name of the cluster subnet group.

Description (string) --
The description of the cluster subnet group.

VpcId (string) --
The VPC ID of the cluster subnet group.

SubnetGroupStatus (string) --
The status of the cluster subnet group. Possible values are Complete , Incomplete and Invalid .

Subnets (list) --
A list of the VPC  Subnet elements.

(dict) --
Describes a subnet.

SubnetIdentifier (string) --
The identifier of the subnet.

SubnetAvailabilityZone (dict) --

Name (string) --
The name of the availability zone.

SupportedPlatforms (list) --

(dict) --
A list of supported platforms for orderable clusters.

Name (string) --






SubnetStatus (string) --
The status of the subnet.





Tags (list) --
The list of tags for the cluster subnet group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.ClusterSubnetGroupAlreadyExistsFault
Redshift.Client.exceptions.ClusterSubnetGroupQuotaExceededFault
Redshift.Client.exceptions.ClusterSubnetQuotaExceededFault
Redshift.Client.exceptions.InvalidSubnet
Redshift.Client.exceptions.UnauthorizedOperation
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault
Redshift.Client.exceptions.DependentServiceRequestThrottlingFault


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
                        'Name': 'string',
                        'SupportedPlatforms': [
                            {
                                'Name': 'string'
                            },
                        ]
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
    
    
    :returns: 
    Name (string) --
    
    """
    pass

def create_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, SourceIds=None, EventCategories=None, Severity=None, Enabled=None, Tags=None):
    """
    Creates an Amazon Redshift event notification subscription. This action requires an ARN (Amazon Resource Name) of an Amazon SNS topic created by either the Amazon Redshift console, the Amazon SNS console, or the Amazon SNS API. To obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.
    You can specify the source type, and lists of Amazon Redshift source IDs, event categories, and event severities. Notifications will be sent for all events you want that match those criteria. For example, you can specify source type = cluster, source ID = my-cluster-1 and mycluster2, event categories = Availability, Backup, and severity = ERROR. The subscription will only send notifications for those ERROR events in the Availability and Backup categories for the specified clusters.
    If you specify both the source type and source IDs, such as source type = cluster and source identifier = my-cluster-1, notifications will be sent for all the cluster events for my-cluster-1. If you specify a source type but do not specify a source identifier, you will receive notice of the events for the objects of that type in your AWS account. If you do not specify either the SourceType nor the SourceIdentifier, you will be notified of events generated from all Amazon Redshift sources belonging to your AWS account. You must specify a source type if you specify a source ID.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param SubscriptionName: [REQUIRED]\nThe name of the event subscription to be created.\nConstraints:\n\nCannot be null, empty, or blank.\nMust contain from 1 to 255 alphanumeric characters or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type SnsTopicArn: string
    :param SnsTopicArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.\n

    :type SourceType: string
    :param SourceType: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account. You must specify a source type in order to specify source IDs.\nValid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.\n

    :type SourceIds: list
    :param SourceIds: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.\nExample: my-cluster-1, my-cluster-2\nExample: my-snapshot-20131010\n\n(string) --\n\n

    :type EventCategories: list
    :param EventCategories: Specifies the Amazon Redshift event categories to be published by the event notification subscription.\nValues: configuration, management, monitoring, security\n\n(string) --\n\n

    :type Severity: string
    :param Severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription.\nValues: ERROR, INFO\n

    :type Enabled: boolean
    :param Enabled: A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

EventSubscription (dict) --
Describes event subscriptions.

CustomerAwsId (string) --
The AWS customer account associated with the Amazon Redshift event notification subscription.

CustSubscriptionId (string) --
The name of the Amazon Redshift event notification subscription.

SnsTopicArn (string) --
The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.

Status (string) --
The status of the Amazon Redshift event notification subscription.
Constraints:

Can be one of the following: active | no-permission | topic-not-exist
The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.


SubscriptionCreationTime (datetime) --
The date and time the Amazon Redshift event notification subscription was created.

SourceType (string) --
The source type of the events returned by the Amazon Redshift event notification, such as cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, or scheduled-action.

SourceIdsList (list) --
A list of the sources that publish events to the Amazon Redshift event notification subscription.

(string) --


EventCategoriesList (list) --
The list of Amazon Redshift event categories specified in the event notification subscription.
Values: Configuration, Management, Monitoring, Security

(string) --


Severity (string) --
The event severity specified in the Amazon Redshift event notification subscription.
Values: ERROR, INFO

Enabled (boolean) --
A boolean value indicating whether the subscription is enabled; true indicates that the subscription is enabled.

Tags (list) --
The list of tags for the event subscription.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.EventSubscriptionQuotaExceededFault
Redshift.Client.exceptions.SubscriptionAlreadyExistFault
Redshift.Client.exceptions.SNSInvalidTopicFault
Redshift.Client.exceptions.SNSNoAuthorizationFault
Redshift.Client.exceptions.SNSTopicArnNotFoundFault
Redshift.Client.exceptions.SubscriptionEventIdNotFoundFault
Redshift.Client.exceptions.SubscriptionCategoryNotFoundFault
Redshift.Client.exceptions.SubscriptionSeverityNotFoundFault
Redshift.Client.exceptions.SourceNotFoundFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault


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
    Creates an HSM client certificate that an Amazon Redshift cluster will use to connect to the client\'s HSM in order to store and retrieve the keys used to encrypt the cluster databases.
    The command returns a public key, which you must store in the HSM. In addition to creating the HSM certificate, you must create an Amazon Redshift HSM configuration that provides a cluster the information needed to store and use encryption keys in the HSM. For more information, go to Hardware Security Modules in the Amazon Redshift Cluster Management Guide.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param HsmClientCertificateIdentifier: [REQUIRED]\nThe identifier to be assigned to the new HSM client certificate that the cluster will use to connect to the HSM to use the database encryption keys.\n

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

HsmClientCertificate (dict) --
Returns information about an HSM client certificate. The certificate is stored in a secure Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data files.

HsmClientCertificateIdentifier (string) --
The identifier of the HSM client certificate.

HsmClientCertificatePublicKey (string) --
The public key that the Amazon Redshift cluster will use to connect to the HSM. You must register the public key in the HSM.

Tags (list) --
The list of tags for the HSM client certificate.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.HsmClientCertificateAlreadyExistsFault
Redshift.Client.exceptions.HsmClientCertificateQuotaExceededFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.HsmClientCertificateAlreadyExistsFault
    Redshift.Client.exceptions.HsmClientCertificateQuotaExceededFault
    Redshift.Client.exceptions.TagLimitExceededFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def create_hsm_configuration(HsmConfigurationIdentifier=None, Description=None, HsmIpAddress=None, HsmPartitionName=None, HsmPartitionPassword=None, HsmServerPublicCertificate=None, Tags=None):
    """
    Creates an HSM configuration that contains the information required by an Amazon Redshift cluster to store and use database encryption keys in a Hardware Security Module (HSM). After creating the HSM configuration, you can specify it as a parameter when creating a cluster. The cluster will then store its encryption keys in the HSM.
    In addition to creating an HSM configuration, you must also create an HSM client certificate. For more information, go to Hardware Security Modules in the Amazon Redshift Cluster Management Guide.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param HsmConfigurationIdentifier: [REQUIRED]\nThe identifier to be assigned to the new Amazon Redshift HSM configuration.\n

    :type Description: string
    :param Description: [REQUIRED]\nA text description of the HSM configuration to be created.\n

    :type HsmIpAddress: string
    :param HsmIpAddress: [REQUIRED]\nThe IP address that the Amazon Redshift cluster must use to access the HSM.\n

    :type HsmPartitionName: string
    :param HsmPartitionName: [REQUIRED]\nThe name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.\n

    :type HsmPartitionPassword: string
    :param HsmPartitionPassword: [REQUIRED]\nThe password required to access the HSM partition.\n

    :type HsmServerPublicCertificate: string
    :param HsmServerPublicCertificate: [REQUIRED]\nThe HSMs public certificate file. When using Cloud HSM, the file name is server.pem.\n

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

HsmConfiguration (dict) --
Returns information about an HSM configuration, which is an object that describes to Amazon Redshift clusters the information they require to connect to an HSM where they can store database encryption keys.

HsmConfigurationIdentifier (string) --
The name of the Amazon Redshift HSM configuration.

Description (string) --
A text description of the HSM configuration.

HsmIpAddress (string) --
The IP address that the Amazon Redshift cluster must use to access the HSM.

HsmPartitionName (string) --
The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.

Tags (list) --
The list of tags for the HSM configuration.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.HsmConfigurationAlreadyExistsFault
Redshift.Client.exceptions.HsmConfigurationQuotaExceededFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.HsmConfigurationAlreadyExistsFault
    Redshift.Client.exceptions.HsmConfigurationQuotaExceededFault
    Redshift.Client.exceptions.TagLimitExceededFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def create_scheduled_action(ScheduledActionName=None, TargetAction=None, Schedule=None, IamRole=None, ScheduledActionDescription=None, StartTime=None, EndTime=None, Enable=None):
    """
    Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the ResizeCluster API operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_scheduled_action(
        ScheduledActionName='string',
        TargetAction={
            'ResizeCluster': {
                'ClusterIdentifier': 'string',
                'ClusterType': 'string',
                'NodeType': 'string',
                'NumberOfNodes': 123,
                'Classic': True|False
            },
            'PauseCluster': {
                'ClusterIdentifier': 'string'
            },
            'ResumeCluster': {
                'ClusterIdentifier': 'string'
            }
        },
        Schedule='string',
        IamRole='string',
        ScheduledActionDescription='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Enable=True|False
    )
    
    
    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]\nThe name of the scheduled action. The name must be unique within an account. For more information about this parameter, see ScheduledAction .\n

    :type TargetAction: dict
    :param TargetAction: [REQUIRED]\nA JSON format string of the Amazon Redshift API operation with input parameters. For more information about this parameter, see ScheduledAction .\n\nResizeCluster (dict) --An action that runs a ResizeCluster API operation.\n\nClusterIdentifier (string) -- [REQUIRED]The unique identifier for the cluster to resize.\n\nClusterType (string) --The new cluster type for the specified cluster.\n\nNodeType (string) --The new node type for the nodes you are adding. If not specified, the cluster\'s current node type is used.\n\nNumberOfNodes (integer) --The new number of nodes for the cluster.\n\nClassic (boolean) --A boolean value indicating whether the resize operation is using the classic resize process. If you don\'t provide this parameter or set the value to false , the resize type is elastic.\n\n\n\nPauseCluster (dict) --An action that runs a PauseCluster API operation.\n\nClusterIdentifier (string) -- [REQUIRED]The identifier of the cluster to be paused.\n\n\n\nResumeCluster (dict) --An action that runs a ResumeCluster API operation.\n\nClusterIdentifier (string) -- [REQUIRED]The identifier of the cluster to be resumed.\n\n\n\n\n

    :type Schedule: string
    :param Schedule: [REQUIRED]\nThe schedule in at( ) or cron( ) format. For more information about this parameter, see ScheduledAction .\n

    :type IamRole: string
    :param IamRole: [REQUIRED]\nThe IAM role to assume to run the target action. For more information about this parameter, see ScheduledAction .\n

    :type ScheduledActionDescription: string
    :param ScheduledActionDescription: The description of the scheduled action.

    :type StartTime: datetime
    :param StartTime: The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger. For more information about this parameter, see ScheduledAction .

    :type EndTime: datetime
    :param EndTime: The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger. For more information about this parameter, see ScheduledAction .

    :type Enable: boolean
    :param Enable: If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about state of the scheduled action, see ScheduledAction .

    :rtype: dict

ReturnsResponse Syntax
{
    'ScheduledActionName': 'string',
    'TargetAction': {
        'ResizeCluster': {
            'ClusterIdentifier': 'string',
            'ClusterType': 'string',
            'NodeType': 'string',
            'NumberOfNodes': 123,
            'Classic': True|False
        },
        'PauseCluster': {
            'ClusterIdentifier': 'string'
        },
        'ResumeCluster': {
            'ClusterIdentifier': 'string'
        }
    },
    'Schedule': 'string',
    'IamRole': 'string',
    'ScheduledActionDescription': 'string',
    'State': 'ACTIVE'|'DISABLED',
    'NextInvocations': [
        datetime(2015, 1, 1),
    ],
    'StartTime': datetime(2015, 1, 1),
    'EndTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --
Describes a scheduled action. You can use a scheduled action to trigger some Amazon Redshift API operations on a schedule. For information about which API operations can be scheduled, see  ScheduledActionType .

ScheduledActionName (string) --
The name of the scheduled action.

TargetAction (dict) --
A JSON format string of the Amazon Redshift API operation with input parameters.
"{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}} ".

ResizeCluster (dict) --
An action that runs a ResizeCluster API operation.

ClusterIdentifier (string) --
The unique identifier for the cluster to resize.

ClusterType (string) --
The new cluster type for the specified cluster.

NodeType (string) --
The new node type for the nodes you are adding. If not specified, the cluster\'s current node type is used.

NumberOfNodes (integer) --
The new number of nodes for the cluster.

Classic (boolean) --
A boolean value indicating whether the resize operation is using the classic resize process. If you don\'t provide this parameter or set the value to false , the resize type is elastic.



PauseCluster (dict) --
An action that runs a PauseCluster API operation.

ClusterIdentifier (string) --
The identifier of the cluster to be paused.



ResumeCluster (dict) --
An action that runs a ResumeCluster API operation.

ClusterIdentifier (string) --
The identifier of the cluster to be resumed.





Schedule (string) --
The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour.
Format of at expressions is "at(yyyy-mm-ddThh:mm:ss) ". For example, "at(2016-03-04T17:27:00) ".
Format of cron expressions is "cron(Minutes Hours Day-of-month Month Day-of-week Year) ". For example, "cron(0 10 ? * MON *) ". For more information, see Cron Expressions in the Amazon CloudWatch Events User Guide .

IamRole (string) --
The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see Using Identity-Based Policies for Amazon Redshift in the Amazon Redshift Cluster Management Guide .

ScheduledActionDescription (string) --
The description of the scheduled action.

State (string) --
The state of the scheduled action. For example, DISABLED .

NextInvocations (list) --
List of times when the scheduled action will run.

(datetime) --


StartTime (datetime) --
The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.

EndTime (datetime) --
The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.







Exceptions

Redshift.Client.exceptions.ScheduledActionAlreadyExistsFault
Redshift.Client.exceptions.ScheduledActionQuotaExceededFault
Redshift.Client.exceptions.ScheduledActionTypeUnsupportedFault
Redshift.Client.exceptions.InvalidScheduleFault
Redshift.Client.exceptions.InvalidScheduledActionFault
Redshift.Client.exceptions.UnauthorizedOperation


    :return: {
        'ScheduledActionName': 'string',
        'TargetAction': {
            'ResizeCluster': {
                'ClusterIdentifier': 'string',
                'ClusterType': 'string',
                'NodeType': 'string',
                'NumberOfNodes': 123,
                'Classic': True|False
            },
            'PauseCluster': {
                'ClusterIdentifier': 'string'
            },
            'ResumeCluster': {
                'ClusterIdentifier': 'string'
            }
        },
        'Schedule': 'string',
        'IamRole': 'string',
        'ScheduledActionDescription': 'string',
        'State': 'ACTIVE'|'DISABLED',
        'NextInvocations': [
            datetime(2015, 1, 1),
        ],
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (datetime) --
    
    """
    pass

def create_snapshot_copy_grant(SnapshotCopyGrantName=None, KmsKeyId=None, Tags=None):
    """
    Creates a snapshot copy grant that permits Amazon Redshift to use a customer master key (CMK) from AWS Key Management Service (AWS KMS) to encrypt copied snapshots in a destination region.
    For more information about managing snapshot copy grants, go to Amazon Redshift Database Encryption in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param SnapshotCopyGrantName: [REQUIRED]\nThe name of the snapshot copy grant. This name must be unique in the region for the AWS account.\nConstraints:\n\nMust contain from 1 to 63 alphanumeric characters or hyphens.\nAlphabetic characters must be lowercase.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\nMust be unique for all clusters within an AWS account.\n\n

    :type KmsKeyId: string
    :param KmsKeyId: The unique identifier of the customer master key (CMK) to which to grant Amazon Redshift permission. If no key is specified, the default key is used.

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

SnapshotCopyGrant (dict) --
The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots with the specified customer master key (CMK) from AWS KMS in the destination region.
For more information about managing snapshot copy grants, go to Amazon Redshift Database Encryption in the Amazon Redshift Cluster Management Guide .

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.

KmsKeyId (string) --
The unique identifier of the customer master key (CMK) in AWS KMS to which Amazon Redshift is granted permission.

Tags (list) --
A list of tag instances.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.SnapshotCopyGrantAlreadyExistsFault
Redshift.Client.exceptions.SnapshotCopyGrantQuotaExceededFault
Redshift.Client.exceptions.LimitExceededFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault
Redshift.Client.exceptions.DependentServiceRequestThrottlingFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.SnapshotCopyGrantAlreadyExistsFault
    Redshift.Client.exceptions.SnapshotCopyGrantQuotaExceededFault
    Redshift.Client.exceptions.LimitExceededFault
    Redshift.Client.exceptions.TagLimitExceededFault
    Redshift.Client.exceptions.InvalidTagFault
    Redshift.Client.exceptions.DependentServiceRequestThrottlingFault
    
    """
    pass

def create_snapshot_schedule(ScheduleDefinitions=None, ScheduleIdentifier=None, ScheduleDescription=None, Tags=None, DryRun=None, NextInvocations=None):
    """
    Create a snapshot schedule that can be associated to a cluster and which overrides the default system backup schedule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_snapshot_schedule(
        ScheduleDefinitions=[
            'string',
        ],
        ScheduleIdentifier='string',
        ScheduleDescription='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        DryRun=True|False,
        NextInvocations=123
    )
    
    
    :type ScheduleDefinitions: list
    :param ScheduleDefinitions: The definition of the snapshot schedule. The definition is made up of schedule expressions, for example 'cron(30 12 *)' or 'rate(12 hours)'.\n\n(string) --\n\n

    :type ScheduleIdentifier: string
    :param ScheduleIdentifier: A unique identifier for a snapshot schedule. Only alphanumeric characters are allowed for the identifier.

    :type ScheduleDescription: string
    :param ScheduleDescription: The description of the snapshot schedule.

    :type Tags: list
    :param Tags: An optional set of tags you can use to search for the schedule.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :type DryRun: boolean
    :param DryRun: 

    :type NextInvocations: integer
    :param NextInvocations: 

    :rtype: dict

ReturnsResponse Syntax
{
    'ScheduleDefinitions': [
        'string',
    ],
    'ScheduleIdentifier': 'string',
    'ScheduleDescription': 'string',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextInvocations': [
        datetime(2015, 1, 1),
    ],
    'AssociatedClusterCount': 123,
    'AssociatedClusters': [
        {
            'ClusterIdentifier': 'string',
            'ScheduleAssociationState': 'MODIFYING'|'ACTIVE'|'FAILED'
        },
    ]
}


Response Structure

(dict) --
Describes a snapshot schedule. You can set a regular interval for creating snapshots of a cluster. You can also schedule snapshots for specific dates.

ScheduleDefinitions (list) --
A list of ScheduleDefinitions.

(string) --


ScheduleIdentifier (string) --
A unique identifier for the schedule.

ScheduleDescription (string) --
The description of the schedule.

Tags (list) --
An optional set of tags describing the schedule.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





NextInvocations (list) --

(datetime) --


AssociatedClusterCount (integer) --
The number of clusters associated with the schedule.

AssociatedClusters (list) --
A list of clusters associated with the schedule. A maximum of 100 clusters is returned.

(dict) --
ClusterIdentifier (string) --
ScheduleAssociationState (string) --










Exceptions

Redshift.Client.exceptions.SnapshotScheduleAlreadyExistsFault
Redshift.Client.exceptions.InvalidScheduleFault
Redshift.Client.exceptions.SnapshotScheduleQuotaExceededFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.ScheduleDefinitionTypeUnsupportedFault


    :return: {
        'ScheduleDefinitions': [
            'string',
        ],
        'ScheduleIdentifier': 'string',
        'ScheduleDescription': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextInvocations': [
            datetime(2015, 1, 1),
        ],
        'AssociatedClusterCount': 123,
        'AssociatedClusters': [
            {
                'ClusterIdentifier': 'string',
                'ScheduleAssociationState': 'MODIFYING'|'ACTIVE'|'FAILED'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_tags(ResourceName=None, Tags=None):
    """
    Adds tags to a cluster.
    A resource can have up to 50 tags. If you try to create more than 50 tags for a resource, you will receive an error and the attempt will fail.
    If you specify a key that already exists for the resource, the value for that key will be updated with the new value.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ResourceName: [REQUIRED]\nThe Amazon Resource Name (ARN) to which you want to add the tag or tags. For example, arn:aws:redshift:us-east-2:123456789:cluster:t1 .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nOne or more name/value pairs to add as tags to the specified resource. Each tag name is passed in with the parameter Key and the corresponding value is passed in with the parameter Value . The Key and Value parameters are separated by a comma (,). Separate multiple tags with a space. For example, --tags 'Key'='owner','Value'='admin' 'Key'='environment','Value'='test' 'Key'='version','Value'='1.0' .\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :returns: 
    Redshift.Client.exceptions.TagLimitExceededFault
    Redshift.Client.exceptions.ResourceNotFoundFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def create_usage_limit(ClusterIdentifier=None, FeatureType=None, LimitType=None, Amount=None, Period=None, BreachAction=None, Tags=None):
    """
    Creates a usage limit for a specified Amazon Redshift feature on a cluster. The usage limit is identified by the returned usage limit identifier.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_usage_limit(
        ClusterIdentifier='string',
        FeatureType='spectrum'|'concurrency-scaling',
        LimitType='time'|'data-scanned',
        Amount=123,
        Period='daily'|'weekly'|'monthly',
        BreachAction='log'|'emit-metric'|'disable',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe identifier of the cluster that you want to limit usage.\n

    :type FeatureType: string
    :param FeatureType: [REQUIRED]\nThe Amazon Redshift feature that you want to limit.\n

    :type LimitType: string
    :param LimitType: [REQUIRED]\nThe type of limit. Depending on the feature type, this can be based on a time duration or data size. If FeatureType is spectrum , then LimitType must be data-scanned . If FeatureType is concurrency-scaling , then LimitType must be time .\n

    :type Amount: integer
    :param Amount: [REQUIRED]\nThe limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB). The value must be a positive number.\n

    :type Period: string
    :param Period: The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly .

    :type BreachAction: string
    :param BreachAction: The action that Amazon Redshift takes when the limit is reached. The default is log. For more information about this parameter, see UsageLimit .

    :type Tags: list
    :param Tags: A list of tag instances.\n\n(dict) --A tag consisting of a name/value pair for a resource.\n\nKey (string) --The key, or name, for the resource tag.\n\nValue (string) --The value for the resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UsageLimitId': 'string',
    'ClusterIdentifier': 'string',
    'FeatureType': 'spectrum'|'concurrency-scaling',
    'LimitType': 'time'|'data-scanned',
    'Amount': 123,
    'Period': 'daily'|'weekly'|'monthly',
    'BreachAction': 'log'|'emit-metric'|'disable',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Describes a usage limit object for a cluster.

UsageLimitId (string) --
The identifier of the usage limit.

ClusterIdentifier (string) --
The identifier of the cluster with a usage limit.

FeatureType (string) --
The Amazon Redshift feature to which the limit applies.

LimitType (string) --
The type of limit. Depending on the feature type, this can be based on a time duration or data size.

Amount (integer) --
The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB).

Period (string) --
The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly .

BreachAction (string) --
The action that Amazon Redshift takes when the limit is reached. Possible values are:

log - To log an event in a system table. The default is log.
emit-metric - To emit CloudWatch metrics.
disable - To disable the feature until the next usage period begins.


Tags (list) --
A list of tag instances.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.











Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.LimitExceededFault
Redshift.Client.exceptions.UsageLimitAlreadyExistsFault
Redshift.Client.exceptions.InvalidUsageLimitFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.UnsupportedOperationFault


    :return: {
        'UsageLimitId': 'string',
        'ClusterIdentifier': 'string',
        'FeatureType': 'spectrum'|'concurrency-scaling',
        'LimitType': 'time'|'data-scanned',
        'Amount': 123,
        'Period': 'daily'|'weekly'|'monthly',
        'BreachAction': 'log'|'emit-metric'|'disable',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    log - To log an event in a system table. The default is log.
    emit-metric - To emit CloudWatch metrics.
    disable - To disable the feature until the next usage period begins.
    
    """
    pass

def delete_cluster(ClusterIdentifier=None, SkipFinalClusterSnapshot=None, FinalClusterSnapshotIdentifier=None, FinalClusterSnapshotRetentionPeriod=None):
    """
    Deletes a previously provisioned cluster without its final snapshot being created. A successful response from the web service indicates that the request was received correctly. Use  DescribeClusters to monitor the status of the deletion. The delete operation cannot be canceled or reverted once submitted. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    If you want to shut down the cluster and retain it for future use, set SkipFinalClusterSnapshot to false and specify a name for FinalClusterSnapshotIdentifier . You can later restore this snapshot to resume using the cluster. If a final cluster snapshot is requested, the status of the cluster will be "final-snapshot" while the snapshot is being taken, then it\'s "deleting" once Amazon Redshift begins deleting the cluster.
    For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cluster(
        ClusterIdentifier='string',
        SkipFinalClusterSnapshot=True|False,
        FinalClusterSnapshotIdentifier='string',
        FinalClusterSnapshotRetentionPeriod=123
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe identifier of the cluster to be deleted.\nConstraints:\n\nMust contain lowercase characters.\nMust contain from 1 to 63 alphanumeric characters or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type SkipFinalClusterSnapshot: boolean
    :param SkipFinalClusterSnapshot: Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If true , a final cluster snapshot is not created. If false , a final cluster snapshot is created before the cluster is deleted.\n\nNote\nThe FinalClusterSnapshotIdentifier parameter must be specified if SkipFinalClusterSnapshot is false .\n\nDefault: false\n

    :type FinalClusterSnapshotIdentifier: string
    :param FinalClusterSnapshotIdentifier: The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, SkipFinalClusterSnapshot must be false .\nConstraints:\n\nMust be 1 to 255 alphanumeric characters.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type FinalClusterSnapshotRetentionPeriod: integer
    :param FinalClusterSnapshotRetentionPeriod: The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.\nThe value must be either -1 or an integer between 1 and 3,653.\nThe default value is -1.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.ClusterSnapshotAlreadyExistsFault
Redshift.Client.exceptions.ClusterSnapshotQuotaExceededFault
Redshift.Client.exceptions.InvalidRetentionPeriodFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
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
    
    Exceptions
    
    :example: response = client.delete_cluster_parameter_group(
        ParameterGroupName='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]\nThe name of the parameter group to be deleted.\nConstraints:\n\nMust be the name of an existing cluster parameter group.\nCannot delete a default cluster parameter group.\n\n

    :returns: 
    Redshift.Client.exceptions.InvalidClusterParameterGroupStateFault
    Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
    
    """
    pass

def delete_cluster_security_group(ClusterSecurityGroupName=None):
    """
    Deletes an Amazon Redshift security group.
    For information about managing security groups, go to Amazon Redshift Cluster Security Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cluster_security_group(
        ClusterSecurityGroupName='string'
    )
    
    
    :type ClusterSecurityGroupName: string
    :param ClusterSecurityGroupName: [REQUIRED]\nThe name of the cluster security group to be deleted.\n

    """
    pass

def delete_cluster_snapshot(SnapshotIdentifier=None, SnapshotClusterIdentifier=None):
    """
    Deletes the specified manual snapshot. The snapshot must be in the available state, with no other users authorized to access the snapshot.
    Unlike automated snapshots, manual snapshots are retained even after you delete your cluster. Amazon Redshift does not delete your manual snapshots. You must delete manual snapshot explicitly to avoid getting charged. If other accounts are authorized to access the snapshot, you must revoke all of the authorizations before you can delete the snapshot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cluster_snapshot(
        SnapshotIdentifier='string',
        SnapshotClusterIdentifier='string'
    )
    
    
    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]\nThe unique identifier of the manual snapshot to be deleted.\nConstraints: Must be the name of an existing snapshot that is in the available , failed , or cancelled state.\n

    :type SnapshotClusterIdentifier: string
    :param SnapshotClusterIdentifier: The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.\nConstraints: Must be the name of valid cluster.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'EnhancedVpcRouting': True|False,
        'MaintenanceTrackName': 'string',
        'ManualSnapshotRetentionPeriod': 123,
        'ManualSnapshotRemainingDays': 123,
        'SnapshotRetentionStartTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Snapshot (dict) --
Describes a snapshot.

SnapshotIdentifier (string) --
The snapshot identifier that is provided in the request.

ClusterIdentifier (string) --
The identifier of the cluster for which the snapshot was taken.

SnapshotCreateTime (datetime) --
The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.

Status (string) --
The snapshot status. The value of the status depends on the API operation used:

CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
DeleteClusterSnapshot returns status as "deleted".


Port (integer) --
The port that the cluster is listening on.

AvailabilityZone (string) --
The Availability Zone in which the cluster was created.

ClusterCreateTime (datetime) --
The time (UTC) when the cluster was originally created.

MasterUsername (string) --
The master user name for the cluster.

ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

SnapshotType (string) --
The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot are of type "manual".

NodeType (string) --
The node type of the nodes in the cluster.

NumberOfNodes (integer) --
The number of nodes in the cluster.

DBName (string) --
The name of the database that was created when the cluster was created.

VpcId (string) --
The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.

Encrypted (boolean) --
If true , the data in the snapshot is encrypted at rest.

KmsKeyId (string) --
The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.

EncryptedWithHSM (boolean) --
A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. true indicates that the data is encrypted using HSM keys.

AccountsWithRestoreAccess (list) --
A list of the AWS customer accounts authorized to restore the snapshot. Returns null if no accounts are authorized. Visible only to the snapshot owner.

(dict) --
Describes an AWS customer account authorized to restore a snapshot.

AccountId (string) --
The identifier of an AWS customer account authorized to restore a snapshot.

AccountAlias (string) --
The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is amazon-redshift-support .





OwnerAccount (string) --
For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.

TotalBackupSizeInMegaBytes (float) --
The size of the complete set of backup data that would be used to restore the cluster.

ActualIncrementalBackupSizeInMegaBytes (float) --
The size of the incremental backup.

BackupProgressInMegaBytes (float) --
The number of megabytes that have been transferred to the snapshot backup.

CurrentBackupRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred to the snapshot backup. Returns 0 for a completed backup.

EstimatedSecondsToCompletion (integer) --
The estimate of the time remaining before the snapshot backup will complete. Returns 0 for a completed backup.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.

SourceRegion (string) --
The source region from which the snapshot was copied.

Tags (list) --
The list of tags for the cluster snapshot.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





RestorableNodeTypes (list) --
The list of node types that this cluster snapshot is able to restore into.

(string) --


EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track for the snapshot.

ManualSnapshotRetentionPeriod (integer) --
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

ManualSnapshotRemainingDays (integer) --
The number of days until a manual snapshot will pass its retention period.

SnapshotRetentionStartTime (datetime) --
A timestamp representing the start of the retention period for the snapshot.









Exceptions

Redshift.Client.exceptions.InvalidClusterSnapshotStateFault
Redshift.Client.exceptions.ClusterSnapshotNotFoundFault


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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'ManualSnapshotRetentionPeriod': 123,
            'ManualSnapshotRemainingDays': 123,
            'SnapshotRetentionStartTime': datetime(2015, 1, 1)
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
    
    Exceptions
    
    :example: response = client.delete_cluster_subnet_group(
        ClusterSubnetGroupName='string'
    )
    
    
    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: [REQUIRED]\nThe name of the cluster subnet group name to be deleted.\n

    """
    pass

def delete_event_subscription(SubscriptionName=None):
    """
    Deletes an Amazon Redshift event notification subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_event_subscription(
        SubscriptionName='string'
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: [REQUIRED]\nThe name of the Amazon Redshift event notification subscription to be deleted.\n

    """
    pass

def delete_hsm_client_certificate(HsmClientCertificateIdentifier=None):
    """
    Deletes the specified HSM client certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_hsm_client_certificate(
        HsmClientCertificateIdentifier='string'
    )
    
    
    :type HsmClientCertificateIdentifier: string
    :param HsmClientCertificateIdentifier: [REQUIRED]\nThe identifier of the HSM client certificate to be deleted.\n

    """
    pass

def delete_hsm_configuration(HsmConfigurationIdentifier=None):
    """
    Deletes the specified Amazon Redshift HSM configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_hsm_configuration(
        HsmConfigurationIdentifier='string'
    )
    
    
    :type HsmConfigurationIdentifier: string
    :param HsmConfigurationIdentifier: [REQUIRED]\nThe identifier of the Amazon Redshift HSM configuration to be deleted.\n

    """
    pass

def delete_scheduled_action(ScheduledActionName=None):
    """
    Deletes a scheduled action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_scheduled_action(
        ScheduledActionName='string'
    )
    
    
    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]\nThe name of the scheduled action to delete.\n

    """
    pass

def delete_snapshot_copy_grant(SnapshotCopyGrantName=None):
    """
    Deletes the specified snapshot copy grant.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_snapshot_copy_grant(
        SnapshotCopyGrantName='string'
    )
    
    
    :type SnapshotCopyGrantName: string
    :param SnapshotCopyGrantName: [REQUIRED]\nThe name of the snapshot copy grant to delete.\n

    """
    pass

def delete_snapshot_schedule(ScheduleIdentifier=None):
    """
    Deletes a snapshot schedule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_snapshot_schedule(
        ScheduleIdentifier='string'
    )
    
    
    :type ScheduleIdentifier: string
    :param ScheduleIdentifier: [REQUIRED]\nA unique identifier of the snapshot schedule to delete.\n

    """
    pass

def delete_tags(ResourceName=None, TagKeys=None):
    """
    Deletes tags from a resource. You must provide the ARN of the resource from which you want to delete the tag or tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_tags(
        ResourceName='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceName: string
    :param ResourceName: [REQUIRED]\nThe Amazon Resource Name (ARN) from which you want to remove the tag or tags. For example, arn:aws:redshift:us-east-2:123456789:cluster:t1 .\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag key that you want to delete.\n\n(string) --\n\n

    :returns: 
    Redshift.Client.exceptions.ResourceNotFoundFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def delete_usage_limit(UsageLimitId=None):
    """
    Deletes a usage limit from a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_usage_limit(
        UsageLimitId='string'
    )
    
    
    :type UsageLimitId: string
    :param UsageLimitId: [REQUIRED]\nThe identifier of the usage limit to delete.\n

    """
    pass

def describe_account_attributes(AttributeNames=None):
    """
    Returns a list of attributes attached to an account
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_attributes(
        AttributeNames=[
            'string',
        ]
    )
    
    
    :type AttributeNames: list
    :param AttributeNames: A list of attribute names.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'AccountAttributes': [
        {
            'AttributeName': 'string',
            'AttributeValues': [
                {
                    'AttributeValue': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
AccountAttributes (list) --A list of attributes assigned to an account.

(dict) --A name value pair that describes an aspect of an account.

AttributeName (string) --The name of the attribute.

AttributeValues (list) --A list of attribute values.

(dict) --Describes an attribute value.

AttributeValue (string) --The value of the attribute.















    :return: {
        'AccountAttributes': [
            {
                'AttributeName': 'string',
                'AttributeValues': [
                    {
                        'AttributeValue': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_cluster_db_revisions(ClusterIdentifier=None, MaxRecords=None, Marker=None):
    """
    Returns an array of ClusterDbRevision objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_cluster_db_revisions(
        ClusterIdentifier='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: A unique identifier for a cluster whose ClusterDbRevisions you are requesting. This parameter is case sensitive. All clusters defined for an account are returned by default.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in the marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the marker parameter and retrying the request.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point for returning a set of response records. When the results of a DescribeClusterDbRevisions request exceed the value specified in MaxRecords , Amazon Redshift returns a value in the marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the marker parameter and retrying the request.\nConstraints: You can specify either the ClusterIdentifier parameter, or the marker parameter, but not both.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ClusterDbRevisions': [
        {
            'ClusterIdentifier': 'string',
            'CurrentDatabaseRevision': 'string',
            'DatabaseRevisionReleaseDate': datetime(2015, 1, 1),
            'RevisionTargets': [
                {
                    'DatabaseRevision': 'string',
                    'Description': 'string',
                    'DatabaseRevisionReleaseDate': datetime(2015, 1, 1)
                },
            ]
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
A string representing the starting point for the next set of revisions. If a value is returned in a response, you can retrieve the next set of revisions by providing the value in the marker parameter and retrying the command. If the marker field is empty, all revisions have already been returned.

ClusterDbRevisions (list) --
A list of revisions.

(dict) --
Describes a ClusterDbRevision .

ClusterIdentifier (string) --
The unique identifier of the cluster.

CurrentDatabaseRevision (string) --
A string representing the current cluster version.

DatabaseRevisionReleaseDate (datetime) --
The date on which the database revision was released.

RevisionTargets (list) --
A list of RevisionTarget objects, where each object describes the database revision that a cluster can be updated to.

(dict) --
Describes a RevisionTarget .

DatabaseRevision (string) --
A unique string that identifies the version to update the cluster to. You can use this value in  ModifyClusterDbRevision .

Description (string) --
A string that describes the changes and features that will be applied to the cluster when it is updated to the corresponding  ClusterDbRevision .

DatabaseRevisionReleaseDate (datetime) --
The date on which the database revision was released.















Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.InvalidClusterStateFault


    :return: {
        'Marker': 'string',
        'ClusterDbRevisions': [
            {
                'ClusterIdentifier': 'string',
                'CurrentDatabaseRevision': 'string',
                'DatabaseRevisionReleaseDate': datetime(2015, 1, 1),
                'RevisionTargets': [
                    {
                        'DatabaseRevision': 'string',
                        'Description': 'string',
                        'DatabaseRevisionReleaseDate': datetime(2015, 1, 1)
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterNotFoundFault
    Redshift.Client.exceptions.InvalidClusterStateFault
    
    """
    pass

def describe_cluster_parameter_groups(ParameterGroupName=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns a list of Amazon Redshift parameter groups, including parameter groups you created and the default parameter group. For each parameter group, the response includes the parameter group name, description, and parameter group family name. You can optionally specify a name to retrieve the description of a specific parameter group.
    For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all parameter groups that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all parameter groups that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, parameter groups are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterParameterGroups request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching cluster parameter groups that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching cluster parameter groups that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the output from the  DescribeClusterParameterGroups action.

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

ParameterGroups (list) --
A list of  ClusterParameterGroup instances. Each instance describes one cluster parameter group.

(dict) --
Describes a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterGroupFamily (string) --
The name of the cluster parameter group family that this cluster parameter group is compatible with.

Description (string) --
The description of the parameter group.

Tags (list) --
The list of tags for the cluster parameter group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.















Exceptions

Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def describe_cluster_parameters(ParameterGroupName=None, Source=None, MaxRecords=None, Marker=None):
    """
    Returns a detailed list of parameters contained within the specified Amazon Redshift parameter group. For each parameter the response includes information such as parameter name, description, data type, value, whether the parameter value is modifiable, and so on.
    You can specify source filter to retrieve parameters of only specific type. For example, to retrieve parameters that were modified by a user action such as from  ModifyClusterParameterGroup , you can specify source equal to user .
    For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_cluster_parameters(
        ParameterGroupName='string',
        Source='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ParameterGroupName: string
    :param ParameterGroupName: [REQUIRED]\nThe name of a cluster parameter group for which to return details.\n

    :type Source: string
    :param Source: The parameter types to return. Specify user to show parameters that are different form the default. Similarly, specify engine-default to show parameters that are the same as the default parameter group.\nDefault: All parameter types returned.\nValid Values: user | engine-default\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterParameters request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the output from the  DescribeClusterParameters action.

Parameters (list) --
A list of  Parameter instances. Each instance lists the parameters of one cluster parameter group.

(dict) --
Describes a parameter in a cluster parameter group.

ParameterName (string) --
The name of the parameter.

ParameterValue (string) --
The value of the parameter.

Description (string) --
A description of the parameter.

Source (string) --
The source of the parameter value, such as "engine-default" or "user".

DataType (string) --
The data type of the parameter.

AllowedValues (string) --
The valid range of values for the parameter.

ApplyType (string) --
Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

IsModifiable (boolean) --
If true , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion (string) --
The earliest engine version to which the parameter can apply.





Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.







Exceptions

Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
    
    """
    pass

def describe_cluster_security_groups(ClusterSecurityGroupName=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns information about Amazon Redshift security groups. If the name of a security group is specified, the response will contain only information about only that security group.
    For information about managing security groups, go to Amazon Redshift Cluster Security Groups in the Amazon Redshift Cluster Management Guide .
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all security groups that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all security groups that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, security groups are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ClusterSecurityGroupName: The name of a cluster security group for which you are requesting details. You can specify either the Marker parameter or a ClusterSecurityGroupName parameter, but not both.\nExample: securitygroup1\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterSecurityGroups request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.\nConstraints: You can specify either the ClusterSecurityGroupName parameter or the Marker parameter, but not both.\n

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching cluster security groups that are associated with the specified key or keys. For example, suppose that you have security groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching cluster security groups that are associated with the specified tag value or values. For example, suppose that you have security groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

ClusterSecurityGroups (list) --
A list of  ClusterSecurityGroup instances.

(dict) --
Describes a security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group to which the operation was applied.

Description (string) --
A description of the security group.

EC2SecurityGroups (list) --
A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.

(dict) --
Describes an Amazon EC2 security group.

Status (string) --
The status of the EC2 security group.

EC2SecurityGroupName (string) --
The name of the EC2 Security Group.

EC2SecurityGroupOwnerId (string) --
The AWS ID of the owner of the EC2 security group specified in the EC2SecurityGroupName field.

Tags (list) --
The list of tags for the EC2 security group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.









IPRanges (list) --
A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.

(dict) --
Describes an IP range used in a security group.

Status (string) --
The status of the IP range, for example, "authorized".

CIDRIP (string) --
The IP range in Classless Inter-Domain Routing (CIDR) notation.

Tags (list) --
The list of tags for the IP range.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.









Tags (list) --
The list of tags for the cluster security group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.















Exceptions

Redshift.Client.exceptions.ClusterSecurityGroupNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterSecurityGroupNotFoundFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def describe_cluster_snapshots(ClusterIdentifier=None, SnapshotIdentifier=None, SnapshotType=None, StartTime=None, EndTime=None, MaxRecords=None, Marker=None, OwnerAccount=None, TagKeys=None, TagValues=None, ClusterExists=None, SortingEntities=None):
    """
    Returns one or more snapshot objects, which contain metadata about your cluster snapshots. By default, this operation returns information about all snapshots of all clusters that are owned by you AWS customer account. No information is returned for snapshots owned by inactive AWS customer accounts.
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all snapshots that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all snapshots that have any combination of those values are returned. Only snapshots that you own are returned in the response; shared snapshots are not returned with the tag key and tag value request parameters.
    If both tag keys and values are omitted from the request, snapshots are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    Exceptions
    
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
        ],
        ClusterExists=True|False,
        SortingEntities=[
            {
                'Attribute': 'SOURCE_TYPE'|'TOTAL_SIZE'|'CREATE_TIME',
                'SortOrder': 'ASC'|'DESC'
            },
        ]
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: The identifier of the cluster which generated the requested snapshots.

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: The snapshot identifier of the snapshot about which to return information.

    :type SnapshotType: string
    :param SnapshotType: The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.\nValid Values: automated | manual\n

    :type StartTime: datetime
    :param StartTime: A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.\nExample: 2012-07-16T18:00:00Z\n

    :type EndTime: datetime
    :param EndTime: A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.\nExample: 2012-07-16T18:00:00Z\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterSnapshots request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type OwnerAccount: string
    :param OwnerAccount: The AWS customer account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your AWS customer account, or do not specify the parameter.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :type ClusterExists: boolean
    :param ClusterExists: A value that indicates whether to return snapshots only for an existing cluster. You can perform table-level restore only by using a snapshot of an existing cluster, that is, a cluster that has not been deleted. Values for this parameter work as follows:\n\nIf ClusterExists is set to true , ClusterIdentifier is required.\nIf ClusterExists is set to false and ClusterIdentifier isn\'t specified, all snapshots associated with deleted clusters (orphaned snapshots) are returned.\nIf ClusterExists is set to false and ClusterIdentifier is specified for a deleted cluster, snapshots associated with that cluster are returned.\nIf ClusterExists is set to false and ClusterIdentifier is specified for an existing cluster, no snapshots are returned.\n\n

    :type SortingEntities: list
    :param SortingEntities: \n(dict) --Describes a sorting entity\n\nAttribute (string) -- [REQUIRED]The category for sorting the snapshots.\n\nSortOrder (string) --The order for listing the attributes.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'ManualSnapshotRetentionPeriod': 123,
            'ManualSnapshotRemainingDays': 123,
            'SnapshotRetentionStartTime': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --
Contains the output from the  DescribeClusterSnapshots action.

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

Snapshots (list) --
A list of  Snapshot instances.

(dict) --
Describes a snapshot.

SnapshotIdentifier (string) --
The snapshot identifier that is provided in the request.

ClusterIdentifier (string) --
The identifier of the cluster for which the snapshot was taken.

SnapshotCreateTime (datetime) --
The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.

Status (string) --
The snapshot status. The value of the status depends on the API operation used:

CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
DeleteClusterSnapshot returns status as "deleted".


Port (integer) --
The port that the cluster is listening on.

AvailabilityZone (string) --
The Availability Zone in which the cluster was created.

ClusterCreateTime (datetime) --
The time (UTC) when the cluster was originally created.

MasterUsername (string) --
The master user name for the cluster.

ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

SnapshotType (string) --
The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot are of type "manual".

NodeType (string) --
The node type of the nodes in the cluster.

NumberOfNodes (integer) --
The number of nodes in the cluster.

DBName (string) --
The name of the database that was created when the cluster was created.

VpcId (string) --
The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.

Encrypted (boolean) --
If true , the data in the snapshot is encrypted at rest.

KmsKeyId (string) --
The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.

EncryptedWithHSM (boolean) --
A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. true indicates that the data is encrypted using HSM keys.

AccountsWithRestoreAccess (list) --
A list of the AWS customer accounts authorized to restore the snapshot. Returns null if no accounts are authorized. Visible only to the snapshot owner.

(dict) --
Describes an AWS customer account authorized to restore a snapshot.

AccountId (string) --
The identifier of an AWS customer account authorized to restore a snapshot.

AccountAlias (string) --
The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is amazon-redshift-support .





OwnerAccount (string) --
For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.

TotalBackupSizeInMegaBytes (float) --
The size of the complete set of backup data that would be used to restore the cluster.

ActualIncrementalBackupSizeInMegaBytes (float) --
The size of the incremental backup.

BackupProgressInMegaBytes (float) --
The number of megabytes that have been transferred to the snapshot backup.

CurrentBackupRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred to the snapshot backup. Returns 0 for a completed backup.

EstimatedSecondsToCompletion (integer) --
The estimate of the time remaining before the snapshot backup will complete. Returns 0 for a completed backup.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.

SourceRegion (string) --
The source region from which the snapshot was copied.

Tags (list) --
The list of tags for the cluster snapshot.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





RestorableNodeTypes (list) --
The list of node types that this cluster snapshot is able to restore into.

(string) --


EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track for the snapshot.

ManualSnapshotRetentionPeriod (integer) --
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

ManualSnapshotRemainingDays (integer) --
The number of days until a manual snapshot will pass its retention period.

SnapshotRetentionStartTime (datetime) --
A timestamp representing the start of the retention period for the snapshot.











Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.ClusterSnapshotNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'ManualSnapshotRetentionPeriod': 123,
                'ManualSnapshotRemainingDays': 123,
                'SnapshotRetentionStartTime': datetime(2015, 1, 1)
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
    
    Exceptions
    
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
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterSubnetGroups request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching cluster subnet groups that are associated with the specified key or keys. For example, suppose that you have subnet groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching cluster subnet groups that are associated with the specified tag value or values. For example, suppose that you have subnet groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                        'Name': 'string',
                        'SupportedPlatforms': [
                            {
                                'Name': 'string'
                            },
                        ]
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


Response Structure

(dict) --
Contains the output from the  DescribeClusterSubnetGroups action.

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

ClusterSubnetGroups (list) --
A list of  ClusterSubnetGroup instances.

(dict) --
Describes a subnet group.

ClusterSubnetGroupName (string) --
The name of the cluster subnet group.

Description (string) --
The description of the cluster subnet group.

VpcId (string) --
The VPC ID of the cluster subnet group.

SubnetGroupStatus (string) --
The status of the cluster subnet group. Possible values are Complete , Incomplete and Invalid .

Subnets (list) --
A list of the VPC  Subnet elements.

(dict) --
Describes a subnet.

SubnetIdentifier (string) --
The identifier of the subnet.

SubnetAvailabilityZone (dict) --

Name (string) --
The name of the availability zone.

SupportedPlatforms (list) --

(dict) --
A list of supported platforms for orderable clusters.

Name (string) --






SubnetStatus (string) --
The status of the subnet.





Tags (list) --
The list of tags for the cluster subnet group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.















Exceptions

Redshift.Client.exceptions.ClusterSubnetGroupNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


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
                            'Name': 'string',
                            'SupportedPlatforms': [
                                {
                                    'Name': 'string'
                                },
                            ]
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
    
    
    :returns: 
    Name (string) --
    
    """
    pass

def describe_cluster_tracks(MaintenanceTrackName=None, MaxRecords=None, Marker=None):
    """
    Returns a list of all the available maintenance tracks.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_cluster_tracks(
        MaintenanceTrackName='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type MaintenanceTrackName: string
    :param MaintenanceTrackName: The name of the maintenance track.

    :type MaxRecords: integer
    :param MaxRecords: An integer value for the maximum number of maintenance tracks to return.

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterTracks request exceed the value specified in MaxRecords , Amazon Redshift returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'MaintenanceTracks': [
        {
            'MaintenanceTrackName': 'string',
            'DatabaseVersion': 'string',
            'UpdateTargets': [
                {
                    'MaintenanceTrackName': 'string',
                    'DatabaseVersion': 'string',
                    'SupportedOperations': [
                        {
                            'OperationName': 'string'
                        },
                    ]
                },
            ]
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

MaintenanceTracks (list) --
A list of maintenance tracks output by the DescribeClusterTracks operation.

(dict) --
Defines a maintenance track that determines which Amazon Redshift version to apply during a maintenance window. If the value for MaintenanceTrack is current , the cluster is updated to the most recently certified maintenance release. If the value is trailing , the cluster is updated to the previously certified maintenance release.

MaintenanceTrackName (string) --
The name of the maintenance track. Possible values are current and trailing .

DatabaseVersion (string) --
The version number for the cluster release.

UpdateTargets (list) --
An array of  UpdateTarget objects to update with the maintenance track.

(dict) --
A maintenance track that you can switch the current track to.

MaintenanceTrackName (string) --
The name of the new maintenance track.

DatabaseVersion (string) --
The cluster version for the new maintenance track.

SupportedOperations (list) --
A list of operations supported by the maintenance track.

(dict) --
Describes the operations that are allowed on a maintenance track.

OperationName (string) --
A list of the supported operations.













Marker (string) --
The starting point to return a set of response tracklist records. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.







Exceptions

Redshift.Client.exceptions.InvalidClusterTrackFault
Redshift.Client.exceptions.UnauthorizedOperation


    :return: {
        'MaintenanceTracks': [
            {
                'MaintenanceTrackName': 'string',
                'DatabaseVersion': 'string',
                'UpdateTargets': [
                    {
                        'MaintenanceTrackName': 'string',
                        'DatabaseVersion': 'string',
                        'SupportedOperations': [
                            {
                                'OperationName': 'string'
                            },
                        ]
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Redshift.Client.exceptions.InvalidClusterTrackFault
    Redshift.Client.exceptions.UnauthorizedOperation
    
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
    :param ClusterVersion: The specific cluster version to return.\nExample: 1.0\n

    :type ClusterParameterGroupFamily: string
    :param ClusterParameterGroupFamily: The name of a specific cluster parameter group family to return details for.\nConstraints:\n\nMust be 1 to 255 alphanumeric characters\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusterVersions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ClusterVersions': [
        {
            'ClusterVersion': 'string',
            'ClusterParameterGroupFamily': 'string',
            'Description': 'string'
        },
    ]
}


Response Structure

(dict) --
Contains the output from the  DescribeClusterVersions action.

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

ClusterVersions (list) --
A list of Version elements.

(dict) --
Describes a cluster version, including the parameter group family and description of the version.

ClusterVersion (string) --
The version number used by the cluster.

ClusterParameterGroupFamily (string) --
The name of the cluster parameter group family for the cluster.

Description (string) --
The description of the cluster version.












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
    
    Exceptions
    
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
    :param ClusterIdentifier: The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.\nThe default is that all clusters defined for an account are returned.\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeClusters request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.\nConstraints: You can specify either the ClusterIdentifier parameter or the Marker parameter, but not both.\n

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Clusters': [
        {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        },
    ]
}


Response Structure

(dict) --
Contains the output from the  DescribeClusters action.

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

Clusters (list) --
A list of Cluster objects, where each object describes one cluster.

(dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.













Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


    :return: {
        'Marker': 'string',
        'Clusters': [
            {
                'ClusterIdentifier': 'string',
                'NodeType': 'string',
                'ClusterStatus': 'string',
                'ClusterAvailabilityStatus': 'string',
                'ModifyStatus': 'string',
                'MasterUsername': 'string',
                'DBName': 'string',
                'Endpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ClusterCreateTime': datetime(2015, 1, 1),
                'AutomatedSnapshotRetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
                    'EnhancedVpcRouting': True|False,
                    'MaintenanceTrackName': 'string',
                    'EncryptionType': 'string'
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
                'DataTransferProgress': {
                    'Status': 'string',
                    'CurrentRateInMegaBytesPerSecond': 123.0,
                    'TotalDataInMegaBytes': 123,
                    'DataTransferredInMegaBytes': 123,
                    'EstimatedTimeToCompletionInSeconds': 123,
                    'ElapsedTimeInSeconds': 123
                },
                'HsmStatus': {
                    'HsmClientCertificateIdentifier': 'string',
                    'HsmConfigurationIdentifier': 'string',
                    'Status': 'string'
                },
                'ClusterSnapshotCopyStatus': {
                    'DestinationRegion': 'string',
                    'RetentionPeriod': 123,
                    'ManualSnapshotRetentionPeriod': 123,
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
                ],
                'PendingActions': [
                    'string',
                ],
                'MaintenanceTrackName': 'string',
                'ElasticResizeNumberOfNodeOptions': 'string',
                'DeferredMaintenanceWindows': [
                    {
                        'DeferMaintenanceIdentifier': 'string',
                        'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                        'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                    },
                ],
                'SnapshotScheduleIdentifier': 'string',
                'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
                'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
                'ExpectedNextSnapshotScheduleTimeStatus': 'string',
                'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
                'ResizeInfo': {
                    'ResizeType': 'string',
                    'AllowCancelResize': True|False
                }
            },
        ]
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
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
    :param ParameterGroupFamily: [REQUIRED]\nThe name of the cluster parameter group family.\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeDefaultClusterParameters request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

DefaultClusterParameters (dict) --
Describes the default cluster parameters for a parameter group family.

ParameterGroupFamily (string) --
The name of the cluster parameter group family to which the engine default parameters apply.

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

Parameters (list) --
The list of cluster default parameters.

(dict) --
Describes a parameter in a cluster parameter group.

ParameterName (string) --
The name of the parameter.

ParameterValue (string) --
The value of the parameter.

Description (string) --
A description of the parameter.

Source (string) --
The source of the parameter value, such as "engine-default" or "user".

DataType (string) --
The data type of the parameter.

AllowedValues (string) --
The valid range of values for the parameter.

ApplyType (string) --
Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

IsModifiable (boolean) --
If true , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion (string) --
The earliest engine version to which the parameter can apply.














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
    :param SourceType: The source type, such as cluster or parameter group, to which the described event categories apply.\nValid values: cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, and scheduled-action.\n

    :rtype: dict
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

def describe_event_subscriptions(SubscriptionName=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Lists descriptions of all the Amazon Redshift event notification subscriptions for a customer account. If you specify a subscription name, lists the description for that subscription.
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all event notification subscriptions that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all subscriptions that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, subscriptions are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_subscriptions(
        SubscriptionName='string',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type SubscriptionName: string
    :param SubscriptionName: The name of the Amazon Redshift event notification subscription to be described.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEventSubscriptions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching event notification subscriptions that are associated with the specified key or keys. For example, suppose that you have subscriptions that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching event notification subscriptions that are associated with the specified tag value or values. For example, suppose that you have subscriptions that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag values associated with them.\n\n(string) --\n\n

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


Response Structure

(dict) --

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

EventSubscriptionsList (list) --
A list of event subscriptions.

(dict) --
Describes event subscriptions.

CustomerAwsId (string) --
The AWS customer account associated with the Amazon Redshift event notification subscription.

CustSubscriptionId (string) --
The name of the Amazon Redshift event notification subscription.

SnsTopicArn (string) --
The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.

Status (string) --
The status of the Amazon Redshift event notification subscription.
Constraints:

Can be one of the following: active | no-permission | topic-not-exist
The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.


SubscriptionCreationTime (datetime) --
The date and time the Amazon Redshift event notification subscription was created.

SourceType (string) --
The source type of the events returned by the Amazon Redshift event notification, such as cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, or scheduled-action.

SourceIdsList (list) --
A list of the sources that publish events to the Amazon Redshift event notification subscription.

(string) --


EventCategoriesList (list) --
The list of Amazon Redshift event categories specified in the event notification subscription.
Values: Configuration, Management, Monitoring, Security

(string) --


Severity (string) --
The event severity specified in the Amazon Redshift event notification subscription.
Values: ERROR, INFO

Enabled (boolean) --
A boolean value indicating whether the subscription is enabled; true indicates that the subscription is enabled.

Tags (list) --
The list of tags for the event subscription.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.















Exceptions

Redshift.Client.exceptions.SubscriptionNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


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
        SourceType='cluster'|'cluster-parameter-group'|'cluster-security-group'|'cluster-snapshot'|'scheduled-action',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Duration=123,
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type SourceIdentifier: string
    :param SourceIdentifier: The identifier of the event source for which events will be returned. If this parameter is not specified, then all sources are included in the response.\nConstraints:\nIf SourceIdentifier is supplied, SourceType must also be provided.\n\nSpecify a cluster identifier when SourceType is cluster .\nSpecify a cluster security group name when SourceType is cluster-security-group .\nSpecify a cluster parameter group name when SourceType is cluster-parameter-group .\nSpecify a cluster snapshot identifier when SourceType is cluster-snapshot .\n\n

    :type SourceType: string
    :param SourceType: The event source to retrieve events for. If no value is specified, all events are returned.\nConstraints:\nIf SourceType is supplied, SourceIdentifier must also be provided.\n\nSpecify cluster when SourceIdentifier is a cluster identifier.\nSpecify cluster-security-group when SourceIdentifier is a cluster security group name.\nSpecify cluster-parameter-group when SourceIdentifier is a cluster parameter group name.\nSpecify cluster-snapshot when SourceIdentifier is a cluster snapshot identifier.\n\n

    :type StartTime: datetime
    :param StartTime: The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.\nExample: 2009-07-08T18:00Z\n

    :type EndTime: datetime
    :param EndTime: The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the ISO8601 Wikipedia page.\nExample: 2009-07-08T18:00Z\n

    :type Duration: integer
    :param Duration: The number of minutes prior to the time of the request for which to retrieve events. For example, if the request is sent at 18:00 and you specify a duration of 60, then only events which have occurred after 17:00 will be returned.\nDefault: 60\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEvents request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Events': [
        {
            'SourceIdentifier': 'string',
            'SourceType': 'cluster'|'cluster-parameter-group'|'cluster-security-group'|'cluster-snapshot'|'scheduled-action',
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


Response Structure

(dict) --

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

Events (list) --
A list of Event instances.

(dict) --
Describes an event.

SourceIdentifier (string) --
The identifier for the source of the event.

SourceType (string) --
The source type for this event.

Message (string) --
The text of this event.

EventCategories (list) --
A list of the event categories.
Values: Configuration, Management, Monitoring, Security

(string) --


Severity (string) --
The severity of the event.
Values: ERROR, INFO

Date (datetime) --
The date and time of the event.

EventId (string) --
The identifier of the event.












    :return: {
        'Marker': 'string',
        'Events': [
            {
                'SourceIdentifier': 'string',
                'SourceType': 'cluster'|'cluster-parameter-group'|'cluster-security-group'|'cluster-snapshot'|'scheduled-action',
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
    
    Exceptions
    
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
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeHsmClientCertificates request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching HSM client certificates that are associated with the specified key or keys. For example, suppose that you have HSM client certificates that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching HSM client certificates that are associated with the specified tag value or values. For example, suppose that you have HSM client certificates that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

HsmClientCertificates (list) --
A list of the identifiers for one or more HSM client certificates used by Amazon Redshift clusters to store and retrieve database encryption keys in an HSM.

(dict) --
Returns information about an HSM client certificate. The certificate is stored in a secure Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data files.

HsmClientCertificateIdentifier (string) --
The identifier of the HSM client certificate.

HsmClientCertificatePublicKey (string) --
The public key that the Amazon Redshift cluster will use to connect to the HSM. You must register the public key in the HSM.

Tags (list) --
The list of tags for the HSM client certificate.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.















Exceptions

Redshift.Client.exceptions.HsmClientCertificateNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.HsmClientCertificateNotFoundFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def describe_hsm_configurations(HsmConfigurationIdentifier=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns information about the specified Amazon Redshift HSM configuration. If no configuration ID is specified, returns information about all the HSM configurations owned by your AWS customer account.
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM connections that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all HSM connections that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, HSM connections are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeHsmConfigurations request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching HSM configurations that are associated with the specified key or keys. For example, suppose that you have HSM configurations that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching HSM configurations that are associated with the specified tag value or values. For example, suppose that you have HSM configurations that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

HsmConfigurations (list) --
A list of HsmConfiguration objects.

(dict) --
Returns information about an HSM configuration, which is an object that describes to Amazon Redshift clusters the information they require to connect to an HSM where they can store database encryption keys.

HsmConfigurationIdentifier (string) --
The name of the Amazon Redshift HSM configuration.

Description (string) --
A text description of the HSM configuration.

HsmIpAddress (string) --
The IP address that the Amazon Redshift cluster must use to access the HSM.

HsmPartitionName (string) --
The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.

Tags (list) --
The list of tags for the HSM configuration.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.















Exceptions

Redshift.Client.exceptions.HsmConfigurationNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.HsmConfigurationNotFoundFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def describe_logging_status(ClusterIdentifier=None):
    """
    Describes whether information, such as queries and connection attempts, is being logged for the specified Amazon Redshift cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_logging_status(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe identifier of the cluster from which to get the logging status.\nExample: examplecluster\n

    :rtype: dict
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






Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault


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

def describe_node_configuration_options(ActionType=None, ClusterIdentifier=None, SnapshotIdentifier=None, OwnerAccount=None, Filters=None, Marker=None, MaxRecords=None):
    """
    Returns properties of possible node configurations such as node type, number of nodes, and disk usage for the specified action type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_node_configuration_options(
        ActionType='restore-cluster'|'recommend-node-config'|'resize-cluster',
        ClusterIdentifier='string',
        SnapshotIdentifier='string',
        OwnerAccount='string',
        Filters=[
            {
                'Name': 'NodeType'|'NumberOfNodes'|'EstimatedDiskUtilizationPercent'|'Mode',
                'Operator': 'eq'|'lt'|'gt'|'le'|'ge'|'in'|'between',
                'Values': [
                    'string',
                ]
            },
        ],
        Marker='string',
        MaxRecords=123
    )
    
    
    :type ActionType: string
    :param ActionType: [REQUIRED]\nThe action type to evaluate for possible node configurations. Specify 'restore-cluster' to get configuration combinations based on an existing snapshot. Specify 'recommend-node-config' to get configuration recommendations based on an existing cluster or snapshot. Specify 'resize-cluster' to get configuration combinations for elastic resize based on an existing cluster.\n

    :type ClusterIdentifier: string
    :param ClusterIdentifier: The identifier of the cluster to evaluate for possible node configurations.

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: The identifier of the snapshot to evaluate for possible node configurations.

    :type OwnerAccount: string
    :param OwnerAccount: The AWS customer account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

    :type Filters: list
    :param Filters: A set of name, operator, and value items to filter the results.\n\n(dict) --A set of elements to filter the returned node configurations.\n\nName (string) --The name of the element to filter.\n\nOperator (string) --The filter operator. If filter Name is NodeType only the \'in\' operator is supported. Provide one value to evaluate for \'eq\', \'lt\', \'le\', \'gt\', and \'ge\'. Provide two values to evaluate for \'between\'. Provide a list of values for \'in\'.\n\nValues (list) --List of values. Compare Name using Operator to Values. If filter Name is NumberOfNodes, then values can range from 0 to 200. If filter Name is EstimatedDiskUtilizationPercent, then values can range from 0 to 100. For example, filter NumberOfNodes (name) GT (operator) 3 (values).\n\n(string) --\n\n\n\n\n\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeNodeConfigurationOptions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 500\nConstraints: minimum 100, maximum 500.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NodeConfigurationOptionList': [
        {
            'NodeType': 'string',
            'NumberOfNodes': 123,
            'EstimatedDiskUtilizationPercent': 123.0,
            'Mode': 'standard'|'high-performance'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

NodeConfigurationOptionList (list) --
A list of valid node configurations.

(dict) --
A list of node configurations.

NodeType (string) --
The node type, such as, "ds2.8xlarge".

NumberOfNodes (integer) --
The number of nodes.

EstimatedDiskUtilizationPercent (float) --
The estimated disk utilizaton percentage.

Mode (string) --
The category of the node configuration recommendation.





Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.







Exceptions

Redshift.Client.exceptions.ClusterSnapshotNotFoundFault
Redshift.Client.exceptions.InvalidClusterSnapshotStateFault
Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.AccessToSnapshotDeniedFault


    :return: {
        'NodeConfigurationOptionList': [
            {
                'NodeType': 'string',
                'NumberOfNodes': 123,
                'EstimatedDiskUtilizationPercent': 123.0,
                'Mode': 'standard'|'high-performance'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterSnapshotNotFoundFault
    Redshift.Client.exceptions.InvalidClusterSnapshotStateFault
    Redshift.Client.exceptions.ClusterNotFoundFault
    Redshift.Client.exceptions.AccessToSnapshotDeniedFault
    
    """
    pass

def describe_orderable_cluster_options(ClusterVersion=None, NodeType=None, MaxRecords=None, Marker=None):
    """
    Returns a list of orderable cluster options. Before you create a new cluster you can use this operation to find what options are available, such as the EC2 Availability Zones (AZ) in the specific AWS Region that you can specify, and the node types you can request. The node types differ by available storage, memory, CPU and price. With the cost involved you might want to obtain a list of cluster options in the specific region and specify values when creating a cluster. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_orderable_cluster_options(
        ClusterVersion='string',
        NodeType='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ClusterVersion: string
    :param ClusterVersion: The version filter value. Specify this parameter to show only the available offerings matching the specified version.\nDefault: All versions.\nConstraints: Must be one of the version returned from DescribeClusterVersions .\n

    :type NodeType: string
    :param NodeType: The node type filter value. Specify this parameter to show only the available offerings matching the specified node type.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeOrderableClusterOptions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'OrderableClusterOptions': [
        {
            'ClusterVersion': 'string',
            'ClusterType': 'string',
            'NodeType': 'string',
            'AvailabilityZones': [
                {
                    'Name': 'string',
                    'SupportedPlatforms': [
                        {
                            'Name': 'string'
                        },
                    ]
                },
            ]
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
Contains the output from the  DescribeOrderableClusterOptions action.

OrderableClusterOptions (list) --
An OrderableClusterOption structure containing information about orderable options for the cluster.

(dict) --
Describes an orderable cluster option.

ClusterVersion (string) --
The version of the orderable cluster.

ClusterType (string) --
The cluster type, for example multi-node .

NodeType (string) --
The node type for the orderable cluster.

AvailabilityZones (list) --
A list of availability zones for the orderable cluster.

(dict) --
Describes an availability zone.

Name (string) --
The name of the availability zone.

SupportedPlatforms (list) --

(dict) --
A list of supported platforms for orderable clusters.

Name (string) --












Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.








    :return: {
        'OrderableClusterOptions': [
            {
                'ClusterVersion': 'string',
                'ClusterType': 'string',
                'NodeType': 'string',
                'AvailabilityZones': [
                    {
                        'Name': 'string',
                        'SupportedPlatforms': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    Name (string) --
    
    """
    pass

def describe_reserved_node_offerings(ReservedNodeOfferingId=None, MaxRecords=None, Marker=None):
    """
    Returns a list of the available reserved node offerings by Amazon Redshift with their descriptions including the node type, the fixed and recurring costs of reserving the node and duration the node will be reserved for you. These descriptions help you determine which reserve node offering you want to purchase. You then use the unique offering ID in you call to  PurchaseReservedNodeOffering to reserve one or more nodes for your Amazon Redshift cluster.
    For more information about reserved node offerings, go to Purchasing Reserved Nodes in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_reserved_node_offerings(
        ReservedNodeOfferingId='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReservedNodeOfferingId: string
    :param ReservedNodeOfferingId: The unique identifier for the offering.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeReservedNodeOfferings request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict

ReturnsResponse Syntax
{
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
            ],
            'ReservedNodeOfferingType': 'Regular'|'Upgradable'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

ReservedNodeOfferings (list) --
A list of ReservedNodeOffering objects.

(dict) --
Describes a reserved node offering.

ReservedNodeOfferingId (string) --
The offering identifier.

NodeType (string) --
The node type offered by the reserved node offering.

Duration (integer) --
The duration, in seconds, for which the offering will reserve the node.

FixedPrice (float) --
The upfront fixed charge you will pay to purchase the specific reserved node offering.

UsagePrice (float) --
The rate you are charged for each hour the cluster that is using the offering is running.

CurrencyCode (string) --
The currency code for the compute nodes offering.

OfferingType (string) --
The anticipated utilization of the reserved node, as defined in the reserved node offering.

RecurringCharges (list) --
The charge to your account regardless of whether you are creating any clusters using the node offering. Recurring charges are only in effect for heavy-utilization reserved nodes.

(dict) --
Describes a recurring charge.

RecurringChargeAmount (float) --
The amount charged per the period of time specified by the recurring charge frequency.

RecurringChargeFrequency (string) --
The frequency at which the recurring charge amount is applied.





ReservedNodeOfferingType (string) --











Exceptions

Redshift.Client.exceptions.ReservedNodeOfferingNotFoundFault
Redshift.Client.exceptions.UnsupportedOperationFault
Redshift.Client.exceptions.DependentServiceUnavailableFault


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
                ],
                'ReservedNodeOfferingType': 'Regular'|'Upgradable'
            },
        ]
    }
    
    
    :returns: 
    Redshift.Client.exceptions.ReservedNodeOfferingNotFoundFault
    Redshift.Client.exceptions.UnsupportedOperationFault
    Redshift.Client.exceptions.DependentServiceUnavailableFault
    
    """
    pass

def describe_reserved_nodes(ReservedNodeId=None, MaxRecords=None, Marker=None):
    """
    Returns the descriptions of the reserved nodes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_reserved_nodes(
        ReservedNodeId='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReservedNodeId: string
    :param ReservedNodeId: Identifier for the node reservation.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeReservedNodes request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :rtype: dict

ReturnsResponse Syntax
{
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
            ],
            'ReservedNodeOfferingType': 'Regular'|'Upgradable'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.

ReservedNodes (list) --
The list of ReservedNode objects.

(dict) --
Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the available reserved node offerings.

ReservedNodeId (string) --
The unique identifier for the reservation.

ReservedNodeOfferingId (string) --
The identifier for the reserved node offering.

NodeType (string) --
The node type of the reserved node.

StartTime (datetime) --
The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.

Duration (integer) --
The duration of the node reservation in seconds.

FixedPrice (float) --
The fixed cost Amazon Redshift charges you for this reserved node.

UsagePrice (float) --
The hourly rate Amazon Redshift charges you for this reserved node.

CurrencyCode (string) --
The currency code for the reserved cluster.

NodeCount (integer) --
The number of reserved compute nodes.

State (string) --
The state of the reserved compute node.
Possible Values:

pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
active-This reserved node is owned by the caller and is available for use.
payment-failed-Payment failed for the purchase attempt.
retired-The reserved node is no longer available.
exchanging-The owner is exchanging the reserved node for another reserved node.


OfferingType (string) --
The anticipated utilization of the reserved node, as defined in the reserved node offering.

RecurringCharges (list) --
The recurring charges for the reserved node.

(dict) --
Describes a recurring charge.

RecurringChargeAmount (float) --
The amount charged per the period of time specified by the recurring charge frequency.

RecurringChargeFrequency (string) --
The frequency at which the recurring charge amount is applied.





ReservedNodeOfferingType (string) --











Exceptions

Redshift.Client.exceptions.ReservedNodeNotFoundFault
Redshift.Client.exceptions.DependentServiceUnavailableFault


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
                ],
                'ReservedNodeOfferingType': 'Regular'|'Upgradable'
            },
        ]
    }
    
    
    :returns: 
    pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
    active-This reserved node is owned by the caller and is available for use.
    payment-failed-Payment failed for the purchase attempt.
    retired-The reserved node is no longer available.
    exchanging-The owner is exchanging the reserved node for another reserved node.
    
    """
    pass

def describe_resize(ClusterIdentifier=None):
    """
    Returns information about the last resize operation for the specified cluster. If no resize operation has ever been initiated for the specified cluster, a HTTP 404 error is returned. If a resize operation was initiated and completed, the status of the resize remains as SUCCEEDED until the next resize.
    A resize operation can be requested using  ModifyCluster and specifying a different number or type of nodes for the cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_resize(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier of a cluster whose resize progress you are requesting. This parameter is case-sensitive.\nBy default, resize operations for all clusters defined for an AWS account are returned.\n

    :rtype: dict
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
    'EstimatedTimeToCompletionInSeconds': 123,
    'ResizeType': 'string',
    'Message': 'string',
    'TargetEncryptionType': 'string',
    'DataTransferProgressPercent': 123.0
}


Response Structure

(dict) --Describes the result of a cluster resize operation.

TargetNodeType (string) --The node type that the cluster will have after the resize operation is complete.

TargetNumberOfNodes (integer) --The number of nodes that the cluster will have after the resize operation is complete.

TargetClusterType (string) --The cluster type after the resize operation is complete.
Valid Values: multi-node | single-node

Status (string) --The status of the resize operation.
Valid Values: NONE | IN_PROGRESS | FAILED | SUCCEEDED | CANCELLING

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

ResizeType (string) --An enum with possible values of ClassicResize and ElasticResize . These values describe the type of resize operation being performed.

Message (string) --An optional string to provide additional details about the resize action.

TargetEncryptionType (string) --The type of encryption for the cluster after the resize is complete.
Possible values are KMS and None . In the China region possible values are: Legacy and None .

DataTransferProgressPercent (float) --The percent of data transferred from source cluster to target cluster.






Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.ResizeNotFoundFault


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
        'EstimatedTimeToCompletionInSeconds': 123,
        'ResizeType': 'string',
        'Message': 'string',
        'TargetEncryptionType': 'string',
        'DataTransferProgressPercent': 123.0
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_scheduled_actions(ScheduledActionName=None, TargetActionType=None, StartTime=None, EndTime=None, Active=None, Filters=None, Marker=None, MaxRecords=None):
    """
    Describes properties of scheduled actions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_scheduled_actions(
        ScheduledActionName='string',
        TargetActionType='ResizeCluster'|'PauseCluster'|'ResumeCluster',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Active=True|False,
        Filters=[
            {
                'Name': 'cluster-identifier'|'iam-role',
                'Values': [
                    'string',
                ]
            },
        ],
        Marker='string',
        MaxRecords=123
    )
    
    
    :type ScheduledActionName: string
    :param ScheduledActionName: The name of the scheduled action to retrieve.

    :type TargetActionType: string
    :param TargetActionType: The type of the scheduled actions to retrieve.

    :type StartTime: datetime
    :param StartTime: The start time in UTC of the scheduled actions to retrieve. Only active scheduled actions that have invocations after this time are retrieved.

    :type EndTime: datetime
    :param EndTime: The end time in UTC of the scheduled action to retrieve. Only active scheduled actions that have invocations before this time are retrieved.

    :type Active: boolean
    :param Active: If true, retrieve only active scheduled actions. If false, retrieve only disabled scheduled actions.

    :type Filters: list
    :param Filters: List of scheduled action filters.\n\n(dict) --A set of elements to filter the returned scheduled actions.\n\nName (string) -- [REQUIRED]The type of element to filter.\n\nValues (list) -- [REQUIRED]List of values. Compare if the value (of type defined by Name ) equals an item in the list of scheduled actions.\n\n(string) --\n\n\n\n\n\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeScheduledActions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'ScheduledActions': [
        {
            'ScheduledActionName': 'string',
            'TargetAction': {
                'ResizeCluster': {
                    'ClusterIdentifier': 'string',
                    'ClusterType': 'string',
                    'NodeType': 'string',
                    'NumberOfNodes': 123,
                    'Classic': True|False
                },
                'PauseCluster': {
                    'ClusterIdentifier': 'string'
                },
                'ResumeCluster': {
                    'ClusterIdentifier': 'string'
                }
            },
            'Schedule': 'string',
            'IamRole': 'string',
            'ScheduledActionDescription': 'string',
            'State': 'ACTIVE'|'DISABLED',
            'NextInvocations': [
                datetime(2015, 1, 1),
            ],
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeScheduledActions request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

ScheduledActions (list) --
List of retrieved scheduled actions.

(dict) --
Describes a scheduled action. You can use a scheduled action to trigger some Amazon Redshift API operations on a schedule. For information about which API operations can be scheduled, see  ScheduledActionType .

ScheduledActionName (string) --
The name of the scheduled action.

TargetAction (dict) --
A JSON format string of the Amazon Redshift API operation with input parameters.
"{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}} ".

ResizeCluster (dict) --
An action that runs a ResizeCluster API operation.

ClusterIdentifier (string) --
The unique identifier for the cluster to resize.

ClusterType (string) --
The new cluster type for the specified cluster.

NodeType (string) --
The new node type for the nodes you are adding. If not specified, the cluster\'s current node type is used.

NumberOfNodes (integer) --
The new number of nodes for the cluster.

Classic (boolean) --
A boolean value indicating whether the resize operation is using the classic resize process. If you don\'t provide this parameter or set the value to false , the resize type is elastic.



PauseCluster (dict) --
An action that runs a PauseCluster API operation.

ClusterIdentifier (string) --
The identifier of the cluster to be paused.



ResumeCluster (dict) --
An action that runs a ResumeCluster API operation.

ClusterIdentifier (string) --
The identifier of the cluster to be resumed.





Schedule (string) --
The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour.
Format of at expressions is "at(yyyy-mm-ddThh:mm:ss) ". For example, "at(2016-03-04T17:27:00) ".
Format of cron expressions is "cron(Minutes Hours Day-of-month Month Day-of-week Year) ". For example, "cron(0 10 ? * MON *) ". For more information, see Cron Expressions in the Amazon CloudWatch Events User Guide .

IamRole (string) --
The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see Using Identity-Based Policies for Amazon Redshift in the Amazon Redshift Cluster Management Guide .

ScheduledActionDescription (string) --
The description of the scheduled action.

State (string) --
The state of the scheduled action. For example, DISABLED .

NextInvocations (list) --
List of times when the scheduled action will run.

(datetime) --


StartTime (datetime) --
The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.

EndTime (datetime) --
The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.











Exceptions

Redshift.Client.exceptions.ScheduledActionNotFoundFault
Redshift.Client.exceptions.UnauthorizedOperation


    :return: {
        'Marker': 'string',
        'ScheduledActions': [
            {
                'ScheduledActionName': 'string',
                'TargetAction': {
                    'ResizeCluster': {
                        'ClusterIdentifier': 'string',
                        'ClusterType': 'string',
                        'NodeType': 'string',
                        'NumberOfNodes': 123,
                        'Classic': True|False
                    },
                    'PauseCluster': {
                        'ClusterIdentifier': 'string'
                    },
                    'ResumeCluster': {
                        'ClusterIdentifier': 'string'
                    }
                },
                'Schedule': 'string',
                'IamRole': 'string',
                'ScheduledActionDescription': 'string',
                'State': 'ACTIVE'|'DISABLED',
                'NextInvocations': [
                    datetime(2015, 1, 1),
                ],
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (datetime) --
    
    """
    pass

def describe_snapshot_copy_grants(SnapshotCopyGrantName=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns a list of snapshot copy grants owned by the AWS account in the destination region.
    For more information about managing snapshot copy grants, go to Amazon Redshift Database Encryption in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeSnapshotCopyGrant request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.\nConstraints: You can specify either the SnapshotCopyGrantName parameter or the Marker parameter, but not both.\n

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Marker (string) --
An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeSnapshotCopyGrant request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
Constraints: You can specify either the SnapshotCopyGrantName parameter or the Marker parameter, but not both.

SnapshotCopyGrants (list) --
The list of SnapshotCopyGrant objects.

(dict) --
The snapshot copy grant that grants Amazon Redshift permission to encrypt copied snapshots with the specified customer master key (CMK) from AWS KMS in the destination region.
For more information about managing snapshot copy grants, go to Amazon Redshift Database Encryption in the Amazon Redshift Cluster Management Guide .

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.

KmsKeyId (string) --
The unique identifier of the customer master key (CMK) in AWS KMS to which Amazon Redshift is granted permission.

Tags (list) --
A list of tag instances.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.















Exceptions

Redshift.Client.exceptions.SnapshotCopyGrantNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.SnapshotCopyGrantNotFoundFault
    Redshift.Client.exceptions.InvalidTagFault
    
    """
    pass

def describe_snapshot_schedules(ClusterIdentifier=None, ScheduleIdentifier=None, TagKeys=None, TagValues=None, Marker=None, MaxRecords=None):
    """
    Returns a list of snapshot schedules.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_snapshot_schedules(
        ClusterIdentifier='string',
        ScheduleIdentifier='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ],
        Marker='string',
        MaxRecords=123
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: The unique identifier for the cluster whose snapshot schedules you want to view.

    :type ScheduleIdentifier: string
    :param ScheduleIdentifier: A unique identifier for a snapshot schedule.

    :type TagKeys: list
    :param TagKeys: The key value for a snapshot schedule tag.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: The value corresponding to the key of the snapshot schedule tag.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the marker parameter and retrying the command. If the marker field is empty, all response records have been retrieved for the request.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.

    :rtype: dict

ReturnsResponse Syntax
{
    'SnapshotSchedules': [
        {
            'ScheduleDefinitions': [
                'string',
            ],
            'ScheduleIdentifier': 'string',
            'ScheduleDescription': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'NextInvocations': [
                datetime(2015, 1, 1),
            ],
            'AssociatedClusterCount': 123,
            'AssociatedClusters': [
                {
                    'ClusterIdentifier': 'string',
                    'ScheduleAssociationState': 'MODIFYING'|'ACTIVE'|'FAILED'
                },
            ]
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

SnapshotSchedules (list) --
A list of SnapshotSchedules.

(dict) --
Describes a snapshot schedule. You can set a regular interval for creating snapshots of a cluster. You can also schedule snapshots for specific dates.

ScheduleDefinitions (list) --
A list of ScheduleDefinitions.

(string) --


ScheduleIdentifier (string) --
A unique identifier for the schedule.

ScheduleDescription (string) --
The description of the schedule.

Tags (list) --
An optional set of tags describing the schedule.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





NextInvocations (list) --

(datetime) --


AssociatedClusterCount (integer) --
The number of clusters associated with the schedule.

AssociatedClusters (list) --
A list of clusters associated with the schedule. A maximum of 100 clusters is returned.

(dict) --
ClusterIdentifier (string) --
ScheduleAssociationState (string) --








Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the marker parameter and retrying the command. If the marker field is empty, all response records have been retrieved for the request.








    :return: {
        'SnapshotSchedules': [
            {
                'ScheduleDefinitions': [
                    'string',
                ],
                'ScheduleIdentifier': 'string',
                'ScheduleDescription': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'NextInvocations': [
                    datetime(2015, 1, 1),
                ],
                'AssociatedClusterCount': 123,
                'AssociatedClusters': [
                    {
                        'ClusterIdentifier': 'string',
                        'ScheduleAssociationState': 'MODIFYING'|'ACTIVE'|'FAILED'
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_storage():
    """
    Returns account level backups storage size and provisional storage.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_storage()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'TotalBackupSizeInMegaBytes': 123.0,
    'TotalProvisionedStorageInMegaBytes': 123.0
}


Response Structure

(dict) --
TotalBackupSizeInMegaBytes (float) --The total amount of storage currently used for snapshots.

TotalProvisionedStorageInMegaBytes (float) --The total amount of storage currently provisioned.







    :return: {
        'TotalBackupSizeInMegaBytes': 123.0,
        'TotalProvisionedStorageInMegaBytes': 123.0
    }
    
    
    """
    pass

def describe_table_restore_status(ClusterIdentifier=None, TableRestoreRequestId=None, MaxRecords=None, Marker=None):
    """
    Lists the status of one or more table restore requests made using the  RestoreTableFromClusterSnapshot API action. If you don\'t specify a value for the TableRestoreRequestId parameter, then DescribeTableRestoreStatus returns the status of all table restore requests ordered by the date and time of the request in ascending order. Otherwise DescribeTableRestoreStatus returns the status of the table specified by TableRestoreRequestId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_table_restore_status(
        ClusterIdentifier='string',
        TableRestoreRequestId='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: The Amazon Redshift cluster that the table is being restored to.

    :type TableRestoreRequestId: string
    :param TableRestoreRequestId: The identifier of the table restore request to return status for. If you don\'t specify a TableRestoreRequestId value, then DescribeTableRestoreStatus returns the status of all in-progress table restore requests.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.

    :type Marker: string
    :param Marker: An optional pagination token provided by a previous DescribeTableRestoreStatus request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the MaxRecords parameter.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

TableRestoreStatusDetails (list) --
A list of status details for one or more table restore requests.

(dict) --
Describes the status of a  RestoreTableFromClusterSnapshot operation.

TableRestoreRequestId (string) --
The unique identifier for the table restore request.

Status (string) --
A value that describes the current state of the table restore request.
Valid Values: SUCCEEDED , FAILED , CANCELED , PENDING , IN_PROGRESS

Message (string) --
A description of the status of the table restore request. Status values include SUCCEEDED , FAILED , CANCELED , PENDING , IN_PROGRESS .

RequestTime (datetime) --
The time that the table restore request was made, in Universal Coordinated Time (UTC).

ProgressInMegaBytes (integer) --
The amount of data restored to the new table so far, in megabytes (MB).

TotalDataInMegaBytes (integer) --
The total amount of data to restore to the new table, in megabytes (MB).

ClusterIdentifier (string) --
The identifier of the Amazon Redshift cluster that the table is being restored to.

SnapshotIdentifier (string) --
The identifier of the snapshot that the table is being restored from.

SourceDatabaseName (string) --
The name of the source database that contains the table being restored.

SourceSchemaName (string) --
The name of the source schema that contains the table being restored.

SourceTableName (string) --
The name of the source table being restored.

TargetDatabaseName (string) --
The name of the database to restore the table to.

TargetSchemaName (string) --
The name of the schema to restore the table to.

NewTableName (string) --
The name of the table to create as a result of the table restore request.





Marker (string) --
A pagination token that can be used in a subsequent  DescribeTableRestoreStatus request.







Exceptions

Redshift.Client.exceptions.TableRestoreNotFoundFault
Redshift.Client.exceptions.ClusterNotFoundFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.TableRestoreNotFoundFault
    Redshift.Client.exceptions.ClusterNotFoundFault
    
    """
    pass

def describe_tags(ResourceName=None, ResourceType=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Returns a list of tags. You can return tags from a specific resource by specifying an ARN, or you can return all tags for a given type of resource, such as clusters, snapshots, and so on.
    The following are limitations for DescribeTags :
    If you specify both tag keys and tag values in the same request, Amazon Redshift returns all resources that match any combination of the specified keys and values. For example, if you have owner and environment for tag keys, and admin and test for tag values, all resources that have any combination of those values are returned.
    If both tag keys and values are omitted from the request, resources are returned regardless of whether they have tag keys or values associated with them.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ResourceName: The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, arn:aws:redshift:us-east-2:123456789:cluster:t1 .

    :type ResourceType: string
    :param ResourceType: The type of resource with which you want to view tags. Valid resource types are:\n\nCluster\nCIDR/IP\nEC2 security group\nSnapshot\nCluster security group\nSubnet group\nHSM connection\nHSM certificate\nParameter group\nSnapshot copy grant\n\nFor more information about Amazon Redshift resource types and constructing ARNs, go to Specifying Policy Elements: Actions, Effects, Resources, and Principals in the Amazon Redshift Cluster Management Guide.\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.

    :type Marker: string
    :param Marker: A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the marker parameter and retrying the command. If the marker field is empty, all response records have been retrieved for the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

TaggedResources (list) --
A list of tags with their associated resources.

(dict) --
A tag and its associated resource.

Tag (dict) --
The tag for the resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.



ResourceName (string) --
The Amazon Resource Name (ARN) with which the tag is associated, for example: arn:aws:redshift:us-east-2:123456789:cluster:t1 .

ResourceType (string) --
The type of resource with which the tag is associated. Valid resource types are:

Cluster
CIDR/IP
EC2 security group
Snapshot
Cluster security group
Subnet group
HSM connection
HSM certificate
Parameter group

For more information about Amazon Redshift resource types and constructing ARNs, go to Constructing an Amazon Redshift Amazon Resource Name (ARN) in the Amazon Redshift Cluster Management Guide.





Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.







Exceptions

Redshift.Client.exceptions.ResourceNotFoundFault
Redshift.Client.exceptions.InvalidTagFault


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
    ResourceName (string) -- The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, arn:aws:redshift:us-east-2:123456789:cluster:t1 .
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
    
    For more information about Amazon Redshift resource types and constructing ARNs, go to Specifying Policy Elements: Actions, Effects, Resources, and Principals in the Amazon Redshift Cluster Management Guide.
    
    MaxRecords (integer) -- The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
    Marker (string) -- A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the marker parameter and retrying the command. If the marker field is empty, all response records have been retrieved for the request.
    TagKeys (list) -- A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
    
    (string) --
    
    
    TagValues (list) -- A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
    
    (string) --
    
    
    
    """
    pass

def describe_usage_limits(UsageLimitId=None, ClusterIdentifier=None, FeatureType=None, MaxRecords=None, Marker=None, TagKeys=None, TagValues=None):
    """
    Shows usage limits on a cluster. Results are filtered based on the combination of input usage limit identifier, cluster identifier, and feature type parameters:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_usage_limits(
        UsageLimitId='string',
        ClusterIdentifier='string',
        FeatureType='spectrum'|'concurrency-scaling',
        MaxRecords=123,
        Marker='string',
        TagKeys=[
            'string',
        ],
        TagValues=[
            'string',
        ]
    )
    
    
    :type UsageLimitId: string
    :param UsageLimitId: The identifier of the usage limit to describe.

    :type ClusterIdentifier: string
    :param ClusterIdentifier: The identifier of the cluster for which you want to describe usage limits.

    :type FeatureType: string
    :param FeatureType: The feature type for which you want to describe usage limits.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.\nDefault: 100\nConstraints: minimum 20, maximum 100.\n

    :type Marker: string
    :param Marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeUsageLimits request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.

    :type TagKeys: list
    :param TagKeys: A tag key or keys for which you want to return all matching usage limit objects that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the usage limit objects have either or both of these tag keys associated with them.\n\n(string) --\n\n

    :type TagValues: list
    :param TagValues: A tag value or values for which you want to return all matching usage limit objects that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the usage limit objects that have either or both of these tag values associated with them.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UsageLimits': [
        {
            'UsageLimitId': 'string',
            'ClusterIdentifier': 'string',
            'FeatureType': 'spectrum'|'concurrency-scaling',
            'LimitType': 'time'|'data-scanned',
            'Amount': 123,
            'Period': 'daily'|'weekly'|'monthly',
            'BreachAction': 'log'|'emit-metric'|'disable',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

UsageLimits (list) --
Contains the output from the  DescribeUsageLimits action.

(dict) --
Describes a usage limit object for a cluster.

UsageLimitId (string) --
The identifier of the usage limit.

ClusterIdentifier (string) --
The identifier of the cluster with a usage limit.

FeatureType (string) --
The Amazon Redshift feature to which the limit applies.

LimitType (string) --
The type of limit. Depending on the feature type, this can be based on a time duration or data size.

Amount (integer) --
The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB).

Period (string) --
The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly .

BreachAction (string) --
The action that Amazon Redshift takes when the limit is reached. Possible values are:

log - To log an event in a system table. The default is log.
emit-metric - To emit CloudWatch metrics.
disable - To disable the feature until the next usage period begins.


Tags (list) --
A list of tag instances.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.









Marker (string) --
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the Marker parameter and retrying the command. If the Marker field is empty, all response records have been retrieved for the request.







Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.UnsupportedOperationFault


    :return: {
        'UsageLimits': [
            {
                'UsageLimitId': 'string',
                'ClusterIdentifier': 'string',
                'FeatureType': 'spectrum'|'concurrency-scaling',
                'LimitType': 'time'|'data-scanned',
                'Amount': 123,
                'Period': 'daily'|'weekly'|'monthly',
                'BreachAction': 'log'|'emit-metric'|'disable',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    UsageLimitId (string) -- The identifier of the usage limit to describe.
    ClusterIdentifier (string) -- The identifier of the cluster for which you want to describe usage limits.
    FeatureType (string) -- The feature type for which you want to describe usage limits.
    MaxRecords (integer) -- The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
    Default: 100
    Constraints: minimum 20, maximum 100.
    
    Marker (string) -- An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeUsageLimits request exceed the value specified in MaxRecords , AWS returns a value in the Marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the Marker parameter and retrying the request.
    TagKeys (list) -- A tag key or keys for which you want to return all matching usage limit objects that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called owner and environment . If you specify both of these tag keys in the request, Amazon Redshift returns a response with the usage limit objects have either or both of these tag keys associated with them.
    
    (string) --
    
    
    TagValues (list) -- A tag value or values for which you want to return all matching usage limit objects that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called admin and test . If you specify both of these tag values in the request, Amazon Redshift returns a response with the usage limit objects that have either or both of these tag values associated with them.
    
    (string) --
    
    
    
    """
    pass

def disable_logging(ClusterIdentifier=None):
    """
    Stops logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_logging(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe identifier of the cluster on which logging is to be stopped.\nExample: examplecluster\n

    :rtype: dict
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






Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault


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
    
    Exceptions
    
    :example: response = client.disable_snapshot_copy(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier of the source cluster that you want to disable copying of snapshots to a destination region.\nConstraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --
Cluster (dict) --Describes a cluster.

ClusterIdentifier (string) --The unique identifier of the cluster.

NodeType (string) --The node type for the nodes in the cluster.

ClusterStatus (string) --The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --The connection endpoint.

Address (string) --The DNS address of the Cluster.

Port (integer) --The port that the database engine is listening on.



ClusterCreateTime (datetime) --The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

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

NodeType (string) --The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --The pending or in-progress change of the cluster type.

ClusterVersion (string) --The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --
Status (string) --Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

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

ApplyStatus (string) --A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --Describes a group of DeferredMaintenanceWindow objects.

(dict) --Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --Returns the value ClassicResize .

AllowCancelResize (boolean) --A boolean value indicating if the resize operation can be cancelled.










Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.SnapshotCopyAlreadyDisabledFault
Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.UnauthorizedOperation


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    Available - The cluster is available for queries.
    Unavailable - The cluster is not available for queries.
    Maintenance - The cluster is intermittently available for queries due to maintenance activities.
    Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
    Failed - The cluster failed and is not available for queries.
    
    """
    pass

def enable_logging(ClusterIdentifier=None, BucketName=None, S3KeyPrefix=None):
    """
    Starts logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_logging(
        ClusterIdentifier='string',
        BucketName='string',
        S3KeyPrefix='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe identifier of the cluster on which logging is to be started.\nExample: examplecluster\n

    :type BucketName: string
    :param BucketName: [REQUIRED]\nThe name of an existing S3 bucket where the log files are to be stored.\nConstraints:\n\nMust be in the same region as the cluster\nThe cluster must have read bucket and put object permissions\n\n

    :type S3KeyPrefix: string
    :param S3KeyPrefix: The prefix applied to the log file names.\nConstraints:\n\nCannot exceed 512 characters\nCannot contain spaces( ), double quotes ('), single quotes (\'), a backslash (), or control characters. The hexadecimal codes for invalid characters are:\nx00 to x20\nx22\nx27\nx5c\nx7f or larger\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LoggingEnabled': True|False,
    'BucketName': 'string',
    'S3KeyPrefix': 'string',
    'LastSuccessfulDeliveryTime': datetime(2015, 1, 1),
    'LastFailureTime': datetime(2015, 1, 1),
    'LastFailureMessage': 'string'
}


Response Structure

(dict) --
Describes the status of logging for a cluster.

LoggingEnabled (boolean) --

true if logging is on, false if logging is off.


BucketName (string) --
The name of the S3 bucket where the log files are stored.

S3KeyPrefix (string) --
The prefix applied to the log file names.

LastSuccessfulDeliveryTime (datetime) --
The last time that logs were delivered.

LastFailureTime (datetime) --
The last time when logs failed to be delivered.

LastFailureMessage (string) --
The message indicating that logs failed to be delivered.







Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.BucketNotFoundFault
Redshift.Client.exceptions.InsufficientS3BucketPolicyFault
Redshift.Client.exceptions.InvalidS3KeyPrefixFault
Redshift.Client.exceptions.InvalidS3BucketNameFault
Redshift.Client.exceptions.InvalidClusterStateFault


    :return: {
        'LoggingEnabled': True|False,
        'BucketName': 'string',
        'S3KeyPrefix': 'string',
        'LastSuccessfulDeliveryTime': datetime(2015, 1, 1),
        'LastFailureTime': datetime(2015, 1, 1),
        'LastFailureMessage': 'string'
    }
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterNotFoundFault
    Redshift.Client.exceptions.BucketNotFoundFault
    Redshift.Client.exceptions.InsufficientS3BucketPolicyFault
    Redshift.Client.exceptions.InvalidS3KeyPrefixFault
    Redshift.Client.exceptions.InvalidS3BucketNameFault
    Redshift.Client.exceptions.InvalidClusterStateFault
    
    """
    pass

def enable_snapshot_copy(ClusterIdentifier=None, DestinationRegion=None, RetentionPeriod=None, SnapshotCopyGrantName=None, ManualSnapshotRetentionPeriod=None):
    """
    Enables the automatic copy of snapshots from one region to another region for a specified cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_snapshot_copy(
        ClusterIdentifier='string',
        DestinationRegion='string',
        RetentionPeriod=123,
        SnapshotCopyGrantName='string',
        ManualSnapshotRetentionPeriod=123
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier of the source cluster to copy snapshots from.\nConstraints: Must be the valid name of an existing cluster that does not already have cross-region snapshot copy enabled.\n

    :type DestinationRegion: string
    :param DestinationRegion: [REQUIRED]\nThe destination AWS Region that you want to copy snapshots to.\nConstraints: Must be the name of a valid AWS Region. For more information, see Regions and Endpoints in the Amazon Web Services General Reference.\n

    :type RetentionPeriod: integer
    :param RetentionPeriod: The number of days to retain automated snapshots in the destination region after they are copied from the source region.\nDefault: 7.\nConstraints: Must be at least 1 and no more than 35.\n

    :type SnapshotCopyGrantName: string
    :param SnapshotCopyGrantName: The name of the snapshot copy grant to use when snapshots of an AWS KMS-encrypted cluster are copied to the destination region.

    :type ManualSnapshotRetentionPeriod: integer
    :param ManualSnapshotRetentionPeriod: The number of days to retain newly copied snapshots in the destination AWS Region after they are copied from the source AWS Region. If the value is -1, the manual snapshot is retained indefinitely.\nThe value must be either -1 or an integer between 1 and 3,653.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.IncompatibleOrderableOptions
Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.CopyToRegionDisabledFault
Redshift.Client.exceptions.SnapshotCopyAlreadyEnabledFault
Redshift.Client.exceptions.UnknownSnapshotCopyRegionFault
Redshift.Client.exceptions.UnauthorizedOperation
Redshift.Client.exceptions.SnapshotCopyGrantNotFoundFault
Redshift.Client.exceptions.LimitExceededFault
Redshift.Client.exceptions.DependentServiceRequestThrottlingFault
Redshift.Client.exceptions.InvalidRetentionPeriodFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
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
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_cluster_credentials(DbUser=None, DbName=None, ClusterIdentifier=None, DurationSeconds=None, AutoCreate=None, DbGroups=None):
    """
    Returns a database user name and temporary password with temporary authorization to log on to an Amazon Redshift database. The action returns the database user name prefixed with IAM: if AutoCreate is False or IAMA: if AutoCreate is True . You can optionally specify one or more database user groups that the user will join at log on. By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes). For more information, see Using IAM Authentication to Generate Database User Credentials in the Amazon Redshift Cluster Management Guide.
    The AWS Identity and Access Management (IAM)user or role that executes GetClusterCredentials must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see Resource Policies for GetClusterCredentials in the Amazon Redshift Cluster Management Guide.
    If the DbGroups parameter is specified, the IAM policy must allow the redshift:JoinGroup action with access to the listed dbgroups .
    In addition, if the AutoCreate parameter is set to True , then the policy must include the redshift:CreateClusterUser privilege.
    If the DbName parameter is specified, the IAM policy must allow access to the resource dbname for the specified database name.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DbUser: [REQUIRED]\nThe name of a database user. If a user name matching DbUser exists in the database, the temporary user credentials have the same permissions as the existing user. If DbUser doesn\'t exist in the database and Autocreate is True , a new user is created using the value for DbUser with PUBLIC permissions. If a database user matching the value for DbUser doesn\'t exist and Autocreate is False , then the command succeeds but the connection attempt will fail because the user doesn\'t exist in the database.\nFor more information, see CREATE USER in the Amazon Redshift Database Developer Guide.\nConstraints:\n\nMust be 1 to 64 alphanumeric characters or hyphens. The user name can\'t be PUBLIC .\nMust contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.\nFirst character must be a letter.\nMust not contain a colon ( : ) or slash ( / ).\nCannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.\n\n

    :type DbName: string
    :param DbName: The name of a database that DbUser is authorized to log on to. If DbName is not specified, DbUser can log on to any existing database.\nConstraints:\n\nMust be 1 to 64 alphanumeric characters or hyphens\nMust contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.\nFirst character must be a letter.\nMust not contain a colon ( : ) or slash ( / ).\nCannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.\n\n

    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier of the cluster that contains the database for which your are requesting credentials. This parameter is case sensitive.\n

    :type DurationSeconds: integer
    :param DurationSeconds: The number of seconds until the returned temporary password expires.\nConstraint: minimum 900, maximum 3600.\nDefault: 900\n

    :type AutoCreate: boolean
    :param AutoCreate: Create a database user with the name specified for the user named in DbUser if one does not exist.

    :type DbGroups: list
    :param DbGroups: A list of the names of existing database groups that the user named in DbUser will join for the current session, in addition to any group memberships for an existing user. If not specified, a new user is added only to PUBLIC.\nDatabase group name constraints\n\nMust be 1 to 64 alphanumeric characters or hyphens\nMust contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.\nFirst character must be a letter.\nMust not contain a colon ( : ) or slash ( / ).\nCannot be a reserved word. A list of reserved words can be found in Reserved Words in the Amazon Redshift Database Developer Guide.\n\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DbUser': 'string',
    'DbPassword': 'string',
    'Expiration': datetime(2015, 1, 1)
}


Response Structure

(dict) --
Temporary credentials with authorization to log on to an Amazon Redshift database.

DbUser (string) --
A database user name that is authorized to log on to the database DbName using the password DbPassword . If the specified DbUser exists in the database, the new user name has the same database privileges as the the user named in DbUser. By default, the user is added to PUBLIC. If the DbGroups parameter is specifed, DbUser is added to the listed groups for any sessions created using these credentials.

DbPassword (string) --
A temporary password that authorizes the user name returned by DbUser to log on to the database DbName .

Expiration (datetime) --
The date and time the password in DbPassword expires.







Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.UnsupportedOperationFault


    :return: {
        'DbUser': 'string',
        'DbPassword': 'string',
        'Expiration': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterNotFoundFault
    Redshift.Client.exceptions.UnsupportedOperationFault
    
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

def get_reserved_node_exchange_offerings(ReservedNodeId=None, MaxRecords=None, Marker=None):
    """
    Returns an array of DC2 ReservedNodeOfferings that matches the payment type, term, and usage price of the given DC1 reserved node.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_reserved_node_exchange_offerings(
        ReservedNodeId='string',
        MaxRecords=123,
        Marker='string'
    )
    
    
    :type ReservedNodeId: string
    :param ReservedNodeId: [REQUIRED]\nA string representing the node identifier for the DC1 Reserved Node to be exchanged.\n

    :type MaxRecords: integer
    :param MaxRecords: An integer setting the maximum number of ReservedNodeOfferings to retrieve.

    :type Marker: string
    :param Marker: A value that indicates the starting point for the next set of ReservedNodeOfferings.

    :rtype: dict

ReturnsResponse Syntax
{
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
            ],
            'ReservedNodeOfferingType': 'Regular'|'Upgradable'
        },
    ]
}


Response Structure

(dict) --

Marker (string) --
An optional parameter that specifies the starting point for returning a set of response records. When the results of a GetReservedNodeExchangeOfferings request exceed the value specified in MaxRecords, Amazon Redshift returns a value in the marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the marker parameter and retrying the request.

ReservedNodeOfferings (list) --
Returns an array of  ReservedNodeOffering objects.

(dict) --
Describes a reserved node offering.

ReservedNodeOfferingId (string) --
The offering identifier.

NodeType (string) --
The node type offered by the reserved node offering.

Duration (integer) --
The duration, in seconds, for which the offering will reserve the node.

FixedPrice (float) --
The upfront fixed charge you will pay to purchase the specific reserved node offering.

UsagePrice (float) --
The rate you are charged for each hour the cluster that is using the offering is running.

CurrencyCode (string) --
The currency code for the compute nodes offering.

OfferingType (string) --
The anticipated utilization of the reserved node, as defined in the reserved node offering.

RecurringCharges (list) --
The charge to your account regardless of whether you are creating any clusters using the node offering. Recurring charges are only in effect for heavy-utilization reserved nodes.

(dict) --
Describes a recurring charge.

RecurringChargeAmount (float) --
The amount charged per the period of time specified by the recurring charge frequency.

RecurringChargeFrequency (string) --
The frequency at which the recurring charge amount is applied.





ReservedNodeOfferingType (string) --











Exceptions

Redshift.Client.exceptions.ReservedNodeNotFoundFault
Redshift.Client.exceptions.InvalidReservedNodeStateFault
Redshift.Client.exceptions.ReservedNodeAlreadyMigratedFault
Redshift.Client.exceptions.ReservedNodeOfferingNotFoundFault
Redshift.Client.exceptions.UnsupportedOperationFault
Redshift.Client.exceptions.DependentServiceUnavailableFault


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
                ],
                'ReservedNodeOfferingType': 'Regular'|'Upgradable'
            },
        ]
    }
    
    
    :returns: 
    Redshift.Client.exceptions.ReservedNodeNotFoundFault
    Redshift.Client.exceptions.InvalidReservedNodeStateFault
    Redshift.Client.exceptions.ReservedNodeAlreadyMigratedFault
    Redshift.Client.exceptions.ReservedNodeOfferingNotFoundFault
    Redshift.Client.exceptions.UnsupportedOperationFault
    Redshift.Client.exceptions.DependentServiceUnavailableFault
    
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

def modify_cluster(ClusterIdentifier=None, ClusterType=None, NodeType=None, NumberOfNodes=None, ClusterSecurityGroups=None, VpcSecurityGroupIds=None, MasterUserPassword=None, ClusterParameterGroupName=None, AutomatedSnapshotRetentionPeriod=None, ManualSnapshotRetentionPeriod=None, PreferredMaintenanceWindow=None, ClusterVersion=None, AllowVersionUpgrade=None, HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None, NewClusterIdentifier=None, PubliclyAccessible=None, ElasticIp=None, EnhancedVpcRouting=None, MaintenanceTrackName=None, Encrypted=None, KmsKeyId=None):
    """
    Modifies the settings for a cluster.
    You can also change node type and the number of nodes to scale up or down the cluster. When resizing a cluster, you must specify both the number of nodes and the node type even if one of the parameters does not change.
    You can add another security or parameter group, or change the master user password. Resetting a cluster password or modifying the security groups associated with a cluster do not need a reboot. However, modifying a parameter group requires a reboot for parameters to take effect. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
        ManualSnapshotRetentionPeriod=123,
        PreferredMaintenanceWindow='string',
        ClusterVersion='string',
        AllowVersionUpgrade=True|False,
        HsmClientCertificateIdentifier='string',
        HsmConfigurationIdentifier='string',
        NewClusterIdentifier='string',
        PubliclyAccessible=True|False,
        ElasticIp='string',
        EnhancedVpcRouting=True|False,
        MaintenanceTrackName='string',
        Encrypted=True|False,
        KmsKeyId='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier of the cluster to be modified.\nExample: examplecluster\n

    :type ClusterType: string
    :param ClusterType: The new cluster type.\nWhen you submit your cluster resize request, your existing cluster goes into a read-only mode. After Amazon Redshift provisions a new cluster based on your resize requirements, there will be outage for a period while the old cluster is deleted and your connection is switched to the new cluster. You can use DescribeResize to track the progress of the resize request.\nValid Values: multi-node | single-node\n

    :type NodeType: string
    :param NodeType: The new node type of the cluster. If you specify a new node type, you must also specify the number of nodes parameter.\nFor more information about resizing clusters, go to Resizing Clusters in Amazon Redshift in the Amazon Redshift Cluster Management Guide .\nValid Values: ds2.xlarge | ds2.8xlarge | dc1.large | dc1.8xlarge | dc2.large | dc2.8xlarge | ra3.4xlarge | ra3.16xlarge\n

    :type NumberOfNodes: integer
    :param NumberOfNodes: The new number of nodes of the cluster. If you specify a new number of nodes, you must also specify the node type parameter.\nFor more information about resizing clusters, go to Resizing Clusters in Amazon Redshift in the Amazon Redshift Cluster Management Guide .\nValid Values: Integer greater than 0 .\n

    :type ClusterSecurityGroups: list
    :param ClusterSecurityGroups: A list of cluster security groups to be authorized on this cluster. This change is asynchronously applied as soon as possible.\nSecurity groups currently associated with the cluster, and not in the list of groups to apply, will be revoked from the cluster.\nConstraints:\n\nMust be 1 to 255 alphanumeric characters or hyphens\nFirst character must be a letter\nCannot end with a hyphen or contain two consecutive hyphens\n\n\n(string) --\n\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of virtual private cloud (VPC) security groups to be associated with the cluster. This change is asynchronously applied as soon as possible.\n\n(string) --\n\n

    :type MasterUserPassword: string
    :param MasterUserPassword: The new password for the cluster master user. This change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the MasterUserPassword element exists in the PendingModifiedValues element of the operation response.\n\nNote\nOperations never return the password, so this operation provides a way to regain access to the master user account for a cluster if the password is lost.\n\nDefault: Uses existing setting.\nConstraints:\n\nMust be between 8 and 64 characters in length.\nMust contain at least one uppercase letter.\nMust contain at least one lowercase letter.\nMust contain one number.\nCan be any printable ASCII character (ASCII code 33 to 126) except \' (single quote), ' (double quote), , /, @, or space.\n\n

    :type ClusterParameterGroupName: string
    :param ClusterParameterGroupName: The name of the cluster parameter group to apply to this cluster. This change is applied only after the cluster is rebooted. To reboot a cluster use RebootCluster .\nDefault: Uses existing setting.\nConstraints: The cluster parameter group must be in the same parameter group family that matches the cluster version.\n

    :type AutomatedSnapshotRetentionPeriod: integer
    :param AutomatedSnapshotRetentionPeriod: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with CreateClusterSnapshot .\nIf you decrease the automated snapshot retention period from its current value, existing automated snapshots that fall outside of the new retention period will be immediately deleted.\nDefault: Uses existing setting.\nConstraints: Must be a value from 0 to 35.\n

    :type ManualSnapshotRetentionPeriod: integer
    :param ManualSnapshotRetentionPeriod: The default for number of days that a newly created manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. This value doesn\'t retroactively change the retention periods of existing manual snapshots.\nThe value must be either -1 or an integer between 1 and 3,653.\nThe default value is -1.\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, if necessary. If system maintenance is necessary during the window, it may result in an outage.\nThis maintenance window change is made immediately. If the new maintenance window indicates the current time, there must be at least 120 minutes between the current time and end of the window in order to ensure that pending changes are applied.\nDefault: Uses existing setting.\nFormat: ddd:hh24:mi-ddd:hh24:mi, for example wed:07:30-wed:08:00 .\nValid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun\nConstraints: Must be at least 30 minutes.\n

    :type ClusterVersion: string
    :param ClusterVersion: The new version number of the Amazon Redshift engine to upgrade to.\nFor major version upgrades, if a non-default cluster parameter group is currently in use, a new cluster parameter group in the cluster parameter group family for the new version must be specified. The new cluster parameter group can be the default for that cluster parameter group family. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .\nExample: 1.0\n

    :type AllowVersionUpgrade: boolean
    :param AllowVersionUpgrade: If true , major version upgrades will be applied automatically to the cluster during the maintenance window.\nDefault: false\n

    :type HsmClientCertificateIdentifier: string
    :param HsmClientCertificateIdentifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

    :type HsmConfigurationIdentifier: string
    :param HsmConfigurationIdentifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

    :type NewClusterIdentifier: string
    :param NewClusterIdentifier: The new identifier for the cluster.\nConstraints:\n\nMust contain from 1 to 63 alphanumeric characters or hyphens.\nAlphabetic characters must be lowercase.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\nMust be unique for all clusters within an AWS account.\n\nExample: examplecluster\n

    :type PubliclyAccessible: boolean
    :param PubliclyAccessible: If true , the cluster can be accessed from a public network. Only clusters in VPCs can be set to be publicly available.

    :type ElasticIp: string
    :param ElasticIp: The Elastic IP (EIP) address for the cluster.\nConstraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to Supported Platforms to Launch Your Cluster in the Amazon Redshift Cluster Management Guide.\n

    :type EnhancedVpcRouting: boolean
    :param EnhancedVpcRouting: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.\nIf this option is true , enhanced VPC routing is enabled.\nDefault: false\n

    :type MaintenanceTrackName: string
    :param MaintenanceTrackName: The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the PendingModifiedValues for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.

    :type Encrypted: boolean
    :param Encrypted: Indicates whether the cluster is encrypted. If the value is encrypted (true) and you provide a value for the KmsKeyId parameter, we encrypt the cluster with the provided KmsKeyId . If you don\'t provide a KmsKeyId , we encrypt with the default key. In the China region we use legacy encryption if you specify that the cluster is encrypted.\nIf the value is not encrypted (false), then the cluster is decrypted.\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.InvalidClusterSecurityGroupStateFault
Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.NumberOfNodesQuotaExceededFault
Redshift.Client.exceptions.NumberOfNodesPerClusterLimitExceededFault
Redshift.Client.exceptions.ClusterSecurityGroupNotFoundFault
Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
Redshift.Client.exceptions.InsufficientClusterCapacityFault
Redshift.Client.exceptions.UnsupportedOptionFault
Redshift.Client.exceptions.UnauthorizedOperation
Redshift.Client.exceptions.HsmClientCertificateNotFoundFault
Redshift.Client.exceptions.HsmConfigurationNotFoundFault
Redshift.Client.exceptions.ClusterAlreadyExistsFault
Redshift.Client.exceptions.LimitExceededFault
Redshift.Client.exceptions.DependentServiceRequestThrottlingFault
Redshift.Client.exceptions.InvalidElasticIpFault
Redshift.Client.exceptions.TableLimitExceededFault
Redshift.Client.exceptions.InvalidClusterTrackFault
Redshift.Client.exceptions.InvalidRetentionPeriodFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
    rebooting
    renaming
    resizing
    rotating-keys
    storage-full
    updating-hsm
    
    """
    pass

def modify_cluster_db_revision(ClusterIdentifier=None, RevisionTarget=None):
    """
    Modifies the database revision of a cluster. The database revision is a unique revision of the database running in a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_cluster_db_revision(
        ClusterIdentifier='string',
        RevisionTarget='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier of a cluster whose database revision you want to modify.\nExample: examplecluster\n

    :type RevisionTarget: string
    :param RevisionTarget: [REQUIRED]\nThe identifier of the database revision. You can retrieve this value from the response to the DescribeClusterDbRevisions request.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.ClusterOnLatestRevisionFault
Redshift.Client.exceptions.InvalidClusterStateFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
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
    
    Exceptions
    
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
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier of the cluster for which you want to associate or disassociate IAM roles.\n

    :type AddIamRoles: list
    :param AddIamRoles: Zero or more IAM roles to associate with the cluster. The roles must be in their Amazon Resource Name (ARN) format. You can associate up to 10 IAM roles with a single cluster in a single request.\n\n(string) --\n\n

    :type RemoveIamRoles: list
    :param RemoveIamRoles: Zero or more IAM roles in ARN format to disassociate from the cluster. You can disassociate up to 10 IAM roles from a single cluster in a single request.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.ClusterNotFoundFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
    rebooting
    renaming
    resizing
    rotating-keys
    storage-full
    updating-hsm
    
    """
    pass

def modify_cluster_maintenance(ClusterIdentifier=None, DeferMaintenance=None, DeferMaintenanceIdentifier=None, DeferMaintenanceStartTime=None, DeferMaintenanceEndTime=None, DeferMaintenanceDuration=None):
    """
    Modifies the maintenance settings of a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_cluster_maintenance(
        ClusterIdentifier='string',
        DeferMaintenance=True|False,
        DeferMaintenanceIdentifier='string',
        DeferMaintenanceStartTime=datetime(2015, 1, 1),
        DeferMaintenanceEndTime=datetime(2015, 1, 1),
        DeferMaintenanceDuration=123
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nA unique identifier for the cluster.\n

    :type DeferMaintenance: boolean
    :param DeferMaintenance: A boolean indicating whether to enable the deferred maintenance window.

    :type DeferMaintenanceIdentifier: string
    :param DeferMaintenanceIdentifier: A unique identifier for the deferred maintenance window.

    :type DeferMaintenanceStartTime: datetime
    :param DeferMaintenanceStartTime: A timestamp indicating the start time for the deferred maintenance window.

    :type DeferMaintenanceEndTime: datetime
    :param DeferMaintenanceEndTime: A timestamp indicating end time for the deferred maintenance window. If you specify an end time, you can\'t specify a duration.

    :type DeferMaintenanceDuration: integer
    :param DeferMaintenanceDuration: An integer indicating the duration of the maintenance window in days. If you specify a duration, you can\'t specify an end time. The duration must be 45 days or less.

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.InvalidClusterStateFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
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
    
    Exceptions
    
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
    :param ParameterGroupName: [REQUIRED]\nThe name of the parameter group to be modified.\n

    :type Parameters: list
    :param Parameters: [REQUIRED]\nAn array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.\nFor each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.\nFor the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.\n\n(dict) --Describes a parameter in a cluster parameter group.\n\nParameterName (string) --The name of the parameter.\n\nParameterValue (string) --The value of the parameter.\n\nDescription (string) --A description of the parameter.\n\nSource (string) --The source of the parameter value, such as 'engine-default' or 'user'.\n\nDataType (string) --The data type of the parameter.\n\nAllowedValues (string) --The valid range of values for the parameter.\n\nApplyType (string) --Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .\n\nIsModifiable (boolean) --If true , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.\n\nMinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ParameterGroupName': 'string',
    'ParameterGroupStatus': 'string'
}


Response Structure

(dict) --

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterGroupStatus (string) --
The status of the parameter group. For example, if you made a change to a parameter group name-value pair, then the change could be pending a reboot of an associated cluster.







Exceptions

Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
Redshift.Client.exceptions.InvalidClusterParameterGroupStateFault


    :return: {
        'ParameterGroupName': 'string',
        'ParameterGroupStatus': 'string'
    }
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
    Redshift.Client.exceptions.InvalidClusterParameterGroupStateFault
    
    """
    pass

def modify_cluster_snapshot(SnapshotIdentifier=None, ManualSnapshotRetentionPeriod=None, Force=None):
    """
    Modifies the settings for a snapshot.
    This exanmple modifies the manual retention period setting for a cluster snapshot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_cluster_snapshot(
        SnapshotIdentifier='string',
        ManualSnapshotRetentionPeriod=123,
        Force=True|False
    )
    
    
    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]\nThe identifier of the snapshot whose setting you want to modify.\n

    :type ManualSnapshotRetentionPeriod: integer
    :param ManualSnapshotRetentionPeriod: The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.\nIf the manual snapshot falls outside of the new retention period, you can specify the force option to immediately delete the snapshot.\nThe value must be either -1 or an integer between 1 and 3,653.\n

    :type Force: boolean
    :param Force: A Boolean option to override an exception if the retention period has already passed.

    :rtype: dict

ReturnsResponse Syntax
{
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
        'EnhancedVpcRouting': True|False,
        'MaintenanceTrackName': 'string',
        'ManualSnapshotRetentionPeriod': 123,
        'ManualSnapshotRemainingDays': 123,
        'SnapshotRetentionStartTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Snapshot (dict) --
Describes a snapshot.

SnapshotIdentifier (string) --
The snapshot identifier that is provided in the request.

ClusterIdentifier (string) --
The identifier of the cluster for which the snapshot was taken.

SnapshotCreateTime (datetime) --
The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.

Status (string) --
The snapshot status. The value of the status depends on the API operation used:

CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
DeleteClusterSnapshot returns status as "deleted".


Port (integer) --
The port that the cluster is listening on.

AvailabilityZone (string) --
The Availability Zone in which the cluster was created.

ClusterCreateTime (datetime) --
The time (UTC) when the cluster was originally created.

MasterUsername (string) --
The master user name for the cluster.

ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

SnapshotType (string) --
The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot are of type "manual".

NodeType (string) --
The node type of the nodes in the cluster.

NumberOfNodes (integer) --
The number of nodes in the cluster.

DBName (string) --
The name of the database that was created when the cluster was created.

VpcId (string) --
The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.

Encrypted (boolean) --
If true , the data in the snapshot is encrypted at rest.

KmsKeyId (string) --
The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.

EncryptedWithHSM (boolean) --
A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. true indicates that the data is encrypted using HSM keys.

AccountsWithRestoreAccess (list) --
A list of the AWS customer accounts authorized to restore the snapshot. Returns null if no accounts are authorized. Visible only to the snapshot owner.

(dict) --
Describes an AWS customer account authorized to restore a snapshot.

AccountId (string) --
The identifier of an AWS customer account authorized to restore a snapshot.

AccountAlias (string) --
The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is amazon-redshift-support .





OwnerAccount (string) --
For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.

TotalBackupSizeInMegaBytes (float) --
The size of the complete set of backup data that would be used to restore the cluster.

ActualIncrementalBackupSizeInMegaBytes (float) --
The size of the incremental backup.

BackupProgressInMegaBytes (float) --
The number of megabytes that have been transferred to the snapshot backup.

CurrentBackupRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred to the snapshot backup. Returns 0 for a completed backup.

EstimatedSecondsToCompletion (integer) --
The estimate of the time remaining before the snapshot backup will complete. Returns 0 for a completed backup.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.

SourceRegion (string) --
The source region from which the snapshot was copied.

Tags (list) --
The list of tags for the cluster snapshot.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





RestorableNodeTypes (list) --
The list of node types that this cluster snapshot is able to restore into.

(string) --


EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track for the snapshot.

ManualSnapshotRetentionPeriod (integer) --
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

ManualSnapshotRemainingDays (integer) --
The number of days until a manual snapshot will pass its retention period.

SnapshotRetentionStartTime (datetime) --
A timestamp representing the start of the retention period for the snapshot.









Exceptions

Redshift.Client.exceptions.InvalidClusterSnapshotStateFault
Redshift.Client.exceptions.ClusterSnapshotNotFoundFault
Redshift.Client.exceptions.InvalidRetentionPeriodFault


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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'ManualSnapshotRetentionPeriod': 123,
            'ManualSnapshotRemainingDays': 123,
            'SnapshotRetentionStartTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
    DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
    DeleteClusterSnapshot returns status as "deleted".
    
    """
    pass

def modify_cluster_snapshot_schedule(ClusterIdentifier=None, ScheduleIdentifier=None, DisassociateSchedule=None):
    """
    Modifies a snapshot schedule for a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_cluster_snapshot_schedule(
        ClusterIdentifier='string',
        ScheduleIdentifier='string',
        DisassociateSchedule=True|False
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nA unique identifier for the cluster whose snapshot schedule you want to modify.\n

    :type ScheduleIdentifier: string
    :param ScheduleIdentifier: A unique alphanumeric identifier for the schedule that you want to associate with the cluster.

    :type DisassociateSchedule: boolean
    :param DisassociateSchedule: A boolean to indicate whether to remove the assoiciation between the cluster and the schedule.

    :returns: 
    Redshift.Client.exceptions.ClusterNotFoundFault
    Redshift.Client.exceptions.SnapshotScheduleNotFoundFault
    Redshift.Client.exceptions.InvalidClusterSnapshotScheduleStateFault
    
    """
    pass

def modify_cluster_subnet_group(ClusterSubnetGroupName=None, Description=None, SubnetIds=None):
    """
    Modifies a cluster subnet group to include the specified list of VPC subnets. The operation replaces the existing list of subnets with the new list of subnets.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_cluster_subnet_group(
        ClusterSubnetGroupName='string',
        Description='string',
        SubnetIds=[
            'string',
        ]
    )
    
    
    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: [REQUIRED]\nThe name of the subnet group to be modified.\n

    :type Description: string
    :param Description: A text description of the subnet group to be modified.

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nAn array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterSubnetGroup': {
        'ClusterSubnetGroupName': 'string',
        'Description': 'string',
        'VpcId': 'string',
        'SubnetGroupStatus': 'string',
        'Subnets': [
            {
                'SubnetIdentifier': 'string',
                'SubnetAvailabilityZone': {
                    'Name': 'string',
                    'SupportedPlatforms': [
                        {
                            'Name': 'string'
                        },
                    ]
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


Response Structure

(dict) --

ClusterSubnetGroup (dict) --
Describes a subnet group.

ClusterSubnetGroupName (string) --
The name of the cluster subnet group.

Description (string) --
The description of the cluster subnet group.

VpcId (string) --
The VPC ID of the cluster subnet group.

SubnetGroupStatus (string) --
The status of the cluster subnet group. Possible values are Complete , Incomplete and Invalid .

Subnets (list) --
A list of the VPC  Subnet elements.

(dict) --
Describes a subnet.

SubnetIdentifier (string) --
The identifier of the subnet.

SubnetAvailabilityZone (dict) --

Name (string) --
The name of the availability zone.

SupportedPlatforms (list) --

(dict) --
A list of supported platforms for orderable clusters.

Name (string) --






SubnetStatus (string) --
The status of the subnet.





Tags (list) --
The list of tags for the cluster subnet group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.ClusterSubnetGroupNotFoundFault
Redshift.Client.exceptions.ClusterSubnetQuotaExceededFault
Redshift.Client.exceptions.SubnetAlreadyInUse
Redshift.Client.exceptions.InvalidSubnet
Redshift.Client.exceptions.UnauthorizedOperation
Redshift.Client.exceptions.DependentServiceRequestThrottlingFault


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
                        'Name': 'string',
                        'SupportedPlatforms': [
                            {
                                'Name': 'string'
                            },
                        ]
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
    
    
    :returns: 
    Name (string) --
    
    """
    pass

def modify_event_subscription(SubscriptionName=None, SnsTopicArn=None, SourceType=None, SourceIds=None, EventCategories=None, Severity=None, Enabled=None):
    """
    Modifies an existing Amazon Redshift event notification subscription.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param SubscriptionName: [REQUIRED]\nThe name of the modified Amazon Redshift event notification subscription.\n

    :type SnsTopicArn: string
    :param SnsTopicArn: The Amazon Resource Name (ARN) of the SNS topic to be used by the event notification subscription.

    :type SourceType: string
    :param SourceType: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account. You must specify a source type in order to specify source IDs.\nValid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.\n

    :type SourceIds: list
    :param SourceIds: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.\nExample: my-cluster-1, my-cluster-2\nExample: my-snapshot-20131010\n\n(string) --\n\n

    :type EventCategories: list
    :param EventCategories: Specifies the Amazon Redshift event categories to be published by the event notification subscription.\nValues: configuration, management, monitoring, security\n\n(string) --\n\n

    :type Severity: string
    :param Severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription.\nValues: ERROR, INFO\n

    :type Enabled: boolean
    :param Enabled: A Boolean value indicating if the subscription is enabled. true indicates the subscription is enabled

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

EventSubscription (dict) --
Describes event subscriptions.

CustomerAwsId (string) --
The AWS customer account associated with the Amazon Redshift event notification subscription.

CustSubscriptionId (string) --
The name of the Amazon Redshift event notification subscription.

SnsTopicArn (string) --
The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.

Status (string) --
The status of the Amazon Redshift event notification subscription.
Constraints:

Can be one of the following: active | no-permission | topic-not-exist
The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.


SubscriptionCreationTime (datetime) --
The date and time the Amazon Redshift event notification subscription was created.

SourceType (string) --
The source type of the events returned by the Amazon Redshift event notification, such as cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, or scheduled-action.

SourceIdsList (list) --
A list of the sources that publish events to the Amazon Redshift event notification subscription.

(string) --


EventCategoriesList (list) --
The list of Amazon Redshift event categories specified in the event notification subscription.
Values: Configuration, Management, Monitoring, Security

(string) --


Severity (string) --
The event severity specified in the Amazon Redshift event notification subscription.
Values: ERROR, INFO

Enabled (boolean) --
A boolean value indicating whether the subscription is enabled; true indicates that the subscription is enabled.

Tags (list) --
The list of tags for the event subscription.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.SubscriptionNotFoundFault
Redshift.Client.exceptions.SNSInvalidTopicFault
Redshift.Client.exceptions.SNSNoAuthorizationFault
Redshift.Client.exceptions.SNSTopicArnNotFoundFault
Redshift.Client.exceptions.SubscriptionEventIdNotFoundFault
Redshift.Client.exceptions.SubscriptionCategoryNotFoundFault
Redshift.Client.exceptions.SubscriptionSeverityNotFoundFault
Redshift.Client.exceptions.SourceNotFoundFault
Redshift.Client.exceptions.InvalidSubscriptionStateFault


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

def modify_scheduled_action(ScheduledActionName=None, TargetAction=None, Schedule=None, IamRole=None, ScheduledActionDescription=None, StartTime=None, EndTime=None, Enable=None):
    """
    Modifies a scheduled action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_scheduled_action(
        ScheduledActionName='string',
        TargetAction={
            'ResizeCluster': {
                'ClusterIdentifier': 'string',
                'ClusterType': 'string',
                'NodeType': 'string',
                'NumberOfNodes': 123,
                'Classic': True|False
            },
            'PauseCluster': {
                'ClusterIdentifier': 'string'
            },
            'ResumeCluster': {
                'ClusterIdentifier': 'string'
            }
        },
        Schedule='string',
        IamRole='string',
        ScheduledActionDescription='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Enable=True|False
    )
    
    
    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]\nThe name of the scheduled action to modify.\n

    :type TargetAction: dict
    :param TargetAction: A modified JSON format of the scheduled action. For more information about this parameter, see ScheduledAction .\n\nResizeCluster (dict) --An action that runs a ResizeCluster API operation.\n\nClusterIdentifier (string) -- [REQUIRED]The unique identifier for the cluster to resize.\n\nClusterType (string) --The new cluster type for the specified cluster.\n\nNodeType (string) --The new node type for the nodes you are adding. If not specified, the cluster\'s current node type is used.\n\nNumberOfNodes (integer) --The new number of nodes for the cluster.\n\nClassic (boolean) --A boolean value indicating whether the resize operation is using the classic resize process. If you don\'t provide this parameter or set the value to false , the resize type is elastic.\n\n\n\nPauseCluster (dict) --An action that runs a PauseCluster API operation.\n\nClusterIdentifier (string) -- [REQUIRED]The identifier of the cluster to be paused.\n\n\n\nResumeCluster (dict) --An action that runs a ResumeCluster API operation.\n\nClusterIdentifier (string) -- [REQUIRED]The identifier of the cluster to be resumed.\n\n\n\n\n

    :type Schedule: string
    :param Schedule: A modified schedule in either at( ) or cron( ) format. For more information about this parameter, see ScheduledAction .

    :type IamRole: string
    :param IamRole: A different IAM role to assume to run the target action. For more information about this parameter, see ScheduledAction .

    :type ScheduledActionDescription: string
    :param ScheduledActionDescription: A modified description of the scheduled action.

    :type StartTime: datetime
    :param StartTime: A modified start time of the scheduled action. For more information about this parameter, see ScheduledAction .

    :type EndTime: datetime
    :param EndTime: A modified end time of the scheduled action. For more information about this parameter, see ScheduledAction .

    :type Enable: boolean
    :param Enable: A modified enable flag of the scheduled action. If true, the scheduled action is active. If false, the scheduled action is disabled.

    :rtype: dict

ReturnsResponse Syntax
{
    'ScheduledActionName': 'string',
    'TargetAction': {
        'ResizeCluster': {
            'ClusterIdentifier': 'string',
            'ClusterType': 'string',
            'NodeType': 'string',
            'NumberOfNodes': 123,
            'Classic': True|False
        },
        'PauseCluster': {
            'ClusterIdentifier': 'string'
        },
        'ResumeCluster': {
            'ClusterIdentifier': 'string'
        }
    },
    'Schedule': 'string',
    'IamRole': 'string',
    'ScheduledActionDescription': 'string',
    'State': 'ACTIVE'|'DISABLED',
    'NextInvocations': [
        datetime(2015, 1, 1),
    ],
    'StartTime': datetime(2015, 1, 1),
    'EndTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --
Describes a scheduled action. You can use a scheduled action to trigger some Amazon Redshift API operations on a schedule. For information about which API operations can be scheduled, see  ScheduledActionType .

ScheduledActionName (string) --
The name of the scheduled action.

TargetAction (dict) --
A JSON format string of the Amazon Redshift API operation with input parameters.
"{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}} ".

ResizeCluster (dict) --
An action that runs a ResizeCluster API operation.

ClusterIdentifier (string) --
The unique identifier for the cluster to resize.

ClusterType (string) --
The new cluster type for the specified cluster.

NodeType (string) --
The new node type for the nodes you are adding. If not specified, the cluster\'s current node type is used.

NumberOfNodes (integer) --
The new number of nodes for the cluster.

Classic (boolean) --
A boolean value indicating whether the resize operation is using the classic resize process. If you don\'t provide this parameter or set the value to false , the resize type is elastic.



PauseCluster (dict) --
An action that runs a PauseCluster API operation.

ClusterIdentifier (string) --
The identifier of the cluster to be paused.



ResumeCluster (dict) --
An action that runs a ResumeCluster API operation.

ClusterIdentifier (string) --
The identifier of the cluster to be resumed.





Schedule (string) --
The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour.
Format of at expressions is "at(yyyy-mm-ddThh:mm:ss) ". For example, "at(2016-03-04T17:27:00) ".
Format of cron expressions is "cron(Minutes Hours Day-of-month Month Day-of-week Year) ". For example, "cron(0 10 ? * MON *) ". For more information, see Cron Expressions in the Amazon CloudWatch Events User Guide .

IamRole (string) --
The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see Using Identity-Based Policies for Amazon Redshift in the Amazon Redshift Cluster Management Guide .

ScheduledActionDescription (string) --
The description of the scheduled action.

State (string) --
The state of the scheduled action. For example, DISABLED .

NextInvocations (list) --
List of times when the scheduled action will run.

(datetime) --


StartTime (datetime) --
The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.

EndTime (datetime) --
The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.







Exceptions

Redshift.Client.exceptions.ScheduledActionNotFoundFault
Redshift.Client.exceptions.ScheduledActionTypeUnsupportedFault
Redshift.Client.exceptions.InvalidScheduleFault
Redshift.Client.exceptions.InvalidScheduledActionFault
Redshift.Client.exceptions.UnauthorizedOperation


    :return: {
        'ScheduledActionName': 'string',
        'TargetAction': {
            'ResizeCluster': {
                'ClusterIdentifier': 'string',
                'ClusterType': 'string',
                'NodeType': 'string',
                'NumberOfNodes': 123,
                'Classic': True|False
            },
            'PauseCluster': {
                'ClusterIdentifier': 'string'
            },
            'ResumeCluster': {
                'ClusterIdentifier': 'string'
            }
        },
        'Schedule': 'string',
        'IamRole': 'string',
        'ScheduledActionDescription': 'string',
        'State': 'ACTIVE'|'DISABLED',
        'NextInvocations': [
            datetime(2015, 1, 1),
        ],
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (datetime) --
    
    """
    pass

def modify_snapshot_copy_retention_period(ClusterIdentifier=None, RetentionPeriod=None, Manual=None):
    """
    Modifies the number of days to retain snapshots in the destination AWS Region after they are copied from the source AWS Region. By default, this operation only changes the retention period of copied automated snapshots. The retention periods for both new and existing copied automated snapshots are updated with the new retention period. You can set the manual option to change only the retention periods of copied manual snapshots. If you set this option, only newly copied manual snapshots have the new retention period.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_snapshot_copy_retention_period(
        ClusterIdentifier='string',
        RetentionPeriod=123,
        Manual=True|False
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier of the cluster for which you want to change the retention period for either automated or manual snapshots that are copied to a destination AWS Region.\nConstraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.\n

    :type RetentionPeriod: integer
    :param RetentionPeriod: [REQUIRED]\nThe number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region.\nBy default, this only changes the retention period of copied automated snapshots.\nIf you decrease the retention period for automated snapshots that are copied to a destination AWS Region, Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period.\nConstraints: Must be at least 1 and no more than 35 for automated snapshots.\nIf you specify the manual option, only newly copied manual snapshots will have the new retention period.\nIf you specify the value of -1 newly copied manual snapshots are retained indefinitely.\nConstraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.\n

    :type Manual: boolean
    :param Manual: Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.SnapshotCopyDisabledFault
Redshift.Client.exceptions.UnauthorizedOperation
Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.InvalidRetentionPeriodFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
    rebooting
    renaming
    resizing
    rotating-keys
    storage-full
    updating-hsm
    
    """
    pass

def modify_snapshot_schedule(ScheduleIdentifier=None, ScheduleDefinitions=None):
    """
    Modifies a snapshot schedule. Any schedule associated with a cluster is modified asynchronously.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_snapshot_schedule(
        ScheduleIdentifier='string',
        ScheduleDefinitions=[
            'string',
        ]
    )
    
    
    :type ScheduleIdentifier: string
    :param ScheduleIdentifier: [REQUIRED]\nA unique alphanumeric identifier of the schedule to modify.\n

    :type ScheduleDefinitions: list
    :param ScheduleDefinitions: [REQUIRED]\nAn updated list of schedule definitions. A schedule definition is made up of schedule expressions, for example, 'cron(30 12 *)' or 'rate(12 hours)'.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ScheduleDefinitions': [
        'string',
    ],
    'ScheduleIdentifier': 'string',
    'ScheduleDescription': 'string',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextInvocations': [
        datetime(2015, 1, 1),
    ],
    'AssociatedClusterCount': 123,
    'AssociatedClusters': [
        {
            'ClusterIdentifier': 'string',
            'ScheduleAssociationState': 'MODIFYING'|'ACTIVE'|'FAILED'
        },
    ]
}


Response Structure

(dict) --
Describes a snapshot schedule. You can set a regular interval for creating snapshots of a cluster. You can also schedule snapshots for specific dates.

ScheduleDefinitions (list) --
A list of ScheduleDefinitions.

(string) --


ScheduleIdentifier (string) --
A unique identifier for the schedule.

ScheduleDescription (string) --
The description of the schedule.

Tags (list) --
An optional set of tags describing the schedule.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





NextInvocations (list) --

(datetime) --


AssociatedClusterCount (integer) --
The number of clusters associated with the schedule.

AssociatedClusters (list) --
A list of clusters associated with the schedule. A maximum of 100 clusters is returned.

(dict) --
ClusterIdentifier (string) --
ScheduleAssociationState (string) --










Exceptions

Redshift.Client.exceptions.InvalidScheduleFault
Redshift.Client.exceptions.SnapshotScheduleNotFoundFault
Redshift.Client.exceptions.SnapshotScheduleUpdateInProgressFault


    :return: {
        'ScheduleDefinitions': [
            'string',
        ],
        'ScheduleIdentifier': 'string',
        'ScheduleDescription': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextInvocations': [
            datetime(2015, 1, 1),
        ],
        'AssociatedClusterCount': 123,
        'AssociatedClusters': [
            {
                'ClusterIdentifier': 'string',
                'ScheduleAssociationState': 'MODIFYING'|'ACTIVE'|'FAILED'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_usage_limit(UsageLimitId=None, Amount=None, BreachAction=None):
    """
    Modifies a usage limit in a cluster. You can\'t modify the feature type or period of a usage limit.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_usage_limit(
        UsageLimitId='string',
        Amount=123,
        BreachAction='log'|'emit-metric'|'disable'
    )
    
    
    :type UsageLimitId: string
    :param UsageLimitId: [REQUIRED]\nThe identifier of the usage limit to modify.\n

    :type Amount: integer
    :param Amount: The new limit amount. For more information about this parameter, see UsageLimit .

    :type BreachAction: string
    :param BreachAction: The new action that Amazon Redshift takes when the limit is reached. For more information about this parameter, see UsageLimit .

    :rtype: dict

ReturnsResponse Syntax
{
    'UsageLimitId': 'string',
    'ClusterIdentifier': 'string',
    'FeatureType': 'spectrum'|'concurrency-scaling',
    'LimitType': 'time'|'data-scanned',
    'Amount': 123,
    'Period': 'daily'|'weekly'|'monthly',
    'BreachAction': 'log'|'emit-metric'|'disable',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Describes a usage limit object for a cluster.

UsageLimitId (string) --
The identifier of the usage limit.

ClusterIdentifier (string) --
The identifier of the cluster with a usage limit.

FeatureType (string) --
The Amazon Redshift feature to which the limit applies.

LimitType (string) --
The type of limit. Depending on the feature type, this can be based on a time duration or data size.

Amount (integer) --
The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB).

Period (string) --
The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly .

BreachAction (string) --
The action that Amazon Redshift takes when the limit is reached. Possible values are:

log - To log an event in a system table. The default is log.
emit-metric - To emit CloudWatch metrics.
disable - To disable the feature until the next usage period begins.


Tags (list) --
A list of tag instances.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.











Exceptions

Redshift.Client.exceptions.InvalidUsageLimitFault
Redshift.Client.exceptions.UsageLimitNotFoundFault
Redshift.Client.exceptions.UnsupportedOperationFault


    :return: {
        'UsageLimitId': 'string',
        'ClusterIdentifier': 'string',
        'FeatureType': 'spectrum'|'concurrency-scaling',
        'LimitType': 'time'|'data-scanned',
        'Amount': 123,
        'Period': 'daily'|'weekly'|'monthly',
        'BreachAction': 'log'|'emit-metric'|'disable',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    log - To log an event in a system table. The default is log.
    emit-metric - To emit CloudWatch metrics.
    disable - To disable the feature until the next usage period begins.
    
    """
    pass

def pause_cluster(ClusterIdentifier=None):
    """
    Pauses a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.pause_cluster(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe identifier of the cluster to be paused.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --
Cluster (dict) --Describes a cluster.

ClusterIdentifier (string) --The unique identifier of the cluster.

NodeType (string) --The node type for the nodes in the cluster.

ClusterStatus (string) --The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --The connection endpoint.

Address (string) --The DNS address of the Cluster.

Port (integer) --The port that the database engine is listening on.



ClusterCreateTime (datetime) --The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

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

NodeType (string) --The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --The pending or in-progress change of the cluster type.

ClusterVersion (string) --The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --
Status (string) --Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

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

ApplyStatus (string) --A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --Describes a group of DeferredMaintenanceWindow objects.

(dict) --Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --Returns the value ClassicResize .

AllowCancelResize (boolean) --A boolean value indicating if the resize operation can be cancelled.










Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.InvalidClusterStateFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    Available - The cluster is available for queries.
    Unavailable - The cluster is not available for queries.
    Maintenance - The cluster is intermittently available for queries due to maintenance activities.
    Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
    Failed - The cluster failed and is not available for queries.
    
    """
    pass

def purchase_reserved_node_offering(ReservedNodeOfferingId=None, NodeCount=None):
    """
    Allows you to purchase reserved nodes. Amazon Redshift offers a predefined set of reserved node offerings. You can purchase one or more of the offerings. You can call the  DescribeReservedNodeOfferings API to obtain the available reserved node offerings. You can call this API by providing a specific reserved node offering and the number of nodes you want to reserve.
    For more information about reserved node offerings, go to Purchasing Reserved Nodes in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.purchase_reserved_node_offering(
        ReservedNodeOfferingId='string',
        NodeCount=123
    )
    
    
    :type ReservedNodeOfferingId: string
    :param ReservedNodeOfferingId: [REQUIRED]\nThe unique identifier of the reserved node offering you want to purchase.\n

    :type NodeCount: integer
    :param NodeCount: The number of reserved nodes that you want to purchase.\nDefault: 1\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        ],
        'ReservedNodeOfferingType': 'Regular'|'Upgradable'
    }
}


Response Structure

(dict) --

ReservedNode (dict) --
Describes a reserved node. You can call the  DescribeReservedNodeOfferings API to obtain the available reserved node offerings.

ReservedNodeId (string) --
The unique identifier for the reservation.

ReservedNodeOfferingId (string) --
The identifier for the reserved node offering.

NodeType (string) --
The node type of the reserved node.

StartTime (datetime) --
The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.

Duration (integer) --
The duration of the node reservation in seconds.

FixedPrice (float) --
The fixed cost Amazon Redshift charges you for this reserved node.

UsagePrice (float) --
The hourly rate Amazon Redshift charges you for this reserved node.

CurrencyCode (string) --
The currency code for the reserved cluster.

NodeCount (integer) --
The number of reserved compute nodes.

State (string) --
The state of the reserved compute node.
Possible Values:

pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
active-This reserved node is owned by the caller and is available for use.
payment-failed-Payment failed for the purchase attempt.
retired-The reserved node is no longer available.
exchanging-The owner is exchanging the reserved node for another reserved node.


OfferingType (string) --
The anticipated utilization of the reserved node, as defined in the reserved node offering.

RecurringCharges (list) --
The recurring charges for the reserved node.

(dict) --
Describes a recurring charge.

RecurringChargeAmount (float) --
The amount charged per the period of time specified by the recurring charge frequency.

RecurringChargeFrequency (string) --
The frequency at which the recurring charge amount is applied.





ReservedNodeOfferingType (string) --









Exceptions

Redshift.Client.exceptions.ReservedNodeOfferingNotFoundFault
Redshift.Client.exceptions.ReservedNodeAlreadyExistsFault
Redshift.Client.exceptions.ReservedNodeQuotaExceededFault
Redshift.Client.exceptions.UnsupportedOperationFault


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
            ],
            'ReservedNodeOfferingType': 'Regular'|'Upgradable'
        }
    }
    
    
    :returns: 
    pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
    active-This reserved node is owned by the caller and is available for use.
    payment-failed-Payment failed for the purchase attempt.
    retired-The reserved node is no longer available.
    exchanging-The owner is exchanging the reserved node for another reserved node.
    
    """
    pass

def reboot_cluster(ClusterIdentifier=None):
    """
    Reboots a cluster. This action is taken as soon as possible. It results in a momentary outage to the cluster, during which the cluster status is set to rebooting . A cluster event is created when the reboot is completed. Any pending cluster modifications (see  ModifyCluster ) are applied at this reboot. For more information about managing clusters, go to Amazon Redshift Clusters in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reboot_cluster(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe cluster identifier.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --
Cluster (dict) --Describes a cluster.

ClusterIdentifier (string) --The unique identifier of the cluster.

NodeType (string) --The node type for the nodes in the cluster.

ClusterStatus (string) --The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --The connection endpoint.

Address (string) --The DNS address of the Cluster.

Port (integer) --The port that the database engine is listening on.



ClusterCreateTime (datetime) --The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

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

NodeType (string) --The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --The pending or in-progress change of the cluster type.

ClusterVersion (string) --The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --
Status (string) --Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

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

ApplyStatus (string) --A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --Describes a group of DeferredMaintenanceWindow objects.

(dict) --Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --Returns the value ClassicResize .

AllowCancelResize (boolean) --A boolean value indicating if the resize operation can be cancelled.










Exceptions

Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.ClusterNotFoundFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    Available - The cluster is available for queries.
    Unavailable - The cluster is not available for queries.
    Maintenance - The cluster is intermittently available for queries due to maintenance activities.
    Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
    Failed - The cluster failed and is not available for queries.
    
    """
    pass

def reset_cluster_parameter_group(ParameterGroupName=None, ResetAllParameters=None, Parameters=None):
    """
    Sets one or more parameters of the specified parameter group to their default values and sets the source values of the parameters to "engine-default". To reset the entire parameter group specify the ResetAllParameters parameter. For parameter changes to take effect you must reboot any associated clusters.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ParameterGroupName: [REQUIRED]\nThe name of the cluster parameter group to be reset.\n

    :type ResetAllParameters: boolean
    :param ResetAllParameters: If true , all parameters in the specified parameter group will be reset to their default values.\nDefault: true\n

    :type Parameters: list
    :param Parameters: An array of names of parameters to be reset. If ResetAllParameters option is not used, then at least one parameter name must be supplied.\nConstraints: A maximum of 20 parameters can be reset in a single request.\n\n(dict) --Describes a parameter in a cluster parameter group.\n\nParameterName (string) --The name of the parameter.\n\nParameterValue (string) --The value of the parameter.\n\nDescription (string) --A description of the parameter.\n\nSource (string) --The source of the parameter value, such as 'engine-default' or 'user'.\n\nDataType (string) --The data type of the parameter.\n\nAllowedValues (string) --The valid range of values for the parameter.\n\nApplyType (string) --Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .\n\nIsModifiable (boolean) --If true , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.\n\nMinimumEngineVersion (string) --The earliest engine version to which the parameter can apply.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ParameterGroupName': 'string',
    'ParameterGroupStatus': 'string'
}


Response Structure

(dict) --

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterGroupStatus (string) --
The status of the parameter group. For example, if you made a change to a parameter group name-value pair, then the change could be pending a reboot of an associated cluster.







Exceptions

Redshift.Client.exceptions.InvalidClusterParameterGroupStateFault
Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault


    :return: {
        'ParameterGroupName': 'string',
        'ParameterGroupStatus': 'string'
    }
    
    
    :returns: 
    Redshift.Client.exceptions.InvalidClusterParameterGroupStateFault
    Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
    
    """
    pass

def resize_cluster(ClusterIdentifier=None, ClusterType=None, NodeType=None, NumberOfNodes=None, Classic=None):
    """
    Changes the size of the cluster. You can change the cluster\'s type, or change the number or type of nodes. The default behavior is to use the elastic resize method. With an elastic resize, your cluster is available for read and write operations more quickly than with the classic resize method.
    Elastic resize operations have the following restrictions:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resize_cluster(
        ClusterIdentifier='string',
        ClusterType='string',
        NodeType='string',
        NumberOfNodes=123,
        Classic=True|False
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier for the cluster to resize.\n

    :type ClusterType: string
    :param ClusterType: The new cluster type for the specified cluster.

    :type NodeType: string
    :param NodeType: The new node type for the nodes you are adding. If not specified, the cluster\'s current node type is used.

    :type NumberOfNodes: integer
    :param NumberOfNodes: The new number of nodes for the cluster.

    :type Classic: boolean
    :param Classic: A boolean value indicating whether the resize operation is using the classic resize process. If you don\'t provide this parameter or set the value to false , the resize type is elastic.

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.NumberOfNodesQuotaExceededFault
Redshift.Client.exceptions.NumberOfNodesPerClusterLimitExceededFault
Redshift.Client.exceptions.InsufficientClusterCapacityFault
Redshift.Client.exceptions.UnsupportedOptionFault
Redshift.Client.exceptions.UnsupportedOperationFault
Redshift.Client.exceptions.UnauthorizedOperation
Redshift.Client.exceptions.LimitExceededFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    ClusterIdentifier (string) -- [REQUIRED]
    The unique identifier for the cluster to resize.
    
    ClusterType (string) -- The new cluster type for the specified cluster.
    NodeType (string) -- The new node type for the nodes you are adding. If not specified, the cluster\'s current node type is used.
    NumberOfNodes (integer) -- The new number of nodes for the cluster.
    Classic (boolean) -- A boolean value indicating whether the resize operation is using the classic resize process. If you don\'t provide this parameter or set the value to false , the resize type is elastic.
    
    """
    pass

def restore_from_cluster_snapshot(ClusterIdentifier=None, SnapshotIdentifier=None, SnapshotClusterIdentifier=None, Port=None, AvailabilityZone=None, AllowVersionUpgrade=None, ClusterSubnetGroupName=None, PubliclyAccessible=None, OwnerAccount=None, HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None, ElasticIp=None, ClusterParameterGroupName=None, ClusterSecurityGroups=None, VpcSecurityGroupIds=None, PreferredMaintenanceWindow=None, AutomatedSnapshotRetentionPeriod=None, ManualSnapshotRetentionPeriod=None, KmsKeyId=None, NodeType=None, EnhancedVpcRouting=None, AdditionalInfo=None, IamRoles=None, MaintenanceTrackName=None, SnapshotScheduleIdentifier=None, NumberOfNodes=None):
    """
    Creates a new cluster from a snapshot. By default, Amazon Redshift creates the resulting cluster with the same configuration as the original cluster from which the snapshot was created, except that the new cluster is created with the default cluster security and parameter groups. After Amazon Redshift creates the cluster, you can use the  ModifyCluster API to associate a different security group and different parameter group with the restored cluster. If you are using a DS node type, you can also choose to change to another DS node type of the same size during restore.
    If you restore a cluster into a VPC, you must provide a cluster subnet group where you want the cluster restored.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
        ManualSnapshotRetentionPeriod=123,
        KmsKeyId='string',
        NodeType='string',
        EnhancedVpcRouting=True|False,
        AdditionalInfo='string',
        IamRoles=[
            'string',
        ],
        MaintenanceTrackName='string',
        SnapshotScheduleIdentifier='string',
        NumberOfNodes=123
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe identifier of the cluster that will be created from restoring the snapshot.\nConstraints:\n\nMust contain from 1 to 63 alphanumeric characters or hyphens.\nAlphabetic characters must be lowercase.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\nMust be unique for all clusters within an AWS account.\n\n

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]\nThe name of the snapshot from which to create the new cluster. This parameter isn\'t case sensitive.\nExample: my-snapshot-id\n

    :type SnapshotClusterIdentifier: string
    :param SnapshotClusterIdentifier: The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

    :type Port: integer
    :param Port: The port number on which the cluster accepts connections.\nDefault: The same port as the original cluster.\nConstraints: Must be between 1115 and 65535 .\n

    :type AvailabilityZone: string
    :param AvailabilityZone: The Amazon EC2 Availability Zone in which to restore the cluster.\nDefault: A random, system-chosen Availability Zone.\nExample: us-east-2a\n

    :type AllowVersionUpgrade: boolean
    :param AllowVersionUpgrade: If true , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.\nDefault: true\n

    :type ClusterSubnetGroupName: string
    :param ClusterSubnetGroupName: The name of the subnet group where you want to cluster restored.\nA snapshot of cluster in VPC can be restored only in VPC. Therefore, you must provide subnet group name where you want the cluster restored.\n

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
    :param ClusterParameterGroupName: The name of the parameter group to be associated with this cluster.\nDefault: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to Working with Amazon Redshift Parameter Groups .\nConstraints:\n\nMust be 1 to 255 alphanumeric characters or hyphens.\nFirst character must be a letter.\nCannot end with a hyphen or contain two consecutive hyphens.\n\n

    :type ClusterSecurityGroups: list
    :param ClusterSecurityGroups: A list of security groups to be associated with this cluster.\nDefault: The default cluster security group for Amazon Redshift.\nCluster security groups only apply to clusters outside of VPCs.\n\n(string) --\n\n

    :type VpcSecurityGroupIds: list
    :param VpcSecurityGroupIds: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.\nDefault: The default VPC security group is associated with the cluster.\nVPC security groups only apply to clusters in VPCs.\n\n(string) --\n\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which automated cluster maintenance can occur.\nFormat: ddd:hh24:mi-ddd:hh24:mi\nDefault: The value selected for the cluster from which the snapshot was taken. For more information about the time blocks for each region, see Maintenance Windows in Amazon Redshift Cluster Management Guide.\nValid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun\nConstraints: Minimum 30-minute window.\n

    :type AutomatedSnapshotRetentionPeriod: integer
    :param AutomatedSnapshotRetentionPeriod: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with CreateClusterSnapshot .\nDefault: The value selected for the cluster from which the snapshot was taken.\nConstraints: Must be a value from 0 to 35.\n

    :type ManualSnapshotRetentionPeriod: integer
    :param ManualSnapshotRetentionPeriod: The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.\nThe value must be either -1 or an integer between 1 and 3,653.\n

    :type KmsKeyId: string
    :param KmsKeyId: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster that you restore from a shared snapshot.

    :type NodeType: string
    :param NodeType: The node type that the restored cluster will be provisioned with.\nDefault: The node type of the cluster from which the snapshot was taken. You can modify this if you are using any DS node type. In that case, you can choose to restore into another DS node type of the same size. For example, you can restore ds1.8xlarge into ds2.8xlarge, or ds1.xlarge into ds2.xlarge. If you have a DC instance type, you must restore into that same instance type and size. In other words, you can only restore a dc1.large instance type into another dc1.large instance type or dc2.large instance type. You can\'t restore dc1.8xlarge to dc2.8xlarge. First restore to a dc1.8xlarge cluster, then resize to a dc2.8large cluster. For more information about node types, see About Clusters and Nodes in the Amazon Redshift Cluster Management Guide .\n

    :type EnhancedVpcRouting: boolean
    :param EnhancedVpcRouting: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.\nIf this option is true , enhanced VPC routing is enabled.\nDefault: false\n

    :type AdditionalInfo: string
    :param AdditionalInfo: Reserved.

    :type IamRoles: list
    :param IamRoles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 10 IAM roles in a single request.\nA cluster can have up to 10 IAM roles associated at any time.\n\n(string) --\n\n

    :type MaintenanceTrackName: string
    :param MaintenanceTrackName: The name of the maintenance track for the restored cluster. When you take a snapshot, the snapshot inherits the MaintenanceTrack value from the cluster. The snapshot might be on a different track than the cluster that was the source for the snapshot. For example, suppose that you take a snapshot of a cluster that is on the current track and then change the cluster to be on the trailing track. In this case, the snapshot and the source cluster are on different tracks.

    :type SnapshotScheduleIdentifier: string
    :param SnapshotScheduleIdentifier: A unique identifier for the snapshot schedule.

    :type NumberOfNodes: integer
    :param NumberOfNodes: The number of nodes specified when provisioning the restored cluster.

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --

Cluster (dict) --
Describes a cluster.

ClusterIdentifier (string) --
The unique identifier of the cluster.

NodeType (string) --
The node type for the nodes in the cluster.

ClusterStatus (string) --
The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --
The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --
The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --
The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --
The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --
The connection endpoint.

Address (string) --
The DNS address of the Cluster.

Port (integer) --
The port that the database engine is listening on.



ClusterCreateTime (datetime) --
The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --
The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --
The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups (list) --
A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains ClusterSecurityGroup.Name and ClusterSecurityGroup.Status subelements.
Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the VpcSecurityGroups parameter.

(dict) --
Describes a cluster security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group.

Status (string) --
The status of the cluster security group.





VpcSecurityGroups (list) --
A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(dict) --
Describes the members of a VPC security group.

VpcSecurityGroupId (string) --
The identifier of the VPC security group.

Status (string) --
The status of the VPC security group.





ClusterParameterGroups (list) --
The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(dict) --
Describes the status of a parameter group.

ParameterGroupName (string) --
The name of the cluster parameter group.

ParameterApplyStatus (string) --
The status of parameter updates.

ClusterParameterStatusList (list) --
The list of parameter statuses.
For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

(dict) --
Describes the status of a parameter group.

ParameterName (string) --
The name of the parameter.

ParameterApplyStatus (string) --
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.
The following are possible statuses and descriptions.

in-sync : The parameter value is in sync with the database.
pending-reboot : The parameter value will be applied after the cluster reboots.
applying : The parameter value is being applied to the database.
invalid-parameter : Cannot apply the parameter value because it has an invalid value or syntax.
apply-deferred : The parameter contains static property changes. The changes are deferred until the cluster reboots.
apply-error : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
unknown-error : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.


ParameterApplyErrorDescription (string) --
The error that prevented the parameter from being applied to the database.









ClusterSubnetGroupName (string) --
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId (string) --
The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone (string) --
The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow (string) --
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues (dict) --
A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword (string) --
The pending or in-progress change of the master user password for the cluster.

NodeType (string) --
The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --
The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --
The pending or in-progress change of the cluster type.

ClusterVersion (string) --
The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --
The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --
The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --
The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --
The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --
A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --
The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --
A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --
A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --
A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --
The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --

Status (string) --
Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --
Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --
Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --
Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --
Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --
Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --
A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --
A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName (string) --
The name of the snapshot copy grant.



ClusterPublicKey (string) --
The public key for the cluster.

ClusterNodes (list) --
The nodes in the cluster.

(dict) --
The identifier of a node in a cluster.

NodeRole (string) --
Whether the node is a leader node or a compute node.

PrivateIPAddress (string) --
The private IP address of a node within a cluster.

PublicIPAddress (string) --
The public IP address of a node within a cluster.





ElasticIpStatus (dict) --
The status of the elastic IP (EIP) address.

ElasticIp (string) --
The elastic IP (EIP) address for the cluster.

Status (string) --
The status of the elastic IP (EIP) address.



ClusterRevisionNumber (string) --
The specific revision number of the database in the cluster.

Tags (list) --
The list of tags for the cluster.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





KmsKeyId (string) --
The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

IamRoles (list) --
A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

(dict) --
An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

IamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role, for example, arn:aws:iam::123456789012:role/RedshiftCopyUnload .

ApplyStatus (string) --
A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --
Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --
The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --
The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --
Describes a group of DeferredMaintenanceWindow objects.

(dict) --
Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --
A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --
A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --
A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --
A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --
The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --
The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --
The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --
The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --
Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --
Returns the value ClassicResize .

AllowCancelResize (boolean) --
A boolean value indicating if the resize operation can be cancelled.











Exceptions

Redshift.Client.exceptions.AccessToSnapshotDeniedFault
Redshift.Client.exceptions.ClusterAlreadyExistsFault
Redshift.Client.exceptions.ClusterSnapshotNotFoundFault
Redshift.Client.exceptions.ClusterQuotaExceededFault
Redshift.Client.exceptions.InsufficientClusterCapacityFault
Redshift.Client.exceptions.InvalidClusterSnapshotStateFault
Redshift.Client.exceptions.InvalidRestoreFault
Redshift.Client.exceptions.NumberOfNodesQuotaExceededFault
Redshift.Client.exceptions.NumberOfNodesPerClusterLimitExceededFault
Redshift.Client.exceptions.InvalidVPCNetworkStateFault
Redshift.Client.exceptions.InvalidClusterSubnetGroupStateFault
Redshift.Client.exceptions.InvalidSubnet
Redshift.Client.exceptions.ClusterSubnetGroupNotFoundFault
Redshift.Client.exceptions.UnauthorizedOperation
Redshift.Client.exceptions.HsmClientCertificateNotFoundFault
Redshift.Client.exceptions.HsmConfigurationNotFoundFault
Redshift.Client.exceptions.InvalidElasticIpFault
Redshift.Client.exceptions.ClusterParameterGroupNotFoundFault
Redshift.Client.exceptions.ClusterSecurityGroupNotFoundFault
Redshift.Client.exceptions.LimitExceededFault
Redshift.Client.exceptions.DependentServiceRequestThrottlingFault
Redshift.Client.exceptions.InvalidClusterTrackFault
Redshift.Client.exceptions.SnapshotScheduleNotFoundFault
Redshift.Client.exceptions.TagLimitExceededFault
Redshift.Client.exceptions.InvalidTagFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    available
    available, prep-for-resize
    available, resize-cleanup
    cancelling-resize
    creating
    deleting
    final-snapshot
    hardware-failure
    incompatible-hsm
    incompatible-network
    incompatible-parameters
    incompatible-restore
    modifying
    paused
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
    
    Exceptions
    
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
    :param ClusterIdentifier: [REQUIRED]\nThe identifier of the Amazon Redshift cluster to restore the table to.\n

    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]\nThe identifier of the snapshot to restore the table from. This snapshot must have been created from the Amazon Redshift cluster specified by the ClusterIdentifier parameter.\n

    :type SourceDatabaseName: string
    :param SourceDatabaseName: [REQUIRED]\nThe name of the source database that contains the table to restore from.\n

    :type SourceSchemaName: string
    :param SourceSchemaName: The name of the source schema that contains the table to restore from. If you do not specify a SourceSchemaName value, the default is public .

    :type SourceTableName: string
    :param SourceTableName: [REQUIRED]\nThe name of the source table to restore from.\n

    :type TargetDatabaseName: string
    :param TargetDatabaseName: The name of the database to restore the table to.

    :type TargetSchemaName: string
    :param TargetSchemaName: The name of the schema to restore the table to.

    :type NewTableName: string
    :param NewTableName: [REQUIRED]\nThe name of the table to create as a result of the current request.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

TableRestoreStatus (dict) --
Describes the status of a  RestoreTableFromClusterSnapshot operation.

TableRestoreRequestId (string) --
The unique identifier for the table restore request.

Status (string) --
A value that describes the current state of the table restore request.
Valid Values: SUCCEEDED , FAILED , CANCELED , PENDING , IN_PROGRESS

Message (string) --
A description of the status of the table restore request. Status values include SUCCEEDED , FAILED , CANCELED , PENDING , IN_PROGRESS .

RequestTime (datetime) --
The time that the table restore request was made, in Universal Coordinated Time (UTC).

ProgressInMegaBytes (integer) --
The amount of data restored to the new table so far, in megabytes (MB).

TotalDataInMegaBytes (integer) --
The total amount of data to restore to the new table, in megabytes (MB).

ClusterIdentifier (string) --
The identifier of the Amazon Redshift cluster that the table is being restored to.

SnapshotIdentifier (string) --
The identifier of the snapshot that the table is being restored from.

SourceDatabaseName (string) --
The name of the source database that contains the table being restored.

SourceSchemaName (string) --
The name of the source schema that contains the table being restored.

SourceTableName (string) --
The name of the source table being restored.

TargetDatabaseName (string) --
The name of the database to restore the table to.

TargetSchemaName (string) --
The name of the schema to restore the table to.

NewTableName (string) --
The name of the table to create as a result of the table restore request.









Exceptions

Redshift.Client.exceptions.ClusterSnapshotNotFoundFault
Redshift.Client.exceptions.InProgressTableRestoreQuotaExceededFault
Redshift.Client.exceptions.InvalidClusterSnapshotStateFault
Redshift.Client.exceptions.InvalidTableRestoreArgumentFault
Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.UnsupportedOperationFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterSnapshotNotFoundFault
    Redshift.Client.exceptions.InProgressTableRestoreQuotaExceededFault
    Redshift.Client.exceptions.InvalidClusterSnapshotStateFault
    Redshift.Client.exceptions.InvalidTableRestoreArgumentFault
    Redshift.Client.exceptions.ClusterNotFoundFault
    Redshift.Client.exceptions.InvalidClusterStateFault
    Redshift.Client.exceptions.UnsupportedOperationFault
    
    """
    pass

def resume_cluster(ClusterIdentifier=None):
    """
    Resumes a paused cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resume_cluster(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe identifier of the cluster to be resumed.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --
Cluster (dict) --Describes a cluster.

ClusterIdentifier (string) --The unique identifier of the cluster.

NodeType (string) --The node type for the nodes in the cluster.

ClusterStatus (string) --The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --The connection endpoint.

Address (string) --The DNS address of the Cluster.

Port (integer) --The port that the database engine is listening on.



ClusterCreateTime (datetime) --The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

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

NodeType (string) --The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --The pending or in-progress change of the cluster type.

ClusterVersion (string) --The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --
Status (string) --Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

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

ApplyStatus (string) --A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --Describes a group of DeferredMaintenanceWindow objects.

(dict) --Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --Returns the value ClassicResize .

AllowCancelResize (boolean) --A boolean value indicating if the resize operation can be cancelled.










Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.InvalidClusterStateFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    Available - The cluster is available for queries.
    Unavailable - The cluster is not available for queries.
    Maintenance - The cluster is intermittently available for queries due to maintenance activities.
    Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
    Failed - The cluster failed and is not available for queries.
    
    """
    pass

def revoke_cluster_security_group_ingress(ClusterSecurityGroupName=None, CIDRIP=None, EC2SecurityGroupName=None, EC2SecurityGroupOwnerId=None):
    """
    Revokes an ingress rule in an Amazon Redshift security group for a previously authorized IP range or Amazon EC2 security group. To add an ingress rule, see  AuthorizeClusterSecurityGroupIngress . For information about managing security groups, go to Amazon Redshift Cluster Security Groups in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.revoke_cluster_security_group_ingress(
        ClusterSecurityGroupName='string',
        CIDRIP='string',
        EC2SecurityGroupName='string',
        EC2SecurityGroupOwnerId='string'
    )
    
    
    :type ClusterSecurityGroupName: string
    :param ClusterSecurityGroupName: [REQUIRED]\nThe name of the security Group from which to revoke the ingress rule.\n

    :type CIDRIP: string
    :param CIDRIP: The IP range for which to revoke access. This range must be a valid Classless Inter-Domain Routing (CIDR) block of IP addresses. If CIDRIP is specified, EC2SecurityGroupName and EC2SecurityGroupOwnerId cannot be provided.

    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: The name of the EC2 Security Group whose access is to be revoked. If EC2SecurityGroupName is specified, EC2SecurityGroupOwnerId must also be provided and CIDRIP cannot be provided.

    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: The AWS account number of the owner of the security group specified in the EC2SecurityGroupName parameter. The AWS access key ID is not an acceptable value. If EC2SecurityGroupOwnerId is specified, EC2SecurityGroupName must also be provided. and CIDRIP cannot be provided.\nExample: 111122223333\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ClusterSecurityGroup (dict) --
Describes a security group.

ClusterSecurityGroupName (string) --
The name of the cluster security group to which the operation was applied.

Description (string) --
A description of the security group.

EC2SecurityGroups (list) --
A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.

(dict) --
Describes an Amazon EC2 security group.

Status (string) --
The status of the EC2 security group.

EC2SecurityGroupName (string) --
The name of the EC2 Security Group.

EC2SecurityGroupOwnerId (string) --
The AWS ID of the owner of the EC2 security group specified in the EC2SecurityGroupName field.

Tags (list) --
The list of tags for the EC2 security group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.









IPRanges (list) --
A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.

(dict) --
Describes an IP range used in a security group.

Status (string) --
The status of the IP range, for example, "authorized".

CIDRIP (string) --
The IP range in Classless Inter-Domain Routing (CIDR) notation.

Tags (list) --
The list of tags for the IP range.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.









Tags (list) --
The list of tags for the cluster security group.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.













Exceptions

Redshift.Client.exceptions.ClusterSecurityGroupNotFoundFault
Redshift.Client.exceptions.AuthorizationNotFoundFault
Redshift.Client.exceptions.InvalidClusterSecurityGroupStateFault


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
    
    
    :returns: 
    Redshift.Client.exceptions.ClusterSecurityGroupNotFoundFault
    Redshift.Client.exceptions.AuthorizationNotFoundFault
    Redshift.Client.exceptions.InvalidClusterSecurityGroupStateFault
    
    """
    pass

def revoke_snapshot_access(SnapshotIdentifier=None, SnapshotClusterIdentifier=None, AccountWithRestoreAccess=None):
    """
    Removes the ability of the specified AWS customer account to restore the specified snapshot. If the account is currently restoring the snapshot, the restore will run to completion.
    For more information about working with snapshots, go to Amazon Redshift Snapshots in the Amazon Redshift Cluster Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.revoke_snapshot_access(
        SnapshotIdentifier='string',
        SnapshotClusterIdentifier='string',
        AccountWithRestoreAccess='string'
    )
    
    
    :type SnapshotIdentifier: string
    :param SnapshotIdentifier: [REQUIRED]\nThe identifier of the snapshot that the account can no longer access.\n

    :type SnapshotClusterIdentifier: string
    :param SnapshotClusterIdentifier: The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

    :type AccountWithRestoreAccess: string
    :param AccountWithRestoreAccess: [REQUIRED]\nThe identifier of the AWS customer account that can no longer restore the specified snapshot.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'EnhancedVpcRouting': True|False,
        'MaintenanceTrackName': 'string',
        'ManualSnapshotRetentionPeriod': 123,
        'ManualSnapshotRemainingDays': 123,
        'SnapshotRetentionStartTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Snapshot (dict) --
Describes a snapshot.

SnapshotIdentifier (string) --
The snapshot identifier that is provided in the request.

ClusterIdentifier (string) --
The identifier of the cluster for which the snapshot was taken.

SnapshotCreateTime (datetime) --
The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.

Status (string) --
The snapshot status. The value of the status depends on the API operation used:

CreateClusterSnapshot and  CopyClusterSnapshot returns status as "creating".
DescribeClusterSnapshots returns status as "creating", "available", "final snapshot", or "failed".
DeleteClusterSnapshot returns status as "deleted".


Port (integer) --
The port that the cluster is listening on.

AvailabilityZone (string) --
The Availability Zone in which the cluster was created.

ClusterCreateTime (datetime) --
The time (UTC) when the cluster was originally created.

MasterUsername (string) --
The master user name for the cluster.

ClusterVersion (string) --
The version ID of the Amazon Redshift engine that is running on the cluster.

SnapshotType (string) --
The snapshot type. Snapshots created using  CreateClusterSnapshot and  CopyClusterSnapshot are of type "manual".

NodeType (string) --
The node type of the nodes in the cluster.

NumberOfNodes (integer) --
The number of nodes in the cluster.

DBName (string) --
The name of the database that was created when the cluster was created.

VpcId (string) --
The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.

Encrypted (boolean) --
If true , the data in the snapshot is encrypted at rest.

KmsKeyId (string) --
The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.

EncryptedWithHSM (boolean) --
A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. true indicates that the data is encrypted using HSM keys.

AccountsWithRestoreAccess (list) --
A list of the AWS customer accounts authorized to restore the snapshot. Returns null if no accounts are authorized. Visible only to the snapshot owner.

(dict) --
Describes an AWS customer account authorized to restore a snapshot.

AccountId (string) --
The identifier of an AWS customer account authorized to restore a snapshot.

AccountAlias (string) --
The identifier of an AWS support account authorized to restore a snapshot. For AWS support, the identifier is amazon-redshift-support .





OwnerAccount (string) --
For manual snapshots, the AWS customer account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.

TotalBackupSizeInMegaBytes (float) --
The size of the complete set of backup data that would be used to restore the cluster.

ActualIncrementalBackupSizeInMegaBytes (float) --
The size of the incremental backup.

BackupProgressInMegaBytes (float) --
The number of megabytes that have been transferred to the snapshot backup.

CurrentBackupRateInMegaBytesPerSecond (float) --
The number of megabytes per second being transferred to the snapshot backup. Returns 0 for a completed backup.

EstimatedSecondsToCompletion (integer) --
The estimate of the time remaining before the snapshot backup will complete. Returns 0 for a completed backup.

ElapsedTimeInSeconds (integer) --
The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.

SourceRegion (string) --
The source region from which the snapshot was copied.

Tags (list) --
The list of tags for the cluster snapshot.

(dict) --
A tag consisting of a name/value pair for a resource.

Key (string) --
The key, or name, for the resource tag.

Value (string) --
The value for the resource tag.





RestorableNodeTypes (list) --
The list of node types that this cluster snapshot is able to restore into.

(string) --


EnhancedVpcRouting (boolean) --
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --
The name of the maintenance track for the snapshot.

ManualSnapshotRetentionPeriod (integer) --
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

ManualSnapshotRemainingDays (integer) --
The number of days until a manual snapshot will pass its retention period.

SnapshotRetentionStartTime (datetime) --
A timestamp representing the start of the retention period for the snapshot.









Exceptions

Redshift.Client.exceptions.AccessToSnapshotDeniedFault
Redshift.Client.exceptions.AuthorizationNotFoundFault
Redshift.Client.exceptions.ClusterSnapshotNotFoundFault


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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'ManualSnapshotRetentionPeriod': 123,
            'ManualSnapshotRemainingDays': 123,
            'SnapshotRetentionStartTime': datetime(2015, 1, 1)
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
    
    Exceptions
    
    :example: response = client.rotate_encryption_key(
        ClusterIdentifier='string'
    )
    
    
    :type ClusterIdentifier: string
    :param ClusterIdentifier: [REQUIRED]\nThe unique identifier of the cluster that you want to rotate the encryption keys for.\nConstraints: Must be the name of valid cluster that has encryption enabled.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Cluster': {
        'ClusterIdentifier': 'string',
        'NodeType': 'string',
        'ClusterStatus': 'string',
        'ClusterAvailabilityStatus': 'string',
        'ModifyStatus': 'string',
        'MasterUsername': 'string',
        'DBName': 'string',
        'Endpoint': {
            'Address': 'string',
            'Port': 123
        },
        'ClusterCreateTime': datetime(2015, 1, 1),
        'AutomatedSnapshotRetentionPeriod': 123,
        'ManualSnapshotRetentionPeriod': 123,
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
            'EnhancedVpcRouting': True|False,
            'MaintenanceTrackName': 'string',
            'EncryptionType': 'string'
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
        'DataTransferProgress': {
            'Status': 'string',
            'CurrentRateInMegaBytesPerSecond': 123.0,
            'TotalDataInMegaBytes': 123,
            'DataTransferredInMegaBytes': 123,
            'EstimatedTimeToCompletionInSeconds': 123,
            'ElapsedTimeInSeconds': 123
        },
        'HsmStatus': {
            'HsmClientCertificateIdentifier': 'string',
            'HsmConfigurationIdentifier': 'string',
            'Status': 'string'
        },
        'ClusterSnapshotCopyStatus': {
            'DestinationRegion': 'string',
            'RetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
        ],
        'PendingActions': [
            'string',
        ],
        'MaintenanceTrackName': 'string',
        'ElasticResizeNumberOfNodeOptions': 'string',
        'DeferredMaintenanceWindows': [
            {
                'DeferMaintenanceIdentifier': 'string',
                'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                'DeferMaintenanceEndTime': datetime(2015, 1, 1)
            },
        ],
        'SnapshotScheduleIdentifier': 'string',
        'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
        'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
        'ExpectedNextSnapshotScheduleTimeStatus': 'string',
        'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
        'ResizeInfo': {
            'ResizeType': 'string',
            'AllowCancelResize': True|False
        }
    }
}


Response Structure

(dict) --
Cluster (dict) --Describes a cluster.

ClusterIdentifier (string) --The unique identifier of the cluster.

NodeType (string) --The node type for the nodes in the cluster.

ClusterStatus (string) --The current state of the cluster. Possible values are the following:

available
available, prep-for-resize
available, resize-cleanup
cancelling-resize
creating
deleting
final-snapshot
hardware-failure
incompatible-hsm
incompatible-network
incompatible-parameters
incompatible-restore
modifying
paused
rebooting
renaming
resizing
rotating-keys
storage-full
updating-hsm


ClusterAvailabilityStatus (string) --The availability status of the cluster for queries. Possible values are the following:

Available - The cluster is available for queries.
Unavailable - The cluster is not available for queries.
Maintenance - The cluster is intermittently available for queries due to maintenance activities.
Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
Failed - The cluster failed and is not available for queries.


ModifyStatus (string) --The status of a modify operation, if any, initiated for the cluster.

MasterUsername (string) --The master user name for the cluster. This name is used to connect to the database that is specified in the DBName parameter.

DBName (string) --The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named dev dev was created by default.

Endpoint (dict) --The connection endpoint.

Address (string) --The DNS address of the Cluster.

Port (integer) --The port that the database engine is listening on.



ClusterCreateTime (datetime) --The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod (integer) --The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod (integer) --The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn\'t change the retention period of existing snapshots.
The value must be either -1 or an integer between 1 and 3,653.

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

NodeType (string) --The pending or in-progress change of the cluster\'s node type.

NumberOfNodes (integer) --The pending or in-progress change of the number of nodes in the cluster.

ClusterType (string) --The pending or in-progress change of the cluster type.

ClusterVersion (string) --The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod (integer) --The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier (string) --The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible (boolean) --The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting (boolean) --An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
If this option is true , enhanced VPC routing is enabled.
Default: false

MaintenanceTrackName (string) --The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType (string) --The encryption type for a cluster. Possible values are: KMS and None. For the China region the possible values are None, and Legacy.



ClusterVersion (string) --The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade (boolean) --A boolean value that, if true , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes (integer) --The number of compute nodes in the cluster.

PubliclyAccessible (boolean) --A boolean value that, if true , indicates that the cluster can be accessed from a public network.

Encrypted (boolean) --A boolean value that, if true , indicates that data in the cluster is encrypted at rest.

RestoreStatus (dict) --A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status (string) --The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond (float) --The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 and DS2 node types.

SnapshotSizeInMegaBytes (integer) --The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 and DS2 node types.

ProgressInMegaBytes (integer) --The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 and DS2 node types.

ElapsedTimeInSeconds (integer) --The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 and DS2 node types.

EstimatedTimeToCompletionInSeconds (integer) --The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 and DS2 node types.



DataTransferProgress (dict) --
Status (string) --Describes the status of the cluster. While the transfer is in progress the status is transferringdata .

CurrentRateInMegaBytesPerSecond (float) --Describes the data transfer rate in MB\'s per second.

TotalDataInMegaBytes (integer) --Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes (integer) --Describes the total amount of data that has been transfered in MB\'s.

EstimatedTimeToCompletionInSeconds (integer) --Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds (integer) --Describes the number of seconds that have elapsed during the data transfer.



HsmStatus (dict) --A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.
Values: active, applying

HsmClientCertificateIdentifier (string) --Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier (string) --Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status (string) --Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Values: active, applying



ClusterSnapshotCopyStatus (dict) --A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion (string) --The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod (integer) --The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.

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

ApplyStatus (string) --A value that describes the status of the IAM role\'s association with an Amazon Redshift cluster.
The following are possible statuses and descriptions.

in-sync : The role is available for use by the cluster.
adding : The role is in the process of being associated with the cluster.
removing : The role is in the process of being disassociated with the cluster.






PendingActions (list) --Cluster operations that are waiting to be started.

(string) --


MaintenanceTrackName (string) --The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions (string) --The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows (list) --Describes a group of DeferredMaintenanceWindow objects.

(dict) --Describes a deferred maintenance window

DeferMaintenanceIdentifier (string) --A unique identifier for the maintenance window.

DeferMaintenanceStartTime (datetime) --A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime (datetime) --A timestamp for the end of the time period when we defer maintenance.





SnapshotScheduleIdentifier (string) --A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState (string) --The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime (datetime) --The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus (string) --The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

OnTrack - The next snapshot is expected to be taken on time.
Pending - The next snapshot is pending to be taken.


NextMaintenanceWindowStartTime (datetime) --The date and time in UTC when system maintenance can begin.

ResizeInfo (dict) --Returns the following:

AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
ResizeType: Returns ClassicResize


ResizeType (string) --Returns the value ClassicResize .

AllowCancelResize (boolean) --A boolean value indicating if the resize operation can be cancelled.










Exceptions

Redshift.Client.exceptions.ClusterNotFoundFault
Redshift.Client.exceptions.InvalidClusterStateFault
Redshift.Client.exceptions.DependentServiceRequestThrottlingFault


    :return: {
        'Cluster': {
            'ClusterIdentifier': 'string',
            'NodeType': 'string',
            'ClusterStatus': 'string',
            'ClusterAvailabilityStatus': 'string',
            'ModifyStatus': 'string',
            'MasterUsername': 'string',
            'DBName': 'string',
            'Endpoint': {
                'Address': 'string',
                'Port': 123
            },
            'ClusterCreateTime': datetime(2015, 1, 1),
            'AutomatedSnapshotRetentionPeriod': 123,
            'ManualSnapshotRetentionPeriod': 123,
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
                'EnhancedVpcRouting': True|False,
                'MaintenanceTrackName': 'string',
                'EncryptionType': 'string'
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
            'DataTransferProgress': {
                'Status': 'string',
                'CurrentRateInMegaBytesPerSecond': 123.0,
                'TotalDataInMegaBytes': 123,
                'DataTransferredInMegaBytes': 123,
                'EstimatedTimeToCompletionInSeconds': 123,
                'ElapsedTimeInSeconds': 123
            },
            'HsmStatus': {
                'HsmClientCertificateIdentifier': 'string',
                'HsmConfigurationIdentifier': 'string',
                'Status': 'string'
            },
            'ClusterSnapshotCopyStatus': {
                'DestinationRegion': 'string',
                'RetentionPeriod': 123,
                'ManualSnapshotRetentionPeriod': 123,
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
            ],
            'PendingActions': [
                'string',
            ],
            'MaintenanceTrackName': 'string',
            'ElasticResizeNumberOfNodeOptions': 'string',
            'DeferredMaintenanceWindows': [
                {
                    'DeferMaintenanceIdentifier': 'string',
                    'DeferMaintenanceStartTime': datetime(2015, 1, 1),
                    'DeferMaintenanceEndTime': datetime(2015, 1, 1)
                },
            ],
            'SnapshotScheduleIdentifier': 'string',
            'SnapshotScheduleState': 'MODIFYING'|'ACTIVE'|'FAILED',
            'ExpectedNextSnapshotScheduleTime': datetime(2015, 1, 1),
            'ExpectedNextSnapshotScheduleTimeStatus': 'string',
            'NextMaintenanceWindowStartTime': datetime(2015, 1, 1),
            'ResizeInfo': {
                'ResizeType': 'string',
                'AllowCancelResize': True|False
            }
        }
    }
    
    
    :returns: 
    Available - The cluster is available for queries.
    Unavailable - The cluster is not available for queries.
    Maintenance - The cluster is intermittently available for queries due to maintenance activities.
    Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
    Failed - The cluster failed and is not available for queries.
    
    """
    pass

