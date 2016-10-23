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


def add_ip_routes(DirectoryId=None, IpRoutes=None, UpdateSecurityGroupForDirectoryControllers=None):
    """
    :param DirectoryId: [REQUIRED]
            Identifier (ID) of the directory to which to add the address block.
            
    :type DirectoryId: string
    :param IpRoutes: [REQUIRED]
            IP address blocks, using CIDR format, of the traffic to route. This is often the IP address block of the DNS server used for your on-premises domain.
            (dict) --IP address block. This is often the address block of the DNS server used for your on-premises domain.
            CidrIp (string) --IP address block using CIDR format, for example 10.0.0.0/24. This is often the address block of the DNS server used for your on-premises domain. For a single IP address use a CIDR address block with /32. For example 10.0.0.0/32.
            Description (string) --Description of the address block.
            
            
    :type IpRoutes: list
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
            
    :type UpdateSecurityGroupForDirectoryControllers: boolean
    """
    pass


def add_tags_to_resource(ResourceId=None, Tags=None):
    """
    :param ResourceId: [REQUIRED]
            Identifier (ID) for the directory to which to add the tag.
            
    :type ResourceId: string
    :param Tags: [REQUIRED]
            The tags to be assigned to the Amazon Directory Services directory.
            (dict) --Metadata assigned to an Amazon Directory Services directory consisting of a key-value pair.
            Key (string) -- [REQUIRED]Required name of the tag. The string value can be Unicode characters and cannot be prefixed with 'aws:'. The string can contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) -- [REQUIRED]The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


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


def connect_directory(Name=None, ShortName=None, Password=None, Description=None, Size=None, ConnectSettings=None):
    """
    :param Name: [REQUIRED]
            The fully-qualified name of the on-premises directory, such as corp.example.com .
            
    :type Name: string
    :param ShortName: The NetBIOS name of the on-premises directory, such as CORP .
    :type ShortName: string
    :param Password: [REQUIRED]
            The password for the on-premises user account.
            
    :type Password: string
    :param Description: A textual description for the directory.
    :type Description: string
    :param Size: [REQUIRED]
            The size of the directory.
            
    :type Size: string
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
            
    :type ConnectSettings: dict
    """
    pass


def create_alias(DirectoryId=None, Alias=None):
    """
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to create the alias.
            
    :type DirectoryId: string
    :param Alias: [REQUIRED]
            The requested alias.
            The alias must be unique amongst all aliases in AWS. This operation throws an EntityAlreadyExistsException error if the alias already exists.
            
    :type Alias: string
    """
    pass


def create_computer(DirectoryId=None, ComputerName=None, Password=None, OrganizationalUnitDistinguishedName=None,
                    ComputerAttributes=None):
    """
    :param DirectoryId: [REQUIRED]
            The identifier of the directory in which to create the computer account.
            
    :type DirectoryId: string
    :param ComputerName: [REQUIRED]
            The name of the computer account.
            
    :type ComputerName: string
    :param Password: [REQUIRED]
            A one-time password that is used to join the computer to the directory. You should generate a random, strong password to use for this parameter.
            
    :type Password: string
    :param OrganizationalUnitDistinguishedName: The fully-qualified distinguished name of the organizational unit to place the computer account in.
    :type OrganizationalUnitDistinguishedName: string
    :param ComputerAttributes: An array of Attribute objects that contain any LDAP attributes to apply to the computer account.
            (dict) --Represents a named directory attribute.
            Name (string) --The name of the attribute.
            Value (string) --The value of the attribute.
            
            
    :type ComputerAttributes: list
    """
    pass


def create_conditional_forwarder(DirectoryId=None, RemoteDomainName=None, DnsIpAddrs=None):
    """
    :param DirectoryId: [REQUIRED]
            The directory ID of the AWS directory for which you are creating the conditional forwarder.
            
    :type DirectoryId: string
    :param RemoteDomainName: [REQUIRED]
            The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.
            
    :type RemoteDomainName: string
    :param DnsIpAddrs: [REQUIRED]
            The IP addresses of the remote DNS server associated with RemoteDomainName.
            (string) --
            
    :type DnsIpAddrs: list
    """
    pass


def create_directory(Name=None, ShortName=None, Password=None, Description=None, Size=None, VpcSettings=None):
    """
    :param Name: [REQUIRED]
            The fully qualified name for the directory, such as corp.example.com .
            
    :type Name: string
    :param ShortName: The short name of the directory, such as CORP .
    :type ShortName: string
    :param Password: [REQUIRED]
            The password for the directory administrator. The directory creation process creates a directory administrator account with the username Administrator and this password.
            
    :type Password: string
    :param Description: A textual description for the directory.
    :type Description: string
    :param Size: [REQUIRED]
            The size of the directory.
            
    :type Size: string
    :param VpcSettings: A DirectoryVpcSettings object that contains additional information for the operation.
            VpcId (string) -- [REQUIRED]The identifier of the VPC in which to create the directory.
            SubnetIds (list) -- [REQUIRED]The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service creates a directory server and a DNS server in each of these subnets.
            (string) --
            
    :type VpcSettings: dict
    """
    pass


def create_microsoft_ad(Name=None, ShortName=None, Password=None, Description=None, VpcSettings=None):
    """
    :param Name: [REQUIRED]
            The fully qualified domain name for the directory, such as corp.example.com . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
            
    :type Name: string
    :param ShortName: The NetBIOS name for your domain. A short identifier for your domain, such as CORP . If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, CORP for the directory DNS corp.example.com .
    :type ShortName: string
    :param Password: [REQUIRED]
            The password for the default administrative user named Admin .
            
    :type Password: string
    :param Description: A textual description for the directory. This label will appear on the AWS console Directory Details page after the directory is created.
    :type Description: string
    :param VpcSettings: [REQUIRED]
            Contains VPC information for the CreateDirectory or CreateMicrosoftAD operation.
            VpcId (string) -- [REQUIRED]The identifier of the VPC in which to create the directory.
            SubnetIds (list) -- [REQUIRED]The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service creates a directory server and a DNS server in each of these subnets.
            (string) --
            
    :type VpcSettings: dict
    """
    pass


def create_snapshot(DirectoryId=None, Name=None):
    """
    :param DirectoryId: [REQUIRED]
            The identifier of the directory of which to take a snapshot.
            
    :type DirectoryId: string
    :param Name: The descriptive name to apply to the snapshot.
    :type Name: string
    """
    pass


def create_trust(DirectoryId=None, RemoteDomainName=None, TrustPassword=None, TrustDirection=None, TrustType=None,
                 ConditionalForwarderIpAddrs=None):
    """
    :param DirectoryId: [REQUIRED]
            The Directory ID of the Microsoft AD in the AWS cloud for which to establish the trust relationship.
            
    :type DirectoryId: string
    :param RemoteDomainName: [REQUIRED]
            The Fully Qualified Domain Name (FQDN) of the external domain for which to create the trust relationship.
            
    :type RemoteDomainName: string
    :param TrustPassword: [REQUIRED]
            The trust password. The must be the same password that was used when creating the trust relationship on the external domain.
            
    :type TrustPassword: string
    :param TrustDirection: [REQUIRED]
            The direction of the trust relationship.
            
    :type TrustDirection: string
    :param TrustType: The trust relationship type.
    :type TrustType: string
    :param ConditionalForwarderIpAddrs: The IP addresses of the remote DNS server associated with RemoteDomainName.
            (string) --
            
    :type ConditionalForwarderIpAddrs: list
    """
    pass


def delete_conditional_forwarder(DirectoryId=None, RemoteDomainName=None):
    """
    :param DirectoryId: [REQUIRED]
            The directory ID for which you are deleting the conditional forwarder.
            
    :type DirectoryId: string
    :param RemoteDomainName: [REQUIRED]
            The fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.
            
    :type RemoteDomainName: string
    """
    pass


def delete_directory(DirectoryId=None):
    """
    :param DirectoryId: [REQUIRED]
            The identifier of the directory to delete.
            Return typedict
            ReturnsResponse Syntax{
              'DirectoryId': 'string'
            }
            Response Structure
            (dict) --Contains the results of the DeleteDirectory operation.
            DirectoryId (string) --The directory identifier.
            
            
    :type DirectoryId: string
    """
    pass


def delete_snapshot(SnapshotId=None):
    """
    :param SnapshotId: [REQUIRED]
            The identifier of the directory snapshot to be deleted.
            Return typedict
            ReturnsResponse Syntax{
              'SnapshotId': 'string'
            }
            Response Structure
            (dict) --Contains the results of the DeleteSnapshot operation.
            SnapshotId (string) --The identifier of the directory snapshot that was deleted.
            
            
    :type SnapshotId: string
    """
    pass


def delete_trust(TrustId=None, DeleteAssociatedConditionalForwarder=None):
    """
    :param TrustId: [REQUIRED]
            The Trust ID of the trust relationship to be deleted.
            
    :type TrustId: string
    :param DeleteAssociatedConditionalForwarder: Delete a conditional forwarder as part of a DeleteTrustRequest.
    :type DeleteAssociatedConditionalForwarder: boolean
    """
    pass


def deregister_event_topic(DirectoryId=None, TopicName=None):
    """
    :param DirectoryId: [REQUIRED]
            The Directory ID to remove as a publisher. This directory will no longer send messages to the specified SNS topic.
            
    :type DirectoryId: string
    :param TopicName: [REQUIRED]
            The name of the SNS topic from which to remove the directory as a publisher.
            
    :type TopicName: string
    """
    pass


def describe_conditional_forwarders(DirectoryId=None, RemoteDomainNames=None):
    """
    :param DirectoryId: [REQUIRED]
            The directory ID for which to get the list of associated conditional forwarders.
            
    :type DirectoryId: string
    :param RemoteDomainNames: The fully qualified domain names (FQDN) of the remote domains for which to get the list of associated conditional forwarders. If this member is null, all conditional forwarders are returned.
            (string) --
            
    :type RemoteDomainNames: list
    """
    pass


def describe_directories(DirectoryIds=None, NextToken=None, Limit=None):
    """
    :param DirectoryIds: A list of identifiers of the directories for which to obtain the information. If this member is null, all directories that belong to the current account are returned.
            An empty list results in an InvalidParameterException being thrown.
            (string) --
            
    :type DirectoryIds: list
    :param NextToken: The DescribeDirectoriesResult.NextToken value from a previous call to DescribeDirectories . Pass null if this is the first call.
    :type NextToken: string
    :param Limit: The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.
    :type Limit: integer
    """
    pass


def describe_event_topics(DirectoryId=None, TopicNames=None):
    """
    :param DirectoryId: The Directory ID for which to get the list of associated SNS topics. If this member is null, associations for all Directory IDs are returned.
    :type DirectoryId: string
    :param TopicNames: A list of SNS topic names for which to obtain the information. If this member is null, all associations for the specified Directory ID are returned.
            An empty list results in an InvalidParameterException being thrown.
            (string) --
            
    :type TopicNames: list
    """
    pass


def describe_snapshots(DirectoryId=None, SnapshotIds=None, NextToken=None, Limit=None):
    """
    :param DirectoryId: The identifier of the directory for which to retrieve snapshot information.
    :type DirectoryId: string
    :param SnapshotIds: A list of identifiers of the snapshots to obtain the information for. If this member is null or empty, all snapshots are returned using the Limit and NextToken members.
            (string) --
            
    :type SnapshotIds: list
    :param NextToken: The DescribeSnapshotsResult.NextToken value from a previous call to DescribeSnapshots . Pass null if this is the first call.
    :type NextToken: string
    :param Limit: The maximum number of objects to return.
    :type Limit: integer
    """
    pass


def describe_trusts(DirectoryId=None, TrustIds=None, NextToken=None, Limit=None):
    """
    :param DirectoryId: The Directory ID of the AWS directory that is a part of the requested trust relationship.
    :type DirectoryId: string
    :param TrustIds: A list of identifiers of the trust relationships for which to obtain the information. If this member is null, all trust relationships that belong to the current account are returned.
            An empty list results in an InvalidParameterException being thrown.
            (string) --
            
    :type TrustIds: list
    :param NextToken: The DescribeTrustsResult.NextToken value from a previous call to DescribeTrusts . Pass null if this is the first call.
    :type NextToken: string
    :param Limit: The maximum number of objects to return.
    :type Limit: integer
    """
    pass


def disable_radius(DirectoryId=None):
    """
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to disable MFA.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the results of the DisableRadius operation.
            
            
    :type DirectoryId: string
    """
    pass


def disable_sso(DirectoryId=None, UserName=None, Password=None):
    """
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to disable single-sign on.
            
    :type DirectoryId: string
    :param UserName: The username of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. This account must have privileges to remove a service principal name.
            If the AD Connector service account does not have privileges to remove a service principal name, you can specify an alternate account with the UserName and Password parameters. These credentials are only used to disable single sign-on and are not stored by the service. The AD Connector service account is not changed.
            
    :type UserName: string
    :param Password: The password of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. For more information, see the UserName parameter.
    :type Password: string
    """
    pass


def enable_radius(DirectoryId=None, RadiusSettings=None):
    """
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to enable MFA.
            
    :type DirectoryId: string
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
            
    :type RadiusSettings: dict
    """
    pass


def enable_sso(DirectoryId=None, UserName=None, Password=None):
    """
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to enable single-sign on.
            
    :type DirectoryId: string
    :param UserName: The username of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. This account must have privileges to add a service principal name.
            If the AD Connector service account does not have privileges to add a service principal name, you can specify an alternate account with the UserName and Password parameters. These credentials are only used to enable single sign-on and are not stored by the service. The AD Connector service account is not changed.
            
    :type UserName: string
    :param Password: The password of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. For more information, see the UserName parameter.
    :type Password: string
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


