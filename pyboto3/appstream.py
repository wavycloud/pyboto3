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

def associate_fleet(FleetName=None, StackName=None):
    """
    Associates the specified fleet with the specified stack.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_fleet(
        FleetName='string',
        StackName='string'
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]
            The name of the fleet.
            

    :type StackName: string
    :param StackName: [REQUIRED]
            The name of the stack.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

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

def copy_image(SourceImageName=None, DestinationImageName=None, DestinationRegion=None, DestinationImageDescription=None):
    """
    Copies the image within the same region or to a new region within the same AWS account. Note that any tags you added to the image will not be copied.
    See also: AWS API Documentation
    
    
    :example: response = client.copy_image(
        SourceImageName='string',
        DestinationImageName='string',
        DestinationRegion='string',
        DestinationImageDescription='string'
    )
    
    
    :type SourceImageName: string
    :param SourceImageName: [REQUIRED]
            The name of the image to copy.
            

    :type DestinationImageName: string
    :param DestinationImageName: [REQUIRED]
            The name that the image will have when it is copied to the destination.
            

    :type DestinationRegion: string
    :param DestinationRegion: [REQUIRED]
            The destination region to which the image will be copied. This parameter is required, even if you are copying an image within the same region.
            

    :type DestinationImageDescription: string
    :param DestinationImageDescription: The description that the image will have when it is copied to the destination.

    :rtype: dict
    :return: {
        'DestinationImageName': 'string'
    }
    
    
    """
    pass

def create_directory_config(DirectoryName=None, OrganizationalUnitDistinguishedNames=None, ServiceAccountCredentials=None):
    """
    Creates a directory configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.create_directory_config(
        DirectoryName='string',
        OrganizationalUnitDistinguishedNames=[
            'string',
        ],
        ServiceAccountCredentials={
            'AccountName': 'string',
            'AccountPassword': 'string'
        }
    )
    
    
    :type DirectoryName: string
    :param DirectoryName: [REQUIRED]
            The fully qualified name of the directory (for example, corp.example.com).
            

    :type OrganizationalUnitDistinguishedNames: list
    :param OrganizationalUnitDistinguishedNames: [REQUIRED]
            The distinguished names of the organizational units for computer accounts.
            (string) --
            

    :type ServiceAccountCredentials: dict
    :param ServiceAccountCredentials: [REQUIRED]
            The credentials for the service account used by the streaming instance to connect to the directory.
            AccountName (string) -- [REQUIRED]The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
            AccountPassword (string) -- [REQUIRED]The password for the account.
            

    :rtype: dict
    :return: {
        'DirectoryConfig': {
            'DirectoryName': 'string',
            'OrganizationalUnitDistinguishedNames': [
                'string',
            ],
            'ServiceAccountCredentials': {
                'AccountName': 'string',
                'AccountPassword': 'string'
            },
            'CreatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_fleet(Name=None, ImageName=None, InstanceType=None, FleetType=None, ComputeCapacity=None, VpcConfig=None, MaxUserDurationInSeconds=None, DisconnectTimeoutInSeconds=None, Description=None, DisplayName=None, EnableDefaultInternetAccess=None, DomainJoinInfo=None):
    """
    Creates a fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.create_fleet(
        Name='string',
        ImageName='string',
        InstanceType='string',
        FleetType='ALWAYS_ON'|'ON_DEMAND',
        ComputeCapacity={
            'DesiredInstances': 123
        },
        VpcConfig={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        MaxUserDurationInSeconds=123,
        DisconnectTimeoutInSeconds=123,
        Description='string',
        DisplayName='string',
        EnableDefaultInternetAccess=True|False,
        DomainJoinInfo={
            'DirectoryName': 'string',
            'OrganizationalUnitDistinguishedName': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A unique name for the fleet.
            

    :type ImageName: string
    :param ImageName: [REQUIRED]
            The name of the image used to create the fleet.
            

    :type InstanceType: string
    :param InstanceType: [REQUIRED]
            The instance type to use when launching fleet instances. The following instance types are available:
            stream.standard.medium
            stream.standard.large
            stream.compute.large
            stream.compute.xlarge
            stream.compute.2xlarge
            stream.compute.4xlarge
            stream.compute.8xlarge
            stream.memory.large
            stream.memory.xlarge
            stream.memory.2xlarge
            stream.memory.4xlarge
            stream.memory.8xlarge
            stream.graphics-design.large
            stream.graphics-design.xlarge
            stream.graphics-design.2xlarge
            stream.graphics-design.4xlarge
            stream.graphics-desktop.2xlarge
            stream.graphics-pro.4xlarge
            stream.graphics-pro.8xlarge
            stream.graphics-pro.16xlarge
            

    :type FleetType: string
    :param FleetType: The fleet type.
            ALWAYS_ON
            Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.
            ON_DEMAND
            Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.
            

    :type ComputeCapacity: dict
    :param ComputeCapacity: [REQUIRED]
            The desired capacity for the fleet.
            DesiredInstances (integer) -- [REQUIRED]The desired number of streaming instances.
            

    :type VpcConfig: dict
    :param VpcConfig: The VPC configuration for the fleet.
            SubnetIds (list) --The subnets to which a network interface is established from the fleet instance.
            (string) --
            SecurityGroupIds (list) --The security groups for the fleet.
            (string) --
            

    :type MaxUserDurationInSeconds: integer
    :param MaxUserDurationInSeconds: The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.

    :type DisconnectTimeoutInSeconds: integer
    :param DisconnectTimeoutInSeconds: The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.

    :type Description: string
    :param Description: The description for display.

    :type DisplayName: string
    :param DisplayName: The fleet name for display.

    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: Enables or disables default internet access for the fleet.

    :type DomainJoinInfo: dict
    :param DomainJoinInfo: The information needed to join a Microsoft Active Directory domain.
            DirectoryName (string) --The fully qualified name of the directory (for example, corp.example.com).
            OrganizationalUnitDistinguishedName (string) --The distinguished name of the organizational unit for computer accounts.
            

    :rtype: dict
    :return: {
        'Fleet': {
            'Arn': 'string',
            'Name': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'ImageName': 'string',
            'InstanceType': 'string',
            'FleetType': 'ALWAYS_ON'|'ON_DEMAND',
            'ComputeCapacityStatus': {
                'Desired': 123,
                'Running': 123,
                'InUse': 123,
                'Available': 123
            },
            'MaxUserDurationInSeconds': 123,
            'DisconnectTimeoutInSeconds': 123,
            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'CreatedTime': datetime(2015, 1, 1),
            'FleetErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ],
            'EnableDefaultInternetAccess': True|False,
            'DomainJoinInfo': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedName': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_image_builder(Name=None, ImageName=None, InstanceType=None, Description=None, DisplayName=None, VpcConfig=None, EnableDefaultInternetAccess=None, DomainJoinInfo=None, AppstreamAgentVersion=None):
    """
    Creates an image builder.
    The initial state of the builder is PENDING . When it is ready, the state is RUNNING .
    See also: AWS API Documentation
    
    
    :example: response = client.create_image_builder(
        Name='string',
        ImageName='string',
        InstanceType='string',
        Description='string',
        DisplayName='string',
        VpcConfig={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        EnableDefaultInternetAccess=True|False,
        DomainJoinInfo={
            'DirectoryName': 'string',
            'OrganizationalUnitDistinguishedName': 'string'
        },
        AppstreamAgentVersion='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A unique name for the image builder.
            

    :type ImageName: string
    :param ImageName: [REQUIRED]
            The name of the image used to create the builder.
            

    :type InstanceType: string
    :param InstanceType: [REQUIRED]
            The instance type to use when launching the image builder.
            

    :type Description: string
    :param Description: The description for display.

    :type DisplayName: string
    :param DisplayName: The image builder name for display.

    :type VpcConfig: dict
    :param VpcConfig: The VPC configuration for the image builder. You can specify only one subnet.
            SubnetIds (list) --The subnets to which a network interface is established from the fleet instance.
            (string) --
            SecurityGroupIds (list) --The security groups for the fleet.
            (string) --
            

    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: Enables or disables default internet access for the image builder.

    :type DomainJoinInfo: dict
    :param DomainJoinInfo: The information needed to join a Microsoft Active Directory domain.
            DirectoryName (string) --The fully qualified name of the directory (for example, corp.example.com).
            OrganizationalUnitDistinguishedName (string) --The distinguished name of the organizational unit for computer accounts.
            

    :type AppstreamAgentVersion: string
    :param AppstreamAgentVersion: The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].

    :rtype: dict
    :return: {
        'ImageBuilder': {
            'Name': 'string',
            'Arn': 'string',
            'ImageArn': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'InstanceType': 'string',
            'Platform': 'WINDOWS',
            'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
            'StateChangeReason': {
                'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                'Message': 'string'
            },
            'CreatedTime': datetime(2015, 1, 1),
            'EnableDefaultInternetAccess': True|False,
            'DomainJoinInfo': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedName': 'string'
            },
            'ImageBuilderErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string',
                    'ErrorTimestamp': datetime(2015, 1, 1)
                },
            ],
            'AppstreamAgentVersion': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_image_builder_streaming_url(Name=None, Validity=None):
    """
    Creates a URL to start an image builder streaming session.
    See also: AWS API Documentation
    
    
    :example: response = client.create_image_builder_streaming_url(
        Name='string',
        Validity=123
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the image builder.
            

    :type Validity: integer
    :param Validity: The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.

    :rtype: dict
    :return: {
        'StreamingURL': 'string',
        'Expires': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def create_stack(Name=None, Description=None, DisplayName=None, StorageConnectors=None, RedirectURL=None, FeedbackURL=None):
    """
    Creates a stack.
    See also: AWS API Documentation
    
    
    :example: response = client.create_stack(
        Name='string',
        Description='string',
        DisplayName='string',
        StorageConnectors=[
            {
                'ConnectorType': 'HOMEFOLDERS',
                'ResourceIdentifier': 'string'
            },
        ],
        RedirectURL='string',
        FeedbackURL='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the stack.
            

    :type Description: string
    :param Description: The description for display.

    :type DisplayName: string
    :param DisplayName: The stack name for display.

    :type StorageConnectors: list
    :param StorageConnectors: The storage connectors to enable.
            (dict) --Describes a storage connector.
            ConnectorType (string) -- [REQUIRED]The type of storage connector.
            ResourceIdentifier (string) --The ARN of the storage connector.
            
            

    :type RedirectURL: string
    :param RedirectURL: The URL that users are redirected to after their streaming session ends.

    :type FeedbackURL: string
    :param FeedbackURL: The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.

    :rtype: dict
    :return: {
        'Stack': {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'StorageConnectors': [
                {
                    'ConnectorType': 'HOMEFOLDERS',
                    'ResourceIdentifier': 'string'
                },
            ],
            'RedirectURL': 'string',
            'FeedbackURL': 'string',
            'StackErrors': [
                {
                    'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_streaming_url(StackName=None, FleetName=None, UserId=None, ApplicationId=None, Validity=None, SessionContext=None):
    """
    Creates a URL to start a streaming session for the specified user.
    See also: AWS API Documentation
    
    
    :example: response = client.create_streaming_url(
        StackName='string',
        FleetName='string',
        UserId='string',
        ApplicationId='string',
        Validity=123,
        SessionContext='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name of the stack.
            

    :type FleetName: string
    :param FleetName: [REQUIRED]
            The name of the fleet.
            

    :type UserId: string
    :param UserId: [REQUIRED]
            The ID of the user.
            

    :type ApplicationId: string
    :param ApplicationId: The name of the application to launch after the session starts. This is the name that you specified as Name in the Image Assistant.

    :type Validity: integer
    :param Validity: The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 60 seconds.

    :type SessionContext: string
    :param SessionContext: The session context. For more information, see Session Context in the Amazon AppStream 2.0 Developer Guide .

    :rtype: dict
    :return: {
        'StreamingURL': 'string',
        'Expires': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def delete_directory_config(DirectoryName=None):
    """
    Deletes the specified directory configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_directory_config(
        DirectoryName='string'
    )
    
    
    :type DirectoryName: string
    :param DirectoryName: [REQUIRED]
            The name of the directory configuration.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_fleet(Name=None):
    """
    Deletes the specified fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_fleet(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the fleet.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_image(Name=None):
    """
    Deletes the specified image. You cannot delete an image that is currently in use. After you delete an image, you cannot provision new capacity using the image.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_image(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the image.
            

    :rtype: dict
    :return: {
        'Image': {
            'Name': 'string',
            'Arn': 'string',
            'BaseImageArn': 'string',
            'DisplayName': 'string',
            'State': 'PENDING'|'AVAILABLE'|'FAILED'|'COPYING'|'DELETING',
            'Visibility': 'PUBLIC'|'PRIVATE',
            'ImageBuilderSupported': True|False,
            'Platform': 'WINDOWS',
            'Description': 'string',
            'StateChangeReason': {
                'Code': 'INTERNAL_ERROR'|'IMAGE_BUILDER_NOT_AVAILABLE'|'IMAGE_COPY_FAILURE',
                'Message': 'string'
            },
            'Applications': [
                {
                    'Name': 'string',
                    'DisplayName': 'string',
                    'IconURL': 'string',
                    'LaunchPath': 'string',
                    'LaunchParameters': 'string',
                    'Enabled': True|False,
                    'Metadata': {
                        'string': 'string'
                    }
                },
            ],
            'CreatedTime': datetime(2015, 1, 1),
            'PublicBaseImageReleasedDate': datetime(2015, 1, 1),
            'AppstreamAgentVersion': 'string'
        }
    }
    
    
    """
    pass

def delete_image_builder(Name=None):
    """
    Deletes the specified image builder and releases the capacity.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_image_builder(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the image builder.
            

    :rtype: dict
    :return: {
        'ImageBuilder': {
            'Name': 'string',
            'Arn': 'string',
            'ImageArn': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'InstanceType': 'string',
            'Platform': 'WINDOWS',
            'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
            'StateChangeReason': {
                'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                'Message': 'string'
            },
            'CreatedTime': datetime(2015, 1, 1),
            'EnableDefaultInternetAccess': True|False,
            'DomainJoinInfo': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedName': 'string'
            },
            'ImageBuilderErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string',
                    'ErrorTimestamp': datetime(2015, 1, 1)
                },
            ],
            'AppstreamAgentVersion': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_stack(Name=None):
    """
    Deletes the specified stack. After this operation completes, the environment can no longer be activated and any reservations made for the stack are released.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_stack(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the stack.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_directory_configs(DirectoryNames=None, MaxResults=None, NextToken=None):
    """
    Describes the specified directory configurations. Note that although the response syntax in this topic includes the account password, this password is not returned in the actual response.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_directory_configs(
        DirectoryNames=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DirectoryNames: list
    :param DirectoryNames: The directory names.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: The maximum size of each page of results.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'DirectoryConfigs': [
            {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedNames': [
                    'string',
                ],
                'ServiceAccountCredentials': {
                    'AccountName': 'string',
                    'AccountPassword': 'string'
                },
                'CreatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_fleets(Names=None, NextToken=None):
    """
    Describes the specified fleets or all fleets in the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_fleets(
        Names=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: The names of the fleets to describe.
            (string) --
            

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'Fleets': [
            {
                'Arn': 'string',
                'Name': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'ImageName': 'string',
                'InstanceType': 'string',
                'FleetType': 'ALWAYS_ON'|'ON_DEMAND',
                'ComputeCapacityStatus': {
                    'Desired': 123,
                    'Running': 123,
                    'InUse': 123,
                    'Available': 123
                },
                'MaxUserDurationInSeconds': 123,
                'DisconnectTimeoutInSeconds': 123,
                'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'CreatedTime': datetime(2015, 1, 1),
                'FleetErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ],
                'EnableDefaultInternetAccess': True|False,
                'DomainJoinInfo': {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_image_builders(Names=None, MaxResults=None, NextToken=None):
    """
    Describes the specified image builders or all image builders in the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_image_builders(
        Names=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: The names of the image builders to describe.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: The maximum size of each page of results.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'ImageBuilders': [
            {
                'Name': 'string',
                'Arn': 'string',
                'ImageArn': 'string',
                'Description': 'string',
                'DisplayName': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'InstanceType': 'string',
                'Platform': 'WINDOWS',
                'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                    'Message': 'string'
                },
                'CreatedTime': datetime(2015, 1, 1),
                'EnableDefaultInternetAccess': True|False,
                'DomainJoinInfo': {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string'
                },
                'ImageBuilderErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string',
                        'ErrorTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'AppstreamAgentVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_images(Names=None):
    """
    Describes the specified images or all images in the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_images(
        Names=[
            'string',
        ]
    )
    
    
    :type Names: list
    :param Names: The names of the images to describe.
            (string) --
            

    :rtype: dict
    :return: {
        'Images': [
            {
                'Name': 'string',
                'Arn': 'string',
                'BaseImageArn': 'string',
                'DisplayName': 'string',
                'State': 'PENDING'|'AVAILABLE'|'FAILED'|'COPYING'|'DELETING',
                'Visibility': 'PUBLIC'|'PRIVATE',
                'ImageBuilderSupported': True|False,
                'Platform': 'WINDOWS',
                'Description': 'string',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'IMAGE_BUILDER_NOT_AVAILABLE'|'IMAGE_COPY_FAILURE',
                    'Message': 'string'
                },
                'Applications': [
                    {
                        'Name': 'string',
                        'DisplayName': 'string',
                        'IconURL': 'string',
                        'LaunchPath': 'string',
                        'LaunchParameters': 'string',
                        'Enabled': True|False,
                        'Metadata': {
                            'string': 'string'
                        }
                    },
                ],
                'CreatedTime': datetime(2015, 1, 1),
                'PublicBaseImageReleasedDate': datetime(2015, 1, 1),
                'AppstreamAgentVersion': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_sessions(StackName=None, FleetName=None, UserId=None, NextToken=None, Limit=None, AuthenticationType=None):
    """
    Describes the streaming sessions for the specified stack and fleet. If a user ID is provided, only the streaming sessions for only that user are returned. If an authentication type is not provided, the default is to authenticate users using a streaming URL.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_sessions(
        StackName='string',
        FleetName='string',
        UserId='string',
        NextToken='string',
        Limit=123,
        AuthenticationType='API'|'SAML'|'USERPOOL'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name of the stack. This value is case-sensitive.
            

    :type FleetName: string
    :param FleetName: [REQUIRED]
            The name of the fleet. This value is case-sensitive.
            

    :type UserId: string
    :param UserId: The user ID.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :type Limit: integer
    :param Limit: The size of each page of results. The default value is 20 and the maximum value is 50.

    :type AuthenticationType: string
    :param AuthenticationType: The authentication method. Specify API for a user authenticated using a streaming URL or SAML for a SAML federated user. The default is to authenticate users using a streaming URL.

    :rtype: dict
    :return: {
        'Sessions': [
            {
                'Id': 'string',
                'UserId': 'string',
                'StackName': 'string',
                'FleetName': 'string',
                'State': 'ACTIVE'|'PENDING'|'EXPIRED',
                'AuthenticationType': 'API'|'SAML'|'USERPOOL'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_stacks(Names=None, NextToken=None):
    """
    Describes the specified stacks or all stacks in the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stacks(
        Names=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: The names of the stacks to describe.
            (string) --
            

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'Stacks': [
            {
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'DisplayName': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'StorageConnectors': [
                    {
                        'ConnectorType': 'HOMEFOLDERS',
                        'ResourceIdentifier': 'string'
                    },
                ],
                'RedirectURL': 'string',
                'FeedbackURL': 'string',
                'StackErrors': [
                    {
                        'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def disassociate_fleet(FleetName=None, StackName=None):
    """
    Disassociates the specified fleet from the specified stack.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_fleet(
        FleetName='string',
        StackName='string'
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]
            The name of the fleet.
            

    :type StackName: string
    :param StackName: [REQUIRED]
            The name of the stack.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def expire_session(SessionId=None):
    """
    Stops the specified streaming session.
    See also: AWS API Documentation
    
    
    :example: response = client.expire_session(
        SessionId='string'
    )
    
    
    :type SessionId: string
    :param SessionId: [REQUIRED]
            The ID of the streaming session.
            

    :rtype: dict
    :return: {}
    
    
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

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_associated_fleets(StackName=None, NextToken=None):
    """
    Lists the fleets associated with the specified stack.
    See also: AWS API Documentation
    
    
    :example: response = client.list_associated_fleets(
        StackName='string',
        NextToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name of the stack.
            

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'Names': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_associated_stacks(FleetName=None, NextToken=None):
    """
    Lists the stacks associated with the specified fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.list_associated_stacks(
        FleetName='string',
        NextToken='string'
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]
            The name of the fleet.
            

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'Names': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Lists the tags for the specified AppStream 2.0 resource. You can tag AppStream 2.0 image builders, images, fleets, and stacks.
    For more information about tags, see Tagging Your Resources in the Amazon AppStream 2.0 Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource.
            

    :rtype: dict
    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def start_fleet(Name=None):
    """
    Starts the specified fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.start_fleet(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the fleet.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def start_image_builder(Name=None, AppstreamAgentVersion=None):
    """
    Starts the specified image builder.
    See also: AWS API Documentation
    
    
    :example: response = client.start_image_builder(
        Name='string',
        AppstreamAgentVersion='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the image builder.
            

    :type AppstreamAgentVersion: string
    :param AppstreamAgentVersion: The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].

    :rtype: dict
    :return: {
        'ImageBuilder': {
            'Name': 'string',
            'Arn': 'string',
            'ImageArn': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'InstanceType': 'string',
            'Platform': 'WINDOWS',
            'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
            'StateChangeReason': {
                'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                'Message': 'string'
            },
            'CreatedTime': datetime(2015, 1, 1),
            'EnableDefaultInternetAccess': True|False,
            'DomainJoinInfo': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedName': 'string'
            },
            'ImageBuilderErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string',
                    'ErrorTimestamp': datetime(2015, 1, 1)
                },
            ],
            'AppstreamAgentVersion': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def stop_fleet(Name=None):
    """
    Stops the specified fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_fleet(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the fleet.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def stop_image_builder(Name=None):
    """
    Stops the specified image builder.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_image_builder(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the image builder.
            

    :rtype: dict
    :return: {
        'ImageBuilder': {
            'Name': 'string',
            'Arn': 'string',
            'ImageArn': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'InstanceType': 'string',
            'Platform': 'WINDOWS',
            'State': 'PENDING'|'UPDATING_AGENT'|'RUNNING'|'STOPPING'|'STOPPED'|'REBOOTING'|'SNAPSHOTTING'|'DELETING'|'FAILED',
            'StateChangeReason': {
                'Code': 'INTERNAL_ERROR'|'IMAGE_UNAVAILABLE',
                'Message': 'string'
            },
            'CreatedTime': datetime(2015, 1, 1),
            'EnableDefaultInternetAccess': True|False,
            'DomainJoinInfo': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedName': 'string'
            },
            'ImageBuilderErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string',
                    'ErrorTimestamp': datetime(2015, 1, 1)
                },
            ],
            'AppstreamAgentVersion': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds or overwrites one or more tags for the specified AppStream 2.0 resource. You can tag AppStream 2.0 image builders, images, fleets, and stacks.
    Each tag consists of a key and an optional value. If a resource already has a tag with the same key, this operation updates its value.
    To list the current tags for your resources, use  ListTagsForResource . To disassociate tags from your resources, use  UntagResource .
    For more information about tags, see Tagging Your Resources in the Amazon AppStream 2.0 Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource.
            

    :type Tags: dict
    :param Tags: [REQUIRED]
            The tags to associate. A tag is a key-value pair (the value is optional). For example, Environment=Test , or, if you do not specify a value, Environment= .
            If you do not specify a value, we set the value to an empty string.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Disassociates the specified tags from the specified AppStream 2.0 resource.
    To list the current tags for your resources, use  ListTagsForResource .
    For more information about tags, see Tagging Your Resources in the Amazon AppStream 2.0 Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tag keys for the tags to disassociate.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_directory_config(DirectoryName=None, OrganizationalUnitDistinguishedNames=None, ServiceAccountCredentials=None):
    """
    Updates the specified directory configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.update_directory_config(
        DirectoryName='string',
        OrganizationalUnitDistinguishedNames=[
            'string',
        ],
        ServiceAccountCredentials={
            'AccountName': 'string',
            'AccountPassword': 'string'
        }
    )
    
    
    :type DirectoryName: string
    :param DirectoryName: [REQUIRED]
            The name of the directory configuration.
            

    :type OrganizationalUnitDistinguishedNames: list
    :param OrganizationalUnitDistinguishedNames: The distinguished names of the organizational units for computer accounts.
            (string) --
            

    :type ServiceAccountCredentials: dict
    :param ServiceAccountCredentials: The credentials for the service account used by the streaming instance to connect to the directory.
            AccountName (string) -- [REQUIRED]The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
            AccountPassword (string) -- [REQUIRED]The password for the account.
            

    :rtype: dict
    :return: {
        'DirectoryConfig': {
            'DirectoryName': 'string',
            'OrganizationalUnitDistinguishedNames': [
                'string',
            ],
            'ServiceAccountCredentials': {
                'AccountName': 'string',
                'AccountPassword': 'string'
            },
            'CreatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_fleet(ImageName=None, Name=None, InstanceType=None, ComputeCapacity=None, VpcConfig=None, MaxUserDurationInSeconds=None, DisconnectTimeoutInSeconds=None, DeleteVpcConfig=None, Description=None, DisplayName=None, EnableDefaultInternetAccess=None, DomainJoinInfo=None, AttributesToDelete=None):
    """
    Updates the specified fleet.
    If the fleet is in the STOPPED state, you can update any attribute except the fleet name. If the fleet is in the RUNNING state, you can update the DisplayName and ComputeCapacity attributes. If the fleet is in the STARTING or STOPPING state, you can't update it.
    See also: AWS API Documentation
    
    
    :example: response = client.update_fleet(
        ImageName='string',
        Name='string',
        InstanceType='string',
        ComputeCapacity={
            'DesiredInstances': 123
        },
        VpcConfig={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        MaxUserDurationInSeconds=123,
        DisconnectTimeoutInSeconds=123,
        DeleteVpcConfig=True|False,
        Description='string',
        DisplayName='string',
        EnableDefaultInternetAccess=True|False,
        DomainJoinInfo={
            'DirectoryName': 'string',
            'OrganizationalUnitDistinguishedName': 'string'
        },
        AttributesToDelete=[
            'VPC_CONFIGURATION'|'VPC_CONFIGURATION_SECURITY_GROUP_IDS'|'DOMAIN_JOIN_INFO',
        ]
    )
    
    
    :type ImageName: string
    :param ImageName: The name of the image used to create the fleet.

    :type Name: string
    :param Name: [REQUIRED]
            A unique name for the fleet.
            

    :type InstanceType: string
    :param InstanceType: The instance type to use when launching fleet instances. The following instance types are available:
            stream.standard.medium
            stream.standard.large
            stream.compute.large
            stream.compute.xlarge
            stream.compute.2xlarge
            stream.compute.4xlarge
            stream.compute.8xlarge
            stream.memory.large
            stream.memory.xlarge
            stream.memory.2xlarge
            stream.memory.4xlarge
            stream.memory.8xlarge
            stream.graphics-design.large
            stream.graphics-design.xlarge
            stream.graphics-design.2xlarge
            stream.graphics-design.4xlarge
            stream.graphics-desktop.2xlarge
            stream.graphics-pro.4xlarge
            stream.graphics-pro.8xlarge
            stream.graphics-pro.16xlarge
            

    :type ComputeCapacity: dict
    :param ComputeCapacity: The desired capacity for the fleet.
            DesiredInstances (integer) -- [REQUIRED]The desired number of streaming instances.
            

    :type VpcConfig: dict
    :param VpcConfig: The VPC configuration for the fleet.
            SubnetIds (list) --The subnets to which a network interface is established from the fleet instance.
            (string) --
            SecurityGroupIds (list) --The security groups for the fleet.
            (string) --
            

    :type MaxUserDurationInSeconds: integer
    :param MaxUserDurationInSeconds: The maximum time that a streaming session can run, in seconds. Specify a value between 600 and 57600.

    :type DisconnectTimeoutInSeconds: integer
    :param DisconnectTimeoutInSeconds: The time after disconnection when a session is considered to have ended, in seconds. If a user who was disconnected reconnects within this time interval, the user is connected to their previous session. Specify a value between 60 and 57600.

    :type DeleteVpcConfig: boolean
    :param DeleteVpcConfig: Deletes the VPC association for the specified fleet.

    :type Description: string
    :param Description: The description for display.

    :type DisplayName: string
    :param DisplayName: The fleet name for display.

    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: Enables or disables default internet access for the fleet.

    :type DomainJoinInfo: dict
    :param DomainJoinInfo: The information needed to join a Microsoft Active Directory domain.
            DirectoryName (string) --The fully qualified name of the directory (for example, corp.example.com).
            OrganizationalUnitDistinguishedName (string) --The distinguished name of the organizational unit for computer accounts.
            

    :type AttributesToDelete: list
    :param AttributesToDelete: The fleet attributes to delete.
            (string) --The fleet attribute.
            

    :rtype: dict
    :return: {
        'Fleet': {
            'Arn': 'string',
            'Name': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'ImageName': 'string',
            'InstanceType': 'string',
            'FleetType': 'ALWAYS_ON'|'ON_DEMAND',
            'ComputeCapacityStatus': {
                'Desired': 123,
                'Running': 123,
                'InUse': 123,
                'Available': 123
            },
            'MaxUserDurationInSeconds': 123,
            'DisconnectTimeoutInSeconds': 123,
            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'CreatedTime': datetime(2015, 1, 1),
            'FleetErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ],
            'EnableDefaultInternetAccess': True|False,
            'DomainJoinInfo': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedName': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_stack(DisplayName=None, Description=None, Name=None, StorageConnectors=None, DeleteStorageConnectors=None, RedirectURL=None, FeedbackURL=None, AttributesToDelete=None):
    """
    Updates the specified stack.
    See also: AWS API Documentation
    
    
    :example: response = client.update_stack(
        DisplayName='string',
        Description='string',
        Name='string',
        StorageConnectors=[
            {
                'ConnectorType': 'HOMEFOLDERS',
                'ResourceIdentifier': 'string'
            },
        ],
        DeleteStorageConnectors=True|False,
        RedirectURL='string',
        FeedbackURL='string',
        AttributesToDelete=[
            'STORAGE_CONNECTORS'|'REDIRECT_URL'|'FEEDBACK_URL'|'THEME_NAME',
        ]
    )
    
    
    :type DisplayName: string
    :param DisplayName: The stack name for display.

    :type Description: string
    :param Description: The description for display.

    :type Name: string
    :param Name: [REQUIRED]
            The name of the stack.
            

    :type StorageConnectors: list
    :param StorageConnectors: The storage connectors to enable.
            (dict) --Describes a storage connector.
            ConnectorType (string) -- [REQUIRED]The type of storage connector.
            ResourceIdentifier (string) --The ARN of the storage connector.
            
            

    :type DeleteStorageConnectors: boolean
    :param DeleteStorageConnectors: Deletes the storage connectors currently enabled for the stack.

    :type RedirectURL: string
    :param RedirectURL: The URL that users are redirected to after their streaming session ends.

    :type FeedbackURL: string
    :param FeedbackURL: The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.

    :type AttributesToDelete: list
    :param AttributesToDelete: The stack attributes to delete.
            (string) --
            

    :rtype: dict
    :return: {
        'Stack': {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'StorageConnectors': [
                {
                    'ConnectorType': 'HOMEFOLDERS',
                    'ResourceIdentifier': 'string'
                },
            ],
            'RedirectURL': 'string',
            'FeedbackURL': 'string',
            'StackErrors': [
                {
                    'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

