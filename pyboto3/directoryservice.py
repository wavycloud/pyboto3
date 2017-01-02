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

def add_ip_routes(DirectoryId=None, IpRoutes=None, UpdateSecurityGroupForDirectoryControllers=None):
    """
    If the DNS server for your on-premises domain uses a publicly addressable IP address, you must add a CIDR address block to correctly route traffic to and from your Microsoft AD on Amazon Web Services. AddIpRoutes adds this address block. You can also use AddIpRoutes to facilitate routing traffic that uses public IP ranges from your Microsoft AD on AWS to a peer VPC.
    Before you call AddIpRoutes , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the AddIpRoutes operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    
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
    :param DirectoryId: [REQUIRED]
            Identifier (ID) of the directory to which to add the address block.
            

    :type IpRoutes: list
    :param IpRoutes: [REQUIRED]
            IP address blocks, using CIDR format, of the traffic to route. This is often the IP address block of the DNS server used for your on-premises domain.
            (dict) --IP address block. This is often the address block of the DNS server used for your on-premises domain.
            CidrIp (string) --IP address block using CIDR format, for example 10.0.0.0/24. This is often the address block of the DNS server used for your on-premises domain. For a single IP address use a CIDR address block with /32. For example 10.0.0.0/32.
            Description (string) --Description of the address block.
            
            

    :type UpdateSecurityGroupForDirectoryControllers: boolean
    :param UpdateSecurityGroupForDirectoryControllers: If set to true, updates the inbound and outbound rules of the security group that has the description: 'AWS created security group for directory ID directory controllers.' Following are the new rules:
            Inbound:
            Type: Custom UDP Rule, Protocol: UDP, Range: 88, Source: 0.0.0.0/0
            Type: Custom UDP Rule, Protocol: UDP, Range: 123, Source: 0.0.0.0/0
            Type: Custom UDP Rule, Protocol: UDP, Range: 138, Source: 0.0.0.0/0
            Type: Custom UDP Rule, Protocol: UDP, Range: 389, Source: 0.0.0.0/0
            Type: Custom UDP Rule, Protocol: UDP, Range: 464, Source: 0.0.0.0/0
            Type: Custom UDP Rule, Protocol: UDP, Range: 445, Source: 0.0.0.0/0
            Type: Custom TCP Rule, Protocol: TCP, Range: 88, Source: 0.0.0.0/0
            Type: Custom TCP Rule, Protocol: TCP, Range: 135, Source: 0.0.0.0/0
            Type: Custom TCP Rule, Protocol: TCP, Range: 445, Source: 0.0.0.0/0
            Type: Custom TCP Rule, Protocol: TCP, Range: 464, Source: 0.0.0.0/0
            Type: Custom TCP Rule, Protocol: TCP, Range: 636, Source: 0.0.0.0/0
            Type: Custom TCP Rule, Protocol: TCP, Range: 1024-65535, Source: 0.0.0.0/0
            Type: Custom TCP Rule, Protocol: TCP, Range: 3268-33269, Source: 0.0.0.0/0
            Type: DNS (UDP), Protocol: UDP, Range: 53, Source: 0.0.0.0/0
            Type: DNS (TCP), Protocol: TCP, Range: 53, Source: 0.0.0.0/0
            Type: LDAP, Protocol: TCP, Range: 389, Source: 0.0.0.0/0
            Type: All ICMP, Protocol: All, Range: N/A, Source: 0.0.0.0/0
            Outbound:
            Type: All traffic, Protocol: All, Range: All, Destination: 0.0.0.0/0
            These security rules impact an internal network interface that is not exposed publicly.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def add_tags_to_resource(ResourceId=None, Tags=None):
    """
    Adds or overwrites one or more tags for the specified directory. Each directory can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique to each resource.
    See also: AWS API Documentation
    
    
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
    :param ResourceId: [REQUIRED]
            Identifier (ID) for the directory to which to add the tag.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags to be assigned to the directory.
            (dict) --Metadata assigned to a directory consisting of a key-value pair.
            Key (string) -- [REQUIRED]Required name of the tag. The string value can be Unicode characters and cannot be prefixed with 'aws:'. The string can contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) -- [REQUIRED]The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            

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