def get_directory_limits():
    """
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


def get_snapshot_limits(DirectoryId=None):
    """
    :param DirectoryId: [REQUIRED]
            Contains the identifier of the directory to obtain the limits for.
            Return typedict
            ReturnsResponse Syntax{
              'SnapshotLimits': {
                'ManualSnapshotsLimit': 123,
                'ManualSnapshotsCurrentCount': 123,
                'ManualSnapshotsLimitReached': True|False
              }
            }
            Response Structure
            (dict) --Contains the results of the GetSnapshotLimits operation.
            SnapshotLimits (dict) --A SnapshotLimits object that contains the manual snapshot limits for the specified directory.
            ManualSnapshotsLimit (integer) --The maximum number of manual snapshots allowed.
            ManualSnapshotsCurrentCount (integer) --The current number of manual snapshots of the directory.
            ManualSnapshotsLimitReached (boolean) --Indicates if the manual snapshot limit has been reached.
            
            
            
    :type DirectoryId: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_ip_routes(DirectoryId=None, NextToken=None, Limit=None):
    """
    :param DirectoryId: [REQUIRED]
            Identifier (ID) of the directory for which you want to retrieve the IP addresses.
            
    :type DirectoryId: string
    :param NextToken: The ListIpRoutes.NextToken value from a previous call to ListIpRoutes . Pass null if this is the first call.
    :type NextToken: string
    :param Limit: Maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.
    :type Limit: integer
    """
    pass


