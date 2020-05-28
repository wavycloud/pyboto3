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

def cancel_task_execution(TaskExecutionArn=None):
    """
    Cancels execution of a task.
    When you cancel a task execution, the transfer of some files are abruptly interrupted. The contents of files that are transferred to the destination might be incomplete or inconsistent with the source files. However, if you start a new task execution on the same task and you allow the task execution to complete, file content on the destination is complete and consistent. This applies to other unexpected failures that interrupt a task execution. In all of these cases, AWS DataSync successfully complete the transfer when you start the next task execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_task_execution(
        TaskExecutionArn='string'
    )
    
    
    :type TaskExecutionArn: string
    :param TaskExecutionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the task execution to cancel.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {}
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def create_agent(ActivationKey=None, AgentName=None, Tags=None, VpcEndpointId=None, SubnetArns=None, SecurityGroupArns=None):
    """
    Activates an AWS DataSync agent that you have deployed on your host. The activation process associates your agent with your account. In the activation process, you specify information such as the AWS Region that you want to activate the agent in. You activate the agent in the AWS Region where your target locations (in Amazon S3 or Amazon EFS) reside. Your tasks are created in this AWS Region.
    You can activate the agent in a VPC (Virtual private Cloud) or provide the agent access to a VPC endpoint so you can run tasks without going over the public Internet.
    You can use an agent for more than one location. If a task uses multiple agents, all of them need to have status AVAILABLE for the task to run. If you use multiple agents for a source location, the status of all the agents must be AVAILABLE for the task to run.
    Agents are automatically updated by AWS on a regular basis, using a mechanism that ensures minimal interruption to your tasks.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_agent(
        ActivationKey='string',
        AgentName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        VpcEndpointId='string',
        SubnetArns=[
            'string',
        ],
        SecurityGroupArns=[
            'string',
        ]
    )
    
    
    :type ActivationKey: string
    :param ActivationKey: [REQUIRED]\nYour agent activation key. You can get the activation key either by sending an HTTP GET request with redirects that enable you to get the agent IP address (port 80). Alternatively, you can get it from the AWS DataSync console.\nThe redirect URL returned in the response provides you the activation key for your agent in the query string parameter activationKey . It might also include other activation-related parameters; however, these are merely defaults. The arguments you pass to this API call determine the actual configuration of your agent.\nFor more information, see Activating an Agent in the AWS DataSync User Guide.\n

    :type AgentName: string
    :param AgentName: The name you configured for your agent. This value is a text reference that is used to identify the agent in the console.

    :type Tags: list
    :param Tags: The key-value pair that represents the tag that you want to associate with the agent. The value can be an empty string. This value helps you manage, filter, and search for your agents.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @.\n\n\n(dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.\n\nKey (string) -- [REQUIRED]The key for an AWS resource tag.\n\nValue (string) --The value for an AWS resource tag.\n\n\n\n\n

    :type VpcEndpointId: string
    :param VpcEndpointId: The ID of the VPC (Virtual Private Cloud) endpoint that the agent has access to. This is the client-side VPC endpoint, also called a PrivateLink. If you don\'t have a PrivateLink VPC endpoint, see Creating a VPC Endpoint Service Configuration in the AWS VPC User Guide.\nVPC endpoint ID looks like this: vpce-01234d5aff67890e1 .\n

    :type SubnetArns: list
    :param SubnetArns: The Amazon Resource Names (ARNs) of the subnets in which DataSync will create elastic network interfaces for each data transfer task. The agent that runs a task must be private. When you start a task that is associated with an agent created in a VPC, or one that has access to an IP address in a VPC, then the task is also private. In this case, DataSync creates four network interfaces for each task in your subnet. For a data transfer to work, the agent must be able to route to all these four network interfaces.\n\n(string) --\n\n

    :type SecurityGroupArns: list
    :param SecurityGroupArns: The ARNs of the security groups used to protect your data transfer task subnets. See CreateAgentRequest$SubnetArns .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AgentArn': 'string'
}


Response Structure

(dict) --
CreateAgentResponse

AgentArn (string) --
The Amazon Resource Name (ARN) of the agent. Use the ListAgents operation to return a list of agents for your account and AWS Region.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'AgentArn': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def create_location_efs(Subdirectory=None, EfsFilesystemArn=None, Ec2Config=None, Tags=None):
    """
    Creates an endpoint for an Amazon EFS file system.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_location_efs(
        Subdirectory='string',
        EfsFilesystemArn='string',
        Ec2Config={
            'SubnetArn': 'string',
            'SecurityGroupArns': [
                'string',
            ]
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Subdirectory: string
    :param Subdirectory: A subdirectory in the location\xe2\x80\x99s path. This subdirectory in the EFS file system is used to read data from the EFS source location or write data to the EFS destination. By default, AWS DataSync uses the root directory.\n\nNote\nSubdirectory must be specified with forward slashes. For example /path/to/folder .\n\n

    :type EfsFilesystemArn: string
    :param EfsFilesystemArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the Amazon EFS file system.\n

    :type Ec2Config: dict
    :param Ec2Config: [REQUIRED]\nThe subnet and security group that the Amazon EFS file system uses. The security group that you provide needs to be able to communicate with the security group on the mount target in the subnet specified.\nThe exact relationship between security group M (of the mount target) and security group S (which you provide for DataSync to use at this stage) is as follows:\n\nSecurity group M (which you associate with the mount target) must allow inbound access for the Transmission Control Protocol (TCP) on the NFS port (2049) from security group S. You can enable inbound connections either by IP address (CIDR range) or security group.\nSecurity group S (provided to DataSync to access EFS) should have a rule that enables outbound connections to the NFS port on one of the file system\xe2\x80\x99s mount targets. You can enable outbound connections either by IP address (CIDR range) or security group. For information about security groups and mount targets, see Security Groups for Amazon EC2 Instances and Mount Targets in the Amazon EFS User Guide.\n\n\nSubnetArn (string) -- [REQUIRED]The ARN of the subnet and the security group that DataSync uses to access the target EFS file system.\n\nSecurityGroupArns (list) -- [REQUIRED]The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon EC2 resource.\n\n(string) --\n\n\n\n

    :type Tags: list
    :param Tags: The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.\n\n(dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.\n\nKey (string) -- [REQUIRED]The key for an AWS resource tag.\n\nValue (string) --The value for an AWS resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LocationArn': 'string'
}


Response Structure

(dict) --
CreateLocationEfs

LocationArn (string) --
The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def create_location_fsx_windows(Subdirectory=None, FsxFilesystemArn=None, SecurityGroupArns=None, Tags=None, User=None, Domain=None, Password=None):
    """
    Creates an endpoint for an Amazon FSx for Windows file system.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_location_fsx_windows(
        Subdirectory='string',
        FsxFilesystemArn='string',
        SecurityGroupArns=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        User='string',
        Domain='string',
        Password='string'
    )
    
    
    :type Subdirectory: string
    :param Subdirectory: A subdirectory in the location\xe2\x80\x99s path. This subdirectory in the Amazon FSx for Windows file system is used to read data from the Amazon FSx for Windows source location or write data to the FSx for Windows destination.

    :type FsxFilesystemArn: string
    :param FsxFilesystemArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the FSx for Windows file system.\n

    :type SecurityGroupArns: list
    :param SecurityGroupArns: [REQUIRED]\nThe Amazon Resource Names (ARNs) of the security groups that are to use to configure the FSx for Windows file system.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.\n\n(dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.\n\nKey (string) -- [REQUIRED]The key for an AWS resource tag.\n\nValue (string) --The value for an AWS resource tag.\n\n\n\n\n

    :type User: string
    :param User: [REQUIRED]\nThe user who has the permissions to access files and folders in the FSx for Windows file system.\n

    :type Domain: string
    :param Domain: The name of the Windows domain that the FSx for Windows server belongs to.

    :type Password: string
    :param Password: [REQUIRED]\nThe password of the user who has the permissions to access files and folders in the FSx for Windows file system.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LocationArn': 'string'
}


Response Structure

(dict) --

