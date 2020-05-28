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

def cancel_data_repository_task(TaskId=None):
    """
    Cancels an existing Amazon FSx for Lustre data repository task if that task is in either the PENDING or EXECUTING state. When you cancel a task, Amazon FSx does the following.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_data_repository_task(
        TaskId='string'
    )
    
    
    :type TaskId: string
    :param TaskId: [REQUIRED]\nSpecifies the data repository task to cancel.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Lifecycle': 'PENDING'|'EXECUTING'|'FAILED'|'SUCCEEDED'|'CANCELED'|'CANCELING',
    'TaskId': 'string'
}


Response Structure

(dict) --
Lifecycle (string) --The lifecycle status of the data repository task, as follows:

PENDING - Amazon FSx has not started the task.
EXECUTING - Amazon FSx is processing the task.
FAILED - Amazon FSx was not able to complete the task. For example, there may be files the task failed to process. The  DataRepositoryTaskFailureDetails property provides more information about task failures.
SUCCEEDED - FSx completed the task successfully.
CANCELED - Amazon FSx canceled the task and it did not complete.
CANCELING - FSx is in process of canceling the task.


TaskId (string) --The ID of the task being canceled.






Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.UnsupportedOperation
FSx.Client.exceptions.DataRepositoryTaskNotFound
FSx.Client.exceptions.DataRepositoryTaskEnded
FSx.Client.exceptions.InternalServerError


    :return: {
        'Lifecycle': 'PENDING'|'EXECUTING'|'FAILED'|'SUCCEEDED'|'CANCELED'|'CANCELING',
        'TaskId': 'string'
    }
    
    
    :returns: 
    PENDING - Amazon FSx has not started the task.
    EXECUTING - Amazon FSx is processing the task.
    FAILED - Amazon FSx was not able to complete the task. For example, there may be files the task failed to process. The  DataRepositoryTaskFailureDetails property provides more information about task failures.
    SUCCEEDED - FSx completed the task successfully.
    CANCELED - Amazon FSx canceled the task and it did not complete.
    CANCELING - FSx is in process of canceling the task.
    
    """
    pass

def create_backup(FileSystemId=None, ClientRequestToken=None, Tags=None):
    """
    Creates a backup of an existing Amazon FSx for Windows File Server file system. Creating regular backups for your file system is a best practice that complements the replication that Amazon FSx for Windows File Server performs for your file system. It also enables you to restore from user modification of data.
    If a backup with the specified client request token exists, and the parameters match, this operation returns the description of the existing backup. If a backup specified client request token exists, and the parameters don\'t match, this operation returns IncompatibleParameterError . If a backup with the specified client request token doesn\'t exist, CreateBackup does the following:
    By using the idempotent operation, you can retry a CreateBackup operation without the risk of creating an extra backup. This approach can be useful when an initial call fails in a way that makes it unclear whether a backup was created. If you use the same client request token and the initial call created a backup, the operation returns a successful result because all the parameters are the same.
    The CreateFileSystem operation returns while the backup\'s lifecycle state is still CREATING . You can check the file system creation status by calling the  DescribeBackups operation, which returns the backup state along with other information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_backup(
        FileSystemId='string',
        ClientRequestToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system to back up.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: The tags to apply to the backup at backup creation. The key value of the Name tag appears in the console as the backup name.\n\n(dict) --Specifies a key-value pair for a resource tag.\n\nKey (string) --A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.\n\nValue (string) --A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Backup': {
        'BackupId': 'string',
        'Lifecycle': 'AVAILABLE'|'CREATING'|'DELETED'|'FAILED',
        'FailureDetails': {
            'Message': 'string'
        },
        'Type': 'AUTOMATIC'|'USER_INITIATED',
        'ProgressPercent': 123,
        'CreationTime': datetime(2015, 1, 1),
        'KmsKeyId': 'string',
        'ResourceARN': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'FileSystem': {
            'OwnerId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'FileSystemId': 'string',
            'FileSystemType': 'WINDOWS'|'LUSTRE',
            'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
            'FailureDetails': {
                'Message': 'string'
            },
            'StorageCapacity': 123,
            'StorageType': 'SSD'|'HDD',
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ],
            'NetworkInterfaceIds': [
                'string',
            ],
            'DNSName': 'string',
            'KmsKeyId': 'string',
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'WindowsConfiguration': {
                'ActiveDirectoryId': 'string',
                'SelfManagedActiveDirectoryConfiguration': {
                    'DomainName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string',
                    'FileSystemAdministratorsGroup': 'string',
                    'UserName': 'string',
                    'DnsIps': [
                        'string',
                    ]
                },
                'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
                'RemoteAdministrationEndpoint': 'string',
                'PreferredSubnetId': 'string',
                'PreferredFileServerIp': 'string',
                'ThroughputCapacity': 123,
                'MaintenanceOperationsInProgress': [
                    'PATCHING'|'BACKING_UP',
                ],
                'WeeklyMaintenanceStartTime': 'string',
                'DailyAutomaticBackupStartTime': 'string',
                'AutomaticBackupRetentionDays': 123,
                'CopyTagsToBackups': True|False
            },
            'LustreConfiguration': {
                'WeeklyMaintenanceStartTime': 'string',
                'DataRepositoryConfiguration': {
                    'ImportPath': 'string',
                    'ExportPath': 'string',
                    'ImportedFileChunkSize': 123
                },
                'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
                'PerUnitStorageThroughput': 123,
                'MountName': 'string'
            }
        },
        'DirectoryInformation': {
            'DomainName': 'string',
            'ActiveDirectoryId': 'string'
        }
    }
}


Response Structure

(dict) --
The response object for the CreateBackup operation.

Backup (dict) --
A description of the backup.

BackupId (string) --
The ID of the backup.

Lifecycle (string) --
The lifecycle status of the backup.

FailureDetails (dict) --
Details explaining any failures that occur when creating a backup.

Message (string) --
A message describing the backup creation failure.



Type (string) --
The type of the backup.

ProgressPercent (integer) --
The current percent of progress of an asynchronous task.

CreationTime (datetime) --
The time when a particular backup was created.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt this backup of the Amazon FSx for Windows file system\'s data at rest. Amazon FSx for Lustre does not support KMS encryption.

ResourceARN (string) --
The Amazon Resource Name (ARN) for the backup resource.

Tags (list) --
Tags associated with a particular file system.

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





FileSystem (dict) --
Metadata of the file system associated with the backup. This metadata is persisted even if the file system is deleted.

OwnerId (string) --
The AWS account that created the file system. If the file system was created by an AWS Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is the owner.

CreationTime (datetime) --
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId (string) --
The system-generated, unique 17-digit ID of the file system.

FileSystemType (string) --
The type of Amazon FSx file system, either LUSTRE or WINDOWS .

Lifecycle (string) --
The lifecycle status of the file system, following are the possible values and what they mean:

AVAILABLE - The file system is in a healthy state, and is reachable and available for use.
CREATING - Amazon FSx is creating the new file system.
DELETING - Amazon FSx is deleting an existing file system.
FAILED - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
MISCONFIGURED indicates that the file system is in a failed but recoverable state.
UPDATING indicates that the file system is undergoing a customer initiated update.


FailureDetails (dict) --
A structure providing details of any failures that occur when creating the file system has failed.

Message (string) --
A message describing any failures that occurred during file system creation.



StorageCapacity (integer) --
The storage capacity of the file system in gigabytes (GB).

StorageType (string) --
The storage type of the file system. Valid values are SSD and HDD . If set to SSD , the file system uses solid state drive storage. If set to HDD , the file system uses hard disk drive storage.

VpcId (string) --
The ID of the primary VPC for the file system.

SubnetIds (list) --
Specifies the IDs of the subnets that the file system is accessible from. For Windows MULTI_AZ_1 file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the PreferredSubnetID property. All other file systems have only one subnet ID.
For Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the endpoint for the file system. For MULTI_AZ_1 Windows file systems, the endpoint for the file system is available in the PreferredSubnetID .

(string) --
The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.



NetworkInterfaceIds (list) --
The IDs of the elastic network interface from which a specific file system is accessible. The elastic network interface is automatically created in the same VPC that the Amazon FSx file system was created in. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide.
For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string) --
An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide for Linux Instances .



DNSName (string) --
The DNS name for the file system.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file system\'s data for Amazon FSx for Windows File Server file systems and persistent Amazon FSx for Lustre file systems at rest. In either case, if not specified, the Amazon FSx managed key is used. The scratch Amazon FSx for Lustre file systems are always encrypted at rest using Amazon FSx managed keys. For more information, see Encrypt in the AWS Key Management Service API Reference .

ResourceARN (string) --
The Amazon Resource Name (ARN) for the file system resource.

Tags (list) --
The tags to associate with the file system. For more information, see Tagging Your Amazon EC2 Resources in the Amazon EC2 User Guide .

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





WindowsConfiguration (dict) --
The configuration for this Microsoft Windows file system.

ActiveDirectoryId (string) --
The ID for an existing Microsoft Active Directory instance that the file system should join when it\'s created.

SelfManagedActiveDirectoryConfiguration (dict) --
The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server instance is joined.

DomainName (string) --
The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName (string) --
The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server instance is joined.

FileSystemAdministratorsGroup (string) --
The name of the domain group whose members have administrative privileges for the FSx file system.

UserName (string) --
The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps (list) --
A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string) --




DeploymentType (string) --
Specifies the file system deployment type, valid values are the following:

MULTI_AZ_1 - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
SINGLE_AZ_1 - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
SINGLE_AZ_2 - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see Single-AZ and Multi-AZ File Systems .

RemoteAdministrationEndpoint (string) --
For MULTI_AZ_1 deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this is the DNS name of the file system.
This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId (string) --
For MULTI_AZ_1 deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in SubnetIds property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this value is the same as that for SubnetIDs . For more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems

PreferredFileServerIp (string) --
For MULTI_AZ_1 deployment types, the IP address of the primary, or preferred, file server.
Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system\'s DNSName instead. For more information on mapping and mounting file shares, see Accessing File Shares .

ThroughputCapacity (integer) --
The throughput of an Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress (list) --
The list of maintenance operations in progress for this file system.

(string) --
An enumeration specifying the currently ongoing maintenance operation.



WeeklyMaintenanceStartTime (string) --
The preferred time to perform weekly maintenance, in the UTC time zone.

DailyAutomaticBackupStartTime (string) --
The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays (integer) --
The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 35 days.

CopyTagsToBackups (boolean) --
A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn\'t specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.



LustreConfiguration (dict) --
The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime (string) --
The UTC time that you want to begin your weekly maintenance window.

DataRepositoryConfiguration (dict) --
The data repository configuration object for Lustre file systems returned in the response of the CreateFileSystem operation.

ImportPath (string) --
The import path to the Amazon S3 bucket (and optional prefix) that you\'re using as the data repository for your FSx for Lustre file system, for example s3://import-bucket/optional-prefix . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath (string) --
The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize (integer) --
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.



DeploymentType (string) --
The deployment type of the FSX for Lustre file system.

PerUnitStorageThroughput (integer) --
Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for PERSISTENT_1 deployment types. Valid values are 50, 100, 200.

MountName (string) --
You use the MountName value when mounting the file system.
For the SCRATCH_1 deployment type, this value is always "fsx ". For SCRATCH_2 and PERSISTENT_1 deployment types, this value is a string that is unique within an AWS Region.





DirectoryInformation (dict) --
The configuration of the self-managed Microsoft Active Directory (AD) to which the Windows File Server instance is joined.

DomainName (string) --
The fully qualified domain name of the self-managed AD directory.

ActiveDirectoryId (string) --
The ID of the AWS Managed Microsoft Active Directory instance to which the file system is joined.











Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.UnsupportedOperation
FSx.Client.exceptions.FileSystemNotFound
FSx.Client.exceptions.BackupInProgress
FSx.Client.exceptions.IncompatibleParameterError
FSx.Client.exceptions.ServiceLimitExceeded
FSx.Client.exceptions.InternalServerError


    :return: {
        'Backup': {
            'BackupId': 'string',
            'Lifecycle': 'AVAILABLE'|'CREATING'|'DELETED'|'FAILED',
            'FailureDetails': {
                'Message': 'string'
            },
            'Type': 'AUTOMATIC'|'USER_INITIATED',
            'ProgressPercent': 123,
            'CreationTime': datetime(2015, 1, 1),
            'KmsKeyId': 'string',
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'FileSystem': {
                'OwnerId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'FileSystemId': 'string',
                'FileSystemType': 'WINDOWS'|'LUSTRE',
                'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
                'FailureDetails': {
                    'Message': 'string'
                },
                'StorageCapacity': 123,
                'StorageType': 'SSD'|'HDD',
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'NetworkInterfaceIds': [
                    'string',
                ],
                'DNSName': 'string',
                'KmsKeyId': 'string',
                'ResourceARN': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'WindowsConfiguration': {
                    'ActiveDirectoryId': 'string',
                    'SelfManagedActiveDirectoryConfiguration': {
                        'DomainName': 'string',
                        'OrganizationalUnitDistinguishedName': 'string',
                        'FileSystemAdministratorsGroup': 'string',
                        'UserName': 'string',
                        'DnsIps': [
                            'string',
                        ]
                    },
                    'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
                    'RemoteAdministrationEndpoint': 'string',
                    'PreferredSubnetId': 'string',
                    'PreferredFileServerIp': 'string',
                    'ThroughputCapacity': 123,
                    'MaintenanceOperationsInProgress': [
                        'PATCHING'|'BACKING_UP',
                    ],
                    'WeeklyMaintenanceStartTime': 'string',
                    'DailyAutomaticBackupStartTime': 'string',
                    'AutomaticBackupRetentionDays': 123,
                    'CopyTagsToBackups': True|False
                },
                'LustreConfiguration': {
                    'WeeklyMaintenanceStartTime': 'string',
                    'DataRepositoryConfiguration': {
                        'ImportPath': 'string',
                        'ExportPath': 'string',
                        'ImportedFileChunkSize': 123
                    },
                    'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
                    'PerUnitStorageThroughput': 123,
                    'MountName': 'string'
                }
            },
            'DirectoryInformation': {
                'DomainName': 'string',
                'ActiveDirectoryId': 'string'
            }
        }
    }
    
    
    :returns: 
    FileSystemId (string) -- [REQUIRED]
    The ID of the file system to back up.
    
    ClientRequestToken (string) -- (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
    This field is autopopulated if not provided.
    
    Tags (list) -- The tags to apply to the backup at backup creation. The key value of the Name tag appears in the console as the backup name.
    
    (dict) --Specifies a key-value pair for a resource tag.
    
    Key (string) --A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.
    
    Value (string) --A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .
    
    
    
    
    
    
    """
    pass

