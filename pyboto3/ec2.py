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

def accept_reserved_instances_exchange_quote(DryRun=None, ReservedInstanceIds=None, TargetConfigurations=None):
    """
    Accepts the Convertible Reserved Instance exchange quote described in the  GetReservedInstancesExchangeQuote call.
    See also: AWS API Documentation
    
    
    :example: response = client.accept_reserved_instances_exchange_quote(
        DryRun=True|False,
        ReservedInstanceIds=[
            'string',
        ],
        TargetConfigurations=[
            {
                'OfferingId': 'string',
                'InstanceCount': 123
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ReservedInstanceIds: list
    :param ReservedInstanceIds: [REQUIRED]
            The IDs of the Convertible Reserved Instances to exchange for other Convertible Reserved Instances of the same or higher value.
            (string) --
            

    :type TargetConfigurations: list
    :param TargetConfigurations: The configurations of the Convertible Reserved Instance offerings that you are purchasing in this exchange.
            (dict) --Details about the target configuration.
            OfferingId (string) -- [REQUIRED]The Convertible Reserved Instance offering ID.
            InstanceCount (integer) --The number of instances the Covertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request
            
            

    :rtype: dict
    :return: {
        'ExchangeId': 'string'
    }
    
    
    """
    pass

def accept_vpc_peering_connection(DryRun=None, VpcPeeringConnectionId=None):
    """
    Accept a VPC peering connection request. To accept a request, the VPC peering connection must be in the pending-acceptance state, and you must be the owner of the peer VPC. Use  DescribeVpcPeeringConnections to view your outstanding VPC peering connection requests.
    See also: AWS API Documentation
    
    
    :example: response = client.accept_vpc_peering_connection(
        DryRun=True|False,
        VpcPeeringConnectionId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcPeeringConnectionId: string
    :param VpcPeeringConnectionId: The ID of the VPC peering connection.

    :rtype: dict
    :return: {
        'VpcPeeringConnection': {
            'AccepterVpcInfo': {
                'CidrBlock': 'string',
                'OwnerId': 'string',
                'VpcId': 'string',
                'Ipv6CidrBlockSet': [
                    {
                        'Ipv6CidrBlock': 'string'
                    },
                ],
                'PeeringOptions': {
                    'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
                    'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
                    'AllowDnsResolutionFromRemoteVpc': True|False
                }
            },
            'ExpirationTime': datetime(2015, 1, 1),
            'RequesterVpcInfo': {
                'CidrBlock': 'string',
                'OwnerId': 'string',
                'VpcId': 'string',
                'Ipv6CidrBlockSet': [
                    {
                        'Ipv6CidrBlock': 'string'
                    },
                ],
                'PeeringOptions': {
                    'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
                    'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
                    'AllowDnsResolutionFromRemoteVpc': True|False
                }
            },
            'Status': {
                'Code': 'initiating-request'|'pending-acceptance'|'active'|'deleted'|'rejected'|'failed'|'expired'|'provisioning'|'deleting',
                'Message': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'VpcPeeringConnectionId': 'string'
        }
    }
    
    
    """
    pass

def allocate_address(DryRun=None, Domain=None):
    """
    Acquires an Elastic IP address.
    An Elastic IP address is for use either in the EC2-Classic platform or in a VPC. For more information, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example allocates an Elastic IP address to use with an instance in a VPC.
    Expected Output:
    This example allocates an Elastic IP address to use with an instance in EC2-Classic.
    Expected Output:
    
    :example: response = client.allocate_address(
        DryRun=True|False,
        Domain='vpc'|'standard'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Domain: string
    :param Domain: Set to vpc to allocate the address for use with instances in a VPC.
            Default: The address is for use with instances in EC2-Classic.
            

    :rtype: dict
    :return: {
        'PublicIp': 'string',
        'Domain': 'vpc'|'standard',
        'AllocationId': 'string'
    }
    
    
    """
    pass

def allocate_hosts(AutoPlacement=None, ClientToken=None, InstanceType=None, Quantity=None, AvailabilityZone=None):
    """
    Allocates a Dedicated Host to your account. At minimum you need to specify the instance size type, Availability Zone, and quantity of hosts you want to allocate.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_hosts(
        AutoPlacement='on'|'off',
        ClientToken='string',
        InstanceType='string',
        Quantity=123,
        AvailabilityZone='string'
    )
    
    
    :type AutoPlacement: string
    :param AutoPlacement: This is enabled by default. This property allows instances to be automatically placed onto available Dedicated Hosts, when you are launching instances without specifying a host ID.
            Default: Enabled
            

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide .

    :type InstanceType: string
    :param InstanceType: [REQUIRED]
            Specify the instance type that you want your Dedicated Hosts to be configured for. When you specify the instance type, that is the only instance type that you can launch onto that host.
            

    :type Quantity: integer
    :param Quantity: [REQUIRED]
            The number of Dedicated Hosts you want to allocate to your account with these parameters.
            

    :type AvailabilityZone: string
    :param AvailabilityZone: [REQUIRED]
            The Availability Zone for the Dedicated Hosts.
            

    :rtype: dict
    :return: {
        'HostIds': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def assign_ipv6_addresses(NetworkInterfaceId=None, Ipv6Addresses=None, Ipv6AddressCount=None):
    """
    Assigns one or more IPv6 addresses to the specified network interface. You can specify one or more specific IPv6 addresses, or you can specify the number of IPv6 addresses to be automatically assigned from within the subnet's IPv6 CIDR block range. You can assign as many IPv6 addresses to a network interface as you can assign private IPv4 addresses, and the limit varies per instance type. For information, see IP Addresses Per Network Interface Per Instance Type in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.assign_ipv6_addresses(
        NetworkInterfaceId='string',
        Ipv6Addresses=[
            'string',
        ],
        Ipv6AddressCount=123
    )
    
    
    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            

    :type Ipv6Addresses: list
    :param Ipv6Addresses: One or more specific IPv6 addresses to be assigned to the network interface. You can't use this option if you're specifying a number of IPv6 addresses.
            (string) --
            

    :type Ipv6AddressCount: integer
    :param Ipv6AddressCount: The number of IPv6 addresses to assign to the network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.

    :rtype: dict
    :return: {
        'NetworkInterfaceId': 'string',
        'AssignedIpv6Addresses': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def assign_private_ip_addresses(NetworkInterfaceId=None, PrivateIpAddresses=None, SecondaryPrivateIpAddressCount=None, AllowReassignment=None):
    """
    Assigns one or more secondary private IP addresses to the specified network interface. You can specify one or more specific secondary IP addresses, or you can specify the number of secondary IP addresses to be automatically assigned within the subnet's CIDR block range. The number of secondary IP addresses that you can assign to an instance varies by instance type. For information about instance types, see Instance Types in the Amazon Elastic Compute Cloud User Guide . For more information about Elastic IP addresses, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide .
    AssignPrivateIpAddresses is available only in EC2-VPC.
    See also: AWS API Documentation
    
    Examples
    This example assigns the specified secondary private IP address to the specified network interface.
    Expected Output:
    This example assigns two secondary private IP addresses to the specified network interface. Amazon EC2 automatically assigns these IP addresses from the available IP addresses in the CIDR block range of the subnet the network interface is associated with.
    Expected Output:
    
    :example: response = client.assign_private_ip_addresses(
        NetworkInterfaceId='string',
        PrivateIpAddresses=[
            'string',
        ],
        SecondaryPrivateIpAddressCount=123,
        AllowReassignment=True|False
    )
    
    
    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            

    :type PrivateIpAddresses: list
    :param PrivateIpAddresses: One or more IP addresses to be assigned as a secondary private IP address to the network interface. You can't specify this parameter when also specifying a number of secondary IP addresses.
            If you don't specify an IP address, Amazon EC2 automatically selects an IP address within the subnet range.
            (string) --
            

    :type SecondaryPrivateIpAddressCount: integer
    :param SecondaryPrivateIpAddressCount: The number of secondary IP addresses to assign to the network interface. You can't specify this parameter when also specifying private IP addresses.

    :type AllowReassignment: boolean
    :param AllowReassignment: Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.

    :return: response = client.assign_private_ip_addresses(
        NetworkInterfaceId='eni-e5aa89a3',
        PrivateIpAddresses=[
            '10.0.0.82',
        ],
    )
    
    print(response)
    
    
    """
    pass

def associate_address(DryRun=None, InstanceId=None, PublicIp=None, AllocationId=None, NetworkInterfaceId=None, PrivateIpAddress=None, AllowReassociation=None):
    """
    Associates an Elastic IP address with an instance or a network interface.
    An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide .
    [EC2-Classic, VPC in an EC2-VPC-only account] If the Elastic IP address is already associated with a different instance, it is disassociated from that instance and associated with the specified instance. If you associate an Elastic IP address with an instance that has an existing Elastic IP address, the existing address is disassociated from the instance, but remains allocated to your account.
    [VPC in an EC2-Classic account] If you don't specify a private IP address, the Elastic IP address is associated with the primary IP address. If the Elastic IP address is already associated with a different instance or a network interface, you get an error unless you allow reassociation. You cannot associate an Elastic IP address with an instance or network interface that has an existing Elastic IP address.
    See also: AWS API Documentation
    
    Examples
    This example associates the specified Elastic IP address with the specified instance in a VPC.
    Expected Output:
    This example associates the specified Elastic IP address with the specified network interface.
    Expected Output:
    This example associates an Elastic IP address with an instance in EC2-Classic.
    Expected Output:
    
    :example: response = client.associate_address(
        DryRun=True|False,
        InstanceId='string',
        PublicIp='string',
        AllocationId='string',
        NetworkInterfaceId='string',
        PrivateIpAddress='string',
        AllowReassociation=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: The ID of the instance. This is required for EC2-Classic. For EC2-VPC, you can specify either the instance ID or the network interface ID, but not both. The operation fails if you specify an instance ID unless exactly one network interface is attached.

    :type PublicIp: string
    :param PublicIp: The Elastic IP address. This is required for EC2-Classic.

    :type AllocationId: string
    :param AllocationId: [EC2-VPC] The allocation ID. This is required for EC2-VPC.

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [EC2-VPC] The ID of the network interface. If the instance has more than one network interface, you must specify a network interface ID.

    :type PrivateIpAddress: string
    :param PrivateIpAddress: [EC2-VPC] The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.

    :type AllowReassociation: boolean
    :param AllowReassociation: [EC2-VPC] For a VPC in an EC2-Classic account, specify true to allow an Elastic IP address that is already associated with an instance or network interface to be reassociated with the specified instance or network interface. Otherwise, the operation fails. In a VPC in an EC2-VPC-only account, reassociation is automatic, therefore you can specify false to ensure the operation fails if the Elastic IP address is already associated with another resource.

    :rtype: dict
    :return: {
        'AssociationId': 'string'
    }
    
    
    """
    pass

def associate_dhcp_options(DryRun=None, DhcpOptionsId=None, VpcId=None):
    """
    Associates a set of DHCP options (that you've previously created) with the specified VPC, or associates no DHCP options with the VPC.
    After you associate the options with the VPC, any existing instances and all new instances that you launch in that VPC use the options. You don't need to restart or relaunch the instances. They automatically pick up the changes within a few hours, depending on how frequently the instance renews its DHCP lease. You can explicitly renew the lease using the operating system on the instance.
    For more information, see DHCP Options Sets in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example associates the specified DHCP options set with the specified VPC.
    Expected Output:
    This example associates the default DHCP options set with the specified VPC.
    Expected Output:
    
    :example: response = client.associate_dhcp_options(
        DryRun=True|False,
        DhcpOptionsId='string',
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type DhcpOptionsId: string
    :param DhcpOptionsId: [REQUIRED]
            The ID of the DHCP options set, or default to associate no DHCP options with the VPC.
            

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :return: response = client.associate_dhcp_options(
        DhcpOptionsId='dopt-d9070ebb',
        VpcId='vpc-a01106c2',
    )
    
    print(response)
    
    
    """
    pass

def associate_iam_instance_profile(IamInstanceProfile=None, InstanceId=None):
    """
    Associates an IAM instance profile with a running or stopped instance. You cannot associate more than one IAM instance profile with an instance.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_iam_instance_profile(
        IamInstanceProfile={
            'Arn': 'string',
            'Name': 'string'
        },
        InstanceId='string'
    )
    
    
    :type IamInstanceProfile: dict
    :param IamInstanceProfile: [REQUIRED]
            The IAM instance profile.
            Arn (string) --The Amazon Resource Name (ARN) of the instance profile.
            Name (string) --The name of the instance profile.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :rtype: dict
    :return: {
        'IamInstanceProfileAssociation': {
            'AssociationId': 'string',
            'InstanceId': 'string',
            'IamInstanceProfile': {
                'Arn': 'string',
                'Id': 'string'
            },
            'State': 'associating'|'associated'|'disassociating'|'disassociated',
            'Timestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def associate_route_table(DryRun=None, SubnetId=None, RouteTableId=None):
    """
    Associates a subnet with a route table. The subnet and route table must be in the same VPC. This association causes traffic originating from the subnet to be routed according to the routes in the route table. The action returns an association ID, which you need in order to disassociate the route table from the subnet later. A route table can be associated with multiple subnets.
    For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example associates the specified route table with the specified subnet.
    Expected Output:
    
    :example: response = client.associate_route_table(
        DryRun=True|False,
        SubnetId='string',
        RouteTableId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SubnetId: string
    :param SubnetId: [REQUIRED]
            The ID of the subnet.
            

    :type RouteTableId: string
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            

    :rtype: dict
    :return: {
        'AssociationId': 'string'
    }
    
    
    """
    pass

def associate_subnet_cidr_block(SubnetId=None, Ipv6CidrBlock=None):
    """
    Associates a CIDR block with your subnet. You can only associate a single IPv6 CIDR block with your subnet. An IPv6 CIDR block must have a prefix length of /64.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_subnet_cidr_block(
        SubnetId='string',
        Ipv6CidrBlock='string'
    )
    
    
    :type SubnetId: string
    :param SubnetId: [REQUIRED]
            The ID of your subnet.
            

    :type Ipv6CidrBlock: string
    :param Ipv6CidrBlock: [REQUIRED]
            The IPv6 CIDR block for your subnet. The subnet must have a /64 prefix length.
            

    :rtype: dict
    :return: {
        'SubnetId': 'string',
        'Ipv6CidrBlockAssociation': {
            'Ipv6CidrBlock': 'string',
            'Ipv6CidrBlockState': {
                'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                'StatusMessage': 'string'
            },
            'AssociationId': 'string'
        }
    }
    
    
    """
    pass

def associate_vpc_cidr_block(VpcId=None, AmazonProvidedIpv6CidrBlock=None):
    """
    Associates a CIDR block with your VPC. You can only associate a single Amazon-provided IPv6 CIDR block with your VPC. The IPv6 CIDR block size is fixed at /56.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_vpc_cidr_block(
        VpcId='string',
        AmazonProvidedIpv6CidrBlock=True|False
    )
    
    
    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :type AmazonProvidedIpv6CidrBlock: boolean
    :param AmazonProvidedIpv6CidrBlock: Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 addresses, or the size of the CIDR block.

    :rtype: dict
    :return: {
        'VpcId': 'string',
        'Ipv6CidrBlockAssociation': {
            'Ipv6CidrBlock': 'string',
            'Ipv6CidrBlockState': {
                'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                'StatusMessage': 'string'
            },
            'AssociationId': 'string'
        }
    }
    
    
    """
    pass

def attach_classic_link_vpc(DryRun=None, InstanceId=None, VpcId=None, Groups=None):
    """
    Links an EC2-Classic instance to a ClassicLink-enabled VPC through one or more of the VPC's security groups. You cannot link an EC2-Classic instance to more than one VPC at a time. You can only link an instance that's in the running state. An instance is automatically unlinked from a VPC when it's stopped - you can link it to the VPC again when you restart it.
    After you've linked an instance, you cannot change the VPC security groups that are associated with it. To change the security groups, you must first unlink the instance, and then link it again.
    Linking your instance to a VPC is sometimes referred to as attaching your instance.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_classic_link_vpc(
        DryRun=True|False,
        InstanceId='string',
        VpcId='string',
        Groups=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of an EC2-Classic instance to link to the ClassicLink-enabled VPC.
            

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of a ClassicLink-enabled VPC.
            

    :type Groups: list
    :param Groups: [REQUIRED]
            The ID of one or more of the VPC's security groups. You cannot specify security groups from a different VPC.
            (string) --
            

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def attach_internet_gateway(DryRun=None, InternetGatewayId=None, VpcId=None):
    """
    Attaches an Internet gateway to a VPC, enabling connectivity between the Internet and the VPC. For more information about your VPC and Internet gateway, see the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example attaches the specified Internet gateway to the specified VPC.
    Expected Output:
    
    :example: response = client.attach_internet_gateway(
        DryRun=True|False,
        InternetGatewayId='string',
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InternetGatewayId: string
    :param InternetGatewayId: [REQUIRED]
            The ID of the Internet gateway.
            

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :return: response = client.attach_internet_gateway(
        InternetGatewayId='igw-c0a643a9',
        VpcId='vpc-a01106c2',
    )
    
    print(response)
    
    
    """
    pass

def attach_network_interface(DryRun=None, NetworkInterfaceId=None, InstanceId=None, DeviceIndex=None):
    """
    Attaches a network interface to an instance.
    See also: AWS API Documentation
    
    Examples
    This example attaches the specified network interface to the specified instance.
    Expected Output:
    
    :example: response = client.attach_network_interface(
        DryRun=True|False,
        NetworkInterfaceId='string',
        InstanceId='string',
        DeviceIndex=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type DeviceIndex: integer
    :param DeviceIndex: [REQUIRED]
            The index of the device for the network interface attachment.
            

    :rtype: dict
    :return: {
        'AttachmentId': 'string'
    }
    
    
    """
    pass

def attach_volume(DryRun=None, VolumeId=None, InstanceId=None, Device=None):
    """
    Attaches an EBS volume to a running or stopped instance and exposes it to the instance with the specified device name.
    Encrypted EBS volumes may only be attached to instances that support Amazon EBS encryption. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .
    For a list of supported device names, see Attaching an EBS Volume to an Instance . Any device names that aren't reserved for instance store volumes can be used for EBS volumes. For more information, see Amazon EC2 Instance Store in the Amazon Elastic Compute Cloud User Guide .
    If a volume has an AWS Marketplace product code:
    For an overview of the AWS Marketplace, see Introducing AWS Marketplace .
    For more information about EBS volumes, see Attaching Amazon EBS Volumes in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example attaches a volume (vol-1234567890abcdef0) to an instance (i-01474ef662b89480) as /dev/sdf.
    Expected Output:
    
    :example: response = client.attach_volume(
        DryRun=True|False,
        VolumeId='string',
        InstanceId='string',
        Device='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeId: string
    :param VolumeId: [REQUIRED]
            The ID of the EBS volume. The volume and instance must be within the same Availability Zone.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type Device: string
    :param Device: [REQUIRED]
            The device name to expose to the instance (for example, /dev/sdh or xvdh ).
            

    :rtype: dict
    :return: {
        'VolumeId': 'string',
        'InstanceId': 'string',
        'Device': 'string',
        'State': 'attaching'|'attached'|'detaching'|'detached',
        'AttachTime': datetime(2015, 1, 1),
        'DeleteOnTermination': True|False
    }
    
    
    :returns: 
    DryRun (boolean) -- Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    VolumeId (string) -- [REQUIRED]
    The ID of the EBS volume. The volume and instance must be within the same Availability Zone.
    
    InstanceId (string) -- [REQUIRED]
    The ID of the instance.
    
    Device (string) -- [REQUIRED]
    The device name to expose to the instance (for example, /dev/sdh or xvdh ).
    
    
    """
    pass

def attach_vpn_gateway(DryRun=None, VpnGatewayId=None, VpcId=None):
    """
    Attaches a virtual private gateway to a VPC. You can attach one virtual private gateway to one VPC at a time.
    For more information, see Adding a Hardware Virtual Private Gateway to Your VPC in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.attach_vpn_gateway(
        DryRun=True|False,
        VpnGatewayId='string',
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpnGatewayId: string
    :param VpnGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :rtype: dict
    :return: {
        'VpcAttachment': {
            'VpcId': 'string',
            'State': 'attaching'|'attached'|'detaching'|'detached'
        }
    }
    
    
    """
    pass

def authorize_security_group_egress(DryRun=None, GroupId=None, SourceSecurityGroupName=None, SourceSecurityGroupOwnerId=None, IpProtocol=None, FromPort=None, ToPort=None, CidrIp=None, IpPermissions=None):
    """
    [EC2-VPC only] Adds one or more egress rules to a security group for use with a VPC. Specifically, this action permits instances to send traffic to one or more destination IPv4 or IPv6 CIDR address ranges, or to one or more destination security groups for the same VPC. This action doesn't apply to security groups for use in EC2-Classic. For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide . For more information about security group limits, see Amazon VPC Limits .
    Each rule consists of the protocol (for example, TCP), plus either a CIDR range or a source group. For the TCP and UDP protocols, you must also specify the destination port or port range. For the ICMP protocol, you must also specify the ICMP type and code. You can use -1 for the type or code to mean all types or all codes.
    Rule changes are propagated to affected instances as quickly as possible. However, a small delay might occur.
    See also: AWS API Documentation
    
    
    :example: response = client.authorize_security_group_egress(
        DryRun=True|False,
        GroupId='string',
        SourceSecurityGroupName='string',
        SourceSecurityGroupOwnerId='string',
        IpProtocol='string',
        FromPort=123,
        ToPort=123,
        CidrIp='string',
        IpPermissions=[
            {
                'IpProtocol': 'string',
                'FromPort': 123,
                'ToPort': 123,
                'UserIdGroupPairs': [
                    {
                        'UserId': 'string',
                        'GroupName': 'string',
                        'GroupId': 'string',
                        'VpcId': 'string',
                        'VpcPeeringConnectionId': 'string',
                        'PeeringStatus': 'string'
                    },
                ],
                'IpRanges': [
                    {
                        'CidrIp': 'string'
                    },
                ],
                'Ipv6Ranges': [
                    {
                        'CidrIpv6': 'string'
                    },
                ],
                'PrefixListIds': [
                    {
                        'PrefixListId': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupId: string
    :param GroupId: [REQUIRED]
            The ID of the security group.
            

    :type SourceSecurityGroupName: string
    :param SourceSecurityGroupName: The name of a destination security group. To authorize outbound access to a destination security group, we recommend that you use a set of IP permissions instead.

    :type SourceSecurityGroupOwnerId: string
    :param SourceSecurityGroupOwnerId: The AWS account number for a destination security group. To authorize outbound access to a destination security group, we recommend that you use a set of IP permissions instead.

    :type IpProtocol: string
    :param IpProtocol: The IP protocol name or number. We recommend that you specify the protocol in a set of IP permissions instead.

    :type FromPort: integer
    :param FromPort: The start of port range for the TCP and UDP protocols, or an ICMP type number. We recommend that you specify the port range in a set of IP permissions instead.

    :type ToPort: integer
    :param ToPort: The end of port range for the TCP and UDP protocols, or an ICMP type number. We recommend that you specify the port range in a set of IP permissions instead.

    :type CidrIp: string
    :param CidrIp: The CIDR IPv4 address range. We recommend that you specify the CIDR range in a set of IP permissions instead.

    :type IpPermissions: list
    :param IpPermissions: A set of IP permissions. You can't specify a destination security group and a CIDR IP address range.
            (dict) --Describes a security group rule.
            IpProtocol (string) --The IP protocol name (tcp , udp , icmp ) or number (see Protocol Numbers ).
            [EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp , udp , icmp , or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp , udp , and icmp , you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules.
            FromPort (integer) --The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types.
            ToPort (integer) --The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type.
            UserIdGroupPairs (list) --One or more security group and AWS account ID pairs.
            (dict) --Describes a security group and AWS account ID pair.
            UserId (string) --The ID of an AWS account. For a referenced security group in another VPC, the account ID of the referenced security group is returned.
            [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
            GroupName (string) --The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.
            GroupId (string) --The ID of the security group.
            VpcId (string) --The ID of the VPC for the referenced security group, if applicable.
            VpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.
            PeeringStatus (string) --The status of a VPC peering connection, if applicable.
            
            IpRanges (list) --One or more IPv4 ranges.
            (dict) --Describes an IPv4 range.
            CidrIp (string) --The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix.
            
            Ipv6Ranges (list) --[EC2-VPC only] One or more IPv6 ranges.
            (dict) --[EC2-VPC only] Describes an IPv6 range.
            CidrIpv6 (string) --The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix.
            
            PrefixListIds (list) --(Valid for AuthorizeSecurityGroupEgress , RevokeSecurityGroupEgress and DescribeSecurityGroups only) One or more prefix list IDs for an AWS service. In an AuthorizeSecurityGroupEgress request, this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
            (dict) --The ID of the prefix.
            PrefixListId (string) --The ID of the prefix.
            
            
            

    """
    pass

def authorize_security_group_ingress(DryRun=None, GroupName=None, GroupId=None, SourceSecurityGroupName=None, SourceSecurityGroupOwnerId=None, IpProtocol=None, FromPort=None, ToPort=None, CidrIp=None, IpPermissions=None):
    """
    Adds one or more ingress rules to a security group.
    Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.
    [EC2-Classic] This action gives one or more IPv4 CIDR address ranges permission to access a security group in your account, or gives one or more security groups (called the source groups ) permission to access a security group for your account. A source group can be for your own AWS account, or another. You can have up to 100 rules per group.
    [EC2-VPC] This action gives one or more IPv4 or IPv6 CIDR address ranges permission to access a security group in your VPC, or gives one or more other security groups (called the source groups ) permission to access a security group for your VPC. The security groups must all be for the same VPC or a peer VPC in a VPC peering connection. For more information about VPC security group limits, see Amazon VPC Limits .
    See also: AWS API Documentation
    
    
    :example: response = client.authorize_security_group_ingress(
        DryRun=True|False,
        GroupName='string',
        GroupId='string',
        SourceSecurityGroupName='string',
        SourceSecurityGroupOwnerId='string',
        IpProtocol='string',
        FromPort=123,
        ToPort=123,
        CidrIp='string',
        IpPermissions=[
            {
                'IpProtocol': 'string',
                'FromPort': 123,
                'ToPort': 123,
                'UserIdGroupPairs': [
                    {
                        'UserId': 'string',
                        'GroupName': 'string',
                        'GroupId': 'string',
                        'VpcId': 'string',
                        'VpcPeeringConnectionId': 'string',
                        'PeeringStatus': 'string'
                    },
                ],
                'IpRanges': [
                    {
                        'CidrIp': 'string'
                    },
                ],
                'Ipv6Ranges': [
                    {
                        'CidrIpv6': 'string'
                    },
                ],
                'PrefixListIds': [
                    {
                        'PrefixListId': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupName: string
    :param GroupName: [EC2-Classic, default VPC] The name of the security group.

    :type GroupId: string
    :param GroupId: The ID of the security group. Required for a nondefault VPC.

    :type SourceSecurityGroupName: string
    :param SourceSecurityGroupName: [EC2-Classic, default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. Creates rules that grant full ICMP, UDP, and TCP access. To create a rule with a specific IP protocol and port range, use a set of IP permissions instead. For EC2-VPC, the source security group must be in the same VPC.

    :type SourceSecurityGroupOwnerId: string
    :param SourceSecurityGroupOwnerId: [EC2-Classic] The AWS account number for the source security group, if the source security group is in a different account. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range. Creates rules that grant full ICMP, UDP, and TCP access. To create a rule with a specific IP protocol and port range, use a set of IP permissions instead.

    :type IpProtocol: string
    :param IpProtocol: The IP protocol name (tcp , udp , icmp ) or number (see Protocol Numbers ). (VPC only) Use -1 to specify all protocols. If you specify -1 , or a protocol number other than tcp , udp , icmp , or 58 (ICMPv6), traffic on all ports is allowed, regardless of any ports you specify. For tcp , udp , and icmp , you must specify a port range. For protocol 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed.

    :type FromPort: integer
    :param FromPort: The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. For the ICMP/ICMPv6 type number, use -1 to specify all types.

    :type ToPort: integer
    :param ToPort: The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code number. For the ICMP/ICMPv6 code number, use -1 to specify all codes.

    :type CidrIp: string
    :param CidrIp: The CIDR IPv4 address range. You can't specify this parameter when specifying a source security group.

    :type IpPermissions: list
    :param IpPermissions: A set of IP permissions. Can be used to specify multiple rules in a single command.
            (dict) --Describes a security group rule.
            IpProtocol (string) --The IP protocol name (tcp , udp , icmp ) or number (see Protocol Numbers ).
            [EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp , udp , icmp , or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp , udp , and icmp , you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules.
            FromPort (integer) --The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types.
            ToPort (integer) --The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type.
            UserIdGroupPairs (list) --One or more security group and AWS account ID pairs.
            (dict) --Describes a security group and AWS account ID pair.
            UserId (string) --The ID of an AWS account. For a referenced security group in another VPC, the account ID of the referenced security group is returned.
            [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
            GroupName (string) --The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.
            GroupId (string) --The ID of the security group.
            VpcId (string) --The ID of the VPC for the referenced security group, if applicable.
            VpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.
            PeeringStatus (string) --The status of a VPC peering connection, if applicable.
            
            IpRanges (list) --One or more IPv4 ranges.
            (dict) --Describes an IPv4 range.
            CidrIp (string) --The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix.
            
            Ipv6Ranges (list) --[EC2-VPC only] One or more IPv6 ranges.
            (dict) --[EC2-VPC only] Describes an IPv6 range.
            CidrIpv6 (string) --The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix.
            
            PrefixListIds (list) --(Valid for AuthorizeSecurityGroupEgress , RevokeSecurityGroupEgress and DescribeSecurityGroups only) One or more prefix list IDs for an AWS service. In an AuthorizeSecurityGroupEgress request, this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
            (dict) --The ID of the prefix.
            PrefixListId (string) --The ID of the prefix.
            
            
            

    """
    pass

def bundle_instance(DryRun=None, InstanceId=None, Storage=None):
    """
    Bundles an Amazon instance store-backed Windows instance.
    During bundling, only the root device volume (C:) is bundled. Data on other instance store volumes is not preserved.
    For more information, see Creating an Instance Store-Backed Windows AMI .
    See also: AWS API Documentation
    
    
    :example: response = client.bundle_instance(
        DryRun=True|False,
        InstanceId='string',
        Storage={
            'S3': {
                'Bucket': 'string',
                'Prefix': 'string',
                'AWSAccessKeyId': 'string',
                'UploadPolicy': b'bytes',
                'UploadPolicySignature': 'string'
            }
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance to bundle.
            Type: String
            Default: None
            Required: Yes
            

    :type Storage: dict
    :param Storage: [REQUIRED]
            The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.
            S3 (dict) --An Amazon S3 storage location.
            Bucket (string) --The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.
            Prefix (string) --The beginning of the file name of the AMI.
            AWSAccessKeyId (string) --The access key ID of the owner of the bucket. Before you specify a value for your access key ID, review and follow the guidance in Best Practices for Managing AWS Access Keys .
            UploadPolicy (bytes) --An Amazon S3 upload policy that gives Amazon EC2 permission to upload items into Amazon S3 on your behalf.
            UploadPolicySignature (string) --The signature of the JSON document.
            
            

    :rtype: dict
    :return: {
        'BundleTask': {
            'InstanceId': 'string',
            'BundleId': 'string',
            'State': 'pending'|'waiting-for-shutdown'|'bundling'|'storing'|'cancelling'|'complete'|'failed',
            'StartTime': datetime(2015, 1, 1),
            'UpdateTime': datetime(2015, 1, 1),
            'Storage': {
                'S3': {
                    'Bucket': 'string',
                    'Prefix': 'string',
                    'AWSAccessKeyId': 'string',
                    'UploadPolicy': b'bytes',
                    'UploadPolicySignature': 'string'
                }
            },
            'Progress': 'string',
            'BundleTaskError': {
                'Code': 'string',
                'Message': 'string'
            }
        }
    }
    
    
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

def cancel_bundle_task(DryRun=None, BundleId=None):
    """
    Cancels a bundling operation for an instance store-backed Windows instance.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_bundle_task(
        DryRun=True|False,
        BundleId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type BundleId: string
    :param BundleId: [REQUIRED]
            The ID of the bundle task.
            

    :rtype: dict
    :return: {
        'BundleTask': {
            'InstanceId': 'string',
            'BundleId': 'string',
            'State': 'pending'|'waiting-for-shutdown'|'bundling'|'storing'|'cancelling'|'complete'|'failed',
            'StartTime': datetime(2015, 1, 1),
            'UpdateTime': datetime(2015, 1, 1),
            'Storage': {
                'S3': {
                    'Bucket': 'string',
                    'Prefix': 'string',
                    'AWSAccessKeyId': 'string',
                    'UploadPolicy': b'bytes',
                    'UploadPolicySignature': 'string'
                }
            },
            'Progress': 'string',
            'BundleTaskError': {
                'Code': 'string',
                'Message': 'string'
            }
        }
    }
    
    
    """
    pass

def cancel_conversion_task(DryRun=None, ConversionTaskId=None, ReasonMessage=None):
    """
    Cancels an active conversion task. The task can be the import of an instance or volume. The action removes all artifacts of the conversion, including a partially uploaded volume or instance. If the conversion is complete or is in the process of transferring the final disk image, the command fails and returns an exception.
    For more information, see Importing a Virtual Machine Using the Amazon EC2 CLI .
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_conversion_task(
        DryRun=True|False,
        ConversionTaskId='string',
        ReasonMessage='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ConversionTaskId: string
    :param ConversionTaskId: [REQUIRED]
            The ID of the conversion task.
            

    :type ReasonMessage: string
    :param ReasonMessage: The reason for canceling the conversion task.

    """
    pass

def cancel_export_task(ExportTaskId=None):
    """
    Cancels an active export task. The request removes all artifacts of the export, including any partially-created Amazon S3 objects. If the export task is complete or is in the process of transferring the final disk image, the command fails and returns an error.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_export_task(
        ExportTaskId='string'
    )
    
    
    :type ExportTaskId: string
    :param ExportTaskId: [REQUIRED]
            The ID of the export task. This is the ID returned by CreateInstanceExportTask .
            

    """
    pass

def cancel_import_task(DryRun=None, ImportTaskId=None, CancelReason=None):
    """
    Cancels an in-process import virtual machine or import snapshot task.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_import_task(
        DryRun=True|False,
        ImportTaskId='string',
        CancelReason='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImportTaskId: string
    :param ImportTaskId: The ID of the import image or import snapshot task to be canceled.

    :type CancelReason: string
    :param CancelReason: The reason for canceling the task.

    :rtype: dict
    :return: {
        'ImportTaskId': 'string',
        'State': 'string',
        'PreviousState': 'string'
    }
    
    
    """
    pass

def cancel_reserved_instances_listing(ReservedInstancesListingId=None):
    """
    Cancels the specified Reserved Instance listing in the Reserved Instance Marketplace.
    For more information, see Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_reserved_instances_listing(
        ReservedInstancesListingId='string'
    )
    
    
    :type ReservedInstancesListingId: string
    :param ReservedInstancesListingId: [REQUIRED]
            The ID of the Reserved Instance listing.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def cancel_spot_fleet_requests(DryRun=None, SpotFleetRequestIds=None, TerminateInstances=None):
    """
    Cancels the specified Spot fleet requests.
    After you cancel a Spot fleet request, the Spot fleet launches no new Spot instances. You must specify whether the Spot fleet should also terminate its Spot instances. If you terminate the instances, the Spot fleet request enters the cancelled_terminating state. Otherwise, the Spot fleet request enters the cancelled_running state and the instances continue to run until they are interrupted or you terminate them manually.
    See also: AWS API Documentation
    
    Examples
    This example cancels the specified Spot fleet request and terminates its associated Spot Instances.
    Expected Output:
    This example cancels the specified Spot fleet request without terminating its associated Spot Instances.
    Expected Output:
    
    :example: response = client.cancel_spot_fleet_requests(
        DryRun=True|False,
        SpotFleetRequestIds=[
            'string',
        ],
        TerminateInstances=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SpotFleetRequestIds: list
    :param SpotFleetRequestIds: [REQUIRED]
            The IDs of the Spot fleet requests.
            (string) --
            

    :type TerminateInstances: boolean
    :param TerminateInstances: [REQUIRED]
            Indicates whether to terminate instances for a Spot fleet request if it is canceled successfully.
            

    :rtype: dict
    :return: {
        'UnsuccessfulFleetRequests': [
            {
                'SpotFleetRequestId': 'string',
                'Error': {
                    'Code': 'fleetRequestIdDoesNotExist'|'fleetRequestIdMalformed'|'fleetRequestNotInCancellableState'|'unexpectedError',
                    'Message': 'string'
                }
            },
        ],
        'SuccessfulFleetRequests': [
            {
                'SpotFleetRequestId': 'string',
                'CurrentSpotFleetRequestState': 'submitted'|'active'|'cancelled'|'failed'|'cancelled_running'|'cancelled_terminating'|'modifying',
                'PreviousSpotFleetRequestState': 'submitted'|'active'|'cancelled'|'failed'|'cancelled_running'|'cancelled_terminating'|'modifying'
            },
        ]
    }
    
    
    """
    pass

def cancel_spot_instance_requests(DryRun=None, SpotInstanceRequestIds=None):
    """
    Cancels one or more Spot instance requests. Spot instances are instances that Amazon EC2 starts on your behalf when the bid price that you specify exceeds the current Spot price. Amazon EC2 periodically sets the Spot price based on available Spot instance capacity and current Spot instance requests. For more information, see Spot Instance Requests in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example cancels a Spot Instance request.
    Expected Output:
    
    :example: response = client.cancel_spot_instance_requests(
        DryRun=True|False,
        SpotInstanceRequestIds=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SpotInstanceRequestIds: list
    :param SpotInstanceRequestIds: [REQUIRED]
            One or more Spot instance request IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'CancelledSpotInstanceRequests': [
            {
                'SpotInstanceRequestId': 'string',
                'State': 'active'|'open'|'closed'|'cancelled'|'completed'
            },
        ]
    }
    
    
    """
    pass

def confirm_product_instance(DryRun=None, ProductCode=None, InstanceId=None):
    """
    Determines whether a product code is associated with an instance. This action can only be used by the owner of the product code. It is useful when a product code owner needs to verify whether another user's instance is eligible for support.
    See also: AWS API Documentation
    
    Examples
    This example determines whether the specified product code is associated with the specified instance.
    Expected Output:
    
    :example: response = client.confirm_product_instance(
        DryRun=True|False,
        ProductCode='string',
        InstanceId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ProductCode: string
    :param ProductCode: [REQUIRED]
            The product code. This must be a product code that you own.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :rtype: dict
    :return: {
        'OwnerId': 'string',
        'Return': True|False
    }
    
    
    """
    pass

def copy_image(DryRun=None, SourceRegion=None, SourceImageId=None, Name=None, Description=None, ClientToken=None, Encrypted=None, KmsKeyId=None):
    """
    Initiates the copy of an AMI from the specified source region to the current region. You specify the destination region by using its endpoint when making the request.
    For more information, see Copying AMIs in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.copy_image(
        DryRun=True|False,
        SourceRegion='string',
        SourceImageId='string',
        Name='string',
        Description='string',
        ClientToken='string',
        Encrypted=True|False,
        KmsKeyId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SourceRegion: string
    :param SourceRegion: [REQUIRED]
            The name of the region that contains the AMI to copy.
            

    :type SourceImageId: string
    :param SourceImageId: [REQUIRED]
            The ID of the AMI to copy.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the new AMI in the destination region.
            

    :type Description: string
    :param Description: A description for the new AMI in the destination region.

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide .

    :type Encrypted: boolean
    :param Encrypted: Specifies whether the destination snapshots of the copied image should be encrypted. The default CMK for EBS is used unless a non-default AWS Key Management Service (AWS KMS) CMK is specified with KmsKeyId . For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .

    :type KmsKeyId: string
    :param KmsKeyId: The full ARN of the AWS Key Management Service (AWS KMS) CMK to use when encrypting the snapshots of an image during a copy operation. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. The ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1 :012345678910 :key/abcd1234-a123-456a-a12b-a123b4cd56ef . The specified CMK must exist in the region that the snapshot is being copied to. If a KmsKeyId is specified, the Encrypted flag must also be set.

    :rtype: dict
    :return: {
        'ImageId': 'string'
    }
    
    
    """
    pass

def copy_snapshot(DryRun=None, SourceRegion=None, SourceSnapshotId=None, Description=None, DestinationRegion=None, PresignedUrl=None, Encrypted=None, KmsKeyId=None):
    """
    Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3. You can copy the snapshot within the same region or from one region to another. You can use the snapshot to create EBS volumes or Amazon Machine Images (AMIs). The snapshot is copied to the regional endpoint that you send the HTTP request to.
    Copies of encrypted EBS snapshots remain encrypted. Copies of unencrypted snapshots remain unencrypted, unless the Encrypted flag is specified during the snapshot copy operation. By default, encrypted snapshot copies use the default AWS Key Management Service (AWS KMS) customer master key (CMK); however, you can specify a non-default CMK with the KmsKeyId parameter.
    For more information, see Copying an Amazon EBS Snapshot in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example copies a snapshot with the snapshot ID of snap-066877671789bd71b from the us-west-2 region to the us-east-1 region and adds a short description to identify the snapshot.
    Expected Output:
    
    :example: response = client.copy_snapshot(
        DryRun=True|False,
        SourceRegion='string',
        SourceSnapshotId='string',
        Description='string',
        Encrypted=True|False,
        KmsKeyId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SourceRegion: string
    :param SourceRegion: [REQUIRED]
            The ID of the region that contains the snapshot to be copied.
            

    :type SourceSnapshotId: string
    :param SourceSnapshotId: [REQUIRED]
            The ID of the EBS snapshot to copy.
            

    :type Description: string
    :param Description: A description for the EBS snapshot.

    :type DestinationRegion: string
    :param DestinationRegion: The destination region to use in the PresignedUrl parameter of a snapshot copy operation. This parameter is only valid for specifying the destination region in a PresignedUrl parameter, where it is required.
            Note
            CopySnapshot sends the snapshot copy to the regional endpoint that you send the HTTP request to, such as ec2.us-east-1.amazonaws.com (in the AWS CLI, this is specified with the --region parameter or the default region in your AWS configuration file).
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            

    :type PresignedUrl: string
    :param PresignedUrl: The pre-signed URL that facilitates copying an encrypted snapshot. This parameter is only required when copying an encrypted snapshot with the Amazon EC2 Query API; it is available as an optional parameter in all other cases. The PresignedUrl should use the snapshot source endpoint, the CopySnapshot action, and include the SourceRegion , SourceSnapshotId , and DestinationRegion parameters. The PresignedUrl must be signed using AWS Signature Version 4. Because EBS snapshots are stored in Amazon S3, the signing algorithm for this parameter uses the same logic that is described in Authenticating Requests by Using Query Parameters (AWS Signature Version 4) in the Amazon Simple Storage Service API Reference . An invalid or improperly signed PresignedUrl will cause the copy operation to fail asynchronously, and the snapshot will move to an error state.
            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required
            

    :type Encrypted: boolean
    :param Encrypted: Specifies whether the destination snapshot should be encrypted. You can encrypt a copy of an unencrypted snapshot using this flag, but you cannot use it to create an unencrypted copy from an encrypted snapshot. Your default CMK for EBS is used unless a non-default AWS Key Management Service (AWS KMS) CMK is specified with KmsKeyId . For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .

    :type KmsKeyId: string
    :param KmsKeyId: The full ARN of the AWS Key Management Service (AWS KMS) CMK to use when creating the snapshot copy. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. The ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1 :012345678910 :key/abcd1234-a123-456a-a12b-a123b4cd56ef . The specified CMK must exist in the region that the snapshot is being copied to. If a KmsKeyId is specified, the Encrypted flag must also be set.

    :rtype: dict
    :return: {
        'SnapshotId': 'string'
    }
    
    
    """
    pass

def create_customer_gateway(DryRun=None, Type=None, PublicIp=None, BgpAsn=None):
    """
    Provides information to AWS about your VPN customer gateway device. The customer gateway is the appliance at your end of the VPN connection. (The device on the AWS side of the VPN connection is the virtual private gateway.) You must provide the Internet-routable IP address of the customer gateway's external interface. The IP address must be static and may be behind a device performing network address translation (NAT).
    For devices that use Border Gateway Protocol (BGP), you can also provide the device's BGP Autonomous System Number (ASN). You can use an existing ASN assigned to your network. If you don't have an ASN already, you can use a private ASN (in the 64512 - 65534 range).
    For more information about VPN customer gateways, see Adding a Hardware Virtual Private Gateway to Your VPC in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a customer gateway with the specified IP address for its outside interface.
    Expected Output:
    
    :example: response = client.create_customer_gateway(
        DryRun=True|False,
        Type='ipsec.1',
        PublicIp='string',
        BgpAsn=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Type: string
    :param Type: [REQUIRED]
            The type of VPN connection that this customer gateway supports (ipsec.1 ).
            

    :type PublicIp: string
    :param PublicIp: [REQUIRED]
            The Internet-routable IP address for the customer gateway's outside interface. The address must be static.
            

    :type BgpAsn: integer
    :param BgpAsn: [REQUIRED]
            For devices that support BGP, the customer gateway's BGP ASN.
            Default: 65000
            

    :rtype: dict
    :return: {
        'CustomerGateway': {
            'CustomerGatewayId': 'string',
            'State': 'string',
            'Type': 'string',
            'IpAddress': 'string',
            'BgpAsn': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_dhcp_options(DryRun=None, DhcpConfigurations=None):
    """
    Creates a set of DHCP options for your VPC. After creating the set, you must associate it with the VPC, causing all existing and new instances that you launch in the VPC to use this set of DHCP options. The following are the individual DHCP options you can specify. For more information about the options, see RFC 2132 .
    Your VPC automatically starts out with a set of DHCP options that includes only a DNS server that we provide (AmazonProvidedDNS). If you create a set of options, and if your VPC has an Internet gateway, make sure to set the domain-name-servers option either to AmazonProvidedDNS or to a domain name server of your choice. For more information about DHCP options, see DHCP Options Sets in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a DHCP options set.
    Expected Output:
    
    :example: response = client.create_dhcp_options(
        DryRun=True|False,
        DhcpConfigurations=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type DhcpConfigurations: list
    :param DhcpConfigurations: [REQUIRED]
            A DHCP configuration option.
            (dict) --
            Key (string) --
            Values (list) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'DhcpOptions': {
            'DhcpOptionsId': 'string',
            'DhcpConfigurations': [
                {
                    'Key': 'string',
                    'Values': [
                        {
                            'Value': 'string'
                        },
                    ]
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
    
    
    :returns: 
    DryRun (boolean) -- Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    DhcpConfigurations (list) -- [REQUIRED]
    A DHCP configuration option.
    
    (dict) --
    Key (string) --
    Values (list) --
    (string) --
    
    
    
    
    
    
    
    """
    pass

def create_egress_only_internet_gateway(DryRun=None, VpcId=None, ClientToken=None):
    """
    [IPv6 only] Creates an egress-only Internet gateway for your VPC. An egress-only Internet gateway is used to enable outbound communication over IPv6 from instances in your VPC to the Internet, and prevents hosts outside of your VPC from initiating an IPv6 connection with your instance.
    See also: AWS API Documentation
    
    
    :example: response = client.create_egress_only_internet_gateway(
        DryRun=True|False,
        VpcId='string',
        ClientToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC for which to create the egress-only Internet gateway.
            

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency .

    :rtype: dict
    :return: {
        'EgressOnlyInternetGateway': {
            'EgressOnlyInternetGatewayId': 'string',
            'Attachments': [
                {
                    'VpcId': 'string',
                    'State': 'attaching'|'attached'|'detaching'|'detached'
                },
            ]
        },
        'ClientToken': 'string'
    }
    
    
    """
    pass

def create_flow_logs(ResourceIds=None, ResourceType=None, TrafficType=None, LogGroupName=None, DeliverLogsPermissionArn=None, ClientToken=None):
    """
    Creates one or more flow logs to capture IP traffic for a specific network interface, subnet, or VPC. Flow logs are delivered to a specified log group in Amazon CloudWatch Logs. If you specify a VPC or subnet in the request, a log stream is created in CloudWatch Logs for each network interface in the subnet or VPC. Log streams can include information about accepted and rejected traffic to a network interface. You can view the data in your log streams using Amazon CloudWatch Logs.
    In your request, you must also specify an IAM role that has permission to publish logs to CloudWatch Logs.
    See also: AWS API Documentation
    
    
    :example: response = client.create_flow_logs(
        ResourceIds=[
            'string',
        ],
        ResourceType='VPC'|'Subnet'|'NetworkInterface',
        TrafficType='ACCEPT'|'REJECT'|'ALL',
        LogGroupName='string',
        DeliverLogsPermissionArn='string',
        ClientToken='string'
    )
    
    
    :type ResourceIds: list
    :param ResourceIds: [REQUIRED]
            One or more subnet, network interface, or VPC IDs.
            Constraints: Maximum of 1000 resources
            (string) --
            

    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of resource on which to create the flow log.
            

    :type TrafficType: string
    :param TrafficType: [REQUIRED]
            The type of traffic to log.
            

    :type LogGroupName: string
    :param LogGroupName: [REQUIRED]
            The name of the CloudWatch log group.
            

    :type DeliverLogsPermissionArn: string
    :param DeliverLogsPermissionArn: [REQUIRED]
            The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group.
            

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency .

    :rtype: dict
    :return: {
        'FlowLogIds': [
            'string',
        ],
        'ClientToken': 'string',
        'Unsuccessful': [
            {
                'ResourceId': 'string',
                'Error': {
                    'Code': 'string',
                    'Message': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_fpga_image(DryRun=None, InputStorageLocation=None, LogsStorageLocation=None, Description=None, Name=None, ClientToken=None):
    """
    Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP).
    The create operation is asynchronous. To verify that the AFI is ready for use, check the output logs.
    An AFI contains the FPGA bitstream that is ready to download to an FPGA. You can securely deploy an AFI on one or more FPGA-accelerated instances. For more information, see the AWS FPGA Hardware Development Kit .
    See also: AWS API Documentation
    
    
    :example: response = client.create_fpga_image(
        DryRun=True|False,
        InputStorageLocation={
            'Bucket': 'string',
            'Key': 'string'
        },
        LogsStorageLocation={
            'Bucket': 'string',
            'Key': 'string'
        },
        Description='string',
        Name='string',
        ClientToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InputStorageLocation: dict
    :param InputStorageLocation: [REQUIRED]
            The location of the encrypted design checkpoint in Amazon S3. The input must be a tarball.
            Bucket (string) --The name of the S3 bucket.
            Key (string) --The key.
            

    :type LogsStorageLocation: dict
    :param LogsStorageLocation: The location in Amazon S3 for the output logs.
            Bucket (string) --The name of the S3 bucket.
            Key (string) --The key.
            

    :type Description: string
    :param Description: A description for the AFI.

    :type Name: string
    :param Name: A name for the AFI.

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency .

    :rtype: dict
    :return: {
        'FpgaImageId': 'string',
        'FpgaImageGlobalId': 'string'
    }
    
    
    """
    pass

def create_image(DryRun=None, InstanceId=None, Name=None, Description=None, NoReboot=None, BlockDeviceMappings=None):
    """
    Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped.
    If you customized your instance with instance store volumes or EBS volumes in addition to the root device volume, the new AMI contains block device mapping information for those volumes. When you launch an instance from this new AMI, the instance automatically launches with those additional volumes.
    For more information, see Creating Amazon EBS-Backed Linux AMIs in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_image(
        DryRun=True|False,
        InstanceId='string',
        Name='string',
        Description='string',
        NoReboot=True|False,
        BlockDeviceMappings=[
            {
                'VirtualName': 'string',
                'DeviceName': 'string',
                'Ebs': {
                    'SnapshotId': 'string',
                    'VolumeSize': 123,
                    'DeleteOnTermination': True|False,
                    'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                    'Iops': 123,
                    'Encrypted': True|False
                },
                'NoDevice': 'string'
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type Name: string
    :param Name: [REQUIRED]
            A name for the new image.
            Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)
            

    :type Description: string
    :param Description: A description for the new image.

    :type NoReboot: boolean
    :param NoReboot: By default, Amazon EC2 attempts to shut down and reboot the instance before creating the image. If the 'No Reboot' option is set, Amazon EC2 doesn't shut down the instance before creating the image. When this option is used, file system integrity on the created image can't be guaranteed.

    :type BlockDeviceMappings: list
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
            
            

    :rtype: dict
    :return: {
        'ImageId': 'string'
    }
    
    
    """
    pass

def create_instance_export_task(Description=None, InstanceId=None, TargetEnvironment=None, ExportToS3Task=None):
    """
    Exports a running or stopped instance to an S3 bucket.
    For information about the supported operating systems, image formats, and known limitations for the types of instances you can export, see Exporting an Instance as a VM Using VM Import/Export in the VM Import/Export User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_instance_export_task(
        Description='string',
        InstanceId='string',
        TargetEnvironment='citrix'|'vmware'|'microsoft',
        ExportToS3Task={
            'DiskImageFormat': 'VMDK'|'RAW'|'VHD',
            'ContainerFormat': 'ova',
            'S3Bucket': 'string',
            'S3Prefix': 'string'
        }
    )
    
    
    :type Description: string
    :param Description: A description for the conversion task or the resource being exported. The maximum length is 255 bytes.

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type TargetEnvironment: string
    :param TargetEnvironment: The target virtualization environment.

    :type ExportToS3Task: dict
    :param ExportToS3Task: The format and location for an instance export task.
            DiskImageFormat (string) --The format for the exported image.
            ContainerFormat (string) --The container format used to combine disk images with metadata (such as OVF). If absent, only the disk image is exported.
            S3Bucket (string) --The S3 bucket for the destination image. The destination bucket must exist and grant WRITE and READ_ACP permissions to the AWS account vm-import-export@amazon.com .
            S3Prefix (string) --The image is written to a single object in the S3 bucket at the S3 key s3prefix + exportTaskId + '.' + diskImageFormat.
            

    :rtype: dict
    :return: {
        'ExportTask': {
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
        }
    }
    
    
    """
    pass

def create_internet_gateway(DryRun=None):
    """
    Creates an Internet gateway for use with a VPC. After creating the Internet gateway, you attach it to a VPC using  AttachInternetGateway .
    For more information about your VPC and Internet gateway, see the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates an Internet gateway.
    Expected Output:
    
    :example: response = client.create_internet_gateway(
        DryRun=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def create_key_pair(DryRun=None, KeyName=None):
    """
    Creates a 2048-bit RSA key pair with the specified name. Amazon EC2 stores the public key and displays the private key for you to save to a file. The private key is returned as an unencrypted PEM encoded PKCS#8 private key. If a key with the specified name already exists, Amazon EC2 returns an error.
    You can have up to five thousand key pairs per region.
    The key pair returned to you is available only in the region in which you create it. To create a key pair that is available in all regions, use  ImportKeyPair .
    For more information about key pairs, see Key Pairs in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a key pair named my-key-pair.
    Expected Output:
    
    :example: response = client.create_key_pair(
        DryRun=True|False,
        KeyName='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type KeyName: string
    :param KeyName: [REQUIRED]
            A unique name for the key pair.
            Constraints: Up to 255 ASCII characters
            

    :rtype: dict
    :return: {
        'KeyName': 'string',
        'KeyFingerprint': 'string',
        'KeyMaterial': 'string'
    }
    
    
    """
    pass

def create_nat_gateway(SubnetId=None, AllocationId=None, ClientToken=None):
    """
    Creates a NAT gateway in the specified subnet. A NAT gateway can be used to enable instances in a private subnet to connect to the Internet. This action creates a network interface in the specified subnet with a private IP address from the IP address range of the subnet. For more information, see NAT Gateways in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a NAT gateway in subnet subnet-1a2b3c4d and associates an Elastic IP address with the allocation ID eipalloc-37fc1a52 with the NAT gateway.
    Expected Output:
    
    :example: response = client.create_nat_gateway(
        SubnetId='string',
        AllocationId='string',
        ClientToken='string'
    )
    
    
    :type SubnetId: string
    :param SubnetId: [REQUIRED]
            The subnet in which to create the NAT gateway.
            

    :type AllocationId: string
    :param AllocationId: [REQUIRED]
            The allocation ID of an Elastic IP address to associate with the NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it.
            

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency .
            Constraint: Maximum 64 ASCII characters.
            

    :rtype: dict
    :return: {
        'NatGateway': {
            'VpcId': 'string',
            'SubnetId': 'string',
            'NatGatewayId': 'string',
            'CreateTime': datetime(2015, 1, 1),
            'DeleteTime': datetime(2015, 1, 1),
            'NatGatewayAddresses': [
                {
                    'PublicIp': 'string',
                    'AllocationId': 'string',
                    'PrivateIp': 'string',
                    'NetworkInterfaceId': 'string'
                },
            ],
            'State': 'pending'|'failed'|'available'|'deleting'|'deleted',
            'FailureCode': 'string',
            'FailureMessage': 'string',
            'ProvisionedBandwidth': {
                'Provisioned': 'string',
                'Requested': 'string',
                'RequestTime': datetime(2015, 1, 1),
                'ProvisionTime': datetime(2015, 1, 1),
                'Status': 'string'
            }
        },
        'ClientToken': 'string'
    }
    
    
    :returns: 
    pending : The NAT gateway is being created and is not ready to process traffic.
    failed : The NAT gateway could not be created. Check the failureCode and failureMessage fields for the reason.
    available : The NAT gateway is able to process traffic. This status remains until you delete the NAT gateway, and does not indicate the health of the NAT gateway.
    deleting : The NAT gateway is in the process of being terminated and may still be processing traffic.
    deleted : The NAT gateway has been terminated and is no longer processing traffic.
    
    """
    pass

def create_network_acl(DryRun=None, VpcId=None):
    """
    Creates a network ACL in a VPC. Network ACLs provide an optional layer of security (in addition to security groups) for the instances in your VPC.
    For more information about network ACLs, see Network ACLs in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a network ACL for the specified VPC.
    Expected Output:
    
    :example: response = client.create_network_acl(
        DryRun=True|False,
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :rtype: dict
    :return: {
        'NetworkAcl': {
            'NetworkAclId': 'string',
            'VpcId': 'string',
            'IsDefault': True|False,
            'Entries': [
                {
                    'RuleNumber': 123,
                    'Protocol': 'string',
                    'RuleAction': 'allow'|'deny',
                    'Egress': True|False,
                    'CidrBlock': 'string',
                    'Ipv6CidrBlock': 'string',
                    'IcmpTypeCode': {
                        'Type': 123,
                        'Code': 123
                    },
                    'PortRange': {
                        'From': 123,
                        'To': 123
                    }
                },
            ],
            'Associations': [
                {
                    'NetworkAclAssociationId': 'string',
                    'NetworkAclId': 'string',
                    'SubnetId': 'string'
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
    
    
    """
    pass

def create_network_acl_entry(DryRun=None, NetworkAclId=None, RuleNumber=None, Protocol=None, RuleAction=None, Egress=None, CidrBlock=None, Ipv6CidrBlock=None, IcmpTypeCode=None, PortRange=None):
    """
    Creates an entry (a rule) in a network ACL with the specified rule number. Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the ACL, we process the entries in the ACL according to the rule numbers, in ascending order. Each network ACL has a set of ingress rules and a separate set of egress rules.
    We recommend that you leave room between the rule numbers (for example, 100, 110, 120, ...), and not number them one right after the other (for example, 101, 102, 103, ...). This makes it easier to add a rule between existing ones without having to renumber the rules.
    After you add an entry, you can't modify it; you must either replace it, or create an entry and delete the old one.
    For more information about network ACLs, see Network ACLs in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates an entry for the specified network ACL. The rule allows ingress traffic from anywhere (0.0.0.0/0) on UDP port 53 (DNS) into any associated subnet.
    Expected Output:
    
    :example: response = client.create_network_acl_entry(
        DryRun=True|False,
        NetworkAclId='string',
        RuleNumber=123,
        Protocol='string',
        RuleAction='allow'|'deny',
        Egress=True|False,
        CidrBlock='string',
        Ipv6CidrBlock='string',
        IcmpTypeCode={
            'Type': 123,
            'Code': 123
        },
        PortRange={
            'From': 123,
            'To': 123
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkAclId: string
    :param NetworkAclId: [REQUIRED]
            The ID of the network ACL.
            

    :type RuleNumber: integer
    :param RuleNumber: [REQUIRED]
            The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
            Constraints: Positive integer from 1 to 32766. The range 32767 to 65535 is reserved for internal use.
            

    :type Protocol: string
    :param Protocol: [REQUIRED]
            The protocol. A value of -1 or all means all protocols. If you specify all , -1 , or a protocol number other than tcp , udp , or icmp , traffic on all ports is allowed, regardless of any ports or ICMP types or codes you specify. If you specify protocol 58 (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol 58 (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.
            

    :type RuleAction: string
    :param RuleAction: [REQUIRED]
            Indicates whether to allow or deny the traffic that matches the rule.
            

    :type Egress: boolean
    :param Egress: [REQUIRED]
            Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet).
            

    :type CidrBlock: string
    :param CidrBlock: The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).

    :type Ipv6CidrBlock: string
    :param Ipv6CidrBlock: The IPv6 network range to allow or deny, in CIDR notation (for example 2001:db8:1234:1a00::/64 ).

    :type IcmpTypeCode: dict
    :param IcmpTypeCode: ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying the ICMP protocol, or protocol 58 (ICMPv6) with an IPv6 CIDR block.
            Type (integer) --The ICMP type. A value of -1 means all types.
            Code (integer) --The ICMP code. A value of -1 means all codes for the specified ICMP type.
            

    :type PortRange: dict
    :param PortRange: TCP or UDP protocols: The range of ports the rule applies to.
            From (integer) --The first port in the range.
            To (integer) --The last port in the range.
            

    :return: response = client.create_network_acl_entry(
        CidrBlock='0.0.0.0/0',
        Egress=False,
        NetworkAclId='acl-5fb85d36',
        PortRange={
            'From': 53,
            'To': 53,
        },
        Protocol='udp',
        RuleAction='allow',
        RuleNumber=100,
    )
    
    print(response)
    
    
    """
    pass

def create_network_interface(SubnetId=None, Description=None, PrivateIpAddress=None, Groups=None, PrivateIpAddresses=None, SecondaryPrivateIpAddressCount=None, Ipv6Addresses=None, Ipv6AddressCount=None, DryRun=None):
    """
    Creates a network interface in the specified subnet.
    For more information about network interfaces, see Elastic Network Interfaces in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a network interface for the specified subnet.
    Expected Output:
    
    :example: response = client.create_network_interface(
        SubnetId='string',
        Description='string',
        PrivateIpAddress='string',
        Groups=[
            'string',
        ],
        PrivateIpAddresses=[
            {
                'PrivateIpAddress': 'string',
                'Primary': True|False
            },
        ],
        SecondaryPrivateIpAddressCount=123,
        Ipv6Addresses=[
            {
                'Ipv6Address': 'string'
            },
        ],
        Ipv6AddressCount=123,
        DryRun=True|False
    )
    
    
    :type SubnetId: string
    :param SubnetId: [REQUIRED]
            The ID of the subnet to associate with the network interface.
            

    :type Description: string
    :param Description: A description for the network interface.

    :type PrivateIpAddress: string
    :param PrivateIpAddress: The primary private IPv4 address of the network interface. If you don't specify an IPv4 address, Amazon EC2 selects one for you from the subnet's IPv4 CIDR range. If you specify an IP address, you cannot indicate any IP addresses specified in privateIpAddresses as primary (only one IP address can be designated as primary).

    :type Groups: list
    :param Groups: The IDs of one or more security groups.
            (string) --
            

    :type PrivateIpAddresses: list
    :param PrivateIpAddresses: One or more private IPv4 addresses.
            (dict) --Describes a secondary private IPv4 address for a network interface.
            PrivateIpAddress (string) -- [REQUIRED]The private IPv4 addresses.
            Primary (boolean) --Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
            
            

    :type SecondaryPrivateIpAddressCount: integer
    :param SecondaryPrivateIpAddressCount: The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using privateIpAddresses .
            The number of IP addresses you can assign to a network interface varies by instance type. For more information, see IP Addresses Per ENI Per Instance Type in the Amazon Virtual Private Cloud User Guide .
            

    :type Ipv6Addresses: list
    :param Ipv6Addresses: One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't use this option if you're specifying a number of IPv6 addresses.
            (dict) --Describes an IPv6 address.
            Ipv6Address (string) --The IPv6 address.
            
            

    :type Ipv6AddressCount: integer
    :param Ipv6AddressCount: The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses. If your subnet has the AssignIpv6AddressOnCreation attribute set to true , you can specify 0 to override this setting.

    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :rtype: dict
    :return: {
        'NetworkInterface': {
            'NetworkInterfaceId': 'string',
            'SubnetId': 'string',
            'VpcId': 'string',
            'AvailabilityZone': 'string',
            'Description': 'string',
            'OwnerId': 'string',
            'RequesterId': 'string',
            'RequesterManaged': True|False,
            'Status': 'available'|'attaching'|'in-use'|'detaching',
            'MacAddress': 'string',
            'PrivateIpAddress': 'string',
            'PrivateDnsName': 'string',
            'SourceDestCheck': True|False,
            'Groups': [
                {
                    'GroupName': 'string',
                    'GroupId': 'string'
                },
            ],
            'Attachment': {
                'AttachmentId': 'string',
                'InstanceId': 'string',
                'InstanceOwnerId': 'string',
                'DeviceIndex': 123,
                'Status': 'attaching'|'attached'|'detaching'|'detached',
                'AttachTime': datetime(2015, 1, 1),
                'DeleteOnTermination': True|False
            },
            'Association': {
                'PublicIp': 'string',
                'PublicDnsName': 'string',
                'IpOwnerId': 'string',
                'AllocationId': 'string',
                'AssociationId': 'string'
            },
            'TagSet': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'PrivateIpAddresses': [
                {
                    'PrivateIpAddress': 'string',
                    'PrivateDnsName': 'string',
                    'Primary': True|False,
                    'Association': {
                        'PublicIp': 'string',
                        'PublicDnsName': 'string',
                        'IpOwnerId': 'string',
                        'AllocationId': 'string',
                        'AssociationId': 'string'
                    }
                },
            ],
            'Ipv6Addresses': [
                {
                    'Ipv6Address': 'string'
                },
            ],
            'InterfaceType': 'interface'|'natGateway'
        }
    }
    
    
    """
    pass

def create_placement_group(DryRun=None, GroupName=None, Strategy=None):
    """
    Creates a placement group that you launch cluster instances into. You must give the group a name that's unique within the scope of your account.
    For more information about placement groups and cluster instances, see Cluster Instances in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a placement group with the specified name.
    Expected Output:
    
    :example: response = client.create_placement_group(
        DryRun=True|False,
        GroupName='string',
        Strategy='cluster'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupName: string
    :param GroupName: [REQUIRED]
            A name for the placement group.
            Constraints: Up to 255 ASCII characters
            

    :type Strategy: string
    :param Strategy: [REQUIRED]
            The placement strategy.
            

    :return: response = client.create_placement_group(
        GroupName='my-cluster',
        Strategy='cluster',
    )
    
    print(response)
    
    
    """
    pass

def create_reserved_instances_listing(ReservedInstancesId=None, InstanceCount=None, PriceSchedules=None, ClientToken=None):
    """
    Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the Reserved Instance Marketplace. You can submit one Standard Reserved Instance listing at a time. To get a list of your Standard Reserved Instances, you can use the  DescribeReservedInstances operation.
    The Reserved Instance Marketplace matches sellers who want to resell Standard Reserved Instance capacity that they no longer need with buyers who want to purchase additional capacity. Reserved Instances bought and sold through the Reserved Instance Marketplace work like any other Reserved Instances.
    To sell your Standard Reserved Instances, you must first register as a seller in the Reserved Instance Marketplace. After completing the registration process, you can create a Reserved Instance Marketplace listing of some or all of your Standard Reserved Instances, and specify the upfront price to receive for them. Your Standard Reserved Instance listings then become available for purchase. To view the details of your Standard Reserved Instance listing, you can use the  DescribeReservedInstancesListings operation.
    For more information, see Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_reserved_instances_listing(
        ReservedInstancesId='string',
        InstanceCount=123,
        PriceSchedules=[
            {
                'Term': 123,
                'Price': 123.0,
                'CurrencyCode': 'USD'
            },
        ],
        ClientToken='string'
    )
    
    
    :type ReservedInstancesId: string
    :param ReservedInstancesId: [REQUIRED]
            The ID of the active Standard Reserved Instance.
            

    :type InstanceCount: integer
    :param InstanceCount: [REQUIRED]
            The number of instances that are a part of a Reserved Instance account to be listed in the Reserved Instance Marketplace. This number should be less than or equal to the instance count associated with the Reserved Instance ID specified in this call.
            

    :type PriceSchedules: list
    :param PriceSchedules: [REQUIRED]
            A list specifying the price of the Standard Reserved Instance for each month remaining in the Reserved Instance term.
            (dict) --Describes the price for a Reserved Instance.
            Term (integer) --The number of months remaining in the reservation. For example, 2 is the second to the last month before the capacity reservation expires.
            Price (float) --The fixed price for the term.
            CurrencyCode (string) --The currency for transacting the Reserved Instance resale. At this time, the only supported currency is USD .
            
            

    :type ClientToken: string
    :param ClientToken: [REQUIRED]
            Unique, case-sensitive identifier you provide to ensure idempotency of your listings. This helps avoid duplicate listings. For more information, see Ensuring Idempotency .
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def create_route(DryRun=None, RouteTableId=None, DestinationCidrBlock=None, GatewayId=None, DestinationIpv6CidrBlock=None, EgressOnlyInternetGatewayId=None, InstanceId=None, NetworkInterfaceId=None, VpcPeeringConnectionId=None, NatGatewayId=None):
    """
    Creates a route in a route table within a VPC.
    You must specify one of the following targets: Internet gateway or virtual private gateway, NAT instance, NAT gateway, VPC peering connection, network interface, or egress-only Internet gateway.
    When determining how to route traffic, we use the route with the most specific match. For example, traffic is destined for the IPv4 address 192.0.2.3 , and the route table includes the following two IPv4 routes:
    Both routes apply to the traffic destined for 192.0.2.3 . However, the second route in the list covers a smaller number of IP addresses and is therefore more specific, so we use that route to determine where to target the traffic.
    For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a route for the specified route table. The route matches all traffic (0.0.0.0/0) and routes it to the specified Internet gateway.
    Expected Output:
    
    :example: response = client.create_route(
        DryRun=True|False,
        RouteTableId='string',
        DestinationCidrBlock='string',
        GatewayId='string',
        DestinationIpv6CidrBlock='string',
        EgressOnlyInternetGatewayId='string',
        InstanceId='string',
        NetworkInterfaceId='string',
        VpcPeeringConnectionId='string',
        NatGatewayId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type RouteTableId: string
    :param RouteTableId: [REQUIRED]
            The ID of the route table for the route.
            

    :type DestinationCidrBlock: string
    :param DestinationCidrBlock: The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match.

    :type GatewayId: string
    :param GatewayId: The ID of an Internet gateway or virtual private gateway attached to your VPC.

    :type DestinationIpv6CidrBlock: string
    :param DestinationIpv6CidrBlock: The IPv6 CIDR block used for the destination match. Routing decisions are based on the most specific match.

    :type EgressOnlyInternetGatewayId: string
    :param EgressOnlyInternetGatewayId: [IPv6 traffic only] The ID of an egress-only Internet gateway.

    :type InstanceId: string
    :param InstanceId: The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network interface is attached.

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: The ID of a network interface.

    :type VpcPeeringConnectionId: string
    :param VpcPeeringConnectionId: The ID of a VPC peering connection.

    :type NatGatewayId: string
    :param NatGatewayId: [IPv4 traffic only] The ID of a NAT gateway.

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    :returns: 
    DryRun (boolean) -- Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    RouteTableId (string) -- [REQUIRED]
    The ID of the route table for the route.
    
    DestinationCidrBlock (string) -- The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match.
    GatewayId (string) -- The ID of an Internet gateway or virtual private gateway attached to your VPC.
    DestinationIpv6CidrBlock (string) -- The IPv6 CIDR block used for the destination match. Routing decisions are based on the most specific match.
    EgressOnlyInternetGatewayId (string) -- [IPv6 traffic only] The ID of an egress-only Internet gateway.
    InstanceId (string) -- The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network interface is attached.
    NetworkInterfaceId (string) -- The ID of a network interface.
    VpcPeeringConnectionId (string) -- The ID of a VPC peering connection.
    NatGatewayId (string) -- [IPv4 traffic only] The ID of a NAT gateway.
    
    """
    pass

def create_route_table(DryRun=None, VpcId=None):
    """
    Creates a route table for the specified VPC. After you create a route table, you can add routes and associate the table with a subnet.
    For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a route table for the specified VPC.
    Expected Output:
    
    :example: response = client.create_route_table(
        DryRun=True|False,
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :rtype: dict
    :return: {
        'RouteTable': {
            'RouteTableId': 'string',
            'VpcId': 'string',
            'Routes': [
                {
                    'DestinationCidrBlock': 'string',
                    'DestinationPrefixListId': 'string',
                    'GatewayId': 'string',
                    'InstanceId': 'string',
                    'InstanceOwnerId': 'string',
                    'NetworkInterfaceId': 'string',
                    'VpcPeeringConnectionId': 'string',
                    'NatGatewayId': 'string',
                    'State': 'active'|'blackhole',
                    'Origin': 'CreateRouteTable'|'CreateRoute'|'EnableVgwRoutePropagation',
                    'DestinationIpv6CidrBlock': 'string',
                    'EgressOnlyInternetGatewayId': 'string'
                },
            ],
            'Associations': [
                {
                    'RouteTableAssociationId': 'string',
                    'RouteTableId': 'string',
                    'SubnetId': 'string',
                    'Main': True|False
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'PropagatingVgws': [
                {
                    'GatewayId': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CreateRouteTable - The route was automatically created when the route table was created.
    CreateRoute - The route was manually added to the route table.
    EnableVgwRoutePropagation - The route was propagated by route propagation.
    
    """
    pass

def create_security_group(DryRun=None, GroupName=None, Description=None, VpcId=None):
    """
    Creates a security group.
    A security group is for use with instances either in the EC2-Classic platform or in a specific VPC. For more information, see Amazon EC2 Security Groups in the Amazon Elastic Compute Cloud User Guide and Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .
    When you create a security group, you specify a friendly name of your choice. You can have a security group for use in EC2-Classic with the same name as a security group for use in a VPC. However, you can't have two security groups for use in EC2-Classic with the same name or two security groups for use in a VPC with the same name.
    You have a default security group for use in EC2-Classic and a default security group for use in your VPC. If you don't specify a security group when you launch an instance, the instance is launched into the appropriate default security group. A default security group includes a default rule that grants instances unrestricted network access to each other.
    You can add or remove rules from your security groups using  AuthorizeSecurityGroupIngress ,  AuthorizeSecurityGroupEgress ,  RevokeSecurityGroupIngress , and  RevokeSecurityGroupEgress .
    See also: AWS API Documentation
    
    
    :example: response = client.create_security_group(
        DryRun=True|False,
        GroupName='string',
        Description='string',
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the security group.
            Constraints: Up to 255 characters in length
            Constraints for EC2-Classic: ASCII characters
            Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
            

    :type Description: string
    :param Description: [REQUIRED]
            A description for the security group. This is informational only.
            Constraints: Up to 255 characters in length
            Constraints for EC2-Classic: ASCII characters
            Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*
            

    :type VpcId: string
    :param VpcId: [EC2-VPC] The ID of the VPC. Required for EC2-VPC.

    :rtype: dict
    :return: {
        'GroupId': 'string'
    }
    
    
    """
    pass

def create_snapshot(DryRun=None, VolumeId=None, Description=None):
    """
    Creates a snapshot of an EBS volume and stores it in Amazon S3. You can use snapshots for backups, to make copies of EBS volumes, and to save data before shutting down an instance.
    When a snapshot is created, any AWS Marketplace product codes that are associated with the source volume are propagated to the snapshot.
    You can take a snapshot of an attached volume that is in use. However, snapshots only capture data that has been written to your EBS volume at the time the snapshot command is issued; this may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the volume long enough to take a snapshot, your snapshot should be complete. However, if you cannot pause all file writes to the volume, you should unmount the volume from within the instance, issue the snapshot command, and then remount the volume to ensure a consistent and complete snapshot. You may remount and use your volume while the snapshot status is pending .
    To create a snapshot for EBS volumes that serve as root devices, you should stop the instance before taking the snapshot.
    Snapshots that are taken from encrypted volumes are automatically encrypted. Volumes that are created from encrypted snapshots are also automatically encrypted. Your encrypted volumes and any associated snapshots always remain protected.
    For more information, see Amazon Elastic Block Store and Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a snapshot of the volume with a volume ID of vol-1234567890abcdef0 and a short description to identify the snapshot.
    Expected Output:
    
    :example: response = client.create_snapshot(
        DryRun=True|False,
        VolumeId='string',
        Description='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeId: string
    :param VolumeId: [REQUIRED]
            The ID of the EBS volume.
            

    :type Description: string
    :param Description: A description for the snapshot.

    :rtype: dict
    :return: {
        'SnapshotId': 'string',
        'VolumeId': 'string',
        'State': 'pending'|'completed'|'error',
        'StateMessage': 'string',
        'StartTime': datetime(2015, 1, 1),
        'Progress': 'string',
        'OwnerId': 'string',
        'Description': 'string',
        'VolumeSize': 123,
        'OwnerAlias': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'Encrypted': True|False,
        'KmsKeyId': 'string',
        'DataEncryptionKeyId': 'string'
    }
    
    
    """
    pass

def create_spot_datafeed_subscription(DryRun=None, Bucket=None, Prefix=None):
    """
    Creates a data feed for Spot instances, enabling you to view Spot instance usage logs. You can create one data feed per AWS account. For more information, see Spot Instance Data Feed in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a Spot Instance data feed for your AWS account.
    Expected Output:
    
    :example: response = client.create_spot_datafeed_subscription(
        DryRun=True|False,
        Bucket='string',
        Prefix='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Bucket: string
    :param Bucket: [REQUIRED]
            The Amazon S3 bucket in which to store the Spot instance data feed.
            

    :type Prefix: string
    :param Prefix: A prefix for the data feed file names.

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def create_subnet(DryRun=None, VpcId=None, CidrBlock=None, Ipv6CidrBlock=None, AvailabilityZone=None):
    """
    Creates a subnet in an existing VPC.
    When you create each subnet, you provide the VPC ID and the CIDR block you want for the subnet. After you create a subnet, you can't change its CIDR block. The subnet's IPv4 CIDR block can be the same as the VPC's IPv4 CIDR block (assuming you want only a single subnet in the VPC), or a subset of the VPC's IPv4 CIDR block. If you create more than one subnet in a VPC, the subnets' CIDR blocks must not overlap. The smallest IPv4 subnet (and VPC) you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses).
    If you've associated an IPv6 CIDR block with your VPC, you can create a subnet with an IPv6 CIDR block that uses a /64 prefix length.
    If you add more than one subnet to a VPC, they're set up in a star topology with a logical router in the middle.
    If you launch an instance in a VPC using an Amazon EBS-backed AMI, the IP address doesn't change if you stop and restart the instance (unlike a similar instance launched outside a VPC, which gets a new IP address when restarted). It's therefore possible to have a subnet with no running instances (they're all stopped), but no remaining IP addresses available.
    For more information about subnets, see Your VPC and Subnets in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a subnet in the specified VPC with the specified CIDR block. We recommend that you let us select an Availability Zone for you.
    Expected Output:
    
    :example: response = client.create_subnet(
        DryRun=True|False,
        VpcId='string',
        CidrBlock='string',
        Ipv6CidrBlock='string',
        AvailabilityZone='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :type CidrBlock: string
    :param CidrBlock: [REQUIRED]
            The IPv4 network range for the subnet, in CIDR notation. For example, 10.0.0.0/24 .
            

    :type Ipv6CidrBlock: string
    :param Ipv6CidrBlock: The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length.

    :type AvailabilityZone: string
    :param AvailabilityZone: The Availability Zone for the subnet.
            Default: AWS selects one for you. If you create more than one subnet in your VPC, we may not necessarily select a different zone for each subnet.
            

    :rtype: dict
    :return: {
        'Subnet': {
            'SubnetId': 'string',
            'State': 'pending'|'available',
            'VpcId': 'string',
            'CidrBlock': 'string',
            'Ipv6CidrBlockAssociationSet': [
                {
                    'Ipv6CidrBlock': 'string',
                    'Ipv6CidrBlockState': {
                        'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                        'StatusMessage': 'string'
                    },
                    'AssociationId': 'string'
                },
            ],
            'AssignIpv6AddressOnCreation': True|False,
            'AvailableIpAddressCount': 123,
            'AvailabilityZone': 'string',
            'DefaultForAz': True|False,
            'MapPublicIpOnLaunch': True|False,
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_tags(DryRun=None, Resources=None, Tags=None):
    """
    Adds or overwrites one or more tags for the specified Amazon EC2 resource or resources. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique per resource.
    For more information about tags, see Tagging Your Resources in the Amazon Elastic Compute Cloud User Guide . For more information about creating IAM policies that control users' access to resources based on tags, see Supported Resource-Level Permissions for Amazon EC2 API Actions in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example adds the tag Stack=production to the specified image, or overwrites an existing tag for the AMI where the tag key is Stack.
    Expected Output:
    
    :example: response = client.create_tags(
        DryRun=True|False,
        Resources=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Resources: list
    :param Resources: [REQUIRED]
            The IDs of one or more resources to tag. For example, ami-1a2b3c4d.
            (string) --
            

    :type Tags: list
    :param Tags: [REQUIRED]
            One or more tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.
            (dict) --Describes a tag.
            Key (string) --The key of the tag.
            Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:
            Value (string) --The value of the tag.
            Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
            
            

    :return: response = client.create_tags(
        Resources=[
            'ami-78a54011',
        ],
        Tags=[
            {
                'Key': 'Stack',
                'Value': 'production',
            },
        ],
    )
    
    print(response)
    
    
    """
    pass

def create_volume(DryRun=None, Size=None, SnapshotId=None, AvailabilityZone=None, VolumeType=None, Iops=None, Encrypted=None, KmsKeyId=None, TagSpecifications=None):
    """
    Creates an EBS volume that can be attached to an instance in the same Availability Zone. The volume is created in the regional endpoint that you send the HTTP request to. For more information see Regions and Endpoints .
    You can create a new empty volume or restore a volume from an EBS snapshot. Any AWS Marketplace product codes from the snapshot are propagated to the volume.
    You can create encrypted volumes with the Encrypted parameter. Encrypted volumes may only be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are also automatically encrypted. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .
    You can tag your volumes during creation. For more information, see Tagging Your Amazon EC2 Resources .
    For more information, see Creating an Amazon EBS Volume in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates an 80 GiB General Purpose (SSD) volume in the Availability Zone us-east-1a.
    Expected Output:
    This example creates a new Provisioned IOPS (SSD) volume with 1000 provisioned IOPS from a snapshot in the Availability Zone us-east-1a.
    Expected Output:
    
    :example: response = client.create_volume(
        DryRun=True|False,
        Size=123,
        SnapshotId='string',
        AvailabilityZone='string',
        VolumeType='standard'|'io1'|'gp2'|'sc1'|'st1',
        Iops=123,
        Encrypted=True|False,
        KmsKeyId='string',
        TagSpecifications=[
            {
                'ResourceType': 'customer-gateway'|'dhcp-options'|'image'|'instance'|'internet-gateway'|'network-acl'|'network-interface'|'reserved-instances'|'route-table'|'snapshot'|'spot-instances-request'|'subnet'|'security-group'|'volume'|'vpc'|'vpn-connection'|'vpn-gateway',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Size: integer
    :param Size: The size of the volume, in GiBs.
            Constraints: 1-16384 for gp2 , 4-16384 for io1 , 500-16384 for st1 , 500-16384 for sc1 , and 1-1024 for standard . If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
            Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
            

    :type SnapshotId: string
    :param SnapshotId: The snapshot from which to create the volume.

    :type AvailabilityZone: string
    :param AvailabilityZone: [REQUIRED]
            The Availability Zone in which to create the volume. Use DescribeAvailabilityZones to list the Availability Zones that are currently available to you.
            

    :type VolumeType: string
    :param VolumeType: The volume type. This can be gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic volumes.
            Default: standard
            

    :type Iops: integer
    :param Iops: Only valid for Provisioned IOPS SSD volumes. The number of I/O operations per second (IOPS) to provision for the volume, with a maximum ratio of 50 IOPS/GiB.
            Constraint: Range is 100 to 20000 for Provisioned IOPS SSD volumes
            

    :type Encrypted: boolean
    :param Encrypted: Specifies whether the volume should be encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or vice versa. If your AMI uses encrypted volumes, you can only launch it on supported instance types. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .

    :type KmsKeyId: string
    :param KmsKeyId: The full ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. The ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1 :012345678910 :key/abcd1234-a123-456a-a12b-a123b4cd56ef . If a KmsKeyId is specified, the Encrypted flag must also be set.

    :type TagSpecifications: list
    :param TagSpecifications: The tags to apply to the volume during creation.
            (dict) --The tags to apply to a resource when the resource is being created.
            ResourceType (string) --The type of resource to tag. Currently, the resource types that support tagging on creation are instance and volume .
            Tags (list) --The tags to apply to the resource.
            (dict) --Describes a tag.
            Key (string) --The key of the tag.
            Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:
            Value (string) --The value of the tag.
            Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
            
            
            

    :rtype: dict
    :return: {
        'VolumeId': 'string',
        'Size': 123,
        'SnapshotId': 'string',
        'AvailabilityZone': 'string',
        'State': 'creating'|'available'|'in-use'|'deleting'|'deleted'|'error',
        'CreateTime': datetime(2015, 1, 1),
        'Attachments': [
            {
                'VolumeId': 'string',
                'InstanceId': 'string',
                'Device': 'string',
                'State': 'attaching'|'attached'|'detaching'|'detached',
                'AttachTime': datetime(2015, 1, 1),
                'DeleteOnTermination': True|False
            },
        ],
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
        'Iops': 123,
        'Encrypted': True|False,
        'KmsKeyId': 'string'
    }
    
    
    """
    pass

def create_vpc(DryRun=None, CidrBlock=None, InstanceTenancy=None, AmazonProvidedIpv6CidrBlock=None):
    """
    Creates a VPC with the specified IPv4 CIDR block. The smallest VPC you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses). To help you decide how big to make your VPC, see Your VPC and Subnets in the Amazon Virtual Private Cloud User Guide .
    You can optionally request an Amazon-provided IPv6 CIDR block for the VPC. The IPv6 CIDR block uses a /56 prefix length, and is allocated from Amazon's pool of IPv6 addresses. You cannot choose the IPv6 range for your VPC.
    By default, each instance you launch in the VPC has the default DHCP options, which includes only a default DNS server that we provide (AmazonProvidedDNS). For more information about DHCP options, see DHCP Options Sets in the Amazon Virtual Private Cloud User Guide .
    You can specify the instance tenancy value for the VPC when you create it. You can't change this value for the VPC after you create it. For more information, see Dedicated Instances in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a VPC with the specified CIDR block.
    Expected Output:
    
    :example: response = client.create_vpc(
        DryRun=True|False,
        CidrBlock='string',
        InstanceTenancy='default'|'dedicated'|'host',
        AmazonProvidedIpv6CidrBlock=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type CidrBlock: string
    :param CidrBlock: [REQUIRED]
            The IPv4 network range for the VPC, in CIDR notation. For example, 10.0.0.0/16 .
            

    :type InstanceTenancy: string
    :param InstanceTenancy: The tenancy options for instances launched into the VPC. For default , instances are launched with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy VPC. For dedicated , instances are launched as dedicated tenancy instances by default. You can only launch instances with a tenancy of dedicated or host into a dedicated tenancy VPC.
            Important: The host value cannot be used with this parameter. Use the default or dedicated values only.
            Default: default
            

    :type AmazonProvidedIpv6CidrBlock: boolean
    :param AmazonProvidedIpv6CidrBlock: Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block.

    :rtype: dict
    :return: {
        'Vpc': {
            'VpcId': 'string',
            'State': 'pending'|'available',
            'CidrBlock': 'string',
            'DhcpOptionsId': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'InstanceTenancy': 'default'|'dedicated'|'host',
            'IsDefault': True|False,
            'Ipv6CidrBlockAssociationSet': [
                {
                    'Ipv6CidrBlock': 'string',
                    'Ipv6CidrBlockState': {
                        'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                        'StatusMessage': 'string'
                    },
                    'AssociationId': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_vpc_endpoint(DryRun=None, VpcId=None, ServiceName=None, PolicyDocument=None, RouteTableIds=None, ClientToken=None):
    """
    Creates a VPC endpoint for a specified AWS service. An endpoint enables you to create a private connection between your VPC and another AWS service in your account. You can specify an endpoint policy to attach to the endpoint that will control access to the service from your VPC. You can also specify the VPC route tables that use the endpoint.
    Use  DescribeVpcEndpointServices to get a list of supported AWS services.
    See also: AWS API Documentation
    
    
    :example: response = client.create_vpc_endpoint(
        DryRun=True|False,
        VpcId='string',
        ServiceName='string',
        PolicyDocument='string',
        RouteTableIds=[
            'string',
        ],
        ClientToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC in which the endpoint will be used.
            

    :type ServiceName: string
    :param ServiceName: [REQUIRED]
            The AWS service name, in the form ``com.amazonaws.*region* .*service* `` . To get a list of available services, use the DescribeVpcEndpointServices request.
            

    :type PolicyDocument: string
    :param PolicyDocument: A policy to attach to the endpoint that controls access to the service. The policy must be in valid JSON format. If this parameter is not specified, we attach a default policy that allows full access to the service.

    :type RouteTableIds: list
    :param RouteTableIds: One or more route table IDs.
            (string) --
            

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency .

    :rtype: dict
    :return: {
        'VpcEndpoint': {
            'VpcEndpointId': 'string',
            'VpcId': 'string',
            'ServiceName': 'string',
            'State': 'Pending'|'Available'|'Deleting'|'Deleted',
            'PolicyDocument': 'string',
            'RouteTableIds': [
                'string',
            ],
            'CreationTimestamp': datetime(2015, 1, 1)
        },
        'ClientToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_vpc_peering_connection(DryRun=None, VpcId=None, PeerVpcId=None, PeerOwnerId=None):
    """
    Requests a VPC peering connection between two VPCs: a requester VPC that you own and a peer VPC with which to create the connection. The peer VPC can belong to another AWS account. The requester VPC and peer VPC cannot have overlapping CIDR blocks.
    The owner of the peer VPC must accept the peering request to activate the peering connection. The VPC peering connection request expires after 7 days, after which it cannot be accepted or rejected.
    If you try to create a VPC peering connection between VPCs that have overlapping CIDR blocks, the VPC peering connection status goes to failed .
    See also: AWS API Documentation
    
    
    :example: response = client.create_vpc_peering_connection(
        DryRun=True|False,
        VpcId='string',
        PeerVpcId='string',
        PeerOwnerId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: The ID of the requester VPC.

    :type PeerVpcId: string
    :param PeerVpcId: The ID of the VPC with which you are creating the VPC peering connection.

    :type PeerOwnerId: string
    :param PeerOwnerId: The AWS account ID of the owner of the peer VPC.
            Default: Your AWS account ID
            

    :rtype: dict
    :return: {
        'VpcPeeringConnection': {
            'AccepterVpcInfo': {
                'CidrBlock': 'string',
                'OwnerId': 'string',
                'VpcId': 'string',
                'Ipv6CidrBlockSet': [
                    {
                        'Ipv6CidrBlock': 'string'
                    },
                ],
                'PeeringOptions': {
                    'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
                    'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
                    'AllowDnsResolutionFromRemoteVpc': True|False
                }
            },
            'ExpirationTime': datetime(2015, 1, 1),
            'RequesterVpcInfo': {
                'CidrBlock': 'string',
                'OwnerId': 'string',
                'VpcId': 'string',
                'Ipv6CidrBlockSet': [
                    {
                        'Ipv6CidrBlock': 'string'
                    },
                ],
                'PeeringOptions': {
                    'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
                    'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
                    'AllowDnsResolutionFromRemoteVpc': True|False
                }
            },
            'Status': {
                'Code': 'initiating-request'|'pending-acceptance'|'active'|'deleted'|'rejected'|'failed'|'expired'|'provisioning'|'deleting',
                'Message': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'VpcPeeringConnectionId': 'string'
        }
    }
    
    
    """
    pass

def create_vpn_connection(DryRun=None, Type=None, CustomerGatewayId=None, VpnGatewayId=None, Options=None):
    """
    Creates a VPN connection between an existing virtual private gateway and a VPN customer gateway. The only supported connection type is ipsec.1 .
    The response includes information that you need to give to your network administrator to configure your customer gateway.
    If you decide to shut down your VPN connection for any reason and later create a new VPN connection, you must reconfigure your customer gateway with the new information returned from this call.
    This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error.
    For more information about VPN connections, see Adding a Hardware Virtual Private Gateway to Your VPC in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_vpn_connection(
        DryRun=True|False,
        Type='string',
        CustomerGatewayId='string',
        VpnGatewayId='string',
        Options={
            'StaticRoutesOnly': True|False
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Type: string
    :param Type: [REQUIRED]
            The type of VPN connection (ipsec.1 ).
            

    :type CustomerGatewayId: string
    :param CustomerGatewayId: [REQUIRED]
            The ID of the customer gateway.
            

    :type VpnGatewayId: string
    :param VpnGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            

    :type Options: dict
    :param Options: Indicates whether the VPN connection requires static routes. If you are creating a VPN connection for a device that does not support BGP, you must specify true .
            Default: false
            StaticRoutesOnly (boolean) --Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don't support BGP.
            

    :rtype: dict
    :return: {
        'VpnConnection': {
            'VpnConnectionId': 'string',
            'State': 'pending'|'available'|'deleting'|'deleted',
            'CustomerGatewayConfiguration': 'string',
            'Type': 'ipsec.1',
            'CustomerGatewayId': 'string',
            'VpnGatewayId': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'VgwTelemetry': [
                {
                    'OutsideIpAddress': 'string',
                    'Status': 'UP'|'DOWN',
                    'LastStatusChange': datetime(2015, 1, 1),
                    'StatusMessage': 'string',
                    'AcceptedRouteCount': 123
                },
            ],
            'Options': {
                'StaticRoutesOnly': True|False
            },
            'Routes': [
                {
                    'DestinationCidrBlock': 'string',
                    'Source': 'Static',
                    'State': 'pending'|'available'|'deleting'|'deleted'
                },
            ]
        }
    }
    
    
    """
    pass

def create_vpn_connection_route(VpnConnectionId=None, DestinationCidrBlock=None):
    """
    Creates a static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway.
    For more information about VPN connections, see Adding a Hardware Virtual Private Gateway to Your VPC in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_vpn_connection_route(
        VpnConnectionId='string',
        DestinationCidrBlock='string'
    )
    
    
    :type VpnConnectionId: string
    :param VpnConnectionId: [REQUIRED]
            The ID of the VPN connection.
            

    :type DestinationCidrBlock: string
    :param DestinationCidrBlock: [REQUIRED]
            The CIDR block associated with the local subnet of the customer network.
            

    """
    pass

def create_vpn_gateway(DryRun=None, Type=None, AvailabilityZone=None):
    """
    Creates a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself.
    For more information about virtual private gateways, see Adding a Hardware Virtual Private Gateway to Your VPC in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_vpn_gateway(
        DryRun=True|False,
        Type='ipsec.1',
        AvailabilityZone='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Type: string
    :param Type: [REQUIRED]
            The type of VPN connection this virtual private gateway supports.
            

    :type AvailabilityZone: string
    :param AvailabilityZone: The Availability Zone for the virtual private gateway.

    :rtype: dict
    :return: {
        'VpnGateway': {
            'VpnGatewayId': 'string',
            'State': 'pending'|'available'|'deleting'|'deleted',
            'Type': 'ipsec.1',
            'AvailabilityZone': 'string',
            'VpcAttachments': [
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
    
    
    """
    pass

def delete_customer_gateway(DryRun=None, CustomerGatewayId=None):
    """
    Deletes the specified customer gateway. You must delete the VPN connection before you can delete the customer gateway.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified customer gateway.
    Expected Output:
    
    :example: response = client.delete_customer_gateway(
        DryRun=True|False,
        CustomerGatewayId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type CustomerGatewayId: string
    :param CustomerGatewayId: [REQUIRED]
            The ID of the customer gateway.
            

    :return: response = client.delete_customer_gateway(
        CustomerGatewayId='cgw-0e11f167',
    )
    
    print(response)
    
    
    """
    pass

def delete_dhcp_options(DryRun=None, DhcpOptionsId=None):
    """
    Deletes the specified set of DHCP options. You must disassociate the set of DHCP options before you can delete it. You can disassociate the set of DHCP options by associating either a new set of options or the default set of options with the VPC.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified DHCP options set.
    Expected Output:
    
    :example: response = client.delete_dhcp_options(
        DryRun=True|False,
        DhcpOptionsId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type DhcpOptionsId: string
    :param DhcpOptionsId: [REQUIRED]
            The ID of the DHCP options set.
            

    :return: response = client.delete_dhcp_options(
        DhcpOptionsId='dopt-d9070ebb',
    )
    
    print(response)
    
    
    """
    pass

def delete_egress_only_internet_gateway(DryRun=None, EgressOnlyInternetGatewayId=None):
    """
    Deletes an egress-only Internet gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_egress_only_internet_gateway(
        DryRun=True|False,
        EgressOnlyInternetGatewayId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type EgressOnlyInternetGatewayId: string
    :param EgressOnlyInternetGatewayId: [REQUIRED]
            The ID of the egress-only Internet gateway.
            

    :rtype: dict
    :return: {
        'ReturnCode': True|False
    }
    
    
    """
    pass

def delete_flow_logs(FlowLogIds=None):
    """
    Deletes one or more flow logs.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_flow_logs(
        FlowLogIds=[
            'string',
        ]
    )
    
    
    :type FlowLogIds: list
    :param FlowLogIds: [REQUIRED]
            One or more flow log IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'Unsuccessful': [
            {
                'ResourceId': 'string',
                'Error': {
                    'Code': 'string',
                    'Message': 'string'
                }
            },
        ]
    }
    
    
    """
    pass

def delete_internet_gateway(DryRun=None, InternetGatewayId=None):
    """
    Deletes the specified Internet gateway. You must detach the Internet gateway from the VPC before you can delete it.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified Internet gateway.
    Expected Output:
    
    :example: response = client.delete_internet_gateway(
        DryRun=True|False,
        InternetGatewayId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InternetGatewayId: string
    :param InternetGatewayId: [REQUIRED]
            The ID of the Internet gateway.
            

    :return: response = client.delete_internet_gateway(
        InternetGatewayId='igw-c0a643a9',
    )
    
    print(response)
    
    
    """
    pass

def delete_key_pair(DryRun=None, KeyName=None):
    """
    Deletes the specified key pair, by removing the public key from Amazon EC2.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified key pair.
    Expected Output:
    
    :example: response = client.delete_key_pair(
        DryRun=True|False,
        KeyName='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type KeyName: string
    :param KeyName: [REQUIRED]
            The name of the key pair.
            

    :return: response = client.delete_key_pair(
        KeyName='my-key-pair',
    )
    
    print(response)
    
    
    """
    pass

def delete_nat_gateway(NatGatewayId=None):
    """
    Deletes the specified NAT gateway. Deleting a NAT gateway disassociates its Elastic IP address, but does not release the address from your account. Deleting a NAT gateway does not delete any NAT gateway routes in your route tables.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified NAT gateway.
    Expected Output:
    
    :example: response = client.delete_nat_gateway(
        NatGatewayId='string'
    )
    
    
    :type NatGatewayId: string
    :param NatGatewayId: [REQUIRED]
            The ID of the NAT gateway.
            

    :rtype: dict
    :return: {
        'NatGatewayId': 'string'
    }
    
    
    """
    pass

def delete_network_acl(DryRun=None, NetworkAclId=None):
    """
    Deletes the specified network ACL. You can't delete the ACL if it's associated with any subnets. You can't delete the default network ACL.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified network ACL.
    Expected Output:
    
    :example: response = client.delete_network_acl(
        DryRun=True|False,
        NetworkAclId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkAclId: string
    :param NetworkAclId: [REQUIRED]
            The ID of the network ACL.
            

    :return: response = client.delete_network_acl(
        NetworkAclId='acl-5fb85d36',
    )
    
    print(response)
    
    
    """
    pass

def delete_network_acl_entry(DryRun=None, NetworkAclId=None, RuleNumber=None, Egress=None):
    """
    Deletes the specified ingress or egress entry (rule) from the specified network ACL.
    See also: AWS API Documentation
    
    Examples
    This example deletes ingress rule number 100 from the specified network ACL.
    Expected Output:
    
    :example: response = client.delete_network_acl_entry(
        DryRun=True|False,
        NetworkAclId='string',
        RuleNumber=123,
        Egress=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkAclId: string
    :param NetworkAclId: [REQUIRED]
            The ID of the network ACL.
            

    :type RuleNumber: integer
    :param RuleNumber: [REQUIRED]
            The rule number of the entry to delete.
            

    :type Egress: boolean
    :param Egress: [REQUIRED]
            Indicates whether the rule is an egress rule.
            

    :return: response = client.delete_network_acl_entry(
        Egress=True,
        NetworkAclId='acl-5fb85d36',
        RuleNumber=100,
    )
    
    print(response)
    
    
    """
    pass

def delete_network_interface(DryRun=None, NetworkInterfaceId=None):
    """
    Deletes the specified network interface. You must detach the network interface before you can delete it.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified network interface.
    Expected Output:
    
    :example: response = client.delete_network_interface(
        DryRun=True|False,
        NetworkInterfaceId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            

    :return: response = client.delete_network_interface(
        NetworkInterfaceId='eni-e5aa89a3',
    )
    
    print(response)
    
    
    """
    pass

def delete_placement_group(DryRun=None, GroupName=None):
    """
    Deletes the specified placement group. You must terminate all instances in the placement group before you can delete the placement group. For more information about placement groups and cluster instances, see Cluster Instances in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified placement group.
    Expected Output:
    
    :example: response = client.delete_placement_group(
        DryRun=True|False,
        GroupName='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupName: string
    :param GroupName: [REQUIRED]
            The name of the placement group.
            

    :return: response = client.delete_placement_group(
        GroupName='my-cluster',
    )
    
    print(response)
    
    
    """
    pass

def delete_route(DryRun=None, RouteTableId=None, DestinationCidrBlock=None, DestinationIpv6CidrBlock=None):
    """
    Deletes the specified route from the specified route table.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified route from the specified route table.
    Expected Output:
    
    :example: response = client.delete_route(
        DryRun=True|False,
        RouteTableId='string',
        DestinationCidrBlock='string',
        DestinationIpv6CidrBlock='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type RouteTableId: string
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            

    :type DestinationCidrBlock: string
    :param DestinationCidrBlock: The IPv4 CIDR range for the route. The value you specify must match the CIDR for the route exactly.

    :type DestinationIpv6CidrBlock: string
    :param DestinationIpv6CidrBlock: The IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly.

    :return: response = client.delete_route(
        DestinationCidrBlock='0.0.0.0/0',
        RouteTableId='rtb-22574640',
    )
    
    print(response)
    
    
    """
    pass

def delete_route_table(DryRun=None, RouteTableId=None):
    """
    Deletes the specified route table. You must disassociate the route table from any subnets before you can delete it. You can't delete the main route table.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified route table.
    Expected Output:
    
    :example: response = client.delete_route_table(
        DryRun=True|False,
        RouteTableId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type RouteTableId: string
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            

    :return: response = client.delete_route_table(
        RouteTableId='rtb-22574640',
    )
    
    print(response)
    
    
    """
    pass

def delete_security_group(DryRun=None, GroupName=None, GroupId=None):
    """
    Deletes a security group.
    If you attempt to delete a security group that is associated with an instance, or is referenced by another security group, the operation fails with InvalidGroup.InUse in EC2-Classic or DependencyViolation in EC2-VPC.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_security_group(
        DryRun=True|False,
        GroupName='string',
        GroupId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupName: string
    :param GroupName: [EC2-Classic, default VPC] The name of the security group. You can specify either the security group name or the security group ID.

    :type GroupId: string
    :param GroupId: The ID of the security group. Required for a nondefault VPC.

    """
    pass

def delete_snapshot(DryRun=None, SnapshotId=None):
    """
    Deletes the specified snapshot.
    When you make periodic snapshots of a volume, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the volume.
    You cannot delete a snapshot of the root device of an EBS volume used by a registered AMI. You must first de-register the AMI before you can delete the snapshot.
    For more information, see Deleting an Amazon EBS Snapshot in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example deletes a snapshot with the snapshot ID of snap-1234567890abcdef0. If the command succeeds, no output is returned.
    Expected Output:
    
    :example: response = client.delete_snapshot(
        DryRun=True|False,
        SnapshotId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]
            The ID of the EBS snapshot.
            

    :return: response = client.delete_snapshot(
        SnapshotId='snap-1234567890abcdef0',
    )
    
    print(response)
    
    
    """
    pass

def delete_spot_datafeed_subscription(DryRun=None):
    """
    Deletes the data feed for Spot instances.
    See also: AWS API Documentation
    
    Examples
    This example deletes a Spot data feed subscription for the account.
    Expected Output:
    
    :example: response = client.delete_spot_datafeed_subscription(
        DryRun=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :return: response = client.delete_spot_datafeed_subscription(
    )
    
    print(response)
    
    
    """
    pass

def delete_subnet(DryRun=None, SubnetId=None):
    """
    Deletes the specified subnet. You must terminate all running instances in the subnet before you can delete the subnet.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified subnet.
    Expected Output:
    
    :example: response = client.delete_subnet(
        DryRun=True|False,
        SubnetId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SubnetId: string
    :param SubnetId: [REQUIRED]
            The ID of the subnet.
            

    :return: response = client.delete_subnet(
        SubnetId='subnet-9d4a7b6c',
    )
    
    print(response)
    
    
    """
    pass

def delete_tags(DryRun=None, Resources=None, Tags=None):
    """
    Deletes the specified set of tags from the specified set of resources. This call is designed to follow a DescribeTags request.
    For more information about tags, see Tagging Your Resources in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example deletes the tag Stack=test from the specified image.
    Expected Output:
    
    :example: response = client.delete_tags(
        DryRun=True|False,
        Resources=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Resources: list
    :param Resources: [REQUIRED]
            The ID of the resource. For example, ami-1a2b3c4d. You can specify more than one resource ID.
            (string) --
            

    :type Tags: list
    :param Tags: One or more tags to delete. If you omit the value parameter, we delete the tag regardless of its value. If you specify this parameter with an empty string as the value, we delete the key only if its value is an empty string.
            (dict) --Describes a tag.
            Key (string) --The key of the tag.
            Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:
            Value (string) --The value of the tag.
            Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
            
            

    :return: response = client.delete_tags(
        Resources=[
            'ami-78a54011',
        ],
        Tags=[
            {
                'Key': 'Stack',
                'Value': 'test',
            },
        ],
    )
    
    print(response)
    
    
    """
    pass

def delete_volume(DryRun=None, VolumeId=None):
    """
    Deletes the specified EBS volume. The volume must be in the available state (not attached to an instance).
    For more information, see Deleting an Amazon EBS Volume in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example deletes an available volume with the volume ID of vol-049df61146c4d7901. If the command succeeds, no output is returned.
    Expected Output:
    
    :example: response = client.delete_volume(
        DryRun=True|False,
        VolumeId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeId: string
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            

    :return: response = client.delete_volume(
        VolumeId='vol-049df61146c4d7901',
    )
    
    print(response)
    
    
    """
    pass

def delete_vpc(DryRun=None, VpcId=None):
    """
    Deletes the specified VPC. You must detach or delete all gateways and resources that are associated with the VPC before you can delete it. For example, you must terminate all instances running in the VPC, delete all security groups associated with the VPC (except the default one), delete all route tables associated with the VPC (except the default one), and so on.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified VPC.
    Expected Output:
    
    :example: response = client.delete_vpc(
        DryRun=True|False,
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :return: response = client.delete_vpc(
        VpcId='vpc-a01106c2',
    )
    
    print(response)
    
    
    """
    pass

def delete_vpc_endpoints(DryRun=None, VpcEndpointIds=None):
    """
    Deletes one or more specified VPC endpoints. Deleting the endpoint also deletes the endpoint routes in the route tables that were associated with the endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vpc_endpoints(
        DryRun=True|False,
        VpcEndpointIds=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcEndpointIds: list
    :param VpcEndpointIds: [REQUIRED]
            One or more endpoint IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'Unsuccessful': [
            {
                'ResourceId': 'string',
                'Error': {
                    'Code': 'string',
                    'Message': 'string'
                }
            },
        ]
    }
    
    
    """
    pass

def delete_vpc_peering_connection(DryRun=None, VpcPeeringConnectionId=None):
    """
    Deletes a VPC peering connection. Either the owner of the requester VPC or the owner of the peer VPC can delete the VPC peering connection if it's in the active state. The owner of the requester VPC can delete a VPC peering connection in the pending-acceptance state.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vpc_peering_connection(
        DryRun=True|False,
        VpcPeeringConnectionId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcPeeringConnectionId: string
    :param VpcPeeringConnectionId: [REQUIRED]
            The ID of the VPC peering connection.
            

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def delete_vpn_connection(DryRun=None, VpnConnectionId=None):
    """
    Deletes the specified VPN connection.
    If you're deleting the VPC and its associated components, we recommend that you detach the virtual private gateway from the VPC and delete the VPC before deleting the VPN connection. If you believe that the tunnel credentials for your VPN connection have been compromised, you can delete the VPN connection and create a new one that has new keys, without needing to delete the VPC or virtual private gateway. If you create a new VPN connection, you must reconfigure the customer gateway using the new configuration information returned with the new VPN connection ID.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vpn_connection(
        DryRun=True|False,
        VpnConnectionId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpnConnectionId: string
    :param VpnConnectionId: [REQUIRED]
            The ID of the VPN connection.
            

    """
    pass

def delete_vpn_connection_route(VpnConnectionId=None, DestinationCidrBlock=None):
    """
    Deletes the specified static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vpn_connection_route(
        VpnConnectionId='string',
        DestinationCidrBlock='string'
    )
    
    
    :type VpnConnectionId: string
    :param VpnConnectionId: [REQUIRED]
            The ID of the VPN connection.
            

    :type DestinationCidrBlock: string
    :param DestinationCidrBlock: [REQUIRED]
            The CIDR block associated with the local subnet of the customer network.
            

    """
    pass

def delete_vpn_gateway(DryRun=None, VpnGatewayId=None):
    """
    Deletes the specified virtual private gateway. We recommend that before you delete a virtual private gateway, you detach it from the VPC and delete the VPN connection. Note that you don't need to delete the virtual private gateway if you plan to delete and recreate the VPN connection between your VPC and your network.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vpn_gateway(
        DryRun=True|False,
        VpnGatewayId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpnGatewayId: string
    :param VpnGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            

    """
    pass

def deregister_image(DryRun=None, ImageId=None):
    """
    Deregisters the specified AMI. After you deregister an AMI, it can't be used to launch new instances.
    This command does not delete the AMI.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_image(
        DryRun=True|False,
        ImageId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImageId: string
    :param ImageId: [REQUIRED]
            The ID of the AMI.
            

    """
    pass

def describe_account_attributes(DryRun=None, AttributeNames=None):
    """
    Describes attributes of your AWS account. The following are the supported account attributes:
    See also: AWS API Documentation
    
    Examples
    This example describes the supported-platforms attribute for your AWS account.
    Expected Output:
    This example describes the attributes for your AWS account.
    Expected Output:
    
    :example: response = client.describe_account_attributes(
        DryRun=True|False,
        AttributeNames=[
            'supported-platforms'|'default-vpc',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type AttributeNames: list
    :param AttributeNames: One or more account attribute names.
            (string) --
            

    :rtype: dict
    :return: {
        'AccountAttributes': [
            {
                'AttributeName': 'string',
                'AttributeValues': [
                    {
                        'AttributeValue': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    DryRun (boolean) -- Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    AttributeNames (list) -- One or more account attribute names.
    
    (string) --
    
    
    
    """
    pass

def describe_addresses(DryRun=None, PublicIps=None, Filters=None, AllocationIds=None):
    """
    Describes one or more of your Elastic IP addresses.
    An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes your Elastic IP addresses.
    Expected Output:
    This example describes your Elastic IP addresses for use with instances in a VPC.
    Expected Output:
    This example describes your Elastic IP addresses for use with instances in EC2-Classic.
    Expected Output:
    
    :example: response = client.describe_addresses(
        DryRun=True|False,
        PublicIps=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        AllocationIds=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type PublicIps: list
    :param PublicIps: [EC2-Classic] One or more Elastic IP addresses.
            Default: Describes all your Elastic IP addresses.
            (string) --
            

    :type Filters: list
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
            
            

    :type AllocationIds: list
    :param AllocationIds: [EC2-VPC] One or more allocation IDs.
            Default: Describes all your Elastic IP addresses.
            (string) --
            

    :rtype: dict
    :return: {
        'Addresses': [
            {
                'InstanceId': 'string',
                'PublicIp': 'string',
                'AllocationId': 'string',
                'AssociationId': 'string',
                'Domain': 'vpc'|'standard',
                'NetworkInterfaceId': 'string',
                'NetworkInterfaceOwnerId': 'string',
                'PrivateIpAddress': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_availability_zones(DryRun=None, ZoneNames=None, Filters=None):
    """
    Describes one or more of the Availability Zones that are available to you. The results include zones only for the region you're currently using. If there is an event impacting an Availability Zone, you can use this request to view the state and any provided message for that Availability Zone.
    For more information, see Regions and Availability Zones in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the Availability Zones that are available to you. The response includes Availability Zones only for the current region.
    Expected Output:
    
    :example: response = client.describe_availability_zones(
        DryRun=True|False,
        ZoneNames=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ZoneNames: list
    :param ZoneNames: The names of one or more Availability Zones.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            message - Information about the Availability Zone.
            region-name - The name of the region for the Availability Zone (for example, us-east-1 ).
            state - The state of the Availability Zone (available | information | impaired | unavailable ).
            zone-name - The name of the Availability Zone (for example, us-east-1a ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'AvailabilityZones': [
            {
                'ZoneName': 'string',
                'State': 'available'|'information'|'impaired'|'unavailable',
                'RegionName': 'string',
                'Messages': [
                    {
                        'Message': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_bundle_tasks(DryRun=None, BundleIds=None, Filters=None):
    """
    Describes one or more of your bundling tasks.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_bundle_tasks(
        DryRun=True|False,
        BundleIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type BundleIds: list
    :param BundleIds: One or more bundle task IDs.
            Default: Describes all your bundle tasks.
            (string) --
            

    :type Filters: list
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
            
            

    :rtype: dict
    :return: {
        'BundleTasks': [
            {
                'InstanceId': 'string',
                'BundleId': 'string',
                'State': 'pending'|'waiting-for-shutdown'|'bundling'|'storing'|'cancelling'|'complete'|'failed',
                'StartTime': datetime(2015, 1, 1),
                'UpdateTime': datetime(2015, 1, 1),
                'Storage': {
                    'S3': {
                        'Bucket': 'string',
                        'Prefix': 'string',
                        'AWSAccessKeyId': 'string',
                        'UploadPolicy': b'bytes',
                        'UploadPolicySignature': 'string'
                    }
                },
                'Progress': 'string',
                'BundleTaskError': {
                    'Code': 'string',
                    'Message': 'string'
                }
            },
        ]
    }
    
    
    """
    pass

def describe_classic_link_instances(DryRun=None, InstanceIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Describes one or more of your linked EC2-Classic instances. This request only returns information about EC2-Classic instances linked to a VPC through ClassicLink; you cannot use this request to return information about other instances.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_classic_link_instances(
        DryRun=True|False,
        InstanceIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceIds: list
    :param InstanceIds: One or more instance IDs. Must be instances linked to a VPC through ClassicLink.
            (string) --
            

    :type Filters: list
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
            
            

    :type NextToken: string
    :param NextToken: The token to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. You cannot specify this parameter and the instance IDs parameter in the same request.
            Constraint: If the value is greater than 1000, we return only 1000 items.
            

    :rtype: dict
    :return: {
        'Instances': [
            {
                'InstanceId': 'string',
                'VpcId': 'string',
                'Groups': [
                    {
                        'GroupName': 'string',
                        'GroupId': 'string'
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_conversion_tasks(DryRun=None, ConversionTaskIds=None):
    """
    Describes one or more of your conversion tasks. For more information, see the VM Import/Export User Guide .
    For information about the import manifest referenced by this API action, see VM Import Manifest .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_conversion_tasks(
        DryRun=True|False,
        ConversionTaskIds=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ConversionTaskIds: list
    :param ConversionTaskIds: One or more conversion task IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'ConversionTasks': [
            {
                'ConversionTaskId': 'string',
                'ExpirationTime': 'string',
                'ImportInstance': {
                    'Volumes': [
                        {
                            'BytesConverted': 123,
                            'AvailabilityZone': 'string',
                            'Image': {
                                'Format': 'VMDK'|'RAW'|'VHD',
                                'Size': 123,
                                'ImportManifestUrl': 'string',
                                'Checksum': 'string'
                            },
                            'Volume': {
                                'Size': 123,
                                'Id': 'string'
                            },
                            'Status': 'string',
                            'StatusMessage': 'string',
                            'Description': 'string'
                        },
                    ],
                    'InstanceId': 'string',
                    'Platform': 'Windows',
                    'Description': 'string'
                },
                'ImportVolume': {
                    'BytesConverted': 123,
                    'AvailabilityZone': 'string',
                    'Description': 'string',
                    'Image': {
                        'Format': 'VMDK'|'RAW'|'VHD',
                        'Size': 123,
                        'ImportManifestUrl': 'string',
                        'Checksum': 'string'
                    },
                    'Volume': {
                        'Size': 123,
                        'Id': 'string'
                    }
                },
                'State': 'active'|'cancelling'|'cancelled'|'completed',
                'StatusMessage': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_customer_gateways(DryRun=None, CustomerGatewayIds=None, Filters=None):
    """
    Describes one or more of your VPN customer gateways.
    For more information about VPN customer gateways, see Adding a Hardware Virtual Private Gateway to Your VPC in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the specified customer gateway.
    Expected Output:
    
    :example: response = client.describe_customer_gateways(
        DryRun=True|False,
        CustomerGatewayIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type CustomerGatewayIds: list
    :param CustomerGatewayIds: One or more customer gateway IDs.
            Default: Describes all your customer gateways.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            bgp-asn - The customer gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
            customer-gateway-id - The ID of the customer gateway.
            ip-address - The IP address of the customer gateway's Internet-routable external interface.
            state - The state of the customer gateway (pending | available | deleting | deleted ).
            type - The type of customer gateway. Currently, the only supported type is ipsec.1 .
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'CustomerGateways': [
            {
                'CustomerGatewayId': 'string',
                'State': 'string',
                'Type': 'string',
                'IpAddress': 'string',
                'BgpAsn': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_dhcp_options(DryRun=None, DhcpOptionsIds=None, Filters=None):
    """
    Describes one or more of your DHCP options sets.
    For more information about DHCP options sets, see DHCP Options Sets in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the specified DHCP options set.
    Expected Output:
    
    :example: response = client.describe_dhcp_options(
        DryRun=True|False,
        DhcpOptionsIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type DhcpOptionsIds: list
    :param DhcpOptionsIds: The IDs of one or more DHCP options sets.
            Default: Describes all your DHCP options sets.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            dhcp-options-id - The ID of a set of DHCP options.
            key - The key for one of the options (for example, domain-name ).
            value - The value for one of the options.
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'DhcpOptions': [
            {
                'DhcpOptionsId': 'string',
                'DhcpConfigurations': [
                    {
                        'Key': 'string',
                        'Values': [
                            {
                                'Value': 'string'
                            },
                        ]
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_egress_only_internet_gateways(DryRun=None, EgressOnlyInternetGatewayIds=None, MaxResults=None, NextToken=None):
    """
    Describes one or more of your egress-only Internet gateways.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_egress_only_internet_gateways(
        DryRun=True|False,
        EgressOnlyInternetGatewayIds=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type EgressOnlyInternetGatewayIds: list
    :param EgressOnlyInternetGatewayIds: One or more egress-only Internet gateway IDs.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned.

    :type NextToken: string
    :param NextToken: The token to retrieve the next page of results.

    :rtype: dict
    :return: {
        'EgressOnlyInternetGateways': [
            {
                'EgressOnlyInternetGatewayId': 'string',
                'Attachments': [
                    {
                        'VpcId': 'string',
                        'State': 'attaching'|'attached'|'detaching'|'detached'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_export_tasks(ExportTaskIds=None):
    """
    Describes one or more of your export tasks.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_export_tasks(
        ExportTaskIds=[
            'string',
        ]
    )
    
    
    :type ExportTaskIds: list
    :param ExportTaskIds: One or more export task IDs.
            (string) --
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_flow_logs(FlowLogIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Describes one or more flow logs. To view the information in your flow logs (the log streams for the network interfaces), you must use the CloudWatch Logs console or the CloudWatch Logs API.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_flow_logs(
        FlowLogIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type FlowLogIds: list
    :param FlowLogIds: One or more flow log IDs.
            (string) --
            

    :type Filters: list
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
            
            

    :type NextToken: string
    :param NextToken: The token to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. You cannot specify this parameter and the flow log IDs parameter in the same request.

    :rtype: dict
    :return: {
        'FlowLogs': [
            {
                'CreationTime': datetime(2015, 1, 1),
                'FlowLogId': 'string',
                'FlowLogStatus': 'string',
                'ResourceId': 'string',
                'TrafficType': 'ACCEPT'|'REJECT'|'ALL',
                'LogGroupName': 'string',
                'DeliverLogsStatus': 'string',
                'DeliverLogsErrorMessage': 'string',
                'DeliverLogsPermissionArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_host_reservation_offerings(OfferingId=None, MinDuration=None, MaxDuration=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes the Dedicated Host Reservations that are available to purchase.
    The results describe all the Dedicated Host Reservation offerings, including offerings that may not match the instance family and region of your Dedicated Hosts. When purchasing an offering, ensure that the the instance family and region of the offering matches that of the Dedicated Host/s it will be associated with. For an overview of supported instance types, see Dedicated Hosts Overview in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_host_reservation_offerings(
        OfferingId='string',
        MinDuration=123,
        MaxDuration=123,
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type OfferingId: string
    :param OfferingId: The ID of the reservation offering.

    :type MinDuration: integer
    :param MinDuration: This is the minimum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 31536000 for one year.

    :type MaxDuration: integer
    :param MaxDuration: This is the maximum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 94608000 for three years.

    :type Filters: list
    :param Filters: One or more filters.
            instance-family - The instance family of the offering (e.g., m4 ).
            payment-option - The payment option (NoUpfront | PartialUpfront | AllUpfront ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned nextToken value. This value can be between 5 and 500; if maxResults is given a larger value than 500, you will receive an error.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :rtype: dict
    :return: {
        'OfferingSet': [
            {
                'OfferingId': 'string',
                'InstanceFamily': 'string',
                'PaymentOption': 'AllUpfront'|'PartialUpfront'|'NoUpfront',
                'UpfrontPrice': 'string',
                'HourlyPrice': 'string',
                'CurrencyCode': 'USD',
                'Duration': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_host_reservations(HostReservationIdSet=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes Dedicated Host Reservations which are associated with Dedicated Hosts in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_host_reservations(
        HostReservationIdSet=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type HostReservationIdSet: list
    :param HostReservationIdSet: One or more host reservation IDs.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            instance-family - The instance family (e.g., m4 ).
            payment-option - The payment option (NoUpfront | PartialUpfront | AllUpfront ).
            state - The state of the reservation (payment-pending | payment-failed | active | retired ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned nextToken value. This value can be between 5 and 500; if maxResults is given a larger value than 500, you will receive an error.

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :rtype: dict
    :return: {
        'HostReservationSet': [
            {
                'HostReservationId': 'string',
                'HostIdSet': [
                    'string',
                ],
                'OfferingId': 'string',
                'InstanceFamily': 'string',
                'PaymentOption': 'AllUpfront'|'PartialUpfront'|'NoUpfront',
                'HourlyPrice': 'string',
                'UpfrontPrice': 'string',
                'CurrencyCode': 'USD',
                'Count': 123,
                'Duration': 123,
                'End': datetime(2015, 1, 1),
                'Start': datetime(2015, 1, 1),
                'State': 'payment-pending'|'payment-failed'|'active'|'retired'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_hosts(HostIds=None, NextToken=None, MaxResults=None, Filters=None):
    """
    Describes one or more of your Dedicated Hosts.
    The results describe only the Dedicated Hosts in the region you're currently using. All listed instances consume capacity on your Dedicated Host. Dedicated Hosts that have recently been released will be listed with the state released .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_hosts(
        HostIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type HostIds: list
    :param HostIds: The IDs of the Dedicated Hosts. The IDs are used for targeted instance launches.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned nextToken value. This value can be between 5 and 500; if maxResults is given a larger value than 500, you will receive an error. You cannot specify this parameter and the host IDs parameter in the same request.

    :type Filters: list
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
            
            

    :rtype: dict
    :return: {
        'Hosts': [
            {
                'HostId': 'string',
                'AutoPlacement': 'on'|'off',
                'HostReservationId': 'string',
                'ClientToken': 'string',
                'HostProperties': {
                    'Sockets': 123,
                    'Cores': 123,
                    'TotalVCpus': 123,
                    'InstanceType': 'string'
                },
                'State': 'available'|'under-assessment'|'permanent-failure'|'released'|'released-permanent-failure',
                'AvailabilityZone': 'string',
                'Instances': [
                    {
                        'InstanceId': 'string',
                        'InstanceType': 'string'
                    },
                ],
                'AvailableCapacity': {
                    'AvailableInstanceCapacity': [
                        {
                            'InstanceType': 'string',
                            'AvailableCapacity': 123,
                            'TotalCapacity': 123
                        },
                    ],
                    'AvailableVCpus': 123
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_iam_instance_profile_associations(AssociationIds=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes your IAM instance profile associations.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_iam_instance_profile_associations(
        AssociationIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AssociationIds: list
    :param AssociationIds: One or more IAM instance profile associations.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            instance-id - The ID of the instance.
            state - The state of the association (associating | associated | disassociating | disassociated ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :rtype: dict
    :return: {
        'IamInstanceProfileAssociations': [
            {
                'AssociationId': 'string',
                'InstanceId': 'string',
                'IamInstanceProfile': {
                    'Arn': 'string',
                    'Id': 'string'
                },
                'State': 'associating'|'associated'|'disassociating'|'disassociated',
                'Timestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_id_format(Resource=None):
    """
    Describes the ID format settings for your resources on a per-region basis, for example, to view which resource types are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types.
    The following resource types support longer IDs: instance | reservation | snapshot | volume .
    These settings apply to the IAM user who makes the request; they do not apply to the entire AWS account. By default, an IAM user defaults to the same settings as the root user, unless they explicitly override the settings by running the  ModifyIdFormat command. Resources created with longer IDs are visible to all IAM users, regardless of these settings and provided that they have permission to use the relevant Describe command for the resource type.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_id_format(
        Resource='string'
    )
    
    
    :type Resource: string
    :param Resource: The type of resource: instance | reservation | snapshot | volume

    :rtype: dict
    :return: {
        'Statuses': [
            {
                'Resource': 'string',
                'UseLongIds': True|False,
                'Deadline': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def describe_identity_id_format(Resource=None, PrincipalArn=None):
    """
    Describes the ID format settings for resources for the specified IAM user, IAM role, or root user. For example, you can view the resource types that are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types. For more information, see Resource IDs in the Amazon Elastic Compute Cloud User Guide .
    The following resource types support longer IDs: instance | reservation | snapshot | volume .
    These settings apply to the principal specified in the request. They do not apply to the principal that makes the request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_identity_id_format(
        Resource='string',
        PrincipalArn='string'
    )
    
    
    :type Resource: string
    :param Resource: The type of resource: instance | reservation | snapshot | volume

    :type PrincipalArn: string
    :param PrincipalArn: [REQUIRED]
            The ARN of the principal, which can be an IAM role, IAM user, or the root user.
            

    :rtype: dict
    :return: {
        'Statuses': [
            {
                'Resource': 'string',
                'UseLongIds': True|False,
                'Deadline': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def describe_image_attribute(DryRun=None, ImageId=None, Attribute=None):
    """
    Describes the specified attribute of the specified AMI. You can specify only one attribute at a time.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_image_attribute(
        DryRun=True|False,
        ImageId='string',
        Attribute='description'|'kernel'|'ramdisk'|'launchPermission'|'productCodes'|'blockDeviceMapping'|'sriovNetSupport'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImageId: string
    :param ImageId: [REQUIRED]
            The ID of the AMI.
            

    :type Attribute: string
    :param Attribute: [REQUIRED]
            The AMI attribute.
            Note : Depending on your account privileges, the blockDeviceMapping attribute may return a Client.AuthFailure error. If this happens, use DescribeImages to get information about the block device mapping for the AMI.
            

    :rtype: dict
    :return: {
        'ImageId': 'string',
        'LaunchPermissions': [
            {
                'UserId': 'string',
                'Group': 'all'
            },
        ],
        'ProductCodes': [
            {
                'ProductCodeId': 'string',
                'ProductCodeType': 'devpay'|'marketplace'
            },
        ],
        'KernelId': {
            'Value': 'string'
        },
        'RamdiskId': {
            'Value': 'string'
        },
        'Description': {
            'Value': 'string'
        },
        'SriovNetSupport': {
            'Value': 'string'
        },
        'BlockDeviceMappings': [
            {
                'VirtualName': 'string',
                'DeviceName': 'string',
                'Ebs': {
                    'SnapshotId': 'string',
                    'VolumeSize': 123,
                    'DeleteOnTermination': True|False,
                    'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                    'Iops': 123,
                    'Encrypted': True|False
                },
                'NoDevice': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_images(DryRun=None, ImageIds=None, Owners=None, ExecutableUsers=None, Filters=None):
    """
    Describes one or more of the images (AMIs, AKIs, and ARIs) available to you. Images available to you include public images, private images that you own, and private images owned by other AWS accounts but for which you have explicit launch permissions.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_images(
        DryRun=True|False,
        ImageIds=[
            'string',
        ],
        Owners=[
            'string',
        ],
        ExecutableUsers=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImageIds: list
    :param ImageIds: One or more image IDs.
            Default: Describes all images available to you.
            (string) --
            

    :type Owners: list
    :param Owners: Filters the images by the owner. Specify an AWS account ID, self (owner is the sender of the request), or an AWS owner alias (valid values are amazon | aws-marketplace | microsoft ). Omitting this option returns all images for which you have launch permissions, regardless of ownership.
            (string) --
            

    :type ExecutableUsers: list
    :param ExecutableUsers: Scopes the images by users with explicit launch permissions. Specify an AWS account ID, self (the sender of the request), or all (public AMIs).
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            architecture - The image architecture (i386 | x86_64 ).
            block-device-mapping.delete-on-termination - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination.
            block-device-mapping.device-name - The device name for the EBS volume (for example, /dev/sdh ).
            block-device-mapping.snapshot-id - The ID of the snapshot used for the EBS volume.
            block-device-mapping.volume-size - The volume size of the EBS volume, in GiB.
            block-device-mapping.volume-type - The volume type of the EBS volume (gp2 | io1 | st1 | sc1 | standard ).
            description - The description of the image (provided during image creation).
            ena-support - A Boolean that indicates whether enhanced networking with ENA is enabled.
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
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            virtualization-type - The virtualization type (paravirtual | hvm ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'Images': [
            {
                'ImageId': 'string',
                'ImageLocation': 'string',
                'State': 'pending'|'available'|'invalid'|'deregistered'|'transient'|'failed'|'error',
                'OwnerId': 'string',
                'CreationDate': 'string',
                'Public': True|False,
                'ProductCodes': [
                    {
                        'ProductCodeId': 'string',
                        'ProductCodeType': 'devpay'|'marketplace'
                    },
                ],
                'Architecture': 'i386'|'x86_64',
                'ImageType': 'machine'|'kernel'|'ramdisk',
                'KernelId': 'string',
                'RamdiskId': 'string',
                'Platform': 'Windows',
                'SriovNetSupport': 'string',
                'EnaSupport': True|False,
                'StateReason': {
                    'Code': 'string',
                    'Message': 'string'
                },
                'ImageOwnerAlias': 'string',
                'Name': 'string',
                'Description': 'string',
                'RootDeviceType': 'ebs'|'instance-store',
                'RootDeviceName': 'string',
                'BlockDeviceMappings': [
                    {
                        'VirtualName': 'string',
                        'DeviceName': 'string',
                        'Ebs': {
                            'SnapshotId': 'string',
                            'VolumeSize': 123,
                            'DeleteOnTermination': True|False,
                            'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                            'Iops': 123,
                            'Encrypted': True|False
                        },
                        'NoDevice': 'string'
                    },
                ],
                'VirtualizationType': 'hvm'|'paravirtual',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Hypervisor': 'ovm'|'xen'
            },
        ]
    }
    
    
    :returns: 
    Server.InsufficientInstanceCapacity : There was insufficient instance capacity to satisfy the launch request.
    Server.InternalError : An internal error occurred during instance launch, resulting in termination.
    Server.ScheduledStop : The instance was stopped due to a scheduled retirement.
    Server.SpotInstanceTermination : A Spot instance was terminated due to an increase in the market price.
    Client.InternalError : A client error caused the instance to terminate on launch.
    Client.InstanceInitiatedShutdown : The instance was shut down using the shutdown -h command from the instance.
    Client.UserInitiatedShutdown : The instance was shut down using the Amazon EC2 API.
    Client.VolumeLimitExceeded : The limit on the number of EBS volumes or total storage was exceeded. Decrease usage or request an increase in your limits.
    Client.InvalidSnapshot.NotFound : The specified snapshot was not found.
    
    """
    pass

def describe_import_image_tasks(DryRun=None, ImportTaskIds=None, NextToken=None, MaxResults=None, Filters=None):
    """
    Displays details about an import virtual machine or import snapshot tasks that are already created.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_import_image_tasks(
        DryRun=True|False,
        ImportTaskIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImportTaskIds: list
    :param ImportTaskIds: A list of import image task IDs.
            (string) --
            

    :type NextToken: string
    :param NextToken: A token that indicates the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type Filters: list
    :param Filters: Filter tasks using the task-state filter and one of the following values: active, completed, deleting, deleted.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'ImportImageTasks': [
            {
                'ImportTaskId': 'string',
                'Architecture': 'string',
                'LicenseType': 'string',
                'Platform': 'string',
                'Hypervisor': 'string',
                'Description': 'string',
                'SnapshotDetails': [
                    {
                        'DiskImageSize': 123.0,
                        'Description': 'string',
                        'Format': 'string',
                        'Url': 'string',
                        'UserBucket': {
                            'S3Bucket': 'string',
                            'S3Key': 'string'
                        },
                        'DeviceName': 'string',
                        'SnapshotId': 'string',
                        'Progress': 'string',
                        'StatusMessage': 'string',
                        'Status': 'string'
                    },
                ],
                'ImageId': 'string',
                'Progress': 'string',
                'StatusMessage': 'string',
                'Status': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_import_snapshot_tasks(DryRun=None, ImportTaskIds=None, NextToken=None, MaxResults=None, Filters=None):
    """
    Describes your import snapshot tasks.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_import_snapshot_tasks(
        DryRun=True|False,
        ImportTaskIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImportTaskIds: list
    :param ImportTaskIds: A list of import snapshot task IDs.
            (string) --
            

    :type NextToken: string
    :param NextToken: A token that indicates the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type Filters: list
    :param Filters: One or more filters.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'ImportSnapshotTasks': [
            {
                'ImportTaskId': 'string',
                'SnapshotTaskDetail': {
                    'DiskImageSize': 123.0,
                    'Description': 'string',
                    'Format': 'string',
                    'Url': 'string',
                    'UserBucket': {
                        'S3Bucket': 'string',
                        'S3Key': 'string'
                    },
                    'SnapshotId': 'string',
                    'Progress': 'string',
                    'StatusMessage': 'string',
                    'Status': 'string'
                },
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_instance_attribute(DryRun=None, InstanceId=None, Attribute=None):
    """
    Describes the specified attribute of the specified instance. You can specify only one attribute at a time. Valid attribute values are: instanceType | kernel | ramdisk | userData | disableApiTermination | instanceInitiatedShutdownBehavior | rootDeviceName | blockDeviceMapping | productCodes | sourceDestCheck | groupSet | ebsOptimized | sriovNetSupport
    See also: AWS API Documentation
    
    Examples
    This example describes the instance type of the specified instance.
    Expected Output:
    This example describes the disableApiTermination attribute of the specified instance.
    Expected Output:
    This example describes the blockDeviceMapping attribute of the specified instance.
    Expected Output:
    
    :example: response = client.describe_instance_attribute(
        DryRun=True|False,
        InstanceId='string',
        Attribute='instanceType'|'kernel'|'ramdisk'|'userData'|'disableApiTermination'|'instanceInitiatedShutdownBehavior'|'rootDeviceName'|'blockDeviceMapping'|'productCodes'|'sourceDestCheck'|'groupSet'|'ebsOptimized'|'sriovNetSupport'|'enaSupport'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type Attribute: string
    :param Attribute: [REQUIRED]
            The instance attribute.
            Note: The enaSupport attribute is not supported at this time.
            

    :rtype: dict
    :return: {
        'InstanceId': 'string',
        'InstanceType': {
            'Value': 'string'
        },
        'KernelId': {
            'Value': 'string'
        },
        'RamdiskId': {
            'Value': 'string'
        },
        'UserData': {
            'Value': 'string'
        },
        'DisableApiTermination': {
            'Value': True|False
        },
        'InstanceInitiatedShutdownBehavior': {
            'Value': 'string'
        },
        'RootDeviceName': {
            'Value': 'string'
        },
        'BlockDeviceMappings': [
            {
                'DeviceName': 'string',
                'Ebs': {
                    'VolumeId': 'string',
                    'Status': 'attaching'|'attached'|'detaching'|'detached',
                    'AttachTime': datetime(2015, 1, 1),
                    'DeleteOnTermination': True|False
                }
            },
        ],
        'ProductCodes': [
            {
                'ProductCodeId': 'string',
                'ProductCodeType': 'devpay'|'marketplace'
            },
        ],
        'EbsOptimized': {
            'Value': True|False
        },
        'SriovNetSupport': {
            'Value': 'string'
        },
        'EnaSupport': {
            'Value': True|False
        },
        'SourceDestCheck': {
            'Value': True|False
        },
        'Groups': [
            {
                'GroupName': 'string',
                'GroupId': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_instance_status(DryRun=None, InstanceIds=None, Filters=None, NextToken=None, MaxResults=None, IncludeAllInstances=None):
    """
    Describes the status of one or more instances. By default, only running instances are described, unless specified otherwise.
    Instance status includes the following components:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_instance_status(
        DryRun=True|False,
        InstanceIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123,
        IncludeAllInstances=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceIds: list
    :param InstanceIds: One or more instance IDs.
            Default: Describes all your instances.
            Constraints: Maximum 100 explicitly specified instance IDs.
            (string) --
            

    :type Filters: list
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
            
            

    :type NextToken: string
    :param NextToken: The token to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.

    :type IncludeAllInstances: boolean
    :param IncludeAllInstances: When true , includes the health status for all instances. When false , includes the health status for running instances only.
            Default: false
            

    :rtype: dict
    :return: {
        'InstanceStatuses': [
            {
                'InstanceId': 'string',
                'AvailabilityZone': 'string',
                'Events': [
                    {
                        'Code': 'instance-reboot'|'system-reboot'|'system-maintenance'|'instance-retirement'|'instance-stop',
                        'Description': 'string',
                        'NotBefore': datetime(2015, 1, 1),
                        'NotAfter': datetime(2015, 1, 1)
                    },
                ],
                'InstanceState': {
                    'Code': 123,
                    'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                },
                'SystemStatus': {
                    'Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing',
                    'Details': [
                        {
                            'Name': 'reachability',
                            'Status': 'passed'|'failed'|'insufficient-data'|'initializing',
                            'ImpairedSince': datetime(2015, 1, 1)
                        },
                    ]
                },
                'InstanceStatus': {
                    'Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing',
                    'Details': [
                        {
                            'Name': 'reachability',
                            'Status': 'passed'|'failed'|'insufficient-data'|'initializing',
                            'ImpairedSince': datetime(2015, 1, 1)
                        },
                    ]
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DryRun (boolean) -- Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    InstanceIds (list) -- One or more instance IDs.
    Default: Describes all your instances.
    Constraints: Maximum 100 explicitly specified instance IDs.
    
    (string) --
    
    
    Filters (list) -- One or more filters.
    
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
    
    
    
    
    
    
    NextToken (string) -- The token to retrieve the next page of results.
    MaxResults (integer) -- The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
    IncludeAllInstances (boolean) -- When true , includes the health status for all instances. When false , includes the health status for running instances only.
    Default: false
    
    
    """
    pass

def describe_instances(DryRun=None, InstanceIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Describes one or more of your instances.
    If you specify one or more instance IDs, Amazon EC2 returns information for those instances. If you do not specify instance IDs, Amazon EC2 returns information for all relevant instances. If you specify an instance ID that is not valid, an error is returned. If you specify an instance that you do not own, it is not included in the returned results.
    Recently terminated instances might appear in the returned results. This interval is usually less than one hour.
    If you describe instances in the rare case where an Availability Zone is experiencing a service disruption and you specify instance IDs that are in the affected zone, or do not specify any instance IDs at all, the call fails. If you describe instances and specify only instance IDs that are in an unaffected zone, the call works normally.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_instances(
        DryRun=True|False,
        InstanceIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceIds: list
    :param InstanceIds: One or more instance IDs.
            Default: Describes all your instances.
            (string) --
            

    :type Filters: list
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
            ip-address - The public IPv4 address of the instance.
            kernel-id - The kernel ID.
            key-name - The name of the key pair used when the instance was launched.
            launch-index - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).
            launch-time - The time when the instance was launched.
            monitoring-state - Indicates whether detailed monitoring is enabled (disabled | enabled ).
            network-interface.addresses.private-ip-address - The private IPv4 address associated with the network interface.
            network-interface.addresses.primary - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address.
            network-interface.addresses.association.public-ip - The ID of the association of an Elastic IP address (IPv4) with a network interface.
            network-interface.addresses.association.ip-owner-id - The owner ID of the private IPv4 address associated with the network interface.
            network-interface.association.public-ip - The address of the Elastic IP address (IPv4) bound to the network interface.
            network-interface.association.ip-owner-id - The owner of the Elastic IP address (IPv4) associated with the network interface.
            network-interface.association.allocation-id - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface.
            network-interface.association.association-id - The association ID returned when the network interface was associated with an IPv4 address.
            network-interface.attachment.attachment-id - The ID of the interface attachment.
            network-interface.attachment.instance-id - The ID of the instance to which the network interface is attached.
            network-interface.attachment.instance-owner-id - The owner ID of the instance to which the network interface is attached.
            network-interface.attachment.device-index - The device index to which the network interface is attached.
            network-interface.attachment.status - The status of the attachment (attaching | attached | detaching | detached ).
            network-interface.attachment.attach-time - The time that the network interface was attached to an instance.
            network-interface.attachment.delete-on-termination - Specifies whether the attachment is deleted when an instance is terminated.
            network-interface.availability-zone - The Availability Zone for the network interface.
            network-interface.description - The description of the network interface.
            network-interface.group-id - The ID of a security group associated with the network interface.
            network-interface.group-name - The name of a security group associated with the network interface.
            network-interface.ipv6-addresses.ipv6-address - The IPv6 address associated with the network interface.
            network-interface.mac-address - The MAC address of the network interface.
            network-interface.network-interface-id - The ID of the network interface.
            network-interface.owner-id - The ID of the owner of the network interface.
            network-interface.private-dns-name - The private DNS name of the network interface.
            network-interface.requester-id - The requester ID for the network interface.
            network-interface.requester-managed - Indicates whether the network interface is being managed by AWS.
            network-interface.status - The status of the network interface (available ) | in-use ).
            network-interface.source-dest-check - Whether the network interface performs source/destination checking. A value of true means checking is enabled, and false means checking is disabled. The value must be false for the network interface to perform network address translation (NAT) in your VPC.
            network-interface.subnet-id - The ID of the subnet for the network interface.
            network-interface.vpc-id - The ID of the VPC for the network interface.
            owner-id - The AWS account ID of the instance owner.
            placement-group-name - The name of the placement group for the instance.
            platform - The platform. Use windows if you have Windows instances; otherwise, leave blank.
            private-dns-name - The private IPv4 DNS name of the instance.
            private-ip-address - The private IPv4 address of the instance.
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
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            tenancy - The tenancy of an instance (dedicated | default | host ).
            virtualization-type - The virtualization type of the instance (paravirtual | hvm ).
            vpc-id - The ID of the VPC that the instance is running in.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter or tag filters in the same call.

    :rtype: dict
    :return: {
        'Reservations': [
            {
                'ReservationId': 'string',
                'OwnerId': 'string',
                'RequesterId': 'string',
                'Groups': [
                    {
                        'GroupName': 'string',
                        'GroupId': 'string'
                    },
                ],
                'Instances': [
                    {
                        'InstanceId': 'string',
                        'ImageId': 'string',
                        'State': {
                            'Code': 123,
                            'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                        },
                        'PrivateDnsName': 'string',
                        'PublicDnsName': 'string',
                        'StateTransitionReason': 'string',
                        'KeyName': 'string',
                        'AmiLaunchIndex': 123,
                        'ProductCodes': [
                            {
                                'ProductCodeId': 'string',
                                'ProductCodeType': 'devpay'|'marketplace'
                            },
                        ],
                        'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                        'LaunchTime': datetime(2015, 1, 1),
                        'Placement': {
                            'AvailabilityZone': 'string',
                            'GroupName': 'string',
                            'Tenancy': 'default'|'dedicated'|'host',
                            'HostId': 'string',
                            'Affinity': 'string'
                        },
                        'KernelId': 'string',
                        'RamdiskId': 'string',
                        'Platform': 'Windows',
                        'Monitoring': {
                            'State': 'disabled'|'disabling'|'enabled'|'pending'
                        },
                        'SubnetId': 'string',
                        'VpcId': 'string',
                        'PrivateIpAddress': 'string',
                        'PublicIpAddress': 'string',
                        'StateReason': {
                            'Code': 'string',
                            'Message': 'string'
                        },
                        'Architecture': 'i386'|'x86_64',
                        'RootDeviceType': 'ebs'|'instance-store',
                        'RootDeviceName': 'string',
                        'BlockDeviceMappings': [
                            {
                                'DeviceName': 'string',
                                'Ebs': {
                                    'VolumeId': 'string',
                                    'Status': 'attaching'|'attached'|'detaching'|'detached',
                                    'AttachTime': datetime(2015, 1, 1),
                                    'DeleteOnTermination': True|False
                                }
                            },
                        ],
                        'VirtualizationType': 'hvm'|'paravirtual',
                        'InstanceLifecycle': 'spot'|'scheduled',
                        'SpotInstanceRequestId': 'string',
                        'ClientToken': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'SecurityGroups': [
                            {
                                'GroupName': 'string',
                                'GroupId': 'string'
                            },
                        ],
                        'SourceDestCheck': True|False,
                        'Hypervisor': 'ovm'|'xen',
                        'NetworkInterfaces': [
                            {
                                'NetworkInterfaceId': 'string',
                                'SubnetId': 'string',
                                'VpcId': 'string',
                                'Description': 'string',
                                'OwnerId': 'string',
                                'Status': 'available'|'attaching'|'in-use'|'detaching',
                                'MacAddress': 'string',
                                'PrivateIpAddress': 'string',
                                'PrivateDnsName': 'string',
                                'SourceDestCheck': True|False,
                                'Groups': [
                                    {
                                        'GroupName': 'string',
                                        'GroupId': 'string'
                                    },
                                ],
                                'Attachment': {
                                    'AttachmentId': 'string',
                                    'DeviceIndex': 123,
                                    'Status': 'attaching'|'attached'|'detaching'|'detached',
                                    'AttachTime': datetime(2015, 1, 1),
                                    'DeleteOnTermination': True|False
                                },
                                'Association': {
                                    'PublicIp': 'string',
                                    'PublicDnsName': 'string',
                                    'IpOwnerId': 'string'
                                },
                                'PrivateIpAddresses': [
                                    {
                                        'PrivateIpAddress': 'string',
                                        'PrivateDnsName': 'string',
                                        'Primary': True|False,
                                        'Association': {
                                            'PublicIp': 'string',
                                            'PublicDnsName': 'string',
                                            'IpOwnerId': 'string'
                                        }
                                    },
                                ],
                                'Ipv6Addresses': [
                                    {
                                        'Ipv6Address': 'string'
                                    },
                                ]
                            },
                        ],
                        'IamInstanceProfile': {
                            'Arn': 'string',
                            'Id': 'string'
                        },
                        'EbsOptimized': True|False,
                        'SriovNetSupport': 'string',
                        'EnaSupport': True|False
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    0 : pending
    16 : running
    32 : shutting-down
    48 : terminated
    64 : stopping
    80 : stopped
    
    """
    pass

def describe_internet_gateways(DryRun=None, InternetGatewayIds=None, Filters=None):
    """
    Describes one or more of your Internet gateways.
    See also: AWS API Documentation
    
    Examples
    This example describes the Internet gateway for the specified VPC.
    Expected Output:
    
    :example: response = client.describe_internet_gateways(
        DryRun=True|False,
        InternetGatewayIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InternetGatewayIds: list
    :param InternetGatewayIds: One or more Internet gateway IDs.
            Default: Describes all your Internet gateways.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            attachment.state - The current state of the attachment between the gateway and the VPC (available ). Present only if a VPC is attached.
            attachment.vpc-id - The ID of an attached VPC.
            internet-gateway-id - The ID of the Internet gateway.
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'InternetGateways': [
            {
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
            },
        ]
    }
    
    
    """
    pass

def describe_key_pairs(DryRun=None, KeyNames=None, Filters=None):
    """
    Describes one or more of your key pairs.
    For more information about key pairs, see Key Pairs in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example displays the fingerprint for the specified key.
    Expected Output:
    
    :example: response = client.describe_key_pairs(
        DryRun=True|False,
        KeyNames=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type KeyNames: list
    :param KeyNames: One or more key pair names.
            Default: Describes all your key pairs.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            fingerprint - The fingerprint of the key pair.
            key-name - The name of the key pair.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'KeyPairs': [
            {
                'KeyName': 'string',
                'KeyFingerprint': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_moving_addresses(DryRun=None, PublicIps=None, NextToken=None, Filters=None, MaxResults=None):
    """
    Describes your Elastic IP addresses that are being moved to the EC2-VPC platform, or that are being restored to the EC2-Classic platform. This request does not return information about any other Elastic IP addresses in your account.
    See also: AWS API Documentation
    
    Examples
    This example describes all of your moving Elastic IP addresses.
    Expected Output:
    
    :example: response = client.describe_moving_addresses(
        DryRun=True|False,
        PublicIps=[
            'string',
        ],
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type PublicIps: list
    :param PublicIps: One or more Elastic IP addresses.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results.

    :type Filters: list
    :param Filters: One or more filters.
            moving-status - The status of the Elastic IP address (MovingToVpc | RestoringToClassic ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value outside of this range, an error is returned.
            Default: If no value is provided, the default is 1000.
            

    :rtype: dict
    :return: {
        'MovingAddressStatuses': [
            {
                'PublicIp': 'string',
                'MoveStatus': 'movingToVpc'|'restoringToClassic'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_nat_gateways(NatGatewayIds=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes one or more of the your NAT gateways.
    See also: AWS API Documentation
    
    Examples
    This example describes the NAT gateway for the specified VPC.
    Expected Output:
    
    :example: response = client.describe_nat_gateways(
        NatGatewayIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type NatGatewayIds: list
    :param NatGatewayIds: One or more NAT gateway IDs.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            nat-gateway-id - The ID of the NAT gateway.
            state - The state of the NAT gateway (pending | failed | available | deleting | deleted ).
            subnet-id - The ID of the subnet in which the NAT gateway resides.
            vpc-id - The ID of the VPC in which the NAT gateway resides.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
            Constraint: If the value specified is greater than 1000, we return only 1000 items.
            

    :type NextToken: string
    :param NextToken: The token to retrieve the next page of results.

    :rtype: dict
    :return: {
        'NatGateways': [
            {
                'VpcId': 'string',
                'SubnetId': 'string',
                'NatGatewayId': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'DeleteTime': datetime(2015, 1, 1),
                'NatGatewayAddresses': [
                    {
                        'PublicIp': 'string',
                        'AllocationId': 'string',
                        'PrivateIp': 'string',
                        'NetworkInterfaceId': 'string'
                    },
                ],
                'State': 'pending'|'failed'|'available'|'deleting'|'deleted',
                'FailureCode': 'string',
                'FailureMessage': 'string',
                'ProvisionedBandwidth': {
                    'Provisioned': 'string',
                    'Requested': 'string',
                    'RequestTime': datetime(2015, 1, 1),
                    'ProvisionTime': datetime(2015, 1, 1),
                    'Status': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    pending : The NAT gateway is being created and is not ready to process traffic.
    failed : The NAT gateway could not be created. Check the failureCode and failureMessage fields for the reason.
    available : The NAT gateway is able to process traffic. This status remains until you delete the NAT gateway, and does not indicate the health of the NAT gateway.
    deleting : The NAT gateway is in the process of being terminated and may still be processing traffic.
    deleted : The NAT gateway has been terminated and is no longer processing traffic.
    
    """
    pass

def describe_network_acls(DryRun=None, NetworkAclIds=None, Filters=None):
    """
    Describes one or more of your network ACLs.
    For more information about network ACLs, see Network ACLs in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the specified network ACL.
    Expected Output:
    
    :example: response = client.describe_network_acls(
        DryRun=True|False,
        NetworkAclIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkAclIds: list
    :param NetworkAclIds: One or more network ACL IDs.
            Default: Describes all your network ACLs.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            association.association-id - The ID of an association ID for the ACL.
            association.network-acl-id - The ID of the network ACL involved in the association.
            association.subnet-id - The ID of the subnet involved in the association.
            default - Indicates whether the ACL is the default network ACL for the VPC.
            entry.cidr - The IPv4 CIDR range specified in the entry.
            entry.egress - Indicates whether the entry applies to egress traffic.
            entry.icmp.code - The ICMP code specified in the entry, if any.
            entry.icmp.type - The ICMP type specified in the entry, if any.
            entry.ipv6-cidr - The IPv6 CIDR range specified in the entry.
            entry.port-range.from - The start of the port range specified in the entry.
            entry.port-range.to - The end of the port range specified in the entry.
            entry.protocol - The protocol specified in the entry (tcp | udp | icmp or a protocol number).
            entry.rule-action - Allows or denies the matching traffic (allow | deny ).
            entry.rule-number - The number of an entry (in other words, rule) in the ACL's set of entries.
            network-acl-id - The ID of the network ACL.
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC for the network ACL.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'NetworkAcls': [
            {
                'NetworkAclId': 'string',
                'VpcId': 'string',
                'IsDefault': True|False,
                'Entries': [
                    {
                        'RuleNumber': 123,
                        'Protocol': 'string',
                        'RuleAction': 'allow'|'deny',
                        'Egress': True|False,
                        'CidrBlock': 'string',
                        'Ipv6CidrBlock': 'string',
                        'IcmpTypeCode': {
                            'Type': 123,
                            'Code': 123
                        },
                        'PortRange': {
                            'From': 123,
                            'To': 123
                        }
                    },
                ],
                'Associations': [
                    {
                        'NetworkAclAssociationId': 'string',
                        'NetworkAclId': 'string',
                        'SubnetId': 'string'
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_network_interface_attribute(DryRun=None, NetworkInterfaceId=None, Attribute=None):
    """
    Describes a network interface attribute. You can specify only one attribute at a time.
    See also: AWS API Documentation
    
    Examples
    This example describes the attachment attribute of the specified network interface.
    Expected Output:
    This example describes the description attribute of the specified network interface.
    Expected Output:
    This example describes the groupSet attribute of the specified network interface.
    Expected Output:
    This example describes the sourceDestCheck attribute of the specified network interface.
    Expected Output:
    
    :example: response = client.describe_network_interface_attribute(
        DryRun=True|False,
        NetworkInterfaceId='string',
        Attribute='description'|'groupSet'|'sourceDestCheck'|'attachment'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            

    :type Attribute: string
    :param Attribute: The attribute of the network interface. This parameter is required.

    :rtype: dict
    :return: {
        'NetworkInterfaceId': 'string',
        'Description': {
            'Value': 'string'
        },
        'SourceDestCheck': {
            'Value': True|False
        },
        'Groups': [
            {
                'GroupName': 'string',
                'GroupId': 'string'
            },
        ],
        'Attachment': {
            'AttachmentId': 'string',
            'InstanceId': 'string',
            'InstanceOwnerId': 'string',
            'DeviceIndex': 123,
            'Status': 'attaching'|'attached'|'detaching'|'detached',
            'AttachTime': datetime(2015, 1, 1),
            'DeleteOnTermination': True|False
        }
    }
    
    
    """
    pass

def describe_network_interfaces(DryRun=None, NetworkInterfaceIds=None, Filters=None):
    """
    Describes one or more of your network interfaces.
    See also: AWS API Documentation
    
    Examples
    Expected Output:
    
    :example: response = client.describe_network_interfaces(
        DryRun=True|False,
        NetworkInterfaceIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkInterfaceIds: list
    :param NetworkInterfaceIds: One or more network interface IDs.
            Default: Describes all your network interfaces.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            addresses.private-ip-address - The private IPv4 addresses associated with the network interface.
            addresses.primary - Whether the private IPv4 address is the primary IP address associated with the network interface.
            addresses.association.public-ip - The association ID returned when the network interface was associated with the Elastic IP address (IPv4).
            addresses.association.owner-id - The owner ID of the addresses associated with the network interface.
            association.association-id - The association ID returned when the network interface was associated with an IPv4 address.
            association.allocation-id - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface.
            association.ip-owner-id - The owner of the Elastic IP address (IPv4) associated with the network interface.
            association.public-ip - The address of the Elastic IP address (IPv4) bound to the network interface.
            association.public-dns-name - The public DNS name for the network interface (IPv4).
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
            ipv6-addresses.ipv6-address - An IPv6 address associated with the network interface.
            mac-address - The MAC address of the network interface.
            network-interface-id - The ID of the network interface.
            owner-id - The AWS account ID of the network interface owner.
            private-ip-address - The private IPv4 address or addresses of the network interface.
            private-dns-name - The private DNS name of the network interface (IPv4).
            requester-id - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on).
            requester-managed - Indicates whether the network interface is being managed by an AWS service (for example, AWS Management Console, Auto Scaling, and so on).
            source-desk-check - Indicates whether the network interface performs source/destination checking. A value of true means checking is enabled, and false means checking is disabled. The value must be false for the network interface to perform network address translation (NAT) in your VPC.
            status - The status of the network interface. If the network interface is not attached to an instance, the status is available ; if a network interface is attached to an instance the status is in-use .
            subnet-id - The ID of the subnet for the network interface.
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC for the network interface.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'NetworkInterfaces': [
            {
                'NetworkInterfaceId': 'string',
                'SubnetId': 'string',
                'VpcId': 'string',
                'AvailabilityZone': 'string',
                'Description': 'string',
                'OwnerId': 'string',
                'RequesterId': 'string',
                'RequesterManaged': True|False,
                'Status': 'available'|'attaching'|'in-use'|'detaching',
                'MacAddress': 'string',
                'PrivateIpAddress': 'string',
                'PrivateDnsName': 'string',
                'SourceDestCheck': True|False,
                'Groups': [
                    {
                        'GroupName': 'string',
                        'GroupId': 'string'
                    },
                ],
                'Attachment': {
                    'AttachmentId': 'string',
                    'InstanceId': 'string',
                    'InstanceOwnerId': 'string',
                    'DeviceIndex': 123,
                    'Status': 'attaching'|'attached'|'detaching'|'detached',
                    'AttachTime': datetime(2015, 1, 1),
                    'DeleteOnTermination': True|False
                },
                'Association': {
                    'PublicIp': 'string',
                    'PublicDnsName': 'string',
                    'IpOwnerId': 'string',
                    'AllocationId': 'string',
                    'AssociationId': 'string'
                },
                'TagSet': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'PrivateIpAddresses': [
                    {
                        'PrivateIpAddress': 'string',
                        'PrivateDnsName': 'string',
                        'Primary': True|False,
                        'Association': {
                            'PublicIp': 'string',
                            'PublicDnsName': 'string',
                            'IpOwnerId': 'string',
                            'AllocationId': 'string',
                            'AssociationId': 'string'
                        }
                    },
                ],
                'Ipv6Addresses': [
                    {
                        'Ipv6Address': 'string'
                    },
                ],
                'InterfaceType': 'interface'|'natGateway'
            },
        ]
    }
    
    
    """
    pass

def describe_placement_groups(DryRun=None, GroupNames=None, Filters=None):
    """
    Describes one or more of your placement groups. For more information about placement groups and cluster instances, see Cluster Instances in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_placement_groups(
        DryRun=True|False,
        GroupNames=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupNames: list
    :param GroupNames: One or more placement group names.
            Default: Describes all your placement groups, or only those otherwise specified.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            group-name - The name of the placement group.
            state - The state of the placement group (pending | available | deleting | deleted ).
            strategy - The strategy of the placement group (cluster ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'PlacementGroups': [
            {
                'GroupName': 'string',
                'Strategy': 'cluster',
                'State': 'pending'|'available'|'deleting'|'deleted'
            },
        ]
    }
    
    
    """
    pass

def describe_prefix_lists(DryRun=None, PrefixListIds=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes available AWS services in a prefix list format, which includes the prefix list name and prefix list ID of the service and the IP address range for the service. A prefix list ID is required for creating an outbound security group rule that allows traffic from a VPC to access an AWS service through a VPC endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_prefix_lists(
        DryRun=True|False,
        PrefixListIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type PrefixListIds: list
    :param PrefixListIds: One or more prefix list IDs.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            prefix-list-id : The ID of a prefix list.
            prefix-list-name : The name of a prefix list.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
            Constraint: If the value specified is greater than 1000, we return only 1000 items.
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)

    :rtype: dict
    :return: {
        'PrefixLists': [
            {
                'PrefixListId': 'string',
                'PrefixListName': 'string',
                'Cidrs': [
                    'string',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_regions(DryRun=None, RegionNames=None, Filters=None):
    """
    Describes one or more regions that are currently available to you.
    For a list of the regions supported by Amazon EC2, see Regions and Endpoints .
    See also: AWS API Documentation
    
    Examples
    This example describes all the regions that are available to you.
    Expected Output:
    
    :example: response = client.describe_regions(
        DryRun=True|False,
        RegionNames=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type RegionNames: list
    :param RegionNames: The names of one or more regions.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            endpoint - The endpoint of the region (for example, ec2.us-east-1.amazonaws.com ).
            region-name - The name of the region (for example, us-east-1 ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'Regions': [
            {
                'RegionName': 'string',
                'Endpoint': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_reserved_instances(DryRun=None, ReservedInstancesIds=None, Filters=None, OfferingType=None, OfferingClass=None):
    """
    Describes one or more of the Reserved Instances that you purchased.
    For more information about Reserved Instances, see Reserved Instances in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_reserved_instances(
        DryRun=True|False,
        ReservedInstancesIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        OfferingType='Heavy Utilization'|'Medium Utilization'|'Light Utilization'|'No Upfront'|'Partial Upfront'|'All Upfront',
        OfferingClass='standard'|'convertible'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ReservedInstancesIds: list
    :param ReservedInstancesIds: One or more Reserved Instance IDs.
            Default: Describes all your Reserved Instances, or only those otherwise specified.
            (string) --
            

    :type Filters: list
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
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            usage-price - The usage price of the Reserved Instance, per hour (for example, 0.84).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type OfferingType: string
    :param OfferingType: The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the Medium Utilization Reserved Instance offering type.

    :type OfferingClass: string
    :param OfferingClass: Describes whether the Reserved Instance is Standard or Convertible.

    :rtype: dict
    :return: {
        'ReservedInstances': [
            {
                'ReservedInstancesId': 'string',
                'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                'AvailabilityZone': 'string',
                'Start': datetime(2015, 1, 1),
                'End': datetime(2015, 1, 1),
                'Duration': 123,
                'UsagePrice': ...,
                'FixedPrice': ...,
                'InstanceCount': 123,
                'ProductDescription': 'Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)',
                'State': 'payment-pending'|'active'|'payment-failed'|'retired',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'InstanceTenancy': 'default'|'dedicated'|'host',
                'CurrencyCode': 'USD',
                'OfferingType': 'Heavy Utilization'|'Medium Utilization'|'Light Utilization'|'No Upfront'|'Partial Upfront'|'All Upfront',
                'RecurringCharges': [
                    {
                        'Frequency': 'Hourly',
                        'Amount': 123.0
                    },
                ],
                'OfferingClass': 'standard'|'convertible',
                'Scope': 'Availability Zone'|'Region'
            },
        ]
    }
    
    
    """
    pass

def describe_reserved_instances_listings(ReservedInstancesId=None, ReservedInstancesListingId=None, Filters=None):
    """
    Describes your account's Reserved Instance listings in the Reserved Instance Marketplace.
    The Reserved Instance Marketplace matches sellers who want to resell Reserved Instance capacity that they no longer need with buyers who want to purchase additional capacity. Reserved Instances bought and sold through the Reserved Instance Marketplace work like any other Reserved Instances.
    As a seller, you choose to list some or all of your Reserved Instances, and you specify the upfront price to receive for them. Your Reserved Instances are then listed in the Reserved Instance Marketplace and are available for purchase.
    As a buyer, you specify the configuration of the Reserved Instance to purchase, and the Marketplace matches what you're searching for with what's available. The Marketplace first sells the lowest priced Reserved Instances to you, and continues to sell available Reserved Instance listings to you until your demand is met. You are charged based on the total price of all of the listings that you purchase.
    For more information, see Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_reserved_instances_listings(
        ReservedInstancesId='string',
        ReservedInstancesListingId='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type ReservedInstancesId: string
    :param ReservedInstancesId: One or more Reserved Instance IDs.

    :type ReservedInstancesListingId: string
    :param ReservedInstancesListingId: One or more Reserved Instance listing IDs.

    :type Filters: list
    :param Filters: One or more filters.
            reserved-instances-id - The ID of the Reserved Instances.
            reserved-instances-listing-id - The ID of the Reserved Instances listing.
            status - The status of the Reserved Instance listing (pending | active | cancelled | closed ).
            status-message - The reason for the status.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_reserved_instances_modifications(ReservedInstancesModificationIds=None, NextToken=None, Filters=None):
    """
    Describes the modifications made to your Reserved Instances. If no parameter is specified, information about all your Reserved Instances modification requests is returned. If a modification ID is specified, only information about the specific modification is returned.
    For more information, see Modifying Reserved Instances in the Amazon Elastic Compute Cloud User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_reserved_instances_modifications(
        ReservedInstancesModificationIds=[
            'string',
        ],
        NextToken='string',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type ReservedInstancesModificationIds: list
    :param ReservedInstancesModificationIds: IDs for the submitted modification request.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token to retrieve the next page of results.

    :type Filters: list
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
            
            

    :rtype: dict
    :return: {
        'ReservedInstancesModifications': [
            {
                'ReservedInstancesModificationId': 'string',
                'ReservedInstancesIds': [
                    {
                        'ReservedInstancesId': 'string'
                    },
                ],
                'ModificationResults': [
                    {
                        'ReservedInstancesId': 'string',
                        'TargetConfiguration': {
                            'AvailabilityZone': 'string',
                            'Platform': 'string',
                            'InstanceCount': 123,
                            'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                            'Scope': 'Availability Zone'|'Region'
                        }
                    },
                ],
                'CreateDate': datetime(2015, 1, 1),
                'UpdateDate': datetime(2015, 1, 1),
                'EffectiveDate': datetime(2015, 1, 1),
                'Status': 'string',
                'StatusMessage': 'string',
                'ClientToken': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_reserved_instances_offerings(DryRun=None, ReservedInstancesOfferingIds=None, InstanceType=None, AvailabilityZone=None, ProductDescription=None, Filters=None, InstanceTenancy=None, OfferingType=None, NextToken=None, MaxResults=None, IncludeMarketplace=None, MinDuration=None, MaxDuration=None, MaxInstanceCount=None, OfferingClass=None):
    """
    Describes Reserved Instance offerings that are available for purchase. With Reserved Instances, you purchase the right to launch instances for a period of time. During that time period, you do not receive insufficient capacity errors, and you pay a lower usage rate than the rate charged for On-Demand instances for the actual time used.
    If you have listed your own Reserved Instances for sale in the Reserved Instance Marketplace, they will be excluded from these results. This is to ensure that you do not purchase your own Reserved Instances.
    For more information, see Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_reserved_instances_offerings(
        DryRun=True|False,
        ReservedInstancesOfferingIds=[
            'string',
        ],
        InstanceType='t1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
        AvailabilityZone='string',
        ProductDescription='Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)',
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        InstanceTenancy='default'|'dedicated'|'host',
        OfferingType='Heavy Utilization'|'Medium Utilization'|'Light Utilization'|'No Upfront'|'Partial Upfront'|'All Upfront',
        NextToken='string',
        MaxResults=123,
        IncludeMarketplace=True|False,
        MinDuration=123,
        MaxDuration=123,
        MaxInstanceCount=123,
        OfferingClass='standard'|'convertible'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ReservedInstancesOfferingIds: list
    :param ReservedInstancesOfferingIds: One or more Reserved Instances offering IDs.
            (string) --
            

    :type InstanceType: string
    :param InstanceType: The instance type that the reservation will cover (for example, m1.small ). For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide .

    :type AvailabilityZone: string
    :param AvailabilityZone: The Availability Zone in which the Reserved Instance can be used.

    :type ProductDescription: string
    :param ProductDescription: The Reserved Instance product platform description. Instances that include (Amazon VPC) in the description are for use with Amazon VPC.

    :type Filters: list
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
            
            

    :type InstanceTenancy: string
    :param InstanceTenancy: The tenancy of the instances covered by the reservation. A Reserved Instance with a tenancy of dedicated is applied to instances that run in a VPC on single-tenant hardware (i.e., Dedicated Instances).
            Important: The host value cannot be used with this parameter. Use the default or dedicated values only.
            Default: default
            

    :type OfferingType: string
    :param OfferingType: The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the Medium Utilization Reserved Instance offering type.

    :type NextToken: string
    :param NextToken: The token to retrieve the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. The maximum is 100.
            Default: 100
            

    :type IncludeMarketplace: boolean
    :param IncludeMarketplace: Include Reserved Instance Marketplace offerings in the response.

    :type MinDuration: integer
    :param MinDuration: The minimum duration (in seconds) to filter when searching for offerings.
            Default: 2592000 (1 month)
            

    :type MaxDuration: integer
    :param MaxDuration: The maximum duration (in seconds) to filter when searching for offerings.
            Default: 94608000 (3 years)
            

    :type MaxInstanceCount: integer
    :param MaxInstanceCount: The maximum number of instances to filter when searching for offerings.
            Default: 20
            

    :type OfferingClass: string
    :param OfferingClass: The offering class of the Reserved Instance. Can be standard or convertible .

    :rtype: dict
    :return: {
        'ReservedInstancesOfferings': [
            {
                'ReservedInstancesOfferingId': 'string',
                'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                'AvailabilityZone': 'string',
                'Duration': 123,
                'UsagePrice': ...,
                'FixedPrice': ...,
                'ProductDescription': 'Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)',
                'InstanceTenancy': 'default'|'dedicated'|'host',
                'CurrencyCode': 'USD',
                'OfferingType': 'Heavy Utilization'|'Medium Utilization'|'Light Utilization'|'No Upfront'|'Partial Upfront'|'All Upfront',
                'RecurringCharges': [
                    {
                        'Frequency': 'Hourly',
                        'Amount': 123.0
                    },
                ],
                'Marketplace': True|False,
                'PricingDetails': [
                    {
                        'Price': 123.0,
                        'Count': 123
                    },
                ],
                'OfferingClass': 'standard'|'convertible',
                'Scope': 'Availability Zone'|'Region'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_route_tables(DryRun=None, RouteTableIds=None, Filters=None):
    """
    Describes one or more of your route tables.
    Each subnet in your VPC must be associated with a route table. If a subnet is not explicitly associated with any route table, it is implicitly associated with the main route table. This command does not return the subnet ID for implicit associations.
    For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the specified route table.
    Expected Output:
    
    :example: response = client.describe_route_tables(
        DryRun=True|False,
        RouteTableIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type RouteTableIds: list
    :param RouteTableIds: One or more route table IDs.
            Default: Describes all your route tables.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            association.route-table-association-id - The ID of an association ID for the route table.
            association.route-table-id - The ID of the route table involved in the association.
            association.subnet-id - The ID of the subnet involved in the association.
            association.main - Indicates whether the route table is the main route table for the VPC (true | false ). Route tables that do not have an association ID are not returned in the response.
            route-table-id - The ID of the route table.
            route.destination-cidr-block - The IPv4 CIDR range specified in a route in the table.
            route.destination-ipv6-cidr-block - The IPv6 CIDR range specified in a route in the route table.
            route.destination-prefix-list-id - The ID (prefix) of the AWS service specified in a route in the table.
            route.egress-only-internet-gateway-id - The ID of an egress-only Internet gateway specified in a route in the route table.
            route.gateway-id - The ID of a gateway specified in a route in the table.
            route.instance-id - The ID of an instance specified in a route in the table.
            route.nat-gateway-id - The ID of a NAT gateway.
            route.origin - Describes how the route was created. CreateRouteTable indicates that the route was automatically created when the route table was created; CreateRoute indicates that the route was manually added to the route table; EnableVgwRoutePropagation indicates that the route was propagated by route propagation.
            route.state - The state of a route in the route table (active | blackhole ). The blackhole state indicates that the route's target isn't available (for example, the specified gateway isn't attached to the VPC, the specified NAT instance has been terminated, and so on).
            route.vpc-peering-connection-id - The ID of a VPC peering connection specified in a route in the table.
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC for the route table.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'RouteTables': [
            {
                'RouteTableId': 'string',
                'VpcId': 'string',
                'Routes': [
                    {
                        'DestinationCidrBlock': 'string',
                        'DestinationPrefixListId': 'string',
                        'GatewayId': 'string',
                        'InstanceId': 'string',
                        'InstanceOwnerId': 'string',
                        'NetworkInterfaceId': 'string',
                        'VpcPeeringConnectionId': 'string',
                        'NatGatewayId': 'string',
                        'State': 'active'|'blackhole',
                        'Origin': 'CreateRouteTable'|'CreateRoute'|'EnableVgwRoutePropagation',
                        'DestinationIpv6CidrBlock': 'string',
                        'EgressOnlyInternetGatewayId': 'string'
                    },
                ],
                'Associations': [
                    {
                        'RouteTableAssociationId': 'string',
                        'RouteTableId': 'string',
                        'SubnetId': 'string',
                        'Main': True|False
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'PropagatingVgws': [
                    {
                        'GatewayId': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    CreateRouteTable - The route was automatically created when the route table was created.
    CreateRoute - The route was manually added to the route table.
    EnableVgwRoutePropagation - The route was propagated by route propagation.
    
    """
    pass

def describe_scheduled_instance_availability(DryRun=None, Recurrence=None, FirstSlotStartTimeRange=None, MinSlotDurationInHours=None, MaxSlotDurationInHours=None, NextToken=None, MaxResults=None, Filters=None):
    """
    Finds available schedules that meet the specified criteria.
    You can search for an available schedule no more than 3 months in advance. You must meet the minimum required duration of 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours.
    After you find a schedule that meets your needs, call  PurchaseScheduledInstances to purchase Scheduled Instances with that schedule.
    See also: AWS API Documentation
    
    Examples
    This example describes a schedule that occurs every week on Sunday, starting on the specified date. Note that the output contains a single schedule as an example.
    Expected Output:
    
    :example: response = client.describe_scheduled_instance_availability(
        DryRun=True|False,
        Recurrence={
            'Frequency': 'string',
            'Interval': 123,
            'OccurrenceDays': [
                123,
            ],
            'OccurrenceRelativeToEnd': True|False,
            'OccurrenceUnit': 'string'
        },
        FirstSlotStartTimeRange={
            'EarliestTime': datetime(2015, 1, 1),
            'LatestTime': datetime(2015, 1, 1)
        },
        MinSlotDurationInHours=123,
        MaxSlotDurationInHours=123,
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Recurrence: dict
    :param Recurrence: [REQUIRED]
            The schedule recurrence.
            Frequency (string) --The frequency (Daily , Weekly , or Monthly ).
            Interval (integer) --The interval quantity. The interval unit depends on the value of Frequency . For example, every 2 weeks or every 2 months.
            OccurrenceDays (list) --The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday). You can't specify this value with a daily schedule. If the occurrence is relative to the end of the month, you can specify only a single day.
            (integer) --
            OccurrenceRelativeToEnd (boolean) --Indicates whether the occurrence is relative to the end of the specified week or month. You can't specify this value with a daily schedule.
            OccurrenceUnit (string) --The unit for OccurrenceDays (DayOfWeek or DayOfMonth ). This value is required for a monthly schedule. You can't specify DayOfWeek with a weekly schedule. You can't specify this value with a daily schedule.
            

    :type FirstSlotStartTimeRange: dict
    :param FirstSlotStartTimeRange: [REQUIRED]
            The time period for the first schedule to start.
            EarliestTime (datetime) -- [REQUIRED]The earliest date and time, in UTC, for the Scheduled Instance to start.
            LatestTime (datetime) -- [REQUIRED]The latest date and time, in UTC, for the Scheduled Instance to start. This value must be later than or equal to the earliest date and at most three months in the future.
            

    :type MinSlotDurationInHours: integer
    :param MinSlotDurationInHours: The minimum available duration, in hours. The minimum required duration is 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours.

    :type MaxSlotDurationInHours: integer
    :param MaxSlotDurationInHours: The maximum available duration, in hours. This value must be greater than MinSlotDurationInHours and less than 1,720.

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 300. To retrieve the remaining results, make another call with the returned NextToken value.

    :type Filters: list
    :param Filters: One or more filters.
            availability-zone - The Availability Zone (for example, us-west-2a ).
            instance-type - The instance type (for example, c4.large ).
            network-platform - The network platform (EC2-Classic or EC2-VPC ).
            platform - The platform (Linux/UNIX or Windows ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'ScheduledInstanceAvailabilitySet': [
            {
                'InstanceType': 'string',
                'Platform': 'string',
                'NetworkPlatform': 'string',
                'AvailabilityZone': 'string',
                'PurchaseToken': 'string',
                'SlotDurationInHours': 123,
                'Recurrence': {
                    'Frequency': 'string',
                    'Interval': 123,
                    'OccurrenceDaySet': [
                        123,
                    ],
                    'OccurrenceRelativeToEnd': True|False,
                    'OccurrenceUnit': 'string'
                },
                'FirstSlotStartTime': datetime(2015, 1, 1),
                'HourlyPrice': 'string',
                'TotalScheduledInstanceHours': 123,
                'AvailableInstanceCount': 123,
                'MinTermDurationInDays': 123,
                'MaxTermDurationInDays': 123
            },
        ]
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def describe_scheduled_instances(DryRun=None, ScheduledInstanceIds=None, SlotStartTimeRange=None, NextToken=None, MaxResults=None, Filters=None):
    """
    Describes one or more of your Scheduled Instances.
    See also: AWS API Documentation
    
    Examples
    This example describes the specified Scheduled Instance.
    Expected Output:
    
    :example: response = client.describe_scheduled_instances(
        DryRun=True|False,
        ScheduledInstanceIds=[
            'string',
        ],
        SlotStartTimeRange={
            'EarliestTime': datetime(2015, 1, 1),
            'LatestTime': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123,
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ScheduledInstanceIds: list
    :param ScheduledInstanceIds: One or more Scheduled Instance IDs.
            (string) --
            

    :type SlotStartTimeRange: dict
    :param SlotStartTimeRange: The time period for the first schedule to start.
            EarliestTime (datetime) --The earliest date and time, in UTC, for the Scheduled Instance to start.
            LatestTime (datetime) --The latest date and time, in UTC, for the Scheduled Instance to start.
            

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 100. To retrieve the remaining results, make another call with the returned NextToken value.

    :type Filters: list
    :param Filters: One or more filters.
            availability-zone - The Availability Zone (for example, us-west-2a ).
            instance-type - The instance type (for example, c4.large ).
            network-platform - The network platform (EC2-Classic or EC2-VPC ).
            platform - The platform (Linux/UNIX or Windows ).
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'ScheduledInstanceSet': [
            {
                'ScheduledInstanceId': 'string',
                'InstanceType': 'string',
                'Platform': 'string',
                'NetworkPlatform': 'string',
                'AvailabilityZone': 'string',
                'SlotDurationInHours': 123,
                'Recurrence': {
                    'Frequency': 'string',
                    'Interval': 123,
                    'OccurrenceDaySet': [
                        123,
                    ],
                    'OccurrenceRelativeToEnd': True|False,
                    'OccurrenceUnit': 'string'
                },
                'PreviousSlotEndTime': datetime(2015, 1, 1),
                'NextSlotStartTime': datetime(2015, 1, 1),
                'HourlyPrice': 'string',
                'TotalScheduledInstanceHours': 123,
                'InstanceCount': 123,
                'TermStartDate': datetime(2015, 1, 1),
                'TermEndDate': datetime(2015, 1, 1),
                'CreateDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def describe_security_group_references(DryRun=None, GroupId=None):
    """
    [EC2-VPC only] Describes the VPCs on the other side of a VPC peering connection that are referencing the security groups you've specified in this request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_security_group_references(
        DryRun=True|False,
        GroupId=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

    :type GroupId: list
    :param GroupId: [REQUIRED]
            One or more security group IDs in your account.
            (string) --
            

    :rtype: dict
    :return: {
        'SecurityGroupReferenceSet': [
            {
                'GroupId': 'string',
                'ReferencingVpcId': 'string',
                'VpcPeeringConnectionId': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_security_groups(DryRun=None, GroupNames=None, GroupIds=None, Filters=None):
    """
    Describes one or more of your security groups.
    A security group is for use with instances either in the EC2-Classic platform or in a specific VPC. For more information, see Amazon EC2 Security Groups in the Amazon Elastic Compute Cloud User Guide and Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_security_groups(
        DryRun=True|False,
        GroupNames=[
            'string',
        ],
        GroupIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupNames: list
    :param GroupNames: [EC2-Classic and default VPC only] One or more security group names. You can specify either the security group name or the security group ID. For security groups in a nondefault VPC, use the group-name filter to describe security groups by name.
            Default: Describes all your security groups.
            (string) --
            

    :type GroupIds: list
    :param GroupIds: One or more security group IDs. Required for security groups in a nondefault VPC.
            Default: Describes all your security groups.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters. If using multiple filters for rules, the results include security groups for which any combination of rules - not necessarily a single rule - match all filters.
            description - The description of the security group.
            egress.ip-permission.prefix-list-id - The ID (prefix) of the AWS service to which the security group allows access.
            group-id - The ID of the security group.
            group-name - The name of the security group.
            ip-permission.cidr - An IPv4 CIDR range that has been granted permission in a security group rule.
            ip-permission.from-port - The start of port range for the TCP and UDP protocols, or an ICMP type number.
            ip-permission.group-id - The ID of a security group that has been granted permission.
            ip-permission.group-name - The name of a security group that has been granted permission.
            ip-permission.ipv6-cidr - An IPv6 CIDR range that has been granted permission in a security group rule.
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
            
            

    :rtype: dict
    :return: {
        'SecurityGroups': [
            {
                'OwnerId': 'string',
                'GroupName': 'string',
                'GroupId': 'string',
                'Description': 'string',
                'IpPermissions': [
                    {
                        'IpProtocol': 'string',
                        'FromPort': 123,
                        'ToPort': 123,
                        'UserIdGroupPairs': [
                            {
                                'UserId': 'string',
                                'GroupName': 'string',
                                'GroupId': 'string',
                                'VpcId': 'string',
                                'VpcPeeringConnectionId': 'string',
                                'PeeringStatus': 'string'
                            },
                        ],
                        'IpRanges': [
                            {
                                'CidrIp': 'string'
                            },
                        ],
                        'Ipv6Ranges': [
                            {
                                'CidrIpv6': 'string'
                            },
                        ],
                        'PrefixListIds': [
                            {
                                'PrefixListId': 'string'
                            },
                        ]
                    },
                ],
                'IpPermissionsEgress': [
                    {
                        'IpProtocol': 'string',
                        'FromPort': 123,
                        'ToPort': 123,
                        'UserIdGroupPairs': [
                            {
                                'UserId': 'string',
                                'GroupName': 'string',
                                'GroupId': 'string',
                                'VpcId': 'string',
                                'VpcPeeringConnectionId': 'string',
                                'PeeringStatus': 'string'
                            },
                        ],
                        'IpRanges': [
                            {
                                'CidrIp': 'string'
                            },
                        ],
                        'Ipv6Ranges': [
                            {
                                'CidrIpv6': 'string'
                            },
                        ],
                        'PrefixListIds': [
                            {
                                'PrefixListId': 'string'
                            },
                        ]
                    },
                ],
                'VpcId': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_snapshot_attribute(DryRun=None, SnapshotId=None, Attribute=None):
    """
    Describes the specified attribute of the specified snapshot. You can specify only one attribute at a time.
    For more information about EBS snapshots, see Amazon EBS Snapshots in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the createVolumePermission attribute on a snapshot with the snapshot ID of snap-066877671789bd71b.
    Expected Output:
    
    :example: response = client.describe_snapshot_attribute(
        DryRun=True|False,
        SnapshotId='string',
        Attribute='productCodes'|'createVolumePermission'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]
            The ID of the EBS snapshot.
            

    :type Attribute: string
    :param Attribute: [REQUIRED]
            The snapshot attribute you would like to view.
            

    :rtype: dict
    :return: {
        'SnapshotId': 'string',
        'CreateVolumePermissions': [
            {
                'UserId': 'string',
                'Group': 'all'
            },
        ],
        'ProductCodes': [
            {
                'ProductCodeId': 'string',
                'ProductCodeType': 'devpay'|'marketplace'
            },
        ]
    }
    
    
    """
    pass

def describe_snapshots(DryRun=None, SnapshotIds=None, OwnerIds=None, RestorableByUserIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Describes one or more of the EBS snapshots available to you. Available snapshots include public snapshots available for any AWS account to launch, private snapshots that you own, and private snapshots owned by another AWS account but for which you've been given explicit create volume permissions.
    The create volume permissions fall into the following categories:
    The list of snapshots returned can be modified by specifying snapshot IDs, snapshot owners, or AWS accounts with create volume permissions. If no options are specified, Amazon EC2 returns all snapshots for which you have create volume permissions.
    If you specify one or more snapshot IDs, only snapshots that have the specified IDs are returned. If you specify an invalid snapshot ID, an error is returned. If you specify a snapshot ID for which you do not have access, it is not included in the returned results.
    If you specify one or more snapshot owners using the OwnerIds option, only snapshots from the specified owners and for which you have access are returned. The results can include the AWS account IDs of the specified owners, amazon for snapshots owned by Amazon, or self for snapshots that you own.
    If you specify a list of restorable users, only snapshots with create snapshot permissions for those users are returned. You can specify AWS account IDs (if you own the snapshots), self for snapshots for which you own or have explicit permissions, or all for public snapshots.
    If you are describing a long list of snapshots, you can paginate the output to make the list more manageable. The MaxResults parameter sets the maximum number of results returned in a single page. If the list of results exceeds your MaxResults value, then that number of results is returned along with a NextToken value that can be passed to a subsequent DescribeSnapshots request to retrieve the remaining results.
    For more information about EBS snapshots, see Amazon EBS Snapshots in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes a snapshot with the snapshot ID of snap-1234567890abcdef0.
    Expected Output:
    This example describes all snapshots owned by the ID 012345678910 that are in the pending status.
    Expected Output:
    
    :example: response = client.describe_snapshots(
        DryRun=True|False,
        SnapshotIds=[
            'string',
        ],
        OwnerIds=[
            'string',
        ],
        RestorableByUserIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SnapshotIds: list
    :param SnapshotIds: One or more snapshot IDs.
            Default: Describes snapshots for which you have launch permissions.
            (string) --
            

    :type OwnerIds: list
    :param OwnerIds: Returns the snapshots owned by the specified owner. Multiple owners can be specified.
            (string) --
            

    :type RestorableByUserIds: list
    :param RestorableByUserIds: One or more AWS accounts IDs that can create volumes from the snapshot.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            description - A description of the snapshot.
            owner-alias - Value from an Amazon-maintained list (amazon | aws-marketplace | microsoft ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM consolew.
            owner-id - The ID of the AWS account that owns the snapshot.
            progress - The progress of the snapshot, as a percentage (for example, 80%).
            snapshot-id - The snapshot ID.
            start-time - The time stamp when the snapshot was initiated.
            status - The status of the snapshot (pending | completed | error ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            volume-id - The ID of the volume the snapshot is for.
            volume-size - The size of the volume, in GiB.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type NextToken: string
    :param NextToken: The NextToken value returned from a previous paginated DescribeSnapshots request where MaxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of snapshot results returned by DescribeSnapshots in paginated output. When this parameter is used, DescribeSnapshots only returns MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another DescribeSnapshots request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then DescribeSnapshots returns all results. You cannot specify this parameter and the snapshot IDs parameter in the same request.

    :rtype: dict
    :return: {
        'Snapshots': [
            {
                'SnapshotId': 'string',
                'VolumeId': 'string',
                'State': 'pending'|'completed'|'error',
                'StateMessage': 'string',
                'StartTime': datetime(2015, 1, 1),
                'Progress': 'string',
                'OwnerId': 'string',
                'Description': 'string',
                'VolumeSize': 123,
                'OwnerAlias': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Encrypted': True|False,
                'KmsKeyId': 'string',
                'DataEncryptionKeyId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DryRun (boolean) -- Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    SnapshotIds (list) -- One or more snapshot IDs.
    Default: Describes snapshots for which you have launch permissions.
    
    (string) --
    
    
    OwnerIds (list) -- Returns the snapshots owned by the specified owner. Multiple owners can be specified.
    
    (string) --
    
    
    RestorableByUserIds (list) -- One or more AWS accounts IDs that can create volumes from the snapshot.
    
    (string) --
    
    
    Filters (list) -- One or more filters.
    
    description - A description of the snapshot.
    owner-alias - Value from an Amazon-maintained list (amazon | aws-marketplace | microsoft ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM consolew.
    owner-id - The ID of the AWS account that owns the snapshot.
    progress - The progress of the snapshot, as a percentage (for example, 80%).
    snapshot-id - The snapshot ID.
    start-time - The time stamp when the snapshot was initiated.
    status - The status of the snapshot (pending | completed | error ).
    tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
    tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter "tag-key=Purpose" and the filter "tag-value=X", you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
    tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
    volume-id - The ID of the volume the snapshot is for.
    volume-size - The size of the volume, in GiB.
    
    
    (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
    
    Name (string) --The name of the filter. Filter names are case-sensitive.
    
    Values (list) --One or more filter values. Filter values are case-sensitive.
    
    (string) --
    
    
    
    
    
    
    NextToken (string) -- The NextToken value returned from a previous paginated DescribeSnapshots request where MaxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.
    MaxResults (integer) -- The maximum number of snapshot results returned by DescribeSnapshots in paginated output. When this parameter is used, DescribeSnapshots only returns MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another DescribeSnapshots request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then DescribeSnapshots returns all results. You cannot specify this parameter and the snapshot IDs parameter in the same request.
    
    """
    pass

def describe_spot_datafeed_subscription(DryRun=None):
    """
    Describes the data feed for Spot instances. For more information, see Spot Instance Data Feed in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the Spot Instance datafeed subscription for your AWS account.
    Expected Output:
    
    :example: response = client.describe_spot_datafeed_subscription(
        DryRun=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_spot_fleet_instances(DryRun=None, SpotFleetRequestId=None, NextToken=None, MaxResults=None):
    """
    Describes the running instances for the specified Spot fleet.
    See also: AWS API Documentation
    
    Examples
    This example lists the Spot Instances associated with the specified Spot fleet.
    Expected Output:
    
    :example: response = client.describe_spot_fleet_instances(
        DryRun=True|False,
        SpotFleetRequestId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SpotFleetRequestId: string
    :param SpotFleetRequestId: [REQUIRED]
            The ID of the Spot fleet request.
            

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.

    :rtype: dict
    :return: {
        'SpotFleetRequestId': 'string',
        'ActiveInstances': [
            {
                'InstanceType': 'string',
                'InstanceId': 'string',
                'SpotInstanceRequestId': 'string',
                'InstanceHealth': 'healthy'|'unhealthy'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_spot_fleet_request_history(DryRun=None, SpotFleetRequestId=None, EventType=None, StartTime=None, NextToken=None, MaxResults=None):
    """
    Describes the events for the specified Spot fleet request during the specified time.
    Spot fleet events are delayed by up to 30 seconds before they can be described. This ensures that you can query by the last evaluated time and not miss a recorded event.
    See also: AWS API Documentation
    
    Examples
    This example returns the history for the specified Spot fleet starting at the specified time.
    Expected Output:
    
    :example: response = client.describe_spot_fleet_request_history(
        DryRun=True|False,
        SpotFleetRequestId='string',
        EventType='instanceChange'|'fleetRequestChange'|'error',
        StartTime=datetime(2015, 1, 1),
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SpotFleetRequestId: string
    :param SpotFleetRequestId: [REQUIRED]
            The ID of the Spot fleet request.
            

    :type EventType: string
    :param EventType: The type of events to describe. By default, all events are described.

    :type StartTime: datetime
    :param StartTime: [REQUIRED]
            The starting date and time for the events, in UTC format (for example, YYYY -MM -DD T*HH* :MM :SS Z).
            

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.

    :rtype: dict
    :return: {
        'SpotFleetRequestId': 'string',
        'StartTime': datetime(2015, 1, 1),
        'LastEvaluatedTime': datetime(2015, 1, 1),
        'HistoryRecords': [
            {
                'Timestamp': datetime(2015, 1, 1),
                'EventType': 'instanceChange'|'fleetRequestChange'|'error',
                'EventInformation': {
                    'InstanceId': 'string',
                    'EventSubType': 'string',
                    'EventDescription': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    error - Indicates an error with the Spot fleet request.
    fleetRequestChange - Indicates a change in the status or configuration of the Spot fleet request.
    instanceChange - Indicates that an instance was launched or terminated.
    
    """
    pass

def describe_spot_fleet_requests(DryRun=None, SpotFleetRequestIds=None, NextToken=None, MaxResults=None):
    """
    Describes your Spot fleet requests.
    Spot fleet requests are deleted 48 hours after they are canceled and their instances are terminated.
    See also: AWS API Documentation
    
    Examples
    This example describes the specified Spot fleet request.
    Expected Output:
    
    :example: response = client.describe_spot_fleet_requests(
        DryRun=True|False,
        SpotFleetRequestIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SpotFleetRequestIds: list
    :param SpotFleetRequestIds: The IDs of the Spot fleet requests.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.

    :rtype: dict
    :return: {
        'SpotFleetRequestConfigs': [
            {
                'SpotFleetRequestId': 'string',
                'SpotFleetRequestState': 'submitted'|'active'|'cancelled'|'failed'|'cancelled_running'|'cancelled_terminating'|'modifying',
                'SpotFleetRequestConfig': {
                    'ClientToken': 'string',
                    'SpotPrice': 'string',
                    'TargetCapacity': 123,
                    'ValidFrom': datetime(2015, 1, 1),
                    'ValidUntil': datetime(2015, 1, 1),
                    'TerminateInstancesWithExpiration': True|False,
                    'IamFleetRole': 'string',
                    'LaunchSpecifications': [
                        {
                            'ImageId': 'string',
                            'KeyName': 'string',
                            'SecurityGroups': [
                                {
                                    'GroupName': 'string',
                                    'GroupId': 'string'
                                },
                            ],
                            'UserData': 'string',
                            'AddressingType': 'string',
                            'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                            'Placement': {
                                'AvailabilityZone': 'string',
                                'GroupName': 'string',
                                'Tenancy': 'default'|'dedicated'|'host'
                            },
                            'KernelId': 'string',
                            'RamdiskId': 'string',
                            'BlockDeviceMappings': [
                                {
                                    'VirtualName': 'string',
                                    'DeviceName': 'string',
                                    'Ebs': {
                                        'SnapshotId': 'string',
                                        'VolumeSize': 123,
                                        'DeleteOnTermination': True|False,
                                        'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                                        'Iops': 123,
                                        'Encrypted': True|False
                                    },
                                    'NoDevice': 'string'
                                },
                            ],
                            'Monitoring': {
                                'Enabled': True|False
                            },
                            'SubnetId': 'string',
                            'NetworkInterfaces': [
                                {
                                    'NetworkInterfaceId': 'string',
                                    'DeviceIndex': 123,
                                    'SubnetId': 'string',
                                    'Description': 'string',
                                    'PrivateIpAddress': 'string',
                                    'Groups': [
                                        'string',
                                    ],
                                    'DeleteOnTermination': True|False,
                                    'PrivateIpAddresses': [
                                        {
                                            'PrivateIpAddress': 'string',
                                            'Primary': True|False
                                        },
                                    ],
                                    'SecondaryPrivateIpAddressCount': 123,
                                    'AssociatePublicIpAddress': True|False,
                                    'Ipv6Addresses': [
                                        {
                                            'Ipv6Address': 'string'
                                        },
                                    ],
                                    'Ipv6AddressCount': 123
                                },
                            ],
                            'IamInstanceProfile': {
                                'Arn': 'string',
                                'Name': 'string'
                            },
                            'EbsOptimized': True|False,
                            'WeightedCapacity': 123.0,
                            'SpotPrice': 'string'
                        },
                    ],
                    'ExcessCapacityTerminationPolicy': 'noTermination'|'default',
                    'AllocationStrategy': 'lowestPrice'|'diversified',
                    'FulfilledCapacity': 123.0,
                    'Type': 'request'|'maintain',
                    'ReplaceUnhealthyInstances': True|False
                },
                'CreateTime': datetime(2015, 1, 1),
                'ActivityStatus': 'error'|'pending_fulfillment'|'pending_termination'|'fulfilled'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_spot_instance_requests(DryRun=None, SpotInstanceRequestIds=None, Filters=None):
    """
    Describes the Spot instance requests that belong to your account. Spot instances are instances that Amazon EC2 launches when the bid price that you specify exceeds the current Spot price. Amazon EC2 periodically sets the Spot price based on available Spot instance capacity and current Spot instance requests. For more information, see Spot Instance Requests in the Amazon Elastic Compute Cloud User Guide .
    You can use DescribeSpotInstanceRequests to find a running Spot instance by examining the response. If the status of the Spot instance is fulfilled , the instance ID appears in the response and contains the identifier of the instance. Alternatively, you can use  DescribeInstances with a filter to look for instances where the instance lifecycle is spot .
    Spot instance requests are deleted 4 hours after they are canceled and their instances are terminated.
    See also: AWS API Documentation
    
    Examples
    This example describes the specified Spot Instance request.
    Expected Output:
    
    :example: response = client.describe_spot_instance_requests(
        DryRun=True|False,
        SpotInstanceRequestIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SpotInstanceRequestIds: list
    :param SpotInstanceRequestIds: One or more Spot instance request IDs.
            (string) --
            

    :type Filters: list
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
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
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
            
            

    :rtype: dict
    :return: {
        'SpotInstanceRequests': [
            {
                'SpotInstanceRequestId': 'string',
                'SpotPrice': 'string',
                'Type': 'one-time'|'persistent',
                'State': 'open'|'active'|'closed'|'cancelled'|'failed',
                'Fault': {
                    'Code': 'string',
                    'Message': 'string'
                },
                'Status': {
                    'Code': 'string',
                    'UpdateTime': datetime(2015, 1, 1),
                    'Message': 'string'
                },
                'ValidFrom': datetime(2015, 1, 1),
                'ValidUntil': datetime(2015, 1, 1),
                'LaunchGroup': 'string',
                'AvailabilityZoneGroup': 'string',
                'LaunchSpecification': {
                    'ImageId': 'string',
                    'KeyName': 'string',
                    'SecurityGroups': [
                        {
                            'GroupName': 'string',
                            'GroupId': 'string'
                        },
                    ],
                    'UserData': 'string',
                    'AddressingType': 'string',
                    'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'GroupName': 'string',
                        'Tenancy': 'default'|'dedicated'|'host'
                    },
                    'KernelId': 'string',
                    'RamdiskId': 'string',
                    'BlockDeviceMappings': [
                        {
                            'VirtualName': 'string',
                            'DeviceName': 'string',
                            'Ebs': {
                                'SnapshotId': 'string',
                                'VolumeSize': 123,
                                'DeleteOnTermination': True|False,
                                'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                                'Iops': 123,
                                'Encrypted': True|False
                            },
                            'NoDevice': 'string'
                        },
                    ],
                    'SubnetId': 'string',
                    'NetworkInterfaces': [
                        {
                            'NetworkInterfaceId': 'string',
                            'DeviceIndex': 123,
                            'SubnetId': 'string',
                            'Description': 'string',
                            'PrivateIpAddress': 'string',
                            'Groups': [
                                'string',
                            ],
                            'DeleteOnTermination': True|False,
                            'PrivateIpAddresses': [
                                {
                                    'PrivateIpAddress': 'string',
                                    'Primary': True|False
                                },
                            ],
                            'SecondaryPrivateIpAddressCount': 123,
                            'AssociatePublicIpAddress': True|False,
                            'Ipv6Addresses': [
                                {
                                    'Ipv6Address': 'string'
                                },
                            ],
                            'Ipv6AddressCount': 123
                        },
                    ],
                    'IamInstanceProfile': {
                        'Arn': 'string',
                        'Name': 'string'
                    },
                    'EbsOptimized': True|False,
                    'Monitoring': {
                        'Enabled': True|False
                    }
                },
                'InstanceId': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'ProductDescription': 'Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)',
                'BlockDurationMinutes': 123,
                'ActualBlockHourlyPrice': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'LaunchedAvailabilityZone': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_spot_price_history(DryRun=None, StartTime=None, EndTime=None, InstanceTypes=None, ProductDescriptions=None, Filters=None, AvailabilityZone=None, MaxResults=None, NextToken=None):
    """
    Describes the Spot price history. For more information, see Spot Instance Pricing History in the Amazon Elastic Compute Cloud User Guide .
    When you specify a start and end time, this operation returns the prices of the instance types within the time range that you specified and the time when the price changed. The price is valid within the time period that you specified; the response merely indicates the last time that the price changed.
    See also: AWS API Documentation
    
    Examples
    This example returns the Spot Price history for m1.xlarge, Linux/UNIX (Amazon VPC) instances for a particular day in January.
    Expected Output:
    
    :example: response = client.describe_spot_price_history(
        DryRun=True|False,
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        InstanceTypes=[
            't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
        ],
        ProductDescriptions=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        AvailabilityZone='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type StartTime: datetime
    :param StartTime: The date and time, up to the past 90 days, from which to start retrieving the price history data, in UTC format (for example, YYYY -MM -DD T*HH* :MM :SS Z).

    :type EndTime: datetime
    :param EndTime: The date and time, up to the current date, from which to stop retrieving the price history data, in UTC format (for example, YYYY -MM -DD T*HH* :MM :SS Z).

    :type InstanceTypes: list
    :param InstanceTypes: Filters the results by the specified instance types. Note that T2 and HS1 instance types are not supported.
            (string) --
            

    :type ProductDescriptions: list
    :param ProductDescriptions: Filters the results by the specified basic product descriptions.
            (string) --
            

    :type Filters: list
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
            
            

    :type AvailabilityZone: string
    :param AvailabilityZone: Filters the results by the specified Availability Zone.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict
    :return: {
        'SpotPriceHistory': [
            {
                'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                'ProductDescription': 'Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)',
                'SpotPrice': 'string',
                'Timestamp': datetime(2015, 1, 1),
                'AvailabilityZone': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_stale_security_groups(DryRun=None, VpcId=None, MaxResults=None, NextToken=None):
    """
    [EC2-VPC only] Describes the stale security group rules for security groups in a specified VPC. Rules are stale when they reference a deleted security group in a peer VPC, or a security group in a peer VPC for which the VPC peering connection has been deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stale_security_groups(
        DryRun=True|False,
        VpcId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)

    :rtype: dict
    :return: {
        'StaleSecurityGroupSet': [
            {
                'GroupId': 'string',
                'GroupName': 'string',
                'Description': 'string',
                'VpcId': 'string',
                'StaleIpPermissions': [
                    {
                        'FromPort': 123,
                        'IpProtocol': 'string',
                        'IpRanges': [
                            'string',
                        ],
                        'PrefixListIds': [
                            'string',
                        ],
                        'ToPort': 123,
                        'UserIdGroupPairs': [
                            {
                                'UserId': 'string',
                                'GroupName': 'string',
                                'GroupId': 'string',
                                'VpcId': 'string',
                                'VpcPeeringConnectionId': 'string',
                                'PeeringStatus': 'string'
                            },
                        ]
                    },
                ],
                'StaleIpPermissionsEgress': [
                    {
                        'FromPort': 123,
                        'IpProtocol': 'string',
                        'IpRanges': [
                            'string',
                        ],
                        'PrefixListIds': [
                            'string',
                        ],
                        'ToPort': 123,
                        'UserIdGroupPairs': [
                            {
                                'UserId': 'string',
                                'GroupName': 'string',
                                'GroupId': 'string',
                                'VpcId': 'string',
                                'VpcPeeringConnectionId': 'string',
                                'PeeringStatus': 'string'
                            },
                        ]
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

def describe_subnets(DryRun=None, SubnetIds=None, Filters=None):
    """
    Describes one or more of your subnets.
    For more information about subnets, see Your VPC and Subnets in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the subnets for the specified VPC.
    Expected Output:
    
    :example: response = client.describe_subnets(
        DryRun=True|False,
        SubnetIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SubnetIds: list
    :param SubnetIds: One or more subnet IDs.
            Default: Describes all your subnets.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            availabilityZone - The Availability Zone for the subnet. You can also use availability-zone as the filter name.
            available-ip-address-count - The number of IPv4 addresses in the subnet that are available.
            cidrBlock - The IPv4 CIDR block of the subnet. The CIDR block you specify must exactly match the subnet's CIDR block for information to be returned for the subnet. You can also use cidr or cidr-block as the filter names.
            defaultForAz - Indicates whether this is the default subnet for the Availability Zone. You can also use default-for-az as the filter name.
            ipv6-cidr-block-association.ipv6-cidr-block - An IPv6 CIDR block associated with the subnet.
            ipv6-cidr-block-association.association-id - An association ID for an IPv6 CIDR block associated with the subnet.
            ipv6-cidr-block-association.state - The state of an IPv6 CIDR block associated with the subnet.
            state - The state of the subnet (pending | available ).
            subnet-id - The ID of the subnet.
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC for the subnet.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'Subnets': [
            {
                'SubnetId': 'string',
                'State': 'pending'|'available',
                'VpcId': 'string',
                'CidrBlock': 'string',
                'Ipv6CidrBlockAssociationSet': [
                    {
                        'Ipv6CidrBlock': 'string',
                        'Ipv6CidrBlockState': {
                            'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                            'StatusMessage': 'string'
                        },
                        'AssociationId': 'string'
                    },
                ],
                'AssignIpv6AddressOnCreation': True|False,
                'AvailableIpAddressCount': 123,
                'AvailabilityZone': 'string',
                'DefaultForAz': True|False,
                'MapPublicIpOnLaunch': True|False,
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_tags(DryRun=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes one or more of the tags for your EC2 resources.
    For more information about tags, see Tagging Your Resources in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the tags for the specified instance.
    Expected Output:
    
    :example: response = client.describe_tags(
        DryRun=True|False,
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Filters: list
    :param Filters: One or more filters.
            key - The tag key.
            resource-id - The resource ID.
            resource-type - The resource type (customer-gateway | dhcp-options | image | instance | internet-gateway | network-acl | network-interface | reserved-instances | route-table | security-group | snapshot | spot-instances-request | subnet | volume | vpc | vpn-connection | vpn-gateway ).
            value - The tag value.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. This value can be between 5 and 1000. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: The token to retrieve the next page of results.

    :rtype: dict
    :return: {
        'Tags': [
            {
                'ResourceId': 'string',
                'ResourceType': 'customer-gateway'|'dhcp-options'|'image'|'instance'|'internet-gateway'|'network-acl'|'network-interface'|'reserved-instances'|'route-table'|'snapshot'|'spot-instances-request'|'subnet'|'security-group'|'volume'|'vpc'|'vpn-connection'|'vpn-gateway',
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_volume_attribute(DryRun=None, VolumeId=None, Attribute=None):
    """
    Describes the specified attribute of the specified volume. You can specify only one attribute at a time.
    For more information about EBS volumes, see Amazon EBS Volumes in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the autoEnableIo attribute of the volume with the ID vol-049df61146c4d7901.
    Expected Output:
    
    :example: response = client.describe_volume_attribute(
        DryRun=True|False,
        VolumeId='string',
        Attribute='autoEnableIO'|'productCodes'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeId: string
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            

    :type Attribute: string
    :param Attribute: The attribute of the volume. This parameter is required.

    :rtype: dict
    :return: {
        'VolumeId': 'string',
        'AutoEnableIO': {
            'Value': True|False
        },
        'ProductCodes': [
            {
                'ProductCodeId': 'string',
                'ProductCodeType': 'devpay'|'marketplace'
            },
        ]
    }
    
    
    """
    pass

def describe_volume_status(DryRun=None, VolumeIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Describes the status of the specified volumes. Volume status provides the result of the checks performed on your volumes to determine events that can impair the performance of your volumes. The performance of a volume can be affected if an issue occurs on the volume's underlying host. If the volume's underlying host experiences a power outage or system issue, after the system is restored, there could be data inconsistencies on the volume. Volume events notify you if this occurs. Volume actions notify you if any action needs to be taken in response to the event.
    The DescribeVolumeStatus operation provides the following information about the specified volumes:
    See also: AWS API Documentation
    
    Examples
    This example describes the status for the volume vol-1234567890abcdef0.
    Expected Output:
    This example describes the status for all volumes that are impaired. In this example output, there are no impaired volumes.
    Expected Output:
    
    :example: response = client.describe_volume_status(
        DryRun=True|False,
        VolumeIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeIds: list
    :param VolumeIds: One or more volume IDs.
            Default: Describes all your volumes.
            (string) --
            

    :type Filters: list
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
            
            

    :type NextToken: string
    :param NextToken: The NextToken value to include in a future DescribeVolumeStatus request. When the results of the request exceed MaxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of volume results returned by DescribeVolumeStatus in paginated output. When this parameter is used, the request only returns MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then DescribeVolumeStatus returns all results. You cannot specify this parameter and the volume IDs parameter in the same request.

    :rtype: dict
    :return: {
        'VolumeStatuses': [
            {
                'VolumeId': 'string',
                'AvailabilityZone': 'string',
                'VolumeStatus': {
                    'Status': 'ok'|'impaired'|'insufficient-data',
                    'Details': [
                        {
                            'Name': 'io-enabled'|'io-performance',
                            'Status': 'string'
                        },
                    ]
                },
                'Events': [
                    {
                        'EventType': 'string',
                        'Description': 'string',
                        'NotBefore': datetime(2015, 1, 1),
                        'NotAfter': datetime(2015, 1, 1),
                        'EventId': 'string'
                    },
                ],
                'Actions': [
                    {
                        'Code': 'string',
                        'Description': 'string',
                        'EventType': 'string',
                        'EventId': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_volumes(DryRun=None, VolumeIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Describes the specified EBS volumes.
    If you are describing a long list of volumes, you can paginate the output to make the list more manageable. The MaxResults parameter sets the maximum number of results returned in a single page. If the list of results exceeds your MaxResults value, then that number of results is returned along with a NextToken value that can be passed to a subsequent DescribeVolumes request to retrieve the remaining results.
    For more information about EBS volumes, see Amazon EBS Volumes in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes all of your volumes in the default region.
    Expected Output:
    This example describes all volumes that are both attached to the instance with the ID i-1234567890abcdef0 and set to delete when the instance terminates.
    Expected Output:
    
    :example: response = client.describe_volumes(
        DryRun=True|False,
        VolumeIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeIds: list
    :param VolumeIds: One or more volume IDs.
            (string) --
            

    :type Filters: list
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
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            volume-id - The volume ID.
            volume-type - The Amazon EBS volume type. This can be gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic volumes.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type NextToken: string
    :param NextToken: The NextToken value returned from a previous paginated DescribeVolumes request where MaxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of volume results returned by DescribeVolumes in paginated output. When this parameter is used, DescribeVolumes only returns MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another DescribeVolumes request with the returned NextToken value. This value can be between 5 and 500; if MaxResults is given a value larger than 500, only 500 results are returned. If this parameter is not used, then DescribeVolumes returns all results. You cannot specify this parameter and the volume IDs parameter in the same request.

    :rtype: dict
    :return: {
        'Volumes': [
            {
                'VolumeId': 'string',
                'Size': 123,
                'SnapshotId': 'string',
                'AvailabilityZone': 'string',
                'State': 'creating'|'available'|'in-use'|'deleting'|'deleted'|'error',
                'CreateTime': datetime(2015, 1, 1),
                'Attachments': [
                    {
                        'VolumeId': 'string',
                        'InstanceId': 'string',
                        'Device': 'string',
                        'State': 'attaching'|'attached'|'detaching'|'detached',
                        'AttachTime': datetime(2015, 1, 1),
                        'DeleteOnTermination': True|False
                    },
                ],
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                'Iops': 123,
                'Encrypted': True|False,
                'KmsKeyId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_volumes_modifications(DryRun=None, VolumeIds=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Reports the current modification status of EBS volumes.
    Current-generation EBS volumes support modification of attributes including type, size, and (for io1 volumes) IOPS provisioning while either attached to or detached from an instance. Following an action from the API or the console to modify a volume, the status of the modification may be modifying , optimizing , completed , or failed . If a volume has never been modified, then certain elements of the returned VolumeModification objects are null.
    You can also use CloudWatch Events to check the status of a modification to an EBS volume. For information about CloudWatch Events, see the Amazon CloudWatch Events User Guide . For more information, see Monitoring Volume Modifications" .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_volumes_modifications(
        DryRun=True|False,
        VolumeIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeIds: list
    :param VolumeIds: One or more volume IDs for which in-progress modifications will be described.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters. Supported filters: volume-id , modification-state , target-size , target-iops , target-volume-type , original-size , original-iops , original-volume-type , start-time .
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type NextToken: string
    :param NextToken: The nextToken value returned by a previous paginated request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results (up to a limit of 500) to be returned in a paginated request.

    :rtype: dict
    :return: {
        'VolumesModifications': [
            {
                'VolumeId': 'string',
                'ModificationState': 'modifying'|'optimizing'|'completed'|'failed',
                'StatusMessage': 'string',
                'TargetSize': 123,
                'TargetIops': 123,
                'TargetVolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                'OriginalSize': 123,
                'OriginalIops': 123,
                'OriginalVolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                'Progress': 123,
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_vpc_attribute(DryRun=None, VpcId=None, Attribute=None):
    """
    Describes the specified attribute of the specified VPC. You can specify only one attribute at a time.
    See also: AWS API Documentation
    
    Examples
    This example describes the enableDnsSupport attribute. This attribute indicates whether DNS resolution is enabled for the VPC. If this attribute is true, the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not.
    Expected Output:
    This example describes the enableDnsHostnames attribute. This attribute indicates whether the instances launched in the VPC get DNS hostnames. If this attribute is true, instances in the VPC get DNS hostnames; otherwise, they do not.
    Expected Output:
    
    :example: response = client.describe_vpc_attribute(
        DryRun=True|False,
        VpcId='string',
        Attribute='enableDnsSupport'|'enableDnsHostnames'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :type Attribute: string
    :param Attribute: [REQUIRED]
            The VPC attribute.
            

    :rtype: dict
    :return: {
        'VpcId': 'string',
        'EnableDnsSupport': {
            'Value': True|False
        },
        'EnableDnsHostnames': {
            'Value': True|False
        }
    }
    
    
    """
    pass

def describe_vpc_classic_link(DryRun=None, VpcIds=None, Filters=None):
    """
    Describes the ClassicLink status of one or more VPCs.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_vpc_classic_link(
        DryRun=True|False,
        VpcIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcIds: list
    :param VpcIds: One or more VPCs for which you want to describe the ClassicLink status.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            is-classic-link-enabled - Whether the VPC is enabled for ClassicLink (true | false ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'Vpcs': [
            {
                'VpcId': 'string',
                'ClassicLinkEnabled': True|False,
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_vpc_classic_link_dns_support(VpcIds=None, MaxResults=None, NextToken=None):
    """
    Describes the ClassicLink DNS support status of one or more VPCs. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_vpc_classic_link_dns_support(
        VpcIds=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type VpcIds: list
    :param VpcIds: One or more VPC IDs.
            (string) --
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)

    :rtype: dict
    :return: {
        'Vpcs': [
            {
                'VpcId': 'string',
                'ClassicLinkDnsSupported': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_vpc_endpoint_services(DryRun=None, MaxResults=None, NextToken=None):
    """
    Describes all supported AWS services that can be specified when creating a VPC endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_vpc_endpoint_services(
        DryRun=True|False,
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
            Constraint: If the value is greater than 1000, we return only 1000 items.
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)

    :rtype: dict
    :return: {
        'ServiceNames': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_vpc_endpoints(DryRun=None, VpcEndpointIds=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes one or more of your VPC endpoints.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_vpc_endpoints(
        DryRun=True|False,
        VpcEndpointIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcEndpointIds: list
    :param VpcEndpointIds: One or more endpoint IDs.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            service-name : The name of the AWS service.
            vpc-id : The ID of the VPC in which the endpoint resides.
            vpc-endpoint-id : The ID of the endpoint.
            vpc-endpoint-state : The state of the endpoint. (pending | available | deleting | deleted )
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
            Constraint: If the value is greater than 1000, we return only 1000 items.
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a prior call.)

    :rtype: dict
    :return: {
        'VpcEndpoints': [
            {
                'VpcEndpointId': 'string',
                'VpcId': 'string',
                'ServiceName': 'string',
                'State': 'Pending'|'Available'|'Deleting'|'Deleted',
                'PolicyDocument': 'string',
                'RouteTableIds': [
                    'string',
                ],
                'CreationTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_vpc_peering_connections(DryRun=None, VpcPeeringConnectionIds=None, Filters=None):
    """
    Describes one or more of your VPC peering connections.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_vpc_peering_connections(
        DryRun=True|False,
        VpcPeeringConnectionIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcPeeringConnectionIds: list
    :param VpcPeeringConnectionIds: One or more VPC peering connection IDs.
            Default: Describes all your VPC peering connections.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            accepter-vpc-info.cidr-block - The IPv4 CIDR block of the peer VPC.
            accepter-vpc-info.owner-id - The AWS account ID of the owner of the peer VPC.
            accepter-vpc-info.vpc-id - The ID of the peer VPC.
            expiration-time - The expiration date and time for the VPC peering connection.
            requester-vpc-info.cidr-block - The IPv4 CIDR block of the requester's VPC.
            requester-vpc-info.owner-id - The AWS account ID of the owner of the requester VPC.
            requester-vpc-info.vpc-id - The ID of the requester VPC.
            status-code - The status of the VPC peering connection (pending-acceptance | failed | expired | provisioning | active | deleted | rejected ).
            status-message - A message that provides more information about the status of the VPC peering connection, if applicable.
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-peering-connection-id - The ID of the VPC peering connection.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'VpcPeeringConnections': [
            {
                'AccepterVpcInfo': {
                    'CidrBlock': 'string',
                    'OwnerId': 'string',
                    'VpcId': 'string',
                    'Ipv6CidrBlockSet': [
                        {
                            'Ipv6CidrBlock': 'string'
                        },
                    ],
                    'PeeringOptions': {
                        'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
                        'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
                        'AllowDnsResolutionFromRemoteVpc': True|False
                    }
                },
                'ExpirationTime': datetime(2015, 1, 1),
                'RequesterVpcInfo': {
                    'CidrBlock': 'string',
                    'OwnerId': 'string',
                    'VpcId': 'string',
                    'Ipv6CidrBlockSet': [
                        {
                            'Ipv6CidrBlock': 'string'
                        },
                    ],
                    'PeeringOptions': {
                        'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
                        'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
                        'AllowDnsResolutionFromRemoteVpc': True|False
                    }
                },
                'Status': {
                    'Code': 'initiating-request'|'pending-acceptance'|'active'|'deleted'|'rejected'|'failed'|'expired'|'provisioning'|'deleting',
                    'Message': 'string'
                },
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'VpcPeeringConnectionId': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_vpcs(DryRun=None, VpcIds=None, Filters=None):
    """
    Describes one or more of your VPCs.
    See also: AWS API Documentation
    
    Examples
    This example describes the specified VPC.
    Expected Output:
    
    :example: response = client.describe_vpcs(
        DryRun=True|False,
        VpcIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcIds: list
    :param VpcIds: One or more VPC IDs.
            Default: Describes all your VPCs.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            cidr - The IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPC's CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, /28 ).
            dhcp-options-id - The ID of a set of DHCP options.
            ipv6-cidr-block-association.ipv6-cidr-block - An IPv6 CIDR block associated with the VPC.
            ipv6-cidr-block-association.association-id - The association ID for an IPv6 CIDR block associated with the VPC.
            ipv6-cidr-block-association.state - The state of an IPv6 CIDR block associated with the VPC.
            isDefault - Indicates whether the VPC is the default VPC.
            state - The state of the VPC (pending | available ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            vpc-id - The ID of the VPC.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'Vpcs': [
            {
                'VpcId': 'string',
                'State': 'pending'|'available',
                'CidrBlock': 'string',
                'DhcpOptionsId': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'InstanceTenancy': 'default'|'dedicated'|'host',
                'IsDefault': True|False,
                'Ipv6CidrBlockAssociationSet': [
                    {
                        'Ipv6CidrBlock': 'string',
                        'Ipv6CidrBlockState': {
                            'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                            'StatusMessage': 'string'
                        },
                        'AssociationId': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_vpn_connections(DryRun=None, VpnConnectionIds=None, Filters=None):
    """
    Describes one or more of your VPN connections.
    For more information about VPN connections, see Adding a Hardware Virtual Private Gateway to Your VPC in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_vpn_connections(
        DryRun=True|False,
        VpnConnectionIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpnConnectionIds: list
    :param VpnConnectionIds: One or more VPN connection IDs.
            Default: Describes your VPN connections.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            customer-gateway-configuration - The configuration information for the customer gateway.
            customer-gateway-id - The ID of a customer gateway associated with the VPN connection.
            state - The state of the VPN connection (pending | available | deleting | deleted ).
            option.static-routes-only - Indicates whether the connection has static routes only. Used for devices that do not support Border Gateway Protocol (BGP).
            route.destination-cidr-block - The destination CIDR block. This corresponds to the subnet used in a customer data center.
            bgp-asn - The BGP Autonomous System Number (ASN) associated with a BGP device.
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            type - The type of VPN connection. Currently the only supported type is ipsec.1 .
            vpn-connection-id - The ID of the VPN connection.
            vpn-gateway-id - The ID of a virtual private gateway associated with the VPN connection.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'VpnConnections': [
            {
                'VpnConnectionId': 'string',
                'State': 'pending'|'available'|'deleting'|'deleted',
                'CustomerGatewayConfiguration': 'string',
                'Type': 'ipsec.1',
                'CustomerGatewayId': 'string',
                'VpnGatewayId': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'VgwTelemetry': [
                    {
                        'OutsideIpAddress': 'string',
                        'Status': 'UP'|'DOWN',
                        'LastStatusChange': datetime(2015, 1, 1),
                        'StatusMessage': 'string',
                        'AcceptedRouteCount': 123
                    },
                ],
                'Options': {
                    'StaticRoutesOnly': True|False
                },
                'Routes': [
                    {
                        'DestinationCidrBlock': 'string',
                        'Source': 'Static',
                        'State': 'pending'|'available'|'deleting'|'deleted'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_vpn_gateways(DryRun=None, VpnGatewayIds=None, Filters=None):
    """
    Describes one or more of your virtual private gateways.
    For more information about virtual private gateways, see Adding an IPsec Hardware VPN to Your VPC in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_vpn_gateways(
        DryRun=True|False,
        VpnGatewayIds=[
            'string',
        ],
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpnGatewayIds: list
    :param VpnGatewayIds: One or more virtual private gateway IDs.
            Default: Describes all your virtual private gateways.
            (string) --
            

    :type Filters: list
    :param Filters: One or more filters.
            attachment.state - The current state of the attachment between the gateway and the VPC (attaching | attached | detaching | detached ).
            attachment.vpc-id - The ID of an attached VPC.
            availability-zone - The Availability Zone for the virtual private gateway (if applicable).
            state - The state of the virtual private gateway (pending | available | deleting | deleted ).
            tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
            tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter 'tag-key=Purpose' and the filter 'tag-value=X', you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
            tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
            type - The type of virtual private gateway. Currently the only supported type is ipsec.1 .
            vpn-gateway-id - The ID of the virtual private gateway.
            (dict) --A filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as tags, attributes, or IDs.
            Name (string) --The name of the filter. Filter names are case-sensitive.
            Values (list) --One or more filter values. Filter values are case-sensitive.
            (string) --
            
            

    :rtype: dict
    :return: {
        'VpnGateways': [
            {
                'VpnGatewayId': 'string',
                'State': 'pending'|'available'|'deleting'|'deleted',
                'Type': 'ipsec.1',
                'AvailabilityZone': 'string',
                'VpcAttachments': [
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
            },
        ]
    }
    
    
    """
    pass

def detach_classic_link_vpc(DryRun=None, InstanceId=None, VpcId=None):
    """
    Unlinks (detaches) a linked EC2-Classic instance from a VPC. After the instance has been unlinked, the VPC security groups are no longer associated with it. An instance is automatically unlinked from a VPC when it's stopped.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_classic_link_vpc(
        DryRun=True|False,
        InstanceId='string',
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance to unlink from the VPC.
            

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC to which the instance is linked.
            

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def detach_internet_gateway(DryRun=None, InternetGatewayId=None, VpcId=None):
    """
    Detaches an Internet gateway from a VPC, disabling connectivity between the Internet and the VPC. The VPC must not contain any running instances with Elastic IP addresses or public IPv4 addresses.
    See also: AWS API Documentation
    
    Examples
    This example detaches the specified Internet gateway from the specified VPC.
    Expected Output:
    
    :example: response = client.detach_internet_gateway(
        DryRun=True|False,
        InternetGatewayId='string',
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InternetGatewayId: string
    :param InternetGatewayId: [REQUIRED]
            The ID of the Internet gateway.
            

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :return: response = client.detach_internet_gateway(
        InternetGatewayId='igw-c0a643a9',
        VpcId='vpc-a01106c2',
    )
    
    print(response)
    
    
    """
    pass

def detach_network_interface(DryRun=None, AttachmentId=None, Force=None):
    """
    Detaches a network interface from an instance.
    See also: AWS API Documentation
    
    Examples
    This example detaches the specified network interface from its attached instance.
    Expected Output:
    
    :example: response = client.detach_network_interface(
        DryRun=True|False,
        AttachmentId='string',
        Force=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type AttachmentId: string
    :param AttachmentId: [REQUIRED]
            The ID of the attachment.
            

    :type Force: boolean
    :param Force: Specifies whether to force a detachment.

    :return: response = client.detach_network_interface(
        AttachmentId='eni-attach-66c4350a',
    )
    
    print(response)
    
    
    """
    pass

def detach_volume(DryRun=None, VolumeId=None, InstanceId=None, Device=None, Force=None):
    """
    Detaches an EBS volume from an instance. Make sure to unmount any file systems on the device within your operating system before detaching the volume. Failure to do so can result in the volume becoming stuck in the busy state while detaching. If this happens, detachment can be delayed indefinitely until you unmount the volume, force detachment, reboot the instance, or all three. If an EBS volume is the root device of an instance, it can't be detached while the instance is running. To detach the root volume, stop the instance first.
    When a volume with an AWS Marketplace product code is detached from an instance, the product code is no longer associated with the instance.
    For more information, see Detaching an Amazon EBS Volume in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example detaches the volume (vol-049df61146c4d7901) from the instance it is attached to.
    Expected Output:
    
    :example: response = client.detach_volume(
        DryRun=True|False,
        VolumeId='string',
        InstanceId='string',
        Device='string',
        Force=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeId: string
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            

    :type InstanceId: string
    :param InstanceId: The ID of the instance.

    :type Device: string
    :param Device: The device name.

    :type Force: boolean
    :param Force: Forces detachment if the previous detachment attempt did not occur cleanly (for example, logging into an instance, unmounting the volume, and detaching normally). This option can lead to data loss or a corrupted file system. Use this option only as a last resort to detach a volume from a failed instance. The instance won't have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures.

    :rtype: dict
    :return: {
        'VolumeId': 'string',
        'InstanceId': 'string',
        'Device': 'string',
        'State': 'attaching'|'attached'|'detaching'|'detached',
        'AttachTime': datetime(2015, 1, 1),
        'DeleteOnTermination': True|False
    }
    
    
    """
    pass

def detach_vpn_gateway(DryRun=None, VpnGatewayId=None, VpcId=None):
    """
    Detaches a virtual private gateway from a VPC. You do this if you're planning to turn off the VPC and not use it anymore. You can confirm a virtual private gateway has been completely detached from a VPC by describing the virtual private gateway (any attachments to the virtual private gateway are also described).
    You must wait for the attachment's state to switch to detached before you can delete the VPC or attach a different VPC to the virtual private gateway.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_vpn_gateway(
        DryRun=True|False,
        VpnGatewayId='string',
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpnGatewayId: string
    :param VpnGatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    """
    pass

def disable_vgw_route_propagation(RouteTableId=None, GatewayId=None):
    """
    Disables a virtual private gateway (VGW) from propagating routes to a specified route table of a VPC.
    See also: AWS API Documentation
    
    Examples
    This example disables the specified virtual private gateway from propagating static routes to the specified route table.
    Expected Output:
    
    :example: response = client.disable_vgw_route_propagation(
        RouteTableId='string',
        GatewayId='string'
    )
    
    
    :type RouteTableId: string
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            

    :type GatewayId: string
    :param GatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            

    :return: response = client.disable_vgw_route_propagation(
        GatewayId='vgw-9a4cacf3',
        RouteTableId='rtb-22574640',
    )
    
    print(response)
    
    
    """
    pass

def disable_vpc_classic_link(DryRun=None, VpcId=None):
    """
    Disables ClassicLink for a VPC. You cannot disable ClassicLink for a VPC that has EC2-Classic instances linked to it.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_vpc_classic_link(
        DryRun=True|False,
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def disable_vpc_classic_link_dns_support(VpcId=None):
    """
    Disables ClassicLink DNS support for a VPC. If disabled, DNS hostnames resolve to public IP addresses when addressed between a linked EC2-Classic instance and instances in the VPC to which it's linked. For more information about ClassicLink, see ClassicLink in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.disable_vpc_classic_link_dns_support(
        VpcId='string'
    )
    
    
    :type VpcId: string
    :param VpcId: The ID of the VPC.

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def disassociate_address(DryRun=None, PublicIp=None, AssociationId=None):
    """
    Disassociates an Elastic IP address from the instance or network interface it's associated with.
    An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide .
    This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error.
    See also: AWS API Documentation
    
    Examples
    This example disassociates an Elastic IP address from an instance in a VPC.
    Expected Output:
    This example disassociates an Elastic IP address from an instance in EC2-Classic.
    Expected Output:
    
    :example: response = client.disassociate_address(
        DryRun=True|False,
        PublicIp='string',
        AssociationId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type PublicIp: string
    :param PublicIp: [EC2-Classic] The Elastic IP address. Required for EC2-Classic.

    :type AssociationId: string
    :param AssociationId: [EC2-VPC] The association ID. Required for EC2-VPC.

    :return: response = client.disassociate_address(
        AssociationId='eipassoc-2bebb745',
    )
    
    print(response)
    
    
    """
    pass

def disassociate_iam_instance_profile(AssociationId=None):
    """
    Disassociates an IAM instance profile from a running or stopped instance.
    Use  DescribeIamInstanceProfileAssociations to get the association ID.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_iam_instance_profile(
        AssociationId='string'
    )
    
    
    :type AssociationId: string
    :param AssociationId: [REQUIRED]
            The ID of the IAM instance profile association.
            

    :rtype: dict
    :return: {
        'IamInstanceProfileAssociation': {
            'AssociationId': 'string',
            'InstanceId': 'string',
            'IamInstanceProfile': {
                'Arn': 'string',
                'Id': 'string'
            },
            'State': 'associating'|'associated'|'disassociating'|'disassociated',
            'Timestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def disassociate_route_table(DryRun=None, AssociationId=None):
    """
    Disassociates a subnet from a route table.
    After you perform this action, the subnet no longer uses the routes in the route table. Instead, it uses the routes in the VPC's main route table. For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example disassociates the specified route table from its associated subnet.
    Expected Output:
    
    :example: response = client.disassociate_route_table(
        DryRun=True|False,
        AssociationId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type AssociationId: string
    :param AssociationId: [REQUIRED]
            The association ID representing the current association between the route table and subnet.
            

    :return: response = client.disassociate_route_table(
        AssociationId='rtbassoc-781d0d1a',
    )
    
    print(response)
    
    
    """
    pass

def disassociate_subnet_cidr_block(AssociationId=None):
    """
    Disassociates a CIDR block from a subnet. Currently, you can disassociate an IPv6 CIDR block only. You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_subnet_cidr_block(
        AssociationId='string'
    )
    
    
    :type AssociationId: string
    :param AssociationId: [REQUIRED]
            The association ID for the CIDR block.
            

    :rtype: dict
    :return: {
        'SubnetId': 'string',
        'Ipv6CidrBlockAssociation': {
            'Ipv6CidrBlock': 'string',
            'Ipv6CidrBlockState': {
                'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                'StatusMessage': 'string'
            },
            'AssociationId': 'string'
        }
    }
    
    
    """
    pass

def disassociate_vpc_cidr_block(AssociationId=None):
    """
    Disassociates a CIDR block from a VPC. Currently, you can disassociate an IPv6 CIDR block only. You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_vpc_cidr_block(
        AssociationId='string'
    )
    
    
    :type AssociationId: string
    :param AssociationId: [REQUIRED]
            The association ID for the CIDR block.
            

    :rtype: dict
    :return: {
        'VpcId': 'string',
        'Ipv6CidrBlockAssociation': {
            'Ipv6CidrBlock': 'string',
            'Ipv6CidrBlockState': {
                'State': 'associating'|'associated'|'disassociating'|'disassociated'|'failing'|'failed',
                'StatusMessage': 'string'
            },
            'AssociationId': 'string'
        }
    }
    
    
    """
    pass

def enable_vgw_route_propagation(RouteTableId=None, GatewayId=None):
    """
    Enables a virtual private gateway (VGW) to propagate routes to the specified route table of a VPC.
    See also: AWS API Documentation
    
    Examples
    This example enables the specified virtual private gateway to propagate static routes to the specified route table.
    Expected Output:
    
    :example: response = client.enable_vgw_route_propagation(
        RouteTableId='string',
        GatewayId='string'
    )
    
    
    :type RouteTableId: string
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            

    :type GatewayId: string
    :param GatewayId: [REQUIRED]
            The ID of the virtual private gateway.
            

    :return: response = client.enable_vgw_route_propagation(
        GatewayId='vgw-9a4cacf3',
        RouteTableId='rtb-22574640',
    )
    
    print(response)
    
    
    """
    pass

def enable_volume_io(DryRun=None, VolumeId=None):
    """
    Enables I/O operations for a volume that had I/O operations disabled because the data on the volume was potentially inconsistent.
    See also: AWS API Documentation
    
    Examples
    This example enables I/O on volume vol-1234567890abcdef0.
    Expected Output:
    
    :example: response = client.enable_volume_io(
        DryRun=True|False,
        VolumeId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeId: string
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            

    :return: response = client.enable_volume_io(
        VolumeId='vol-1234567890abcdef0',
    )
    
    print(response)
    
    
    """
    pass

def enable_vpc_classic_link(DryRun=None, VpcId=None):
    """
    Enables a VPC for ClassicLink. You can then link EC2-Classic instances to your ClassicLink-enabled VPC to allow communication over private IP addresses. You cannot enable your VPC for ClassicLink if any of your VPC's route tables have existing routes for address ranges within the 10.0.0.0/8 IP address range, excluding local routes for VPCs in the 10.0.0.0/16 and 10.1.0.0/16 IP address ranges. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.enable_vpc_classic_link(
        DryRun=True|False,
        VpcId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def enable_vpc_classic_link_dns_support(VpcId=None):
    """
    Enables a VPC to support DNS hostname resolution for ClassicLink. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance. For more information about ClassicLink, see ClassicLink in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.enable_vpc_classic_link_dns_support(
        VpcId='string'
    )
    
    
    :type VpcId: string
    :param VpcId: The ID of the VPC.

    :rtype: dict
    :return: {
        'Return': True|False
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

def get_console_output(DryRun=None, InstanceId=None):
    """
    Gets the console output for the specified instance.
    Instances do not have a physical monitor through which you can view their console output. They also lack physical controls that allow you to power up, reboot, or shut them down. To allow these actions, we provide them through the Amazon EC2 API and command line interface.
    Instance console output is buffered and posted shortly after instance boot, reboot, and termination. Amazon EC2 preserves the most recent 64 KB output which is available for at least one hour after the most recent post.
    For Linux instances, the instance console output displays the exact console output that would normally be displayed on a physical monitor attached to a computer. This output is buffered because the instance produces it and then posts it to a store where the instance's owner can retrieve it.
    For Windows instances, the instance console output includes output from the EC2Config service.
    See also: AWS API Documentation
    
    
    :example: response = client.get_console_output(
        DryRun=True|False,
        InstanceId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :rtype: dict
    :return: {
        'InstanceId': 'string',
        'Timestamp': datetime(2015, 1, 1),
        'Output': 'string'
    }
    
    
    """
    pass

def get_console_screenshot(DryRun=None, InstanceId=None, WakeUp=None):
    """
    Retrieve a JPG-format screenshot of a running instance to help with troubleshooting.
    The returned content is Base64-encoded.
    See also: AWS API Documentation
    
    
    :example: response = client.get_console_screenshot(
        DryRun=True|False,
        InstanceId='string',
        WakeUp=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type WakeUp: boolean
    :param WakeUp: When set to true , acts as keystroke input and wakes up an instance that's in standby or 'sleep' mode.

    :rtype: dict
    :return: {
        'InstanceId': 'string',
        'ImageData': 'string'
    }
    
    
    """
    pass

def get_host_reservation_purchase_preview(OfferingId=None, HostIdSet=None):
    """
    Preview a reservation purchase with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation.
    This is a preview of the  PurchaseHostReservation action and does not result in the offering being purchased.
    See also: AWS API Documentation
    
    
    :example: response = client.get_host_reservation_purchase_preview(
        OfferingId='string',
        HostIdSet=[
            'string',
        ]
    )
    
    
    :type OfferingId: string
    :param OfferingId: [REQUIRED]
            The offering ID of the reservation.
            

    :type HostIdSet: list
    :param HostIdSet: [REQUIRED]
            The ID/s of the Dedicated Host/s that the reservation will be associated with.
            (string) --
            

    :rtype: dict
    :return: {
        'Purchase': [
            {
                'HostReservationId': 'string',
                'HostIdSet': [
                    'string',
                ],
                'InstanceFamily': 'string',
                'PaymentOption': 'AllUpfront'|'PartialUpfront'|'NoUpfront',
                'UpfrontPrice': 'string',
                'HourlyPrice': 'string',
                'CurrencyCode': 'USD',
                'Duration': 123
            },
        ],
        'TotalUpfrontPrice': 'string',
        'TotalHourlyPrice': 'string',
        'CurrencyCode': 'USD'
    }
    
    
    :returns: 
    (string) --
    
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

def get_password_data(DryRun=None, InstanceId=None):
    """
    Retrieves the encrypted administrator password for an instance running Windows.
    The Windows password is generated at boot if the EC2Config service plugin, Ec2SetPassword , is enabled. This usually only happens the first time an AMI is launched, and then Ec2SetPassword is automatically disabled. The password is not generated for rebundled AMIs unless Ec2SetPassword is enabled before bundling.
    The password is encrypted using the key pair that you specified when you launched the instance. You must provide the corresponding key pair file.
    Password generation and encryption takes a few moments. We recommend that you wait up to 15 minutes after launching an instance before trying to retrieve the generated password.
    See also: AWS API Documentation
    
    
    :example: response = client.get_password_data(
        DryRun=True|False,
        InstanceId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the Windows instance.
            

    :rtype: dict
    :return: {
        'InstanceId': 'string',
        'Timestamp': datetime(2015, 1, 1),
        'PasswordData': 'string'
    }
    
    
    """
    pass

def get_reserved_instances_exchange_quote(DryRun=None, ReservedInstanceIds=None, TargetConfigurations=None):
    """
    Returns details about the values and term of your specified Convertible Reserved Instances. When a target configuration is specified, it returns information about whether the exchange is valid and can be performed.
    See also: AWS API Documentation
    
    
    :example: response = client.get_reserved_instances_exchange_quote(
        DryRun=True|False,
        ReservedInstanceIds=[
            'string',
        ],
        TargetConfigurations=[
            {
                'OfferingId': 'string',
                'InstanceCount': 123
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ReservedInstanceIds: list
    :param ReservedInstanceIds: [REQUIRED]
            The IDs of the Convertible Reserved Instances to exchange.
            (string) --
            

    :type TargetConfigurations: list
    :param TargetConfigurations: The configuration requirements of the Convertible Reserved Instances to exchange for your current Convertible Reserved Instances.
            (dict) --Details about the target configuration.
            OfferingId (string) -- [REQUIRED]The Convertible Reserved Instance offering ID.
            InstanceCount (integer) --The number of instances the Covertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request
            
            

    :rtype: dict
    :return: {
        'ReservedInstanceValueSet': [
            {
                'ReservedInstanceId': 'string',
                'ReservationValue': {
                    'RemainingTotalValue': 'string',
                    'RemainingUpfrontValue': 'string',
                    'HourlyPrice': 'string'
                }
            },
        ],
        'ReservedInstanceValueRollup': {
            'RemainingTotalValue': 'string',
            'RemainingUpfrontValue': 'string',
            'HourlyPrice': 'string'
        },
        'TargetConfigurationValueSet': [
            {
                'TargetConfiguration': {
                    'OfferingId': 'string',
                    'InstanceCount': 123
                },
                'ReservationValue': {
                    'RemainingTotalValue': 'string',
                    'RemainingUpfrontValue': 'string',
                    'HourlyPrice': 'string'
                }
            },
        ],
        'TargetConfigurationValueRollup': {
            'RemainingTotalValue': 'string',
            'RemainingUpfrontValue': 'string',
            'HourlyPrice': 'string'
        },
        'PaymentDue': 'string',
        'CurrencyCode': 'string',
        'OutputReservedInstancesWillExpireAt': datetime(2015, 1, 1),
        'IsValidExchange': True|False,
        'ValidationFailureReason': 'string'
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def import_image(DryRun=None, Description=None, DiskContainers=None, LicenseType=None, Hypervisor=None, Architecture=None, Platform=None, ClientData=None, ClientToken=None, RoleName=None):
    """
    Import single or multi-volume disk images or EBS snapshots into an Amazon Machine Image (AMI). For more information, see Importing a VM as an Image Using VM Import/Export in the VM Import/Export User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.import_image(
        DryRun=True|False,
        Description='string',
        DiskContainers=[
            {
                'Description': 'string',
                'Format': 'string',
                'Url': 'string',
                'UserBucket': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'DeviceName': 'string',
                'SnapshotId': 'string'
            },
        ],
        LicenseType='string',
        Hypervisor='string',
        Architecture='string',
        Platform='string',
        ClientData={
            'UploadStart': datetime(2015, 1, 1),
            'UploadEnd': datetime(2015, 1, 1),
            'UploadSize': 123.0,
            'Comment': 'string'
        },
        ClientToken='string',
        RoleName='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Description: string
    :param Description: A description string for the import image task.

    :type DiskContainers: list
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
            
            

    :type LicenseType: string
    :param LicenseType: The license type to be used for the Amazon Machine Image (AMI) after importing.
            Note: You may only use BYOL if you have existing licenses with rights to use these licenses in a third party cloud like AWS. For more information, see Prerequisites in the VM Import/Export User Guide.
            Valid values: AWS | BYOL
            

    :type Hypervisor: string
    :param Hypervisor: The target hypervisor platform.
            Valid values: xen
            

    :type Architecture: string
    :param Architecture: The architecture of the virtual machine.
            Valid values: i386 | x86_64
            

    :type Platform: string
    :param Platform: The operating system of the virtual machine.
            Valid values: Windows | Linux
            

    :type ClientData: dict
    :param ClientData: The client-specific data.
            UploadStart (datetime) --The time that the disk upload starts.
            UploadEnd (datetime) --The time that the disk upload ends.
            UploadSize (float) --The size of the uploaded disk image, in GiB.
            Comment (string) --A user-defined comment about the disk upload.
            

    :type ClientToken: string
    :param ClientToken: The token to enable idempotency for VM import requests.

    :type RoleName: string
    :param RoleName: The name of the role to use when not using the default role, 'vmimport'.

    :rtype: dict
    :return: {
        'ImportTaskId': 'string',
        'Architecture': 'string',
        'LicenseType': 'string',
        'Platform': 'string',
        'Hypervisor': 'string',
        'Description': 'string',
        'SnapshotDetails': [
            {
                'DiskImageSize': 123.0,
                'Description': 'string',
                'Format': 'string',
                'Url': 'string',
                'UserBucket': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'DeviceName': 'string',
                'SnapshotId': 'string',
                'Progress': 'string',
                'StatusMessage': 'string',
                'Status': 'string'
            },
        ],
        'ImageId': 'string',
        'Progress': 'string',
        'StatusMessage': 'string',
        'Status': 'string'
    }
    
    
    """
    pass

def import_instance(DryRun=None, Description=None, LaunchSpecification=None, DiskImages=None, Platform=None):
    """
    Creates an import instance task using metadata from the specified disk image. ImportInstance only supports single-volume VMs. To import multi-volume VMs, use  ImportImage . For more information, see Importing a Virtual Machine Using the Amazon EC2 CLI .
    For information about the import manifest referenced by this API action, see VM Import Manifest .
    See also: AWS API Documentation
    
    
    :example: response = client.import_instance(
        DryRun=True|False,
        Description='string',
        LaunchSpecification={
            'Architecture': 'i386'|'x86_64',
            'GroupNames': [
                'string',
            ],
            'GroupIds': [
                'string',
            ],
            'AdditionalInfo': 'string',
            'UserData': {
                'Data': 'string'
            },
            'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
            'Placement': {
                'AvailabilityZone': 'string',
                'GroupName': 'string',
                'Tenancy': 'default'|'dedicated'|'host',
                'HostId': 'string',
                'Affinity': 'string'
            },
            'Monitoring': True|False,
            'SubnetId': 'string',
            'InstanceInitiatedShutdownBehavior': 'stop'|'terminate',
            'PrivateIpAddress': 'string'
        },
        DiskImages=[
            {
                'Image': {
                    'Format': 'VMDK'|'RAW'|'VHD',
                    'Bytes': 123,
                    'ImportManifestUrl': 'string'
                },
                'Description': 'string',
                'Volume': {
                    'Size': 123
                }
            },
        ],
        Platform='Windows'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Description: string
    :param Description: A description for the instance being imported.

    :type LaunchSpecification: dict
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
            HostId (string) --The ID of the Dedicated Host on which the instance resides. This parameter is not supported for the ImportInstance command.
            Affinity (string) --The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the ImportInstance command.
            Monitoring (boolean) --Indicates whether monitoring is enabled.
            SubnetId (string) --[EC2-VPC] The ID of the subnet in which to launch the instance.
            InstanceInitiatedShutdownBehavior (string) --Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
            PrivateIpAddress (string) --[EC2-VPC] An available IP address from the IP address range of the subnet.
            

    :type DiskImages: list
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
            
            

    :type Platform: string
    :param Platform: [REQUIRED]
            The instance operating system.
            

    :rtype: dict
    :return: {
        'ConversionTask': {
            'ConversionTaskId': 'string',
            'ExpirationTime': 'string',
            'ImportInstance': {
                'Volumes': [
                    {
                        'BytesConverted': 123,
                        'AvailabilityZone': 'string',
                        'Image': {
                            'Format': 'VMDK'|'RAW'|'VHD',
                            'Size': 123,
                            'ImportManifestUrl': 'string',
                            'Checksum': 'string'
                        },
                        'Volume': {
                            'Size': 123,
                            'Id': 'string'
                        },
                        'Status': 'string',
                        'StatusMessage': 'string',
                        'Description': 'string'
                    },
                ],
                'InstanceId': 'string',
                'Platform': 'Windows',
                'Description': 'string'
            },
            'ImportVolume': {
                'BytesConverted': 123,
                'AvailabilityZone': 'string',
                'Description': 'string',
                'Image': {
                    'Format': 'VMDK'|'RAW'|'VHD',
                    'Size': 123,
                    'ImportManifestUrl': 'string',
                    'Checksum': 'string'
                },
                'Volume': {
                    'Size': 123,
                    'Id': 'string'
                }
            },
            'State': 'active'|'cancelling'|'cancelled'|'completed',
            'StatusMessage': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def import_key_pair(DryRun=None, KeyName=None, PublicKeyMaterial=None):
    """
    Imports the public key from an RSA key pair that you created with a third-party tool. Compare this with  CreateKeyPair , in which AWS creates the key pair and gives the keys to you (AWS keeps a copy of the public key). With ImportKeyPair, you create the key pair and give AWS just the public key. The private key is never transferred between you and AWS.
    For more information about key pairs, see Key Pairs in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.import_key_pair(
        DryRun=True|False,
        KeyName='string',
        PublicKeyMaterial=b'bytes'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type KeyName: string
    :param KeyName: [REQUIRED]
            A unique name for the key pair.
            

    :type PublicKeyMaterial: bytes
    :param PublicKeyMaterial: [REQUIRED]
            The public key. For API calls, the text must be base64-encoded. For command line tools, base64 encoding is performed for you.
            

    :rtype: dict
    :return: {
        'KeyName': 'string',
        'KeyFingerprint': 'string'
    }
    
    
    """
    pass

def import_snapshot(DryRun=None, Description=None, DiskContainer=None, ClientData=None, ClientToken=None, RoleName=None):
    """
    Imports a disk into an EBS snapshot.
    See also: AWS API Documentation
    
    
    :example: response = client.import_snapshot(
        DryRun=True|False,
        Description='string',
        DiskContainer={
            'Description': 'string',
            'Format': 'string',
            'Url': 'string',
            'UserBucket': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            }
        },
        ClientData={
            'UploadStart': datetime(2015, 1, 1),
            'UploadEnd': datetime(2015, 1, 1),
            'UploadSize': 123.0,
            'Comment': 'string'
        },
        ClientToken='string',
        RoleName='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Description: string
    :param Description: The description string for the import snapshot task.

    :type DiskContainer: dict
    :param DiskContainer: Information about the disk container.
            Description (string) --The description of the disk image being imported.
            Format (string) --The format of the disk image being imported.
            Valid values: RAW | VHD | VMDK | OVA
            Url (string) --The URL to the Amazon S3-based disk image being imported. It can either be a https URL (https://..) or an Amazon S3 URL (s3://..).
            UserBucket (dict) --The S3 bucket for the disk image.
            S3Bucket (string) --The name of the S3 bucket where the disk image is located.
            S3Key (string) --The file name of the disk image.
            
            

    :type ClientData: dict
    :param ClientData: The client-specific data.
            UploadStart (datetime) --The time that the disk upload starts.
            UploadEnd (datetime) --The time that the disk upload ends.
            UploadSize (float) --The size of the uploaded disk image, in GiB.
            Comment (string) --A user-defined comment about the disk upload.
            

    :type ClientToken: string
    :param ClientToken: Token to enable idempotency for VM import requests.

    :type RoleName: string
    :param RoleName: The name of the role to use when not using the default role, 'vmimport'.

    :rtype: dict
    :return: {
        'ImportTaskId': 'string',
        'SnapshotTaskDetail': {
            'DiskImageSize': 123.0,
            'Description': 'string',
            'Format': 'string',
            'Url': 'string',
            'UserBucket': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'SnapshotId': 'string',
            'Progress': 'string',
            'StatusMessage': 'string',
            'Status': 'string'
        },
        'Description': 'string'
    }
    
    
    """
    pass

def import_volume(DryRun=None, AvailabilityZone=None, Image=None, Description=None, Volume=None):
    """
    Creates an import volume task using metadata from the specified disk image.For more information, see Importing Disks to Amazon EBS .
    For information about the import manifest referenced by this API action, see VM Import Manifest .
    See also: AWS API Documentation
    
    
    :example: response = client.import_volume(
        DryRun=True|False,
        AvailabilityZone='string',
        Image={
            'Format': 'VMDK'|'RAW'|'VHD',
            'Bytes': 123,
            'ImportManifestUrl': 'string'
        },
        Description='string',
        Volume={
            'Size': 123
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type AvailabilityZone: string
    :param AvailabilityZone: [REQUIRED]
            The Availability Zone for the resulting EBS volume.
            

    :type Image: dict
    :param Image: [REQUIRED]
            The disk image.
            Format (string) -- [REQUIRED]The disk image format.
            Bytes (integer) -- [REQUIRED]The size of the disk image, in GiB.
            ImportManifestUrl (string) -- [REQUIRED]A presigned URL for the import manifest stored in Amazon S3 and presented here as an Amazon S3 presigned URL. For information about creating a presigned URL for an Amazon S3 object, read the 'Query String Request Authentication Alternative' section of the Authenticating REST Requests topic in the Amazon Simple Storage Service Developer Guide .
            For information about the import manifest referenced by this API action, see VM Import Manifest .
            

    :type Description: string
    :param Description: A description of the volume.

    :type Volume: dict
    :param Volume: [REQUIRED]
            The volume size.
            Size (integer) -- [REQUIRED]The size of the volume, in GiB.
            

    :rtype: dict
    :return: {
        'ConversionTask': {
            'ConversionTaskId': 'string',
            'ExpirationTime': 'string',
            'ImportInstance': {
                'Volumes': [
                    {
                        'BytesConverted': 123,
                        'AvailabilityZone': 'string',
                        'Image': {
                            'Format': 'VMDK'|'RAW'|'VHD',
                            'Size': 123,
                            'ImportManifestUrl': 'string',
                            'Checksum': 'string'
                        },
                        'Volume': {
                            'Size': 123,
                            'Id': 'string'
                        },
                        'Status': 'string',
                        'StatusMessage': 'string',
                        'Description': 'string'
                    },
                ],
                'InstanceId': 'string',
                'Platform': 'Windows',
                'Description': 'string'
            },
            'ImportVolume': {
                'BytesConverted': 123,
                'AvailabilityZone': 'string',
                'Description': 'string',
                'Image': {
                    'Format': 'VMDK'|'RAW'|'VHD',
                    'Size': 123,
                    'ImportManifestUrl': 'string',
                    'Checksum': 'string'
                },
                'Volume': {
                    'Size': 123,
                    'Id': 'string'
                }
            },
            'State': 'active'|'cancelling'|'cancelled'|'completed',
            'StatusMessage': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def modify_hosts(HostIds=None, AutoPlacement=None):
    """
    Modify the auto-placement setting of a Dedicated Host. When auto-placement is enabled, AWS will place instances that you launch with a tenancy of host , but without targeting a specific host ID, onto any available Dedicated Host in your account which has auto-placement enabled. When auto-placement is disabled, you need to provide a host ID if you want the instance to launch onto a specific host. If no host ID is provided, the instance will be launched onto a suitable host which has auto-placement enabled.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_hosts(
        HostIds=[
            'string',
        ],
        AutoPlacement='on'|'off'
    )
    
    
    :type HostIds: list
    :param HostIds: [REQUIRED]
            The host IDs of the Dedicated Hosts you want to modify.
            (string) --
            

    :type AutoPlacement: string
    :param AutoPlacement: [REQUIRED]
            Specify whether to enable or disable auto-placement.
            

    :rtype: dict
    :return: {
        'Successful': [
            'string',
        ],
        'Unsuccessful': [
            {
                'ResourceId': 'string',
                'Error': {
                    'Code': 'string',
                    'Message': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_id_format(Resource=None, UseLongIds=None):
    """
    Modifies the ID format for the specified resource on a per-region basis. You can specify that resources should receive longer IDs (17-character IDs) when they are created. The following resource types support longer IDs: instance | reservation | snapshot | volume .
    This setting applies to the IAM user who makes the request; it does not apply to the entire AWS account. By default, an IAM user defaults to the same settings as the root user. If you're using this action as the root user, then these settings apply to the entire account, unless an IAM user explicitly overrides these settings for themselves. For more information, see Resource IDs in the Amazon Elastic Compute Cloud User Guide .
    Resources created with longer IDs are visible to all IAM roles and users, regardless of these settings and provided that they have permission to use the relevant Describe command for the resource type.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_id_format(
        Resource='string',
        UseLongIds=True|False
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            The type of resource: instance | reservation | snapshot | volume
            

    :type UseLongIds: boolean
    :param UseLongIds: [REQUIRED]
            Indicate whether the resource should use longer IDs (17-character IDs).
            

    """
    pass

def modify_identity_id_format(Resource=None, UseLongIds=None, PrincipalArn=None):
    """
    Modifies the ID format of a resource for a specified IAM user, IAM role, or the root user for an account; or all IAM users, IAM roles, and the root user for an account. You can specify that resources should receive longer IDs (17-character IDs) when they are created.
    The following resource types support longer IDs: instance | reservation | snapshot | volume . For more information, see Resource IDs in the Amazon Elastic Compute Cloud User Guide .
    This setting applies to the principal specified in the request; it does not apply to the principal that makes the request.
    Resources created with longer IDs are visible to all IAM roles and users, regardless of these settings and provided that they have permission to use the relevant Describe command for the resource type.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_identity_id_format(
        Resource='string',
        UseLongIds=True|False,
        PrincipalArn='string'
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]
            The type of resource: instance | reservation | snapshot | volume
            

    :type UseLongIds: boolean
    :param UseLongIds: [REQUIRED]
            Indicates whether the resource should use longer IDs (17-character IDs)
            

    :type PrincipalArn: string
    :param PrincipalArn: [REQUIRED]
            The ARN of the principal, which can be an IAM user, IAM role, or the root user. Specify all to modify the ID format for all IAM users, IAM roles, and the root user of the account.
            

    """
    pass

def modify_image_attribute(DryRun=None, ImageId=None, Attribute=None, OperationType=None, UserIds=None, UserGroups=None, ProductCodes=None, Value=None, LaunchPermission=None, Description=None):
    """
    Modifies the specified attribute of the specified AMI. You can specify only one attribute at a time.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_image_attribute(
        DryRun=True|False,
        ImageId='string',
        Attribute='string',
        OperationType='add'|'remove',
        UserIds=[
            'string',
        ],
        UserGroups=[
            'string',
        ],
        ProductCodes=[
            'string',
        ],
        Value='string',
        LaunchPermission={
            'Add': [
                {
                    'UserId': 'string',
                    'Group': 'all'
                },
            ],
            'Remove': [
                {
                    'UserId': 'string',
                    'Group': 'all'
                },
            ]
        },
        Description={
            'Value': 'string'
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImageId: string
    :param ImageId: [REQUIRED]
            The ID of the AMI.
            

    :type Attribute: string
    :param Attribute: The name of the attribute to modify.

    :type OperationType: string
    :param OperationType: The operation type.

    :type UserIds: list
    :param UserIds: One or more AWS account IDs. This is only valid when modifying the launchPermission attribute.
            (string) --
            

    :type UserGroups: list
    :param UserGroups: One or more user groups. This is only valid when modifying the launchPermission attribute.
            (string) --
            

    :type ProductCodes: list
    :param ProductCodes: One or more product codes. After you add a product code to an AMI, it can't be removed. This is only valid when modifying the productCodes attribute.
            (string) --
            

    :type Value: string
    :param Value: The value of the attribute being modified. This is only valid when modifying the description attribute.

    :type LaunchPermission: dict
    :param LaunchPermission: A launch permission modification.
            Add (list) --The AWS account ID to add to the list of launch permissions for the AMI.
            (dict) --Describes a launch permission.
            UserId (string) --The AWS account ID.
            Group (string) --The name of the group.
            
            Remove (list) --The AWS account ID to remove from the list of launch permissions for the AMI.
            (dict) --Describes a launch permission.
            UserId (string) --The AWS account ID.
            Group (string) --The name of the group.
            
            

    :type Description: dict
    :param Description: A description for the AMI.
            Value (string) --The attribute value. Note that the value is case-sensitive.
            

    """
    pass

def modify_instance_attribute(DryRun=None, InstanceId=None, Attribute=None, Value=None, BlockDeviceMappings=None, SourceDestCheck=None, DisableApiTermination=None, InstanceType=None, Kernel=None, Ramdisk=None, UserData=None, InstanceInitiatedShutdownBehavior=None, Groups=None, EbsOptimized=None, SriovNetSupport=None, EnaSupport=None):
    """
    Modifies the specified attribute of the specified instance. You can specify only one attribute at a time.
    To modify some attributes, the instance must be stopped. For more information, see Modifying Attributes of a Stopped Instance in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.modify_instance_attribute(
        DryRun=True|False,
        InstanceId='string',
        Attribute='instanceType'|'kernel'|'ramdisk'|'userData'|'disableApiTermination'|'instanceInitiatedShutdownBehavior'|'rootDeviceName'|'blockDeviceMapping'|'productCodes'|'sourceDestCheck'|'groupSet'|'ebsOptimized'|'sriovNetSupport'|'enaSupport',
        Value='string',
        BlockDeviceMappings=[
            {
                'DeviceName': 'string',
                'Ebs': {
                    'VolumeId': 'string',
                    'DeleteOnTermination': True|False
                },
                'VirtualName': 'string',
                'NoDevice': 'string'
            },
        ],
        SourceDestCheck={
            'Value': True|False
        },
        DisableApiTermination={
            'Value': True|False
        },
        InstanceType={
            'Value': 'string'
        },
        Kernel={
            'Value': 'string'
        },
        Ramdisk={
            'Value': 'string'
        },
        UserData={
            'Value': b'bytes'
        },
        InstanceInitiatedShutdownBehavior={
            'Value': 'string'
        },
        Groups=[
            'string',
        ],
        EbsOptimized={
            'Value': True|False
        },
        SriovNetSupport={
            'Value': 'string'
        },
        EnaSupport={
            'Value': True|False
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type Attribute: string
    :param Attribute: The name of the attribute.

    :type Value: string
    :param Value: A new value for the attribute. Use only with the kernel , ramdisk , userData , disableApiTermination , or instanceInitiatedShutdownBehavior attribute.

    :type BlockDeviceMappings: list
    :param BlockDeviceMappings: Modifies the DeleteOnTermination attribute for volumes that are currently attached. The volume must be owned by the caller. If no value is specified for DeleteOnTermination , the default is true and the volume is deleted when the instance is terminated.
            To add instance store volumes to an Amazon EBS-backed instance, you must add them when you launch the instance. For more information, see Updating the Block Device Mapping when Launching an Instance in the Amazon Elastic Compute Cloud User Guide .
            (dict) --Describes a block device mapping entry.
            DeviceName (string) --The device name exposed to the instance (for example, /dev/sdh or xvdh ).
            Ebs (dict) --Parameters used to automatically set up EBS volumes when the instance is launched.
            VolumeId (string) --The ID of the EBS volume.
            DeleteOnTermination (boolean) --Indicates whether the volume is deleted on instance termination.
            VirtualName (string) --The virtual device name.
            NoDevice (string) --suppress the specified device included in the block device mapping.
            
            

    :type SourceDestCheck: dict
    :param SourceDestCheck: Specifies whether source/destination checking is enabled. A value of true means that checking is enabled, and false means checking is disabled. This value must be false for a NAT instance to perform NAT.
            Value (boolean) --The attribute value. The valid values are true or false .
            

    :type DisableApiTermination: dict
    :param DisableApiTermination: If the value is true , you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. You cannot use this paramater for Spot Instances.
            Value (boolean) --The attribute value. The valid values are true or false .
            

    :type InstanceType: dict
    :param InstanceType: Changes the instance type to the specified value. For more information, see Instance Types . If the instance type is not valid, the error returned is InvalidInstanceAttributeValue .
            Value (string) --The attribute value. Note that the value is case-sensitive.
            

    :type Kernel: dict
    :param Kernel: Changes the instance's kernel to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB .
            Value (string) --The attribute value. Note that the value is case-sensitive.
            

    :type Ramdisk: dict
    :param Ramdisk: Changes the instance's RAM disk to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB .
            Value (string) --The attribute value. Note that the value is case-sensitive.
            

    :type UserData: dict
    :param UserData: Changes the instance's user data to the specified value. If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.
            Value (bytes) --
            

    :type InstanceInitiatedShutdownBehavior: dict
    :param InstanceInitiatedShutdownBehavior: Specifies whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
            Value (string) --The attribute value. Note that the value is case-sensitive.
            

    :type Groups: list
    :param Groups: [EC2-VPC] Changes the security groups of the instance. You must specify at least one security group, even if it's just the default security group for the VPC. You must specify the security group ID, not the security group name.
            (string) --
            

    :type EbsOptimized: dict
    :param EbsOptimized: Specifies whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
            Value (boolean) --The attribute value. The valid values are true or false .
            

    :type SriovNetSupport: dict
    :param SriovNetSupport: Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the instance.
            There is no way to disable enhanced networking with the Intel 82599 Virtual Function interface at this time.
            This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.
            Value (string) --The attribute value. Note that the value is case-sensitive.
            

    :type EnaSupport: dict
    :param EnaSupport: Set to true to enable enhanced networking with ENA for the instance.
            This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.
            Value (boolean) --The attribute value. The valid values are true or false .
            

    """
    pass

def modify_instance_placement(InstanceId=None, Tenancy=None, Affinity=None, HostId=None):
    """
    Set the instance affinity value for a specific stopped instance and modify the instance tenancy setting.
    Instance affinity is disabled by default. When instance affinity is host and it is not associated with a specific Dedicated Host, the next time it is launched it will automatically be associated with the host it lands on. This relationship will persist if the instance is stopped/started, or rebooted.
    You can modify the host ID associated with a stopped instance. If a stopped instance has a new host ID association, the instance will target that host when restarted.
    You can modify the tenancy of a stopped instance with a tenancy of host or dedicated .
    Affinity, hostID, and tenancy are not required parameters, but at least one of them must be specified in the request. Affinity and tenancy can be modified in the same request, but tenancy can only be modified on instances that are stopped.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_instance_placement(
        InstanceId='string',
        Tenancy='dedicated'|'host',
        Affinity='default'|'host',
        HostId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance that you are modifying.
            

    :type Tenancy: string
    :param Tenancy: The tenancy of the instance that you are modifying.

    :type Affinity: string
    :param Affinity: The new affinity setting for the instance.

    :type HostId: string
    :param HostId: The ID of the Dedicated Host that the instance will have affinity with.

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def modify_network_interface_attribute(DryRun=None, NetworkInterfaceId=None, Description=None, SourceDestCheck=None, Groups=None, Attachment=None):
    """
    Modifies the specified network interface attribute. You can specify only one attribute at a time.
    See also: AWS API Documentation
    
    Examples
    This example modifies the attachment attribute of the specified network interface.
    Expected Output:
    This example modifies the description attribute of the specified network interface.
    Expected Output:
    This example command modifies the groupSet attribute of the specified network interface.
    Expected Output:
    This example command modifies the sourceDestCheck attribute of the specified network interface.
    Expected Output:
    
    :example: response = client.modify_network_interface_attribute(
        DryRun=True|False,
        NetworkInterfaceId='string',
        Description={
            'Value': 'string'
        },
        SourceDestCheck={
            'Value': True|False
        },
        Groups=[
            'string',
        ],
        Attachment={
            'AttachmentId': 'string',
            'DeleteOnTermination': True|False
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            

    :type Description: dict
    :param Description: A description for the network interface.
            Value (string) --The attribute value. Note that the value is case-sensitive.
            

    :type SourceDestCheck: dict
    :param SourceDestCheck: Indicates whether source/destination checking is enabled. A value of true means checking is enabled, and false means checking is disabled. This value must be false for a NAT instance to perform NAT. For more information, see NAT Instances in the Amazon Virtual Private Cloud User Guide .
            Value (boolean) --The attribute value. The valid values are true or false .
            

    :type Groups: list
    :param Groups: Changes the security groups for the network interface. The new set of groups you specify replaces the current set. You must specify at least one group, even if it's just the default security group in the VPC. You must specify the ID of the security group, not the name.
            (string) --
            

    :type Attachment: dict
    :param Attachment: Information about the interface attachment. If modifying the 'delete on termination' attribute, you must specify the ID of the interface attachment.
            AttachmentId (string) --The ID of the network interface attachment.
            DeleteOnTermination (boolean) --Indicates whether the network interface is deleted when the instance is terminated.
            

    :return: response = client.modify_network_interface_attribute(
        Attachment={
            'AttachmentId': 'eni-attach-43348162',
            'DeleteOnTermination': False,
        },
        NetworkInterfaceId='eni-686ea200',
    )
    
    print(response)
    
    
    """
    pass

def modify_reserved_instances(ClientToken=None, ReservedInstancesIds=None, TargetConfigurations=None):
    """
    Modifies the Availability Zone, instance count, instance type, or network platform (EC2-Classic or EC2-VPC) of your Standard Reserved Instances. The Reserved Instances to be modified must be identical, except for Availability Zone, network platform, and instance type.
    For more information, see Modifying Reserved Instances in the Amazon Elastic Compute Cloud User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_reserved_instances(
        ClientToken='string',
        ReservedInstancesIds=[
            'string',
        ],
        TargetConfigurations=[
            {
                'AvailabilityZone': 'string',
                'Platform': 'string',
                'InstanceCount': 123,
                'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                'Scope': 'Availability Zone'|'Region'
            },
        ]
    )
    
    
    :type ClientToken: string
    :param ClientToken: A unique, case-sensitive token you provide to ensure idempotency of your modification request. For more information, see Ensuring Idempotency .

    :type ReservedInstancesIds: list
    :param ReservedInstancesIds: [REQUIRED]
            The IDs of the Reserved Instances to modify.
            (string) --
            

    :type TargetConfigurations: list
    :param TargetConfigurations: [REQUIRED]
            The configuration settings for the Reserved Instances to modify.
            (dict) --Describes the configuration settings for the modified Reserved Instances.
            AvailabilityZone (string) --The Availability Zone for the modified Reserved Instances.
            Platform (string) --The network platform of the modified Reserved Instances, which is either EC2-Classic or EC2-VPC.
            InstanceCount (integer) --The number of modified Reserved Instances.
            InstanceType (string) --The instance type for the modified Reserved Instances.
            Scope (string) --Whether the Reserved Instance is applied to instances in a region or instances in a specific Availability Zone.
            
            

    :rtype: dict
    :return: {
        'ReservedInstancesModificationId': 'string'
    }
    
    
    """
    pass

def modify_snapshot_attribute(DryRun=None, SnapshotId=None, Attribute=None, OperationType=None, UserIds=None, GroupNames=None, CreateVolumePermission=None):
    """
    Adds or removes permission settings for the specified snapshot. You may add or remove specified AWS account IDs from a snapshot's list of create volume permissions, but you cannot do both in a single API call. If you need to both add and remove account IDs for a snapshot, you must use multiple API calls.
    For more information on modifying snapshot permissions, see Sharing Snapshots in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example modifies snapshot snap-1234567890abcdef0 to remove the create volume permission for a user with the account ID 123456789012. If the command succeeds, no output is returned.
    Expected Output:
    This example makes the snapshot snap-1234567890abcdef0 public.
    Expected Output:
    
    :example: response = client.modify_snapshot_attribute(
        DryRun=True|False,
        SnapshotId='string',
        Attribute='productCodes'|'createVolumePermission',
        OperationType='add'|'remove',
        UserIds=[
            'string',
        ],
        GroupNames=[
            'string',
        ],
        CreateVolumePermission={
            'Add': [
                {
                    'UserId': 'string',
                    'Group': 'all'
                },
            ],
            'Remove': [
                {
                    'UserId': 'string',
                    'Group': 'all'
                },
            ]
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]
            The ID of the snapshot.
            

    :type Attribute: string
    :param Attribute: The snapshot attribute to modify.
            Note
            Only volume creation permissions may be modified at the customer level.
            

    :type OperationType: string
    :param OperationType: The type of operation to perform to the attribute.

    :type UserIds: list
    :param UserIds: The account ID to modify for the snapshot.
            (string) --
            

    :type GroupNames: list
    :param GroupNames: The group to modify for the snapshot.
            (string) --
            

    :type CreateVolumePermission: dict
    :param CreateVolumePermission: A JSON representation of the snapshot attribute modification.
            Add (list) --Adds a specific AWS account ID or group to a volume's list of create volume permissions.
            (dict) --Describes the user or group to be added or removed from the permissions for a volume.
            UserId (string) --The specific AWS account ID that is to be added or removed from a volume's list of create volume permissions.
            Group (string) --The specific group that is to be added or removed from a volume's list of create volume permissions.
            
            Remove (list) --Removes a specific AWS account ID or group from a volume's list of create volume permissions.
            (dict) --Describes the user or group to be added or removed from the permissions for a volume.
            UserId (string) --The specific AWS account ID that is to be added or removed from a volume's list of create volume permissions.
            Group (string) --The specific group that is to be added or removed from a volume's list of create volume permissions.
            
            

    :return: response = client.modify_snapshot_attribute(
        Attribute='createVolumePermission',
        OperationType='remove',
        SnapshotId='snap-1234567890abcdef0',
        UserIds=[
            '123456789012',
        ],
    )
    
    print(response)
    
    
    """
    pass

def modify_spot_fleet_request(SpotFleetRequestId=None, TargetCapacity=None, ExcessCapacityTerminationPolicy=None):
    """
    Modifies the specified Spot fleet request.
    While the Spot fleet request is being modified, it is in the modifying state.
    To scale up your Spot fleet, increase its target capacity. The Spot fleet launches the additional Spot instances according to the allocation strategy for the Spot fleet request. If the allocation strategy is lowestPrice , the Spot fleet launches instances using the Spot pool with the lowest price. If the allocation strategy is diversified , the Spot fleet distributes the instances across the Spot pools.
    To scale down your Spot fleet, decrease its target capacity. First, the Spot fleet cancels any open bids that exceed the new target capacity. You can request that the Spot fleet terminate Spot instances until the size of the fleet no longer exceeds the new target capacity. If the allocation strategy is lowestPrice , the Spot fleet terminates the instances with the highest price per unit. If the allocation strategy is diversified , the Spot fleet terminates instances across the Spot pools. Alternatively, you can request that the Spot fleet keep the fleet at its current size, but not replace any Spot instances that are interrupted or that you terminate manually.
    See also: AWS API Documentation
    
    Examples
    This example increases the target capacity of the specified Spot fleet request.
    Expected Output:
    This example decreases the target capacity of the specified Spot fleet request without terminating any Spot Instances as a result.
    Expected Output:
    
    :example: response = client.modify_spot_fleet_request(
        SpotFleetRequestId='string',
        TargetCapacity=123,
        ExcessCapacityTerminationPolicy='noTermination'|'default'
    )
    
    
    :type SpotFleetRequestId: string
    :param SpotFleetRequestId: [REQUIRED]
            The ID of the Spot fleet request.
            

    :type TargetCapacity: integer
    :param TargetCapacity: The size of the fleet.

    :type ExcessCapacityTerminationPolicy: string
    :param ExcessCapacityTerminationPolicy: Indicates whether running Spot instances should be terminated if the target capacity of the Spot fleet request is decreased below the current size of the Spot fleet.

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def modify_subnet_attribute(SubnetId=None, MapPublicIpOnLaunch=None, AssignIpv6AddressOnCreation=None):
    """
    Modifies a subnet attribute. You can only modify one attribute at a time.
    See also: AWS API Documentation
    
    Examples
    This example modifies the specified subnet so that all instances launched into this subnet are assigned a public IP address.
    Expected Output:
    
    :example: response = client.modify_subnet_attribute(
        SubnetId='string',
        MapPublicIpOnLaunch={
            'Value': True|False
        },
        AssignIpv6AddressOnCreation={
            'Value': True|False
        }
    )
    
    
    :type SubnetId: string
    :param SubnetId: [REQUIRED]
            The ID of the subnet.
            

    :type MapPublicIpOnLaunch: dict
    :param MapPublicIpOnLaunch: Specify true to indicate that network interfaces created in the specified subnet should be assigned a public IPv4 address. This includes a network interface that's created when launching an instance into the subnet (the instance therefore receives a public IPv4 address).
            Value (boolean) --The attribute value. The valid values are true or false .
            

    :type AssignIpv6AddressOnCreation: dict
    :param AssignIpv6AddressOnCreation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. This includes a network interface that's created when launching an instance into the subnet (the instance therefore receives an IPv6 address).
            If you enable the IPv6 addressing feature for your subnet, your network interface or instance only receives an IPv6 address if it's created using version 2016-11-15 or later of the Amazon EC2 API.
            Value (boolean) --The attribute value. The valid values are true or false .
            

    :return: response = client.modify_subnet_attribute(
        MapPublicIpOnLaunch={
            'Value': True,
        },
        SubnetId='subnet-1a2b3c4d',
    )
    
    print(response)
    
    
    """
    pass

def modify_volume(DryRun=None, VolumeId=None, Size=None, VolumeType=None, Iops=None):
    """
    You can modify several parameters of an existing EBS volume, including volume size, volume type, and IOPS capacity. If your EBS volume is attached to a current-generation EC2 instance type, you may be able to apply these changes without stopping the instance or detaching the volume from it. For more information about modifying an EBS volume running Linux, see Modifying the Size, IOPS, or Type of an EBS Volume on Linux . For more information about modifying an EBS volume running Windows, see Modifying the Size, IOPS, or Type of an EBS Volume on Windows .
    When you complete a resize operation on your volume, you need to extend the volume's file-system size to take advantage of the new storage capacity. For information about extending a Linux file system, see Extending a Linux File System . For information about extending a Windows file system, see Extending a Windows File System .
    You can use CloudWatch Events to check the status of a modification to an EBS volume. For information about CloudWatch Events, see the Amazon CloudWatch Events User Guide . You can also track the status of a modification using the  DescribeVolumesModifications API. For information about tracking status changes using either method, see Monitoring Volume Modifications .
    See also: AWS API Documentation
    
    
    :example: response = client.modify_volume(
        DryRun=True|False,
        VolumeId='string',
        Size=123,
        VolumeType='standard'|'io1'|'gp2'|'sc1'|'st1',
        Iops=123
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeId: string
    :param VolumeId: [REQUIRED]

    :type Size: integer
    :param Size: Target size in GiB of the volume to be modified. Target volume size must be greater than or equal to than the existing size of the volume. For information about available EBS volume sizes, see http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html .
            Default: If no size is specified, the existing size is retained.
            

    :type VolumeType: string
    :param VolumeType: Target EBS volume type of the volume to be modified
            The API does not support modifications for volume type standard . You also cannot change the type of a volume to standard .
            Default: If no type is specified, the existing type is retained.
            

    :type Iops: integer
    :param Iops: Target IOPS rate of the volume to be modified.
            Only valid for Provisioned IOPS SSD (io1 ) volumes. For more information about io1 IOPS configuration, see http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html#EBSVolumeTypes_piops .
            Default: If no IOPS value is specified, the existing value is retained.
            

    :rtype: dict
    :return: {
        'VolumeModification': {
            'VolumeId': 'string',
            'ModificationState': 'modifying'|'optimizing'|'completed'|'failed',
            'StatusMessage': 'string',
            'TargetSize': 123,
            'TargetIops': 123,
            'TargetVolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
            'OriginalSize': 123,
            'OriginalIops': 123,
            'OriginalVolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
            'Progress': 123,
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def modify_volume_attribute(DryRun=None, VolumeId=None, AutoEnableIO=None):
    """
    Modifies a volume attribute.
    By default, all I/O operations for the volume are suspended when the data on the volume is determined to be potentially inconsistent, to prevent undetectable, latent data corruption. The I/O access to the volume can be resumed by first enabling I/O access and then checking the data consistency on your volume.
    You can change the default behavior to resume I/O operations. We recommend that you change this only for boot volumes or for volumes that are stateless or disposable.
    See also: AWS API Documentation
    
    Examples
    This example sets the autoEnableIo attribute of the volume with the ID vol-1234567890abcdef0 to true. If the command succeeds, no output is returned.
    Expected Output:
    
    :example: response = client.modify_volume_attribute(
        DryRun=True|False,
        VolumeId='string',
        AutoEnableIO={
            'Value': True|False
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VolumeId: string
    :param VolumeId: [REQUIRED]
            The ID of the volume.
            

    :type AutoEnableIO: dict
    :param AutoEnableIO: Indicates whether the volume should be auto-enabled for I/O operations.
            Value (boolean) --The attribute value. The valid values are true or false .
            

    :return: response = client.modify_volume_attribute(
        AutoEnableIO={
            'Value': True,
        },
        DryRun=True,
        VolumeId='vol-1234567890abcdef0',
    )
    
    print(response)
    
    
    """
    pass

def modify_vpc_attribute(VpcId=None, EnableDnsSupport=None, EnableDnsHostnames=None):
    """
    Modifies the specified attribute of the specified VPC.
    See also: AWS API Documentation
    
    Examples
    This example modifies the enableDnsSupport attribute. This attribute indicates whether DNS resolution is enabled for the VPC. If this attribute is true, the Amazon DNS server resolves DNS hostnames for instances in the VPC to their corresponding IP addresses; otherwise, it does not.
    Expected Output:
    This example modifies the enableDnsHostnames attribute. This attribute indicates whether instances launched in the VPC get DNS hostnames. If this attribute is true, instances in the VPC get DNS hostnames; otherwise, they do not.
    Expected Output:
    
    :example: response = client.modify_vpc_attribute(
        VpcId='string',
        EnableDnsSupport={
            'Value': True|False
        },
        EnableDnsHostnames={
            'Value': True|False
        }
    )
    
    
    :type VpcId: string
    :param VpcId: [REQUIRED]
            The ID of the VPC.
            

    :type EnableDnsSupport: dict
    :param EnableDnsSupport: Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range 'plus two' will succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled.
            You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute.
            Value (boolean) --The attribute value. The valid values are true or false .
            

    :type EnableDnsHostnames: dict
    :param EnableDnsHostnames: Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not.
            You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute. You can only enable DNS hostnames if you've enabled DNS support.
            Value (boolean) --The attribute value. The valid values are true or false .
            

    :return: response = client.modify_vpc_attribute(
        EnableDnsSupport={
            'Value': False,
        },
        VpcId='vpc-a01106c2',
    )
    
    print(response)
    
    
    """
    pass

def modify_vpc_endpoint(DryRun=None, VpcEndpointId=None, ResetPolicy=None, PolicyDocument=None, AddRouteTableIds=None, RemoveRouteTableIds=None):
    """
    Modifies attributes of a specified VPC endpoint. You can modify the policy associated with the endpoint, and you can add and remove route tables associated with the endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_vpc_endpoint(
        DryRun=True|False,
        VpcEndpointId='string',
        ResetPolicy=True|False,
        PolicyDocument='string',
        AddRouteTableIds=[
            'string',
        ],
        RemoveRouteTableIds=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcEndpointId: string
    :param VpcEndpointId: [REQUIRED]
            The ID of the endpoint.
            

    :type ResetPolicy: boolean
    :param ResetPolicy: Specify true to reset the policy document to the default policy. The default policy allows access to the service.

    :type PolicyDocument: string
    :param PolicyDocument: A policy document to attach to the endpoint. The policy must be in valid JSON format.

    :type AddRouteTableIds: list
    :param AddRouteTableIds: One or more route tables IDs to associate with the endpoint.
            (string) --
            

    :type RemoveRouteTableIds: list
    :param RemoveRouteTableIds: One or more route table IDs to disassociate from the endpoint.
            (string) --
            

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def modify_vpc_peering_connection_options(DryRun=None, VpcPeeringConnectionId=None, RequesterPeeringConnectionOptions=None, AccepterPeeringConnectionOptions=None):
    """
    Modifies the VPC peering connection options on one side of a VPC peering connection. You can do the following:
    If the peered VPCs are in different accounts, each owner must initiate a separate request to modify the peering connection options, depending on whether their VPC was the requester or accepter for the VPC peering connection. If the peered VPCs are in the same account, you can modify the requester and accepter options in the same request. To confirm which VPC is the accepter and requester for a VPC peering connection, use the  DescribeVpcPeeringConnections command.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_vpc_peering_connection_options(
        DryRun=True|False,
        VpcPeeringConnectionId='string',
        RequesterPeeringConnectionOptions={
            'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
            'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
            'AllowDnsResolutionFromRemoteVpc': True|False
        },
        AccepterPeeringConnectionOptions={
            'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
            'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
            'AllowDnsResolutionFromRemoteVpc': True|False
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcPeeringConnectionId: string
    :param VpcPeeringConnectionId: [REQUIRED]
            The ID of the VPC peering connection.
            

    :type RequesterPeeringConnectionOptions: dict
    :param RequesterPeeringConnectionOptions: The VPC peering connection options for the requester VPC.
            AllowEgressFromLocalClassicLinkToRemoteVpc (boolean) --If true, enables outbound communication from an EC2-Classic instance that's linked to a local VPC via ClassicLink to instances in a peer VPC.
            AllowEgressFromLocalVpcToRemoteClassicLink (boolean) --If true, enables outbound communication from instances in a local VPC to an EC2-Classic instance that's linked to a peer VPC via ClassicLink.
            AllowDnsResolutionFromRemoteVpc (boolean) --If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.
            

    :type AccepterPeeringConnectionOptions: dict
    :param AccepterPeeringConnectionOptions: The VPC peering connection options for the accepter VPC.
            AllowEgressFromLocalClassicLinkToRemoteVpc (boolean) --If true, enables outbound communication from an EC2-Classic instance that's linked to a local VPC via ClassicLink to instances in a peer VPC.
            AllowEgressFromLocalVpcToRemoteClassicLink (boolean) --If true, enables outbound communication from instances in a local VPC to an EC2-Classic instance that's linked to a peer VPC via ClassicLink.
            AllowDnsResolutionFromRemoteVpc (boolean) --If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.
            

    :rtype: dict
    :return: {
        'RequesterPeeringConnectionOptions': {
            'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
            'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
            'AllowDnsResolutionFromRemoteVpc': True|False
        },
        'AccepterPeeringConnectionOptions': {
            'AllowEgressFromLocalClassicLinkToRemoteVpc': True|False,
            'AllowEgressFromLocalVpcToRemoteClassicLink': True|False,
            'AllowDnsResolutionFromRemoteVpc': True|False
        }
    }
    
    
    :returns: 
    DryRun (boolean) -- Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    VpcPeeringConnectionId (string) -- [REQUIRED]
    The ID of the VPC peering connection.
    
    RequesterPeeringConnectionOptions (dict) -- The VPC peering connection options for the requester VPC.
    
    AllowEgressFromLocalClassicLinkToRemoteVpc (boolean) --If true, enables outbound communication from an EC2-Classic instance that's linked to a local VPC via ClassicLink to instances in a peer VPC.
    
    AllowEgressFromLocalVpcToRemoteClassicLink (boolean) --If true, enables outbound communication from instances in a local VPC to an EC2-Classic instance that's linked to a peer VPC via ClassicLink.
    
    AllowDnsResolutionFromRemoteVpc (boolean) --If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.
    
    
    
    AccepterPeeringConnectionOptions (dict) -- The VPC peering connection options for the accepter VPC.
    
    AllowEgressFromLocalClassicLinkToRemoteVpc (boolean) --If true, enables outbound communication from an EC2-Classic instance that's linked to a local VPC via ClassicLink to instances in a peer VPC.
    
    AllowEgressFromLocalVpcToRemoteClassicLink (boolean) --If true, enables outbound communication from instances in a local VPC to an EC2-Classic instance that's linked to a peer VPC via ClassicLink.
    
    AllowDnsResolutionFromRemoteVpc (boolean) --If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.
    
    
    
    
    """
    pass

def monitor_instances(DryRun=None, InstanceIds=None):
    """
    Enables detailed monitoring for a running instance. Otherwise, basic monitoring is enabled. For more information, see Monitoring Your Instances and Volumes in the Amazon Elastic Compute Cloud User Guide .
    To disable detailed monitoring, see .
    See also: AWS API Documentation
    
    
    :example: response = client.monitor_instances(
        DryRun=True|False,
        InstanceIds=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'InstanceMonitorings': [
            {
                'InstanceId': 'string',
                'Monitoring': {
                    'State': 'disabled'|'disabling'|'enabled'|'pending'
                }
            },
        ]
    }
    
    
    """
    pass

def move_address_to_vpc(DryRun=None, PublicIp=None):
    """
    Moves an Elastic IP address from the EC2-Classic platform to the EC2-VPC platform. The Elastic IP address must be allocated to your account for more than 24 hours, and it must not be associated with an instance. After the Elastic IP address is moved, it is no longer available for use in the EC2-Classic platform, unless you move it back using the  RestoreAddressToClassic request. You cannot move an Elastic IP address that was originally allocated for use in the EC2-VPC platform to the EC2-Classic platform.
    See also: AWS API Documentation
    
    Examples
    This example moves the specified Elastic IP address to the EC2-VPC platform.
    Expected Output:
    
    :example: response = client.move_address_to_vpc(
        DryRun=True|False,
        PublicIp='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type PublicIp: string
    :param PublicIp: [REQUIRED]
            The Elastic IP address.
            

    :rtype: dict
    :return: {
        'AllocationId': 'string',
        'Status': 'MoveInProgress'|'InVpc'|'InClassic'
    }
    
    
    """
    pass

def purchase_host_reservation(OfferingId=None, HostIdSet=None, LimitPrice=None, CurrencyCode=None, ClientToken=None):
    """
    Purchase a reservation with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. This action results in the specified reservation being purchased and charged to your account.
    See also: AWS API Documentation
    
    
    :example: response = client.purchase_host_reservation(
        OfferingId='string',
        HostIdSet=[
            'string',
        ],
        LimitPrice='string',
        CurrencyCode='USD',
        ClientToken='string'
    )
    
    
    :type OfferingId: string
    :param OfferingId: [REQUIRED]
            The ID of the offering.
            

    :type HostIdSet: list
    :param HostIdSet: [REQUIRED]
            The ID/s of the Dedicated Host/s that the reservation will be associated with.
            (string) --
            

    :type LimitPrice: string
    :param LimitPrice: The specified limit is checked against the total upfront cost of the reservation (calculated as the offering's upfront cost multiplied by the host count). If the total upfront cost is greater than the specified price limit, the request will fail. This is used to ensure that the purchase does not exceed the expected upfront cost of the purchase. At this time, the only supported currency is USD . For example, to indicate a limit price of USD 100, specify 100.00.

    :type CurrencyCode: string
    :param CurrencyCode: The currency in which the totalUpfrontPrice , LimitPrice , and totalHourlyPrice amounts are specified. At this time, the only supported currency is USD .

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide .

    :rtype: dict
    :return: {
        'Purchase': [
            {
                'HostReservationId': 'string',
                'HostIdSet': [
                    'string',
                ],
                'InstanceFamily': 'string',
                'PaymentOption': 'AllUpfront'|'PartialUpfront'|'NoUpfront',
                'UpfrontPrice': 'string',
                'HourlyPrice': 'string',
                'CurrencyCode': 'USD',
                'Duration': 123
            },
        ],
        'TotalUpfrontPrice': 'string',
        'TotalHourlyPrice': 'string',
        'CurrencyCode': 'USD',
        'ClientToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def purchase_reserved_instances_offering(DryRun=None, ReservedInstancesOfferingId=None, InstanceCount=None, LimitPrice=None):
    """
    Purchases a Reserved Instance for use with your account. With Reserved Instances, you pay a lower hourly rate compared to On-Demand instance pricing.
    Use  DescribeReservedInstancesOfferings to get a list of Reserved Instance offerings that match your specifications. After you've purchased a Reserved Instance, you can check for your new Reserved Instance with  DescribeReservedInstances .
    For more information, see Reserved Instances and Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.purchase_reserved_instances_offering(
        DryRun=True|False,
        ReservedInstancesOfferingId='string',
        InstanceCount=123,
        LimitPrice={
            'Amount': 123.0,
            'CurrencyCode': 'USD'
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ReservedInstancesOfferingId: string
    :param ReservedInstancesOfferingId: [REQUIRED]
            The ID of the Reserved Instance offering to purchase.
            

    :type InstanceCount: integer
    :param InstanceCount: [REQUIRED]
            The number of Reserved Instances to purchase.
            

    :type LimitPrice: dict
    :param LimitPrice: Specified for Reserved Instance Marketplace offerings to limit the total order and ensure that the Reserved Instances are not purchased at unexpected prices.
            Amount (float) --Used for Reserved Instance Marketplace offerings. Specifies the limit price on the total order (instanceCount * price).
            CurrencyCode (string) --The currency in which the limitPrice amount is specified. At this time, the only supported currency is USD .
            

    :rtype: dict
    :return: {
        'ReservedInstancesId': 'string'
    }
    
    
    """
    pass

def purchase_scheduled_instances(DryRun=None, ClientToken=None, PurchaseRequests=None):
    """
    Purchases one or more Scheduled Instances with the specified schedule.
    Scheduled Instances enable you to purchase Amazon EC2 compute capacity by the hour for a one-year term. Before you can purchase a Scheduled Instance, you must call  DescribeScheduledInstanceAvailability to check for available schedules and obtain a purchase token. After you purchase a Scheduled Instance, you must call  RunScheduledInstances during each scheduled time period.
    After you purchase a Scheduled Instance, you can't cancel, modify, or resell your purchase.
    See also: AWS API Documentation
    
    Examples
    This example purchases a Scheduled Instance.
    Expected Output:
    
    :example: response = client.purchase_scheduled_instances(
        DryRun=True|False,
        ClientToken='string',
        PurchaseRequests=[
            {
                'PurchaseToken': 'string',
                'InstanceCount': 123
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see Ensuring Idempotency .
            This field is autopopulated if not provided.
            

    :type PurchaseRequests: list
    :param PurchaseRequests: [REQUIRED]
            One or more purchase requests.
            (dict) --Describes a request to purchase Scheduled Instances.
            PurchaseToken (string) -- [REQUIRED]The purchase token.
            InstanceCount (integer) -- [REQUIRED]The number of instances.
            
            

    :rtype: dict
    :return: {
        'ScheduledInstanceSet': [
            {
                'ScheduledInstanceId': 'string',
                'InstanceType': 'string',
                'Platform': 'string',
                'NetworkPlatform': 'string',
                'AvailabilityZone': 'string',
                'SlotDurationInHours': 123,
                'Recurrence': {
                    'Frequency': 'string',
                    'Interval': 123,
                    'OccurrenceDaySet': [
                        123,
                    ],
                    'OccurrenceRelativeToEnd': True|False,
                    'OccurrenceUnit': 'string'
                },
                'PreviousSlotEndTime': datetime(2015, 1, 1),
                'NextSlotStartTime': datetime(2015, 1, 1),
                'HourlyPrice': 'string',
                'TotalScheduledInstanceHours': 123,
                'InstanceCount': 123,
                'TermStartDate': datetime(2015, 1, 1),
                'TermEndDate': datetime(2015, 1, 1),
                'CreateDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def reboot_instances(DryRun=None, InstanceIds=None):
    """
    Requests a reboot of one or more instances. This operation is asynchronous; it only queues a request to reboot the specified instances. The operation succeeds if the instances are valid and belong to you. Requests to reboot terminated instances are ignored.
    If an instance does not cleanly shut down within four minutes, Amazon EC2 performs a hard reboot.
    For more information about troubleshooting, see Getting Console Output and Rebooting Instances in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_instances(
        DryRun=True|False,
        InstanceIds=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            

    """
    pass

def register_image(DryRun=None, ImageLocation=None, Name=None, Description=None, Architecture=None, KernelId=None, RamdiskId=None, BillingProducts=None, RootDeviceName=None, BlockDeviceMappings=None, VirtualizationType=None, SriovNetSupport=None, EnaSupport=None):
    """
    Registers an AMI. When you're creating an AMI, this is the final step you must complete before you can launch an instance from the AMI. For more information about creating AMIs, see Creating Your Own AMIs in the Amazon Elastic Compute Cloud User Guide .
    You can also use RegisterImage to create an Amazon EBS-backed Linux AMI from a snapshot of a root device volume. You specify the snapshot using the block device mapping. For more information, see Launching a Linux Instance from a Backup in the Amazon Elastic Compute Cloud User Guide .
    You can't register an image where a secondary (non-root) snapshot has AWS Marketplace product codes.
    Some Linux distributions, such as Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES), use the EC2 billing product code associated with an AMI to verify the subscription status for package updates. Creating an AMI from an EBS snapshot does not maintain this billing code, and subsequent instances launched from such an AMI will not be able to connect to package update infrastructure. To create an AMI that must retain billing codes, see  CreateImage .
    If needed, you can deregister an AMI at any time. Any modifications you make to an AMI backed by an instance store volume invalidates its registration. If you make changes to an image, deregister the previous image and register the new image.
    See also: AWS API Documentation
    
    
    :example: response = client.register_image(
        DryRun=True|False,
        ImageLocation='string',
        Name='string',
        Description='string',
        Architecture='i386'|'x86_64',
        KernelId='string',
        RamdiskId='string',
        BillingProducts=[
            'string',
        ],
        RootDeviceName='string',
        BlockDeviceMappings=[
            {
                'VirtualName': 'string',
                'DeviceName': 'string',
                'Ebs': {
                    'SnapshotId': 'string',
                    'VolumeSize': 123,
                    'DeleteOnTermination': True|False,
                    'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                    'Iops': 123,
                    'Encrypted': True|False
                },
                'NoDevice': 'string'
            },
        ],
        VirtualizationType='string',
        SriovNetSupport='string',
        EnaSupport=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImageLocation: string
    :param ImageLocation: The full path to your AMI manifest in Amazon S3 storage.

    :type Name: string
    :param Name: [REQUIRED]
            A name for your AMI.
            Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)
            

    :type Description: string
    :param Description: A description for your AMI.

    :type Architecture: string
    :param Architecture: The architecture of the AMI.
            Default: For Amazon EBS-backed AMIs, i386 . For instance store-backed AMIs, the architecture specified in the manifest file.
            

    :type KernelId: string
    :param KernelId: The ID of the kernel.

    :type RamdiskId: string
    :param RamdiskId: The ID of the RAM disk.

    :type BillingProducts: list
    :param BillingProducts: The billing product codes. Your account must be authorized to specify billing product codes. Otherwise, you can use the AWS Marketplace to bill for the use of an AMI.
            (string) --
            

    :type RootDeviceName: string
    :param RootDeviceName: The name of the root device (for example, /dev/sda1 , or /dev/xvda ).

    :type BlockDeviceMappings: list
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
            
            

    :type VirtualizationType: string
    :param VirtualizationType: The type of virtualization.
            Default: paravirtual
            

    :type SriovNetSupport: string
    :param SriovNetSupport: Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI.
            There is no way to disable sriovNetSupport at this time.
            This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.
            

    :type EnaSupport: boolean
    :param EnaSupport: Set to true to enable enhanced networking with ENA for the AMI and any instances that you launch from the AMI.
            This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.
            

    :rtype: dict
    :return: {
        'ImageId': 'string'
    }
    
    
    """
    pass

def reject_vpc_peering_connection(DryRun=None, VpcPeeringConnectionId=None):
    """
    Rejects a VPC peering connection request. The VPC peering connection must be in the pending-acceptance state. Use the  DescribeVpcPeeringConnections request to view your outstanding VPC peering connection requests. To delete an active VPC peering connection, or to delete a VPC peering connection request that you initiated, use  DeleteVpcPeeringConnection .
    See also: AWS API Documentation
    
    
    :example: response = client.reject_vpc_peering_connection(
        DryRun=True|False,
        VpcPeeringConnectionId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type VpcPeeringConnectionId: string
    :param VpcPeeringConnectionId: [REQUIRED]
            The ID of the VPC peering connection.
            

    :rtype: dict
    :return: {
        'Return': True|False
    }
    
    
    """
    pass

def release_address(DryRun=None, PublicIp=None, AllocationId=None):
    """
    Releases the specified Elastic IP address.
    After releasing an Elastic IP address, it is released to the IP address pool and might be unavailable to you. Be sure to update your DNS records and any servers or devices that communicate with the address. If you attempt to release an Elastic IP address that you already released, you'll get an AuthFailure error if the address is already allocated to another AWS account.
    [EC2-Classic, default VPC] Releasing an Elastic IP address automatically disassociates it from any instance that it's associated with. To disassociate an Elastic IP address without releasing it, use  DisassociateAddress .
    [Nondefault VPC] You must use  DisassociateAddress to disassociate the Elastic IP address before you try to release it. Otherwise, Amazon EC2 returns an error (InvalidIPAddress.InUse ).
    See also: AWS API Documentation
    
    Examples
    This example releases an Elastic IP address for use with instances in a VPC.
    Expected Output:
    This example releases an Elastic IP address for use with instances in EC2-Classic.
    Expected Output:
    
    :example: response = client.release_address(
        DryRun=True|False,
        PublicIp='string',
        AllocationId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type PublicIp: string
    :param PublicIp: [EC2-Classic] The Elastic IP address. Required for EC2-Classic.

    :type AllocationId: string
    :param AllocationId: [EC2-VPC] The allocation ID. Required for EC2-VPC.

    :return: response = client.release_address(
        AllocationId='eipalloc-64d5890a',
    )
    
    print(response)
    
    
    """
    pass

def release_hosts(HostIds=None):
    """
    When you no longer want to use an On-Demand Dedicated Host it can be released. On-Demand billing is stopped and the host goes into released state. The host ID of Dedicated Hosts that have been released can no longer be specified in another request, e.g., ModifyHosts. You must stop or terminate all instances on a host before it can be released.
    When Dedicated Hosts are released, it make take some time for them to stop counting toward your limit and you may receive capacity errors when trying to allocate new Dedicated hosts. Try waiting a few minutes, and then try again.
    Released hosts will still appear in a  DescribeHosts response.
    See also: AWS API Documentation
    
    
    :example: response = client.release_hosts(
        HostIds=[
            'string',
        ]
    )
    
    
    :type HostIds: list
    :param HostIds: [REQUIRED]
            The IDs of the Dedicated Hosts you want to release.
            (string) --
            

    :rtype: dict
    :return: {
        'Successful': [
            'string',
        ],
        'Unsuccessful': [
            {
                'ResourceId': 'string',
                'Error': {
                    'Code': 'string',
                    'Message': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def replace_iam_instance_profile_association(IamInstanceProfile=None, AssociationId=None):
    """
    Replaces an IAM instance profile for the specified running instance. You can use this action to change the IAM instance profile that's associated with an instance without having to disassociate the existing IAM instance profile first.
    Use  DescribeIamInstanceProfileAssociations to get the association ID.
    See also: AWS API Documentation
    
    
    :example: response = client.replace_iam_instance_profile_association(
        IamInstanceProfile={
            'Arn': 'string',
            'Name': 'string'
        },
        AssociationId='string'
    )
    
    
    :type IamInstanceProfile: dict
    :param IamInstanceProfile: [REQUIRED]
            The IAM instance profile.
            Arn (string) --The Amazon Resource Name (ARN) of the instance profile.
            Name (string) --The name of the instance profile.
            

    :type AssociationId: string
    :param AssociationId: [REQUIRED]
            The ID of the existing IAM instance profile association.
            

    :rtype: dict
    :return: {
        'IamInstanceProfileAssociation': {
            'AssociationId': 'string',
            'InstanceId': 'string',
            'IamInstanceProfile': {
                'Arn': 'string',
                'Id': 'string'
            },
            'State': 'associating'|'associated'|'disassociating'|'disassociated',
            'Timestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def replace_network_acl_association(DryRun=None, AssociationId=None, NetworkAclId=None):
    """
    Changes which network ACL a subnet is associated with. By default when you create a subnet, it's automatically associated with the default network ACL. For more information about network ACLs, see Network ACLs in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example associates the specified network ACL with the subnet for the specified network ACL association.
    Expected Output:
    
    :example: response = client.replace_network_acl_association(
        DryRun=True|False,
        AssociationId='string',
        NetworkAclId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type AssociationId: string
    :param AssociationId: [REQUIRED]
            The ID of the current association between the original network ACL and the subnet.
            

    :type NetworkAclId: string
    :param NetworkAclId: [REQUIRED]
            The ID of the new network ACL to associate with the subnet.
            

    :rtype: dict
    :return: {
        'NewAssociationId': 'string'
    }
    
    
    """
    pass

def replace_network_acl_entry(DryRun=None, NetworkAclId=None, RuleNumber=None, Protocol=None, RuleAction=None, Egress=None, CidrBlock=None, Ipv6CidrBlock=None, IcmpTypeCode=None, PortRange=None):
    """
    Replaces an entry (rule) in a network ACL. For more information about network ACLs, see Network ACLs in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example replaces an entry for the specified network ACL. The new rule 100 allows ingress traffic from 203.0.113.12/24 on UDP port 53 (DNS) into any associated subnet.
    Expected Output:
    
    :example: response = client.replace_network_acl_entry(
        DryRun=True|False,
        NetworkAclId='string',
        RuleNumber=123,
        Protocol='string',
        RuleAction='allow'|'deny',
        Egress=True|False,
        CidrBlock='string',
        Ipv6CidrBlock='string',
        IcmpTypeCode={
            'Type': 123,
            'Code': 123
        },
        PortRange={
            'From': 123,
            'To': 123
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkAclId: string
    :param NetworkAclId: [REQUIRED]
            The ID of the ACL.
            

    :type RuleNumber: integer
    :param RuleNumber: [REQUIRED]
            The rule number of the entry to replace.
            

    :type Protocol: string
    :param Protocol: [REQUIRED]
            The IP protocol. You can specify all or -1 to mean all protocols. If you specify all , -1 , or a protocol number other than tcp , udp , or icmp , traffic on all ports is allowed, regardless of any ports or ICMP types or codes you specify. If you specify protocol 58 (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol 58 (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.
            

    :type RuleAction: string
    :param RuleAction: [REQUIRED]
            Indicates whether to allow or deny the traffic that matches the rule.
            

    :type Egress: boolean
    :param Egress: [REQUIRED]
            Indicates whether to replace the egress rule.
            Default: If no value is specified, we replace the ingress rule.
            

    :type CidrBlock: string
    :param CidrBlock: The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).

    :type Ipv6CidrBlock: string
    :param Ipv6CidrBlock: The IPv6 network range to allow or deny, in CIDR notation (for example 2001:bd8:1234:1a00::/64 ).

    :type IcmpTypeCode: dict
    :param IcmpTypeCode: ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying the ICMP (1) protocol, or protocol 58 (ICMPv6) with an IPv6 CIDR block.
            Type (integer) --The ICMP type. A value of -1 means all types.
            Code (integer) --The ICMP code. A value of -1 means all codes for the specified ICMP type.
            

    :type PortRange: dict
    :param PortRange: TCP or UDP protocols: The range of ports the rule applies to. Required if specifying TCP (6) or UDP (17) for the protocol.
            From (integer) --The first port in the range.
            To (integer) --The last port in the range.
            

    :return: response = client.replace_network_acl_entry(
        CidrBlock='203.0.113.12/24',
        Egress=False,
        NetworkAclId='acl-5fb85d36',
        PortRange={
            'From': 53,
            'To': 53,
        },
        Protocol='udp',
        RuleAction='allow',
        RuleNumber=100,
    )
    
    print(response)
    
    
    """
    pass

def replace_route(DryRun=None, RouteTableId=None, DestinationCidrBlock=None, GatewayId=None, DestinationIpv6CidrBlock=None, EgressOnlyInternetGatewayId=None, InstanceId=None, NetworkInterfaceId=None, VpcPeeringConnectionId=None, NatGatewayId=None):
    """
    Replaces an existing route within a route table in a VPC. You must provide only one of the following: Internet gateway or virtual private gateway, NAT instance, NAT gateway, VPC peering connection, network interface, or egress-only Internet gateway.
    For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example replaces the specified route in the specified table table. The new route matches the specified CIDR and sends the traffic to the specified virtual private gateway.
    Expected Output:
    
    :example: response = client.replace_route(
        DryRun=True|False,
        RouteTableId='string',
        DestinationCidrBlock='string',
        GatewayId='string',
        DestinationIpv6CidrBlock='string',
        EgressOnlyInternetGatewayId='string',
        InstanceId='string',
        NetworkInterfaceId='string',
        VpcPeeringConnectionId='string',
        NatGatewayId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type RouteTableId: string
    :param RouteTableId: [REQUIRED]
            The ID of the route table.
            

    :type DestinationCidrBlock: string
    :param DestinationCidrBlock: The IPv4 CIDR address block used for the destination match. The value you provide must match the CIDR of an existing route in the table.

    :type GatewayId: string
    :param GatewayId: The ID of an Internet gateway or virtual private gateway.

    :type DestinationIpv6CidrBlock: string
    :param DestinationIpv6CidrBlock: The IPv6 CIDR address block used for the destination match. The value you provide must match the CIDR of an existing route in the table.

    :type EgressOnlyInternetGatewayId: string
    :param EgressOnlyInternetGatewayId: [IPv6 traffic only] The ID of an egress-only Internet gateway.

    :type InstanceId: string
    :param InstanceId: The ID of a NAT instance in your VPC.

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: The ID of a network interface.

    :type VpcPeeringConnectionId: string
    :param VpcPeeringConnectionId: The ID of a VPC peering connection.

    :type NatGatewayId: string
    :param NatGatewayId: [IPv4 traffic only] The ID of a NAT gateway.

    :return: response = client.replace_route(
        DestinationCidrBlock='10.0.0.0/16',
        GatewayId='vgw-9a4cacf3',
        RouteTableId='rtb-22574640',
    )
    
    print(response)
    
    
    """
    pass

def replace_route_table_association(DryRun=None, AssociationId=None, RouteTableId=None):
    """
    Changes the route table associated with a given subnet in a VPC. After the operation completes, the subnet uses the routes in the new route table it's associated with. For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide .
    You can also use ReplaceRouteTableAssociation to change which table is the main route table in the VPC. You just specify the main route table's association ID and the route table to be the new main route table.
    See also: AWS API Documentation
    
    Examples
    This example associates the specified route table with the subnet for the specified route table association.
    Expected Output:
    
    :example: response = client.replace_route_table_association(
        DryRun=True|False,
        AssociationId='string',
        RouteTableId='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type AssociationId: string
    :param AssociationId: [REQUIRED]
            The association ID.
            

    :type RouteTableId: string
    :param RouteTableId: [REQUIRED]
            The ID of the new route table to associate with the subnet.
            

    :rtype: dict
    :return: {
        'NewAssociationId': 'string'
    }
    
    
    """
    pass

def report_instance_status(DryRun=None, Instances=None, Status=None, StartTime=None, EndTime=None, ReasonCodes=None, Description=None):
    """
    Submits feedback about the status of an instance. The instance must be in the running state. If your experience with the instance differs from the instance status returned by  DescribeInstanceStatus , use  ReportInstanceStatus to report your experience with the instance. Amazon EC2 collects this information to improve the accuracy of status checks.
    Use of this action does not change the value returned by  DescribeInstanceStatus .
    See also: AWS API Documentation
    
    
    :example: response = client.report_instance_status(
        DryRun=True|False,
        Instances=[
            'string',
        ],
        Status='ok'|'impaired',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        ReasonCodes=[
            'instance-stuck-in-state'|'unresponsive'|'not-accepting-credentials'|'password-not-available'|'performance-network'|'performance-instance-store'|'performance-ebs-volume'|'performance-other'|'other',
        ],
        Description='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type Instances: list
    :param Instances: [REQUIRED]
            One or more instances.
            (string) --
            

    :type Status: string
    :param Status: [REQUIRED]
            The status of all instances listed.
            

    :type StartTime: datetime
    :param StartTime: The time at which the reported instance health state began.

    :type EndTime: datetime
    :param EndTime: The time at which the reported instance health state ended.

    :type ReasonCodes: list
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
            

    :type Description: string
    :param Description: Descriptive text about the health state of your instance.

    """
    pass

def request_spot_fleet(DryRun=None, SpotFleetRequestConfig=None):
    """
    Creates a Spot fleet request.
    You can submit a single request that includes multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet.
    By default, the Spot fleet requests Spot instances in the Spot pool where the price per unit is the lowest. Each launch specification can include its own instance weighting that reflects the value of the instance type to your application workload.
    Alternatively, you can specify that the Spot fleet distribute the target capacity across the Spot pools included in its launch specifications. By ensuring that the Spot instances in your Spot fleet are in different Spot pools, you can improve the availability of your fleet.
    For more information, see Spot Fleet Requests in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a Spot fleet request with two launch specifications that differ only by subnet. The Spot fleet launches the instances in the specified subnet with the lowest price. If the instances are launched in a default VPC, they receive a public IP address by default. If the instances are launched in a nondefault VPC, they do not receive a public IP address by default. Note that you can't specify different subnets from the same Availability Zone in a Spot fleet request.
    Expected Output:
    This example creates a Spot fleet request with two launch specifications that differ only by Availability Zone. The Spot fleet launches the instances in the specified Availability Zone with the lowest price. If your account supports EC2-VPC only, Amazon EC2 launches the Spot instances in the default subnet of the Availability Zone. If your account supports EC2-Classic, Amazon EC2 launches the instances in EC2-Classic in the Availability Zone.
    Expected Output:
    This example assigns public addresses to instances launched in a nondefault VPC. Note that when you specify a network interface, you must include the subnet ID and security group ID using the network interface.
    Expected Output:
    This example creates a Spot fleet request that launches 30 instances using the diversified allocation strategy. The launch specifications differ by instance type. The Spot fleet distributes the instances across the launch specifications such that there are 10 instances of each type.
    Expected Output:
    
    :example: response = client.request_spot_fleet(
        DryRun=True|False,
        SpotFleetRequestConfig={
            'ClientToken': 'string',
            'SpotPrice': 'string',
            'TargetCapacity': 123,
            'ValidFrom': datetime(2015, 1, 1),
            'ValidUntil': datetime(2015, 1, 1),
            'TerminateInstancesWithExpiration': True|False,
            'IamFleetRole': 'string',
            'LaunchSpecifications': [
                {
                    'ImageId': 'string',
                    'KeyName': 'string',
                    'SecurityGroups': [
                        {
                            'GroupName': 'string',
                            'GroupId': 'string'
                        },
                    ],
                    'UserData': 'string',
                    'AddressingType': 'string',
                    'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'GroupName': 'string',
                        'Tenancy': 'default'|'dedicated'|'host'
                    },
                    'KernelId': 'string',
                    'RamdiskId': 'string',
                    'BlockDeviceMappings': [
                        {
                            'VirtualName': 'string',
                            'DeviceName': 'string',
                            'Ebs': {
                                'SnapshotId': 'string',
                                'VolumeSize': 123,
                                'DeleteOnTermination': True|False,
                                'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                                'Iops': 123,
                                'Encrypted': True|False
                            },
                            'NoDevice': 'string'
                        },
                    ],
                    'Monitoring': {
                        'Enabled': True|False
                    },
                    'SubnetId': 'string',
                    'NetworkInterfaces': [
                        {
                            'NetworkInterfaceId': 'string',
                            'DeviceIndex': 123,
                            'SubnetId': 'string',
                            'Description': 'string',
                            'PrivateIpAddress': 'string',
                            'Groups': [
                                'string',
                            ],
                            'DeleteOnTermination': True|False,
                            'PrivateIpAddresses': [
                                {
                                    'PrivateIpAddress': 'string',
                                    'Primary': True|False
                                },
                            ],
                            'SecondaryPrivateIpAddressCount': 123,
                            'AssociatePublicIpAddress': True|False,
                            'Ipv6Addresses': [
                                {
                                    'Ipv6Address': 'string'
                                },
                            ],
                            'Ipv6AddressCount': 123
                        },
                    ],
                    'IamInstanceProfile': {
                        'Arn': 'string',
                        'Name': 'string'
                    },
                    'EbsOptimized': True|False,
                    'WeightedCapacity': 123.0,
                    'SpotPrice': 'string'
                },
            ],
            'ExcessCapacityTerminationPolicy': 'noTermination'|'default',
            'AllocationStrategy': 'lowestPrice'|'diversified',
            'FulfilledCapacity': 123.0,
            'Type': 'request'|'maintain',
            'ReplaceUnhealthyInstances': True|False
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SpotFleetRequestConfig: dict
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
            InstanceType (string) --The instance type. Note that T2 and HS1 instance types are not supported.
            Placement (dict) --The placement information.
            AvailabilityZone (string) --The Availability Zone.
            [Spot fleet only] To specify multiple Availability Zones, separate them using commas; for example, 'us-west-2a, us-west-2b'.
            GroupName (string) --The name of the placement group (for cluster instances).
            Tenancy (string) --The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for Spot instances.
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
            NetworkInterfaces (list) --One or more network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface.
            (dict) --Describes a network interface.
            NetworkInterfaceId (string) --The ID of the network interface.
            DeviceIndex (integer) --The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a RunInstances request, you must provide the device index.
            SubnetId (string) --The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
            Description (string) --The description of the network interface. Applies only if creating a network interface when launching an instance.
            PrivateIpAddress (string) --The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            Groups (list) --The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
            (string) --
            DeleteOnTermination (boolean) --If set to true , the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.
            PrivateIpAddresses (list) --One or more private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            (dict) --Describes a secondary private IPv4 address for a network interface.
            PrivateIpAddress (string) -- [REQUIRED]The private IPv4 addresses.
            Primary (boolean) --Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
            
            SecondaryPrivateIpAddressCount (integer) --The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            AssociatePublicIpAddress (boolean) --Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .
            Ipv6Addresses (list) --One or more IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
            (dict) --Describes an IPv6 address.
            Ipv6Address (string) --The IPv6 address.
            
            Ipv6AddressCount (integer) --A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.
            
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
            ReplaceUnhealthyInstances (boolean) --Indicates whether Spot fleet should replace unhealthy instances.
            

    :rtype: dict
    :return: {
        'SpotFleetRequestId': 'string'
    }
    
    
    """
    pass

def request_spot_instances(DryRun=None, SpotPrice=None, ClientToken=None, InstanceCount=None, Type=None, ValidFrom=None, ValidUntil=None, LaunchGroup=None, AvailabilityZoneGroup=None, BlockDurationMinutes=None, LaunchSpecification=None):
    """
    Creates a Spot instance request. Spot instances are instances that Amazon EC2 launches when the bid price that you specify exceeds the current Spot price. Amazon EC2 periodically sets the Spot price based on available Spot Instance capacity and current Spot instance requests. For more information, see Spot Instance Requests in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a one-time Spot Instance request for five instances in the specified Availability Zone. If your account supports EC2-VPC only, Amazon EC2 launches the instances in the default subnet of the specified Availability Zone. If your account supports EC2-Classic, Amazon EC2 launches the instances in EC2-Classic in the specified Availability Zone.
    Expected Output:
    This example command creates a one-time Spot Instance request for five instances in the specified subnet. Amazon EC2 launches the instances in the specified subnet. If the VPC is a nondefault VPC, the instances do not receive a public IP address by default.
    Expected Output:
    
    :example: response = client.request_spot_instances(
        DryRun=True|False,
        SpotPrice='string',
        ClientToken='string',
        InstanceCount=123,
        Type='one-time'|'persistent',
        ValidFrom=datetime(2015, 1, 1),
        ValidUntil=datetime(2015, 1, 1),
        LaunchGroup='string',
        AvailabilityZoneGroup='string',
        BlockDurationMinutes=123,
        LaunchSpecification={
            'ImageId': 'string',
            'KeyName': 'string',
            'SecurityGroups': [
                'string',
            ],
            'UserData': 'string',
            'AddressingType': 'string',
            'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
            'Placement': {
                'AvailabilityZone': 'string',
                'GroupName': 'string',
                'Tenancy': 'default'|'dedicated'|'host'
            },
            'KernelId': 'string',
            'RamdiskId': 'string',
            'BlockDeviceMappings': [
                {
                    'VirtualName': 'string',
                    'DeviceName': 'string',
                    'Ebs': {
                        'SnapshotId': 'string',
                        'VolumeSize': 123,
                        'DeleteOnTermination': True|False,
                        'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                        'Iops': 123,
                        'Encrypted': True|False
                    },
                    'NoDevice': 'string'
                },
            ],
            'SubnetId': 'string',
            'NetworkInterfaces': [
                {
                    'NetworkInterfaceId': 'string',
                    'DeviceIndex': 123,
                    'SubnetId': 'string',
                    'Description': 'string',
                    'PrivateIpAddress': 'string',
                    'Groups': [
                        'string',
                    ],
                    'DeleteOnTermination': True|False,
                    'PrivateIpAddresses': [
                        {
                            'PrivateIpAddress': 'string',
                            'Primary': True|False
                        },
                    ],
                    'SecondaryPrivateIpAddressCount': 123,
                    'AssociatePublicIpAddress': True|False,
                    'Ipv6Addresses': [
                        {
                            'Ipv6Address': 'string'
                        },
                    ],
                    'Ipv6AddressCount': 123
                },
            ],
            'IamInstanceProfile': {
                'Arn': 'string',
                'Name': 'string'
            },
            'EbsOptimized': True|False,
            'Monitoring': {
                'Enabled': True|False
            },
            'SecurityGroupIds': [
                'string',
            ]
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SpotPrice: string
    :param SpotPrice: [REQUIRED]
            The maximum hourly price (bid) for any Spot instance launched to fulfill the request.
            

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide .

    :type InstanceCount: integer
    :param InstanceCount: The maximum number of Spot instances to launch.
            Default: 1
            

    :type Type: string
    :param Type: The Spot instance request type.
            Default: one-time
            

    :type ValidFrom: datetime
    :param ValidFrom: The start date of the request. If this is a one-time request, the request becomes active at this date and time and remains active until all instances launch, the request expires, or the request is canceled. If the request is persistent, the request becomes active at this date and time and remains active until it expires or is canceled.
            Default: The request is effective indefinitely.
            

    :type ValidUntil: datetime
    :param ValidUntil: The end date of the request. If this is a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached.
            Default: The request is effective indefinitely.
            

    :type LaunchGroup: string
    :param LaunchGroup: The instance launch group. Launch groups are Spot instances that launch together and terminate together.
            Default: Instances are launched and terminated individually
            

    :type AvailabilityZoneGroup: string
    :param AvailabilityZoneGroup: The user-specified name for a logical grouping of bids.
            When you specify an Availability Zone group in a Spot Instance request, all Spot instances in the request are launched in the same Availability Zone. Instance proximity is maintained with this parameter, but the choice of Availability Zone is not. The group applies only to bids for Spot Instances of the same instance type. Any additional Spot instance requests that are specified with the same Availability Zone group name are launched in that same Availability Zone, as long as at least one instance from the group is still active.
            If there is no active instance running in the Availability Zone group that you specify for a new Spot instance request (all instances are terminated, the bid is expired, or the bid falls below current market), then Amazon EC2 launches the instance in any Availability Zone where the constraint can be met. Consequently, the subsequent set of Spot instances could be placed in a different zone from the original request, even if you specified the same Availability Zone group.
            Default: Instances are launched in any available Availability Zone.
            

    :type BlockDurationMinutes: integer
    :param BlockDurationMinutes: The required duration for the Spot instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).
            The duration period starts as soon as your Spot instance receives its instance ID. At the end of the duration period, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.
            Note that you can't specify an Availability Zone group or a launch group if you specify a duration.
            

    :type LaunchSpecification: dict
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
            Tenancy (string) --The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for Spot instances.
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
            NetworkInterfaces (list) --One or more network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface.
            (dict) --Describes a network interface.
            NetworkInterfaceId (string) --The ID of the network interface.
            DeviceIndex (integer) --The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a RunInstances request, you must provide the device index.
            SubnetId (string) --The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
            Description (string) --The description of the network interface. Applies only if creating a network interface when launching an instance.
            PrivateIpAddress (string) --The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            Groups (list) --The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
            (string) --
            DeleteOnTermination (boolean) --If set to true , the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.
            PrivateIpAddresses (list) --One or more private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            (dict) --Describes a secondary private IPv4 address for a network interface.
            PrivateIpAddress (string) -- [REQUIRED]The private IPv4 addresses.
            Primary (boolean) --Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
            
            SecondaryPrivateIpAddressCount (integer) --The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            AssociatePublicIpAddress (boolean) --Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .
            Ipv6Addresses (list) --One or more IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
            (dict) --Describes an IPv6 address.
            Ipv6Address (string) --The IPv6 address.
            
            Ipv6AddressCount (integer) --A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.
            
            IamInstanceProfile (dict) --The IAM instance profile.
            Arn (string) --The Amazon Resource Name (ARN) of the instance profile.
            Name (string) --The name of the instance profile.
            EbsOptimized (boolean) --Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.
            Default: false
            Monitoring (dict) --Describes the monitoring of an instance.
            Enabled (boolean) -- [REQUIRED]Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
            SecurityGroupIds (list) --
            (string) --
            

    :rtype: dict
    :return: {
        'SpotInstanceRequests': [
            {
                'SpotInstanceRequestId': 'string',
                'SpotPrice': 'string',
                'Type': 'one-time'|'persistent',
                'State': 'open'|'active'|'closed'|'cancelled'|'failed',
                'Fault': {
                    'Code': 'string',
                    'Message': 'string'
                },
                'Status': {
                    'Code': 'string',
                    'UpdateTime': datetime(2015, 1, 1),
                    'Message': 'string'
                },
                'ValidFrom': datetime(2015, 1, 1),
                'ValidUntil': datetime(2015, 1, 1),
                'LaunchGroup': 'string',
                'AvailabilityZoneGroup': 'string',
                'LaunchSpecification': {
                    'ImageId': 'string',
                    'KeyName': 'string',
                    'SecurityGroups': [
                        {
                            'GroupName': 'string',
                            'GroupId': 'string'
                        },
                    ],
                    'UserData': 'string',
                    'AddressingType': 'string',
                    'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'GroupName': 'string',
                        'Tenancy': 'default'|'dedicated'|'host'
                    },
                    'KernelId': 'string',
                    'RamdiskId': 'string',
                    'BlockDeviceMappings': [
                        {
                            'VirtualName': 'string',
                            'DeviceName': 'string',
                            'Ebs': {
                                'SnapshotId': 'string',
                                'VolumeSize': 123,
                                'DeleteOnTermination': True|False,
                                'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                                'Iops': 123,
                                'Encrypted': True|False
                            },
                            'NoDevice': 'string'
                        },
                    ],
                    'SubnetId': 'string',
                    'NetworkInterfaces': [
                        {
                            'NetworkInterfaceId': 'string',
                            'DeviceIndex': 123,
                            'SubnetId': 'string',
                            'Description': 'string',
                            'PrivateIpAddress': 'string',
                            'Groups': [
                                'string',
                            ],
                            'DeleteOnTermination': True|False,
                            'PrivateIpAddresses': [
                                {
                                    'PrivateIpAddress': 'string',
                                    'Primary': True|False
                                },
                            ],
                            'SecondaryPrivateIpAddressCount': 123,
                            'AssociatePublicIpAddress': True|False,
                            'Ipv6Addresses': [
                                {
                                    'Ipv6Address': 'string'
                                },
                            ],
                            'Ipv6AddressCount': 123
                        },
                    ],
                    'IamInstanceProfile': {
                        'Arn': 'string',
                        'Name': 'string'
                    },
                    'EbsOptimized': True|False,
                    'Monitoring': {
                        'Enabled': True|False
                    }
                },
                'InstanceId': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'ProductDescription': 'Linux/UNIX'|'Linux/UNIX (Amazon VPC)'|'Windows'|'Windows (Amazon VPC)',
                'BlockDurationMinutes': 123,
                'ActualBlockHourlyPrice': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'LaunchedAvailabilityZone': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def reset_image_attribute(DryRun=None, ImageId=None, Attribute=None):
    """
    Resets an attribute of an AMI to its default value.
    See also: AWS API Documentation
    
    
    :example: response = client.reset_image_attribute(
        DryRun=True|False,
        ImageId='string',
        Attribute='launchPermission'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImageId: string
    :param ImageId: [REQUIRED]
            The ID of the AMI.
            

    :type Attribute: string
    :param Attribute: [REQUIRED]
            The attribute to reset (currently you can only reset the launch permission attribute).
            

    """
    pass

def reset_instance_attribute(DryRun=None, InstanceId=None, Attribute=None):
    """
    Resets an attribute of an instance to its default value. To reset the kernel or ramdisk , the instance must be in a stopped state. To reset the sourceDestCheck , the instance can be either running or stopped.
    The sourceDestCheck attribute controls whether source/destination checking is enabled. The default value is true , which means checking is enabled. This value must be false for a NAT instance to perform NAT. For more information, see NAT Instances in the Amazon Virtual Private Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.reset_instance_attribute(
        DryRun=True|False,
        InstanceId='string',
        Attribute='instanceType'|'kernel'|'ramdisk'|'userData'|'disableApiTermination'|'instanceInitiatedShutdownBehavior'|'rootDeviceName'|'blockDeviceMapping'|'productCodes'|'sourceDestCheck'|'groupSet'|'ebsOptimized'|'sriovNetSupport'|'enaSupport'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type Attribute: string
    :param Attribute: [REQUIRED]
            The attribute to reset.
            Warning
            You can only reset the following attributes: kernel | ramdisk | sourceDestCheck . To change an instance attribute, use ModifyInstanceAttribute .
            

    """
    pass

def reset_network_interface_attribute(DryRun=None, NetworkInterfaceId=None, SourceDestCheck=None):
    """
    Resets a network interface attribute. You can specify only one attribute at a time.
    See also: AWS API Documentation
    
    
    :example: response = client.reset_network_interface_attribute(
        DryRun=True|False,
        NetworkInterfaceId='string',
        SourceDestCheck='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            

    :type SourceDestCheck: string
    :param SourceDestCheck: The source/destination checking attribute. Resets the value to true .

    """
    pass

def reset_snapshot_attribute(DryRun=None, SnapshotId=None, Attribute=None):
    """
    Resets permission settings for the specified snapshot.
    For more information on modifying snapshot permissions, see Sharing Snapshots in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example resets the create volume permissions for snapshot snap-1234567890abcdef0. If the command succeeds, no output is returned.
    Expected Output:
    
    :example: response = client.reset_snapshot_attribute(
        DryRun=True|False,
        SnapshotId='string',
        Attribute='productCodes'|'createVolumePermission'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]
            The ID of the snapshot.
            

    :type Attribute: string
    :param Attribute: [REQUIRED]
            The attribute to reset. Currently, only the attribute for permission to create volumes can be reset.
            

    :return: response = client.reset_snapshot_attribute(
        Attribute='createVolumePermission',
        SnapshotId='snap-1234567890abcdef0',
    )
    
    print(response)
    
    
    """
    pass

def restore_address_to_classic(DryRun=None, PublicIp=None):
    """
    Restores an Elastic IP address that was previously moved to the EC2-VPC platform back to the EC2-Classic platform. You cannot move an Elastic IP address that was originally allocated for use in EC2-VPC. The Elastic IP address must not be associated with an instance or network interface.
    See also: AWS API Documentation
    
    Examples
    This example restores the specified Elastic IP address to the EC2-Classic platform.
    Expected Output:
    
    :example: response = client.restore_address_to_classic(
        DryRun=True|False,
        PublicIp='string'
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type PublicIp: string
    :param PublicIp: [REQUIRED]
            The Elastic IP address.
            

    :rtype: dict
    :return: {
        'Status': 'MoveInProgress'|'InVpc'|'InClassic',
        'PublicIp': 'string'
    }
    
    
    """
    pass

def revoke_security_group_egress(DryRun=None, GroupId=None, SourceSecurityGroupName=None, SourceSecurityGroupOwnerId=None, IpProtocol=None, FromPort=None, ToPort=None, CidrIp=None, IpPermissions=None):
    """
    [EC2-VPC only] Removes one or more egress rules from a security group for EC2-VPC. This action doesn't apply to security groups for use in EC2-Classic. The values that you specify in the revoke request (for example, ports) must match the existing rule's values for the rule to be revoked.
    Each rule consists of the protocol and the IPv4 or IPv6 CIDR range or source security group. For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code.
    Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.
    See also: AWS API Documentation
    
    
    :example: response = client.revoke_security_group_egress(
        DryRun=True|False,
        GroupId='string',
        SourceSecurityGroupName='string',
        SourceSecurityGroupOwnerId='string',
        IpProtocol='string',
        FromPort=123,
        ToPort=123,
        CidrIp='string',
        IpPermissions=[
            {
                'IpProtocol': 'string',
                'FromPort': 123,
                'ToPort': 123,
                'UserIdGroupPairs': [
                    {
                        'UserId': 'string',
                        'GroupName': 'string',
                        'GroupId': 'string',
                        'VpcId': 'string',
                        'VpcPeeringConnectionId': 'string',
                        'PeeringStatus': 'string'
                    },
                ],
                'IpRanges': [
                    {
                        'CidrIp': 'string'
                    },
                ],
                'Ipv6Ranges': [
                    {
                        'CidrIpv6': 'string'
                    },
                ],
                'PrefixListIds': [
                    {
                        'PrefixListId': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupId: string
    :param GroupId: [REQUIRED]
            The ID of the security group.
            

    :type SourceSecurityGroupName: string
    :param SourceSecurityGroupName: The name of a destination security group. To revoke outbound access to a destination security group, we recommend that you use a set of IP permissions instead.

    :type SourceSecurityGroupOwnerId: string
    :param SourceSecurityGroupOwnerId: The AWS account number for a destination security group. To revoke outbound access to a destination security group, we recommend that you use a set of IP permissions instead.

    :type IpProtocol: string
    :param IpProtocol: The IP protocol name or number. We recommend that you specify the protocol in a set of IP permissions instead.

    :type FromPort: integer
    :param FromPort: The start of port range for the TCP and UDP protocols, or an ICMP type number. We recommend that you specify the port range in a set of IP permissions instead.

    :type ToPort: integer
    :param ToPort: The end of port range for the TCP and UDP protocols, or an ICMP type number. We recommend that you specify the port range in a set of IP permissions instead.

    :type CidrIp: string
    :param CidrIp: The CIDR IP address range. We recommend that you specify the CIDR range in a set of IP permissions instead.

    :type IpPermissions: list
    :param IpPermissions: A set of IP permissions. You can't specify a destination security group and a CIDR IP address range.
            (dict) --Describes a security group rule.
            IpProtocol (string) --The IP protocol name (tcp , udp , icmp ) or number (see Protocol Numbers ).
            [EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp , udp , icmp , or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp , udp , and icmp , you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules.
            FromPort (integer) --The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types.
            ToPort (integer) --The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type.
            UserIdGroupPairs (list) --One or more security group and AWS account ID pairs.
            (dict) --Describes a security group and AWS account ID pair.
            UserId (string) --The ID of an AWS account. For a referenced security group in another VPC, the account ID of the referenced security group is returned.
            [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
            GroupName (string) --The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.
            GroupId (string) --The ID of the security group.
            VpcId (string) --The ID of the VPC for the referenced security group, if applicable.
            VpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.
            PeeringStatus (string) --The status of a VPC peering connection, if applicable.
            
            IpRanges (list) --One or more IPv4 ranges.
            (dict) --Describes an IPv4 range.
            CidrIp (string) --The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix.
            
            Ipv6Ranges (list) --[EC2-VPC only] One or more IPv6 ranges.
            (dict) --[EC2-VPC only] Describes an IPv6 range.
            CidrIpv6 (string) --The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix.
            
            PrefixListIds (list) --(Valid for AuthorizeSecurityGroupEgress , RevokeSecurityGroupEgress and DescribeSecurityGroups only) One or more prefix list IDs for an AWS service. In an AuthorizeSecurityGroupEgress request, this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
            (dict) --The ID of the prefix.
            PrefixListId (string) --The ID of the prefix.
            
            
            

    """
    pass

def revoke_security_group_ingress(DryRun=None, GroupName=None, GroupId=None, SourceSecurityGroupName=None, SourceSecurityGroupOwnerId=None, IpProtocol=None, FromPort=None, ToPort=None, CidrIp=None, IpPermissions=None):
    """
    Removes one or more ingress rules from a security group. The values that you specify in the revoke request (for example, ports) must match the existing rule's values for the rule to be removed.
    Each rule consists of the protocol and the CIDR range or source security group. For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code.
    Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.
    See also: AWS API Documentation
    
    
    :example: response = client.revoke_security_group_ingress(
        DryRun=True|False,
        GroupName='string',
        GroupId='string',
        SourceSecurityGroupName='string',
        SourceSecurityGroupOwnerId='string',
        IpProtocol='string',
        FromPort=123,
        ToPort=123,
        CidrIp='string',
        IpPermissions=[
            {
                'IpProtocol': 'string',
                'FromPort': 123,
                'ToPort': 123,
                'UserIdGroupPairs': [
                    {
                        'UserId': 'string',
                        'GroupName': 'string',
                        'GroupId': 'string',
                        'VpcId': 'string',
                        'VpcPeeringConnectionId': 'string',
                        'PeeringStatus': 'string'
                    },
                ],
                'IpRanges': [
                    {
                        'CidrIp': 'string'
                    },
                ],
                'Ipv6Ranges': [
                    {
                        'CidrIpv6': 'string'
                    },
                ],
                'PrefixListIds': [
                    {
                        'PrefixListId': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type GroupName: string
    :param GroupName: [EC2-Classic, default VPC] The name of the security group.

    :type GroupId: string
    :param GroupId: The ID of the security group. Required for a security group in a nondefault VPC.

    :type SourceSecurityGroupName: string
    :param SourceSecurityGroupName: [EC2-Classic, default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. For EC2-VPC, the source security group must be in the same VPC. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.

    :type SourceSecurityGroupOwnerId: string
    :param SourceSecurityGroupOwnerId: [EC2-Classic] The AWS account ID of the source security group, if the source security group is in a different account. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.

    :type IpProtocol: string
    :param IpProtocol: The IP protocol name (tcp , udp , icmp ) or number (see Protocol Numbers ). Use -1 to specify all.

    :type FromPort: integer
    :param FromPort: The start of port range for the TCP and UDP protocols, or an ICMP type number. For the ICMP type number, use -1 to specify all ICMP types.

    :type ToPort: integer
    :param ToPort: The end of port range for the TCP and UDP protocols, or an ICMP code number. For the ICMP code number, use -1 to specify all ICMP codes for the ICMP type.

    :type CidrIp: string
    :param CidrIp: The CIDR IP address range. You can't specify this parameter when specifying a source security group.

    :type IpPermissions: list
    :param IpPermissions: A set of IP permissions. You can't specify a source security group and a CIDR IP address range.
            (dict) --Describes a security group rule.
            IpProtocol (string) --The IP protocol name (tcp , udp , icmp ) or number (see Protocol Numbers ).
            [EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp , udp , icmp , or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp , udp , and icmp , you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules.
            FromPort (integer) --The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types.
            ToPort (integer) --The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type.
            UserIdGroupPairs (list) --One or more security group and AWS account ID pairs.
            (dict) --Describes a security group and AWS account ID pair.
            UserId (string) --The ID of an AWS account. For a referenced security group in another VPC, the account ID of the referenced security group is returned.
            [EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account.
            GroupName (string) --The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.
            GroupId (string) --The ID of the security group.
            VpcId (string) --The ID of the VPC for the referenced security group, if applicable.
            VpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.
            PeeringStatus (string) --The status of a VPC peering connection, if applicable.
            
            IpRanges (list) --One or more IPv4 ranges.
            (dict) --Describes an IPv4 range.
            CidrIp (string) --The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix.
            
            Ipv6Ranges (list) --[EC2-VPC only] One or more IPv6 ranges.
            (dict) --[EC2-VPC only] Describes an IPv6 range.
            CidrIpv6 (string) --The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix.
            
            PrefixListIds (list) --(Valid for AuthorizeSecurityGroupEgress , RevokeSecurityGroupEgress and DescribeSecurityGroups only) One or more prefix list IDs for an AWS service. In an AuthorizeSecurityGroupEgress request, this is the AWS service that you want to access through a VPC endpoint from instances associated with the security group.
            (dict) --The ID of the prefix.
            PrefixListId (string) --The ID of the prefix.
            
            
            

    """
    pass

def run_instances(DryRun=None, ImageId=None, MinCount=None, MaxCount=None, KeyName=None, SecurityGroups=None, SecurityGroupIds=None, UserData=None, InstanceType=None, Placement=None, KernelId=None, RamdiskId=None, BlockDeviceMappings=None, Monitoring=None, SubnetId=None, DisableApiTermination=None, InstanceInitiatedShutdownBehavior=None, PrivateIpAddress=None, Ipv6Addresses=None, Ipv6AddressCount=None, ClientToken=None, AdditionalInfo=None, NetworkInterfaces=None, IamInstanceProfile=None, EbsOptimized=None, TagSpecifications=None):
    """
    Launches the specified number of instances using an AMI for which you have permissions.
    You can specify a number of options, or leave the default options. The following rules apply:
    To ensure faster instance launches, break up large requests into smaller batches. For example, create 5 separate launch requests for 100 instances each instead of 1 launch request for 500 instances.
    An instance is ready for you to use when it's in the running state. You can check the state of your instance using  DescribeInstances . You can tag instances and EBS volumes during launch, after launch, or both. For more information, see  CreateTags and Tagging Your Amazon EC2 Resources .
    Linux instances have access to the public key of the key pair at boot. You can use this key to provide secure access to the instance. Amazon EC2 public images use this feature to provide secure access without passwords. For more information, see Key Pairs in the Amazon Elastic Compute Cloud User Guide .
    For troubleshooting, see What To Do If An Instance Immediately Terminates , and Troubleshooting Connecting to Your Instance in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.run_instances(
        DryRun=True|False,
        ImageId='string',
        MinCount=123,
        MaxCount=123,
        KeyName='string',
        SecurityGroups=[
            'string',
        ],
        SecurityGroupIds=[
            'string',
        ],
        UserData='string',
        InstanceType='t1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
        Placement={
            'AvailabilityZone': 'string',
            'GroupName': 'string',
            'Tenancy': 'default'|'dedicated'|'host',
            'HostId': 'string',
            'Affinity': 'string'
        },
        KernelId='string',
        RamdiskId='string',
        BlockDeviceMappings=[
            {
                'VirtualName': 'string',
                'DeviceName': 'string',
                'Ebs': {
                    'SnapshotId': 'string',
                    'VolumeSize': 123,
                    'DeleteOnTermination': True|False,
                    'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                    'Iops': 123,
                    'Encrypted': True|False
                },
                'NoDevice': 'string'
            },
        ],
        Monitoring={
            'Enabled': True|False
        },
        SubnetId='string',
        DisableApiTermination=True|False,
        InstanceInitiatedShutdownBehavior='stop'|'terminate',
        PrivateIpAddress='string',
        Ipv6Addresses=[
            {
                'Ipv6Address': 'string'
            },
        ],
        Ipv6AddressCount=123,
        ClientToken='string',
        AdditionalInfo='string',
        NetworkInterfaces=[
            {
                'NetworkInterfaceId': 'string',
                'DeviceIndex': 123,
                'SubnetId': 'string',
                'Description': 'string',
                'PrivateIpAddress': 'string',
                'Groups': [
                    'string',
                ],
                'DeleteOnTermination': True|False,
                'PrivateIpAddresses': [
                    {
                        'PrivateIpAddress': 'string',
                        'Primary': True|False
                    },
                ],
                'SecondaryPrivateIpAddressCount': 123,
                'AssociatePublicIpAddress': True|False,
                'Ipv6Addresses': [
                    {
                        'Ipv6Address': 'string'
                    },
                ],
                'Ipv6AddressCount': 123
            },
        ],
        IamInstanceProfile={
            'Arn': 'string',
            'Name': 'string'
        },
        EbsOptimized=True|False,
        TagSpecifications=[
            {
                'ResourceType': 'customer-gateway'|'dhcp-options'|'image'|'instance'|'internet-gateway'|'network-acl'|'network-interface'|'reserved-instances'|'route-table'|'snapshot'|'spot-instances-request'|'subnet'|'security-group'|'volume'|'vpc'|'vpn-connection'|'vpn-gateway',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ImageId: string
    :param ImageId: [REQUIRED]
            The ID of the AMI, which you can get by calling DescribeImages .
            

    :type MinCount: integer
    :param MinCount: [REQUIRED]
            The minimum number of instances to launch. If you specify a minimum that is more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches no instances.
            Constraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 General FAQ.
            

    :type MaxCount: integer
    :param MaxCount: [REQUIRED]
            The maximum number of instances to launch. If you specify more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches the largest possible number of instances above MinCount .
            Constraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 FAQ.
            

    :type KeyName: string
    :param KeyName: The name of the key pair. You can create a key pair using CreateKeyPair or ImportKeyPair .
            Warning
            If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.
            

    :type SecurityGroups: list
    :param SecurityGroups: [EC2-Classic, default VPC] One or more security group names. For a nondefault VPC, you must use security group IDs instead.
            Default: Amazon EC2 uses the default security group.
            (string) --
            

    :type SecurityGroupIds: list
    :param SecurityGroupIds: One or more security group IDs. You can create a security group using CreateSecurityGroup .
            Default: Amazon EC2 uses the default security group.
            (string) --
            

    :type UserData: string
    :param UserData: The user data to make available to the instance. For more information, see Running Commands on Your Linux Instance at Launch (Linux) and Adding User Data (Windows). If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.
            This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.
            

    :type InstanceType: string
    :param InstanceType: The instance type. For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide .
            Default: m1.small
            

    :type Placement: dict
    :param Placement: The placement for the instance.
            AvailabilityZone (string) --The Availability Zone of the instance.
            GroupName (string) --The name of the placement group the instance is in (for cluster compute instances).
            Tenancy (string) --The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the ImportInstance command.
            HostId (string) --The ID of the Dedicated Host on which the instance resides. This parameter is not supported for the ImportInstance command.
            Affinity (string) --The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the ImportInstance command.
            

    :type KernelId: string
    :param KernelId: The ID of the kernel.
            Warning
            We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB in the Amazon Elastic Compute Cloud User Guide .
            

    :type RamdiskId: string
    :param RamdiskId: The ID of the RAM disk.
            Warning
            We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB in the Amazon Elastic Compute Cloud User Guide .
            

    :type BlockDeviceMappings: list
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
            
            

    :type Monitoring: dict
    :param Monitoring: The monitoring for the instance.
            Enabled (boolean) -- [REQUIRED]Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
            

    :type SubnetId: string
    :param SubnetId: [EC2-VPC] The ID of the subnet to launch the instance into.

    :type DisableApiTermination: boolean
    :param DisableApiTermination: If you set this parameter to true , you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. To change this attribute to false after launch, use ModifyInstanceAttribute . Alternatively, if you set InstanceInitiatedShutdownBehavior to terminate , you can terminate the instance by running the shutdown command from the instance.
            Default: false
            

    :type InstanceInitiatedShutdownBehavior: string
    :param InstanceInitiatedShutdownBehavior: Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
            Default: stop
            

    :type PrivateIpAddress: string
    :param PrivateIpAddress: [EC2-VPC] The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.
            Only one private IP address can be designated as primary. You can't specify this option if you've specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if you're launching more than one instance in the request.
            

    :type Ipv6Addresses: list
    :param Ipv6Addresses: [EC2-VPC] Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
            (dict) --Describes an IPv6 address.
            Ipv6Address (string) --The IPv6 address.
            
            

    :type Ipv6AddressCount: integer
    :param Ipv6AddressCount: [EC2-VPC] A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency .
            Constraints: Maximum 64 ASCII characters
            

    :type AdditionalInfo: string
    :param AdditionalInfo: Reserved.

    :type NetworkInterfaces: list
    :param NetworkInterfaces: One or more network interfaces.
            (dict) --Describes a network interface.
            NetworkInterfaceId (string) --The ID of the network interface.
            DeviceIndex (integer) --The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a RunInstances request, you must provide the device index.
            SubnetId (string) --The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
            Description (string) --The description of the network interface. Applies only if creating a network interface when launching an instance.
            PrivateIpAddress (string) --The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            Groups (list) --The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
            (string) --
            DeleteOnTermination (boolean) --If set to true , the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.
            PrivateIpAddresses (list) --One or more private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            (dict) --Describes a secondary private IPv4 address for a network interface.
            PrivateIpAddress (string) -- [REQUIRED]The private IPv4 addresses.
            Primary (boolean) --Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
            
            SecondaryPrivateIpAddressCount (integer) --The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.
            AssociatePublicIpAddress (boolean) --Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .
            Ipv6Addresses (list) --One or more IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
            (dict) --Describes an IPv6 address.
            Ipv6Address (string) --The IPv6 address.
            
            Ipv6AddressCount (integer) --A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.
            
            

    :type IamInstanceProfile: dict
    :param IamInstanceProfile: The IAM instance profile.
            Arn (string) --The Amazon Resource Name (ARN) of the instance profile.
            Name (string) --The name of the instance profile.
            

    :type EbsOptimized: boolean
    :param EbsOptimized: Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
            Default: false
            

    :type TagSpecifications: list
    :param TagSpecifications: The tags to apply to the resources during launch. You can tag instances and volumes. The specified tags are applied to all instances or volumes that are created during launch.
            (dict) --The tags to apply to a resource when the resource is being created.
            ResourceType (string) --The type of resource to tag. Currently, the resource types that support tagging on creation are instance and volume .
            Tags (list) --The tags to apply to the resource.
            (dict) --Describes a tag.
            Key (string) --The key of the tag.
            Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:
            Value (string) --The value of the tag.
            Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
            
            
            

    :rtype: dict
    :return: {
        'ReservationId': 'string',
        'OwnerId': 'string',
        'RequesterId': 'string',
        'Groups': [
            {
                'GroupName': 'string',
                'GroupId': 'string'
            },
        ],
        'Instances': [
            {
                'InstanceId': 'string',
                'ImageId': 'string',
                'State': {
                    'Code': 123,
                    'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                },
                'PrivateDnsName': 'string',
                'PublicDnsName': 'string',
                'StateTransitionReason': 'string',
                'KeyName': 'string',
                'AmiLaunchIndex': 123,
                'ProductCodes': [
                    {
                        'ProductCodeId': 'string',
                        'ProductCodeType': 'devpay'|'marketplace'
                    },
                ],
                'InstanceType': 't1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'t2.xlarge'|'t2.2xlarge'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'i3.large'|'i3.xlarge'|'i3.2xlarge'|'i3.4xlarge'|'i3.8xlarge'|'i3.16xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
                'LaunchTime': datetime(2015, 1, 1),
                'Placement': {
                    'AvailabilityZone': 'string',
                    'GroupName': 'string',
                    'Tenancy': 'default'|'dedicated'|'host',
                    'HostId': 'string',
                    'Affinity': 'string'
                },
                'KernelId': 'string',
                'RamdiskId': 'string',
                'Platform': 'Windows',
                'Monitoring': {
                    'State': 'disabled'|'disabling'|'enabled'|'pending'
                },
                'SubnetId': 'string',
                'VpcId': 'string',
                'PrivateIpAddress': 'string',
                'PublicIpAddress': 'string',
                'StateReason': {
                    'Code': 'string',
                    'Message': 'string'
                },
                'Architecture': 'i386'|'x86_64',
                'RootDeviceType': 'ebs'|'instance-store',
                'RootDeviceName': 'string',
                'BlockDeviceMappings': [
                    {
                        'DeviceName': 'string',
                        'Ebs': {
                            'VolumeId': 'string',
                            'Status': 'attaching'|'attached'|'detaching'|'detached',
                            'AttachTime': datetime(2015, 1, 1),
                            'DeleteOnTermination': True|False
                        }
                    },
                ],
                'VirtualizationType': 'hvm'|'paravirtual',
                'InstanceLifecycle': 'spot'|'scheduled',
                'SpotInstanceRequestId': 'string',
                'ClientToken': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'SecurityGroups': [
                    {
                        'GroupName': 'string',
                        'GroupId': 'string'
                    },
                ],
                'SourceDestCheck': True|False,
                'Hypervisor': 'ovm'|'xen',
                'NetworkInterfaces': [
                    {
                        'NetworkInterfaceId': 'string',
                        'SubnetId': 'string',
                        'VpcId': 'string',
                        'Description': 'string',
                        'OwnerId': 'string',
                        'Status': 'available'|'attaching'|'in-use'|'detaching',
                        'MacAddress': 'string',
                        'PrivateIpAddress': 'string',
                        'PrivateDnsName': 'string',
                        'SourceDestCheck': True|False,
                        'Groups': [
                            {
                                'GroupName': 'string',
                                'GroupId': 'string'
                            },
                        ],
                        'Attachment': {
                            'AttachmentId': 'string',
                            'DeviceIndex': 123,
                            'Status': 'attaching'|'attached'|'detaching'|'detached',
                            'AttachTime': datetime(2015, 1, 1),
                            'DeleteOnTermination': True|False
                        },
                        'Association': {
                            'PublicIp': 'string',
                            'PublicDnsName': 'string',
                            'IpOwnerId': 'string'
                        },
                        'PrivateIpAddresses': [
                            {
                                'PrivateIpAddress': 'string',
                                'PrivateDnsName': 'string',
                                'Primary': True|False,
                                'Association': {
                                    'PublicIp': 'string',
                                    'PublicDnsName': 'string',
                                    'IpOwnerId': 'string'
                                }
                            },
                        ],
                        'Ipv6Addresses': [
                            {
                                'Ipv6Address': 'string'
                            },
                        ]
                    },
                ],
                'IamInstanceProfile': {
                    'Arn': 'string',
                    'Id': 'string'
                },
                'EbsOptimized': True|False,
                'SriovNetSupport': 'string',
                'EnaSupport': True|False
            },
        ]
    }
    
    
    :returns: 
    DryRun (boolean) -- Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .
    ImageId (string) -- [REQUIRED]
    The ID of the AMI, which you can get by calling  DescribeImages .
    
    MinCount (integer) -- [REQUIRED]
    The minimum number of instances to launch. If you specify a minimum that is more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches no instances.
    Constraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 General FAQ.
    
    MaxCount (integer) -- [REQUIRED]
    The maximum number of instances to launch. If you specify more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches the largest possible number of instances above MinCount .
    Constraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 FAQ.
    
    KeyName (string) -- The name of the key pair. You can create a key pair using  CreateKeyPair or  ImportKeyPair .
    
    Warning
    If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.
    
    
    SecurityGroups (list) -- [EC2-Classic, default VPC] One or more security group names. For a nondefault VPC, you must use security group IDs instead.
    Default: Amazon EC2 uses the default security group.
    
    (string) --
    
    
    SecurityGroupIds (list) -- One or more security group IDs. You can create a security group using  CreateSecurityGroup .
    Default: Amazon EC2 uses the default security group.
    
    (string) --
    
    
    UserData (string) -- The user data to make available to the instance. For more information, see Running Commands on Your Linux Instance at Launch (Linux) and Adding User Data (Windows). If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.
    
    This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.
    
    InstanceType (string) -- The instance type. For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide .
    Default: m1.small
    
    Placement (dict) -- The placement for the instance.
    
    AvailabilityZone (string) --The Availability Zone of the instance.
    
    GroupName (string) --The name of the placement group the instance is in (for cluster compute instances).
    
    Tenancy (string) --The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the  ImportInstance command.
    
    HostId (string) --The ID of the Dedicated Host on which the instance resides. This parameter is not supported for the  ImportInstance command.
    
    Affinity (string) --The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the  ImportInstance command.
    
    
    
    KernelId (string) -- The ID of the kernel.
    
    Warning
    We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB in the Amazon Elastic Compute Cloud User Guide .
    
    
    RamdiskId (string) -- The ID of the RAM disk.
    
    Warning
    We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB in the Amazon Elastic Compute Cloud User Guide .
    
    
    BlockDeviceMappings (list) -- The block device mapping.
    
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
    
    
    
    
    
    Monitoring (dict) -- The monitoring for the instance.
    
    Enabled (boolean) -- [REQUIRED]Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
    
    
    
    SubnetId (string) -- [EC2-VPC] The ID of the subnet to launch the instance into.
    DisableApiTermination (boolean) -- If you set this parameter to true , you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. To change this attribute to false after launch, use  ModifyInstanceAttribute . Alternatively, if you set InstanceInitiatedShutdownBehavior to terminate , you can terminate the instance by running the shutdown command from the instance.
    Default: false
    
    InstanceInitiatedShutdownBehavior (string) -- Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).
    Default: stop
    
    PrivateIpAddress (string) -- [EC2-VPC] The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.
    Only one private IP address can be designated as primary. You can't specify this option if you've specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if you're launching more than one instance in the request.
    
    Ipv6Addresses (list) -- [EC2-VPC] Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
    
    (dict) --Describes an IPv6 address.
    
    Ipv6Address (string) --The IPv6 address.
    
    
    
    
    
    Ipv6AddressCount (integer) -- [EC2-VPC] A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.
    ClientToken (string) -- Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency .
    Constraints: Maximum 64 ASCII characters
    
    AdditionalInfo (string) -- Reserved.
    NetworkInterfaces (list) -- One or more network interfaces.
    
    (dict) --Describes a network interface.
    
    NetworkInterfaceId (string) --The ID of the network interface.
    
    DeviceIndex (integer) --The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a  RunInstances request, you must provide the device index.
    
    SubnetId (string) --The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.
    
    Description (string) --The description of the network interface. Applies only if creating a network interface when launching an instance.
    
    PrivateIpAddress (string) --The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a  RunInstances request.
    
    Groups (list) --The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.
    
    (string) --
    
    
    DeleteOnTermination (boolean) --If set to true , the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.
    
    PrivateIpAddresses (list) --One or more private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you're launching more than one instance in a  RunInstances request.
    
    (dict) --Describes a secondary private IPv4 address for a network interface.
    
    PrivateIpAddress (string) -- [REQUIRED]The private IPv4 addresses.
    
    Primary (boolean) --Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
    
    
    
    
    
    SecondaryPrivateIpAddressCount (integer) --The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a  RunInstances request.
    
    AssociatePublicIpAddress (boolean) --Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .
    
    Ipv6Addresses (list) --One or more IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.
    
    (dict) --Describes an IPv6 address.
    
    Ipv6Address (string) --The IPv6 address.
    
    
    
    
    
    Ipv6AddressCount (integer) --A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.
    
    
    
    
    
    IamInstanceProfile (dict) -- The IAM instance profile.
    
    Arn (string) --The Amazon Resource Name (ARN) of the instance profile.
    
    Name (string) --The name of the instance profile.
    
    
    
    EbsOptimized (boolean) -- Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
    Default: false
    
    TagSpecifications (list) -- The tags to apply to the resources during launch. You can tag instances and volumes. The specified tags are applied to all instances or volumes that are created during launch.
    
    (dict) --The tags to apply to a resource when the resource is being created.
    
    ResourceType (string) --The type of resource to tag. Currently, the resource types that support tagging on creation are instance and volume .
    
    Tags (list) --The tags to apply to the resource.
    
    (dict) --Describes a tag.
    
    Key (string) --The key of the tag.
    Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:
    
    Value (string) --The value of the tag.
    Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
    
    
    
    
    
    
    
    
    
    
    """
    pass

def run_scheduled_instances(DryRun=None, ClientToken=None, InstanceCount=None, ScheduledInstanceId=None, LaunchSpecification=None):
    """
    Launches the specified Scheduled Instances.
    Before you can launch a Scheduled Instance, you must purchase it and obtain an identifier using  PurchaseScheduledInstances .
    You must launch a Scheduled Instance during its scheduled time period. You can't stop or reboot a Scheduled Instance, but you can terminate it as needed. If you terminate a Scheduled Instance before the current scheduled time period ends, you can launch it again after a few minutes. For more information, see Scheduled Instances in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    Examples
    This example launches the specified Scheduled Instance in a VPC.
    Expected Output:
    This example launches the specified Scheduled Instance in EC2-Classic.
    Expected Output:
    
    :example: response = client.run_scheduled_instances(
        DryRun=True|False,
        ClientToken='string',
        InstanceCount=123,
        ScheduledInstanceId='string',
        LaunchSpecification={
            'ImageId': 'string',
            'KeyName': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'UserData': 'string',
            'Placement': {
                'AvailabilityZone': 'string',
                'GroupName': 'string'
            },
            'KernelId': 'string',
            'InstanceType': 'string',
            'RamdiskId': 'string',
            'BlockDeviceMappings': [
                {
                    'DeviceName': 'string',
                    'NoDevice': 'string',
                    'VirtualName': 'string',
                    'Ebs': {
                        'SnapshotId': 'string',
                        'VolumeSize': 123,
                        'DeleteOnTermination': True|False,
                        'VolumeType': 'string',
                        'Iops': 123,
                        'Encrypted': True|False
                    }
                },
            ],
            'Monitoring': {
                'Enabled': True|False
            },
            'SubnetId': 'string',
            'NetworkInterfaces': [
                {
                    'NetworkInterfaceId': 'string',
                    'DeviceIndex': 123,
                    'SubnetId': 'string',
                    'Description': 'string',
                    'PrivateIpAddress': 'string',
                    'PrivateIpAddressConfigs': [
                        {
                            'PrivateIpAddress': 'string',
                            'Primary': True|False
                        },
                    ],
                    'SecondaryPrivateIpAddressCount': 123,
                    'AssociatePublicIpAddress': True|False,
                    'Groups': [
                        'string',
                    ],
                    'DeleteOnTermination': True|False,
                    'Ipv6Addresses': [
                        {
                            'Ipv6Address': 'string'
                        },
                    ],
                    'Ipv6AddressCount': 123
                },
            ],
            'IamInstanceProfile': {
                'Arn': 'string',
                'Name': 'string'
            },
            'EbsOptimized': True|False
        }
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type ClientToken: string
    :param ClientToken: Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see Ensuring Idempotency .
            This field is autopopulated if not provided.
            

    :type InstanceCount: integer
    :param InstanceCount: The number of instances.
            Default: 1
            

    :type ScheduledInstanceId: string
    :param ScheduledInstanceId: [REQUIRED]
            The Scheduled Instance ID.
            

    :type LaunchSpecification: dict
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
            PrivateIpAddress (string) --The IPv4 address of the network interface within the subnet.
            PrivateIpAddressConfigs (list) --The private IPv4 addresses.
            (dict) --Describes a private IPv4 address for a Scheduled Instance.
            PrivateIpAddress (string) --The IPv4 address.
            Primary (boolean) --Indicates whether this is a primary IPv4 address. Otherwise, this is a secondary IPv4 address.
            
            SecondaryPrivateIpAddressCount (integer) --The number of secondary private IPv4 addresses.
            AssociatePublicIpAddress (boolean) --Indicates whether to assign a public IPv4 address to instances launched in a VPC. The public IPv4 address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .
            Groups (list) --The IDs of one or more security groups.
            (string) --
            DeleteOnTermination (boolean) --Indicates whether to delete the interface when the instance is terminated.
            Ipv6Addresses (list) --One or more specific IPv6 addresses from the subnet range.
            (dict) --Describes an IPv6 address.
            Ipv6Address (string) --The IPv6 address.
            
            Ipv6AddressCount (integer) --The number of IPv6 addresses to assign to the network interface. The IPv6 addresses are automatically selected from the subnet range.
            
            IamInstanceProfile (dict) --The IAM instance profile.
            Arn (string) --The Amazon Resource Name (ARN).
            Name (string) --The name.
            EbsOptimized (boolean) --Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.
            Default: false
            

    :rtype: dict
    :return: {
        'InstanceIdSet': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def start_instances(InstanceIds=None, AdditionalInfo=None, DryRun=None):
    """
    Starts an Amazon EBS-backed AMI that you've previously stopped.
    Instances that use Amazon EBS volumes as their root devices can be quickly stopped and started. When an instance is stopped, the compute resources are released and you are not billed for hourly instance usage. However, your root partition Amazon EBS volume remains, continues to persist your data, and you are charged for Amazon EBS volume usage. You can restart your instance at any time. Each time you transition an instance from stopped to started, Amazon EC2 charges a full instance hour, even if transitions happen multiple times within a single hour.
    Before stopping an instance, make sure it is in a state from which it can be restarted. Stopping an instance does not preserve data stored in RAM.
    Performing this operation on an instance that uses an instance store as its root device returns an error.
    For more information, see Stopping Instances in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.start_instances(
        InstanceIds=[
            'string',
        ],
        AdditionalInfo='string',
        DryRun=True|False
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            

    :type AdditionalInfo: string
    :param AdditionalInfo: Reserved.

    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :rtype: dict
    :return: {
        'StartingInstances': [
            {
                'InstanceId': 'string',
                'CurrentState': {
                    'Code': 123,
                    'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                },
                'PreviousState': {
                    'Code': 123,
                    'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                }
            },
        ]
    }
    
    
    :returns: 
    0 : pending
    16 : running
    32 : shutting-down
    48 : terminated
    64 : stopping
    80 : stopped
    
    """
    pass

def stop_instances(DryRun=None, InstanceIds=None, Force=None):
    """
    Stops an Amazon EBS-backed instance.
    We don't charge hourly usage for a stopped instance, or data transfer fees; however, your root partition Amazon EBS volume remains, continues to persist your data, and you are charged for Amazon EBS volume usage. Each time you transition an instance from stopped to started, Amazon EC2 charges a full instance hour, even if transitions happen multiple times within a single hour.
    You can't start or stop Spot instances, and you can't stop instance store-backed instances.
    When you stop an instance, we shut it down. You can restart your instance at any time. Before stopping an instance, make sure it is in a state from which it can be restarted. Stopping an instance does not preserve data stored in RAM.
    Stopping an instance is different to rebooting or terminating it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, the root device and any other devices attached during the instance launch are automatically deleted. For more information about the differences between rebooting, stopping, and terminating instances, see Instance Lifecycle in the Amazon Elastic Compute Cloud User Guide .
    When you stop an instance, we attempt to shut it down forcibly after a short while. If your instance appears stuck in the stopping state after a period of time, there may be an issue with the underlying host computer. For more information, see Troubleshooting Stopping Your Instance in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_instances(
        DryRun=True|False,
        InstanceIds=[
            'string',
        ],
        Force=True|False
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            

    :type Force: boolean
    :param Force: Forces the instances to stop. The instances do not have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures. This option is not recommended for Windows instances.
            Default: false
            

    :rtype: dict
    :return: {
        'StoppingInstances': [
            {
                'InstanceId': 'string',
                'CurrentState': {
                    'Code': 123,
                    'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                },
                'PreviousState': {
                    'Code': 123,
                    'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                }
            },
        ]
    }
    
    
    :returns: 
    0 : pending
    16 : running
    32 : shutting-down
    48 : terminated
    64 : stopping
    80 : stopped
    
    """
    pass

def terminate_instances(DryRun=None, InstanceIds=None):
    """
    Shuts down one or more instances. This operation is idempotent; if you terminate an instance more than once, each call succeeds.
    If you specify multiple instances and the request fails (for example, because of a single incorrect instance ID), none of the instances are terminated.
    Terminated instances remain visible after termination (for approximately one hour).
    By default, Amazon EC2 deletes all EBS volumes that were attached when the instance launched. Volumes attached after instance launch continue running.
    You can stop, start, and terminate EBS-backed instances. You can only terminate instance store-backed instances. What happens to an instance differs if you stop it or terminate it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, any attached EBS volumes with the DeleteOnTermination block device mapping parameter set to true are automatically deleted. For more information about the differences between stopping and terminating instances, see Instance Lifecycle in the Amazon Elastic Compute Cloud User Guide .
    For more information about troubleshooting, see Troubleshooting Terminating Your Instance in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.terminate_instances(
        DryRun=True|False,
        InstanceIds=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            Constraints: Up to 1000 instance IDs. We recommend breaking up this request into smaller batches.
            (string) --
            

    :rtype: dict
    :return: {
        'TerminatingInstances': [
            {
                'InstanceId': 'string',
                'CurrentState': {
                    'Code': 123,
                    'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                },
                'PreviousState': {
                    'Code': 123,
                    'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                }
            },
        ]
    }
    
    
    :returns: 
    0 : pending
    16 : running
    32 : shutting-down
    48 : terminated
    64 : stopping
    80 : stopped
    
    """
    pass

def unassign_ipv6_addresses(NetworkInterfaceId=None, Ipv6Addresses=None):
    """
    Unassigns one or more IPv6 addresses from a network interface.
    See also: AWS API Documentation
    
    
    :example: response = client.unassign_ipv6_addresses(
        NetworkInterfaceId='string',
        Ipv6Addresses=[
            'string',
        ]
    )
    
    
    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            

    :type Ipv6Addresses: list
    :param Ipv6Addresses: [REQUIRED]
            The IPv6 addresses to unassign from the network interface.
            (string) --
            

    :rtype: dict
    :return: {
        'NetworkInterfaceId': 'string',
        'UnassignedIpv6Addresses': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def unassign_private_ip_addresses(NetworkInterfaceId=None, PrivateIpAddresses=None):
    """
    Unassigns one or more secondary private IP addresses from a network interface.
    See also: AWS API Documentation
    
    Examples
    This example unassigns the specified private IP address from the specified network interface.
    Expected Output:
    
    :example: response = client.unassign_private_ip_addresses(
        NetworkInterfaceId='string',
        PrivateIpAddresses=[
            'string',
        ]
    )
    
    
    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The ID of the network interface.
            

    :type PrivateIpAddresses: list
    :param PrivateIpAddresses: [REQUIRED]
            The secondary private IP addresses to unassign from the network interface. You can specify this option multiple times to unassign more than one IP address.
            (string) --
            

    :return: response = client.unassign_private_ip_addresses(
        NetworkInterfaceId='eni-e5aa89a3',
        PrivateIpAddresses=[
            '10.0.0.82',
        ],
    )
    
    print(response)
    
    
    """
    pass

def unmonitor_instances(DryRun=None, InstanceIds=None):
    """
    Disables detailed monitoring for a running instance. For more information, see Monitoring Your Instances and Volumes in the Amazon Elastic Compute Cloud User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.unmonitor_instances(
        DryRun=True|False,
        InstanceIds=[
            'string',
        ]
    )
    
    
    :type DryRun: boolean
    :param DryRun: Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation . Otherwise, it is UnauthorizedOperation .

    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'InstanceMonitorings': [
            {
                'InstanceId': 'string',
                'Monitoring': {
                    'State': 'disabled'|'disabling'|'enabled'|'pending'
                }
            },
        ]
    }
    
    
    """
    pass