LocationArn (string) --
The Amazon Resource Name (ARN) of the FSx for Windows file system location that is created.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def create_location_nfs(Subdirectory=None, ServerHostname=None, OnPremConfig=None, MountOptions=None, Tags=None):
    """
    Defines a file system on a Network File System (NFS) server that can be read from or written to
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_location_nfs(
        Subdirectory='string',
        ServerHostname='string',
        OnPremConfig={
            'AgentArns': [
                'string',
            ]
        },
        MountOptions={
            'Version': 'AUTOMATIC'|'NFS3'|'NFS4_0'|'NFS4_1'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Subdirectory: string
    :param Subdirectory: [REQUIRED]\nThe subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination. The NFS path should be a path that\'s exported by the NFS server, or a subdirectory of that path. The path should be such that it can be mounted by other NFS clients in your network.\nTo see all the paths exported by your NFS server. run 'showmount -e nfs-server-name ' from an NFS client that has access to your server. You can specify any directory that appears in the results, and any subdirectory of that directory. Ensure that the NFS export is accessible without Kerberos authentication.\nTo transfer all the data in the folder you specified, DataSync needs to have permissions to read all the data. To ensure this, either configure the NFS export with no_root_squash, or ensure that the permissions for all of the files that you want DataSync allow read access for all users. Doing either enables the agent to read the files. For the agent to access directories, you must additionally enable all execute access.\nFor information about NFS export configuration, see 18.7. The /etc/exports Configuration File in the Red Hat Enterprise Linux documentation.\n

    :type ServerHostname: string
    :param ServerHostname: [REQUIRED]\nThe name of the NFS server. This value is the IP address or Domain Name Service (DNS) name of the NFS server. An agent that is installed on-premises uses this host name to mount the NFS server in a network.\n\nNote\nThis name must either be DNS-compliant or must be an IP version 4 (IPv4) address.\n\n

    :type OnPremConfig: dict
    :param OnPremConfig: [REQUIRED]\nContains a list of Amazon Resource Names (ARNs) of agents that are used to connect to an NFS server.\n\nAgentArns (list) -- [REQUIRED]ARNs)of the agents to use for an NFS location.\n\n(string) --\n\n\n\n

    :type MountOptions: dict
    :param MountOptions: The NFS mount options that DataSync can use to mount your NFS share.\n\nVersion (string) --The specific NFS version that you want DataSync to use to mount your NFS share. If the server refuses to use the version specified, the sync will fail. If you don\'t specify a version, DataSync defaults to AUTOMATIC . That is, DataSync automatically selects a version based on negotiation with the NFS server.\nYou can specify the following NFS versions:\n\n**NFSv3 ** - stateless protocol version that allows for asynchronous writes on the server.\n**NFSv4.0 ** - stateful, firewall-friendly protocol version that supports delegations and pseudo filesystems.\n**NFSv4.1 ** - stateful protocol version that supports sessions, directory delegations, and parallel data processing. Version 4.1 also includes all features available in version 4.0.\n\n\n\n

    :type Tags: list
    :param Tags: The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.\n\n(dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.\n\nKey (string) -- [REQUIRED]The key for an AWS resource tag.\n\nValue (string) --The value for an AWS resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LocationArn': 'string'
}


Response Structure

(dict) --
CreateLocationNfsResponse

LocationArn (string) --
The Amazon Resource Name (ARN) of the source NFS file system location that is created.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def create_location_s3(Subdirectory=None, S3BucketArn=None, S3StorageClass=None, S3Config=None, Tags=None):
    """
    Creates an endpoint for an Amazon S3 bucket.
    For AWS DataSync to access a destination S3 bucket, it needs an AWS Identity and Access Management (IAM) role that has the required permissions. You can set up the required permissions by creating an IAM policy that grants the required permissions and attaching the policy to the role. An example of such a policy is shown in the examples section.
    For more information, see https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html#create-s3-location in the AWS DataSync User Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_location_s3(
        Subdirectory='string',
        S3BucketArn='string',
        S3StorageClass='STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
        S3Config={
            'BucketAccessRoleArn': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Subdirectory: string
    :param Subdirectory: A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.

    :type S3BucketArn: string
    :param S3BucketArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Amazon S3 bucket.\n

    :type S3StorageClass: string
    :param S3StorageClass: The Amazon S3 storage class that you want to store your files in when this location is used as a task destination. For more information about S3 storage classes, see Amazon S3 Storage Classes in the Amazon Simple Storage Service Developer Guide . Some storage classes have behaviors that can affect your S3 storage cost. For detailed information, see using-storage-classes .

    :type S3Config: dict
    :param S3Config: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket.\nFor detailed information about using such a role, see Creating a Location for Amazon S3 in the AWS DataSync User Guide .\n\nBucketAccessRoleArn (string) -- [REQUIRED]The Amazon S3 bucket to access. This bucket is used as a parameter in the CreateLocationS3 operation.\n\n\n

    :type Tags: list
    :param Tags: The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.\n\n(dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.\n\nKey (string) -- [REQUIRED]The key for an AWS resource tag.\n\nValue (string) --The value for an AWS resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LocationArn': 'string'
}


Response Structure

(dict) --
CreateLocationS3Response

LocationArn (string) --
The Amazon Resource Name (ARN) of the source Amazon S3 bucket location that is created.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def create_location_smb(Subdirectory=None, ServerHostname=None, User=None, Domain=None, Password=None, AgentArns=None, MountOptions=None, Tags=None):
    """
    Defines a file system on an Server Message Block (SMB) server that can be read from or written to.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_location_smb(
        Subdirectory='string',
        ServerHostname='string',
        User='string',
        Domain='string',
        Password='string',
        AgentArns=[
            'string',
        ],
        MountOptions={
            'Version': 'AUTOMATIC'|'SMB2'|'SMB3'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Subdirectory: string
    :param Subdirectory: [REQUIRED]\nThe subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination. The SMB path should be a path that\'s exported by the SMB server, or a subdirectory of that path. The path should be such that it can be mounted by other SMB clients in your network.\n\nNote\nSubdirectory must be specified with forward slashes. For example /path/to/folder .\n\nTo transfer all the data in the folder you specified, DataSync needs to have permissions to mount the SMB share, as well as to access all the data in that share. To ensure this, either ensure that the user/password specified belongs to the user who can mount the share, and who has the appropriate permissions for all of the files and directories that you want DataSync to access, or use credentials of a member of the Backup Operators group to mount the share. Doing either enables the agent to access the data. For the agent to access directories, you must additionally enable all execute access.\n

    :type ServerHostname: string
    :param ServerHostname: [REQUIRED]\nThe name of the SMB server. This value is the IP address or Domain Name Service (DNS) name of the SMB server. An agent that is installed on-premises uses this hostname to mount the SMB server in a network.\n\nNote\nThis name must either be DNS-compliant or must be an IP version 4 (IPv4) address.\n\n

    :type User: string
    :param User: [REQUIRED]\nThe user who can mount the share, has the permissions to access files and folders in the SMB share.\n

    :type Domain: string
    :param Domain: The name of the Windows domain that the SMB server belongs to.

    :type Password: string
    :param Password: [REQUIRED]\nThe password of the user who can mount the share, has the permissions to access files and folders in the SMB share.\n

    :type AgentArns: list
    :param AgentArns: [REQUIRED]\nThe Amazon Resource Names (ARNs) of agents to use for a Simple Message Block (SMB) location.\n\n(string) --\n\n

    :type MountOptions: dict
    :param MountOptions: The mount options used by DataSync to access the SMB server.\n\nVersion (string) --The specific SMB version that you want DataSync to use to mount your SMB share. If you don\'t specify a version, DataSync defaults to AUTOMATIC . That is, DataSync automatically selects a version based on negotiation with the SMB server.\n\n\n

    :type Tags: list
    :param Tags: The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.\n\n(dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.\n\nKey (string) -- [REQUIRED]The key for an AWS resource tag.\n\nValue (string) --The value for an AWS resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LocationArn': 'string'
}


Response Structure

(dict) --
CreateLocationSmbResponse

LocationArn (string) --
The Amazon Resource Name (ARN) of the source SMB file system location that is created.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def create_task(SourceLocationArn=None, DestinationLocationArn=None, CloudWatchLogGroupArn=None, Name=None, Options=None, Excludes=None, Schedule=None, Tags=None):
    """
    Creates a task. A task is a set of two locations (source and destination) and a set of Options that you use to control the behavior of a task. If you don\'t specify Options when you create a task, AWS DataSync populates them with service defaults.
    When you create a task, it first enters the CREATING state. During CREATING AWS DataSync attempts to mount the on-premises Network File System (NFS) location. The task transitions to the AVAILABLE state without waiting for the AWS location to become mounted. If required, AWS DataSync mounts the AWS location before each task execution.
    If an agent that is associated with a source (NFS) location goes offline, the task transitions to the UNAVAILABLE status. If the status of the task remains in the CREATING status for more than a few minutes, it means that your agent might be having trouble mounting the source NFS file system. Check the task\'s ErrorCode and ErrorDetail. Mount issues are often caused by either a misconfigured firewall or a mistyped NFS server host name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_task(
        SourceLocationArn='string',
        DestinationLocationArn='string',
        CloudWatchLogGroupArn='string',
        Name='string',
        Options={
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'ONLY_FILES_TRANSFERRED'|'NONE',
            'OverwriteMode': 'ALWAYS'|'NEVER',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'PRESERVE',
            'BytesPerSecond': 123,
            'TaskQueueing': 'ENABLED'|'DISABLED',
            'LogLevel': 'OFF'|'BASIC'|'TRANSFER'
        },
        Excludes=[
            {
                'FilterType': 'SIMPLE_PATTERN',
                'Value': 'string'
            },
        ],
        Schedule={
            'ScheduleExpression': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type SourceLocationArn: string
    :param SourceLocationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the source location for the task.\n

    :type DestinationLocationArn: string
    :param DestinationLocationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of an AWS storage resource\'s location.\n

    :type CloudWatchLogGroupArn: string
    :param CloudWatchLogGroupArn: The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that is used to monitor and log events in the task.\nFor more information on these groups, see Working with Log Groups and Log Streams in the Amazon CloudWatch User Guide.\nFor more information about how to use CloudWatch Logs with DataSync, see Monitoring Your Task in the AWS DataSync User Guide.\n

    :type Name: string
    :param Name: The name of a task. This value is a text reference that is used to identify the task in the console.

    :type Options: dict
    :param Options: The set of configuration options that control the behavior of a single execution of the task that occurs when you call StartTaskExecution . You can configure these options to preserve metadata such as user ID (UID) and group ID (GID), file permissions, data integrity verification, and so on.\nFor each individual task execution, you can override these options by specifying the OverrideOptions before starting a the task execution. For more information, see the operation.\n\nVerifyMode (string) --A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.\nDefault value: POINT_IN_TIME_CONSISTENT.\nPOINT_IN_TIME_CONSISTENT: Perform verification (recommended).\nONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.\nNONE: Skip verification.\n\nOverwriteMode (string) --A value that determines whether files at the destination should be overwritten or preserved when copying files. If set to NEVER a destination file will not be replaced by a source file, even if the destination file differs from the source file. If you modify files in the destination and you sync the files, you can use this value to protect against overwriting those changes.\nSome storage classes have specific behaviors that can affect your S3 storage cost. For detailed information, see using-storage-classes in the AWS DataSync User Guide .\n\nAtime (string) --A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set Atime to BEST_EFFORT, DataSync attempts to preserve the original Atime attribute on all source files (that is, the version before the PREPARING phase). However, Atime \'s behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.\nDefault value: BEST_EFFORT.\nBEST_EFFORT: Attempt to preserve the per-file Atime value (recommended).\nNONE: Ignore Atime .\n\nNote\nIf Atime is set to BEST_EFFORT, Mtime must be set to PRESERVE.\nIf Atime is set to NONE, Mtime must also be NONE.\n\n\nMtime (string) --A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.\nDefault value: PRESERVE.\nPRESERVE: Preserve original Mtime (recommended)\nNONE: Ignore Mtime .\n\nNote\nIf Mtime is set to PRESERVE, Atime must be set to BEST_EFFORT.\nIf Mtime is set to NONE, Atime must also be set to NONE.\n\n\nUid (string) --The user ID (UID) of the file\'s owner.\nDefault value: INT_VALUE. This preserves the integer value of the ID.\nINT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).\nNONE: Ignore UID and GID.\n\nGid (string) --The group ID (GID) of the file\'s owners.\nDefault value: INT_VALUE. This preserves the integer value of the ID.\nINT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).\nNONE: Ignore UID and GID.\n\nPreserveDeletedFiles (string) --A value that specifies whether files in the destination that don\'t exist in the source file system should be preserved. This option can affect your storage cost. If your task deletes objects, you might incur minimum storage duration charges for certain storage classes. For detailed information, see using-storage-classes in the AWS DataSync User Guide .\nDefault value: PRESERVE.\nPRESERVE: Ignore such destination files (recommended).\nREMOVE: Delete destination files that aren\xe2\x80\x99t present in the source.\n\nPreserveDevices (string) --A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.\n\nNote\nAWS DataSync can\'t sync the actual contents of such devices, because they are nonterminal and don\'t return an end-of-file (EOF) marker.\n\nDefault value: NONE.\nNONE: Ignore special devices (recommended).\nPRESERVE: Preserve character and block device metadata. This option isn\'t currently supported for Amazon EFS.\n\nPosixPermissions (string) --A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.\nDefault value: PRESERVE.\nPRESERVE: Preserve POSIX-style permissions (recommended).\nNONE: Ignore permissions.\n\nNote\nAWS DataSync can preserve extant permissions of a source location.\n\n\nBytesPerSecond (integer) --A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to 1048576 (=1024*1024 ).\n\nTaskQueueing (string) --A value that determines whether tasks should be queued before executing the tasks. If set to ENABLED , the tasks will be queued. The default is ENABLED .\nIf you use the same agent to run multiple tasks you can enable the tasks to run in series. For more information see queue-task-execution .\n\nLogLevel (string) --A value that determines the type of logs DataSync will deliver to your AWS CloudWatch Logs file. If set to OFF , no logs will be delivered. BASIC will deliver a few logs per transfer operation and TRANSFER will deliver a verbose log that contains logs for every file that is transferred.\n\n\n

    :type Excludes: list
    :param Excludes: A list of filter rules that determines which files to exclude from a task. The list should contain a single filter string that consists of the patterns to exclude. The patterns are delimited by '|' (that is, a pipe), for example, '/folder1|/folder2'\n\n(dict) --Specifies which files, folders and objects to include or exclude when transferring files from source to destination.\n\nFilterType (string) --The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.\n\nValue (string) --A single filter string that consists of the patterns to include or exclude. The patterns are delimited by '|' (that is, a pipe), for example: /folder1|/folder2\n\n\n\n\n

    :type Schedule: dict
    :param Schedule: Specifies a schedule used to periodically transfer files from a source to a destination location. The schedule should be specified in UTC time. For more information, see task-scheduling .\n\nScheduleExpression (string) -- [REQUIRED]A cron expression that specifies when AWS DataSync initiates a scheduled transfer from a source to a destination location.\n\n\n

    :type Tags: list
    :param Tags: The key-value pair that represents the tag that you want to add to the resource. The value can be an empty string.\n\n(dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.\n\nKey (string) -- [REQUIRED]The key for an AWS resource tag.\n\nValue (string) --The value for an AWS resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TaskArn': 'string'
}


Response Structure

(dict) --
CreateTaskResponse

TaskArn (string) --
The Amazon Resource Name (ARN) of the task.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'TaskArn': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def delete_agent(AgentArn=None):
    """
    Deletes an agent. To specify which agent to delete, use the Amazon Resource Name (ARN) of the agent in your request. The operation disassociates the agent from your AWS account. However, it doesn\'t delete the agent virtual machine (VM) from your on-premises environment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_agent(
        AgentArn='string'
    )
    
    
    :type AgentArn: string
    :param AgentArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the agent to delete. Use the ListAgents operation to return a list of agents for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {}
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def delete_location(LocationArn=None):
    """
    Deletes the configuration of a location used by AWS DataSync.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_location(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the location to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {}
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def delete_task(TaskArn=None):
    """
    Deletes a task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_task(
        TaskArn='string'
    )
    
    
    :type TaskArn: string
    :param TaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the task to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {}
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def describe_agent(AgentArn=None):
    """
    Returns metadata such as the name, the network interfaces, and the status (that is, whether the agent is running or not) for an agent. To specify which agent to describe, use the Amazon Resource Name (ARN) of the agent in your request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_agent(
        AgentArn='string'
    )
    
    
    :type AgentArn: string
    :param AgentArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the agent to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AgentArn': 'string',
    'Name': 'string',
    'Status': 'ONLINE'|'OFFLINE',
    'LastConnectionTime': datetime(2015, 1, 1),
    'CreationTime': datetime(2015, 1, 1),
    'EndpointType': 'PUBLIC'|'PRIVATE_LINK'|'FIPS',
    'PrivateLinkConfig': {
        'VpcEndpointId': 'string',
        'PrivateLinkEndpoint': 'string',
        'SubnetArns': [
            'string',
        ],
        'SecurityGroupArns': [
            'string',
        ]
    }
}


Response Structure

(dict) --DescribeAgentResponse

AgentArn (string) --The Amazon Resource Name (ARN) of the agent.

Name (string) --The name of the agent.

Status (string) --The status of the agent. If the status is ONLINE, then the agent is configured properly and is available to use. The Running status is the normal running status for an agent. If the status is OFFLINE, the agent\'s VM is turned off or the agent is in an unhealthy state. When the issue that caused the unhealthy state is resolved, the agent returns to ONLINE status.

LastConnectionTime (datetime) --The time that the agent last connected to DataSyc.

CreationTime (datetime) --The time that the agent was activated (that is, created in your account).

EndpointType (string) --The type of endpoint that your agent is connected to. If the endpoint is a VPC endpoint, the agent is not accessible over the public Internet.

PrivateLinkConfig (dict) --The subnet and the security group that DataSync used to access a VPC endpoint.

VpcEndpointId (string) --The ID of the VPC endpoint that is configured for an agent. An agent that is configured with a VPC endpoint will not be accessible over the public Internet.

PrivateLinkEndpoint (string) --The private endpoint that is configured for an agent that has access to IP addresses in a PrivateLink . An agent that is configured with this endpoint will not be accessible over the public Internet.

SubnetArns (list) --The Amazon Resource Names (ARNs) of the subnets that are configured for an agent activated in a VPC or an agent that has access to a VPC endpoint.

(string) --


SecurityGroupArns (list) --The Amazon Resource Names (ARNs) of the security groups that are configured for the EC2 resource that hosts an agent activated in a VPC or an agent that has access to a VPC endpoint.

(string) --









Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'AgentArn': 'string',
        'Name': 'string',
        'Status': 'ONLINE'|'OFFLINE',
        'LastConnectionTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1),
        'EndpointType': 'PUBLIC'|'PRIVATE_LINK'|'FIPS',
        'PrivateLinkConfig': {
            'VpcEndpointId': 'string',
            'PrivateLinkEndpoint': 'string',
            'SubnetArns': [
                'string',
            ],
            'SecurityGroupArns': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_location_efs(LocationArn=None):
    """
    Returns metadata, such as the path information about an Amazon EFS location.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_location_efs(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the EFS location to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LocationArn': 'string',
    'LocationUri': 'string',
    'Ec2Config': {
        'SubnetArn': 'string',
        'SecurityGroupArns': [
            'string',
        ]
    },
    'CreationTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --DescribeLocationEfsResponse

LocationArn (string) --The Amazon resource Name (ARN) of the EFS location that was described.

LocationUri (string) --The URL of the EFS location that was described.

Ec2Config (dict) --The subnet and the security group that DataSync uses to access target EFS file system. The subnet must have at least one mount target for that file system. The security group that you provide needs to be able to communicate with the security group on the mount target in the subnet specified.

SubnetArn (string) --The ARN of the subnet and the security group that DataSync uses to access the target EFS file system.

SecurityGroupArns (list) --The Amazon Resource Names (ARNs) of the security groups that are configured for the Amazon EC2 resource.

(string) --




CreationTime (datetime) --The time that the EFS location was created.






Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string',
        'LocationUri': 'string',
        'Ec2Config': {
            'SubnetArn': 'string',
            'SecurityGroupArns': [
                'string',
            ]
        },
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def describe_location_fsx_windows(LocationArn=None):
    """
    Returns metadata, such as the path information about an Amazon FSx for Windows location.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_location_fsx_windows(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the FSx for Windows location to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LocationArn': 'string',
    'LocationUri': 'string',
    'SecurityGroupArns': [
        'string',
    ],
    'CreationTime': datetime(2015, 1, 1),
    'User': 'string',
    'Domain': 'string'
}


Response Structure

(dict) --
LocationArn (string) --The Amazon resource Name (ARN) of the FSx for Windows location that was described.

LocationUri (string) --The URL of the FSx for Windows location that was described.

SecurityGroupArns (list) --The Amazon Resource Names (ARNs) of the security groups that are configured for the for the FSx for Windows file system.

(string) --


CreationTime (datetime) --The time that the FSx for Windows location was created.

User (string) --The user who has the permissions to access files and folders in the FSx for Windows file system.

Domain (string) --The name of the Windows domain that the FSx for Windows server belongs to.






Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string',
        'LocationUri': 'string',
        'SecurityGroupArns': [
            'string',
        ],
        'CreationTime': datetime(2015, 1, 1),
        'User': 'string',
        'Domain': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def describe_location_nfs(LocationArn=None):
    """
    Returns metadata, such as the path information, about a NFS location.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_location_nfs(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]\nThe Amazon resource Name (ARN) of the NFS location to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LocationArn': 'string',
    'LocationUri': 'string',
    'OnPremConfig': {
        'AgentArns': [
            'string',
        ]
    },
    'MountOptions': {
        'Version': 'AUTOMATIC'|'NFS3'|'NFS4_0'|'NFS4_1'
    },
    'CreationTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --DescribeLocationNfsResponse

LocationArn (string) --The Amazon resource Name (ARN) of the NFS location that was described.

LocationUri (string) --The URL of the source NFS location that was described.

OnPremConfig (dict) --A list of Amazon Resource Names (ARNs) of agents to use for a Network File System (NFS) location.

AgentArns (list) --ARNs)of the agents to use for an NFS location.

(string) --




MountOptions (dict) --The NFS mount options that DataSync used to mount your NFS share.

Version (string) --The specific NFS version that you want DataSync to use to mount your NFS share. If the server refuses to use the version specified, the sync will fail. If you don\'t specify a version, DataSync defaults to AUTOMATIC . That is, DataSync automatically selects a version based on negotiation with the NFS server.
You can specify the following NFS versions:

**NFSv3 ** - stateless protocol version that allows for asynchronous writes on the server.
**NFSv4.0 ** - stateful, firewall-friendly protocol version that supports delegations and pseudo filesystems.
**NFSv4.1 ** - stateful protocol version that supports sessions, directory delegations, and parallel data processing. Version 4.1 also includes all features available in version 4.0.




CreationTime (datetime) --The time that the NFS location was created.






Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string',
        'LocationUri': 'string',
        'OnPremConfig': {
            'AgentArns': [
                'string',
            ]
        },
        'MountOptions': {
            'Version': 'AUTOMATIC'|'NFS3'|'NFS4_0'|'NFS4_1'
        },
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    **NFSv3 ** - stateless protocol version that allows for asynchronous writes on the server.
    **NFSv4.0 ** - stateful, firewall-friendly protocol version that supports delegations and pseudo filesystems.
    **NFSv4.1 ** - stateful protocol version that supports sessions, directory delegations, and parallel data processing. Version 4.1 also includes all features available in version 4.0.
    
    """
    pass

def describe_location_s3(LocationArn=None):
    """
    Returns metadata, such as bucket name, about an Amazon S3 bucket location.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_location_s3(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Amazon S3 bucket location to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LocationArn': 'string',
    'LocationUri': 'string',
    'S3StorageClass': 'STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
    'S3Config': {
        'BucketAccessRoleArn': 'string'
    },
    'CreationTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --DescribeLocationS3Response

LocationArn (string) --The Amazon Resource Name (ARN) of the Amazon S3 bucket location.

LocationUri (string) --The URL of the Amazon S3 location that was described.

S3StorageClass (string) --The Amazon S3 storage class that you chose to store your files in when this location is used as a task destination. For more information about S3 storage classes, see Amazon S3 Storage Classes in the Amazon Simple Storage Service Developer Guide . Some storage classes have behaviors that can affect your S3 storage cost. For detailed information, see  using-storage-classes .

S3Config (dict) --The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that is used to access an Amazon S3 bucket.
For detailed information about using such a role, see Creating a Location for Amazon S3 in the AWS DataSync User Guide .

BucketAccessRoleArn (string) --The Amazon S3 bucket to access. This bucket is used as a parameter in the  CreateLocationS3 operation.



CreationTime (datetime) --The time that the Amazon S3 bucket location was created.






Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string',
        'LocationUri': 'string',
        'S3StorageClass': 'STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
        'S3Config': {
            'BucketAccessRoleArn': 'string'
        },
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_location_smb(LocationArn=None):
    """
    Returns metadata, such as the path and user information about a SMB location.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_location_smb(
        LocationArn='string'
    )
    
    
    :type LocationArn: string
    :param LocationArn: [REQUIRED]\nThe Amazon resource Name (ARN) of the SMB location to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LocationArn': 'string',
    'LocationUri': 'string',
    'AgentArns': [
        'string',
    ],
    'User': 'string',
    'Domain': 'string',
    'MountOptions': {
        'Version': 'AUTOMATIC'|'SMB2'|'SMB3'
    },
    'CreationTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --DescribeLocationSmbResponse

LocationArn (string) --The Amazon resource Name (ARN) of the SMB location that was described.

LocationUri (string) --The URL of the source SBM location that was described.

AgentArns (list) --The Amazon Resource Name (ARN) of the source SMB file system location that is created.

(string) --


User (string) --The user who can mount the share, has the permissions to access files and folders in the SMB share.

Domain (string) --The name of the Windows domain that the SMB server belongs to.

MountOptions (dict) --The mount options that are available for DataSync to use to access an SMB location.

Version (string) --The specific SMB version that you want DataSync to use to mount your SMB share. If you don\'t specify a version, DataSync defaults to AUTOMATIC . That is, DataSync automatically selects a version based on negotiation with the SMB server.



CreationTime (datetime) --The time that the SMB location was created.






Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'LocationArn': 'string',
        'LocationUri': 'string',
        'AgentArns': [
            'string',
        ],
        'User': 'string',
        'Domain': 'string',
        'MountOptions': {
            'Version': 'AUTOMATIC'|'SMB2'|'SMB3'
        },
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def describe_task(TaskArn=None):
    """
    Returns metadata about a task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_task(
        TaskArn='string'
    )
    
    
    :type TaskArn: string
    :param TaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the task to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TaskArn': 'string',
    'Status': 'AVAILABLE'|'CREATING'|'QUEUED'|'RUNNING'|'UNAVAILABLE',
    'Name': 'string',
    'CurrentTaskExecutionArn': 'string',
    'SourceLocationArn': 'string',
    'DestinationLocationArn': 'string',
    'CloudWatchLogGroupArn': 'string',
    'SourceNetworkInterfaceArns': [
        'string',
    ],
    'DestinationNetworkInterfaceArns': [
        'string',
    ],
    'Options': {
        'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'ONLY_FILES_TRANSFERRED'|'NONE',
        'OverwriteMode': 'ALWAYS'|'NEVER',
        'Atime': 'NONE'|'BEST_EFFORT',
        'Mtime': 'NONE'|'PRESERVE',
        'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
        'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
        'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
        'PreserveDevices': 'NONE'|'PRESERVE',
        'PosixPermissions': 'NONE'|'PRESERVE',
        'BytesPerSecond': 123,
        'TaskQueueing': 'ENABLED'|'DISABLED',
        'LogLevel': 'OFF'|'BASIC'|'TRANSFER'
    },
    'Excludes': [
        {
            'FilterType': 'SIMPLE_PATTERN',
            'Value': 'string'
        },
    ],
    'Schedule': {
        'ScheduleExpression': 'string'
    },
    'ErrorCode': 'string',
    'ErrorDetail': 'string',
    'CreationTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --DescribeTaskResponse

TaskArn (string) --The Amazon Resource Name (ARN) of the task that was described.

Status (string) --The status of the task that was described.
For detailed information about task execution statuses, see Understanding Task Statuses in the AWS DataSync User Guide.

Name (string) --The name of the task that was described.

CurrentTaskExecutionArn (string) --The Amazon Resource Name (ARN) of the task execution that is syncing files.

SourceLocationArn (string) --The Amazon Resource Name (ARN) of the source file system\'s location.

DestinationLocationArn (string) --The Amazon Resource Name (ARN) of the AWS storage resource\'s location.

CloudWatchLogGroupArn (string) --The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that was used to monitor and log events in the task.
For more information on these groups, see Working with Log Groups and Log Streams in the Amazon CloudWatch User Guide .

SourceNetworkInterfaceArns (list) --The Amazon Resource Name (ARN) of the source ENIs (Elastic Network Interface) that was created for your subnet.

(string) --


DestinationNetworkInterfaceArns (list) --The Amazon Resource Name (ARN) of the destination ENIs (Elastic Network Interface) that was created for your subnet.

(string) --


Options (dict) --The set of configuration options that control the behavior of a single execution of the task that occurs when you call StartTaskExecution . You can configure these options to preserve metadata such as user ID (UID) and group (GID), file permissions, data integrity verification, and so on.
For each individual task execution, you can override these options by specifying the overriding OverrideOptions value to operation.

VerifyMode (string) --A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
Default value: POINT_IN_TIME_CONSISTENT.
POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.
NONE: Skip verification.

OverwriteMode (string) --A value that determines whether files at the destination should be overwritten or preserved when copying files. If set to NEVER a destination file will not be replaced by a source file, even if the destination file differs from the source file. If you modify files in the destination and you sync the files, you can use this value to protect against overwriting those changes.
Some storage classes have specific behaviors that can affect your S3 storage cost. For detailed information, see  using-storage-classes in the AWS DataSync User Guide .

Atime (string) --A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set Atime to BEST_EFFORT, DataSync attempts to preserve the original Atime attribute on all source files (that is, the version before the PREPARING phase). However, Atime \'s behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.
Default value: BEST_EFFORT.
BEST_EFFORT: Attempt to preserve the per-file Atime value (recommended).
NONE: Ignore Atime .

Note
If Atime is set to BEST_EFFORT, Mtime must be set to PRESERVE.
If Atime is set to NONE, Mtime must also be NONE.


Mtime (string) --A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
Default value: PRESERVE.
PRESERVE: Preserve original Mtime (recommended)
NONE: Ignore Mtime .

Note
If Mtime is set to PRESERVE, Atime must be set to BEST_EFFORT.
If Mtime is set to NONE, Atime must also be set to NONE.


Uid (string) --The user ID (UID) of the file\'s owner.
Default value: INT_VALUE. This preserves the integer value of the ID.
INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
NONE: Ignore UID and GID.

Gid (string) --The group ID (GID) of the file\'s owners.
Default value: INT_VALUE. This preserves the integer value of the ID.
INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
NONE: Ignore UID and GID.

PreserveDeletedFiles (string) --A value that specifies whether files in the destination that don\'t exist in the source file system should be preserved. This option can affect your storage cost. If your task deletes objects, you might incur minimum storage duration charges for certain storage classes. For detailed information, see  using-storage-classes in the AWS DataSync User Guide .
Default value: PRESERVE.
PRESERVE: Ignore such destination files (recommended).
REMOVE: Delete destination files that aren\xe2\x80\x99t present in the source.

PreserveDevices (string) --A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.

Note
AWS DataSync can\'t sync the actual contents of such devices, because they are nonterminal and don\'t return an end-of-file (EOF) marker.

Default value: NONE.
NONE: Ignore special devices (recommended).
PRESERVE: Preserve character and block device metadata. This option isn\'t currently supported for Amazon EFS.

PosixPermissions (string) --A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
Default value: PRESERVE.
PRESERVE: Preserve POSIX-style permissions (recommended).
NONE: Ignore permissions.

Note
AWS DataSync can preserve extant permissions of a source location.


BytesPerSecond (integer) --A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to 1048576 (=1024*1024 ).

TaskQueueing (string) --A value that determines whether tasks should be queued before executing the tasks. If set to ENABLED , the tasks will be queued. The default is ENABLED .
If you use the same agent to run multiple tasks you can enable the tasks to run in series. For more information see  queue-task-execution .

LogLevel (string) --A value that determines the type of logs DataSync will deliver to your AWS CloudWatch Logs file. If set to OFF , no logs will be delivered. BASIC will deliver a few logs per transfer operation and TRANSFER will deliver a verbose log that contains logs for every file that is transferred.



Excludes (list) --A list of filter rules that determines which files to exclude from a task. The list should contain a single filter string that consists of the patterns to exclude. The patterns are delimited by "|" (that is, a pipe), for example: "/folder1|/folder2"

(dict) --Specifies which files, folders and objects to include or exclude when transferring files from source to destination.

FilterType (string) --The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

Value (string) --A single filter string that consists of the patterns to include or exclude. The patterns are delimited by "|" (that is, a pipe), for example: /folder1|/folder2





Schedule (dict) --The schedule used to periodically transfer files from a source to a destination location.

ScheduleExpression (string) --A cron expression that specifies when AWS DataSync initiates a scheduled transfer from a source to a destination location.



ErrorCode (string) --Errors that AWS DataSync encountered during execution of the task. You can use this error code to help troubleshoot issues.

ErrorDetail (string) --Detailed description of an error that was encountered during the task execution. You can use this information to help troubleshoot issues.

CreationTime (datetime) --The time that the task was created.






Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'TaskArn': 'string',
        'Status': 'AVAILABLE'|'CREATING'|'QUEUED'|'RUNNING'|'UNAVAILABLE',
        'Name': 'string',
        'CurrentTaskExecutionArn': 'string',
        'SourceLocationArn': 'string',
        'DestinationLocationArn': 'string',
        'CloudWatchLogGroupArn': 'string',
        'SourceNetworkInterfaceArns': [
            'string',
        ],
        'DestinationNetworkInterfaceArns': [
            'string',
        ],
        'Options': {
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'ONLY_FILES_TRANSFERRED'|'NONE',
            'OverwriteMode': 'ALWAYS'|'NEVER',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'PRESERVE',
            'BytesPerSecond': 123,
            'TaskQueueing': 'ENABLED'|'DISABLED',
            'LogLevel': 'OFF'|'BASIC'|'TRANSFER'
        },
        'Excludes': [
            {
                'FilterType': 'SIMPLE_PATTERN',
                'Value': 'string'
            },
        ],
        'Schedule': {
            'ScheduleExpression': 'string'
        },
        'ErrorCode': 'string',
        'ErrorDetail': 'string',
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_task_execution(TaskExecutionArn=None):
    """
    Returns detailed metadata about a task that is being executed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_task_execution(
        TaskExecutionArn='string'
    )
    
    
    :type TaskExecutionArn: string
    :param TaskExecutionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the task that is being executed.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TaskExecutionArn': 'string',
    'Status': 'QUEUED'|'LAUNCHING'|'PREPARING'|'TRANSFERRING'|'VERIFYING'|'SUCCESS'|'ERROR',
    'Options': {
        'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'ONLY_FILES_TRANSFERRED'|'NONE',
        'OverwriteMode': 'ALWAYS'|'NEVER',
        'Atime': 'NONE'|'BEST_EFFORT',
        'Mtime': 'NONE'|'PRESERVE',
        'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
        'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
        'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
        'PreserveDevices': 'NONE'|'PRESERVE',
        'PosixPermissions': 'NONE'|'PRESERVE',
        'BytesPerSecond': 123,
        'TaskQueueing': 'ENABLED'|'DISABLED',
        'LogLevel': 'OFF'|'BASIC'|'TRANSFER'
    },
    'Excludes': [
        {
            'FilterType': 'SIMPLE_PATTERN',
            'Value': 'string'
        },
    ],
    'Includes': [
        {
            'FilterType': 'SIMPLE_PATTERN',
            'Value': 'string'
        },
    ],
    'StartTime': datetime(2015, 1, 1),
    'EstimatedFilesToTransfer': 123,
    'EstimatedBytesToTransfer': 123,
    'FilesTransferred': 123,
    'BytesWritten': 123,
    'BytesTransferred': 123,
    'Result': {
        'PrepareDuration': 123,
        'PrepareStatus': 'PENDING'|'SUCCESS'|'ERROR',
        'TotalDuration': 123,
        'TransferDuration': 123,
        'TransferStatus': 'PENDING'|'SUCCESS'|'ERROR',
        'VerifyDuration': 123,
        'VerifyStatus': 'PENDING'|'SUCCESS'|'ERROR',
        'ErrorCode': 'string',
        'ErrorDetail': 'string'
    }
}


Response Structure

(dict) --DescribeTaskExecutionResponse

TaskExecutionArn (string) --The Amazon Resource Name (ARN) of the task execution that was described. TaskExecutionArn is hierarchical and includes TaskArn for the task that was executed.
For example, a TaskExecution value with the ARN arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2/execution/exec-08ef1e88ec491019b executed the task with the ARN arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2 .

Status (string) --The status of the task execution.
For detailed information about task execution statuses, see Understanding Task Statuses in the AWS DataSync User Guide.

Options (dict) --Represents the options that are available to control the behavior of a  StartTaskExecution operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file permissions, and also overwriting files in the destination, data integrity verification, and so on.
A task has a set of default options associated with it. If you don\'t specify an option in  StartTaskExecution , the default value is used. You can override the defaults options on each task execution by specifying an overriding Options value to  StartTaskExecution .

VerifyMode (string) --A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.
Default value: POINT_IN_TIME_CONSISTENT.
POINT_IN_TIME_CONSISTENT: Perform verification (recommended).
ONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.
NONE: Skip verification.

OverwriteMode (string) --A value that determines whether files at the destination should be overwritten or preserved when copying files. If set to NEVER a destination file will not be replaced by a source file, even if the destination file differs from the source file. If you modify files in the destination and you sync the files, you can use this value to protect against overwriting those changes.
Some storage classes have specific behaviors that can affect your S3 storage cost. For detailed information, see  using-storage-classes in the AWS DataSync User Guide .

Atime (string) --A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set Atime to BEST_EFFORT, DataSync attempts to preserve the original Atime attribute on all source files (that is, the version before the PREPARING phase). However, Atime \'s behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.
Default value: BEST_EFFORT.
BEST_EFFORT: Attempt to preserve the per-file Atime value (recommended).
NONE: Ignore Atime .

Note
If Atime is set to BEST_EFFORT, Mtime must be set to PRESERVE.
If Atime is set to NONE, Mtime must also be NONE.


Mtime (string) --A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.
Default value: PRESERVE.
PRESERVE: Preserve original Mtime (recommended)
NONE: Ignore Mtime .

Note
If Mtime is set to PRESERVE, Atime must be set to BEST_EFFORT.
If Mtime is set to NONE, Atime must also be set to NONE.


Uid (string) --The user ID (UID) of the file\'s owner.
Default value: INT_VALUE. This preserves the integer value of the ID.
INT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).
NONE: Ignore UID and GID.

Gid (string) --The group ID (GID) of the file\'s owners.
Default value: INT_VALUE. This preserves the integer value of the ID.
INT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).
NONE: Ignore UID and GID.