def create_data_repository_task(Type=None, Paths=None, FileSystemId=None, Report=None, ClientRequestToken=None, Tags=None):
    """
    Creates an Amazon FSx for Lustre data repository task. You use data repository tasks to perform bulk operations between your Amazon FSx file system and its linked data repository. An example of a data repository task is exporting any data and metadata changes, including POSIX metadata, to files, directories, and symbolic links (symlinks) from your FSx file system to its linked data repository. A CreateDataRepositoryTask operation will fail if a data repository is not linked to the FSx file system. To learn more about data repository tasks, see Using Data Repository Tasks . To learn more about linking a data repository to your file system, see Setting the Export Prefix .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_data_repository_task(
        Type='EXPORT_TO_REPOSITORY',
        Paths=[
            'string',
        ],
        FileSystemId='string',
        Report={
            'Enabled': True|False,
            'Path': 'string',
            'Format': 'REPORT_CSV_20191124',
            'Scope': 'FAILED_FILES_ONLY'
        },
        ClientRequestToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Type: string
    :param Type: [REQUIRED]\nSpecifies the type of data repository task to create.\n

    :type Paths: list
    :param Paths: (Optional) The path or paths on the Amazon FSx file system to use when the data repository task is processed. The default path is the file system root directory. The paths you provide need to be relative to the mount point of the file system. If the mount point is /mnt/fsx and /mnt/fsx/path1 is a directory or file on the file system you want to export, then the path to provide is path1 . If a path that you provide isn\'t valid, the task fails.\n\n(string) --\n\n

    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe globally unique ID of the file system, assigned by Amazon FSx.\n

    :type Report: dict
    :param Report: [REQUIRED]\nDefines whether or not Amazon FSx provides a CompletionReport once the task has completed. A CompletionReport provides a detailed report on the files that Amazon FSx processed that meet the criteria specified by the Scope parameter. For more information, see Working with Task Completion Reports .\n\nEnabled (boolean) -- [REQUIRED]Set Enabled to True to generate a CompletionReport when the task completes. If set to true , then you need to provide a report Scope , Path , and Format . Set Enabled to False if you do not want a CompletionReport generated when the task completes.\n\nPath (string) --Required if Enabled is set to true . Specifies the location of the report on the file system\'s linked S3 data repository. An absolute path that defines where the completion report will be stored in the destination location. The Path you provide must be located within the file system\xe2\x80\x99s ExportPath. An example Path value is 's3://myBucket/myExportPath/optionalPrefix'. The report provides the following information for each file in the report: FilePath, FileStatus, and ErrorCode. To learn more about a file system\'s ExportPath , see .\n\nFormat (string) --Required if Enabled is set to true . Specifies the format of the CompletionReport . REPORT_CSV_20191124 is the only format currently supported. When Format is set to REPORT_CSV_20191124 , the CompletionReport is provided in CSV format, and is delivered to {path}/task-{id}/failures.csv .\n\nScope (string) --Required if Enabled is set to true . Specifies the scope of the CompletionReport ; FAILED_FILES_ONLY is the only scope currently supported. When Scope is set to FAILED_FILES_ONLY , the CompletionReport only contains information about files that the data repository task failed to process.\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) An idempotency token for resource creation, in a string of up to 64 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: A list of Tag values, with a maximum of 50 elements.\n\n(dict) --Specifies a key-value pair for a resource tag.\n\nKey (string) --A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.\n\nValue (string) --A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DataRepositoryTask': {
        'TaskId': 'string',
        'Lifecycle': 'PENDING'|'EXECUTING'|'FAILED'|'SUCCEEDED'|'CANCELED'|'CANCELING',
        'Type': 'EXPORT_TO_REPOSITORY',
        'CreationTime': datetime(2015, 1, 1),
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'ResourceARN': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'FileSystemId': 'string',
        'Paths': [
            'string',
        ],
        'FailureDetails': {
            'Message': 'string'
        },
        'Status': {
            'TotalCount': 123,
            'SucceededCount': 123,
            'FailedCount': 123,
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
        'Report': {
            'Enabled': True|False,
            'Path': 'string',
            'Format': 'REPORT_CSV_20191124',
            'Scope': 'FAILED_FILES_ONLY'
        }
    }
}


Response Structure

(dict) --

DataRepositoryTask (dict) --
The description of the data repository task that you just created.

TaskId (string) --
The system-generated, unique 17-digit ID of the data repository task.

Lifecycle (string) --
The lifecycle status of the data repository task, as follows:

PENDING - Amazon FSx has not started the task.
EXECUTING - Amazon FSx is processing the task.
FAILED - Amazon FSx was not able to complete the task. For example, there may be files the task failed to process. The  DataRepositoryTaskFailureDetails property provides more information about task failures.
SUCCEEDED - FSx completed the task successfully.
CANCELED - Amazon FSx canceled the task and it did not complete.
CANCELING - FSx is in process of canceling the task.


Note
You cannot delete an FSx for Lustre file system if there are data repository tasks for the file system in the PENDING or EXECUTING states. Please retry when the data repository task is finished (with a status of CANCELED , SUCCEEDED , or FAILED ). You can use the DescribeDataRepositoryTask action to monitor the task status. Contact the FSx team if you need to delete your file system immediately.


Type (string) --
The type of data repository task; EXPORT_TO_REPOSITORY is the only type currently supported.

CreationTime (datetime) --
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

StartTime (datetime) --
The time that Amazon FSx began processing the task.

EndTime (datetime) --
The time that Amazon FSx completed processing the task, populated after the task is complete.

ResourceARN (string) --
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

Tags (list) --
A list of Tag values, with a maximum of 50 elements.

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





FileSystemId (string) --
The globally unique ID of the file system, assigned by Amazon FSx.

Paths (list) --
An array of paths on the Amazon FSx for Lustre file system that specify the data for the data repository task to process. For example, in an EXPORT_TO_REPOSITORY task, the paths specify which data to export to the linked data repository.
(Default) If Paths is not specified, Amazon FSx uses the file system root directory.

(string) --


FailureDetails (dict) --
Failure message describing why the task failed, it is populated only when Lifecycle is set to FAILED .

Message (string) --
A detailed error message.



Status (dict) --
Provides the status of the number of files that the task has processed successfully and failed to process.

TotalCount (integer) --
The total number of files that the task will process. While a task is executing, the sum of SucceededCount plus FailedCount may not equal TotalCount . When the task is complete, TotalCount equals the sum of SucceededCount plus FailedCount .

SucceededCount (integer) --
A running total of the number of files that the task has successfully processed.

FailedCount (integer) --
A running total of the number of files that the task failed to process.

LastUpdatedTime (datetime) --
The time at which the task status was last updated.



Report (dict) --
Provides a report detailing the data repository task results of the files processed that match the criteria specified in the report Scope parameter. FSx delivers the report to the file system\'s linked data repository in Amazon S3, using the path specified in the report Path parameter. You can specify whether or not a report gets generated for a task using the Enabled parameter.

Enabled (boolean) --
Set Enabled to True to generate a CompletionReport when the task completes. If set to true , then you need to provide a report Scope , Path , and Format . Set Enabled to False if you do not want a CompletionReport generated when the task completes.

Path (string) --
Required if Enabled is set to true . Specifies the location of the report on the file system\'s linked S3 data repository. An absolute path that defines where the completion report will be stored in the destination location. The Path you provide must be located within the file system\xe2\x80\x99s ExportPath. An example Path value is "s3://myBucket/myExportPath/optionalPrefix". The report provides the following information for each file in the report: FilePath, FileStatus, and ErrorCode. To learn more about a file system\'s ExportPath , see .

Format (string) --
Required if Enabled is set to true . Specifies the format of the CompletionReport . REPORT_CSV_20191124 is the only format currently supported. When Format is set to REPORT_CSV_20191124 , the CompletionReport is provided in CSV format, and is delivered to {path}/task-{id}/failures.csv .

Scope (string) --
Required if Enabled is set to true . Specifies the scope of the CompletionReport ; FAILED_FILES_ONLY is the only scope currently supported. When Scope is set to FAILED_FILES_ONLY , the CompletionReport only contains information about files that the data repository task failed to process.











Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.UnsupportedOperation
FSx.Client.exceptions.FileSystemNotFound
FSx.Client.exceptions.IncompatibleParameterError
FSx.Client.exceptions.ServiceLimitExceeded
FSx.Client.exceptions.InternalServerError
FSx.Client.exceptions.DataRepositoryTaskExecuting


    :return: {
        'DataRepositoryTask': {
            'TaskId': 'string',
            'Lifecycle': 'PENDING'|'EXECUTING'|'FAILED'|'SUCCEEDED'|'CANCELED'|'CANCELING',
            'Type': 'EXPORT_TO_REPOSITORY',
            'CreationTime': datetime(2015, 1, 1),
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'FileSystemId': 'string',
            'Paths': [
                'string',
            ],
            'FailureDetails': {
                'Message': 'string'
            },
            'Status': {
                'TotalCount': 123,
                'SucceededCount': 123,
                'FailedCount': 123,
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
            'Report': {
                'Enabled': True|False,
                'Path': 'string',
                'Format': 'REPORT_CSV_20191124',
                'Scope': 'FAILED_FILES_ONLY'
            }
        }
    }
    
    
    :returns: 
    PENDING - Amazon FSx has not started the task.
    EXECUTING - Amazon FSx is processing the task.
    FAILED - Amazon FSx was not able to complete the task. For example, there may be files the task failed to process. The  DataRepositoryTaskFailureDetails property provides more information about task failures.
    SUCCEEDED - FSx completed the task successfully.
    CANCELED - Amazon FSx canceled the task and it did not complete.
    CANCELING - FSx is in process of canceling the task.
    
    """
    pass

