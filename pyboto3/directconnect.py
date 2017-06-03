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

def allocate_connection_on_interconnect(bandwidth=None, connectionName=None, ownerAccount=None, interconnectId=None, vlan=None):
    """
    Deprecated in favor of  AllocateHostedConnection .
    Creates a hosted connection on an interconnect.
    Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the given interconnect.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_connection_on_interconnect(
        bandwidth='string',
        connectionName='string',
        ownerAccount='string',
        interconnectId='string',
        vlan=123
    )
    
    
    :type bandwidth: string
    :param bandwidth: [REQUIRED]
            Bandwidth of the connection.
            Example: '500Mbps '
            Default: None
            Values: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, or 500Mbps
            

    :type connectionName: string
    :param connectionName: [REQUIRED]
            Name of the provisioned connection.
            Example: '500M Connection to AWS '
            Default: None
            

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]
            Numeric account Id of the customer for whom the connection will be provisioned.
            Example: 123443215678
            Default: None
            

    :type interconnectId: string
    :param interconnectId: [REQUIRED]
            ID of the interconnect on which the connection will be provisioned.
            Example: dxcon-456abc78
            Default: None
            

    :type vlan: integer
    :param vlan: [REQUIRED]
            The dedicated VLAN provisioned to the connection.
            Example: 101
            Default: None
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string'
    }
    
    
    :returns: 
    Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    Pending : The connection has been approved, and is being initialized.
    Available : The network link is up, and the connection is ready for use.
    Down : The network link is down.
    Deleting : The connection is in the process of being deleted.
    Deleted : The connection has been deleted.
    Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    
    """
    pass

def allocate_hosted_connection(connectionId=None, ownerAccount=None, bandwidth=None, connectionName=None, vlan=None):
    """
    Creates a hosted connection on an interconnect or a link aggregation group (LAG).
    Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the given interconnect or LAG.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_hosted_connection(
        connectionId='string',
        ownerAccount='string',
        bandwidth='string',
        connectionName='string',
        vlan=123
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the interconnect or LAG on which the connection will be provisioned.
            Example: dxcon-456abc78 or dxlag-abc123
            Default: None
            

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]
            The numeric account ID of the customer for whom the connection will be provisioned.
            Example: 123443215678
            Default: None
            

    :type bandwidth: string
    :param bandwidth: [REQUIRED]
            The bandwidth of the connection.
            Example: 500Mbps
            Default: None
            Values: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, or 500Mbps
            

    :type connectionName: string
    :param connectionName: [REQUIRED]
            The name of the provisioned connection.
            Example: '500M Connection to AWS '
            Default: None
            

    :type vlan: integer
    :param vlan: [REQUIRED]
            The dedicated VLAN provisioned to the hosted connection.
            Example: 101
            Default: None
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string'
    }
    
    
    :returns: 
    Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    Pending : The connection has been approved, and is being initialized.
    Available : The network link is up, and the connection is ready for use.
    Down : The network link is down.
    Deleting : The connection is in the process of being deleted.
    Deleted : The connection has been deleted.
    Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    
    """
    pass

def allocate_private_virtual_interface(connectionId=None, ownerAccount=None, newPrivateVirtualInterfaceAllocation=None):
    """
    Provisions a private virtual interface to be owned by another AWS customer.
    Virtual interfaces created using this action must be confirmed by the virtual interface owner by using the  ConfirmPrivateVirtualInterface action. Until then, the virtual interface will be in 'Confirming' state, and will not be available for handling traffic.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_private_virtual_interface(
        connectionId='string',
        ownerAccount='string',
        newPrivateVirtualInterfaceAllocation={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'customerAddress': 'string'
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The connection ID on which the private virtual interface is provisioned.
            Default: None
            

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]
            The AWS account that will own the new private virtual interface.
            Default: None
            

    :type newPrivateVirtualInterfaceAllocation: dict
    :param newPrivateVirtualInterfaceAllocation: [REQUIRED]
            Detailed information for the private virtual interface to be provisioned.
            Default: None
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer.
            Example: 'My VPC'
            vlan (integer) -- [REQUIRED]The VLAN ID.
            Example: 101
            asn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            authKey (string) --The authentication key for BGP configuration.
            Example: asdf34example
            amazonAddress (string) --IP address assigned to the Amazon interface.
            Example: 192.168.1.1/30 or 2001:db8::1/125
            addressFamily (string) --Indicates the address family for the BGP peer.
            ipv4 : IPv4 address family
            ipv6 : IPv6 address family
            customerAddress (string) --IP address assigned to the customer interface.
            Example: 192.168.1.2/30 or 2001:db8::2/125
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'virtualGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'
            },
        ]
    }
    
    
    :returns: 
    ipv4 : IPv4 address family
    ipv6 : IPv6 address family
    
    """
    pass