PreserveDeletedFiles (string) --A value that specifies whether files in the destination that don\'t exist in the source file system should be preserved. This option can affect your storage cost. If your task deletes objects, you might incur minimum storage duration charges for certain storage classes. For detailed information, see  using-storage-classes in the AWS DataSync User Guide .
Default value: PRESERVE.
PRESERVE: Ignore such destination files (recommended).
REMOVE: Delete destination files that aren\xe2\x80\x99t present in the source.

PreserveDevices (string) --A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.

Note
AWS DataSync can\'t sync the actual contents of such devices, because they are nonterminal and don\'t return an end-of-file (EOF) marker.

Default value: NONE.
NONE: Ignore special devices (recommended).
PRESERVE: Preserve character and block device metadata. This option isn\'t currently supported for Amazon EFS.

PosixPermissions (string) --A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.
Default value: PRESERVE.
PRESERVE: Preserve POSIX-style permissions (recommended).
NONE: Ignore permissions.

Note
AWS DataSync can preserve extant permissions of a source location.


BytesPerSecond (integer) --A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to 1048576 (=1024*1024 ).

TaskQueueing (string) --A value that determines whether tasks should be queued before executing the tasks. If set to ENABLED , the tasks will be queued. The default is ENABLED .
If you use the same agent to run multiple tasks you can enable the tasks to run in series. For more information see  queue-task-execution .

