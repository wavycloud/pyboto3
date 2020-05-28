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

def associate_ip_groups(DirectoryId=None, GroupIds=None):
    """
    Associates the specified IP access control group with the specified directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_ip_groups(
        DirectoryId='string',
        GroupIds=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory.\n

    :type GroupIds: list
    :param GroupIds: [REQUIRED]\nThe identifiers of one or more IP access control groups.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.ResourceLimitExceededException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.OperationNotSupportedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def authorize_ip_rules(GroupId=None, UserRules=None):
    """
    Adds one or more rules to the specified IP access control group.
    This action gives users permission to access their WorkSpaces from the CIDR address ranges specified in the rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.authorize_ip_rules(
        GroupId='string',
        UserRules=[
            {
                'ipRule': 'string',
                'ruleDesc': 'string'
            },
        ]
    )
    
    
    :type GroupId: string
    :param GroupId: [REQUIRED]\nThe identifier of the group.\n

    :type UserRules: list
    :param UserRules: [REQUIRED]\nThe rules to add to the group.\n\n(dict) --Describes a rule for an IP access control group.\n\nipRule (string) --The IP address range, in CIDR notation.\n\nruleDesc (string) --The description.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.ResourceLimitExceededException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def copy_workspace_image(Name=None, Description=None, SourceImageId=None, SourceRegion=None, Tags=None):
    """
    Copies the specified image from the specified Region to the current Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.copy_workspace_image(
        Name='string',
        Description='string',
        SourceImageId='string',
        SourceRegion='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the image.\n

    :type Description: string
    :param Description: A description of the image.

    :type SourceImageId: string
    :param SourceImageId: [REQUIRED]\nThe identifier of the source image.\n

    :type SourceRegion: string
    :param SourceRegion: [REQUIRED]\nThe identifier of the source Region.\n

    :type Tags: list
    :param Tags: The tags for the image.\n\n(dict) --Describes a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ImageId': 'string'
}


Response Structure

(dict) --

ImageId (string) --
The identifier of the image.







Exceptions

WorkSpaces.Client.exceptions.ResourceLimitExceededException
WorkSpaces.Client.exceptions.ResourceAlreadyExistsException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.ResourceUnavailableException
WorkSpaces.Client.exceptions.OperationNotSupportedException
WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.InvalidParameterValuesException


    :return: {
        'ImageId': 'string'
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.ResourceLimitExceededException
    WorkSpaces.Client.exceptions.ResourceAlreadyExistsException
    WorkSpaces.Client.exceptions.ResourceNotFoundException
    WorkSpaces.Client.exceptions.ResourceUnavailableException
    WorkSpaces.Client.exceptions.OperationNotSupportedException
    WorkSpaces.Client.exceptions.AccessDeniedException
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    
    """
    pass

def create_ip_group(GroupName=None, GroupDesc=None, UserRules=None, Tags=None):
    """
    Creates an IP access control group.
    An IP access control group provides you with the ability to control the IP addresses from which users are allowed to access their WorkSpaces. To specify the CIDR address ranges, add rules to your IP access control group and then associate the group with your directory. You can add rules when you create the group or at any time using  AuthorizeIpRules .
    There is a default IP access control group associated with your directory. If you don\'t associate an IP access control group with your directory, the default group is used. The default group includes a default rule that allows users to access their WorkSpaces from anywhere. You cannot modify the default IP access control group for your directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_ip_group(
        GroupName='string',
        GroupDesc='string',
        UserRules=[
            {
                'ipRule': 'string',
                'ruleDesc': 'string'
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group.\n

    :type GroupDesc: string
    :param GroupDesc: The description of the group.

    :type UserRules: list
    :param UserRules: The rules to add to the group.\n\n(dict) --Describes a rule for an IP access control group.\n\nipRule (string) --The IP address range, in CIDR notation.\n\nruleDesc (string) --The description.\n\n\n\n\n

    :type Tags: list
    :param Tags: The tags. Each WorkSpaces resource can have a maximum of 50 tags.\n\n(dict) --Describes a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GroupId': 'string'
}


Response Structure

(dict) --

GroupId (string) --
The identifier of the group.







Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceLimitExceededException
WorkSpaces.Client.exceptions.ResourceAlreadyExistsException
WorkSpaces.Client.exceptions.ResourceCreationFailedException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {
        'GroupId': 'string'
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    WorkSpaces.Client.exceptions.ResourceLimitExceededException
    WorkSpaces.Client.exceptions.ResourceAlreadyExistsException
    WorkSpaces.Client.exceptions.ResourceCreationFailedException
    WorkSpaces.Client.exceptions.AccessDeniedException
    
    """
    pass

