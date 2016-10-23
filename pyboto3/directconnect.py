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


def allocate_connection_on_interconnect(bandwidth=None, connectionName=None, ownerAccount=None, interconnectId=None,
                                        vlan=None):
    """
    :param bandwidth: [REQUIRED]
            Bandwidth of the connection.
            Example: '500Mbps '
            Default: None
            Values: 50M, 100M, 200M, 300M, 400M, or 500M
            
    :type bandwidth: string
    :param connectionName: [REQUIRED]
            Name of the provisioned connection.
            Example: '500M Connection to AWS '
            Default: None
            
    :type connectionName: string
    :param ownerAccount: [REQUIRED]
            Numeric account Id of the customer for whom the connection will be provisioned.
            Example: 123443215678
            Default: None
            
    :type ownerAccount: string
    :param interconnectId: [REQUIRED]
            ID of the interconnect on which the connection will be provisioned.
            Example: dxcon-456abc78
            Default: None
            
    :type interconnectId: string
    :param vlan: [REQUIRED]
            The dedicated VLAN provisioned to the connection.
            Example: 101
            Default: None
            
    :type vlan: integer
    """
    pass


def allocate_private_virtual_interface(connectionId=None, ownerAccount=None, newPrivateVirtualInterfaceAllocation=None):
    """
    :param connectionId: [REQUIRED]
            The connection ID on which the private virtual interface is provisioned.
            Default: None
            
    :type connectionId: string
    :param ownerAccount: [REQUIRED]
            The AWS account that will own the new private virtual interface.
            Default: None
            
    :type ownerAccount: string
    :param newPrivateVirtualInterfaceAllocation: [REQUIRED]
            Detailed information for the private virtual interface to be provisioned.
            Default: None
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer.
            Example: 'My VPC'
            vlan (integer) -- [REQUIRED]The VLAN ID.
            Example: 101
            asn (integer) -- [REQUIRED]Autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            authKey (string) --Authentication key for BGP configuration.
            Example: asdf34example
            amazonAddress (string) --IP address assigned to the Amazon interface.
            Example: 192.168.1.1/30
            customerAddress (string) --IP address assigned to the customer interface.
            Example: 192.168.1.2/30
            
    :type newPrivateVirtualInterfaceAllocation: dict
    """
    pass