LogLevel (string) --A value that determines the type of logs DataSync will deliver to your AWS CloudWatch Logs file. If set to OFF , no logs will be delivered. BASIC will deliver a few logs per transfer operation and TRANSFER will deliver a verbose log that contains logs for every file that is transferred.



Excludes (list) --A list of filter rules that determines which files to exclude from a task. The list should contain a single filter string that consists of the patterns to exclude. The patterns are delimited by "|" (that is, a pipe), for example: "/folder1|/folder2"

(dict) --Specifies which files, folders and objects to include or exclude when transferring files from source to destination.

FilterType (string) --The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

Value (string) --A single filter string that consists of the patterns to include or exclude. The patterns are delimited by "|" (that is, a pipe), for example: /folder1|/folder2





Includes (list) --A list of filter rules that determines which files to include when running a task. The list should contain a single filter string that consists of the patterns to include. The patterns are delimited by "|" (that is, a pipe), for example: "/folder1|/folder2"

(dict) --Specifies which files, folders and objects to include or exclude when transferring files from source to destination.

FilterType (string) --The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.

Value (string) --A single filter string that consists of the patterns to include or exclude. The patterns are delimited by "|" (that is, a pipe), for example: /folder1|/folder2





StartTime (datetime) --The time that the task execution was started.