def create_file_system(ClientRequestToken=None, FileSystemType=None, StorageCapacity=None, StorageType=None, SubnetIds=None, SecurityGroupIds=None, Tags=None, KmsKeyId=None, WindowsConfiguration=None, LustreConfiguration=None):
    """
    Creates a new, empty Amazon FSx file system.
    If a file system with the specified client request token exists and the parameters match, CreateFileSystem returns the description of the existing file system. If a file system specified client request token exists and the parameters don\'t match, this call returns IncompatibleParameterError . If a file system with the specified client request token doesn\'t exist, CreateFileSystem does the following:
    This operation requires a client request token in the request that Amazon FSx uses to ensure idempotent creation. This means that calling the operation multiple times with the same client request token has no effect. By using the idempotent operation, you can retry a CreateFileSystem operation without the risk of creating an extra file system. This approach can be useful when an initial call fails in a way that makes it unclear whether a file system was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a file system, the client receives success as long as the parameters are the same.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_file_system(
        ClientRequestToken='string',
        FileSystemType='WINDOWS'|'LUSTRE',
        StorageCapacity=123,
        StorageType='SSD'|'HDD',
        SubnetIds=[
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
        KmsKeyId='string',
        WindowsConfiguration={
            'ActiveDirectoryId': 'string',
            'SelfManagedActiveDirectoryConfiguration': {
                'DomainName': 'string',
                'OrganizationalUnitDistinguishedName': 'string',
                'FileSystemAdministratorsGroup': 'string',
                'UserName': 'string',
                'Password': 'string',
                'DnsIps': [
                    'string',
                ]
            },
            'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
            'PreferredSubnetId': 'string',
            'ThroughputCapacity': 123,
            'WeeklyMaintenanceStartTime': 'string',
            'DailyAutomaticBackupStartTime': 'string',
            'AutomaticBackupRetentionDays': 123,
            'CopyTagsToBackups': True|False
        },
        LustreConfiguration={
            'WeeklyMaintenanceStartTime': 'string',
            'ImportPath': 'string',
            'ExportPath': 'string',
            'ImportedFileChunkSize': 123,
            'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
            'PerUnitStorageThroughput': 123
        }
    )
    
    
    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.\nThis field is autopopulated if not provided.\n

    :type FileSystemType: string
    :param FileSystemType: [REQUIRED]\nThe type of Amazon FSx file system to create, either WINDOWS or LUSTRE .\n

    :type StorageCapacity: integer
    :param StorageCapacity: [REQUIRED]\nSets the storage capacity of the file system that you\'re creating.\nFor Lustre file systems:\n\nFor SCRATCH_2 and PERSISTENT_1 deployment types, valid values are 1.2, 2.4, and increments of 2.4 TiB.\nFor SCRATCH_1 deployment type, valid values are 1.2, 2.4, and increments of 3.6 TiB.\n\nFor Windows file systems:\n\nIf StorageType=SSD , valid values are 32 GiB - 65,536 GiB (64 TiB).\nIf StorageType=HDD , valid values are 2000 GiB - 65,536 GiB (64 TiB).\n\n

    :type StorageType: string
    :param StorageType: Sets the storage type for the Amazon FSx for Windows file system you\'re creating. Valid values are SSD and HDD .\n\nSet to SSD to use solid state drive storage. SSD is supported on all Windows deployment types.\nSet to HDD to use hard disk drive storage. HDD is supported on SINGLE_AZ_2 and MULTI_AZ_1 Windows file system deployment types.\n\nDefault value is SSD . For more information, see Storage Type Options in the Amazon FSx for Windows User Guide .\n

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nSpecifies the IDs of the subnets that the file system will be accessible from. For Windows MULTI_AZ_1 file system deployment types, provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the WindowsConfiguration > PreferredSubnetID property.\nFor Windows SINGLE_AZ_1 and SINGLE_AZ_2 file system deployment types and Lustre file systems, provide exactly one subnet ID. The file server is launched in that subnet\'s Availability Zone.\n\n(string) --The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.\n\n\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: A list of IDs specifying the security groups to apply to all network interfaces created for file system access. This list isn\'t returned in later requests to describe the file system.\n\n(string) --The ID of your Amazon EC2 security group. This ID is used to control network access to the endpoint that Amazon FSx creates on your behalf in each subnet. For more information, see Amazon EC2 Security Groups for Linux Instances in the Amazon EC2 User Guide .\n\n\n

    :type Tags: list
    :param Tags: The tags to apply to the file system being created. The key value of the Name tag appears in the console as the file system name.\n\n(dict) --Specifies a key-value pair for a resource tag.\n\nKey (string) --A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.\n\nValue (string) --A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .\n\n\n\n\n

    :type KmsKeyId: string
    :param KmsKeyId: The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file system\'s data for Amazon FSx for Windows File Server file systems and Amazon FSx for Lustre PERSISTENT_1 file systems at rest. In either case, if not specified, the Amazon FSx managed key is used. The Amazon FSx for Lustre SCRATCH_1 and SCRATCH_2 file systems are always encrypted at rest using Amazon FSx managed keys. For more information, see Encrypt in the AWS Key Management Service API Reference .

    :type WindowsConfiguration: dict
    :param WindowsConfiguration: The Microsoft Windows configuration for the file system being created.\n\nActiveDirectoryId (string) --The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file system should join when it\'s created.\n\nSelfManagedActiveDirectoryConfiguration (dict) --The configuration that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory.\n\nDomainName (string) -- [REQUIRED]The fully qualified domain name of the self-managed AD directory, such as corp.example.com .\n\nOrganizationalUnitDistinguishedName (string) --(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. Amazon FSx only accepts OU as the direct parent of the file system. An example is OU=FSx,DC=yourdomain,DC=corp,DC=com . To learn more, see RFC 2253 . If none is provided, the FSx file system is created in the default location of your self-managed AD directory.\n\nWarning\nOnly Organizational Unit (OU) objects can be the direct parent of the file system that you\'re creating.\n\n\nFileSystemAdministratorsGroup (string) --(Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don\'t provide one, your AD domain\'s Domain Admins group is used.\n\nUserName (string) -- [REQUIRED]The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in OrganizationalUnitDistinguishedName , or in the default location of your AD domain.\n\nPassword (string) -- [REQUIRED]The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.\n\nDnsIps (list) -- [REQUIRED]A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the one in which your Amazon FSx file system is being created, or in the private IP version 4 (IPv4) address ranges, as specified in RFC 1918 :\n\n10.0.0.0 - 10.255.255.255 (10/8 prefix)\n172.16.0.0 - 172.31.255.255 (172.16/12 prefix)\n192.168.0.0 - 192.168.255.255 (192.168/16 prefix)\n\n\n(string) --\n\n\n\n\nDeploymentType (string) --Specifies the file system deployment type, valid values are the following:\n\nMULTI_AZ_1 - Deploys a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. You can only deploy a Multi-AZ file system in AWS Regions that have a minimum of three Availability Zones. Also supports HDD storage type\nSINGLE_AZ_1 - (Default) Choose to deploy a file system that is configured for single AZ redundancy.\nSINGLE_AZ_2 - The latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports HDD storage type.\n\nFor more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems .\n\nPreferredSubnetId (string) --Required when DeploymentType is set to MULTI_AZ_1 . This specifies the subnet in which you want the preferred file server to be located. For in-AWS applications, we recommend that you launch your clients in the same Availability Zone (AZ) as your preferred file server to reduce cross-AZ data transfer costs and minimize latency.\n\nThroughputCapacity (integer) -- [REQUIRED]The throughput of an Amazon FSx file system, measured in megabytes per second, in 2 to the n th increments, between 2^3 (8) and 2^11 (2048).\n\nWeeklyMaintenanceStartTime (string) --The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone.\n\nDailyAutomaticBackupStartTime (string) --The preferred time to take daily automatic backups, formatted HH:MM in the UTC time zone.\n\nAutomaticBackupRetentionDays (integer) --The number of days to retain automatic backups. The default is to retain backups for 7 days. Setting this value to 0 disables the creation of automatic backups. The maximum retention period for backups is 35 days.\n\nCopyTagsToBackups (boolean) --A boolean flag indicating whether tags for the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn\'t specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.\n\n\n

    :type LustreConfiguration: dict
    :param LustreConfiguration: The Lustre configuration for the file system being created.\n\nWeeklyMaintenanceStartTime (string) --The preferred time to perform weekly maintenance, in the UTC time zone.\n\nImportPath (string) --(Optional) The path to the Amazon S3 bucket (including the optional prefix) that you\'re using as the data repository for your Amazon FSx for Lustre file system. The root of your FSx for Lustre file system will be mapped to the root of the Amazon S3 bucket you select. An example is s3://import-bucket/optional-prefix . If you specify a prefix after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.\n\nExportPath (string) --(Optional) The path in Amazon S3 where the root of your Amazon FSx file system is exported. The path must use the same Amazon S3 bucket as specified in ImportPath. You can provide an optional prefix to which new and changed data is to be exported from your Amazon FSx for Lustre file system. If an ExportPath value is not provided, Amazon FSx sets a default export path, s3://import-bucket/FSxLustre[creation-timestamp] . The timestamp is in UTC format, for example s3://import-bucket/FSxLustre20181105T222312Z .\nThe Amazon S3 export bucket must be the same as the import bucket specified by ImportPath . If you only specify a bucket name, such as s3://import-bucket , you get a 1:1 mapping of file system objects to S3 bucket objects. This mapping means that the input data in S3 is overwritten on export. If you provide a custom prefix in the export path, such as s3://import-bucket/[custom-optional-prefix] , Amazon FSx exports the contents of your file system to that export prefix in the Amazon S3 bucket.\n\nImportedFileChunkSize (integer) --(Optional) For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.\nThe default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.\n\nDeploymentType (string) --(Optional) Choose SCRATCH_1 and SCRATCH_2 deployment types when you need temporary storage and shorter-term processing of data. The SCRATCH_2 deployment type provides in-transit encryption of data and higher burst throughput capacity than SCRATCH_1 .\nChoose PERSISTENT_1 deployment type for longer-term storage and workloads and encryption of data in transit. To learn more about deployment types, see FSx for Lustre Deployment Options .\nEncryption of data in-transit is automatically enabled when you access a SCRATCH_2 or PERSISTENT_1 file system from Amazon EC2 instances that support this feature . (Default = SCRATCH_1 )\nEncryption of data in-transit for SCRATCH_2 and PERSISTENT_1 deployment types is supported when accessed from supported instance types in supported AWS Regions. To learn more, Encrypting Data in Transit .\n\nPerUnitStorageThroughput (integer) --Required for the PERSISTENT_1 deployment type, describes the amount of read and write throughput for each 1 tebibyte of storage, in MB/s/TiB. File system throughput capacity is calculated by multiplying \xef\xac\x81le system storage capacity (TiB) by the PerUnitStorageThroughput (MB/s/TiB). For a 2.4 TiB \xef\xac\x81le system, provisioning 50 MB/s/TiB of PerUnitStorageThroughput yields 117 MB/s of \xef\xac\x81le system throughput. You pay for the amount of throughput that you provision.\nValid values are 50, 100, 200.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FileSystem': {
        'OwnerId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'FileSystemId': 'string',
        'FileSystemType': 'WINDOWS'|'LUSTRE',
        'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
        'FailureDetails': {
            'Message': 'string'
        },
        'StorageCapacity': 123,
        'StorageType': 'SSD'|'HDD',
        'VpcId': 'string',
        'SubnetIds': [
            'string',
        ],
        'NetworkInterfaceIds': [
            'string',
        ],
        'DNSName': 'string',
        'KmsKeyId': 'string',
        'ResourceARN': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'WindowsConfiguration': {
            'ActiveDirectoryId': 'string',
            'SelfManagedActiveDirectoryConfiguration': {
                'DomainName': 'string',
                'OrganizationalUnitDistinguishedName': 'string',
                'FileSystemAdministratorsGroup': 'string',
                'UserName': 'string',
                'DnsIps': [
                    'string',
                ]
            },
            'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
            'RemoteAdministrationEndpoint': 'string',
            'PreferredSubnetId': 'string',
            'PreferredFileServerIp': 'string',
            'ThroughputCapacity': 123,
            'MaintenanceOperationsInProgress': [
                'PATCHING'|'BACKING_UP',
            ],
            'WeeklyMaintenanceStartTime': 'string',
            'DailyAutomaticBackupStartTime': 'string',
            'AutomaticBackupRetentionDays': 123,
            'CopyTagsToBackups': True|False
        },
        'LustreConfiguration': {
            'WeeklyMaintenanceStartTime': 'string',
            'DataRepositoryConfiguration': {
                'ImportPath': 'string',
                'ExportPath': 'string',
                'ImportedFileChunkSize': 123
            },
            'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
            'PerUnitStorageThroughput': 123,
            'MountName': 'string'
        }
    }
}


Response Structure

(dict) --
The response object returned after the file system is created.

FileSystem (dict) --
The configuration of the file system that was created.

OwnerId (string) --
The AWS account that created the file system. If the file system was created by an AWS Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is the owner.

CreationTime (datetime) --
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId (string) --
The system-generated, unique 17-digit ID of the file system.

FileSystemType (string) --
The type of Amazon FSx file system, either LUSTRE or WINDOWS .

Lifecycle (string) --
The lifecycle status of the file system, following are the possible values and what they mean:

AVAILABLE - The file system is in a healthy state, and is reachable and available for use.
CREATING - Amazon FSx is creating the new file system.
DELETING - Amazon FSx is deleting an existing file system.
FAILED - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
MISCONFIGURED indicates that the file system is in a failed but recoverable state.
UPDATING indicates that the file system is undergoing a customer initiated update.


FailureDetails (dict) --
A structure providing details of any failures that occur when creating the file system has failed.

Message (string) --
A message describing any failures that occurred during file system creation.



StorageCapacity (integer) --
The storage capacity of the file system in gigabytes (GB).

StorageType (string) --
The storage type of the file system. Valid values are SSD and HDD . If set to SSD , the file system uses solid state drive storage. If set to HDD , the file system uses hard disk drive storage.

VpcId (string) --
The ID of the primary VPC for the file system.

SubnetIds (list) --
Specifies the IDs of the subnets that the file system is accessible from. For Windows MULTI_AZ_1 file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the PreferredSubnetID property. All other file systems have only one subnet ID.
For Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the endpoint for the file system. For MULTI_AZ_1 Windows file systems, the endpoint for the file system is available in the PreferredSubnetID .

(string) --
The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.



NetworkInterfaceIds (list) --
The IDs of the elastic network interface from which a specific file system is accessible. The elastic network interface is automatically created in the same VPC that the Amazon FSx file system was created in. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide.
For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string) --
An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide for Linux Instances .



DNSName (string) --
The DNS name for the file system.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file system\'s data for Amazon FSx for Windows File Server file systems and persistent Amazon FSx for Lustre file systems at rest. In either case, if not specified, the Amazon FSx managed key is used. The scratch Amazon FSx for Lustre file systems are always encrypted at rest using Amazon FSx managed keys. For more information, see Encrypt in the AWS Key Management Service API Reference .

ResourceARN (string) --
The Amazon Resource Name (ARN) for the file system resource.

Tags (list) --
The tags to associate with the file system. For more information, see Tagging Your Amazon EC2 Resources in the Amazon EC2 User Guide .

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





WindowsConfiguration (dict) --
The configuration for this Microsoft Windows file system.

ActiveDirectoryId (string) --
The ID for an existing Microsoft Active Directory instance that the file system should join when it\'s created.

SelfManagedActiveDirectoryConfiguration (dict) --
The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server instance is joined.

DomainName (string) --
The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName (string) --
The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server instance is joined.

FileSystemAdministratorsGroup (string) --
The name of the domain group whose members have administrative privileges for the FSx file system.

UserName (string) --
The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps (list) --
A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string) --




DeploymentType (string) --
Specifies the file system deployment type, valid values are the following:

MULTI_AZ_1 - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
SINGLE_AZ_1 - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
SINGLE_AZ_2 - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see Single-AZ and Multi-AZ File Systems .

RemoteAdministrationEndpoint (string) --
For MULTI_AZ_1 deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this is the DNS name of the file system.
This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId (string) --
For MULTI_AZ_1 deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in SubnetIds property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this value is the same as that for SubnetIDs . For more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems

PreferredFileServerIp (string) --
For MULTI_AZ_1 deployment types, the IP address of the primary, or preferred, file server.
Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system\'s DNSName instead. For more information on mapping and mounting file shares, see Accessing File Shares .

ThroughputCapacity (integer) --
The throughput of an Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress (list) --
The list of maintenance operations in progress for this file system.

(string) --
An enumeration specifying the currently ongoing maintenance operation.



WeeklyMaintenanceStartTime (string) --
The preferred time to perform weekly maintenance, in the UTC time zone.

DailyAutomaticBackupStartTime (string) --
The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays (integer) --
The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 35 days.

CopyTagsToBackups (boolean) --
A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn\'t specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.



LustreConfiguration (dict) --
The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime (string) --
The UTC time that you want to begin your weekly maintenance window.

DataRepositoryConfiguration (dict) --
The data repository configuration object for Lustre file systems returned in the response of the CreateFileSystem operation.

ImportPath (string) --
The import path to the Amazon S3 bucket (and optional prefix) that you\'re using as the data repository for your FSx for Lustre file system, for example s3://import-bucket/optional-prefix . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath (string) --
The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize (integer) --
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.



DeploymentType (string) --
The deployment type of the FSX for Lustre file system.

PerUnitStorageThroughput (integer) --
Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for PERSISTENT_1 deployment types. Valid values are 50, 100, 200.

MountName (string) --
You use the MountName value when mounting the file system.
For the SCRATCH_1 deployment type, this value is always "fsx ". For SCRATCH_2 and PERSISTENT_1 deployment types, this value is a string that is unique within an AWS Region.











Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.ActiveDirectoryError
FSx.Client.exceptions.IncompatibleParameterError
FSx.Client.exceptions.InvalidImportPath
FSx.Client.exceptions.InvalidExportPath
FSx.Client.exceptions.InvalidNetworkSettings
FSx.Client.exceptions.InvalidPerUnitStorageThroughput
FSx.Client.exceptions.ServiceLimitExceeded
FSx.Client.exceptions.InternalServerError
FSx.Client.exceptions.MissingFileSystemConfiguration


    :return: {
        'FileSystem': {
            'OwnerId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'FileSystemId': 'string',
            'FileSystemType': 'WINDOWS'|'LUSTRE',
            'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
            'FailureDetails': {
                'Message': 'string'
            },
            'StorageCapacity': 123,
            'StorageType': 'SSD'|'HDD',
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ],
            'NetworkInterfaceIds': [
                'string',
            ],
            'DNSName': 'string',
            'KmsKeyId': 'string',
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'WindowsConfiguration': {
                'ActiveDirectoryId': 'string',
                'SelfManagedActiveDirectoryConfiguration': {
                    'DomainName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string',
                    'FileSystemAdministratorsGroup': 'string',
                    'UserName': 'string',
                    'DnsIps': [
                        'string',
                    ]
                },
                'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
                'RemoteAdministrationEndpoint': 'string',
                'PreferredSubnetId': 'string',
                'PreferredFileServerIp': 'string',
                'ThroughputCapacity': 123,
                'MaintenanceOperationsInProgress': [
                    'PATCHING'|'BACKING_UP',
                ],
                'WeeklyMaintenanceStartTime': 'string',
                'DailyAutomaticBackupStartTime': 'string',
                'AutomaticBackupRetentionDays': 123,
                'CopyTagsToBackups': True|False
            },
            'LustreConfiguration': {
                'WeeklyMaintenanceStartTime': 'string',
                'DataRepositoryConfiguration': {
                    'ImportPath': 'string',
                    'ExportPath': 'string',
                    'ImportedFileChunkSize': 123
                },
                'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
                'PerUnitStorageThroughput': 123,
                'MountName': 'string'
            }
        }
    }
    
    
    :returns: 
    ClientRequestToken (string) -- (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
    This field is autopopulated if not provided.
    
    FileSystemType (string) -- [REQUIRED]
    The type of Amazon FSx file system to create, either WINDOWS or LUSTRE .
    
    StorageCapacity (integer) -- [REQUIRED]
    Sets the storage capacity of the file system that you\'re creating.
    For Lustre file systems:
    
    For SCRATCH_2 and PERSISTENT_1 deployment types, valid values are 1.2, 2.4, and increments of 2.4 TiB.
    For SCRATCH_1 deployment type, valid values are 1.2, 2.4, and increments of 3.6 TiB.
    
    For Windows file systems:
    
    If StorageType=SSD , valid values are 32 GiB - 65,536 GiB (64 TiB).
    If StorageType=HDD , valid values are 2000 GiB - 65,536 GiB (64 TiB).
    
    
    StorageType (string) -- Sets the storage type for the Amazon FSx for Windows file system you\'re creating. Valid values are SSD and HDD .
    
    Set to SSD to use solid state drive storage. SSD is supported on all Windows deployment types.
    Set to HDD to use hard disk drive storage. HDD is supported on SINGLE_AZ_2 and MULTI_AZ_1 Windows file system deployment types.
    
    Default value is SSD . For more information, see Storage Type Options in the Amazon FSx for Windows User Guide .
    
    SubnetIds (list) -- [REQUIRED]
    Specifies the IDs of the subnets that the file system will be accessible from. For Windows MULTI_AZ_1 file system deployment types, provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the WindowsConfiguration > PreferredSubnetID property.
    For Windows SINGLE_AZ_1 and SINGLE_AZ_2 file system deployment types and Lustre file systems, provide exactly one subnet ID. The file server is launched in that subnet\'s Availability Zone.
    
    (string) --The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.
    
    
    
    SecurityGroupIds (list) -- A list of IDs specifying the security groups to apply to all network interfaces created for file system access. This list isn\'t returned in later requests to describe the file system.
    
    (string) --The ID of your Amazon EC2 security group. This ID is used to control network access to the endpoint that Amazon FSx creates on your behalf in each subnet. For more information, see Amazon EC2 Security Groups for Linux Instances in the Amazon EC2 User Guide .
    
    
    
    Tags (list) -- The tags to apply to the file system being created. The key value of the Name tag appears in the console as the file system name.
    
    (dict) --Specifies a key-value pair for a resource tag.
    
    Key (string) --A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.
    
    Value (string) --A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .
    
    
    
    
    
    KmsKeyId (string) -- The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file system\'s data for Amazon FSx for Windows File Server file systems and Amazon FSx for Lustre PERSISTENT_1 file systems at rest. In either case, if not specified, the Amazon FSx managed key is used. The Amazon FSx for Lustre SCRATCH_1 and SCRATCH_2 file systems are always encrypted at rest using Amazon FSx managed keys. For more information, see Encrypt in the AWS Key Management Service API Reference .
    WindowsConfiguration (dict) -- The Microsoft Windows configuration for the file system being created.
    
    ActiveDirectoryId (string) --The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file system should join when it\'s created.
    
    SelfManagedActiveDirectoryConfiguration (dict) --The configuration that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory.
    
    DomainName (string) -- [REQUIRED]The fully qualified domain name of the self-managed AD directory, such as corp.example.com .
    
    OrganizationalUnitDistinguishedName (string) --(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. Amazon FSx only accepts OU as the direct parent of the file system. An example is OU=FSx,DC=yourdomain,DC=corp,DC=com . To learn more, see RFC 2253 . If none is provided, the FSx file system is created in the default location of your self-managed AD directory.
    
    Warning
    Only Organizational Unit (OU) objects can be the direct parent of the file system that you\'re creating.
    
    
    FileSystemAdministratorsGroup (string) --(Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don\'t provide one, your AD domain\'s Domain Admins group is used.
    
    UserName (string) -- [REQUIRED]The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in OrganizationalUnitDistinguishedName , or in the default location of your AD domain.
    
    Password (string) -- [REQUIRED]The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
    
    DnsIps (list) -- [REQUIRED]A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the one in which your Amazon FSx file system is being created, or in the private IP version 4 (IPv4) address ranges, as specified in RFC 1918 :
    
    10.0.0.0 - 10.255.255.255 (10/8 prefix)
    172.16.0.0 - 172.31.255.255 (172.16/12 prefix)
    192.168.0.0 - 192.168.255.255 (192.168/16 prefix)
    
    
    (string) --
    
    
    
    
    DeploymentType (string) --Specifies the file system deployment type, valid values are the following:
    
    MULTI_AZ_1 - Deploys a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. You can only deploy a Multi-AZ file system in AWS Regions that have a minimum of three Availability Zones. Also supports HDD storage type
    SINGLE_AZ_1 - (Default) Choose to deploy a file system that is configured for single AZ redundancy.
    SINGLE_AZ_2 - The latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports HDD storage type.
    
    For more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems .
    
    PreferredSubnetId (string) --Required when DeploymentType is set to MULTI_AZ_1 . This specifies the subnet in which you want the preferred file server to be located. For in-AWS applications, we recommend that you launch your clients in the same Availability Zone (AZ) as your preferred file server to reduce cross-AZ data transfer costs and minimize latency.
    
    ThroughputCapacity (integer) -- [REQUIRED]The throughput of an Amazon FSx file system, measured in megabytes per second, in 2 to the n th increments, between 2^3 (8) and 2^11 (2048).
    
    WeeklyMaintenanceStartTime (string) --The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone.
    
    DailyAutomaticBackupStartTime (string) --The preferred time to take daily automatic backups, formatted HH:MM in the UTC time zone.
    
    AutomaticBackupRetentionDays (integer) --The number of days to retain automatic backups. The default is to retain backups for 7 days. Setting this value to 0 disables the creation of automatic backups. The maximum retention period for backups is 35 days.
    
    CopyTagsToBackups (boolean) --A boolean flag indicating whether tags for the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn\'t specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.
    
    
    
    LustreConfiguration (dict) -- The Lustre configuration for the file system being created.
    
    WeeklyMaintenanceStartTime (string) --The preferred time to perform weekly maintenance, in the UTC time zone.
    
    ImportPath (string) --(Optional) The path to the Amazon S3 bucket (including the optional prefix) that you\'re using as the data repository for your Amazon FSx for Lustre file system. The root of your FSx for Lustre file system will be mapped to the root of the Amazon S3 bucket you select. An example is s3://import-bucket/optional-prefix . If you specify a prefix after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.
    
    ExportPath (string) --(Optional) The path in Amazon S3 where the root of your Amazon FSx file system is exported. The path must use the same Amazon S3 bucket as specified in ImportPath. You can provide an optional prefix to which new and changed data is to be exported from your Amazon FSx for Lustre file system. If an ExportPath value is not provided, Amazon FSx sets a default export path, s3://import-bucket/FSxLustre[creation-timestamp] . The timestamp is in UTC format, for example s3://import-bucket/FSxLustre20181105T222312Z .
    The Amazon S3 export bucket must be the same as the import bucket specified by ImportPath . If you only specify a bucket name, such as s3://import-bucket , you get a 1:1 mapping of file system objects to S3 bucket objects. This mapping means that the input data in S3 is overwritten on export. If you provide a custom prefix in the export path, such as s3://import-bucket/[custom-optional-prefix] , Amazon FSx exports the contents of your file system to that export prefix in the Amazon S3 bucket.
    
    ImportedFileChunkSize (integer) --(Optional) For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
    The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.
    
    DeploymentType (string) --(Optional) Choose SCRATCH_1 and SCRATCH_2 deployment types when you need temporary storage and shorter-term processing of data. The SCRATCH_2 deployment type provides in-transit encryption of data and higher burst throughput capacity than SCRATCH_1 .
    Choose PERSISTENT_1 deployment type for longer-term storage and workloads and encryption of data in transit. To learn more about deployment types, see FSx for Lustre Deployment Options .
    Encryption of data in-transit is automatically enabled when you access a SCRATCH_2 or PERSISTENT_1 file system from Amazon EC2 instances that support this feature . (Default = SCRATCH_1 )
    Encryption of data in-transit for SCRATCH_2 and PERSISTENT_1 deployment types is supported when accessed from supported instance types in supported AWS Regions. To learn more, Encrypting Data in Transit .
    
    PerUnitStorageThroughput (integer) --Required for the PERSISTENT_1 deployment type, describes the amount of read and write throughput for each 1 tebibyte of storage, in MB/s/TiB. File system throughput capacity is calculated by multiplying \xef\xac\x81le system storage capacity (TiB) by the PerUnitStorageThroughput (MB/s/TiB). For a 2.4 TiB \xef\xac\x81le system, provisioning 50 MB/s/TiB of PerUnitStorageThroughput yields 117 MB/s of \xef\xac\x81le system throughput. You pay for the amount of throughput that you provision.
    Valid values are 50, 100, 200.
    
    
    
    
    """
    pass

