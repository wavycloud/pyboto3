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
    
    Exceptions
    
    :example: response = client.associate_fleet(
        FleetName='string',
        StackName='string'
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]\nThe name of the fleet.\n

    :type StackName: string
    :param StackName: [REQUIRED]\nThe name of the stack.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ConcurrentModificationException
AppStream.Client.exceptions.IncompatibleImageException
AppStream.Client.exceptions.OperationNotPermittedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def batch_associate_user_stack(UserStackAssociations=None):
    """
    Associates the specified users with the specified stacks. Users in a user pool cannot be assigned to stacks with fleets that are joined to an Active Directory domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_associate_user_stack(
        UserStackAssociations=[
            {
                'StackName': 'string',
                'UserName': 'string',
                'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                'SendEmailNotification': True|False
            },
        ]
    )
    
    
    :type UserStackAssociations: list
    :param UserStackAssociations: [REQUIRED]\nThe list of UserStackAssociation objects.\n\n(dict) --Describes a user in the user pool and the associated stack.\n\nStackName (string) -- [REQUIRED]The name of the stack that is associated with the user.\n\nUserName (string) -- [REQUIRED]The email address of the user who is associated with the stack.\n\nNote\nUsers\' email addresses are case-sensitive.\n\n\nAuthenticationType (string) -- [REQUIRED]The authentication type for the user.\n\nSendEmailNotification (boolean) --Specifies whether a welcome email is sent to a user after the user is created in the user pool.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'errors': [
        {
            'UserStackAssociation': {
                'StackName': 'string',
                'UserName': 'string',
                'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                'SendEmailNotification': True|False
            },
            'ErrorCode': 'STACK_NOT_FOUND'|'USER_NAME_NOT_FOUND'|'INTERNAL_ERROR',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
errors (list) --The list of UserStackAssociationError objects.

(dict) --Describes the error that is returned when a user can\xe2\x80\x99t be associated with or disassociated from a stack.

UserStackAssociation (dict) --Information about the user and associated stack.

StackName (string) --The name of the stack that is associated with the user.

UserName (string) --The email address of the user who is associated with the stack.

Note
Users\' email addresses are case-sensitive.


AuthenticationType (string) --The authentication type for the user.

SendEmailNotification (boolean) --Specifies whether a welcome email is sent to a user after the user is created in the user pool.



ErrorCode (string) --The error code for the error that is returned when a user can\xe2\x80\x99t be associated with or disassociated from a stack.

ErrorMessage (string) --The error message for the error that is returned when a user can\xe2\x80\x99t be associated with or disassociated from a stack.










Exceptions

AppStream.Client.exceptions.OperationNotPermittedException


    :return: {
        'errors': [
            {
                'UserStackAssociation': {
                    'StackName': 'string',
                    'UserName': 'string',
                    'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                    'SendEmailNotification': True|False
                },
                'ErrorCode': 'STACK_NOT_FOUND'|'USER_NAME_NOT_FOUND'|'INTERNAL_ERROR',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_disassociate_user_stack(UserStackAssociations=None):
    """
    Disassociates the specified users from the specified stacks.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_disassociate_user_stack(
        UserStackAssociations=[
            {
                'StackName': 'string',
                'UserName': 'string',
                'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                'SendEmailNotification': True|False
            },
        ]
    )
    
    
    :type UserStackAssociations: list
    :param UserStackAssociations: [REQUIRED]\nThe list of UserStackAssociation objects.\n\n(dict) --Describes a user in the user pool and the associated stack.\n\nStackName (string) -- [REQUIRED]The name of the stack that is associated with the user.\n\nUserName (string) -- [REQUIRED]The email address of the user who is associated with the stack.\n\nNote\nUsers\' email addresses are case-sensitive.\n\n\nAuthenticationType (string) -- [REQUIRED]The authentication type for the user.\n\nSendEmailNotification (boolean) --Specifies whether a welcome email is sent to a user after the user is created in the user pool.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'errors': [
        {
            'UserStackAssociation': {
                'StackName': 'string',
                'UserName': 'string',
                'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                'SendEmailNotification': True|False
            },
            'ErrorCode': 'STACK_NOT_FOUND'|'USER_NAME_NOT_FOUND'|'INTERNAL_ERROR',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
errors (list) --The list of UserStackAssociationError objects.

(dict) --Describes the error that is returned when a user can\xe2\x80\x99t be associated with or disassociated from a stack.

UserStackAssociation (dict) --Information about the user and associated stack.

StackName (string) --The name of the stack that is associated with the user.

UserName (string) --The email address of the user who is associated with the stack.

Note
Users\' email addresses are case-sensitive.


AuthenticationType (string) --The authentication type for the user.

SendEmailNotification (boolean) --Specifies whether a welcome email is sent to a user after the user is created in the user pool.



ErrorCode (string) --The error code for the error that is returned when a user can\xe2\x80\x99t be associated with or disassociated from a stack.

ErrorMessage (string) --The error message for the error that is returned when a user can\xe2\x80\x99t be associated with or disassociated from a stack.











    :return: {
        'errors': [
            {
                'UserStackAssociation': {
                    'StackName': 'string',
                    'UserName': 'string',
                    'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                    'SendEmailNotification': True|False
                },
                'ErrorCode': 'STACK_NOT_FOUND'|'USER_NAME_NOT_FOUND'|'INTERNAL_ERROR',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def copy_image(SourceImageName=None, DestinationImageName=None, DestinationRegion=None, DestinationImageDescription=None):
    """
    Copies the image within the same region or to a new region within the same AWS account. Note that any tags you added to the image will not be copied.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.copy_image(
        SourceImageName='string',
        DestinationImageName='string',
        DestinationRegion='string',
        DestinationImageDescription='string'
    )
    
    
    :type SourceImageName: string
    :param SourceImageName: [REQUIRED]\nThe name of the image to copy.\n

    :type DestinationImageName: string
    :param DestinationImageName: [REQUIRED]\nThe name that the image will have when it is copied to the destination.\n

    :type DestinationRegion: string
    :param DestinationRegion: [REQUIRED]\nThe destination region to which the image will be copied. This parameter is required, even if you are copying an image within the same region.\n

    :type DestinationImageDescription: string
    :param DestinationImageDescription: The description that the image will have when it is copied to the destination.

    :rtype: dict

ReturnsResponse Syntax
{
    'DestinationImageName': 'string'
}


Response Structure

(dict) --

DestinationImageName (string) --
The name of the destination image.







Exceptions

AppStream.Client.exceptions.ResourceAlreadyExistsException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ResourceNotAvailableException
AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.IncompatibleImageException


    :return: {
        'DestinationImageName': 'string'
    }
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceAlreadyExistsException
    AppStream.Client.exceptions.ResourceNotFoundException
    AppStream.Client.exceptions.ResourceNotAvailableException
    AppStream.Client.exceptions.LimitExceededException
    AppStream.Client.exceptions.InvalidAccountStatusException
    AppStream.Client.exceptions.IncompatibleImageException
    
    """
    pass

def create_directory_config(DirectoryName=None, OrganizationalUnitDistinguishedNames=None, ServiceAccountCredentials=None):
    """
    Creates a Directory Config object in AppStream 2.0. This object includes the configuration information required to join fleets and image builders to Microsoft Active Directory domains.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryName: [REQUIRED]\nThe fully qualified name of the directory (for example, corp.example.com).\n

    :type OrganizationalUnitDistinguishedNames: list
    :param OrganizationalUnitDistinguishedNames: [REQUIRED]\nThe distinguished names of the organizational units for computer accounts.\n\n(string) --\n\n

    :type ServiceAccountCredentials: dict
    :param ServiceAccountCredentials: [REQUIRED]\nThe credentials for the service account used by the fleet or image builder to connect to the directory.\n\nAccountName (string) -- [REQUIRED]The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.\n\nAccountPassword (string) -- [REQUIRED]The password for the account.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

DirectoryConfig (dict) --
Information about the directory configuration.

DirectoryName (string) --
The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedNames (list) --
The distinguished names of the organizational units for computer accounts.

(string) --


ServiceAccountCredentials (dict) --
The credentials for the service account used by the fleet or image builder to connect to the directory.

AccountName (string) --
The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.

AccountPassword (string) --
The password for the account.



CreatedTime (datetime) --
The time the directory configuration was created.









Exceptions

AppStream.Client.exceptions.ResourceAlreadyExistsException
AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException


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

def create_fleet(Name=None, ImageName=None, ImageArn=None, InstanceType=None, FleetType=None, ComputeCapacity=None, VpcConfig=None, MaxUserDurationInSeconds=None, DisconnectTimeoutInSeconds=None, Description=None, DisplayName=None, EnableDefaultInternetAccess=None, DomainJoinInfo=None, Tags=None, IdleDisconnectTimeoutInSeconds=None, IamRoleArn=None):
    """
    Creates a fleet. A fleet consists of streaming instances that run a specified image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_fleet(
        Name='string',
        ImageName='string',
        ImageArn='string',
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
        },
        Tags={
            'string': 'string'
        },
        IdleDisconnectTimeoutInSeconds=123,
        IamRoleArn='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA unique name for the fleet.\n

    :type ImageName: string
    :param ImageName: The name of the image used to create the fleet.

    :type ImageArn: string
    :param ImageArn: The ARN of the public, private, or shared image to use.

    :type InstanceType: string
    :param InstanceType: [REQUIRED]\nThe instance type to use when launching fleet instances. The following instance types are available:\n\nstream.standard.medium\nstream.standard.large\nstream.compute.large\nstream.compute.xlarge\nstream.compute.2xlarge\nstream.compute.4xlarge\nstream.compute.8xlarge\nstream.memory.large\nstream.memory.xlarge\nstream.memory.2xlarge\nstream.memory.4xlarge\nstream.memory.8xlarge\nstream.graphics-design.large\nstream.graphics-design.xlarge\nstream.graphics-design.2xlarge\nstream.graphics-design.4xlarge\nstream.graphics-desktop.2xlarge\nstream.graphics-pro.4xlarge\nstream.graphics-pro.8xlarge\nstream.graphics-pro.16xlarge\n\n

    :type FleetType: string
    :param FleetType: The fleet type.\n\nALWAYS_ON\nProvides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.\n\nON_DEMAND\nProvide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.\n

    :type ComputeCapacity: dict
    :param ComputeCapacity: [REQUIRED]\nThe desired capacity for the fleet.\n\nDesiredInstances (integer) -- [REQUIRED]The desired number of streaming instances.\n\n\n

    :type VpcConfig: dict
    :param VpcConfig: The VPC configuration for the fleet.\n\nSubnetIds (list) --The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.\n\n(string) --\n\n\nSecurityGroupIds (list) --The identifiers of the security groups for the fleet or image builder.\n\n(string) --\n\n\n\n

    :type MaxUserDurationInSeconds: integer
    :param MaxUserDurationInSeconds: The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.\nSpecify a value between 600 and 360000.\n

    :type DisconnectTimeoutInSeconds: integer
    :param DisconnectTimeoutInSeconds: The amount of time that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.\nSpecify a value between 60 and 360000.\n

    :type Description: string
    :param Description: The description to display.

    :type DisplayName: string
    :param DisplayName: The fleet name to display.

    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: Enables or disables default internet access for the fleet.

    :type DomainJoinInfo: dict
    :param DomainJoinInfo: The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.\n\nDirectoryName (string) --The fully qualified name of the directory (for example, corp.example.com).\n\nOrganizationalUnitDistinguishedName (string) --The distinguished name of the organizational unit for computer accounts.\n\n\n

    :type Tags: dict
    :param Tags: The tags to associate with the fleet. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=.\nIf you do not specify a value, the value is set to an empty string.\nGenerally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters:\n_ . : / = + - @\nFor more information, see Tagging Your Resources in the Amazon AppStream 2.0 Administration Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type IdleDisconnectTimeoutInSeconds: integer
    :param IdleDisconnectTimeoutInSeconds: The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the DisconnectTimeoutInSeconds time interval begins. Users are notified before they are disconnected due to inactivity. If they try to reconnect to the streaming session before the time interval specified in DisconnectTimeoutInSeconds elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in IdleDisconnectTimeoutInSeconds elapses, they are disconnected.\nTo prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 3600. The default value is 0.\n\nNote\nIf you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don\'t do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.\n\n

    :type IamRoleArn: string
    :param IamRoleArn: The Amazon Resource Name (ARN) of the IAM role to apply to the fleet. To assume a role, a fleet instance calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.\nFor more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Fleet': {
        'Arn': 'string',
        'Name': 'string',
        'DisplayName': 'string',
        'Description': 'string',
        'ImageName': 'string',
        'ImageArn': 'string',
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
                'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                'ErrorMessage': 'string'
            },
        ],
        'EnableDefaultInternetAccess': True|False,
        'DomainJoinInfo': {
            'DirectoryName': 'string',
            'OrganizationalUnitDistinguishedName': 'string'
        },
        'IdleDisconnectTimeoutInSeconds': 123,
        'IamRoleArn': 'string'
    }
}


