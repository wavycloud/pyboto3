"""
The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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
"""


def can_paginate(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
    :type operation_name: string
    """
    pass


def create_tags(ResourceId=None, Tags=None):
    """
    :param ResourceId: [REQUIRED]
            The resource ID of the request.
            
    :type ResourceId: string
    :param Tags: [REQUIRED]
            The tags of the request.
            (dict) --Describes the tag of the WorkSpace.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            
    :type Tags: list
    """
    pass


def create_workspaces(Workspaces=None):
    """
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
            
            
            Return typedict
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
            Response Structure
            (dict) --Contains the result of the CreateWorkspaces operation.
            FailedRequests (list) --An array of structures that represent the WorkSpaces that could not be created.
            (dict) --Contains information about a WorkSpace that could not be created.
            WorkspaceRequest (dict) --A FailedCreateWorkspaceRequest$WorkspaceRequest object that contains the information about the WorkSpace that could not be created.
            DirectoryId (string) --The identifier of the AWS Directory Service directory to create the WorkSpace in. You can use the DescribeWorkspaceDirectories operation to obtain a list of the directories that are available.
            UserName (string) --The username that the WorkSpace is assigned to. This username must exist in the AWS Directory Service directory specified by the DirectoryId member.
            BundleId (string) --The identifier of the bundle to create the WorkSpace from. You can use the DescribeWorkspaceBundles operation to obtain a list of the bundles that are available.
            VolumeEncryptionKey (string) --The KMS key used to encrypt data stored on your WorkSpace.
            UserVolumeEncryptionEnabled (boolean) --Specifies whether the data stored on the user volume, or D: drive, is encrypted.
            RootVolumeEncryptionEnabled (boolean) --Specifies whether the data stored on the root volume, or C: drive, is encrypted.
            WorkspaceProperties (dict) --Describes the properties of a WorkSpace.
            RunningMode (string) --The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.
            RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
            Tags (list) --The tags of the WorkSpace request.
            (dict) --Describes the tag of the WorkSpace.
            Key (string) --The key of the tag.
            Value (string) --The value of the tag.
            
            ErrorCode (string) --The error code.
            ErrorMessage (string) --The textual error message.
            
            PendingRequests (list) --An array of structures that represent the WorkSpaces that were created.
            Because this operation is asynchronous, the identifier in WorkspaceId is not immediately available. If you immediately call DescribeWorkspaces with this identifier, no information will be returned.
            (dict) --Contains information about a WorkSpace.
            WorkspaceId (string) --The identifier of the WorkSpace.
            DirectoryId (string) --The identifier of the AWS Directory Service directory that the WorkSpace belongs to.
            UserName (string) --The user that the WorkSpace is assigned to.
            IpAddress (string) --The IP address of the WorkSpace.
            State (string) --The operational state of the WorkSpace.
            BundleId (string) --The identifier of the bundle that the WorkSpace was created from.
            SubnetId (string) --The identifier of the subnet that the WorkSpace is in.
            ErrorMessage (string) --If the WorkSpace could not be created, this contains a textual error message that describes the failure.
            ErrorCode (string) --If the WorkSpace could not be created, this contains the error code.
            ComputerName (string) --The name of the WorkSpace as seen by the operating system.
            VolumeEncryptionKey (string) --The KMS key used to encrypt data stored on your WorkSpace.
            UserVolumeEncryptionEnabled (boolean) --Specifies whether the data stored on the user volume, or D: drive, is encrypted.
            RootVolumeEncryptionEnabled (boolean) --Specifies whether the data stored on the root volume, or C: drive, is encrypted.
            WorkspaceProperties (dict) --Describes the properties of a WorkSpace.
            RunningMode (string) --The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.
            RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
            
            
            
            
    :type Workspaces: list
    """
    pass


def delete_tags(ResourceId=None, TagKeys=None):
    """
    :param ResourceId: [REQUIRED]
            The resource ID of the request.
            
    :type ResourceId: string
    :param TagKeys: [REQUIRED]
            The tag keys of the request.
            (string) --
            
    :type TagKeys: list
    """
    pass


def describe_tags(ResourceId=None):
    """
    :param ResourceId: [REQUIRED]
            The resource ID of the request.
            Return typedict
            ReturnsResponse Syntax{
              'TagList': [
                {
                  'Key': 'string',
                  'Value': 'string'
                },
              ]
            }
            Response Structure
            (dict) --The result of the DescribeTags operation.
            TagList (list) --The list of tags.
            (dict) --Describes the tag of the WorkSpace.
            Key (string) --The key of the tag.
            Value (string) --The value of the tag.
            
            
            
    :type ResourceId: string
    """
    pass


def describe_workspace_bundles(BundleIds=None, Owner=None, NextToken=None):
    """
    :param BundleIds: An array of strings that contains the identifiers of the bundles to retrieve. This parameter cannot be combined with any other filter parameter.
            (string) --
            
    :type BundleIds: list
    :param Owner: The owner of the bundles to retrieve. This parameter cannot be combined with any other filter parameter.
            This contains one of the following values:
            null- Retrieves the bundles that belong to the account making the call.
            AMAZON - Retrieves the bundles that are provided by AWS.
            
    :type Owner: string
    :param NextToken: The NextToken value from a previous call to this operation. Pass null if this is the first call.
    :type NextToken: string
    """
    pass


def describe_workspace_directories(DirectoryIds=None, NextToken=None):
    """
    :param DirectoryIds: An array of strings that contains the directory identifiers to retrieve information for. If this member is null, all directories are retrieved.
            (string) --
            
    :type DirectoryIds: list
    :param NextToken: The NextToken value from a previous call to this operation. Pass null if this is the first call.
    :type NextToken: string
    """
    pass


def describe_workspaces(WorkspaceIds=None, DirectoryId=None, UserName=None, BundleId=None, Limit=None, NextToken=None):
    """
    :param WorkspaceIds: An array of strings that contain the identifiers of the WorkSpaces for which to retrieve information. This parameter cannot be combined with any other filter parameter.
            Because the CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call DescribeWorkspaces with this identifier, no information is returned.
            (string) --
            
    :type WorkspaceIds: list
    :param DirectoryId: Specifies the directory identifier to which to limit the WorkSpaces. Optionally, you can specify a specific directory user with the UserName parameter. This parameter cannot be combined with any other filter parameter.
    :type DirectoryId: string
    :param UserName: Used with the DirectoryId parameter to specify the directory user for whom to obtain the WorkSpace.
    :type UserName: string
    :param BundleId: The identifier of a bundle to obtain the WorkSpaces for. All WorkSpaces that are created from this bundle will be retrieved. This parameter cannot be combined with any other filter parameter.
    :type BundleId: string
    :param Limit: The maximum number of items to return.
    :type Limit: integer
    :param NextToken: The NextToken value from a previous call to this operation. Pass null if this is the first call.
    :type NextToken: string
    """
    pass


def describe_workspaces_connection_status(WorkspaceIds=None, NextToken=None):
    """
    :param WorkspaceIds: An array of strings that contain the identifiers of the WorkSpaces.
            (string) --
            
    :type WorkspaceIds: list
    :param NextToken: The next token of the request.
    :type NextToken: string
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    :param ClientMethod: The client method to presign for
    :type ClientMethod: string
    :param Params: The parameters normally passed to
            ClientMethod.
    :type Params: dict
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
    :type ExpiresIn: int
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
    :type HttpMethod: string
    """
    pass


def get_paginator(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
    :type operation_name: string
    """
    pass


def get_waiter():
    """
    """
    pass


def modify_workspace_properties(WorkspaceId=None, WorkspaceProperties=None):
    """
    :param WorkspaceId: [REQUIRED]
            The ID of the WorkSpace.
            
    :type WorkspaceId: string
    :param WorkspaceProperties: [REQUIRED]
            The WorkSpace properties of the request.
            RunningMode (string) --The running mode of the WorkSpace. AlwaysOn WorkSpaces are billed monthly. AutoStop WorkSpaces are billed by the hour and stopped when no longer being used in order to save on costs.
            RunningModeAutoStopTimeoutInMinutes (integer) --The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
            
    :type WorkspaceProperties: dict
    """
    pass


def reboot_workspaces(RebootWorkspaceRequests=None):
    """
    :param RebootWorkspaceRequests: [REQUIRED]
            An array of structures that specify the WorkSpaces to reboot.
            (dict) --Contains information used with the RebootWorkspaces operation to reboot a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace to reboot.
            
            Return typedict
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
            (dict) --Contains the results of the RebootWorkspaces operation.
            FailedRequests (list) --An array of structures representing any WorkSpaces that could not be rebooted.
            (dict) --Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
            WorkspaceId (string) --The identifier of the WorkSpace.
            ErrorCode (string) --The error code.
            ErrorMessage (string) --The textual error message.
            
            
            
    :type RebootWorkspaceRequests: list
    """
    pass


def rebuild_workspaces(RebuildWorkspaceRequests=None):
    """
    :param RebuildWorkspaceRequests: [REQUIRED]
            An array of structures that specify the WorkSpaces to rebuild.
            (dict) --Contains information used with the RebuildWorkspaces operation to rebuild a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace to rebuild.
            
            Return typedict
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
            (dict) --Contains the results of the RebuildWorkspaces operation.
            FailedRequests (list) --An array of structures representing any WorkSpaces that could not be rebuilt.
            (dict) --Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
            WorkspaceId (string) --The identifier of the WorkSpace.
            ErrorCode (string) --The error code.
            ErrorMessage (string) --The textual error message.
            
            
            
    :type RebuildWorkspaceRequests: list
    """
    pass


def start_workspaces(StartWorkspaceRequests=None):
    """
    :param StartWorkspaceRequests: [REQUIRED]
            The requests.
            (dict) --Describes the start request.
            WorkspaceId (string) --The ID of the WorkSpace.
            
            Return typedict
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
            FailedRequests (list) --The failed requests.
            (dict) --Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
            WorkspaceId (string) --The identifier of the WorkSpace.
            ErrorCode (string) --The error code.
            ErrorMessage (string) --The textual error message.
            
            
            
    :type StartWorkspaceRequests: list
    """
    pass


def stop_workspaces(StopWorkspaceRequests=None):
    """
    :param StopWorkspaceRequests: [REQUIRED]
            The requests.
            (dict) --Describes the stop request.
            WorkspaceId (string) --The ID of the WorkSpace.
            
            Return typedict
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
            FailedRequests (list) --The failed requests.
            (dict) --Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
            WorkspaceId (string) --The identifier of the WorkSpace.
            ErrorCode (string) --The error code.
            ErrorMessage (string) --The textual error message.
            
            
            
    :type StopWorkspaceRequests: list
    """
    pass


def terminate_workspaces(TerminateWorkspaceRequests=None):
    """
    :param TerminateWorkspaceRequests: [REQUIRED]
            An array of structures that specify the WorkSpaces to terminate.
            (dict) --Contains information used with the TerminateWorkspaces operation to terminate a WorkSpace.
            WorkspaceId (string) -- [REQUIRED]The identifier of the WorkSpace to terminate.
            
            Return typedict
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
            (dict) --Contains the results of the TerminateWorkspaces operation.
            FailedRequests (list) --An array of structures representing any WorkSpaces that could not be terminated.
            (dict) --Contains information about a WorkSpace that could not be rebooted ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
            WorkspaceId (string) --The identifier of the WorkSpace.
            ErrorCode (string) --The error code.
            ErrorMessage (string) --The textual error message.
            
            
            
    :type TerminateWorkspaceRequests: list
    """
    pass