EstimatedFilesToTransfer (integer) --The expected number of files that is to be transferred over the network. This value is calculated during the PREPARING phase, before the TRANSFERRING phase. This value is the expected number of files to be transferred. It\'s calculated based on comparing the content of the source and destination locations and finding the delta that needs to be transferred.

EstimatedBytesToTransfer (integer) --The estimated physical number of bytes that is to be transferred over the network.

FilesTransferred (integer) --The actual number of files that was transferred over the network. This value is calculated and updated on an ongoing basis during the TRANSFERRING phase. It\'s updated periodically when each file is read from the source and sent over the network.
If failures occur during a transfer, this value can be less than EstimatedFilesToTransfer . This value can also be greater than EstimatedFilesTransferred in some cases. This element is implementation-specific for some location types, so don\'t use it as an indicator for a correct file number or to monitor your task execution.

BytesWritten (integer) --The number of logical bytes written to the destination AWS storage resource.

BytesTransferred (integer) --The physical number of bytes transferred over the network.

Result (dict) --The result of the task execution.

PrepareDuration (integer) --The total time in milliseconds that AWS DataSync spent in the PREPARING phase.

PrepareStatus (string) --The status of the PREPARING phase.

TotalDuration (integer) --The total time in milliseconds that AWS DataSync took to transfer the file from the source to the destination location.