def allocate_public_virtual_interface(connectionId=None, ownerAccount=None, newPublicVirtualInterfaceAllocation=None):
    """
    :param connectionId: [REQUIRED]
            The connection ID on which the public virtual interface is provisioned.
            Default: None
            
    :type connectionId: string
    :param ownerAccount: [REQUIRED]
            The AWS account that will own the new public virtual interface.
            Default: None
            
    :type ownerAccount: string
    :param newPublicVirtualInterfaceAllocation: [REQUIRED]
            Detailed information for the public virtual interface to be provisioned.
            Default: None
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer.
            Example: 'My VPC'
            vlan (integer) -- [REQUIRED]The VLAN ID.
            Example: 101
            asn (integer) -- [REQUIRED]Autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            authKey (string) --Authentication key for BGP configuration.
            Example: asdf34example
            amazonAddress (string) -- [REQUIRED]IP address assigned to the Amazon interface.
            Example: 192.168.1.1/30
            customerAddress (string) -- [REQUIRED]IP address assigned to the customer interface.
            Example: 192.168.1.2/30
            routeFilterPrefixes (list) -- [REQUIRED]A list of routes to be advertised to the AWS network in this region (public virtual interface).
            (dict) --A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.
            cidr (string) --CIDR notation for the advertised route. Multiple routes are separated by commas.
            Example: 10.10.10.0/24,10.10.11.0/24
            
            
    :type newPublicVirtualInterfaceAllocation: dict
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


def confirm_connection(connectionId=None):
    """
    :param connectionId: [REQUIRED]
            ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            Return typedict
            ReturnsResponse Syntax{
              'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
            }
            Response Structure
            (dict) --The response received when ConfirmConnection is called.
            connectionState (string) --State of the connection.
            Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
            Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
            Pending : The connection has been approved, and is being initialized.
            Available : The network link is up, and the connection is ready for use.
            Down : The network link is down.
            Deleting : The connection is in the process of being deleted.
            Deleted : The connection has been deleted.
            Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
            
            
    :type connectionId: string
    """
    pass


def confirm_private_virtual_interface(virtualInterfaceId=None, virtualGatewayId=None):
    """
    :param virtualInterfaceId: [REQUIRED]
            ID of the virtual interface.
            Example: dxvif-123dfg56
            Default: None
            
    :type virtualInterfaceId: string
    :param virtualGatewayId: [REQUIRED]
            ID of the virtual private gateway that will be attached to the virtual interface.
            A virtual private gateway can be managed via the Amazon Virtual Private Cloud (VPC) console or the EC2 CreateVpnGateway action.
            Default: None
            
    :type virtualGatewayId: string
    """
    pass


def confirm_public_virtual_interface(virtualInterfaceId=None):
    """
    :param virtualInterfaceId: [REQUIRED]
            ID of the virtual interface.
            Example: dxvif-123dfg56
            Default: None
            Return typedict
            ReturnsResponse Syntax{
              'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
            }
            Response Structure
            (dict) --The response received when ConfirmPublicVirtualInterface is called.
            virtualInterfaceState (string) --State of the virtual interface.
            Confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
            Verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
            Pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
            Available : A virtual interface that is able to forward traffic.
            Down : A virtual interface that is BGP down.
            Deleting : A virtual interface is in this state immediately after calling DeleteVirtualInterface until it can no longer forward traffic.
            Deleted : A virtual interface that cannot forward traffic.
            Rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state.
            
            
    :type virtualInterfaceId: string
    """
    pass


def create_connection(location=None, bandwidth=None, connectionName=None):
    """
    :param location: [REQUIRED]
            Where the connection is located.
            Example: EqSV5
            Default: None
            
    :type location: string
    :param bandwidth: [REQUIRED]
            Bandwidth of the connection.
            Example: 1Gbps
            Default: None
            
    :type bandwidth: string
    :param connectionName: [REQUIRED]
            The name of the connection.
            Example: 'My Connection to AWS '
            Default: None
            
    :type connectionName: string
    """
    pass


def create_interconnect(interconnectName=None, bandwidth=None, location=None):
    """
    :param interconnectName: [REQUIRED]
            The name of the interconnect.
            Example: '1G Interconnect to AWS '
            Default: None
            
    :type interconnectName: string
    :param bandwidth: [REQUIRED]
            The port bandwidth
            Example: 1Gbps
            Default: None
            Available values: 1Gbps,10Gbps
            
    :type bandwidth: string
    :param location: [REQUIRED]
            Where the interconnect is located
            Example: EqSV5
            Default: None
            
    :type location: string
    """
    pass


def create_private_virtual_interface(connectionId=None, newPrivateVirtualInterface=None):
    """
    :param connectionId: [REQUIRED]
            ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            
    :type connectionId: string
    :param newPrivateVirtualInterface: [REQUIRED]
            Detailed information for the private virtual interface to be created.
            Default: None
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer.
            Example: 'My VPC'
            vlan (integer) -- [REQUIRED]The VLAN ID.
            Example: 101
            asn (integer) -- [REQUIRED]Autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            authKey (string) --Authentication key for BGP configuration.
            Example: asdf34example
            amazonAddress (string) --IP address assigned to the Amazon interface.
            Example: 192.168.1.1/30
            customerAddress (string) --IP address assigned to the customer interface.
            Example: 192.168.1.2/30
            virtualGatewayId (string) -- [REQUIRED]The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.
            Example: vgw-123er56
            
    :type newPrivateVirtualInterface: dict
    """
    pass


def create_public_virtual_interface(connectionId=None, newPublicVirtualInterface=None):
    """
    :param connectionId: [REQUIRED]
            ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            
    :type connectionId: string
    :param newPublicVirtualInterface: [REQUIRED]
            Detailed information for the public virtual interface to be created.
            Default: None
            virtualInterfaceName (string) -- [REQUIRED]The name of the virtual interface assigned by the customer.
            Example: 'My VPC'
            vlan (integer) -- [REQUIRED]The VLAN ID.
            Example: 101
            asn (integer) -- [REQUIRED]Autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            Example: 65000
            authKey (string) --Authentication key for BGP configuration.
            Example: asdf34example
            amazonAddress (string) -- [REQUIRED]IP address assigned to the Amazon interface.
            Example: 192.168.1.1/30
            customerAddress (string) -- [REQUIRED]IP address assigned to the customer interface.
            Example: 192.168.1.2/30
            routeFilterPrefixes (list) -- [REQUIRED]A list of routes to be advertised to the AWS network in this region (public virtual interface).
            (dict) --A route filter prefix that the customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.
            cidr (string) --CIDR notation for the advertised route. Multiple routes are separated by commas.
            Example: 10.10.10.0/24,10.10.11.0/24
            
            
    :type newPublicVirtualInterface: dict
    """
    pass


def delete_connection(connectionId=None):
    """
    :param connectionId: [REQUIRED]
            ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            Return typedict
            ReturnsResponse Syntax{
              'ownerAccount': 'string',
              'connectionId': 'string',
              'connectionName': 'string',
              'connectionState': 'ordering'|'requested'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected',
              'region': 'string',
              'location': 'string',
              'bandwidth': 'string',
              'vlan': 123,
              'partnerName': 'string',
              'loaIssueTime': datetime(2015, 1, 1)
            }
            Response Structure
            (dict) --A connection represents the physical network connection between the AWS Direct Connect location and the customer.
            ownerAccount (string) --The AWS account that will own the new connection.
            connectionId (string) --ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            connectionName (string) --The name of the connection.
            Example: 'My Connection to AWS '
            Default: None
            connectionState (string) --State of the connection.
            Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
            Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
            Pending : The connection has been approved, and is being initialized.
            Available : The network link is up, and the connection is ready for use.
            Down : The network link is down.
            Deleting : The connection is in the process of being deleted.
            Deleted : The connection has been deleted.
            Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
            region (string) --The AWS region where the connection is located.
            Example: us-east-1
            Default: None
            location (string) --Where the connection is located.
            Example: EqSV5
            Default: None
            bandwidth (string) --Bandwidth of the connection.
            Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)
            Default: None
            vlan (integer) --The VLAN ID.
            Example: 101
            partnerName (string) --The name of the AWS Direct Connect service provider associated with the connection.
            loaIssueTime (datetime) --The time of the most recent call to DescribeConnectionLoa for this Connection.
            
            
    :type connectionId: string
    """
    pass


def delete_interconnect(interconnectId=None):
    """
    :param interconnectId: [REQUIRED]
            The ID of the interconnect.
            Example: dxcon-abc123
            Return typedict
            ReturnsResponse Syntax{
              'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted'
            }
            Response Structure
            (dict) --The response received when DeleteInterconnect is called.
            interconnectState (string) --State of the interconnect.
            Requested : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
            Pending : The interconnect has been approved, and is being initialized.
            Available : The network link is up, and the interconnect is ready for use.
            Down : The network link is down.
            Deleting : The interconnect is in the process of being deleted.
            Deleted : The interconnect has been deleted.
            
            
    :type interconnectId: string
    """
    pass


def delete_virtual_interface(virtualInterfaceId=None):
    """
    :param virtualInterfaceId: [REQUIRED]
            ID of the virtual interface.
            Example: dxvif-123dfg56
            Default: None
            Return typedict
            ReturnsResponse Syntax{
              'virtualInterfaceState': 'confirming'|'verifying'|'pending'|'available'|'down'|'deleting'|'deleted'|'rejected'
            }
            Response Structure
            (dict) --The response received when DeleteVirtualInterface is called.
            virtualInterfaceState (string) --State of the virtual interface.
            Confirming : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
            Verifying : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
            Pending : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
            Available : A virtual interface that is able to forward traffic.
            Down : A virtual interface that is BGP down.
            Deleting : A virtual interface is in this state immediately after calling DeleteVirtualInterface until it can no longer forward traffic.
            Deleted : A virtual interface that cannot forward traffic.
            Rejected : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the 'Confirming' state is deleted by the virtual interface owner, the virtual interface will enter the 'Rejected' state.
            
            
    :type virtualInterfaceId: string
    """
    pass


def describe_connection_loa(connectionId=None, providerName=None, loaContentType=None):
    """
    :param connectionId: [REQUIRED]
            ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            
    :type connectionId: string
    :param providerName: The name of the APN partner or service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.
            Default: None
            
    :type providerName: string
    :param loaContentType: A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is 'application/pdf'.
            Default: application/pdf
            
    :type loaContentType: string
    """
    pass


def describe_connections(connectionId=None):
    """
    :param connectionId: ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            Return typedict
            ReturnsResponse Syntax{
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
                  'loaIssueTime': datetime(2015, 1, 1)
                },
              ]
            }
            Response Structure
            (dict) --A structure containing a list of connections.
            connections (list) --A list of connections.
            (dict) --A connection represents the physical network connection between the AWS Direct Connect location and the customer.
            ownerAccount (string) --The AWS account that will own the new connection.
            connectionId (string) --ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            connectionName (string) --The name of the connection.
            Example: 'My Connection to AWS '
            Default: None
            connectionState (string) --State of the connection.
            Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
            Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
            Pending : The connection has been approved, and is being initialized.
            Available : The network link is up, and the connection is ready for use.
            Down : The network link is down.
            Deleting : The connection is in the process of being deleted.
            Deleted : The connection has been deleted.
            Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
            region (string) --The AWS region where the connection is located.
            Example: us-east-1
            Default: None
            location (string) --Where the connection is located.
            Example: EqSV5
            Default: None
            bandwidth (string) --Bandwidth of the connection.
            Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)
            Default: None
            vlan (integer) --The VLAN ID.
            Example: 101
            partnerName (string) --The name of the AWS Direct Connect service provider associated with the connection.
            loaIssueTime (datetime) --The time of the most recent call to DescribeConnectionLoa for this Connection.
            
            
            
    :type connectionId: string
    """
    pass


def describe_connections_on_interconnect(interconnectId=None):
    """
    :param interconnectId: [REQUIRED]
            ID of the interconnect on which a list of connection is provisioned.
            Example: dxcon-abc123
            Default: None
            Return typedict
            ReturnsResponse Syntax{
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
                  'loaIssueTime': datetime(2015, 1, 1)
                },
              ]
            }
            Response Structure
            (dict) --A structure containing a list of connections.
            connections (list) --A list of connections.
            (dict) --A connection represents the physical network connection between the AWS Direct Connect location and the customer.
            ownerAccount (string) --The AWS account that will own the new connection.
            connectionId (string) --ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            connectionName (string) --The name of the connection.
            Example: 'My Connection to AWS '
            Default: None
            connectionState (string) --State of the connection.
            Ordering : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
            Requested : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
            Pending : The connection has been approved, and is being initialized.
            Available : The network link is up, and the connection is ready for use.
            Down : The network link is down.
            Deleting : The connection is in the process of being deleted.
            Deleted : The connection has been deleted.
            Rejected : A hosted connection in the 'Ordering' state will enter the 'Rejected' state if it is deleted by the end customer.
            region (string) --The AWS region where the connection is located.
            Example: us-east-1
            Default: None
            location (string) --Where the connection is located.
            Example: EqSV5
            Default: None
            bandwidth (string) --Bandwidth of the connection.
            Example: 1Gbps (for regular connections), or 500Mbps (for hosted connections)
            Default: None
            vlan (integer) --The VLAN ID.
            Example: 101
            partnerName (string) --The name of the AWS Direct Connect service provider associated with the connection.
            loaIssueTime (datetime) --The time of the most recent call to DescribeConnectionLoa for this Connection.
            
            
            
    :type interconnectId: string
    """
    pass


def describe_interconnect_loa(interconnectId=None, providerName=None, loaContentType=None):
    """
    :param interconnectId: [REQUIRED]
            The ID of the interconnect.
            Example: dxcon-abc123
            
    :type interconnectId: string
    :param providerName: The name of the service provider who establishes connectivity on your behalf. If you supply this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.
            Default: None
            
    :type providerName: string
    :param loaContentType: A standard media type indicating the content type of the LOA-CFA document. Currently, the only supported value is 'application/pdf'.
            Default: application/pdf
            
    :type loaContentType: string
    """
    pass


def describe_interconnects(interconnectId=None):
    """
    :param interconnectId: The ID of the interconnect.
            Example: dxcon-abc123
            Return typedict
            ReturnsResponse Syntax{
              'interconnects': [
                {
                  'interconnectId': 'string',
                  'interconnectName': 'string',
                  'interconnectState': 'requested'|'pending'|'available'|'down'|'deleting'|'deleted',
                  'region': 'string',
                  'location': 'string',
                  'bandwidth': 'string',
                  'loaIssueTime': datetime(2015, 1, 1)
                },
              ]
            }
            Response Structure
            (dict) --A structure containing a list of interconnects.
            interconnects (list) --A list of interconnects.
            (dict) --An interconnect is a connection that can host other connections.
            Like a standard AWS Direct Connect connection, an interconnect represents the physical connection between an AWS Direct Connect partner's network and a specific Direct Connect location. An AWS Direct Connect partner who owns an interconnect can provision hosted connections on the interconnect for their end customers, thereby providing the end customers with connectivity to AWS services.
            The resources of the interconnect, including bandwidth and VLAN numbers, are shared by all of the hosted connections on the interconnect, and the owner of the interconnect determines how these resources are assigned.
            interconnectId (string) --The ID of the interconnect.
            Example: dxcon-abc123
            interconnectName (string) --The name of the interconnect.
            Example: '1G Interconnect to AWS '
            interconnectState (string) --State of the interconnect.
            Requested : The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
            Pending : The interconnect has been approved, and is being initialized.
            Available : The network link is up, and the interconnect is ready for use.
            Down : The network link is down.
            Deleting : The interconnect is in the process of being deleted.
            Deleted : The interconnect has been deleted.
            region (string) --The AWS region where the connection is located.
            Example: us-east-1
            Default: None
            location (string) --Where the connection is located.
            Example: EqSV5
            Default: None
            bandwidth (string) --Bandwidth of the connection.
            Example: 1Gbps
            Default: None
            loaIssueTime (datetime) --The time of the most recent call to DescribeInterconnectLoa for this Interconnect.
            
            
            
    :type interconnectId: string
    """
    pass


def describe_locations():
    """
    """
    pass


def describe_virtual_gateways():
    """
    """
    pass


def describe_virtual_interfaces(connectionId=None, virtualInterfaceId=None):
    """
    :param connectionId: ID of the connection.
            Example: dxcon-fg5678gh
            Default: None
            
    :type connectionId: string
    :param virtualInterfaceId: ID of the virtual interface.
            Example: dxvif-123dfg56
            Default: None
            
    :type virtualInterfaceId: string
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


def get_waiter():
    """
    """
    pass