def cancel_schema_extension(DirectoryId=None, SchemaExtensionId=None):
    """
    Cancels an in-progress schema extension to a Microsoft AD directory. Once a schema extension has started replicating to all domain controllers, the task can no longer be canceled. A schema extension can be canceled during any of the following states; Initializing , CreatingSnapshot , and UpdatingSchema .
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_schema_extension(
        DirectoryId='string',
        SchemaExtensionId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory whose schema extension will be canceled.
            

    :type SchemaExtensionId: string
    :param SchemaExtensionId: [REQUIRED]
            The identifier of the schema extension that will be canceled.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def connect_directory(Name=None, ShortName=None, Password=None, Description=None, Size=None, ConnectSettings=None):
    """
    Creates an AD Connector to connect to an on-premises directory.
    Before you call ConnectDirectory , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the ConnectDirectory operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    
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
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The fully-qualified name of the on-premises directory, such as corp.example.com .
            

    :type ShortName: string
    :param ShortName: The NetBIOS name of the on-premises directory, such as CORP .

    :type Password: string
    :param Password: [REQUIRED]
            The password for the on-premises user account.
            

    :type Description: string
    :param Description: A textual description for the directory.

    :type Size: string
    :param Size: [REQUIRED]
            The size of the directory.
            

    :type ConnectSettings: dict
    :param ConnectSettings: [REQUIRED]
            A DirectoryConnectSettings object that contains additional information for the operation.
            VpcId (string) -- [REQUIRED]The identifier of the VPC in which the AD Connector is created.
            SubnetIds (list) -- [REQUIRED]A list of subnet identifiers in the VPC in which the AD Connector is created.
            (string) --
            CustomerDnsIps (list) -- [REQUIRED]A list of one or more IP addresses of DNS servers or domain controllers in the on-premises directory.
            (string) --
            CustomerUserName (string) -- [REQUIRED]The username of an account in the on-premises directory that is used to connect to the directory. This account must have the following privileges:
            Read users and groups
            Create computer objects
            Join computers to the domain
            

    :rtype: dict
    :return: {
        'DirectoryId': 'string'
    }
    
    
    """
    pass

def create_alias(DirectoryId=None, Alias=None):
    """
    Creates an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as http://alias.awsapps.com .
    See also: AWS API Documentation
    
    
    :example: response = client.create_alias(
        DirectoryId='string',
        Alias='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to create the alias.
            

    :type Alias: string
    :param Alias: [REQUIRED]
            The requested alias.
            The alias must be unique amongst all aliases in AWS. This operation throws an EntityAlreadyExistsException error if the alias already exists.
            

    :rtype: dict
    :return: {
        'DirectoryId': 'string',
        'Alias': 'string'
    }
    
    
    """
    pass

def create_computer(DirectoryId=None, ComputerName=None, Password=None, OrganizationalUnitDistinguishedName=None, ComputerAttributes=None):
    """
    Creates a computer account in the specified directory, and joins the computer to the directory.
    See also: AWS API Documentation
    
    
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
    :param DirectoryId: [REQUIRED]
            The identifier of the directory in which to create the computer account.
            

    :type ComputerName: string
    :param ComputerName: [REQUIRED]
            The name of the computer account.
            

    :type Password: string
    :param Password: [REQUIRED]
            A one-time password that is used to join the computer to the directory. You should generate a random, strong password to use for this parameter.
            

    :type OrganizationalUnitDistinguishedName: string
    :param OrganizationalUnitDistinguishedName: The fully-qualified distinguished name of the organizational unit to place the computer account in.

    :type ComputerAttributes: list
    :param ComputerAttributes: An array of Attribute objects that contain any LDAP attributes to apply to the computer account.
            (dict) --Represents a named directory attribute.
            Name (string) --The name of the attribute.
            Value (string) --The value of the attribute.
            
            

    :rtype: dict
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
    
    
    """
    pass

def create_conditional_forwarder(DirectoryId=None, RemoteDomainName=None, DnsIpAddrs=None):
    """
    Creates a conditional forwarder associated with your AWS directory. Conditional forwarders are required in order to set up a trust relationship with another domain. The conditional forwarder points to the trusted domain.
    See also: AWS API Documentation
    
    
    :example: response = client.create_conditional_forwarder(
        DirectoryId='string',
        RemoteDomainName='string',
        DnsIpAddrs=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The directory ID of the AWS directory for which you are creating the conditional forwarder.
            

    :type RemoteDomainName: string
    :param RemoteDomainName: [REQUIRED]
            The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.
            

    :type DnsIpAddrs: list
    :param DnsIpAddrs: [REQUIRED]
            The IP addresses of the remote DNS server associated with RemoteDomainName.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_directory(Name=None, ShortName=None, Password=None, Description=None, Size=None, VpcSettings=None):
    """
    Creates a Simple AD directory.
    Before you call CreateDirectory , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the CreateDirectory operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    
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
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The fully qualified name for the directory, such as corp.example.com .
            

    :type ShortName: string
    :param ShortName: The short name of the directory, such as CORP .

    :type Password: string
    :param Password: [REQUIRED]
            The password for the directory administrator. The directory creation process creates a directory administrator account with the username Administrator and this password.
            

    :type Description: string
    :param Description: A textual description for the directory.

    :type Size: string
    :param Size: [REQUIRED]
            The size of the directory.
            

    :type VpcSettings: dict
    :param VpcSettings: A DirectoryVpcSettings object that contains additional information for the operation.
            VpcId (string) -- [REQUIRED]The identifier of the VPC in which to create the directory.
            SubnetIds (list) -- [REQUIRED]The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service creates a directory server and a DNS server in each of these subnets.
            (string) --
            

    :rtype: dict
    :return: {
        'DirectoryId': 'string'
    }
    
    
    """
    pass

def create_microsoft_ad(Name=None, ShortName=None, Password=None, Description=None, VpcSettings=None):
    """
    Creates a Microsoft AD in the AWS cloud.
    Before you call CreateMicrosoftAD , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the CreateMicrosoftAD operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    
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
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The fully qualified domain name for the directory, such as corp.example.com . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
            

    :type ShortName: string
    :param ShortName: The NetBIOS name for your domain. A short identifier for your domain, such as CORP . If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, CORP for the directory DNS corp.example.com .

    :type Password: string
    :param Password: [REQUIRED]
            The password for the default administrative user named Admin .
            

    :type Description: string
    :param Description: A textual description for the directory. This label will appear on the AWS console Directory Details page after the directory is created.

    :type VpcSettings: dict
    :param VpcSettings: [REQUIRED]
            Contains VPC information for the CreateDirectory or CreateMicrosoftAD operation.
            VpcId (string) -- [REQUIRED]The identifier of the VPC in which to create the directory.
            SubnetIds (list) -- [REQUIRED]The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service creates a directory server and a DNS server in each of these subnets.
            (string) --
            

    :rtype: dict
    :return: {
        'DirectoryId': 'string'
    }
    
    
    """
    pass

def create_snapshot(DirectoryId=None, Name=None):
    """
    Creates a snapshot of a Simple AD or Microsoft AD directory in the AWS cloud.
    See also: AWS API Documentation
    
    
    :example: response = client.create_snapshot(
        DirectoryId='string',
        Name='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory of which to take a snapshot.
            

    :type Name: string
    :param Name: The descriptive name to apply to the snapshot.

    :rtype: dict
    :return: {
        'SnapshotId': 'string'
    }
    
    
    """
    pass

def create_trust(DirectoryId=None, RemoteDomainName=None, TrustPassword=None, TrustDirection=None, TrustType=None, ConditionalForwarderIpAddrs=None):
    """
    AWS Directory Service for Microsoft Active Directory allows you to configure trust relationships. For example, you can establish a trust between your Microsoft AD in the AWS cloud, and your existing on-premises Microsoft Active Directory. This would allow you to provide users and groups access to resources in either domain, with a single set of credentials.
    This action initiates the creation of the AWS side of a trust relationship between a Microsoft AD in the AWS cloud and an external domain.
    See also: AWS API Documentation
    
    
    :example: response = client.create_trust(
        DirectoryId='string',
        RemoteDomainName='string',
        TrustPassword='string',
        TrustDirection='One-Way: Outgoing'|'One-Way: Incoming'|'Two-Way',
        TrustType='Forest',
        ConditionalForwarderIpAddrs=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The Directory ID of the Microsoft AD in the AWS cloud for which to establish the trust relationship.
            

    :type RemoteDomainName: string
    :param RemoteDomainName: [REQUIRED]
            The Fully Qualified Domain Name (FQDN) of the external domain for which to create the trust relationship.
            

    :type TrustPassword: string
    :param TrustPassword: [REQUIRED]
            The trust password. The must be the same password that was used when creating the trust relationship on the external domain.
            

    :type TrustDirection: string
    :param TrustDirection: [REQUIRED]
            The direction of the trust relationship.
            

    :type TrustType: string
    :param TrustType: The trust relationship type.

    :type ConditionalForwarderIpAddrs: list
    :param ConditionalForwarderIpAddrs: The IP addresses of the remote DNS server associated with RemoteDomainName.
            (string) --
            

    :rtype: dict
    :return: {
        'TrustId': 'string'
    }
    
    
    """
    pass

def delete_conditional_forwarder(DirectoryId=None, RemoteDomainName=None):
    """
    Deletes a conditional forwarder that has been set up for your AWS directory.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_conditional_forwarder(
        DirectoryId='string',
        RemoteDomainName='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The directory ID for which you are deleting the conditional forwarder.
            

    :type RemoteDomainName: string
    :param RemoteDomainName: [REQUIRED]
            The fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_directory(DirectoryId=None):
    """
    Deletes an AWS Directory Service directory.
    Before you call DeleteDirectory , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the DeleteDirectory operation, see AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_directory(
        DirectoryId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory to delete.
            

    :rtype: dict
    :return: {
        'DirectoryId': 'string'
    }
    
    
    """
    pass

def delete_snapshot(SnapshotId=None):
    """
    Deletes a directory snapshot.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_snapshot(
        SnapshotId='string'
    )
    
    
    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]
            The identifier of the directory snapshot to be deleted.
            

    :rtype: dict
    :return: {
        'SnapshotId': 'string'
    }
    
    
    """
    pass

def delete_trust(TrustId=None, DeleteAssociatedConditionalForwarder=None):
    """
    Deletes an existing trust relationship between your Microsoft AD in the AWS cloud and an external domain.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_trust(
        TrustId='string',
        DeleteAssociatedConditionalForwarder=True|False
    )
    
    
    :type TrustId: string
    :param TrustId: [REQUIRED]
            The Trust ID of the trust relationship to be deleted.
            

    :type DeleteAssociatedConditionalForwarder: boolean
    :param DeleteAssociatedConditionalForwarder: Delete a conditional forwarder as part of a DeleteTrustRequest.

    :rtype: dict
    :return: {
        'TrustId': 'string'
    }
    
    
    """
    pass

def deregister_event_topic(DirectoryId=None, TopicName=None):
    """
    Removes the specified directory as a publisher to the specified SNS topic.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_event_topic(
        DirectoryId='string',
        TopicName='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The Directory ID to remove as a publisher. This directory will no longer send messages to the specified SNS topic.
            

    :type TopicName: string
    :param TopicName: [REQUIRED]
            The name of the SNS topic from which to remove the directory as a publisher.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_conditional_forwarders(DirectoryId=None, RemoteDomainNames=None):
    """
    Obtains information about the conditional forwarders for this account.
    If no input parameters are provided for RemoteDomainNames, this request describes all conditional forwarders for the specified directory ID.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_conditional_forwarders(
        DirectoryId='string',
        RemoteDomainNames=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The directory ID for which to get the list of associated conditional forwarders.
            

    :type RemoteDomainNames: list
    :param RemoteDomainNames: The fully qualified domain names (FQDN) of the remote domains for which to get the list of associated conditional forwarders. If this member is null, all conditional forwarders are returned.
            (string) --
            

    :rtype: dict
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
    
    
    :example: response = client.describe_directories(
        DirectoryIds=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryIds: list
    :param DirectoryIds: A list of identifiers of the directories for which to obtain the information. If this member is null, all directories that belong to the current account are returned.
            An empty list results in an InvalidParameterException being thrown.
            (string) --
            

    :type NextToken: string
    :param NextToken: The DescribeDirectoriesResult.NextToken value from a previous call to DescribeDirectories . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.

    :rtype: dict
    :return: {
        'DirectoryDescriptions': [
            {
                'DirectoryId': 'string',
                'Name': 'string',
                'ShortName': 'string',
                'Size': 'Small'|'Large',
                'Alias': 'string',
                'AccessUrl': 'string',
                'Description': 'string',
                'DnsIpAddrs': [
                    'string',
                ],
                'Stage': 'Requested'|'Creating'|'Created'|'Active'|'Inoperable'|'Impaired'|'Restoring'|'RestoreFailed'|'Deleting'|'Deleted'|'Failed',
                'LaunchTime': datetime(2015, 1, 1),
                'StageLastUpdatedDateTime': datetime(2015, 1, 1),
                'Type': 'SimpleAD'|'ADConnector'|'MicrosoftAD',
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
                'SsoEnabled': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_event_topics(DirectoryId=None, TopicNames=None):
    """
    Obtains information about which SNS topics receive status messages from the specified directory.
    If no input parameters are provided, such as DirectoryId or TopicName, this request describes all of the associations in the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_topics(
        DirectoryId='string',
        TopicNames=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: The Directory ID for which to get the list of associated SNS topics. If this member is null, associations for all Directory IDs are returned.

    :type TopicNames: list
    :param TopicNames: A list of SNS topic names for which to obtain the information. If this member is null, all associations for the specified Directory ID are returned.
            An empty list results in an InvalidParameterException being thrown.
            (string) --
            

    :rtype: dict
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
    
    
    """
    pass

def describe_snapshots(DirectoryId=None, SnapshotIds=None, NextToken=None, Limit=None):
    """
    Obtains information about the directory snapshots that belong to this account.
    This operation supports pagination with the use of the NextToken request and response parameters. If more results are available, the DescribeSnapshots.NextToken member contains a token that you pass in the next call to  DescribeSnapshots to retrieve the next set of items.
    You can also specify a maximum number of return results with the Limit parameter.
    See also: AWS API Documentation
    
    
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
    :param SnapshotIds: A list of identifiers of the snapshots to obtain the information for. If this member is null or empty, all snapshots are returned using the Limit and NextToken members.
            (string) --
            

    :type NextToken: string
    :param NextToken: The DescribeSnapshotsResult.NextToken value from a previous call to DescribeSnapshots . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The maximum number of objects to return.

    :rtype: dict
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
    
    
    """
    pass

def describe_trusts(DirectoryId=None, TrustIds=None, NextToken=None, Limit=None):
    """
    Obtains information about the trust relationships for this account.
    If no input parameters are provided, such as DirectoryId or TrustIds, this request describes all the trust relationships belonging to the account.
    See also: AWS API Documentation
    
    
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
    :param TrustIds: A list of identifiers of the trust relationships for which to obtain the information. If this member is null, all trust relationships that belong to the current account are returned.
            An empty list results in an InvalidParameterException being thrown.
            (string) --
            

    :type NextToken: string
    :param NextToken: The DescribeTrustsResult.NextToken value from a previous call to DescribeTrusts . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The maximum number of objects to return.

    :rtype: dict
    :return: {
        'Trusts': [
            {
                'DirectoryId': 'string',
                'TrustId': 'string',
                'RemoteDomainName': 'string',
                'TrustType': 'Forest',
                'TrustDirection': 'One-Way: Outgoing'|'One-Way: Incoming'|'Two-Way',
                'TrustState': 'Creating'|'Created'|'Verifying'|'VerifyFailed'|'Verified'|'Deleting'|'Deleted'|'Failed',
                'CreatedDateTime': datetime(2015, 1, 1),
                'LastUpdatedDateTime': datetime(2015, 1, 1),
                'StateLastUpdatedDateTime': datetime(2015, 1, 1),
                'TrustStateReason': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def disable_radius(DirectoryId=None):
    """
    Disables multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector directory.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_radius(
        DirectoryId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to disable MFA.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def disable_sso(DirectoryId=None, UserName=None, Password=None):
    """
    Disables single-sign on for a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_sso(
        DirectoryId='string',
        UserName='string',
        Password='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to disable single-sign on.
            

    :type UserName: string
    :param UserName: The username of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. This account must have privileges to remove a service principal name.
            If the AD Connector service account does not have privileges to remove a service principal name, you can specify an alternate account with the UserName and Password parameters. These credentials are only used to disable single sign-on and are not stored by the service. The AD Connector service account is not changed.
            

    :type Password: string
    :param Password: The password of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. For more information, see the UserName parameter.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def enable_radius(DirectoryId=None, RadiusSettings=None):
    """
    Enables multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector directory.
    See also: AWS API Documentation
    
    
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
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to enable MFA.
            

    :type RadiusSettings: dict
    :param RadiusSettings: [REQUIRED]
            A RadiusSettings object that contains information about the RADIUS server.
            RadiusServers (list) --An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.
            (string) --
            RadiusPort (integer) --The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.
            RadiusTimeout (integer) --The amount of time, in seconds, to wait for the RADIUS server to respond.
            RadiusRetries (integer) --The maximum number of times that communication with the RADIUS server is attempted.
            SharedSecret (string) --Not currently used.
            AuthenticationProtocol (string) --The protocol specified for your RADIUS endpoints.
            DisplayLabel (string) --Not currently used.
            UseSameUsername (boolean) --Not currently used.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def enable_sso(DirectoryId=None, UserName=None, Password=None):
    """
    Enables single sign-on for a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_sso(
        DirectoryId='string',
        UserName='string',
        Password='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to enable single-sign on.
            

    :type UserName: string
    :param UserName: The username of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. This account must have privileges to add a service principal name.
            If the AD Connector service account does not have privileges to add a service principal name, you can specify an alternate account with the UserName and Password parameters. These credentials are only used to enable single sign-on and are not stored by the service. The AD Connector service account is not changed.
            

    :type Password: string
    :param Password: The password of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. For more information, see the UserName parameter.

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

def get_directory_limits():
    """
    Obtains directory limit information for the current region.
    See also: AWS API Documentation
    
    
    :example: response = client.get_directory_limits()
    
    
    :rtype: dict
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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
    """
    pass

def get_snapshot_limits(DirectoryId=None):
    """
    Obtains the manual snapshot limits for a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.get_snapshot_limits(
        DirectoryId='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            Contains the identifier of the directory to obtain the limits for.
            

    :rtype: dict
    :return: {
        'SnapshotLimits': {
            'ManualSnapshotsLimit': 123,
            'ManualSnapshotsCurrentCount': 123,
            'ManualSnapshotsLimitReached': True|False
        }
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_ip_routes(DirectoryId=None, NextToken=None, Limit=None):
    """
    Lists the address blocks that you have added to a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.list_ip_routes(
        DirectoryId='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            Identifier (ID) of the directory for which you want to retrieve the IP addresses.
            

    :type NextToken: string
    :param NextToken: The ListIpRoutes.NextToken value from a previous call to ListIpRoutes . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: Maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.

    :rtype: dict
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
    
    
    """
    pass

def list_schema_extensions(DirectoryId=None, NextToken=None, Limit=None):
    """
    Lists all schema extensions applied to a Microsoft AD Directory.
    See also: AWS API Documentation
    
    
    :example: response = client.list_schema_extensions(
        DirectoryId='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory from which to retrieve the schema extension information.
            

    :type NextToken: string
    :param NextToken: The ListSchemaExtensions.NextToken value from a previous call to ListSchemaExtensions . Pass null if this is the first call.

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :rtype: dict
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
    
    
    """
    pass

def list_tags_for_resource(ResourceId=None, NextToken=None, Limit=None):
    """
    Lists all tags on a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceId='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            Identifier (ID) of the directory for which you want to retrieve tags.
            

    :type NextToken: string
    :param NextToken: Reserved for future use.

    :type Limit: integer
    :param Limit: Reserved for future use.

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def register_event_topic(DirectoryId=None, TopicName=None):
    """
    Associates a directory with an SNS topic. This establishes the directory as a publisher to the specified SNS topic. You can then receive email or text (SMS) messages when the status of your directory changes. You get notified if your directory goes from an Active status to an Impaired or Inoperable status. You also receive a notification when the directory returns to an Active status.
    See also: AWS API Documentation
    
    
    :example: response = client.register_event_topic(
        DirectoryId='string',
        TopicName='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The Directory ID that will publish status messages to the SNS topic.
            

    :type TopicName: string
    :param TopicName: [REQUIRED]
            The SNS topic name to which the directory will publish status messages. This SNS topic must be in the same region as the specified Directory ID.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def remove_ip_routes(DirectoryId=None, CidrIps=None):
    """
    Removes IP address blocks from a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_ip_routes(
        DirectoryId='string',
        CidrIps=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            Identifier (ID) of the directory from which you want to remove the IP addresses.
            

    :type CidrIps: list
    :param CidrIps: [REQUIRED]
            IP address blocks that you want to remove.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_tags_from_resource(ResourceId=None, TagKeys=None):
    """
    Removes tags from a directory.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags_from_resource(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            Identifier (ID) of the directory from which to remove the tag.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tag key (name) of the tag to be removed.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def restore_from_snapshot(SnapshotId=None):
    """
    Restores a directory using an existing directory snapshot.
    When you restore a directory from a snapshot, any changes made to the directory after the snapshot date are overwritten.
    This action returns as soon as the restore operation is initiated. You can monitor the progress of the restore operation by calling the  DescribeDirectories operation with the directory identifier. When the DirectoryDescription.Stage value changes to Active , the restore operation is complete.
    See also: AWS API Documentation
    
    
    :example: response = client.restore_from_snapshot(
        SnapshotId='string'
    )
    
    
    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]
            The identifier of the snapshot to restore from.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def start_schema_extension(DirectoryId=None, CreateSnapshotBeforeSchemaExtension=None, LdifContent=None, Description=None):
    """
    Applies a schema extension to a Microsoft AD directory.
    See also: AWS API Documentation
    
    
    :example: response = client.start_schema_extension(
        DirectoryId='string',
        CreateSnapshotBeforeSchemaExtension=True|False,
        LdifContent='string',
        Description='string'
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which the schema extension will be applied to.
            

    :type CreateSnapshotBeforeSchemaExtension: boolean
    :param CreateSnapshotBeforeSchemaExtension: [REQUIRED]
            If true, creates a snapshot of the directory before applying the schema extension.
            

    :type LdifContent: string
    :param LdifContent: [REQUIRED]
            The LDIF file represented as a string. To construct the LdifContent string, precede each line as it would be formatted in an ldif file with n. See the example request below for more details. The file size can be no larger than 1MB.
            

    :type Description: string
    :param Description: [REQUIRED]
            A description of the schema extension.
            

    :rtype: dict
    :return: {
        'SchemaExtensionId': 'string'
    }
    
    
    """
    pass

def update_conditional_forwarder(DirectoryId=None, RemoteDomainName=None, DnsIpAddrs=None):
    """
    Updates a conditional forwarder that has been set up for your AWS directory.
    See also: AWS API Documentation
    
    
    :example: response = client.update_conditional_forwarder(
        DirectoryId='string',
        RemoteDomainName='string',
        DnsIpAddrs=[
            'string',
        ]
    )
    
    
    :type DirectoryId: string
    :param DirectoryId: [REQUIRED]
            The directory ID of the AWS directory for which to update the conditional forwarder.
            

    :type RemoteDomainName: string
    :param RemoteDomainName: [REQUIRED]
            The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.
            

    :type DnsIpAddrs: list
    :param DnsIpAddrs: [REQUIRED]
            The updated IP addresses of the remote DNS server associated with the conditional forwarder.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_radius(DirectoryId=None, RadiusSettings=None):
    """
    Updates the Remote Authentication Dial In User Service (RADIUS) server information for an AD Connector directory.
    See also: AWS API Documentation
    
    
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
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to update the RADIUS server information.
            

    :type RadiusSettings: dict
    :param RadiusSettings: [REQUIRED]
            A RadiusSettings object that contains information about the RADIUS server.
            RadiusServers (list) --An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP addresses of your RADIUS server load balancer.
            (string) --
            RadiusPort (integer) --The port that your RADIUS server is using for communications. Your on-premises network must allow inbound traffic over this port from the AWS Directory Service servers.
            RadiusTimeout (integer) --The amount of time, in seconds, to wait for the RADIUS server to respond.
            RadiusRetries (integer) --The maximum number of times that communication with the RADIUS server is attempted.
            SharedSecret (string) --Not currently used.
            AuthenticationProtocol (string) --The protocol specified for your RADIUS endpoints.
            DisplayLabel (string) --Not currently used.
            UseSameUsername (boolean) --Not currently used.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def verify_trust(TrustId=None):
    """
    AWS Directory Service for Microsoft Active Directory allows you to configure and verify trust relationships.
    This action verifies a trust relationship between your Microsoft AD in the AWS cloud and an external domain.
    See also: AWS API Documentation
    
    
    :example: response = client.verify_trust(
        TrustId='string'
    )
    
    
    :type TrustId: string
    :param TrustId: [REQUIRED]
            The unique Trust ID of the trust relationship to verify.
            

    :rtype: dict
    :return: {
        'TrustId': 'string'
    }
    
    
    """
    pass