TransferDuration (integer) --The total time in milliseconds that AWS DataSync spent in the TRANSFERRING phase.

TransferStatus (string) --The status of the TRANSFERRING Phase.

VerifyDuration (integer) --The total time in milliseconds that AWS DataSync spent in the VERIFYING phase.

VerifyStatus (string) --The status of the VERIFYING Phase.

ErrorCode (string) --Errors that AWS DataSync encountered during execution of the task. You can use this error code to help troubleshoot issues.

ErrorDetail (string) --Detailed description of an error that was encountered during the task execution. You can use this information to help troubleshoot issues.








Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'TaskExecutionArn': 'string',
        'Status': 'QUEUED'|'LAUNCHING'|'PREPARING'|'TRANSFERRING'|'VERIFYING'|'SUCCESS'|'ERROR',
        'Options': {
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'ONLY_FILES_TRANSFERRED'|'NONE',
            'OverwriteMode': 'ALWAYS'|'NEVER',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'PRESERVE',
            'BytesPerSecond': 123,
            'TaskQueueing': 'ENABLED'|'DISABLED',
            'LogLevel': 'OFF'|'BASIC'|'TRANSFER'
        },
        'Excludes': [
            {
                'FilterType': 'SIMPLE_PATTERN',
                'Value': 'string'
            },
        ],
        'Includes': [
            {
                'FilterType': 'SIMPLE_PATTERN',
                'Value': 'string'
            },
        ],
        'StartTime': datetime(2015, 1, 1),
        'EstimatedFilesToTransfer': 123,
        'EstimatedBytesToTransfer': 123,
        'FilesTransferred': 123,
        'BytesWritten': 123,
        'BytesTransferred': 123,
        'Result': {
            'PrepareDuration': 123,
            'PrepareStatus': 'PENDING'|'SUCCESS'|'ERROR',
            'TotalDuration': 123,
            'TransferDuration': 123,
            'TransferStatus': 'PENDING'|'SUCCESS'|'ERROR',
            'VerifyDuration': 123,
            'VerifyStatus': 'PENDING'|'SUCCESS'|'ERROR',
            'ErrorCode': 'string',
            'ErrorDetail': 'string'
        }
    }
    
    
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