def create_tags(ResourceId=None, Tags=None):
    """
    Creates the specified tags for the specified WorkSpaces resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_tags(
        ResourceId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, and IP access control groups.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags. Each WorkSpaces resource can have a maximum of 50 tags. If you want to add new tags to a set of existing tags, you must submit all of the existing tags along with the new ones.\n\n(dict) --Describes a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceLimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_workspaces(Workspaces=None):
    """
    Creates one or more WorkSpaces.
    This operation is asynchronous and returns before the WorkSpaces are created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_workspaces(
        Workspaces=[
            {
                'DirectoryId': 'string',
                'UserName': 'string',
                'BundleId': 'string',
                'VolumeEncryptionKey': 'string',
                'UserVolumeEncryptionEnabled': True|False,
                'RootVolumeEncryptionEnabled': True|False,
                'WorkspaceProperties': {
                    'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                    'RunningModeAutoStopTimeoutInMinutes': 123,
                    'RootVolumeSizeGib': 123,
                    'UserVolumeSizeGib': 123,
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type Workspaces: list
    :param Workspaces: [REQUIRED]\nThe WorkSpaces to create. You can specify up to 25 WorkSpaces.\n\n(dict) --Describes the information used to create a WorkSpace.\n\nDirectoryId (string) -- [REQUIRED]The identifier of the AWS Directory Service directory for the WorkSpace. You can use DescribeWorkspaceDirectories to list the available directories.\n\nUserName (string) -- [REQUIRED]The user name of the user for the WorkSpace. This user name must exist in the AWS Directory Service directory for the WorkSpace.\n\nBundleId (string) -- [REQUIRED]The identifier of the bundle for the WorkSpace. You can use DescribeWorkspaceBundles to list the available bundles.\n\nVolumeEncryptionKey (string) --The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.\n\nUserVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the user volume is encrypted.\n\nRootVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the root volume is encrypted.\n\nWorkspaceProperties (dict) --The WorkSpace properties.\n\nRunningMode (string) --The running mode. For more information, see Manage the WorkSpace Running Mode .\n\nRunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.\n\nRootVolumeSizeGib (integer) --The size of the root volume.\n\nUserVolumeSizeGib (integer) --The size of the user storage.\n\nComputeTypeName (string) --The compute type. For more information, see Amazon WorkSpaces Bundles .\n\n\n\nTags (list) --The tags for the WorkSpace.\n\n(dict) --Describes a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedRequests': [
        {
            'WorkspaceRequest': {
                'DirectoryId': 'string',
                'UserName': 'string',
                'BundleId': 'string',
                'VolumeEncryptionKey': 'string',
                'UserVolumeEncryptionEnabled': True|False,
                'RootVolumeEncryptionEnabled': True|False,
                'WorkspaceProperties': {
                    'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                    'RunningModeAutoStopTimeoutInMinutes': 123,
                    'RootVolumeSizeGib': 123,
                    'UserVolumeSizeGib': 123,
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ],
    'PendingRequests': [
        {
            'WorkspaceId': 'string',
            'DirectoryId': 'string',
            'UserName': 'string',
            'IpAddress': 'string',
            'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'RESTORING'|'MAINTENANCE'|'ADMIN_MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
            'BundleId': 'string',
            'SubnetId': 'string',
            'ErrorMessage': 'string',
            'ErrorCode': 'string',
            'ComputerName': 'string',
            'VolumeEncryptionKey': 'string',
            'UserVolumeEncryptionEnabled': True|False,
            'RootVolumeEncryptionEnabled': True|False,
            'WorkspaceProperties': {
                'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                'RunningModeAutoStopTimeoutInMinutes': 123,
                'RootVolumeSizeGib': 123,
                'UserVolumeSizeGib': 123,
                'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
            },
            'ModificationStates': [
                {
                    'Resource': 'ROOT_VOLUME'|'USER_VOLUME'|'COMPUTE_TYPE',
                    'State': 'UPDATE_INITIATED'|'UPDATE_IN_PROGRESS'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
FailedRequests (list) --Information about the WorkSpaces that could not be created.

(dict) --Describes a WorkSpace that cannot be created.

WorkspaceRequest (dict) --Information about the WorkSpace.

DirectoryId (string) --The identifier of the AWS Directory Service directory for the WorkSpace. You can use  DescribeWorkspaceDirectories to list the available directories.

UserName (string) --The user name of the user for the WorkSpace. This user name must exist in the AWS Directory Service directory for the WorkSpace.

BundleId (string) --The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles to list the available bundles.

VolumeEncryptionKey (string) --The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.

UserVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the user volume is encrypted.

RootVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the root volume is encrypted.

WorkspaceProperties (dict) --The WorkSpace properties.

RunningMode (string) --The running mode. For more information, see Manage the WorkSpace Running Mode .

RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.

RootVolumeSizeGib (integer) --The size of the root volume.

UserVolumeSizeGib (integer) --The size of the user storage.

ComputeTypeName (string) --The compute type. For more information, see Amazon WorkSpaces Bundles .



Tags (list) --The tags for the WorkSpace.

(dict) --Describes a tag.

Key (string) --The key of the tag.

Value (string) --The value of the tag.







ErrorCode (string) --The error code that is returned if the WorkSpace cannot be created.

ErrorMessage (string) --The text of the error message that is returned if the WorkSpace cannot be created.





PendingRequests (list) --Information about the WorkSpaces that were created.
Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call  DescribeWorkspaces before the WorkSpace is created, the information returned can be incomplete.

(dict) --Describes a WorkSpace.

WorkspaceId (string) --The identifier of the WorkSpace.

DirectoryId (string) --The identifier of the AWS Directory Service directory for the WorkSpace.

UserName (string) --The user for the WorkSpace.

IpAddress (string) --The IP address of the WorkSpace.

State (string) --The operational state of the WorkSpace.

BundleId (string) --The identifier of the bundle used to create the WorkSpace.

SubnetId (string) --The identifier of the subnet for the WorkSpace.

ErrorMessage (string) --The text of the error message that is returned if the WorkSpace cannot be created.

ErrorCode (string) --The error code that is returned if the WorkSpace cannot be created.

ComputerName (string) --The name of the WorkSpace, as seen by the operating system.

VolumeEncryptionKey (string) --The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.

UserVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the user volume is encrypted.

RootVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the root volume is encrypted.

WorkspaceProperties (dict) --The properties of the WorkSpace.

RunningMode (string) --The running mode. For more information, see Manage the WorkSpace Running Mode .

RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.

RootVolumeSizeGib (integer) --The size of the root volume.

UserVolumeSizeGib (integer) --The size of the user storage.

ComputeTypeName (string) --The compute type. For more information, see Amazon WorkSpaces Bundles .



ModificationStates (list) --The modification states of the WorkSpace.

(dict) --Describes a WorkSpace modification.

Resource (string) --The resource.

State (string) --The modification state.














Exceptions

WorkSpaces.Client.exceptions.ResourceLimitExceededException
WorkSpaces.Client.exceptions.InvalidParameterValuesException


    :return: {
        'FailedRequests': [
            {
                'WorkspaceRequest': {
                    'DirectoryId': 'string',
                    'UserName': 'string',
                    'BundleId': 'string',
                    'VolumeEncryptionKey': 'string',
                    'UserVolumeEncryptionEnabled': True|False,
                    'RootVolumeEncryptionEnabled': True|False,
                    'WorkspaceProperties': {
                        'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                        'RunningModeAutoStopTimeoutInMinutes': 123,
                        'RootVolumeSizeGib': 123,
                        'UserVolumeSizeGib': 123,
                        'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ],
        'PendingRequests': [
            {
                'WorkspaceId': 'string',
                'DirectoryId': 'string',
                'UserName': 'string',
                'IpAddress': 'string',
                'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'RESTORING'|'MAINTENANCE'|'ADMIN_MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
                'BundleId': 'string',
                'SubnetId': 'string',
                'ErrorMessage': 'string',
                'ErrorCode': 'string',
                'ComputerName': 'string',
                'VolumeEncryptionKey': 'string',
                'UserVolumeEncryptionEnabled': True|False,
                'RootVolumeEncryptionEnabled': True|False,
                'WorkspaceProperties': {
                    'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                    'RunningModeAutoStopTimeoutInMinutes': 123,
                    'RootVolumeSizeGib': 123,
                    'UserVolumeSizeGib': 123,
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                },
                'ModificationStates': [
                    {
                        'Resource': 'ROOT_VOLUME'|'USER_VOLUME'|'COMPUTE_TYPE',
                        'State': 'UPDATE_INITIATED'|'UPDATE_IN_PROGRESS'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def delete_ip_group(GroupId=None):
    """
    Deletes the specified IP access control group.
    You cannot delete an IP access control group that is associated with a directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_ip_group(
        GroupId='string'
    )
    
    
    :type GroupId: string
    :param GroupId: [REQUIRED]\nThe identifier of the IP access control group.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.ResourceAssociatedException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    WorkSpaces.Client.exceptions.ResourceNotFoundException
    WorkSpaces.Client.exceptions.ResourceAssociatedException
    WorkSpaces.Client.exceptions.AccessDeniedException
    
    """
    pass

def delete_tags(ResourceId=None, TagKeys=None):
    """
    Deletes the specified tags from the specified WorkSpaces resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_tags(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, and IP access control groups.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.InvalidParameterValuesException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_workspace_image(ImageId=None):
    """
    Deletes the specified image from your account. To delete an image, you must first delete any bundles that are associated with the image and un-share the image if it is shared with other accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_workspace_image(
        ImageId='string'
    )
    
    
    :type ImageId: string
    :param ImageId: [REQUIRED]\nThe identifier of the image.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WorkSpaces.Client.exceptions.ResourceAssociatedException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    WorkSpaces.Client.exceptions.ResourceAssociatedException
    WorkSpaces.Client.exceptions.InvalidResourceStateException
    WorkSpaces.Client.exceptions.AccessDeniedException
    
    """
    pass

def deregister_workspace_directory(DirectoryId=None):
    """
    Deregisters the specified directory. This operation is asynchronous and returns before the WorkSpace directory is deregistered. If any WorkSpaces are registered to this directory, you must remove them before you can deregister the directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_workspace_directory(
        DirectoryId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory. If any WorkSpaces are registered to this directory, you must remove them before you deregister the directory, or you will receive an OperationNotSupportedException error.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.OperationNotSupportedException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.InvalidResourceStateException


    :return: {}
    
    
    :returns: 
    WorkSpaces.Client.exceptions.AccessDeniedException
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    WorkSpaces.Client.exceptions.OperationNotSupportedException
    WorkSpaces.Client.exceptions.ResourceNotFoundException
    WorkSpaces.Client.exceptions.InvalidResourceStateException
    
    """
    pass

def describe_account():
    """
    Retrieves a list that describes the configuration of Bring Your Own License (BYOL) for the specified account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_account()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'DedicatedTenancySupport': 'ENABLED'|'DISABLED',
    'DedicatedTenancyManagementCidrRange': 'string'
}


Response Structure

(dict) --
DedicatedTenancySupport (string) --The status of BYOL (whether BYOL is enabled or disabled).

DedicatedTenancyManagementCidrRange (string) --The IP address range, specified as an IPv4 CIDR block, used for the management network interface.
The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.






Exceptions

WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {
        'DedicatedTenancySupport': 'ENABLED'|'DISABLED',
        'DedicatedTenancyManagementCidrRange': 'string'
    }
    
    
    """
    pass

def describe_account_modifications(NextToken=None):
    """
    Retrieves a list that describes modifications to the configuration of Bring Your Own License (BYOL) for the specified account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_account_modifications(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict
ReturnsResponse Syntax{
    'AccountModifications': [
        {
            'ModificationState': 'PENDING'|'COMPLETED'|'FAILED',
            'DedicatedTenancySupport': 'ENABLED'|'DISABLED',
            'DedicatedTenancyManagementCidrRange': 'string',
            'StartTime': datetime(2015, 1, 1),
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
AccountModifications (list) --The list of modifications to the configuration of BYOL.

(dict) --Describes a modification to the configuration of Bring Your Own License (BYOL) for the specified account.

ModificationState (string) --The state of the modification to the configuration of BYOL.

DedicatedTenancySupport (string) --The status of BYOL (whether BYOL is being enabled or disabled).

DedicatedTenancyManagementCidrRange (string) --The IP address range, specified as an IPv4 CIDR block, for the management network interface used for the account.

StartTime (datetime) --The timestamp when the modification of the BYOL configuration was started.

ErrorCode (string) --The error code that is returned if the configuration of BYOL cannot be modified.

ErrorMessage (string) --The text of the error message that is returned if the configuration of BYOL cannot be modified.





NextToken (string) --The token to use to retrieve the next set of results, or null if no more results are available.






Exceptions

WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {
        'AccountModifications': [
            {
                'ModificationState': 'PENDING'|'COMPLETED'|'FAILED',
                'DedicatedTenancySupport': 'ENABLED'|'DISABLED',
                'DedicatedTenancyManagementCidrRange': 'string',
                'StartTime': datetime(2015, 1, 1),
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_client_properties(ResourceIds=None):
    """
    Retrieves a list that describes one or more specified Amazon WorkSpaces clients.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_client_properties(
        ResourceIds=[
            'string',
        ]
    )
    
    
    :type ResourceIds: list
    :param ResourceIds: [REQUIRED]\nThe resource identifier, in the form of directory IDs.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'ClientPropertiesList': [
        {
            'ResourceId': 'string',
            'ClientProperties': {
                'ReconnectEnabled': 'ENABLED'|'DISABLED'
            }
        },
    ]
}


Response Structure

(dict) --
ClientPropertiesList (list) --Information about the specified Amazon WorkSpaces clients.

(dict) --Information about the Amazon WorkSpaces client.

ResourceId (string) --The resource identifier, in the form of a directory ID.

ClientProperties (dict) --Information about the Amazon WorkSpaces client.

ReconnectEnabled (string) --Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When enabled, users can choose to reconnect to their WorkSpaces without re-entering their credentials.












Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {
        'ClientPropertiesList': [
            {
                'ResourceId': 'string',
                'ClientProperties': {
                    'ReconnectEnabled': 'ENABLED'|'DISABLED'
                }
            },
        ]
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    WorkSpaces.Client.exceptions.ResourceNotFoundException
    WorkSpaces.Client.exceptions.AccessDeniedException
    
    """
    pass

def describe_ip_groups(GroupIds=None, NextToken=None, MaxResults=None):
    """
    Describes one or more of your IP access control groups.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_ip_groups(
        GroupIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type GroupIds: list
    :param GroupIds: The identifiers of one or more IP access control groups.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Result': [
        {
            'groupId': 'string',
            'groupName': 'string',
            'groupDesc': 'string',
            'userRules': [
                {
                    'ipRule': 'string',
                    'ruleDesc': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Result (list) --
Information about the IP access control groups.

(dict) --
Describes an IP access control group.

groupId (string) --
The identifier of the group.

groupName (string) --
The name of the group.

groupDesc (string) --
The description of the group.

userRules (list) --
The rules.

(dict) --
Describes a rule for an IP access control group.

ipRule (string) --
The IP address range, in CIDR notation.

ruleDesc (string) --
The description.









NextToken (string) --
The token to use to retrieve the next set of results, or null if no more results are available.







Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {
        'Result': [
            {
                'groupId': 'string',
                'groupName': 'string',
                'groupDesc': 'string',
                'userRules': [
                    {
                        'ipRule': 'string',
                        'ruleDesc': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    WorkSpaces.Client.exceptions.AccessDeniedException
    
    """
    pass

def describe_tags(ResourceId=None):
    """
    Describes the specified tags for the specified WorkSpaces resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_tags(
        ResourceId='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, and IP access control groups.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TagList': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
TagList (list) --The tags.

(dict) --Describes a tag.

Key (string) --The key of the tag.

Value (string) --The value of the tag.










Exceptions

WorkSpaces.Client.exceptions.ResourceNotFoundException


    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_workspace_bundles(BundleIds=None, Owner=None, NextToken=None):
    """
    Retrieves a list that describes the available WorkSpace bundles.
    You can filter the results using either bundle ID or owner, but not both.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_workspace_bundles(
        BundleIds=[
            'string',
        ],
        Owner='string',
        NextToken='string'
    )
    
    
    :type BundleIds: list
    :param BundleIds: The identifiers of the bundles. You cannot combine this parameter with any other filter.\n\n(string) --\n\n

    :type Owner: string
    :param Owner: The owner of the bundles. You cannot combine this parameter with any other filter.\nSpecify AMAZON to describe the bundles provided by AWS or null to describe the bundles that belong to your account.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'Bundles': [
        {
            'BundleId': 'string',
            'Name': 'string',
            'Owner': 'string',
            'Description': 'string',
            'ImageId': 'string',
            'RootStorage': {
                'Capacity': 'string'
            },
            'UserStorage': {
                'Capacity': 'string'
            },
            'ComputeType': {
                'Name': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
            },
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Bundles (list) --
Information about the bundles.

(dict) --
Describes a WorkSpace bundle.

BundleId (string) --
The bundle identifier.

Name (string) --
The name of the bundle.

Owner (string) --
The owner of the bundle. This is the account identifier of the owner, or AMAZON if the bundle is provided by AWS.

Description (string) --
A description.

ImageId (string) --
The image identifier of the bundle.

RootStorage (dict) --
The size of the root volume.

Capacity (string) --
The size of the root volume.



UserStorage (dict) --
The size of the user storage.

Capacity (string) --
The size of the user storage.



ComputeType (dict) --
The compute type. For more information, see Amazon WorkSpaces Bundles .

Name (string) --
The compute type.



LastUpdatedTime (datetime) --
The last time that the bundle was updated.





NextToken (string) --
The token to use to retrieve the next set of results, or null if there are no more results available. This token is valid for one day and must be used within that time frame.







Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException


    :return: {
        'Bundles': [
            {
                'BundleId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'Description': 'string',
                'ImageId': 'string',
                'RootStorage': {
                    'Capacity': 'string'
                },
                'UserStorage': {
                    'Capacity': 'string'
                },
                'ComputeType': {
                    'Name': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                },
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    
    """
    pass

def describe_workspace_directories(DirectoryIds=None, Limit=None, NextToken=None):
    """
    Describes the available directories that are registered with Amazon WorkSpaces.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_workspace_directories(
        DirectoryIds=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type DirectoryIds: list
    :param DirectoryIds: The identifiers of the directories. If the value is null, all directories are retrieved.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of directories to return.

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Directories': [
        {
            'DirectoryId': 'string',
            'Alias': 'string',
            'DirectoryName': 'string',
            'RegistrationCode': 'string',
            'SubnetIds': [
                'string',
            ],
            'DnsIpAddresses': [
                'string',
            ],
            'CustomerUserName': 'string',
            'IamRoleId': 'string',
            'DirectoryType': 'SIMPLE_AD'|'AD_CONNECTOR',
            'WorkspaceSecurityGroupId': 'string',
            'State': 'REGISTERING'|'REGISTERED'|'DEREGISTERING'|'DEREGISTERED'|'ERROR',
            'WorkspaceCreationProperties': {
                'EnableWorkDocs': True|False,
                'EnableInternetAccess': True|False,
                'DefaultOu': 'string',
                'CustomSecurityGroupId': 'string',
                'UserEnabledAsLocalAdministrator': True|False,
                'EnableMaintenanceMode': True|False
            },
            'ipGroupIds': [
                'string',
            ],
            'WorkspaceAccessProperties': {
                'DeviceTypeWindows': 'ALLOW'|'DENY',
                'DeviceTypeOsx': 'ALLOW'|'DENY',
                'DeviceTypeWeb': 'ALLOW'|'DENY',
                'DeviceTypeIos': 'ALLOW'|'DENY',
                'DeviceTypeAndroid': 'ALLOW'|'DENY',
                'DeviceTypeChromeOs': 'ALLOW'|'DENY',
                'DeviceTypeZeroClient': 'ALLOW'|'DENY'
            },
            'Tenancy': 'DEDICATED'|'SHARED',
            'SelfservicePermissions': {
                'RestartWorkspace': 'ENABLED'|'DISABLED',
                'IncreaseVolumeSize': 'ENABLED'|'DISABLED',
                'ChangeComputeType': 'ENABLED'|'DISABLED',
                'SwitchRunningMode': 'ENABLED'|'DISABLED',
                'RebuildWorkspace': 'ENABLED'|'DISABLED'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Directories (list) --
Information about the directories.

(dict) --
Describes a directory that is used with Amazon WorkSpaces.

DirectoryId (string) --
The directory identifier.

Alias (string) --
The directory alias.

DirectoryName (string) --
The name of the directory.

RegistrationCode (string) --
The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.

SubnetIds (list) --
The identifiers of the subnets used with the directory.

(string) --


DnsIpAddresses (list) --
The IP addresses of the DNS servers for the directory.

(string) --


CustomerUserName (string) --
The user name for the service account.

IamRoleId (string) --
The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.

DirectoryType (string) --
The directory type.

WorkspaceSecurityGroupId (string) --
The identifier of the security group that is assigned to new WorkSpaces.

State (string) --
The state of the directory\'s registration with Amazon WorkSpaces.

WorkspaceCreationProperties (dict) --
The default creation properties for all WorkSpaces in the directory.

EnableWorkDocs (boolean) --
Specifies whether the directory is enabled for Amazon WorkDocs.

EnableInternetAccess (boolean) --
Specifies whether to automatically assign an Elastic public IP address to WorkSpaces in this directory by default. If enabled, the Elastic public IP address allows outbound internet access from your WorkSpaces when you\xe2\x80\x99re using an internet gateway in the Amazon VPC in which your WorkSpaces are located. If you\'re using a Network Address Translation (NAT) gateway for outbound internet access from your VPC, or if your WorkSpaces are in public subnets and you manually assign them Elastic IP addresses, you should disable this setting. This setting applies to new WorkSpaces that you launch or to existing WorkSpaces that you rebuild. For more information, see Configure a VPC for Amazon WorkSpaces .

DefaultOu (string) --
The organizational unit (OU) in the directory for the WorkSpace machine accounts.

CustomSecurityGroupId (string) --
The identifier of any security groups to apply to WorkSpaces when they are created.

UserEnabledAsLocalAdministrator (boolean) --
Specifies whether WorkSpace users are local administrators on their WorkSpaces.

EnableMaintenanceMode (boolean) --
Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see WorkSpace Maintenance .



ipGroupIds (list) --
The identifiers of the IP access control groups associated with the directory.

(string) --


WorkspaceAccessProperties (dict) --
The devices and operating systems that users can use to access WorkSpaces.

DeviceTypeWindows (string) --
Indicates whether users can use Windows clients to access their WorkSpaces. To restrict WorkSpaces access to trusted devices (also known as managed devices) with valid certificates, specify a value of TRUST . For more information, see Restrict WorkSpaces Access to Trusted Devices .

DeviceTypeOsx (string) --
Indicates whether users can use macOS clients to access their WorkSpaces. To restrict WorkSpaces access to trusted devices (also known as managed devices) with valid certificates, specify a value of TRUST . For more information, see Restrict WorkSpaces Access to Trusted Devices .

DeviceTypeWeb (string) --
Indicates whether users can access their WorkSpaces through a web browser.

DeviceTypeIos (string) --
Indicates whether users can use iOS devices to access their WorkSpaces.

DeviceTypeAndroid (string) --
Indicates whether users can use Android devices to access their WorkSpaces.

DeviceTypeChromeOs (string) --
Indicates whether users can use Chromebooks to access their WorkSpaces.

DeviceTypeZeroClient (string) --
Indicates whether users can use zero client devices to access their WorkSpaces.



Tenancy (string) --
Specifies whether the directory is dedicated or shared. To use Bring Your Own License (BYOL), this value must be set to DEDICATED . For more information, see Bring Your Own Windows Desktop Images .

SelfservicePermissions (dict) --
The default self-service permissions for WorkSpaces in the directory.

RestartWorkspace (string) --
Specifies whether users can restart their WorkSpace.

IncreaseVolumeSize (string) --
Specifies whether users can increase the volume size of the drives on their WorkSpace.

ChangeComputeType (string) --
Specifies whether users can change the compute type (bundle) for their WorkSpace.

SwitchRunningMode (string) --
Specifies whether users can switch the running mode of their WorkSpace.

RebuildWorkspace (string) --
Specifies whether users can rebuild the operating system of a WorkSpace to its original state.







NextToken (string) --
The token to use to retrieve the next set of results, or null if no more results are available.







Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException


    :return: {
        'Directories': [
            {
                'DirectoryId': 'string',
                'Alias': 'string',
                'DirectoryName': 'string',
                'RegistrationCode': 'string',
                'SubnetIds': [
                    'string',
                ],
                'DnsIpAddresses': [
                    'string',
                ],
                'CustomerUserName': 'string',
                'IamRoleId': 'string',
                'DirectoryType': 'SIMPLE_AD'|'AD_CONNECTOR',
                'WorkspaceSecurityGroupId': 'string',
                'State': 'REGISTERING'|'REGISTERED'|'DEREGISTERING'|'DEREGISTERED'|'ERROR',
                'WorkspaceCreationProperties': {
                    'EnableWorkDocs': True|False,
                    'EnableInternetAccess': True|False,
                    'DefaultOu': 'string',
                    'CustomSecurityGroupId': 'string',
                    'UserEnabledAsLocalAdministrator': True|False,
                    'EnableMaintenanceMode': True|False
                },
                'ipGroupIds': [
                    'string',
                ],
                'WorkspaceAccessProperties': {
                    'DeviceTypeWindows': 'ALLOW'|'DENY',
                    'DeviceTypeOsx': 'ALLOW'|'DENY',
                    'DeviceTypeWeb': 'ALLOW'|'DENY',
                    'DeviceTypeIos': 'ALLOW'|'DENY',
                    'DeviceTypeAndroid': 'ALLOW'|'DENY',
                    'DeviceTypeChromeOs': 'ALLOW'|'DENY',
                    'DeviceTypeZeroClient': 'ALLOW'|'DENY'
                },
                'Tenancy': 'DEDICATED'|'SHARED',
                'SelfservicePermissions': {
                    'RestartWorkspace': 'ENABLED'|'DISABLED',
                    'IncreaseVolumeSize': 'ENABLED'|'DISABLED',
                    'ChangeComputeType': 'ENABLED'|'DISABLED',
                    'SwitchRunningMode': 'ENABLED'|'DISABLED',
                    'RebuildWorkspace': 'ENABLED'|'DISABLED'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_workspace_images(ImageIds=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list that describes one or more specified images, if the image identifiers are provided. Otherwise, all images in the account are described.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_workspace_images(
        ImageIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ImageIds: list
    :param ImageIds: The identifier of the image.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Images': [
        {
            'ImageId': 'string',
            'Name': 'string',
            'Description': 'string',
            'OperatingSystem': {
                'Type': 'WINDOWS'|'LINUX'
            },
            'State': 'AVAILABLE'|'PENDING'|'ERROR',
            'RequiredTenancy': 'DEFAULT'|'DEDICATED',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Images (list) --
Information about the images.

(dict) --
Describes a WorkSpace image.

ImageId (string) --
The identifier of the image.

Name (string) --
The name of the image.

Description (string) --
The description of the image.

OperatingSystem (dict) --
The operating system that the image is running.

Type (string) --
The operating system.



State (string) --
The status of the image.

RequiredTenancy (string) --
Specifies whether the image is running on dedicated hardware. When Bring Your Own License (BYOL) is enabled, this value is set to DEDICATED . For more information, see Bring Your Own Windows Desktop Images .

ErrorCode (string) --
The error code that is returned for the image.

ErrorMessage (string) --
The text of the error message that is returned for the image.





NextToken (string) --
The token to use to retrieve the next set of results, or null if no more results are available.







Exceptions

WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {
        'Images': [
            {
                'ImageId': 'string',
                'Name': 'string',
                'Description': 'string',
                'OperatingSystem': {
                    'Type': 'WINDOWS'|'LINUX'
                },
                'State': 'AVAILABLE'|'PENDING'|'ERROR',
                'RequiredTenancy': 'DEFAULT'|'DEDICATED',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.AccessDeniedException
    
    """
    pass

def describe_workspace_snapshots(WorkspaceId=None):
    """
    Describes the snapshots for the specified WorkSpace.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_workspace_snapshots(
        WorkspaceId='string'
    )
    
    
    :type WorkspaceId: string
    :param WorkspaceId: [REQUIRED]\nThe identifier of the WorkSpace.\n

    :rtype: dict
ReturnsResponse Syntax{
    'RebuildSnapshots': [
        {
            'SnapshotTime': datetime(2015, 1, 1)
        },
    ],
    'RestoreSnapshots': [
        {
            'SnapshotTime': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --
RebuildSnapshots (list) --Information about the snapshots that can be used to rebuild a WorkSpace. These snapshots include the user volume.

(dict) --Describes a snapshot.

SnapshotTime (datetime) --The time when the snapshot was created.





RestoreSnapshots (list) --Information about the snapshots that can be used to restore a WorkSpace. These snapshots include both the root volume and the user volume.

(dict) --Describes a snapshot.

SnapshotTime (datetime) --The time when the snapshot was created.










Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {
        'RebuildSnapshots': [
            {
                'SnapshotTime': datetime(2015, 1, 1)
            },
        ],
        'RestoreSnapshots': [
            {
                'SnapshotTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def describe_workspaces(WorkspaceIds=None, DirectoryId=None, UserName=None, BundleId=None, Limit=None, NextToken=None):
    """
    Describes the specified WorkSpaces.
    You can filter the results by using the bundle identifier, directory identifier, or owner, but you can specify only one filter at a time.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_workspaces(
        WorkspaceIds=[
            'string',
        ],
        DirectoryId='string',
        UserName='string',
        BundleId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type WorkspaceIds: list
    :param WorkspaceIds: The identifiers of the WorkSpaces. You cannot combine this parameter with any other filter.\nBecause the CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call DescribeWorkspaces with this identifier, no information is returned.\n\n(string) --\n\n

    :type DirectoryId: string
    :param DirectoryId: The identifier of the directory. In addition, you can optionally specify a specific directory user (see UserName ). You cannot combine this parameter with any other filter.

    :type UserName: string
    :param UserName: The name of the directory user. You must specify this parameter with DirectoryId .

    :type BundleId: string
    :param BundleId: The identifier of the bundle. All WorkSpaces that are created from this bundle are retrieved. You cannot combine this parameter with any other filter.

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Workspaces': [
        {
            'WorkspaceId': 'string',
            'DirectoryId': 'string',
            'UserName': 'string',
            'IpAddress': 'string',
            'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'RESTORING'|'MAINTENANCE'|'ADMIN_MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
            'BundleId': 'string',
            'SubnetId': 'string',
            'ErrorMessage': 'string',
            'ErrorCode': 'string',
            'ComputerName': 'string',
            'VolumeEncryptionKey': 'string',
            'UserVolumeEncryptionEnabled': True|False,
            'RootVolumeEncryptionEnabled': True|False,
            'WorkspaceProperties': {
                'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                'RunningModeAutoStopTimeoutInMinutes': 123,
                'RootVolumeSizeGib': 123,
                'UserVolumeSizeGib': 123,
                'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
            },
            'ModificationStates': [
                {
                    'Resource': 'ROOT_VOLUME'|'USER_VOLUME'|'COMPUTE_TYPE',
                    'State': 'UPDATE_INITIATED'|'UPDATE_IN_PROGRESS'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Workspaces (list) --
Information about the WorkSpaces.
Because  CreateWorkspaces is an asynchronous operation, some of the returned information could be incomplete.

(dict) --
Describes a WorkSpace.

WorkspaceId (string) --
The identifier of the WorkSpace.

DirectoryId (string) --
The identifier of the AWS Directory Service directory for the WorkSpace.

UserName (string) --
The user for the WorkSpace.

IpAddress (string) --
The IP address of the WorkSpace.

State (string) --
The operational state of the WorkSpace.

BundleId (string) --
The identifier of the bundle used to create the WorkSpace.

SubnetId (string) --
The identifier of the subnet for the WorkSpace.

ErrorMessage (string) --
The text of the error message that is returned if the WorkSpace cannot be created.

ErrorCode (string) --
The error code that is returned if the WorkSpace cannot be created.

ComputerName (string) --
The name of the WorkSpace, as seen by the operating system.

VolumeEncryptionKey (string) --
The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.

UserVolumeEncryptionEnabled (boolean) --
Indicates whether the data stored on the user volume is encrypted.

RootVolumeEncryptionEnabled (boolean) --
Indicates whether the data stored on the root volume is encrypted.

WorkspaceProperties (dict) --
The properties of the WorkSpace.

RunningMode (string) --
The running mode. For more information, see Manage the WorkSpace Running Mode .

RunningModeAutoStopTimeoutInMinutes (integer) --
The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.

RootVolumeSizeGib (integer) --
The size of the root volume.

UserVolumeSizeGib (integer) --
The size of the user storage.

ComputeTypeName (string) --
The compute type. For more information, see Amazon WorkSpaces Bundles .



ModificationStates (list) --
The modification states of the WorkSpace.

(dict) --
Describes a WorkSpace modification.

Resource (string) --
The resource.

State (string) --
The modification state.









NextToken (string) --
The token to use to retrieve the next set of results, or null if no more results are available.







Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceUnavailableException


    :return: {
        'Workspaces': [
            {
                'WorkspaceId': 'string',
                'DirectoryId': 'string',
                'UserName': 'string',
                'IpAddress': 'string',
                'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'RESTORING'|'MAINTENANCE'|'ADMIN_MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
                'BundleId': 'string',
                'SubnetId': 'string',
                'ErrorMessage': 'string',
                'ErrorCode': 'string',
                'ComputerName': 'string',
                'VolumeEncryptionKey': 'string',
                'UserVolumeEncryptionEnabled': True|False,
                'RootVolumeEncryptionEnabled': True|False,
                'WorkspaceProperties': {
                    'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                    'RunningModeAutoStopTimeoutInMinutes': 123,
                    'RootVolumeSizeGib': 123,
                    'UserVolumeSizeGib': 123,
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                },
                'ModificationStates': [
                    {
                        'Resource': 'ROOT_VOLUME'|'USER_VOLUME'|'COMPUTE_TYPE',
                        'State': 'UPDATE_INITIATED'|'UPDATE_IN_PROGRESS'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    WorkSpaces.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def describe_workspaces_connection_status(WorkspaceIds=None, NextToken=None):
    """
    Describes the connection status of the specified WorkSpaces.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_workspaces_connection_status(
        WorkspaceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type WorkspaceIds: list
    :param WorkspaceIds: The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'WorkspacesConnectionStatus': [
        {
            'WorkspaceId': 'string',
            'ConnectionState': 'CONNECTED'|'DISCONNECTED'|'UNKNOWN',
            'ConnectionStateCheckTimestamp': datetime(2015, 1, 1),
            'LastKnownUserConnectionTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

WorkspacesConnectionStatus (list) --
Information about the connection status of the WorkSpace.

(dict) --
Describes the connection status of a WorkSpace.

WorkspaceId (string) --
The identifier of the WorkSpace.

ConnectionState (string) --
The connection state of the WorkSpace. The connection state is unknown if the WorkSpace is stopped.

ConnectionStateCheckTimestamp (datetime) --
The timestamp of the connection status check.

LastKnownUserConnectionTimestamp (datetime) --
The timestamp of the last known user connection.





NextToken (string) --
The token to use to retrieve the next set of results, or null if no more results are available.







Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException


    :return: {
        'WorkspacesConnectionStatus': [
            {
                'WorkspaceId': 'string',
                'ConnectionState': 'CONNECTED'|'DISCONNECTED'|'UNKNOWN',
                'ConnectionStateCheckTimestamp': datetime(2015, 1, 1),
                'LastKnownUserConnectionTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    
    """
    pass

def disassociate_ip_groups(DirectoryId=None, GroupIds=None):
    """
    Disassociates the specified IP access control group from the specified directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_ip_groups(
        DirectoryId='string',
        GroupIds=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory.\n

    :type GroupIds: list
    :param GroupIds: [REQUIRED]\nThe identifiers of one or more IP access control groups.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def import_workspace_image(Ec2ImageId=None, IngestionProcess=None, ImageName=None, ImageDescription=None, Tags=None):
    """
    Imports the specified Windows 7 or Windows 10 Bring Your Own License (BYOL) image into Amazon WorkSpaces. The image must be an already licensed EC2 image that is in your AWS account, and you must own the image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.import_workspace_image(
        Ec2ImageId='string',
        IngestionProcess='BYOL_REGULAR'|'BYOL_GRAPHICS'|'BYOL_GRAPHICSPRO',
        ImageName='string',
        ImageDescription='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Ec2ImageId: string
    :param Ec2ImageId: [REQUIRED]\nThe identifier of the EC2 image.\n

    :type IngestionProcess: string
    :param IngestionProcess: [REQUIRED]\nThe ingestion process to be used when importing the image.\n

    :type ImageName: string
    :param ImageName: [REQUIRED]\nThe name of the WorkSpace image.\n

    :type ImageDescription: string
    :param ImageDescription: [REQUIRED]\nThe description of the WorkSpace image.\n

    :type Tags: list
    :param Tags: The tags. Each WorkSpaces resource can have a maximum of 50 tags.\n\n(dict) --Describes a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ImageId': 'string'
}


Response Structure

(dict) --

ImageId (string) --
The identifier of the WorkSpace image.







Exceptions

WorkSpaces.Client.exceptions.ResourceLimitExceededException
WorkSpaces.Client.exceptions.ResourceAlreadyExistsException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.OperationNotSupportedException
WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.InvalidParameterValuesException


    :return: {
        'ImageId': 'string'
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.ResourceLimitExceededException
    WorkSpaces.Client.exceptions.ResourceAlreadyExistsException
    WorkSpaces.Client.exceptions.ResourceNotFoundException
    WorkSpaces.Client.exceptions.OperationNotSupportedException
    WorkSpaces.Client.exceptions.AccessDeniedException
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    
    """
    pass

def list_available_management_cidr_ranges(ManagementCidrRangeConstraint=None, MaxResults=None, NextToken=None):
    """
    Retrieves a list of IP address ranges, specified as IPv4 CIDR blocks, that you can use for the network management interface when you enable Bring Your Own License (BYOL).
    The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_available_management_cidr_ranges(
        ManagementCidrRangeConstraint='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ManagementCidrRangeConstraint: string
    :param ManagementCidrRangeConstraint: [REQUIRED]\nThe IP address range to search. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block).\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return.

    :type NextToken: string
    :param NextToken: If you received a NextToken from a previous call that was paginated, provide this token to receive the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ManagementCidrRanges': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ManagementCidrRanges (list) --
The list of available IP address ranges, specified as IPv4 CIDR blocks.

(string) --


NextToken (string) --
The token to use to retrieve the next set of results, or null if no more results are available.







Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {
        'ManagementCidrRanges': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def migrate_workspace(SourceWorkspaceId=None, BundleId=None):
    """
    Migrates a WorkSpace from one operating system or bundle type to another, while retaining the data on the user volume.
    The migration process recreates the WorkSpace by using a new root volume from the target bundle image and the user volume from the last available snapshot of the original WorkSpace. During migration, the original D:\\Users\\%USERNAME% user profile folder is renamed to D:\\Users\\%USERNAME%MMddyyTHHmmss%.NotMigrated . A new D:\\Users\\%USERNAME%\\ folder is generated by the new OS. Certain files in the old user profile are moved to the new user profile.
    For available migration scenarios, details about what happens during migration, and best practices, see Migrate a WorkSpace .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.migrate_workspace(
        SourceWorkspaceId='string',
        BundleId='string'
    )
    
    
    :type SourceWorkspaceId: string
    :param SourceWorkspaceId: [REQUIRED]\nThe identifier of the WorkSpace to migrate from.\n

    :type BundleId: string
    :param BundleId: [REQUIRED]\nThe identifier of the target bundle type to migrate the WorkSpace to.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SourceWorkspaceId': 'string',
    'TargetWorkspaceId': 'string'
}


Response Structure

(dict) --

SourceWorkspaceId (string) --
The original identifier of the WorkSpace that is being migrated.

TargetWorkspaceId (string) --
The new identifier of the WorkSpace that is being migrated. If the migration does not succeed, the target WorkSpace ID will not be used, and the WorkSpace will still have the original WorkSpace ID.







Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.OperationNotSupportedException
WorkSpaces.Client.exceptions.OperationInProgressException
WorkSpaces.Client.exceptions.ResourceUnavailableException


    :return: {
        'SourceWorkspaceId': 'string',
        'TargetWorkspaceId': 'string'
    }
    
    
    :returns: 
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    WorkSpaces.Client.exceptions.ResourceNotFoundException
    WorkSpaces.Client.exceptions.AccessDeniedException
    WorkSpaces.Client.exceptions.OperationNotSupportedException
    WorkSpaces.Client.exceptions.OperationInProgressException
    WorkSpaces.Client.exceptions.ResourceUnavailableException
    
    """
    pass

def modify_account(DedicatedTenancySupport=None, DedicatedTenancyManagementCidrRange=None):
    """
    Modifies the configuration of Bring Your Own License (BYOL) for the specified account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_account(
        DedicatedTenancySupport='ENABLED',
        DedicatedTenancyManagementCidrRange='string'
    )
    
    
    :type DedicatedTenancySupport: string
    :param DedicatedTenancySupport: The status of BYOL.

    :type DedicatedTenancyManagementCidrRange: string
    :param DedicatedTenancyManagementCidrRange: The IP address range, specified as an IPv4 CIDR block, for the management network interface. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block). The CIDR block size must be /16 (for example, 203.0.113.25/16). It must also be specified as available by the ListAvailableManagementCidrRanges operation.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.ResourceUnavailableException
WorkSpaces.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def modify_client_properties(ResourceId=None, ClientProperties=None):
    """
    Modifies the properties of the specified Amazon WorkSpaces clients.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_client_properties(
        ResourceId='string',
        ClientProperties={
            'ReconnectEnabled': 'ENABLED'|'DISABLED'
        }
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe resource identifiers, in the form of directory IDs.\n

    :type ClientProperties: dict
    :param ClientProperties: [REQUIRED]\nInformation about the Amazon WorkSpaces client.\n\nReconnectEnabled (string) --Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When enabled, users can choose to reconnect to their WorkSpaces without re-entering their credentials.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def modify_selfservice_permissions(ResourceId=None, SelfservicePermissions=None):
    """
    Modifies the self-service WorkSpace management capabilities for your users. For more information, see Enable Self-Service WorkSpace Management Capabilities for Your Users .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_selfservice_permissions(
        ResourceId='string',
        SelfservicePermissions={
            'RestartWorkspace': 'ENABLED'|'DISABLED',
            'IncreaseVolumeSize': 'ENABLED'|'DISABLED',
            'ChangeComputeType': 'ENABLED'|'DISABLED',
            'SwitchRunningMode': 'ENABLED'|'DISABLED',
            'RebuildWorkspace': 'ENABLED'|'DISABLED'
        }
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the directory.\n

    :type SelfservicePermissions: dict
    :param SelfservicePermissions: [REQUIRED]\nThe permissions to enable or disable self-service capabilities.\n\nRestartWorkspace (string) --Specifies whether users can restart their WorkSpace.\n\nIncreaseVolumeSize (string) --Specifies whether users can increase the volume size of the drives on their WorkSpace.\n\nChangeComputeType (string) --Specifies whether users can change the compute type (bundle) for their WorkSpace.\n\nSwitchRunningMode (string) --Specifies whether users can switch the running mode of their WorkSpace.\n\nRebuildWorkspace (string) --Specifies whether users can rebuild the operating system of a WorkSpace to its original state.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def modify_workspace_access_properties(ResourceId=None, WorkspaceAccessProperties=None):
    """
    Specifies which devices and operating systems users can use to access their WorkSpaces. For more information, see Control Device Access .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_workspace_access_properties(
        ResourceId='string',
        WorkspaceAccessProperties={
            'DeviceTypeWindows': 'ALLOW'|'DENY',
            'DeviceTypeOsx': 'ALLOW'|'DENY',
            'DeviceTypeWeb': 'ALLOW'|'DENY',
            'DeviceTypeIos': 'ALLOW'|'DENY',
            'DeviceTypeAndroid': 'ALLOW'|'DENY',
            'DeviceTypeChromeOs': 'ALLOW'|'DENY',
            'DeviceTypeZeroClient': 'ALLOW'|'DENY'
        }
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the directory.\n

    :type WorkspaceAccessProperties: dict
    :param WorkspaceAccessProperties: [REQUIRED]\nThe device types and operating systems to enable or disable for access.\n\nDeviceTypeWindows (string) --Indicates whether users can use Windows clients to access their WorkSpaces. To restrict WorkSpaces access to trusted devices (also known as managed devices) with valid certificates, specify a value of TRUST . For more information, see Restrict WorkSpaces Access to Trusted Devices .\n\nDeviceTypeOsx (string) --Indicates whether users can use macOS clients to access their WorkSpaces. To restrict WorkSpaces access to trusted devices (also known as managed devices) with valid certificates, specify a value of TRUST . For more information, see Restrict WorkSpaces Access to Trusted Devices .\n\nDeviceTypeWeb (string) --Indicates whether users can access their WorkSpaces through a web browser.\n\nDeviceTypeIos (string) --Indicates whether users can use iOS devices to access their WorkSpaces.\n\nDeviceTypeAndroid (string) --Indicates whether users can use Android devices to access their WorkSpaces.\n\nDeviceTypeChromeOs (string) --Indicates whether users can use Chromebooks to access their WorkSpaces.\n\nDeviceTypeZeroClient (string) --Indicates whether users can use zero client devices to access their WorkSpaces.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def modify_workspace_creation_properties(ResourceId=None, WorkspaceCreationProperties=None):
    """
    Modify the default properties used to create WorkSpaces.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_workspace_creation_properties(
        ResourceId='string',
        WorkspaceCreationProperties={
            'EnableInternetAccess': True|False,
            'DefaultOu': 'string',
            'CustomSecurityGroupId': 'string',
            'UserEnabledAsLocalAdministrator': True|False,
            'EnableMaintenanceMode': True|False
        }
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the directory.\n

    :type WorkspaceCreationProperties: dict
    :param WorkspaceCreationProperties: [REQUIRED]\nThe default properties for creating WorkSpaces.\n\nEnableInternetAccess (boolean) --Indicates whether internet access is enabled for your WorkSpaces.\n\nDefaultOu (string) --The default organizational unit (OU) for your WorkSpace directories.\n\nCustomSecurityGroupId (string) --The identifier of your custom security group.\n\nUserEnabledAsLocalAdministrator (boolean) --Indicates whether users are local administrators of their WorkSpaces.\n\nEnableMaintenanceMode (boolean) --Indicates whether maintenance mode is enabled for your WorkSpaces. For more information, see WorkSpace Maintenance .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def modify_workspace_properties(WorkspaceId=None, WorkspaceProperties=None):
    """
    Modifies the specified WorkSpace properties.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_workspace_properties(
        WorkspaceId='string',
        WorkspaceProperties={
            'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
            'RunningModeAutoStopTimeoutInMinutes': 123,
            'RootVolumeSizeGib': 123,
            'UserVolumeSizeGib': 123,
            'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
        }
    )
    
    
    :type WorkspaceId: string
    :param WorkspaceId: [REQUIRED]\nThe identifier of the WorkSpace.\n

    :type WorkspaceProperties: dict
    :param WorkspaceProperties: [REQUIRED]\nThe properties of the WorkSpace.\n\nRunningMode (string) --The running mode. For more information, see Manage the WorkSpace Running Mode .\n\nRunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.\n\nRootVolumeSizeGib (integer) --The size of the root volume.\n\nUserVolumeSizeGib (integer) --The size of the user storage.\n\nComputeTypeName (string) --The compute type. For more information, see Amazon WorkSpaces Bundles .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.OperationInProgressException
WorkSpaces.Client.exceptions.UnsupportedWorkspaceConfigurationException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.ResourceUnavailableException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def modify_workspace_state(WorkspaceId=None, WorkspaceState=None):
    """
    Sets the state of the specified WorkSpace.
    To maintain a WorkSpace without being interrupted, set the WorkSpace state to ADMIN_MAINTENANCE . WorkSpaces in this state do not respond to requests to reboot, stop, start, rebuild, or restore. An AutoStop WorkSpace in this state is not stopped. Users cannot log into a WorkSpace in the ADMIN_MAINTENANCE state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_workspace_state(
        WorkspaceId='string',
        WorkspaceState='AVAILABLE'|'ADMIN_MAINTENANCE'
    )
    
    
    :type WorkspaceId: string
    :param WorkspaceId: [REQUIRED]\nThe identifier of the WorkSpace.\n

    :type WorkspaceState: string
    :param WorkspaceState: [REQUIRED]\nThe WorkSpace state.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reboot_workspaces(RebootWorkspaceRequests=None):
    """
    Reboots the specified WorkSpaces.
    You cannot reboot a WorkSpace unless its state is AVAILABLE or UNHEALTHY .
    This operation is asynchronous and returns before the WorkSpaces have rebooted.
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_workspaces(
        RebootWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type RebootWorkspaceRequests: list
    :param RebootWorkspaceRequests: [REQUIRED]\nThe WorkSpaces to reboot. You can specify up to 25 WorkSpaces.\n\n(dict) --Describes the information used to reboot a WorkSpace.\n\nWorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedRequests': [
        {
            'WorkspaceId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
FailedRequests (list) --Information about the WorkSpaces that could not be rebooted.

(dict) --Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

WorkspaceId (string) --The identifier of the WorkSpace.

ErrorCode (string) --The error code that is returned if the WorkSpace cannot be rebooted.

ErrorMessage (string) --The text of the error message that is returned if the WorkSpace cannot be rebooted.











    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def rebuild_workspaces(RebuildWorkspaceRequests=None):
    """
    Rebuilds the specified WorkSpace.
    You cannot rebuild a WorkSpace unless its state is AVAILABLE , ERROR , UNHEALTHY , or STOPPED .
    Rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see Rebuild a WorkSpace .
    This operation is asynchronous and returns before the WorkSpaces have been completely rebuilt.
    See also: AWS API Documentation
    
    
    :example: response = client.rebuild_workspaces(
        RebuildWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type RebuildWorkspaceRequests: list
    :param RebuildWorkspaceRequests: [REQUIRED]\nThe WorkSpace to rebuild. You can specify a single WorkSpace.\n\n(dict) --Describes the information used to rebuild a WorkSpace.\n\nWorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedRequests': [
        {
            'WorkspaceId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
FailedRequests (list) --Information about the WorkSpace that could not be rebuilt.

(dict) --Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

WorkspaceId (string) --The identifier of the WorkSpace.

ErrorCode (string) --The error code that is returned if the WorkSpace cannot be rebooted.

ErrorMessage (string) --The text of the error message that is returned if the WorkSpace cannot be rebooted.











    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def register_workspace_directory(DirectoryId=None, SubnetIds=None, EnableWorkDocs=None, EnableSelfService=None, Tenancy=None, Tags=None):
    """
    Registers the specified directory. This operation is asynchronous and returns before the WorkSpace directory is registered. If this is the first time you are registering a directory, you will need to create the workspaces_DefaultRole role before you can register a directory. For more information, see Creating the workspaces_DefaultRole Role .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_workspace_directory(
        DirectoryId='string',
        SubnetIds=[
            'string',
        ],
        EnableWorkDocs=True|False,
        EnableSelfService=True|False,
        Tenancy='DEDICATED'|'SHARED',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory. You cannot register a directory if it does not have a status of Active. If the directory does not have a status of Active, you will receive an InvalidResourceStateException error. If you have already registered the maximum number of directories that you can register with Amazon WorkSpaces, you will receive a ResourceLimitExceededException error. Deregister directories that you are not using for WorkSpaces, and try again.\n

    :type SubnetIds: list
    :param SubnetIds: The identifiers of the subnets for your virtual private cloud (VPC). Make sure that the subnets are in supported Availability Zones. The subnets must also be in separate Availability Zones. If these conditions are not met, you will receive an OperationNotSupportedException error.\n\n(string) --\n\n

    :type EnableWorkDocs: boolean
    :param EnableWorkDocs: [REQUIRED]\nIndicates whether Amazon WorkDocs is enabled or disabled. If you have enabled this parameter and WorkDocs is not available in the Region, you will receive an OperationNotSupportedException error. Set EnableWorkDocs to disabled, and try again.\n

    :type EnableSelfService: boolean
    :param EnableSelfService: Indicates whether self-service capabilities are enabled or disabled.

    :type Tenancy: string
    :param Tenancy: Indicates whether your WorkSpace directory is dedicated or shared. To use Bring Your Own License (BYOL) images, this value must be set to DEDICATED and your AWS account must be enabled for BYOL. If your account has not been enabled for BYOL, you will receive an InvalidParameterValuesException error. For more information about BYOL images, see Bring Your Own Windows Desktop Images .

    :type Tags: list
    :param Tags: The tags associated with the directory.\n\n(dict) --Describes a tag.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) --The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.ResourceLimitExceededException
WorkSpaces.Client.exceptions.AccessDeniedException
WorkSpaces.Client.exceptions.WorkspacesDefaultRoleNotFoundException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.UnsupportedNetworkConfigurationException
WorkSpaces.Client.exceptions.OperationNotSupportedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def restore_workspace(WorkspaceId=None):
    """
    Restores the specified WorkSpace to its last known healthy state.
    You cannot restore a WorkSpace unless its state is AVAILABLE , ERROR , UNHEALTHY , or STOPPED .
    Restoring a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see Restore a WorkSpace .
    This operation is asynchronous and returns before the WorkSpace is completely restored.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_workspace(
        WorkspaceId='string'
    )
    
    
    :type WorkspaceId: string
    :param WorkspaceId: [REQUIRED]\nThe identifier of the WorkSpace.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    WorkSpaces.Client.exceptions.InvalidParameterValuesException
    WorkSpaces.Client.exceptions.ResourceNotFoundException
    WorkSpaces.Client.exceptions.AccessDeniedException
    
    """
    pass

def revoke_ip_rules(GroupId=None, UserRules=None):
    """
    Removes one or more rules from the specified IP access control group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.revoke_ip_rules(
        GroupId='string',
        UserRules=[
            'string',
        ]
    )
    
    
    :type GroupId: string
    :param GroupId: [REQUIRED]\nThe identifier of the group.\n

    :type UserRules: list
    :param UserRules: [REQUIRED]\nThe rules to remove from the group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_workspaces(StartWorkspaceRequests=None):
    """
    Starts the specified WorkSpaces.
    You cannot start a WorkSpace unless it has a running mode of AutoStop and a state of STOPPED .
    See also: AWS API Documentation
    
    
    :example: response = client.start_workspaces(
        StartWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type StartWorkspaceRequests: list
    :param StartWorkspaceRequests: [REQUIRED]\nThe WorkSpaces to start. You can specify up to 25 WorkSpaces.\n\n(dict) --Information used to start a WorkSpace.\n\nWorkspaceId (string) --The identifier of the WorkSpace.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedRequests': [
        {
            'WorkspaceId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
FailedRequests (list) --Information about the WorkSpaces that could not be started.

(dict) --Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

WorkspaceId (string) --The identifier of the WorkSpace.

ErrorCode (string) --The error code that is returned if the WorkSpace cannot be rebooted.

ErrorMessage (string) --The text of the error message that is returned if the WorkSpace cannot be rebooted.











    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def stop_workspaces(StopWorkspaceRequests=None):
    """
    Stops the specified WorkSpaces.
    You cannot stop a WorkSpace unless it has a running mode of AutoStop and a state of AVAILABLE , IMPAIRED , UNHEALTHY , or ERROR .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_workspaces(
        StopWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type StopWorkspaceRequests: list
    :param StopWorkspaceRequests: [REQUIRED]\nThe WorkSpaces to stop. You can specify up to 25 WorkSpaces.\n\n(dict) --Describes the information used to stop a WorkSpace.\n\nWorkspaceId (string) --The identifier of the WorkSpace.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedRequests': [
        {
            'WorkspaceId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
FailedRequests (list) --Information about the WorkSpaces that could not be stopped.

(dict) --Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

WorkspaceId (string) --The identifier of the WorkSpace.

ErrorCode (string) --The error code that is returned if the WorkSpace cannot be rebooted.

ErrorMessage (string) --The text of the error message that is returned if the WorkSpace cannot be rebooted.











    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def terminate_workspaces(TerminateWorkspaceRequests=None):
    """
    Terminates the specified WorkSpaces.
    Terminating a WorkSpace is a permanent action and cannot be undone. The user\'s data is destroyed. If you need to archive any user data, contact Amazon Web Services before terminating the WorkSpace.
    You can terminate a WorkSpace that is in any state except SUSPENDED .
    This operation is asynchronous and returns before the WorkSpaces have been completely terminated.
    See also: AWS API Documentation
    
    
    :example: response = client.terminate_workspaces(
        TerminateWorkspaceRequests=[
            {
                'WorkspaceId': 'string'
            },
        ]
    )
    
    
    :type TerminateWorkspaceRequests: list
    :param TerminateWorkspaceRequests: [REQUIRED]\nThe WorkSpaces to terminate. You can specify up to 25 WorkSpaces.\n\n(dict) --Describes the information used to terminate a WorkSpace.\n\nWorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedRequests': [
        {
            'WorkspaceId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
FailedRequests (list) --Information about the WorkSpaces that could not be terminated.

(dict) --Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

WorkspaceId (string) --The identifier of the WorkSpace.

ErrorCode (string) --The error code that is returned if the WorkSpace cannot be rebooted.

ErrorMessage (string) --The text of the error message that is returned if the WorkSpace cannot be rebooted.











    :return: {
        'FailedRequests': [
            {
                'WorkspaceId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def update_rules_of_ip_group(GroupId=None, UserRules=None):
    """
    Replaces the current rules of the specified IP access control group with the specified rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_rules_of_ip_group(
        GroupId='string',
        UserRules=[
            {
                'ipRule': 'string',
                'ruleDesc': 'string'
            },
        ]
    )
    
    
    :type GroupId: string
    :param GroupId: [REQUIRED]\nThe identifier of the group.\n

    :type UserRules: list
    :param UserRules: [REQUIRED]\nOne or more rules.\n\n(dict) --Describes a rule for an IP access control group.\n\nipRule (string) --The IP address range, in CIDR notation.\n\nruleDesc (string) --The description.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkSpaces.Client.exceptions.InvalidParameterValuesException
WorkSpaces.Client.exceptions.ResourceNotFoundException
WorkSpaces.Client.exceptions.ResourceLimitExceededException
WorkSpaces.Client.exceptions.InvalidResourceStateException
WorkSpaces.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

