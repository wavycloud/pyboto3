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
    Creates tags for a WorkSpace.
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
            The resource ID of the request.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags of the request.
            (dict) --Describes the tag of the WorkSpace.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_workspaces(Workspaces=None):
    """
    Creates one or more WorkSpaces.
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
                    'RunningModeAutoStopTimeoutInMinutes': 123
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
            An array of structures that specify the WorkSpaces to create.
            (dict) --Contains information about a WorkSpace creation request.
            DirectoryId (string) -- [REQUIRED]The identifier of the AWS Directory Service directory to create the WorkSpace in. You can use the DescribeWorkspaceDirectories operation to obtain a list of the directories that are available.
            UserName (string) -- [REQUIRED]The username that the WorkSpace is assigned to. This username must exist in the AWS Directory Service directory specified by the DirectoryId member.
            BundleId (string) -- [REQUIRED]The identifier of the bundle to create the WorkSpace from. You can use the DescribeWorkspaceBundles operation to obtain a list of the bundles that are available.
            VolumeEncryptionKey (string) --The KMS key used to encrypt data stored on your WorkSpace.
            UserVolumeEncryptionEnabled (boolean) --Specifies whether the data stored on the user volume, or D: drive, is encrypted.
            RootVolumeEncryptionEnabled (boolean) --Specifies whether the data stored on the root volume, or C: drive, is encrypted.
            WorkspaceProperties (dict) --Describes the properties of a WorkSpace.
            RunningMode (string) --The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.
            RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
            Tags (list) --The tags of the WorkSpace request.
            (dict) --Describes the tag of the WorkSpace.
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
                        'RunningModeAutoStopTimeoutInMinutes': 123
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
                'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'STOPPING'|'STOPPED'|'ERROR',
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
                    'RunningModeAutoStopTimeoutInMinutes': 123
                }
            },
        ]
    }
    
    
    """
    pass

