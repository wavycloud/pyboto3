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

def accept_shared_directory(SharedDirectoryId=None):
    """
    Accepts a directory sharing request that was sent from the directory owner account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_shared_directory(
        SharedDirectoryId='string'
    )
    
    
    :type SharedDirectoryId: string
    :param SharedDirectoryId: [REQUIRED]\nIdentifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SharedDirectory': {
        'OwnerAccountId': 'string',
        'OwnerDirectoryId': 'string',
        'ShareMethod': 'ORGANIZATIONS'|'HANDSHAKE',
        'SharedAccountId': 'string',
        'SharedDirectoryId': 'string',
        'ShareStatus': 'Shared'|'PendingAcceptance'|'Rejected'|'Rejecting'|'RejectFailed'|'Sharing'|'ShareFailed'|'Deleted'|'Deleting',
        'ShareNotes': 'string',
        'CreatedDateTime': datetime(2015, 1, 1),
        'LastUpdatedDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
SharedDirectory (dict) --The shared directory in the directory consumer account.

OwnerAccountId (string) --Identifier of the directory owner account, which contains the directory that has been shared to the consumer account.

OwnerDirectoryId (string) --Identifier of the directory in the directory owner account.

ShareMethod (string) --The method used when sharing a directory to determine whether the directory should be shared within your AWS organization (ORGANIZATIONS ) or with any AWS account by sending a shared directory request (HANDSHAKE ).

SharedAccountId (string) --Identifier of the directory consumer account that has access to the shared directory (OwnerDirectoryId ) in the directory owner account.

SharedDirectoryId (string) --Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.

ShareStatus (string) --Current directory status of the shared AWS Managed Microsoft AD directory.

ShareNotes (string) --A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.

CreatedDateTime (datetime) --The date and time that the shared directory was created.

LastUpdatedDateTime (datetime) --The date and time that the shared directory was last updated.








Exceptions

DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.DirectoryAlreadySharedException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SharedDirectory': {
            'OwnerAccountId': 'string',
            'OwnerDirectoryId': 'string',
            'ShareMethod': 'ORGANIZATIONS'|'HANDSHAKE',
            'SharedAccountId': 'string',
            'SharedDirectoryId': 'string',
            'ShareStatus': 'Shared'|'PendingAcceptance'|'Rejected'|'Rejecting'|'RejectFailed'|'Sharing'|'ShareFailed'|'Deleted'|'Deleting',
            'ShareNotes': 'string',
            'CreatedDateTime': datetime(2015, 1, 1),
            'LastUpdatedDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def add_ip_routes(DirectoryId=None, IpRoutes=None, UpdateSecurityGroupForDirectoryControllers=None):
    """
    If the DNS server for your on-premises domain uses a publicly addressable IP address, you must add a CIDR address block to correctly route traffic to and from your Microsoft AD on Amazon Web Services. AddIpRoutes adds this address block. You can also use AddIpRoutes to facilitate routing traffic that uses public IP ranges from your Microsoft AD on AWS to a peer VPC.
    Before you call AddIpRoutes , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the AddIpRoutes operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_ip_routes(
        DirectoryId='string',
        IpRoutes=[
            {
                'CidrIp': 'string',
                'Description': 'string'
            },
        ],
        UpdateSecurityGroupForDirectoryControllers=True|False
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nIdentifier (ID) of the directory to which to add the address block.\n

    :type IpRoutes: list
    :param IpRoutes: [REQUIRED]\nIP address blocks, using CIDR format, of the traffic to route. This is often the IP address block of the DNS server used for your on-premises domain.\n\n(dict) --IP address block. This is often the address block of the DNS server used for your on-premises domain.\n\nCidrIp (string) --IP address block using CIDR format, for example 10.0.0.0/24. This is often the address block of the DNS server used for your on-premises domain. For a single IP address use a CIDR address block with /32. For example 10.0.0.0/32.\n\nDescription (string) --Description of the address block.\n\n\n\n\n

    :type UpdateSecurityGroupForDirectoryControllers: boolean
    :param UpdateSecurityGroupForDirectoryControllers: If set to true, updates the inbound and outbound rules of the security group that has the description: 'AWS created security group for directory ID directory controllers.' Following are the new rules:\nInbound:\n\nType: Custom UDP Rule, Protocol: UDP, Range: 88, Source: 0.0.0.0/0\nType: Custom UDP Rule, Protocol: UDP, Range: 123, Source: 0.0.0.0/0\nType: Custom UDP Rule, Protocol: UDP, Range: 138, Source: 0.0.0.0/0\nType: Custom UDP Rule, Protocol: UDP, Range: 389, Source: 0.0.0.0/0\nType: Custom UDP Rule, Protocol: UDP, Range: 464, Source: 0.0.0.0/0\nType: Custom UDP Rule, Protocol: UDP, Range: 445, Source: 0.0.0.0/0\nType: Custom TCP Rule, Protocol: TCP, Range: 88, Source: 0.0.0.0/0\nType: Custom TCP Rule, Protocol: TCP, Range: 135, Source: 0.0.0.0/0\nType: Custom TCP Rule, Protocol: TCP, Range: 445, Source: 0.0.0.0/0\nType: Custom TCP Rule, Protocol: TCP, Range: 464, Source: 0.0.0.0/0\nType: Custom TCP Rule, Protocol: TCP, Range: 636, Source: 0.0.0.0/0\nType: Custom TCP Rule, Protocol: TCP, Range: 1024-65535, Source: 0.0.0.0/0\nType: Custom TCP Rule, Protocol: TCP, Range: 3268-33269, Source: 0.0.0.0/0\nType: DNS (UDP), Protocol: UDP, Range: 53, Source: 0.0.0.0/0\nType: DNS (TCP), Protocol: TCP, Range: 53, Source: 0.0.0.0/0\nType: LDAP, Protocol: TCP, Range: 389, Source: 0.0.0.0/0\nType: All ICMP, Protocol: All, Range: N/A, Source: 0.0.0.0/0\n\nOutbound:\n\nType: All traffic, Protocol: All, Range: All, Destination: 0.0.0.0/0\n\nThese security rules impact an internal network interface that is not exposed publicly.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.EntityAlreadyExistsException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.IpRouteLimitExceededException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def add_tags_to_resource(ResourceId=None, Tags=None):
    """
    Adds or overwrites one or more tags for the specified directory. Each directory can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique to each resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_tags_to_resource(
        ResourceId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nIdentifier (ID) for the directory to which to add the tag.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to be assigned to the directory.\n\n(dict) --Metadata assigned to a directory consisting of a key-value pair.\n\nKey (string) -- [REQUIRED]Required name of the tag. The string value can be Unicode characters and cannot be prefixed with 'aws:'. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) -- [REQUIRED]The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.TagLimitExceededException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


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

def cancel_schema_extension(DirectoryId=None, SchemaExtensionId=None):
    """
    Cancels an in-progress schema extension to a Microsoft AD directory. Once a schema extension has started replicating to all domain controllers, the task can no longer be canceled. A schema extension can be canceled during any of the following states; Initializing , CreatingSnapshot , and UpdatingSchema .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_schema_extension(
        DirectoryId='string',
        SchemaExtensionId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory whose schema extension will be canceled.\n

    :type SchemaExtensionId: string
    :param SchemaExtensionId: [REQUIRED]\nThe identifier of the schema extension that will be canceled.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def connect_directory(Name=None, ShortName=None, Password=None, Description=None, Size=None, ConnectSettings=None, Tags=None):
    """
    Creates an AD Connector to connect to an on-premises directory.
    Before you call ConnectDirectory , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the ConnectDirectory operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.connect_directory(
        Name='string',
        ShortName='string',
        Password='string',
        Description='string',
        Size='Small'|'Large',
        ConnectSettings={
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ],
            'CustomerDnsIps': [
                'string',
            ],
            'CustomerUserName': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe fully qualified name of the on-premises directory, such as corp.example.com .\n

    :type ShortName: string
    :param ShortName: The NetBIOS name of the on-premises directory, such as CORP .

    :type Password: string
    :param Password: [REQUIRED]\nThe password for the on-premises user account.\n

    :type Description: string
    :param Description: A description for the directory.

    :type Size: string
    :param Size: [REQUIRED]\nThe size of the directory.\n

    :type ConnectSettings: dict
    :param ConnectSettings: [REQUIRED]\nA DirectoryConnectSettings object that contains additional information for the operation.\n\nVpcId (string) -- [REQUIRED]The identifier of the VPC in which the AD Connector is created.\n\nSubnetIds (list) -- [REQUIRED]A list of subnet identifiers in the VPC in which the AD Connector is created.\n\n(string) --\n\n\nCustomerDnsIps (list) -- [REQUIRED]A list of one or more IP addresses of DNS servers or domain controllers in the on-premises directory.\n\n(string) --\n\n\nCustomerUserName (string) -- [REQUIRED]The user name of an account in the on-premises directory that is used to connect to the directory. This account must have the following permissions:\n\nRead users and groups\nCreate computer objects\nJoin computers to the domain\n\n\n\n

    :type Tags: list
    :param Tags: The tags to be assigned to AD Connector.\n\n(dict) --Metadata assigned to a directory consisting of a key-value pair.\n\nKey (string) -- [REQUIRED]Required name of the tag. The string value can be Unicode characters and cannot be prefixed with 'aws:'. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) -- [REQUIRED]The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DirectoryId': 'string'
}


Response Structure

(dict) --
Contains the results of the  ConnectDirectory operation.

DirectoryId (string) --
The identifier of the new directory.







Exceptions

DirectoryService.Client.exceptions.DirectoryLimitExceededException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'DirectoryId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.DirectoryLimitExceededException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def create_alias(DirectoryId=None, Alias=None):
    """
    Creates an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as http://<alias>.awsapps.com .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_alias(
        DirectoryId='string',
        Alias='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory for which to create the alias.\n

    :type Alias: string
    :param Alias: [REQUIRED]\nThe requested alias.\nThe alias must be unique amongst all aliases in AWS. This operation throws an EntityAlreadyExistsException error if the alias already exists.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DirectoryId': 'string',
    'Alias': 'string'
}


Response Structure

(dict) --
Contains the results of the  CreateAlias operation.

DirectoryId (string) --
The identifier of the directory.

Alias (string) --
The alias for the directory.







Exceptions

DirectoryService.Client.exceptions.EntityAlreadyExistsException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'DirectoryId': 'string',
        'Alias': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityAlreadyExistsException
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def create_computer(DirectoryId=None, ComputerName=None, Password=None, OrganizationalUnitDistinguishedName=None, ComputerAttributes=None):
    """
    Creates a computer account in the specified directory, and joins the computer to the directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_computer(
        DirectoryId='string',
        ComputerName='string',
        Password='string',
        OrganizationalUnitDistinguishedName='string',
        ComputerAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory in which to create the computer account.\n

    :type ComputerName: string
    :param ComputerName: [REQUIRED]\nThe name of the computer account.\n

    :type Password: string
    :param Password: [REQUIRED]\nA one-time password that is used to join the computer to the directory. You should generate a random, strong password to use for this parameter.\n

    :type OrganizationalUnitDistinguishedName: string
    :param OrganizationalUnitDistinguishedName: The fully-qualified distinguished name of the organizational unit to place the computer account in.

    :type ComputerAttributes: list
    :param ComputerAttributes: An array of Attribute objects that contain any LDAP attributes to apply to the computer account.\n\n(dict) --Represents a named directory attribute.\n\nName (string) --The name of the attribute.\n\nValue (string) --The value of the attribute.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Computer': {
        'ComputerId': 'string',
        'ComputerName': 'string',
        'ComputerAttributes': [
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Contains the results for the  CreateComputer operation.

Computer (dict) --
A  Computer object that represents the computer account.

ComputerId (string) --
The identifier of the computer.

ComputerName (string) --
The computer name.

ComputerAttributes (list) --
An array of  Attribute objects containing the LDAP attributes that belong to the computer account.

(dict) --
Represents a named directory attribute.

Name (string) --
The name of the attribute.

Value (string) --
The value of the attribute.













Exceptions

DirectoryService.Client.exceptions.AuthenticationFailedException
DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.EntityAlreadyExistsException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'Computer': {
            'ComputerId': 'string',
            'ComputerName': 'string',
            'ComputerAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.AuthenticationFailedException
    DirectoryService.Client.exceptions.DirectoryUnavailableException
    DirectoryService.Client.exceptions.EntityAlreadyExistsException
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def create_conditional_forwarder(DirectoryId=None, RemoteDomainName=None, DnsIpAddrs=None):
    """
    Creates a conditional forwarder associated with your AWS directory. Conditional forwarders are required in order to set up a trust relationship with another domain. The conditional forwarder points to the trusted domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_conditional_forwarder(
        DirectoryId='string',
        RemoteDomainName='string',
        DnsIpAddrs=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe directory ID of the AWS directory for which you are creating the conditional forwarder.\n

    :type RemoteDomainName: string
    :param RemoteDomainName: [REQUIRED]\nThe fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.\n

    :type DnsIpAddrs: list
    :param DnsIpAddrs: [REQUIRED]\nThe IP addresses of the remote DNS server associated with RemoteDomainName.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The result of a CreateConditinalForwarder request.





Exceptions

DirectoryService.Client.exceptions.EntityAlreadyExistsException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityAlreadyExistsException
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.DirectoryUnavailableException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def create_directory(Name=None, ShortName=None, Password=None, Description=None, Size=None, VpcSettings=None, Tags=None):
    """
    Creates a Simple AD directory. For more information, see Simple Active Directory in the AWS Directory Service Admin Guide .
    Before you call CreateDirectory , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the CreateDirectory operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_directory(
        Name='string',
        ShortName='string',
        Password='string',
        Description='string',
        Size='Small'|'Large',
        VpcSettings={
            'VpcId': 'string',
            'SubnetIds': [
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
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe fully qualified name for the directory, such as corp.example.com .\n

    :type ShortName: string
    :param ShortName: The NetBIOS name of the directory, such as CORP .

    :type Password: string
    :param Password: [REQUIRED]\nThe password for the directory administrator. The directory creation process creates a directory administrator account with the user name Administrator and this password.\nIf you need to change the password for the administrator account, you can use the ResetUserPassword API call.\n

    :type Description: string
    :param Description: A description for the directory.

    :type Size: string
    :param Size: [REQUIRED]\nThe size of the directory.\n

    :type VpcSettings: dict
    :param VpcSettings: A DirectoryVpcSettings object that contains additional information for the operation.\n\nVpcId (string) -- [REQUIRED]The identifier of the VPC in which to create the directory.\n\nSubnetIds (list) -- [REQUIRED]The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service creates a directory server and a DNS server in each of these subnets.\n\n(string) --\n\n\n\n

    :type Tags: list
    :param Tags: The tags to be assigned to the Simple AD directory.\n\n(dict) --Metadata assigned to a directory consisting of a key-value pair.\n\nKey (string) -- [REQUIRED]Required name of the tag. The string value can be Unicode characters and cannot be prefixed with 'aws:'. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) -- [REQUIRED]The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DirectoryId': 'string'
}


Response Structure

(dict) --
Contains the results of the  CreateDirectory operation.

DirectoryId (string) --
The identifier of the directory that was created.







Exceptions

DirectoryService.Client.exceptions.DirectoryLimitExceededException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'DirectoryId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.DirectoryLimitExceededException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def create_log_subscription(DirectoryId=None, LogGroupName=None):
    """
    Creates a subscription to forward real-time Directory Service domain controller security logs to the specified Amazon CloudWatch log group in your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_log_subscription(
        DirectoryId='string',
        LogGroupName='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nIdentifier of the directory to which you want to subscribe and receive real-time logs to your specified CloudWatch log group.\n

    :type LogGroupName: string
    :param LogGroupName: [REQUIRED]\nThe name of the CloudWatch log group where the real-time domain controller logs are forwarded.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.EntityAlreadyExistsException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.InsufficientPermissionsException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_microsoft_ad(Name=None, ShortName=None, Password=None, Description=None, VpcSettings=None, Edition=None, Tags=None):
    """
    Creates a Microsoft AD directory in the AWS Cloud. For more information, see AWS Managed Microsoft AD in the AWS Directory Service Admin Guide .
    Before you call CreateMicrosoftAD , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the CreateMicrosoftAD operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_microsoft_ad(
        Name='string',
        ShortName='string',
        Password='string',
        Description='string',
        VpcSettings={
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ]
        },
        Edition='Enterprise'|'Standard',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe fully qualified domain name for the AWS Managed Microsoft AD directory, such as corp.example.com . This name will resolve inside your VPC only. It does not need to be publicly resolvable.\n

    :type ShortName: string
    :param ShortName: The NetBIOS name for your domain, such as CORP . If you don\'t specify a NetBIOS name, it will default to the first part of your directory DNS. For example, CORP for the directory DNS corp.example.com .

    :type Password: string
    :param Password: [REQUIRED]\nThe password for the default administrative user named Admin .\nIf you need to change the password for the administrator account, you can use the ResetUserPassword API call.\n

    :type Description: string
    :param Description: A description for the directory. This label will appear on the AWS console Directory Details page after the directory is created.

    :type VpcSettings: dict
    :param VpcSettings: [REQUIRED]\nContains VPC information for the CreateDirectory or CreateMicrosoftAD operation.\n\nVpcId (string) -- [REQUIRED]The identifier of the VPC in which to create the directory.\n\nSubnetIds (list) -- [REQUIRED]The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service creates a directory server and a DNS server in each of these subnets.\n\n(string) --\n\n\n\n

    :type Edition: string
    :param Edition: AWS Managed Microsoft AD is available in two editions: Standard and Enterprise . Enterprise is the default.

    :type Tags: list
    :param Tags: The tags to be assigned to the AWS Managed Microsoft AD directory.\n\n(dict) --Metadata assigned to a directory consisting of a key-value pair.\n\nKey (string) -- [REQUIRED]Required name of the tag. The string value can be Unicode characters and cannot be prefixed with 'aws:'. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\nValue (string) -- [REQUIRED]The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: '^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$').\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DirectoryId': 'string'
}


Response Structure

(dict) --
Result of a CreateMicrosoftAD request.

DirectoryId (string) --
The identifier of the directory that was created.







Exceptions

DirectoryService.Client.exceptions.DirectoryLimitExceededException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException
DirectoryService.Client.exceptions.UnsupportedOperationException


    :return: {
        'DirectoryId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.DirectoryLimitExceededException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    
    """
    pass

def create_snapshot(DirectoryId=None, Name=None):
    """
    Creates a snapshot of a Simple AD or Microsoft AD directory in the AWS cloud.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_snapshot(
        DirectoryId='string',
        Name='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory of which to take a snapshot.\n

    :type Name: string
    :param Name: The descriptive name to apply to the snapshot.

    :rtype: dict

ReturnsResponse Syntax
{
    'SnapshotId': 'string'
}


Response Structure

(dict) --
Contains the results of the  CreateSnapshot operation.

SnapshotId (string) --
The identifier of the snapshot that was created.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.SnapshotLimitExceededException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SnapshotId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.SnapshotLimitExceededException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def create_trust(DirectoryId=None, RemoteDomainName=None, TrustPassword=None, TrustDirection=None, TrustType=None, ConditionalForwarderIpAddrs=None, SelectiveAuth=None):
    """
    AWS Directory Service for Microsoft Active Directory allows you to configure trust relationships. For example, you can establish a trust between your AWS Managed Microsoft AD directory, and your existing on-premises Microsoft Active Directory. This would allow you to provide users and groups access to resources in either domain, with a single set of credentials.
    This action initiates the creation of the AWS side of a trust relationship between an AWS Managed Microsoft AD directory and an external domain. You can create either a forest trust or an external trust.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_trust(
        DirectoryId='string',
        RemoteDomainName='string',
        TrustPassword='string',
        TrustDirection='One-Way: Outgoing'|'One-Way: Incoming'|'Two-Way',
        TrustType='Forest'|'External',
        ConditionalForwarderIpAddrs=[
            'string',
        ],
        SelectiveAuth='Enabled'|'Disabled'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe Directory ID of the AWS Managed Microsoft AD directory for which to establish the trust relationship.\n

    :type RemoteDomainName: string
    :param RemoteDomainName: [REQUIRED]\nThe Fully Qualified Domain Name (FQDN) of the external domain for which to create the trust relationship.\n

    :type TrustPassword: string
    :param TrustPassword: [REQUIRED]\nThe trust password. The must be the same password that was used when creating the trust relationship on the external domain.\n

    :type TrustDirection: string
    :param TrustDirection: [REQUIRED]\nThe direction of the trust relationship.\n

    :type TrustType: string
    :param TrustType: The trust relationship type. Forest is the default.

    :type ConditionalForwarderIpAddrs: list
    :param ConditionalForwarderIpAddrs: The IP addresses of the remote DNS server associated with RemoteDomainName.\n\n(string) --\n\n

    :type SelectiveAuth: string
    :param SelectiveAuth: Optional parameter to enable selective authentication for the trust.

    :rtype: dict

ReturnsResponse Syntax
{
    'TrustId': 'string'
}


Response Structure

(dict) --
The result of a CreateTrust request.

TrustId (string) --
A unique identifier for the trust relationship that was created.







Exceptions

DirectoryService.Client.exceptions.EntityAlreadyExistsException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException
DirectoryService.Client.exceptions.UnsupportedOperationException


    :return: {
        'TrustId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityAlreadyExistsException
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    
    """
    pass

def delete_conditional_forwarder(DirectoryId=None, RemoteDomainName=None):
    """
    Deletes a conditional forwarder that has been set up for your AWS directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_conditional_forwarder(
        DirectoryId='string',
        RemoteDomainName='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe directory ID for which you are deleting the conditional forwarder.\n

    :type RemoteDomainName: string
    :param RemoteDomainName: [REQUIRED]\nThe fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The result of a DeleteConditionalForwarder request.





Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.DirectoryUnavailableException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def delete_directory(DirectoryId=None):
    """
    Deletes an AWS Directory Service directory.
    Before you call DeleteDirectory , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the DeleteDirectory operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_directory(
        DirectoryId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DirectoryId': 'string'
}


Response Structure

(dict) --Contains the results of the  DeleteDirectory operation.

DirectoryId (string) --The directory identifier.






Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'DirectoryId': 'string'
    }
    
    
    """
    pass

def delete_log_subscription(DirectoryId=None):
    """
    Deletes the specified log subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_log_subscription(
        DirectoryId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nIdentifier of the directory whose log subscription you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def delete_snapshot(SnapshotId=None):
    """
    Deletes a directory snapshot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_snapshot(
        SnapshotId='string'
    )
    
    
    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]\nThe identifier of the directory snapshot to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SnapshotId': 'string'
}


Response Structure

(dict) --Contains the results of the  DeleteSnapshot operation.

SnapshotId (string) --The identifier of the directory snapshot that was deleted.






Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SnapshotId': 'string'
    }
    
    
    """
    pass

def delete_trust(TrustId=None, DeleteAssociatedConditionalForwarder=None):
    """
    Deletes an existing trust relationship between your AWS Managed Microsoft AD directory and an external domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_trust(
        TrustId='string',
        DeleteAssociatedConditionalForwarder=True|False
    )
    
    
    :type TrustId: string
    :param TrustId: [REQUIRED]\nThe Trust ID of the trust relationship to be deleted.\n

    :type DeleteAssociatedConditionalForwarder: boolean
    :param DeleteAssociatedConditionalForwarder: Delete a conditional forwarder as part of a DeleteTrustRequest.

    :rtype: dict

ReturnsResponse Syntax
{
    'TrustId': 'string'
}


Response Structure

(dict) --
The result of a DeleteTrust request.

TrustId (string) --
The Trust ID of the trust relationship that was deleted.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException
DirectoryService.Client.exceptions.UnsupportedOperationException


    :return: {
        'TrustId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    
    """
    pass

def deregister_certificate(DirectoryId=None, CertificateId=None):
    """
    Deletes from the system the certificate that was registered for a secured LDAP connection.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_certificate(
        DirectoryId='string',
        CertificateId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory.\n

    :type CertificateId: string
    :param CertificateId: [REQUIRED]\nThe identifier of the certificate.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.DirectoryDoesNotExistException
DirectoryService.Client.exceptions.CertificateDoesNotExistException
DirectoryService.Client.exceptions.CertificateInUseException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def deregister_event_topic(DirectoryId=None, TopicName=None):
    """
    Removes the specified directory as a publisher to the specified SNS topic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_event_topic(
        DirectoryId='string',
        TopicName='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe Directory ID to remove as a publisher. This directory will no longer send messages to the specified SNS topic.\n

    :type TopicName: string
    :param TopicName: [REQUIRED]\nThe name of the SNS topic from which to remove the directory as a publisher.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The result of a DeregisterEventTopic request.





Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def describe_certificate(DirectoryId=None, CertificateId=None):
    """
    Displays information about the certificate registered for a secured LDAP connection.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_certificate(
        DirectoryId='string',
        CertificateId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory.\n

    :type CertificateId: string
    :param CertificateId: [REQUIRED]\nThe identifier of the certificate.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Certificate': {
        'CertificateId': 'string',
        'State': 'Registering'|'Registered'|'RegisterFailed'|'Deregistering'|'Deregistered'|'DeregisterFailed',
        'StateReason': 'string',
        'CommonName': 'string',
        'RegisteredDateTime': datetime(2015, 1, 1),
        'ExpiryDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Certificate (dict) --
Information about the certificate, including registered date time, certificate state, the reason for the state, expiration date time, and certificate common name.

CertificateId (string) --
The identifier of the certificate.

State (string) --
The state of the certificate.

StateReason (string) --
Describes a state change for the certificate.

CommonName (string) --
The common name for the certificate.

RegisteredDateTime (datetime) --
The date and time that the certificate was registered.

ExpiryDateTime (datetime) --
The date and time when the certificate will expire.









Exceptions

DirectoryService.Client.exceptions.DirectoryDoesNotExistException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.CertificateDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'Certificate': {
            'CertificateId': 'string',
            'State': 'Registering'|'Registered'|'RegisterFailed'|'Deregistering'|'Deregistered'|'DeregisterFailed',
            'StateReason': 'string',
            'CommonName': 'string',
            'RegisteredDateTime': datetime(2015, 1, 1),
            'ExpiryDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.DirectoryDoesNotExistException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.CertificateDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def describe_conditional_forwarders(DirectoryId=None, RemoteDomainNames=None):
    """
    Obtains information about the conditional forwarders for this account.
    If no input parameters are provided for RemoteDomainNames, this request describes all conditional forwarders for the specified directory ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_conditional_forwarders(
        DirectoryId='string',
        RemoteDomainNames=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe directory ID for which to get the list of associated conditional forwarders.\n

    :type RemoteDomainNames: list
    :param RemoteDomainNames: The fully qualified domain names (FQDN) of the remote domains for which to get the list of associated conditional forwarders. If this member is null, all conditional forwarders are returned.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConditionalForwarders': [
        {
            'RemoteDomainName': 'string',
            'DnsIpAddrs': [
                'string',
            ],
            'ReplicationScope': 'Domain'
        },
    ]
}


Response Structure

(dict) --
The result of a DescribeConditionalForwarder request.

ConditionalForwarders (list) --
The list of conditional forwarders that have been created.

(dict) --
Points to a remote domain with which you are setting up a trust relationship. Conditional forwarders are required in order to set up a trust relationship with another domain.

RemoteDomainName (string) --
The fully qualified domain name (FQDN) of the remote domains pointed to by the conditional forwarder.

DnsIpAddrs (list) --
The IP addresses of the remote DNS server associated with RemoteDomainName. This is the IP address of the DNS server that your conditional forwarder points to.

(string) --


ReplicationScope (string) --
The replication scope of the conditional forwarder. The only allowed value is Domain , which will replicate the conditional forwarder to all of the domain controllers for your AWS directory.











Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'ConditionalForwarders': [
            {
                'RemoteDomainName': 'string',
                'DnsIpAddrs': [
                    'string',
                ],
                'ReplicationScope': 'Domain'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_directories(DirectoryIds=None, NextToken=None, Limit=None):
    """
    Obtains information about the directories that belong to this account.
    You can retrieve information about specific directories by passing the directory identifiers in the DirectoryIds parameter. Otherwise, all directories that belong to the current account are returned.
    This operation supports pagination with the use of the NextToken request and response parameters. If more results are available, the DescribeDirectoriesResult.NextToken member contains a token that you pass in the next call to  DescribeDirectories to retrieve the next set of items.
    You can also specify a maximum number of return results with the Limit parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_directories(
        DirectoryIds=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryIds: list
    :param DirectoryIds: A list of identifiers of the directories for which to obtain the information. If this member is null, all directories that belong to the current account are returned.\nAn empty list results in an InvalidParameterException being thrown.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The DescribeDirectoriesResult.NextToken value from a previous call to DescribeDirectories . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.

    :rtype: dict

ReturnsResponse Syntax
{
    'DirectoryDescriptions': [
        {
            'DirectoryId': 'string',
            'Name': 'string',
            'ShortName': 'string',
            'Size': 'Small'|'Large',
            'Edition': 'Enterprise'|'Standard',
            'Alias': 'string',
            'AccessUrl': 'string',
            'Description': 'string',
            'DnsIpAddrs': [
                'string',
            ],
            'Stage': 'Requested'|'Creating'|'Created'|'Active'|'Inoperable'|'Impaired'|'Restoring'|'RestoreFailed'|'Deleting'|'Deleted'|'Failed',
            'ShareStatus': 'Shared'|'PendingAcceptance'|'Rejected'|'Rejecting'|'RejectFailed'|'Sharing'|'ShareFailed'|'Deleted'|'Deleting',
            'ShareMethod': 'ORGANIZATIONS'|'HANDSHAKE',
            'ShareNotes': 'string',
            'LaunchTime': datetime(2015, 1, 1),
            'StageLastUpdatedDateTime': datetime(2015, 1, 1),
            'Type': 'SimpleAD'|'ADConnector'|'MicrosoftAD'|'SharedMicrosoftAD',
            'VpcSettings': {
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupId': 'string',
                'AvailabilityZones': [
                    'string',
                ]
            },
            'ConnectSettings': {
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'CustomerUserName': 'string',
                'SecurityGroupId': 'string',
                'AvailabilityZones': [
                    'string',
                ],
                'ConnectIps': [
                    'string',
                ]
            },
            'RadiusSettings': {
                'RadiusServers': [
                    'string',
                ],
                'RadiusPort': 123,
                'RadiusTimeout': 123,
                'RadiusRetries': 123,
                'SharedSecret': 'string',
                'AuthenticationProtocol': 'PAP'|'CHAP'|'MS-CHAPv1'|'MS-CHAPv2',
                'DisplayLabel': 'string',
                'UseSameUsername': True|False
            },
            'RadiusStatus': 'Creating'|'Completed'|'Failed',
            'StageReason': 'string',
            'SsoEnabled': True|False,
            'DesiredNumberOfDomainControllers': 123,
            'OwnerDirectoryDescription': {
                'DirectoryId': 'string',
                'AccountId': 'string',
                'DnsIpAddrs': [
                    'string',
                ],
                'VpcSettings': {
                    'VpcId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupId': 'string',
                    'AvailabilityZones': [
                        'string',
                    ]
                },
                'RadiusSettings': {
                    'RadiusServers': [
                        'string',
                    ],
                    'RadiusPort': 123,
                    'RadiusTimeout': 123,
                    'RadiusRetries': 123,
                    'SharedSecret': 'string',
                    'AuthenticationProtocol': 'PAP'|'CHAP'|'MS-CHAPv1'|'MS-CHAPv2',
                    'DisplayLabel': 'string',
                    'UseSameUsername': True|False
                },
                'RadiusStatus': 'Creating'|'Completed'|'Failed'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Contains the results of the  DescribeDirectories operation.

DirectoryDescriptions (list) --
The list of  DirectoryDescription objects that were retrieved.
It is possible that this list contains less than the number of items specified in the Limit member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.

(dict) --
Contains information about an AWS Directory Service directory.

DirectoryId (string) --
The directory identifier.

Name (string) --
The fully qualified name of the directory.

ShortName (string) --
The short name of the directory.

Size (string) --
The directory size.

Edition (string) --
The edition associated with this directory.

Alias (string) --
The alias for the directory. If no alias has been created for the directory, the alias is the directory identifier, such as d-XXXXXXXXXX .

AccessUrl (string) --
The access URL for the directory, such as http://<alias>.awsapps.com . If no alias has been created for the directory, <alias> is the directory identifier, such as d-XXXXXXXXXX .

Description (string) --
The description for the directory.

DnsIpAddrs (list) --
The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers. For an AD Connector directory, these are the IP addresses of the DNS servers or domain controllers in the on-premises directory to which the AD Connector is connected.

(string) --


Stage (string) --
The current stage of the directory.

ShareStatus (string) --
Current directory status of the shared AWS Managed Microsoft AD directory.

ShareMethod (string) --
The method used when sharing a directory to determine whether the directory should be shared within your AWS organization (ORGANIZATIONS ) or with any AWS account by sending a shared directory request (HANDSHAKE ).

ShareNotes (string) --
A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.

LaunchTime (datetime) --
Specifies when the directory was created.

StageLastUpdatedDateTime (datetime) --
The date and time that the stage was last updated.

Type (string) --
The directory size.

VpcSettings (dict) --
A  DirectoryVpcSettingsDescription object that contains additional information about a directory. This member is only present if the directory is a Simple AD or Managed AD directory.

VpcId (string) --
The identifier of the VPC that the directory is in.

SubnetIds (list) --
The identifiers of the subnets for the directory servers.

(string) --


SecurityGroupId (string) --
The domain controller security group identifier for the directory.

AvailabilityZones (list) --
The list of Availability Zones that the directory is in.

(string) --




ConnectSettings (dict) --
A  DirectoryConnectSettingsDescription object that contains additional information about an AD Connector directory. This member is only present if the directory is an AD Connector directory.

VpcId (string) --
The identifier of the VPC that the AD Connector is in.

SubnetIds (list) --
A list of subnet identifiers in the VPC that the AD Connector is in.

(string) --


CustomerUserName (string) --
The user name of the service account in the on-premises directory.

SecurityGroupId (string) --
The security group identifier for the AD Connector directory.

AvailabilityZones (list) --
A list of the Availability Zones that the directory is in.

(string) --


ConnectIps (list) --
The IP addresses of the AD Connector servers.

(string) --




RadiusSettings (dict) --
A  RadiusSettings object that contains information about the RADIUS server configured for this directory.

RadiusServers (list) --
An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.

(string) --


RadiusPort (integer) --
The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.

RadiusTimeout (integer) --
The amount of time, in seconds, to wait for the RADIUS server to respond.

RadiusRetries (integer) --
The maximum number of times that communication with the RADIUS server is attempted.

SharedSecret (string) --
Required for enabling RADIUS on the directory.

AuthenticationProtocol (string) --
The protocol specified for your RADIUS endpoints.

DisplayLabel (string) --
Not currently used.

UseSameUsername (boolean) --
Not currently used.



RadiusStatus (string) --
The status of the RADIUS MFA server connection.

StageReason (string) --
Additional information about the directory stage.

SsoEnabled (boolean) --
Indicates if single sign-on is enabled for the directory. For more information, see  EnableSso and  DisableSso .

DesiredNumberOfDomainControllers (integer) --
The desired number of domain controllers in the directory if the directory is Microsoft AD.

OwnerDirectoryDescription (dict) --
Describes the AWS Managed Microsoft AD directory in the directory owner account.

DirectoryId (string) --
Identifier of the AWS Managed Microsoft AD directory in the directory owner account.

AccountId (string) --
Identifier of the directory owner account.

DnsIpAddrs (list) --
IP address of the directory\xe2\x80\x99s domain controllers.

(string) --


VpcSettings (dict) --
Information about the VPC settings for the directory.

VpcId (string) --
The identifier of the VPC that the directory is in.

SubnetIds (list) --
The identifiers of the subnets for the directory servers.

(string) --


SecurityGroupId (string) --
The domain controller security group identifier for the directory.

AvailabilityZones (list) --
The list of Availability Zones that the directory is in.

(string) --




RadiusSettings (dict) --
A  RadiusSettings object that contains information about the RADIUS server.

RadiusServers (list) --
An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.

(string) --


RadiusPort (integer) --
The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.

RadiusTimeout (integer) --
The amount of time, in seconds, to wait for the RADIUS server to respond.

RadiusRetries (integer) --
The maximum number of times that communication with the RADIUS server is attempted.

SharedSecret (string) --
Required for enabling RADIUS on the directory.

AuthenticationProtocol (string) --
The protocol specified for your RADIUS endpoints.

DisplayLabel (string) --
Not currently used.

UseSameUsername (boolean) --
Not currently used.



RadiusStatus (string) --
Information about the status of the RADIUS server.







NextToken (string) --
If not null, more results are available. Pass this value for the NextToken parameter in a subsequent call to  DescribeDirectories to retrieve the next set of items.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'DirectoryDescriptions': [
            {
                'DirectoryId': 'string',
                'Name': 'string',
                'ShortName': 'string',
                'Size': 'Small'|'Large',
                'Edition': 'Enterprise'|'Standard',
                'Alias': 'string',
                'AccessUrl': 'string',
                'Description': 'string',
                'DnsIpAddrs': [
                    'string',
                ],
                'Stage': 'Requested'|'Creating'|'Created'|'Active'|'Inoperable'|'Impaired'|'Restoring'|'RestoreFailed'|'Deleting'|'Deleted'|'Failed',
                'ShareStatus': 'Shared'|'PendingAcceptance'|'Rejected'|'Rejecting'|'RejectFailed'|'Sharing'|'ShareFailed'|'Deleted'|'Deleting',
                'ShareMethod': 'ORGANIZATIONS'|'HANDSHAKE',
                'ShareNotes': 'string',
                'LaunchTime': datetime(2015, 1, 1),
                'StageLastUpdatedDateTime': datetime(2015, 1, 1),
                'Type': 'SimpleAD'|'ADConnector'|'MicrosoftAD'|'SharedMicrosoftAD',
                'VpcSettings': {
                    'VpcId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupId': 'string',
                    'AvailabilityZones': [
                        'string',
                    ]
                },
                'ConnectSettings': {
                    'VpcId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'CustomerUserName': 'string',
                    'SecurityGroupId': 'string',
                    'AvailabilityZones': [
                        'string',
                    ],
                    'ConnectIps': [
                        'string',
                    ]
                },
                'RadiusSettings': {
                    'RadiusServers': [
                        'string',
                    ],
                    'RadiusPort': 123,
                    'RadiusTimeout': 123,
                    'RadiusRetries': 123,
                    'SharedSecret': 'string',
                    'AuthenticationProtocol': 'PAP'|'CHAP'|'MS-CHAPv1'|'MS-CHAPv2',
                    'DisplayLabel': 'string',
                    'UseSameUsername': True|False
                },
                'RadiusStatus': 'Creating'|'Completed'|'Failed',
                'StageReason': 'string',
                'SsoEnabled': True|False,
                'DesiredNumberOfDomainControllers': 123,
                'OwnerDirectoryDescription': {
                    'DirectoryId': 'string',
                    'AccountId': 'string',
                    'DnsIpAddrs': [
                        'string',
                    ],
                    'VpcSettings': {
                        'VpcId': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupId': 'string',
                        'AvailabilityZones': [
                            'string',
                        ]
                    },
                    'RadiusSettings': {
                        'RadiusServers': [
                            'string',
                        ],
                        'RadiusPort': 123,
                        'RadiusTimeout': 123,
                        'RadiusRetries': 123,
                        'SharedSecret': 'string',
                        'AuthenticationProtocol': 'PAP'|'CHAP'|'MS-CHAPv1'|'MS-CHAPv2',
                        'DisplayLabel': 'string',
                        'UseSameUsername': True|False
                    },
                    'RadiusStatus': 'Creating'|'Completed'|'Failed'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_domain_controllers(DirectoryId=None, DomainControllerIds=None, NextToken=None, Limit=None):
    """
    Provides information about any domain controllers in your directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_domain_controllers(
        DirectoryId='string',
        DomainControllerIds=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nIdentifier of the directory for which to retrieve the domain controller information.\n

    :type DomainControllerIds: list
    :param DomainControllerIds: A list of identifiers for the domain controllers whose information will be provided.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The DescribeDomainControllers.NextToken value from a previous call to DescribeDomainControllers . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'DomainControllers': [
        {
            'DirectoryId': 'string',
            'DomainControllerId': 'string',
            'DnsIpAddr': 'string',
            'VpcId': 'string',
            'SubnetId': 'string',
            'AvailabilityZone': 'string',
            'Status': 'Creating'|'Active'|'Impaired'|'Restoring'|'Deleting'|'Deleted'|'Failed',
            'StatusReason': 'string',
            'LaunchTime': datetime(2015, 1, 1),
            'StatusLastUpdatedDateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DomainControllers (list) --
List of the  DomainController objects that were retrieved.

(dict) --
Contains information about the domain controllers for a specified directory.

DirectoryId (string) --
Identifier of the directory where the domain controller resides.

DomainControllerId (string) --
Identifies a specific domain controller in the directory.

DnsIpAddr (string) --
The IP address of the domain controller.

VpcId (string) --
The identifier of the VPC that contains the domain controller.

SubnetId (string) --
Identifier of the subnet in the VPC that contains the domain controller.

AvailabilityZone (string) --
The Availability Zone where the domain controller is located.

Status (string) --
The status of the domain controller.

StatusReason (string) --
A description of the domain controller state.

LaunchTime (datetime) --
Specifies when the domain controller was created.

StatusLastUpdatedDateTime (datetime) --
The date and time that the status was last updated.





NextToken (string) --
If not null, more results are available. Pass this value for the NextToken parameter in a subsequent call to  DescribeDomainControllers retrieve the next set of items.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException
DirectoryService.Client.exceptions.UnsupportedOperationException


    :return: {
        'DomainControllers': [
            {
                'DirectoryId': 'string',
                'DomainControllerId': 'string',
                'DnsIpAddr': 'string',
                'VpcId': 'string',
                'SubnetId': 'string',
                'AvailabilityZone': 'string',
                'Status': 'Creating'|'Active'|'Impaired'|'Restoring'|'Deleting'|'Deleted'|'Failed',
                'StatusReason': 'string',
                'LaunchTime': datetime(2015, 1, 1),
                'StatusLastUpdatedDateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    
    """
    pass

def describe_event_topics(DirectoryId=None, TopicNames=None):
    """
    Obtains information about which SNS topics receive status messages from the specified directory.
    If no input parameters are provided, such as DirectoryId or TopicName, this request describes all of the associations in the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_topics(
        DirectoryId='string',
        TopicNames=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: The Directory ID for which to get the list of associated SNS topics. If this member is null, associations for all Directory IDs are returned.

    :type TopicNames: list
    :param TopicNames: A list of SNS topic names for which to obtain the information. If this member is null, all associations for the specified Directory ID are returned.\nAn empty list results in an InvalidParameterException being thrown.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EventTopics': [
        {
            'DirectoryId': 'string',
            'TopicName': 'string',
            'TopicArn': 'string',
            'CreatedDateTime': datetime(2015, 1, 1),
            'Status': 'Registered'|'Topic not found'|'Failed'|'Deleted'
        },
    ]
}


Response Structure

(dict) --
The result of a DescribeEventTopic request.

EventTopics (list) --
A list of SNS topic names that receive status messages from the specified Directory ID.

(dict) --
Information about SNS topic and AWS Directory Service directory associations.

DirectoryId (string) --
The Directory ID of an AWS Directory Service directory that will publish status messages to an SNS topic.

TopicName (string) --
The name of an AWS SNS topic the receives status messages from the directory.

TopicArn (string) --
The SNS topic ARN (Amazon Resource Name).

CreatedDateTime (datetime) --
The date and time of when you associated your directory with the SNS topic.

Status (string) --
The topic registration status.











Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'EventTopics': [
            {
                'DirectoryId': 'string',
                'TopicName': 'string',
                'TopicArn': 'string',
                'CreatedDateTime': datetime(2015, 1, 1),
                'Status': 'Registered'|'Topic not found'|'Failed'|'Deleted'
            },
        ]
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def describe_ldaps_settings(DirectoryId=None, Type=None, NextToken=None, Limit=None):
    """
    Describes the status of LDAP security for the specified directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_ldaps_settings(
        DirectoryId='string',
        Type='Client',
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory.\n

    :type Type: string
    :param Type: The type of LDAP security to enable. Currently only the value Client is supported.

    :type NextToken: string
    :param NextToken: The type of next token used for pagination.

    :type Limit: integer
    :param Limit: Specifies the number of items that should be displayed on one page.

    :rtype: dict

ReturnsResponse Syntax
{
    'LDAPSSettingsInfo': [
        {
            'LDAPSStatus': 'Enabling'|'Enabled'|'EnableFailed'|'Disabled',
            'LDAPSStatusReason': 'string',
            'LastUpdatedDateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LDAPSSettingsInfo (list) --
Information about LDAP security for the specified directory, including status of enablement, state last updated date time, and the reason for the state.

(dict) --
Contains general information about the LDAPS settings.

LDAPSStatus (string) --
The state of the LDAPS settings.

LDAPSStatusReason (string) --
Describes a state change for LDAPS.

LastUpdatedDateTime (datetime) --
The date and time when the LDAPS settings were last updated.





NextToken (string) --
The next token used to retrieve the LDAPS settings if the number of setting types exceeds page limit and there is another page.







Exceptions

DirectoryService.Client.exceptions.DirectoryDoesNotExistException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'LDAPSSettingsInfo': [
            {
                'LDAPSStatus': 'Enabling'|'Enabled'|'EnableFailed'|'Disabled',
                'LDAPSStatusReason': 'string',
                'LastUpdatedDateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.DirectoryDoesNotExistException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def describe_shared_directories(OwnerDirectoryId=None, SharedDirectoryIds=None, NextToken=None, Limit=None):
    """
    Returns the shared directories in your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_shared_directories(
        OwnerDirectoryId='string',
        SharedDirectoryIds=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type OwnerDirectoryId: string
    :param OwnerDirectoryId: [REQUIRED]\nReturns the identifier of the directory in the directory owner account.\n

    :type SharedDirectoryIds: list
    :param SharedDirectoryIds: A list of identifiers of all shared directories in your account.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The DescribeSharedDirectoriesResult.NextToken value from a previous call to DescribeSharedDirectories . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The number of shared directories to return in the response object.

    :rtype: dict

ReturnsResponse Syntax
{
    'SharedDirectories': [
        {
            'OwnerAccountId': 'string',
            'OwnerDirectoryId': 'string',
            'ShareMethod': 'ORGANIZATIONS'|'HANDSHAKE',
            'SharedAccountId': 'string',
            'SharedDirectoryId': 'string',
            'ShareStatus': 'Shared'|'PendingAcceptance'|'Rejected'|'Rejecting'|'RejectFailed'|'Sharing'|'ShareFailed'|'Deleted'|'Deleting',
            'ShareNotes': 'string',
            'CreatedDateTime': datetime(2015, 1, 1),
            'LastUpdatedDateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SharedDirectories (list) --
A list of all shared directories in your account.

(dict) --
Details about the shared directory in the directory owner account for which the share request in the directory consumer account has been accepted.

OwnerAccountId (string) --
Identifier of the directory owner account, which contains the directory that has been shared to the consumer account.

OwnerDirectoryId (string) --
Identifier of the directory in the directory owner account.

ShareMethod (string) --
The method used when sharing a directory to determine whether the directory should be shared within your AWS organization (ORGANIZATIONS ) or with any AWS account by sending a shared directory request (HANDSHAKE ).

SharedAccountId (string) --
Identifier of the directory consumer account that has access to the shared directory (OwnerDirectoryId ) in the directory owner account.

SharedDirectoryId (string) --
Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.

ShareStatus (string) --
Current directory status of the shared AWS Managed Microsoft AD directory.

ShareNotes (string) --
A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.

CreatedDateTime (datetime) --
The date and time that the shared directory was created.

LastUpdatedDateTime (datetime) --
The date and time that the shared directory was last updated.





NextToken (string) --
If not null, token that indicates that more results are available. Pass this value for the NextToken parameter in a subsequent call to  DescribeSharedDirectories to retrieve the next set of items.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SharedDirectories': [
            {
                'OwnerAccountId': 'string',
                'OwnerDirectoryId': 'string',
                'ShareMethod': 'ORGANIZATIONS'|'HANDSHAKE',
                'SharedAccountId': 'string',
                'SharedDirectoryId': 'string',
                'ShareStatus': 'Shared'|'PendingAcceptance'|'Rejected'|'Rejecting'|'RejectFailed'|'Sharing'|'ShareFailed'|'Deleted'|'Deleting',
                'ShareNotes': 'string',
                'CreatedDateTime': datetime(2015, 1, 1),
                'LastUpdatedDateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def describe_snapshots(DirectoryId=None, SnapshotIds=None, NextToken=None, Limit=None):
    """
    Obtains information about the directory snapshots that belong to this account.
    This operation supports pagination with the use of the NextToken request and response parameters. If more results are available, the DescribeSnapshots.NextToken member contains a token that you pass in the next call to  DescribeSnapshots to retrieve the next set of items.
    You can also specify a maximum number of return results with the Limit parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_snapshots(
        DirectoryId='string',
        SnapshotIds=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: The identifier of the directory for which to retrieve snapshot information.

    :type SnapshotIds: list
    :param SnapshotIds: A list of identifiers of the snapshots to obtain the information for. If this member is null or empty, all snapshots are returned using the Limit and NextToken members.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The DescribeSnapshotsResult.NextToken value from a previous call to DescribeSnapshots . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The maximum number of objects to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Snapshots': [
        {
            'DirectoryId': 'string',
            'SnapshotId': 'string',
            'Type': 'Auto'|'Manual',
            'Name': 'string',
            'Status': 'Creating'|'Completed'|'Failed',
            'StartTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Contains the results of the  DescribeSnapshots operation.

Snapshots (list) --
The list of  Snapshot objects that were retrieved.
It is possible that this list contains less than the number of items specified in the Limit member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.

(dict) --
Describes a directory snapshot.

DirectoryId (string) --
The directory identifier.

SnapshotId (string) --
The snapshot identifier.

Type (string) --
The snapshot type.

Name (string) --
The descriptive name of the snapshot.

Status (string) --
The snapshot status.

StartTime (datetime) --
The date and time that the snapshot was taken.





NextToken (string) --
If not null, more results are available. Pass this value in the NextToken member of a subsequent call to  DescribeSnapshots .







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'Snapshots': [
            {
                'DirectoryId': 'string',
                'SnapshotId': 'string',
                'Type': 'Auto'|'Manual',
                'Name': 'string',
                'Status': 'Creating'|'Completed'|'Failed',
                'StartTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def describe_trusts(DirectoryId=None, TrustIds=None, NextToken=None, Limit=None):
    """
    Obtains information about the trust relationships for this account.
    If no input parameters are provided, such as DirectoryId or TrustIds, this request describes all the trust relationships belonging to the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_trusts(
        DirectoryId='string',
        TrustIds=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: The Directory ID of the AWS directory that is a part of the requested trust relationship.

    :type TrustIds: list
    :param TrustIds: A list of identifiers of the trust relationships for which to obtain the information. If this member is null, all trust relationships that belong to the current account are returned.\nAn empty list results in an InvalidParameterException being thrown.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The DescribeTrustsResult.NextToken value from a previous call to DescribeTrusts . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The maximum number of objects to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Trusts': [
        {
            'DirectoryId': 'string',
            'TrustId': 'string',
            'RemoteDomainName': 'string',
            'TrustType': 'Forest'|'External',
            'TrustDirection': 'One-Way: Outgoing'|'One-Way: Incoming'|'Two-Way',
            'TrustState': 'Creating'|'Created'|'Verifying'|'VerifyFailed'|'Verified'|'Updating'|'UpdateFailed'|'Updated'|'Deleting'|'Deleted'|'Failed',
            'CreatedDateTime': datetime(2015, 1, 1),
            'LastUpdatedDateTime': datetime(2015, 1, 1),
            'StateLastUpdatedDateTime': datetime(2015, 1, 1),
            'TrustStateReason': 'string',
            'SelectiveAuth': 'Enabled'|'Disabled'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The result of a DescribeTrust request.

Trusts (list) --
The list of Trust objects that were retrieved.
It is possible that this list contains less than the number of items specified in the Limit member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.

(dict) --
Describes a trust relationship between an AWS Managed Microsoft AD directory and an external domain.

DirectoryId (string) --
The Directory ID of the AWS directory involved in the trust relationship.

TrustId (string) --
The unique ID of the trust relationship.

RemoteDomainName (string) --
The Fully Qualified Domain Name (FQDN) of the external domain involved in the trust relationship.

TrustType (string) --
The trust relationship type. Forest is the default.

TrustDirection (string) --
The trust relationship direction.

TrustState (string) --
The trust relationship state.

CreatedDateTime (datetime) --
The date and time that the trust relationship was created.

LastUpdatedDateTime (datetime) --
The date and time that the trust relationship was last updated.

StateLastUpdatedDateTime (datetime) --
The date and time that the TrustState was last updated.

TrustStateReason (string) --
The reason for the TrustState.

SelectiveAuth (string) --
Current state of selective authentication for the trust.





NextToken (string) --
If not null, more results are available. Pass this value for the NextToken parameter in a subsequent call to  DescribeTrusts to retrieve the next set of items.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException
DirectoryService.Client.exceptions.UnsupportedOperationException


    :return: {
        'Trusts': [
            {
                'DirectoryId': 'string',
                'TrustId': 'string',
                'RemoteDomainName': 'string',
                'TrustType': 'Forest'|'External',
                'TrustDirection': 'One-Way: Outgoing'|'One-Way: Incoming'|'Two-Way',
                'TrustState': 'Creating'|'Created'|'Verifying'|'VerifyFailed'|'Verified'|'Updating'|'UpdateFailed'|'Updated'|'Deleting'|'Deleted'|'Failed',
                'CreatedDateTime': datetime(2015, 1, 1),
                'LastUpdatedDateTime': datetime(2015, 1, 1),
                'StateLastUpdatedDateTime': datetime(2015, 1, 1),
                'TrustStateReason': 'string',
                'SelectiveAuth': 'Enabled'|'Disabled'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    
    """
    pass

def disable_ldaps(DirectoryId=None, Type=None):
    """
    Deactivates LDAP secure calls for the specified directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_ldaps(
        DirectoryId='string',
        Type='Client'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory.\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of LDAP security to enable. Currently only the value Client is supported.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.DirectoryDoesNotExistException
DirectoryService.Client.exceptions.InvalidLDAPSStatusException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disable_radius(DirectoryId=None):
    """
    Disables multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector or Microsoft AD directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_radius(
        DirectoryId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory for which to disable MFA.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Contains the results of the  DisableRadius operation.




Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    """
    pass

def disable_sso(DirectoryId=None, UserName=None, Password=None):
    """
    Disables single-sign on for a directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_sso(
        DirectoryId='string',
        UserName='string',
        Password='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory for which to disable single-sign on.\n

    :type UserName: string
    :param UserName: The username of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. This account must have privileges to remove a service principal name.\nIf the AD Connector service account does not have privileges to remove a service principal name, you can specify an alternate account with the UserName and Password parameters. These credentials are only used to disable single sign-on and are not stored by the service. The AD Connector service account is not changed.\n

    :type Password: string
    :param Password: The password of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. For more information, see the UserName parameter.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the results of the  DisableSso operation.





Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InsufficientPermissionsException
DirectoryService.Client.exceptions.AuthenticationFailedException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InsufficientPermissionsException
    DirectoryService.Client.exceptions.AuthenticationFailedException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def enable_ldaps(DirectoryId=None, Type=None):
    """
    Activates the switch for the specific directory to always use LDAP secure calls.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_ldaps(
        DirectoryId='string',
        Type='Client'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory.\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of LDAP security to enable. Currently only the value Client is supported.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.DirectoryDoesNotExistException
DirectoryService.Client.exceptions.NoAvailableCertificateException
DirectoryService.Client.exceptions.InvalidLDAPSStatusException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def enable_radius(DirectoryId=None, RadiusSettings=None):
    """
    Enables multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector or Microsoft AD directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_radius(
        DirectoryId='string',
        RadiusSettings={
            'RadiusServers': [
                'string',
            ],
            'RadiusPort': 123,
            'RadiusTimeout': 123,
            'RadiusRetries': 123,
            'SharedSecret': 'string',
            'AuthenticationProtocol': 'PAP'|'CHAP'|'MS-CHAPv1'|'MS-CHAPv2',
            'DisplayLabel': 'string',
            'UseSameUsername': True|False
        }
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory for which to enable MFA.\n

    :type RadiusSettings: dict
    :param RadiusSettings: [REQUIRED]\nA RadiusSettings object that contains information about the RADIUS server.\n\nRadiusServers (list) --An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.\n\n(string) --\n\n\nRadiusPort (integer) --The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.\n\nRadiusTimeout (integer) --The amount of time, in seconds, to wait for the RADIUS server to respond.\n\nRadiusRetries (integer) --The maximum number of times that communication with the RADIUS server is attempted.\n\nSharedSecret (string) --Required for enabling RADIUS on the directory.\n\nAuthenticationProtocol (string) --The protocol specified for your RADIUS endpoints.\n\nDisplayLabel (string) --Not currently used.\n\nUseSameUsername (boolean) --Not currently used.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the results of the  EnableRadius operation.





Exceptions

DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.EntityAlreadyExistsException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.EntityAlreadyExistsException
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def enable_sso(DirectoryId=None, UserName=None, Password=None):
    """
    Enables single sign-on for a directory. Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_sso(
        DirectoryId='string',
        UserName='string',
        Password='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory for which to enable single-sign on.\n

    :type UserName: string
    :param UserName: The username of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. This account must have privileges to add a service principal name.\nIf the AD Connector service account does not have privileges to add a service principal name, you can specify an alternate account with the UserName and Password parameters. These credentials are only used to enable single sign-on and are not stored by the service. The AD Connector service account is not changed.\n

    :type Password: string
    :param Password: The password of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. For more information, see the UserName parameter.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the results of the  EnableSso operation.





Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InsufficientPermissionsException
DirectoryService.Client.exceptions.AuthenticationFailedException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InsufficientPermissionsException
    DirectoryService.Client.exceptions.AuthenticationFailedException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
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

def get_directory_limits():
    """
    Obtains directory limit information for the current Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_directory_limits()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'DirectoryLimits': {
        'CloudOnlyDirectoriesLimit': 123,
        'CloudOnlyDirectoriesCurrentCount': 123,
        'CloudOnlyDirectoriesLimitReached': True|False,
        'CloudOnlyMicrosoftADLimit': 123,
        'CloudOnlyMicrosoftADCurrentCount': 123,
        'CloudOnlyMicrosoftADLimitReached': True|False,
        'ConnectedDirectoriesLimit': 123,
        'ConnectedDirectoriesCurrentCount': 123,
        'ConnectedDirectoriesLimitReached': True|False
    }
}


Response Structure

(dict) --Contains the results of the  GetDirectoryLimits operation.

DirectoryLimits (dict) --A  DirectoryLimits object that contains the directory limits for the current rRegion.

CloudOnlyDirectoriesLimit (integer) --The maximum number of cloud directories allowed in the Region.

CloudOnlyDirectoriesCurrentCount (integer) --The current number of cloud directories in the Region.

CloudOnlyDirectoriesLimitReached (boolean) --Indicates if the cloud directory limit has been reached.

CloudOnlyMicrosoftADLimit (integer) --The maximum number of AWS Managed Microsoft AD directories allowed in the region.

CloudOnlyMicrosoftADCurrentCount (integer) --The current number of AWS Managed Microsoft AD directories in the region.

CloudOnlyMicrosoftADLimitReached (boolean) --Indicates if the AWS Managed Microsoft AD directory limit has been reached.

ConnectedDirectoriesLimit (integer) --The maximum number of connected directories allowed in the Region.

ConnectedDirectoriesCurrentCount (integer) --The current number of connected directories in the Region.

ConnectedDirectoriesLimitReached (boolean) --Indicates if the connected directory limit has been reached.








Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'DirectoryLimits': {
            'CloudOnlyDirectoriesLimit': 123,
            'CloudOnlyDirectoriesCurrentCount': 123,
            'CloudOnlyDirectoriesLimitReached': True|False,
            'CloudOnlyMicrosoftADLimit': 123,
            'CloudOnlyMicrosoftADCurrentCount': 123,
            'CloudOnlyMicrosoftADLimitReached': True|False,
            'ConnectedDirectoriesLimit': 123,
            'ConnectedDirectoriesCurrentCount': 123,
            'ConnectedDirectoriesLimitReached': True|False
        }
    }
    
    
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

def get_snapshot_limits(DirectoryId=None):
    """
    Obtains the manual snapshot limits for a directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_snapshot_limits(
        DirectoryId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nContains the identifier of the directory to obtain the limits for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SnapshotLimits': {
        'ManualSnapshotsLimit': 123,
        'ManualSnapshotsCurrentCount': 123,
        'ManualSnapshotsLimitReached': True|False
    }
}


Response Structure

(dict) --Contains the results of the  GetSnapshotLimits operation.

SnapshotLimits (dict) --A  SnapshotLimits object that contains the manual snapshot limits for the specified directory.

ManualSnapshotsLimit (integer) --The maximum number of manual snapshots allowed.

ManualSnapshotsCurrentCount (integer) --The current number of manual snapshots of the directory.

ManualSnapshotsLimitReached (boolean) --Indicates if the manual snapshot limit has been reached.








Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SnapshotLimits': {
            'ManualSnapshotsLimit': 123,
            'ManualSnapshotsCurrentCount': 123,
            'ManualSnapshotsLimitReached': True|False
        }
    }
    
    
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

def list_certificates(DirectoryId=None, NextToken=None, Limit=None):
    """
    For the specified directory, lists all the certificates registered for a secured LDAP connection.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_certificates(
        DirectoryId='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory.\n

    :type NextToken: string
    :param NextToken: A token for requesting another page of certificates if the NextToken response element indicates that more certificates are available. Use the value of the returned NextToken element in your request until the token comes back as null . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The number of items that should show up on one page

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'CertificatesInfo': [
        {
            'CertificateId': 'string',
            'CommonName': 'string',
            'State': 'Registering'|'Registered'|'RegisterFailed'|'Deregistering'|'Deregistered'|'DeregisterFailed',
            'ExpiryDateTime': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
Indicates whether another page of certificates is available when the number of available certificates exceeds the page limit.

CertificatesInfo (list) --
A list of certificates with basic details including certificate ID, certificate common name, certificate state.

(dict) --
Contains general information about a certificate.

CertificateId (string) --
The identifier of the certificate.

CommonName (string) --
The common name for the certificate.

State (string) --
The state of the certificate.

ExpiryDateTime (datetime) --
The date and time when the certificate will expire.











Exceptions

DirectoryService.Client.exceptions.DirectoryDoesNotExistException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'NextToken': 'string',
        'CertificatesInfo': [
            {
                'CertificateId': 'string',
                'CommonName': 'string',
                'State': 'Registering'|'Registered'|'RegisterFailed'|'Deregistering'|'Deregistered'|'DeregisterFailed',
                'ExpiryDateTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.DirectoryDoesNotExistException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def list_ip_routes(DirectoryId=None, NextToken=None, Limit=None):
    """
    Lists the address blocks that you have added to a directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_ip_routes(
        DirectoryId='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nIdentifier (ID) of the directory for which you want to retrieve the IP addresses.\n

    :type NextToken: string
    :param NextToken: The ListIpRoutes.NextToken value from a previous call to ListIpRoutes . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: Maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.

    :rtype: dict

ReturnsResponse Syntax
{
    'IpRoutesInfo': [
        {
            'DirectoryId': 'string',
            'CidrIp': 'string',
            'IpRouteStatusMsg': 'Adding'|'Added'|'Removing'|'Removed'|'AddFailed'|'RemoveFailed',
            'AddedDateTime': datetime(2015, 1, 1),
            'IpRouteStatusReason': 'string',
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

IpRoutesInfo (list) --
A list of  IpRoute s.

(dict) --
Information about one or more IP address blocks.

DirectoryId (string) --
Identifier (ID) of the directory associated with the IP addresses.

CidrIp (string) --
IP address block in the  IpRoute .

IpRouteStatusMsg (string) --
The status of the IP address block.

AddedDateTime (datetime) --
The date and time the address block was added to the directory.

IpRouteStatusReason (string) --
The reason for the IpRouteStatusMsg.

Description (string) --
Description of the  IpRouteInfo .





NextToken (string) --
If not null, more results are available. Pass this value for the NextToken parameter in a subsequent call to  ListIpRoutes to retrieve the next set of items.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'IpRoutesInfo': [
            {
                'DirectoryId': 'string',
                'CidrIp': 'string',
                'IpRouteStatusMsg': 'Adding'|'Added'|'Removing'|'Removed'|'AddFailed'|'RemoveFailed',
                'AddedDateTime': datetime(2015, 1, 1),
                'IpRouteStatusReason': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def list_log_subscriptions(DirectoryId=None, NextToken=None, Limit=None):
    """
    Lists the active log subscriptions for the AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_log_subscriptions(
        DirectoryId='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: If a DirectoryID is provided, lists only the log subscription associated with that directory. If no DirectoryId is provided, lists all log subscriptions associated with your AWS account. If there are no log subscriptions for the AWS account or the directory, an empty list will be returned.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return.

    :type Limit: integer
    :param Limit: The maximum number of items returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'LogSubscriptions': [
        {
            'DirectoryId': 'string',
            'LogGroupName': 'string',
            'SubscriptionCreatedDateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LogSubscriptions (list) --
A list of active  LogSubscription objects for calling the AWS account.

(dict) --
Represents a log subscription, which tracks real-time data from a chosen log group to a specified destination.

DirectoryId (string) --
Identifier (ID) of the directory that you want to associate with the log subscription.

LogGroupName (string) --
The name of the log group.

SubscriptionCreatedDateTime (datetime) --
The date and time that the log subscription was created.





NextToken (string) --
The token for the next set of items to return.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'LogSubscriptions': [
            {
                'DirectoryId': 'string',
                'LogGroupName': 'string',
                'SubscriptionCreatedDateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def list_schema_extensions(DirectoryId=None, NextToken=None, Limit=None):
    """
    Lists all schema extensions applied to a Microsoft AD Directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_schema_extensions(
        DirectoryId='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory from which to retrieve the schema extension information.\n

    :type NextToken: string
    :param NextToken: The ListSchemaExtensions.NextToken value from a previous call to ListSchemaExtensions . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'SchemaExtensionsInfo': [
        {
            'DirectoryId': 'string',
            'SchemaExtensionId': 'string',
            'Description': 'string',
            'SchemaExtensionStatus': 'Initializing'|'CreatingSnapshot'|'UpdatingSchema'|'Replicating'|'CancelInProgress'|'RollbackInProgress'|'Cancelled'|'Failed'|'Completed',
            'SchemaExtensionStatusReason': 'string',
            'StartDateTime': datetime(2015, 1, 1),
            'EndDateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SchemaExtensionsInfo (list) --
Information about the schema extensions applied to the directory.

(dict) --
Information about a schema extension.

DirectoryId (string) --
The identifier of the directory to which the schema extension is applied.

SchemaExtensionId (string) --
The identifier of the schema extension.

Description (string) --
A description of the schema extension.

SchemaExtensionStatus (string) --
The current status of the schema extension.

SchemaExtensionStatusReason (string) --
The reason for the SchemaExtensionStatus .

StartDateTime (datetime) --
The date and time that the schema extension started being applied to the directory.

EndDateTime (datetime) --
The date and time that the schema extension was completed.





NextToken (string) --
If not null, more results are available. Pass this value for the NextToken parameter in a subsequent call to ListSchemaExtensions to retrieve the next set of items.







Exceptions

DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SchemaExtensionsInfo': [
            {
                'DirectoryId': 'string',
                'SchemaExtensionId': 'string',
                'Description': 'string',
                'SchemaExtensionStatus': 'Initializing'|'CreatingSnapshot'|'UpdatingSchema'|'Replicating'|'CancelInProgress'|'RollbackInProgress'|'Cancelled'|'Failed'|'Completed',
                'SchemaExtensionStatusReason': 'string',
                'StartDateTime': datetime(2015, 1, 1),
                'EndDateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def list_tags_for_resource(ResourceId=None, NextToken=None, Limit=None):
    """
    Lists all tags on a directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceId='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nIdentifier (ID) of the directory for which you want to retrieve tags.\n

    :type NextToken: string
    :param NextToken: Reserved for future use.

    :type Limit: integer
    :param Limit: Reserved for future use.

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
List of tags returned by the ListTagsForResource operation.

(dict) --
Metadata assigned to a directory consisting of a key-value pair.

Key (string) --
Required name of the tag. The string value can be Unicode characters and cannot be prefixed with "aws:". The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

Value (string) --
The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, \'_\', \'.\', \'/\', \'=\', \'+\', \'-\' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").





NextToken (string) --
Reserved for future use.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidNextTokenException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


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
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidNextTokenException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def register_certificate(DirectoryId=None, CertificateData=None):
    """
    Registers a certificate for secured LDAP connection.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_certificate(
        DirectoryId='string',
        CertificateData='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory.\n

    :type CertificateData: string
    :param CertificateData: [REQUIRED]\nThe certificate PEM string that needs to be registered.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CertificateId': 'string'
}


Response Structure

(dict) --

CertificateId (string) --
The identifier of the certificate.







Exceptions

DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.DirectoryDoesNotExistException
DirectoryService.Client.exceptions.InvalidCertificateException
DirectoryService.Client.exceptions.CertificateLimitExceededException
DirectoryService.Client.exceptions.CertificateAlreadyExistsException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'CertificateId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.DirectoryUnavailableException
    DirectoryService.Client.exceptions.DirectoryDoesNotExistException
    DirectoryService.Client.exceptions.InvalidCertificateException
    DirectoryService.Client.exceptions.CertificateLimitExceededException
    DirectoryService.Client.exceptions.CertificateAlreadyExistsException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def register_event_topic(DirectoryId=None, TopicName=None):
    """
    Associates a directory with an SNS topic. This establishes the directory as a publisher to the specified SNS topic. You can then receive email or text (SMS) messages when the status of your directory changes. You get notified if your directory goes from an Active status to an Impaired or Inoperable status. You also receive a notification when the directory returns to an Active status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_event_topic(
        DirectoryId='string',
        TopicName='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe Directory ID that will publish status messages to the SNS topic.\n

    :type TopicName: string
    :param TopicName: [REQUIRED]\nThe SNS topic name to which the directory will publish status messages. This SNS topic must be in the same region as the specified Directory ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The result of a RegisterEventTopic request.





Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def reject_shared_directory(SharedDirectoryId=None):
    """
    Rejects a directory sharing request that was sent from the directory owner account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reject_shared_directory(
        SharedDirectoryId='string'
    )
    
    
    :type SharedDirectoryId: string
    :param SharedDirectoryId: [REQUIRED]\nIdentifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SharedDirectoryId': 'string'
}


Response Structure

(dict) --
SharedDirectoryId (string) --Identifier of the shared directory in the directory consumer account.






Exceptions

DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.DirectoryAlreadySharedException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SharedDirectoryId': 'string'
    }
    
    
    """
    pass

def remove_ip_routes(DirectoryId=None, CidrIps=None):
    """
    Removes IP address blocks from a directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_ip_routes(
        DirectoryId='string',
        CidrIps=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nIdentifier (ID) of the directory from which you want to remove the IP addresses.\n

    :type CidrIps: list
    :param CidrIps: [REQUIRED]\nIP address blocks that you want to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_tags_from_resource(ResourceId=None, TagKeys=None):
    """
    Removes tags from a directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_tags_from_resource(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nIdentifier (ID) of the directory from which to remove the tag.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag key (name) of the tag to be removed.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reset_user_password(DirectoryId=None, UserName=None, NewPassword=None):
    """
    Resets the password for any user in your AWS Managed Microsoft AD or Simple AD directory.
    You can reset the password for any user in your directory with the following exceptions:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reset_user_password(
        DirectoryId='string',
        UserName='string',
        NewPassword='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nIdentifier of the AWS Managed Microsoft AD or Simple AD directory in which the user resides.\n

    :type UserName: string
    :param UserName: [REQUIRED]\nThe user name of the user whose password will be reset.\n

    :type NewPassword: string
    :param NewPassword: [REQUIRED]\nThe new password that will be reset.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.UserDoesNotExistException
DirectoryService.Client.exceptions.InvalidPasswordException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryId (string) -- [REQUIRED]
    Identifier of the AWS Managed Microsoft AD or Simple AD directory in which the user resides.
    
    UserName (string) -- [REQUIRED]
    The user name of the user whose password will be reset.
    
    NewPassword (string) -- [REQUIRED]
    The new password that will be reset.
    
    
    """
    pass

def restore_from_snapshot(SnapshotId=None):
    """
    Restores a directory using an existing directory snapshot.
    When you restore a directory from a snapshot, any changes made to the directory after the snapshot date are overwritten.
    This action returns as soon as the restore operation is initiated. You can monitor the progress of the restore operation by calling the  DescribeDirectories operation with the directory identifier. When the DirectoryDescription.Stage value changes to Active , the restore operation is complete.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_from_snapshot(
        SnapshotId='string'
    )
    
    
    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]\nThe identifier of the snapshot to restore from.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Contains the results of the  RestoreFromSnapshot operation.




Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    """
    pass

def share_directory(DirectoryId=None, ShareNotes=None, ShareTarget=None, ShareMethod=None):
    """
    Shares a specified directory (DirectoryId ) in your AWS account (directory owner) with another AWS account (directory consumer). With this operation you can use your directory from any AWS account and from any Amazon VPC within an AWS Region.
    When you share your AWS Managed Microsoft AD directory, AWS Directory Service creates a shared directory in the directory consumer account. This shared directory contains the metadata to provide access to the directory within the directory owner account. The shared directory is visible in all VPCs in the directory consumer account.
    The ShareMethod parameter determines whether the specified directory can be shared between AWS accounts inside the same AWS organization (ORGANIZATIONS ). It also determines whether you can share the directory with any other AWS account either inside or outside of the organization (HANDSHAKE ).
    The ShareNotes parameter is only used when HANDSHAKE is called, which sends a directory sharing request to the directory consumer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.share_directory(
        DirectoryId='string',
        ShareNotes='string',
        ShareTarget={
            'Id': 'string',
            'Type': 'ACCOUNT'
        },
        ShareMethod='ORGANIZATIONS'|'HANDSHAKE'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nIdentifier of the AWS Managed Microsoft AD directory that you want to share with other AWS accounts.\n

    :type ShareNotes: string
    :param ShareNotes: A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.

    :type ShareTarget: dict
    :param ShareTarget: [REQUIRED]\nIdentifier for the directory consumer account with whom the directory is to be shared.\n\nId (string) -- [REQUIRED]Identifier of the directory consumer account.\n\nType (string) -- [REQUIRED]Type of identifier to be used in the Id field.\n\n\n

    :type ShareMethod: string
    :param ShareMethod: [REQUIRED]\nThe method used when sharing a directory to determine whether the directory should be shared within your AWS organization (ORGANIZATIONS ) or with any AWS account by sending a directory sharing request (HANDSHAKE ).\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SharedDirectoryId': 'string'
}


Response Structure

(dict) --

SharedDirectoryId (string) --
Identifier of the directory that is stored in the directory consumer account that is shared from the specified directory (DirectoryId ).







Exceptions

DirectoryService.Client.exceptions.DirectoryAlreadySharedException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidTargetException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ShareLimitExceededException
DirectoryService.Client.exceptions.OrganizationsException
DirectoryService.Client.exceptions.AccessDeniedException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SharedDirectoryId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.DirectoryAlreadySharedException
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidTargetException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ShareLimitExceededException
    DirectoryService.Client.exceptions.OrganizationsException
    DirectoryService.Client.exceptions.AccessDeniedException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def start_schema_extension(DirectoryId=None, CreateSnapshotBeforeSchemaExtension=None, LdifContent=None, Description=None):
    """
    Applies a schema extension to a Microsoft AD directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_schema_extension(
        DirectoryId='string',
        CreateSnapshotBeforeSchemaExtension=True|False,
        LdifContent='string',
        Description='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory for which the schema extension will be applied to.\n

    :type CreateSnapshotBeforeSchemaExtension: boolean
    :param CreateSnapshotBeforeSchemaExtension: [REQUIRED]\nIf true, creates a snapshot of the directory before applying the schema extension.\n

    :type LdifContent: string
    :param LdifContent: [REQUIRED]\nThe LDIF file represented as a string. To construct the LdifContent string, precede each line as it would be formatted in an ldif file with n. See the example request below for more details. The file size can be no larger than 1MB.\n

    :type Description: string
    :param Description: [REQUIRED]\nA description of the schema extension.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SchemaExtensionId': 'string'
}


Response Structure

(dict) --

SchemaExtensionId (string) --
The identifier of the schema extension that will be applied.







Exceptions

DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.SnapshotLimitExceededException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SchemaExtensionId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.DirectoryUnavailableException
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.SnapshotLimitExceededException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def unshare_directory(DirectoryId=None, UnshareTarget=None):
    """
    Stops the directory sharing between the directory owner and consumer accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unshare_directory(
        DirectoryId='string',
        UnshareTarget={
            'Id': 'string',
            'Type': 'ACCOUNT'
        }
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the AWS Managed Microsoft AD directory that you want to stop sharing.\n

    :type UnshareTarget: dict
    :param UnshareTarget: [REQUIRED]\nIdentifier for the directory consumer account with whom the directory has to be unshared.\n\nId (string) -- [REQUIRED]Identifier of the directory consumer account.\n\nType (string) -- [REQUIRED]Type of identifier to be used in the Id field.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SharedDirectoryId': 'string'
}


Response Structure

(dict) --

SharedDirectoryId (string) --
Identifier of the directory stored in the directory consumer account that is to be unshared from the specified directory (DirectoryId ).







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidTargetException
DirectoryService.Client.exceptions.DirectoryNotSharedException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'SharedDirectoryId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidTargetException
    DirectoryService.Client.exceptions.DirectoryNotSharedException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def update_conditional_forwarder(DirectoryId=None, RemoteDomainName=None, DnsIpAddrs=None):
    """
    Updates a conditional forwarder that has been set up for your AWS directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_conditional_forwarder(
        DirectoryId='string',
        RemoteDomainName='string',
        DnsIpAddrs=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe directory ID of the AWS directory for which to update the conditional forwarder.\n

    :type RemoteDomainName: string
    :param RemoteDomainName: [REQUIRED]\nThe fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.\n

    :type DnsIpAddrs: list
    :param DnsIpAddrs: [REQUIRED]\nThe updated IP addresses of the remote DNS server associated with the conditional forwarder.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The result of an UpdateConditionalForwarder request.





Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.DirectoryUnavailableException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.UnsupportedOperationException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def update_number_of_domain_controllers(DirectoryId=None, DesiredNumber=None):
    """
    Adds or removes domain controllers to or from the directory. Based on the difference between current value and new value (provided through this API call), domain controllers will be added or removed. It may take up to 45 minutes for any new domain controllers to become fully active once the requested number of domain controllers is updated. During this time, you cannot make another update request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_number_of_domain_controllers(
        DirectoryId='string',
        DesiredNumber=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nIdentifier of the directory to which the domain controllers will be added or removed.\n

    :type DesiredNumber: integer
    :param DesiredNumber: [REQUIRED]\nThe number of domain controllers desired in the directory.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.DirectoryUnavailableException
DirectoryService.Client.exceptions.DomainControllerLimitExceededException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.UnsupportedOperationException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_radius(DirectoryId=None, RadiusSettings=None):
    """
    Updates the Remote Authentication Dial In User Service (RADIUS) server information for an AD Connector or Microsoft AD directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_radius(
        DirectoryId='string',
        RadiusSettings={
            'RadiusServers': [
                'string',
            ],
            'RadiusPort': 123,
            'RadiusTimeout': 123,
            'RadiusRetries': 123,
            'SharedSecret': 'string',
            'AuthenticationProtocol': 'PAP'|'CHAP'|'MS-CHAPv1'|'MS-CHAPv2',
            'DisplayLabel': 'string',
            'UseSameUsername': True|False
        }
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]\nThe identifier of the directory for which to update the RADIUS server information.\n

    :type RadiusSettings: dict
    :param RadiusSettings: [REQUIRED]\nA RadiusSettings object that contains information about the RADIUS server.\n\nRadiusServers (list) --An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.\n\n(string) --\n\n\nRadiusPort (integer) --The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.\n\nRadiusTimeout (integer) --The amount of time, in seconds, to wait for the RADIUS server to respond.\n\nRadiusRetries (integer) --The maximum number of times that communication with the RADIUS server is attempted.\n\nSharedSecret (string) --Required for enabling RADIUS on the directory.\n\nAuthenticationProtocol (string) --The protocol specified for your RADIUS endpoints.\n\nDisplayLabel (string) --Not currently used.\n\nUseSameUsername (boolean) --Not currently used.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Contains the results of the  UpdateRadius operation.





Exceptions

DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {}
    
    
    :returns: 
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def update_trust(TrustId=None, SelectiveAuth=None):
    """
    Updates the trust that has been set up between your AWS Managed Microsoft AD directory and an on-premises Active Directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_trust(
        TrustId='string',
        SelectiveAuth='Enabled'|'Disabled'
    )
    
    
    :type TrustId: string
    :param TrustId: [REQUIRED]\nIdentifier of the trust relationship.\n

    :type SelectiveAuth: string
    :param SelectiveAuth: Updates selective authentication for the trust.

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestId': 'string',
    'TrustId': 'string'
}


Response Structure

(dict) --

RequestId (string) --
The AWS request identifier.

TrustId (string) --
Identifier of the trust relationship.







Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException


    :return: {
        'RequestId': 'string',
        'TrustId': 'string'
    }
    
    
    :returns: 
    DirectoryService.Client.exceptions.EntityDoesNotExistException
    DirectoryService.Client.exceptions.InvalidParameterException
    DirectoryService.Client.exceptions.ClientException
    DirectoryService.Client.exceptions.ServiceException
    
    """
    pass

def verify_trust(TrustId=None):
    """
    AWS Directory Service for Microsoft Active Directory allows you to configure and verify trust relationships.
    This action verifies a trust relationship between your AWS Managed Microsoft AD directory and an external domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.verify_trust(
        TrustId='string'
    )
    
    
    :type TrustId: string
    :param TrustId: [REQUIRED]\nThe unique Trust ID of the trust relationship to verify.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TrustId': 'string'
}


Response Structure

(dict) --Result of a VerifyTrust request.

TrustId (string) --The unique Trust ID of the trust relationship that was verified.






Exceptions

DirectoryService.Client.exceptions.EntityDoesNotExistException
DirectoryService.Client.exceptions.InvalidParameterException
DirectoryService.Client.exceptions.ClientException
DirectoryService.Client.exceptions.ServiceException
DirectoryService.Client.exceptions.UnsupportedOperationException


    :return: {
        'TrustId': 'string'
    }
    
    
    """
    pass

