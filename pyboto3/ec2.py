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


def accept_reserved_instances_exchange_quote(DryRun=None, ReservedInstanceIds=None, TargetConfigurations=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ReservedInstanceIds: [REQUIRED]
            The IDs of the Convertible Reserved Instances that you want to exchange for other Convertible Reserved Instances of the same or higher value.
            (string) --
            
    :type ReservedInstanceIds: list
    :param TargetConfigurations: The configurations of the Convertible Reserved Instance offerings you are purchasing in this exchange.
            (dict) --Details about the target configuration.
            OfferingId (string) -- [REQUIRED]The Convertible Reserved Instance offering ID. If this isn't included in the request, the response lists your current Convertible Reserved Instance/s and their value/s.
            InstanceCount (integer) --The number of instances the Covertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request
            
            
    :type TargetConfigurations: list
    """
    pass


def accept_vpc_peering_connection(DryRun=None, VpcPeeringConnectionId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcPeeringConnectionId: The ID of the VPC peering connection.
    :type VpcPeeringConnectionId: string
    """
    pass


def allocate_address(DryRun=None, Domain=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Domain: Set to vpc to allocate the address for use with instances in a VPC.
            Default: The address is for use with instances in EC2-Classic.
            
    :type Domain: string
    """
    pass


def allocate_hosts(AutoPlacement=None, ClientToken=None, InstanceType=None, Quantity=None, AvailabilityZone=None):
    """
    :param AutoPlacement: This is enabled by default. This property allows instances to be automatically placed onto available Dedicated Hosts, when you are launching instances without specifying a host ID.
            Default: Enabled
            
    :type AutoPlacement: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide .
    :type ClientToken: string
    :param InstanceType: [REQUIRED]
            Specify the instance type that you want your Dedicated Hosts to be configured for. When you specify the instance type, that is the only instance type that you can launch onto that host.
            
    :type InstanceType: string
    :param Quantity: [REQUIRED]
            The number of Dedicated Hosts you want to allocate to your account with these parameters.
            
    :type Quantity: integer
    :param AvailabilityZone: [REQUIRED]
            The Availability Zone for the Dedicated Hosts.
            
    :type AvailabilityZone: string
    """
    pass


def assign_private_ip_addresses(NetworkInterfaceId=None, PrivateIpAddresses=None, SecondaryPrivateIpAddressCount=None,
                                AllowReassignment=None):
    """
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            
    :type NetworkInterfaceId: string
    :param PrivateIpAddresses: One or more IP addresses to be assigned as a secondary private IP address to the network interface. You can't specify this parameter when also specifying a number of secondary IP addresses.
            If you don't specify an IP address, Amazon EC2 automatically selects an IP address within the subnet range.
            (string) --
            
    :type PrivateIpAddresses: list
    :param SecondaryPrivateIpAddressCount: The number of secondary IP addresses to assign to the network interface. You can't specify this parameter when also specifying private IP addresses.
    :type SecondaryPrivateIpAddressCount: integer
    :param AllowReassignment: Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.
    :type AllowReassignment: boolean
    """
    pass


def associate_address(DryRun=None, InstanceId=None, PublicIp=None, AllocationId=None, NetworkInterfaceId=None,
                      PrivateIpAddress=None, AllowReassociation=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: The ID of the instance. This is required for EC2-Classic. For EC2-VPC, you can specify either the instance ID or the network interface ID, but not both. The operation fails if you specify an instance ID unless exactly one network interface is attached.
    :type InstanceId: string
    :param PublicIp: The Elastic IP address. This is required for EC2-Classic.
    :type PublicIp: string
    :param AllocationId: [EC2-VPC] The allocation ID. This is required for EC2-VPC.
    :type AllocationId: string
    :param NetworkInterfaceId: [EC2-VPC] The ID of the network interface. If the instance has more than one network interface, you must specify a network interface ID.
    :type NetworkInterfaceId: string
    :param PrivateIpAddress: [EC2-VPC] The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.
    :type PrivateIpAddress: string
    :param AllowReassociation: [EC2-VPC] For a VPC in an EC2-Classic account, specify true to allow an Elastic IP address that is already associated with an instance or network interface to be reassociated with the specified instance or network interface. Otherwise, the operation fails. In a VPC in an EC2-VPC-only account, reassociation is automatic, therefore you can specify false to ensure the operation fails if the Elastic IP address is already associated with another resource.
    :type AllowReassociation: boolean
    """
    pass


def associate_dhcp_options(DryRun=None, DhcpOptionsId=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param DhcpOptionsId: [REQUIRED]
            The ID of the DHCP options set, or default to associate no DHCP options with the VPC.
            
    :type DhcpOptionsId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def associate_route_table(DryRun=None, SubnetId=None, RouteTableId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SubnetId: [REQUIRED]
            The ID of the subnet.
            
    :type SubnetId: string
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            
    :type RouteTableId: string
    """
    pass


def attach_classic_link_vpc(DryRun=None, InstanceId=None, VpcId=None, Groups=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of an EC2-Classic instance to link to the ClassicLink-enabled VPC.
            
    :type InstanceId: string
    :param VpcId: [REQUIRED]
            The ID of a ClassicLink-enabled VPC.
            
    :type VpcId: string
    :param Groups: [REQUIRED]
            The ID of one or more of the VPC's security groups. You cannot specify security groups from a different VPC.
            (string) --
            
    :type Groups: list
    """
    pass


def attach_internet_gateway(DryRun=None, InternetGatewayId=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InternetGatewayId: [REQUIRED]
            The ID of the Internet gateway.
            
    :type InternetGatewayId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def attach_network_interface(DryRun=None, NetworkInterfaceId=None, InstanceId=None, DeviceIndex=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            
    :type NetworkInterfaceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param DeviceIndex: [REQUIRED]
            The index of the device for the network interface attachment.
            
    :type DeviceIndex: integer
    """
    pass


def attach_volume(DryRun=None, VolumeId=None, InstanceId=None, Device=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VolumeId: [REQUIRED]
            The ID of the EBS volume. The volume and instance must be within the same Availability Zone.
            
    :type VolumeId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param Device: [REQUIRED]
            The device name to expose to the instance (for example, /dev/sdh or xvdh ).
            
    :type Device: string
    """
    pass


def attach_vpn_gateway(DryRun=None, VpnGatewayId=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpnGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            
    :type VpnGatewayId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def authorize_security_group_egress(DryRun=None, GroupId=None, SourceSecurityGroupName=None,
                                    SourceSecurityGroupOwnerId=None, IpProtocol=None, FromPort=None, ToPort=None,
                                    CidrIp=None, IpPermissions=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupId: [REQUIRED]
            The ID of the security group.
            
    :type GroupId: string
    :param SourceSecurityGroupName: The name of a destination security group. To authorize outbound access to a destination security group, we recommend that you use a set of IP permissions instead.
    :type SourceSecurityGroupName: string
    :param SourceSecurityGroupOwnerId: The AWS account number for a destination security group. To authorize outbound access to a destination security group, we recommend that you use a set of IP permissions instead.
    :type SourceSecurityGroupOwnerId: string
    :param IpProtocol: The IP protocol name or number. We recommend that you specify the protocol in a set of IP permissions instead.
    :type IpProtocol: string
    :param FromPort: The start of port range for the TCP and UDP protocols, or an ICMP type number. We recommend that you specify the port range in a set of IP permissions instead.
    :type FromPort: integer
    :param ToPort: The end of port range for the TCP and UDP protocols, or an ICMP type number. We recommend that you specify the port range in a set of IP permissions instead.
    :type ToPort: integer
    :param CidrIp: The CIDR IP address range. We recommend that you specify the CIDR range in a set of IP permissions instead.
    :type CidrIp: string
    :param IpPermissions: A set of IP permissions. You can't specify a destination security group and a CIDR IP address range.
            (dict) --Describes a security group rule.
            IpProtocol (string) --The IP protocol name (for tcp , udp , and icmp ) or number (see Protocol Numbers ).
            [EC2-VPC only] When you authorize or revoke security group rules, you can use -1 to specify all.
            FromPort (integer) --The start of port range for the TCP and UDP protocols, or an ICMP type number. A value of -1 indicates all ICMP types.
            ToPort (integer) --The end of port range for the TCP and UDP protocols, or an ICMP code. A value of -1 indicates all ICMP codes for the specified ICMP type.
            UserIdGroupPairs (list) --One or more security group and AWS account ID pairs.
            (dict) --Describes a security group and AWS account ID pair.
            UserId (string) --The ID of an AWS account. For a referenced security group in another VPC, the account ID of the referenced security group is returned.
            [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
            GroupName (string) --The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.
            GroupId (string) --The ID of the security group.
            VpcId (string) --The ID of the VPC for the referenced security group, if applicable.
            VpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.
            PeeringStatus (string) --The status of a VPC peering connection, if applicable.
            
            IpRanges (list) --One or more IP ranges.
            (dict) --Describes an IP range.
            CidrIp (string) --The CIDR range. You can either specify a CIDR range or a source security group, not both.
            
            PrefixListIds (list) --(Valid for AuthorizeSecurityGroupEgress , RevokeSecurityGroupEgress and DescribeSecurityGroups only) One or more prefix list IDs for an AWS service. In an AuthorizeSecurityGroupEgress request, this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
            (dict) --The ID of the prefix.
            PrefixListId (string) --The ID of the prefix.
            
            
            
    :type IpPermissions: list
    """
    pass


def authorize_security_group_ingress(DryRun=None, GroupName=None, GroupId=None, SourceSecurityGroupName=None,
                                     SourceSecurityGroupOwnerId=None, IpProtocol=None, FromPort=None, ToPort=None,
                                     CidrIp=None, IpPermissions=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupName: [EC2-Classic, default VPC] The name of the security group.
    :type GroupName: string
    :param GroupId: The ID of the security group. Required for a nondefault VPC.
    :type GroupId: string
    :param SourceSecurityGroupName: [EC2-Classic, default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. Creates rules that grant full ICMP, UDP, and TCP access. To create a rule with a specific IP protocol and port range, use a set of IP permissions instead. For EC2-VPC, the source security group must be in the same VPC.
    :type SourceSecurityGroupName: string
    :param SourceSecurityGroupOwnerId: [EC2-Classic] The AWS account number for the source security group, if the source security group is in a different account. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range. Creates rules that grant full ICMP, UDP, and TCP access. To create a rule with a specific IP protocol and port range, use a set of IP permissions instead.
    :type SourceSecurityGroupOwnerId: string
    :param IpProtocol: The IP protocol name (tcp , udp , icmp ) or number (see Protocol Numbers ). (VPC only) Use -1 to specify all traffic. If you specify -1 , traffic on all ports is allowed, regardless of any ports you specify.
    :type IpProtocol: string
    :param FromPort: The start of port range for the TCP and UDP protocols, or an ICMP type number. For the ICMP type number, use -1 to specify all ICMP types.
    :type FromPort: integer
    :param ToPort: The end of port range for the TCP and UDP protocols, or an ICMP code number. For the ICMP code number, use -1 to specify all ICMP codes for the ICMP type.
    :type ToPort: integer
    :param CidrIp: The CIDR IP address range. You can't specify this parameter when specifying a source security group.
    :type CidrIp: string
    :param IpPermissions: A set of IP permissions. Can be used to specify multiple rules in a single command.
            (dict) --Describes a security group rule.
            IpProtocol (string) --The IP protocol name (for tcp , udp , and icmp ) or number (see Protocol Numbers ).
            [EC2-VPC only] When you authorize or revoke security group rules, you can use -1 to specify all.
            FromPort (integer) --The start of port range for the TCP and UDP protocols, or an ICMP type number. A value of -1 indicates all ICMP types.
            ToPort (integer) --The end of port range for the TCP and UDP protocols, or an ICMP code. A value of -1 indicates all ICMP codes for the specified ICMP type.
            UserIdGroupPairs (list) --One or more security group and AWS account ID pairs.
            (dict) --Describes a security group and AWS account ID pair.
            UserId (string) --The ID of an AWS account. For a referenced security group in another VPC, the account ID of the referenced security group is returned.
            [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
            GroupName (string) --The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.
            GroupId (string) --The ID of the security group.
            VpcId (string) --The ID of the VPC for the referenced security group, if applicable.
            VpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.
            PeeringStatus (string) --The status of a VPC peering connection, if applicable.
            
            IpRanges (list) --One or more IP ranges.
            (dict) --Describes an IP range.
            CidrIp (string) --The CIDR range. You can either specify a CIDR range or a source security group, not both.
            
            PrefixListIds (list) --(Valid for AuthorizeSecurityGroupEgress , RevokeSecurityGroupEgress and DescribeSecurityGroups only) One or more prefix list IDs for an AWS service. In an AuthorizeSecurityGroupEgress request, this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
            (dict) --The ID of the prefix.
            PrefixListId (string) --The ID of the prefix.
            
            
            
    :type IpPermissions: list
    """
    pass


def bundle_instance(DryRun=None, InstanceId=None, Storage=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of the instance to bundle.
            Type: String
            Default: None
            Required: Yes
            
    :type InstanceId: string
    :param Storage: [REQUIRED]
            The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.
            S3 (dict) --An Amazon S3 storage location.
            Bucket (string) --The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.
            Prefix (string) --The beginning of the file name of the AMI.
            AWSAccessKeyId (string) --The access key ID of the owner of the bucket. Before you specify a value for your access key ID, review and follow the guidance in Best Practices for Managing AWS Access Keys .
            UploadPolicy (bytes) --An Amazon S3 upload policy that gives Amazon EC2 permission to upload items into Amazon S3 on your behalf.
            UploadPolicySignature (string) --The signature of the JSON document.
            
            
    :type Storage: dict
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


def cancel_bundle_task(DryRun=None, BundleId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param BundleId: [REQUIRED]
            The ID of the bundle task.
            
    :type BundleId: string
    """
    pass


def cancel_conversion_task(DryRun=None, ConversionTaskId=None, ReasonMessage=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ConversionTaskId: [REQUIRED]
            The ID of the conversion task.
            
    :type ConversionTaskId: string
    :param ReasonMessage: The reason for canceling the conversion task.
    :type ReasonMessage: string
    """
    pass


def cancel_export_task(ExportTaskId=None):
    """
    :param ExportTaskId: [REQUIRED]
            The ID of the export task. This is the ID returned by CreateInstanceExportTask .
            ReturnsNone
            
    :type ExportTaskId: string
    """
    pass


def cancel_import_task(DryRun=None, ImportTaskId=None, CancelReason=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImportTaskId: The ID of the import image or import snapshot task to be canceled.
    :type ImportTaskId: string
    :param CancelReason: The reason for canceling the task.
    :type CancelReason: string
    """
    pass


def cancel_reserved_instances_listing(ReservedInstancesListingId=None):
    """
    :param ReservedInstancesListingId: [REQUIRED]
            The ID of the Reserved Instance listing.
            Return typedict
            ReturnsResponse Syntax{
              'ReservedInstancesListings': [
                {
                  'ReservedInstancesListingId': 'string',
                  'ReservedInstancesId': 'string',
                  'CreateDate': datetime(2015, 1, 1),
                  'UpdateDate': datetime(2015, 1, 1),
                  'Status': 'active'|'pending'|'cancelled'|'closed',
                  'StatusMessage': 'string',
                  'InstanceCounts': [
                    {
                      'State': 'available'|'sold'|'cancelled'|'pending',
                      'InstanceCount': 123
                    },
                  ],
                  'PriceSchedules': [
                    {
                      'Term': 123,
                      'Price': 123.0,
                      'CurrencyCode': 'USD',
                      'Active': True|False
                    },
                  ],
                  'Tags': [
                    {
                      'Key': 'string',
                      'Value': 'string'
                    },
                  ],
                  'ClientToken': 'string'
                },
              ]
            }
            Response Structure
            (dict) --Contains the output of CancelReservedInstancesListing.
            ReservedInstancesListings (list) --The Reserved Instance listing.
            (dict) --Describes a Reserved Instance listing.
            ReservedInstancesListingId (string) --The ID of the Reserved Instance listing.
            ReservedInstancesId (string) --The ID of the Reserved Instance.
            CreateDate (datetime) --The time the listing was created.
            UpdateDate (datetime) --The last modified timestamp of the listing.
            Status (string) --The status of the Reserved Instance listing.
            StatusMessage (string) --The reason for the current status of the Reserved Instance listing. The response can be blank.
            InstanceCounts (list) --The number of instances in this state.
            (dict) --Describes a Reserved Instance listing state.
            State (string) --The states of the listed Reserved Instances.
            InstanceCount (integer) --The number of listed Reserved Instances in the state specified by the state .
            
            PriceSchedules (list) --The price of the Reserved Instance listing.
            (dict) --Describes the price for a Reserved Instance.
            Term (integer) --The number of months remaining in the reservation. For example, 2 is the second to the last month before the capacity reservation expires.
            Price (float) --The fixed price for the term.
            CurrencyCode (string) --The currency for transacting the Reserved Instance resale. At this time, the only supported currency is USD .
            Active (boolean) --The current price schedule, as determined by the term remaining for the Reserved Instance in the listing.
            A specific price schedule is always in effect, but only one price schedule can be active at any time. Take, for example, a Reserved Instance listing that has five months remaining in its term. When you specify price schedules for five months and two months, this means that schedule 1, covering the first three months of the remaining term, will be active during months 5, 4, and 3. Then schedule 2, covering the last two months of the term, will be active for months 2 and 1.
            
            Tags (list) --Any tags assigned to the resource.
            (dict) --Describes a tag.
            Key (string) --The key of the tag.
            Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:
            Value (string) --The value of the tag.
            Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
            
            ClientToken (string) --A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see Ensuring Idempotency .
            
            
            
    :type ReservedInstancesListingId: string
    """
    pass


def cancel_spot_fleet_requests(DryRun=None, SpotFleetRequestIds=None, TerminateInstances=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SpotFleetRequestIds: [REQUIRED]
            The IDs of the Spot fleet requests.
            (string) --
            
    :type SpotFleetRequestIds: list
    :param TerminateInstances: [REQUIRED]
            Indicates whether to terminate instances for a Spot fleet request if it is canceled successfully.
            
    :type TerminateInstances: boolean
    """
    pass


def cancel_spot_instance_requests(DryRun=None, SpotInstanceRequestIds=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SpotInstanceRequestIds: [REQUIRED]
            One or more Spot instance request IDs.
            (string) --
            
    :type SpotInstanceRequestIds: list
    """
    pass


def confirm_product_instance(DryRun=None, ProductCode=None, InstanceId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ProductCode: [REQUIRED]
            The product code. This must be a product code that you own.
            
    :type ProductCode: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    """
    pass


def copy_image(DryRun=None, SourceRegion=None, SourceImageId=None, Name=None, Description=None, ClientToken=None,
               Encrypted=None, KmsKeyId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SourceRegion: [REQUIRED]
            The name of the region that contains the AMI to copy.
            
    :type SourceRegion: string
    :param SourceImageId: [REQUIRED]
            The ID of the AMI to copy.
            
    :type SourceImageId: string
    :param Name: [REQUIRED]
            The name of the new AMI in the destination region.
            
    :type Name: string
    :param Description: A description for the new AMI in the destination region.
    :type Description: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide .
    :type ClientToken: string
    :param Encrypted: Specifies whether the destination snapshots of the copied image should be encrypted. The default CMK for EBS is used unless a non-default AWS Key Management Service (AWS KMS) CMK is specified with KmsKeyId . For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .
    :type Encrypted: boolean
    :param KmsKeyId: The full ARN of the AWS Key Management Service (AWS KMS) CMK to use when encrypting the snapshots of an image during a copy operation. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. The ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1 :012345678910 :key/abcd1234-a123-456a-a12b-a123b4cd56ef . The specified CMK must exist in the region that the snapshot is being copied to. If a KmsKeyId is specified, the Encrypted flag must also be set.
    :type KmsKeyId: string
    """
    pass


def copy_snapshot(DryRun=None, SourceRegion=None, SourceSnapshotId=None, Description=None, DestinationRegion=None,
                  PresignedUrl=None, Encrypted=None, KmsKeyId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SourceRegion: [REQUIRED]
            The ID of the region that contains the snapshot to be copied.
            
    :type SourceRegion: string
    :param SourceSnapshotId: [REQUIRED]
            The ID of the EBS snapshot to copy.
            
    :type SourceSnapshotId: string
    :param Description: A description for the EBS snapshot.
    :type Description: string
    :param DestinationRegion: The destination region to use in the PresignedUrl parameter of a snapshot copy operation. This parameter is only valid for specifying the destination region in a PresignedUrl parameter, where it is required.
            Note
            CopySnapshot sends the snapshot copy to the regional endpoint that you send the HTTP request to, such as ec2.us-east-1.amazonaws.com (in the AWS CLI, this is specified with the --region parameter or the default region in your AWS configuration file).
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            
    :type DestinationRegion: string
    :param PresignedUrl: The pre-signed URL that facilitates copying an encrypted snapshot. This parameter is only required when copying an encrypted snapshot with the Amazon EC2 Query API; it is available as an optional parameter in all other cases. The PresignedUrl should use the snapshot source endpoint, the CopySnapshot action, and include the SourceRegion , SourceSnapshotId , and DestinationRegion parameters. The PresignedUrl must be signed using AWS Signature Version 4. Because EBS snapshots are stored in Amazon S3, the signing algorithm for this parameter uses the same logic that is described in Authenticating Requests by Using Query Parameters (AWS Signature Version 4) in the Amazon Simple Storage Service API Reference . An invalid or improperly signed PresignedUrl will cause the copy operation to fail asynchronously, and the snapshot will move to an error state.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            
    :type PresignedUrl: string
    :param Encrypted: Specifies whether the destination snapshot should be encrypted. You can encrypt a copy of an unencrypted snapshot using this flag, but you cannot use it to create an unencrypted copy from an encrypted snapshot. Your default CMK for EBS is used unless a non-default AWS Key Management Service (AWS KMS) CMK is specified with KmsKeyId . For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .
    :type Encrypted: boolean
    :param KmsKeyId: The full ARN of the AWS Key Management Service (AWS KMS) CMK to use when creating the snapshot copy. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. The ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1 :012345678910 :key/abcd1234-a123-456a-a12b-a123b4cd56ef . The specified CMK must exist in the region that the snapshot is being copied to. If a KmsKeyId is specified, the Encrypted flag must also be set.
    :type KmsKeyId: string
    """
    pass


def create_customer_gateway(DryRun=None, Type=None, PublicIp=None, BgpAsn=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Type: [REQUIRED]
            The type of VPN connection that this customer gateway supports (ipsec.1 ).
            
    :type Type: string
    :param PublicIp: [REQUIRED]
            The Internet-routable IP address for the customer gateway's outside interface. The address must be static.
            
    :type PublicIp: string
    :param BgpAsn: [REQUIRED]
            For devices that support BGP, the customer gateway's BGP ASN.
            Default: 65000
            
    :type BgpAsn: integer
    """
    pass


def create_dhcp_options(DryRun=None, DhcpConfigurations=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param DhcpConfigurations: [REQUIRED]
            A DHCP configuration option.
            (dict) --
            Key (string) --
            Values (list) --
            (string) --
            
            
    :type DhcpConfigurations: list
    """
    pass


def create_flow_logs(ResourceIds=None, ResourceType=None, TrafficType=None, LogGroupName=None,
                     DeliverLogsPermissionArn=None, ClientToken=None):
    """
    :param ResourceIds: [REQUIRED]
            One or more subnet, network interface, or VPC IDs.
            Constraints: Maximum of 1000 resources
            (string) --
            
    :type ResourceIds: list
    :param ResourceType: [REQUIRED]
            The type of resource on which to create the flow log.
            
    :type ResourceType: string
    :param TrafficType: [REQUIRED]
            The type of traffic to log.
            
    :type TrafficType: string
    :param LogGroupName: [REQUIRED]
            The name of the CloudWatch log group.
            
    :type LogGroupName: string
    :param DeliverLogsPermissionArn: [REQUIRED]
            The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group.
            
    :type DeliverLogsPermissionArn: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency .
    :type ClientToken: string
    """
    pass


def create_image(DryRun=None, InstanceId=None, Name=None, Description=None, NoReboot=None, BlockDeviceMappings=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param Name: [REQUIRED]
            A name for the new image.
            Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)
            
    :type Name: string
    :param Description: A description for the new image.
    :type Description: string
    :param NoReboot: By default, Amazon EC2 attempts to shut down and reboot the instance before creating the image. If the 'No Reboot' option is set, Amazon EC2 doesn't shut down the instance before creating the image. When this option is used, file system integrity on the created image can't be guaranteed.
    :type NoReboot: boolean
    :param BlockDeviceMappings: Information about one or more block device mappings.
            (dict) --Describes a block device mapping.
            VirtualName (string) --The virtual device name (ephemeral N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1 .The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
            Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
            DeviceName (string) --The device name exposed to the instance (for example, /dev/sdh or xvdh ).
            Ebs (dict) --Parameters used to automatically set up EBS volumes when the instance is launched.
            SnapshotId (string) --The ID of the snapshot.
            VolumeSize (integer) --The size of the volume, in GiB.
            Constraints: 1-16384 for General Purpose SSD (gp2 ), 4-16384 for Provisioned IOPS SSD (io1 ), 500-16384 for Throughput Optimized HDD (st1 ), 500-16384 for Cold HDD (sc1 ), and 1-1024 for Magnetic (standard ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
            Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
            DeleteOnTermination (boolean) --Indicates whether the EBS volume is deleted on instance termination.
            VolumeType (string) --The volume type: gp2 , io1 , st1 , sc1 , or standard .
            Default: standard
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports. For io1 , this represents the number of IOPS that are provisioned for the volume. For gp2 , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide .
            Constraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes.
            Condition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2 , st1 , sc1 , or standard volumes.
            Encrypted (boolean) --Indicates whether the EBS volume is encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption.
            NoDevice (string) --Suppresses the specified device included in the block device mapping of the AMI.
            
            
    :type BlockDeviceMappings: list
    """
    pass


def create_instance_export_task(Description=None, InstanceId=None, TargetEnvironment=None, ExportToS3Task=None):
    """
    :param Description: A description for the conversion task or the resource being exported. The maximum length is 255 bytes.
    :type Description: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param TargetEnvironment: The target virtualization environment.
    :type TargetEnvironment: string
    :param ExportToS3Task: The format and location for an instance export task.
            DiskImageFormat (string) --The format for the exported image.
            ContainerFormat (string) --The container format used to combine disk images with metadata (such as OVF). If absent, only the disk image is exported.
            S3Bucket (string) --The S3 bucket for the destination image. The destination bucket must exist and grant WRITE and READ_ACP permissions to the AWS account vm-import-export@amazon.com .
            S3Prefix (string) --The image is written to a single object in the S3 bucket at the S3 key s3prefix + exportTaskId + '.' + diskImageFormat.
            
    :type ExportToS3Task: dict
    """
    pass


def create_internet_gateway(DryRun=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
            Return typedict
            ReturnsResponse Syntax{
              'InternetGateway': {
                'InternetGatewayId': 'string',
                'Attachments': [
                  {
                    'VpcId': 'string',
                    'State': 'attaching'|'attached'|'detaching'|'detached'
                  },
                ],
                'Tags': [
                  {
                    'Key': 'string',
                    'Value': 'string'
                  },
                ]
              }
            }
            Response Structure
            (dict) --Contains the output of CreateInternetGateway.
            InternetGateway (dict) --Information about the Internet gateway.
            InternetGatewayId (string) --The ID of the Internet gateway.
            Attachments (list) --Any VPCs attached to the Internet gateway.
            (dict) --Describes the attachment of a VPC to an Internet gateway.
            VpcId (string) --The ID of the VPC.
            State (string) --The current state of the attachment.
            
            Tags (list) --Any tags assigned to the Internet gateway.
            (dict) --Describes a tag.
            Key (string) --The key of the tag.
            Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:
            Value (string) --The value of the tag.
            Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
            
            
            
            Examples
            This example creates an Internet gateway.
            response = client.create_internet_gateway(
            )
            print(response)
            Expected Output:
            {
              'InternetGateway': {
                'Attachments': [
                ],
                'InternetGatewayId': 'igw-c0a643a9',
                'Tags': [
                ],
              },
              'ResponseMetadata': {
                '...': '...',
              },
            }
            
    :type DryRun: boolean
    """
    pass


def create_key_pair(DryRun=None, KeyName=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param KeyName: [REQUIRED]
            A unique name for the key pair.
            Constraints: Up to 255 ASCII characters
            
    :type KeyName: string
    """
    pass


def create_nat_gateway(SubnetId=None, AllocationId=None, ClientToken=None):
    """
    :param SubnetId: [REQUIRED]
            The subnet in which to create the NAT gateway.
            
    :type SubnetId: string
    :param AllocationId: [REQUIRED]
            The allocation ID of an Elastic IP address to associate with the NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it.
            
    :type AllocationId: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency .
            Constraint: Maximum 64 ASCII characters.
            
    :type ClientToken: string
    """
    pass


def create_network_acl(DryRun=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def create_network_acl_entry(DryRun=None, NetworkAclId=None, RuleNumber=None, Protocol=None, RuleAction=None,
                             Egress=None, CidrBlock=None, IcmpTypeCode=None, PortRange=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkAclId: [REQUIRED]
            The ID of the network ACL.
            
    :type NetworkAclId: string
    :param RuleNumber: [REQUIRED]
            The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
            Constraints: Positive integer from 1 to 32766. The range 32767 to 65535 is reserved for internal use.
            
    :type RuleNumber: integer
    :param Protocol: [REQUIRED]
            The protocol. A value of -1 means all protocols.
            
    :type Protocol: string
    :param RuleAction: [REQUIRED]
            Indicates whether to allow or deny the traffic that matches the rule.
            
    :type RuleAction: string
    :param Egress: [REQUIRED]
            Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet).
            
    :type Egress: boolean
    :param CidrBlock: [REQUIRED]
            The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
            
    :type CidrBlock: string
    :param IcmpTypeCode: ICMP protocol: The ICMP type and code. Required if specifying ICMP for the protocol.
            Type (integer) --The ICMP code. A value of -1 means all codes for the specified ICMP type.
            Code (integer) --The ICMP type. A value of -1 means all types.
            
    :type IcmpTypeCode: dict
    :param PortRange: TCP or UDP protocols: The range of ports the rule applies to.
            From (integer) --The first port in the range.
            To (integer) --The last port in the range.
            
    :type PortRange: dict
    """
    pass


def create_network_interface(SubnetId=None, Description=None, PrivateIpAddress=None, Groups=None,
                             PrivateIpAddresses=None, SecondaryPrivateIpAddressCount=None, DryRun=None):
    """
    :param SubnetId: [REQUIRED]
            The ID of the subnet to associate with the network interface.
            
    :type SubnetId: string
    :param Description: A description for the network interface.
    :type Description: string
    :param PrivateIpAddress: The primary private IP address of the network interface. If you don't specify an IP address, Amazon EC2 selects one for you from the subnet range. If you specify an IP address, you cannot indicate any IP addresses specified in privateIpAddresses as primary (only one IP address can be designated as primary).
    :type PrivateIpAddress: string
    :param Groups: The IDs of one or more security groups.
            (string) --
            
    :type Groups: list
    :param PrivateIpAddresses: One or more private IP addresses.
            (dict) --Describes a secondary private IP address for a network interface.
            PrivateIpAddress (string) -- [REQUIRED]The private IP addresses.
            Primary (boolean) --Indicates whether the private IP address is the primary private IP address. Only one IP address can be designated as primary.
            
            
    :type PrivateIpAddresses: list
    :param SecondaryPrivateIpAddressCount: The number of secondary private IP addresses to assign to a network interface. When you specify a number of secondary IP addresses, Amazon EC2 selects these IP addresses within the subnet range. You can't specify this option and specify more than one private IP address using privateIpAddresses .
            The number of IP addresses you can assign to a network interface varies by instance type. For more information, see Private IP Addresses Per ENI Per Instance Type in the Amazon Elastic Compute Cloud User Guide .
            
    :type SecondaryPrivateIpAddressCount: integer
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    """
    pass


def create_placement_group(DryRun=None, GroupName=None, Strategy=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupName: [REQUIRED]
            A name for the placement group.
            Constraints: Up to 255 ASCII characters
            
    :type GroupName: string
    :param Strategy: [REQUIRED]
            The placement strategy.
            
    :type Strategy: string
    """
    pass


def create_reserved_instances_listing(ReservedInstancesId=None, InstanceCount=None, PriceSchedules=None,
                                      ClientToken=None):
    """
    :param ReservedInstancesId: [REQUIRED]
            The ID of the active Standard Reserved Instance.
            
    :type ReservedInstancesId: string
    :param InstanceCount: [REQUIRED]
            The number of instances that are a part of a Reserved Instance account to be listed in the Reserved Instance Marketplace. This number should be less than or equal to the instance count associated with the Reserved Instance ID specified in this call.
            
    :type InstanceCount: integer
    :param PriceSchedules: [REQUIRED]
            A list specifying the price of the Standard Reserved Instance for each month remaining in the Reserved Instance term.
            (dict) --Describes the price for a Reserved Instance.
            Term (integer) --The number of months remaining in the reservation. For example, 2 is the second to the last month before the capacity reservation expires.
            Price (float) --The fixed price for the term.
            CurrencyCode (string) --The currency for transacting the Reserved Instance resale. At this time, the only supported currency is USD .
            
            
    :type PriceSchedules: list
    :param ClientToken: [REQUIRED]
            Unique, case-sensitive identifier you provide to ensure idempotency of your listings. This helps avoid duplicate listings. For more information, see Ensuring Idempotency .
            
    :type ClientToken: string
    """
    pass


def create_route(DryRun=None, RouteTableId=None, DestinationCidrBlock=None, GatewayId=None, InstanceId=None,
                 NetworkInterfaceId=None, VpcPeeringConnectionId=None, NatGatewayId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param RouteTableId: [REQUIRED]
            The ID of the route table for the route.
            
    :type RouteTableId: string
    :param DestinationCidrBlock: [REQUIRED]
            The CIDR address block used for the destination match. Routing decisions are based on the most specific match.
            
    :type DestinationCidrBlock: string
    :param GatewayId: The ID of an Internet gateway or virtual private gateway attached to your VPC.
    :type GatewayId: string
    :param InstanceId: The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network interface is attached.
    :type InstanceId: string
    :param NetworkInterfaceId: The ID of a network interface.
    :type NetworkInterfaceId: string
    :param VpcPeeringConnectionId: The ID of a VPC peering connection.
    :type VpcPeeringConnectionId: string
    :param NatGatewayId: The ID of a NAT gateway.
    :type NatGatewayId: string
    """
    pass


def create_route_table(DryRun=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def create_security_group(DryRun=None, GroupName=None, Description=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupName: [REQUIRED]
            The name of the security group.
            Constraints: Up to 255 characters in length
            Constraints for EC2-Classic: ASCII characters
            Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
            
    :type GroupName: string
    :param Description: [REQUIRED]
            A description for the security group. This is informational only.
            Constraints: Up to 255 characters in length
            Constraints for EC2-Classic: ASCII characters
            Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
            
    :type Description: string
    :param VpcId: [EC2-VPC] The ID of the VPC. Required for EC2-VPC.
    :type VpcId: string
    """
    pass


def create_snapshot(DryRun=None, VolumeId=None, Description=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VolumeId: [REQUIRED]
            The ID of the EBS volume.
            
    :type VolumeId: string
    :param Description: A description for the snapshot.
    :type Description: string
    """
    pass


def create_spot_datafeed_subscription(DryRun=None, Bucket=None, Prefix=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Bucket: [REQUIRED]
            The Amazon S3 bucket in which to store the Spot instance data feed.
            
    :type Bucket: string
    :param Prefix: A prefix for the data feed file names.
    :type Prefix: string
    """
    pass


def create_subnet(DryRun=None, VpcId=None, CidrBlock=None, AvailabilityZone=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    :param CidrBlock: [REQUIRED]
            The network range for the subnet, in CIDR notation. For example, 10.0.0.0/24 .
            
    :type CidrBlock: string
    :param AvailabilityZone: The Availability Zone for the subnet.
            Default: AWS selects one for you. If you create more than one subnet in your VPC, we may not necessarily select a different zone for each subnet.
            
    :type AvailabilityZone: string
    """
    pass


def create_tags(DryRun=None, Resources=None, Tags=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Resources: [REQUIRED]
            The IDs of one or more resources to tag. For example, ami-1a2b3c4d.
            (string) --
            
    :type Resources: list
    :param Tags: [REQUIRED]
            One or more tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.
            (dict) --Describes a tag.
            Key (string) --The key of the tag.
            Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:
            Value (string) --The value of the tag.
            Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
            
            
    :type Tags: list
    """
    pass


def create_volume(DryRun=None, Size=None, SnapshotId=None, AvailabilityZone=None, VolumeType=None, Iops=None,
                  Encrypted=None, KmsKeyId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Size: The size of the volume, in GiBs.
            Constraints: 1-16384 for gp2 , 4-16384 for io1 , 500-16384 for st1 , 500-16384 for sc1 , and 1-1024 for standard . If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
            Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
            
    :type Size: integer
    :param SnapshotId: The snapshot from which to create the volume.
    :type SnapshotId: string
    :param AvailabilityZone: [REQUIRED]
            The Availability Zone in which to create the volume. Use DescribeAvailabilityZones to list the Availability Zones that are currently available to you.
            
    :type AvailabilityZone: string
    :param VolumeType: The volume type. This can be gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic volumes.
            Default: standard
            
    :type VolumeType: string
    :param Iops: Only valid for Provisioned IOPS SSD volumes. The number of I/O operations per second (IOPS) to provision for the volume, with a maximum ratio of 30 IOPS/GiB.
            Constraint: Range is 100 to 20000 for Provisioned IOPS SSD volumes
            
    :type Iops: integer
    :param Encrypted: Specifies whether the volume should be encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or vice versa. If your AMI uses encrypted volumes, you can only launch it on supported instance types. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .
    :type Encrypted: boolean
    :param KmsKeyId: The full ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. The ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1 :012345678910 :key/abcd1234-a123-456a-a12b-a123b4cd56ef . If a KmsKeyId is specified, the Encrypted flag must also be set.
    :type KmsKeyId: string
    """
    pass


def create_vpc(DryRun=None, CidrBlock=None, InstanceTenancy=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param CidrBlock: [REQUIRED]
            The network range for the VPC, in CIDR notation. For example, 10.0.0.0/16 .
            
    :type CidrBlock: string
    :param InstanceTenancy: The tenancy options for instances launched into the VPC. For default , instances are launched with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy VPC. For dedicated , instances are launched as dedicated tenancy instances by default. You can only launch instances with a tenancy of dedicated or host into a dedicated tenancy VPC.
            Important: The host value cannot be used with this parameter. Use the default or dedicated values only.
            Default: default
            
    :type InstanceTenancy: string
    """
    pass


def create_vpc_endpoint(DryRun=None, VpcId=None, ServiceName=None, PolicyDocument=None, RouteTableIds=None,
                        ClientToken=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcId: [REQUIRED]
            The ID of the VPC in which the endpoint will be used.
            
    :type VpcId: string
    :param ServiceName: [REQUIRED]
            The AWS service name, in the form ``com.amazonaws.*region* .*service* `` . To get a list of available services, use the DescribeVpcEndpointServices request.
            
    :type ServiceName: string
    :param PolicyDocument: A policy to attach to the endpoint that controls access to the service. The policy must be in valid JSON format. If this parameter is not specified, we attach a default policy that allows full access to the service.
    :type PolicyDocument: string
    :param RouteTableIds: One or more route table IDs.
            (string) --
            
    :type RouteTableIds: list
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency .
    :type ClientToken: string
    """
    pass


def create_vpc_peering_connection(DryRun=None, VpcId=None, PeerVpcId=None, PeerOwnerId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcId: The ID of the requester VPC.
    :type VpcId: string
    :param PeerVpcId: The ID of the VPC with which you are creating the VPC peering connection.
    :type PeerVpcId: string
    :param PeerOwnerId: The AWS account ID of the owner of the peer VPC.
            Default: Your AWS account ID
            
    :type PeerOwnerId: string
    """
    pass


def create_vpn_connection(DryRun=None, Type=None, CustomerGatewayId=None, VpnGatewayId=None, Options=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Type: [REQUIRED]
            The type of VPN connection (ipsec.1 ).
            
    :type Type: string
    :param CustomerGatewayId: [REQUIRED]
            The ID of the customer gateway.
            
    :type CustomerGatewayId: string
    :param VpnGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            
    :type VpnGatewayId: string
    :param Options: Indicates whether the VPN connection requires static routes. If you are creating a VPN connection for a device that does not support BGP, you must specify true .
            Default: false
            StaticRoutesOnly (boolean) --Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don't support BGP.
            
    :type Options: dict
    """
    pass


def create_vpn_connection_route(VpnConnectionId=None, DestinationCidrBlock=None):
    """
    :param VpnConnectionId: [REQUIRED]
            The ID of the VPN connection.
            
    :type VpnConnectionId: string
    :param DestinationCidrBlock: [REQUIRED]
            The CIDR block associated with the local subnet of the customer network.
            
    :type DestinationCidrBlock: string
    """
    pass


def create_vpn_gateway(DryRun=None, Type=None, AvailabilityZone=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Type: [REQUIRED]
            The type of VPN connection this virtual private gateway supports.
            
    :type Type: string
    :param AvailabilityZone: The Availability Zone for the virtual private gateway.
    :type AvailabilityZone: string
    """
    pass


def delete_customer_gateway(DryRun=None, CustomerGatewayId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param CustomerGatewayId: [REQUIRED]
            The ID of the customer gateway.
            
    :type CustomerGatewayId: string
    """
    pass


def delete_dhcp_options(DryRun=None, DhcpOptionsId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param DhcpOptionsId: [REQUIRED]
            The ID of the DHCP options set.
            
    :type DhcpOptionsId: string
    """
    pass


def delete_flow_logs(FlowLogIds=None):
    """
    :param FlowLogIds: [REQUIRED]
            One or more flow log IDs.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'Unsuccessful': [
                {
                  'Error': {
                    'Code': 'string',
                    'Message': 'string'
                  },
                  'ResourceId': 'string'
                },
              ]
            }
            Response Structure
            (dict) --Contains the output of DeleteFlowLogs.
            Unsuccessful (list) --Information about the flow logs that could not be deleted successfully.
            (dict) --Information about items that were not successfully processed in a batch call.
            Error (dict) --Information about the error.
            Code (string) --The error code.
            Message (string) --The error message accompanying the error code.
            ResourceId (string) --The ID of the resource.
            
            
            
    :type FlowLogIds: list
    """
    pass


def delete_internet_gateway(DryRun=None, InternetGatewayId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InternetGatewayId: [REQUIRED]
            The ID of the Internet gateway.
            
    :type InternetGatewayId: string
    """
    pass


def delete_key_pair(DryRun=None, KeyName=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param KeyName: [REQUIRED]
            The name of the key pair.
            
    :type KeyName: string
    """
    pass


def delete_nat_gateway(NatGatewayId=None):
    """
    :param NatGatewayId: [REQUIRED]
            The ID of the NAT gateway.
            Return typedict
            ReturnsResponse Syntax{
              'NatGatewayId': 'string'
            }
            Response Structure
            (dict) --Contains the output of DeleteNatGateway.
            NatGatewayId (string) --The ID of the NAT gateway.
            
            Examples
            This example deletes the specified NAT gateway.
            response = client.delete_nat_gateway(
              NatGatewayId='nat-04ae55e711cec5680',
            )
            print(response)
            Expected Output:
            {
              'NatGatewayId': 'nat-04ae55e711cec5680',
              'ResponseMetadata': {
                '...': '...',
              },
            }
            
    :type NatGatewayId: string
    """
    pass


def delete_network_acl(DryRun=None, NetworkAclId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkAclId: [REQUIRED]
            The ID of the network ACL.
            
    :type NetworkAclId: string
    """
    pass


def delete_network_acl_entry(DryRun=None, NetworkAclId=None, RuleNumber=None, Egress=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkAclId: [REQUIRED]
            The ID of the network ACL.
            
    :type NetworkAclId: string
    :param RuleNumber: [REQUIRED]
            The rule number of the entry to delete.
            
    :type RuleNumber: integer
    :param Egress: [REQUIRED]
            Indicates whether the rule is an egress rule.
            
    :type Egress: boolean
    """
    pass


def delete_network_interface(DryRun=None, NetworkInterfaceId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            
    :type NetworkInterfaceId: string
    """
    pass


def delete_placement_group(DryRun=None, GroupName=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupName: [REQUIRED]
            The name of the placement group.
            
    :type GroupName: string
    """
    pass


def delete_route(DryRun=None, RouteTableId=None, DestinationCidrBlock=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            
    :type RouteTableId: string
    :param DestinationCidrBlock: [REQUIRED]
            The CIDR range for the route. The value you specify must match the CIDR for the route exactly.
            
    :type DestinationCidrBlock: string
    """
    pass


def delete_route_table(DryRun=None, RouteTableId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            
    :type RouteTableId: string
    """
    pass


def delete_security_group(DryRun=None, GroupName=None, GroupId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupName: [EC2-Classic, default VPC] The name of the security group. You can specify either the security group name or the security group ID.
    :type GroupName: string
    :param GroupId: The ID of the security group. Required for a nondefault VPC.
    :type GroupId: string
    """
    pass


def delete_snapshot(DryRun=None, SnapshotId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SnapshotId: [REQUIRED]
            The ID of the EBS snapshot.
            
    :type SnapshotId: string
    """
    pass


def delete_spot_datafeed_subscription(DryRun=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
            ReturnsNone
            Examples
            This example deletes a Spot data feed subscription for the account.
            response = client.delete_spot_datafeed_subscription(
            )
            print(response)
            Expected Output:
            {
              'ResponseMetadata': {
                '...': '...',
              },
            }
            
    :type DryRun: boolean
    """
    pass


def delete_subnet(DryRun=None, SubnetId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SubnetId: [REQUIRED]
            The ID of the subnet.
            
    :type SubnetId: string
    """
    pass


def delete_tags(DryRun=None, Resources=None, Tags=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Resources: [REQUIRED]
            The ID of the resource. For example, ami-1a2b3c4d. You can specify more than one resource ID.
            (string) --
            
    :type Resources: list
    :param Tags: One or more tags to delete. If you omit the value parameter, we delete the tag regardless of its value. If you specify this parameter with an empty string as the value, we delete the key only if its value is an empty string.
            (dict) --Describes a tag.
            Key (string) --The key of the tag.
            Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:
            Value (string) --The value of the tag.
            Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
            
            
    :type Tags: list
    """
    pass


def delete_volume(DryRun=None, VolumeId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            
    :type VolumeId: string
    """
    pass


def delete_vpc(DryRun=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def delete_vpc_endpoints(DryRun=None, VpcEndpointIds=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcEndpointIds: [REQUIRED]
            One or more endpoint IDs.
            (string) --
            
    :type VpcEndpointIds: list
    """
    pass


def delete_vpc_peering_connection(DryRun=None, VpcPeeringConnectionId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcPeeringConnectionId: [REQUIRED]
            The ID of the VPC peering connection.
            
    :type VpcPeeringConnectionId: string
    """
    pass


def delete_vpn_connection(DryRun=None, VpnConnectionId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpnConnectionId: [REQUIRED]
            The ID of the VPN connection.
            
    :type VpnConnectionId: string
    """
    pass


def delete_vpn_connection_route(VpnConnectionId=None, DestinationCidrBlock=None):
    """
    :param VpnConnectionId: [REQUIRED]
            The ID of the VPN connection.
            
    :type VpnConnectionId: string
    :param DestinationCidrBlock: [REQUIRED]
            The CIDR block associated with the local subnet of the customer network.
            
    :type DestinationCidrBlock: string
    """
    pass


def delete_vpn_gateway(DryRun=None, VpnGatewayId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpnGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            
    :type VpnGatewayId: string
    """
    pass


def deregister_image(DryRun=None, ImageId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImageId: [REQUIRED]
            The ID of the AMI.
            
    :type ImageId: string
    """
    pass


def describe_account_attributes(DryRun=None, AttributeNames=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param AttributeNames: One or more account attribute names.
            (string) --
            
    :type AttributeNames: list
    """
    pass


def describe_addresses(DryRun=None, PublicIps=None, Filters=None, AllocationIds=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param PublicIps: [EC2-Classic] One or more Elastic IP addresses.
            Default: Describes all your Elastic IP addresses.
            (string) --
            
    :type PublicIps: list
    :param Filters: One or more filters. Filter names and values are case-sensitive.
            allocation-id - [EC2-VPC] The allocation ID for the address.
            association-id - [EC2-VPC] The association ID for the address.
            domain - Indicates whether the address is for use in EC2-Classic (standard ) or in a VPC (vpc ).
            instance-id - The ID of the instance the address is associated with, if any.
            network-interface-id - [EC2-VPC] The ID of the network interface that the address is associated with, if any.
            network-interface-owner-id - The AWS account ID of the owner.
            private-ip-address - [EC2-VPC] The private IP address associated with the Elastic IP address.
            public-ip - The Elastic IP address.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param AllocationIds: [EC2-VPC] One or more allocation IDs.
            Default: Describes all your Elastic IP addresses.
            (string) --
            
    :type AllocationIds: list
    """
    pass


def describe_availability_zones(DryRun=None, ZoneNames=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ZoneNames: The names of one or more Availability Zones.
            (string) --
            
    :type ZoneNames: list
    :param Filters: One or more filters.
            message - Information about the Availability Zone.
            region-name - The name of the region for the Availability Zone (for example, us-east-1 ).
            state - The state of the Availability Zone (available | information | impaired | unavailable ).
            zone-name - The name of the Availability Zone (for example, us-east-1a ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_bundle_tasks(DryRun=None, BundleIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param BundleIds: One or more bundle task IDs.
            Default: Describes all your bundle tasks.
            (string) --
            
    :type BundleIds: list
    :param Filters: One or more filters.
            bundle-id - The ID of the bundle task.
            error-code - If the task failed, the error code returned.
            error-message - If the task failed, the error message returned.
            instance-id - The ID of the instance.
            progress - The level of task completion, as a percentage (for example, 20%).
            s3-bucket - The Amazon S3 bucket to store the AMI.
            s3-prefix - The beginning of the AMI name.
            start-time - The time the task started (for example, 2013-09-15T17:15:20.000Z).
            state - The state of the task (pending | waiting-for-shutdown | bundling | storing | cancelling | complete | failed ).
            update-time - The time of the most recent update for the task.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_classic_link_instances(DryRun=None, InstanceIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceIds: One or more instance IDs. Must be instances linked to a VPC through ClassicLink.
            (string) --
            
    :type InstanceIds: list
    :param Filters: One or more filters.
            group-id - The ID of a VPC security group that's associated with the instance.
            instance-id - The ID of the instance.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC that the instance is linked to.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param NextToken: The token to retrieve the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. You cannot specify this parameter and the instance IDs parameter in the same request.
            Constraint: If the value is greater than 1000, we return only 1000 items.
            
    :type MaxResults: integer
    """
    pass


def describe_conversion_tasks(DryRun=None, ConversionTaskIds=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ConversionTaskIds: One or more conversion task IDs.
            (string) --
            
    :type ConversionTaskIds: list
    """
    pass


def describe_customer_gateways(DryRun=None, CustomerGatewayIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param CustomerGatewayIds: One or more customer gateway IDs.
            Default: Describes all your customer gateways.
            (string) --
            
    :type CustomerGatewayIds: list
    :param Filters: One or more filters.
            bgp-asn - The customer gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
            customer-gateway-id - The ID of the customer gateway.
            ip-address - The IP address of the customer gateway's Internet-routable external interface.
            state - The state of the customer gateway (pending | available | deleting | deleted ).
            type - The type of customer gateway. Currently, the only supported type is ipsec.1 .
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_dhcp_options(DryRun=None, DhcpOptionsIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param DhcpOptionsIds: The IDs of one or more DHCP options sets.
            Default: Describes all your DHCP options sets.
            (string) --
            
    :type DhcpOptionsIds: list
    :param Filters: One or more filters.
            dhcp-options-id - The ID of a set of DHCP options.
            key - The key for one of the options (for example, domain-name ).
            value - The value for one of the options.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_export_tasks(ExportTaskIds=None):
    """
    :param ExportTaskIds: One or more export task IDs.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'ExportTasks': [
                {
                  'ExportTaskId': 'string',
                  'Description': 'string',
                  'State': 'active'|'cancelling'|'cancelled'|'completed',
                  'StatusMessage': 'string',
                  'InstanceExportDetails': {
                    'InstanceId': 'string',
                    'TargetEnvironment': 'citrix'|'vmware'|'microsoft'
                  },
                  'ExportToS3Task': {
                    'DiskImageFormat': 'VMDK'|'RAW'|'VHD',
                    'ContainerFormat': 'ova',
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                  }
                },
              ]
            }
            Response Structure
            (dict) --Contains the output for DescribeExportTasks.
            ExportTasks (list) --Information about the export tasks.
            (dict) --Describes an instance export task.
            ExportTaskId (string) --The ID of the export task.
            Description (string) --A description of the resource being exported.
            State (string) --The state of the export task.
            StatusMessage (string) --The status message related to the export task.
            InstanceExportDetails (dict) --Information about the instance to export.
            InstanceId (string) --The ID of the resource being exported.
            TargetEnvironment (string) --The target virtualization environment.
            ExportToS3Task (dict) --Information about the export task.
            DiskImageFormat (string) --The format for the exported image.
            ContainerFormat (string) --The container format used to combine disk images with metadata (such as OVF). If absent, only the disk image is exported.
            S3Bucket (string) --The S3 bucket for the destination image. The destination bucket must exist and grant WRITE and READ_ACP permissions to the AWS account vm-import-export@amazon.com .
            S3Key (string) --The encryption key for your S3 bucket.
            
            
            
            
    :type ExportTaskIds: list
    """
    pass


def describe_flow_logs(FlowLogIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    :param FlowLogIds: One or more flow log IDs.
            (string) --
            
    :type FlowLogIds: list
    :param Filters: One or more filters.
            deliver-log-status - The status of the logs delivery (SUCCESS | FAILED ).
            flow-log-id - The ID of the flow log.
            log-group-name - The name of the log group.
            resource-id - The ID of the VPC, subnet, or network interface.
            traffic-type - The type of traffic (ACCEPT | REJECT | ALL )
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param NextToken: The token to retrieve the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. You cannot specify this parameter and the flow log IDs parameter in the same request.
    :type MaxResults: integer
    """
    pass


def describe_host_reservation_offerings(OfferingId=None, MinDuration=None, MaxDuration=None, Filters=None,
                                        MaxResults=None, NextToken=None):
    """
    :param OfferingId: The ID of the reservation offering.
    :type OfferingId: string
    :param MinDuration: This is the minimum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 31536000 for one year.
    :type MinDuration: integer
    :param MaxDuration: This is the maximum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 94608000 for three years.
    :type MaxDuration: integer
    :param Filters: One or more filters.
            instance-family - The instance family of the offering (e.g., m4 ).
            payment-option - The payment option (No Upfront | Partial Upfront | All Upfront ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned nextToken value. This value can be between 5 and 500; if maxResults is given a larger value than 500, you will receive an error.
    :type MaxResults: integer
    :param NextToken: The token to use to retrieve the next page of results.
    :type NextToken: string
    """
    pass


def describe_host_reservations(HostReservationIdSet=None, Filters=None, MaxResults=None, NextToken=None):
    """
    :param HostReservationIdSet: One or more host reservation IDs.
            (string) --
            
    :type HostReservationIdSet: list
    :param Filters: One or more filters.
            instance-family - The instance family (e.g., m4 ).
            payment-option - The payment option (No Upfront | Partial Upfront | All Upfront ).
            state - The state of the reservation (payment-pending | payment-failed | active | retired ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned nextToken value. This value can be between 5 and 500; if maxResults is given a larger value than 500, you will receive an error.
    :type MaxResults: integer
    :param NextToken: The token to use to retrieve the next page of results.
    :type NextToken: string
    """
    pass


def describe_hosts(HostIds=None, NextToken=None, MaxResults=None, Filters=None):
    """
    :param HostIds: The IDs of the Dedicated Hosts. The IDs are used for targeted instance launches.
            (string) --
            
    :type HostIds: list
    :param NextToken: The token to retrieve the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned nextToken value. This value can be between 5 and 500; if maxResults is given a larger value than 500, you will receive an error. You cannot specify this parameter and the host IDs parameter in the same request.
    :type MaxResults: integer
    :param Filters: One or more filters.
            instance-type - The instance type size that the Dedicated Host is configured to support.
            auto-placement - Whether auto-placement is enabled or disabled (on | off ).
            host-reservation-id - The ID of the reservation assigned to this host.
            client-token - The idempotency token you provided when you launched the instance
            state - The allocation state of the Dedicated Host (available | under-assessment | permanent-failure | released | released-permanent-failure ).
            availability-zone - The Availability Zone of the host.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_id_format(Resource=None):
    """
    :param Resource: The type of resource: instance | reservation | snapshot | volume
            Return typedict
            ReturnsResponse Syntax{
              'Statuses': [
                {
                  'Resource': 'string',
                  'UseLongIds': True|False,
                  'Deadline': datetime(2015, 1, 1)
                },
              ]
            }
            Response Structure
            (dict) --Contains the output of DescribeIdFormat.
            Statuses (list) --Information about the ID format for the resource.
            (dict) --Describes the ID format for a resource.
            Resource (string) --The type of resource.
            UseLongIds (boolean) --Indicates whether longer IDs (17-character IDs) are enabled for the resource.
            Deadline (datetime) --The date in UTC at which you are permanently switched over to using longer IDs. If a deadline is not yet available for this resource type, this field is not returned.
            
            
            
    :type Resource: string
    """
    pass


def describe_identity_id_format(Resource=None, PrincipalArn=None):
    """
    :param Resource: The type of resource: instance | reservation | snapshot | volume
    :type Resource: string
    :param PrincipalArn: [REQUIRED]
            The ARN of the principal, which can be an IAM role, IAM user, or the root user.
            
    :type PrincipalArn: string
    """
    pass


def describe_image_attribute(DryRun=None, ImageId=None, Attribute=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImageId: [REQUIRED]
            The ID of the AMI.
            
    :type ImageId: string
    :param Attribute: [REQUIRED]
            The AMI attribute.
            Note : Depending on your account privileges, the blockDeviceMapping attribute may return a Client.AuthFailure error. If this happens, use DescribeImages to get information about the block device mapping for the AMI.
            
    :type Attribute: string
    """
    pass


def describe_images(DryRun=None, ImageIds=None, Owners=None, ExecutableUsers=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImageIds: One or more image IDs.
            Default: Describes all images available to you.
            (string) --
            
    :type ImageIds: list
    :param Owners: Filters the images by the owner. Specify an AWS account ID, self (owner is the sender of the request), or an AWS owner alias (valid values are amazon | aws-marketplace | microsoft ). Omitting this option returns all images for which you have launch permissions, regardless of ownership.
            (string) --
            
    :type Owners: list
    :param ExecutableUsers: Scopes the images by users with explicit launch permissions. Specify an AWS account ID, self (the sender of the request), or all (public AMIs).
            (string) --
            
    :type ExecutableUsers: list
    :param Filters: One or more filters.
            architecture - The image architecture (i386 | x86_64 ).
            block-device-mapping.delete-on-termination - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination.
            block-device-mapping.device-name - The device name for the EBS volume (for example, /dev/sdh ).
            block-device-mapping.snapshot-id - The ID of the snapshot used for the EBS volume.
            block-device-mapping.volume-size - The volume size of the EBS volume, in GiB.
            block-device-mapping.volume-type - The volume type of the EBS volume (gp2 | io1 | st1 | sc1 | standard ).
            description - The description of the image (provided during image creation).
            hypervisor - The hypervisor type (ovm | xen ).
            image-id - The ID of the image.
            image-type - The image type (machine | kernel | ramdisk ).
            is-public - A Boolean that indicates whether the image is public.
            kernel-id - The kernel ID.
            manifest-location - The location of the image manifest.
            name - The name of the AMI (provided during image creation).
            owner-alias - String value from an Amazon-maintained list (amazon | aws-marketplace | microsoft ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console.
            owner-id - The AWS account ID of the image owner.
            platform - The platform. To only list Windows-based AMIs, use windows .
            product-code - The product code.
            product-code.type - The type of the product code (devpay | marketplace ).
            ramdisk-id - The RAM disk ID.
            root-device-name - The name of the root device volume (for example, /dev/sda1 ).
            root-device-type - The type of the root device volume (ebs | instance-store ).
            state - The state of the image (available | pending | failed ).
            state-reason-code - The reason code for the state change.
            state-reason-message - The message for the state change.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            virtualization-type - The virtualization type (paravirtual | hvm ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_import_image_tasks(DryRun=None, ImportTaskIds=None, NextToken=None, MaxResults=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImportTaskIds: A list of import image task IDs.
            (string) --
            
    :type ImportTaskIds: list
    :param NextToken: A token that indicates the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.
    :type MaxResults: integer
    :param Filters: Filter tasks using the task-state filter and one of the following values: active, completed, deleting, deleted.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_import_snapshot_tasks(DryRun=None, ImportTaskIds=None, NextToken=None, MaxResults=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImportTaskIds: A list of import snapshot task IDs.
            (string) --
            
    :type ImportTaskIds: list
    :param NextToken: A token that indicates the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.
    :type MaxResults: integer
    :param Filters: One or more filters.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_instance_attribute(DryRun=None, InstanceId=None, Attribute=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param Attribute: [REQUIRED]
            The instance attribute.
            Note: The enaSupport attribute is not supported at this time.
            
    :type Attribute: string
    """
    pass


def describe_instance_status(DryRun=None, InstanceIds=None, Filters=None, NextToken=None, MaxResults=None,
                             IncludeAllInstances=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceIds: One or more instance IDs.
            Default: Describes all your instances.
            Constraints: Maximum 100 explicitly specified instance IDs.
            (string) --
            
    :type InstanceIds: list
    :param Filters: One or more filters.
            availability-zone - The Availability Zone of the instance.
            event.code - The code for the scheduled event (instance-reboot | system-reboot | system-maintenance | instance-retirement | instance-stop ).
            event.description - A description of the event.
            event.not-after - The latest end time for the scheduled event (for example, 2014-09-15T17:15:20.000Z ).
            event.not-before - The earliest start time for the scheduled event (for example, 2014-09-15T17:15:20.000Z ).
            instance-state-code - The code for the instance state, as a 16-bit unsigned integer. The high byte is an opaque internal value and should be ignored. The low byte is set based on the state represented. The valid values are 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped).
            instance-state-name - The state of the instance (pending | running | shutting-down | terminated | stopping | stopped ).
            instance-status.reachability - Filters on instance status where the name is reachability (passed | failed | initializing | insufficient-data ).
            instance-status.status - The status of the instance (ok | impaired | initializing | insufficient-data | not-applicable ).
            system-status.reachability - Filters on system status where the name is reachability (passed | failed | initializing | insufficient-data ).
            system-status.status - The system status of the instance (ok | impaired | initializing | insufficient-data | not-applicable ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param NextToken: The token to retrieve the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
    :type MaxResults: integer
    :param IncludeAllInstances: When true , includes the health status for all instances. When false , includes the health status for running instances only.
            Default: false
            
    :type IncludeAllInstances: boolean
    """
    pass


def describe_instances(DryRun=None, InstanceIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceIds: One or more instance IDs.
            Default: Describes all your instances.
            (string) --
            
    :type InstanceIds: list
    :param Filters: One or more filters.
            affinity - The affinity setting for an instance running on a Dedicated Host (default | host ).
            architecture - The instance architecture (i386 | x86_64 ).
            availability-zone - The Availability Zone of the instance.
            block-device-mapping.attach-time - The attach time for an EBS volume mapped to the instance, for example, 2010-09-15T17:15:20.000Z .
            block-device-mapping.delete-on-termination - A Boolean that indicates whether the EBS volume is deleted on instance termination.
            block-device-mapping.device-name - The device name for the EBS volume (for example, /dev/sdh or xvdh ).
            block-device-mapping.status - The status for the EBS volume (attaching | attached | detaching | detached ).
            block-device-mapping.volume-id - The volume ID of the EBS volume.
            client-token - The idempotency token you provided when you launched the instance.
            dns-name - The public DNS name of the instance.
            group-id - The ID of the security group for the instance. EC2-Classic only.
            group-name - The name of the security group for the instance. EC2-Classic only.
            host-id - The ID of the Dedicated Host on which the instance is running, if applicable.
            hypervisor - The hypervisor type of the instance (ovm | xen ).
            iam-instance-profile.arn - The instance profile associated with the instance. Specified as an ARN.
            image-id - The ID of the image used to launch the instance.
            instance-id - The ID of the instance.
            instance-lifecycle - Indicates whether this is a Spot Instance or a Scheduled Instance (spot | scheduled ).
            instance-state-code - The state of the instance, as a 16-bit unsigned integer. The high byte is an opaque internal value and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped).
            instance-state-name - The state of the instance (pending | running | shutting-down | terminated | stopping | stopped ).
            instance-type - The type of instance (for example, t2.micro ).
            instance.group-id - The ID of the security group for the instance.
            instance.group-name - The name of the security group for the instance.
            ip-address - The public IP address of the instance.
            kernel-id - The kernel ID.
            key-name - The name of the key pair used when the instance was launched.
            launch-index - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).
            launch-time - The time when the instance was launched.
            monitoring-state - Indicates whether monitoring is enabled for the instance (disabled | enabled ).
            owner-id - The AWS account ID of the instance owner.
            placement-group-name - The name of the placement group for the instance.
            platform - The platform. Use windows if you have Windows instances; otherwise, leave blank.
            private-dns-name - The private DNS name of the instance.
            private-ip-address - The private IP address of the instance.
            product-code - The product code associated with the AMI used to launch the instance.
            product-code.type - The type of product code (devpay | marketplace ).
            ramdisk-id - The RAM disk ID.
            reason - The reason for the current state of the instance (for example, shows 'User Initiated [date]' when you stop or terminate the instance). Similar to the state-reason-code filter.
            requester-id - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on).
            reservation-id - The ID of the instance's reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you'll get one reservation ID. If you launch ten instances using the same launch request, you'll also get one reservation ID.
            root-device-name - The name of the root device for the instance (for example, /dev/sda1 or /dev/xvda ).
            root-device-type - The type of root device that the instance uses (ebs | instance-store ).
            source-dest-check - Indicates whether the instance performs source/destination checking. A value of true means that checking is enabled, and false means checking is disabled. The value must be false for the instance to perform network address translation (NAT) in your VPC.
            spot-instance-request-id - The ID of the Spot instance request.
            state-reason-code - The reason code for the state change.
            state-reason-message - A message that describes the state change.
            subnet-id - The ID of the subnet for the instance.
            tag :key =*value* - The key/value combination of a tag assigned to the resource, where tag :key is the tag's key.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            tenancy - The tenancy of an instance (dedicated | default | host ).
            virtualization-type - The virtualization type of the instance (paravirtual | hvm ).
            vpc-id - The ID of the VPC that the instance is running in.
            network-interface.description - The description of the network interface.
            network-interface.subnet-id - The ID of the subnet for the network interface.
            network-interface.vpc-id - The ID of the VPC for the network interface.
            network-interface.network-interface-id - The ID of the network interface.
            network-interface.owner-id - The ID of the owner of the network interface.
            network-interface.availability-zone - The Availability Zone for the network interface.
            network-interface.requester-id - The requester ID for the network interface.
            network-interface.requester-managed - Indicates whether the network interface is being managed by AWS.
            network-interface.status - The status of the network interface (available ) | in-use ).
            network-interface.mac-address - The MAC address of the network interface.
            network-interface.private-dns-name - The private DNS name of the network interface.
            network-interface.source-dest-check - Whether the network interface performs source/destination checking. A value of true means checking is enabled, and false means checking is disabled. The value must be false for the network interface to perform network address translation (NAT) in your VPC.
            network-interface.group-id - The ID of a security group associated with the network interface.
            network-interface.group-name - The name of a security group associated with the network interface.
            network-interface.attachment.attachment-id - The ID of the interface attachment.
            network-interface.attachment.instance-id - The ID of the instance to which the network interface is attached.
            network-interface.attachment.instance-owner-id - The owner ID of the instance to which the network interface is attached.
            network-interface.addresses.private-ip-address - The private IP address associated with the network interface.
            network-interface.attachment.device-index - The device index to which the network interface is attached.
            network-interface.attachment.status - The status of the attachment (attaching | attached | detaching | detached ).
            network-interface.attachment.attach-time - The time that the network interface was attached to an instance.
            network-interface.attachment.delete-on-termination - Specifies whether the attachment is deleted when an instance is terminated.
            network-interface.addresses.primary - Specifies whether the IP address of the network interface is the primary private IP address.
            network-interface.addresses.association.public-ip - The ID of the association of an Elastic IP address with a network interface.
            network-interface.addresses.association.ip-owner-id - The owner ID of the private IP address associated with the network interface.
            association.public-ip - The address of the Elastic IP address bound to the network interface.
            association.ip-owner-id - The owner of the Elastic IP address associated with the network interface.
            association.allocation-id - The allocation ID returned when you allocated the Elastic IP address for your network interface.
            association.association-id - The association ID returned when the network interface was associated with an IP address.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param NextToken: The token to request the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter or tag filters in the same call.
    :type MaxResults: integer
    """
    pass


def describe_internet_gateways(DryRun=None, InternetGatewayIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InternetGatewayIds: One or more Internet gateway IDs.
            Default: Describes all your Internet gateways.
            (string) --
            
    :type InternetGatewayIds: list
    :param Filters: One or more filters.
            attachment.state - The current state of the attachment between the gateway and the VPC (available ). Present only if a VPC is attached.
            attachment.vpc-id - The ID of an attached VPC.
            internet-gateway-id - The ID of the Internet gateway.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_key_pairs(DryRun=None, KeyNames=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param KeyNames: One or more key pair names.
            Default: Describes all your key pairs.
            (string) --
            
    :type KeyNames: list
    :param Filters: One or more filters.
            fingerprint - The fingerprint of the key pair.
            key-name - The name of the key pair.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_moving_addresses(DryRun=None, PublicIps=None, NextToken=None, Filters=None, MaxResults=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param PublicIps: One or more Elastic IP addresses.
            (string) --
            
    :type PublicIps: list
    :param NextToken: The token to use to retrieve the next page of results.
    :type NextToken: string
    :param Filters: One or more filters.
            moving-status - The status of the Elastic IP address (MovingToVpc | RestoringToClassic ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value outside of this range, an error is returned.
            Default: If no value is provided, the default is 1000.
            
    :type MaxResults: integer
    """
    pass


def describe_nat_gateways(NatGatewayIds=None, Filters=None, MaxResults=None, NextToken=None):
    """
    :param NatGatewayIds: One or more NAT gateway IDs.
            (string) --
            
    :type NatGatewayIds: list
    :param Filters: One or more filters.
            nat-gateway-id - The ID of the NAT gateway.
            state - The state of the NAT gateway (pending | failed | available | deleting | deleted ).
            subnet-id - The ID of the subnet in which the NAT gateway resides.
            vpc-id - The ID of the VPC in which the NAT gateway resides.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
            Constraint: If the value specified is greater than 1000, we return only 1000 items.
            
    :type MaxResults: integer
    :param NextToken: The token to retrieve the next page of results.
    :type NextToken: string
    """
    pass


def describe_network_acls(DryRun=None, NetworkAclIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkAclIds: One or more network ACL IDs.
            Default: Describes all your network ACLs.
            (string) --
            
    :type NetworkAclIds: list
    :param Filters: One or more filters.
            association.association-id - The ID of an association ID for the ACL.
            association.network-acl-id - The ID of the network ACL involved in the association.
            association.subnet-id - The ID of the subnet involved in the association.
            default - Indicates whether the ACL is the default network ACL for the VPC.
            entry.cidr - The CIDR range specified in the entry.
            entry.egress - Indicates whether the entry applies to egress traffic.
            entry.icmp.code - The ICMP code specified in the entry, if any.
            entry.icmp.type - The ICMP type specified in the entry, if any.
            entry.port-range.from - The start of the port range specified in the entry.
            entry.port-range.to - The end of the port range specified in the entry.
            entry.protocol - The protocol specified in the entry (tcp | udp | icmp or a protocol number).
            entry.rule-action - Allows or denies the matching traffic (allow | deny ).
            entry.rule-number - The number of an entry (in other words, rule) in the ACL's set of entries.
            network-acl-id - The ID of the network ACL.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC for the network ACL.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_network_interface_attribute(DryRun=None, NetworkInterfaceId=None, Attribute=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            
    :type NetworkInterfaceId: string
    :param Attribute: The attribute of the network interface.
    :type Attribute: string
    """
    pass


def describe_network_interfaces(DryRun=None, NetworkInterfaceIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkInterfaceIds: One or more network interface IDs.
            Default: Describes all your network interfaces.
            (string) --
            
    :type NetworkInterfaceIds: list
    :param Filters: One or more filters.
            addresses.private-ip-address - The private IP addresses associated with the network interface.
            addresses.primary - Whether the private IP address is the primary IP address associated with the network interface.
            addresses.association.public-ip - The association ID returned when the network interface was associated with the Elastic IP address.
            addresses.association.owner-id - The owner ID of the addresses associated with the network interface.
            association.association-id - The association ID returned when the network interface was associated with an IP address.
            association.allocation-id - The allocation ID returned when you allocated the Elastic IP address for your network interface.
            association.ip-owner-id - The owner of the Elastic IP address associated with the network interface.
            association.public-ip - The address of the Elastic IP address bound to the network interface.
            association.public-dns-name - The public DNS name for the network interface.
            attachment.attachment-id - The ID of the interface attachment.
            attachment.attach.time - The time that the network interface was attached to an instance.
            attachment.delete-on-termination - Indicates whether the attachment is deleted when an instance is terminated.
            attachment.device-index - The device index to which the network interface is attached.
            attachment.instance-id - The ID of the instance to which the network interface is attached.
            attachment.instance-owner-id - The owner ID of the instance to which the network interface is attached.
            attachment.nat-gateway-id - The ID of the NAT gateway to which the network interface is attached.
            attachment.status - The status of the attachment (attaching | attached | detaching | detached ).
            availability-zone - The Availability Zone of the network interface.
            description - The description of the network interface.
            group-id - The ID of a security group associated with the network interface.
            group-name - The name of a security group associated with the network interface.
            mac-address - The MAC address of the network interface.
            network-interface-id - The ID of the network interface.
            owner-id - The AWS account ID of the network interface owner.
            private-ip-address - The private IP address or addresses of the network interface.
            private-dns-name - The private DNS name of the network interface.
            requester-id - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on).
            requester-managed - Indicates whether the network interface is being managed by an AWS service (for example, AWS Management Console, Auto Scaling, and so on).
            source-desk-check - Indicates whether the network interface performs source/destination checking. A value of true means checking is enabled, and false means checking is disabled. The value must be false for the network interface to perform network address translation (NAT) in your VPC.
            status - The status of the network interface. If the network interface is not attached to an instance, the status is available ; if a network interface is attached to an instance the status is in-use .
            subnet-id - The ID of the subnet for the network interface.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC for the network interface.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_placement_groups(DryRun=None, GroupNames=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupNames: One or more placement group names.
            Default: Describes all your placement groups, or only those otherwise specified.
            (string) --
            
    :type GroupNames: list
    :param Filters: One or more filters.
            group-name - The name of the placement group.
            state - The state of the placement group (pending | available | deleting | deleted ).
            strategy - The strategy of the placement group (cluster ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_prefix_lists(DryRun=None, PrefixListIds=None, Filters=None, MaxResults=None, NextToken=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param PrefixListIds: One or more prefix list IDs.
            (string) --
            
    :type PrefixListIds: list
    :param Filters: One or more filters.
            prefix-list-id : The ID of a prefix list.
            prefix-list-name : The name of a prefix list.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
            Constraint: If the value specified is greater than 1000, we return only 1000 items.
            
    :type MaxResults: integer
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)
    :type NextToken: string
    """
    pass


def describe_regions(DryRun=None, RegionNames=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param RegionNames: The names of one or more regions.
            (string) --
            
    :type RegionNames: list
    :param Filters: One or more filters.
            endpoint - The endpoint of the region (for example, ec2.us-east-1.amazonaws.com ).
            region-name - The name of the region (for example, us-east-1 ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_reserved_instances(DryRun=None, ReservedInstancesIds=None, Filters=None, OfferingType=None,
                                OfferingClass=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ReservedInstancesIds: One or more Reserved Instance IDs.
            Default: Describes all your Reserved Instances, or only those otherwise specified.
            (string) --
            
    :type ReservedInstancesIds: list
    :param Filters: One or more filters.
            availability-zone - The Availability Zone where the Reserved Instance can be used.
            duration - The duration of the Reserved Instance (one year or three years), in seconds (31536000 | 94608000 ).
            end - The time when the Reserved Instance expires (for example, 2015-08-07T11:54:42.000Z).
            fixed-price - The purchase price of the Reserved Instance (for example, 9800.0).
            instance-type - The instance type that is covered by the reservation.
            scope - The scope of the Reserved Instance (Region or Availability Zone ).
            product-description - The Reserved Instance product platform description. Instances that include (Amazon VPC) in the product platform description will only be displayed to EC2-Classic account holders and are for use with Amazon VPC (Linux/UNIX | Linux/UNIX (Amazon VPC) | SUSE Linux | SUSE Linux (Amazon VPC) | Red Hat Enterprise Linux | Red Hat Enterprise Linux (Amazon VPC) | Windows | Windows (Amazon VPC) | Windows with SQL Server Standard | Windows with SQL Server Standard (Amazon VPC) | Windows with SQL Server Web | Windows with SQL Server Web (Amazon VPC) | Windows with SQL Server Enterprise | Windows with SQL Server Enterprise (Amazon VPC) ).
            reserved-instances-id - The ID of the Reserved Instance.
            start - The time at which the Reserved Instance purchase request was placed (for example, 2014-08-07T11:54:42.000Z).
            state - The state of the Reserved Instance (payment-pending | active | payment-failed | retired ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            usage-price - The usage price of the Reserved Instance, per hour (for example, 0.84).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param OfferingType: The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the Medium Utilization Reserved Instance offering type.
    :type OfferingType: string
    :param OfferingClass: Describes whether the Reserved Instance is Standard or Convertible.
    :type OfferingClass: string
    """
    pass


def describe_reserved_instances_listings(ReservedInstancesId=None, ReservedInstancesListingId=None, Filters=None):
    """
    :param ReservedInstancesId: One or more Reserved Instance IDs.
    :type ReservedInstancesId: string
    :param ReservedInstancesListingId: One or more Reserved Instance listing IDs.
    :type ReservedInstancesListingId: string
    :param Filters: One or more filters.
            reserved-instances-id - The ID of the Reserved Instances.
            reserved-instances-listing-id - The ID of the Reserved Instances listing.
            status - The status of the Reserved Instance listing (pending | active | cancelled | closed ).
            status-message - The reason for the status.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_reserved_instances_modifications(ReservedInstancesModificationIds=None, NextToken=None, Filters=None):
    """
    :param ReservedInstancesModificationIds: IDs for the submitted modification request.
            (string) --
            
    :type ReservedInstancesModificationIds: list
    :param NextToken: The token to retrieve the next page of results.
    :type NextToken: string
    :param Filters: One or more filters.
            client-token - The idempotency token for the modification request.
            create-date - The time when the modification request was created.
            effective-date - The time when the modification becomes effective.
            modification-result.reserved-instances-id - The ID for the Reserved Instances created as part of the modification request. This ID is only available when the status of the modification is fulfilled .
            modification-result.target-configuration.availability-zone - The Availability Zone for the new Reserved Instances.
            modification-result.target-configuration.instance-count - The number of new Reserved Instances.
            modification-result.target-configuration.instance-type - The instance type of the new Reserved Instances.
            modification-result.target-configuration.platform - The network platform of the new Reserved Instances (EC2-Classic | EC2-VPC ).
            reserved-instances-id - The ID of the Reserved Instances modified.
            reserved-instances-modification-id - The ID of the modification request.
            status - The status of the Reserved Instances modification request (processing | fulfilled | failed ).
            status-message - The reason for the status.
            update-date - The time when the modification request was last updated.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_reserved_instances_offerings(DryRun=None, ReservedInstancesOfferingIds=None, InstanceType=None,
                                          AvailabilityZone=None, ProductDescription=None, Filters=None,
                                          InstanceTenancy=None, OfferingType=None, NextToken=None, MaxResults=None,
                                          IncludeMarketplace=None, MinDuration=None, MaxDuration=None,
                                          MaxInstanceCount=None, OfferingClass=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ReservedInstancesOfferingIds: One or more Reserved Instances offering IDs.
            (string) --
            
    :type ReservedInstancesOfferingIds: list
    :param InstanceType: The instance type that the reservation will cover (for example, m1.small ). For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide .
    :type InstanceType: string
    :param AvailabilityZone: The Availability Zone in which the Reserved Instance can be used.
    :type AvailabilityZone: string
    :param ProductDescription: The Reserved Instance product platform description. Instances that include (Amazon VPC) in the description are for use with Amazon VPC.
    :type ProductDescription: string
    :param Filters: One or more filters.
            availability-zone - The Availability Zone where the Reserved Instance can be used.
            duration - The duration of the Reserved Instance (for example, one year or three years), in seconds (31536000 | 94608000 ).
            fixed-price - The purchase price of the Reserved Instance (for example, 9800.0).
            instance-type - The instance type that is covered by the reservation.
            marketplace - Set to true to show only Reserved Instance Marketplace offerings. When this filter is not used, which is the default behavior, all offerings from both AWS and the Reserved Instance Marketplace are listed.
            product-description - The Reserved Instance product platform description. Instances that include (Amazon VPC) in the product platform description will only be displayed to EC2-Classic account holders and are for use with Amazon VPC. (Linux/UNIX | Linux/UNIX (Amazon VPC) | SUSE Linux | SUSE Linux (Amazon VPC) | Red Hat Enterprise Linux | Red Hat Enterprise Linux (Amazon VPC) | Windows | Windows (Amazon VPC) | Windows with SQL Server Standard | Windows with SQL Server Standard (Amazon VPC) | Windows with SQL Server Web | Windows with SQL Server Web (Amazon VPC) | Windows with SQL Server Enterprise | Windows with SQL Server Enterprise (Amazon VPC) )
            reserved-instances-offering-id - The Reserved Instances offering ID.
            scope - The scope of the Reserved Instance (Availability Zone or Region ).
            usage-price - The usage price of the Reserved Instance, per hour (for example, 0.84).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param InstanceTenancy: The tenancy of the instances covered by the reservation. A Reserved Instance with a tenancy of dedicated is applied to instances that run in a VPC on single-tenant hardware (i.e., Dedicated Instances).
            Default: default
            
    :type InstanceTenancy: string
    :param OfferingType: The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the Medium Utilization Reserved Instance offering type.
    :type OfferingType: string
    :param NextToken: The token to retrieve the next page of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. The maximum is 100.
            Default: 100
            
    :type MaxResults: integer
    :param IncludeMarketplace: Include Reserved Instance Marketplace offerings in the response.
    :type IncludeMarketplace: boolean
    :param MinDuration: The minimum duration (in seconds) to filter when searching for offerings.
            Default: 2592000 (1 month)
            
    :type MinDuration: integer
    :param MaxDuration: The maximum duration (in seconds) to filter when searching for offerings.
            Default: 94608000 (3 years)
            
    :type MaxDuration: integer
    :param MaxInstanceCount: The maximum number of instances to filter when searching for offerings.
            Default: 20
            
    :type MaxInstanceCount: integer
    :param OfferingClass: The offering class of the Reserved Instance. Can be standard or convertible .
    :type OfferingClass: string
    """
    pass


def describe_route_tables(DryRun=None, RouteTableIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param RouteTableIds: One or more route table IDs.
            Default: Describes all your route tables.
            (string) --
            
    :type RouteTableIds: list
    :param Filters: One or more filters.
            association.route-table-association-id - The ID of an association ID for the route table.
            association.route-table-id - The ID of the route table involved in the association.
            association.subnet-id - The ID of the subnet involved in the association.
            association.main - Indicates whether the route table is the main route table for the VPC (true | false ).
            route-table-id - The ID of the route table.
            route.destination-cidr-block - The CIDR range specified in a route in the table.
            route.destination-prefix-list-id - The ID (prefix) of the AWS service specified in a route in the table.
            route.gateway-id - The ID of a gateway specified in a route in the table.
            route.instance-id - The ID of an instance specified in a route in the table.
            route.nat-gateway-id - The ID of a NAT gateway.
            route.origin - Describes how the route was created. CreateRouteTable indicates that the route was automatically created when the route table was created; CreateRoute indicates that the route was manually added to the route table; EnableVgwRoutePropagation indicates that the route was propagated by route propagation.
            route.state - The state of a route in the route table (active | blackhole ). The blackhole state indicates that the route's target isn't available (for example, the specified gateway isn't attached to the VPC, the specified NAT instance has been terminated, and so on).
            route.vpc-peering-connection-id - The ID of a VPC peering connection specified in a route in the table.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC for the route table.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_scheduled_instance_availability(DryRun=None, Recurrence=None, FirstSlotStartTimeRange=None,
                                             MinSlotDurationInHours=None, MaxSlotDurationInHours=None, NextToken=None,
                                             MaxResults=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Recurrence: [REQUIRED]
            The schedule recurrence.
            Frequency (string) --The frequency (Daily , Weekly , or Monthly ).
            Interval (integer) --The interval quantity. The interval unit depends on the value of Frequency . For example, every 2 weeks or every 2 months.
            OccurrenceDays (list) --The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday). You can't specify this value with a daily schedule. If the occurrence is relative to the end of the month, you can specify only a single day.
            (integer) --
            OccurrenceRelativeToEnd (boolean) --Indicates whether the occurrence is relative to the end of the specified week or month. You can't specify this value with a daily schedule.
            OccurrenceUnit (string) --The unit for OccurrenceDays (DayOfWeek or DayOfMonth ). This value is required for a monthly schedule. You can't specify DayOfWeek with a weekly schedule. You can't specify this value with a daily schedule.
            
    :type Recurrence: dict
    :param FirstSlotStartTimeRange: [REQUIRED]
            The time period for the first schedule to start.
            EarliestTime (datetime) -- [REQUIRED]The earliest date and time, in UTC, for the Scheduled Instance to start.
            LatestTime (datetime) -- [REQUIRED]The latest date and time, in UTC, for the Scheduled Instance to start. This value must be later than or equal to the earliest date and at most three months in the future.
            
    :type FirstSlotStartTimeRange: dict
    :param MinSlotDurationInHours: The minimum available duration, in hours. The minimum required duration is 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours.
    :type MinSlotDurationInHours: integer
    :param MaxSlotDurationInHours: The maximum available duration, in hours. This value must be greater than MinSlotDurationInHours and less than 1,720.
    :type MaxSlotDurationInHours: integer
    :param NextToken: The token for the next set of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 300. To retrieve the remaining results, make another call with the returned NextToken value.
    :type MaxResults: integer
    :param Filters: One or more filters.
            availability-zone - The Availability Zone (for example, us-west-2a ).
            instance-type - The instance type (for example, c4.large ).
            network-platform - The network platform (EC2-Classic or EC2-VPC ).
            platform - The platform (Linux/UNIX or Windows ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_scheduled_instances(DryRun=None, ScheduledInstanceIds=None, SlotStartTimeRange=None, NextToken=None,
                                 MaxResults=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ScheduledInstanceIds: One or more Scheduled Instance IDs.
            (string) --
            
    :type ScheduledInstanceIds: list
    :param SlotStartTimeRange: The time period for the first schedule to start.
            EarliestTime (datetime) --The earliest date and time, in UTC, for the Scheduled Instance to start.
            LatestTime (datetime) --The latest date and time, in UTC, for the Scheduled Instance to start.
            
    :type SlotStartTimeRange: dict
    :param NextToken: The token for the next set of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 100. To retrieve the remaining results, make another call with the returned NextToken value.
    :type MaxResults: integer
    :param Filters: One or more filters.
            availability-zone - The Availability Zone (for example, us-west-2a ).
            instance-type - The instance type (for example, c4.large ).
            network-platform - The network platform (EC2-Classic or EC2-VPC ).
            platform - The platform (Linux/UNIX or Windows ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_security_group_references(DryRun=None, GroupId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.
    :type DryRun: boolean
    :param GroupId: [REQUIRED]
            One or more security group IDs in your account.
            (string) --
            
    :type GroupId: list
    """
    pass


def describe_security_groups(DryRun=None, GroupNames=None, GroupIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupNames: [EC2-Classic and default VPC only] One or more security group names. You can specify either the security group name or the security group ID. For security groups in a nondefault VPC, use the group-name filter to describe security groups by name.
            Default: Describes all your security groups.
            (string) --
            
    :type GroupNames: list
    :param GroupIds: One or more security group IDs. Required for security groups in a nondefault VPC.
            Default: Describes all your security groups.
            (string) --
            
    :type GroupIds: list
    :param Filters: One or more filters. If using multiple filters for rules, the results include security groups for which any combination of rules - not necessarily a single rule - match all filters.
            description - The description of the security group.
            egress.ip-permission.prefix-list-id - The ID (prefix) of the AWS service to which the security group allows access.
            group-id - The ID of the security group.
            group-name - The name of the security group.
            ip-permission.cidr - A CIDR range that has been granted permission.
            ip-permission.from-port - The start of port range for the TCP and UDP protocols, or an ICMP type number.
            ip-permission.group-id - The ID of a security group that has been granted permission.
            ip-permission.group-name - The name of a security group that has been granted permission.
            ip-permission.protocol - The IP protocol for the permission (tcp | udp | icmp or a protocol number).
            ip-permission.to-port - The end of port range for the TCP and UDP protocols, or an ICMP code.
            ip-permission.user-id - The ID of an AWS account that has been granted permission.
            owner-id - The AWS account ID of the owner of the security group.
            tag-key - The key of a tag assigned to the security group.
            tag-value - The value of a tag assigned to the security group.
            vpc-id - The ID of the VPC specified when the security group was created.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_snapshot_attribute(DryRun=None, SnapshotId=None, Attribute=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SnapshotId: [REQUIRED]
            The ID of the EBS snapshot.
            
    :type SnapshotId: string
    :param Attribute: [REQUIRED]
            The snapshot attribute you would like to view.
            
    :type Attribute: string
    """
    pass


def describe_snapshots(DryRun=None, SnapshotIds=None, OwnerIds=None, RestorableByUserIds=None, Filters=None,
                       NextToken=None, MaxResults=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SnapshotIds: One or more snapshot IDs.
            Default: Describes snapshots for which you have launch permissions.
            (string) --
            
    :type SnapshotIds: list
    :param OwnerIds: Returns the snapshots owned by the specified owner. Multiple owners can be specified.
            (string) --
            
    :type OwnerIds: list
    :param RestorableByUserIds: One or more AWS accounts IDs that can create volumes from the snapshot.
            (string) --
            
    :type RestorableByUserIds: list
    :param Filters: One or more filters.
            description - A description of the snapshot.
            owner-alias - Value from an Amazon-maintained list (amazon | aws-marketplace | microsoft ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM consolew.
            owner-id - The ID of the AWS account that owns the snapshot.
            progress - The progress of the snapshot, as a percentage (for example, 80%).
            snapshot-id - The snapshot ID.
            start-time - The time stamp when the snapshot was initiated.
            status - The status of the snapshot (pending | completed | error ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            volume-id - The ID of the volume the snapshot is for.
            volume-size - The size of the volume, in GiB.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param NextToken: The NextToken value returned from a previous paginated DescribeSnapshots request where MaxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.
    :type NextToken: string
    :param MaxResults: The maximum number of snapshot results returned by DescribeSnapshots in paginated output. When this parameter is used, DescribeSnapshots only returns MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another DescribeSnapshots request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then DescribeSnapshots returns all results. You cannot specify this parameter and the snapshot IDs parameter in the same request.
    :type MaxResults: integer
    """
    pass


def describe_spot_datafeed_subscription(DryRun=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
            Return typedict
            ReturnsResponse Syntax{
              'SpotDatafeedSubscription': {
                'OwnerId': 'string',
                'Bucket': 'string',
                'Prefix': 'string',
                'State': 'Active'|'Inactive',
                'Fault': {
                  'Code': 'string',
                  'Message': 'string'
                }
              }
            }
            Response Structure
            (dict) --Contains the output of DescribeSpotDatafeedSubscription.
            SpotDatafeedSubscription (dict) --The Spot instance data feed subscription.
            OwnerId (string) --The AWS account ID of the account.
            Bucket (string) --The Amazon S3 bucket where the Spot instance data feed is located.
            Prefix (string) --The prefix that is prepended to data feed files.
            State (string) --The state of the Spot instance data feed subscription.
            Fault (dict) --The fault codes for the Spot instance request, if any.
            Code (string) --The reason code for the Spot instance state change.
            Message (string) --The message for the Spot instance state change.
            
            
            Examples
            This example describes the Spot Instance datafeed subscription for your AWS account.
            response = client.describe_spot_datafeed_subscription(
            )
            print(response)
            Expected Output:
            {
              'SpotDatafeedSubscription': {
                'Bucket': 'my-s3-bucket',
                'OwnerId': '123456789012',
                'Prefix': 'spotdata',
                'State': 'Active',
              },
              'ResponseMetadata': {
                '...': '...',
              },
            }
            
    :type DryRun: boolean
    """
    pass


def describe_spot_fleet_instances(DryRun=None, SpotFleetRequestId=None, NextToken=None, MaxResults=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SpotFleetRequestId: [REQUIRED]
            The ID of the Spot fleet request.
            
    :type SpotFleetRequestId: string
    :param NextToken: The token for the next set of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.
    :type MaxResults: integer
    """
    pass


def describe_spot_fleet_request_history(DryRun=None, SpotFleetRequestId=None, EventType=None, StartTime=None,
                                        NextToken=None, MaxResults=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SpotFleetRequestId: [REQUIRED]
            The ID of the Spot fleet request.
            
    :type SpotFleetRequestId: string
    :param EventType: The type of events to describe. By default, all events are described.
    :type EventType: string
    :param StartTime: [REQUIRED]
            The starting date and time for the events, in UTC format (for example, YYYY -MM -DD T*HH* :MM :SS Z).
            
    :type StartTime: datetime
    :param NextToken: The token for the next set of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.
    :type MaxResults: integer
    """
    pass


def describe_spot_fleet_requests(DryRun=None, SpotFleetRequestIds=None, NextToken=None, MaxResults=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SpotFleetRequestIds: The IDs of the Spot fleet requests.
            (string) --
            
    :type SpotFleetRequestIds: list
    :param NextToken: The token for the next set of results.
    :type NextToken: string
    :param MaxResults: The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.
    :type MaxResults: integer
    """
    pass


def describe_spot_instance_requests(DryRun=None, SpotInstanceRequestIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SpotInstanceRequestIds: One or more Spot instance request IDs.
            (string) --
            
    :type SpotInstanceRequestIds: list
    :param Filters: One or more filters.
            availability-zone-group - The Availability Zone group.
            create-time - The time stamp when the Spot instance request was created.
            fault-code - The fault code related to the request.
            fault-message - The fault message related to the request.
            instance-id - The ID of the instance that fulfilled the request.
            launch-group - The Spot instance launch group.
            launch.block-device-mapping.delete-on-termination - Indicates whether the Amazon EBS volume is deleted on instance termination.
            launch.block-device-mapping.device-name - The device name for the Amazon EBS volume (for example, /dev/sdh ).
            launch.block-device-mapping.snapshot-id - The ID of the snapshot used for the Amazon EBS volume.
            launch.block-device-mapping.volume-size - The size of the Amazon EBS volume, in GiB.
            launch.block-device-mapping.volume-type - The type of the Amazon EBS volume: gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic.
            launch.group-id - The security group for the instance.
            launch.image-id - The ID of the AMI.
            launch.instance-type - The type of instance (for example, m3.medium ).
            launch.kernel-id - The kernel ID.
            launch.key-name - The name of the key pair the instance launched with.
            launch.monitoring-enabled - Whether monitoring is enabled for the Spot instance.
            launch.ramdisk-id - The RAM disk ID.
            network-interface.network-interface-id - The ID of the network interface.
            network-interface.device-index - The index of the device for the network interface attachment on the instance.
            network-interface.subnet-id - The ID of the subnet for the instance.
            network-interface.description - A description of the network interface.
            network-interface.private-ip-address - The primary private IP address of the network interface.
            network-interface.delete-on-termination - Indicates whether the network interface is deleted when the instance is terminated.
            network-interface.group-id - The ID of the security group associated with the network interface.
            network-interface.group-name - The name of the security group associated with the network interface.
            network-interface.addresses.primary - Indicates whether the IP address is the primary private IP address.
            product-description - The product description associated with the instance (Linux/UNIX | Windows ).
            spot-instance-request-id - The Spot instance request ID.
            spot-price - The maximum hourly price for any Spot instance launched to fulfill the request.
            state - The state of the Spot instance request (open | active | closed | cancelled | failed ). Spot bid status information can help you track your Amazon EC2 Spot instance requests. For more information, see Spot Bid Status in the Amazon Elastic Compute Cloud User Guide.
            status-code - The short code describing the most recent evaluation of your Spot instance request.
            status-message - The message explaining the status of the Spot instance request.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            type - The type of Spot instance request (one-time | persistent ).
            launched-availability-zone - The Availability Zone in which the bid is launched.
            valid-from - The start date of the request.
            valid-until - The end date of the request.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_spot_price_history(DryRun=None, StartTime=None, EndTime=None, InstanceTypes=None, ProductDescriptions=None,
                                Filters=None, AvailabilityZone=None, MaxResults=None, NextToken=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param StartTime: The date and time, up to the past 90 days, from which to start retrieving the price history data, in UTC format (for example, YYYY -MM -DD T*HH* :MM :SS Z).
    :type StartTime: datetime
    :param EndTime: The date and time, up to the current date, from which to stop retrieving the price history data, in UTC format (for example, YYYY -MM -DD T*HH* :MM :SS Z).
    :type EndTime: datetime
    :param InstanceTypes: Filters the results by the specified instance types.
            (string) --
            
    :type InstanceTypes: list
    :param ProductDescriptions: Filters the results by the specified basic product descriptions.
            (string) --
            
    :type ProductDescriptions: list
    :param Filters: One or more filters.
            availability-zone - The Availability Zone for which prices should be returned.
            instance-type - The type of instance (for example, m3.medium ).
            product-description - The product description for the Spot price (Linux/UNIX | SUSE Linux | Windows | Linux/UNIX (Amazon VPC) | SUSE Linux (Amazon VPC) | Windows (Amazon VPC) ).
            spot-price - The Spot price. The value must match exactly (or use wildcards; greater than or less than comparison is not supported).
            timestamp - The timestamp of the Spot price history, in UTC format (for example, YYYY -MM -DD T*HH* :MM :SS Z). You can use wildcards (* and ?). Greater than or less than comparison is not supported.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param AvailabilityZone: Filters the results by the specified Availability Zone.
    :type AvailabilityZone: string
    :param MaxResults: The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.
    :type MaxResults: integer
    :param NextToken: The token for the next set of results.
    :type NextToken: string
    """
    pass


def describe_stale_security_groups(DryRun=None, VpcId=None, MaxResults=None, NextToken=None):
    """
    :param DryRun: Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.
    :type DryRun: boolean
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
    :type MaxResults: integer
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)
    :type NextToken: string
    """
    pass


def describe_subnets(DryRun=None, SubnetIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SubnetIds: One or more subnet IDs.
            Default: Describes all your subnets.
            (string) --
            
    :type SubnetIds: list
    :param Filters: One or more filters.
            availabilityZone - The Availability Zone for the subnet. You can also use availability-zone as the filter name.
            available-ip-address-count - The number of IP addresses in the subnet that are available.
            cidrBlock - The CIDR block of the subnet. The CIDR block you specify must exactly match the subnet's CIDR block for information to be returned for the subnet. You can also use cidr or cidr-block as the filter names.
            defaultForAz - Indicates whether this is the default subnet for the Availability Zone. You can also use default-for-az as the filter name.
            state - The state of the subnet (pending | available ).
            subnet-id - The ID of the subnet.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC for the subnet.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_tags(DryRun=None, Filters=None, MaxResults=None, NextToken=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Filters: One or more filters.
            key - The tag key.
            resource-id - The resource ID.
            resource-type - The resource type (customer-gateway | dhcp-options | image | instance | internet-gateway | network-acl | network-interface | reserved-instances | route-table | security-group | snapshot | spot-instances-request | subnet | volume | vpc | vpn-connection | vpn-gateway ).
            value - The tag value.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param MaxResults: The maximum number of results to return in a single call. This value can be between 5 and 1000. To retrieve the remaining results, make another call with the returned NextToken value.
    :type MaxResults: integer
    :param NextToken: The token to retrieve the next page of results.
    :type NextToken: string
    """
    pass


def describe_volume_attribute(DryRun=None, VolumeId=None, Attribute=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            
    :type VolumeId: string
    :param Attribute: The instance attribute.
    :type Attribute: string
    """
    pass


def describe_volume_status(DryRun=None, VolumeIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VolumeIds: One or more volume IDs.
            Default: Describes all your volumes.
            (string) --
            
    :type VolumeIds: list
    :param Filters: One or more filters.
            action.code - The action code for the event (for example, enable-volume-io ).
            action.description - A description of the action.
            action.event-id - The event ID associated with the action.
            availability-zone - The Availability Zone of the instance.
            event.description - A description of the event.
            event.event-id - The event ID.
            event.event-type - The event type (for io-enabled : passed | failed ; for io-performance : io-performance:degraded | io-performance:severely-degraded | io-performance:stalled ).
            event.not-after - The latest end time for the event.
            event.not-before - The earliest start time for the event.
            volume-status.details-name - The cause for volume-status.status (io-enabled | io-performance ).
            volume-status.details-status - The status of volume-status.details-name (for io-enabled : passed | failed ; for io-performance : normal | degraded | severely-degraded | stalled ).
            volume-status.status - The status of the volume (ok | impaired | warning | insufficient-data ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param NextToken: The NextToken value to include in a future DescribeVolumeStatus request. When the results of the request exceed MaxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.
    :type NextToken: string
    :param MaxResults: The maximum number of volume results returned by DescribeVolumeStatus in paginated output. When this parameter is used, the request only returns MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then DescribeVolumeStatus returns all results. You cannot specify this parameter and the volume IDs parameter in the same request.
    :type MaxResults: integer
    """
    pass


def describe_volumes(DryRun=None, VolumeIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VolumeIds: One or more volume IDs.
            (string) --
            
    :type VolumeIds: list
    :param Filters: One or more filters.
            attachment.attach-time - The time stamp when the attachment initiated.
            attachment.delete-on-termination - Whether the volume is deleted on instance termination.
            attachment.device - The device name that is exposed to the instance (for example, /dev/sda1 ).
            attachment.instance-id - The ID of the instance the volume is attached to.
            attachment.status - The attachment state (attaching | attached | detaching | detached ).
            availability-zone - The Availability Zone in which the volume was created.
            create-time - The time stamp when the volume was created.
            encrypted - The encryption status of the volume.
            size - The size of the volume, in GiB.
            snapshot-id - The snapshot from which the volume was created.
            status - The status of the volume (creating | available | in-use | deleting | deleted | error ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            volume-id - The volume ID.
            volume-type - The Amazon EBS volume type. This can be gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic volumes.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param NextToken: The NextToken value returned from a previous paginated DescribeVolumes request where MaxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.
    :type NextToken: string
    :param MaxResults: The maximum number of volume results returned by DescribeVolumes in paginated output. When this parameter is used, DescribeVolumes only returns MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another DescribeVolumes request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then DescribeVolumes returns all results. You cannot specify this parameter and the volume IDs parameter in the same request.
    :type MaxResults: integer
    """
    pass


def describe_vpc_attribute(DryRun=None, VpcId=None, Attribute=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    :param Attribute: [REQUIRED]
            The VPC attribute.
            
    :type Attribute: string
    """
    pass


def describe_vpc_classic_link(DryRun=None, VpcIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcIds: One or more VPCs for which you want to describe the ClassicLink status.
            (string) --
            
    :type VpcIds: list
    :param Filters: One or more filters.
            is-classic-link-enabled - Whether the VPC is enabled for ClassicLink (true | false ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_vpc_classic_link_dns_support(VpcIds=None, MaxResults=None, NextToken=None):
    """
    :param VpcIds: One or more VPC IDs.
            (string) --
            
    :type VpcIds: list
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
    :type MaxResults: integer
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)
    :type NextToken: string
    """
    pass


def describe_vpc_endpoint_services(DryRun=None, MaxResults=None, NextToken=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
            Constraint: If the value is greater than 1000, we return only 1000 items.
            
    :type MaxResults: integer
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)
    :type NextToken: string
    """
    pass


def describe_vpc_endpoints(DryRun=None, VpcEndpointIds=None, Filters=None, MaxResults=None, NextToken=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcEndpointIds: One or more endpoint IDs.
            (string) --
            
    :type VpcEndpointIds: list
    :param Filters: One or more filters.
            service-name : The name of the AWS service.
            vpc-id : The ID of the VPC in which the endpoint resides.
            vpc-endpoint-id : The ID of the endpoint.
            vpc-endpoint-state : The state of the endpoint. (pending | available | deleting | deleted )
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
            Constraint: If the value is greater than 1000, we return only 1000 items.
            
    :type MaxResults: integer
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)
    :type NextToken: string
    """
    pass


def describe_vpc_peering_connections(DryRun=None, VpcPeeringConnectionIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcPeeringConnectionIds: One or more VPC peering connection IDs.
            Default: Describes all your VPC peering connections.
            (string) --
            
    :type VpcPeeringConnectionIds: list
    :param Filters: One or more filters.
            accepter-vpc-info.cidr-block - The CIDR block of the peer VPC.
            accepter-vpc-info.owner-id - The AWS account ID of the owner of the peer VPC.
            accepter-vpc-info.vpc-id - The ID of the peer VPC.
            expiration-time - The expiration date and time for the VPC peering connection.
            requester-vpc-info.cidr-block - The CIDR block of the requester's VPC.
            requester-vpc-info.owner-id - The AWS account ID of the owner of the requester VPC.
            requester-vpc-info.vpc-id - The ID of the requester VPC.
            status-code - The status of the VPC peering connection (pending-acceptance | failed | expired | provisioning | active | deleted | rejected ).
            status-message - A message that provides more information about the status of the VPC peering connection, if applicable.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-peering-connection-id - The ID of the VPC peering connection.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_vpcs(DryRun=None, VpcIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcIds: One or more VPC IDs.
            Default: Describes all your VPCs.
            (string) --
            
    :type VpcIds: list
    :param Filters: One or more filters.
            cidr - The CIDR block of the VPC. The CIDR block you specify must exactly match the VPC's CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, /28 ).
            dhcp-options-id - The ID of a set of DHCP options.
            isDefault - Indicates whether the VPC is the default VPC.
            state - The state of the VPC (pending | available ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_vpn_connections(DryRun=None, VpnConnectionIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpnConnectionIds: One or more VPN connection IDs.
            Default: Describes your VPN connections.
            (string) --
            
    :type VpnConnectionIds: list
    :param Filters: One or more filters.
            customer-gateway-configuration - The configuration information for the customer gateway.
            customer-gateway-id - The ID of a customer gateway associated with the VPN connection.
            state - The state of the VPN connection (pending | available | deleting | deleted ).
            option.static-routes-only - Indicates whether the connection has static routes only. Used for devices that do not support Border Gateway Protocol (BGP).
            route.destination-cidr-block - The destination CIDR block. This corresponds to the subnet used in a customer data center.
            bgp-asn - The BGP Autonomous System Number (ASN) associated with a BGP device.
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            type - The type of VPN connection. Currently the only supported type is ipsec.1 .
            vpn-connection-id - The ID of the VPN connection.
            vpn-gateway-id - The ID of a virtual private gateway associated with the VPN connection.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def describe_vpn_gateways(DryRun=None, VpnGatewayIds=None, Filters=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpnGatewayIds: One or more virtual private gateway IDs.
            Default: Describes all your virtual private gateways.
            (string) --
            
    :type VpnGatewayIds: list
    :param Filters: One or more filters.
            attachment.state - The current state of the attachment between the gateway and the VPC (attaching | attached | detaching | detached ).
            attachment.vpc-id - The ID of an attached VPC.
            availability-zone - The Availability Zone for the virtual private gateway (if applicable).
            state - The state of the virtual private gateway (pending | available | deleting | deleted ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            type - The type of virtual private gateway. Currently the only supported type is ipsec.1 .
            vpn-gateway-id - The ID of the virtual private gateway.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            
    :type Filters: list
    """
    pass


def detach_classic_link_vpc(DryRun=None, InstanceId=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of the instance to unlink from the VPC.
            
    :type InstanceId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC to which the instance is linked.
            
    :type VpcId: string
    """
    pass


def detach_internet_gateway(DryRun=None, InternetGatewayId=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InternetGatewayId: [REQUIRED]
            The ID of the Internet gateway.
            
    :type InternetGatewayId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def detach_network_interface(DryRun=None, AttachmentId=None, Force=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param AttachmentId: [REQUIRED]
            The ID of the attachment.
            
    :type AttachmentId: string
    :param Force: Specifies whether to force a detachment.
    :type Force: boolean
    """
    pass


def detach_volume(DryRun=None, VolumeId=None, InstanceId=None, Device=None, Force=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            
    :type VolumeId: string
    :param InstanceId: The ID of the instance.
    :type InstanceId: string
    :param Device: The device name.
    :type Device: string
    :param Force: Forces detachment if the previous detachment attempt did not occur cleanly (for example, logging into an instance, unmounting the volume, and detaching normally). This option can lead to data loss or a corrupted file system. Use this option only as a last resort to detach a volume from a failed instance. The instance won't have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures.
    :type Force: boolean
    """
    pass


def detach_vpn_gateway(DryRun=None, VpnGatewayId=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpnGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            
    :type VpnGatewayId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def disable_vgw_route_propagation(RouteTableId=None, GatewayId=None):
    """
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            
    :type RouteTableId: string
    :param GatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            
    :type GatewayId: string
    """
    pass


def disable_vpc_classic_link(DryRun=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def disable_vpc_classic_link_dns_support(VpcId=None):
    """
    :param VpcId: The ID of the VPC.
            Return typedict
            ReturnsResponse Syntax{
              'Return': True|False
            }
            Response Structure
            (dict) --Contains the output of DisableVpcClassicLinkDnsSupport.
            Return (boolean) --Returns true if the request succeeds; otherwise, it returns an error.
            
            
    :type VpcId: string
    """
    pass


def disassociate_address(DryRun=None, PublicIp=None, AssociationId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param PublicIp: [EC2-Classic] The Elastic IP address. Required for EC2-Classic.
    :type PublicIp: string
    :param AssociationId: [EC2-VPC] The association ID. Required for EC2-VPC.
    :type AssociationId: string
    """
    pass


def disassociate_route_table(DryRun=None, AssociationId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param AssociationId: [REQUIRED]
            The association ID representing the current association between the route table and subnet.
            
    :type AssociationId: string
    """
    pass


def enable_vgw_route_propagation(RouteTableId=None, GatewayId=None):
    """
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            
    :type RouteTableId: string
    :param GatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            
    :type GatewayId: string
    """
    pass


def enable_volume_io(DryRun=None, VolumeId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            
    :type VolumeId: string
    """
    pass


def enable_vpc_classic_link(DryRun=None, VpcId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    """
    pass


def enable_vpc_classic_link_dns_support(VpcId=None):
    """
    :param VpcId: The ID of the VPC.
            Return typedict
            ReturnsResponse Syntax{
              'Return': True|False
            }
            Response Structure
            (dict) --Contains the output of EnableVpcClassicLinkDnsSupport.
            Return (boolean) --Returns true if the request succeeds; otherwise, it returns an error.
            
            
    :type VpcId: string
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


def get_console_output(DryRun=None, InstanceId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    """
    pass


def get_console_screenshot(DryRun=None, InstanceId=None, WakeUp=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param WakeUp: When set to true , acts as keystroke input and wakes up an instance that's in standby or 'sleep' mode.
    :type WakeUp: boolean
    """
    pass


def get_host_reservation_purchase_preview(OfferingId=None, HostIdSet=None):
    """
    :param OfferingId: [REQUIRED]
            The offering ID of the reservation.
            
    :type OfferingId: string
    :param HostIdSet: [REQUIRED]
            The ID/s of the Dedicated Host/s that the reservation will be associated with.
            (string) --
            
    :type HostIdSet: list
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


def get_password_data(DryRun=None, InstanceId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of the Windows instance.
            
    :type InstanceId: string
    """
    pass


def get_reserved_instances_exchange_quote(DryRun=None, ReservedInstanceIds=None, TargetConfigurations=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ReservedInstanceIds: [REQUIRED]
            The ID/s of the Convertible Reserved Instances you want to exchange.
            (string) --
            
    :type ReservedInstanceIds: list
    :param TargetConfigurations: The configuration requirements of the Convertible Reserved Instances you want in exchange for your current Convertible Reserved Instances.
            (dict) --Details about the target configuration.
            OfferingId (string) -- [REQUIRED]The Convertible Reserved Instance offering ID. If this isn't included in the request, the response lists your current Convertible Reserved Instance/s and their value/s.
            InstanceCount (integer) --The number of instances the Covertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request
            
            
    :type TargetConfigurations: list
    """
    pass


def get_waiter():
    """
    """
    pass


def import_image(DryRun=None, Description=None, DiskContainers=None, LicenseType=None, Hypervisor=None,
                 Architecture=None, Platform=None, ClientData=None, ClientToken=None, RoleName=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Description: A description string for the import image task.
    :type Description: string
    :param DiskContainers: Information about the disk containers.
            (dict) --Describes the disk container object for an import image task.
            Description (string) --The description of the disk image.
            Format (string) --The format of the disk image being imported.
            Valid values: RAW | VHD | VMDK | OVA
            Url (string) --The URL to the Amazon S3-based disk image being imported. The URL can either be a https URL (https://..) or an Amazon S3 URL (s3://..)
            UserBucket (dict) --The S3 bucket for the disk image.
            S3Bucket (string) --The name of the S3 bucket where the disk image is located.
            S3Key (string) --The file name of the disk image.
            DeviceName (string) --The block device mapping for the disk.
            SnapshotId (string) --The ID of the EBS snapshot to be used for importing the snapshot.
            
            
    :type DiskContainers: list
    :param LicenseType: The license type to be used for the Amazon Machine Image (AMI) after importing.
            Note: You may only use BYOL if you have existing licenses with rights to use these licenses in a third party cloud like AWS. For more information, see Prerequisites in the VM Import/Export User Guide.
            Valid values: AWS | BYOL
            
    :type LicenseType: string
    :param Hypervisor: The target hypervisor platform.
            Valid values: xen
            
    :type Hypervisor: string
    :param Architecture: The architecture of the virtual machine.
            Valid values: i386 | x86_64
            
    :type Architecture: string
    :param Platform: The operating system of the virtual machine.
            Valid values: Windows | Linux
            
    :type Platform: string
    :param ClientData: The client-specific data.
            UploadStart (datetime) --The time that the disk upload starts.
            UploadEnd (datetime) --The time that the disk upload ends.
            UploadSize (float) --The size of the uploaded disk image, in GiB.
            Comment (string) --A user-defined comment about the disk upload.
            
    :type ClientData: dict
    :param ClientToken: The token to enable idempotency for VM import requests.
    :type ClientToken: string
    :param RoleName: The name of the role to use when not using the default role, 'vmimport'.
    :type RoleName: string
    """
    pass


def import_instance(DryRun=None, Description=None, LaunchSpecification=None, DiskImages=None, Platform=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Description: A description for the instance being imported.
    :type Description: string
    :param LaunchSpecification: The launch specification.
            Architecture (string) --The architecture of the instance.
            GroupNames (list) --One or more security group names.
            (string) --
            GroupIds (list) --One or more security group IDs.
            (string) --
            AdditionalInfo (string) --Reserved.
            UserData (dict) --The user data to make available to the instance. If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.
            Data (string) --The user data. If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.
            InstanceType (string) --The instance type. For more information about the instance types that you can import, see Instance Types in the VM Import/Export User Guide.
            Placement (dict) --The placement information for the instance.
            AvailabilityZone (string) --The Availability Zone of the instance.
            GroupName (string) --The name of the placement group the instance is in (for cluster compute instances).
            Tenancy (string) --The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the ImportInstance command.
            HostId (string) --The ID of the Dedicted host on which the instance resides. This parameter is not support for the ImportInstance command.
            Affinity (string) --The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the ImportInstance command.
            Monitoring (boolean) --Indicates whether monitoring is enabled.
            SubnetId (string) --[EC2-VPC] The ID of the subnet in which to launch the instance.
            InstanceInitiatedShutdownBehavior (string) --Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
            PrivateIpAddress (string) --[EC2-VPC] An available IP address from the IP address range of the subnet.
            
    :type LaunchSpecification: dict
    :param DiskImages: The disk image.
            (dict) --Describes a disk image.
            Image (dict) --Information about the disk image.
            Format (string) -- [REQUIRED]The disk image format.
            Bytes (integer) -- [REQUIRED]The size of the disk image, in GiB.
            ImportManifestUrl (string) -- [REQUIRED]A presigned URL for the import manifest stored in Amazon S3 and presented here as an Amazon S3 presigned URL. For information about creating a presigned URL for an Amazon S3 object, read the 'Query String Request Authentication Alternative' section of the Authenticating REST Requests topic in the Amazon Simple Storage Service Developer Guide .
            For information about the import manifest referenced by this API action, see VM Import Manifest .
            Description (string) --A description of the disk image.
            Volume (dict) --Information about the volume.
            Size (integer) -- [REQUIRED]The size of the volume, in GiB.
            
            
    :type DiskImages: list
    :param Platform: [REQUIRED]
            The instance operating system.
            
    :type Platform: string
    """
    pass


def import_key_pair(DryRun=None, KeyName=None, PublicKeyMaterial=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param KeyName: [REQUIRED]
            A unique name for the key pair.
            
    :type KeyName: string
    :param PublicKeyMaterial: [REQUIRED]
            The public key. For API calls, the text must be base64-encoded. For command line tools, base64 encoding is performed for you.
            
    :type PublicKeyMaterial: bytes
    """
    pass


def import_snapshot(DryRun=None, Description=None, DiskContainer=None, ClientData=None, ClientToken=None,
                    RoleName=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Description: The description string for the import snapshot task.
    :type Description: string
    :param DiskContainer: Information about the disk container.
            Description (string) --The description of the disk image being imported.
            Format (string) --The format of the disk image being imported.
            Valid values: RAW | VHD | VMDK | OVA
            Url (string) --The URL to the Amazon S3-based disk image being imported. It can either be a https URL (https://..) or an Amazon S3 URL (s3://..).
            UserBucket (dict) --The S3 bucket for the disk image.
            S3Bucket (string) --The name of the S3 bucket where the disk image is located.
            S3Key (string) --The file name of the disk image.
            
            
    :type DiskContainer: dict
    :param ClientData: The client-specific data.
            UploadStart (datetime) --The time that the disk upload starts.
            UploadEnd (datetime) --The time that the disk upload ends.
            UploadSize (float) --The size of the uploaded disk image, in GiB.
            Comment (string) --A user-defined comment about the disk upload.
            
    :type ClientData: dict
    :param ClientToken: Token to enable idempotency for VM import requests.
    :type ClientToken: string
    :param RoleName: The name of the role to use when not using the default role, 'vmimport'.
    :type RoleName: string
    """
    pass


def import_volume(DryRun=None, AvailabilityZone=None, Image=None, Description=None, Volume=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param AvailabilityZone: [REQUIRED]
            The Availability Zone for the resulting EBS volume.
            
    :type AvailabilityZone: string
    :param Image: [REQUIRED]
            The disk image.
            Format (string) -- [REQUIRED]The disk image format.
            Bytes (integer) -- [REQUIRED]The size of the disk image, in GiB.
            ImportManifestUrl (string) -- [REQUIRED]A presigned URL for the import manifest stored in Amazon S3 and presented here as an Amazon S3 presigned URL. For information about creating a presigned URL for an Amazon S3 object, read the 'Query String Request Authentication Alternative' section of the Authenticating REST Requests topic in the Amazon Simple Storage Service Developer Guide .
            For information about the import manifest referenced by this API action, see VM Import Manifest .
            
    :type Image: dict
    :param Description: A description of the volume.
    :type Description: string
    :param Volume: [REQUIRED]
            The volume size.
            Size (integer) -- [REQUIRED]The size of the volume, in GiB.
            
    :type Volume: dict
    """
    pass


def modify_hosts(HostIds=None, AutoPlacement=None):
    """
    :param HostIds: [REQUIRED]
            The host IDs of the Dedicated Hosts you want to modify.
            (string) --
            
    :type HostIds: list
    :param AutoPlacement: [REQUIRED]
            Specify whether to enable or disable auto-placement.
            
    :type AutoPlacement: string
    """
    pass


def modify_id_format(Resource=None, UseLongIds=None):
    """
    :param Resource: [REQUIRED]
            The type of resource: instance | reservation | snapshot | volume
            
    :type Resource: string
    :param UseLongIds: [REQUIRED]
            Indicate whether the resource should use longer IDs (17-character IDs).
            
    :type UseLongIds: boolean
    """
    pass


def modify_identity_id_format(Resource=None, UseLongIds=None, PrincipalArn=None):
    """
    :param Resource: [REQUIRED]
            The type of resource: instance | reservation | snapshot | volume
            
    :type Resource: string
    :param UseLongIds: [REQUIRED]
            Indicates whether the resource should use longer IDs (17-character IDs)
            
    :type UseLongIds: boolean
    :param PrincipalArn: [REQUIRED]
            The ARN of the principal, which can be an IAM user, IAM role, or the root user. Specify all to modify the ID format for all IAM users, IAM roles, and the root user of the account.
            
    :type PrincipalArn: string
    """
    pass


def modify_image_attribute(DryRun=None, ImageId=None, Attribute=None, OperationType=None, UserIds=None, UserGroups=None,
                           ProductCodes=None, Value=None, LaunchPermission=None, Description=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImageId: [REQUIRED]
            The ID of the AMI.
            
    :type ImageId: string
    :param Attribute: The name of the attribute to modify.
    :type Attribute: string
    :param OperationType: The operation type.
    :type OperationType: string
    :param UserIds: One or more AWS account IDs. This is only valid when modifying the launchPermission attribute.
            (string) --
            
    :type UserIds: list
    :param UserGroups: One or more user groups. This is only valid when modifying the launchPermission attribute.
            (string) --
            
    :type UserGroups: list
    :param ProductCodes: One or more product codes. After you add a product code to an AMI, it can't be removed. This is only valid when modifying the productCodes attribute.
            (string) --
            
    :type ProductCodes: list
    :param Value: The value of the attribute being modified. This is only valid when modifying the description attribute.
    :type Value: string
    :param LaunchPermission: A launch permission modification.
            Add (list) --The AWS account ID to add to the list of launch permissions for the AMI.
            (dict) --Describes a launch permission.
            UserId (string) --The AWS account ID.
            Group (string) --The name of the group.
            
            Remove (list) --The AWS account ID to remove from the list of launch permissions for the AMI.
            (dict) --Describes a launch permission.
            UserId (string) --The AWS account ID.
            Group (string) --The name of the group.
            
            
    :type LaunchPermission: dict
    :param Description: A description for the AMI.
            Value (string) --The attribute value. Note that the value is case-sensitive.
            
    :type Description: dict
    """
    pass


def modify_instance_attribute(DryRun=None, InstanceId=None, Attribute=None, Value=None, BlockDeviceMappings=None,
                              SourceDestCheck=None, DisableApiTermination=None, InstanceType=None, Kernel=None,
                              Ramdisk=None, UserData=None, InstanceInitiatedShutdownBehavior=None, Groups=None,
                              EbsOptimized=None, SriovNetSupport=None, EnaSupport=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param Attribute: The name of the attribute.
    :type Attribute: string
    :param Value: A new value for the attribute. Use only with the kernel , ramdisk , userData , disableApiTermination , or instanceInitiatedShutdownBehavior attribute.
    :type Value: string
    :param BlockDeviceMappings: Modifies the DeleteOnTermination attribute for volumes that are currently attached. The volume must be owned by the caller. If no value is specified for DeleteOnTermination , the default is true and the volume is deleted when the instance is terminated.
            To add instance store volumes to an Amazon EBS-backed instance, you must add them when you launch the instance. For more information, see Updating the Block Device Mapping when Launching an Instance in the Amazon Elastic Compute Cloud User Guide .
            (dict) --Describes a block device mapping entry.
            DeviceName (string) --The device name exposed to the instance (for example, /dev/sdh or xvdh ).
            Ebs (dict) --Parameters used to automatically set up EBS volumes when the instance is launched.
            VolumeId (string) --The ID of the EBS volume.
            DeleteOnTermination (boolean) --Indicates whether the volume is deleted on instance termination.
            VirtualName (string) --The virtual device name.
            NoDevice (string) --suppress the specified device included in the block device mapping.
            
            
    :type BlockDeviceMappings: list
    :param SourceDestCheck: Specifies whether source/destination checking is enabled. A value of true means that checking is enabled, and false means checking is disabled. This value must be false for a NAT instance to perform NAT.
            Value (boolean) --The attribute value. The valid values are true or false .
            
    :type SourceDestCheck: dict
    :param DisableApiTermination: If the value is true , you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. You cannot use this paramater for Spot Instances.
            Value (boolean) --The attribute value. The valid values are true or false .
            
    :type DisableApiTermination: dict
    :param InstanceType: Changes the instance type to the specified value. For more information, see Instance Types . If the instance type is not valid, the error returned is InvalidInstanceAttributeValue .
            Value (string) --The attribute value. Note that the value is case-sensitive.
            
    :type InstanceType: dict
    :param Kernel: Changes the instance's kernel to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB .
            Value (string) --The attribute value. Note that the value is case-sensitive.
            
    :type Kernel: dict
    :param Ramdisk: Changes the instance's RAM disk to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB .
            Value (string) --The attribute value. Note that the value is case-sensitive.
            
    :type Ramdisk: dict
    :param UserData: Changes the instance's user data to the specified value. If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.
            Value (bytes) --
            
    :type UserData: dict
    :param InstanceInitiatedShutdownBehavior: Specifies whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
            Value (string) --The attribute value. Note that the value is case-sensitive.
            
    :type InstanceInitiatedShutdownBehavior: dict
    :param Groups: [EC2-VPC] Changes the security groups of the instance. You must specify at least one security group, even if it's just the default security group for the VPC. You must specify the security group ID, not the security group name.
            (string) --
            
    :type Groups: list
    :param EbsOptimized: Specifies whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
            Value (boolean) --The attribute value. The valid values are true or false .
            
    :type EbsOptimized: dict
    :param SriovNetSupport: Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the instance.
            There is no way to disable enhanced networking with the Intel 82599 Virtual Function interface at this time.
            This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.
            Value (string) --The attribute value. Note that the value is case-sensitive.
            
    :type SriovNetSupport: dict
    :param EnaSupport: Set to true to enable enhanced networking with ENA for the instance.
            This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.
            Value (boolean) --The attribute value. The valid values are true or false .
            
    :type EnaSupport: dict
    """
    pass


def modify_instance_placement(InstanceId=None, Tenancy=None, Affinity=None, HostId=None):
    """
    :param InstanceId: [REQUIRED]
            The ID of the instance that you are modifying.
            
    :type InstanceId: string
    :param Tenancy: The tenancy of the instance that you are modifying.
    :type Tenancy: string
    :param Affinity: The new affinity setting for the instance.
    :type Affinity: string
    :param HostId: The ID of the Dedicated Host that the instance will have affinity with.
    :type HostId: string
    """
    pass


def modify_network_interface_attribute(DryRun=None, NetworkInterfaceId=None, Description=None, SourceDestCheck=None,
                                       Groups=None, Attachment=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            
    :type NetworkInterfaceId: string
    :param Description: A description for the network interface.
            Value (string) --The attribute value. Note that the value is case-sensitive.
            
    :type Description: dict
    :param SourceDestCheck: Indicates whether source/destination checking is enabled. A value of true means checking is enabled, and false means checking is disabled. This value must be false for a NAT instance to perform NAT. For more information, see NAT Instances in the Amazon Virtual Private Cloud User Guide .
            Value (boolean) --The attribute value. The valid values are true or false .
            
    :type SourceDestCheck: dict
    :param Groups: Changes the security groups for the network interface. The new set of groups you specify replaces the current set. You must specify at least one group, even if it's just the default security group in the VPC. You must specify the ID of the security group, not the name.
            (string) --
            
    :type Groups: list
    :param Attachment: Information about the interface attachment. If modifying the 'delete on termination' attribute, you must specify the ID of the interface attachment.
            AttachmentId (string) --The ID of the network interface attachment.
            DeleteOnTermination (boolean) --Indicates whether the network interface is deleted when the instance is terminated.
            
    :type Attachment: dict
    """
    pass


def modify_reserved_instances(ClientToken=None, ReservedInstancesIds=None, TargetConfigurations=None):
    """
    :param ClientToken: A unique, case-sensitive token you provide to ensure idempotency of your modification request. For more information, see Ensuring Idempotency .
    :type ClientToken: string
    :param ReservedInstancesIds: [REQUIRED]
            The IDs of the Reserved Instances to modify.
            (string) --
            
    :type ReservedInstancesIds: list
    :param TargetConfigurations: [REQUIRED]
            The configuration settings for the Reserved Instances to modify.
            (dict) --Describes the configuration settings for the modified Reserved Instances.
            AvailabilityZone (string) --The Availability Zone for the modified Reserved Instances.
            Platform (string) --The network platform of the modified Reserved Instances, which is either EC2-Classic or EC2-VPC.
            InstanceCount (integer) --The number of modified Reserved Instances.
            InstanceType (string) --The instance type for the modified Reserved Instances.
            Scope (string) --Whether the Reserved Instance is standard or convertible .
            
            
    :type TargetConfigurations: list
    """
    pass


def modify_snapshot_attribute(DryRun=None, SnapshotId=None, Attribute=None, OperationType=None, UserIds=None,
                              GroupNames=None, CreateVolumePermission=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SnapshotId: [REQUIRED]
            The ID of the snapshot.
            
    :type SnapshotId: string
    :param Attribute: The snapshot attribute to modify.
            Note
            Only volume creation permissions may be modified at the customer level.
            
    :type Attribute: string
    :param OperationType: The type of operation to perform to the attribute.
    :type OperationType: string
    :param UserIds: The account ID to modify for the snapshot.
            (string) --
            
    :type UserIds: list
    :param GroupNames: The group to modify for the snapshot.
            (string) --
            
    :type GroupNames: list
    :param CreateVolumePermission: A JSON representation of the snapshot attribute modification.
            Add (list) --Adds a specific AWS account ID or group to a volume's list of create volume permissions.
            (dict) --Describes the user or group to be added or removed from the permissions for a volume.
            UserId (string) --The specific AWS account ID that is to be added or removed from a volume's list of create volume permissions.
            Group (string) --The specific group that is to be added or removed from a volume's list of create volume permissions.
            
            Remove (list) --Removes a specific AWS account ID or group from a volume's list of create volume permissions.
            (dict) --Describes the user or group to be added or removed from the permissions for a volume.
            UserId (string) --The specific AWS account ID that is to be added or removed from a volume's list of create volume permissions.
            Group (string) --The specific group that is to be added or removed from a volume's list of create volume permissions.
            
            
    :type CreateVolumePermission: dict
    """
    pass


def modify_spot_fleet_request(SpotFleetRequestId=None, TargetCapacity=None, ExcessCapacityTerminationPolicy=None):
    """
    :param SpotFleetRequestId: [REQUIRED]
            The ID of the Spot fleet request.
            
    :type SpotFleetRequestId: string
    :param TargetCapacity: The size of the fleet.
    :type TargetCapacity: integer
    :param ExcessCapacityTerminationPolicy: Indicates whether running Spot instances should be terminated if the target capacity of the Spot fleet request is decreased below the current size of the Spot fleet.
    :type ExcessCapacityTerminationPolicy: string
    """
    pass


def modify_subnet_attribute(SubnetId=None, MapPublicIpOnLaunch=None):
    """
    :param SubnetId: [REQUIRED]
            The ID of the subnet.
            
    :type SubnetId: string
    :param MapPublicIpOnLaunch: Specify true to indicate that instances launched into the specified subnet should be assigned public IP address.
            Value (boolean) --The attribute value. The valid values are true or false .
            
    :type MapPublicIpOnLaunch: dict
    """
    pass


def modify_volume_attribute(DryRun=None, VolumeId=None, AutoEnableIO=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            
    :type VolumeId: string
    :param AutoEnableIO: Indicates whether the volume should be auto-enabled for I/O operations.
            Value (boolean) --The attribute value. The valid values are true or false .
            
    :type AutoEnableIO: dict
    """
    pass


def modify_vpc_attribute(VpcId=None, EnableDnsSupport=None, EnableDnsHostnames=None):
    """
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            
    :type VpcId: string
    :param EnableDnsSupport: Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range 'plus two' will succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled.
            You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute.
            Value (boolean) --The attribute value. The valid values are true or false .
            
    :type EnableDnsSupport: dict
    :param EnableDnsHostnames: Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not.
            You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute. You can only enable DNS hostnames if you've enabled DNS support.
            Value (boolean) --The attribute value. The valid values are true or false .
            
    :type EnableDnsHostnames: dict
    """
    pass


def modify_vpc_endpoint(DryRun=None, VpcEndpointId=None, ResetPolicy=None, PolicyDocument=None, AddRouteTableIds=None,
                        RemoveRouteTableIds=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcEndpointId: [REQUIRED]
            The ID of the endpoint.
            
    :type VpcEndpointId: string
    :param ResetPolicy: Specify true to reset the policy document to the default policy. The default policy allows access to the service.
    :type ResetPolicy: boolean
    :param PolicyDocument: A policy document to attach to the endpoint. The policy must be in valid JSON format.
    :type PolicyDocument: string
    :param AddRouteTableIds: One or more route tables IDs to associate with the endpoint.
            (string) --
            
    :type AddRouteTableIds: list
    :param RemoveRouteTableIds: One or more route table IDs to disassociate from the endpoint.
            (string) --
            
    :type RemoveRouteTableIds: list
    """
    pass


def modify_vpc_peering_connection_options(DryRun=None, VpcPeeringConnectionId=None,
                                          RequesterPeeringConnectionOptions=None,
                                          AccepterPeeringConnectionOptions=None):
    """
    :param DryRun: Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcPeeringConnectionId: [REQUIRED]
            The ID of the VPC peering connection.
            
    :type VpcPeeringConnectionId: string
    :param RequesterPeeringConnectionOptions: The VPC peering connection options for the requester VPC.
            AllowEgressFromLocalClassicLinkToRemoteVpc (boolean) --If true, enables outbound communication from an EC2-Classic instance that's linked to a local VPC via ClassicLink to instances in a peer VPC.
            AllowEgressFromLocalVpcToRemoteClassicLink (boolean) --If true, enables outbound communication from instances in a local VPC to an EC2-Classic instance that's linked to a peer VPC via ClassicLink.
            AllowDnsResolutionFromRemoteVpc (boolean) --If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.
            
    :type RequesterPeeringConnectionOptions: dict
    :param AccepterPeeringConnectionOptions: The VPC peering connection options for the accepter VPC.
            AllowEgressFromLocalClassicLinkToRemoteVpc (boolean) --If true, enables outbound communication from an EC2-Classic instance that's linked to a local VPC via ClassicLink to instances in a peer VPC.
            AllowEgressFromLocalVpcToRemoteClassicLink (boolean) --If true, enables outbound communication from instances in a local VPC to an EC2-Classic instance that's linked to a peer VPC via ClassicLink.
            AllowDnsResolutionFromRemoteVpc (boolean) --If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.
            
    :type AccepterPeeringConnectionOptions: dict
    """
    pass


def monitor_instances(DryRun=None, InstanceIds=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            
    :type InstanceIds: list
    """
    pass


def move_address_to_vpc(DryRun=None, PublicIp=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param PublicIp: [REQUIRED]
            The Elastic IP address.
            
    :type PublicIp: string
    """
    pass


def purchase_host_reservation(OfferingId=None, HostIdSet=None, LimitPrice=None, CurrencyCode=None, ClientToken=None):
    """
    :param OfferingId: [REQUIRED]
            The ID of the offering.
            
    :type OfferingId: string
    :param HostIdSet: [REQUIRED]
            The ID/s of the Dedicated Host/s that the reservation will be associated with.
            (string) --
            
    :type HostIdSet: list
    :param LimitPrice: The specified limit is checked against the total upfront cost of the reservation (calculated as the offering's upfront cost multiplied by the host count). If the total upfront cost is greater than the specified price limit, the request will fail. This is used to ensure that the purchase does not exceed the expected upfront cost of the purchase. At this time, the only supported currency is USD . For example, to indicate a limit price of USD 100, specify 100.00.
    :type LimitPrice: string
    :param CurrencyCode: The currency in which the totalUpfrontPrice , LimitPrice , and totalHourlyPrice amounts are specified. At this time, the only supported currency is USD .
    :type CurrencyCode: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide .
    :type ClientToken: string
    """
    pass


def purchase_reserved_instances_offering(DryRun=None, ReservedInstancesOfferingId=None, InstanceCount=None,
                                         LimitPrice=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ReservedInstancesOfferingId: [REQUIRED]
            The ID of the Reserved Instance offering to purchase.
            
    :type ReservedInstancesOfferingId: string
    :param InstanceCount: [REQUIRED]
            The number of Reserved Instances to purchase.
            
    :type InstanceCount: integer
    :param LimitPrice: Specified for Reserved Instance Marketplace offerings to limit the total order and ensure that the Reserved Instances are not purchased at unexpected prices.
            Amount (float) --Used for Reserved Instance Marketplace offerings. Specifies the limit price on the total order (instanceCount * price).
            CurrencyCode (string) --The currency in which the limitPrice amount is specified. At this time, the only supported currency is USD .
            
    :type LimitPrice: dict
    """
    pass


def purchase_scheduled_instances(DryRun=None, ClientToken=None, PurchaseRequests=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ClientToken: Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see Ensuring Idempotency .
    :type ClientToken: string
    :param PurchaseRequests: [REQUIRED]
            One or more purchase requests.
            (dict) --Describes a request to purchase Scheduled Instances.
            PurchaseToken (string) -- [REQUIRED]The purchase token.
            InstanceCount (integer) -- [REQUIRED]The number of instances.
            
            
    :type PurchaseRequests: list
    """
    pass


def reboot_instances(DryRun=None, InstanceIds=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            
    :type InstanceIds: list
    """
    pass


def register_image(DryRun=None, ImageLocation=None, Name=None, Description=None, Architecture=None, KernelId=None,
                   RamdiskId=None, RootDeviceName=None, BlockDeviceMappings=None, VirtualizationType=None,
                   SriovNetSupport=None, EnaSupport=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImageLocation: The full path to your AMI manifest in Amazon S3 storage.
    :type ImageLocation: string
    :param Name: [REQUIRED]
            A name for your AMI.
            Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)
            
    :type Name: string
    :param Description: A description for your AMI.
    :type Description: string
    :param Architecture: The architecture of the AMI.
            Default: For Amazon EBS-backed AMIs, i386 . For instance store-backed AMIs, the architecture specified in the manifest file.
            
    :type Architecture: string
    :param KernelId: The ID of the kernel.
    :type KernelId: string
    :param RamdiskId: The ID of the RAM disk.
    :type RamdiskId: string
    :param RootDeviceName: The name of the root device (for example, /dev/sda1 , or /dev/xvda ).
    :type RootDeviceName: string
    :param BlockDeviceMappings: One or more block device mapping entries.
            (dict) --Describes a block device mapping.
            VirtualName (string) --The virtual device name (ephemeral N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1 .The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
            Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
            DeviceName (string) --The device name exposed to the instance (for example, /dev/sdh or xvdh ).
            Ebs (dict) --Parameters used to automatically set up EBS volumes when the instance is launched.
            SnapshotId (string) --The ID of the snapshot.
            VolumeSize (integer) --The size of the volume, in GiB.
            Constraints: 1-16384 for General Purpose SSD (gp2 ), 4-16384 for Provisioned IOPS SSD (io1 ), 500-16384 for Throughput Optimized HDD (st1 ), 500-16384 for Cold HDD (sc1 ), and 1-1024 for Magnetic (standard ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
            Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
            DeleteOnTermination (boolean) --Indicates whether the EBS volume is deleted on instance termination.
            VolumeType (string) --The volume type: gp2 , io1 , st1 , sc1 , or standard .
            Default: standard
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports. For io1 , this represents the number of IOPS that are provisioned for the volume. For gp2 , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide .
            Constraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes.
            Condition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2 , st1 , sc1 , or standard volumes.
            Encrypted (boolean) --Indicates whether the EBS volume is encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption.
            NoDevice (string) --Suppresses the specified device included in the block device mapping of the AMI.
            
            
    :type BlockDeviceMappings: list
    :param VirtualizationType: The type of virtualization.
            Default: paravirtual
            
    :type VirtualizationType: string
    :param SriovNetSupport: Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI.
            There is no way to disable sriovNetSupport at this time.
            This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.
            
    :type SriovNetSupport: string
    :param EnaSupport: Set to true to enable enhanced networking with ENA for the AMI and any instances that you launch from the AMI.
            This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.
            
    :type EnaSupport: boolean
    """
    pass


def reject_vpc_peering_connection(DryRun=None, VpcPeeringConnectionId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param VpcPeeringConnectionId: [REQUIRED]
            The ID of the VPC peering connection.
            
    :type VpcPeeringConnectionId: string
    """
    pass


def release_address(DryRun=None, PublicIp=None, AllocationId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param PublicIp: [EC2-Classic] The Elastic IP address. Required for EC2-Classic.
    :type PublicIp: string
    :param AllocationId: [EC2-VPC] The allocation ID. Required for EC2-VPC.
    :type AllocationId: string
    """
    pass


def release_hosts(HostIds=None):
    """
    :param HostIds: [REQUIRED]
            The IDs of the Dedicated Hosts you want to release.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'Successful': [
                'string',
              ],
              'Unsuccessful': [
                {
                  'Error': {
                    'Code': 'string',
                    'Message': 'string'
                  },
                  'ResourceId': 'string'
                },
              ]
            }
            Response Structure
            (dict) --Contains the output of ReleaseHosts.
            Successful (list) --The IDs of the Dedicated Hosts that were successfully released.
            (string) --
            Unsuccessful (list) --The IDs of the Dedicated Hosts that could not be released, including an error message.
            (dict) --Information about items that were not successfully processed in a batch call.
            Error (dict) --Information about the error.
            Code (string) --The error code.
            Message (string) --The error message accompanying the error code.
            ResourceId (string) --The ID of the resource.
            
            
            
    :type HostIds: list
    """
    pass


def replace_network_acl_association(DryRun=None, AssociationId=None, NetworkAclId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param AssociationId: [REQUIRED]
            The ID of the current association between the original network ACL and the subnet.
            
    :type AssociationId: string
    :param NetworkAclId: [REQUIRED]
            The ID of the new network ACL to associate with the subnet.
            
    :type NetworkAclId: string
    """
    pass


def replace_network_acl_entry(DryRun=None, NetworkAclId=None, RuleNumber=None, Protocol=None, RuleAction=None,
                              Egress=None, CidrBlock=None, IcmpTypeCode=None, PortRange=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkAclId: [REQUIRED]
            The ID of the ACL.
            
    :type NetworkAclId: string
    :param RuleNumber: [REQUIRED]
            The rule number of the entry to replace.
            
    :type RuleNumber: integer
    :param Protocol: [REQUIRED]
            The IP protocol. You can specify all or -1 to mean all protocols.
            
    :type Protocol: string
    :param RuleAction: [REQUIRED]
            Indicates whether to allow or deny the traffic that matches the rule.
            
    :type RuleAction: string
    :param Egress: [REQUIRED]
            Indicates whether to replace the egress rule.
            Default: If no value is specified, we replace the ingress rule.
            
    :type Egress: boolean
    :param CidrBlock: [REQUIRED]
            The network range to allow or deny, in CIDR notation.
            
    :type CidrBlock: string
    :param IcmpTypeCode: ICMP protocol: The ICMP type and code. Required if specifying 1 (ICMP) for the protocol.
            Type (integer) --The ICMP code. A value of -1 means all codes for the specified ICMP type.
            Code (integer) --The ICMP type. A value of -1 means all types.
            
    :type IcmpTypeCode: dict
    :param PortRange: TCP or UDP protocols: The range of ports the rule applies to. Required if specifying 6 (TCP) or 17 (UDP) for the protocol.
            From (integer) --The first port in the range.
            To (integer) --The last port in the range.
            
    :type PortRange: dict
    """
    pass


def replace_route(DryRun=None, RouteTableId=None, DestinationCidrBlock=None, GatewayId=None, InstanceId=None,
                  NetworkInterfaceId=None, VpcPeeringConnectionId=None, NatGatewayId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            
    :type RouteTableId: string
    :param DestinationCidrBlock: [REQUIRED]
            The CIDR address block used for the destination match. The value you provide must match the CIDR of an existing route in the table.
            
    :type DestinationCidrBlock: string
    :param GatewayId: The ID of an Internet gateway or virtual private gateway.
    :type GatewayId: string
    :param InstanceId: The ID of a NAT instance in your VPC.
    :type InstanceId: string
    :param NetworkInterfaceId: The ID of a network interface.
    :type NetworkInterfaceId: string
    :param VpcPeeringConnectionId: The ID of a VPC peering connection.
    :type VpcPeeringConnectionId: string
    :param NatGatewayId: The ID of a NAT gateway.
    :type NatGatewayId: string
    """
    pass


def replace_route_table_association(DryRun=None, AssociationId=None, RouteTableId=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param AssociationId: [REQUIRED]
            The association ID.
            
    :type AssociationId: string
    :param RouteTableId: [REQUIRED]
            The ID of the new route table to associate with the subnet.
            
    :type RouteTableId: string
    """
    pass


def report_instance_status(DryRun=None, Instances=None, Status=None, StartTime=None, EndTime=None, ReasonCodes=None,
                           Description=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param Instances: [REQUIRED]
            One or more instances.
            (string) --
            
    :type Instances: list
    :param Status: [REQUIRED]
            The status of all instances listed.
            
    :type Status: string
    :param StartTime: The time at which the reported instance health state began.
    :type StartTime: datetime
    :param EndTime: The time at which the reported instance health state ended.
    :type EndTime: datetime
    :param ReasonCodes: [REQUIRED]
            One or more reason codes that describes the health state of your instance.
            instance-stuck-in-state : My instance is stuck in a state.
            unresponsive : My instance is unresponsive.
            not-accepting-credentials : My instance is not accepting my credentials.
            password-not-available : A password is not available for my instance.
            performance-network : My instance is experiencing performance problems which I believe are network related.
            performance-instance-store : My instance is experiencing performance problems which I believe are related to the instance stores.
            performance-ebs-volume : My instance is experiencing performance problems which I believe are related to an EBS volume.
            performance-other : My instance is experiencing performance problems.
            other : [explain using the description parameter]
            (string) --
            
    :type ReasonCodes: list
    :param Description: Descriptive text about the health state of your instance.
    :type Description: string
    """
    pass


def request_spot_fleet(DryRun=None, SpotFleetRequestConfig=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SpotFleetRequestConfig: [REQUIRED]
            The configuration for the Spot fleet request.
            ClientToken (string) --A unique, case-sensitive identifier you provide to ensure idempotency of your listings. This helps avoid duplicate listings. For more information, see Ensuring Idempotency .
            SpotPrice (string) -- [REQUIRED]The bid price per unit hour.
            TargetCapacity (integer) -- [REQUIRED]The number of units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O.
            ValidFrom (datetime) --The start date and time of the request, in UTC format (for example, YYYY -MM -DD T*HH* :MM :SS Z). The default is to start fulfilling the request immediately.
            ValidUntil (datetime) --The end date and time of the request, in UTC format (for example, YYYY -MM -DD T*HH* :MM :SS Z). At this point, no new Spot instance requests are placed or enabled to fulfill the request.
            TerminateInstancesWithExpiration (boolean) --Indicates whether running Spot instances should be terminated when the Spot fleet request expires.
            IamFleetRole (string) -- [REQUIRED]Grants the Spot fleet permission to terminate Spot instances on your behalf when you cancel its Spot fleet request using CancelSpotFleetRequests or when the Spot fleet request expires, if you set terminateInstancesWithExpiration .
            LaunchSpecifications (list) -- [REQUIRED]Information about the launch specifications for the Spot fleet request.
            (dict) --Describes the launch specification for one or more Spot instances.
            ImageId (string) --The ID of the AMI.
            KeyName (string) --The name of the key pair.
            SecurityGroups (list) --One or more security groups. When requesting instances in a VPC, you must specify the IDs of the security groups. When requesting instances in EC2-Classic, you can specify the names or the IDs of the security groups.
            (dict) --Describes a security group.
            GroupName (string) --The name of the security group.
            GroupId (string) --The ID of the security group.
            
            UserData (string) --The user data to make available to the instances. If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.
            AddressingType (string) --Deprecated.
            InstanceType (string) --The instance type.
            Placement (dict) --The placement information.
            AvailabilityZone (string) --The Availability Zone.
            [Spot fleet only] To specify multiple Availability Zones, separate them using commas; for example, 'us-west-2a, us-west-2b'.
            GroupName (string) --The name of the placement group (for cluster instances).
            KernelId (string) --The ID of the kernel.
            RamdiskId (string) --The ID of the RAM disk.
            BlockDeviceMappings (list) --One or more block device mapping entries.
            (dict) --Describes a block device mapping.
            VirtualName (string) --The virtual device name (ephemeral N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1 .The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
            Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
            DeviceName (string) --The device name exposed to the instance (for example, /dev/sdh or xvdh ).
            Ebs (dict) --Parameters used to automatically set up EBS volumes when the instance is launched.
            SnapshotId (string) --The ID of the snapshot.
            VolumeSize (integer) --The size of the volume, in GiB.
            Constraints: 1-16384 for General Purpose SSD (gp2 ), 4-16384 for Provisioned IOPS SSD (io1 ), 500-16384 for Throughput Optimized HDD (st1 ), 500-16384 for Cold HDD (sc1 ), and 1-1024 for Magnetic (standard ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
            Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
            DeleteOnTermination (boolean) --Indicates whether the EBS volume is deleted on instance termination.
            VolumeType (string) --The volume type: gp2 , io1 , st1 , sc1 , or standard .
            Default: standard
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports. For io1 , this represents the number of IOPS that are provisioned for the volume. For gp2 , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide .
            Constraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes.
            Condition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2 , st1 , sc1 , or standard volumes.
            Encrypted (boolean) --Indicates whether the EBS volume is encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption.
            NoDevice (string) --Suppresses the specified device included in the block device mapping of the AMI.
            
            Monitoring (dict) --Enable or disable monitoring for the instances.
            Enabled (boolean) --Enables monitoring for the instance.
            Default: false
            SubnetId (string) --The ID of the subnet in which to launch the instances. To specify multiple subnets, separate them using commas; for example, 'subnet-a61dafcf, subnet-65ea5f08'.
            NetworkInterfaces (list) --One or more network interfaces.
            (dict) --Describes a network interface.
            NetworkInterfaceId (string) --The ID of the network interface.
            DeviceIndex (integer) --The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a RunInstances request, you must provide the device index.
            SubnetId (string) --The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
            Description (string) --The description of the network interface. Applies only if creating a network interface when launching an instance.
            PrivateIpAddress (string) --The private IP address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            Groups (list) --The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
            (string) --
            DeleteOnTermination (boolean) --If set to true , the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.
            PrivateIpAddresses (list) --One or more private IP addresses to assign to the network interface. Only one private IP address can be designated as primary. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            (dict) --Describes a secondary private IP address for a network interface.
            PrivateIpAddress (string) -- [REQUIRED]The private IP addresses.
            Primary (boolean) --Indicates whether the private IP address is the primary private IP address. Only one IP address can be designated as primary.
            
            SecondaryPrivateIpAddressCount (integer) --The number of secondary private IP addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            AssociatePublicIpAddress (boolean) --Indicates whether to assign a public IP address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .
            
            IamInstanceProfile (dict) --The IAM instance profile.
            Arn (string) --The Amazon Resource Name (ARN) of the instance profile.
            Name (string) --The name of the instance profile.
            EbsOptimized (boolean) --Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
            Default: false
            WeightedCapacity (float) --The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms (instances or a performance characteristic such as vCPUs, memory, or I/O).
            If the target capacity divided by this value is not a whole number, we round the number of instances to the next whole number. If this value is not specified, the default is 1.
            SpotPrice (string) --The bid price per unit hour for the specified instance type. If this value is not specified, the default is the Spot bid price specified for the fleet. To determine the bid price per unit hour, divide the Spot bid price by the value of WeightedCapacity .
            
            ExcessCapacityTerminationPolicy (string) --Indicates whether running Spot instances should be terminated if the target capacity of the Spot fleet request is decreased below the current size of the Spot fleet.
            AllocationStrategy (string) --Indicates how to allocate the target capacity across the Spot pools specified by the Spot fleet request. The default is lowestPrice .
            FulfilledCapacity (float) --The number of units fulfilled by this request compared to the set target capacity.
            Type (string) --The type of request. Indicates whether the fleet will only request the target capacity or also attempt to maintain it. When you request a certain target capacity, the fleet will only place the required bids. It will not attempt to replenish Spot instances if capacity is diminished, nor will it submit bids in alternative Spot pools if capacity is not available. When you want to maintain a certain target capacity, fleet will place the required bids to meet this target capacity. It will also automatically replenish any interrupted instances. Default: maintain .
            
    :type SpotFleetRequestConfig: dict
    """
    pass


def request_spot_instances(DryRun=None, SpotPrice=None, ClientToken=None, InstanceCount=None, Type=None, ValidFrom=None,
                           ValidUntil=None, LaunchGroup=None, AvailabilityZoneGroup=None, BlockDurationMinutes=None,
                           LaunchSpecification=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SpotPrice: [REQUIRED]
            The maximum hourly price (bid) for any Spot instance launched to fulfill the request.
            
    :type SpotPrice: string
    :param ClientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide .
    :type ClientToken: string
    :param InstanceCount: The maximum number of Spot instances to launch.
            Default: 1
            
    :type InstanceCount: integer
    :param Type: The Spot instance request type.
            Default: one-time
            
    :type Type: string
    :param ValidFrom: The start date of the request. If this is a one-time request, the request becomes active at this date and time and remains active until all instances launch, the request expires, or the request is canceled. If the request is persistent, the request becomes active at this date and time and remains active until it expires or is canceled.
            Default: The request is effective indefinitely.
            
    :type ValidFrom: datetime
    :param ValidUntil: The end date of the request. If this is a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached.
            Default: The request is effective indefinitely.
            
    :type ValidUntil: datetime
    :param LaunchGroup: The instance launch group. Launch groups are Spot instances that launch together and terminate together.
            Default: Instances are launched and terminated individually
            
    :type LaunchGroup: string
    :param AvailabilityZoneGroup: The user-specified name for a logical grouping of bids.
            When you specify an Availability Zone group in a Spot Instance request, all Spot instances in the request are launched in the same Availability Zone. Instance proximity is maintained with this parameter, but the choice of Availability Zone is not. The group applies only to bids for Spot Instances of the same instance type. Any additional Spot instance requests that are specified with the same Availability Zone group name are launched in that same Availability Zone, as long as at least one instance from the group is still active.
            If there is no active instance running in the Availability Zone group that you specify for a new Spot instance request (all instances are terminated, the bid is expired, or the bid falls below current market), then Amazon EC2 launches the instance in any Availability Zone where the constraint can be met. Consequently, the subsequent set of Spot instances could be placed in a different zone from the original request, even if you specified the same Availability Zone group.
            Default: Instances are launched in any available Availability Zone.
            
    :type AvailabilityZoneGroup: string
    :param BlockDurationMinutes: The required duration for the Spot instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
            The duration period starts as soon as your Spot instance receives its instance ID. At the end of the duration period, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.
            Note that you can't specify an Availability Zone group or a launch group if you specify a duration.
            
    :type BlockDurationMinutes: integer
    :param LaunchSpecification: Describes the launch specification for an instance.
            ImageId (string) --The ID of the AMI.
            KeyName (string) --The name of the key pair.
            SecurityGroups (list) --
            (string) --
            UserData (string) --The user data to make available to the instances. If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.
            AddressingType (string) --Deprecated.
            InstanceType (string) --The instance type.
            Placement (dict) --The placement information for the instance.
            AvailabilityZone (string) --The Availability Zone.
            [Spot fleet only] To specify multiple Availability Zones, separate them using commas; for example, 'us-west-2a, us-west-2b'.
            GroupName (string) --The name of the placement group (for cluster instances).
            KernelId (string) --The ID of the kernel.
            RamdiskId (string) --The ID of the RAM disk.
            BlockDeviceMappings (list) --One or more block device mapping entries.
            Although you can specify encrypted EBS volumes in this block device mapping for your Spot Instances, these volumes are not encrypted.
            (dict) --Describes a block device mapping.
            VirtualName (string) --The virtual device name (ephemeral N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1 .The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
            Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
            DeviceName (string) --The device name exposed to the instance (for example, /dev/sdh or xvdh ).
            Ebs (dict) --Parameters used to automatically set up EBS volumes when the instance is launched.
            SnapshotId (string) --The ID of the snapshot.
            VolumeSize (integer) --The size of the volume, in GiB.
            Constraints: 1-16384 for General Purpose SSD (gp2 ), 4-16384 for Provisioned IOPS SSD (io1 ), 500-16384 for Throughput Optimized HDD (st1 ), 500-16384 for Cold HDD (sc1 ), and 1-1024 for Magnetic (standard ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
            Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
            DeleteOnTermination (boolean) --Indicates whether the EBS volume is deleted on instance termination.
            VolumeType (string) --The volume type: gp2 , io1 , st1 , sc1 , or standard .
            Default: standard
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports. For io1 , this represents the number of IOPS that are provisioned for the volume. For gp2 , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide .
            Constraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes.
            Condition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2 , st1 , sc1 , or standard volumes.
            Encrypted (boolean) --Indicates whether the EBS volume is encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption.
            NoDevice (string) --Suppresses the specified device included in the block device mapping of the AMI.
            
            SubnetId (string) --The ID of the subnet in which to launch the instance.
            NetworkInterfaces (list) --One or more network interfaces.
            (dict) --Describes a network interface.
            NetworkInterfaceId (string) --The ID of the network interface.
            DeviceIndex (integer) --The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a RunInstances request, you must provide the device index.
            SubnetId (string) --The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
            Description (string) --The description of the network interface. Applies only if creating a network interface when launching an instance.
            PrivateIpAddress (string) --The private IP address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            Groups (list) --The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
            (string) --
            DeleteOnTermination (boolean) --If set to true , the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.
            PrivateIpAddresses (list) --One or more private IP addresses to assign to the network interface. Only one private IP address can be designated as primary. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            (dict) --Describes a secondary private IP address for a network interface.
            PrivateIpAddress (string) -- [REQUIRED]The private IP addresses.
            Primary (boolean) --Indicates whether the private IP address is the primary private IP address. Only one IP address can be designated as primary.
            
            SecondaryPrivateIpAddressCount (integer) --The number of secondary private IP addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            AssociatePublicIpAddress (boolean) --Indicates whether to assign a public IP address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .
            
            IamInstanceProfile (dict) --The IAM instance profile.
            Arn (string) --The Amazon Resource Name (ARN) of the instance profile.
            Name (string) --The name of the instance profile.
            EbsOptimized (boolean) --Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
            Default: false
            Monitoring (dict) --Describes the monitoring for the instance.
            Enabled (boolean) -- [REQUIRED]Indicates whether monitoring is enabled for the instance.
            SecurityGroupIds (list) --
            (string) --
            
    :type LaunchSpecification: dict
    """
    pass


def reset_image_attribute(DryRun=None, ImageId=None, Attribute=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImageId: [REQUIRED]
            The ID of the AMI.
            
    :type ImageId: string
    :param Attribute: [REQUIRED]
            The attribute to reset (currently you can only reset the launch permission attribute).
            
    :type Attribute: string
    """
    pass


def reset_instance_attribute(DryRun=None, InstanceId=None, Attribute=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param Attribute: [REQUIRED]
            The attribute to reset.
            Warning
            You can only reset the following attributes: kernel | ramdisk | sourceDestCheck . To change an instance attribute, use ModifyInstanceAttribute .
            
    :type Attribute: string
    """
    pass


def reset_network_interface_attribute(DryRun=None, NetworkInterfaceId=None, SourceDestCheck=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            
    :type NetworkInterfaceId: string
    :param SourceDestCheck: The source/destination checking attribute. Resets the value to true .
    :type SourceDestCheck: string
    """
    pass


def reset_snapshot_attribute(DryRun=None, SnapshotId=None, Attribute=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param SnapshotId: [REQUIRED]
            The ID of the snapshot.
            
    :type SnapshotId: string
    :param Attribute: [REQUIRED]
            The attribute to reset. Currently, only the attribute for permission to create volumes can be reset.
            
    :type Attribute: string
    """
    pass


def restore_address_to_classic(DryRun=None, PublicIp=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param PublicIp: [REQUIRED]
            The Elastic IP address.
            
    :type PublicIp: string
    """
    pass


def revoke_security_group_egress(DryRun=None, GroupId=None, SourceSecurityGroupName=None,
                                 SourceSecurityGroupOwnerId=None, IpProtocol=None, FromPort=None, ToPort=None,
                                 CidrIp=None, IpPermissions=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupId: [REQUIRED]
            The ID of the security group.
            
    :type GroupId: string
    :param SourceSecurityGroupName: The name of a destination security group. To revoke outbound access to a destination security group, we recommend that you use a set of IP permissions instead.
    :type SourceSecurityGroupName: string
    :param SourceSecurityGroupOwnerId: The AWS account number for a destination security group. To revoke outbound access to a destination security group, we recommend that you use a set of IP permissions instead.
    :type SourceSecurityGroupOwnerId: string
    :param IpProtocol: The IP protocol name or number. We recommend that you specify the protocol in a set of IP permissions instead.
    :type IpProtocol: string
    :param FromPort: The start of port range for the TCP and UDP protocols, or an ICMP type number. We recommend that you specify the port range in a set of IP permissions instead.
    :type FromPort: integer
    :param ToPort: The end of port range for the TCP and UDP protocols, or an ICMP type number. We recommend that you specify the port range in a set of IP permissions instead.
    :type ToPort: integer
    :param CidrIp: The CIDR IP address range. We recommend that you specify the CIDR range in a set of IP permissions instead.
    :type CidrIp: string
    :param IpPermissions: A set of IP permissions. You can't specify a destination security group and a CIDR IP address range.
            (dict) --Describes a security group rule.
            IpProtocol (string) --The IP protocol name (for tcp , udp , and icmp ) or number (see Protocol Numbers ).
            [EC2-VPC only] When you authorize or revoke security group rules, you can use -1 to specify all.
            FromPort (integer) --The start of port range for the TCP and UDP protocols, or an ICMP type number. A value of -1 indicates all ICMP types.
            ToPort (integer) --The end of port range for the TCP and UDP protocols, or an ICMP code. A value of -1 indicates all ICMP codes for the specified ICMP type.
            UserIdGroupPairs (list) --One or more security group and AWS account ID pairs.
            (dict) --Describes a security group and AWS account ID pair.
            UserId (string) --The ID of an AWS account. For a referenced security group in another VPC, the account ID of the referenced security group is returned.
            [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
            GroupName (string) --The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.
            GroupId (string) --The ID of the security group.
            VpcId (string) --The ID of the VPC for the referenced security group, if applicable.
            VpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.
            PeeringStatus (string) --The status of a VPC peering connection, if applicable.
            
            IpRanges (list) --One or more IP ranges.
            (dict) --Describes an IP range.
            CidrIp (string) --The CIDR range. You can either specify a CIDR range or a source security group, not both.
            
            PrefixListIds (list) --(Valid for AuthorizeSecurityGroupEgress , RevokeSecurityGroupEgress and DescribeSecurityGroups only) One or more prefix list IDs for an AWS service. In an AuthorizeSecurityGroupEgress request, this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
            (dict) --The ID of the prefix.
            PrefixListId (string) --The ID of the prefix.
            
            
            
    :type IpPermissions: list
    """
    pass


def revoke_security_group_ingress(DryRun=None, GroupName=None, GroupId=None, SourceSecurityGroupName=None,
                                  SourceSecurityGroupOwnerId=None, IpProtocol=None, FromPort=None, ToPort=None,
                                  CidrIp=None, IpPermissions=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param GroupName: [EC2-Classic, default VPC] The name of the security group.
    :type GroupName: string
    :param GroupId: The ID of the security group. Required for a security group in a nondefault VPC.
    :type GroupId: string
    :param SourceSecurityGroupName: [EC2-Classic, default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. For EC2-VPC, the source security group must be in the same VPC. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.
    :type SourceSecurityGroupName: string
    :param SourceSecurityGroupOwnerId: [EC2-Classic] The AWS account ID of the source security group, if the source security group is in a different account. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.
    :type SourceSecurityGroupOwnerId: string
    :param IpProtocol: The IP protocol name (tcp , udp , icmp ) or number (see Protocol Numbers ). Use -1 to specify all.
    :type IpProtocol: string
    :param FromPort: The start of port range for the TCP and UDP protocols, or an ICMP type number. For the ICMP type number, use -1 to specify all ICMP types.
    :type FromPort: integer
    :param ToPort: The end of port range for the TCP and UDP protocols, or an ICMP code number. For the ICMP code number, use -1 to specify all ICMP codes for the ICMP type.
    :type ToPort: integer
    :param CidrIp: The CIDR IP address range. You can't specify this parameter when specifying a source security group.
    :type CidrIp: string
    :param IpPermissions: A set of IP permissions. You can't specify a source security group and a CIDR IP address range.
            (dict) --Describes a security group rule.
            IpProtocol (string) --The IP protocol name (for tcp , udp , and icmp ) or number (see Protocol Numbers ).
            [EC2-VPC only] When you authorize or revoke security group rules, you can use -1 to specify all.
            FromPort (integer) --The start of port range for the TCP and UDP protocols, or an ICMP type number. A value of -1 indicates all ICMP types.
            ToPort (integer) --The end of port range for the TCP and UDP protocols, or an ICMP code. A value of -1 indicates all ICMP codes for the specified ICMP type.
            UserIdGroupPairs (list) --One or more security group and AWS account ID pairs.
            (dict) --Describes a security group and AWS account ID pair.
            UserId (string) --The ID of an AWS account. For a referenced security group in another VPC, the account ID of the referenced security group is returned.
            [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
            GroupName (string) --The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.
            GroupId (string) --The ID of the security group.
            VpcId (string) --The ID of the VPC for the referenced security group, if applicable.
            VpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.
            PeeringStatus (string) --The status of a VPC peering connection, if applicable.
            
            IpRanges (list) --One or more IP ranges.
            (dict) --Describes an IP range.
            CidrIp (string) --The CIDR range. You can either specify a CIDR range or a source security group, not both.
            
            PrefixListIds (list) --(Valid for AuthorizeSecurityGroupEgress , RevokeSecurityGroupEgress and DescribeSecurityGroups only) One or more prefix list IDs for an AWS service. In an AuthorizeSecurityGroupEgress request, this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
            (dict) --The ID of the prefix.
            PrefixListId (string) --The ID of the prefix.
            
            
            
    :type IpPermissions: list
    """
    pass


def run_instances(DryRun=None, ImageId=None, MinCount=None, MaxCount=None, KeyName=None, SecurityGroups=None,
                  SecurityGroupIds=None, UserData=None, InstanceType=None, Placement=None, KernelId=None,
                  RamdiskId=None, BlockDeviceMappings=None, Monitoring=None, SubnetId=None, DisableApiTermination=None,
                  InstanceInitiatedShutdownBehavior=None, PrivateIpAddress=None, ClientToken=None, AdditionalInfo=None,
                  NetworkInterfaces=None, IamInstanceProfile=None, EbsOptimized=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ImageId: [REQUIRED]
            The ID of the AMI, which you can get by calling DescribeImages .
            
    :type ImageId: string
    :param MinCount: [REQUIRED]
            The minimum number of instances to launch. If you specify a minimum that is more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches no instances.
            Constraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 General FAQ.
            
    :type MinCount: integer
    :param MaxCount: [REQUIRED]
            The maximum number of instances to launch. If you specify more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches the largest possible number of instances above MinCount .
            Constraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 FAQ.
            
    :type MaxCount: integer
    :param KeyName: The name of the key pair. You can create a key pair using CreateKeyPair or ImportKeyPair .
            Warning
            If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.
            
    :type KeyName: string
    :param SecurityGroups: [EC2-Classic, default VPC] One or more security group names. For a nondefault VPC, you must use security group IDs instead.
            Default: Amazon EC2 uses the default security group.
            (string) --
            
    :type SecurityGroups: list
    :param SecurityGroupIds: One or more security group IDs. You can create a security group using CreateSecurityGroup .
            Default: Amazon EC2 uses the default security group.
            (string) --
            
    :type SecurityGroupIds: list
    :param UserData: The user data to make available to the instance. For more information, see Running Commands on Your Linux Instance at Launch (Linux) and Adding User Data (Windows). If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.
            This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.
            
    :type UserData: string
    :param InstanceType: The instance type. For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide .
            Default: m1.small
            
    :type InstanceType: string
    :param Placement: The placement for the instance.
            AvailabilityZone (string) --The Availability Zone of the instance.
            GroupName (string) --The name of the placement group the instance is in (for cluster compute instances).
            Tenancy (string) --The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the ImportInstance command.
            HostId (string) --The ID of the Dedicted host on which the instance resides. This parameter is not support for the ImportInstance command.
            Affinity (string) --The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the ImportInstance command.
            
    :type Placement: dict
    :param KernelId: The ID of the kernel.
            Warning
            We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB in the Amazon Elastic Compute Cloud User Guide .
            
    :type KernelId: string
    :param RamdiskId: The ID of the RAM disk.
            Warning
            We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB in the Amazon Elastic Compute Cloud User Guide .
            
    :type RamdiskId: string
    :param BlockDeviceMappings: The block device mapping.
            Warning
            Supplying both a snapshot ID and an encryption value as arguments for block-device mapping results in an error. This is because only blank volumes can be encrypted on start, and these are not created from a snapshot. If a snapshot is the basis for the volume, it contains data by definition and its encryption status cannot be changed using this action.
            (dict) --Describes a block device mapping.
            VirtualName (string) --The virtual device name (ephemeral N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1 .The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
            Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
            DeviceName (string) --The device name exposed to the instance (for example, /dev/sdh or xvdh ).
            Ebs (dict) --Parameters used to automatically set up EBS volumes when the instance is launched.
            SnapshotId (string) --The ID of the snapshot.
            VolumeSize (integer) --The size of the volume, in GiB.
            Constraints: 1-16384 for General Purpose SSD (gp2 ), 4-16384 for Provisioned IOPS SSD (io1 ), 500-16384 for Throughput Optimized HDD (st1 ), 500-16384 for Cold HDD (sc1 ), and 1-1024 for Magnetic (standard ) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
            Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
            DeleteOnTermination (boolean) --Indicates whether the EBS volume is deleted on instance termination.
            VolumeType (string) --The volume type: gp2 , io1 , st1 , sc1 , or standard .
            Default: standard
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports. For io1 , this represents the number of IOPS that are provisioned for the volume. For gp2 , this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide .
            Constraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes.
            Condition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2 , st1 , sc1 , or standard volumes.
            Encrypted (boolean) --Indicates whether the EBS volume is encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption.
            NoDevice (string) --Suppresses the specified device included in the block device mapping of the AMI.
            
            
    :type BlockDeviceMappings: list
    :param Monitoring: The monitoring for the instance.
            Enabled (boolean) -- [REQUIRED]Indicates whether monitoring is enabled for the instance.
            
    :type Monitoring: dict
    :param SubnetId: [EC2-VPC] The ID of the subnet to launch the instance into.
    :type SubnetId: string
    :param DisableApiTermination: If you set this parameter to true , you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. If you set this parameter to true and then later want to be able to terminate the instance, you must first change the value of the disableApiTermination attribute to false using ModifyInstanceAttribute . Alternatively, if you set InstanceInitiatedShutdownBehavior to terminate , you can terminate the instance by running the shutdown command from the instance.
            Default: false
            
    :type DisableApiTermination: boolean
    :param InstanceInitiatedShutdownBehavior: Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
            Default: stop
            
    :type InstanceInitiatedShutdownBehavior: string
    :param PrivateIpAddress: [EC2-VPC] The primary IP address. You must specify a value from the IP address range of the subnet.
            Only one private IP address can be designated as primary. Therefore, you can't specify this parameter if PrivateIpAddresses.n.Primary is set to true and PrivateIpAddresses.n.PrivateIpAddress is set to an IP address.
            You cannot specify this option if you're launching more than one instance in the request.
            Default: We select an IP address from the IP address range of the subnet.
            
    :type PrivateIpAddress: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency .
            Constraints: Maximum 64 ASCII characters
            
    :type ClientToken: string
    :param AdditionalInfo: Reserved.
    :type AdditionalInfo: string
    :param NetworkInterfaces: One or more network interfaces.
            (dict) --Describes a network interface.
            NetworkInterfaceId (string) --The ID of the network interface.
            DeviceIndex (integer) --The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a RunInstances request, you must provide the device index.
            SubnetId (string) --The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
            Description (string) --The description of the network interface. Applies only if creating a network interface when launching an instance.
            PrivateIpAddress (string) --The private IP address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            Groups (list) --The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
            (string) --
            DeleteOnTermination (boolean) --If set to true , the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.
            PrivateIpAddresses (list) --One or more private IP addresses to assign to the network interface. Only one private IP address can be designated as primary. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            (dict) --Describes a secondary private IP address for a network interface.
            PrivateIpAddress (string) -- [REQUIRED]The private IP addresses.
            Primary (boolean) --Indicates whether the private IP address is the primary private IP address. Only one IP address can be designated as primary.
            
            SecondaryPrivateIpAddressCount (integer) --The number of secondary private IP addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            AssociatePublicIpAddress (boolean) --Indicates whether to assign a public IP address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .
            
            
    :type NetworkInterfaces: list
    :param IamInstanceProfile: The IAM instance profile.
            Arn (string) --The Amazon Resource Name (ARN) of the instance profile.
            Name (string) --The name of the instance profile.
            
    :type IamInstanceProfile: dict
    :param EbsOptimized: Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
            Default: false
            
    :type EbsOptimized: boolean
    """
    pass


def run_scheduled_instances(DryRun=None, ClientToken=None, InstanceCount=None, ScheduledInstanceId=None,
                            LaunchSpecification=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param ClientToken: Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see Ensuring Idempotency .
    :type ClientToken: string
    :param InstanceCount: The number of instances.
            Default: 1
            
    :type InstanceCount: integer
    :param ScheduledInstanceId: [REQUIRED]
            The Scheduled Instance ID.
            
    :type ScheduledInstanceId: string
    :param LaunchSpecification: [REQUIRED]
            The launch specification. You must match the instance type, Availability Zone, network, and platform of the schedule that you purchased.
            ImageId (string) -- [REQUIRED]The ID of the Amazon Machine Image (AMI).
            KeyName (string) --The name of the key pair.
            SecurityGroupIds (list) --The IDs of one or more security groups.
            (string) --
            UserData (string) --The base64-encoded MIME user data.
            Placement (dict) --The placement information.
            AvailabilityZone (string) --The Availability Zone.
            GroupName (string) --The name of the placement group.
            KernelId (string) --The ID of the kernel.
            InstanceType (string) --The instance type.
            RamdiskId (string) --The ID of the RAM disk.
            BlockDeviceMappings (list) --One or more block device mapping entries.
            (dict) --Describes a block device mapping for a Scheduled Instance.
            DeviceName (string) --The device name exposed to the instance (for example, /dev/sdh or xvdh ).
            NoDevice (string) --Suppresses the specified device included in the block device mapping of the AMI.
            VirtualName (string) --The virtual device name (ephemeral N). Instance store volumes are numbered starting from 0. An instance type with two available instance store volumes can specify mappings for ephemeral0 and ephemeral1 .The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
            Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.
            Ebs (dict) --Parameters used to set up EBS volumes automatically when the instance is launched.
            SnapshotId (string) --The ID of the snapshot.
            VolumeSize (integer) --The size of the volume, in GiB.
            Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
            DeleteOnTermination (boolean) --Indicates whether the volume is deleted on instance termination.
            VolumeType (string) --The volume type. gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, Throughput Optimized HDD for st1 , Cold HDD for sc1 , or standard for Magnetic.
            Default: standard
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports. For io1 volumes, this represents the number of IOPS that are provisioned for the volume. For gp2 volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about gp2 baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide .
            Constraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes.
            Condition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2 , st1 , sc1 , or standard volumes.
            Encrypted (boolean) --Indicates whether the volume is encrypted. You can attached encrypted volumes only to instances that support them.
            
            Monitoring (dict) --Enable or disable monitoring for the instances.
            Enabled (boolean) --Indicates whether monitoring is enabled.
            SubnetId (string) --The ID of the subnet in which to launch the instances.
            NetworkInterfaces (list) --One or more network interfaces.
            (dict) --Describes a network interface for a Scheduled Instance.
            NetworkInterfaceId (string) --The ID of the network interface.
            DeviceIndex (integer) --The index of the device for the network interface attachment.
            SubnetId (string) --The ID of the subnet.
            Description (string) --The description.
            PrivateIpAddress (string) --The IP address of the network interface within the subnet.
            PrivateIpAddressConfigs (list) --The private IP addresses.
            (dict) --Describes a private IP address for a Scheduled Instance.
            PrivateIpAddress (string) --The IP address.
            Primary (boolean) --Indicates whether this is a primary IP address. Otherwise, this is a secondary IP address.
            
            SecondaryPrivateIpAddressCount (integer) --The number of secondary private IP addresses.
            AssociatePublicIpAddress (boolean) --Indicates whether to assign a public IP address to instances launched in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .
            Groups (list) --The IDs of one or more security groups.
            (string) --
            DeleteOnTermination (boolean) --Indicates whether to delete the interface when the instance is terminated.
            
            IamInstanceProfile (dict) --The IAM instance profile.
            Arn (string) --The Amazon Resource Name (ARN).
            Name (string) --The name.
            EbsOptimized (boolean) --Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
            Default: false
            
    :type LaunchSpecification: dict
    """
    pass


def start_instances(InstanceIds=None, AdditionalInfo=None, DryRun=None):
    """
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            
    :type InstanceIds: list
    :param AdditionalInfo: Reserved.
    :type AdditionalInfo: string
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    """
    pass


def stop_instances(DryRun=None, InstanceIds=None, Force=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            
    :type InstanceIds: list
    :param Force: Forces the instances to stop. The instances do not have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures. This option is not recommended for Windows instances.
            Default: false
            
    :type Force: boolean
    """
    pass


def terminate_instances(DryRun=None, InstanceIds=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            Constraints: Up to 1000 instance IDs. We recommend breaking up this request into smaller batches.
            (string) --
            
    :type InstanceIds: list
    """
    pass


def unassign_private_ip_addresses(NetworkInterfaceId=None, PrivateIpAddresses=None):
    """
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            
    :type NetworkInterfaceId: string
    :param PrivateIpAddresses: [REQUIRED]
            The secondary private IP addresses to unassign from the network interface. You can specify this option multiple times to unassign more than one IP address.
            (string) --
            
    :type PrivateIpAddresses: list
    """
    pass


def unmonitor_instances(DryRun=None, InstanceIds=None):
    """
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    :type DryRun: boolean
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            
    :type InstanceIds: list
    """
    pass
