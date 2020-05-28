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

def create_access_point(ClientToken=None, Tags=None, FileSystemId=None, PosixUser=None, RootDirectory=None):
    """
    Creates an EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. The operating system user and group override any identity information provided by the NFS client. The file system path is exposed as the access point\'s root directory. Applications using the access point can only access data in its own directory and below. To learn more, see Mounting a File System Using EFS Access Points .
    This operation requires permissions for the elasticfilesystem:CreateAccessPoint action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_access_point(
        ClientToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        FileSystemId='string',
        PosixUser={
            'Uid': 123,
            'Gid': 123,
            'SecondaryGids': [
                123,
            ]
        },
        RootDirectory={
            'Path': 'string',
            'CreationInfo': {
                'OwnerUid': 123,
                'OwnerGid': 123,
                'Permissions': 'string'
            }
        }
    )
    
    
    :type ClientToken: string
    :param ClientToken: [REQUIRED]\nA string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: Creates tags associated with the access point. Each tag is a key-value pair.\n\n(dict) --A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /\n\nKey (string) -- [REQUIRED]The tag key (String). The key can\'t start with aws: .\n\nValue (string) -- [REQUIRED]The value of the tag key.\n\n\n\n\n

    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the EFS file system that the access point provides access to.\n

    :type PosixUser: dict
    :param PosixUser: The operating system user and group applied to all file system requests made using the access point.\n\nUid (integer) -- [REQUIRED]The POSIX user ID used for all file system operations using this access point.\n\nGid (integer) -- [REQUIRED]The POSIX group ID used for all file system operations using this access point.\n\nSecondaryGids (list) --Secondary POSIX group IDs used for all file system operations using this access point.\n\n(integer) --\n\n\n\n

    :type RootDirectory: dict
    :param RootDirectory: Specifies the directory on the Amazon EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the RootDirectory > Path specified does not exist, EFS creates it and applies the CreationInfo settings when a client connects to an access point. When specifying a RootDirectory , you need to provide the Path , and the CreationInfo is optional.\n\nPath (string) --Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the CreationInfo .\n\nCreationInfo (dict) --(Optional) Specifies the POSIX IDs and permissions to apply to the access point\'s RootDirectory . If the RootDirectory > Path specified does not exist, EFS creates the root directory using the CreationInfo settings when a client connects to an access point. When specifying the CreationInfo , you must provide values for all properties.\n\nWarning\nIf you do not provide CreationInfo and the specified RootDirectory > Path does not exist, attempts to mount the file system using the access point will fail.\n\n\nOwnerUid (integer) -- [REQUIRED]Specifies the POSIX user ID to apply to the RootDirectory . Accepts values from 0 to 2^32 (4294967295).\n\nOwnerGid (integer) -- [REQUIRED]Specifies the POSIX group ID to apply to the RootDirectory . Accepts values from 0 to 2^32 (4294967295).\n\nPermissions (string) -- [REQUIRED]Specifies the POSIX permissions to apply to the RootDirectory , in the format of an octal number representing the file\'s mode bits.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClientToken': 'string',
    'Name': 'string',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'AccessPointId': 'string',
    'AccessPointArn': 'string',
    'FileSystemId': 'string',
    'PosixUser': {
        'Uid': 123,
        'Gid': 123,
        'SecondaryGids': [
            123,
        ]
    },
    'RootDirectory': {
        'Path': 'string',
        'CreationInfo': {
            'OwnerUid': 123,
            'OwnerGid': 123,
            'Permissions': 'string'
        }
    },
    'OwnerId': 'string',
    'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted'
}


Response Structure

(dict) --
Provides a description of an EFS file system access point.

ClientToken (string) --
The opaque string specified in the request to ensure idempotent creation.

Name (string) --
The name of the access point. This is the value of the Name tag.

Tags (list) --
The tags associated with the access point, presented as an array of Tag objects.

(dict) --
A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /

Key (string) --
The tag key (String). The key can\'t start with aws: .

Value (string) --
The value of the tag key.





AccessPointId (string) --
The ID of the access point, assigned by Amazon EFS.

AccessPointArn (string) --
The unique Amazon Resource Name (ARN) associated with the access point.

FileSystemId (string) --
The ID of the EFS file system that the access point applies to.

PosixUser (dict) --
The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.

Uid (integer) --
The POSIX user ID used for all file system operations using this access point.

Gid (integer) --
The POSIX group ID used for all file system operations using this access point.

SecondaryGids (list) --
Secondary POSIX group IDs used for all file system operations using this access point.

(integer) --




RootDirectory (dict) --
The directory on the Amazon EFS file system that the access point exposes as the root directory to NFS clients using the access point.

Path (string) --
Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the CreationInfo .

CreationInfo (dict) --
(Optional) Specifies the POSIX IDs and permissions to apply to the access point\'s RootDirectory . If the RootDirectory > Path specified does not exist, EFS creates the root directory using the CreationInfo settings when a client connects to an access point. When specifying the CreationInfo , you must provide values for all properties.

Warning
If you do not provide CreationInfo and the specified RootDirectory > Path does not exist, attempts to mount the file system using the access point will fail.


OwnerUid (integer) --
Specifies the POSIX user ID to apply to the RootDirectory . Accepts values from 0 to 2^32 (4294967295).

OwnerGid (integer) --
Specifies the POSIX group ID to apply to the RootDirectory . Accepts values from 0 to 2^32 (4294967295).

Permissions (string) --
Specifies the POSIX permissions to apply to the RootDirectory , in the format of an octal number representing the file\'s mode bits.





OwnerId (string) --
Identified the AWS account that owns the access point resource.

LifeCycleState (string) --
Identifies the lifecycle phase of the access point.







Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.AccessPointAlreadyExists
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound
EFS.Client.exceptions.AccessPointLimitExceeded


    :return: {
        'ClientToken': 'string',
        'Name': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'AccessPointId': 'string',
        'AccessPointArn': 'string',
        'FileSystemId': 'string',
        'PosixUser': {
            'Uid': 123,
            'Gid': 123,
            'SecondaryGids': [
                123,
            ]
        },
        'RootDirectory': {
            'Path': 'string',
            'CreationInfo': {
                'OwnerUid': 123,
                'OwnerGid': 123,
                'Permissions': 'string'
            }
        },
        'OwnerId': 'string',
        'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted'
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def create_file_system(CreationToken=None, PerformanceMode=None, Encrypted=None, KmsKeyId=None, ThroughputMode=None, ProvisionedThroughputInMibps=None, Tags=None):
    """
    Creates a new, empty file system. The operation requires a creation token in the request that Amazon EFS uses to ensure idempotent creation (calling the operation with same creation token has no effect). If a file system does not currently exist that is owned by the caller\'s AWS account with the specified creation token, this operation does the following:
    Otherwise, this operation returns a FileSystemAlreadyExists error with the ID of the existing file system.
    The idempotent operation allows you to retry a CreateFileSystem call without risk of creating an extra file system. This can happen when an initial call fails in a way that leaves it uncertain whether or not a file system was actually created. An example might be that a transport level timeout occurred or your connection was reset. As long as you use the same creation token, if the initial call had succeeded in creating a file system, the client can learn of its existence from the FileSystemAlreadyExists error.
    This operation also takes an optional PerformanceMode parameter that you choose for your file system. We recommend generalPurpose performance mode for most file systems. File systems using the maxIO performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can\'t be changed after the file system has been created. For more information, see Amazon EFS: Performance Modes .
    After the file system is fully created, Amazon EFS sets its lifecycle state to available , at which point you can create one or more mount targets for the file system in your VPC. For more information, see  CreateMountTarget . You mount your Amazon EFS file system on an EC2 instances in your VPC by using the mount target. For more information, see Amazon EFS: How it Works .
    This operation requires permissions for the elasticfilesystem:CreateFileSystem action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation creates a new file system with the default generalpurpose performance mode.
    Expected Output:
    
    :example: response = client.create_file_system(
        CreationToken='string',
        PerformanceMode='generalPurpose'|'maxIO',
        Encrypted=True|False,
        KmsKeyId='string',
        ThroughputMode='bursting'|'provisioned',
        ProvisionedThroughputInMibps=123.0,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CreationToken: string
    :param CreationToken: [REQUIRED]\nA string of up to 64 ASCII characters. Amazon EFS uses this to ensure idempotent creation.\nThis field is autopopulated if not provided.\n

    :type PerformanceMode: string
    :param PerformanceMode: The performance mode of the file system. We recommend generalPurpose performance mode for most file systems. File systems using the maxIO performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can\'t be changed after the file system has been created.

    :type Encrypted: boolean
    :param Encrypted: A Boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying CreateFileSystemRequest$KmsKeyId for an existing AWS Key Management Service (AWS KMS) customer master key (CMK). If you don\'t specify a CMK, then the default CMK for Amazon EFS, /aws/elasticfilesystem , is used to protect the encrypted file system.

    :type KmsKeyId: string
    :param KmsKeyId: The ID of the AWS KMS CMK to be used to protect the encrypted file system. This parameter is only required if you want to use a nondefault CMK. If this parameter is not specified, the default CMK for Amazon EFS is used. This ID can be in one of the following formats:\n\nKey ID - A unique identifier of the key, for example 1234abcd-12ab-34cd-56ef-1234567890ab .\nARN - An Amazon Resource Name (ARN) for the key, for example arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab .\nKey alias - A previously created display name for a key, for example alias/projectKey1 .\nKey alias ARN - An ARN for a key alias, for example arn:aws:kms:us-west-2:444455556666:alias/projectKey1 .\n\nIf KmsKeyId is specified, the CreateFileSystemRequest$Encrypted parameter must be set to true.\n\nWarning\nEFS accepts only symmetric CMKs. You cannot use asymmetric CMKs with EFS file systems.\n\n

    :type ThroughputMode: string
    :param ThroughputMode: The throughput mode for the file system to be created. There are two throughput modes to choose from for your file system: bursting and provisioned . If you set ThroughputMode to provisioned , you must also set a value for ProvisionedThroughPutInMibps . You can decrease your file system\'s throughput in Provisioned Throughput mode or change between the throughput modes as long as it\xe2\x80\x99s been more than 24 hours since the last decrease or throughput mode change. For more, see Specifying Throughput with Provisioned Mode in the Amazon EFS User Guide.

    :type ProvisionedThroughputInMibps: float
    :param ProvisionedThroughputInMibps: The throughput, measured in MiB/s, that you want to provision for a file system that you\'re creating. Valid values are 1-1024. Required if ThroughputMode is set to provisioned . The upper limit for throughput is 1024 MiB/s. You can get this limit increased by contacting AWS Support. For more information, see Amazon EFS Limits That You Can Increase in the Amazon EFS User Guide.

    :type Tags: list
    :param Tags: A value that specifies to create one or more tags associated with the file system. Each tag is a user-defined key-value pair. Name your file system on creation by including a 'Key':'Name','Value':'{value}' key-value pair.\n\n(dict) --A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /\n\nKey (string) -- [REQUIRED]The tag key (String). The key can\'t start with aws: .\n\nValue (string) -- [REQUIRED]The value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OwnerId': 'string',
    'CreationToken': 'string',
    'FileSystemId': 'string',
    'CreationTime': datetime(2015, 1, 1),
    'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
    'Name': 'string',
    'NumberOfMountTargets': 123,
    'SizeInBytes': {
        'Value': 123,
        'Timestamp': datetime(2015, 1, 1),
        'ValueInIA': 123,
        'ValueInStandard': 123
    },
    'PerformanceMode': 'generalPurpose'|'maxIO',
    'Encrypted': True|False,
    'KmsKeyId': 'string',
    'ThroughputMode': 'bursting'|'provisioned',
    'ProvisionedThroughputInMibps': 123.0,
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
A description of the file system.

OwnerId (string) --
The AWS account that created the file system. If the file system was created by an IAM user, the parent account to which the user belongs is the owner.

CreationToken (string) --
The opaque string specified in the request.

FileSystemId (string) --
The ID of the file system, assigned by Amazon EFS.

CreationTime (datetime) --
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

LifeCycleState (string) --
The lifecycle phase of the file system.

Name (string) --
You can add tags to a file system, including a Name tag. For more information, see  CreateFileSystem . If the file system has a Name tag, Amazon EFS returns the value in this field.

NumberOfMountTargets (integer) --
The current number of mount targets that the file system has. For more information, see  CreateMountTarget .

SizeInBytes (dict) --
The latest known metered size (in bytes) of data stored in the file system, in its Value field, and the time at which that size was determined in its Timestamp field. The Timestamp value is the integer number of seconds since 1970-01-01T00:00:00Z. The SizeInBytes value doesn\'t represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, SizeInBytes represents actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size that the file system was at any point in time.

Value (integer) --
The latest known metered size (in bytes) of data stored in the file system.

Timestamp (datetime) --
The time at which the size of data, returned in the Value field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.

ValueInIA (integer) --
The latest known metered size (in bytes) of data stored in the Infrequent Access storage class.

ValueInStandard (integer) --
The latest known metered size (in bytes) of data stored in the Standard storage class.



PerformanceMode (string) --
The performance mode of the file system.

Encrypted (boolean) --
A Boolean value that, if true, indicates that the file system is encrypted.

KmsKeyId (string) --
The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted file system.

ThroughputMode (string) --
The throughput mode for a file system. There are two throughput modes to choose from for your file system: bursting and provisioned . If you set ThroughputMode to provisioned , you must also set a value for ProvisionedThroughPutInMibps . You can decrease your file system\'s throughput in Provisioned Throughput mode or change between the throughput modes as long as it\xe2\x80\x99s been more than 24 hours since the last decrease or throughput mode change.

ProvisionedThroughputInMibps (float) --
The throughput, measured in MiB/s, that you want to provision for a file system. Valid values are 1-1024. Required if ThroughputMode is set to provisioned . The limit on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS Support. For more information, see Amazon EFS Limits That You Can Increase in the Amazon EFS User Guide.

Tags (list) --
The tags associated with the file system, presented as an array of Tag objects.

(dict) --
A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /

Key (string) --
The tag key (String). The key can\'t start with aws: .

Value (string) --
The value of the tag key.











Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemAlreadyExists
EFS.Client.exceptions.FileSystemLimitExceeded
EFS.Client.exceptions.InsufficientThroughputCapacity
EFS.Client.exceptions.ThroughputLimitExceeded

Examples
This operation creates a new file system with the default generalpurpose performance mode.
response = client.create_file_system(
    CreationToken='tokenstring',
    PerformanceMode='generalPurpose',
)

print(response)


Expected Output:
{
    'CreationTime': datetime(2016, 12, 15, 22, 38, 44, 3, 350, 0),
    'CreationToken': 'tokenstring',
    'FileSystemId': 'fs-01234567',
    'LifeCycleState': 'creating',
    'NumberOfMountTargets': 0,
    'OwnerId': '012345678912',
    'PerformanceMode': 'generalPurpose',
    'SizeInBytes': {
        'Value': 0,
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'OwnerId': 'string',
        'CreationToken': 'string',
        'FileSystemId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
        'Name': 'string',
        'NumberOfMountTargets': 123,
        'SizeInBytes': {
            'Value': 123,
            'Timestamp': datetime(2015, 1, 1),
            'ValueInIA': 123,
            'ValueInStandard': 123
        },
        'PerformanceMode': 'generalPurpose'|'maxIO',
        'Encrypted': True|False,
        'KmsKeyId': 'string',
        'ThroughputMode': 'bursting'|'provisioned',
        'ProvisionedThroughputInMibps': 123.0,
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    CreationToken (string) -- [REQUIRED]
    A string of up to 64 ASCII characters. Amazon EFS uses this to ensure idempotent creation.
    This field is autopopulated if not provided.
    
    PerformanceMode (string) -- The performance mode of the file system. We recommend generalPurpose performance mode for most file systems. File systems using the maxIO performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can\'t be changed after the file system has been created.
    Encrypted (boolean) -- A Boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying  CreateFileSystemRequest$KmsKeyId for an existing AWS Key Management Service (AWS KMS) customer master key (CMK). If you don\'t specify a CMK, then the default CMK for Amazon EFS, /aws/elasticfilesystem , is used to protect the encrypted file system.
    KmsKeyId (string) -- The ID of the AWS KMS CMK to be used to protect the encrypted file system. This parameter is only required if you want to use a nondefault CMK. If this parameter is not specified, the default CMK for Amazon EFS is used. This ID can be in one of the following formats:
    
    Key ID - A unique identifier of the key, for example 1234abcd-12ab-34cd-56ef-1234567890ab .
    ARN - An Amazon Resource Name (ARN) for the key, for example arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab .
    Key alias - A previously created display name for a key, for example alias/projectKey1 .
    Key alias ARN - An ARN for a key alias, for example arn:aws:kms:us-west-2:444455556666:alias/projectKey1 .
    
    If KmsKeyId is specified, the  CreateFileSystemRequest$Encrypted parameter must be set to true.
    
    Warning
    EFS accepts only symmetric CMKs. You cannot use asymmetric CMKs with EFS file systems.
    
    
    ThroughputMode (string) -- The throughput mode for the file system to be created. There are two throughput modes to choose from for your file system: bursting and provisioned . If you set ThroughputMode to provisioned , you must also set a value for ProvisionedThroughPutInMibps . You can decrease your file system\'s throughput in Provisioned Throughput mode or change between the throughput modes as long as it\xe2\x80\x99s been more than 24 hours since the last decrease or throughput mode change. For more, see Specifying Throughput with Provisioned Mode in the Amazon EFS User Guide.
    ProvisionedThroughputInMibps (float) -- The throughput, measured in MiB/s, that you want to provision for a file system that you\'re creating. Valid values are 1-1024. Required if ThroughputMode is set to provisioned . The upper limit for throughput is 1024 MiB/s. You can get this limit increased by contacting AWS Support. For more information, see Amazon EFS Limits That You Can Increase in the Amazon EFS User Guide.
    Tags (list) -- A value that specifies to create one or more tags associated with the file system. Each tag is a user-defined key-value pair. Name your file system on creation by including a "Key":"Name","Value":"{value}" key-value pair.
    
    (dict) --A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /
    
    Key (string) -- [REQUIRED]The tag key (String). The key can\'t start with aws: .
    
    Value (string) -- [REQUIRED]The value of the tag key.
    
    
    
    
    
    
    """
    pass

def create_mount_target(FileSystemId=None, SubnetId=None, IpAddress=None, SecurityGroups=None):
    """
    Creates a mount target for a file system. You can then mount the file system on EC2 instances by using the mount target.
    You can create one mount target in each Availability Zone in your VPC. All EC2 instances in a VPC within a given Availability Zone share a single mount target for a given file system. If you have multiple subnets in an Availability Zone, you create a mount target in one of the subnets. EC2 instances do not need to be in the same subnet as the mount target in order to access their file system. For more information, see Amazon EFS: How it Works .
    In the request, you also specify a file system ID for which you are creating the mount target and the file system\'s lifecycle state must be available . For more information, see  DescribeFileSystems .
    In the request, you also provide a subnet ID, which determines the following:
    After creating the mount target, Amazon EFS returns a response that includes, a MountTargetId and an IpAddress . You use this IP address when mounting the file system in an EC2 instance. You can also use the mount target\'s DNS name when mounting the file system. The EC2 instance on which you mount the file system by using the mount target can resolve the mount target\'s DNS name to its IP address. For more information, see How it Works: Implementation Overview .
    Note that you can create mount targets for a file system in only one VPC, and there can be only one mount target per Availability Zone. That is, if the file system already has one or more mount targets created for it, the subnet specified in the request to add another mount target must meet the following requirements:
    If the request satisfies the requirements, Amazon EFS does the following:
    Each Amazon EFS mount target has one corresponding requester-managed EC2 network interface. After the network interface is created, Amazon EFS sets the NetworkInterfaceId field in the mount target\'s description to the network interface ID, and the IpAddress field to its address. If network interface creation fails, the entire CreateMountTarget operation fails.
    We recommend that you create a mount target in each of the Availability Zones. There are cost considerations for using a file system in an Availability Zone through a mount target created in another Availability Zone. For more information, see Amazon EFS . In addition, by always using a mount target local to the instance\'s Availability Zone, you eliminate a partial failure scenario. If the Availability Zone in which your mount target is created goes down, then you can\'t access your file system through that mount target.
    This operation requires permissions for the following action on the file system:
    This operation also requires permissions for the following Amazon EC2 actions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation creates a new mount target for an EFS file system.
    Expected Output:
    
    :example: response = client.create_mount_target(
        FileSystemId='string',
        SubnetId='string',
        IpAddress='string',
        SecurityGroups=[
            'string',
        ]
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system for which to create the mount target.\n

    :type SubnetId: string
    :param SubnetId: [REQUIRED]\nThe ID of the subnet to add the mount target in.\n

    :type IpAddress: string
    :param IpAddress: Valid IPv4 address within the address range of the specified subnet.

    :type SecurityGroups: list
    :param SecurityGroups: Up to five VPC security group IDs, of the form sg-xxxxxxxx . These must be for the same VPC as subnet specified.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OwnerId': 'string',
    'MountTargetId': 'string',
    'FileSystemId': 'string',
    'SubnetId': 'string',
    'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
    'IpAddress': 'string',
    'NetworkInterfaceId': 'string',
    'AvailabilityZoneId': 'string',
    'AvailabilityZoneName': 'string'
}


Response Structure

(dict) --
Provides a description of a mount target.

OwnerId (string) --
AWS account ID that owns the resource.

MountTargetId (string) --
System-assigned mount target ID.

FileSystemId (string) --
The ID of the file system for which the mount target is intended.

SubnetId (string) --
The ID of the mount target\'s subnet.

LifeCycleState (string) --
Lifecycle state of the mount target.

IpAddress (string) --
Address at which the file system can be mounted by using the mount target.

NetworkInterfaceId (string) --
The ID of the network interface that Amazon EFS created when it created the mount target.

AvailabilityZoneId (string) --
The unique and consistent identifier of the Availability Zone (AZ) that the mount target resides in. For example, use1-az1 is an AZ ID for the us-east-1 Region and it has the same location in every AWS account.

AvailabilityZoneName (string) --
The name of the Availability Zone (AZ) that the mount target resides in. AZs are independently mapped to names for each AWS account. For example, the Availability Zone us-east-1a for your AWS account might not be the same location as us-east-1a for another AWS account.







Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound
EFS.Client.exceptions.IncorrectFileSystemLifeCycleState
EFS.Client.exceptions.MountTargetConflict
EFS.Client.exceptions.SubnetNotFound
EFS.Client.exceptions.NoFreeAddressesInSubnet
EFS.Client.exceptions.IpAddressInUse
EFS.Client.exceptions.NetworkInterfaceLimitExceeded
EFS.Client.exceptions.SecurityGroupLimitExceeded
EFS.Client.exceptions.SecurityGroupNotFound
EFS.Client.exceptions.UnsupportedAvailabilityZone

Examples
This operation creates a new mount target for an EFS file system.
response = client.create_mount_target(
    FileSystemId='fs-01234567',
    SubnetId='subnet-1234abcd',
)

print(response)


Expected Output:
{
    'FileSystemId': 'fs-01234567',
    'IpAddress': '192.0.0.2',
    'LifeCycleState': 'creating',
    'MountTargetId': 'fsmt-12340abc',
    'NetworkInterfaceId': 'eni-cedf6789',
    'OwnerId': '012345678912',
    'SubnetId': 'subnet-1234abcd',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'OwnerId': 'string',
        'MountTargetId': 'string',
        'FileSystemId': 'string',
        'SubnetId': 'string',
        'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
        'IpAddress': 'string',
        'NetworkInterfaceId': 'string',
        'AvailabilityZoneId': 'string',
        'AvailabilityZoneName': 'string'
    }
    
    
    :returns: 
    Must belong to the same VPC as the subnets of the existing mount targets
    Must not be in the same Availability Zone as any of the subnets of the existing mount targets
    
    """
    pass

def create_tags(FileSystemId=None, Tags=None):
    """
    Creates or overwrites tags associated with a file system. Each tag is a key-value pair. If a tag key specified in the request already exists on the file system, this operation overwrites its value with the value provided in the request. If you add the Name tag to your file system, Amazon EFS returns it in the response to the  DescribeFileSystems operation.
    This operation requires permission for the elasticfilesystem:CreateTags action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation creates a new tag for an EFS file system.
    Expected Output:
    
    :example: response = client.create_tags(
        FileSystemId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system whose tags you want to modify (String). This operation modifies the tags only, not the file system.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nAn array of Tag objects to add. Each Tag object is a key-value pair.\n\n(dict) --A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /\n\nKey (string) -- [REQUIRED]The tag key (String). The key can\'t start with aws: .\n\nValue (string) -- [REQUIRED]The value of the tag key.\n\n\n\n\n

    :return: response = client.create_tags(
        FileSystemId='fs-01234567',
        Tags=[
            {
                'Key': 'Name',
                'Value': 'MyFileSystem',
            },
        ],
    )
    
    print(response)
    
    
    :returns: 
    EFS.Client.exceptions.BadRequest
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.FileSystemNotFound
    
    """
    pass

def delete_access_point(AccessPointId=None):
    """
    Deletes the specified access point. After deletion is complete, new clients can no longer connect to the access points. Clients connected to the access point at the time of deletion will continue to function until they terminate their connection.
    This operation requires permissions for the elasticfilesystem:DeleteAccessPoint action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_access_point(
        AccessPointId='string'
    )
    
    
    :type AccessPointId: string
    :param AccessPointId: [REQUIRED]\nThe ID of the access point that you want to delete.\n

    """
    pass

def delete_file_system(FileSystemId=None):
    """
    Deletes a file system, permanently severing access to its contents. Upon return, the file system no longer exists and you can\'t access any contents of the deleted file system.
    You can\'t delete a file system that is in use. That is, if the file system has any mount targets, you must first delete them. For more information, see  DescribeMountTargets and  DeleteMountTarget .
    This operation requires permissions for the elasticfilesystem:DeleteFileSystem action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation deletes an EFS file system.
    Expected Output:
    
    :example: response = client.delete_file_system(
        FileSystemId='string'
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system you want to delete.\n

    :return: response = client.delete_file_system(
        FileSystemId='fs-01234567',
    )
    
    print(response)
    
    
    """
    pass

def delete_file_system_policy(FileSystemId=None):
    """
    Deletes the FileSystemPolicy for the specified file system. The default FileSystemPolicy goes into effect once the existing policy is deleted. For more information about the default file system policy, see Using Resource-based Policies with EFS .
    This operation requires permissions for the elasticfilesystem:DeleteFileSystemPolicy action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_file_system_policy(
        FileSystemId='string'
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nSpecifies the EFS file system for which to delete the FileSystemPolicy .\n

    """
    pass

def delete_mount_target(MountTargetId=None):
    """
    Deletes the specified mount target.
    This operation forcibly breaks any mounts of the file system by using the mount target that is being deleted, which might disrupt instances or applications using those mounts. To avoid applications getting cut off abruptly, you might consider unmounting any mounts of the mount target, if feasible. The operation also deletes the associated network interface. Uncommitted writes might be lost, but breaking a mount target using this operation does not corrupt the file system itself. The file system you created remains. You can mount an EC2 instance in your VPC by using another mount target.
    This operation requires permissions for the following action on the file system:
    The operation also requires permissions for the following Amazon EC2 action on the mount target\'s network interface:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation deletes a mount target.
    Expected Output:
    
    :example: response = client.delete_mount_target(
        MountTargetId='string'
    )
    
    
    :type MountTargetId: string
    :param MountTargetId: [REQUIRED]\nThe ID of the mount target to delete (String).\n

    :return: response = client.delete_mount_target(
        MountTargetId='fsmt-12340abc',
    )
    
    print(response)
    
    
    :returns: 
    ec2:DeleteNetworkInterface
    
    """
    pass

def delete_tags(FileSystemId=None, TagKeys=None):
    """
    Deletes the specified tags from a file system. If the DeleteTags request includes a tag key that doesn\'t exist, Amazon EFS ignores it and doesn\'t cause an error. For more information about tags and related restrictions, see Tag Restrictions in the AWS Billing and Cost Management User Guide .
    This operation requires permissions for the elasticfilesystem:DeleteTags action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation deletes tags for an EFS file system.
    Expected Output:
    
    :example: response = client.delete_tags(
        FileSystemId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system whose tags you want to delete (String).\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of tag keys to delete.\n\n(string) --\n\n

    :return: response = client.delete_tags(
        FileSystemId='fs-01234567',
        TagKeys=[
            'Name',
        ],
    )
    
    print(response)
    
    
    :returns: 
    EFS.Client.exceptions.BadRequest
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.FileSystemNotFound
    
    """
    pass

def describe_access_points(MaxResults=None, NextToken=None, AccessPointId=None, FileSystemId=None):
    """
    Returns the description of a specific Amazon EFS access point if the AccessPointId is provided. If you provide an EFS FileSystemId , it returns descriptions of all access points for that file system. You can provide either an AccessPointId or a FileSystemId in the request, but not both.
    This operation requires permissions for the elasticfilesystem:DescribeAccessPoints action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_access_points(
        MaxResults=123,
        NextToken='string',
        AccessPointId='string',
        FileSystemId='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: (Optional) When retrieving all access points for a file system, you can optionally specify the MaxItems parameter to limit the number of objects returned in a response. The default value is 100.

    :type NextToken: string
    :param NextToken: NextToken is present if the response is paginated. You can use NextMarker in the subsequent request to fetch the next page of access point descriptions.

    :type AccessPointId: string
    :param AccessPointId: (Optional) Specifies an EFS access point to describe in the response; mutually exclusive with FileSystemId .

    :type FileSystemId: string
    :param FileSystemId: (Optional) If you provide a FileSystemId , EFS returns all access points for that file system; mutually exclusive with AccessPointId .

    :rtype: dict

ReturnsResponse Syntax
{
    'AccessPoints': [
        {
            'ClientToken': 'string',
            'Name': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'AccessPointId': 'string',
            'AccessPointArn': 'string',
            'FileSystemId': 'string',
            'PosixUser': {
                'Uid': 123,
                'Gid': 123,
                'SecondaryGids': [
                    123,
                ]
            },
            'RootDirectory': {
                'Path': 'string',
                'CreationInfo': {
                    'OwnerUid': 123,
                    'OwnerGid': 123,
                    'Permissions': 'string'
                }
            },
            'OwnerId': 'string',
            'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AccessPoints (list) --
An array of access point descriptions.

(dict) --
Provides a description of an EFS file system access point.

ClientToken (string) --
The opaque string specified in the request to ensure idempotent creation.

Name (string) --
The name of the access point. This is the value of the Name tag.

Tags (list) --
The tags associated with the access point, presented as an array of Tag objects.

(dict) --
A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /

Key (string) --
The tag key (String). The key can\'t start with aws: .

Value (string) --
The value of the tag key.





AccessPointId (string) --
The ID of the access point, assigned by Amazon EFS.

AccessPointArn (string) --
The unique Amazon Resource Name (ARN) associated with the access point.

FileSystemId (string) --
The ID of the EFS file system that the access point applies to.

PosixUser (dict) --
The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.

Uid (integer) --
The POSIX user ID used for all file system operations using this access point.

Gid (integer) --
The POSIX group ID used for all file system operations using this access point.

SecondaryGids (list) --
Secondary POSIX group IDs used for all file system operations using this access point.

(integer) --




RootDirectory (dict) --
The directory on the Amazon EFS file system that the access point exposes as the root directory to NFS clients using the access point.

Path (string) --
Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the CreationInfo .

CreationInfo (dict) --
(Optional) Specifies the POSIX IDs and permissions to apply to the access point\'s RootDirectory . If the RootDirectory > Path specified does not exist, EFS creates the root directory using the CreationInfo settings when a client connects to an access point. When specifying the CreationInfo , you must provide values for all properties.

Warning
If you do not provide CreationInfo and the specified RootDirectory > Path does not exist, attempts to mount the file system using the access point will fail.


OwnerUid (integer) --
Specifies the POSIX user ID to apply to the RootDirectory . Accepts values from 0 to 2^32 (4294967295).

OwnerGid (integer) --
Specifies the POSIX group ID to apply to the RootDirectory . Accepts values from 0 to 2^32 (4294967295).

Permissions (string) --
Specifies the POSIX permissions to apply to the RootDirectory , in the format of an octal number representing the file\'s mode bits.





OwnerId (string) --
Identified the AWS account that owns the access point resource.

LifeCycleState (string) --
Identifies the lifecycle phase of the access point.





NextToken (string) --
Present if there are more access points than returned in the response. You can use the NextMarker in the subsequent request to fetch the additional descriptions.







Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound
EFS.Client.exceptions.AccessPointNotFound


    :return: {
        'AccessPoints': [
            {
                'ClientToken': 'string',
                'Name': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'AccessPointId': 'string',
                'AccessPointArn': 'string',
                'FileSystemId': 'string',
                'PosixUser': {
                    'Uid': 123,
                    'Gid': 123,
                    'SecondaryGids': [
                        123,
                    ]
                },
                'RootDirectory': {
                    'Path': 'string',
                    'CreationInfo': {
                        'OwnerUid': 123,
                        'OwnerGid': 123,
                        'Permissions': 'string'
                    }
                },
                'OwnerId': 'string',
                'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def describe_file_system_policy(FileSystemId=None):
    """
    Returns the FileSystemPolicy for the specified EFS file system.
    This operation requires permissions for the elasticfilesystem:DescribeFileSystemPolicy action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_file_system_policy(
        FileSystemId='string'
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nSpecifies which EFS file system to retrieve the FileSystemPolicy for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'FileSystemId': 'string',
    'Policy': 'string'
}


Response Structure

(dict) --
FileSystemId (string) --Specifies the EFS file system to which the FileSystemPolicy applies.

Policy (string) --The JSON formatted FileSystemPolicy for the EFS file system.






Exceptions

EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound
EFS.Client.exceptions.PolicyNotFound


    :return: {
        'FileSystemId': 'string',
        'Policy': 'string'
    }
    
    
    """
    pass

def describe_file_systems(MaxItems=None, Marker=None, CreationToken=None, FileSystemId=None):
    """
    Returns the description of a specific Amazon EFS file system if either the file system CreationToken or the FileSystemId is provided. Otherwise, it returns descriptions of all file systems owned by the caller\'s AWS account in the AWS Region of the endpoint that you\'re calling.
    When retrieving all file system descriptions, you can optionally specify the MaxItems parameter to limit the number of descriptions in a response. Currently, this number is automatically set to 10. If more file system descriptions remain, Amazon EFS returns a NextMarker , an opaque token, in the response. In this case, you should send a subsequent request with the Marker request parameter set to the value of NextMarker .
    To retrieve a list of your file system descriptions, this operation is used in an iterative process, where DescribeFileSystems is called first without the Marker and then the operation continues to call it with the Marker parameter set to the value of the NextMarker from the previous response until the response has no NextMarker .
    The order of file systems returned in the response of one DescribeFileSystems call and the order of file systems returned across the responses of a multi-call iteration is unspecified.
    This operation requires permissions for the elasticfilesystem:DescribeFileSystems action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation describes all of the EFS file systems in an account.
    Expected Output:
    
    :example: response = client.describe_file_systems(
        MaxItems=123,
        Marker='string',
        CreationToken='string',
        FileSystemId='string'
    )
    
    
    :type MaxItems: integer
    :param MaxItems: (Optional) Specifies the maximum number of file systems to return in the response (integer). This number is automatically set to 100. The response is paginated at 100 per page if you have more than 100 file systems.

    :type Marker: string
    :param Marker: (Optional) Opaque pagination token returned from a previous DescribeFileSystems operation (String). If present, specifies to continue the list from where the returning call had left off.

    :type CreationToken: string
    :param CreationToken: (Optional) Restricts the list to the file system with this creation token (String). You specify a creation token when you create an Amazon EFS file system.

    :type FileSystemId: string
    :param FileSystemId: (Optional) ID of the file system whose description you want to retrieve (String).

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'FileSystems': [
        {
            'OwnerId': 'string',
            'CreationToken': 'string',
            'FileSystemId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
            'Name': 'string',
            'NumberOfMountTargets': 123,
            'SizeInBytes': {
                'Value': 123,
                'Timestamp': datetime(2015, 1, 1),
                'ValueInIA': 123,
                'ValueInStandard': 123
            },
            'PerformanceMode': 'generalPurpose'|'maxIO',
            'Encrypted': True|False,
            'KmsKeyId': 'string',
            'ThroughputMode': 'bursting'|'provisioned',
            'ProvisionedThroughputInMibps': 123.0,
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

Marker (string) --
Present if provided by caller in the request (String).

FileSystems (list) --
An array of file system descriptions.

(dict) --
A description of the file system.

OwnerId (string) --
The AWS account that created the file system. If the file system was created by an IAM user, the parent account to which the user belongs is the owner.

CreationToken (string) --
The opaque string specified in the request.

FileSystemId (string) --
The ID of the file system, assigned by Amazon EFS.

CreationTime (datetime) --
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

LifeCycleState (string) --
The lifecycle phase of the file system.

Name (string) --
You can add tags to a file system, including a Name tag. For more information, see  CreateFileSystem . If the file system has a Name tag, Amazon EFS returns the value in this field.

NumberOfMountTargets (integer) --
The current number of mount targets that the file system has. For more information, see  CreateMountTarget .

SizeInBytes (dict) --
The latest known metered size (in bytes) of data stored in the file system, in its Value field, and the time at which that size was determined in its Timestamp field. The Timestamp value is the integer number of seconds since 1970-01-01T00:00:00Z. The SizeInBytes value doesn\'t represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, SizeInBytes represents actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size that the file system was at any point in time.

Value (integer) --
The latest known metered size (in bytes) of data stored in the file system.

Timestamp (datetime) --
The time at which the size of data, returned in the Value field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.

ValueInIA (integer) --
The latest known metered size (in bytes) of data stored in the Infrequent Access storage class.

ValueInStandard (integer) --
The latest known metered size (in bytes) of data stored in the Standard storage class.



PerformanceMode (string) --
The performance mode of the file system.

Encrypted (boolean) --
A Boolean value that, if true, indicates that the file system is encrypted.

KmsKeyId (string) --
The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted file system.

ThroughputMode (string) --
The throughput mode for a file system. There are two throughput modes to choose from for your file system: bursting and provisioned . If you set ThroughputMode to provisioned , you must also set a value for ProvisionedThroughPutInMibps . You can decrease your file system\'s throughput in Provisioned Throughput mode or change between the throughput modes as long as it\xe2\x80\x99s been more than 24 hours since the last decrease or throughput mode change.

ProvisionedThroughputInMibps (float) --
The throughput, measured in MiB/s, that you want to provision for a file system. Valid values are 1-1024. Required if ThroughputMode is set to provisioned . The limit on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS Support. For more information, see Amazon EFS Limits That You Can Increase in the Amazon EFS User Guide.

Tags (list) --
The tags associated with the file system, presented as an array of Tag objects.

(dict) --
A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /

Key (string) --
The tag key (String). The key can\'t start with aws: .

Value (string) --
The value of the tag key.









NextMarker (string) --
Present if there are more file systems than returned in the response (String). You can use the NextMarker in the subsequent request to fetch the descriptions.







Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound

Examples
This operation describes all of the EFS file systems in an account.
response = client.describe_file_systems(
)

print(response)


Expected Output:
{
    'FileSystems': [
        {
            'CreationTime': datetime(2016, 12, 15, 22, 38, 44, 3, 350, 0),
            'CreationToken': 'tokenstring',
            'FileSystemId': 'fs-01234567',
            'LifeCycleState': 'available',
            'Name': 'MyFileSystem',
            'NumberOfMountTargets': 1,
            'OwnerId': '012345678912',
            'PerformanceMode': 'generalPurpose',
            'SizeInBytes': {
                'Value': 6144,
            },
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'FileSystems': [
            {
                'OwnerId': 'string',
                'CreationToken': 'string',
                'FileSystemId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
                'Name': 'string',
                'NumberOfMountTargets': 123,
                'SizeInBytes': {
                    'Value': 123,
                    'Timestamp': datetime(2015, 1, 1),
                    'ValueInIA': 123,
                    'ValueInStandard': 123
                },
                'PerformanceMode': 'generalPurpose'|'maxIO',
                'Encrypted': True|False,
                'KmsKeyId': 'string',
                'ThroughputMode': 'bursting'|'provisioned',
                'ProvisionedThroughputInMibps': 123.0,
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    EFS.Client.exceptions.BadRequest
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.FileSystemNotFound
    
    """
    pass

def describe_lifecycle_configuration(FileSystemId=None):
    """
    Returns the current LifecycleConfiguration object for the specified Amazon EFS file system. EFS lifecycle management uses the LifecycleConfiguration object to identify which files to move to the EFS Infrequent Access (IA) storage class. For a file system without a LifecycleConfiguration object, the call returns an empty array in the response.
    This operation requires permissions for the elasticfilesystem:DescribeLifecycleConfiguration operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_lifecycle_configuration(
        FileSystemId='string'
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system whose LifecycleConfiguration object you want to retrieve (String).\n

    :rtype: dict
ReturnsResponse Syntax{
    'LifecyclePolicies': [
        {
            'TransitionToIA': 'AFTER_7_DAYS'|'AFTER_14_DAYS'|'AFTER_30_DAYS'|'AFTER_60_DAYS'|'AFTER_90_DAYS'
        },
    ]
}


Response Structure

(dict) --
LifecyclePolicies (list) --An array of lifecycle management policies. Currently, EFS supports a maximum of one policy per file system.

(dict) --Describes a policy used by EFS lifecycle management to transition files to the Infrequent Access (IA) storage class.

TransitionToIA (string) --A value that describes the period of time that a file is not accessed, after which it transitions to the IA storage class. Metadata operations such as listing the contents of a directory don\'t count as file access events.










Exceptions

EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.FileSystemNotFound


    :return: {
        'LifecyclePolicies': [
            {
                'TransitionToIA': 'AFTER_7_DAYS'|'AFTER_14_DAYS'|'AFTER_30_DAYS'|'AFTER_60_DAYS'|'AFTER_90_DAYS'
            },
        ]
    }
    
    
    """
    pass

def describe_mount_target_security_groups(MountTargetId=None):
    """
    Returns the security groups currently in effect for a mount target. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not deleted .
    This operation requires permissions for the following actions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation describes all of the security groups for a file system\'s mount target.
    Expected Output:
    
    :example: response = client.describe_mount_target_security_groups(
        MountTargetId='string'
    )
    
    
    :type MountTargetId: string
    :param MountTargetId: [REQUIRED]\nThe ID of the mount target whose security groups you want to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SecurityGroups': [
        'string',
    ]
}


Response Structure

(dict) --
SecurityGroups (list) --An array of security groups.

(string) --







Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.MountTargetNotFound
EFS.Client.exceptions.IncorrectMountTargetState

Examples
This operation describes all of the security groups for a file system\'s mount target.
response = client.describe_mount_target_security_groups(
    MountTargetId='fsmt-12340abc',
)

print(response)


Expected Output:
{
    'SecurityGroups': [
        'sg-fghi4567',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SecurityGroups': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_mount_targets(MaxItems=None, Marker=None, FileSystemId=None, MountTargetId=None, AccessPointId=None):
    """
    Returns the descriptions of all the current mount targets, or a specific mount target, for a file system. When requesting all of the current mount targets, the order of mount targets returned in the response is unspecified.
    This operation requires permissions for the elasticfilesystem:DescribeMountTargets action, on either the file system ID that you specify in FileSystemId , or on the file system of the mount target that you specify in MountTargetId .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation describes all of a file system\'s mount targets.
    Expected Output:
    
    :example: response = client.describe_mount_targets(
        MaxItems=123,
        Marker='string',
        FileSystemId='string',
        MountTargetId='string',
        AccessPointId='string'
    )
    
    
    :type MaxItems: integer
    :param MaxItems: (Optional) Maximum number of mount targets to return in the response. Currently, this number is automatically set to 10, and other values are ignored. The response is paginated at 100 per page if you have more than 100 mount targets.

    :type Marker: string
    :param Marker: (Optional) Opaque pagination token returned from a previous DescribeMountTargets operation (String). If present, it specifies to continue the list from where the previous returning call left off.

    :type FileSystemId: string
    :param FileSystemId: (Optional) ID of the file system whose mount targets you want to list (String). It must be included in your request if an AccessPointId or MountTargetId is not included. Accepts either a file system ID or ARN as input.

    :type MountTargetId: string
    :param MountTargetId: (Optional) ID of the mount target that you want to have described (String). It must be included in your request if FileSystemId is not included. Accepts either a mount target ID or ARN as input.

    :type AccessPointId: string
    :param AccessPointId: (Optional) The ID of the access point whose mount targets that you want to list. It must be included in your request if a FileSystemId or MountTargetId is not included in your request. Accepts either an access point ID or ARN as input.

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'MountTargets': [
        {
            'OwnerId': 'string',
            'MountTargetId': 'string',
            'FileSystemId': 'string',
            'SubnetId': 'string',
            'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
            'IpAddress': 'string',
            'NetworkInterfaceId': 'string',
            'AvailabilityZoneId': 'string',
            'AvailabilityZoneName': 'string'
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

Marker (string) --
If the request included the Marker , the response returns that value in this field.

MountTargets (list) --
Returns the file system\'s mount targets as an array of MountTargetDescription objects.

(dict) --
Provides a description of a mount target.

OwnerId (string) --
AWS account ID that owns the resource.

MountTargetId (string) --
System-assigned mount target ID.

FileSystemId (string) --
The ID of the file system for which the mount target is intended.

SubnetId (string) --
The ID of the mount target\'s subnet.

LifeCycleState (string) --
Lifecycle state of the mount target.

IpAddress (string) --
Address at which the file system can be mounted by using the mount target.

NetworkInterfaceId (string) --
The ID of the network interface that Amazon EFS created when it created the mount target.

AvailabilityZoneId (string) --
The unique and consistent identifier of the Availability Zone (AZ) that the mount target resides in. For example, use1-az1 is an AZ ID for the us-east-1 Region and it has the same location in every AWS account.

AvailabilityZoneName (string) --
The name of the Availability Zone (AZ) that the mount target resides in. AZs are independently mapped to names for each AWS account. For example, the Availability Zone us-east-1a for your AWS account might not be the same location as us-east-1a for another AWS account.





NextMarker (string) --
If a value is present, there are more mount targets to return. In a subsequent request, you can provide Marker in your request with this value to retrieve the next set of mount targets.







Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound
EFS.Client.exceptions.MountTargetNotFound
EFS.Client.exceptions.AccessPointNotFound

Examples
This operation describes all of a file system\'s mount targets.
response = client.describe_mount_targets(
    FileSystemId='fs-01234567',
)

print(response)


Expected Output:
{
    'MountTargets': [
        {
            'FileSystemId': 'fs-01234567',
            'IpAddress': '192.0.0.2',
            'LifeCycleState': 'available',
            'MountTargetId': 'fsmt-12340abc',
            'NetworkInterfaceId': 'eni-cedf6789',
            'OwnerId': '012345678912',
            'SubnetId': 'subnet-1234abcd',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'MountTargets': [
            {
                'OwnerId': 'string',
                'MountTargetId': 'string',
                'FileSystemId': 'string',
                'SubnetId': 'string',
                'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
                'IpAddress': 'string',
                'NetworkInterfaceId': 'string',
                'AvailabilityZoneId': 'string',
                'AvailabilityZoneName': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    EFS.Client.exceptions.BadRequest
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.FileSystemNotFound
    EFS.Client.exceptions.MountTargetNotFound
    EFS.Client.exceptions.AccessPointNotFound
    
    """
    pass

def describe_tags(MaxItems=None, Marker=None, FileSystemId=None):
    """
    Returns the tags associated with a file system. The order of tags returned in the response of one DescribeTags call and the order of tags returned across the responses of a multiple-call iteration (when using pagination) is unspecified.
    This operation requires permissions for the elasticfilesystem:DescribeTags action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation describes all of a file system\'s tags.
    Expected Output:
    
    :example: response = client.describe_tags(
        MaxItems=123,
        Marker='string',
        FileSystemId='string'
    )
    
    
    :type MaxItems: integer
    :param MaxItems: (Optional) The maximum number of file system tags to return in the response. Currently, this number is automatically set to 100, and other values are ignored. The response is paginated at 100 per page if you have more than 100 tags.

    :type Marker: string
    :param Marker: (Optional) An opaque pagination token returned from a previous DescribeTags operation (String). If present, it specifies to continue the list from where the previous call left off.

    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system whose tag set you want to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextMarker': 'string'
}


Response Structure

(dict) --

Marker (string) --
If the request included a Marker , the response returns that value in this field.

Tags (list) --
Returns tags associated with the file system as an array of Tag objects.

(dict) --
A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /

Key (string) --
The tag key (String). The key can\'t start with aws: .

Value (string) --
The value of the tag key.





NextMarker (string) --
If a value is present, there are more tags to return. In a subsequent request, you can provide the value of NextMarker as the value of the Marker parameter in your next request to retrieve the next set of tags.







Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound

Examples
This operation describes all of a file system\'s tags.
response = client.describe_tags(
    FileSystemId='fs-01234567',
)

print(response)


Expected Output:
{
    'Tags': [
        {
            'Key': 'Name',
            'Value': 'MyFileSystem',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Marker': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    EFS.Client.exceptions.BadRequest
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.FileSystemNotFound
    
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

def list_tags_for_resource(ResourceId=None, MaxResults=None, NextToken=None):
    """
    Lists all tags for a top-level EFS resource. You must provide the ID of the resource that you want to retrieve the tags for.
    This operation requires permissions for the elasticfilesystem:DescribeAccessPoints action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nSpecifies the EFS resource you want to retrieve tags for. You can retrieve tags for EFS file systems and access points using this API endpoint.\n

    :type MaxResults: integer
    :param MaxResults: (Optional) Specifies the maximum number of tag objects to return in the response. The default value is 100.

    :type NextToken: string
    :param NextToken: You can use NextToken in a subsequent request to fetch the next page of access point descriptions if the response payload was paginated.

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

Tags (list) --
An array of the tags for the specified EFS resource.

(dict) --
A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /

Key (string) --
The tag key (String). The key can\'t start with aws: .

Value (string) --
The value of the tag key.





NextToken (string) --

NextToken is present if the response payload is paginated. You can use NextToken in a subsequent request to fetch the next page of access point descriptions.








Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound
EFS.Client.exceptions.AccessPointNotFound


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
    EFS.Client.exceptions.BadRequest
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.FileSystemNotFound
    EFS.Client.exceptions.AccessPointNotFound
    
    """
    pass

def modify_mount_target_security_groups(MountTargetId=None, SecurityGroups=None):
    """
    Modifies the set of security groups in effect for a mount target.
    When you create a mount target, Amazon EFS also creates a new network interface. For more information, see  CreateMountTarget . This operation replaces the security groups in effect for the network interface associated with a mount target, with the SecurityGroups provided in the request. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not deleted .
    The operation requires permissions for the following actions:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation modifies the security groups associated with a mount target for a file system.
    Expected Output:
    
    :example: response = client.modify_mount_target_security_groups(
        MountTargetId='string',
        SecurityGroups=[
            'string',
        ]
    )
    
    
    :type MountTargetId: string
    :param MountTargetId: [REQUIRED]\nThe ID of the mount target whose security groups you want to modify.\n

    :type SecurityGroups: list
    :param SecurityGroups: An array of up to five VPC security group IDs.\n\n(string) --\n\n

    :return: response = client.modify_mount_target_security_groups(
        MountTargetId='fsmt-12340abc',
        SecurityGroups=[
            'sg-abcd1234',
        ],
    )
    
    print(response)
    
    
    :returns: 
    MountTargetId (string) -- [REQUIRED]
    The ID of the mount target whose security groups you want to modify.
    
    SecurityGroups (list) -- An array of up to five VPC security group IDs.
    
    (string) --
    
    
    
    """
    pass

def put_file_system_policy(FileSystemId=None, Policy=None, BypassPolicyLockoutSafetyCheck=None):
    """
    Applies an Amazon EFS FileSystemPolicy to an Amazon EFS file system. A file system policy is an IAM resource-based policy and can contain multiple policy statements. A file system always has exactly one file system policy, which can be the default policy or an explicit policy set or updated using this API operation. When an explicit policy is set, it overrides the default policy. For more information about the default file system policy, see Default EFS File System Policy .
    This operation requires permissions for the elasticfilesystem:PutFileSystemPolicy action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_file_system_policy(
        FileSystemId='string',
        Policy='string',
        BypassPolicyLockoutSafetyCheck=True|False
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the EFS file system that you want to create or update the FileSystemPolicy for.\n

    :type Policy: string
    :param Policy: [REQUIRED]\nThe FileSystemPolicy that you\'re creating. Accepts a JSON formatted policy definition. To find out more about the elements that make up a file system policy, see EFS Resource-based Policies .\n

    :type BypassPolicyLockoutSafetyCheck: boolean
    :param BypassPolicyLockoutSafetyCheck: (Optional) A flag to indicate whether to bypass the FileSystemPolicy lockout safety check. The policy lockout safety check determines whether the policy in the request will prevent the principal making the request will be locked out from making future PutFileSystemPolicy requests on the file system. Set BypassPolicyLockoutSafetyCheck to True only when you intend to prevent the principal that is making the request from making a subsequent PutFileSystemPolicy request on the file system. The default value is False.

    :rtype: dict

ReturnsResponse Syntax
{
    'FileSystemId': 'string',
    'Policy': 'string'
}


Response Structure

(dict) --

FileSystemId (string) --
Specifies the EFS file system to which the FileSystemPolicy applies.

Policy (string) --
The JSON formatted FileSystemPolicy for the EFS file system.







Exceptions

EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound
EFS.Client.exceptions.InvalidPolicyException
EFS.Client.exceptions.IncorrectFileSystemLifeCycleState


    :return: {
        'FileSystemId': 'string',
        'Policy': 'string'
    }
    
    
    :returns: 
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.FileSystemNotFound
    EFS.Client.exceptions.InvalidPolicyException
    EFS.Client.exceptions.IncorrectFileSystemLifeCycleState
    
    """
    pass

def put_lifecycle_configuration(FileSystemId=None, LifecyclePolicies=None):
    """
    Enables lifecycle management by creating a new LifecycleConfiguration object. A LifecycleConfiguration object defines when files in an Amazon EFS file system are automatically transitioned to the lower-cost EFS Infrequent Access (IA) storage class. A LifecycleConfiguration applies to all files in a file system.
    Each Amazon EFS file system supports one lifecycle configuration, which applies to all files in the file system. If a LifecycleConfiguration object already exists for the specified file system, a PutLifecycleConfiguration call modifies the existing configuration. A PutLifecycleConfiguration call with an empty LifecyclePolicies array in the request body deletes any existing LifecycleConfiguration and disables lifecycle management.
    In the request, specify the following:
    This operation requires permissions for the elasticfilesystem:PutLifecycleConfiguration operation.
    To apply a LifecycleConfiguration object to an encrypted file system, you need the same AWS Key Management Service (AWS KMS) permissions as when you created the encrypted file system.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_lifecycle_configuration(
        FileSystemId='string',
        LifecyclePolicies=[
            {
                'TransitionToIA': 'AFTER_7_DAYS'|'AFTER_14_DAYS'|'AFTER_30_DAYS'|'AFTER_60_DAYS'|'AFTER_90_DAYS'
            },
        ]
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system for which you are creating the LifecycleConfiguration object (String).\n

    :type LifecyclePolicies: list
    :param LifecyclePolicies: [REQUIRED]\nAn array of LifecyclePolicy objects that define the file system\'s LifecycleConfiguration object. A LifecycleConfiguration object tells lifecycle management when to transition files from the Standard storage class to the Infrequent Access storage class.\n\n(dict) --Describes a policy used by EFS lifecycle management to transition files to the Infrequent Access (IA) storage class.\n\nTransitionToIA (string) --A value that describes the period of time that a file is not accessed, after which it transitions to the IA storage class. Metadata operations such as listing the contents of a directory don\'t count as file access events.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LifecyclePolicies': [
        {
            'TransitionToIA': 'AFTER_7_DAYS'|'AFTER_14_DAYS'|'AFTER_30_DAYS'|'AFTER_60_DAYS'|'AFTER_90_DAYS'
        },
    ]
}


Response Structure

(dict) --

LifecyclePolicies (list) --
An array of lifecycle management policies. Currently, EFS supports a maximum of one policy per file system.

(dict) --
Describes a policy used by EFS lifecycle management to transition files to the Infrequent Access (IA) storage class.

TransitionToIA (string) --
A value that describes the period of time that a file is not accessed, after which it transitions to the IA storage class. Metadata operations such as listing the contents of a directory don\'t count as file access events.











Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.FileSystemNotFound
EFS.Client.exceptions.IncorrectFileSystemLifeCycleState


    :return: {
        'LifecyclePolicies': [
            {
                'TransitionToIA': 'AFTER_7_DAYS'|'AFTER_14_DAYS'|'AFTER_30_DAYS'|'AFTER_60_DAYS'|'AFTER_90_DAYS'
            },
        ]
    }
    
    
    :returns: 
    FileSystemId (string) -- [REQUIRED]
    The ID of the file system for which you are creating the LifecycleConfiguration object (String).
    
    LifecyclePolicies (list) -- [REQUIRED]
    An array of LifecyclePolicy objects that define the file system\'s LifecycleConfiguration object. A LifecycleConfiguration object tells lifecycle management when to transition files from the Standard storage class to the Infrequent Access storage class.
    
    (dict) --Describes a policy used by EFS lifecycle management to transition files to the Infrequent Access (IA) storage class.
    
    TransitionToIA (string) --A value that describes the period of time that a file is not accessed, after which it transitions to the IA storage class. Metadata operations such as listing the contents of a directory don\'t count as file access events.
    
    
    
    
    
    
    """
    pass

def tag_resource(ResourceId=None, Tags=None):
    """
    Creates a tag for an EFS resource. You can create tags for EFS file systems and access points using this API operation.
    This operation requires permissions for the elasticfilesystem:TagResource action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID specifying the EFS resource that you want to create a tag for.\n

    :type Tags: list
    :param Tags: [REQUIRED]\n\n(dict) --A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /\n\nKey (string) -- [REQUIRED]The tag key (String). The key can\'t start with aws: .\n\nValue (string) -- [REQUIRED]The value of the tag key.\n\n\n\n\n

    :returns: 
    EFS.Client.exceptions.BadRequest
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.FileSystemNotFound
    EFS.Client.exceptions.AccessPointNotFound
    
    """
    pass

def untag_resource(ResourceId=None, TagKeys=None):
    """
    Removes tags from an EFS resource. You can remove tags from EFS file systems and access points using this API operation.
    This operation requires permissions for the elasticfilesystem:UntagResource action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nSpecifies the EFS resource that you want to remove tags from.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe keys of the key:value tag pairs that you want to remove from the specified EFS resource.\n\n(string) --\n\n

    :returns: 
    EFS.Client.exceptions.BadRequest
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.FileSystemNotFound
    EFS.Client.exceptions.AccessPointNotFound
    
    """
    pass

def update_file_system(FileSystemId=None, ThroughputMode=None, ProvisionedThroughputInMibps=None):
    """
    Updates the throughput mode or the amount of provisioned throughput of an existing file system.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_file_system(
        FileSystemId='string',
        ThroughputMode='bursting'|'provisioned',
        ProvisionedThroughputInMibps=123.0
    )
    
    
    :type FileSystemId: string
    :param FileSystemId: [REQUIRED]\nThe ID of the file system that you want to update.\n

    :type ThroughputMode: string
    :param ThroughputMode: (Optional) The throughput mode that you want your file system to use. If you\'re not updating your throughput mode, you don\'t need to provide this value in your request. If you are changing the ThroughputMode to provisioned , you must also set a value for ProvisionedThroughputInMibps .

    :type ProvisionedThroughputInMibps: float
    :param ProvisionedThroughputInMibps: (Optional) The amount of throughput, in MiB/s, that you want to provision for your file system. Valid values are 1-1024. Required if ThroughputMode is changed to provisioned on update. If you\'re not updating the amount of provisioned throughput for your file system, you don\'t need to provide this value in your request.

    :rtype: dict

ReturnsResponse Syntax
{
    'OwnerId': 'string',
    'CreationToken': 'string',
    'FileSystemId': 'string',
    'CreationTime': datetime(2015, 1, 1),
    'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
    'Name': 'string',
    'NumberOfMountTargets': 123,
    'SizeInBytes': {
        'Value': 123,
        'Timestamp': datetime(2015, 1, 1),
        'ValueInIA': 123,
        'ValueInStandard': 123
    },
    'PerformanceMode': 'generalPurpose'|'maxIO',
    'Encrypted': True|False,
    'KmsKeyId': 'string',
    'ThroughputMode': 'bursting'|'provisioned',
    'ProvisionedThroughputInMibps': 123.0,
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
A description of the file system.

OwnerId (string) --
The AWS account that created the file system. If the file system was created by an IAM user, the parent account to which the user belongs is the owner.

CreationToken (string) --
The opaque string specified in the request.

FileSystemId (string) --
The ID of the file system, assigned by Amazon EFS.

CreationTime (datetime) --
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

LifeCycleState (string) --
The lifecycle phase of the file system.

Name (string) --
You can add tags to a file system, including a Name tag. For more information, see  CreateFileSystem . If the file system has a Name tag, Amazon EFS returns the value in this field.

NumberOfMountTargets (integer) --
The current number of mount targets that the file system has. For more information, see  CreateMountTarget .

SizeInBytes (dict) --
The latest known metered size (in bytes) of data stored in the file system, in its Value field, and the time at which that size was determined in its Timestamp field. The Timestamp value is the integer number of seconds since 1970-01-01T00:00:00Z. The SizeInBytes value doesn\'t represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, SizeInBytes represents actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size that the file system was at any point in time.

Value (integer) --
The latest known metered size (in bytes) of data stored in the file system.

Timestamp (datetime) --
The time at which the size of data, returned in the Value field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.

ValueInIA (integer) --
The latest known metered size (in bytes) of data stored in the Infrequent Access storage class.

ValueInStandard (integer) --
The latest known metered size (in bytes) of data stored in the Standard storage class.



PerformanceMode (string) --
The performance mode of the file system.

Encrypted (boolean) --
A Boolean value that, if true, indicates that the file system is encrypted.

KmsKeyId (string) --
The ID of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted file system.

ThroughputMode (string) --
The throughput mode for a file system. There are two throughput modes to choose from for your file system: bursting and provisioned . If you set ThroughputMode to provisioned , you must also set a value for ProvisionedThroughPutInMibps . You can decrease your file system\'s throughput in Provisioned Throughput mode or change between the throughput modes as long as it\xe2\x80\x99s been more than 24 hours since the last decrease or throughput mode change.

ProvisionedThroughputInMibps (float) --
The throughput, measured in MiB/s, that you want to provision for a file system. Valid values are 1-1024. Required if ThroughputMode is set to provisioned . The limit on throughput is 1024 MiB/s. You can get these limits increased by contacting AWS Support. For more information, see Amazon EFS Limits That You Can Increase in the Amazon EFS User Guide.

Tags (list) --
The tags associated with the file system, presented as an array of Tag objects.

(dict) --
A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /

Key (string) --
The tag key (String). The key can\'t start with aws: .

Value (string) --
The value of the tag key.











Exceptions

EFS.Client.exceptions.BadRequest
EFS.Client.exceptions.FileSystemNotFound
EFS.Client.exceptions.IncorrectFileSystemLifeCycleState
EFS.Client.exceptions.InsufficientThroughputCapacity
EFS.Client.exceptions.InternalServerError
EFS.Client.exceptions.ThroughputLimitExceeded
EFS.Client.exceptions.TooManyRequests


    :return: {
        'OwnerId': 'string',
        'CreationToken': 'string',
        'FileSystemId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'LifeCycleState': 'creating'|'available'|'updating'|'deleting'|'deleted',
        'Name': 'string',
        'NumberOfMountTargets': 123,
        'SizeInBytes': {
            'Value': 123,
            'Timestamp': datetime(2015, 1, 1),
            'ValueInIA': 123,
            'ValueInStandard': 123
        },
        'PerformanceMode': 'generalPurpose'|'maxIO',
        'Encrypted': True|False,
        'KmsKeyId': 'string',
        'ThroughputMode': 'bursting'|'provisioned',
        'ProvisionedThroughputInMibps': 123.0,
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    EFS.Client.exceptions.BadRequest
    EFS.Client.exceptions.FileSystemNotFound
    EFS.Client.exceptions.IncorrectFileSystemLifeCycleState
    EFS.Client.exceptions.InsufficientThroughputCapacity
    EFS.Client.exceptions.InternalServerError
    EFS.Client.exceptions.ThroughputLimitExceeded
    EFS.Client.exceptions.TooManyRequests
    
    """
    pass

