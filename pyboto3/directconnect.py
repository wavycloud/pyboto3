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

def accept_direct_connect_gateway_association_proposal(directConnectGatewayId=None, proposalId=None, associatedGatewayOwnerAccount=None, overrideAllowedPrefixesToDirectConnectGateway=None):
    """
    Accepts a proposal request to attach a virtual private gateway or transit gateway to a Direct Connect gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_direct_connect_gateway_association_proposal(
        directConnectGatewayId='string',
        proposalId='string',
        associatedGatewayOwnerAccount='string',
        overrideAllowedPrefixesToDirectConnectGateway=[
            {
                'cidr': 'string'
            },
        ]
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: [REQUIRED]\nThe ID of the Direct Connect gateway.\n

    :type proposalId: string
    :param proposalId: [REQUIRED]\nThe ID of the request proposal.\n

    :type associatedGatewayOwnerAccount: string
    :param associatedGatewayOwnerAccount: [REQUIRED]\nThe ID of the AWS account that owns the virtual private gateway or transit gateway.\n

    :type overrideAllowedPrefixesToDirectConnectGateway: list
    :param overrideAllowedPrefixesToDirectConnectGateway: Overrides the Amazon VPC prefixes advertised to the Direct Connect gateway.\nFor information about how to set the prefixes, see Allowed Prefixes in the AWS Direct Connect User Guide .\n\n(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.\n\ncidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGatewayAssociation': {
        'directConnectGatewayId': 'string',
        'directConnectGatewayOwnerAccount': 'string',
        'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
        'stateChangeError': 'string',
        'associatedGateway': {
            'id': 'string',
            'type': 'virtualPrivateGateway'|'transitGateway',
            'ownerAccount': 'string',
            'region': 'string'
        },
        'associationId': 'string',
        'allowedPrefixesToDirectConnectGateway': [
            {
                'cidr': 'string'
            },
        ],
        'virtualGatewayId': 'string',
        'virtualGatewayRegion': 'string',
        'virtualGatewayOwnerAccount': 'string'
    }
}


Response Structure

(dict) --

directConnectGatewayAssociation (dict) --
Information about an association between a Direct Connect gateway and a virtual private gateway or transit gateway.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount (string) --
The ID of the AWS account that owns the associated gateway.

associationState (string) --
The state of the association. The following are the possible values:

associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.


stateChangeError (string) --
The error message if the state of an object failed to advance.

associatedGateway (dict) --
Information about the associated gateway.

id (string) --
The ID of the associated gateway.

type (string) --
The type of associated gateway.

ownerAccount (string) --
The ID of the AWS account that owns the associated virtual private gateway or transit gateway.

region (string) --
The Region where the associated gateway is located.



associationId (string) --
The ID of the Direct Connect gateway association.

allowedPrefixesToDirectConnectGateway (list) --
The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

virtualGatewayRegion (string) --
The AWS Region where the virtual private gateway is located.

virtualGatewayOwnerAccount (string) --
The ID of the AWS account that owns the virtual private gateway.









Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGatewayAssociation': {
            'directConnectGatewayId': 'string',
            'directConnectGatewayOwnerAccount': 'string',
            'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
            'stateChangeError': 'string',
            'associatedGateway': {
                'id': 'string',
                'type': 'virtualPrivateGateway'|'transitGateway',
                'ownerAccount': 'string',
                'region': 'string'
            },
            'associationId': 'string',
            'allowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ],
            'virtualGatewayId': 'string',
            'virtualGatewayRegion': 'string',
            'virtualGatewayOwnerAccount': 'string'
        }
    }
    
    
    :returns: 
    associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
    associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
    disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
    disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.
    
    """
    pass

def allocate_connection_on_interconnect(bandwidth=None, connectionName=None, ownerAccount=None, interconnectId=None, vlan=None):
    """
    Deprecated. Use  AllocateHostedConnection instead.
    Creates a hosted connection on an interconnect.
    Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the specified interconnect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.allocate_connection_on_interconnect(
        bandwidth='string',
        connectionName='string',
        ownerAccount='string',
        interconnectId='string',
        vlan=123
    )
    
    
    :type bandwidth: string
    :param bandwidth: [REQUIRED]\nThe bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, and 10Gbps. Note that only those AWS Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps or 10Gbps hosted connection.\n

    :type connectionName: string
    :param connectionName: [REQUIRED]\nThe name of the provisioned connection.\n

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]\nThe ID of the AWS account of the customer for whom the connection will be provisioned.\n

    :type interconnectId: string
    :param interconnectId: [REQUIRED]\nThe ID of the interconnect on which the connection will be provisioned.\n

    :type vlan: integer
    :param vlan: [REQUIRED]\nThe dedicated VLAN provisioned to the connection.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'connectionId': 'string',
    'connectionName': 'string',
    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'region': 'string',
    'location': 'string',
    'bandwidth': 'string',
    'vlan': 123,
    'partnerName': 'string',
    'loaIssueTime': datetime(2015, 1, 1),
    'lagId': 'string',
    'awsDevice': 'string',
    'jumboFrameCapable': True|False,
    'awsDeviceV2': 'string',
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --
Information about an AWS Direct Connect connection.

ownerAccount (string) --
The ID of the AWS account that owns the connection.

connectionId (string) --
The ID of the connection.

connectionName (string) --
The name of the connection.

connectionState (string) --
The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --
The AWS Region where the connection is located.

location (string) --
The location of the connection.

bandwidth (string) --
The bandwidth of the connection.

vlan (integer) --
The ID of the VLAN.

partnerName (string) --
The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --
The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --
The ID of the LAG.

awsDevice (string) --
The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the connection.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the connection.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    unknown : The state of the connection is not available.
    
    """
    pass

def allocate_hosted_connection(connectionId=None, ownerAccount=None, bandwidth=None, connectionName=None, vlan=None, tags=None):
    """
    Creates a hosted connection on the specified interconnect or a link aggregation group (LAG) of interconnects.
    Allocates a VLAN number and a specified amount of capacity (bandwidth) for use by a hosted connection on the specified interconnect or LAG of interconnects. AWS polices the hosted connection for the specified capacity and the AWS Direct Connect Partner must also police the hosted connection for the specified capacity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.allocate_hosted_connection(
        connectionId='string',
        ownerAccount='string',
        bandwidth='string',
        connectionName='string',
        vlan=123,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the interconnect or LAG.\n

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]\nThe ID of the AWS account ID of the customer for the connection.\n

    :type bandwidth: string
    :param bandwidth: [REQUIRED]\nThe bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, and 10Gbps. Note that only those AWS Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps or 10Gbps hosted connection.\n

    :type connectionName: string
    :param connectionName: [REQUIRED]\nThe name of the hosted connection.\n

    :type vlan: integer
    :param vlan: [REQUIRED]\nThe dedicated VLAN provisioned to the hosted connection.\n

    :type tags: list
    :param tags: The tags associated with the connection.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'connectionId': 'string',
    'connectionName': 'string',
    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'region': 'string',
    'location': 'string',
    'bandwidth': 'string',
    'vlan': 123,
    'partnerName': 'string',
    'loaIssueTime': datetime(2015, 1, 1),
    'lagId': 'string',
    'awsDevice': 'string',
    'jumboFrameCapable': True|False,
    'awsDeviceV2': 'string',
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --
Information about an AWS Direct Connect connection.

ownerAccount (string) --
The ID of the AWS account that owns the connection.

connectionId (string) --
The ID of the connection.

connectionName (string) --
The name of the connection.

connectionState (string) --
The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --
The AWS Region where the connection is located.

location (string) --
The location of the connection.

bandwidth (string) --
The bandwidth of the connection.

vlan (integer) --
The ID of the VLAN.

partnerName (string) --
The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --
The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --
The ID of the LAG.

awsDevice (string) --
The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the connection.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the connection.







Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    unknown : The state of the connection is not available.
    
    """
    pass