def delete_tags(ResourceId=None, TagKeys=None):
    """
    Deletes tags from a WorkSpace.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The resource ID of the request.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tag keys of the request.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_tags(ResourceId=None):
    """
    Describes tags for a WorkSpace.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_tags(
        ResourceId='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The resource ID of the request.
            

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
    Obtains information about the WorkSpace bundles that are available to your account in the specified region.
    You can filter the results with either the BundleIds parameter, or the Owner parameter, but not both.
    This operation supports pagination with the use of the NextToken request and response parameters. If more results are available, the NextToken response member contains a token that you pass in the next call to this operation to retrieve the next set of items.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspace_bundles(
        BundleIds=[
            'string',
        ],
        Owner='string',
        NextToken='string'
    )
    
    
    :type BundleIds: list
    :param BundleIds: An array of strings that contains the identifiers of the bundles to retrieve. This parameter cannot be combined with any other filter parameter.
            (string) --
            

    :type Owner: string
    :param Owner: The owner of the bundles to retrieve. This parameter cannot be combined with any other filter parameter.
            This contains one of the following values:
            null- Retrieves the bundles that belong to the account making the call.
            AMAZON - Retrieves the bundles that are provided by AWS.
            

    :type NextToken: string
    :param NextToken: The NextToken value from a previous call to this operation. Pass null if this is the first call.

    :rtype: dict
    :return: {
        'Bundles': [
            {
                'BundleId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'Description': 'string',
                'UserStorage': {
                    'Capacity': 'string'
                },
                'ComputeType': {
                    'Name': 'VALUE'|'STANDARD'|'PERFORMANCE'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_workspace_directories(DirectoryIds=None, NextToken=None):
    """
    Retrieves information about the AWS Directory Service directories in the region that are registered with Amazon WorkSpaces and are available to your account.
    This operation supports pagination with the use of the NextToken request and response parameters. If more results are available, the NextToken response member contains a token that you pass in the next call to this operation to retrieve the next set of items.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspace_directories(
        DirectoryIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type DirectoryIds: list
    :param DirectoryIds: An array of strings that contains the directory identifiers to retrieve information for. If this member is null, all directories are retrieved.
            (string) --
            

    :type NextToken: string
    :param NextToken: The NextToken value from a previous call to this operation. Pass null if this is the first call.

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
    Obtains information about the specified WorkSpaces.
    Only one of the filter parameters, such as BundleId , DirectoryId , or WorkspaceIds , can be specified at a time.
    This operation supports pagination with the use of the NextToken request and response parameters. If more results are available, the NextToken response member contains a token that you pass in the next call to this operation to retrieve the next set of items.
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
    :param WorkspaceIds: An array of strings that contain the identifiers of the WorkSpaces for which to retrieve information. This parameter cannot be combined with any other filter parameter.
            Because the CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call DescribeWorkspaces with this identifier, no information is returned.
            (string) --
            

    :type DirectoryId: string
    :param DirectoryId: Specifies the directory identifier to which to limit the WorkSpaces. Optionally, you can specify a specific directory user with the UserName parameter. This parameter cannot be combined with any other filter parameter.

    :type UserName: string
    :param UserName: Used with the DirectoryId parameter to specify the directory user for whom to obtain the WorkSpace.

    :type BundleId: string
    :param BundleId: The identifier of a bundle to obtain the WorkSpaces for. All WorkSpaces that are created from this bundle will be retrieved. This parameter cannot be combined with any other filter parameter.

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :type NextToken: string
    :param NextToken: The NextToken value from a previous call to this operation. Pass null if this is the first call.

    :rtype: dict
    :return: {
        'Workspaces': [
            {
                'WorkspaceId': 'string',
                'DirectoryId': 'string',
                'UserName': 'string',
                'IpAddress': 'string',
                'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'STOPPING'|'STOPPED'|'ERROR',
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
                    'RunningModeAutoStopTimeoutInMinutes': 123
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_workspaces_connection_status(WorkspaceIds=None, NextToken=None):
    """
    Describes the connection status of a specified WorkSpace.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workspaces_connection_status(
        WorkspaceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type WorkspaceIds: list
    :param WorkspaceIds: An array of strings that contain the identifiers of the WorkSpaces.
            (string) --
            

    :type NextToken: string
    :param NextToken: The next token of the request.

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
    Modifies the WorkSpace properties, including the running mode and AutoStop time.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_workspace_properties(
        WorkspaceId='string',
        WorkspaceProperties={
            'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
            'RunningModeAutoStopTimeoutInMinutes': 123
        }
    )
    
    
    :type WorkspaceId: string
    :param WorkspaceId: [REQUIRED]
            The ID of the WorkSpace.
            

    :type WorkspaceProperties: dict
    :param WorkspaceProperties: [REQUIRED]
            The WorkSpace properties of the request.
            RunningMode (string) --The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.
            RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reboot_workspaces(RebootWorkspaceRequests=None):
    """
    Reboots the specified WorkSpaces.
    To be able to reboot a WorkSpace, the WorkSpace must have a State of AVAILABLE , IMPAIRED , or INOPERABLE .
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
            An array of structures that specify the WorkSpaces to reboot.
            (dict) --Contains information used with the RebootWorkspaces operation to reboot a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace to reboot.
            
            

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
    Rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. Rebuilding a WorkSpace causes the following to occur:
    To be able to rebuild a WorkSpace, the WorkSpace must have a State of AVAILABLE or ERROR .
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
            An array of structures that specify the WorkSpaces to rebuild.
            (dict) --Contains information used with the RebuildWorkspaces operation to rebuild a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace to rebuild.
            
            

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
    Starts the specified WorkSpaces. The WorkSpaces must have a running mode of AutoStop and a state of STOPPED.
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
            The requests.
            (dict) --Describes the start request.
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
    Stops the specified WorkSpaces. The WorkSpaces must have a running mode of AutoStop and a state of AVAILABLE, IMPAIRED, UNHEALTHY, or ERROR.
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
            The requests.
            (dict) --Describes the stop request.
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
    Terminating a WorkSpace is a permanent action and cannot be undone. The user's data is not maintained and will be destroyed. If you need to archive any user data, contact Amazon Web Services before terminating the WorkSpace.
    You can terminate a WorkSpace that is in any state except SUSPENDED .
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
            An array of structures that specify the WorkSpaces to terminate.
            (dict) --Contains information used with the TerminateWorkspaces operation to terminate a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace to terminate.
            
            

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