Response Structure

(dict) --

Fleet (dict) --
Information about the fleet.

Arn (string) --
The Amazon Resource Name (ARN) for the fleet.

Name (string) --
The name of the fleet.

DisplayName (string) --
The fleet name to display.

Description (string) --
The description to display.

ImageName (string) --
The name of the image used to create the fleet.

ImageArn (string) --
The ARN for the public, private, or shared image.

InstanceType (string) --
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


FleetType (string) --
The fleet type.

ALWAYS_ON

Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.

ON_DEMAND

Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.

ComputeCapacityStatus (dict) --
The capacity status for the fleet.

Desired (integer) --
The desired number of streaming instances.

Running (integer) --
The total number of simultaneous streaming instances that are running.

InUse (integer) --
The number of instances in use for streaming.

Available (integer) --
The number of currently available instances that can be used to stream sessions.



MaxUserDurationInSeconds (integer) --
The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
Specify a value between 600 and 360000.

DisconnectTimeoutInSeconds (integer) --
The amount of time that a streaming session remains active after users disconnect. If they try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
Specify a value between 60 and 360000.

State (string) --
The current state for the fleet.

VpcConfig (dict) --
The VPC configuration for the fleet.

SubnetIds (list) --
The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string) --


SecurityGroupIds (list) --
The identifiers of the security groups for the fleet or image builder.

(string) --




CreatedTime (datetime) --
The time the fleet was created.

FleetErrors (list) --
The fleet errors.

(dict) --
Describes a fleet error.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.





EnableDefaultInternetAccess (boolean) --
Indicates whether default internet access is enabled for the fleet.

DomainJoinInfo (dict) --
The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.

DirectoryName (string) --
The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName (string) --
The distinguished name of the organizational unit for computer accounts.



IdleDisconnectTimeoutInSeconds (integer) --
The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the DisconnectTimeoutInSeconds time interval begins. Users are notified before they are disconnected due to inactivity. If users try to reconnect to the streaming session before the time interval specified in DisconnectTimeoutInSeconds elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in IdleDisconnectTimeoutInSeconds elapses, they are disconnected.
To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 3600. The default value is 0.

Note
If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don\'t do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.


IamRoleArn (string) --
The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.
For more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .









Exceptions