def allocate_public_virtual_interface(connectionId=None, ownerAccount=None, newPublicVirtualInterfaceAllocation=None):
    """
    Provisions a public virtual interface to be owned by a different customer.
    The owner of a connection calls this function to provision a public virtual interface which will be owned by another AWS customer.
    Virtual interfaces created using this function must be confirmed by the virtual interface owner by calling ConfirmPublicVirtualInterface. Until this step has been completed, the virtual interface will be in 'Confirming' state, and will not be available for handling traffic.
    When creating an IPv6 public virtual interface (addressFamily is 'ipv6'), the customer and amazon address fields should be left blank to use auto-assigned IPv6 space. Custom IPv6 Addresses are currently not supported.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_public_virtual_interface(
        connectionId='string',
        ownerAccount='string',
        newPublicVirtualInterfaceAllocation={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The connection ID on which the public virtual interface is provisioned.
            Default: None
            

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]
            The AWS account that will own the new public virtual interface.
            Default: None
            

    :type newPublicVirtualInterfaceAllocation: dict
    :param newPublicVirtualInterfaceAllocation: [REQUIRED]
            Detailed information for the public virtual interface to be provisioned.
            Default: None
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer.
            Example: 'My VPC'
            vlan (integer) -- [REQUIRED]The VLAN ID.
            Example: 101
            asn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            authKey (string) --The authentication key for BGP configuration.
            Example: asdf34example
            amazonAddress (string) --IP address assigned to the Amazon interface.
            Example: 192.168.1.1/30 or 2001:db8::1/125
            customerAddress (string) --IP address assigned to the customer interface.
            Example: 192.168.1.2/30 or 2001:db8::2/125
            addressFamily (string) --Indicates the address family for the BGP peer.
            ipv4 : IPv4 address family
            ipv6 : IPv6 address family
            routeFilterPrefixes (list) --A list of routes to be advertised to the AWS network in this region (public virtual interface).
            (dict) --A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.
            cidr (string) --CIDR notation for the advertised route. Multiple routes are separated by commas.
            IPv6 CIDRs must be at least a /64 or shorter
            Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64
            
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'virtualGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'
            },
        ]
    }
    
    
    :returns: 
    ipv4 : IPv4 address family
    ipv6 : IPv6 address family
    
    """
    pass

def associate_connection_with_lag(connectionId=None, lagId=None):
    """
    Associates an existing connection with a link aggregation group (LAG). The connection is interrupted and re-established as a member of the LAG (connectivity to AWS will be interrupted). The connection must be hosted on the same AWS Direct Connect endpoint as the LAG, and its bandwidth must match the bandwidth for the LAG. You can reassociate a connection that's currently associated with a different LAG; however, if removing the connection will cause the original LAG to fall below its setting for minimum number of operational connections, the request fails.
    Any virtual interfaces that are directly associated with the connection are automatically re-associated with the LAG. If the connection was originally associated with a different LAG, the virtual interfaces remain associated with the original LAG.
    For interconnects, any hosted connections are automatically re-associated with the LAG. If the interconnect was originally associated with a different LAG, the hosted connections remain associated with the original LAG.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_connection_with_lag(
        connectionId='string',
        lagId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection.
            Example: dxcon-abc123
            Default: None
            

    :type lagId: string
    :param lagId: [REQUIRED]
            The ID of the LAG with which to associate the connection.
            Example: dxlag-abc123
            Default: None
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string'
    }
    
    
    :returns: 
    Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    Pending : The connection has been approved, and is being initialized.
    Available : The network link is up, and the connection is ready for use.
    Down : The network link is down.
    Deleting : The connection is in the process of being deleted.
    Deleted : The connection has been deleted.
    Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    
    """
    pass

def associate_hosted_connection(connectionId=None, parentConnectionId=None):
    """
    Associates a hosted connection and its virtual interfaces with a link aggregation group (LAG) or interconnect. If the target interconnect or LAG has an existing hosted connection with a conflicting VLAN number or IP address, the operation fails. This action temporarily interrupts the hosted connection's connectivity to AWS as it is being migrated.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_hosted_connection(
        connectionId='string',
        parentConnectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the hosted connection.
            Example: dxcon-abc123
            Default: None
            

    :type parentConnectionId: string
    :param parentConnectionId: [REQUIRED]
            The ID of the interconnect or the LAG.
            Example: dxcon-abc123 or dxlag-abc123
            Default: None
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string'
    }
    
    
    :returns: 
    Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    Pending : The connection has been approved, and is being initialized.
    Available : The network link is up, and the connection is ready for use.
    Down : The network link is down.
    Deleting : The connection is in the process of being deleted.
    Deleted : The connection has been deleted.
    Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    
    """
    pass