def allocate_private_virtual_interface(connectionId=None, ownerAccount=None, newPrivateVirtualInterfaceAllocation=None):
    """
    Provisions a private virtual interface to be owned by the specified AWS account.
    Virtual interfaces created using this action must be confirmed by the owner using  ConfirmPrivateVirtualInterface . Until then, the virtual interface is in the Confirming state and is not available to handle traffic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.allocate_private_virtual_interface(
        connectionId='string',
        ownerAccount='string',
        newPrivateVirtualInterfaceAllocation={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'mtu': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'customerAddress': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection on which the private virtual interface is provisioned.\n

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]\nThe ID of the AWS account that owns the virtual private interface.\n

    :type newPrivateVirtualInterfaceAllocation: dict
    :param newPrivateVirtualInterfaceAllocation: [REQUIRED]\nInformation about the private virtual interface.\n\nvirtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer network.\n\nvlan (integer) -- [REQUIRED]The ID of the VLAN.\n\nasn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.\nThe valid values are 1-2147483647.\n\nmtu (integer) --The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.\n\nauthKey (string) --The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.\n\namazonAddress (string) --The IP address assigned to the Amazon interface.\n\naddressFamily (string) --The address family for the BGP peer.\n\ncustomerAddress (string) --The IP address assigned to the customer interface.\n\ntags (list) --The tags associated with the private virtual interface.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'virtualInterfaceId': 'string',
    'location': 'string',
    'connectionId': 'string',
    'virtualInterfaceType': 'string',
    'virtualInterfaceName': 'string',
    'vlan': 123,
    'asn': 123,
    'amazonSideAsn': 123,
    'authKey': 'string',
    'amazonAddress': 'string',
    'customerAddress': 'string',
    'addressFamily': 'ipv4'|'ipv6',
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'customerRouterConfig': 'string',
    'mtu': 123,
    'jumboFrameCapable': True|False,
    'virtualGatewayId': 'string',
    'directConnectGatewayId': 'string',
    'routeFilterPrefixes': [
        {
            'cidr': 'string'
        },
    ],
    'bgpPeers': [
        {
            'bgpPeerId': 'string',
            'asn': 123,
            'authKey': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
            'bgpStatus': 'up'|'down'|'unknown',
            'awsDeviceV2': 'string'
        },
    ],
    'region': 'string',
    'awsDeviceV2': 'string',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
Information about a virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.











Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def allocate_public_virtual_interface(connectionId=None, ownerAccount=None, newPublicVirtualInterfaceAllocation=None):
    """
    Provisions a public virtual interface to be owned by the specified AWS account.
    The owner of a connection calls this function to provision a public virtual interface to be owned by the specified AWS account.
    Virtual interfaces created using this function must be confirmed by the owner using  ConfirmPublicVirtualInterface . Until this step has been completed, the virtual interface is in the confirming state and is not available to handle traffic.
    When creating an IPv6 public virtual interface, omit the Amazon address and customer address. IPv6 addresses are automatically assigned from the Amazon pool of IPv6 addresses; you cannot specify custom IPv6 addresses.
    See also: AWS API Documentation
    
    Exceptions
    
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
            ],
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection on which the public virtual interface is provisioned.\n

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]\nThe ID of the AWS account that owns the public virtual interface.\n

    :type newPublicVirtualInterfaceAllocation: dict
    :param newPublicVirtualInterfaceAllocation: [REQUIRED]\nInformation about the public virtual interface.\n\nvirtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer network.\n\nvlan (integer) -- [REQUIRED]The ID of the VLAN.\n\nasn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.\nThe valid values are 1-2147483647.\n\nauthKey (string) --The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.\n\namazonAddress (string) --The IP address assigned to the Amazon interface.\n\ncustomerAddress (string) --The IP address assigned to the customer interface.\n\naddressFamily (string) --The address family for the BGP peer.\n\nrouteFilterPrefixes (list) --The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.\n\n(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.\n\ncidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.\n\n\n\n\n\ntags (list) --The tags associated with the public virtual interface.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'virtualInterfaceId': 'string',
    'location': 'string',
    'connectionId': 'string',
    'virtualInterfaceType': 'string',
    'virtualInterfaceName': 'string',
    'vlan': 123,
    'asn': 123,
    'amazonSideAsn': 123,
    'authKey': 'string',
    'amazonAddress': 'string',
    'customerAddress': 'string',
    'addressFamily': 'ipv4'|'ipv6',
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'customerRouterConfig': 'string',
    'mtu': 123,
    'jumboFrameCapable': True|False,
    'virtualGatewayId': 'string',
    'directConnectGatewayId': 'string',
    'routeFilterPrefixes': [
        {
            'cidr': 'string'
        },
    ],
    'bgpPeers': [
        {
            'bgpPeerId': 'string',
            'asn': 123,
            'authKey': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
            'bgpStatus': 'up'|'down'|'unknown',
            'awsDeviceV2': 'string'
        },
    ],
    'region': 'string',
    'awsDeviceV2': 'string',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
Information about a virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.











Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def allocate_transit_virtual_interface(connectionId=None, ownerAccount=None, newTransitVirtualInterfaceAllocation=None):
    """
    Provisions a transit virtual interface to be owned by the specified AWS account. Use this type of interface to connect a transit gateway to your Direct Connect gateway.
    The owner of a connection provisions a transit virtual interface to be owned by the specified AWS account.
    After you create a transit virtual interface, it must be confirmed by the owner using  ConfirmTransitVirtualInterface . Until this step has been completed, the transit virtual interface is in the requested state and is not available to handle traffic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.allocate_transit_virtual_interface(
        connectionId='string',
        ownerAccount='string',
        newTransitVirtualInterfaceAllocation={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'mtu': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection on which the transit virtual interface is provisioned.\n

    :type ownerAccount: string
    :param ownerAccount: [REQUIRED]\nThe ID of the AWS account that owns the transit virtual interface.\n

    :type newTransitVirtualInterfaceAllocation: dict
    :param newTransitVirtualInterfaceAllocation: [REQUIRED]\nInformation about the transit virtual interface.\n\nvirtualInterfaceName (string) --The name of the virtual interface assigned by the customer network.\n\nvlan (integer) --The ID of the VLAN.\n\nasn (integer) --The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.\nThe valid values are 1-2147483647.\n\nmtu (integer) --The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.\n\nauthKey (string) --The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.\n\namazonAddress (string) --The IP address assigned to the Amazon interface.\n\ncustomerAddress (string) --The IP address assigned to the customer interface.\n\naddressFamily (string) --The address family for the BGP peer.\n\ntags (list) --The tags associated with the transitive virtual interface.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualInterface': {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

virtualInterface (dict) --
Information about a virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.













Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


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
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'customerRouterConfig': 'string',
            'mtu': 123,
            'jumboFrameCapable': True|False,
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'bgpPeerId': 'string',
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'|'unknown',
                    'awsDeviceV2': 'string'
                },
            ],
            'region': 'string',
            'awsDeviceV2': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def associate_connection_with_lag(connectionId=None, lagId=None):
    """
    Associates an existing connection with a link aggregation group (LAG). The connection is interrupted and re-established as a member of the LAG (connectivity to AWS is interrupted). The connection must be hosted on the same AWS Direct Connect endpoint as the LAG, and its bandwidth must match the bandwidth for the LAG. You can re-associate a connection that\'s currently associated with a different LAG; however, if removing the connection would cause the original LAG to fall below its setting for minimum number of operational connections, the request fails.
    Any virtual interfaces that are directly associated with the connection are automatically re-associated with the LAG. If the connection was originally associated with a different LAG, the virtual interfaces remain associated with the original LAG.
    For interconnects, any hosted connections are automatically re-associated with the LAG. If the interconnect was originally associated with a different LAG, the hosted connections remain associated with the original LAG.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_connection_with_lag(
        connectionId='string',
        lagId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection.\n

    :type lagId: string
    :param lagId: [REQUIRED]\nThe ID of the LAG with which to associate the connection.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'connectionId': 'string',
    'connectionName': 'string',
    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'region': 'string',
    'location': 'string',
    'bandwidth': 'string',
    'vlan': 123,
    'partnerName': 'string',
    'loaIssueTime': datetime(2015, 1, 1),
    'lagId': 'string',
    'awsDevice': 'string',
    'jumboFrameCapable': True|False,
    'awsDeviceV2': 'string',
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --
Information about an AWS Direct Connect connection.

ownerAccount (string) --
The ID of the AWS account that owns the connection.

connectionId (string) --
The ID of the connection.

connectionName (string) --
The name of the connection.

connectionState (string) --
The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --
The AWS Region where the connection is located.

location (string) --
The location of the connection.

bandwidth (string) --
The bandwidth of the connection.

vlan (integer) --
The ID of the VLAN.

partnerName (string) --
The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --
The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --
The ID of the LAG.

awsDevice (string) --
The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the connection.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the connection.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    unknown : The state of the connection is not available.
    
    """
    pass

def associate_hosted_connection(connectionId=None, parentConnectionId=None):
    """
    Associates a hosted connection and its virtual interfaces with a link aggregation group (LAG) or interconnect. If the target interconnect or LAG has an existing hosted connection with a conflicting VLAN number or IP address, the operation fails. This action temporarily interrupts the hosted connection\'s connectivity to AWS as it is being migrated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_hosted_connection(
        connectionId='string',
        parentConnectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the hosted connection.\n

    :type parentConnectionId: string
    :param parentConnectionId: [REQUIRED]\nThe ID of the interconnect or the LAG.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'connectionId': 'string',
    'connectionName': 'string',
    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'region': 'string',
    'location': 'string',
    'bandwidth': 'string',
    'vlan': 123,
    'partnerName': 'string',
    'loaIssueTime': datetime(2015, 1, 1),
    'lagId': 'string',
    'awsDevice': 'string',
    'jumboFrameCapable': True|False,
    'awsDeviceV2': 'string',
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --
Information about an AWS Direct Connect connection.

ownerAccount (string) --
The ID of the AWS account that owns the connection.

connectionId (string) --
The ID of the connection.

connectionName (string) --
The name of the connection.

connectionState (string) --
The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --
The AWS Region where the connection is located.

location (string) --
The location of the connection.

bandwidth (string) --
The bandwidth of the connection.

vlan (integer) --
The ID of the VLAN.

partnerName (string) --
The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --
The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --
The ID of the LAG.

awsDevice (string) --
The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the connection.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the connection.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    unknown : The state of the connection is not available.
    
    """
    pass

def associate_virtual_interface(virtualInterfaceId=None, connectionId=None):
    """
    Associates a virtual interface with a specified link aggregation group (LAG) or connection. Connectivity to AWS is temporarily interrupted as the virtual interface is being migrated. If the target connection or LAG has an associated virtual interface with a conflicting VLAN number or a conflicting IP address, the operation fails.
    Virtual interfaces associated with a hosted connection cannot be associated with a LAG; hosted connections must be migrated along with their virtual interfaces using  AssociateHostedConnection .
    To reassociate a virtual interface to a new connection or LAG, the requester must own either the virtual interface itself or the connection to which the virtual interface is currently associated. Additionally, the requester must own the connection or LAG for the association.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_virtual_interface(
        virtualInterfaceId='string',
        connectionId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]\nThe ID of the virtual interface.\n

    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the LAG or connection.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'virtualInterfaceId': 'string',
    'location': 'string',
    'connectionId': 'string',
    'virtualInterfaceType': 'string',
    'virtualInterfaceName': 'string',
    'vlan': 123,
    'asn': 123,
    'amazonSideAsn': 123,
    'authKey': 'string',
    'amazonAddress': 'string',
    'customerAddress': 'string',
    'addressFamily': 'ipv4'|'ipv6',
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'customerRouterConfig': 'string',
    'mtu': 123,
    'jumboFrameCapable': True|False,
    'virtualGatewayId': 'string',
    'directConnectGatewayId': 'string',
    'routeFilterPrefixes': [
        {
            'cidr': 'string'
        },
    ],
    'bgpPeers': [
        {
            'bgpPeerId': 'string',
            'asn': 123,
            'authKey': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
            'bgpStatus': 'up'|'down'|'unknown',
            'awsDeviceV2': 'string'
        },
    ],
    'region': 'string',
    'awsDeviceV2': 'string',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
Information about a virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.











Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def confirm_connection(connectionId=None):
    """
    Confirms the creation of the specified hosted connection on an interconnect.
    Upon creation, the hosted connection is initially in the Ordering state, and remains in this state until the owner confirms creation of the hosted connection.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.confirm_connection(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the hosted connection.\n

    :rtype: dict
ReturnsResponse Syntax{
    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
}


Response Structure

(dict) --
connectionState (string) --The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def confirm_private_virtual_interface(virtualInterfaceId=None, virtualGatewayId=None, directConnectGatewayId=None):
    """
    Accepts ownership of a private virtual interface created by another AWS account.
    After the virtual interface owner makes this call, the virtual interface is created and attached to the specified virtual private gateway or Direct Connect gateway, and is made available to handle traffic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.confirm_private_virtual_interface(
        virtualInterfaceId='string',
        virtualGatewayId='string',
        directConnectGatewayId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]\nThe ID of the virtual interface.\n

    :type virtualGatewayId: string
    :param virtualGatewayId: The ID of the virtual private gateway.

    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
}


Response Structure

(dict) --

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.








Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def confirm_public_virtual_interface(virtualInterfaceId=None):
    """
    Accepts ownership of a public virtual interface created by another AWS account.
    After the virtual interface owner makes this call, the specified virtual interface is created and made available to handle traffic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.confirm_public_virtual_interface(
        virtualInterfaceId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]\nThe ID of the virtual interface.\n

    :rtype: dict
ReturnsResponse Syntax{
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
}


Response Structure

(dict) --
virtualInterfaceState (string) --The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def confirm_transit_virtual_interface(virtualInterfaceId=None, directConnectGatewayId=None):
    """
    Accepts ownership of a transit virtual interface created by another AWS account.
    After the owner of the transit virtual interface makes this call, the specified transit virtual interface is created and made available to handle traffic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.confirm_transit_virtual_interface(
        virtualInterfaceId='string',
        directConnectGatewayId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]\nThe ID of the virtual interface.\n

    :type directConnectGatewayId: string
    :param directConnectGatewayId: [REQUIRED]\nThe ID of the Direct Connect gateway.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
}


Response Structure

(dict) --

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.








Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def create_bgp_peer(virtualInterfaceId=None, newBGPPeer=None):
    """
    Creates a BGP peer on the specified virtual interface.
    You must create a BGP peer for the corresponding address family (IPv4/IPv6) in order to access AWS resources that also use that address family.
    If logical redundancy is not supported by the connection, interconnect, or LAG, the BGP peer cannot be in the same address family as an existing BGP peer on the virtual interface.
    When creating a IPv6 BGP peer, omit the Amazon address and customer address. IPv6 addresses are automatically assigned from the Amazon pool of IPv6 addresses; you cannot specify custom IPv6 addresses.
    For a public virtual interface, the Autonomous System Number (ASN) must be private or already whitelisted for the virtual interface.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param virtualInterfaceId: The ID of the virtual interface.

    :type newBGPPeer: dict
    :param newBGPPeer: Information about the BGP peer.\n\nasn (integer) --The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.\n\nauthKey (string) --The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.\n\naddressFamily (string) --The address family for the BGP peer.\n\namazonAddress (string) --The IP address assigned to the Amazon interface.\n\ncustomerAddress (string) --The IP address assigned to the customer interface.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualInterface': {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

virtualInterface (dict) --
The virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.













Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


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
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'customerRouterConfig': 'string',
            'mtu': 123,
            'jumboFrameCapable': True|False,
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'bgpPeerId': 'string',
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'|'unknown',
                    'awsDeviceV2': 'string'
                },
            ],
            'region': 'string',
            'awsDeviceV2': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def create_connection(location=None, bandwidth=None, connectionName=None, lagId=None, tags=None, providerName=None):
    """
    Creates a connection between a customer network and a specific AWS Direct Connect location.
    A connection links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router.
    To find the locations for your Region, use  DescribeLocations .
    You can automatically add the new connection to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new connection is allocated on the same AWS Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no connection is created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_connection(
        location='string',
        bandwidth='string',
        connectionName='string',
        lagId='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        providerName='string'
    )
    
    
    :type location: string
    :param location: [REQUIRED]\nThe location of the connection.\n

    :type bandwidth: string
    :param bandwidth: [REQUIRED]\nThe bandwidth of the connection.\n

    :type connectionName: string
    :param connectionName: [REQUIRED]\nThe name of the connection.\n

    :type lagId: string
    :param lagId: The ID of the LAG.

    :type tags: list
    :param tags: The tags to associate with the lag.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n

    :type providerName: string
    :param providerName: The name of the service provider associated with the requested connection.

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'connectionId': 'string',
    'connectionName': 'string',
    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'region': 'string',
    'location': 'string',
    'bandwidth': 'string',
    'vlan': 123,
    'partnerName': 'string',
    'loaIssueTime': datetime(2015, 1, 1),
    'lagId': 'string',
    'awsDevice': 'string',
    'jumboFrameCapable': True|False,
    'awsDeviceV2': 'string',
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --
Information about an AWS Direct Connect connection.

ownerAccount (string) --
The ID of the AWS account that owns the connection.

connectionId (string) --
The ID of the connection.

connectionName (string) --
The name of the connection.

connectionState (string) --
The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --
The AWS Region where the connection is located.

location (string) --
The location of the connection.

bandwidth (string) --
The bandwidth of the connection.

vlan (integer) --
The ID of the VLAN.

partnerName (string) --
The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --
The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --
The ID of the LAG.

awsDevice (string) --
The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the connection.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the connection.







Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    unknown : The state of the connection is not available.
    
    """
    pass

def create_direct_connect_gateway(directConnectGatewayName=None, amazonSideAsn=None):
    """
    Creates a Direct Connect gateway, which is an intermediate object that enables you to connect a set of virtual interfaces and virtual private gateways. A Direct Connect gateway is global and visible in any AWS Region after it is created. The virtual interfaces and virtual private gateways that are connected through a Direct Connect gateway can be in different AWS Regions. This enables you to connect to a VPC in any Region, regardless of the Region in which the virtual interfaces are located, and pass traffic between them.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_direct_connect_gateway(
        directConnectGatewayName='string',
        amazonSideAsn=123
    )
    
    
    :type directConnectGatewayName: string
    :param directConnectGatewayName: [REQUIRED]\nThe name of the Direct Connect gateway.\n

    :type amazonSideAsn: integer
    :param amazonSideAsn: The autonomous system number (ASN) for Border Gateway Protocol (BGP) to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294. The default is 64512.

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGateway': {
        'directConnectGatewayId': 'string',
        'directConnectGatewayName': 'string',
        'amazonSideAsn': 123,
        'ownerAccount': 'string',
        'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
        'stateChangeError': 'string'
    }
}


Response Structure

(dict) --

directConnectGateway (dict) --
The Direct Connect gateway.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

directConnectGatewayName (string) --
The name of the Direct Connect gateway.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

ownerAccount (string) --
The ID of the AWS account that owns the Direct Connect gateway.

directConnectGatewayState (string) --
The state of the Direct Connect gateway. The following are the possible values:

pending : The initial state after calling  CreateDirectConnectGateway .
available : The Direct Connect gateway is ready for use.
deleting : The initial state after calling  DeleteDirectConnectGateway .
deleted : The Direct Connect gateway is deleted and cannot pass traffic.


