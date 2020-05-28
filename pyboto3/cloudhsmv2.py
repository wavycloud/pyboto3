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

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def copy_backup_to_region(DestinationRegion=None, BackupId=None, TagList=None):
    """
    Copy an AWS CloudHSM cluster backup to a different region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.copy_backup_to_region(
        DestinationRegion='string',
        BackupId='string',
        TagList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DestinationRegion: string
    :param DestinationRegion: [REQUIRED]\nThe AWS region that will contain your copied CloudHSM cluster backup.\n

    :type BackupId: string
    :param BackupId: [REQUIRED]\nThe ID of the backup that will be copied to the destination region.\n

    :type TagList: list
    :param TagList: \n(dict) --Contains a tag. A tag is a key-value pair.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DestinationBackup': {
        'CreateTimestamp': datetime(2015, 1, 1),
        'SourceRegion': 'string',
        'SourceBackup': 'string',
        'SourceCluster': 'string'
    }
}


Response Structure

(dict) --

DestinationBackup (dict) --
Information on the backup that will be copied to the destination region, including CreateTimestamp, SourceBackup, SourceCluster, and Source Region. CreateTimestamp of the destination backup will be the same as that of the source backup.
You will need to use the sourceBackupID returned in this operation to use the  DescribeBackups operation on the backup that will be copied to the destination region.

CreateTimestamp (datetime) --
The date and time when both the source backup was created.

SourceRegion (string) --
The AWS region that contains the source backup from which the new backup was copied.

SourceBackup (string) --
The identifier (ID) of the source backup from which the new backup was copied.

SourceCluster (string) --
The identifier (ID) of the cluster containing the source backup from which the new backup was copied.









Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmTagException


    :return: {
        'DestinationBackup': {
            'CreateTimestamp': datetime(2015, 1, 1),
            'SourceRegion': 'string',
            'SourceBackup': 'string',
            'SourceCluster': 'string'
        }
    }
    
    
    :returns: 
    CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
    CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
    CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
    CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
    CloudHSMV2.Client.exceptions.CloudHsmServiceException
    CloudHSMV2.Client.exceptions.CloudHsmTagException
    
    """
    pass

