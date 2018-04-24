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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def create_tags(ResourceId=None, Tags=None):
    """
    Creates tags for the specified WorkSpace.
    See also: AWS API Documentation
    
    
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
    :param ResourceId: [REQUIRED]
            The ID of the resource.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags. Each resource can have a maximum of 50 tags.
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            

    :rtype: dict
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
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'
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
    :param Workspaces: [REQUIRED]
            Information about the WorkSpaces to create.
            (dict) --Information used to create a WorkSpace.
            DirectoryId (string) -- [REQUIRED]The identifier of the AWS Directory Service directory for the WorkSpace. You can use DescribeWorkspaceDirectories to list the available directories.
            UserName (string) -- [REQUIRED]The username of the user for the WorkSpace. This username must exist in the AWS Directory Service directory for the WorkSpace.
            BundleId (string) -- [REQUIRED]The identifier of the bundle for the WorkSpace. You can use DescribeWorkspaceBundles to list the available bundles.
            VolumeEncryptionKey (string) --The KMS key used to encrypt data stored on your WorkSpace.
            UserVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the user volume is encrypted.
            RootVolumeEncryptionEnabled (boolean) --Indicates whether the data stored on the root volume is encrypted.
            WorkspaceProperties (dict) --The WorkSpace properties.
            RunningMode (string) --The running mode. For more information, see Manage the WorkSpace Running Mode .
            RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
            RootVolumeSizeGib (integer) --The size of the root volume.
            UserVolumeSizeGib (integer) --The size of the user storage.
            ComputeTypeName (string) --The compute type. For more information, see Amazon WorkSpaces Bundles .
            Tags (list) --The tags for the WorkSpace.
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            
            

    :rtype: dict
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
                        'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'
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
                'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
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
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'
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

def delete_tags(ResourceId=None, TagKeys=None):
    """
    Deletes the specified tags from a WorkSpace.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the resource.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tag keys.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_tags(ResourceId=None):
    """
    Describes the tags for the specified WorkSpace.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_tags(
        ResourceId='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the resource.
            

    :rtype: dict
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
    Describes the available WorkSpace bundles.
    You can filter the results using either bundle ID or owner, but not both.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspace_bundles(
        BundleIds=[
            'string',
        ],
        Owner='string',
        NextToken='string'
    )
    
    
    :type BundleIds: list
    :param BundleIds: The IDs of the bundles. This parameter cannot be combined with any other filter.
            (string) --
            

    :type Owner: string
    :param Owner: The owner of the bundles. This parameter cannot be combined with any other filter.
            Specify AMAZON to describe the bundles provided by AWS or null to describe the bundles that belong to your account.
            

    :type NextToken: string
    :param NextToken: The token for the next set of results. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Bundles': [
            {
                'BundleId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'Description': 'string',
                'RootStorage': {
                    'Capacity': 'string'
                },
                'UserStorage': {
                    'Capacity': 'string'
                },
                'ComputeType': {
                    'Name': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_workspace_directories(DirectoryIds=None, NextToken=None):
    """
    Describes the available AWS Directory Service directories that are registered with Amazon WorkSpaces.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspace_directories(
        DirectoryIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type DirectoryIds: list
    :param DirectoryIds: The identifiers of the directories. If the value is null, all directories are retrieved.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token for the next set of results. (You received this token from a previous call.)

    :rtype: dict
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
                    'UserEnabledAsLocalAdministrator': True|False
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_workspaces(WorkspaceIds=None, DirectoryId=None, UserName=None, BundleId=None, Limit=None, NextToken=None):
    """
    Describes the specified WorkSpaces.
    You can filter the results using bundle ID, directory ID, or owner, but you can specify only one filter at a time.
    See also: AWS API Documentation
    
    
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
    :param WorkspaceIds: The IDs of the WorkSpaces. This parameter cannot be combined with any other filter.
            Because the CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call DescribeWorkspaces with this identifier, no information is returned.
            (string) --
            

    :type DirectoryId: string
    :param DirectoryId: The ID of the directory. In addition, you can optionally specify a specific directory user (see UserName ). This parameter cannot be combined with any other filter.

    :type UserName: string
    :param UserName: The name of the directory user. You must specify this parameter with DirectoryId .

    :type BundleId: string
    :param BundleId: The ID of the bundle. All WorkSpaces that are created from this bundle are retrieved. This parameter cannot be combined with any other filter.

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :type NextToken: string
    :param NextToken: The token for the next set of results. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Workspaces': [
            {
                'WorkspaceId': 'string',
                'DirectoryId': 'string',
                'UserName': 'string',
                'IpAddress': 'string',
                'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
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
                    'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'
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
    
    
    """
    pass

def describe_workspaces_connection_status(WorkspaceIds=None, NextToken=None):
    """
    Describes the connection status of the specified WorkSpaces.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspaces_connection_status(
        WorkspaceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type WorkspaceIds: list
    :param WorkspaceIds: The identifiers of the WorkSpaces.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token for the next set of results. (You received this token from a previous call.)

    :rtype: dict
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

def modify_workspace_properties(WorkspaceId=None, WorkspaceProperties=None):
    """
    Modifies the specified WorkSpace properties.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_workspace_properties(
        WorkspaceId='string',
        WorkspaceProperties={
            'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
            'RunningModeAutoStopTimeoutInMinutes': 123,
            'RootVolumeSizeGib': 123,
            'UserVolumeSizeGib': 123,
            'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'
        }
    )
    
    
    :type WorkspaceId: string
    :param WorkspaceId: [REQUIRED]
            The ID of the WorkSpace.
            

    :type WorkspaceProperties: dict
    :param WorkspaceProperties: [REQUIRED]
            The properties of the WorkSpace.
            RunningMode (string) --The running mode. For more information, see Manage the WorkSpace Running Mode .
            RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
            RootVolumeSizeGib (integer) --The size of the root volume.
            UserVolumeSizeGib (integer) --The size of the user storage.
            ComputeTypeName (string) --The compute type. For more information, see Amazon WorkSpaces Bundles .
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reboot_workspaces(RebootWorkspaceRequests=None):
    """
    Reboots the specified WorkSpaces.
    You cannot reboot a WorkSpace unless its state is AVAILABLE , IMPAIRED , or INOPERABLE .
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
    :param RebootWorkspaceRequests: [REQUIRED]
            The WorkSpaces to reboot.
            (dict) --Information used to reboot a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace.
            
            

    :rtype: dict
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
    Rebuilds the specified WorkSpaces.
    You cannot rebuild a WorkSpace unless its state is AVAILABLE or ERROR .
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
    :param RebuildWorkspaceRequests: [REQUIRED]
            The WorkSpaces to rebuild.
            (dict) --Information used to rebuild a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace.
            
            

    :rtype: dict
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
    :param StartWorkspaceRequests: [REQUIRED]
            The WorkSpaces to start.
            (dict) --Information used to start a WorkSpace.
            WorkspaceId (string) --The ID of the WorkSpace.
            
            

    :rtype: dict
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
    :param StopWorkspaceRequests: [REQUIRED]
            The WorkSpaces to stop.
            (dict) --Information used to stop a WorkSpace.
            WorkspaceId (string) --The ID of the WorkSpace.
            
            

    :rtype: dict
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
    Terminating a WorkSpace is a permanent action and cannot be undone. The user's data is destroyed. If you need to archive any user data, contact Amazon Web Services before terminating the WorkSpace.
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
    :param TerminateWorkspaceRequests: [REQUIRED]
            The WorkSpaces to terminate.
            (dict) --Information used to terminate a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace.
            
            

    :rtype: dict
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