def list_tags_for_resource(ResourceId=None, NextToken=None, Limit=None):
    """
    :param ResourceId: [REQUIRED]
            Identifier (ID) of the directory for which you want to retrieve tags.
            
    :type ResourceId: string
    :param NextToken: Reserved for future use.
    :type NextToken: string
    :param Limit: Reserved for future use.
    :type Limit: integer
    """
    pass


def register_event_topic(DirectoryId=None, TopicName=None):
    """
    :param DirectoryId: [REQUIRED]
            The Directory ID that will publish status messages to the SNS topic.
            
    :type DirectoryId: string
    :param TopicName: [REQUIRED]
            The SNS topic name to which the directory will publish status messages. This SNS topic must be in the same region as the specified Directory ID.
            
    :type TopicName: string
    """
    pass


def remove_ip_routes(DirectoryId=None, CidrIps=None):
    """
    :param DirectoryId: [REQUIRED]
            Identifier (ID) of the directory from which you want to remove the IP addresses.
            
    :type DirectoryId: string
    :param CidrIps: [REQUIRED]
            IP address blocks that you want to remove.
            (string) --
            
    :type CidrIps: list
    """
    pass


def remove_tags_from_resource(ResourceId=None, TagKeys=None):
    """
    :param ResourceId: [REQUIRED]
            Identifier (ID) of the directory from which to remove the tag.
            
    :type ResourceId: string
    :param TagKeys: [REQUIRED]
            The tag key (name) of the tag to be removed.
            (string) --
            
    :type TagKeys: list
    """
    pass