def create_cluster(SubnetIds=None, HsmType=None, SourceBackupId=None, TagList=None):
    """
    Creates a new AWS CloudHSM cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_cluster(
        SubnetIds=[
            'string',
        ],
        HsmType='string',
        SourceBackupId='string',
        TagList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nThe identifiers (IDs) of the subnets where you are creating the cluster. You must specify at least one subnet. If you specify multiple subnets, they must meet the following criteria:\n\nAll subnets must be in the same virtual private cloud (VPC).\nYou can specify only one subnet per Availability Zone.\n\n\n(string) --\n\n

    :type HsmType: string
    :param HsmType: [REQUIRED]\nThe type of HSM to use in the cluster. Currently the only allowed value is hsm1.medium .\n

    :type SourceBackupId: string
    :param SourceBackupId: The identifier (ID) of the cluster backup to restore. Use this value to restore the cluster from a backup instead of creating a new cluster. To find the backup ID, use DescribeBackups .

    :type TagList: list
    :param TagList: \n(dict) --Contains a tag. A tag is a key-value pair.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Cluster': {
        'BackupPolicy': 'DEFAULT',
        'ClusterId': 'string',
        'CreateTimestamp': datetime(2015, 1, 1),
        'Hsms': [
            {
                'AvailabilityZone': 'string',
                'ClusterId': 'string',
                'SubnetId': 'string',
                'EniId': 'string',
                'EniIp': 'string',
                'HsmId': 'string',
                'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
                'StateMessage': 'string'
            },
        ],
        'HsmType': 'string',
        'PreCoPassword': 'string',
        'SecurityGroup': 'string',
        'SourceBackupId': 'string',
        'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
        'StateMessage': 'string',
        'SubnetMapping': {
            'string': 'string'
        },
        'VpcId': 'string',
        'Certificates': {
            'ClusterCsr': 'string',
            'HsmCertificate': 'string',
            'AwsHardwareCertificate': 'string',
            'ManufacturerHardwareCertificate': 'string',
            'ClusterCertificate': 'string'
        },
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Cluster (dict) --
Information about the cluster that was created.

BackupPolicy (string) --
The cluster\'s backup policy.

ClusterId (string) --
The cluster\'s identifier (ID).

CreateTimestamp (datetime) --
The date and time when the cluster was created.

Hsms (list) --
Contains information about the HSMs in the cluster.

(dict) --
Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

AvailabilityZone (string) --
The Availability Zone that contains the HSM.

ClusterId (string) --
The identifier (ID) of the cluster that contains the HSM.

SubnetId (string) --
The subnet that contains the HSM\'s elastic network interface (ENI).

EniId (string) --
The identifier (ID) of the HSM\'s elastic network interface (ENI).

EniIp (string) --
The IP address of the HSM\'s elastic network interface (ENI).

HsmId (string) --
The HSM\'s identifier (ID).

State (string) --
The HSM\'s state.

StateMessage (string) --
A description of the HSM\'s state.





HsmType (string) --
The type of HSM that the cluster contains.

PreCoPassword (string) --
The default password for the cluster\'s Pre-Crypto Officer (PRECO) user.

SecurityGroup (string) --
The identifier (ID) of the cluster\'s security group.

SourceBackupId (string) --
The identifier (ID) of the backup used to create the cluster. This value exists only when the cluster was created from a backup.

State (string) --
The cluster\'s state.

StateMessage (string) --
A description of the cluster\'s state.

SubnetMapping (dict) --
A map from availability zone to the cluster\xe2\x80\x99s subnet in that availability zone.

(string) --
(string) --




VpcId (string) --
The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

Certificates (dict) --
Contains one or more certificates or a certificate signing request (CSR).

ClusterCsr (string) --
The cluster\'s certificate signing request (CSR). The CSR exists only when the cluster\'s state is UNINITIALIZED .

HsmCertificate (string) --
The HSM certificate issued (signed) by the HSM hardware.

AwsHardwareCertificate (string) --
The HSM hardware certificate issued (signed) by AWS CloudHSM.

ManufacturerHardwareCertificate (string) --
The HSM hardware certificate issued (signed) by the hardware manufacturer.

ClusterCertificate (string) --
The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster\'s owner.



TagList (list) --

(dict) --
Contains a tag. A tag is a key-value pair.

Key (string) --
The key of the tag.

Value (string) --
The value of the tag.













Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmTagException


    :return: {
        'Cluster': {
            'BackupPolicy': 'DEFAULT',
            'ClusterId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'Hsms': [
                {
                    'AvailabilityZone': 'string',
                    'ClusterId': 'string',
                    'SubnetId': 'string',
                    'EniId': 'string',
                    'EniIp': 'string',
                    'HsmId': 'string',
                    'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
                    'StateMessage': 'string'
                },
            ],
            'HsmType': 'string',
            'PreCoPassword': 'string',
            'SecurityGroup': 'string',
            'SourceBackupId': 'string',
            'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
            'StateMessage': 'string',
            'SubnetMapping': {
                'string': 'string'
            },
            'VpcId': 'string',
            'Certificates': {
                'ClusterCsr': 'string',
                'HsmCertificate': 'string',
                'AwsHardwareCertificate': 'string',
                'ManufacturerHardwareCertificate': 'string',
                'ClusterCertificate': 'string'
            },
            'TagList': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_hsm(ClusterId=None, AvailabilityZone=None, IpAddress=None):
    """
    Creates a new hardware security module (HSM) in the specified AWS CloudHSM cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_hsm(
        ClusterId='string',
        AvailabilityZone='string',
        IpAddress='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe identifier (ID) of the HSM\'s cluster. To find the cluster ID, use DescribeClusters .\n

    :type AvailabilityZone: string
    :param AvailabilityZone: [REQUIRED]\nThe Availability Zone where you are creating the HSM. To find the cluster\'s Availability Zones, use DescribeClusters .\n

    :type IpAddress: string
    :param IpAddress: The HSM\'s IP address. If you specify an IP address, use an available address from the subnet that maps to the Availability Zone where you are creating the HSM. If you don\'t specify an IP address, one is chosen for you from that subnet.

    :rtype: dict

ReturnsResponse Syntax
{
    'Hsm': {
        'AvailabilityZone': 'string',
        'ClusterId': 'string',
        'SubnetId': 'string',
        'EniId': 'string',
        'EniIp': 'string',
        'HsmId': 'string',
        'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
        'StateMessage': 'string'
    }
}


Response Structure

(dict) --

Hsm (dict) --
Information about the HSM that was created.

AvailabilityZone (string) --
The Availability Zone that contains the HSM.

ClusterId (string) --
The identifier (ID) of the cluster that contains the HSM.

SubnetId (string) --
The subnet that contains the HSM\'s elastic network interface (ENI).

EniId (string) --
The identifier (ID) of the HSM\'s elastic network interface (ENI).

EniIp (string) --
The IP address of the HSM\'s elastic network interface (ENI).

HsmId (string) --
The HSM\'s identifier (ID).

State (string) --
The HSM\'s state.

StateMessage (string) --
A description of the HSM\'s state.









Exceptions

CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException


    :return: {
        'Hsm': {
            'AvailabilityZone': 'string',
            'ClusterId': 'string',
            'SubnetId': 'string',
            'EniId': 'string',
            'EniIp': 'string',
            'HsmId': 'string',
            'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
            'StateMessage': 'string'
        }
    }
    
    
    :returns: 
    CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
    CloudHSMV2.Client.exceptions.CloudHsmServiceException
    CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
    CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
    CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
    
    """
    pass

def delete_backup(BackupId=None):
    """
    Deletes a specified AWS CloudHSM backup. A backup can be restored up to 7 days after the DeleteBackup request is made. For more information on restoring a backup, see  RestoreBackup .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backup(
        BackupId='string'
    )
    
    
    :type BackupId: string
    :param BackupId: [REQUIRED]\nThe ID of the backup to be deleted. To find the ID of a backup, use the DescribeBackups operation.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Backup': {
        'BackupId': 'string',
        'BackupState': 'CREATE_IN_PROGRESS'|'READY'|'DELETED'|'PENDING_DELETION',
        'ClusterId': 'string',
        'CreateTimestamp': datetime(2015, 1, 1),
        'CopyTimestamp': datetime(2015, 1, 1),
        'SourceRegion': 'string',
        'SourceBackup': 'string',
        'SourceCluster': 'string',
        'DeleteTimestamp': datetime(2015, 1, 1),
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Backup (dict) --Information on the Backup object deleted.

BackupId (string) --The identifier (ID) of the backup.

BackupState (string) --The state of the backup.

ClusterId (string) --The identifier (ID) of the cluster that was backed up.

CreateTimestamp (datetime) --The date and time when the backup was created.

CopyTimestamp (datetime) --The date and time when the backup was copied from a source backup.

SourceRegion (string) --The AWS region that contains the source backup from which the new backup was copied.

SourceBackup (string) --The identifier (ID) of the source backup from which the new backup was copied.

SourceCluster (string) --The identifier (ID) of the cluster containing the source backup from which the new backup was copied. .

DeleteTimestamp (datetime) --The date and time when the backup will be permanently deleted.

TagList (list) --
(dict) --Contains a tag. A tag is a key-value pair.

Key (string) --The key of the tag.

Value (string) --The value of the tag.












Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException


    :return: {
        'Backup': {
            'BackupId': 'string',
            'BackupState': 'CREATE_IN_PROGRESS'|'READY'|'DELETED'|'PENDING_DELETION',
            'ClusterId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'CopyTimestamp': datetime(2015, 1, 1),
            'SourceRegion': 'string',
            'SourceBackup': 'string',
            'SourceCluster': 'string',
            'DeleteTimestamp': datetime(2015, 1, 1),
            'TagList': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def delete_cluster(ClusterId=None):
    """
    Deletes the specified AWS CloudHSM cluster. Before you can delete a cluster, you must delete all HSMs in the cluster. To see if the cluster contains any HSMs, use  DescribeClusters . To delete an HSM, use  DeleteHsm .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cluster(
        ClusterId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe identifier (ID) of the cluster that you are deleting. To find the cluster ID, use DescribeClusters .\n

    :rtype: dict
ReturnsResponse Syntax{
    'Cluster': {
        'BackupPolicy': 'DEFAULT',
        'ClusterId': 'string',
        'CreateTimestamp': datetime(2015, 1, 1),
        'Hsms': [
            {
                'AvailabilityZone': 'string',
                'ClusterId': 'string',
                'SubnetId': 'string',
                'EniId': 'string',
                'EniIp': 'string',
                'HsmId': 'string',
                'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
                'StateMessage': 'string'
            },
        ],
        'HsmType': 'string',
        'PreCoPassword': 'string',
        'SecurityGroup': 'string',
        'SourceBackupId': 'string',
        'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
        'StateMessage': 'string',
        'SubnetMapping': {
            'string': 'string'
        },
        'VpcId': 'string',
        'Certificates': {
            'ClusterCsr': 'string',
            'HsmCertificate': 'string',
            'AwsHardwareCertificate': 'string',
            'ManufacturerHardwareCertificate': 'string',
            'ClusterCertificate': 'string'
        },
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Cluster (dict) --Information about the cluster that was deleted.

BackupPolicy (string) --The cluster\'s backup policy.

ClusterId (string) --The cluster\'s identifier (ID).

CreateTimestamp (datetime) --The date and time when the cluster was created.

Hsms (list) --Contains information about the HSMs in the cluster.

(dict) --Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

AvailabilityZone (string) --The Availability Zone that contains the HSM.

ClusterId (string) --The identifier (ID) of the cluster that contains the HSM.

SubnetId (string) --The subnet that contains the HSM\'s elastic network interface (ENI).

EniId (string) --The identifier (ID) of the HSM\'s elastic network interface (ENI).

EniIp (string) --The IP address of the HSM\'s elastic network interface (ENI).

HsmId (string) --The HSM\'s identifier (ID).

State (string) --The HSM\'s state.

StateMessage (string) --A description of the HSM\'s state.





HsmType (string) --The type of HSM that the cluster contains.

PreCoPassword (string) --The default password for the cluster\'s Pre-Crypto Officer (PRECO) user.

SecurityGroup (string) --The identifier (ID) of the cluster\'s security group.

SourceBackupId (string) --The identifier (ID) of the backup used to create the cluster. This value exists only when the cluster was created from a backup.

State (string) --The cluster\'s state.

StateMessage (string) --A description of the cluster\'s state.

SubnetMapping (dict) --A map from availability zone to the cluster\xe2\x80\x99s subnet in that availability zone.

(string) --
(string) --




VpcId (string) --The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

Certificates (dict) --Contains one or more certificates or a certificate signing request (CSR).

ClusterCsr (string) --The cluster\'s certificate signing request (CSR). The CSR exists only when the cluster\'s state is UNINITIALIZED .

HsmCertificate (string) --The HSM certificate issued (signed) by the HSM hardware.

AwsHardwareCertificate (string) --The HSM hardware certificate issued (signed) by AWS CloudHSM.

ManufacturerHardwareCertificate (string) --The HSM hardware certificate issued (signed) by the hardware manufacturer.

ClusterCertificate (string) --The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster\'s owner.



TagList (list) --
(dict) --Contains a tag. A tag is a key-value pair.

Key (string) --The key of the tag.

Value (string) --The value of the tag.












Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmTagException


    :return: {
        'Cluster': {
            'BackupPolicy': 'DEFAULT',
            'ClusterId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'Hsms': [
                {
                    'AvailabilityZone': 'string',
                    'ClusterId': 'string',
                    'SubnetId': 'string',
                    'EniId': 'string',
                    'EniIp': 'string',
                    'HsmId': 'string',
                    'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
                    'StateMessage': 'string'
                },
            ],
            'HsmType': 'string',
            'PreCoPassword': 'string',
            'SecurityGroup': 'string',
            'SourceBackupId': 'string',
            'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
            'StateMessage': 'string',
            'SubnetMapping': {
                'string': 'string'
            },
            'VpcId': 'string',
            'Certificates': {
                'ClusterCsr': 'string',
                'HsmCertificate': 'string',
                'AwsHardwareCertificate': 'string',
                'ManufacturerHardwareCertificate': 'string',
                'ClusterCertificate': 'string'
            },
            'TagList': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
    CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
    CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
    CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
    CloudHSMV2.Client.exceptions.CloudHsmServiceException
    CloudHSMV2.Client.exceptions.CloudHsmTagException
    
    """
    pass

def delete_hsm(ClusterId=None, HsmId=None, EniId=None, EniIp=None):
    """
    Deletes the specified HSM. To specify an HSM, you can use its identifier (ID), the IP address of the HSM\'s elastic network interface (ENI), or the ID of the HSM\'s ENI. You need to specify only one of these values. To find these values, use  DescribeClusters .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_hsm(
        ClusterId='string',
        HsmId='string',
        EniId='string',
        EniIp='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe identifier (ID) of the cluster that contains the HSM that you are deleting.\n

    :type HsmId: string
    :param HsmId: The identifier (ID) of the HSM that you are deleting.

    :type EniId: string
    :param EniId: The identifier (ID) of the elastic network interface (ENI) of the HSM that you are deleting.

    :type EniIp: string
    :param EniIp: The IP address of the elastic network interface (ENI) of the HSM that you are deleting.

    :rtype: dict

ReturnsResponse Syntax
{
    'HsmId': 'string'
}


Response Structure

(dict) --

HsmId (string) --
The identifier (ID) of the HSM that was deleted.







Exceptions

CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException


    :return: {
        'HsmId': 'string'
    }
    
    
    :returns: 
    CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
    CloudHSMV2.Client.exceptions.CloudHsmServiceException
    CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
    CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
    CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
    
    """
    pass

def describe_backups(NextToken=None, MaxResults=None, Filters=None, SortAscending=None):
    """
    Gets information about backups of AWS CloudHSM clusters.
    This is a paginated operation, which means that each response might contain only a subset of all the backups. When the response contains only a subset of backups, it includes a NextToken value. Use this value in a subsequent DescribeBackups request to get more backups. When you receive a response with no NextToken (or an empty or null value), that means there are no more backups to get.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_backups(
        NextToken='string',
        MaxResults=123,
        Filters={
            'string': [
                'string',
            ]
        },
        SortAscending=True|False
    )
    
    
    :type NextToken: string
    :param NextToken: The NextToken value that you received in the previous response. Use this value to get more backups.

    :type MaxResults: integer
    :param MaxResults: The maximum number of backups to return in the response. When there are more backups than the number you specify, the response contains a NextToken value.

    :type Filters: dict
    :param Filters: One or more filters to limit the items returned in the response.\nUse the backupIds filter to return only the specified backups. Specify backups by their backup identifier (ID).\nUse the sourceBackupIds filter to return only the backups created from a source backup. The sourceBackupID of a source backup is returned by the CopyBackupToRegion operation.\nUse the clusterIds filter to return only the backups for the specified clusters. Specify clusters by their cluster identifier (ID).\nUse the states filter to return only backups that match the specified state.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type SortAscending: boolean
    :param SortAscending: Designates whether or not to sort the return backups by ascending chronological order of generation.

    :rtype: dict

ReturnsResponse Syntax
{
    'Backups': [
        {
            'BackupId': 'string',
            'BackupState': 'CREATE_IN_PROGRESS'|'READY'|'DELETED'|'PENDING_DELETION',
            'ClusterId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'CopyTimestamp': datetime(2015, 1, 1),
            'SourceRegion': 'string',
            'SourceBackup': 'string',
            'SourceCluster': 'string',
            'DeleteTimestamp': datetime(2015, 1, 1),
            'TagList': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Backups (list) --
A list of backups.

(dict) --
Contains information about a backup of an AWS CloudHSM cluster. All backup objects contain the BackupId, BackupState, ClusterId, and CreateTimestamp parameters. Backups that were copied into a destination region additionally contain the CopyTimestamp, SourceBackup, SourceCluster, and SourceRegion paramters. A backup that is pending deletion will include the DeleteTimestamp parameter.

BackupId (string) --
The identifier (ID) of the backup.

BackupState (string) --
The state of the backup.

ClusterId (string) --
The identifier (ID) of the cluster that was backed up.

CreateTimestamp (datetime) --
The date and time when the backup was created.

CopyTimestamp (datetime) --
The date and time when the backup was copied from a source backup.

SourceRegion (string) --
The AWS region that contains the source backup from which the new backup was copied.

SourceBackup (string) --
The identifier (ID) of the source backup from which the new backup was copied.

SourceCluster (string) --
The identifier (ID) of the cluster containing the source backup from which the new backup was copied. .

DeleteTimestamp (datetime) --
The date and time when the backup will be permanently deleted.

TagList (list) --

(dict) --
Contains a tag. A tag is a key-value pair.

Key (string) --
The key of the tag.

Value (string) --
The value of the tag.









NextToken (string) --
An opaque string that indicates that the response contains only a subset of backups. Use this value in a subsequent DescribeBackups request to get more backups.







Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmTagException


    :return: {
        'Backups': [
            {
                'BackupId': 'string',
                'BackupState': 'CREATE_IN_PROGRESS'|'READY'|'DELETED'|'PENDING_DELETION',
                'ClusterId': 'string',
                'CreateTimestamp': datetime(2015, 1, 1),
                'CopyTimestamp': datetime(2015, 1, 1),
                'SourceRegion': 'string',
                'SourceBackup': 'string',
                'SourceCluster': 'string',
                'DeleteTimestamp': datetime(2015, 1, 1),
                'TagList': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
    CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
    CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
    CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
    CloudHSMV2.Client.exceptions.CloudHsmServiceException
    CloudHSMV2.Client.exceptions.CloudHsmTagException
    
    """
    pass

def describe_clusters(Filters=None, NextToken=None, MaxResults=None):
    """
    Gets information about AWS CloudHSM clusters.
    This is a paginated operation, which means that each response might contain only a subset of all the clusters. When the response contains only a subset of clusters, it includes a NextToken value. Use this value in a subsequent DescribeClusters request to get more clusters. When you receive a response with no NextToken (or an empty or null value), that means there are no more clusters to get.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_clusters(
        Filters={
            'string': [
                'string',
            ]
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: dict
    :param Filters: One or more filters to limit the items returned in the response.\nUse the clusterIds filter to return only the specified clusters. Specify clusters by their cluster identifier (ID).\nUse the vpcIds filter to return only the clusters in the specified virtual private clouds (VPCs). Specify VPCs by their VPC identifier (ID).\nUse the states filter to return only clusters that match the specified state.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The NextToken value that you received in the previous response. Use this value to get more clusters.

    :type MaxResults: integer
    :param MaxResults: The maximum number of clusters to return in the response. When there are more clusters than the number you specify, the response contains a NextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'Clusters': [
        {
            'BackupPolicy': 'DEFAULT',
            'ClusterId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'Hsms': [
                {
                    'AvailabilityZone': 'string',
                    'ClusterId': 'string',
                    'SubnetId': 'string',
                    'EniId': 'string',
                    'EniIp': 'string',
                    'HsmId': 'string',
                    'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
                    'StateMessage': 'string'
                },
            ],
            'HsmType': 'string',
            'PreCoPassword': 'string',
            'SecurityGroup': 'string',
            'SourceBackupId': 'string',
            'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
            'StateMessage': 'string',
            'SubnetMapping': {
                'string': 'string'
            },
            'VpcId': 'string',
            'Certificates': {
                'ClusterCsr': 'string',
                'HsmCertificate': 'string',
                'AwsHardwareCertificate': 'string',
                'ManufacturerHardwareCertificate': 'string',
                'ClusterCertificate': 'string'
            },
            'TagList': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Clusters (list) --
A list of clusters.

(dict) --
Contains information about an AWS CloudHSM cluster.

BackupPolicy (string) --
The cluster\'s backup policy.

ClusterId (string) --
The cluster\'s identifier (ID).

CreateTimestamp (datetime) --
The date and time when the cluster was created.

Hsms (list) --
Contains information about the HSMs in the cluster.

(dict) --
Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

AvailabilityZone (string) --
The Availability Zone that contains the HSM.

ClusterId (string) --
The identifier (ID) of the cluster that contains the HSM.

SubnetId (string) --
The subnet that contains the HSM\'s elastic network interface (ENI).

EniId (string) --
The identifier (ID) of the HSM\'s elastic network interface (ENI).

EniIp (string) --
The IP address of the HSM\'s elastic network interface (ENI).

HsmId (string) --
The HSM\'s identifier (ID).

State (string) --
The HSM\'s state.

StateMessage (string) --
A description of the HSM\'s state.





HsmType (string) --
The type of HSM that the cluster contains.

PreCoPassword (string) --
The default password for the cluster\'s Pre-Crypto Officer (PRECO) user.

SecurityGroup (string) --
The identifier (ID) of the cluster\'s security group.

SourceBackupId (string) --
The identifier (ID) of the backup used to create the cluster. This value exists only when the cluster was created from a backup.

State (string) --
The cluster\'s state.

StateMessage (string) --
A description of the cluster\'s state.

SubnetMapping (dict) --
A map from availability zone to the cluster\xe2\x80\x99s subnet in that availability zone.

(string) --
(string) --




VpcId (string) --
The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

Certificates (dict) --
Contains one or more certificates or a certificate signing request (CSR).

ClusterCsr (string) --
The cluster\'s certificate signing request (CSR). The CSR exists only when the cluster\'s state is UNINITIALIZED .

HsmCertificate (string) --
The HSM certificate issued (signed) by the HSM hardware.

AwsHardwareCertificate (string) --
The HSM hardware certificate issued (signed) by AWS CloudHSM.

ManufacturerHardwareCertificate (string) --
The HSM hardware certificate issued (signed) by the hardware manufacturer.

ClusterCertificate (string) --
The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster\'s owner.



TagList (list) --

(dict) --
Contains a tag. A tag is a key-value pair.

Key (string) --
The key of the tag.

Value (string) --
The value of the tag.









NextToken (string) --
An opaque string that indicates that the response contains only a subset of clusters. Use this value in a subsequent DescribeClusters request to get more clusters.







Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmTagException


    :return: {
        'Clusters': [
            {
                'BackupPolicy': 'DEFAULT',
                'ClusterId': 'string',
                'CreateTimestamp': datetime(2015, 1, 1),
                'Hsms': [
                    {
                        'AvailabilityZone': 'string',
                        'ClusterId': 'string',
                        'SubnetId': 'string',
                        'EniId': 'string',
                        'EniIp': 'string',
                        'HsmId': 'string',
                        'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
                        'StateMessage': 'string'
                    },
                ],
                'HsmType': 'string',
                'PreCoPassword': 'string',
                'SecurityGroup': 'string',
                'SourceBackupId': 'string',
                'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
                'StateMessage': 'string',
                'SubnetMapping': {
                    'string': 'string'
                },
                'VpcId': 'string',
                'Certificates': {
                    'ClusterCsr': 'string',
                    'HsmCertificate': 'string',
                    'AwsHardwareCertificate': 'string',
                    'ManufacturerHardwareCertificate': 'string',
                    'ClusterCertificate': 'string'
                },
                'TagList': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
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

def initialize_cluster(ClusterId=None, SignedCert=None, TrustAnchor=None):
    """
    Claims an AWS CloudHSM cluster by submitting the cluster certificate issued by your issuing certificate authority (CA) and the CA\'s root certificate. Before you can claim a cluster, you must sign the cluster\'s certificate signing request (CSR) with your issuing CA. To get the cluster\'s CSR, use  DescribeClusters .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.initialize_cluster(
        ClusterId='string',
        SignedCert='string',
        TrustAnchor='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe identifier (ID) of the cluster that you are claiming. To find the cluster ID, use DescribeClusters .\n

    :type SignedCert: string
    :param SignedCert: [REQUIRED]\nThe cluster certificate issued (signed) by your issuing certificate authority (CA). The certificate must be in PEM format and can contain a maximum of 5000 characters.\n

    :type TrustAnchor: string
    :param TrustAnchor: [REQUIRED]\nThe issuing certificate of the issuing certificate authority (CA) that issued (signed) the cluster certificate. You must use a self-signed certificate. The certificate used to sign the HSM CSR must be directly available, and thus must be the root certificate. The certificate must be in PEM format and can contain a maximum of 5000 characters.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
    'StateMessage': 'string'
}


Response Structure

(dict) --

State (string) --
The cluster\'s state.

StateMessage (string) --
A description of the cluster\'s state.







Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException


    :return: {
        'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
        'StateMessage': 'string'
    }
    
    
    :returns: 
    CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
    CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
    CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
    CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
    CloudHSMV2.Client.exceptions.CloudHsmServiceException
    
    """
    pass

def list_tags(ResourceId=None, NextToken=None, MaxResults=None):
    """
    Gets a list of tags for the specified AWS CloudHSM cluster.
    This is a paginated operation, which means that each response might contain only a subset of all the tags. When the response contains only a subset of tags, it includes a NextToken value. Use this value in a subsequent ListTags request to get more tags. When you receive a response with no NextToken (or an empty or null value), that means there are no more tags to get.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags(
        ResourceId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe cluster identifier (ID) for the cluster whose tags you are getting. To find the cluster ID, use DescribeClusters .\n

    :type NextToken: string
    :param NextToken: The NextToken value that you received in the previous response. Use this value to get more tags.

    :type MaxResults: integer
    :param MaxResults: The maximum number of tags to return in the response. When there are more tags than the number you specify, the response contains a NextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'TagList': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TagList (list) --
A list of tags.

(dict) --
Contains a tag. A tag is a key-value pair.

Key (string) --
The key of the tag.

Value (string) --
The value of the tag.





NextToken (string) --
An opaque string that indicates that the response contains only a subset of tags. Use this value in a subsequent ListTags request to get more tags.







Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmTagException


    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
    CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
    CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
    CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
    CloudHSMV2.Client.exceptions.CloudHsmServiceException
    CloudHSMV2.Client.exceptions.CloudHsmTagException
    
    """
    pass

def restore_backup(BackupId=None):
    """
    Restores a specified AWS CloudHSM backup that is in the PENDING_DELETION state. For mor information on deleting a backup, see  DeleteBackup .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_backup(
        BackupId='string'
    )
    
    
    :type BackupId: string
    :param BackupId: [REQUIRED]\nThe ID of the backup to be restored. To find the ID of a backup, use the DescribeBackups operation.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Backup': {
        'BackupId': 'string',
        'BackupState': 'CREATE_IN_PROGRESS'|'READY'|'DELETED'|'PENDING_DELETION',
        'ClusterId': 'string',
        'CreateTimestamp': datetime(2015, 1, 1),
        'CopyTimestamp': datetime(2015, 1, 1),
        'SourceRegion': 'string',
        'SourceBackup': 'string',
        'SourceCluster': 'string',
        'DeleteTimestamp': datetime(2015, 1, 1),
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Backup (dict) --Information on the Backup object created.

BackupId (string) --The identifier (ID) of the backup.

BackupState (string) --The state of the backup.

ClusterId (string) --The identifier (ID) of the cluster that was backed up.

CreateTimestamp (datetime) --The date and time when the backup was created.

CopyTimestamp (datetime) --The date and time when the backup was copied from a source backup.

SourceRegion (string) --The AWS region that contains the source backup from which the new backup was copied.

SourceBackup (string) --The identifier (ID) of the source backup from which the new backup was copied.

SourceCluster (string) --The identifier (ID) of the cluster containing the source backup from which the new backup was copied. .

DeleteTimestamp (datetime) --The date and time when the backup will be permanently deleted.

TagList (list) --
(dict) --Contains a tag. A tag is a key-value pair.

Key (string) --The key of the tag.

Value (string) --The value of the tag.












Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException


    :return: {
        'Backup': {
            'BackupId': 'string',
            'BackupState': 'CREATE_IN_PROGRESS'|'READY'|'DELETED'|'PENDING_DELETION',
            'ClusterId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'CopyTimestamp': datetime(2015, 1, 1),
            'SourceRegion': 'string',
            'SourceBackup': 'string',
            'SourceCluster': 'string',
            'DeleteTimestamp': datetime(2015, 1, 1),
            'TagList': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def tag_resource(ResourceId=None, TagList=None):
    """
    Adds or overwrites one or more tags for the specified AWS CloudHSM cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceId='string',
        TagList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe cluster identifier (ID) for the cluster that you are tagging. To find the cluster ID, use DescribeClusters .\n

    :type TagList: list
    :param TagList: [REQUIRED]\nA list of one or more tags.\n\n(dict) --Contains a tag. A tag is a key-value pair.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmTagException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceId=None, TagKeyList=None):
    """
    Removes the specified tag or tags from the specified AWS CloudHSM cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceId='string',
        TagKeyList=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe cluster identifier (ID) for the cluster whose tags you are removing. To find the cluster ID, use DescribeClusters .\n

    :type TagKeyList: list
    :param TagKeyList: [REQUIRED]\nA list of one or more tag keys for the tags that you are removing. Specify only the tag keys, not the tag values.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudHSMV2.Client.exceptions.CloudHsmAccessDeniedException
CloudHSMV2.Client.exceptions.CloudHsmInternalFailureException
CloudHSMV2.Client.exceptions.CloudHsmInvalidRequestException
CloudHSMV2.Client.exceptions.CloudHsmResourceNotFoundException
CloudHSMV2.Client.exceptions.CloudHsmServiceException
CloudHSMV2.Client.exceptions.CloudHsmTagException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