def create_file_system_from_backup(BackupId=None, ClientRequestToken=None, SubnetIds=None, SecurityGroupIds=None, Tags=None, WindowsConfiguration=None, StorageType=None):
    """
    Creates a new Amazon FSx file system from an existing Amazon FSx for Windows File Server backup.
    If a file system with the specified client request token exists and the parameters match, this operation returns the description of the file system. If a client request token specified by the file system exists and the parameters don\'t match, this call returns IncompatibleParameterError . If a file system with the specified client request token doesn\'t exist, this operation does the following:
    Parameters like Active Directory, default share name, automatic backup, and backup settings default to the parameters of the file system that was backed up, unless overridden. You can explicitly supply other settings.
    By using the idempotent operation, you can retry a CreateFileSystemFromBackup call without the risk of creating an extra file system. This approach can be useful when an initial call fails in a way that makes it unclear whether a file system was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a file system, the client receives success as long as the parameters are the same.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_file_system_from_backup(
        BackupId='string',
        ClientRequestToken='string',
        SubnetIds=[
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
        WindowsConfiguration={
            'ActiveDirectoryId': 'string',
            'SelfManagedActiveDirectoryConfiguration': {
                'DomainName': 'string',
                'OrganizationalUnitDistinguishedName': 'string',
                'FileSystemAdministratorsGroup': 'string',
                'UserName': 'string',
                'Password': 'string',
                'DnsIps': [
                    'string',
                ]
            },
            'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
            'PreferredSubnetId': 'string',
            'ThroughputCapacity': 123,
            'WeeklyMaintenanceStartTime': 'string',
            'DailyAutomaticBackupStartTime': 'string',
            'AutomaticBackupRetentionDays': 123,
            'CopyTagsToBackups': True|False
        },
        StorageType='SSD'|'HDD'
    )
    
    
    :type BackupId: string
    :param BackupId: [REQUIRED]\nThe ID of the backup. Specifies the backup to use if you\'re creating a file system from an existing backup.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.\nThis field is autopopulated if not provided.\n

    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]\nSpecifies the IDs of the subnets that the file system will be accessible from. For Windows MULTI_AZ_1 file system deployment types, provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the WindowsConfiguration > PreferredSubnetID property.\nFor Windows SINGLE_AZ_1 and SINGLE_AZ_2 deployment types and Lustre file systems, provide exactly one subnet ID. The file server is launched in that subnet\'s Availability Zone.\n\n(string) --The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.\n\n\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups apply to all network interfaces. This value isn\'t returned in later DescribeFileSystem requests.\n\n(string) --The ID of your Amazon EC2 security group. This ID is used to control network access to the endpoint that Amazon FSx creates on your behalf in each subnet. For more information, see Amazon EC2 Security Groups for Linux Instances in the Amazon EC2 User Guide .\n\n\n

    :type Tags: list
    :param Tags: The tags to be applied to the file system at file system creation. The key value of the Name tag appears in the console as the file system name.\n\n(dict) --Specifies a key-value pair for a resource tag.\n\nKey (string) --A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.\n\nValue (string) --A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .\n\n\n\n\n

    :type WindowsConfiguration: dict
    :param WindowsConfiguration: The configuration for this Microsoft Windows file system.\n\nActiveDirectoryId (string) --The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file system should join when it\'s created.\n\nSelfManagedActiveDirectoryConfiguration (dict) --The configuration that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory.\n\nDomainName (string) -- [REQUIRED]The fully qualified domain name of the self-managed AD directory, such as corp.example.com .\n\nOrganizationalUnitDistinguishedName (string) --(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. Amazon FSx only accepts OU as the direct parent of the file system. An example is OU=FSx,DC=yourdomain,DC=corp,DC=com . To learn more, see RFC 2253 . If none is provided, the FSx file system is created in the default location of your self-managed AD directory.\n\nWarning\nOnly Organizational Unit (OU) objects can be the direct parent of the file system that you\'re creating.\n\n\nFileSystemAdministratorsGroup (string) --(Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don\'t provide one, your AD domain\'s Domain Admins group is used.\n\nUserName (string) -- [REQUIRED]The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in OrganizationalUnitDistinguishedName , or in the default location of your AD domain.\n\nPassword (string) -- [REQUIRED]The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.\n\nDnsIps (list) -- [REQUIRED]A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the one in which your Amazon FSx file system is being created, or in the private IP version 4 (IPv4) address ranges, as specified in RFC 1918 :\n\n10.0.0.0 - 10.255.255.255 (10/8 prefix)\n172.16.0.0 - 172.31.255.255 (172.16/12 prefix)\n192.168.0.0 - 192.168.255.255 (192.168/16 prefix)\n\n\n(string) --\n\n\n\n\nDeploymentType (string) --Specifies the file system deployment type, valid values are the following:\n\nMULTI_AZ_1 - Deploys a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. You can only deploy a Multi-AZ file system in AWS Regions that have a minimum of three Availability Zones. Also supports HDD storage type\nSINGLE_AZ_1 - (Default) Choose to deploy a file system that is configured for single AZ redundancy.\nSINGLE_AZ_2 - The latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports HDD storage type.\n\nFor more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems .\n\nPreferredSubnetId (string) --Required when DeploymentType is set to MULTI_AZ_1 . This specifies the subnet in which you want the preferred file server to be located. For in-AWS applications, we recommend that you launch your clients in the same Availability Zone (AZ) as your preferred file server to reduce cross-AZ data transfer costs and minimize latency.\n\nThroughputCapacity (integer) -- [REQUIRED]The throughput of an Amazon FSx file system, measured in megabytes per second, in 2 to the n th increments, between 2^3 (8) and 2^11 (2048).\n\nWeeklyMaintenanceStartTime (string) --The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone.\n\nDailyAutomaticBackupStartTime (string) --The preferred time to take daily automatic backups, formatted HH:MM in the UTC time zone.\n\nAutomaticBackupRetentionDays (integer) --The number of days to retain automatic backups. The default is to retain backups for 7 days. Setting this value to 0 disables the creation of automatic backups. The maximum retention period for backups is 35 days.\n\nCopyTagsToBackups (boolean) --A boolean flag indicating whether tags for the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn\'t specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.\n\n\n

    :type StorageType: string
    :param StorageType: Sets the storage type for the Windows file system you\'re creating from a backup. Valid values are SSD and HDD .\n\nSet to SSD to use solid state drive storage. Supported on all Windows deployment types.\nSet to HDD to use hard disk drive storage. Supported on SINGLE_AZ_2 and MULTI_AZ_1 Windows file system deployment types.\n\nDefault value is SSD .\n\nNote\nHDD and SSD storage types have different minimum storage capacity requirements. A restored file system\'s storage capacity is tied to the file system that was backed up. You can create a file system that uses HDD storage from a backup of a file system that used SSD storage only if the original SSD file system had a storage capacity of at least 2000 GiB.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FileSystem': {
        'OwnerId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'FileSystemId': 'string',
        'FileSystemType': 'WINDOWS'|'LUSTRE',
        'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
        'FailureDetails': {
            'Message': 'string'
        },
        'StorageCapacity': 123,
        'StorageType': 'SSD'|'HDD',
        'VpcId': 'string',
        'SubnetIds': [
            'string',
        ],
        'NetworkInterfaceIds': [
            'string',
        ],
        'DNSName': 'string',
        'KmsKeyId': 'string',
        'ResourceARN': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'WindowsConfiguration': {
            'ActiveDirectoryId': 'string',
            'SelfManagedActiveDirectoryConfiguration': {
                'DomainName': 'string',
                'OrganizationalUnitDistinguishedName': 'string',
                'FileSystemAdministratorsGroup': 'string',
                'UserName': 'string',
                'DnsIps': [
                    'string',
                ]
            },
            'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
            'RemoteAdministrationEndpoint': 'string',
            'PreferredSubnetId': 'string',
            'PreferredFileServerIp': 'string',
            'ThroughputCapacity': 123,
            'MaintenanceOperationsInProgress': [
                'PATCHING'|'BACKING_UP',
            ],
            'WeeklyMaintenanceStartTime': 'string',
            'DailyAutomaticBackupStartTime': 'string',
            'AutomaticBackupRetentionDays': 123,
            'CopyTagsToBackups': True|False
        },
        'LustreConfiguration': {
            'WeeklyMaintenanceStartTime': 'string',
            'DataRepositoryConfiguration': {
                'ImportPath': 'string',
                'ExportPath': 'string',
                'ImportedFileChunkSize': 123
            },
            'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
            'PerUnitStorageThroughput': 123,
            'MountName': 'string'
        }
    }
}


Response Structure

(dict) --
The response object for the CreateFileSystemFromBackup operation.

FileSystem (dict) --
A description of the file system.

OwnerId (string) --
The AWS account that created the file system. If the file system was created by an AWS Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is the owner.

CreationTime (datetime) --
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId (string) --
The system-generated, unique 17-digit ID of the file system.

FileSystemType (string) --
The type of Amazon FSx file system, either LUSTRE or WINDOWS .

Lifecycle (string) --
The lifecycle status of the file system, following are the possible values and what they mean:

AVAILABLE - The file system is in a healthy state, and is reachable and available for use.
CREATING - Amazon FSx is creating the new file system.
DELETING - Amazon FSx is deleting an existing file system.
FAILED - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
MISCONFIGURED indicates that the file system is in a failed but recoverable state.
UPDATING indicates that the file system is undergoing a customer initiated update.


FailureDetails (dict) --
A structure providing details of any failures that occur when creating the file system has failed.

Message (string) --
A message describing any failures that occurred during file system creation.



StorageCapacity (integer) --
The storage capacity of the file system in gigabytes (GB).

StorageType (string) --
The storage type of the file system. Valid values are SSD and HDD . If set to SSD , the file system uses solid state drive storage. If set to HDD , the file system uses hard disk drive storage.

VpcId (string) --
The ID of the primary VPC for the file system.

SubnetIds (list) --
Specifies the IDs of the subnets that the file system is accessible from. For Windows MULTI_AZ_1 file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the PreferredSubnetID property. All other file systems have only one subnet ID.
For Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the endpoint for the file system. For MULTI_AZ_1 Windows file systems, the endpoint for the file system is available in the PreferredSubnetID .

(string) --
The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.



NetworkInterfaceIds (list) --
The IDs of the elastic network interface from which a specific file system is accessible. The elastic network interface is automatically created in the same VPC that the Amazon FSx file system was created in. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide.
For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string) --
An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide for Linux Instances .



DNSName (string) --
The DNS name for the file system.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file system\'s data for Amazon FSx for Windows File Server file systems and persistent Amazon FSx for Lustre file systems at rest. In either case, if not specified, the Amazon FSx managed key is used. The scratch Amazon FSx for Lustre file systems are always encrypted at rest using Amazon FSx managed keys. For more information, see Encrypt in the AWS Key Management Service API Reference .

ResourceARN (string) --
The Amazon Resource Name (ARN) for the file system resource.

Tags (list) --
The tags to associate with the file system. For more information, see Tagging Your Amazon EC2 Resources in the Amazon EC2 User Guide .

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





WindowsConfiguration (dict) --
The configuration for this Microsoft Windows file system.

ActiveDirectoryId (string) --
The ID for an existing Microsoft Active Directory instance that the file system should join when it\'s created.

SelfManagedActiveDirectoryConfiguration (dict) --
The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server instance is joined.

DomainName (string) --
The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName (string) --
The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server instance is joined.

FileSystemAdministratorsGroup (string) --
The name of the domain group whose members have administrative privileges for the FSx file system.

UserName (string) --
The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps (list) --
A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string) --




DeploymentType (string) --
Specifies the file system deployment type, valid values are the following:

MULTI_AZ_1 - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
SINGLE_AZ_1 - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
SINGLE_AZ_2 - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see Single-AZ and Multi-AZ File Systems .

RemoteAdministrationEndpoint (string) --
For MULTI_AZ_1 deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this is the DNS name of the file system.
This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId (string) --
For MULTI_AZ_1 deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in SubnetIds property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this value is the same as that for SubnetIDs . For more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems

PreferredFileServerIp (string) --
For MULTI_AZ_1 deployment types, the IP address of the primary, or preferred, file server.
Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system\'s DNSName instead. For more information on mapping and mounting file shares, see Accessing File Shares .

ThroughputCapacity (integer) --
The throughput of an Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress (list) --
The list of maintenance operations in progress for this file system.

(string) --
An enumeration specifying the currently ongoing maintenance operation.



WeeklyMaintenanceStartTime (string) --
The preferred time to perform weekly maintenance, in the UTC time zone.

DailyAutomaticBackupStartTime (string) --
The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays (integer) --
The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 35 days.

CopyTagsToBackups (boolean) --
A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn\'t specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.



LustreConfiguration (dict) --
The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime (string) --
The UTC time that you want to begin your weekly maintenance window.

DataRepositoryConfiguration (dict) --
The data repository configuration object for Lustre file systems returned in the response of the CreateFileSystem operation.

ImportPath (string) --
The import path to the Amazon S3 bucket (and optional prefix) that you\'re using as the data repository for your FSx for Lustre file system, for example s3://import-bucket/optional-prefix . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath (string) --
The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize (integer) --
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.



DeploymentType (string) --
The deployment type of the FSX for Lustre file system.

PerUnitStorageThroughput (integer) --
Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for PERSISTENT_1 deployment types. Valid values are 50, 100, 200.

MountName (string) --
You use the MountName value when mounting the file system.
For the SCRATCH_1 deployment type, this value is always "fsx ". For SCRATCH_2 and PERSISTENT_1 deployment types, this value is a string that is unique within an AWS Region.











Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.ActiveDirectoryError
FSx.Client.exceptions.IncompatibleParameterError
FSx.Client.exceptions.InvalidNetworkSettings
FSx.Client.exceptions.ServiceLimitExceeded
FSx.Client.exceptions.BackupNotFound
FSx.Client.exceptions.InternalServerError
FSx.Client.exceptions.MissingFileSystemConfiguration


    :return: {
        'FileSystem': {
            'OwnerId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'FileSystemId': 'string',
            'FileSystemType': 'WINDOWS'|'LUSTRE',
            'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
            'FailureDetails': {
                'Message': 'string'
            },
            'StorageCapacity': 123,
            'StorageType': 'SSD'|'HDD',
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ],
            'NetworkInterfaceIds': [
                'string',
            ],
            'DNSName': 'string',
            'KmsKeyId': 'string',
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'WindowsConfiguration': {
                'ActiveDirectoryId': 'string',
                'SelfManagedActiveDirectoryConfiguration': {
                    'DomainName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string',
                    'FileSystemAdministratorsGroup': 'string',
                    'UserName': 'string',
                    'DnsIps': [
                        'string',
                    ]
                },
                'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
                'RemoteAdministrationEndpoint': 'string',
                'PreferredSubnetId': 'string',
                'PreferredFileServerIp': 'string',
                'ThroughputCapacity': 123,
                'MaintenanceOperationsInProgress': [
                    'PATCHING'|'BACKING_UP',
                ],
                'WeeklyMaintenanceStartTime': 'string',
                'DailyAutomaticBackupStartTime': 'string',
                'AutomaticBackupRetentionDays': 123,
                'CopyTagsToBackups': True|False
            },
            'LustreConfiguration': {
                'WeeklyMaintenanceStartTime': 'string',
                'DataRepositoryConfiguration': {
                    'ImportPath': 'string',
                    'ExportPath': 'string',
                    'ImportedFileChunkSize': 123
                },
                'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
                'PerUnitStorageThroughput': 123,
                'MountName': 'string'
            }
        }
    }
    
    
    :returns: 
    BackupId (string) -- [REQUIRED]
    The ID of the backup. Specifies the backup to use if you\'re creating a file system from an existing backup.
    
    ClientRequestToken (string) -- (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent creation. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.
    This field is autopopulated if not provided.
    
    SubnetIds (list) -- [REQUIRED]
    Specifies the IDs of the subnets that the file system will be accessible from. For Windows MULTI_AZ_1 file system deployment types, provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the WindowsConfiguration > PreferredSubnetID property.
    For Windows SINGLE_AZ_1 and SINGLE_AZ_2 deployment types and Lustre file systems, provide exactly one subnet ID. The file server is launched in that subnet\'s Availability Zone.
    
    (string) --The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.
    
    
    
    SecurityGroupIds (list) -- A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups apply to all network interfaces. This value isn\'t returned in later DescribeFileSystem requests.
    
    (string) --The ID of your Amazon EC2 security group. This ID is used to control network access to the endpoint that Amazon FSx creates on your behalf in each subnet. For more information, see Amazon EC2 Security Groups for Linux Instances in the Amazon EC2 User Guide .
    
    
    
    Tags (list) -- The tags to be applied to the file system at file system creation. The key value of the Name tag appears in the console as the file system name.
    
    (dict) --Specifies a key-value pair for a resource tag.
    
    Key (string) --A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.
    
    Value (string) --A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .
    
    
    
    
    
    WindowsConfiguration (dict) -- The configuration for this Microsoft Windows file system.
    
    ActiveDirectoryId (string) --The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file system should join when it\'s created.
    
    SelfManagedActiveDirectoryConfiguration (dict) --The configuration that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory.
    
    DomainName (string) -- [REQUIRED]The fully qualified domain name of the self-managed AD directory, such as corp.example.com .
    
    OrganizationalUnitDistinguishedName (string) --(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. Amazon FSx only accepts OU as the direct parent of the file system. An example is OU=FSx,DC=yourdomain,DC=corp,DC=com . To learn more, see RFC 2253 . If none is provided, the FSx file system is created in the default location of your self-managed AD directory.
    
    Warning
    Only Organizational Unit (OU) objects can be the direct parent of the file system that you\'re creating.
    
    
    FileSystemAdministratorsGroup (string) --(Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don\'t provide one, your AD domain\'s Domain Admins group is used.
    
    UserName (string) -- [REQUIRED]The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in OrganizationalUnitDistinguishedName , or in the default location of your AD domain.
    
    Password (string) -- [REQUIRED]The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
    
    DnsIps (list) -- [REQUIRED]A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the one in which your Amazon FSx file system is being created, or in the private IP version 4 (IPv4) address ranges, as specified in RFC 1918 :
    
    10.0.0.0 - 10.255.255.255 (10/8 prefix)
    172.16.0.0 - 172.31.255.255 (172.16/12 prefix)
    192.168.0.0 - 192.168.255.255 (192.168/16 prefix)
    
    
    (string) --
    
    
    
    
    DeploymentType (string) --Specifies the file system deployment type, valid values are the following:
    
    MULTI_AZ_1 - Deploys a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. You can only deploy a Multi-AZ file system in AWS Regions that have a minimum of three Availability Zones. Also supports HDD storage type
    SINGLE_AZ_1 - (Default) Choose to deploy a file system that is configured for single AZ redundancy.
    SINGLE_AZ_2 - The latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports HDD storage type.
    
    For more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems .
    
    PreferredSubnetId (string) --Required when DeploymentType is set to MULTI_AZ_1 . This specifies the subnet in which you want the preferred file server to be located. For in-AWS applications, we recommend that you launch your clients in the same Availability Zone (AZ) as your preferred file server to reduce cross-AZ data transfer costs and minimize latency.
    
    ThroughputCapacity (integer) -- [REQUIRED]The throughput of an Amazon FSx file system, measured in megabytes per second, in 2 to the n th increments, between 2^3 (8) and 2^11 (2048).
    
    WeeklyMaintenanceStartTime (string) --The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone.
    
    DailyAutomaticBackupStartTime (string) --The preferred time to take daily automatic backups, formatted HH:MM in the UTC time zone.
    
    AutomaticBackupRetentionDays (integer) --The number of days to retain automatic backups. The default is to retain backups for 7 days. Setting this value to 0 disables the creation of automatic backups. The maximum retention period for backups is 35 days.
    
    CopyTagsToBackups (boolean) --A boolean flag indicating whether tags for the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn\'t specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.
    
    
    
    StorageType (string) -- Sets the storage type for the Windows file system you\'re creating from a backup. Valid values are SSD and HDD .
    
    Set to SSD to use solid state drive storage. Supported on all Windows deployment types.
    Set to HDD to use hard disk drive storage. Supported on SINGLE_AZ_2 and MULTI_AZ_1 Windows file system deployment types.
    
    Default value is SSD .
    
    Note
    HDD and SSD storage types have different minimum storage capacity requirements. A restored file system\'s storage capacity is tied to the file system that was backed up. You can create a file system that uses HDD storage from a backup of a file system that used SSD storage only if the original SSD file system had a storage capacity of at least 2000 GiB.
    
    
    
    """
    pass