stateChangeError (string) --
The error message if the state of an object failed to advance.









Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGateway': {
            'directConnectGatewayId': 'string',
            'directConnectGatewayName': 'string',
            'amazonSideAsn': 123,
            'ownerAccount': 'string',
            'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
            'stateChangeError': 'string'
        }
    }
    
    
    :returns: 
    pending : The initial state after calling  CreateDirectConnectGateway .
    available : The Direct Connect gateway is ready for use.
    deleting : The initial state after calling  DeleteDirectConnectGateway .
    deleted : The Direct Connect gateway is deleted and cannot pass traffic.
    
    """
    pass

def create_direct_connect_gateway_association(directConnectGatewayId=None, gatewayId=None, addAllowedPrefixesToDirectConnectGateway=None, virtualGatewayId=None):
    """
    Creates an association between a Direct Connect gateway and a virtual private gateway. The virtual private gateway must be attached to a VPC and must not be associated with another Direct Connect gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_direct_connect_gateway_association(
        directConnectGatewayId='string',
        gatewayId='string',
        addAllowedPrefixesToDirectConnectGateway=[
            {
                'cidr': 'string'
            },
        ],
        virtualGatewayId='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: [REQUIRED]\nThe ID of the Direct Connect gateway.\n

    :type gatewayId: string
    :param gatewayId: The ID of the virtual private gateway or transit gateway.

    :type addAllowedPrefixesToDirectConnectGateway: list
    :param addAllowedPrefixesToDirectConnectGateway: The Amazon VPC prefixes to advertise to the Direct Connect gateway\nThis parameter is required when you create an association to a transit gateway.\nFor information about how to set the prefixes, see Allowed Prefixes in the AWS Direct Connect User Guide .\n\n(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.\n\ncidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.\n\n\n\n\n

    :type virtualGatewayId: string
    :param virtualGatewayId: The ID of the virtual private gateway.

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGatewayAssociation': {
        'directConnectGatewayId': 'string',
        'directConnectGatewayOwnerAccount': 'string',
        'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
        'stateChangeError': 'string',
        'associatedGateway': {
            'id': 'string',
            'type': 'virtualPrivateGateway'|'transitGateway',
            'ownerAccount': 'string',
            'region': 'string'
        },
        'associationId': 'string',
        'allowedPrefixesToDirectConnectGateway': [
            {
                'cidr': 'string'
            },
        ],
        'virtualGatewayId': 'string',
        'virtualGatewayRegion': 'string',
        'virtualGatewayOwnerAccount': 'string'
    }
}


Response Structure

(dict) --

directConnectGatewayAssociation (dict) --
The association to be created.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount (string) --
The ID of the AWS account that owns the associated gateway.

associationState (string) --
The state of the association. The following are the possible values:

associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.


stateChangeError (string) --
The error message if the state of an object failed to advance.

associatedGateway (dict) --
Information about the associated gateway.

id (string) --
The ID of the associated gateway.

type (string) --
The type of associated gateway.

ownerAccount (string) --
The ID of the AWS account that owns the associated virtual private gateway or transit gateway.

region (string) --
The Region where the associated gateway is located.



associationId (string) --
The ID of the Direct Connect gateway association.

allowedPrefixesToDirectConnectGateway (list) --
The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

virtualGatewayRegion (string) --
The AWS Region where the virtual private gateway is located.