def associate_virtual_interface(virtualInterfaceId=None, connectionId=None):
    """
    Associates a virtual interface with a specified link aggregation group (LAG) or connection. Connectivity to AWS is temporarily interrupted as the virtual interface is being migrated. If the target connection or LAG has an associated virtual interface with a conflicting VLAN number or a conflicting IP address, the operation fails.
    Virtual interfaces associated with a hosted connection cannot be associated with a LAG; hosted connections must be migrated along with their virtual interfaces using  AssociateHostedConnection .
    Hosted virtual interfaces (an interface for which the owner of the connection is not the owner of physical connection) can only be reassociated by the owner of the physical connection.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_virtual_interface(
        virtualInterfaceId='string',
        connectionId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]
            The ID of the virtual interface.
            Example: dxvif-123dfg56
            Default: None
            

    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the LAG or connection with which to associate the virtual interface.
            Example: dxlag-abc123 or dxcon-abc123
            Default: None
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'virtualGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'
            },
        ]
    }
    
    
    :returns: 
    ipv4 : IPv4 address family
    ipv6 : IPv6 address family
    
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

def confirm_connection(connectionId=None):
    """
    Confirm the creation of a hosted connection on an interconnect.
    Upon creation, the hosted connection is initially in the 'Ordering' state, and will remain in this state until the owner calls ConfirmConnection to confirm creation of the hosted connection.
    See also: AWS API Documentation
    
    
    :example: response = client.confirm_connection(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).
            Example: dxcon-fg5678gh
            Default: None
            

    :rtype: dict
    :return: {
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
    }
    
    
    """
    pass

def confirm_private_virtual_interface(virtualInterfaceId=None, virtualGatewayId=None):
    """
    Accept ownership of a private virtual interface created by another customer.
    After the virtual interface owner calls this function, the virtual interface will be created and attached to the given virtual private gateway, and will be available for handling traffic.
    See also: AWS API Documentation
    
    
    :example: response = client.confirm_private_virtual_interface(
        virtualInterfaceId='string',
        virtualGatewayId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]
            The ID of the virtual interface.
            Example: dxvif-123dfg56
            Default: None
            

    :type virtualGatewayId: string
    :param virtualGatewayId: [REQUIRED]
            ID of the virtual private gateway that will be attached to the virtual interface.
            A virtual private gateway can be managed via the Amazon Virtual Private Cloud (VPC) console or the EC2 CreateVpnGateway action.
            Default: None
            

    :rtype: dict
    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
    }
    
    
    :returns: 
    Confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    Verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    Pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    Available : A virtual interface that is able to forward traffic.
    Down : A virtual interface that is BGP down.
    Deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    Deleted : A virtual interface that cannot forward traffic.
    Rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state.
    
    """
    pass

def confirm_public_virtual_interface(virtualInterfaceId=None):
    """
    Accept ownership of a public virtual interface created by another customer.
    After the virtual interface owner calls this function, the specified virtual interface will be created and made available for handling traffic.
    See also: AWS API Documentation
    
    
    :example: response = client.confirm_public_virtual_interface(
        virtualInterfaceId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]
            The ID of the virtual interface.
            Example: dxvif-123dfg56
            Default: None
            

    :rtype: dict
    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
    }
    
    
    """
    pass

def create_bgp_peer(virtualInterfaceId=None, newBGPPeer=None):
    """
    Creates a new BGP peer on a specified virtual interface. The BGP peer cannot be in the same address family (IPv4/IPv6) of an existing BGP peer on the virtual interface.
    You must create a BGP peer for the corresponding address family in order to access AWS resources that also use that address family.
    When creating a IPv6 BGP peer, the Amazon address and customer address fields must be left blank. IPv6 addresses are automatically assigned from Amazon's pool of IPv6 addresses; you cannot specify custom IPv6 addresses.
    For a public virtual interface, the Autonomous System Number (ASN) must be private or already whitelisted for the virtual interface.
    See also: AWS API Documentation
    
    
    :example: response = client.create_bgp_peer(
        virtualInterfaceId='string',
        newBGPPeer={
            'asn': 123,
            'authKey': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'amazonAddress': 'string',
            'customerAddress': 'string'
        }
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface on which the BGP peer will be provisioned.
            Example: dxvif-456abc78
            Default: None
            

    :type newBGPPeer: dict
    :param newBGPPeer: Detailed information for the BGP peer to be created.
            Default: None
            asn (integer) --The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            authKey (string) --The authentication key for BGP configuration.
            Example: asdf34example
            addressFamily (string) --Indicates the address family for the BGP peer.
            ipv4 : IPv4 address family
            ipv6 : IPv6 address family
            amazonAddress (string) --IP address assigned to the Amazon interface.
            Example: 192.168.1.1/30 or 2001:db8::1/125
            customerAddress (string) --IP address assigned to the customer interface.
            Example: 192.168.1.2/30 or 2001:db8::2/125
            

    :rtype: dict
    :return: {
        'virtualInterface': {
            'ownerAccount': 'string',
            'virtualInterfaceId': 'string',
            'location': 'string',
            'connectionId': 'string',
            'virtualInterfaceType': 'string',
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'customerRouterConfig': 'string',
            'virtualGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'
                },
            ]
        }
    }
    
    
    :returns: 
    ipv4 : IPv4 address family
    ipv6 : IPv6 address family
    
    """
    pass

def create_connection(location=None, bandwidth=None, connectionName=None, lagId=None):
    """
    Creates a new connection between the customer network and a specific AWS Direct Connect location.
    A connection links your internal network to an AWS Direct Connect location over a standard 1 gigabit or 10 gigabit Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router. An AWS Direct Connect location provides access to Amazon Web Services in the region it is associated with. You can establish connections with AWS Direct Connect locations in multiple regions, but a connection in one region does not provide connectivity to other regions.
    You can automatically add the new connection to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new connection is allocated on the same AWS Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no connection will be created.
    See also: AWS API Documentation
    
    
    :example: response = client.create_connection(
        location='string',
        bandwidth='string',
        connectionName='string',
        lagId='string'
    )
    
    
    :type location: string
    :param location: [REQUIRED]
            Where the connection is located.
            Example: EqSV5
            Default: None
            

    :type bandwidth: string
    :param bandwidth: [REQUIRED]
            Bandwidth of the connection.
            Example: 1Gbps
            Default: None
            

    :type connectionName: string
    :param connectionName: [REQUIRED]
            The name of the connection.
            Example: 'My Connection to AWS '
            Default: None
            

    :type lagId: string
    :param lagId: The ID of the LAG.
            Example: dxlag-fg5678gh
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string'
    }
    
    
    :returns: 
    Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    Pending : The connection has been approved, and is being initialized.
    Available : The network link is up, and the connection is ready for use.
    Down : The network link is down.
    Deleting : The connection is in the process of being deleted.
    Deleted : The connection has been deleted.
    Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    
    """
    pass

def create_interconnect(interconnectName=None, bandwidth=None, location=None, lagId=None):
    """
    Creates a new interconnect between a AWS Direct Connect partner's network and a specific AWS Direct Connect location.
    An interconnect is a connection which is capable of hosting other connections. The AWS Direct Connect partner can use an interconnect to provide sub-1Gbps AWS Direct Connect service to tier 2 customers who do not have their own connections. Like a standard connection, an interconnect links the AWS Direct Connect partner's network to an AWS Direct Connect location over a standard 1 Gbps or 10 Gbps Ethernet fiber-optic cable. One end is connected to the partner's router, the other to an AWS Direct Connect router.
    You can automatically add the new interconnect to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new interconnect is allocated on the same AWS Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no interconnect will be created.
    For each end customer, the AWS Direct Connect partner provisions a connection on their interconnect by calling AllocateConnectionOnInterconnect. The end customer can then connect to AWS resources by creating a virtual interface on their connection, using the VLAN assigned to them by the AWS Direct Connect partner.
    See also: AWS API Documentation
    
    
    :example: response = client.create_interconnect(
        interconnectName='string',
        bandwidth='string',
        location='string',
        lagId='string'
    )
    
    
    :type interconnectName: string
    :param interconnectName: [REQUIRED]
            The name of the interconnect.
            Example: '1G Interconnect to AWS '
            Default: None
            

    :type bandwidth: string
    :param bandwidth: [REQUIRED]
            The port bandwidth
            Example: 1Gbps
            Default: None
            Available values: 1Gbps,10Gbps
            

    :type location: string
    :param location: [REQUIRED]
            Where the interconnect is located
            Example: EqSV5
            Default: None
            

    :type lagId: string
    :param lagId: The ID of the LAG.
            Example: dxlag-fg5678gh
            

    :rtype: dict
    :return: {
        'interconnectId': 'string',
        'interconnectName': 'string',
        'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string'
    }
    
    
    :returns: 
    Requested : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    Pending : The interconnect has been approved, and is being initialized.
    Available : The network link is up, and the interconnect is ready for use.
    Down : The network link is down.
    Deleting : The interconnect is in the process of being deleted.
    Deleted : The interconnect has been deleted.
    
    """
    pass

def create_lag(numberOfConnections=None, location=None, connectionsBandwidth=None, lagName=None, connectionId=None):
    """
    Creates a new link aggregation group (LAG) with the specified number of bundled physical connections between the customer network and a specific AWS Direct Connect location. A LAG is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple 1 gigabit or 10 gigabit interfaces, allowing you to treat them as a single interface.
    All connections in a LAG must use the same bandwidth (for example, 10 Gbps), and must terminate at the same AWS Direct Connect endpoint.
    You can have up to 10 connections per LAG. Regardless of this limit, if you request more connections for the LAG than AWS Direct Connect can allocate on a single endpoint, no LAG is created.
    You can specify an existing physical connection or interconnect to include in the LAG (which counts towards the total number of connections). Doing so interrupts the current physical connection or hosted connections, and re-establishes them as a member of the LAG. The LAG will be created on the same AWS Direct Connect endpoint to which the connection terminates. Any virtual interfaces associated with the connection are automatically disassociated and re-associated with the LAG. The connection ID does not change.
    If the AWS account used to create a LAG is a registered AWS Direct Connect partner, the LAG is automatically enabled to host sub-connections. For a LAG owned by a partner, any associated virtual interfaces cannot be directly configured.
    See also: AWS API Documentation
    
    
    :example: response = client.create_lag(
        numberOfConnections=123,
        location='string',
        connectionsBandwidth='string',
        lagName='string',
        connectionId='string'
    )
    
    
    :type numberOfConnections: integer
    :param numberOfConnections: [REQUIRED]
            The number of physical connections initially provisioned and bundled by the LAG.
            Default: None
            

    :type location: string
    :param location: [REQUIRED]
            The AWS Direct Connect location in which the LAG should be allocated.
            Example: EqSV5
            Default: None
            

    :type connectionsBandwidth: string
    :param connectionsBandwidth: [REQUIRED]
            The bandwidth of the individual physical connections bundled by the LAG.
            Default: None
            Available values: 1Gbps, 10Gbps
            

    :type lagName: string
    :param lagName: [REQUIRED]
            The name of the LAG.
            Example: '3x10G LAG to AWS '
            Default: None
            

    :type connectionId: string
    :param connectionId: The ID of an existing connection to migrate to the LAG.
            Default: None
            

    :rtype: dict
    :return: {
        'connectionsBandwidth': 'string',
        'numberOfConnections': 123,
        'lagId': 'string',
        'ownerAccount': 'string',
        'lagName': 'string',
        'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
        'location': 'string',
        'region': 'string',
        'minimumLinks': 123,
        'awsDevice': 'string',
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string'
            },
        ],
        'allowsHostedConnections': True|False
    }
    
    
    :returns: 
    Requested : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
    Pending : The LAG has been approved, and is being initialized.
    Available : The network link is established, and the LAG is ready for use.
    Down : The network link is down.
    Deleting : The LAG is in the process of being deleted.
    Deleted : The LAG has been deleted.
    
    """
    pass

def create_private_virtual_interface(connectionId=None, newPrivateVirtualInterface=None):
    """
    Creates a new private virtual interface. A virtual interface is the VLAN that transports AWS Direct Connect traffic. A private virtual interface supports sending traffic to a single virtual private cloud (VPC).
    See also: AWS API Documentation
    
    
    :example: response = client.create_private_virtual_interface(
        connectionId='string',
        newPrivateVirtualInterface={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualGatewayId': 'string'
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).
            Example: dxcon-fg5678gh
            Default: None
            

    :type newPrivateVirtualInterface: dict
    :param newPrivateVirtualInterface: [REQUIRED]
            Detailed information for the private virtual interface to be created.
            Default: None
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer.
            Example: 'My VPC'
            vlan (integer) -- [REQUIRED]The VLAN ID.
            Example: 101
            asn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            authKey (string) --The authentication key for BGP configuration.
            Example: asdf34example
            amazonAddress (string) --IP address assigned to the Amazon interface.
            Example: 192.168.1.1/30 or 2001:db8::1/125
            customerAddress (string) --IP address assigned to the customer interface.
            Example: 192.168.1.2/30 or 2001:db8::2/125
            addressFamily (string) --Indicates the address family for the BGP peer.
            ipv4 : IPv4 address family
            ipv6 : IPv6 address family
            virtualGatewayId (string) -- [REQUIRED]The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.
            Example: vgw-123er56
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'virtualGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'
            },
        ]
    }
    
    
    :returns: 
    ipv4 : IPv4 address family
    ipv6 : IPv6 address family
    
    """
    pass

def create_public_virtual_interface(connectionId=None, newPublicVirtualInterface=None):
    """
    Creates a new public virtual interface. A virtual interface is the VLAN that transports AWS Direct Connect traffic. A public virtual interface supports sending traffic to public services of AWS such as Amazon Simple Storage Service (Amazon S3).
    When creating an IPv6 public virtual interface (addressFamily is 'ipv6'), the customer and amazon address fields should be left blank to use auto-assigned IPv6 space. Custom IPv6 Addresses are currently not supported.
    See also: AWS API Documentation
    
    
    :example: response = client.create_public_virtual_interface(
        connectionId='string',
        newPublicVirtualInterface={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).
            Example: dxcon-fg5678gh
            Default: None
            

    :type newPublicVirtualInterface: dict
    :param newPublicVirtualInterface: [REQUIRED]
            Detailed information for the public virtual interface to be created.
            Default: None
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer.
            Example: 'My VPC'
            vlan (integer) -- [REQUIRED]The VLAN ID.
            Example: 101
            asn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            authKey (string) --The authentication key for BGP configuration.
            Example: asdf34example
            amazonAddress (string) --IP address assigned to the Amazon interface.
            Example: 192.168.1.1/30 or 2001:db8::1/125
            customerAddress (string) --IP address assigned to the customer interface.
            Example: 192.168.1.2/30 or 2001:db8::2/125
            addressFamily (string) --Indicates the address family for the BGP peer.
            ipv4 : IPv4 address family
            ipv6 : IPv6 address family
            routeFilterPrefixes (list) --A list of routes to be advertised to the AWS network in this region (public virtual interface).
            (dict) --A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.
            cidr (string) --CIDR notation for the advertised route. Multiple routes are separated by commas.
            IPv6 CIDRs must be at least a /64 or shorter
            Example: 10.10.10.0/24,10.10.11.0/24,2001:db8::/64
            
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'customerRouterConfig': 'string',
        'virtualGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'
            },
        ]
    }
    
    
    :returns: 
    ipv4 : IPv4 address family
    ipv6 : IPv6 address family
    
    """
    pass

def delete_bgp_peer(virtualInterfaceId=None, asn=None, customerAddress=None):
    """
    Deletes a BGP peer on the specified virtual interface that matches the specified customer address and ASN. You cannot delete the last BGP peer from a virtual interface.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bgp_peer(
        virtualInterfaceId='string',
        asn=123,
        customerAddress='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface from which the BGP peer will be deleted.
            Example: dxvif-456abc78
            Default: None
            

    :type asn: integer
    :param asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            

    :type customerAddress: string
    :param customerAddress: IP address assigned to the customer interface.
            Example: 192.168.1.2/30 or 2001:db8::2/125
            

    :rtype: dict
    :return: {
        'virtualInterface': {
            'ownerAccount': 'string',
            'virtualInterfaceId': 'string',
            'location': 'string',
            'connectionId': 'string',
            'virtualInterfaceType': 'string',
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
            'customerRouterConfig': 'string',
            'virtualGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'
                },
            ]
        }
    }
    
    
    :returns: 
    ipv4 : IPv4 address family
    ipv6 : IPv6 address family
    
    """
    pass

def delete_connection(connectionId=None):
    """
    Deletes the connection.
    Deleting a connection only stops the AWS Direct Connect port hour and data transfer charges. You need to cancel separately with the providers any services or charges for cross-connects or network circuits that connect you to the AWS Direct Connect location.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_connection(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).
            Example: dxcon-fg5678gh
            Default: None
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string'
    }
    
    
    """
    pass

def delete_interconnect(interconnectId=None):
    """
    Deletes the specified interconnect.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_interconnect(
        interconnectId='string'
    )
    
    
    :type interconnectId: string
    :param interconnectId: [REQUIRED]
            The ID of the interconnect.
            Example: dxcon-abc123
            

    :rtype: dict
    :return: {
        'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'
    }
    
    
    """
    pass

def delete_lag(lagId=None):
    """
    Deletes a link aggregation group (LAG). You cannot delete a LAG if it has active virtual interfaces or hosted connections.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_lag(
        lagId='string'
    )
    
    
    :type lagId: string
    :param lagId: [REQUIRED]
            The ID of the LAG to delete.
            Example: dxlag-abc123
            Default: None
            

    :rtype: dict
    :return: {
        'connectionsBandwidth': 'string',
        'numberOfConnections': 123,
        'lagId': 'string',
        'ownerAccount': 'string',
        'lagName': 'string',
        'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
        'location': 'string',
        'region': 'string',
        'minimumLinks': 123,
        'awsDevice': 'string',
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string'
            },
        ],
        'allowsHostedConnections': True|False
    }
    
    
    :returns: 
    Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    Pending : The connection has been approved, and is being initialized.
    Available : The network link is up, and the connection is ready for use.
    Down : The network link is down.
    Deleting : The connection is in the process of being deleted.
    Deleted : The connection has been deleted.
    Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    
    """
    pass

def delete_virtual_interface(virtualInterfaceId=None):
    """
    Deletes a virtual interface.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_virtual_interface(
        virtualInterfaceId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]
            The ID of the virtual interface.
            Example: dxvif-123dfg56
            Default: None
            

    :rtype: dict
    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
    }
    
    
    """
    pass

def describe_connection_loa(connectionId=None, providerName=None, loaContentType=None):
    """
    Deprecated in favor of  DescribeLoa .
    Returns the LOA-CFA for a Connection.
    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that your APN partner or service provider uses when establishing your cross connect to AWS at the colocation facility. For more information, see Requesting Cross Connects at AWS Direct Connect Locations in the AWS Direct Connect user guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_connection_loa(
        connectionId='string',
        providerName='string',
        loaContentType='application/pdf'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).
            Example: dxcon-fg5678gh
            Default: None
            

    :type providerName: string
    :param providerName: The name of the APN partner or service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.
            Default: None
            

    :type loaContentType: string
    :param loaContentType: A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is 'application/pdf'.
            Default: application/pdf
            

    :rtype: dict
    :return: {
        'loa': {
            'loaContent': b'bytes',
            'loaContentType': 'application/pdf'
        }
    }
    
    
    """
    pass

def describe_connections(connectionId=None):
    """
    Displays all connections in this region.
    If a connection ID is provided, the call returns only that particular connection.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_connections(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).
            Example: dxcon-fg5678gh
            Default: None
            

    :rtype: dict
    :return: {
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_connections_on_interconnect(interconnectId=None):
    """
    Deprecated in favor of  DescribeHostedConnections .
    Returns a list of connections that have been provisioned on the given interconnect.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_connections_on_interconnect(
        interconnectId='string'
    )
    
    
    :type interconnectId: string
    :param interconnectId: [REQUIRED]
            ID of the interconnect on which a list of connection is provisioned.
            Example: dxcon-abc123
            Default: None
            

    :rtype: dict
    :return: {
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_hosted_connections(connectionId=None):
    """
    Returns a list of hosted connections that have been provisioned on the given interconnect or link aggregation group (LAG).
    See also: AWS API Documentation
    
    
    :example: response = client.describe_hosted_connections(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the interconnect or LAG on which the hosted connections are provisioned.
            Example: dxcon-abc123 or dxlag-abc123
            Default: None
            

    :rtype: dict
    :return: {
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_interconnect_loa(interconnectId=None, providerName=None, loaContentType=None):
    """
    Deprecated in favor of  DescribeLoa .
    Returns the LOA-CFA for an Interconnect.
    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to AWS at the colocation facility. For more information, see Requesting Cross Connects at AWS Direct Connect Locations in the AWS Direct Connect user guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_interconnect_loa(
        interconnectId='string',
        providerName='string',
        loaContentType='application/pdf'
    )
    
    
    :type interconnectId: string
    :param interconnectId: [REQUIRED]
            The ID of the interconnect.
            Example: dxcon-abc123
            

    :type providerName: string
    :param providerName: The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.
            Default: None
            

    :type loaContentType: string
    :param loaContentType: A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is 'application/pdf'.
            Default: application/pdf
            

    :rtype: dict
    :return: {
        'loa': {
            'loaContent': b'bytes',
            'loaContentType': 'application/pdf'
        }
    }
    
    
    """
    pass

def describe_interconnects(interconnectId=None):
    """
    Returns a list of interconnects owned by the AWS account.
    If an interconnect ID is provided, it will only return this particular interconnect.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_interconnects(
        interconnectId='string'
    )
    
    
    :type interconnectId: string
    :param interconnectId: The ID of the interconnect.
            Example: dxcon-abc123
            

    :rtype: dict
    :return: {
        'interconnects': [
            {
                'interconnectId': 'string',
                'interconnectName': 'string',
                'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_lags(lagId=None):
    """
    Describes the link aggregation groups (LAGs) in your account.
    If a LAG ID is provided, only information about the specified LAG is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_lags(
        lagId='string'
    )
    
    
    :type lagId: string
    :param lagId: The ID of the LAG.
            Example: dxlag-abc123
            Default: None
            

    :rtype: dict
    :return: {
        'lags': [
            {
                'connectionsBandwidth': 'string',
                'numberOfConnections': 123,
                'lagId': 'string',
                'ownerAccount': 'string',
                'lagName': 'string',
                'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
                'location': 'string',
                'region': 'string',
                'minimumLinks': 123,
                'awsDevice': 'string',
                'connections': [
                    {
                        'ownerAccount': 'string',
                        'connectionId': 'string',
                        'connectionName': 'string',
                        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                        'region': 'string',
                        'location': 'string',
                        'bandwidth': 'string',
                        'vlan': 123,
                        'partnerName': 'string',
                        'loaIssueTime': datetime(2015, 1, 1),
                        'lagId': 'string',
                        'awsDevice': 'string'
                    },
                ],
                'allowsHostedConnections': True|False
            },
        ]
    }
    
    
    :returns: 
    Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    Pending : The connection has been approved, and is being initialized.
    Available : The network link is up, and the connection is ready for use.
    Down : The network link is down.
    Deleting : The connection is in the process of being deleted.
    Deleted : The connection has been deleted.
    Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    
    """
    pass

def describe_loa(connectionId=None, providerName=None, loaContentType=None):
    """
    Returns the LOA-CFA for a connection, interconnect, or link aggregation group (LAG).
    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to AWS at the colocation facility. For more information, see Requesting Cross Connects at AWS Direct Connect Locations in the AWS Direct Connect user guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_loa(
        connectionId='string',
        providerName='string',
        loaContentType='application/pdf'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of a connection, LAG, or interconnect for which to get the LOA-CFA information.
            Example: dxcon-abc123 or dxlag-abc123
            Default: None
            

    :type providerName: string
    :param providerName: The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.
            Default: None
            

    :type loaContentType: string
    :param loaContentType: A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is 'application/pdf'.
            Default: application/pdf
            

    :rtype: dict
    :return: {
        'loaContent': b'bytes',
        'loaContentType': 'application/pdf'
    }
    
    
    """
    pass

def describe_locations():
    """
    Returns the list of AWS Direct Connect locations in the current AWS region. These are the locations that may be selected when calling CreateConnection or CreateInterconnect.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_locations()
    
    
    :rtype: dict
    :return: {
        'locations': [
            {
                'locationCode': 'string',
                'locationName': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_tags(resourceArns=None):
    """
    Describes the tags associated with the specified Direct Connect resources.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_tags(
        resourceArns=[
            'string',
        ]
    )
    
    
    :type resourceArns: list
    :param resourceArns: [REQUIRED]
            The Amazon Resource Names (ARNs) of the Direct Connect resources.
            (string) --
            

    :rtype: dict
    :return: {
        'resourceTags': [
            {
                'resourceArn': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_virtual_gateways():
    """
    Returns a list of virtual private gateways owned by the AWS account.
    You can create one or more AWS Direct Connect private virtual interfaces linking to a virtual private gateway. A virtual private gateway can be managed via Amazon Virtual Private Cloud (VPC) console or the EC2 CreateVpnGateway action.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_virtual_gateways()
    
    
    :rtype: dict
    :return: {
        'virtualGateways': [
            {
                'virtualGatewayId': 'string',
                'virtualGatewayState': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_virtual_interfaces(connectionId=None, virtualInterfaceId=None):
    """
    Displays all virtual interfaces for an AWS account. Virtual interfaces deleted fewer than 15 minutes before you make the request are also returned. If you specify a connection ID, only the virtual interfaces associated with the connection are returned. If you specify a virtual interface ID, then only a single virtual interface is returned.
    A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_virtual_interfaces(
        connectionId='string',
        virtualInterfaceId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).
            Example: dxcon-fg5678gh
            Default: None
            

    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface.
            Example: dxvif-123dfg56
            Default: None
            

    :rtype: dict
    :return: {
        'virtualInterfaces': [
            {
                'ownerAccount': 'string',
                'virtualInterfaceId': 'string',
                'location': 'string',
                'connectionId': 'string',
                'virtualInterfaceType': 'string',
                'virtualInterfaceName': 'string',
                'vlan': 123,
                'asn': 123,
                'authKey': 'string',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'customerRouterConfig': 'string',
                'virtualGatewayId': 'string',
                'routeFilterPrefixes': [
                    {
                        'cidr': 'string'
                    },
                ],
                'bgpPeers': [
                    {
                        'asn': 123,
                        'authKey': 'string',
                        'addressFamily': 'ipv4'|'ipv6',
                        'amazonAddress': 'string',
                        'customerAddress': 'string',
                        'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                        'bgpStatus': 'up'|'down'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ipv4 : IPv4 address family
    ipv6 : IPv6 address family
    
    """
    pass

def disassociate_connection_from_lag(connectionId=None, lagId=None):
    """
    Disassociates a connection from a link aggregation group (LAG). The connection is interrupted and re-established as a standalone connection (the connection is not deleted; to delete the connection, use the  DeleteConnection request). If the LAG has associated virtual interfaces or hosted connections, they remain associated with the LAG. A disassociated connection owned by an AWS Direct Connect partner is automatically converted to an interconnect.
    If disassociating the connection will cause the LAG to fall below its setting for minimum number of operational connections, the request fails, except when it's the last member of the LAG. If all connections are disassociated, the LAG continues to exist as an empty LAG with no physical connections.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_connection_from_lag(
        connectionId='string',
        lagId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]
            The ID of the connection to disassociate from the LAG.
            Example: dxcon-abc123
            Default: None
            

    :type lagId: string
    :param lagId: [REQUIRED]
            The ID of the LAG.
            Example: dxlag-abc123
            Default: None
            

    :rtype: dict
    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string'
    }
    
    
    :returns: 
    Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    Pending : The connection has been approved, and is being initialized.
    Available : The network link is up, and the connection is ready for use.
    Down : The network link is down.
    Deleting : The connection is in the process of being deleted.
    Deleted : The connection has been deleted.
    Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
    
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

def tag_resource(resourceArn=None, tags=None):
    """
    Adds the specified tags to the specified Direct Connect resource. Each Direct Connect resource can have a maximum of 50 tags.
    Each tag consists of a key and an optional value. If a tag with the same key is already associated with the Direct Connect resource, this action updates its value.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the Direct Connect resource.
            Example: arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-fg5678gh
            

    :type tags: list
    :param tags: [REQUIRED]
            The list of tags to add.
            (dict) --Information about a tag.
            key (string) -- [REQUIRED]The key of the tag.
            value (string) --The value of the tag.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes one or more tags from the specified Direct Connect resource.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the Direct Connect resource.
            

    :type tagKeys: list
    :param tagKeys: [REQUIRED]
            The list of tag keys to remove.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_lag(lagId=None, lagName=None, minimumLinks=None):
    """
    Updates the attributes of a link aggregation group (LAG).
    You can update the following attributes:
    When you create a LAG, the default value for the minimum number of operational connections is zero (0). If you update this value, and the number of operational connections falls below the specified value, the LAG will automatically go down to avoid overutilization of the remaining connections. Adjusting this value should be done with care as it could force the LAG down if the value is set higher than the current number of operational connections.
    See also: AWS API Documentation
    
    
    :example: response = client.update_lag(
        lagId='string',
        lagName='string',
        minimumLinks=123
    )
    
    
    :type lagId: string
    :param lagId: [REQUIRED]
            The ID of the LAG to update.
            Example: dxlag-abc123
            Default: None
            

    :type lagName: string
    :param lagName: The name for the LAG.
            Example: '3x10G LAG to AWS '
            Default: None
            

    :type minimumLinks: integer
    :param minimumLinks: The minimum number of physical connections that must be operational for the LAG itself to be operational.
            Default: None
            

    :rtype: dict
    :return: {
        'connectionsBandwidth': 'string',
        'numberOfConnections': 123,
        'lagId': 'string',
        'ownerAccount': 'string',
        'lagName': 'string',
        'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
        'location': 'string',
        'region': 'string',
        'minimumLinks': 123,
        'awsDevice': 'string',
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string'
            },
        ],
        'allowsHostedConnections': True|False
    }
    
    
    :returns: 
    lagId (string) -- [REQUIRED]
    The ID of the LAG to update.
    Example: dxlag-abc123
    Default: None
    
    lagName (string) -- The name for the LAG.
    Example: "3x10G LAG to AWS "
    Default: None
    
    minimumLinks (integer) -- The minimum number of physical connections that must be operational for the LAG itself to be operational.
    Default: None
    
    
    """
    pass