AppStream.Client.exceptions.ResourceAlreadyExistsException
AppStream.Client.exceptions.ResourceNotAvailableException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.InvalidRoleException
AppStream.Client.exceptions.ConcurrentModificationException
AppStream.Client.exceptions.InvalidParameterCombinationException
AppStream.Client.exceptions.IncompatibleImageException
AppStream.Client.exceptions.OperationNotPermittedException


    :return: {
        'Fleet': {
            'Arn': 'string',
            'Name': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'ImageName': 'string',
            'ImageArn': 'string',
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
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ],
            'EnableDefaultInternetAccess': True|False,
            'DomainJoinInfo': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedName': 'string'
            },
            'IdleDisconnectTimeoutInSeconds': 123,
            'IamRoleArn': 'string'
        }
    }
    
    
    :returns: 
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
    
    """
    pass

def create_image_builder(Name=None, ImageName=None, ImageArn=None, InstanceType=None, Description=None, DisplayName=None, VpcConfig=None, IamRoleArn=None, EnableDefaultInternetAccess=None, DomainJoinInfo=None, AppstreamAgentVersion=None, Tags=None, AccessEndpoints=None):
    """
    Creates an image builder. An image builder is a virtual machine that is used to create an image.
    The initial state of the builder is PENDING . When it is ready, the state is RUNNING .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_image_builder(
        Name='string',
        ImageName='string',
        ImageArn='string',
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
        IamRoleArn='string',
        EnableDefaultInternetAccess=True|False,
        DomainJoinInfo={
            'DirectoryName': 'string',
            'OrganizationalUnitDistinguishedName': 'string'
        },
        AppstreamAgentVersion='string',
        Tags={
            'string': 'string'
        },
        AccessEndpoints=[
            {
                'EndpointType': 'STREAMING',
                'VpceId': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA unique name for the image builder.\n

    :type ImageName: string
    :param ImageName: The name of the image used to create the image builder.

    :type ImageArn: string
    :param ImageArn: The ARN of the public, private, or shared image to use.

    :type InstanceType: string
    :param InstanceType: [REQUIRED]\nThe instance type to use when launching the image builder. The following instance types are available:\n\nstream.standard.medium\nstream.standard.large\nstream.compute.large\nstream.compute.xlarge\nstream.compute.2xlarge\nstream.compute.4xlarge\nstream.compute.8xlarge\nstream.memory.large\nstream.memory.xlarge\nstream.memory.2xlarge\nstream.memory.4xlarge\nstream.memory.8xlarge\nstream.graphics-design.large\nstream.graphics-design.xlarge\nstream.graphics-design.2xlarge\nstream.graphics-design.4xlarge\nstream.graphics-desktop.2xlarge\nstream.graphics-pro.4xlarge\nstream.graphics-pro.8xlarge\nstream.graphics-pro.16xlarge\n\n

    :type Description: string
    :param Description: The description to display.

    :type DisplayName: string
    :param DisplayName: The image builder name to display.

    :type VpcConfig: dict
    :param VpcConfig: The VPC configuration for the image builder. You can specify only one subnet.\n\nSubnetIds (list) --The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.\n\n(string) --\n\n\nSecurityGroupIds (list) --The identifiers of the security groups for the fleet or image builder.\n\n(string) --\n\n\n\n

    :type IamRoleArn: string
    :param IamRoleArn: The Amazon Resource Name (ARN) of the IAM role to apply to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.\nFor more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .\n

    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: Enables or disables default internet access for the image builder.

    :type DomainJoinInfo: dict
    :param DomainJoinInfo: The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.\n\nDirectoryName (string) --The fully qualified name of the directory (for example, corp.example.com).\n\nOrganizationalUnitDistinguishedName (string) --The distinguished name of the organizational unit for computer accounts.\n\n\n

    :type AppstreamAgentVersion: string
    :param AppstreamAgentVersion: The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].

    :type Tags: dict
    :param Tags: The tags to associate with the image builder. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=.\nGenerally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters:\n_ . : / = + - @\nIf you do not specify a value, the value is set to an empty string.\nFor more information about tags, see Tagging Your Resources in the Amazon AppStream 2.0 Administration Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type AccessEndpoints: list
    :param AccessEndpoints: The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the image builder only through the specified endpoints.\n\n(dict) --Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.\n\nEndpointType (string) -- [REQUIRED]The type of interface endpoint.\n\nVpceId (string) --The identifier (ID) of the VPC in which the interface endpoint is used.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
        'IamRoleArn': 'string',
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
        'NetworkAccessConfiguration': {
            'EniPrivateIpAddress': 'string',
            'EniId': 'string'
        },
        'ImageBuilderErrors': [
            {
                'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                'ErrorMessage': 'string',
                'ErrorTimestamp': datetime(2015, 1, 1)
            },
        ],
        'AppstreamAgentVersion': 'string',
        'AccessEndpoints': [
            {
                'EndpointType': 'STREAMING',
                'VpceId': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ImageBuilder (dict) --
Information about the image builder.

Name (string) --
The name of the image builder.

Arn (string) --
The ARN for the image builder.

ImageArn (string) --
The ARN of the image from which this builder was created.

Description (string) --
The description to display.

DisplayName (string) --
The image builder name to display.

VpcConfig (dict) --
The VPC configuration of the image builder.

SubnetIds (list) --
The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string) --


SecurityGroupIds (list) --
The identifiers of the security groups for the fleet or image builder.

(string) --




InstanceType (string) --
The instance type for the image builder. The following instance types are available:

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


Platform (string) --
The operating system platform of the image builder.

IamRoleArn (string) --
The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.
For more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .

State (string) --
The state of the image builder.

StateChangeReason (dict) --
The reason why the last state change occurred.

Code (string) --
The state change reason code.

Message (string) --
The state change reason message.



CreatedTime (datetime) --
The time stamp when the image builder was created.

EnableDefaultInternetAccess (boolean) --
Enables or disables default internet access for the image builder.

DomainJoinInfo (dict) --
The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.

DirectoryName (string) --
The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName (string) --
The distinguished name of the organizational unit for computer accounts.



NetworkAccessConfiguration (dict) --
Describes the network details of the fleet or image builder instance.

EniPrivateIpAddress (string) --
The private IP address of the elastic network interface that is attached to instances in your VPC.

EniId (string) --
The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.



ImageBuilderErrors (list) --
The image builder errors.

(dict) --
Describes a resource error.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.

ErrorTimestamp (datetime) --
The time the error occurred.





AppstreamAgentVersion (string) --
The version of the AppStream 2.0 agent that is currently being used by the image builder.

AccessEndpoints (list) --
The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.

(dict) --
Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType (string) --
The type of interface endpoint.

VpceId (string) --
The identifier (ID) of the VPC in which the interface endpoint is used.













Exceptions

AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.ResourceAlreadyExistsException
AppStream.Client.exceptions.ResourceNotAvailableException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.InvalidRoleException
AppStream.Client.exceptions.ConcurrentModificationException
AppStream.Client.exceptions.InvalidParameterCombinationException
AppStream.Client.exceptions.IncompatibleImageException
AppStream.Client.exceptions.OperationNotPermittedException


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
            'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
            'IamRoleArn': 'string',
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
            'NetworkAccessConfiguration': {
                'EniPrivateIpAddress': 'string',
                'EniId': 'string'
            },
            'ImageBuilderErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string',
                    'ErrorTimestamp': datetime(2015, 1, 1)
                },
            ],
            'AppstreamAgentVersion': 'string',
            'AccessEndpoints': [
                {
                    'EndpointType': 'STREAMING',
                    'VpceId': 'string'
                },
            ]
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
    
    Exceptions
    
    :example: response = client.create_image_builder_streaming_url(
        Name='string',
        Validity=123
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the image builder.\n

    :type Validity: integer
    :param Validity: The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamingURL': 'string',
    'Expires': datetime(2015, 1, 1)
}


Response Structure

(dict) --

StreamingURL (string) --
The URL to start the AppStream 2.0 streaming session.

Expires (datetime) --
The elapsed time, in seconds after the Unix epoch, when this URL expires.







Exceptions

AppStream.Client.exceptions.OperationNotPermittedException
AppStream.Client.exceptions.ResourceNotFoundException


    :return: {
        'StreamingURL': 'string',
        'Expires': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    AppStream.Client.exceptions.OperationNotPermittedException
    AppStream.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_stack(Name=None, Description=None, DisplayName=None, StorageConnectors=None, RedirectURL=None, FeedbackURL=None, UserSettings=None, ApplicationSettings=None, Tags=None, AccessEndpoints=None, EmbedHostDomains=None):
    """
    Creates a stack to start streaming applications to users. A stack consists of an associated fleet, user access policies, and storage configurations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_stack(
        Name='string',
        Description='string',
        DisplayName='string',
        StorageConnectors=[
            {
                'ConnectorType': 'HOMEFOLDERS'|'GOOGLE_DRIVE'|'ONE_DRIVE',
                'ResourceIdentifier': 'string',
                'Domains': [
                    'string',
                ]
            },
        ],
        RedirectURL='string',
        FeedbackURL='string',
        UserSettings=[
            {
                'Action': 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE'|'CLIPBOARD_COPY_TO_LOCAL_DEVICE'|'FILE_UPLOAD'|'FILE_DOWNLOAD'|'PRINTING_TO_LOCAL_DEVICE',
                'Permission': 'ENABLED'|'DISABLED'
            },
        ],
        ApplicationSettings={
            'Enabled': True|False,
            'SettingsGroup': 'string'
        },
        Tags={
            'string': 'string'
        },
        AccessEndpoints=[
            {
                'EndpointType': 'STREAMING',
                'VpceId': 'string'
            },
        ],
        EmbedHostDomains=[
            'string',
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the stack.\n

    :type Description: string
    :param Description: The description to display.

    :type DisplayName: string
    :param DisplayName: The stack name to display.

    :type StorageConnectors: list
    :param StorageConnectors: The storage connectors to enable.\n\n(dict) --Describes a connector that enables persistent storage for users.\n\nConnectorType (string) -- [REQUIRED]The type of storage connector.\n\nResourceIdentifier (string) --The ARN of the storage connector.\n\nDomains (list) --The names of the domains for the account.\n\n(string) -- GSuite domain for GDrive integration.\n\n\n\n\n\n

    :type RedirectURL: string
    :param RedirectURL: The URL that users are redirected to after their streaming session ends.

    :type FeedbackURL: string
    :param FeedbackURL: The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.

    :type UserSettings: list
    :param UserSettings: The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.\n\n(dict) --Describes an action and whether the action is enabled or disabled for users during their streaming sessions.\n\nAction (string) -- [REQUIRED]The action that is enabled or disabled.\n\nPermission (string) -- [REQUIRED]Indicates whether the action is enabled or disabled.\n\n\n\n\n

    :type ApplicationSettings: dict
    :param ApplicationSettings: The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.\n\nEnabled (boolean) -- [REQUIRED]Enables or disables persistent application settings for users during their streaming sessions.\n\nSettingsGroup (string) --The path prefix for the S3 bucket where users\xe2\x80\x99 persistent application settings are stored. You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack.\n\n\n

    :type Tags: dict
    :param Tags: The tags to associate with the stack. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=.\nIf you do not specify a value, the value is set to an empty string.\nGenerally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters:\n_ . : / = + - @\nFor more information about tags, see Tagging Your Resources in the Amazon AppStream 2.0 Administration Guide .\n\n(string) --\n(string) --\n\n\n\n

    :type AccessEndpoints: list
    :param AccessEndpoints: The list of interface VPC endpoint (interface endpoint) objects. Users of the stack can connect to AppStream 2.0 only through the specified endpoints.\n\n(dict) --Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.\n\nEndpointType (string) -- [REQUIRED]The type of interface endpoint.\n\nVpceId (string) --The identifier (ID) of the VPC in which the interface endpoint is used.\n\n\n\n\n

    :type EmbedHostDomains: list
    :param EmbedHostDomains: The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.\n\n(string) -- Specifies a valid domain that can embed AppStream. Valid examples include: ['testorigin.tt--com', 'testingorigin.com.us', 'test.com.us'] Invalid examples include: ['test,com', '.com', 'h*llo.com'. '']\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Stack': {
        'Arn': 'string',
        'Name': 'string',
        'Description': 'string',
        'DisplayName': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'StorageConnectors': [
            {
                'ConnectorType': 'HOMEFOLDERS'|'GOOGLE_DRIVE'|'ONE_DRIVE',
                'ResourceIdentifier': 'string',
                'Domains': [
                    'string',
                ]
            },
        ],
        'RedirectURL': 'string',
        'FeedbackURL': 'string',
        'StackErrors': [
            {
                'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                'ErrorMessage': 'string'
            },
        ],
        'UserSettings': [
            {
                'Action': 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE'|'CLIPBOARD_COPY_TO_LOCAL_DEVICE'|'FILE_UPLOAD'|'FILE_DOWNLOAD'|'PRINTING_TO_LOCAL_DEVICE',
                'Permission': 'ENABLED'|'DISABLED'
            },
        ],
        'ApplicationSettings': {
            'Enabled': True|False,
            'SettingsGroup': 'string',
            'S3BucketName': 'string'
        },
        'AccessEndpoints': [
            {
                'EndpointType': 'STREAMING',
                'VpceId': 'string'
            },
        ],
        'EmbedHostDomains': [
            'string',
        ]
    }
}


Response Structure

(dict) --

Stack (dict) --
Information about the stack.

Arn (string) --
The ARN of the stack.

Name (string) --
The name of the stack.

Description (string) --
The description to display.

DisplayName (string) --
The stack name to display.

CreatedTime (datetime) --
The time the stack was created.

StorageConnectors (list) --
The storage connectors to enable.

(dict) --
Describes a connector that enables persistent storage for users.

ConnectorType (string) --
The type of storage connector.

ResourceIdentifier (string) --
The ARN of the storage connector.

Domains (list) --
The names of the domains for the account.

(string) -- GSuite domain for GDrive integration.






RedirectURL (string) --
The URL that users are redirected to after their streaming session ends.

FeedbackURL (string) --
The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.

StackErrors (list) --
The errors for the stack.

(dict) --
Describes a stack error.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.





UserSettings (list) --
The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.

(dict) --
Describes an action and whether the action is enabled or disabled for users during their streaming sessions.

Action (string) --
The action that is enabled or disabled.

Permission (string) --
Indicates whether the action is enabled or disabled.





ApplicationSettings (dict) --
The persistent application settings for users of the stack.

Enabled (boolean) --
Specifies whether persistent application settings are enabled for users during their streaming sessions.

SettingsGroup (string) --
The path prefix for the S3 bucket where users\xe2\x80\x99 persistent application settings are stored.

S3BucketName (string) --
The S3 bucket where users\xe2\x80\x99 persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region.



AccessEndpoints (list) --
The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to AppStream 2.0 only through the specified endpoints.

(dict) --
Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType (string) --
The type of interface endpoint.

VpceId (string) --
The identifier (ID) of the VPC in which the interface endpoint is used.





EmbedHostDomains (list) --
The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

(string) -- Specifies a valid domain that can embed AppStream. Valid examples include: ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples include: ["test,com", ".com", "h*llo.com". ""]










Exceptions

AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.ResourceAlreadyExistsException
AppStream.Client.exceptions.ConcurrentModificationException
AppStream.Client.exceptions.InvalidRoleException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Stack': {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'StorageConnectors': [
                {
                    'ConnectorType': 'HOMEFOLDERS'|'GOOGLE_DRIVE'|'ONE_DRIVE',
                    'ResourceIdentifier': 'string',
                    'Domains': [
                        'string',
                    ]
                },
            ],
            'RedirectURL': 'string',
            'FeedbackURL': 'string',
            'StackErrors': [
                {
                    'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ],
            'UserSettings': [
                {
                    'Action': 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE'|'CLIPBOARD_COPY_TO_LOCAL_DEVICE'|'FILE_UPLOAD'|'FILE_DOWNLOAD'|'PRINTING_TO_LOCAL_DEVICE',
                    'Permission': 'ENABLED'|'DISABLED'
                },
            ],
            'ApplicationSettings': {
                'Enabled': True|False,
                'SettingsGroup': 'string',
                'S3BucketName': 'string'
            },
            'AccessEndpoints': [
                {
                    'EndpointType': 'STREAMING',
                    'VpceId': 'string'
                },
            ],
            'EmbedHostDomains': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) -- GSuite domain for GDrive integration.
    
    """
    pass

def create_streaming_url(StackName=None, FleetName=None, UserId=None, ApplicationId=None, Validity=None, SessionContext=None):
    """
    Creates a temporary URL to start an AppStream 2.0 streaming session for the specified user. A streaming URL enables application streaming to be tested without user setup.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_streaming_url(
        StackName='string',
        FleetName='string',
        UserId='string',
        ApplicationId='string',
        Validity=123,
        SessionContext='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name of the stack.\n

    :type FleetName: string
    :param FleetName: [REQUIRED]\nThe name of the fleet.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe identifier of the user.\n

    :type ApplicationId: string
    :param ApplicationId: The name of the application to launch after the session starts. This is the name that you specified as Name in the Image Assistant.

    :type Validity: integer
    :param Validity: The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 60 seconds.

    :type SessionContext: string
    :param SessionContext: The session context. For more information, see Session Context in the Amazon AppStream 2.0 Administration Guide .

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamingURL': 'string',
    'Expires': datetime(2015, 1, 1)
}


Response Structure

(dict) --

StreamingURL (string) --
The URL to start the AppStream 2.0 streaming session.

Expires (datetime) --
The elapsed time, in seconds after the Unix epoch, when this URL expires.







Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ResourceNotAvailableException
AppStream.Client.exceptions.OperationNotPermittedException
AppStream.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'StreamingURL': 'string',
        'Expires': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceNotFoundException
    AppStream.Client.exceptions.ResourceNotAvailableException
    AppStream.Client.exceptions.OperationNotPermittedException
    AppStream.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def create_usage_report_subscription():
    """
    Creates a usage report subscription.  reports are generated daily.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_usage_report_subscription()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'S3BucketName': 'string',
    'Schedule': 'DAILY'
}


Response Structure

(dict) --
S3BucketName (string) --The Amazon S3 bucket where generated reports are stored.
If you enabled on-instance session scripts and Amazon S3 logging for your session script configuration, AppStream 2.0 created an S3 bucket to store the script output. The bucket is unique to your account and Region. When you enable usage reporting in this case, AppStream 2.0 uses the same bucket to store your usage reports. If you haven\'t already enabled on-instance session scripts, when you enable usage reports, AppStream 2.0 creates a new S3 bucket.

Schedule (string) --The schedule for generating usage reports.






Exceptions

AppStream.Client.exceptions.InvalidRoleException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.LimitExceededException


    :return: {
        'S3BucketName': 'string',
        'Schedule': 'DAILY'
    }
    
    
    """
    pass

def create_user(UserName=None, MessageAction=None, FirstName=None, LastName=None, AuthenticationType=None):
    """
    Creates a new user in the user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user(
        UserName='string',
        MessageAction='SUPPRESS'|'RESEND',
        FirstName='string',
        LastName='string',
        AuthenticationType='API'|'SAML'|'USERPOOL'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe email address of the user.\n\nNote\nUsers\' email addresses are case-sensitive. During login, if they specify an email address that doesn\'t use the same capitalization as the email address specified when their user pool account was created, a 'user does not exist' error message displays.\n\n

    :type MessageAction: string
    :param MessageAction: The action to take for the welcome email that is sent to a user after the user is created in the user pool. If you specify SUPPRESS, no email is sent. If you specify RESEND, do not specify the first name or last name of the user. If the value is null, the email is sent.\n\nNote\nThe temporary password in the welcome email is valid for only 7 days. If users don\xe2\x80\x99t set their passwords within 7 days, you must send them a new welcome email.\n\n

    :type FirstName: string
    :param FirstName: The first name, or given name, of the user.

    :type LastName: string
    :param LastName: The last name, or surname, of the user.

    :type AuthenticationType: string
    :param AuthenticationType: [REQUIRED]\nThe authentication type for the user. You must specify USERPOOL.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.ResourceAlreadyExistsException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.InvalidParameterCombinationException
AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.OperationNotPermittedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_directory_config(DirectoryName=None):
    """
    Deletes the specified Directory Config object from AppStream 2.0. This object includes the information required to join streaming instances to an Active Directory domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_directory_config(
        DirectoryName='string'
    )
    
    
    :type DirectoryName: string
    :param DirectoryName: [REQUIRED]\nThe name of the directory configuration.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AppStream.Client.exceptions.ResourceInUseException
AppStream.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceInUseException
    AppStream.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def delete_fleet(Name=None):
    """
    Deletes the specified fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_fleet(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AppStream.Client.exceptions.ResourceInUseException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceInUseException
    AppStream.Client.exceptions.ResourceNotFoundException
    AppStream.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_image(Name=None):
    """
    Deletes the specified image. You cannot delete an image when it is in use. After you delete an image, you cannot provision new capacity using the image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_image(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the image.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Image': {
        'Name': 'string',
        'Arn': 'string',
        'BaseImageArn': 'string',
        'DisplayName': 'string',
        'State': 'PENDING'|'AVAILABLE'|'FAILED'|'COPYING'|'DELETING',
        'Visibility': 'PUBLIC'|'PRIVATE'|'SHARED',
        'ImageBuilderSupported': True|False,
        'ImageBuilderName': 'string',
        'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
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
        'AppstreamAgentVersion': 'string',
        'ImagePermissions': {
            'allowFleet': True|False,
            'allowImageBuilder': True|False
        }
    }
}


Response Structure

(dict) --
Image (dict) --Information about the image.

Name (string) --The name of the image.

Arn (string) --The ARN of the image.

BaseImageArn (string) --The ARN of the image from which this image was created.

DisplayName (string) --The image name to display.

State (string) --The image starts in the PENDING state. If image creation succeeds, the state is AVAILABLE . If image creation fails, the state is FAILED .

Visibility (string) --Indicates whether the image is public or private.

ImageBuilderSupported (boolean) --Indicates whether an image builder can be launched from this image.

ImageBuilderName (string) --The name of the image builder that was used to create the private image. If the image is shared, this value is null.

Platform (string) --The operating system platform of the image.

Description (string) --The description to display.

StateChangeReason (dict) --The reason why the last state change occurred.

Code (string) --The state change reason code.

Message (string) --The state change reason message.



Applications (list) --The applications associated with the image.

(dict) --Describes an application in the application catalog.

Name (string) --The name of the application.

DisplayName (string) --The application name to display.

IconURL (string) --The URL for the application icon. This URL might be time-limited.

LaunchPath (string) --The path to the application executable in the instance.

LaunchParameters (string) --The arguments that are passed to the application at launch.

Enabled (boolean) --If there is a problem, the application can be disabled after image creation.

Metadata (dict) --Additional attributes that describe the application.

(string) --
(string) --








CreatedTime (datetime) --The time the image was created.

PublicBaseImageReleasedDate (datetime) --The release date of the public base image. For private images, this date is the release date of the base image from which the image was created.

AppstreamAgentVersion (string) --The version of the AppStream 2.0 agent to use for instances that are launched from this image.

ImagePermissions (dict) --The permissions to provide to the destination AWS account for the specified image.

allowFleet (boolean) --Indicates whether the image can be used for a fleet.

allowImageBuilder (boolean) --Indicates whether the image can be used for an image builder.










Exceptions

AppStream.Client.exceptions.ResourceInUseException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.OperationNotPermittedException
AppStream.Client.exceptions.ConcurrentModificationException


    :return: {
        'Image': {
            'Name': 'string',
            'Arn': 'string',
            'BaseImageArn': 'string',
            'DisplayName': 'string',
            'State': 'PENDING'|'AVAILABLE'|'FAILED'|'COPYING'|'DELETING',
            'Visibility': 'PUBLIC'|'PRIVATE'|'SHARED',
            'ImageBuilderSupported': True|False,
            'ImageBuilderName': 'string',
            'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
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
            'AppstreamAgentVersion': 'string',
            'ImagePermissions': {
                'allowFleet': True|False,
                'allowImageBuilder': True|False
            }
        }
    }
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceInUseException
    AppStream.Client.exceptions.ResourceNotFoundException
    AppStream.Client.exceptions.OperationNotPermittedException
    AppStream.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_image_builder(Name=None):
    """
    Deletes the specified image builder and releases the capacity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_image_builder(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the image builder.\n

    :rtype: dict
ReturnsResponse Syntax{
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
        'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
        'IamRoleArn': 'string',
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
        'NetworkAccessConfiguration': {
            'EniPrivateIpAddress': 'string',
            'EniId': 'string'
        },
        'ImageBuilderErrors': [
            {
                'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                'ErrorMessage': 'string',
                'ErrorTimestamp': datetime(2015, 1, 1)
            },
        ],
        'AppstreamAgentVersion': 'string',
        'AccessEndpoints': [
            {
                'EndpointType': 'STREAMING',
                'VpceId': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
ImageBuilder (dict) --Information about the image builder.

Name (string) --The name of the image builder.

Arn (string) --The ARN for the image builder.

ImageArn (string) --The ARN of the image from which this builder was created.

Description (string) --The description to display.

DisplayName (string) --The image builder name to display.

VpcConfig (dict) --The VPC configuration of the image builder.

SubnetIds (list) --The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string) --


SecurityGroupIds (list) --The identifiers of the security groups for the fleet or image builder.

(string) --




InstanceType (string) --The instance type for the image builder. The following instance types are available:

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


Platform (string) --The operating system platform of the image builder.

IamRoleArn (string) --The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.
For more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .

State (string) --The state of the image builder.

StateChangeReason (dict) --The reason why the last state change occurred.

Code (string) --The state change reason code.

Message (string) --The state change reason message.



CreatedTime (datetime) --The time stamp when the image builder was created.

EnableDefaultInternetAccess (boolean) --Enables or disables default internet access for the image builder.

DomainJoinInfo (dict) --The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.

DirectoryName (string) --The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName (string) --The distinguished name of the organizational unit for computer accounts.



NetworkAccessConfiguration (dict) --Describes the network details of the fleet or image builder instance.

EniPrivateIpAddress (string) --The private IP address of the elastic network interface that is attached to instances in your VPC.

EniId (string) --The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.



ImageBuilderErrors (list) --The image builder errors.

(dict) --Describes a resource error.

ErrorCode (string) --The error code.

ErrorMessage (string) --The error message.

ErrorTimestamp (datetime) --The time the error occurred.





AppstreamAgentVersion (string) --The version of the AppStream 2.0 agent that is currently being used by the image builder.

AccessEndpoints (list) --The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.

(dict) --Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType (string) --The type of interface endpoint.

VpceId (string) --The identifier (ID) of the VPC in which the interface endpoint is used.












Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.OperationNotPermittedException
AppStream.Client.exceptions.ConcurrentModificationException


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
            'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
            'IamRoleArn': 'string',
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
            'NetworkAccessConfiguration': {
                'EniPrivateIpAddress': 'string',
                'EniId': 'string'
            },
            'ImageBuilderErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string',
                    'ErrorTimestamp': datetime(2015, 1, 1)
                },
            ],
            'AppstreamAgentVersion': 'string',
            'AccessEndpoints': [
                {
                    'EndpointType': 'STREAMING',
                    'VpceId': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_image_permissions(Name=None, SharedAccountId=None):
    """
    Deletes permissions for the specified private image. After you delete permissions for an image, AWS accounts to which you previously granted these permissions can no longer use the image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_image_permissions(
        Name='string',
        SharedAccountId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the private image.\n

    :type SharedAccountId: string
    :param SharedAccountId: [REQUIRED]\nThe 12-digit identifier of the AWS account for which to delete image permissions.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.ResourceNotAvailableException
AppStream.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_stack(Name=None):
    """
    Deletes the specified stack. After the stack is deleted, the application streaming environment provided by the stack is no longer available to users. Also, any reservations made for application streaming sessions for the stack are released.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stack(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the stack.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AppStream.Client.exceptions.ResourceInUseException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceInUseException
    AppStream.Client.exceptions.ResourceNotFoundException
    AppStream.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_usage_report_subscription():
    """
    Disables usage report generation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_usage_report_subscription()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    AppStream.Client.exceptions.InvalidAccountStatusException
    AppStream.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def delete_user(UserName=None, AuthenticationType=None):
    """
    Deletes a user from the user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user(
        UserName='string',
        AuthenticationType='API'|'SAML'|'USERPOOL'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe email address of the user.\n\nNote\nUsers\' email addresses are case-sensitive.\n\n

    :type AuthenticationType: string
    :param AuthenticationType: [REQUIRED]\nThe authentication type for the user. You must specify USERPOOL.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_directory_configs(DirectoryNames=None, MaxResults=None, NextToken=None):
    """
    Retrieves a list that describes one or more specified Directory Config objects for AppStream 2.0, if the names for these objects are provided. Otherwise, all Directory Config objects in the account are described. These objects include the configuration information required to join fleets and image builders to Microsoft Active Directory domains.
    Although the response syntax in this topic includes the account password, this password is not returned in the actual response.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_directory_configs(
        DirectoryNames=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DirectoryNames: list
    :param DirectoryNames: The directory names.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum size of each page of results.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

DirectoryConfigs (list) --
Information about the directory configurations. Note that although the response syntax in this topic includes the account password, this password is not returned in the actual response.

(dict) --
Describes the configuration information required to join fleets and image builders to Microsoft Active Directory domains.

DirectoryName (string) --
The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedNames (list) --
The distinguished names of the organizational units for computer accounts.

(string) --


ServiceAccountCredentials (dict) --
The credentials for the service account used by the fleet or image builder to connect to the directory.

AccountName (string) --
The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.

AccountPassword (string) --
The password for the account.



CreatedTime (datetime) --
The time the directory configuration was created.





NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.ResourceNotFoundException


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
    Retrieves a list that describes one or more specified fleets, if the fleet names are provided. Otherwise, all fleets in the account are described.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_fleets(
        Names=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: The names of the fleets to describe.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'Fleets': [
        {
            'Arn': 'string',
            'Name': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'ImageName': 'string',
            'ImageArn': 'string',
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
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ],
            'EnableDefaultInternetAccess': True|False,
            'DomainJoinInfo': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedName': 'string'
            },
            'IdleDisconnectTimeoutInSeconds': 123,
            'IamRoleArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Fleets (list) --
Information about the fleets.

(dict) --
Describes a fleet.

Arn (string) --
The Amazon Resource Name (ARN) for the fleet.

Name (string) --
The name of the fleet.

DisplayName (string) --
The fleet name to display.

Description (string) --
The description to display.

ImageName (string) --
The name of the image used to create the fleet.

ImageArn (string) --
The ARN for the public, private, or shared image.

InstanceType (string) --
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


FleetType (string) --
The fleet type.

ALWAYS_ON

Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.

ON_DEMAND

Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.

ComputeCapacityStatus (dict) --
The capacity status for the fleet.

Desired (integer) --
The desired number of streaming instances.

Running (integer) --
The total number of simultaneous streaming instances that are running.

InUse (integer) --
The number of instances in use for streaming.

Available (integer) --
The number of currently available instances that can be used to stream sessions.



MaxUserDurationInSeconds (integer) --
The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
Specify a value between 600 and 360000.

DisconnectTimeoutInSeconds (integer) --
The amount of time that a streaming session remains active after users disconnect. If they try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
Specify a value between 60 and 360000.

State (string) --
The current state for the fleet.

VpcConfig (dict) --
The VPC configuration for the fleet.

SubnetIds (list) --
The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string) --


SecurityGroupIds (list) --
The identifiers of the security groups for the fleet or image builder.

(string) --




CreatedTime (datetime) --
The time the fleet was created.

FleetErrors (list) --
The fleet errors.

(dict) --
Describes a fleet error.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.





EnableDefaultInternetAccess (boolean) --
Indicates whether default internet access is enabled for the fleet.

DomainJoinInfo (dict) --
The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.

DirectoryName (string) --
The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName (string) --
The distinguished name of the organizational unit for computer accounts.



IdleDisconnectTimeoutInSeconds (integer) --
The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the DisconnectTimeoutInSeconds time interval begins. Users are notified before they are disconnected due to inactivity. If users try to reconnect to the streaming session before the time interval specified in DisconnectTimeoutInSeconds elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in IdleDisconnectTimeoutInSeconds elapses, they are disconnected.
To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 3600. The default value is 0.

Note
If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don\'t do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.


IamRoleArn (string) --
The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.
For more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .





NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.ResourceNotFoundException


    :return: {
        'Fleets': [
            {
                'Arn': 'string',
                'Name': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'ImageName': 'string',
                'ImageArn': 'string',
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
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ],
                'EnableDefaultInternetAccess': True|False,
                'DomainJoinInfo': {
                    'DirectoryName': 'string',
                    'OrganizationalUnitDistinguishedName': 'string'
                },
                'IdleDisconnectTimeoutInSeconds': 123,
                'IamRoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
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
    
    """
    pass

def describe_image_builders(Names=None, MaxResults=None, NextToken=None):
    """
    Retrieves a list that describes one or more specified image builders, if the image builder names are provided. Otherwise, all image builders in the account are described.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_image_builders(
        Names=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: The names of the image builders to describe.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum size of each page of results.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
            'IamRoleArn': 'string',
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
            'NetworkAccessConfiguration': {
                'EniPrivateIpAddress': 'string',
                'EniId': 'string'
            },
            'ImageBuilderErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string',
                    'ErrorTimestamp': datetime(2015, 1, 1)
                },
            ],
            'AppstreamAgentVersion': 'string',
            'AccessEndpoints': [
                {
                    'EndpointType': 'STREAMING',
                    'VpceId': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ImageBuilders (list) --
Information about the image builders.

(dict) --
Describes a virtual machine that is used to create an image.

Name (string) --
The name of the image builder.

Arn (string) --
The ARN for the image builder.

ImageArn (string) --
The ARN of the image from which this builder was created.

Description (string) --
The description to display.

DisplayName (string) --
The image builder name to display.

VpcConfig (dict) --
The VPC configuration of the image builder.

SubnetIds (list) --
The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string) --


SecurityGroupIds (list) --
The identifiers of the security groups for the fleet or image builder.

(string) --




InstanceType (string) --
The instance type for the image builder. The following instance types are available:

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


Platform (string) --
The operating system platform of the image builder.

IamRoleArn (string) --
The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.
For more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .

State (string) --
The state of the image builder.

StateChangeReason (dict) --
The reason why the last state change occurred.

Code (string) --
The state change reason code.

Message (string) --
The state change reason message.



CreatedTime (datetime) --
The time stamp when the image builder was created.

EnableDefaultInternetAccess (boolean) --
Enables or disables default internet access for the image builder.

DomainJoinInfo (dict) --
The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.

DirectoryName (string) --
The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName (string) --
The distinguished name of the organizational unit for computer accounts.



NetworkAccessConfiguration (dict) --
Describes the network details of the fleet or image builder instance.

EniPrivateIpAddress (string) --
The private IP address of the elastic network interface that is attached to instances in your VPC.

EniId (string) --
The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.



ImageBuilderErrors (list) --
The image builder errors.

(dict) --
Describes a resource error.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.

ErrorTimestamp (datetime) --
The time the error occurred.





AppstreamAgentVersion (string) --
The version of the AppStream 2.0 agent that is currently being used by the image builder.

AccessEndpoints (list) --
The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.

(dict) --
Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType (string) --
The type of interface endpoint.

VpceId (string) --
The identifier (ID) of the VPC in which the interface endpoint is used.









NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.ResourceNotFoundException


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
                'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
                'IamRoleArn': 'string',
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
                'NetworkAccessConfiguration': {
                    'EniPrivateIpAddress': 'string',
                    'EniId': 'string'
                },
                'ImageBuilderErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string',
                        'ErrorTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'AppstreamAgentVersion': 'string',
                'AccessEndpoints': [
                    {
                        'EndpointType': 'STREAMING',
                        'VpceId': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_image_permissions(Name=None, MaxResults=None, SharedAwsAccountIds=None, NextToken=None):
    """
    Retrieves a list that describes the permissions for shared AWS account IDs on a private image that you own.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_image_permissions(
        Name='string',
        MaxResults=123,
        SharedAwsAccountIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the private image for which to describe permissions. The image must be one that you own.\n

    :type MaxResults: integer
    :param MaxResults: The maximum size of each page of results.

    :type SharedAwsAccountIds: list
    :param SharedAwsAccountIds: The 12-digit identifier of one or more AWS accounts with which the image is shared.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'SharedImagePermissionsList': [
        {
            'sharedAccountId': 'string',
            'imagePermissions': {
                'allowFleet': True|False,
                'allowImageBuilder': True|False
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Name (string) --
The name of the private image.

SharedImagePermissionsList (list) --
The permissions for a private image that you own.

(dict) --
Describes the permissions that are available to the specified AWS account for a shared image.

sharedAccountId (string) --
The 12-digit identifier of the AWS account with which the image is shared.

imagePermissions (dict) --
Describes the permissions for a shared image.

allowFleet (boolean) --
Indicates whether the image can be used for a fleet.

allowImageBuilder (boolean) --
Indicates whether the image can be used for an image builder.







NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.ResourceNotFoundException


    :return: {
        'Name': 'string',
        'SharedImagePermissionsList': [
            {
                'sharedAccountId': 'string',
                'imagePermissions': {
                    'allowFleet': True|False,
                    'allowImageBuilder': True|False
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_images(Names=None, Arns=None, Type=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list that describes one or more specified images, if the image names or image ARNs are provided. Otherwise, all images in the account are described.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_images(
        Names=[
            'string',
        ],
        Arns=[
            'string',
        ],
        Type='PUBLIC'|'PRIVATE'|'SHARED',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Names: list
    :param Names: The names of the public or private images to describe.\n\n(string) --\n\n

    :type Arns: list
    :param Arns: The ARNs of the public, private, and shared images to describe.\n\n(string) --\n\n

    :type Type: string
    :param Type: The type of image (public, private, or shared) to describe.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :type MaxResults: integer
    :param MaxResults: The maximum size of each page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Images': [
        {
            'Name': 'string',
            'Arn': 'string',
            'BaseImageArn': 'string',
            'DisplayName': 'string',
            'State': 'PENDING'|'AVAILABLE'|'FAILED'|'COPYING'|'DELETING',
            'Visibility': 'PUBLIC'|'PRIVATE'|'SHARED',
            'ImageBuilderSupported': True|False,
            'ImageBuilderName': 'string',
            'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
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
            'AppstreamAgentVersion': 'string',
            'ImagePermissions': {
                'allowFleet': True|False,
                'allowImageBuilder': True|False
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Images (list) --
Information about the images.

(dict) --
Describes an image.

Name (string) --
The name of the image.

Arn (string) --
The ARN of the image.

BaseImageArn (string) --
The ARN of the image from which this image was created.

DisplayName (string) --
The image name to display.

State (string) --
The image starts in the PENDING state. If image creation succeeds, the state is AVAILABLE . If image creation fails, the state is FAILED .

Visibility (string) --
Indicates whether the image is public or private.

ImageBuilderSupported (boolean) --
Indicates whether an image builder can be launched from this image.

ImageBuilderName (string) --
The name of the image builder that was used to create the private image. If the image is shared, this value is null.

Platform (string) --
The operating system platform of the image.

Description (string) --
The description to display.

StateChangeReason (dict) --
The reason why the last state change occurred.

Code (string) --
The state change reason code.

Message (string) --
The state change reason message.



Applications (list) --
The applications associated with the image.

(dict) --
Describes an application in the application catalog.

Name (string) --
The name of the application.

DisplayName (string) --
The application name to display.

IconURL (string) --
The URL for the application icon. This URL might be time-limited.

LaunchPath (string) --
The path to the application executable in the instance.

LaunchParameters (string) --
The arguments that are passed to the application at launch.

Enabled (boolean) --
If there is a problem, the application can be disabled after image creation.

Metadata (dict) --
Additional attributes that describe the application.

(string) --
(string) --








CreatedTime (datetime) --
The time the image was created.

PublicBaseImageReleasedDate (datetime) --
The release date of the public base image. For private images, this date is the release date of the base image from which the image was created.

AppstreamAgentVersion (string) --
The version of the AppStream 2.0 agent to use for instances that are launched from this image.

ImagePermissions (dict) --
The permissions to provide to the destination AWS account for the specified image.

allowFleet (boolean) --
Indicates whether the image can be used for a fleet.

allowImageBuilder (boolean) --
Indicates whether the image can be used for an image builder.







NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.InvalidParameterCombinationException
AppStream.Client.exceptions.ResourceNotFoundException


    :return: {
        'Images': [
            {
                'Name': 'string',
                'Arn': 'string',
                'BaseImageArn': 'string',
                'DisplayName': 'string',
                'State': 'PENDING'|'AVAILABLE'|'FAILED'|'COPYING'|'DELETING',
                'Visibility': 'PUBLIC'|'PRIVATE'|'SHARED',
                'ImageBuilderSupported': True|False,
                'ImageBuilderName': 'string',
                'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
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
                'AppstreamAgentVersion': 'string',
                'ImagePermissions': {
                    'allowFleet': True|False,
                    'allowImageBuilder': True|False
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_sessions(StackName=None, FleetName=None, UserId=None, NextToken=None, Limit=None, AuthenticationType=None):
    """
    Retrieves a list that describes the streaming sessions for a specified stack and fleet. If a UserId is provided for the stack and fleet, only streaming sessions for that user are described. If an authentication type is not provided, the default is to authenticate users using a streaming URL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_sessions(
        StackName='string',
        FleetName='string',
        UserId='string',
        NextToken='string',
        Limit=123,
        AuthenticationType='API'|'SAML'|'USERPOOL'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name of the stack. This value is case-sensitive.\n

    :type FleetName: string
    :param FleetName: [REQUIRED]\nThe name of the fleet. This value is case-sensitive.\n

    :type UserId: string
    :param UserId: The user identifier.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :type Limit: integer
    :param Limit: The size of each page of results. The default value is 20 and the maximum value is 50.

    :type AuthenticationType: string
    :param AuthenticationType: The authentication method. Specify API for a user authenticated using a streaming URL or SAML for a SAML federated user. The default is to authenticate users using a streaming URL.

    :rtype: dict

ReturnsResponse Syntax
{
    'Sessions': [
        {
            'Id': 'string',
            'UserId': 'string',
            'StackName': 'string',
            'FleetName': 'string',
            'State': 'ACTIVE'|'PENDING'|'EXPIRED',
            'ConnectionState': 'CONNECTED'|'NOT_CONNECTED',
            'StartTime': datetime(2015, 1, 1),
            'MaxExpirationTime': datetime(2015, 1, 1),
            'AuthenticationType': 'API'|'SAML'|'USERPOOL',
            'NetworkAccessConfiguration': {
                'EniPrivateIpAddress': 'string',
                'EniId': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Sessions (list) --
Information about the streaming sessions.

(dict) --
Describes a streaming session.

Id (string) --
The identifier of the streaming session.

UserId (string) --
The identifier of the user for whom the session was created.

StackName (string) --
The name of the stack for the streaming session.

FleetName (string) --
The name of the fleet for the streaming session.

State (string) --
The current state of the streaming session.

ConnectionState (string) --
Specifies whether a user is connected to the streaming session.

StartTime (datetime) --
The time when a streaming instance is dedicated for the user.

MaxExpirationTime (datetime) --
The time when the streaming session is set to expire. This time is based on the MaxUserDurationinSeconds value, which determines the maximum length of time that a streaming session can run. A streaming session might end earlier than the time specified in SessionMaxExpirationTime , when the DisconnectTimeOutInSeconds elapses or the user chooses to end his or her session. If the DisconnectTimeOutInSeconds elapses, or the user chooses to end his or her session, the streaming instance is terminated and the streaming session ends.

AuthenticationType (string) --
The authentication method. The user is authenticated using a streaming URL (API ) or SAML 2.0 federation (SAML ).

NetworkAccessConfiguration (dict) --
The network details for the streaming session.

EniPrivateIpAddress (string) --
The private IP address of the elastic network interface that is attached to instances in your VPC.

EniId (string) --
The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.







NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Sessions': [
            {
                'Id': 'string',
                'UserId': 'string',
                'StackName': 'string',
                'FleetName': 'string',
                'State': 'ACTIVE'|'PENDING'|'EXPIRED',
                'ConnectionState': 'CONNECTED'|'NOT_CONNECTED',
                'StartTime': datetime(2015, 1, 1),
                'MaxExpirationTime': datetime(2015, 1, 1),
                'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                'NetworkAccessConfiguration': {
                    'EniPrivateIpAddress': 'string',
                    'EniId': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AppStream.Client.exceptions.InvalidParameterCombinationException
    
    """
    pass

def describe_stacks(Names=None, NextToken=None):
    """
    Retrieves a list that describes one or more specified stacks, if the stack names are provided. Otherwise, all stacks in the account are described.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stacks(
        Names=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: The names of the stacks to describe.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'Stacks': [
        {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'StorageConnectors': [
                {
                    'ConnectorType': 'HOMEFOLDERS'|'GOOGLE_DRIVE'|'ONE_DRIVE',
                    'ResourceIdentifier': 'string',
                    'Domains': [
                        'string',
                    ]
                },
            ],
            'RedirectURL': 'string',
            'FeedbackURL': 'string',
            'StackErrors': [
                {
                    'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ],
            'UserSettings': [
                {
                    'Action': 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE'|'CLIPBOARD_COPY_TO_LOCAL_DEVICE'|'FILE_UPLOAD'|'FILE_DOWNLOAD'|'PRINTING_TO_LOCAL_DEVICE',
                    'Permission': 'ENABLED'|'DISABLED'
                },
            ],
            'ApplicationSettings': {
                'Enabled': True|False,
                'SettingsGroup': 'string',
                'S3BucketName': 'string'
            },
            'AccessEndpoints': [
                {
                    'EndpointType': 'STREAMING',
                    'VpceId': 'string'
                },
            ],
            'EmbedHostDomains': [
                'string',
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Stacks (list) --
Information about the stacks.

(dict) --
Describes a stack.

Arn (string) --
The ARN of the stack.

Name (string) --
The name of the stack.

Description (string) --
The description to display.

DisplayName (string) --
The stack name to display.

CreatedTime (datetime) --
The time the stack was created.

StorageConnectors (list) --
The storage connectors to enable.

(dict) --
Describes a connector that enables persistent storage for users.

ConnectorType (string) --
The type of storage connector.

ResourceIdentifier (string) --
The ARN of the storage connector.

Domains (list) --
The names of the domains for the account.

(string) -- GSuite domain for GDrive integration.






RedirectURL (string) --
The URL that users are redirected to after their streaming session ends.

FeedbackURL (string) --
The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.

StackErrors (list) --
The errors for the stack.

(dict) --
Describes a stack error.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.





UserSettings (list) --
The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.

(dict) --
Describes an action and whether the action is enabled or disabled for users during their streaming sessions.

Action (string) --
The action that is enabled or disabled.

Permission (string) --
Indicates whether the action is enabled or disabled.





ApplicationSettings (dict) --
The persistent application settings for users of the stack.

Enabled (boolean) --
Specifies whether persistent application settings are enabled for users during their streaming sessions.

SettingsGroup (string) --
The path prefix for the S3 bucket where users\xe2\x80\x99 persistent application settings are stored.

S3BucketName (string) --
The S3 bucket where users\xe2\x80\x99 persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region.



AccessEndpoints (list) --
The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to AppStream 2.0 only through the specified endpoints.

(dict) --
Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType (string) --
The type of interface endpoint.

VpceId (string) --
The identifier (ID) of the VPC in which the interface endpoint is used.





EmbedHostDomains (list) --
The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

(string) -- Specifies a valid domain that can embed AppStream. Valid examples include: ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples include: ["test,com", ".com", "h*llo.com". ""]






NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.ResourceNotFoundException


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
                        'ConnectorType': 'HOMEFOLDERS'|'GOOGLE_DRIVE'|'ONE_DRIVE',
                        'ResourceIdentifier': 'string',
                        'Domains': [
                            'string',
                        ]
                    },
                ],
                'RedirectURL': 'string',
                'FeedbackURL': 'string',
                'StackErrors': [
                    {
                        'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ],
                'UserSettings': [
                    {
                        'Action': 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE'|'CLIPBOARD_COPY_TO_LOCAL_DEVICE'|'FILE_UPLOAD'|'FILE_DOWNLOAD'|'PRINTING_TO_LOCAL_DEVICE',
                        'Permission': 'ENABLED'|'DISABLED'
                    },
                ],
                'ApplicationSettings': {
                    'Enabled': True|False,
                    'SettingsGroup': 'string',
                    'S3BucketName': 'string'
                },
                'AccessEndpoints': [
                    {
                        'EndpointType': 'STREAMING',
                        'VpceId': 'string'
                    },
                ],
                'EmbedHostDomains': [
                    'string',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) -- GSuite domain for GDrive integration.
    
    """
    pass

def describe_usage_report_subscriptions(MaxResults=None, NextToken=None):
    """
    Retrieves a list that describes one or more usage report subscriptions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_usage_report_subscriptions(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum size of each page of results.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'UsageReportSubscriptions': [
        {
            'S3BucketName': 'string',
            'Schedule': 'DAILY',
            'LastGeneratedReportDate': datetime(2015, 1, 1),
            'SubscriptionErrors': [
                {
                    'ErrorCode': 'RESOURCE_NOT_FOUND'|'ACCESS_DENIED'|'INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

UsageReportSubscriptions (list) --
Information about the usage report subscription.

(dict) --
Describes information about the usage report subscription.

S3BucketName (string) --
The Amazon S3 bucket where generated reports are stored.
If you enabled on-instance session scripts and Amazon S3 logging for your session script configuration, AppStream 2.0 created an S3 bucket to store the script output. The bucket is unique to your account and Region. When you enable usage reporting in this case, AppStream 2.0 uses the same bucket to store your usage reports. If you haven\'t already enabled on-instance session scripts, when you enable usage reports, AppStream 2.0 creates a new S3 bucket.

Schedule (string) --
The schedule for generating usage reports.

LastGeneratedReportDate (datetime) --
The time when the last usage report was generated.

SubscriptionErrors (list) --
The errors that were returned if usage reports couldn\'t be generated.

(dict) --
Describes the error that is returned when a usage report can\'t be generated.

ErrorCode (string) --
The error code for the error that is returned when a usage report can\'t be generated.

ErrorMessage (string) --
The error message for the error that is returned when a usage report can\'t be generated.









NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.InvalidAccountStatusException


    :return: {
        'UsageReportSubscriptions': [
            {
                'S3BucketName': 'string',
                'Schedule': 'DAILY',
                'LastGeneratedReportDate': datetime(2015, 1, 1),
                'SubscriptionErrors': [
                    {
                        'ErrorCode': 'RESOURCE_NOT_FOUND'|'ACCESS_DENIED'|'INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceNotFoundException
    AppStream.Client.exceptions.InvalidAccountStatusException
    
    """
    pass

def describe_user_stack_associations(StackName=None, UserName=None, AuthenticationType=None, MaxResults=None, NextToken=None):
    """
    Retrieves a list that describes the UserStackAssociation objects. You must specify either or both of the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_user_stack_associations(
        StackName='string',
        UserName='string',
        AuthenticationType='API'|'SAML'|'USERPOOL',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type StackName: string
    :param StackName: The name of the stack that is associated with the user.

    :type UserName: string
    :param UserName: The email address of the user who is associated with the stack.\n\nNote\nUsers\' email addresses are case-sensitive.\n\n

    :type AuthenticationType: string
    :param AuthenticationType: The authentication type for the user who is associated with the stack. You must specify USERPOOL.

    :type MaxResults: integer
    :param MaxResults: The maximum size of each page of results.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'UserStackAssociations': [
        {
            'StackName': 'string',
            'UserName': 'string',
            'AuthenticationType': 'API'|'SAML'|'USERPOOL',
            'SendEmailNotification': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

UserStackAssociations (list) --
The UserStackAssociation objects.

(dict) --
Describes a user in the user pool and the associated stack.

StackName (string) --
The name of the stack that is associated with the user.

UserName (string) --
The email address of the user who is associated with the stack.

Note
Users\' email addresses are case-sensitive.


AuthenticationType (string) --
The authentication type for the user.

SendEmailNotification (boolean) --
Specifies whether a welcome email is sent to a user after the user is created in the user pool.





NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'UserStackAssociations': [
            {
                'StackName': 'string',
                'UserName': 'string',
                'AuthenticationType': 'API'|'SAML'|'USERPOOL',
                'SendEmailNotification': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    StackName (string) -- The name of the stack that is associated with the user.
    UserName (string) -- The email address of the user who is associated with the stack.
    
    Note
    Users\' email addresses are case-sensitive.
    
    
    AuthenticationType (string) -- The authentication type for the user who is associated with the stack. You must specify USERPOOL.
    MaxResults (integer) -- The maximum size of each page of results.
    NextToken (string) -- The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
    
    """
    pass

def describe_users(AuthenticationType=None, MaxResults=None, NextToken=None):
    """
    Retrieves a list that describes one or more specified users in the user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_users(
        AuthenticationType='API'|'SAML'|'USERPOOL',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AuthenticationType: string
    :param AuthenticationType: [REQUIRED]\nThe authentication type for the users in the user pool to describe. You must specify USERPOOL.\n

    :type MaxResults: integer
    :param MaxResults: The maximum size of each page of results.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'Users': [
        {
            'Arn': 'string',
            'UserName': 'string',
            'Enabled': True|False,
            'Status': 'string',
            'FirstName': 'string',
            'LastName': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'AuthenticationType': 'API'|'SAML'|'USERPOOL'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Users (list) --
Information about users in the user pool.

(dict) --
Describes a user in the user pool.

Arn (string) --
The ARN of the user.

UserName (string) --
The email address of the user.

Note
Users\' email addresses are case-sensitive.


Enabled (boolean) --
Specifies whether the user in the user pool is enabled.

Status (string) --
The status of the user in the user pool. The status can be one of the following:

UNCONFIRMED \xe2\x80\x93 The user is created but not confirmed.
CONFIRMED \xe2\x80\x93 The user is confirmed.
ARCHIVED \xe2\x80\x93 The user is no longer active.
COMPROMISED \xe2\x80\x93 The user is disabled because of a potential security threat.
UNKNOWN \xe2\x80\x93 The user status is not known.


FirstName (string) --
The first name, or given name, of the user.

LastName (string) --
The last name, or surname, of the user.

CreatedTime (datetime) --
The date and time the user was created in the user pool.

AuthenticationType (string) --
The authentication type for the user.





NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.







Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.InvalidParameterCombinationException


    :return: {
        'Users': [
            {
                'Arn': 'string',
                'UserName': 'string',
                'Enabled': True|False,
                'Status': 'string',
                'FirstName': 'string',
                'LastName': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'AuthenticationType': 'API'|'SAML'|'USERPOOL'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    UNCONFIRMED \xe2\x80\x93 The user is created but not confirmed.
    CONFIRMED \xe2\x80\x93 The user is confirmed.
    ARCHIVED \xe2\x80\x93 The user is no longer active.
    COMPROMISED \xe2\x80\x93 The user is disabled because of a potential security threat.
    UNKNOWN \xe2\x80\x93 The user status is not known.
    
    """
    pass

def disable_user(UserName=None, AuthenticationType=None):
    """
    Disables the specified user in the user pool. Users can\'t sign in to AppStream 2.0 until they are re-enabled. This action does not delete the user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_user(
        UserName='string',
        AuthenticationType='API'|'SAML'|'USERPOOL'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe email address of the user.\n\nNote\nUsers\' email addresses are case-sensitive.\n\n

    :type AuthenticationType: string
    :param AuthenticationType: [REQUIRED]\nThe authentication type for the user. You must specify USERPOOL.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_fleet(FleetName=None, StackName=None):
    """
    Disassociates the specified fleet from the specified stack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_fleet(
        FleetName='string',
        StackName='string'
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]\nThe name of the fleet.\n

    :type StackName: string
    :param StackName: [REQUIRED]\nThe name of the stack.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.ResourceInUseException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def enable_user(UserName=None, AuthenticationType=None):
    """
    Enables a user in the user pool. After being enabled, users can sign in to AppStream 2.0 and open applications from the stacks to which they are assigned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_user(
        UserName='string',
        AuthenticationType='API'|'SAML'|'USERPOOL'
    )
    
    
    :type UserName: string
    :param UserName: [REQUIRED]\nThe email address of the user.\n\nNote\nUsers\' email addresses are case-sensitive. During login, if they specify an email address that doesn\'t use the same capitalization as the email address specified when their user pool account was created, a 'user does not exist' error message displays.\n\n

    :type AuthenticationType: string
    :param AuthenticationType: [REQUIRED]\nThe authentication type for the user. You must specify USERPOOL.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.InvalidAccountStatusException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def expire_session(SessionId=None):
    """
    Immediately stops the specified streaming session.
    See also: AWS API Documentation
    
    
    :example: response = client.expire_session(
        SessionId='string'
    )
    
    
    :type SessionId: string
    :param SessionId: [REQUIRED]\nThe identifier of the streaming session.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --




    :return: {}
    
    
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

def list_associated_fleets(StackName=None, NextToken=None):
    """
    Retrieves the name of the fleet that is associated with the specified stack.
    See also: AWS API Documentation
    
    
    :example: response = client.list_associated_fleets(
        StackName='string',
        NextToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name of the stack.\n

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'Names': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Names (list) --
The name of the fleet.

(string) --


NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.








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
    Retrieves the name of the stack with which the specified fleet is associated.
    See also: AWS API Documentation
    
    
    :example: response = client.list_associated_stacks(
        FleetName='string',
        NextToken='string'
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]\nThe name of the fleet.\n

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict

ReturnsResponse Syntax
{
    'Names': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Names (list) --
The name of the stack.

(string) --


NextToken (string) --
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.








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
    Retrieves a list of all tags for the specified AppStream 2.0 resource. You can tag AppStream 2.0 image builders, images, fleets, and stacks.
    For more information about tags, see Tagging Your Resources in the Amazon AppStream 2.0 Administration Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The information about the tags.

(string) --
(string) --









Exceptions

AppStream.Client.exceptions.ResourceNotFoundException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def start_fleet(Name=None):
    """
    Starts the specified fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_fleet(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.OperationNotPermittedException
AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.ConcurrentModificationException
AppStream.Client.exceptions.ResourceNotAvailableException
AppStream.Client.exceptions.InvalidRoleException


    :return: {}
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceNotFoundException
    AppStream.Client.exceptions.OperationNotPermittedException
    AppStream.Client.exceptions.LimitExceededException
    AppStream.Client.exceptions.InvalidAccountStatusException
    AppStream.Client.exceptions.ConcurrentModificationException
    AppStream.Client.exceptions.ResourceNotAvailableException
    AppStream.Client.exceptions.InvalidRoleException
    
    """
    pass

def start_image_builder(Name=None, AppstreamAgentVersion=None):
    """
    Starts the specified image builder.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_image_builder(
        Name='string',
        AppstreamAgentVersion='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the image builder.\n

    :type AppstreamAgentVersion: string
    :param AppstreamAgentVersion: The version of the AppStream 2.0 agent to use for this image builder. To use the latest version of the AppStream 2.0 agent, specify [LATEST].

    :rtype: dict

ReturnsResponse Syntax
{
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
        'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
        'IamRoleArn': 'string',
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
        'NetworkAccessConfiguration': {
            'EniPrivateIpAddress': 'string',
            'EniId': 'string'
        },
        'ImageBuilderErrors': [
            {
                'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                'ErrorMessage': 'string',
                'ErrorTimestamp': datetime(2015, 1, 1)
            },
        ],
        'AppstreamAgentVersion': 'string',
        'AccessEndpoints': [
            {
                'EndpointType': 'STREAMING',
                'VpceId': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ImageBuilder (dict) --
Information about the image builder.

Name (string) --
The name of the image builder.

Arn (string) --
The ARN for the image builder.

ImageArn (string) --
The ARN of the image from which this builder was created.

Description (string) --
The description to display.

DisplayName (string) --
The image builder name to display.

VpcConfig (dict) --
The VPC configuration of the image builder.

SubnetIds (list) --
The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string) --


SecurityGroupIds (list) --
The identifiers of the security groups for the fleet or image builder.

(string) --




InstanceType (string) --
The instance type for the image builder. The following instance types are available:

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


Platform (string) --
The operating system platform of the image builder.

IamRoleArn (string) --
The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.
For more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .

State (string) --
The state of the image builder.

StateChangeReason (dict) --
The reason why the last state change occurred.

Code (string) --
The state change reason code.

Message (string) --
The state change reason message.



CreatedTime (datetime) --
The time stamp when the image builder was created.

EnableDefaultInternetAccess (boolean) --
Enables or disables default internet access for the image builder.

DomainJoinInfo (dict) --
The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.

DirectoryName (string) --
The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName (string) --
The distinguished name of the organizational unit for computer accounts.



NetworkAccessConfiguration (dict) --
Describes the network details of the fleet or image builder instance.

EniPrivateIpAddress (string) --
The private IP address of the elastic network interface that is attached to instances in your VPC.

EniId (string) --
The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.



ImageBuilderErrors (list) --
The image builder errors.

(dict) --
Describes a resource error.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.

ErrorTimestamp (datetime) --
The time the error occurred.





AppstreamAgentVersion (string) --
The version of the AppStream 2.0 agent that is currently being used by the image builder.

AccessEndpoints (list) --
The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.

(dict) --
Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType (string) --
The type of interface endpoint.

VpceId (string) --
The identifier (ID) of the VPC in which the interface endpoint is used.













Exceptions

AppStream.Client.exceptions.ResourceNotAvailableException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ConcurrentModificationException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.IncompatibleImageException


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
            'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
            'IamRoleArn': 'string',
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
            'NetworkAccessConfiguration': {
                'EniPrivateIpAddress': 'string',
                'EniId': 'string'
            },
            'ImageBuilderErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string',
                    'ErrorTimestamp': datetime(2015, 1, 1)
                },
            ],
            'AppstreamAgentVersion': 'string',
            'AccessEndpoints': [
                {
                    'EndpointType': 'STREAMING',
                    'VpceId': 'string'
                },
            ]
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
    
    Exceptions
    
    :example: response = client.stop_fleet(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    AppStream.Client.exceptions.ResourceNotFoundException
    AppStream.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def stop_image_builder(Name=None):
    """
    Stops the specified image builder.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_image_builder(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the image builder.\n

    :rtype: dict
ReturnsResponse Syntax{
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
        'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
        'IamRoleArn': 'string',
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
        'NetworkAccessConfiguration': {
            'EniPrivateIpAddress': 'string',
            'EniId': 'string'
        },
        'ImageBuilderErrors': [
            {
                'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                'ErrorMessage': 'string',
                'ErrorTimestamp': datetime(2015, 1, 1)
            },
        ],
        'AppstreamAgentVersion': 'string',
        'AccessEndpoints': [
            {
                'EndpointType': 'STREAMING',
                'VpceId': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
ImageBuilder (dict) --Information about the image builder.

Name (string) --The name of the image builder.

Arn (string) --The ARN for the image builder.

ImageArn (string) --The ARN of the image from which this builder was created.

Description (string) --The description to display.

DisplayName (string) --The image builder name to display.

VpcConfig (dict) --The VPC configuration of the image builder.

SubnetIds (list) --The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string) --


SecurityGroupIds (list) --The identifiers of the security groups for the fleet or image builder.

(string) --




InstanceType (string) --The instance type for the image builder. The following instance types are available:

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


Platform (string) --The operating system platform of the image builder.

IamRoleArn (string) --The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.
For more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .

State (string) --The state of the image builder.

StateChangeReason (dict) --The reason why the last state change occurred.

Code (string) --The state change reason code.

Message (string) --The state change reason message.



CreatedTime (datetime) --The time stamp when the image builder was created.

EnableDefaultInternetAccess (boolean) --Enables or disables default internet access for the image builder.

DomainJoinInfo (dict) --The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.

DirectoryName (string) --The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName (string) --The distinguished name of the organizational unit for computer accounts.



NetworkAccessConfiguration (dict) --Describes the network details of the fleet or image builder instance.

EniPrivateIpAddress (string) --The private IP address of the elastic network interface that is attached to instances in your VPC.

EniId (string) --The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.



ImageBuilderErrors (list) --The image builder errors.

(dict) --Describes a resource error.

ErrorCode (string) --The error code.

ErrorMessage (string) --The error message.

ErrorTimestamp (datetime) --The time the error occurred.





AppstreamAgentVersion (string) --The version of the AppStream 2.0 agent that is currently being used by the image builder.

AccessEndpoints (list) --The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.

(dict) --Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType (string) --The type of interface endpoint.

VpceId (string) --The identifier (ID) of the VPC in which the interface endpoint is used.












Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.OperationNotPermittedException
AppStream.Client.exceptions.ConcurrentModificationException


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
            'Platform': 'WINDOWS'|'WINDOWS_SERVER_2016'|'WINDOWS_SERVER_2019',
            'IamRoleArn': 'string',
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
            'NetworkAccessConfiguration': {
                'EniPrivateIpAddress': 'string',
                'EniId': 'string'
            },
            'ImageBuilderErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string',
                    'ErrorTimestamp': datetime(2015, 1, 1)
                },
            ],
            'AppstreamAgentVersion': 'string',
            'AccessEndpoints': [
                {
                    'EndpointType': 'STREAMING',
                    'VpceId': 'string'
                },
            ]
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
    For more information about tags, see Tagging Your Resources in the Amazon AppStream 2.0 Administration Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe tags to associate. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=.\nIf you do not specify a value, the value is set to an empty string.\nGenerally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters:\n_ . : / = + - @\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Disassociates one or more specified tags from the specified AppStream 2.0 resource.
    To list the current tags for your resources, use  ListTagsForResource .
    For more information about tags, see Tagging Your Resources in the Amazon AppStream 2.0 Administration Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys for the tags to disassociate.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_directory_config(DirectoryName=None, OrganizationalUnitDistinguishedNames=None, ServiceAccountCredentials=None):
    """
    Updates the specified Directory Config object in AppStream 2.0. This object includes the configuration information required to join fleets and image builders to Microsoft Active Directory domains.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DirectoryName: [REQUIRED]\nThe name of the Directory Config object.\n

    :type OrganizationalUnitDistinguishedNames: list
    :param OrganizationalUnitDistinguishedNames: The distinguished names of the organizational units for computer accounts.\n\n(string) --\n\n

    :type ServiceAccountCredentials: dict
    :param ServiceAccountCredentials: The credentials for the service account used by the fleet or image builder to connect to the directory.\n\nAccountName (string) -- [REQUIRED]The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.\n\nAccountPassword (string) -- [REQUIRED]The password for the account.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

DirectoryConfig (dict) --
Information about the Directory Config object.

DirectoryName (string) --
The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedNames (list) --
The distinguished names of the organizational units for computer accounts.

(string) --


ServiceAccountCredentials (dict) --
The credentials for the service account used by the fleet or image builder to connect to the directory.

AccountName (string) --
The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.

AccountPassword (string) --
The password for the account.



CreatedTime (datetime) --
The time the directory configuration was created.









Exceptions

AppStream.Client.exceptions.ResourceInUseException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ConcurrentModificationException


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

def update_fleet(ImageName=None, ImageArn=None, Name=None, InstanceType=None, ComputeCapacity=None, VpcConfig=None, MaxUserDurationInSeconds=None, DisconnectTimeoutInSeconds=None, DeleteVpcConfig=None, Description=None, DisplayName=None, EnableDefaultInternetAccess=None, DomainJoinInfo=None, IdleDisconnectTimeoutInSeconds=None, AttributesToDelete=None, IamRoleArn=None):
    """
    Updates the specified fleet.
    If the fleet is in the STOPPED state, you can update any attribute except the fleet name. If the fleet is in the RUNNING state, you can update the DisplayName , ComputeCapacity , ImageARN , ImageName , IdleDisconnectTimeoutInSeconds , and DisconnectTimeoutInSeconds attributes. If the fleet is in the STARTING or STOPPING state, you can\'t update it.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_fleet(
        ImageName='string',
        ImageArn='string',
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
        IdleDisconnectTimeoutInSeconds=123,
        AttributesToDelete=[
            'VPC_CONFIGURATION'|'VPC_CONFIGURATION_SECURITY_GROUP_IDS'|'DOMAIN_JOIN_INFO'|'IAM_ROLE_ARN',
        ],
        IamRoleArn='string'
    )
    
    
    :type ImageName: string
    :param ImageName: The name of the image used to create the fleet.

    :type ImageArn: string
    :param ImageArn: The ARN of the public, private, or shared image to use.

    :type Name: string
    :param Name: A unique name for the fleet.

    :type InstanceType: string
    :param InstanceType: The instance type to use when launching fleet instances. The following instance types are available:\n\nstream.standard.medium\nstream.standard.large\nstream.compute.large\nstream.compute.xlarge\nstream.compute.2xlarge\nstream.compute.4xlarge\nstream.compute.8xlarge\nstream.memory.large\nstream.memory.xlarge\nstream.memory.2xlarge\nstream.memory.4xlarge\nstream.memory.8xlarge\nstream.graphics-design.large\nstream.graphics-design.xlarge\nstream.graphics-design.2xlarge\nstream.graphics-design.4xlarge\nstream.graphics-desktop.2xlarge\nstream.graphics-pro.4xlarge\nstream.graphics-pro.8xlarge\nstream.graphics-pro.16xlarge\n\n

    :type ComputeCapacity: dict
    :param ComputeCapacity: The desired capacity for the fleet.\n\nDesiredInstances (integer) -- [REQUIRED]The desired number of streaming instances.\n\n\n

    :type VpcConfig: dict
    :param VpcConfig: The VPC configuration for the fleet.\n\nSubnetIds (list) --The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.\n\n(string) --\n\n\nSecurityGroupIds (list) --The identifiers of the security groups for the fleet or image builder.\n\n(string) --\n\n\n\n

    :type MaxUserDurationInSeconds: integer
    :param MaxUserDurationInSeconds: The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.\nSpecify a value between 600 and 360000.\n

    :type DisconnectTimeoutInSeconds: integer
    :param DisconnectTimeoutInSeconds: The amount of time that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.\nSpecify a value between 60 and 360000.\n

    :type DeleteVpcConfig: boolean
    :param DeleteVpcConfig: Deletes the VPC association for the specified fleet.

    :type Description: string
    :param Description: The description to display.

    :type DisplayName: string
    :param DisplayName: The fleet name to display.

    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: Enables or disables default internet access for the fleet.

    :type DomainJoinInfo: dict
    :param DomainJoinInfo: The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.\n\nDirectoryName (string) --The fully qualified name of the directory (for example, corp.example.com).\n\nOrganizationalUnitDistinguishedName (string) --The distinguished name of the organizational unit for computer accounts.\n\n\n

    :type IdleDisconnectTimeoutInSeconds: integer
    :param IdleDisconnectTimeoutInSeconds: The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the DisconnectTimeoutInSeconds time interval begins. Users are notified before they are disconnected due to inactivity. If users try to reconnect to the streaming session before the time interval specified in DisconnectTimeoutInSeconds elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in IdleDisconnectTimeoutInSeconds elapses, they are disconnected.\nTo prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 3600. The default value is 0.\n\nNote\nIf you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don\'t do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.\n\n

    :type AttributesToDelete: list
    :param AttributesToDelete: The fleet attributes to delete.\n\n(string) --The fleet attribute.\n\n\n

    :type IamRoleArn: string
    :param IamRoleArn: The Amazon Resource Name (ARN) of the IAM role to apply to the fleet. To assume a role, a fleet instance calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.\nFor more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Fleet': {
        'Arn': 'string',
        'Name': 'string',
        'DisplayName': 'string',
        'Description': 'string',
        'ImageName': 'string',
        'ImageArn': 'string',
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
                'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                'ErrorMessage': 'string'
            },
        ],
        'EnableDefaultInternetAccess': True|False,
        'DomainJoinInfo': {
            'DirectoryName': 'string',
            'OrganizationalUnitDistinguishedName': 'string'
        },
        'IdleDisconnectTimeoutInSeconds': 123,
        'IamRoleArn': 'string'
    }
}


Response Structure

(dict) --

Fleet (dict) --
Information about the fleet.

Arn (string) --
The Amazon Resource Name (ARN) for the fleet.

Name (string) --
The name of the fleet.

DisplayName (string) --
The fleet name to display.

Description (string) --
The description to display.

ImageName (string) --
The name of the image used to create the fleet.

ImageArn (string) --
The ARN for the public, private, or shared image.

InstanceType (string) --
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


FleetType (string) --
The fleet type.

ALWAYS_ON

Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.

ON_DEMAND

Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.

ComputeCapacityStatus (dict) --
The capacity status for the fleet.

Desired (integer) --
The desired number of streaming instances.

Running (integer) --
The total number of simultaneous streaming instances that are running.

InUse (integer) --
The number of instances in use for streaming.

Available (integer) --
The number of currently available instances that can be used to stream sessions.



MaxUserDurationInSeconds (integer) --
The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
Specify a value between 600 and 360000.

DisconnectTimeoutInSeconds (integer) --
The amount of time that a streaming session remains active after users disconnect. If they try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
Specify a value between 60 and 360000.

State (string) --
The current state for the fleet.

VpcConfig (dict) --
The VPC configuration for the fleet.

SubnetIds (list) --
The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.

(string) --


SecurityGroupIds (list) --
The identifiers of the security groups for the fleet or image builder.

(string) --




CreatedTime (datetime) --
The time the fleet was created.

FleetErrors (list) --
The fleet errors.

(dict) --
Describes a fleet error.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.





EnableDefaultInternetAccess (boolean) --
Indicates whether default internet access is enabled for the fleet.

DomainJoinInfo (dict) --
The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain.

DirectoryName (string) --
The fully qualified name of the directory (for example, corp.example.com).

OrganizationalUnitDistinguishedName (string) --
The distinguished name of the organizational unit for computer accounts.



IdleDisconnectTimeoutInSeconds (integer) --
The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the DisconnectTimeoutInSeconds time interval begins. Users are notified before they are disconnected due to inactivity. If users try to reconnect to the streaming session before the time interval specified in DisconnectTimeoutInSeconds elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in IdleDisconnectTimeoutInSeconds elapses, they are disconnected.
To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 3600. The default value is 0.

Note
If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don\'t do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity.


IamRoleArn (string) --
The ARN of the IAM role that is applied to the fleet. To assume a role, the fleet instance calls the AWS Security Token Service (STS) AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. AppStream 2.0 retrieves the temporary credentials and creates the AppStream_Machine_Role credential profile on the instance.
For more information, see Using an IAM Role to Grant Permissions to Applications and Scripts Running on AppStream 2.0 Streaming Instances in the Amazon AppStream 2.0 Administration Guide .









Exceptions

AppStream.Client.exceptions.ResourceInUseException
AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.InvalidRoleException
AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ResourceNotAvailableException
AppStream.Client.exceptions.InvalidParameterCombinationException
AppStream.Client.exceptions.ConcurrentModificationException
AppStream.Client.exceptions.IncompatibleImageException
AppStream.Client.exceptions.OperationNotPermittedException


    :return: {
        'Fleet': {
            'Arn': 'string',
            'Name': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'ImageName': 'string',
            'ImageArn': 'string',
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
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'MACHINE_ROLE_IS_MISSING'|'STS_DISABLED_IN_REGION'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION'|'SECURITY_GROUPS_NOT_FOUND'|'IGW_NOT_ATTACHED'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION'|'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND'|'DOMAIN_JOIN_ERROR_ACCESS_DENIED'|'DOMAIN_JOIN_ERROR_LOGON_FAILURE'|'DOMAIN_JOIN_ERROR_INVALID_PARAMETER'|'DOMAIN_JOIN_ERROR_MORE_DATA'|'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN'|'DOMAIN_JOIN_ERROR_NOT_SUPPORTED'|'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME'|'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED'|'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED'|'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED'|'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ],
            'EnableDefaultInternetAccess': True|False,
            'DomainJoinInfo': {
                'DirectoryName': 'string',
                'OrganizationalUnitDistinguishedName': 'string'
            },
            'IdleDisconnectTimeoutInSeconds': 123,
            'IamRoleArn': 'string'
        }
    }
    
    
    :returns: 
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
    
    """
    pass

def update_image_permissions(Name=None, SharedAccountId=None, ImagePermissions=None):
    """
    Adds or updates permissions for the specified private image.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_image_permissions(
        Name='string',
        SharedAccountId='string',
        ImagePermissions={
            'allowFleet': True|False,
            'allowImageBuilder': True|False
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the private image.\n

    :type SharedAccountId: string
    :param SharedAccountId: [REQUIRED]\nThe 12-digit identifier of the AWS account for which you want add or update image permissions.\n

    :type ImagePermissions: dict
    :param ImagePermissions: [REQUIRED]\nThe permissions for the image.\n\nallowFleet (boolean) --Indicates whether the image can be used for a fleet.\n\nallowImageBuilder (boolean) --Indicates whether the image can be used for an image builder.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ResourceNotAvailableException
AppStream.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_stack(DisplayName=None, Description=None, Name=None, StorageConnectors=None, DeleteStorageConnectors=None, RedirectURL=None, FeedbackURL=None, AttributesToDelete=None, UserSettings=None, ApplicationSettings=None, AccessEndpoints=None, EmbedHostDomains=None):
    """
    Updates the specified fields for the specified stack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_stack(
        DisplayName='string',
        Description='string',
        Name='string',
        StorageConnectors=[
            {
                'ConnectorType': 'HOMEFOLDERS'|'GOOGLE_DRIVE'|'ONE_DRIVE',
                'ResourceIdentifier': 'string',
                'Domains': [
                    'string',
                ]
            },
        ],
        DeleteStorageConnectors=True|False,
        RedirectURL='string',
        FeedbackURL='string',
        AttributesToDelete=[
            'STORAGE_CONNECTORS'|'STORAGE_CONNECTOR_HOMEFOLDERS'|'STORAGE_CONNECTOR_GOOGLE_DRIVE'|'STORAGE_CONNECTOR_ONE_DRIVE'|'REDIRECT_URL'|'FEEDBACK_URL'|'THEME_NAME'|'USER_SETTINGS'|'EMBED_HOST_DOMAINS'|'IAM_ROLE_ARN'|'ACCESS_ENDPOINTS',
        ],
        UserSettings=[
            {
                'Action': 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE'|'CLIPBOARD_COPY_TO_LOCAL_DEVICE'|'FILE_UPLOAD'|'FILE_DOWNLOAD'|'PRINTING_TO_LOCAL_DEVICE',
                'Permission': 'ENABLED'|'DISABLED'
            },
        ],
        ApplicationSettings={
            'Enabled': True|False,
            'SettingsGroup': 'string'
        },
        AccessEndpoints=[
            {
                'EndpointType': 'STREAMING',
                'VpceId': 'string'
            },
        ],
        EmbedHostDomains=[
            'string',
        ]
    )
    
    
    :type DisplayName: string
    :param DisplayName: The stack name to display.

    :type Description: string
    :param Description: The description to display.

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the stack.\n

    :type StorageConnectors: list
    :param StorageConnectors: The storage connectors to enable.\n\n(dict) --Describes a connector that enables persistent storage for users.\n\nConnectorType (string) -- [REQUIRED]The type of storage connector.\n\nResourceIdentifier (string) --The ARN of the storage connector.\n\nDomains (list) --The names of the domains for the account.\n\n(string) -- GSuite domain for GDrive integration.\n\n\n\n\n\n

    :type DeleteStorageConnectors: boolean
    :param DeleteStorageConnectors: Deletes the storage connectors currently enabled for the stack.

    :type RedirectURL: string
    :param RedirectURL: The URL that users are redirected to after their streaming session ends.

    :type FeedbackURL: string
    :param FeedbackURL: The URL that users are redirected to after they choose the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.

    :type AttributesToDelete: list
    :param AttributesToDelete: The stack attributes to delete.\n\n(string) --\n\n

    :type UserSettings: list
    :param UserSettings: The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.\n\n(dict) --Describes an action and whether the action is enabled or disabled for users during their streaming sessions.\n\nAction (string) -- [REQUIRED]The action that is enabled or disabled.\n\nPermission (string) -- [REQUIRED]Indicates whether the action is enabled or disabled.\n\n\n\n\n

    :type ApplicationSettings: dict
    :param ApplicationSettings: The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.\n\nEnabled (boolean) -- [REQUIRED]Enables or disables persistent application settings for users during their streaming sessions.\n\nSettingsGroup (string) --The path prefix for the S3 bucket where users\xe2\x80\x99 persistent application settings are stored. You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack.\n\n\n

    :type AccessEndpoints: list
    :param AccessEndpoints: The list of interface VPC endpoint (interface endpoint) objects. Users of the stack can connect to AppStream 2.0 only through the specified endpoints.\n\n(dict) --Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.\n\nEndpointType (string) -- [REQUIRED]The type of interface endpoint.\n\nVpceId (string) --The identifier (ID) of the VPC in which the interface endpoint is used.\n\n\n\n\n

    :type EmbedHostDomains: list
    :param EmbedHostDomains: The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.\n\n(string) -- Specifies a valid domain that can embed AppStream. Valid examples include: ['testorigin.tt--com', 'testingorigin.com.us', 'test.com.us'] Invalid examples include: ['test,com', '.com', 'h*llo.com'. '']\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Stack': {
        'Arn': 'string',
        'Name': 'string',
        'Description': 'string',
        'DisplayName': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'StorageConnectors': [
            {
                'ConnectorType': 'HOMEFOLDERS'|'GOOGLE_DRIVE'|'ONE_DRIVE',
                'ResourceIdentifier': 'string',
                'Domains': [
                    'string',
                ]
            },
        ],
        'RedirectURL': 'string',
        'FeedbackURL': 'string',
        'StackErrors': [
            {
                'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                'ErrorMessage': 'string'
            },
        ],
        'UserSettings': [
            {
                'Action': 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE'|'CLIPBOARD_COPY_TO_LOCAL_DEVICE'|'FILE_UPLOAD'|'FILE_DOWNLOAD'|'PRINTING_TO_LOCAL_DEVICE',
                'Permission': 'ENABLED'|'DISABLED'
            },
        ],
        'ApplicationSettings': {
            'Enabled': True|False,
            'SettingsGroup': 'string',
            'S3BucketName': 'string'
        },
        'AccessEndpoints': [
            {
                'EndpointType': 'STREAMING',
                'VpceId': 'string'
            },
        ],
        'EmbedHostDomains': [
            'string',
        ]
    }
}


Response Structure

(dict) --

Stack (dict) --
Information about the stack.

Arn (string) --
The ARN of the stack.

Name (string) --
The name of the stack.

Description (string) --
The description to display.

DisplayName (string) --
The stack name to display.

CreatedTime (datetime) --
The time the stack was created.

StorageConnectors (list) --
The storage connectors to enable.

(dict) --
Describes a connector that enables persistent storage for users.

ConnectorType (string) --
The type of storage connector.

ResourceIdentifier (string) --
The ARN of the storage connector.

Domains (list) --
The names of the domains for the account.

(string) -- GSuite domain for GDrive integration.






RedirectURL (string) --
The URL that users are redirected to after their streaming session ends.

FeedbackURL (string) --
The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.

StackErrors (list) --
The errors for the stack.

(dict) --
Describes a stack error.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message.





UserSettings (list) --
The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.

(dict) --
Describes an action and whether the action is enabled or disabled for users during their streaming sessions.

Action (string) --
The action that is enabled or disabled.

Permission (string) --
Indicates whether the action is enabled or disabled.





ApplicationSettings (dict) --
The persistent application settings for users of the stack.

Enabled (boolean) --
Specifies whether persistent application settings are enabled for users during their streaming sessions.

SettingsGroup (string) --
The path prefix for the S3 bucket where users\xe2\x80\x99 persistent application settings are stored.

S3BucketName (string) --
The S3 bucket where users\xe2\x80\x99 persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region.



AccessEndpoints (list) --
The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to AppStream 2.0 only through the specified endpoints.

(dict) --
Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and AppStream 2.0. When you specify an interface endpoint for a stack, users of the stack can connect to AppStream 2.0 only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

EndpointType (string) --
The type of interface endpoint.

VpceId (string) --
The identifier (ID) of the VPC in which the interface endpoint is used.





EmbedHostDomains (list) --
The domains where AppStream 2.0 streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded AppStream 2.0 streaming sessions.

(string) -- Specifies a valid domain that can embed AppStream. Valid examples include: ["testorigin.tt--com", "testingorigin.com.us", "test.com.us"] Invalid examples include: ["test,com", ".com", "h*llo.com". ""]










Exceptions

AppStream.Client.exceptions.ResourceNotFoundException
AppStream.Client.exceptions.ResourceInUseException
AppStream.Client.exceptions.InvalidRoleException
AppStream.Client.exceptions.InvalidParameterCombinationException
AppStream.Client.exceptions.LimitExceededException
AppStream.Client.exceptions.InvalidAccountStatusException
AppStream.Client.exceptions.IncompatibleImageException
AppStream.Client.exceptions.OperationNotPermittedException
AppStream.Client.exceptions.ConcurrentModificationException


    :return: {
        'Stack': {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'StorageConnectors': [
                {
                    'ConnectorType': 'HOMEFOLDERS'|'GOOGLE_DRIVE'|'ONE_DRIVE',
                    'ResourceIdentifier': 'string',
                    'Domains': [
                        'string',
                    ]
                },
            ],
            'RedirectURL': 'string',
            'FeedbackURL': 'string',
            'StackErrors': [
                {
                    'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ],
            'UserSettings': [
                {
                    'Action': 'CLIPBOARD_COPY_FROM_LOCAL_DEVICE'|'CLIPBOARD_COPY_TO_LOCAL_DEVICE'|'FILE_UPLOAD'|'FILE_DOWNLOAD'|'PRINTING_TO_LOCAL_DEVICE',
                    'Permission': 'ENABLED'|'DISABLED'
                },
            ],
            'ApplicationSettings': {
                'Enabled': True|False,
                'SettingsGroup': 'string',
                'S3BucketName': 'string'
            },
            'AccessEndpoints': [
                {
                    'EndpointType': 'STREAMING',
                    'VpceId': 'string'
                },
            ],
            'EmbedHostDomains': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) -- GSuite domain for GDrive integration.
    
    """
    pass