virtualGatewayOwnerAccount (string) --
The ID of the AWS account that owns the virtual private gateway.









Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGatewayAssociation': {
            'directConnectGatewayId': 'string',
            'directConnectGatewayOwnerAccount': 'string',
            'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
            'stateChangeError': 'string',
            'associatedGateway': {
                'id': 'string',
                'type': 'virtualPrivateGateway'|'transitGateway',
                'ownerAccount': 'string',
                'region': 'string'
            },
            'associationId': 'string',
            'allowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ],
            'virtualGatewayId': 'string',
            'virtualGatewayRegion': 'string',
            'virtualGatewayOwnerAccount': 'string'
        }
    }
    
    
    :returns: 
    associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
    associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
    disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
    disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.
    
    """
    pass

def create_direct_connect_gateway_association_proposal(directConnectGatewayId=None, directConnectGatewayOwnerAccount=None, gatewayId=None, addAllowedPrefixesToDirectConnectGateway=None, removeAllowedPrefixesToDirectConnectGateway=None):
    """
    Creates a proposal to associate the specified virtual private gateway or transit gateway with the specified Direct Connect gateway.
    You can only associate a Direct Connect gateway and virtual private gateway or transit gateway when the account that owns the Direct Connect gateway and the account that owns the virtual private gateway or transit gateway have the same AWS Payer ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_direct_connect_gateway_association_proposal(
        directConnectGatewayId='string',
        directConnectGatewayOwnerAccount='string',
        gatewayId='string',
        addAllowedPrefixesToDirectConnectGateway=[
            {
                'cidr': 'string'
            },
        ],
        removeAllowedPrefixesToDirectConnectGateway=[
            {
                'cidr': 'string'
            },
        ]
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: [REQUIRED]\nThe ID of the Direct Connect gateway.\n

    :type directConnectGatewayOwnerAccount: string
    :param directConnectGatewayOwnerAccount: [REQUIRED]\nThe ID of the AWS account that owns the Direct Connect gateway.\n

    :type gatewayId: string
    :param gatewayId: [REQUIRED]\nThe ID of the virtual private gateway or transit gateway.\n

    :type addAllowedPrefixesToDirectConnectGateway: list
    :param addAllowedPrefixesToDirectConnectGateway: The Amazon VPC prefixes to advertise to the Direct Connect gateway.\n\n(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.\n\ncidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.\n\n\n\n\n

    :type removeAllowedPrefixesToDirectConnectGateway: list
    :param removeAllowedPrefixesToDirectConnectGateway: The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.\n\n(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.\n\ncidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGatewayAssociationProposal': {
        'proposalId': 'string',
        'directConnectGatewayId': 'string',
        'directConnectGatewayOwnerAccount': 'string',
        'proposalState': 'requested'|'accepted'|'deleted',
        'associatedGateway': {
            'id': 'string',
            'type': 'virtualPrivateGateway'|'transitGateway',
            'ownerAccount': 'string',
            'region': 'string'
        },
        'existingAllowedPrefixesToDirectConnectGateway': [
            {
                'cidr': 'string'
            },
        ],
        'requestedAllowedPrefixesToDirectConnectGateway': [
            {
                'cidr': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

directConnectGatewayAssociationProposal (dict) --
Information about the Direct Connect gateway proposal.

proposalId (string) --
The ID of the association proposal.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount (string) --
The ID of the AWS account that owns the Direct Connect gateway.

proposalState (string) --
The state of the proposal. The following are possible values:

accepted : The proposal has been accepted. The Direct Connect gateway association is available to use in this state.
deleted : The proposal has been deleted by the owner that made the proposal. The Direct Connect gateway association cannot be used in this state.
requested : The proposal has been requested. The Direct Connect gateway association cannot be used in this state.


associatedGateway (dict) --
Information about the associated gateway.

id (string) --
The ID of the associated gateway.

type (string) --
The type of associated gateway.

ownerAccount (string) --
The ID of the AWS account that owns the associated virtual private gateway or transit gateway.

region (string) --
The Region where the associated gateway is located.



existingAllowedPrefixesToDirectConnectGateway (list) --
The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





requestedAllowedPrefixesToDirectConnectGateway (list) --
The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.













Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGatewayAssociationProposal': {
            'proposalId': 'string',
            'directConnectGatewayId': 'string',
            'directConnectGatewayOwnerAccount': 'string',
            'proposalState': 'requested'|'accepted'|'deleted',
            'associatedGateway': {
                'id': 'string',
                'type': 'virtualPrivateGateway'|'transitGateway',
                'ownerAccount': 'string',
                'region': 'string'
            },
            'existingAllowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ],
            'requestedAllowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    accepted : The proposal has been accepted. The Direct Connect gateway association is available to use in this state.
    deleted : The proposal has been deleted by the owner that made the proposal. The Direct Connect gateway association cannot be used in this state.
    requested : The proposal has been requested. The Direct Connect gateway association cannot be used in this state.
    
    """
    pass

def create_interconnect(interconnectName=None, bandwidth=None, location=None, lagId=None, tags=None, providerName=None):
    """
    Creates an interconnect between an AWS Direct Connect Partner\'s network and a specific AWS Direct Connect location.
    An interconnect is a connection that is capable of hosting other connections. The AWS Direct Connect partner can use an interconnect to provide AWS Direct Connect hosted connections to customers through their own network services. Like a standard connection, an interconnect links the partner\'s network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end is connected to the partner\'s router, the other to an AWS Direct Connect router.
    You can automatically add the new interconnect to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new interconnect is allocated on the same AWS Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no interconnect is created.
    For each end customer, the AWS Direct Connect Partner provisions a connection on their interconnect by calling  AllocateHostedConnection . The end customer can then connect to AWS resources by creating a virtual interface on their connection, using the VLAN assigned to them by the AWS Direct Connect Partner.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_interconnect(
        interconnectName='string',
        bandwidth='string',
        location='string',
        lagId='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        providerName='string'
    )
    
    
    :type interconnectName: string
    :param interconnectName: [REQUIRED]\nThe name of the interconnect.\n

    :type bandwidth: string
    :param bandwidth: [REQUIRED]\nThe port bandwidth, in Gbps. The possible values are 1 and 10.\n

    :type location: string
    :param location: [REQUIRED]\nThe location of the interconnect.\n

    :type lagId: string
    :param lagId: The ID of the LAG.

    :type tags: list
    :param tags: The tags to associate with the interconnect.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n

    :type providerName: string
    :param providerName: The name of the service provider associated with the interconnect.

    :rtype: dict

ReturnsResponse Syntax
{
    'interconnectId': 'string',
    'interconnectName': 'string',
    'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
    'region': 'string',
    'location': 'string',
    'bandwidth': 'string',
    'loaIssueTime': datetime(2015, 1, 1),
    'lagId': 'string',
    'awsDevice': 'string',
    'jumboFrameCapable': True|False,
    'awsDeviceV2': 'string',
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --
Information about an interconnect.

interconnectId (string) --
The ID of the interconnect.

interconnectName (string) --
The name of the interconnect.

interconnectState (string) --
The state of the interconnect. The following are the possible values:

requested : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The interconnect is approved, and is being initialized.
available : The network link is up, and the interconnect is ready for use.
down : The network link is down.
deleting : The interconnect is being deleted.
deleted : The interconnect is deleted.
unknown : The state of the interconnect is not available.


region (string) --
The AWS Region where the connection is located.

location (string) --
The location of the connection.

bandwidth (string) --
The bandwidth of the connection.

loaIssueTime (datetime) --
The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --
The ID of the LAG.

awsDevice (string) --
The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --
Indicates whether the interconnect supports a secondary BGP in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the interconnect.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the interconnect.







Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'interconnectId': 'string',
        'interconnectName': 'string',
        'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    requested : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The interconnect is approved, and is being initialized.
    available : The network link is up, and the interconnect is ready for use.
    down : The network link is down.
    deleting : The interconnect is being deleted.
    deleted : The interconnect is deleted.
    unknown : The state of the interconnect is not available.
    
    """
    pass

def create_lag(numberOfConnections=None, location=None, connectionsBandwidth=None, lagName=None, connectionId=None, tags=None, childConnectionTags=None, providerName=None):
    """
    Creates a link aggregation group (LAG) with the specified number of bundled physical connections between the customer network and a specific AWS Direct Connect location. A LAG is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple interfaces, enabling you to treat them as a single interface.
    All connections in a LAG must use the same bandwidth and must terminate at the same AWS Direct Connect endpoint.
    You can have up to 10 connections per LAG. Regardless of this limit, if you request more connections for the LAG than AWS Direct Connect can allocate on a single endpoint, no LAG is created.
    You can specify an existing physical connection or interconnect to include in the LAG (which counts towards the total number of connections). Doing so interrupts the current physical connection or hosted connections, and re-establishes them as a member of the LAG. The LAG will be created on the same AWS Direct Connect endpoint to which the connection terminates. Any virtual interfaces associated with the connection are automatically disassociated and re-associated with the LAG. The connection ID does not change.
    If the AWS account used to create a LAG is a registered AWS Direct Connect Partner, the LAG is automatically enabled to host sub-connections. For a LAG owned by a partner, any associated virtual interfaces cannot be directly configured.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_lag(
        numberOfConnections=123,
        location='string',
        connectionsBandwidth='string',
        lagName='string',
        connectionId='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        childConnectionTags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        providerName='string'
    )
    
    
    :type numberOfConnections: integer
    :param numberOfConnections: [REQUIRED]\nThe number of physical connections initially provisioned and bundled by the LAG.\n

    :type location: string
    :param location: [REQUIRED]\nThe location for the LAG.\n

    :type connectionsBandwidth: string
    :param connectionsBandwidth: [REQUIRED]\nThe bandwidth of the individual physical connections bundled by the LAG. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, and 10Gbps.\n

    :type lagName: string
    :param lagName: [REQUIRED]\nThe name of the LAG.\n

    :type connectionId: string
    :param connectionId: The ID of an existing connection to migrate to the LAG.

    :type tags: list
    :param tags: The tags to associate with the LAG.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n

    :type childConnectionTags: list
    :param childConnectionTags: The tags to associate with the automtically created LAGs.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n

    :type providerName: string
    :param providerName: The name of the service provider associated with the LAG.

    :rtype: dict

ReturnsResponse Syntax
{
    'connectionsBandwidth': 'string',
    'numberOfConnections': 123,
    'lagId': 'string',
    'ownerAccount': 'string',
    'lagName': 'string',
    'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
    'location': 'string',
    'region': 'string',
    'minimumLinks': 123,
    'awsDevice': 'string',
    'awsDeviceV2': 'string',
    'connections': [
        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string',
            'jumboFrameCapable': True|False,
            'awsDeviceV2': 'string',
            'hasLogicalRedundancy': 'unknown'|'yes'|'no',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'providerName': 'string'
        },
    ],
    'allowsHostedConnections': True|False,
    'jumboFrameCapable': True|False,
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --
Information about a link aggregation group (LAG).

connectionsBandwidth (string) --
The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps and 10Gbps.

numberOfConnections (integer) --
The number of physical connections bundled by the LAG, up to a maximum of 10.

lagId (string) --
The ID of the LAG.

ownerAccount (string) --
The ID of the AWS account that owns the LAG.

lagName (string) --
The name of the LAG.

lagState (string) --
The state of the LAG. The following are the possible values:

requested : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
pending : The LAG has been approved and is being initialized.
available : The network link is established and the LAG is ready for use.
down : The network link is down.
deleting : The LAG is being deleted.
deleted : The LAG is deleted.
unknown : The state of the LAG is not available.


location (string) --
The location of the LAG.

region (string) --
The AWS Region where the connection is located.

minimumLinks (integer) --
The minimum number of physical connections that must be operational for the LAG itself to be operational.

awsDevice (string) --
The AWS Direct Connect endpoint that hosts the LAG.

awsDeviceV2 (string) --
The AWS Direct Connect endpoint that hosts the LAG.

connections (list) --
The connections bundled by the LAG.

(dict) --
Information about an AWS Direct Connect connection.

ownerAccount (string) --
The ID of the AWS account that owns the connection.

connectionId (string) --
The ID of the connection.

connectionName (string) --
The name of the connection.

connectionState (string) --
The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --
The AWS Region where the connection is located.

location (string) --
The location of the connection.

bandwidth (string) --
The bandwidth of the connection.

vlan (integer) --
The ID of the VLAN.

partnerName (string) --
The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --
The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --
The ID of the LAG.

awsDevice (string) --
The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the connection.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the connection.





allowsHostedConnections (boolean) --
Indicates whether the LAG can host other connections.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

hasLogicalRedundancy (string) --
Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the LAG.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the LAG.







Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'connectionsBandwidth': 'string',
        'numberOfConnections': 123,
        'lagId': 'string',
        'ownerAccount': 'string',
        'lagName': 'string',
        'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
        'location': 'string',
        'region': 'string',
        'minimumLinks': 123,
        'awsDevice': 'string',
        'awsDeviceV2': 'string',
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'providerName': 'string'
            },
        ],
        'allowsHostedConnections': True|False,
        'jumboFrameCapable': True|False,
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    requested : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
    pending : The LAG has been approved and is being initialized.
    available : The network link is established and the LAG is ready for use.
    down : The network link is down.
    deleting : The LAG is being deleted.
    deleted : The LAG is deleted.
    unknown : The state of the LAG is not available.
    
    """
    pass

def create_private_virtual_interface(connectionId=None, newPrivateVirtualInterface=None):
    """
    Creates a private virtual interface. A virtual interface is the VLAN that transports AWS Direct Connect traffic. A private virtual interface can be connected to either a Direct Connect gateway or a Virtual Private Gateway (VGW). Connecting the private virtual interface to a Direct Connect gateway enables the possibility for connecting to multiple VPCs, including VPCs in different AWS Regions. Connecting the private virtual interface to a VGW only provides access to a single VPC within the same Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_private_virtual_interface(
        connectionId='string',
        newPrivateVirtualInterface={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'mtu': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection.\n

    :type newPrivateVirtualInterface: dict
    :param newPrivateVirtualInterface: [REQUIRED]\nInformation about the private virtual interface.\n\nvirtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer network.\n\nvlan (integer) -- [REQUIRED]The ID of the VLAN.\n\nasn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.\nThe valid values are 1-2147483647.\n\nmtu (integer) --The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.\n\nauthKey (string) --The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.\n\namazonAddress (string) --The IP address assigned to the Amazon interface.\n\ncustomerAddress (string) --The IP address assigned to the customer interface.\n\naddressFamily (string) --The address family for the BGP peer.\n\nvirtualGatewayId (string) --The ID of the virtual private gateway.\n\ndirectConnectGatewayId (string) --The ID of the Direct Connect gateway.\n\ntags (list) --The tags associated with the private virtual interface.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'virtualInterfaceId': 'string',
    'location': 'string',
    'connectionId': 'string',
    'virtualInterfaceType': 'string',
    'virtualInterfaceName': 'string',
    'vlan': 123,
    'asn': 123,
    'amazonSideAsn': 123,
    'authKey': 'string',
    'amazonAddress': 'string',
    'customerAddress': 'string',
    'addressFamily': 'ipv4'|'ipv6',
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'customerRouterConfig': 'string',
    'mtu': 123,
    'jumboFrameCapable': True|False,
    'virtualGatewayId': 'string',
    'directConnectGatewayId': 'string',
    'routeFilterPrefixes': [
        {
            'cidr': 'string'
        },
    ],
    'bgpPeers': [
        {
            'bgpPeerId': 'string',
            'asn': 123,
            'authKey': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
            'bgpStatus': 'up'|'down'|'unknown',
            'awsDeviceV2': 'string'
        },
    ],
    'region': 'string',
    'awsDeviceV2': 'string',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
Information about a virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.











Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def create_public_virtual_interface(connectionId=None, newPublicVirtualInterface=None):
    """
    Creates a public virtual interface. A virtual interface is the VLAN that transports AWS Direct Connect traffic. A public virtual interface supports sending traffic to public services of AWS such as Amazon S3.
    When creating an IPv6 public virtual interface (addressFamily is ipv6 ), leave the customer and amazon address fields blank to use auto-assigned IPv6 space. Custom IPv6 addresses are not supported.
    See also: AWS API Documentation
    
    Exceptions
    
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
            ],
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection.\n

    :type newPublicVirtualInterface: dict
    :param newPublicVirtualInterface: [REQUIRED]\nInformation about the public virtual interface.\n\nvirtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer network.\n\nvlan (integer) -- [REQUIRED]The ID of the VLAN.\n\nasn (integer) -- [REQUIRED]The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.\nThe valid values are 1-2147483647.\n\nauthKey (string) --The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.\n\namazonAddress (string) --The IP address assigned to the Amazon interface.\n\ncustomerAddress (string) --The IP address assigned to the customer interface.\n\naddressFamily (string) --The address family for the BGP peer.\n\nrouteFilterPrefixes (list) --The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.\n\n(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.\n\ncidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.\n\n\n\n\n\ntags (list) --The tags associated with the public virtual interface.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'virtualInterfaceId': 'string',
    'location': 'string',
    'connectionId': 'string',
    'virtualInterfaceType': 'string',
    'virtualInterfaceName': 'string',
    'vlan': 123,
    'asn': 123,
    'amazonSideAsn': 123,
    'authKey': 'string',
    'amazonAddress': 'string',
    'customerAddress': 'string',
    'addressFamily': 'ipv4'|'ipv6',
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'customerRouterConfig': 'string',
    'mtu': 123,
    'jumboFrameCapable': True|False,
    'virtualGatewayId': 'string',
    'directConnectGatewayId': 'string',
    'routeFilterPrefixes': [
        {
            'cidr': 'string'
        },
    ],
    'bgpPeers': [
        {
            'bgpPeerId': 'string',
            'asn': 123,
            'authKey': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
            'bgpStatus': 'up'|'down'|'unknown',
            'awsDeviceV2': 'string'
        },
    ],
    'region': 'string',
    'awsDeviceV2': 'string',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
Information about a virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.











Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def create_transit_virtual_interface(connectionId=None, newTransitVirtualInterface=None):
    """
    Creates a transit virtual interface. A transit virtual interface should be used to access one or more transit gateways associated with Direct Connect gateways. A transit virtual interface enables the connection of multiple VPCs attached to a transit gateway to a Direct Connect gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_transit_virtual_interface(
        connectionId='string',
        newTransitVirtualInterface={
            'virtualInterfaceName': 'string',
            'vlan': 123,
            'asn': 123,
            'mtu': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'directConnectGatewayId': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection.\n

    :type newTransitVirtualInterface: dict
    :param newTransitVirtualInterface: [REQUIRED]\nInformation about the transit virtual interface.\n\nvirtualInterfaceName (string) --The name of the virtual interface assigned by the customer network.\n\nvlan (integer) --The ID of the VLAN.\n\nasn (integer) --The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.\nThe valid values are 1-2147483647.\n\nmtu (integer) --The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.\n\nauthKey (string) --The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.\n\namazonAddress (string) --The IP address assigned to the Amazon interface.\n\ncustomerAddress (string) --The IP address assigned to the customer interface.\n\naddressFamily (string) --The address family for the BGP peer.\n\ndirectConnectGatewayId (string) --The ID of the Direct Connect gateway.\n\ntags (list) --The tags associated with the transitive virtual interface.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualInterface': {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

virtualInterface (dict) --
Information about a virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.













Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


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
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'customerRouterConfig': 'string',
            'mtu': 123,
            'jumboFrameCapable': True|False,
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'bgpPeerId': 'string',
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'|'unknown',
                    'awsDeviceV2': 'string'
                },
            ],
            'region': 'string',
            'awsDeviceV2': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def delete_bgp_peer(virtualInterfaceId=None, asn=None, customerAddress=None, bgpPeerId=None):
    """
    Deletes the specified BGP peer on the specified virtual interface with the specified customer address and ASN.
    You cannot delete the last BGP peer from a virtual interface.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_bgp_peer(
        virtualInterfaceId='string',
        asn=123,
        customerAddress='string',
        bgpPeerId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface.

    :type asn: integer
    :param asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    :type customerAddress: string
    :param customerAddress: The IP address assigned to the customer interface.

    :type bgpPeerId: string
    :param bgpPeerId: The ID of the BGP peer.

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualInterface': {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

virtualInterface (dict) --
The virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.













Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


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
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'customerRouterConfig': 'string',
            'mtu': 123,
            'jumboFrameCapable': True|False,
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'bgpPeerId': 'string',
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'|'unknown',
                    'awsDeviceV2': 'string'
                },
            ],
            'region': 'string',
            'awsDeviceV2': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def delete_connection(connectionId=None):
    """
    Deletes the specified connection.
    Deleting a connection only stops the AWS Direct Connect port hour and data transfer charges. If you are partnering with any third parties to connect with the AWS Direct Connect location, you must cancel your service with them separately.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_connection(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ownerAccount': 'string',
    'connectionId': 'string',
    'connectionName': 'string',
    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'region': 'string',
    'location': 'string',
    'bandwidth': 'string',
    'vlan': 123,
    'partnerName': 'string',
    'loaIssueTime': datetime(2015, 1, 1),
    'lagId': 'string',
    'awsDevice': 'string',
    'jumboFrameCapable': True|False,
    'awsDeviceV2': 'string',
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --Information about an AWS Direct Connect connection.

ownerAccount (string) --The ID of the AWS account that owns the connection.

connectionId (string) --The ID of the connection.

connectionName (string) --The name of the connection.

connectionState (string) --The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --The AWS Region where the connection is located.

location (string) --The location of the connection.

bandwidth (string) --The bandwidth of the connection.

vlan (integer) --The ID of the VLAN.

partnerName (string) --The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --The ID of the LAG.

awsDevice (string) --The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --The tags associated with the connection.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.





providerName (string) --The name of the service provider associated with the connection.






Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def delete_direct_connect_gateway(directConnectGatewayId=None):
    """
    Deletes the specified Direct Connect gateway. You must first delete all virtual interfaces that are attached to the Direct Connect gateway and disassociate all virtual private gateways associated with the Direct Connect gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_direct_connect_gateway(
        directConnectGatewayId='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: [REQUIRED]\nThe ID of the Direct Connect gateway.\n

    :rtype: dict
ReturnsResponse Syntax{
    'directConnectGateway': {
        'directConnectGatewayId': 'string',
        'directConnectGatewayName': 'string',
        'amazonSideAsn': 123,
        'ownerAccount': 'string',
        'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
        'stateChangeError': 'string'
    }
}


Response Structure

(dict) --
directConnectGateway (dict) --The Direct Connect gateway.

directConnectGatewayId (string) --The ID of the Direct Connect gateway.

directConnectGatewayName (string) --The name of the Direct Connect gateway.

amazonSideAsn (integer) --The autonomous system number (ASN) for the Amazon side of the connection.

ownerAccount (string) --The ID of the AWS account that owns the Direct Connect gateway.

directConnectGatewayState (string) --The state of the Direct Connect gateway. The following are the possible values:

pending : The initial state after calling  CreateDirectConnectGateway .
available : The Direct Connect gateway is ready for use.
deleting : The initial state after calling  DeleteDirectConnectGateway .
deleted : The Direct Connect gateway is deleted and cannot pass traffic.


stateChangeError (string) --The error message if the state of an object failed to advance.








Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGateway': {
            'directConnectGatewayId': 'string',
            'directConnectGatewayName': 'string',
            'amazonSideAsn': 123,
            'ownerAccount': 'string',
            'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
            'stateChangeError': 'string'
        }
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def delete_direct_connect_gateway_association(associationId=None, directConnectGatewayId=None, virtualGatewayId=None):
    """
    Deletes the association between the specified Direct Connect gateway and virtual private gateway.
    We recommend that you specify the associationID to delete the association. Alternatively, if you own virtual gateway and a Direct Connect gateway association, you can specify the virtualGatewayId and directConnectGatewayId to delete an association.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_direct_connect_gateway_association(
        associationId='string',
        directConnectGatewayId='string',
        virtualGatewayId='string'
    )
    
    
    :type associationId: string
    :param associationId: The ID of the Direct Connect gateway association.

    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :type virtualGatewayId: string
    :param virtualGatewayId: The ID of the virtual private gateway.

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGatewayAssociation': {
        'directConnectGatewayId': 'string',
        'directConnectGatewayOwnerAccount': 'string',
        'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
        'stateChangeError': 'string',
        'associatedGateway': {
            'id': 'string',
            'type': 'virtualPrivateGateway'|'transitGateway',
            'ownerAccount': 'string',
            'region': 'string'
        },
        'associationId': 'string',
        'allowedPrefixesToDirectConnectGateway': [
            {
                'cidr': 'string'
            },
        ],
        'virtualGatewayId': 'string',
        'virtualGatewayRegion': 'string',
        'virtualGatewayOwnerAccount': 'string'
    }
}


Response Structure

(dict) --

directConnectGatewayAssociation (dict) --
Information about the deleted association.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount (string) --
The ID of the AWS account that owns the associated gateway.

associationState (string) --
The state of the association. The following are the possible values:

associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.


stateChangeError (string) --
The error message if the state of an object failed to advance.

associatedGateway (dict) --
Information about the associated gateway.

id (string) --
The ID of the associated gateway.

type (string) --
The type of associated gateway.

ownerAccount (string) --
The ID of the AWS account that owns the associated virtual private gateway or transit gateway.

region (string) --
The Region where the associated gateway is located.



associationId (string) --
The ID of the Direct Connect gateway association.

allowedPrefixesToDirectConnectGateway (list) --
The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

virtualGatewayRegion (string) --
The AWS Region where the virtual private gateway is located.

virtualGatewayOwnerAccount (string) --
The ID of the AWS account that owns the virtual private gateway.









Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGatewayAssociation': {
            'directConnectGatewayId': 'string',
            'directConnectGatewayOwnerAccount': 'string',
            'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
            'stateChangeError': 'string',
            'associatedGateway': {
                'id': 'string',
                'type': 'virtualPrivateGateway'|'transitGateway',
                'ownerAccount': 'string',
                'region': 'string'
            },
            'associationId': 'string',
            'allowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ],
            'virtualGatewayId': 'string',
            'virtualGatewayRegion': 'string',
            'virtualGatewayOwnerAccount': 'string'
        }
    }
    
    
    :returns: 
    associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
    associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
    disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
    disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.
    
    """
    pass

def delete_direct_connect_gateway_association_proposal(proposalId=None):
    """
    Deletes the association proposal request between the specified Direct Connect gateway and virtual private gateway or transit gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_direct_connect_gateway_association_proposal(
        proposalId='string'
    )
    
    
    :type proposalId: string
    :param proposalId: [REQUIRED]\nThe ID of the proposal.\n

    :rtype: dict
ReturnsResponse Syntax{
    'directConnectGatewayAssociationProposal': {
        'proposalId': 'string',
        'directConnectGatewayId': 'string',
        'directConnectGatewayOwnerAccount': 'string',
        'proposalState': 'requested'|'accepted'|'deleted',
        'associatedGateway': {
            'id': 'string',
            'type': 'virtualPrivateGateway'|'transitGateway',
            'ownerAccount': 'string',
            'region': 'string'
        },
        'existingAllowedPrefixesToDirectConnectGateway': [
            {
                'cidr': 'string'
            },
        ],
        'requestedAllowedPrefixesToDirectConnectGateway': [
            {
                'cidr': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
directConnectGatewayAssociationProposal (dict) --The ID of the associated gateway.

proposalId (string) --The ID of the association proposal.

directConnectGatewayId (string) --The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount (string) --The ID of the AWS account that owns the Direct Connect gateway.

proposalState (string) --The state of the proposal. The following are possible values:

accepted : The proposal has been accepted. The Direct Connect gateway association is available to use in this state.
deleted : The proposal has been deleted by the owner that made the proposal. The Direct Connect gateway association cannot be used in this state.
requested : The proposal has been requested. The Direct Connect gateway association cannot be used in this state.


associatedGateway (dict) --Information about the associated gateway.

id (string) --The ID of the associated gateway.

type (string) --The type of associated gateway.

ownerAccount (string) --The ID of the AWS account that owns the associated virtual private gateway or transit gateway.

region (string) --The Region where the associated gateway is located.



existingAllowedPrefixesToDirectConnectGateway (list) --The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





requestedAllowedPrefixesToDirectConnectGateway (list) --The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.












Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGatewayAssociationProposal': {
            'proposalId': 'string',
            'directConnectGatewayId': 'string',
            'directConnectGatewayOwnerAccount': 'string',
            'proposalState': 'requested'|'accepted'|'deleted',
            'associatedGateway': {
                'id': 'string',
                'type': 'virtualPrivateGateway'|'transitGateway',
                'ownerAccount': 'string',
                'region': 'string'
            },
            'existingAllowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ],
            'requestedAllowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def delete_interconnect(interconnectId=None):
    """
    Deletes the specified interconnect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_interconnect(
        interconnectId='string'
    )
    
    
    :type interconnectId: string
    :param interconnectId: [REQUIRED]\nThe ID of the interconnect.\n

    :rtype: dict
ReturnsResponse Syntax{
    'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown'
}


Response Structure

(dict) --
interconnectState (string) --The state of the interconnect. The following are the possible values:

requested : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The interconnect is approved, and is being initialized.
available : The network link is up, and the interconnect is ready for use.
down : The network link is down.
deleting : The interconnect is being deleted.
deleted : The interconnect is deleted.
unknown : The state of the interconnect is not available.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown'
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def delete_lag(lagId=None):
    """
    Deletes the specified link aggregation group (LAG). You cannot delete a LAG if it has active virtual interfaces or hosted connections.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_lag(
        lagId='string'
    )
    
    
    :type lagId: string
    :param lagId: [REQUIRED]\nThe ID of the LAG.\n

    :rtype: dict
ReturnsResponse Syntax{
    'connectionsBandwidth': 'string',
    'numberOfConnections': 123,
    'lagId': 'string',
    'ownerAccount': 'string',
    'lagName': 'string',
    'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
    'location': 'string',
    'region': 'string',
    'minimumLinks': 123,
    'awsDevice': 'string',
    'awsDeviceV2': 'string',
    'connections': [
        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string',
            'jumboFrameCapable': True|False,
            'awsDeviceV2': 'string',
            'hasLogicalRedundancy': 'unknown'|'yes'|'no',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'providerName': 'string'
        },
    ],
    'allowsHostedConnections': True|False,
    'jumboFrameCapable': True|False,
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --Information about a link aggregation group (LAG).

connectionsBandwidth (string) --The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps and 10Gbps.

numberOfConnections (integer) --The number of physical connections bundled by the LAG, up to a maximum of 10.

lagId (string) --The ID of the LAG.

ownerAccount (string) --The ID of the AWS account that owns the LAG.

lagName (string) --The name of the LAG.

lagState (string) --The state of the LAG. The following are the possible values:

requested : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
pending : The LAG has been approved and is being initialized.
available : The network link is established and the LAG is ready for use.
down : The network link is down.
deleting : The LAG is being deleted.
deleted : The LAG is deleted.
unknown : The state of the LAG is not available.


location (string) --The location of the LAG.

region (string) --The AWS Region where the connection is located.

minimumLinks (integer) --The minimum number of physical connections that must be operational for the LAG itself to be operational.

awsDevice (string) --The AWS Direct Connect endpoint that hosts the LAG.

awsDeviceV2 (string) --The AWS Direct Connect endpoint that hosts the LAG.

connections (list) --The connections bundled by the LAG.

(dict) --Information about an AWS Direct Connect connection.

ownerAccount (string) --The ID of the AWS account that owns the connection.

connectionId (string) --The ID of the connection.

connectionName (string) --The name of the connection.

connectionState (string) --The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --The AWS Region where the connection is located.

location (string) --The location of the connection.

bandwidth (string) --The bandwidth of the connection.

vlan (integer) --The ID of the VLAN.

partnerName (string) --The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --The ID of the LAG.

awsDevice (string) --The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --The tags associated with the connection.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.





providerName (string) --The name of the service provider associated with the connection.





allowsHostedConnections (boolean) --Indicates whether the LAG can host other connections.

jumboFrameCapable (boolean) --Indicates whether jumbo frames (9001 MTU) are supported.

hasLogicalRedundancy (string) --Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --The tags associated with the LAG.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.





providerName (string) --The name of the service provider associated with the LAG.






Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'connectionsBandwidth': 'string',
        'numberOfConnections': 123,
        'lagId': 'string',
        'ownerAccount': 'string',
        'lagName': 'string',
        'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
        'location': 'string',
        'region': 'string',
        'minimumLinks': 123,
        'awsDevice': 'string',
        'awsDeviceV2': 'string',
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'providerName': 'string'
            },
        ],
        'allowsHostedConnections': True|False,
        'jumboFrameCapable': True|False,
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    unknown : The state of the connection is not available.
    
    """
    pass

def delete_virtual_interface(virtualInterfaceId=None):
    """
    Deletes a virtual interface.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_virtual_interface(
        virtualInterfaceId='string'
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]\nThe ID of the virtual interface.\n

    :rtype: dict
ReturnsResponse Syntax{
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
}


Response Structure

(dict) --
virtualInterfaceState (string) --The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown'
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_connection_loa(connectionId=None, providerName=None, loaContentType=None):
    """
    Deprecated. Use  DescribeLoa instead.
    Gets the LOA-CFA for a connection.
    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that your APN partner or service provider uses when establishing your cross connect to AWS at the colocation facility. For more information, see Requesting Cross Connects at AWS Direct Connect Locations in the AWS Direct Connect User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_connection_loa(
        connectionId='string',
        providerName='string',
        loaContentType='application/pdf'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection.\n

    :type providerName: string
    :param providerName: The name of the APN partner or service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.

    :type loaContentType: string
    :param loaContentType: The standard media type for the LOA-CFA document. The only supported value is application/pdf.

    :rtype: dict

ReturnsResponse Syntax
{
    'loa': {
        'loaContent': b'bytes',
        'loaContentType': 'application/pdf'
    }
}


Response Structure

(dict) --

loa (dict) --
The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).

loaContent (bytes) --
The binary contents of the LOA-CFA document.

loaContentType (string) --
The standard media type for the LOA-CFA document. The only supported value is application/pdf.









Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'loa': {
            'loaContent': b'bytes',
            'loaContentType': 'application/pdf'
        }
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_connections(connectionId=None):
    """
    Displays the specified connection or all connections in this Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_connections(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: The ID of the connection.

    :rtype: dict
ReturnsResponse Syntax{
    'connections': [
        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string',
            'jumboFrameCapable': True|False,
            'awsDeviceV2': 'string',
            'hasLogicalRedundancy': 'unknown'|'yes'|'no',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'providerName': 'string'
        },
    ]
}


Response Structure

(dict) --
connections (list) --The connections.

(dict) --Information about an AWS Direct Connect connection.

ownerAccount (string) --The ID of the AWS account that owns the connection.

connectionId (string) --The ID of the connection.

connectionName (string) --The name of the connection.

connectionState (string) --The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --The AWS Region where the connection is located.

location (string) --The location of the connection.

bandwidth (string) --The bandwidth of the connection.

vlan (integer) --The ID of the VLAN.

partnerName (string) --The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --The ID of the LAG.

awsDevice (string) --The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --The tags associated with the connection.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.





providerName (string) --The name of the service provider associated with the connection.










Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'providerName': 'string'
            },
        ]
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_connections_on_interconnect(interconnectId=None):
    """
    Deprecated. Use  DescribeHostedConnections instead.
    Lists the connections that have been provisioned on the specified interconnect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_connections_on_interconnect(
        interconnectId='string'
    )
    
    
    :type interconnectId: string
    :param interconnectId: [REQUIRED]\nThe ID of the interconnect.\n

    :rtype: dict
ReturnsResponse Syntax{
    'connections': [
        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string',
            'jumboFrameCapable': True|False,
            'awsDeviceV2': 'string',
            'hasLogicalRedundancy': 'unknown'|'yes'|'no',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'providerName': 'string'
        },
    ]
}


Response Structure

(dict) --
connections (list) --The connections.

(dict) --Information about an AWS Direct Connect connection.

ownerAccount (string) --The ID of the AWS account that owns the connection.

connectionId (string) --The ID of the connection.

connectionName (string) --The name of the connection.

connectionState (string) --The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --The AWS Region where the connection is located.

location (string) --The location of the connection.

bandwidth (string) --The bandwidth of the connection.

vlan (integer) --The ID of the VLAN.

partnerName (string) --The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --The ID of the LAG.

awsDevice (string) --The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --The tags associated with the connection.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.





providerName (string) --The name of the service provider associated with the connection.










Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'providerName': 'string'
            },
        ]
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_direct_connect_gateway_association_proposals(directConnectGatewayId=None, proposalId=None, associatedGatewayId=None, maxResults=None, nextToken=None):
    """
    Describes one or more association proposals for connection between a virtual private gateway or transit gateway and a Direct Connect gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_direct_connect_gateway_association_proposals(
        directConnectGatewayId='string',
        proposalId='string',
        associatedGatewayId='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :type proposalId: string
    :param proposalId: The ID of the proposal.

    :type associatedGatewayId: string
    :param associatedGatewayId: The ID of the associated gateway.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.\nIf MaxResults is given a value larger than 100, only 100 results are returned.\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGatewayAssociationProposals': [
        {
            'proposalId': 'string',
            'directConnectGatewayId': 'string',
            'directConnectGatewayOwnerAccount': 'string',
            'proposalState': 'requested'|'accepted'|'deleted',
            'associatedGateway': {
                'id': 'string',
                'type': 'virtualPrivateGateway'|'transitGateway',
                'ownerAccount': 'string',
                'region': 'string'
            },
            'existingAllowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ],
            'requestedAllowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

directConnectGatewayAssociationProposals (list) --
Describes the Direct Connect gateway association proposals.

(dict) --
Information about the proposal request to attach a virtual private gateway to a Direct Connect gateway.

proposalId (string) --
The ID of the association proposal.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount (string) --
The ID of the AWS account that owns the Direct Connect gateway.

proposalState (string) --
The state of the proposal. The following are possible values:

accepted : The proposal has been accepted. The Direct Connect gateway association is available to use in this state.
deleted : The proposal has been deleted by the owner that made the proposal. The Direct Connect gateway association cannot be used in this state.
requested : The proposal has been requested. The Direct Connect gateway association cannot be used in this state.


associatedGateway (dict) --
Information about the associated gateway.

id (string) --
The ID of the associated gateway.

type (string) --
The type of associated gateway.

ownerAccount (string) --
The ID of the AWS account that owns the associated virtual private gateway or transit gateway.

region (string) --
The Region where the associated gateway is located.



existingAllowedPrefixesToDirectConnectGateway (list) --
The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





requestedAllowedPrefixesToDirectConnectGateway (list) --
The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.









nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGatewayAssociationProposals': [
            {
                'proposalId': 'string',
                'directConnectGatewayId': 'string',
                'directConnectGatewayOwnerAccount': 'string',
                'proposalState': 'requested'|'accepted'|'deleted',
                'associatedGateway': {
                    'id': 'string',
                    'type': 'virtualPrivateGateway'|'transitGateway',
                    'ownerAccount': 'string',
                    'region': 'string'
                },
                'existingAllowedPrefixesToDirectConnectGateway': [
                    {
                        'cidr': 'string'
                    },
                ],
                'requestedAllowedPrefixesToDirectConnectGateway': [
                    {
                        'cidr': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    accepted : The proposal has been accepted. The Direct Connect gateway association is available to use in this state.
    deleted : The proposal has been deleted by the owner that made the proposal. The Direct Connect gateway association cannot be used in this state.
    requested : The proposal has been requested. The Direct Connect gateway association cannot be used in this state.
    
    """
    pass

def describe_direct_connect_gateway_associations(associationId=None, associatedGatewayId=None, directConnectGatewayId=None, maxResults=None, nextToken=None, virtualGatewayId=None):
    """
    Lists the associations between your Direct Connect gateways and virtual private gateways. You must specify a Direct Connect gateway, a virtual private gateway, or both. If you specify a Direct Connect gateway, the response contains all virtual private gateways associated with the Direct Connect gateway. If you specify a virtual private gateway, the response contains all Direct Connect gateways associated with the virtual private gateway. If you specify both, the response contains the association between the Direct Connect gateway and the virtual private gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_direct_connect_gateway_associations(
        associationId='string',
        associatedGatewayId='string',
        directConnectGatewayId='string',
        maxResults=123,
        nextToken='string',
        virtualGatewayId='string'
    )
    
    
    :type associationId: string
    :param associationId: The ID of the Direct Connect gateway association.

    :type associatedGatewayId: string
    :param associatedGatewayId: The ID of the associated gateway.

    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.\nIf MaxResults is given a value larger than 100, only 100 results are returned.\n

    :type nextToken: string
    :param nextToken: The token provided in the previous call to retrieve the next page.

    :type virtualGatewayId: string
    :param virtualGatewayId: The ID of the virtual private gateway.

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGatewayAssociations': [
        {
            'directConnectGatewayId': 'string',
            'directConnectGatewayOwnerAccount': 'string',
            'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
            'stateChangeError': 'string',
            'associatedGateway': {
                'id': 'string',
                'type': 'virtualPrivateGateway'|'transitGateway',
                'ownerAccount': 'string',
                'region': 'string'
            },
            'associationId': 'string',
            'allowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ],
            'virtualGatewayId': 'string',
            'virtualGatewayRegion': 'string',
            'virtualGatewayOwnerAccount': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

directConnectGatewayAssociations (list) --
Information about the associations.

(dict) --
Information about an association between a Direct Connect gateway and a virtual private gateway or transit gateway.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount (string) --
The ID of the AWS account that owns the associated gateway.

associationState (string) --
The state of the association. The following are the possible values:

associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.


stateChangeError (string) --
The error message if the state of an object failed to advance.

associatedGateway (dict) --
Information about the associated gateway.

id (string) --
The ID of the associated gateway.

type (string) --
The type of associated gateway.

ownerAccount (string) --
The ID of the AWS account that owns the associated virtual private gateway or transit gateway.

region (string) --
The Region where the associated gateway is located.



associationId (string) --
The ID of the Direct Connect gateway association.

allowedPrefixesToDirectConnectGateway (list) --
The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

virtualGatewayRegion (string) --
The AWS Region where the virtual private gateway is located.

virtualGatewayOwnerAccount (string) --
The ID of the AWS account that owns the virtual private gateway.





nextToken (string) --
The token to retrieve the next page.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGatewayAssociations': [
            {
                'directConnectGatewayId': 'string',
                'directConnectGatewayOwnerAccount': 'string',
                'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
                'stateChangeError': 'string',
                'associatedGateway': {
                    'id': 'string',
                    'type': 'virtualPrivateGateway'|'transitGateway',
                    'ownerAccount': 'string',
                    'region': 'string'
                },
                'associationId': 'string',
                'allowedPrefixesToDirectConnectGateway': [
                    {
                        'cidr': 'string'
                    },
                ],
                'virtualGatewayId': 'string',
                'virtualGatewayRegion': 'string',
                'virtualGatewayOwnerAccount': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
    associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
    disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
    disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.
    
    """
    pass

def describe_direct_connect_gateway_attachments(directConnectGatewayId=None, virtualInterfaceId=None, maxResults=None, nextToken=None):
    """
    Lists the attachments between your Direct Connect gateways and virtual interfaces. You must specify a Direct Connect gateway, a virtual interface, or both. If you specify a Direct Connect gateway, the response contains all virtual interfaces attached to the Direct Connect gateway. If you specify a virtual interface, the response contains all Direct Connect gateways attached to the virtual interface. If you specify both, the response contains the attachment between the Direct Connect gateway and the virtual interface.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_direct_connect_gateway_attachments(
        directConnectGatewayId='string',
        virtualInterfaceId='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.\nIf MaxResults is given a value larger than 100, only 100 results are returned.\n

    :type nextToken: string
    :param nextToken: The token provided in the previous call to retrieve the next page.

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGatewayAttachments': [
        {
            'directConnectGatewayId': 'string',
            'virtualInterfaceId': 'string',
            'virtualInterfaceRegion': 'string',
            'virtualInterfaceOwnerAccount': 'string',
            'attachmentState': 'attaching'|'attached'|'detaching'|'detached',
            'attachmentType': 'TransitVirtualInterface'|'PrivateVirtualInterface',
            'stateChangeError': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

directConnectGatewayAttachments (list) --
The attachments.

(dict) --
Information about an attachment between a Direct Connect gateway and a virtual interface.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

virtualInterfaceId (string) --
The ID of the virtual interface.

virtualInterfaceRegion (string) --
The AWS Region where the virtual interface is located.

virtualInterfaceOwnerAccount (string) --
The ID of the AWS account that owns the virtual interface.

attachmentState (string) --
The state of the attachment. The following are the possible values:

attaching : The initial state after a virtual interface is created using the Direct Connect gateway.
attached : The Direct Connect gateway and virtual interface are attached and ready to pass traffic.
detaching : The initial state after calling  DeleteVirtualInterface .
detached : The virtual interface is detached from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual interface is stopped.


attachmentType (string) --
The type of attachment.

stateChangeError (string) --
The error message if the state of an object failed to advance.





nextToken (string) --
The token to retrieve the next page.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGatewayAttachments': [
            {
                'directConnectGatewayId': 'string',
                'virtualInterfaceId': 'string',
                'virtualInterfaceRegion': 'string',
                'virtualInterfaceOwnerAccount': 'string',
                'attachmentState': 'attaching'|'attached'|'detaching'|'detached',
                'attachmentType': 'TransitVirtualInterface'|'PrivateVirtualInterface',
                'stateChangeError': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    attaching : The initial state after a virtual interface is created using the Direct Connect gateway.
    attached : The Direct Connect gateway and virtual interface are attached and ready to pass traffic.
    detaching : The initial state after calling  DeleteVirtualInterface .
    detached : The virtual interface is detached from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual interface is stopped.
    
    """
    pass

def describe_direct_connect_gateways(directConnectGatewayId=None, maxResults=None, nextToken=None):
    """
    Lists all your Direct Connect gateways or only the specified Direct Connect gateway. Deleted Direct Connect gateways are not returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_direct_connect_gateways(
        directConnectGatewayId='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type directConnectGatewayId: string
    :param directConnectGatewayId: The ID of the Direct Connect gateway.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.\nIf MaxResults is given a value larger than 100, only 100 results are returned.\n

    :type nextToken: string
    :param nextToken: The token provided in the previous call to retrieve the next page.

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGateways': [
        {
            'directConnectGatewayId': 'string',
            'directConnectGatewayName': 'string',
            'amazonSideAsn': 123,
            'ownerAccount': 'string',
            'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
            'stateChangeError': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

directConnectGateways (list) --
The Direct Connect gateways.

(dict) --
Information about a Direct Connect gateway, which enables you to connect virtual interfaces and virtual private gateway or transit gateways.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

directConnectGatewayName (string) --
The name of the Direct Connect gateway.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

ownerAccount (string) --
The ID of the AWS account that owns the Direct Connect gateway.

directConnectGatewayState (string) --
The state of the Direct Connect gateway. The following are the possible values:

pending : The initial state after calling  CreateDirectConnectGateway .
available : The Direct Connect gateway is ready for use.
deleting : The initial state after calling  DeleteDirectConnectGateway .
deleted : The Direct Connect gateway is deleted and cannot pass traffic.


stateChangeError (string) --
The error message if the state of an object failed to advance.





nextToken (string) --
The token to retrieve the next page.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGateways': [
            {
                'directConnectGatewayId': 'string',
                'directConnectGatewayName': 'string',
                'amazonSideAsn': 123,
                'ownerAccount': 'string',
                'directConnectGatewayState': 'pending'|'available'|'deleting'|'deleted',
                'stateChangeError': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    pending : The initial state after calling  CreateDirectConnectGateway .
    available : The Direct Connect gateway is ready for use.
    deleting : The initial state after calling  DeleteDirectConnectGateway .
    deleted : The Direct Connect gateway is deleted and cannot pass traffic.
    
    """
    pass

def describe_hosted_connections(connectionId=None):
    """
    Lists the hosted connections that have been provisioned on the specified interconnect or link aggregation group (LAG).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_hosted_connections(
        connectionId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the interconnect or LAG.\n

    :rtype: dict
ReturnsResponse Syntax{
    'connections': [
        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string',
            'jumboFrameCapable': True|False,
            'awsDeviceV2': 'string',
            'hasLogicalRedundancy': 'unknown'|'yes'|'no',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'providerName': 'string'
        },
    ]
}


Response Structure

(dict) --
connections (list) --The connections.

(dict) --Information about an AWS Direct Connect connection.

ownerAccount (string) --The ID of the AWS account that owns the connection.

connectionId (string) --The ID of the connection.

connectionName (string) --The name of the connection.

connectionState (string) --The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --The AWS Region where the connection is located.

location (string) --The location of the connection.

bandwidth (string) --The bandwidth of the connection.

vlan (integer) --The ID of the VLAN.

partnerName (string) --The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --The ID of the LAG.

awsDevice (string) --The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --The tags associated with the connection.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.





providerName (string) --The name of the service provider associated with the connection.










Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'providerName': 'string'
            },
        ]
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_interconnect_loa(interconnectId=None, providerName=None, loaContentType=None):
    """
    Deprecated. Use  DescribeLoa instead.
    Gets the LOA-CFA for the specified interconnect.
    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to AWS at the colocation facility. For more information, see Requesting Cross Connects at AWS Direct Connect Locations in the AWS Direct Connect User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_interconnect_loa(
        interconnectId='string',
        providerName='string',
        loaContentType='application/pdf'
    )
    
    
    :type interconnectId: string
    :param interconnectId: [REQUIRED]\nThe ID of the interconnect.\n

    :type providerName: string
    :param providerName: The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.

    :type loaContentType: string
    :param loaContentType: The standard media type for the LOA-CFA document. The only supported value is application/pdf.

    :rtype: dict

ReturnsResponse Syntax
{
    'loa': {
        'loaContent': b'bytes',
        'loaContentType': 'application/pdf'
    }
}


Response Structure

(dict) --

loa (dict) --
The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).

loaContent (bytes) --
The binary contents of the LOA-CFA document.

loaContentType (string) --
The standard media type for the LOA-CFA document. The only supported value is application/pdf.









Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'loa': {
            'loaContent': b'bytes',
            'loaContentType': 'application/pdf'
        }
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_interconnects(interconnectId=None):
    """
    Lists the interconnects owned by the AWS account or only the specified interconnect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_interconnects(
        interconnectId='string'
    )
    
    
    :type interconnectId: string
    :param interconnectId: The ID of the interconnect.

    :rtype: dict
ReturnsResponse Syntax{
    'interconnects': [
        {
            'interconnectId': 'string',
            'interconnectName': 'string',
            'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string',
            'jumboFrameCapable': True|False,
            'awsDeviceV2': 'string',
            'hasLogicalRedundancy': 'unknown'|'yes'|'no',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'providerName': 'string'
        },
    ]
}


Response Structure

(dict) --
interconnects (list) --The interconnects.

(dict) --Information about an interconnect.

interconnectId (string) --The ID of the interconnect.

interconnectName (string) --The name of the interconnect.

interconnectState (string) --The state of the interconnect. The following are the possible values:

requested : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The interconnect is approved, and is being initialized.
available : The network link is up, and the interconnect is ready for use.
down : The network link is down.
deleting : The interconnect is being deleted.
deleted : The interconnect is deleted.
unknown : The state of the interconnect is not available.


region (string) --The AWS Region where the connection is located.

location (string) --The location of the connection.

bandwidth (string) --The bandwidth of the connection.

loaIssueTime (datetime) --The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --The ID of the LAG.

awsDevice (string) --The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --Indicates whether the interconnect supports a secondary BGP in the same address family (IPv4/IPv6).

tags (list) --The tags associated with the interconnect.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.





providerName (string) --The name of the service provider associated with the interconnect.










Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'interconnects': [
            {
                'interconnectId': 'string',
                'interconnectName': 'string',
                'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'providerName': 'string'
            },
        ]
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_lags(lagId=None):
    """
    Describes all your link aggregation groups (LAG) or the specified LAG.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_lags(
        lagId='string'
    )
    
    
    :type lagId: string
    :param lagId: The ID of the LAG.

    :rtype: dict
ReturnsResponse Syntax{
    'lags': [
        {
            'connectionsBandwidth': 'string',
            'numberOfConnections': 123,
            'lagId': 'string',
            'ownerAccount': 'string',
            'lagName': 'string',
            'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
            'location': 'string',
            'region': 'string',
            'minimumLinks': 123,
            'awsDevice': 'string',
            'awsDeviceV2': 'string',
            'connections': [
                {
                    'ownerAccount': 'string',
                    'connectionId': 'string',
                    'connectionName': 'string',
                    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
                    'region': 'string',
                    'location': 'string',
                    'bandwidth': 'string',
                    'vlan': 123,
                    'partnerName': 'string',
                    'loaIssueTime': datetime(2015, 1, 1),
                    'lagId': 'string',
                    'awsDevice': 'string',
                    'jumboFrameCapable': True|False,
                    'awsDeviceV2': 'string',
                    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'providerName': 'string'
                },
            ],
            'allowsHostedConnections': True|False,
            'jumboFrameCapable': True|False,
            'hasLogicalRedundancy': 'unknown'|'yes'|'no',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'providerName': 'string'
        },
    ]
}


Response Structure

(dict) --
lags (list) --The LAGs.

(dict) --Information about a link aggregation group (LAG).

connectionsBandwidth (string) --The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps and 10Gbps.

numberOfConnections (integer) --The number of physical connections bundled by the LAG, up to a maximum of 10.

lagId (string) --The ID of the LAG.

ownerAccount (string) --The ID of the AWS account that owns the LAG.

lagName (string) --The name of the LAG.

lagState (string) --The state of the LAG. The following are the possible values:

requested : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
pending : The LAG has been approved and is being initialized.
available : The network link is established and the LAG is ready for use.
down : The network link is down.
deleting : The LAG is being deleted.
deleted : The LAG is deleted.
unknown : The state of the LAG is not available.


location (string) --The location of the LAG.

region (string) --The AWS Region where the connection is located.

minimumLinks (integer) --The minimum number of physical connections that must be operational for the LAG itself to be operational.

awsDevice (string) --The AWS Direct Connect endpoint that hosts the LAG.

awsDeviceV2 (string) --The AWS Direct Connect endpoint that hosts the LAG.

connections (list) --The connections bundled by the LAG.

(dict) --Information about an AWS Direct Connect connection.

ownerAccount (string) --The ID of the AWS account that owns the connection.

connectionId (string) --The ID of the connection.

connectionName (string) --The name of the connection.

connectionState (string) --The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --The AWS Region where the connection is located.

location (string) --The location of the connection.

bandwidth (string) --The bandwidth of the connection.

vlan (integer) --The ID of the VLAN.

partnerName (string) --The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --The ID of the LAG.

awsDevice (string) --The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --The tags associated with the connection.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.





providerName (string) --The name of the service provider associated with the connection.





allowsHostedConnections (boolean) --Indicates whether the LAG can host other connections.

jumboFrameCapable (boolean) --Indicates whether jumbo frames (9001 MTU) are supported.

hasLogicalRedundancy (string) --Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --The tags associated with the LAG.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.





providerName (string) --The name of the service provider associated with the LAG.










Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'lags': [
            {
                'connectionsBandwidth': 'string',
                'numberOfConnections': 123,
                'lagId': 'string',
                'ownerAccount': 'string',
                'lagName': 'string',
                'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
                'location': 'string',
                'region': 'string',
                'minimumLinks': 123,
                'awsDevice': 'string',
                'awsDeviceV2': 'string',
                'connections': [
                    {
                        'ownerAccount': 'string',
                        'connectionId': 'string',
                        'connectionName': 'string',
                        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
                        'region': 'string',
                        'location': 'string',
                        'bandwidth': 'string',
                        'vlan': 123,
                        'partnerName': 'string',
                        'loaIssueTime': datetime(2015, 1, 1),
                        'lagId': 'string',
                        'awsDevice': 'string',
                        'jumboFrameCapable': True|False,
                        'awsDeviceV2': 'string',
                        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'providerName': 'string'
                    },
                ],
                'allowsHostedConnections': True|False,
                'jumboFrameCapable': True|False,
                'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'providerName': 'string'
            },
        ]
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    unknown : The state of the connection is not available.
    
    """
    pass

def describe_loa(connectionId=None, providerName=None, loaContentType=None):
    """
    Gets the LOA-CFA for a connection, interconnect, or link aggregation group (LAG).
    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA) is a document that is used when establishing your cross connect to AWS at the colocation facility. For more information, see Requesting Cross Connects at AWS Direct Connect Locations in the AWS Direct Connect User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_loa(
        connectionId='string',
        providerName='string',
        loaContentType='application/pdf'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of a connection, LAG, or interconnect.\n

    :type providerName: string
    :param providerName: The name of the service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.

    :type loaContentType: string
    :param loaContentType: The standard media type for the LOA-CFA document. The only supported value is application/pdf.

    :rtype: dict

ReturnsResponse Syntax
{
    'loaContent': b'bytes',
    'loaContentType': 'application/pdf'
}


Response Structure

(dict) --
Information about a Letter of Authorization - Connecting Facility Assignment (LOA-CFA) for a connection.

loaContent (bytes) --
The binary contents of the LOA-CFA document.

loaContentType (string) --
The standard media type for the LOA-CFA document. The only supported value is application/pdf.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'loaContent': b'bytes',
        'loaContentType': 'application/pdf'
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_locations():
    """
    Lists the AWS Direct Connect locations in the current AWS Region. These are the locations that can be selected when calling  CreateConnection or  CreateInterconnect .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_locations()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'locations': [
        {
            'locationCode': 'string',
            'locationName': 'string',
            'region': 'string',
            'availablePortSpeeds': [
                'string',
            ],
            'availableProviders': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
locations (list) --The locations.

(dict) --Information about an AWS Direct Connect location.

locationCode (string) --The code for the location.

locationName (string) --The name of the location. This includes the name of the colocation partner and the physical site of the building.

region (string) --The AWS Region for the location.

availablePortSpeeds (list) --The available port speeds for the location.

(string) --


availableProviders (list) --The name of the service provider for the location.

(string) --











Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'locations': [
            {
                'locationCode': 'string',
                'locationName': 'string',
                'region': 'string',
                'availablePortSpeeds': [
                    'string',
                ],
                'availableProviders': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_tags(resourceArns=None):
    """
    Describes the tags associated with the specified AWS Direct Connect resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_tags(
        resourceArns=[
            'string',
        ]
    )
    
    
    :type resourceArns: list
    :param resourceArns: [REQUIRED]\nThe Amazon Resource Names (ARNs) of the resources.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
resourceTags (list) --Information about the tags.

(dict) --Information about a tag associated with an AWS Direct Connect resource.

resourceArn (string) --The Amazon Resource Name (ARN) of the resource.

tags (list) --The tags.

(dict) --Information about a tag.

key (string) --The key.

value (string) --The value.














Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


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
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_virtual_gateways():
    """
    Lists the virtual private gateways owned by the AWS account.
    You can create one or more AWS Direct Connect private virtual interfaces linked to a virtual private gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_virtual_gateways()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'virtualGateways': [
        {
            'virtualGatewayId': 'string',
            'virtualGatewayState': 'string'
        },
    ]
}


Response Structure

(dict) --
virtualGateways (list) --The virtual private gateways.

(dict) --Information about a virtual private gateway for a private virtual interface.

virtualGatewayId (string) --The ID of the virtual private gateway.

virtualGatewayState (string) --The state of the virtual private gateway. The following are the possible values:

pending : Initial state after creating the virtual private gateway.
available : Ready for use by a private virtual interface.
deleting : Initial state after deleting the virtual private gateway.
deleted : The virtual private gateway is deleted. The private virtual interface is unable to send traffic over this gateway.











Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'virtualGateways': [
            {
                'virtualGatewayId': 'string',
                'virtualGatewayState': 'string'
            },
        ]
    }
    
    
    :returns: 
    DirectConnect.Client.exceptions.DirectConnectServerException
    DirectConnect.Client.exceptions.DirectConnectClientException
    
    """
    pass

def describe_virtual_interfaces(connectionId=None, virtualInterfaceId=None):
    """
    Displays all virtual interfaces for an AWS account. Virtual interfaces deleted fewer than 15 minutes before you make the request are also returned. If you specify a connection ID, only the virtual interfaces associated with the connection are returned. If you specify a virtual interface ID, then only a single virtual interface is returned.
    A virtual interface (VLAN) transmits the traffic between the AWS Direct Connect location and the customer network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_virtual_interfaces(
        connectionId='string',
        virtualInterfaceId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: The ID of the connection.

    :type virtualInterfaceId: string
    :param virtualInterfaceId: The ID of the virtual interface.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'amazonSideAsn': 123,
            'authKey': 'string',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'customerRouterConfig': 'string',
            'mtu': 123,
            'jumboFrameCapable': True|False,
            'virtualGatewayId': 'string',
            'directConnectGatewayId': 'string',
            'routeFilterPrefixes': [
                {
                    'cidr': 'string'
                },
            ],
            'bgpPeers': [
                {
                    'bgpPeerId': 'string',
                    'asn': 123,
                    'authKey': 'string',
                    'addressFamily': 'ipv4'|'ipv6',
                    'amazonAddress': 'string',
                    'customerAddress': 'string',
                    'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                    'bgpStatus': 'up'|'down'|'unknown',
                    'awsDeviceV2': 'string'
                },
            ],
            'region': 'string',
            'awsDeviceV2': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --

virtualInterfaces (list) --
The virtual interfaces

(dict) --
Information about a virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.















Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


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
                'amazonSideAsn': 123,
                'authKey': 'string',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
                'customerRouterConfig': 'string',
                'mtu': 123,
                'jumboFrameCapable': True|False,
                'virtualGatewayId': 'string',
                'directConnectGatewayId': 'string',
                'routeFilterPrefixes': [
                    {
                        'cidr': 'string'
                    },
                ],
                'bgpPeers': [
                    {
                        'bgpPeerId': 'string',
                        'asn': 123,
                        'authKey': 'string',
                        'addressFamily': 'ipv4'|'ipv6',
                        'amazonAddress': 'string',
                        'customerAddress': 'string',
                        'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                        'bgpStatus': 'up'|'down'|'unknown',
                        'awsDeviceV2': 'string'
                    },
                ],
                'region': 'string',
                'awsDeviceV2': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

def disassociate_connection_from_lag(connectionId=None, lagId=None):
    """
    Disassociates a connection from a link aggregation group (LAG). The connection is interrupted and re-established as a standalone connection (the connection is not deleted; to delete the connection, use the  DeleteConnection request). If the LAG has associated virtual interfaces or hosted connections, they remain associated with the LAG. A disassociated connection owned by an AWS Direct Connect Partner is automatically converted to an interconnect.
    If disassociating the connection would cause the LAG to fall below its setting for minimum number of operational connections, the request fails, except when it\'s the last member of the LAG. If all connections are disassociated, the LAG continues to exist as an empty LAG with no physical connections.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_connection_from_lag(
        connectionId='string',
        lagId='string'
    )
    
    
    :type connectionId: string
    :param connectionId: [REQUIRED]\nThe ID of the connection.\n

    :type lagId: string
    :param lagId: [REQUIRED]\nThe ID of the LAG.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'connectionId': 'string',
    'connectionName': 'string',
    'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'region': 'string',
    'location': 'string',
    'bandwidth': 'string',
    'vlan': 123,
    'partnerName': 'string',
    'loaIssueTime': datetime(2015, 1, 1),
    'lagId': 'string',
    'awsDevice': 'string',
    'jumboFrameCapable': True|False,
    'awsDeviceV2': 'string',
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --
Information about an AWS Direct Connect connection.

ownerAccount (string) --
The ID of the AWS account that owns the connection.

connectionId (string) --
The ID of the connection.

connectionName (string) --
The name of the connection.

connectionState (string) --
The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --
The AWS Region where the connection is located.

location (string) --
The location of the connection.

bandwidth (string) --
The bandwidth of the connection.

vlan (integer) --
The ID of the VLAN.

partnerName (string) --
The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --
The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --
The ID of the LAG.

awsDevice (string) --
The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the connection.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the connection.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'connectionId': 'string',
        'connectionName': 'string',
        'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'region': 'string',
        'location': 'string',
        'bandwidth': 'string',
        'vlan': 123,
        'partnerName': 'string',
        'loaIssueTime': datetime(2015, 1, 1),
        'lagId': 'string',
        'awsDevice': 'string',
        'jumboFrameCapable': True|False,
        'awsDeviceV2': 'string',
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
    requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
    pending : The connection has been approved and is being initialized.
    available : The network link is up and the connection is ready for use.
    down : The network link is down.
    deleting : The connection is being deleted.
    deleted : The connection has been deleted.
    rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
    unknown : The state of the connection is not available.
    
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

def tag_resource(resourceArn=None, tags=None):
    """
    Adds the specified tags to the specified AWS Direct Connect resource. Each resource can have a maximum of 50 tags.
    Each tag consists of a key and an optional value. If a tag with the same key is already associated with the resource, this action updates its value.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe tags to add.\n\n(dict) --Information about a tag.\n\nkey (string) -- [REQUIRED]The key.\n\nvalue (string) --The value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectConnect.Client.exceptions.DuplicateTagKeysException
DirectConnect.Client.exceptions.TooManyTagsException
DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes one or more tags from the specified AWS Direct Connect resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe tag keys of the tags to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_direct_connect_gateway_association(associationId=None, addAllowedPrefixesToDirectConnectGateway=None, removeAllowedPrefixesToDirectConnectGateway=None):
    """
    Updates the specified attributes of the Direct Connect gateway association.
    Add or remove prefixes from the association.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_direct_connect_gateway_association(
        associationId='string',
        addAllowedPrefixesToDirectConnectGateway=[
            {
                'cidr': 'string'
            },
        ],
        removeAllowedPrefixesToDirectConnectGateway=[
            {
                'cidr': 'string'
            },
        ]
    )
    
    
    :type associationId: string
    :param associationId: The ID of the Direct Connect gateway association.

    :type addAllowedPrefixesToDirectConnectGateway: list
    :param addAllowedPrefixesToDirectConnectGateway: The Amazon VPC prefixes to advertise to the Direct Connect gateway.\n\n(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.\n\ncidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.\n\n\n\n\n

    :type removeAllowedPrefixesToDirectConnectGateway: list
    :param removeAllowedPrefixesToDirectConnectGateway: The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.\n\n(dict) --Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.\n\ncidr (string) --The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'directConnectGatewayAssociation': {
        'directConnectGatewayId': 'string',
        'directConnectGatewayOwnerAccount': 'string',
        'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
        'stateChangeError': 'string',
        'associatedGateway': {
            'id': 'string',
            'type': 'virtualPrivateGateway'|'transitGateway',
            'ownerAccount': 'string',
            'region': 'string'
        },
        'associationId': 'string',
        'allowedPrefixesToDirectConnectGateway': [
            {
                'cidr': 'string'
            },
        ],
        'virtualGatewayId': 'string',
        'virtualGatewayRegion': 'string',
        'virtualGatewayOwnerAccount': 'string'
    }
}


Response Structure

(dict) --

directConnectGatewayAssociation (dict) --
Information about an association between a Direct Connect gateway and a virtual private gateway or transit gateway.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount (string) --
The ID of the AWS account that owns the associated gateway.

associationState (string) --
The state of the association. The following are the possible values:

associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.


stateChangeError (string) --
The error message if the state of an object failed to advance.

associatedGateway (dict) --
Information about the associated gateway.

id (string) --
The ID of the associated gateway.

type (string) --
The type of associated gateway.

ownerAccount (string) --
The ID of the AWS account that owns the associated virtual private gateway or transit gateway.

region (string) --
The Region where the associated gateway is located.



associationId (string) --
The ID of the Direct Connect gateway association.

allowedPrefixesToDirectConnectGateway (list) --
The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

virtualGatewayRegion (string) --
The AWS Region where the virtual private gateway is located.

virtualGatewayOwnerAccount (string) --
The ID of the AWS account that owns the virtual private gateway.









Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'directConnectGatewayAssociation': {
            'directConnectGatewayId': 'string',
            'directConnectGatewayOwnerAccount': 'string',
            'associationState': 'associating'|'associated'|'disassociating'|'disassociated'|'updating',
            'stateChangeError': 'string',
            'associatedGateway': {
                'id': 'string',
                'type': 'virtualPrivateGateway'|'transitGateway',
                'ownerAccount': 'string',
                'region': 'string'
            },
            'associationId': 'string',
            'allowedPrefixesToDirectConnectGateway': [
                {
                    'cidr': 'string'
                },
            ],
            'virtualGatewayId': 'string',
            'virtualGatewayRegion': 'string',
            'virtualGatewayOwnerAccount': 'string'
        }
    }
    
    
    :returns: 
    associating : The initial state after calling  CreateDirectConnectGatewayAssociation .
    associated : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
    disassociating : The initial state after calling  DeleteDirectConnectGatewayAssociation .
    disassociated : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.
    
    """
    pass

def update_lag(lagId=None, lagName=None, minimumLinks=None):
    """
    Updates the attributes of the specified link aggregation group (LAG).
    You can update the following attributes:
    When you create a LAG, the default value for the minimum number of operational connections is zero (0). If you update this value and the number of operational connections falls below the specified value, the LAG automatically goes down to avoid over-utilization of the remaining connections. Adjust this value with care, as it could force the LAG down if it is set higher than the current number of operational connections.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_lag(
        lagId='string',
        lagName='string',
        minimumLinks=123
    )
    
    
    :type lagId: string
    :param lagId: [REQUIRED]\nThe ID of the LAG.\n

    :type lagName: string
    :param lagName: The name of the LAG.

    :type minimumLinks: integer
    :param minimumLinks: The minimum number of physical connections that must be operational for the LAG itself to be operational.

    :rtype: dict

ReturnsResponse Syntax
{
    'connectionsBandwidth': 'string',
    'numberOfConnections': 123,
    'lagId': 'string',
    'ownerAccount': 'string',
    'lagName': 'string',
    'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
    'location': 'string',
    'region': 'string',
    'minimumLinks': 123,
    'awsDevice': 'string',
    'awsDeviceV2': 'string',
    'connections': [
        {
            'ownerAccount': 'string',
            'connectionId': 'string',
            'connectionName': 'string',
            'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
            'region': 'string',
            'location': 'string',
            'bandwidth': 'string',
            'vlan': 123,
            'partnerName': 'string',
            'loaIssueTime': datetime(2015, 1, 1),
            'lagId': 'string',
            'awsDevice': 'string',
            'jumboFrameCapable': True|False,
            'awsDeviceV2': 'string',
            'hasLogicalRedundancy': 'unknown'|'yes'|'no',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'providerName': 'string'
        },
    ],
    'allowsHostedConnections': True|False,
    'jumboFrameCapable': True|False,
    'hasLogicalRedundancy': 'unknown'|'yes'|'no',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'providerName': 'string'
}


Response Structure

(dict) --
Information about a link aggregation group (LAG).

connectionsBandwidth (string) --
The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps and 10Gbps.

numberOfConnections (integer) --
The number of physical connections bundled by the LAG, up to a maximum of 10.

lagId (string) --
The ID of the LAG.

ownerAccount (string) --
The ID of the AWS account that owns the LAG.

lagName (string) --
The name of the LAG.

lagState (string) --
The state of the LAG. The following are the possible values:

requested : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
pending : The LAG has been approved and is being initialized.
available : The network link is established and the LAG is ready for use.
down : The network link is down.
deleting : The LAG is being deleted.
deleted : The LAG is deleted.
unknown : The state of the LAG is not available.


location (string) --
The location of the LAG.

region (string) --
The AWS Region where the connection is located.

minimumLinks (integer) --
The minimum number of physical connections that must be operational for the LAG itself to be operational.

awsDevice (string) --
The AWS Direct Connect endpoint that hosts the LAG.

awsDeviceV2 (string) --
The AWS Direct Connect endpoint that hosts the LAG.

connections (list) --
The connections bundled by the LAG.

(dict) --
Information about an AWS Direct Connect connection.

ownerAccount (string) --
The ID of the AWS account that owns the connection.

connectionId (string) --
The ID of the connection.

connectionName (string) --
The name of the connection.

connectionState (string) --
The state of the connection. The following are the possible values:

ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
pending : The connection has been approved and is being initialized.
available : The network link is up and the connection is ready for use.
down : The network link is down.
deleting : The connection is being deleted.
deleted : The connection has been deleted.
rejected : A hosted connection in the ordering state enters the rejected state if it is deleted by the customer.
unknown : The state of the connection is not available.


region (string) --
The AWS Region where the connection is located.

location (string) --
The location of the connection.

bandwidth (string) --
The bandwidth of the connection.

vlan (integer) --
The ID of the VLAN.

partnerName (string) --
The name of the AWS Direct Connect service provider associated with the connection.

loaIssueTime (datetime) --
The time of the most recent call to  DescribeLoa for this connection.

lagId (string) --
The ID of the LAG.

awsDevice (string) --
The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the physical connection terminates.

hasLogicalRedundancy (string) --
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the connection.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the connection.





allowsHostedConnections (boolean) --
Indicates whether the LAG can host other connections.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

hasLogicalRedundancy (string) --
Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags (list) --
The tags associated with the LAG.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.





providerName (string) --
The name of the service provider associated with the LAG.







Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'connectionsBandwidth': 'string',
        'numberOfConnections': 123,
        'lagId': 'string',
        'ownerAccount': 'string',
        'lagName': 'string',
        'lagState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'unknown',
        'location': 'string',
        'region': 'string',
        'minimumLinks': 123,
        'awsDevice': 'string',
        'awsDeviceV2': 'string',
        'connections': [
            {
                'ownerAccount': 'string',
                'connectionId': 'string',
                'connectionName': 'string',
                'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
                'region': 'string',
                'location': 'string',
                'bandwidth': 'string',
                'vlan': 123,
                'partnerName': 'string',
                'loaIssueTime': datetime(2015, 1, 1),
                'lagId': 'string',
                'awsDevice': 'string',
                'jumboFrameCapable': True|False,
                'awsDeviceV2': 'string',
                'hasLogicalRedundancy': 'unknown'|'yes'|'no',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'providerName': 'string'
            },
        ],
        'allowsHostedConnections': True|False,
        'jumboFrameCapable': True|False,
        'hasLogicalRedundancy': 'unknown'|'yes'|'no',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'providerName': 'string'
    }
    
    
    :returns: 
    lagId (string) -- [REQUIRED]
    The ID of the LAG.
    
    lagName (string) -- The name of the LAG.
    minimumLinks (integer) -- The minimum number of physical connections that must be operational for the LAG itself to be operational.
    
    """
    pass

def update_virtual_interface_attributes(virtualInterfaceId=None, mtu=None):
    """
    Updates the specified attributes of the specified virtual private interface.
    Setting the MTU of a virtual interface to 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn\'t updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call  DescribeConnections . To check whether your virtual interface supports jumbo frames, call  DescribeVirtualInterfaces .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_virtual_interface_attributes(
        virtualInterfaceId='string',
        mtu=123
    )
    
    
    :type virtualInterfaceId: string
    :param virtualInterfaceId: [REQUIRED]\nThe ID of the virtual private interface.\n

    :type mtu: integer
    :param mtu: The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

    :rtype: dict

ReturnsResponse Syntax
{
    'ownerAccount': 'string',
    'virtualInterfaceId': 'string',
    'location': 'string',
    'connectionId': 'string',
    'virtualInterfaceType': 'string',
    'virtualInterfaceName': 'string',
    'vlan': 123,
    'asn': 123,
    'amazonSideAsn': 123,
    'authKey': 'string',
    'amazonAddress': 'string',
    'customerAddress': 'string',
    'addressFamily': 'ipv4'|'ipv6',
    'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
    'customerRouterConfig': 'string',
    'mtu': 123,
    'jumboFrameCapable': True|False,
    'virtualGatewayId': 'string',
    'directConnectGatewayId': 'string',
    'routeFilterPrefixes': [
        {
            'cidr': 'string'
        },
    ],
    'bgpPeers': [
        {
            'bgpPeerId': 'string',
            'asn': 123,
            'authKey': 'string',
            'addressFamily': 'ipv4'|'ipv6',
            'amazonAddress': 'string',
            'customerAddress': 'string',
            'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
            'bgpStatus': 'up'|'down'|'unknown',
            'awsDeviceV2': 'string'
        },
    ],
    'region': 'string',
    'awsDeviceV2': 'string',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
Information about a virtual interface.

ownerAccount (string) --
The ID of the AWS account that owns the virtual interface.

virtualInterfaceId (string) --
The ID of the virtual interface.

location (string) --
The location of the connection.

connectionId (string) --
The ID of the connection.

virtualInterfaceType (string) --
The type of virtual interface. The possible values are private and public .

virtualInterfaceName (string) --
The name of the virtual interface assigned by the customer network.

vlan (integer) --
The ID of the VLAN.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
The valid values are 1-2147483647.

amazonSideAsn (integer) --
The autonomous system number (ASN) for the Amazon side of the connection.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

addressFamily (string) --
The address family for the BGP peer.

virtualInterfaceState (string) --
The state of the virtual interface. The following are the possible values:

confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
available : A virtual interface that is able to forward traffic.
down : A virtual interface that is BGP down.
deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
deleted : A virtual interface that cannot forward traffic.
rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
unknown : The state of the virtual interface is not available.


customerRouterConfig (string) --
The customer router configuration.

mtu (integer) --
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.

jumboFrameCapable (boolean) --
Indicates whether jumbo frames (9001 MTU) are supported.

virtualGatewayId (string) --
The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId (string) --
The ID of the Direct Connect gateway.

routeFilterPrefixes (list) --
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.

(dict) --
Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr (string) --
The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.





bgpPeers (list) --
The BGP peers configured on this virtual interface.

(dict) --
Information about a BGP peer.

bgpPeerId (string) --
The ID of the BGP peer.

asn (integer) --
The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey (string) --
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily (string) --
The address family for the BGP peer.

amazonAddress (string) --
The IP address assigned to the Amazon interface.

customerAddress (string) --
The IP address assigned to the customer interface.

bgpPeerState (string) --
The state of the BGP peer. The following are the possible values:

verifying : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
pending : The BGP peer is created, and remains in this state until it is ready to be established.
available : The BGP peer is ready to be established.
deleting : The BGP peer is being deleted.
deleted : The BGP peer is deleted and cannot be established.


bgpStatus (string) --
The status of the BGP peer. The following are the possible values:

up : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
down : The BGP peer is down.
unknown : The BGP peer status is not available.


awsDeviceV2 (string) --
The Direct Connect endpoint on which the BGP peer terminates.





region (string) --
The AWS Region where the virtual interface is located.

awsDeviceV2 (string) --
The Direct Connect endpoint on which the virtual interface terminates.

tags (list) --
The tags associated with the virtual interface.

(dict) --
Information about a tag.

key (string) --
The key.

value (string) --
The value.











Exceptions

DirectConnect.Client.exceptions.DirectConnectServerException
DirectConnect.Client.exceptions.DirectConnectClientException


    :return: {
        'ownerAccount': 'string',
        'virtualInterfaceId': 'string',
        'location': 'string',
        'connectionId': 'string',
        'virtualInterfaceType': 'string',
        'virtualInterfaceName': 'string',
        'vlan': 123,
        'asn': 123,
        'amazonSideAsn': 123,
        'authKey': 'string',
        'amazonAddress': 'string',
        'customerAddress': 'string',
        'addressFamily': 'ipv4'|'ipv6',
        'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'|'unknown',
        'customerRouterConfig': 'string',
        'mtu': 123,
        'jumboFrameCapable': True|False,
        'virtualGatewayId': 'string',
        'directConnectGatewayId': 'string',
        'routeFilterPrefixes': [
            {
                'cidr': 'string'
            },
        ],
        'bgpPeers': [
            {
                'bgpPeerId': 'string',
                'asn': 123,
                'authKey': 'string',
                'addressFamily': 'ipv4'|'ipv6',
                'amazonAddress': 'string',
                'customerAddress': 'string',
                'bgpPeerState': 'verifying'|'pending'|'available'|'deleting'|'deleted',
                'bgpStatus': 'up'|'down'|'unknown',
                'awsDeviceV2': 'string'
            },
        ],
        'region': 'string',
        'awsDeviceV2': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
    verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
    pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
    available : A virtual interface that is able to forward traffic.
    down : A virtual interface that is BGP down.
    deleting : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
    deleted : A virtual interface that cannot forward traffic.
    rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the Confirming state is deleted by the virtual interface owner, the virtual interface enters the Rejected state.
    unknown : The state of the virtual interface is not available.
    
    """
    pass