def delete_backup(BackupId=None, ClientRequestToken=None):
    """
    Deletes an Amazon FSx for Windows File Server backup, deleting its contents. After deletion, the backup no longer exists, and its data is gone.
    The DeleteBackup call returns instantly. The backup will not show up in later DescribeBackups calls.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backup(
        BackupId='string',
        ClientRequestToken='string'
    )
    
    
    :type BackupId: string
    :param BackupId: [REQUIRED]\nThe ID of the backup you want to delete.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent deletion. This is automatically filled on your behalf when using the AWS CLI or SDK.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BackupId': 'string',
    'Lifecycle': 'AVAILABLE'|'CREATING'|'DELETED'|'FAILED'
}


Response Structure

(dict) --
The response object for DeleteBackup operation.

BackupId (string) --
The ID of the backup deleted.

Lifecycle (string) --
The lifecycle of the backup. Should be DELETED .







Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.BackupInProgress
FSx.Client.exceptions.BackupNotFound
FSx.Client.exceptions.BackupRestoring
FSx.Client.exceptions.IncompatibleParameterError
FSx.Client.exceptions.InternalServerError


    :return: {
        'BackupId': 'string',
        'Lifecycle': 'AVAILABLE'|'CREATING'|'DELETED'|'FAILED'
    }
    
    
    :returns: 
    FSx.Client.exceptions.BadRequest
    FSx.Client.exceptions.BackupInProgress
    FSx.Client.exceptions.BackupNotFound
    FSx.Client.exceptions.BackupRestoring
    FSx.Client.exceptions.IncompatibleParameterError
    FSx.Client.exceptions.InternalServerError
    
    """
    pass

def delete_file_system(FileSystemId=None, ClientRequestToken=None, WindowsConfiguration=None):
    """
    Deletes a file system, deleting its contents. After deletion, the file system no longer exists, and its data is gone. Any existing automatic backups will also be deleted.
    By default, when you delete an Amazon FSx for Windows File Server file system, a final backup is created upon deletion. This final backup is not subject to the file system\'s retention policy, and must be manually deleted.
    The DeleteFileSystem action returns while the file system has the DELETING status. You can check the file system deletion status by calling the  DescribeFileSystems action, which returns a list of file systems in your account. If you pass the file system ID for a deleted file system, the  DescribeFileSystems returns a FileSystemNotFound error.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_file_system(
        FileSystemId='string',
        ClientRequestToken='string',
        WindowsConfiguration={
            'SkipFinalBackup': True|False,
            'FinalBackupTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system you want to delete.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent deletion. This is automatically filled on your behalf when using the AWS CLI or SDK.\nThis field is autopopulated if not provided.\n

    :type WindowsConfiguration: dict
    :param WindowsConfiguration: The configuration object for the Microsoft Windows file system used in the DeleteFileSystem operation.\n\nSkipFinalBackup (boolean) --By default, Amazon FSx for Windows takes a final backup on your behalf when the DeleteFileSystem operation is invoked. Doing this helps protect you from data loss, and we highly recommend taking the final backup. If you want to skip this backup, use this flag to do so.\n\nFinalBackupTags (list) --A set of tags for your final backup.\n\n(dict) --Specifies a key-value pair for a resource tag.\n\nKey (string) --A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.\n\nValue (string) --A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FileSystemId': 'string',
    'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
    'WindowsResponse': {
        'FinalBackupId': 'string',
        'FinalBackupTags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
The response object for the DeleteFileSystem operation.

FileSystemId (string) --
The ID of the file system being deleted.

Lifecycle (string) --
The file system lifecycle for the deletion request. Should be DELETING .

WindowsResponse (dict) --
The response object for the Microsoft Windows file system used in the DeleteFileSystem operation.

FinalBackupId (string) --
The ID of the final backup for this file system.

FinalBackupTags (list) --
The set of tags applied to the final backup.

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .













Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.IncompatibleParameterError
FSx.Client.exceptions.FileSystemNotFound
FSx.Client.exceptions.ServiceLimitExceeded
FSx.Client.exceptions.InternalServerError


    :return: {
        'FileSystemId': 'string',
        'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
        'WindowsResponse': {
            'FinalBackupId': 'string',
            'FinalBackupTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    FSx.Client.exceptions.BadRequest
    FSx.Client.exceptions.IncompatibleParameterError
    FSx.Client.exceptions.FileSystemNotFound
    FSx.Client.exceptions.ServiceLimitExceeded
    FSx.Client.exceptions.InternalServerError
    
    """
    pass

