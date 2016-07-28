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

import boto3


class Ds(object):
    def __init__(self):
        self.client = boto3.client('Ds')

    def add_tags_to_resource(self, ResourceId=None, Tags=None):
        """
        :param ResourceId: [REQUIRED]
            The ID of the directory to which to add the tag.
            
        :type ResourceId: string
        :param Tags: [REQUIRED]
            The tags to be assigned to the Amazon Directory Services directory.
            (dict) --Metadata assigned to an Amazon Directory Services directory consisting of a key-value pair.
            Key (string) -- [REQUIRED]A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) -- [REQUIRED]A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
        :type Tags: list
        """
        self.client.add_tags_to_resource(ResourceId=ResourceId, Tags=Tags)

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def connect_directory(self, Name=None, ShortName=None, Password=None, Description=None, Size=None,
                          ConnectSettings=None):
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
        self.client.connect_directory(Name=Name, ShortName=ShortName, Password=Password, Description=Description,
                                      Size=Size, ConnectSettings=ConnectSettings)

    def create_alias(self, DirectoryId=None, Alias=None):
        """
        :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to create the alias.
            
        :type DirectoryId: string
        :param Alias: [REQUIRED]
            The requested alias.
            The alias must be unique amongst all aliases in AWS. This operation throws an EntityAlreadyExistsException error if the alias already exists.
            
        :type Alias: string
        """
        self.client.create_alias(DirectoryId=DirectoryId, Alias=Alias)

    def create_computer(self, DirectoryId=None, ComputerName=None, Password=None,
                        OrganizationalUnitDistinguishedName=None, ComputerAttributes=None):
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
        self.client.create_computer(DirectoryId=DirectoryId, ComputerName=ComputerName, Password=Password,
                                    OrganizationalUnitDistinguishedName=OrganizationalUnitDistinguishedName,
                                    ComputerAttributes=ComputerAttributes)

    def create_conditional_forwarder(self, DirectoryId=None, RemoteDomainName=None, DnsIpAddrs=None):
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
        self.client.create_conditional_forwarder(DirectoryId=DirectoryId, RemoteDomainName=RemoteDomainName,
                                                 DnsIpAddrs=DnsIpAddrs)

    def create_directory(self, Name=None, ShortName=None, Password=None, Description=None, Size=None, VpcSettings=None):
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
        self.client.create_directory(Name=Name, ShortName=ShortName, Password=Password, Description=Description,
                                     Size=Size, VpcSettings=VpcSettings)

    def create_microsoft_ad(self, Name=None, ShortName=None, Password=None, Description=None, VpcSettings=None):
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
        self.client.create_microsoft_ad(Name=Name, ShortName=ShortName, Password=Password, Description=Description,
                                        VpcSettings=VpcSettings)

    def create_snapshot(self, DirectoryId=None, Name=None):
        """
        :param DirectoryId: [REQUIRED]
            The identifier of the directory of which to take a snapshot.
            
        :type DirectoryId: string
        :param Name: The descriptive name to apply to the snapshot.
        :type Name: string
        """
        self.client.create_snapshot(DirectoryId=DirectoryId, Name=Name)

    def create_trust(self, DirectoryId=None, RemoteDomainName=None, TrustPassword=None, TrustDirection=None,
                     TrustType=None, ConditionalForwarderIpAddrs=None):
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
        self.client.create_trust(DirectoryId=DirectoryId, RemoteDomainName=RemoteDomainName,
                                 TrustPassword=TrustPassword, TrustDirection=TrustDirection, TrustType=TrustType,
                                 ConditionalForwarderIpAddrs=ConditionalForwarderIpAddrs)

    def delete_conditional_forwarder(self, DirectoryId=None, RemoteDomainName=None):
        """
        :param DirectoryId: [REQUIRED]
            The directory ID for which you are deleting the conditional forwarder.
            
        :type DirectoryId: string
        :param RemoteDomainName: [REQUIRED]
            The fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.
            
        :type RemoteDomainName: string
        """
        self.client.delete_conditional_forwarder(DirectoryId=DirectoryId, RemoteDomainName=RemoteDomainName)

    def delete_directory(self, DirectoryId=None):
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
        self.client.delete_directory(DirectoryId=DirectoryId)

    def delete_snapshot(self, SnapshotId=None):
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
        self.client.delete_snapshot(SnapshotId=SnapshotId)

    def delete_trust(self, TrustId=None, DeleteAssociatedConditionalForwarder=None):
        """
        :param TrustId: [REQUIRED]
            The Trust ID of the trust relationship to be deleted.
            
        :type TrustId: string
        :param DeleteAssociatedConditionalForwarder: Delete a conditional forwarder as part of a DeleteTrustRequest.
        :type DeleteAssociatedConditionalForwarder: boolean
        """
        self.client.delete_trust(TrustId=TrustId,
                                 DeleteAssociatedConditionalForwarder=DeleteAssociatedConditionalForwarder)

    def deregister_event_topic(self, DirectoryId=None, TopicName=None):
        """
        :param DirectoryId: [REQUIRED]
            The Directory ID to remove as a publisher. This directory will no longer send messages to the specified SNS topic.
            
        :type DirectoryId: string
        :param TopicName: [REQUIRED]
            The name of the SNS topic from which to remove the directory as a publisher.
            
        :type TopicName: string
        """
        self.client.deregister_event_topic(DirectoryId=DirectoryId, TopicName=TopicName)

    def describe_conditional_forwarders(self, DirectoryId=None, RemoteDomainNames=None):
        """
        :param DirectoryId: [REQUIRED]
            The directory ID for which to get the list of associated conditional forwarders.
            
        :type DirectoryId: string
        :param RemoteDomainNames: The fully qualified domain names (FQDN) of the remote domains for which to get the list of associated conditional forwarders. If this member is null, all conditional forwarders are returned.
            (string) --
            
        :type RemoteDomainNames: list
        """
        self.client.describe_conditional_forwarders(DirectoryId=DirectoryId, RemoteDomainNames=RemoteDomainNames)

    def describe_directories(self, DirectoryIds=None, NextToken=None, Limit=None):
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
        self.client.describe_directories(DirectoryIds=DirectoryIds, NextToken=NextToken, Limit=Limit)

    def describe_event_topics(self, DirectoryId=None, TopicNames=None):
        """
        :param DirectoryId: The Directory ID for which to get the list of associated SNS topics. If this member is null, associations for all Directory IDs are returned.
        :type DirectoryId: string
        :param TopicNames: A list of SNS topic names for which to obtain the information. If this member is null, all associations for the specified Directory ID are returned.
            An empty list results in an InvalidParameterException being thrown.
            (string) --
            
        :type TopicNames: list
        """
        self.client.describe_event_topics(DirectoryId=DirectoryId, TopicNames=TopicNames)

    def describe_snapshots(self, DirectoryId=None, SnapshotIds=None, NextToken=None, Limit=None):
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
        self.client.describe_snapshots(DirectoryId=DirectoryId, SnapshotIds=SnapshotIds, NextToken=NextToken,
                                       Limit=Limit)

    def describe_trusts(self, DirectoryId=None, TrustIds=None, NextToken=None, Limit=None):
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
        self.client.describe_trusts(DirectoryId=DirectoryId, TrustIds=TrustIds, NextToken=NextToken, Limit=Limit)

    def disable_radius(self, DirectoryId=None):
        """
        :param DirectoryId: [REQUIRED]
            The identifier of the directory for which to disable MFA.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the results of the DisableRadius operation.
            
            
        :type DirectoryId: string
        """
        self.client.disable_radius(DirectoryId=DirectoryId)

    def disable_sso(self, DirectoryId=None, UserName=None, Password=None):
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
        self.client.disable_sso(DirectoryId=DirectoryId, UserName=UserName, Password=Password)

    def enable_radius(self, DirectoryId=None, RadiusSettings=None):
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
            SharedSecret (string) --The shared secret code that was specified when your RADIUS endpoints were created.
            AuthenticationProtocol (string) --The protocol specified for your RADIUS endpoints.
            DisplayLabel (string) --Not currently used.
            UseSameUsername (boolean) --Not currently used.
            
        :type RadiusSettings: dict
        """
        self.client.enable_radius(DirectoryId=DirectoryId, RadiusSettings=RadiusSettings)

    def enable_sso(self, DirectoryId=None, UserName=None, Password=None):
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
        self.client.enable_sso(DirectoryId=DirectoryId, UserName=UserName, Password=Password)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_directory_limits(self):
        """
        """
        self.client.get_directory_limits()

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_snapshot_limits(self, DirectoryId=None):
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
        self.client.get_snapshot_limits(DirectoryId=DirectoryId)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def list_tags_for_resource(self, ResourceId=None, NextToken=None, Limit=None):
        """
        :param ResourceId: [REQUIRED]
            The ID of the directory for which you want to retrieve tags.
            
        :type ResourceId: string
        :param NextToken: Reserved for future use.
        :type NextToken: string
        :param Limit: Reserved for future use.
        :type Limit: integer
        """
        self.client.list_tags_for_resource(ResourceId=ResourceId, NextToken=NextToken, Limit=Limit)

    def register_event_topic(self, DirectoryId=None, TopicName=None):
        """
        :param DirectoryId: [REQUIRED]
            The Directory ID that will publish status messages to the SNS topic.
            
        :type DirectoryId: string
        :param TopicName: [REQUIRED]
            The SNS topic name to which the directory will publish status messages. This SNS topic must be in the same region as the specified Directory ID.
            
        :type TopicName: string
        """
        self.client.register_event_topic(DirectoryId=DirectoryId, TopicName=TopicName)

    def remove_tags_from_resource(self, ResourceId=None, TagKeys=None):
        """
        :param ResourceId: [REQUIRED]
            The ID of the directory from which to remove the tag.
            
        :type ResourceId: string
        :param TagKeys: [REQUIRED]
            The tag key (name) of the tag to be removed.
            (string) --
            
        :type TagKeys: list
        """
        self.client.remove_tags_from_resource(ResourceId=ResourceId, TagKeys=TagKeys)

    def restore_from_snapshot(self, SnapshotId=None):
        """
        :param SnapshotId: [REQUIRED]
            The identifier of the snapshot to restore from.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the results of the RestoreFromSnapshot operation.
            
            
        :type SnapshotId: string
        """
        self.client.restore_from_snapshot(SnapshotId=SnapshotId)

    def update_conditional_forwarder(self, DirectoryId=None, RemoteDomainName=None, DnsIpAddrs=None):
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
        self.client.update_conditional_forwarder(DirectoryId=DirectoryId, RemoteDomainName=RemoteDomainName,
                                                 DnsIpAddrs=DnsIpAddrs)

    def update_radius(self, DirectoryId=None, RadiusSettings=None):
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
            SharedSecret (string) --The shared secret code that was specified when your RADIUS endpoints were created.
            AuthenticationProtocol (string) --The protocol specified for your RADIUS endpoints.
            DisplayLabel (string) --Not currently used.
            UseSameUsername (boolean) --Not currently used.
            
        :type RadiusSettings: dict
        """
        self.client.update_radius(DirectoryId=DirectoryId, RadiusSettings=RadiusSettings)

    def verify_trust(self, TrustId=None):
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
        self.client.verify_trust(TrustId=TrustId)