def list_agents(MaxResults=None, NextToken=None):
    """
    Returns a list of agents owned by an AWS account in the AWS Region specified in the request. The returned list is ordered by agent Amazon Resource Name (ARN).
    By default, this operation returns a maximum of 100 agents. This operation supports pagination that enables you to optionally reduce the number of agents returned in a response.
    If you have more agents than are returned in a response (that is, the response returns only a truncated list of your agents), the response contains a marker that you can specify in your next request to fetch the next page of agents.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_agents(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of agents to list.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of agents.

    :rtype: dict

ReturnsResponse Syntax
{
    'Agents': [
        {
            'AgentArn': 'string',
            'Name': 'string',
            'Status': 'ONLINE'|'OFFLINE'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
ListAgentsResponse

Agents (list) --
A list of agents in your account.

(dict) --
Represents a single entry in a list of agents. AgentListEntry returns an array that contains a list of agents when the  ListAgents operation is called.

AgentArn (string) --
The Amazon Resource Name (ARN) of the agent.

Name (string) --
The name of the agent.

Status (string) --
The status of the agent.





NextToken (string) --
An opaque string that indicates the position at which to begin returning the next list of agents.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'Agents': [
            {
                'AgentArn': 'string',
                'Name': 'string',
                'Status': 'ONLINE'|'OFFLINE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def list_locations(MaxResults=None, NextToken=None):
    """
    Returns a lists of source and destination locations.
    If you have more locations than are returned in a response (that is, the response returns only a truncated list of your agents), the response contains a token that you can specify in your next request to fetch the next page of locations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_locations(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of locations to return.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of locations.

    :rtype: dict

ReturnsResponse Syntax
{
    'Locations': [
        {
            'LocationArn': 'string',
            'LocationUri': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
ListLocationsResponse

Locations (list) --
An array that contains a list of locations.

(dict) --
Represents a single entry in a list of locations. LocationListEntry returns an array that contains a list of locations when the  ListLocations operation is called.

LocationArn (string) --
The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon EFS, the location is the export path. For Amazon S3, the location is the prefix path that you want to mount and use as the root of the location.

LocationUri (string) --
Represents a list of URLs of a location. LocationUri returns an array that contains a list of locations when the  ListLocations operation is called.
Format: TYPE://GLOBAL_ID/SUBDIR .
TYPE designates the type of location. Valid values: NFS | EFS | S3.
GLOBAL_ID is the globally unique identifier of the resource that backs the location. An example for EFS is us-east-2.fs-abcd1234 . An example for Amazon S3 is the bucket name, such as myBucket . An example for NFS is a valid IPv4 address or a host name compliant with Domain Name Service (DNS).
SUBDIR is a valid file system path, delimited by forward slashes as is the *nix convention. For NFS and Amazon EFS, it\'s the export path to mount the location. For Amazon S3, it\'s the prefix path that you mount to and treat as the root of the location.





NextToken (string) --
An opaque string that indicates the position at which to begin returning the next list of locations.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'Locations': [
            {
                'LocationArn': 'string',
                'LocationUri': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None, MaxResults=None, NextToken=None):
    """
    Returns all the tags associated with a specified resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource whose tags to list.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of locations to return.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of locations.

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
ListTagsForResourceResponse

Tags (list) --
Array of resource tags.

(dict) --
Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the  ListTagsForResource operation is called.

Key (string) --
The key for an AWS resource tag.

Value (string) --
The value for an AWS resource tag.





NextToken (string) --
An opaque string that indicates the position at which to begin returning the next list of resource tags.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


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
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def list_task_executions(TaskArn=None, MaxResults=None, NextToken=None):
    """
    Returns a list of executed tasks.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_task_executions(
        TaskArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type TaskArn: string
    :param TaskArn: The Amazon Resource Name (ARN) of the task whose tasks you want to list.

    :type MaxResults: integer
    :param MaxResults: The maximum number of executed tasks to list.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of the executed tasks.

    :rtype: dict

ReturnsResponse Syntax
{
    'TaskExecutions': [
        {
            'TaskExecutionArn': 'string',
            'Status': 'QUEUED'|'LAUNCHING'|'PREPARING'|'TRANSFERRING'|'VERIFYING'|'SUCCESS'|'ERROR'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
ListTaskExecutionsResponse

TaskExecutions (list) --
A list of executed tasks.

(dict) --
Represents a single entry in a list of task executions. TaskExecutionListEntry returns an array that contains a list of specific invocations of a task when  ListTaskExecutions operation is called.

TaskExecutionArn (string) --
The Amazon Resource Name (ARN) of the task that was executed.

Status (string) --
The status of a task execution.





NextToken (string) --
An opaque string that indicates the position at which to begin returning the next list of executed tasks.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'TaskExecutions': [
            {
                'TaskExecutionArn': 'string',
                'Status': 'QUEUED'|'LAUNCHING'|'PREPARING'|'TRANSFERRING'|'VERIFYING'|'SUCCESS'|'ERROR'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def list_tasks(MaxResults=None, NextToken=None):
    """
    Returns a list of all the tasks.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tasks(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of tasks to return.

    :type NextToken: string
    :param NextToken: An opaque string that indicates the position at which to begin the next list of tasks.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tasks': [
        {
            'TaskArn': 'string',
            'Status': 'AVAILABLE'|'CREATING'|'QUEUED'|'RUNNING'|'UNAVAILABLE',
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
ListTasksResponse

Tasks (list) --
A list of all the tasks that are returned.

(dict) --
Represents a single entry in a list of tasks. TaskListEntry returns an array that contains a list of tasks when the  ListTasks operation is called. A task includes the source and destination file systems to sync and the options to use for the tasks.

TaskArn (string) --
The Amazon Resource Name (ARN) of the task.

Status (string) --
The status of the task.

Name (string) --
The name of the task.





NextToken (string) --
An opaque string that indicates the position at which to begin returning the next list of tasks.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'Tasks': [
            {
                'TaskArn': 'string',
                'Status': 'AVAILABLE'|'CREATING'|'QUEUED'|'RUNNING'|'UNAVAILABLE',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def start_task_execution(TaskArn=None, OverrideOptions=None, Includes=None):
    """
    Starts a specific invocation of a task. A TaskExecution value represents an individual run of a task. Each task can have at most one TaskExecution at a time.
    For detailed information, see the Task Execution section in the Components and Terminology topic in the AWS DataSync User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_task_execution(
        TaskArn='string',
        OverrideOptions={
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'ONLY_FILES_TRANSFERRED'|'NONE',
            'OverwriteMode': 'ALWAYS'|'NEVER',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'PRESERVE',
            'BytesPerSecond': 123,
            'TaskQueueing': 'ENABLED'|'DISABLED',
            'LogLevel': 'OFF'|'BASIC'|'TRANSFER'
        },
        Includes=[
            {
                'FilterType': 'SIMPLE_PATTERN',
                'Value': 'string'
            },
        ]
    )
    
    
    :type TaskArn: string
    :param TaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the task to start.\n

    :type OverrideOptions: dict
    :param OverrideOptions: Represents the options that are available to control the behavior of a StartTaskExecution operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file permissions, and also overwriting files in the destination, data integrity verification, and so on.\nA task has a set of default options associated with it. If you don\'t specify an option in StartTaskExecution , the default value is used. You can override the defaults options on each task execution by specifying an overriding Options value to StartTaskExecution .\n\nVerifyMode (string) --A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.\nDefault value: POINT_IN_TIME_CONSISTENT.\nPOINT_IN_TIME_CONSISTENT: Perform verification (recommended).\nONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.\nNONE: Skip verification.\n\nOverwriteMode (string) --A value that determines whether files at the destination should be overwritten or preserved when copying files. If set to NEVER a destination file will not be replaced by a source file, even if the destination file differs from the source file. If you modify files in the destination and you sync the files, you can use this value to protect against overwriting those changes.\nSome storage classes have specific behaviors that can affect your S3 storage cost. For detailed information, see using-storage-classes in the AWS DataSync User Guide .\n\nAtime (string) --A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set Atime to BEST_EFFORT, DataSync attempts to preserve the original Atime attribute on all source files (that is, the version before the PREPARING phase). However, Atime \'s behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.\nDefault value: BEST_EFFORT.\nBEST_EFFORT: Attempt to preserve the per-file Atime value (recommended).\nNONE: Ignore Atime .\n\nNote\nIf Atime is set to BEST_EFFORT, Mtime must be set to PRESERVE.\nIf Atime is set to NONE, Mtime must also be NONE.\n\n\nMtime (string) --A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.\nDefault value: PRESERVE.\nPRESERVE: Preserve original Mtime (recommended)\nNONE: Ignore Mtime .\n\nNote\nIf Mtime is set to PRESERVE, Atime must be set to BEST_EFFORT.\nIf Mtime is set to NONE, Atime must also be set to NONE.\n\n\nUid (string) --The user ID (UID) of the file\'s owner.\nDefault value: INT_VALUE. This preserves the integer value of the ID.\nINT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).\nNONE: Ignore UID and GID.\n\nGid (string) --The group ID (GID) of the file\'s owners.\nDefault value: INT_VALUE. This preserves the integer value of the ID.\nINT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).\nNONE: Ignore UID and GID.\n\nPreserveDeletedFiles (string) --A value that specifies whether files in the destination that don\'t exist in the source file system should be preserved. This option can affect your storage cost. If your task deletes objects, you might incur minimum storage duration charges for certain storage classes. For detailed information, see using-storage-classes in the AWS DataSync User Guide .\nDefault value: PRESERVE.\nPRESERVE: Ignore such destination files (recommended).\nREMOVE: Delete destination files that aren\xe2\x80\x99t present in the source.\n\nPreserveDevices (string) --A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.\n\nNote\nAWS DataSync can\'t sync the actual contents of such devices, because they are nonterminal and don\'t return an end-of-file (EOF) marker.\n\nDefault value: NONE.\nNONE: Ignore special devices (recommended).\nPRESERVE: Preserve character and block device metadata. This option isn\'t currently supported for Amazon EFS.\n\nPosixPermissions (string) --A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.\nDefault value: PRESERVE.\nPRESERVE: Preserve POSIX-style permissions (recommended).\nNONE: Ignore permissions.\n\nNote\nAWS DataSync can preserve extant permissions of a source location.\n\n\nBytesPerSecond (integer) --A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to 1048576 (=1024*1024 ).\n\nTaskQueueing (string) --A value that determines whether tasks should be queued before executing the tasks. If set to ENABLED , the tasks will be queued. The default is ENABLED .\nIf you use the same agent to run multiple tasks you can enable the tasks to run in series. For more information see queue-task-execution .\n\nLogLevel (string) --A value that determines the type of logs DataSync will deliver to your AWS CloudWatch Logs file. If set to OFF , no logs will be delivered. BASIC will deliver a few logs per transfer operation and TRANSFER will deliver a verbose log that contains logs for every file that is transferred.\n\n\n

    :type Includes: list
    :param Includes: A list of filter rules that determines which files to include when running a task. The pattern should contain a single filter string that consists of the patterns to include. The patterns are delimited by '|' (that is, a pipe). For example: '/folder1|/folder2'\n\n(dict) --Specifies which files, folders and objects to include or exclude when transferring files from source to destination.\n\nFilterType (string) --The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.\n\nValue (string) --A single filter string that consists of the patterns to include or exclude. The patterns are delimited by '|' (that is, a pipe), for example: /folder1|/folder2\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TaskExecutionArn': 'string'
}


Response Structure

(dict) --
StartTaskExecutionResponse

TaskExecutionArn (string) --
The Amazon Resource Name (ARN) of the specific task execution that was started.







Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {
        'TaskExecutionArn': 'string'
    }
    
    
    :returns: 
    DataSync.Client.exceptions.InvalidRequestException
    DataSync.Client.exceptions.InternalException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Applies a key-value pair to an AWS resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to apply the tag to.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to apply.\n\n(dict) --Represents a single entry in a list of AWS resource tags. TagListEntry returns an array that contains a list of tasks when the ListTagsForResource operation is called.\n\nKey (string) -- [REQUIRED]The key for an AWS resource tag.\n\nValue (string) --The value for an AWS resource tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, Keys=None):
    """
    Removes a tag from an AWS resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        Keys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to remove the tag from.\n

    :type Keys: list
    :param Keys: [REQUIRED]\nThe keys in the key-value pair in the tag to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_agent(AgentArn=None, Name=None):
    """
    Updates the name of an agent.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_agent(
        AgentArn='string',
        Name='string'
    )
    
    
    :type AgentArn: string
    :param AgentArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the agent to update.\n

    :type Name: string
    :param Name: The name that you want to use to configure the agent.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_task(TaskArn=None, Options=None, Excludes=None, Schedule=None, Name=None, CloudWatchLogGroupArn=None):
    """
    Updates the metadata associated with a task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_task(
        TaskArn='string',
        Options={
            'VerifyMode': 'POINT_IN_TIME_CONSISTENT'|'ONLY_FILES_TRANSFERRED'|'NONE',
            'OverwriteMode': 'ALWAYS'|'NEVER',
            'Atime': 'NONE'|'BEST_EFFORT',
            'Mtime': 'NONE'|'PRESERVE',
            'Uid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'Gid': 'NONE'|'INT_VALUE'|'NAME'|'BOTH',
            'PreserveDeletedFiles': 'PRESERVE'|'REMOVE',
            'PreserveDevices': 'NONE'|'PRESERVE',
            'PosixPermissions': 'NONE'|'PRESERVE',
            'BytesPerSecond': 123,
            'TaskQueueing': 'ENABLED'|'DISABLED',
            'LogLevel': 'OFF'|'BASIC'|'TRANSFER'
        },
        Excludes=[
            {
                'FilterType': 'SIMPLE_PATTERN',
                'Value': 'string'
            },
        ],
        Schedule={
            'ScheduleExpression': 'string'
        },
        Name='string',
        CloudWatchLogGroupArn='string'
    )
    
    
    :type TaskArn: string
    :param TaskArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource name of the task to update.\n

    :type Options: dict
    :param Options: Represents the options that are available to control the behavior of a StartTaskExecution operation. Behavior includes preserving metadata such as user ID (UID), group ID (GID), and file permissions, and also overwriting files in the destination, data integrity verification, and so on.\nA task has a set of default options associated with it. If you don\'t specify an option in StartTaskExecution , the default value is used. You can override the defaults options on each task execution by specifying an overriding Options value to StartTaskExecution .\n\nVerifyMode (string) --A value that determines whether a data integrity verification should be performed at the end of a task execution after all data and metadata have been transferred.\nDefault value: POINT_IN_TIME_CONSISTENT.\nPOINT_IN_TIME_CONSISTENT: Perform verification (recommended).\nONLY_FILES_TRANSFERRED: Perform verification on only files that were transferred.\nNONE: Skip verification.\n\nOverwriteMode (string) --A value that determines whether files at the destination should be overwritten or preserved when copying files. If set to NEVER a destination file will not be replaced by a source file, even if the destination file differs from the source file. If you modify files in the destination and you sync the files, you can use this value to protect against overwriting those changes.\nSome storage classes have specific behaviors that can affect your S3 storage cost. For detailed information, see using-storage-classes in the AWS DataSync User Guide .\n\nAtime (string) --A file metadata value that shows the last time a file was accessed (that is, when the file was read or written to). If you set Atime to BEST_EFFORT, DataSync attempts to preserve the original Atime attribute on all source files (that is, the version before the PREPARING phase). However, Atime \'s behavior is not fully standard across platforms, so AWS DataSync can only do this on a best-effort basis.\nDefault value: BEST_EFFORT.\nBEST_EFFORT: Attempt to preserve the per-file Atime value (recommended).\nNONE: Ignore Atime .\n\nNote\nIf Atime is set to BEST_EFFORT, Mtime must be set to PRESERVE.\nIf Atime is set to NONE, Mtime must also be NONE.\n\n\nMtime (string) --A value that indicates the last time that a file was modified (that is, a file was written to) before the PREPARING phase.\nDefault value: PRESERVE.\nPRESERVE: Preserve original Mtime (recommended)\nNONE: Ignore Mtime .\n\nNote\nIf Mtime is set to PRESERVE, Atime must be set to BEST_EFFORT.\nIf Mtime is set to NONE, Atime must also be set to NONE.\n\n\nUid (string) --The user ID (UID) of the file\'s owner.\nDefault value: INT_VALUE. This preserves the integer value of the ID.\nINT_VALUE: Preserve the integer value of UID and group ID (GID) (recommended).\nNONE: Ignore UID and GID.\n\nGid (string) --The group ID (GID) of the file\'s owners.\nDefault value: INT_VALUE. This preserves the integer value of the ID.\nINT_VALUE: Preserve the integer value of user ID (UID) and GID (recommended).\nNONE: Ignore UID and GID.\n\nPreserveDeletedFiles (string) --A value that specifies whether files in the destination that don\'t exist in the source file system should be preserved. This option can affect your storage cost. If your task deletes objects, you might incur minimum storage duration charges for certain storage classes. For detailed information, see using-storage-classes in the AWS DataSync User Guide .\nDefault value: PRESERVE.\nPRESERVE: Ignore such destination files (recommended).\nREMOVE: Delete destination files that aren\xe2\x80\x99t present in the source.\n\nPreserveDevices (string) --A value that determines whether AWS DataSync should preserve the metadata of block and character devices in the source file system, and recreate the files with that device name and metadata on the destination.\n\nNote\nAWS DataSync can\'t sync the actual contents of such devices, because they are nonterminal and don\'t return an end-of-file (EOF) marker.\n\nDefault value: NONE.\nNONE: Ignore special devices (recommended).\nPRESERVE: Preserve character and block device metadata. This option isn\'t currently supported for Amazon EFS.\n\nPosixPermissions (string) --A value that determines which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.\nDefault value: PRESERVE.\nPRESERVE: Preserve POSIX-style permissions (recommended).\nNONE: Ignore permissions.\n\nNote\nAWS DataSync can preserve extant permissions of a source location.\n\n\nBytesPerSecond (integer) --A value that limits the bandwidth used by AWS DataSync. For example, if you want AWS DataSync to use a maximum of 1 MB, set this value to 1048576 (=1024*1024 ).\n\nTaskQueueing (string) --A value that determines whether tasks should be queued before executing the tasks. If set to ENABLED , the tasks will be queued. The default is ENABLED .\nIf you use the same agent to run multiple tasks you can enable the tasks to run in series. For more information see queue-task-execution .\n\nLogLevel (string) --A value that determines the type of logs DataSync will deliver to your AWS CloudWatch Logs file. If set to OFF , no logs will be delivered. BASIC will deliver a few logs per transfer operation and TRANSFER will deliver a verbose log that contains logs for every file that is transferred.\n\n\n

    :type Excludes: list
    :param Excludes: A list of filter rules that determines which files to exclude from a task. The list should contain a single filter string that consists of the patterns to exclude. The patterns are delimited by '|' (that is, a pipe), for example: '/folder1|/folder2'\n\n(dict) --Specifies which files, folders and objects to include or exclude when transferring files from source to destination.\n\nFilterType (string) --The type of filter rule to apply. AWS DataSync only supports the SIMPLE_PATTERN rule type.\n\nValue (string) --A single filter string that consists of the patterns to include or exclude. The patterns are delimited by '|' (that is, a pipe), for example: /folder1|/folder2\n\n\n\n\n

    :type Schedule: dict
    :param Schedule: Specifies a schedule used to periodically transfer files from a source to a destination location. You can configure your task to execute hourly, daily, weekly or on specific days of the week. You control when in the day or hour you want the task to execute. The time you specify is UTC time. For more information, see task-scheduling .\n\nScheduleExpression (string) -- [REQUIRED]A cron expression that specifies when AWS DataSync initiates a scheduled transfer from a source to a destination location.\n\n\n

    :type Name: string
    :param Name: The name of the task to update.

    :type CloudWatchLogGroupArn: string
    :param CloudWatchLogGroupArn: The Amazon Resource Name (ARN) of the resource name of the CloudWatch LogGroup.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DataSync.Client.exceptions.InvalidRequestException
DataSync.Client.exceptions.InternalException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