def restore_from_snapshot(SnapshotId=None):
    """
    :param SnapshotId: [REQUIRED]
            The identifier of the snapshot to restore from.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the results of the RestoreFromSnapshot operation.
            
            
    :type SnapshotId: string
    """
    pass


def update_conditional_forwarder(DirectoryId=None, RemoteDomainName=None, DnsIpAddrs=None):
    """
    :param DirectoryId: [REQUIRED]
            The directory ID of the AWS directory for which to update the conditional forwarder.
            
    :type DirectoryId: string
    :param RemoteDomainName: [REQUIRED]
            The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.
            
    :type RemoteDomainName: string
    :param DnsIpAddrs: [REQUIRED]
            The updated IP addresses of the remote DNS server associated with the conditional forwarder.
            (string) --
            
    :type DnsIpAddrs: list
    """
    pass


def update_radius(DirectoryId=None, RadiusSettings=None):
    """
    :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to update the RADIUS server information.
            
    :type DirectoryId: string
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
            
    :type RadiusSettings: dict
    """
    pass


def verify_trust(TrustId=None):
    """
    :param TrustId: [REQUIRED]
            The unique Trust ID of the trust relationship to verify.
            Return typedict
            ReturnsResponse Syntax{
              'TrustId': 'string'
            }
            Response Structure
            (dict) --Result of a VerifyTrust request.
            TrustId (string) --The unique Trust ID of the trust relationship that was verified.
            
            
    :type TrustId: string
    """
    pass