def describe_backups(BackupIds=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Returns the description of specific Amazon FSx for Windows File Server backups, if a BackupIds value is provided for that backup. Otherwise, it returns all backups owned by your AWS account in the AWS Region of the endpoint that you\'re calling.
    When retrieving all backups, you can optionally specify the MaxResults parameter to limit the number of backups in a response. If more backups remain, Amazon FSx returns a NextToken value in the response. In this case, send a later request with the NextToken request parameter set to the value of NextToken from the last response.
    This action is used in an iterative process to retrieve a list of your backups. DescribeBackups is called first without a NextToken value. Then the action continues to be called with the NextToken parameter set to the value of the last NextToken value until a response has no NextToken .
    When using this action, keep the following in mind:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_backups(
        BackupIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'file-system-id'|'backup-type',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type BackupIds: list
    :param BackupIds: (Optional) IDs of the backups you want to retrieve (String). This overrides any filters. If any IDs are not found, BackupNotFound will be thrown.\n\n(string) --The ID of the backup. Specifies the backup to use if you\'re creating a file system from an existing backup.\n\n\n

    :type Filters: list
    :param Filters: (Optional) Filters structure. Supported names are file-system-id and backup-type.\n\n(dict) --A filter used to restrict the results of describe calls. You can use multiple filters to return results that meet all applied filter requirements.\n\nName (string) --The name for this filter.\n\nValues (list) --The values of the filter. These are all the values for any of the applied filters.\n\n(string) --The value for a filter.\n\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: (Optional) Maximum number of backups to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the MaxResults parameter specified in the request and the service\'s internal maximum number of items per page.

    :type NextToken: string
    :param NextToken: (Optional) Opaque pagination token returned from a previous DescribeBackups operation (String). If a token present, the action continues the list from where the returning call left off.

    :rtype: dict

ReturnsResponse Syntax
{
    'Backups': [
        {
            'BackupId': 'string',
            'Lifecycle': 'AVAILABLE'|'CREATING'|'DELETED'|'FAILED',
            'FailureDetails': {
                'Message': 'string'
            },
            'Type': 'AUTOMATIC'|'USER_INITIATED',
            'ProgressPercent': 123,
            'CreationTime': datetime(2015, 1, 1),
            'KmsKeyId': 'string',
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'FileSystem': {
                'OwnerId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'FileSystemId': 'string',
                'FileSystemType': 'WINDOWS'|'LUSTRE',
                'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
                'FailureDetails': {
                    'Message': 'string'
                },
                'StorageCapacity': 123,
                'StorageType': 'SSD'|'HDD',
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'NetworkInterfaceIds': [
                    'string',
                ],
                'DNSName': 'string',
                'KmsKeyId': 'string',
                'ResourceARN': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'WindowsConfiguration': {
                    'ActiveDirectoryId': 'string',
                    'SelfManagedActiveDirectoryConfiguration': {
                        'DomainName': 'string',
                        'OrganizationalUnitDistinguishedName': 'string',
                        'FileSystemAdministratorsGroup': 'string',
                        'UserName': 'string',
                        'DnsIps': [
                            'string',
                        ]
                    },
                    'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
                    'RemoteAdministrationEndpoint': 'string',
                    'PreferredSubnetId': 'string',
                    'PreferredFileServerIp': 'string',
                    'ThroughputCapacity': 123,
                    'MaintenanceOperationsInProgress': [
                        'PATCHING'|'BACKING_UP',
                    ],
                    'WeeklyMaintenanceStartTime': 'string',
                    'DailyAutomaticBackupStartTime': 'string',
                    'AutomaticBackupRetentionDays': 123,
                    'CopyTagsToBackups': True|False
                },
                'LustreConfiguration': {
                    'WeeklyMaintenanceStartTime': 'string',
                    'DataRepositoryConfiguration': {
                        'ImportPath': 'string',
                        'ExportPath': 'string',
                        'ImportedFileChunkSize': 123
                    },
                    'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
                    'PerUnitStorageThroughput': 123,
                    'MountName': 'string'
                }
            },
            'DirectoryInformation': {
                'DomainName': 'string',
                'ActiveDirectoryId': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Response object for DescribeBackups operation.

Backups (list) --
Any array of backups.

(dict) --
A backup of an Amazon FSx for Windows File Server file system. You can create a new file system from a backup to protect against data loss.

BackupId (string) --
The ID of the backup.

Lifecycle (string) --
The lifecycle status of the backup.

FailureDetails (dict) --
Details explaining any failures that occur when creating a backup.

Message (string) --
A message describing the backup creation failure.



Type (string) --
The type of the backup.

ProgressPercent (integer) --
The current percent of progress of an asynchronous task.

CreationTime (datetime) --
The time when a particular backup was created.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt this backup of the Amazon FSx for Windows file system\'s data at rest. Amazon FSx for Lustre does not support KMS encryption.

ResourceARN (string) --
The Amazon Resource Name (ARN) for the backup resource.

Tags (list) --
Tags associated with a particular file system.

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





FileSystem (dict) --
Metadata of the file system associated with the backup. This metadata is persisted even if the file system is deleted.

OwnerId (string) --
The AWS account that created the file system. If the file system was created by an AWS Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is the owner.

CreationTime (datetime) --
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId (string) --
The system-generated, unique 17-digit ID of the file system.

FileSystemType (string) --
The type of Amazon FSx file system, either LUSTRE or WINDOWS .

Lifecycle (string) --
The lifecycle status of the file system, following are the possible values and what they mean:

AVAILABLE - The file system is in a healthy state, and is reachable and available for use.
CREATING - Amazon FSx is creating the new file system.
DELETING - Amazon FSx is deleting an existing file system.
FAILED - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
MISCONFIGURED indicates that the file system is in a failed but recoverable state.
UPDATING indicates that the file system is undergoing a customer initiated update.


FailureDetails (dict) --
A structure providing details of any failures that occur when creating the file system has failed.

Message (string) --
A message describing any failures that occurred during file system creation.



StorageCapacity (integer) --
The storage capacity of the file system in gigabytes (GB).

StorageType (string) --
The storage type of the file system. Valid values are SSD and HDD . If set to SSD , the file system uses solid state drive storage. If set to HDD , the file system uses hard disk drive storage.

VpcId (string) --
The ID of the primary VPC for the file system.

SubnetIds (list) --
Specifies the IDs of the subnets that the file system is accessible from. For Windows MULTI_AZ_1 file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the PreferredSubnetID property. All other file systems have only one subnet ID.
For Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the endpoint for the file system. For MULTI_AZ_1 Windows file systems, the endpoint for the file system is available in the PreferredSubnetID .

(string) --
The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.



NetworkInterfaceIds (list) --
The IDs of the elastic network interface from which a specific file system is accessible. The elastic network interface is automatically created in the same VPC that the Amazon FSx file system was created in. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide.
For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string) --
An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide for Linux Instances .



DNSName (string) --
The DNS name for the file system.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file system\'s data for Amazon FSx for Windows File Server file systems and persistent Amazon FSx for Lustre file systems at rest. In either case, if not specified, the Amazon FSx managed key is used. The scratch Amazon FSx for Lustre file systems are always encrypted at rest using Amazon FSx managed keys. For more information, see Encrypt in the AWS Key Management Service API Reference .

ResourceARN (string) --
The Amazon Resource Name (ARN) for the file system resource.

Tags (list) --
The tags to associate with the file system. For more information, see Tagging Your Amazon EC2 Resources in the Amazon EC2 User Guide .

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





WindowsConfiguration (dict) --
The configuration for this Microsoft Windows file system.

ActiveDirectoryId (string) --
The ID for an existing Microsoft Active Directory instance that the file system should join when it\'s created.

SelfManagedActiveDirectoryConfiguration (dict) --
The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server instance is joined.

DomainName (string) --
The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName (string) --
The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server instance is joined.

FileSystemAdministratorsGroup (string) --
The name of the domain group whose members have administrative privileges for the FSx file system.

UserName (string) --
The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps (list) --
A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string) --




DeploymentType (string) --
Specifies the file system deployment type, valid values are the following:

MULTI_AZ_1 - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
SINGLE_AZ_1 - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
SINGLE_AZ_2 - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see Single-AZ and Multi-AZ File Systems .

RemoteAdministrationEndpoint (string) --
For MULTI_AZ_1 deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this is the DNS name of the file system.
This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId (string) --
For MULTI_AZ_1 deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in SubnetIds property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this value is the same as that for SubnetIDs . For more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems

PreferredFileServerIp (string) --
For MULTI_AZ_1 deployment types, the IP address of the primary, or preferred, file server.
Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system\'s DNSName instead. For more information on mapping and mounting file shares, see Accessing File Shares .

ThroughputCapacity (integer) --
The throughput of an Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress (list) --
The list of maintenance operations in progress for this file system.

(string) --
An enumeration specifying the currently ongoing maintenance operation.



WeeklyMaintenanceStartTime (string) --
The preferred time to perform weekly maintenance, in the UTC time zone.

DailyAutomaticBackupStartTime (string) --
The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays (integer) --
The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 35 days.

CopyTagsToBackups (boolean) --
A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn\'t specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.



LustreConfiguration (dict) --
The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime (string) --
The UTC time that you want to begin your weekly maintenance window.

DataRepositoryConfiguration (dict) --
The data repository configuration object for Lustre file systems returned in the response of the CreateFileSystem operation.

ImportPath (string) --
The import path to the Amazon S3 bucket (and optional prefix) that you\'re using as the data repository for your FSx for Lustre file system, for example s3://import-bucket/optional-prefix . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath (string) --
The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize (integer) --
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.



DeploymentType (string) --
The deployment type of the FSX for Lustre file system.

PerUnitStorageThroughput (integer) --
Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for PERSISTENT_1 deployment types. Valid values are 50, 100, 200.

MountName (string) --
You use the MountName value when mounting the file system.
For the SCRATCH_1 deployment type, this value is always "fsx ". For SCRATCH_2 and PERSISTENT_1 deployment types, this value is a string that is unique within an AWS Region.





DirectoryInformation (dict) --
The configuration of the self-managed Microsoft Active Directory (AD) to which the Windows File Server instance is joined.

DomainName (string) --
The fully qualified domain name of the self-managed AD directory.

ActiveDirectoryId (string) --
The ID of the AWS Managed Microsoft Active Directory instance to which the file system is joined.







NextToken (string) --
This is present if there are more backups than returned in the response (String). You can use the NextToken value in the later request to fetch the backups.







Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.FileSystemNotFound
FSx.Client.exceptions.BackupNotFound
FSx.Client.exceptions.InternalServerError


    :return: {
        'Backups': [
            {
                'BackupId': 'string',
                'Lifecycle': 'AVAILABLE'|'CREATING'|'DELETED'|'FAILED',
                'FailureDetails': {
                    'Message': 'string'
                },
                'Type': 'AUTOMATIC'|'USER_INITIATED',
                'ProgressPercent': 123,
                'CreationTime': datetime(2015, 1, 1),
                'KmsKeyId': 'string',
                'ResourceARN': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'FileSystem': {
                    'OwnerId': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'FileSystemId': 'string',
                    'FileSystemType': 'WINDOWS'|'LUSTRE',
                    'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
                    'FailureDetails': {
                        'Message': 'string'
                    },
                    'StorageCapacity': 123,
                    'StorageType': 'SSD'|'HDD',
                    'VpcId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'NetworkInterfaceIds': [
                        'string',
                    ],
                    'DNSName': 'string',
                    'KmsKeyId': 'string',
                    'ResourceARN': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'WindowsConfiguration': {
                        'ActiveDirectoryId': 'string',
                        'SelfManagedActiveDirectoryConfiguration': {
                            'DomainName': 'string',
                            'OrganizationalUnitDistinguishedName': 'string',
                            'FileSystemAdministratorsGroup': 'string',
                            'UserName': 'string',
                            'DnsIps': [
                                'string',
                            ]
                        },
                        'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
                        'RemoteAdministrationEndpoint': 'string',
                        'PreferredSubnetId': 'string',
                        'PreferredFileServerIp': 'string',
                        'ThroughputCapacity': 123,
                        'MaintenanceOperationsInProgress': [
                            'PATCHING'|'BACKING_UP',
                        ],
                        'WeeklyMaintenanceStartTime': 'string',
                        'DailyAutomaticBackupStartTime': 'string',
                        'AutomaticBackupRetentionDays': 123,
                        'CopyTagsToBackups': True|False
                    },
                    'LustreConfiguration': {
                        'WeeklyMaintenanceStartTime': 'string',
                        'DataRepositoryConfiguration': {
                            'ImportPath': 'string',
                            'ExportPath': 'string',
                            'ImportedFileChunkSize': 123
                        },
                        'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
                        'PerUnitStorageThroughput': 123,
                        'MountName': 'string'
                    }
                },
                'DirectoryInformation': {
                    'DomainName': 'string',
                    'ActiveDirectoryId': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    BackupIds (list) -- (Optional) IDs of the backups you want to retrieve (String). This overrides any filters. If any IDs are not found, BackupNotFound will be thrown.
    
    (string) --The ID of the backup. Specifies the backup to use if you\'re creating a file system from an existing backup.
    
    
    
    Filters (list) -- (Optional) Filters structure. Supported names are file-system-id and backup-type.
    
    (dict) --A filter used to restrict the results of describe calls. You can use multiple filters to return results that meet all applied filter requirements.
    
    Name (string) --The name for this filter.
    
    Values (list) --The values of the filter. These are all the values for any of the applied filters.
    
    (string) --The value for a filter.
    
    
    
    
    
    
    
    MaxResults (integer) -- (Optional) Maximum number of backups to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the MaxResults parameter specified in the request and the service\'s internal maximum number of items per page.
    NextToken (string) -- (Optional) Opaque pagination token returned from a previous DescribeBackups operation (String). If a token present, the action continues the list from where the returning call left off.
    
    """
    pass

def describe_data_repository_tasks(TaskIds=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Returns the description of specific Amazon FSx for Lustre data repository tasks, if one or more TaskIds values are provided in the request, or if filters are used in the request. You can use filters to narrow the response to include just tasks for specific file systems, or tasks in a specific lifecycle state. Otherwise, it returns all data repository tasks owned by your AWS account in the AWS Region of the endpoint that you\'re calling.
    When retrieving all tasks, you can paginate the response by using the optional MaxResults parameter to limit the number of tasks returned in a response. If more tasks remain, Amazon FSx returns a NextToken value in the response. In this case, send a later request with the NextToken request parameter set to the value of NextToken from the last response.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_data_repository_tasks(
        TaskIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'file-system-id'|'task-lifecycle',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type TaskIds: list
    :param TaskIds: (Optional) IDs of the tasks whose descriptions you want to retrieve (String).\n\n(string) --\n\n

    :type Filters: list
    :param Filters: (Optional) You can use filters to narrow the DescribeDataRepositoryTasks response to include just tasks for specific file systems, or tasks in a specific lifecycle state.\n\n(dict) --(Optional) An array of filter objects you can use to filter the response of data repository tasks you will see in the the response. You can filter the tasks returned in the response by one or more file system IDs, task lifecycles, and by task type. A filter object consists of a filter Name , and one or more Values for the filter.\n\nName (string) --Name of the task property to use in filtering the tasks returned in the response.\n\nUse file-system-id to retrieve data repository tasks for specific file systems.\nUse task-lifecycle to retrieve data repository tasks with one or more specific lifecycle states, as follows: CANCELED, EXECUTING, FAILED, PENDING, and SUCCEEDED.\n\n\nValues (list) --Use Values to include the specific file system IDs and task lifecycle states for the filters you are using.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of resources to return in the response. This value must be an integer greater than zero.

    :type NextToken: string
    :param NextToken: (Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous NextToken value left off.

    :rtype: dict

ReturnsResponse Syntax
{
    'DataRepositoryTasks': [
        {
            'TaskId': 'string',
            'Lifecycle': 'PENDING'|'EXECUTING'|'FAILED'|'SUCCEEDED'|'CANCELED'|'CANCELING',
            'Type': 'EXPORT_TO_REPOSITORY',
            'CreationTime': datetime(2015, 1, 1),
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'FileSystemId': 'string',
            'Paths': [
                'string',
            ],
            'FailureDetails': {
                'Message': 'string'
            },
            'Status': {
                'TotalCount': 123,
                'SucceededCount': 123,
                'FailedCount': 123,
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
            'Report': {
                'Enabled': True|False,
                'Path': 'string',
                'Format': 'REPORT_CSV_20191124',
                'Scope': 'FAILED_FILES_ONLY'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DataRepositoryTasks (list) --
The collection of data repository task descriptions returned.

(dict) --
A description of the data repository task. You use data repository tasks to perform bulk transfer operations between your Amazon FSx file system and its linked data repository.

TaskId (string) --
The system-generated, unique 17-digit ID of the data repository task.

Lifecycle (string) --
The lifecycle status of the data repository task, as follows:

PENDING - Amazon FSx has not started the task.
EXECUTING - Amazon FSx is processing the task.
FAILED - Amazon FSx was not able to complete the task. For example, there may be files the task failed to process. The  DataRepositoryTaskFailureDetails property provides more information about task failures.
SUCCEEDED - FSx completed the task successfully.
CANCELED - Amazon FSx canceled the task and it did not complete.
CANCELING - FSx is in process of canceling the task.


Note
You cannot delete an FSx for Lustre file system if there are data repository tasks for the file system in the PENDING or EXECUTING states. Please retry when the data repository task is finished (with a status of CANCELED , SUCCEEDED , or FAILED ). You can use the DescribeDataRepositoryTask action to monitor the task status. Contact the FSx team if you need to delete your file system immediately.


Type (string) --
The type of data repository task; EXPORT_TO_REPOSITORY is the only type currently supported.

CreationTime (datetime) --
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

StartTime (datetime) --
The time that Amazon FSx began processing the task.

EndTime (datetime) --
The time that Amazon FSx completed processing the task, populated after the task is complete.

ResourceARN (string) --
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .

Tags (list) --
A list of Tag values, with a maximum of 50 elements.

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





FileSystemId (string) --
The globally unique ID of the file system, assigned by Amazon FSx.

Paths (list) --
An array of paths on the Amazon FSx for Lustre file system that specify the data for the data repository task to process. For example, in an EXPORT_TO_REPOSITORY task, the paths specify which data to export to the linked data repository.
(Default) If Paths is not specified, Amazon FSx uses the file system root directory.

(string) --


FailureDetails (dict) --
Failure message describing why the task failed, it is populated only when Lifecycle is set to FAILED .

Message (string) --
A detailed error message.



Status (dict) --
Provides the status of the number of files that the task has processed successfully and failed to process.

TotalCount (integer) --
The total number of files that the task will process. While a task is executing, the sum of SucceededCount plus FailedCount may not equal TotalCount . When the task is complete, TotalCount equals the sum of SucceededCount plus FailedCount .

SucceededCount (integer) --
A running total of the number of files that the task has successfully processed.

FailedCount (integer) --
A running total of the number of files that the task failed to process.

LastUpdatedTime (datetime) --
The time at which the task status was last updated.



Report (dict) --
Provides a report detailing the data repository task results of the files processed that match the criteria specified in the report Scope parameter. FSx delivers the report to the file system\'s linked data repository in Amazon S3, using the path specified in the report Path parameter. You can specify whether or not a report gets generated for a task using the Enabled parameter.

Enabled (boolean) --
Set Enabled to True to generate a CompletionReport when the task completes. If set to true , then you need to provide a report Scope , Path , and Format . Set Enabled to False if you do not want a CompletionReport generated when the task completes.

Path (string) --
Required if Enabled is set to true . Specifies the location of the report on the file system\'s linked S3 data repository. An absolute path that defines where the completion report will be stored in the destination location. The Path you provide must be located within the file system\xe2\x80\x99s ExportPath. An example Path value is "s3://myBucket/myExportPath/optionalPrefix". The report provides the following information for each file in the report: FilePath, FileStatus, and ErrorCode. To learn more about a file system\'s ExportPath , see .

Format (string) --
Required if Enabled is set to true . Specifies the format of the CompletionReport . REPORT_CSV_20191124 is the only format currently supported. When Format is set to REPORT_CSV_20191124 , the CompletionReport is provided in CSV format, and is delivered to {path}/task-{id}/failures.csv .

Scope (string) --
Required if Enabled is set to true . Specifies the scope of the CompletionReport ; FAILED_FILES_ONLY is the only scope currently supported. When Scope is set to FAILED_FILES_ONLY , the CompletionReport only contains information about files that the data repository task failed to process.







NextToken (string) --
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous NextToken value left off.







Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.FileSystemNotFound
FSx.Client.exceptions.DataRepositoryTaskNotFound
FSx.Client.exceptions.InternalServerError


    :return: {
        'DataRepositoryTasks': [
            {
                'TaskId': 'string',
                'Lifecycle': 'PENDING'|'EXECUTING'|'FAILED'|'SUCCEEDED'|'CANCELED'|'CANCELING',
                'Type': 'EXPORT_TO_REPOSITORY',
                'CreationTime': datetime(2015, 1, 1),
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'ResourceARN': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'FileSystemId': 'string',
                'Paths': [
                    'string',
                ],
                'FailureDetails': {
                    'Message': 'string'
                },
                'Status': {
                    'TotalCount': 123,
                    'SucceededCount': 123,
                    'FailedCount': 123,
                    'LastUpdatedTime': datetime(2015, 1, 1)
                },
                'Report': {
                    'Enabled': True|False,
                    'Path': 'string',
                    'Format': 'REPORT_CSV_20191124',
                    'Scope': 'FAILED_FILES_ONLY'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    PENDING - Amazon FSx has not started the task.
    EXECUTING - Amazon FSx is processing the task.
    FAILED - Amazon FSx was not able to complete the task. For example, there may be files the task failed to process. The  DataRepositoryTaskFailureDetails property provides more information about task failures.
    SUCCEEDED - FSx completed the task successfully.
    CANCELED - Amazon FSx canceled the task and it did not complete.
    CANCELING - FSx is in process of canceling the task.
    
    """
    pass

def describe_file_systems(FileSystemIds=None, MaxResults=None, NextToken=None):
    """
    Returns the description of specific Amazon FSx file systems, if a FileSystemIds value is provided for that file system. Otherwise, it returns descriptions of all file systems owned by your AWS account in the AWS Region of the endpoint that you\'re calling.
    When retrieving all file system descriptions, you can optionally specify the MaxResults parameter to limit the number of descriptions in a response. If more file system descriptions remain, Amazon FSx returns a NextToken value in the response. In this case, send a later request with the NextToken request parameter set to the value of NextToken from the last response.
    This action is used in an iterative process to retrieve a list of your file system descriptions. DescribeFileSystems is called first without a NextToken value. Then the action continues to be called with the NextToken parameter set to the value of the last NextToken value until a response has no NextToken .
    When using this action, keep the following in mind:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_file_systems(
        FileSystemIds=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type FileSystemIds: list
    :param FileSystemIds: (Optional) IDs of the file systems whose descriptions you want to retrieve (String).\n\n(string) --The globally unique ID of the file system, assigned by Amazon FSx.\n\n\n

    :type MaxResults: integer
    :param MaxResults: (Optional) Maximum number of file systems to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the MaxResults parameter specified in the request and the service\'s internal maximum number of items per page.

    :type NextToken: string
    :param NextToken: (Optional) Opaque pagination token returned from a previous DescribeFileSystems operation (String). If a token present, the action continues the list from where the returning call left off.

    :rtype: dict

ReturnsResponse Syntax
{
    'FileSystems': [
        {
            'OwnerId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'FileSystemId': 'string',
            'FileSystemType': 'WINDOWS'|'LUSTRE',
            'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
            'FailureDetails': {
                'Message': 'string'
            },
            'StorageCapacity': 123,
            'StorageType': 'SSD'|'HDD',
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ],
            'NetworkInterfaceIds': [
                'string',
            ],
            'DNSName': 'string',
            'KmsKeyId': 'string',
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'WindowsConfiguration': {
                'ActiveDirectoryId': 'string',
                'SelfManagedActiveDirectoryConfiguration': {
                    'DomainName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string',
                    'FileSystemAdministratorsGroup': 'string',
                    'UserName': 'string',
                    'DnsIps': [
                        'string',
                    ]
                },
                'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
                'RemoteAdministrationEndpoint': 'string',
                'PreferredSubnetId': 'string',
                'PreferredFileServerIp': 'string',
                'ThroughputCapacity': 123,
                'MaintenanceOperationsInProgress': [
                    'PATCHING'|'BACKING_UP',
                ],
                'WeeklyMaintenanceStartTime': 'string',
                'DailyAutomaticBackupStartTime': 'string',
                'AutomaticBackupRetentionDays': 123,
                'CopyTagsToBackups': True|False
            },
            'LustreConfiguration': {
                'WeeklyMaintenanceStartTime': 'string',
                'DataRepositoryConfiguration': {
                    'ImportPath': 'string',
                    'ExportPath': 'string',
                    'ImportedFileChunkSize': 123
                },
                'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
                'PerUnitStorageThroughput': 123,
                'MountName': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The response object for DescribeFileSystems operation.

FileSystems (list) --
An array of file system descriptions.

(dict) --
A description of a specific Amazon FSx file system.

OwnerId (string) --
The AWS account that created the file system. If the file system was created by an AWS Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is the owner.

CreationTime (datetime) --
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId (string) --
The system-generated, unique 17-digit ID of the file system.

FileSystemType (string) --
The type of Amazon FSx file system, either LUSTRE or WINDOWS .

Lifecycle (string) --
The lifecycle status of the file system, following are the possible values and what they mean:

AVAILABLE - The file system is in a healthy state, and is reachable and available for use.
CREATING - Amazon FSx is creating the new file system.
DELETING - Amazon FSx is deleting an existing file system.
FAILED - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
MISCONFIGURED indicates that the file system is in a failed but recoverable state.
UPDATING indicates that the file system is undergoing a customer initiated update.


FailureDetails (dict) --
A structure providing details of any failures that occur when creating the file system has failed.

Message (string) --
A message describing any failures that occurred during file system creation.



StorageCapacity (integer) --
The storage capacity of the file system in gigabytes (GB).

StorageType (string) --
The storage type of the file system. Valid values are SSD and HDD . If set to SSD , the file system uses solid state drive storage. If set to HDD , the file system uses hard disk drive storage.

VpcId (string) --
The ID of the primary VPC for the file system.

SubnetIds (list) --
Specifies the IDs of the subnets that the file system is accessible from. For Windows MULTI_AZ_1 file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the PreferredSubnetID property. All other file systems have only one subnet ID.
For Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the endpoint for the file system. For MULTI_AZ_1 Windows file systems, the endpoint for the file system is available in the PreferredSubnetID .

(string) --
The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.



NetworkInterfaceIds (list) --
The IDs of the elastic network interface from which a specific file system is accessible. The elastic network interface is automatically created in the same VPC that the Amazon FSx file system was created in. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide.
For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string) --
An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide for Linux Instances .



DNSName (string) --
The DNS name for the file system.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file system\'s data for Amazon FSx for Windows File Server file systems and persistent Amazon FSx for Lustre file systems at rest. In either case, if not specified, the Amazon FSx managed key is used. The scratch Amazon FSx for Lustre file systems are always encrypted at rest using Amazon FSx managed keys. For more information, see Encrypt in the AWS Key Management Service API Reference .

ResourceARN (string) --
The Amazon Resource Name (ARN) for the file system resource.

Tags (list) --
The tags to associate with the file system. For more information, see Tagging Your Amazon EC2 Resources in the Amazon EC2 User Guide .

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





WindowsConfiguration (dict) --
The configuration for this Microsoft Windows file system.

ActiveDirectoryId (string) --
The ID for an existing Microsoft Active Directory instance that the file system should join when it\'s created.

SelfManagedActiveDirectoryConfiguration (dict) --
The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server instance is joined.

DomainName (string) --
The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName (string) --
The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server instance is joined.

FileSystemAdministratorsGroup (string) --
The name of the domain group whose members have administrative privileges for the FSx file system.

UserName (string) --
The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps (list) --
A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string) --




DeploymentType (string) --
Specifies the file system deployment type, valid values are the following:

MULTI_AZ_1 - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
SINGLE_AZ_1 - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
SINGLE_AZ_2 - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see Single-AZ and Multi-AZ File Systems .

RemoteAdministrationEndpoint (string) --
For MULTI_AZ_1 deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this is the DNS name of the file system.
This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId (string) --
For MULTI_AZ_1 deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in SubnetIds property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this value is the same as that for SubnetIDs . For more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems

PreferredFileServerIp (string) --
For MULTI_AZ_1 deployment types, the IP address of the primary, or preferred, file server.
Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system\'s DNSName instead. For more information on mapping and mounting file shares, see Accessing File Shares .

ThroughputCapacity (integer) --
The throughput of an Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress (list) --
The list of maintenance operations in progress for this file system.

(string) --
An enumeration specifying the currently ongoing maintenance operation.



WeeklyMaintenanceStartTime (string) --
The preferred time to perform weekly maintenance, in the UTC time zone.

DailyAutomaticBackupStartTime (string) --
The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays (integer) --
The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 35 days.

CopyTagsToBackups (boolean) --
A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn\'t specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.



LustreConfiguration (dict) --
The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime (string) --
The UTC time that you want to begin your weekly maintenance window.

DataRepositoryConfiguration (dict) --
The data repository configuration object for Lustre file systems returned in the response of the CreateFileSystem operation.

ImportPath (string) --
The import path to the Amazon S3 bucket (and optional prefix) that you\'re using as the data repository for your FSx for Lustre file system, for example s3://import-bucket/optional-prefix . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath (string) --
The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize (integer) --
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.



DeploymentType (string) --
The deployment type of the FSX for Lustre file system.

PerUnitStorageThroughput (integer) --
Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for PERSISTENT_1 deployment types. Valid values are 50, 100, 200.

MountName (string) --
You use the MountName value when mounting the file system.
For the SCRATCH_1 deployment type, this value is always "fsx ". For SCRATCH_2 and PERSISTENT_1 deployment types, this value is a string that is unique within an AWS Region.







NextToken (string) --
Present if there are more file systems than returned in the response (String). You can use the NextToken value in the later request to fetch the descriptions.







Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.FileSystemNotFound
FSx.Client.exceptions.InternalServerError


    :return: {
        'FileSystems': [
            {
                'OwnerId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'FileSystemId': 'string',
                'FileSystemType': 'WINDOWS'|'LUSTRE',
                'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
                'FailureDetails': {
                    'Message': 'string'
                },
                'StorageCapacity': 123,
                'StorageType': 'SSD'|'HDD',
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'NetworkInterfaceIds': [
                    'string',
                ],
                'DNSName': 'string',
                'KmsKeyId': 'string',
                'ResourceARN': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'WindowsConfiguration': {
                    'ActiveDirectoryId': 'string',
                    'SelfManagedActiveDirectoryConfiguration': {
                        'DomainName': 'string',
                        'OrganizationalUnitDistinguishedName': 'string',
                        'FileSystemAdministratorsGroup': 'string',
                        'UserName': 'string',
                        'DnsIps': [
                            'string',
                        ]
                    },
                    'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
                    'RemoteAdministrationEndpoint': 'string',
                    'PreferredSubnetId': 'string',
                    'PreferredFileServerIp': 'string',
                    'ThroughputCapacity': 123,
                    'MaintenanceOperationsInProgress': [
                        'PATCHING'|'BACKING_UP',
                    ],
                    'WeeklyMaintenanceStartTime': 'string',
                    'DailyAutomaticBackupStartTime': 'string',
                    'AutomaticBackupRetentionDays': 123,
                    'CopyTagsToBackups': True|False
                },
                'LustreConfiguration': {
                    'WeeklyMaintenanceStartTime': 'string',
                    'DataRepositoryConfiguration': {
                        'ImportPath': 'string',
                        'ExportPath': 'string',
                        'ImportedFileChunkSize': 123
                    },
                    'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
                    'PerUnitStorageThroughput': 123,
                    'MountName': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FileSystemIds (list) -- (Optional) IDs of the file systems whose descriptions you want to retrieve (String).
    
    (string) --The globally unique ID of the file system, assigned by Amazon FSx.
    
    
    
    MaxResults (integer) -- (Optional) Maximum number of file systems to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the MaxResults parameter specified in the request and the service\'s internal maximum number of items per page.
    NextToken (string) -- (Optional) Opaque pagination token returned from a previous DescribeFileSystems operation (String). If a token present, the action continues the list from where the returning call left off.
    
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

def list_tags_for_resource(ResourceARN=None, MaxResults=None, NextToken=None):
    """
    Lists tags for an Amazon FSx file systems and backups in the case of Amazon FSx for Windows File Server.
    When retrieving all tags, you can optionally specify the MaxResults parameter to limit the number of tags in a response. If more tags remain, Amazon FSx returns a NextToken value in the response. In this case, send a later request with the NextToken request parameter set to the value of NextToken from the last response.
    This action is used in an iterative process to retrieve a list of your tags. ListTagsForResource is called first without a NextToken value. Then the action continues to be called with the NextToken parameter set to the value of the last NextToken value until a response has no NextToken .
    When using this action, keep the following in mind:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe ARN of the Amazon FSx resource that will have its tags listed.\n

    :type MaxResults: integer
    :param MaxResults: (Optional) Maximum number of tags to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the MaxResults parameter specified in the request and the service\'s internal maximum number of items per page.

    :type NextToken: string
    :param NextToken: (Optional) Opaque pagination token returned from a previous ListTagsForResource operation (String). If a token present, the action continues the list from where the returning call left off.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The response object for ListTagsForResource operation.

Tags (list) --
A list of tags on the resource.

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





NextToken (string) --
This is present if there are more tags than returned in the response (String). You can use the NextToken value in the later request to fetch the tags.







Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.InternalServerError
FSx.Client.exceptions.ResourceNotFound
FSx.Client.exceptions.NotServiceResourceError
FSx.Client.exceptions.ResourceDoesNotSupportTagging


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ResourceARN (string) -- [REQUIRED]
    The ARN of the Amazon FSx resource that will have its tags listed.
    
    MaxResults (integer) -- (Optional) Maximum number of tags to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the MaxResults parameter specified in the request and the service\'s internal maximum number of items per page.
    NextToken (string) -- (Optional) Opaque pagination token returned from a previous ListTagsForResource operation (String). If a token present, the action continues the list from where the returning call left off.
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Tags an Amazon FSx resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Amazon FSx resource that you want to tag.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA list of tags for the resource. If a tag with a given key already exists, the value is replaced by the one specified in this parameter.\n\n(dict) --Specifies a key-value pair for a resource tag.\n\nKey (string) --A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.\n\nValue (string) --A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The response object for the TagResource operation.





Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.InternalServerError
FSx.Client.exceptions.ResourceNotFound
FSx.Client.exceptions.NotServiceResourceError
FSx.Client.exceptions.ResourceDoesNotSupportTagging


    :return: {}
    
    
    :returns: 
    FSx.Client.exceptions.BadRequest
    FSx.Client.exceptions.InternalServerError
    FSx.Client.exceptions.ResourceNotFound
    FSx.Client.exceptions.NotServiceResourceError
    FSx.Client.exceptions.ResourceDoesNotSupportTagging
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    This action removes a tag from an Amazon FSx resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe ARN of the Amazon FSx resource to untag.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of keys of tags on the resource to untag. In case the tag key doesn\'t exist, the call will still succeed to be idempotent.\n\n(string) --A string of 1 to 128 characters that specifies the key for a tag. Tag keys must be unique for the resource to which they are attached.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The response object for UntagResource action.





Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.InternalServerError
FSx.Client.exceptions.ResourceNotFound
FSx.Client.exceptions.NotServiceResourceError
FSx.Client.exceptions.ResourceDoesNotSupportTagging


    :return: {}
    
    
    :returns: 
    FSx.Client.exceptions.BadRequest
    FSx.Client.exceptions.InternalServerError
    FSx.Client.exceptions.ResourceNotFound
    FSx.Client.exceptions.NotServiceResourceError
    FSx.Client.exceptions.ResourceDoesNotSupportTagging
    
    """
    pass

def update_file_system(FileSystemId=None, ClientRequestToken=None, WindowsConfiguration=None, LustreConfiguration=None):
    """
    Updates a file system configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_file_system(
        FileSystemId='string',
        ClientRequestToken='string',
        WindowsConfiguration={
            'WeeklyMaintenanceStartTime': 'string',
            'DailyAutomaticBackupStartTime': 'string',
            'AutomaticBackupRetentionDays': 123,
            'SelfManagedActiveDirectoryConfiguration': {
                'UserName': 'string',
                'Password': 'string',
                'DnsIps': [
                    'string',
                ]
            }
        },
        LustreConfiguration={
            'WeeklyMaintenanceStartTime': 'string'
        }
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe globally unique ID of the file system, assigned by Amazon FSx.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent updates. This string is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.\nThis field is autopopulated if not provided.\n

    :type WindowsConfiguration: dict
    :param WindowsConfiguration: The configuration update for this Microsoft Windows file system. The only supported options are for backup and maintenance and for self-managed Active Directory configuration.\n\nWeeklyMaintenanceStartTime (string) --The preferred time to perform weekly maintenance, in the UTC time zone.\n\nDailyAutomaticBackupStartTime (string) --The preferred time to take daily automatic backups, in the UTC time zone.\n\nAutomaticBackupRetentionDays (integer) --The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 35 days.\n\nSelfManagedActiveDirectoryConfiguration (dict) --The configuration Amazon FSx uses to join the Windows File Server instance to the self-managed Microsoft AD directory.\n\nUserName (string) --The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in OrganizationalUnitDistinguishedName .\n\nPassword (string) --The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.\n\nDnsIps (list) --A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory.\n\n(string) --\n\n\n\n\n\n

    :type LustreConfiguration: dict
    :param LustreConfiguration: The configuration object for Amazon FSx for Lustre file systems used in the UpdateFileSystem operation.\n\nWeeklyMaintenanceStartTime (string) --The preferred time to perform weekly maintenance, in the UTC time zone.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FileSystem': {
        'OwnerId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'FileSystemId': 'string',
        'FileSystemType': 'WINDOWS'|'LUSTRE',
        'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
        'FailureDetails': {
            'Message': 'string'
        },
        'StorageCapacity': 123,
        'StorageType': 'SSD'|'HDD',
        'VpcId': 'string',
        'SubnetIds': [
            'string',
        ],
        'NetworkInterfaceIds': [
            'string',
        ],
        'DNSName': 'string',
        'KmsKeyId': 'string',
        'ResourceARN': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'WindowsConfiguration': {
            'ActiveDirectoryId': 'string',
            'SelfManagedActiveDirectoryConfiguration': {
                'DomainName': 'string',
                'OrganizationalUnitDistinguishedName': 'string',
                'FileSystemAdministratorsGroup': 'string',
                'UserName': 'string',
                'DnsIps': [
                    'string',
                ]
            },
            'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
            'RemoteAdministrationEndpoint': 'string',
            'PreferredSubnetId': 'string',
            'PreferredFileServerIp': 'string',
            'ThroughputCapacity': 123,
            'MaintenanceOperationsInProgress': [
                'PATCHING'|'BACKING_UP',
            ],
            'WeeklyMaintenanceStartTime': 'string',
            'DailyAutomaticBackupStartTime': 'string',
            'AutomaticBackupRetentionDays': 123,
            'CopyTagsToBackups': True|False
        },
        'LustreConfiguration': {
            'WeeklyMaintenanceStartTime': 'string',
            'DataRepositoryConfiguration': {
                'ImportPath': 'string',
                'ExportPath': 'string',
                'ImportedFileChunkSize': 123
            },
            'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
            'PerUnitStorageThroughput': 123,
            'MountName': 'string'
        }
    }
}


Response Structure

(dict) --
The response object for the UpdateFileSystem operation.

FileSystem (dict) --
A description of the file system that was updated.

OwnerId (string) --
The AWS account that created the file system. If the file system was created by an AWS Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is the owner.

CreationTime (datetime) --
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileSystemId (string) --
The system-generated, unique 17-digit ID of the file system.

FileSystemType (string) --
The type of Amazon FSx file system, either LUSTRE or WINDOWS .

Lifecycle (string) --
The lifecycle status of the file system, following are the possible values and what they mean:

AVAILABLE - The file system is in a healthy state, and is reachable and available for use.
CREATING - Amazon FSx is creating the new file system.
DELETING - Amazon FSx is deleting an existing file system.
FAILED - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
MISCONFIGURED indicates that the file system is in a failed but recoverable state.
UPDATING indicates that the file system is undergoing a customer initiated update.


FailureDetails (dict) --
A structure providing details of any failures that occur when creating the file system has failed.

Message (string) --
A message describing any failures that occurred during file system creation.



StorageCapacity (integer) --
The storage capacity of the file system in gigabytes (GB).

StorageType (string) --
The storage type of the file system. Valid values are SSD and HDD . If set to SSD , the file system uses solid state drive storage. If set to HDD , the file system uses hard disk drive storage.

VpcId (string) --
The ID of the primary VPC for the file system.

SubnetIds (list) --
Specifies the IDs of the subnets that the file system is accessible from. For Windows MULTI_AZ_1 file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the PreferredSubnetID property. All other file systems have only one subnet ID.
For Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the endpoint for the file system. For MULTI_AZ_1 Windows file systems, the endpoint for the file system is available in the PreferredSubnetID .

(string) --
The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.



NetworkInterfaceIds (list) --
The IDs of the elastic network interface from which a specific file system is accessible. The elastic network interface is automatically created in the same VPC that the Amazon FSx file system was created in. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide.
For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

(string) --
An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see Elastic Network Interfaces in the Amazon EC2 User Guide for Linux Instances .



DNSName (string) --
The DNS name for the file system.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file system\'s data for Amazon FSx for Windows File Server file systems and persistent Amazon FSx for Lustre file systems at rest. In either case, if not specified, the Amazon FSx managed key is used. The scratch Amazon FSx for Lustre file systems are always encrypted at rest using Amazon FSx managed keys. For more information, see Encrypt in the AWS Key Management Service API Reference .

ResourceARN (string) --
The Amazon Resource Name (ARN) for the file system resource.

Tags (list) --
The tags to associate with the file system. For more information, see Tagging Your Amazon EC2 Resources in the Amazon EC2 User Guide .

(dict) --
Specifies a key-value pair for a resource tag.

Key (string) --
A value that specifies the TagKey , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value (string) --
A value that specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and don\'t have to be unique in a tag set. For example, you can have a key-value pair in a tag set of finances : April and also of payroll : April .





WindowsConfiguration (dict) --
The configuration for this Microsoft Windows file system.

ActiveDirectoryId (string) --
The ID for an existing Microsoft Active Directory instance that the file system should join when it\'s created.

SelfManagedActiveDirectoryConfiguration (dict) --
The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server instance is joined.

DomainName (string) --
The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName (string) --
The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server instance is joined.

FileSystemAdministratorsGroup (string) --
The name of the domain group whose members have administrative privileges for the FSx file system.

UserName (string) --
The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps (list) --
A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string) --




DeploymentType (string) --
Specifies the file system deployment type, valid values are the following:

MULTI_AZ_1 - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
SINGLE_AZ_1 - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
SINGLE_AZ_2 - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.

For more information, see Single-AZ and Multi-AZ File Systems .

RemoteAdministrationEndpoint (string) --
For MULTI_AZ_1 deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this is the DNS name of the file system.
This endpoint is temporarily unavailable when the file system is undergoing maintenance.

PreferredSubnetId (string) --
For MULTI_AZ_1 deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in SubnetIds property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.
For SINGLE_AZ_1 and SINGLE_AZ_2 deployment types, this value is the same as that for SubnetIDs . For more information, see Availability and Durability: Single-AZ and Multi-AZ File Systems

PreferredFileServerIp (string) --
For MULTI_AZ_1 deployment types, the IP address of the primary, or preferred, file server.
Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IP address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system\'s DNSName instead. For more information on mapping and mounting file shares, see Accessing File Shares .

ThroughputCapacity (integer) --
The throughput of an Amazon FSx file system, measured in megabytes per second.

MaintenanceOperationsInProgress (list) --
The list of maintenance operations in progress for this file system.

(string) --
An enumeration specifying the currently ongoing maintenance operation.



WeeklyMaintenanceStartTime (string) --
The preferred time to perform weekly maintenance, in the UTC time zone.

DailyAutomaticBackupStartTime (string) --
The preferred time to take daily automatic backups, in the UTC time zone.

AutomaticBackupRetentionDays (integer) --
The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 35 days.

CopyTagsToBackups (boolean) --
A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If it\'s set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn\'t specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.



LustreConfiguration (dict) --
The configuration for the Amazon FSx for Lustre file system.

WeeklyMaintenanceStartTime (string) --
The UTC time that you want to begin your weekly maintenance window.

DataRepositoryConfiguration (dict) --
The data repository configuration object for Lustre file systems returned in the response of the CreateFileSystem operation.

ImportPath (string) --
The import path to the Amazon S3 bucket (and optional prefix) that you\'re using as the data repository for your FSx for Lustre file system, for example s3://import-bucket/optional-prefix . If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.

ExportPath (string) --
The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.

ImportedFileChunkSize (integer) --
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.



DeploymentType (string) --
The deployment type of the FSX for Lustre file system.

PerUnitStorageThroughput (integer) --
Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). This option is only valid for PERSISTENT_1 deployment types. Valid values are 50, 100, 200.

MountName (string) --
You use the MountName value when mounting the file system.
For the SCRATCH_1 deployment type, this value is always "fsx ". For SCRATCH_2 and PERSISTENT_1 deployment types, this value is a string that is unique within an AWS Region.











Exceptions

FSx.Client.exceptions.BadRequest
FSx.Client.exceptions.UnsupportedOperation
FSx.Client.exceptions.IncompatibleParameterError
FSx.Client.exceptions.InternalServerError
FSx.Client.exceptions.FileSystemNotFound
FSx.Client.exceptions.MissingFileSystemConfiguration


    :return: {
        'FileSystem': {
            'OwnerId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'FileSystemId': 'string',
            'FileSystemType': 'WINDOWS'|'LUSTRE',
            'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
            'FailureDetails': {
                'Message': 'string'
            },
            'StorageCapacity': 123,
            'StorageType': 'SSD'|'HDD',
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ],
            'NetworkInterfaceIds': [
                'string',
            ],
            'DNSName': 'string',
            'KmsKeyId': 'string',
            'ResourceARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'WindowsConfiguration': {
                'ActiveDirectoryId': 'string',
                'SelfManagedActiveDirectoryConfiguration': {
                    'DomainName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string',
                    'FileSystemAdministratorsGroup': 'string',
                    'UserName': 'string',
                    'DnsIps': [
                        'string',
                    ]
                },
                'DeploymentType': 'MULTI_AZ_1'|'SINGLE_AZ_1'|'SINGLE_AZ_2',
                'RemoteAdministrationEndpoint': 'string',
                'PreferredSubnetId': 'string',
                'PreferredFileServerIp': 'string',
                'ThroughputCapacity': 123,
                'MaintenanceOperationsInProgress': [
                    'PATCHING'|'BACKING_UP',
                ],
                'WeeklyMaintenanceStartTime': 'string',
                'DailyAutomaticBackupStartTime': 'string',
                'AutomaticBackupRetentionDays': 123,
                'CopyTagsToBackups': True|False
            },
            'LustreConfiguration': {
                'WeeklyMaintenanceStartTime': 'string',
                'DataRepositoryConfiguration': {
                    'ImportPath': 'string',
                    'ExportPath': 'string',
                    'ImportedFileChunkSize': 123
                },
                'DeploymentType': 'SCRATCH_1'|'SCRATCH_2'|'PERSISTENT_1',
                'PerUnitStorageThroughput': 123,
                'MountName': 'string'
            }
        }
    }
    
    
    :returns: 
    AVAILABLE - The file system is in a healthy state, and is reachable and available for use.
    CREATING - Amazon FSx is creating the new file system.
    DELETING - Amazon FSx is deleting an existing file system.
    FAILED - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
    MISCONFIGURED indicates that the file system is in a failed but recoverable state.
    UPDATING indicates that the file system is undergoing a customer initiated update.
    
    """
    pass

