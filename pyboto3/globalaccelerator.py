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

def advertise_byoip_cidr(Cidr=None):
    """
    Advertises an IPv4 address range that is provisioned for use with your AWS resources through bring your own IP addresses (BYOIP). It can take a few minutes before traffic to the specified addresses starts routing to AWS because of propagation delays. To see an AWS CLI example of advertising an address range, scroll down to Example .
    To stop advertising the BYOIP address range, use WithdrawByoipCidr .
    For more information, see Bring Your Own IP Addresses (BYOIP) in the AWS Global Accelerator Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.advertise_byoip_cidr(
        Cidr='string'
    )
    
    
    :type Cidr: string
    :param Cidr: [REQUIRED]\nThe address range, in CIDR notation. This must be the exact range that you provisioned. You can\'t advertise only a portion of the provisioned range.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ByoipCidr': {
        'Cidr': 'string',
        'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
        'Events': [
            {
                'Message': 'string',
                'Timestamp': datetime(2015, 1, 1)
            },
        ]
    }
}


Response Structure

(dict) --
ByoipCidr (dict) --Information about the address range.

Cidr (string) --The address range, in CIDR notation.

State (string) --The state of the address pool.

Events (list) --A history of status changes for an IP address range that that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

(dict) --A complex type that contains a Message and a Timestamp value for changes that you make in the status an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Message (string) --A string that contains an Event message describing changes that you make in the status of an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Timestamp (datetime) --A timestamp when you make a status change for an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).












Exceptions

GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.AccessDeniedException
GlobalAccelerator.Client.exceptions.ByoipCidrNotFoundException
GlobalAccelerator.Client.exceptions.IncorrectCidrStateException


    :return: {
        'ByoipCidr': {
            'Cidr': 'string',
            'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
            'Events': [
                {
                    'Message': 'string',
                    'Timestamp': datetime(2015, 1, 1)
                },
            ]
        }
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

def create_accelerator(Name=None, IpAddressType=None, IpAddresses=None, Enabled=None, IdempotencyToken=None, Tags=None):
    """
    Create an accelerator. An accelerator includes one or more listeners that process inbound connections and direct traffic to one or more endpoint groups, each of which includes endpoints, such as Network Load Balancers. To see an AWS CLI example of creating an accelerator, scroll down to Example .
    If you bring your own IP address ranges to AWS Global Accelerator (BYOIP), you can assign IP addresses from your own pool to your accelerator as the static IP address entry points. Only one IP address from each of your IP address ranges can be used for each accelerator.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_accelerator(
        Name='string',
        IpAddressType='IPV4',
        IpAddresses=[
            'string',
        ],
        Enabled=True|False,
        IdempotencyToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of an accelerator. The name can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.\n

    :type IpAddressType: string
    :param IpAddressType: The value for the address type must be IPv4.

    :type IpAddresses: list
    :param IpAddresses: Optionally, if you\'ve added your own IP address pool to Global Accelerator, you can choose IP addresses from your own pool to use for the accelerator\'s static IP addresses. You can specify one or two addresses, separated by a comma. Do not include the /32 suffix.\nIf you specify only one IP address from your IP address range, Global Accelerator assigns a second static IP address for the accelerator from the AWS IP address pool.\nFor more information, see Bring Your Own IP Addresses (BYOIP) in the AWS Global Accelerator Developer Guide .\n\n(string) --\n\n

    :type Enabled: boolean
    :param Enabled: Indicates whether an accelerator is enabled. The value is true or false. The default value is true.\nIf the value is set to true, an accelerator cannot be deleted. If set to false, the accelerator can be deleted.\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique, case-sensitive identifier that you provide to ensure the idempotency\xe2\x80\x94that is, the uniqueness\xe2\x80\x94of an accelerator.\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: Create tags for an accelerator.\nFor more information, see Tagging in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .\n\n(dict) --A complex type that contains a Tag key and Tag value.\n\nKey (string) -- [REQUIRED]A string that contains a Tag key.\n\nValue (string) -- [REQUIRED]A string that contains a Tag value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Accelerator': {
        'AcceleratorArn': 'string',
        'Name': 'string',
        'IpAddressType': 'IPV4',
        'Enabled': True|False,
        'IpSets': [
            {
                'IpFamily': 'string',
                'IpAddresses': [
                    'string',
                ]
            },
        ],
        'DnsName': 'string',
        'Status': 'DEPLOYED'|'IN_PROGRESS',
        'CreatedTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Accelerator (dict) --
The accelerator that is created by specifying a listener and the supported IP address types.

AcceleratorArn (string) --
The Amazon Resource Name (ARN) of the accelerator.

Name (string) --
The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

IpAddressType (string) --
The value for the address type must be IPv4.

Enabled (boolean) --
Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.

IpSets (list) --
The static IP addresses that Global Accelerator associates with the accelerator.

(dict) --
A complex type for the set of IP addresses for an accelerator.

IpFamily (string) --
The types of IP addresses included in this IP set.

IpAddresses (list) --
The array of IP addresses in the IP address set. An IP address set can have a maximum of two IP addresses.

(string) --






DnsName (string) --
The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator\'s static IP addresses.
The naming convention for the DNS name is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .awsglobalaccelerator.com. For example: a1234567890abcdef.awsglobalaccelerator.com.
For more information about the default DNS name, see Support for DNS Addressing in Global Accelerator in the AWS Global Accelerator Developer Guide .

Status (string) --
Describes the deployment status of the accelerator.

CreatedTime (datetime) --
The date and time that the accelerator was created.

LastModifiedTime (datetime) --
The date and time that the accelerator was last modified.









Exceptions

GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.LimitExceededException


    :return: {
        'Accelerator': {
            'AcceleratorArn': 'string',
            'Name': 'string',
            'IpAddressType': 'IPV4',
            'Enabled': True|False,
            'IpSets': [
                {
                    'IpFamily': 'string',
                    'IpAddresses': [
                        'string',
                    ]
                },
            ],
            'DnsName': 'string',
            'Status': 'DEPLOYED'|'IN_PROGRESS',
            'CreatedTime': datetime(2015, 1, 1),
            'LastModifiedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_endpoint_group(ListenerArn=None, EndpointGroupRegion=None, EndpointConfigurations=None, TrafficDialPercentage=None, HealthCheckPort=None, HealthCheckProtocol=None, HealthCheckPath=None, HealthCheckIntervalSeconds=None, ThresholdCount=None, IdempotencyToken=None):
    """
    Create an endpoint group for the specified listener. An endpoint group is a collection of endpoints in one AWS Region. To see an AWS CLI example of creating an endpoint group, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_endpoint_group(
        ListenerArn='string',
        EndpointGroupRegion='string',
        EndpointConfigurations=[
            {
                'EndpointId': 'string',
                'Weight': 123,
                'ClientIPPreservationEnabled': True|False
            },
        ],
        TrafficDialPercentage=...,
        HealthCheckPort=123,
        HealthCheckProtocol='TCP'|'HTTP'|'HTTPS',
        HealthCheckPath='string',
        HealthCheckIntervalSeconds=123,
        ThresholdCount=123,
        IdempotencyToken='string'
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener.\n

    :type EndpointGroupRegion: string
    :param EndpointGroupRegion: [REQUIRED]\nThe name of the AWS Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.\n

    :type EndpointConfigurations: list
    :param EndpointConfigurations: The list of endpoint objects.\n\n(dict) --A complex type for endpoints.\n\nEndpointId (string) --An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For EC2 instances, this is the EC2 instance ID.\nAn Application Load Balancer can be either internal or internet-facing.\n\nWeight (integer) --The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see Endpoint Weights in the AWS Global Accelerator Developer Guide .\n\nClientIPPreservationEnabled (boolean) --Indicates whether client IP address preservation is enabled for an Application Load Balancer endpoint. The value is true or false. The default value is true for new accelerators.\nIf the value is set to true, the client\'s IP address is preserved in the X-Forwarded-For request header as traffic travels to applications on the Application Load Balancer endpoint fronted by the accelerator.\nFor more information, see Preserve Client IP Addresses in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .\n\n\n\n\n

    :type TrafficDialPercentage: float
    :param TrafficDialPercentage: The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.\nUse this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.\nThe default value is 100.\n

    :type HealthCheckPort: integer
    :param HealthCheckPort: The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.

    :type HealthCheckProtocol: string
    :param HealthCheckProtocol: The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.

    :type HealthCheckPath: string
    :param HealthCheckPath: If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).

    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: The time\xe2\x80\x9410 seconds or 30 seconds\xe2\x80\x94between each health check for an endpoint. The default value is 30.

    :type ThresholdCount: integer
    :param ThresholdCount: The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique, case-sensitive identifier that you provide to ensure the idempotency\xe2\x80\x94that is, the uniqueness\xe2\x80\x94of the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EndpointGroup': {
        'EndpointGroupArn': 'string',
        'EndpointGroupRegion': 'string',
        'EndpointDescriptions': [
            {
                'EndpointId': 'string',
                'Weight': 123,
                'HealthState': 'INITIAL'|'HEALTHY'|'UNHEALTHY',
                'HealthReason': 'string',
                'ClientIPPreservationEnabled': True|False
            },
        ],
        'TrafficDialPercentage': ...,
        'HealthCheckPort': 123,
        'HealthCheckProtocol': 'TCP'|'HTTP'|'HTTPS',
        'HealthCheckPath': 'string',
        'HealthCheckIntervalSeconds': 123,
        'ThresholdCount': 123
    }
}


Response Structure

(dict) --

EndpointGroup (dict) --
The information about the endpoint group that was created.

EndpointGroupArn (string) --
The Amazon Resource Name (ARN) of the endpoint group.

EndpointGroupRegion (string) --
The AWS Region that this endpoint group belongs.

EndpointDescriptions (list) --
The list of endpoint objects.

(dict) --
A complex type for an endpoint. Each endpoint group can include one or more endpoints, such as load balancers.

EndpointId (string) --
An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For EC2 instances, this is the EC2 instance ID.
An Application Load Balancer can be either internal or internet-facing.

Weight (integer) --
The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see Endpoint Weights in the AWS Global Accelerator Developer Guide .

HealthState (string) --
The health status of the endpoint.

HealthReason (string) --
The reason code associated with why the endpoint is not healthy. If the endpoint state is healthy, a reason code is not provided.
If the endpoint state is unhealthy , the reason code can be one of the following values:

Timeout : The health check requests to the endpoint are timing out before returning a status.
Failed : The health check failed, for example because the endpoint response was invalid (malformed).

If the endpoint state is initial , the reason code can be one of the following values:

ProvisioningInProgress : The endpoint is in the process of being provisioned.
InitialHealthChecking : Global Accelerator is still setting up the minimum number of health checks for the endpoint that are required to determine its health status.


ClientIPPreservationEnabled (boolean) --
Indicates whether client IP address preservation is enabled for an Application Load Balancer endpoint. The value is true or false. The default value is true for new accelerators.
If the value is set to true, the client\'s IP address is preserved in the X-Forwarded-For request header as traffic travels to applications on the Application Load Balancer endpoint fronted by the accelerator.
For more information, see Viewing Client IP Addresses in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .





TrafficDialPercentage (float) --
The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.
Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.
The default value is 100.

HealthCheckPort (integer) --
The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.
The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.

HealthCheckProtocol (string) --
The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.

HealthCheckPath (string) --
If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).

HealthCheckIntervalSeconds (integer) --
The time\xe2\x80\x9410 seconds or 30 seconds\xe2\x80\x94between health checks for each endpoint. The default value is 30.

ThresholdCount (integer) --
The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.









Exceptions

GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.EndpointGroupAlreadyExistsException
GlobalAccelerator.Client.exceptions.ListenerNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.LimitExceededException
GlobalAccelerator.Client.exceptions.AccessDeniedException


    :return: {
        'EndpointGroup': {
            'EndpointGroupArn': 'string',
            'EndpointGroupRegion': 'string',
            'EndpointDescriptions': [
                {
                    'EndpointId': 'string',
                    'Weight': 123,
                    'HealthState': 'INITIAL'|'HEALTHY'|'UNHEALTHY',
                    'HealthReason': 'string',
                    'ClientIPPreservationEnabled': True|False
                },
            ],
            'TrafficDialPercentage': ...,
            'HealthCheckPort': 123,
            'HealthCheckProtocol': 'TCP'|'HTTP'|'HTTPS',
            'HealthCheckPath': 'string',
            'HealthCheckIntervalSeconds': 123,
            'ThresholdCount': 123
        }
    }
    
    
    :returns: 
    Timeout : The health check requests to the endpoint are timing out before returning a status.
    Failed : The health check failed, for example because the endpoint response was invalid (malformed).
    
    """
    pass

def create_listener(AcceleratorArn=None, PortRanges=None, Protocol=None, ClientAffinity=None, IdempotencyToken=None):
    """
    Create a listener to process inbound connections from clients to an accelerator. Connections arrive to assigned static IP addresses on a port, port range, or list of port ranges that you specify. To see an AWS CLI example of creating a listener, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_listener(
        AcceleratorArn='string',
        PortRanges=[
            {
                'FromPort': 123,
                'ToPort': 123
            },
        ],
        Protocol='TCP'|'UDP',
        ClientAffinity='NONE'|'SOURCE_IP',
        IdempotencyToken='string'
    )
    
    
    :type AcceleratorArn: string
    :param AcceleratorArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of your accelerator.\n

    :type PortRanges: list
    :param PortRanges: [REQUIRED]\nThe list of port ranges to support for connections from clients to your accelerator.\n\n(dict) --A complex type for a range of ports for a listener.\n\nFromPort (integer) --The first port in the range of ports, inclusive.\n\nToPort (integer) --The last port in the range of ports, inclusive.\n\n\n\n\n

    :type Protocol: string
    :param Protocol: [REQUIRED]\nThe protocol for connections from clients to your accelerator.\n

    :type ClientAffinity: string
    :param ClientAffinity: Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Clienty affinity gives you control over whether to always route each client to the same specific endpoint.\nAWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is NONE , Global Accelerator uses the 'five-tuple' (5-tuple) properties\xe2\x80\x94source IP address, source port, destination IP address, destination port, and protocol\xe2\x80\x94to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.\nIf you want a given client to always be routed to the same endpoint, set client affinity to SOURCE_IP instead. When you use the SOURCE_IP setting, Global Accelerator uses the 'two-tuple' (2-tuple) properties\xe2\x80\x94 source (client) IP address and destination IP address\xe2\x80\x94to select the hash value.\nThe default value is NONE .\n

    :type IdempotencyToken: string
    :param IdempotencyToken: [REQUIRED]\nA unique, case-sensitive identifier that you provide to ensure the idempotency\xe2\x80\x94that is, the uniqueness\xe2\x80\x94of the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Listener': {
        'ListenerArn': 'string',
        'PortRanges': [
            {
                'FromPort': 123,
                'ToPort': 123
            },
        ],
        'Protocol': 'TCP'|'UDP',
        'ClientAffinity': 'NONE'|'SOURCE_IP'
    }
}


Response Structure

(dict) --

Listener (dict) --
The listener that you\'ve created.

ListenerArn (string) --
The Amazon Resource Name (ARN) of the listener.

PortRanges (list) --
The list of port ranges for the connections from clients to the accelerator.

(dict) --
A complex type for a range of ports for a listener.

FromPort (integer) --
The first port in the range of ports, inclusive.

ToPort (integer) --
The last port in the range of ports, inclusive.





Protocol (string) --
The protocol for the connections from clients to the accelerator.

ClientAffinity (string) --
Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Clienty affinity gives you control over whether to always route each client to the same specific endpoint.
AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is NONE , Global Accelerator uses the "five-tuple" (5-tuple) properties\xe2\x80\x94source IP address, source port, destination IP address, destination port, and protocol\xe2\x80\x94to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.
If you want a given client to always be routed to the same endpoint, set client affinity to SOURCE_IP instead. When you use the SOURCE_IP setting, Global Accelerator uses the "two-tuple" (2-tuple) properties\xe2\x80\x94 source (client) IP address and destination IP address\xe2\x80\x94to select the hash value.
The default value is NONE .









Exceptions

GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.InvalidPortRangeException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.LimitExceededException


    :return: {
        'Listener': {
            'ListenerArn': 'string',
            'PortRanges': [
                {
                    'FromPort': 123,
                    'ToPort': 123
                },
            ],
            'Protocol': 'TCP'|'UDP',
            'ClientAffinity': 'NONE'|'SOURCE_IP'
        }
    }
    
    
    :returns: 
    GlobalAccelerator.Client.exceptions.InvalidArgumentException
    GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
    GlobalAccelerator.Client.exceptions.InvalidPortRangeException
    GlobalAccelerator.Client.exceptions.InternalServiceErrorException
    GlobalAccelerator.Client.exceptions.LimitExceededException
    
    """
    pass

def delete_accelerator(AcceleratorArn=None):
    """
    Delete an accelerator. Before you can delete an accelerator, you must disable it and remove all dependent resources (listeners and endpoint groups). To disable the accelerator, update the accelerator to set Enabled to false.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_accelerator(
        AcceleratorArn='string'
    )
    
    
    :type AcceleratorArn: string
    :param AcceleratorArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of an accelerator.\n

    """
    pass

def delete_endpoint_group(EndpointGroupArn=None):
    """
    Delete an endpoint group from a listener.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_endpoint_group(
        EndpointGroupArn='string'
    )
    
    
    :type EndpointGroupArn: string
    :param EndpointGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the endpoint group to delete.\n

    """
    pass

def delete_listener(ListenerArn=None):
    """
    Delete a listener from an accelerator.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_listener(
        ListenerArn='string'
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener.\n

    """
    pass

def deprovision_byoip_cidr(Cidr=None):
    """
    Releases the specified address range that you provisioned to use with your AWS resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool. To see an AWS CLI example of deprovisioning an address range, scroll down to Example .
    Before you can release an address range, you must stop advertising it by using WithdrawByoipCidr and you must not have any accelerators that are using static IP addresses allocated from its address range.
    For more information, see Bring Your Own IP Addresses (BYOIP) in the AWS Global Accelerator Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deprovision_byoip_cidr(
        Cidr='string'
    )
    
    
    :type Cidr: string
    :param Cidr: [REQUIRED]\nThe address range, in CIDR notation. The prefix must be the same prefix that you specified when you provisioned the address range.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ByoipCidr': {
        'Cidr': 'string',
        'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
        'Events': [
            {
                'Message': 'string',
                'Timestamp': datetime(2015, 1, 1)
            },
        ]
    }
}


Response Structure

(dict) --
ByoipCidr (dict) --Information about the address range.

Cidr (string) --The address range, in CIDR notation.

State (string) --The state of the address pool.

Events (list) --A history of status changes for an IP address range that that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

(dict) --A complex type that contains a Message and a Timestamp value for changes that you make in the status an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Message (string) --A string that contains an Event message describing changes that you make in the status of an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Timestamp (datetime) --A timestamp when you make a status change for an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).












Exceptions

GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.AccessDeniedException
GlobalAccelerator.Client.exceptions.ByoipCidrNotFoundException
GlobalAccelerator.Client.exceptions.IncorrectCidrStateException


    :return: {
        'ByoipCidr': {
            'Cidr': 'string',
            'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
            'Events': [
                {
                    'Message': 'string',
                    'Timestamp': datetime(2015, 1, 1)
                },
            ]
        }
    }
    
    
    """
    pass

def describe_accelerator(AcceleratorArn=None):
    """
    Describe an accelerator. To see an AWS CLI example of describing an accelerator, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_accelerator(
        AcceleratorArn='string'
    )
    
    
    :type AcceleratorArn: string
    :param AcceleratorArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the accelerator to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Accelerator': {
        'AcceleratorArn': 'string',
        'Name': 'string',
        'IpAddressType': 'IPV4',
        'Enabled': True|False,
        'IpSets': [
            {
                'IpFamily': 'string',
                'IpAddresses': [
                    'string',
                ]
            },
        ],
        'DnsName': 'string',
        'Status': 'DEPLOYED'|'IN_PROGRESS',
        'CreatedTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Accelerator (dict) --The description of the accelerator.

AcceleratorArn (string) --The Amazon Resource Name (ARN) of the accelerator.

Name (string) --The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

IpAddressType (string) --The value for the address type must be IPv4.

Enabled (boolean) --Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.

IpSets (list) --The static IP addresses that Global Accelerator associates with the accelerator.

(dict) --A complex type for the set of IP addresses for an accelerator.

IpFamily (string) --The types of IP addresses included in this IP set.

IpAddresses (list) --The array of IP addresses in the IP address set. An IP address set can have a maximum of two IP addresses.

(string) --






DnsName (string) --The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator\'s static IP addresses.
The naming convention for the DNS name is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .awsglobalaccelerator.com. For example: a1234567890abcdef.awsglobalaccelerator.com.
For more information about the default DNS name, see Support for DNS Addressing in Global Accelerator in the AWS Global Accelerator Developer Guide .

Status (string) --Describes the deployment status of the accelerator.

CreatedTime (datetime) --The date and time that the accelerator was created.

LastModifiedTime (datetime) --The date and time that the accelerator was last modified.








Exceptions

GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException


    :return: {
        'Accelerator': {
            'AcceleratorArn': 'string',
            'Name': 'string',
            'IpAddressType': 'IPV4',
            'Enabled': True|False,
            'IpSets': [
                {
                    'IpFamily': 'string',
                    'IpAddresses': [
                        'string',
                    ]
                },
            ],
            'DnsName': 'string',
            'Status': 'DEPLOYED'|'IN_PROGRESS',
            'CreatedTime': datetime(2015, 1, 1),
            'LastModifiedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
    GlobalAccelerator.Client.exceptions.InternalServiceErrorException
    GlobalAccelerator.Client.exceptions.InvalidArgumentException
    
    """
    pass

def describe_accelerator_attributes(AcceleratorArn=None):
    """
    Describe the attributes of an accelerator. To see an AWS CLI example of describing the attributes of an accelerator, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_accelerator_attributes(
        AcceleratorArn='string'
    )
    
    
    :type AcceleratorArn: string
    :param AcceleratorArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the accelerator with the attributes that you want to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AcceleratorAttributes': {
        'FlowLogsEnabled': True|False,
        'FlowLogsS3Bucket': 'string',
        'FlowLogsS3Prefix': 'string'
    }
}


Response Structure

(dict) --
AcceleratorAttributes (dict) --The attributes of the accelerator.

FlowLogsEnabled (boolean) --Indicates whether flow logs are enabled. The default value is false. If the value is true, FlowLogsS3Bucket and FlowLogsS3Prefix must be specified.
For more information, see Flow Logs in the AWS Global Accelerator Developer Guide .

FlowLogsS3Bucket (string) --The name of the Amazon S3 bucket for the flow logs. Attribute is required if FlowLogsEnabled is true . The bucket must exist and have a bucket policy that grants AWS Global Accelerator permission to write to the bucket.

FlowLogsS3Prefix (string) --The prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if FlowLogsEnabled is true .
If you don\xe2\x80\x99t specify a prefix, the flow logs are stored in the root of the bucket. If you specify slash (/) for the S3 bucket prefix, the log file bucket folder structure will include a double slash (//), like the following:
s3-bucket_name//AWSLogs/aws_account_id








Exceptions

GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException


    :return: {
        'AcceleratorAttributes': {
            'FlowLogsEnabled': True|False,
            'FlowLogsS3Bucket': 'string',
            'FlowLogsS3Prefix': 'string'
        }
    }
    
    
    """
    pass

def describe_endpoint_group(EndpointGroupArn=None):
    """
    Describe an endpoint group. To see an AWS CLI example of describing an endpoint group, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_endpoint_group(
        EndpointGroupArn='string'
    )
    
    
    :type EndpointGroupArn: string
    :param EndpointGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the endpoint group to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'EndpointGroup': {
        'EndpointGroupArn': 'string',
        'EndpointGroupRegion': 'string',
        'EndpointDescriptions': [
            {
                'EndpointId': 'string',
                'Weight': 123,
                'HealthState': 'INITIAL'|'HEALTHY'|'UNHEALTHY',
                'HealthReason': 'string',
                'ClientIPPreservationEnabled': True|False
            },
        ],
        'TrafficDialPercentage': ...,
        'HealthCheckPort': 123,
        'HealthCheckProtocol': 'TCP'|'HTTP'|'HTTPS',
        'HealthCheckPath': 'string',
        'HealthCheckIntervalSeconds': 123,
        'ThresholdCount': 123
    }
}


Response Structure

(dict) --
EndpointGroup (dict) --The description of an endpoint group.

EndpointGroupArn (string) --The Amazon Resource Name (ARN) of the endpoint group.

EndpointGroupRegion (string) --The AWS Region that this endpoint group belongs.

EndpointDescriptions (list) --The list of endpoint objects.

(dict) --A complex type for an endpoint. Each endpoint group can include one or more endpoints, such as load balancers.

EndpointId (string) --An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For EC2 instances, this is the EC2 instance ID.
An Application Load Balancer can be either internal or internet-facing.

Weight (integer) --The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see Endpoint Weights in the AWS Global Accelerator Developer Guide .

HealthState (string) --The health status of the endpoint.

HealthReason (string) --The reason code associated with why the endpoint is not healthy. If the endpoint state is healthy, a reason code is not provided.
If the endpoint state is unhealthy , the reason code can be one of the following values:

Timeout : The health check requests to the endpoint are timing out before returning a status.
Failed : The health check failed, for example because the endpoint response was invalid (malformed).

If the endpoint state is initial , the reason code can be one of the following values:

ProvisioningInProgress : The endpoint is in the process of being provisioned.
InitialHealthChecking : Global Accelerator is still setting up the minimum number of health checks for the endpoint that are required to determine its health status.


ClientIPPreservationEnabled (boolean) --Indicates whether client IP address preservation is enabled for an Application Load Balancer endpoint. The value is true or false. The default value is true for new accelerators.
If the value is set to true, the client\'s IP address is preserved in the X-Forwarded-For request header as traffic travels to applications on the Application Load Balancer endpoint fronted by the accelerator.
For more information, see Viewing Client IP Addresses in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .





TrafficDialPercentage (float) --The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.
Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.
The default value is 100.

HealthCheckPort (integer) --The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.
The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.

HealthCheckProtocol (string) --The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.

HealthCheckPath (string) --If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).

HealthCheckIntervalSeconds (integer) --The time\xe2\x80\x9410 seconds or 30 seconds\xe2\x80\x94between health checks for each endpoint. The default value is 30.

ThresholdCount (integer) --The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.








Exceptions

GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.EndpointGroupNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException


    :return: {
        'EndpointGroup': {
            'EndpointGroupArn': 'string',
            'EndpointGroupRegion': 'string',
            'EndpointDescriptions': [
                {
                    'EndpointId': 'string',
                    'Weight': 123,
                    'HealthState': 'INITIAL'|'HEALTHY'|'UNHEALTHY',
                    'HealthReason': 'string',
                    'ClientIPPreservationEnabled': True|False
                },
            ],
            'TrafficDialPercentage': ...,
            'HealthCheckPort': 123,
            'HealthCheckProtocol': 'TCP'|'HTTP'|'HTTPS',
            'HealthCheckPath': 'string',
            'HealthCheckIntervalSeconds': 123,
            'ThresholdCount': 123
        }
    }
    
    
    :returns: 
    ProvisioningInProgress : The endpoint is in the process of being provisioned.
    InitialHealthChecking : Global Accelerator is still setting up the minimum number of health checks for the endpoint that are required to determine its health status.
    
    """
    pass

def describe_listener(ListenerArn=None):
    """
    Describe a listener. To see an AWS CLI example of describing a listener, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_listener(
        ListenerArn='string'
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Listener': {
        'ListenerArn': 'string',
        'PortRanges': [
            {
                'FromPort': 123,
                'ToPort': 123
            },
        ],
        'Protocol': 'TCP'|'UDP',
        'ClientAffinity': 'NONE'|'SOURCE_IP'
    }
}


Response Structure

(dict) --
Listener (dict) --The description of a listener.

ListenerArn (string) --The Amazon Resource Name (ARN) of the listener.

PortRanges (list) --The list of port ranges for the connections from clients to the accelerator.

(dict) --A complex type for a range of ports for a listener.

FromPort (integer) --The first port in the range of ports, inclusive.

ToPort (integer) --The last port in the range of ports, inclusive.





Protocol (string) --The protocol for the connections from clients to the accelerator.

ClientAffinity (string) --Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Clienty affinity gives you control over whether to always route each client to the same specific endpoint.
AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is NONE , Global Accelerator uses the "five-tuple" (5-tuple) properties\xe2\x80\x94source IP address, source port, destination IP address, destination port, and protocol\xe2\x80\x94to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.
If you want a given client to always be routed to the same endpoint, set client affinity to SOURCE_IP instead. When you use the SOURCE_IP setting, Global Accelerator uses the "two-tuple" (2-tuple) properties\xe2\x80\x94 source (client) IP address and destination IP address\xe2\x80\x94to select the hash value.
The default value is NONE .








Exceptions

GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.ListenerNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException


    :return: {
        'Listener': {
            'ListenerArn': 'string',
            'PortRanges': [
                {
                    'FromPort': 123,
                    'ToPort': 123
                },
            ],
            'Protocol': 'TCP'|'UDP',
            'ClientAffinity': 'NONE'|'SOURCE_IP'
        }
    }
    
    
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

def list_accelerators(MaxResults=None, NextToken=None):
    """
    List the accelerators for an AWS account. To see an AWS CLI example of listing the accelerators for an AWS account, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_accelerators(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The number of Global Accelerator objects that you want to return with this call. The default value is 10.

    :type NextToken: string
    :param NextToken: The token for the next set of results. You receive this token from a previous call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Accelerators': [
        {
            'AcceleratorArn': 'string',
            'Name': 'string',
            'IpAddressType': 'IPV4',
            'Enabled': True|False,
            'IpSets': [
                {
                    'IpFamily': 'string',
                    'IpAddresses': [
                        'string',
                    ]
                },
            ],
            'DnsName': 'string',
            'Status': 'DEPLOYED'|'IN_PROGRESS',
            'CreatedTime': datetime(2015, 1, 1),
            'LastModifiedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Accelerators (list) --
The list of accelerators for a customer account.

(dict) --
An accelerator is a complex type that includes one or more listeners that process inbound connections and then direct traffic to one or more endpoint groups, each of which includes endpoints, such as load balancers.

AcceleratorArn (string) --
The Amazon Resource Name (ARN) of the accelerator.

Name (string) --
The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

IpAddressType (string) --
The value for the address type must be IPv4.

Enabled (boolean) --
Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.

IpSets (list) --
The static IP addresses that Global Accelerator associates with the accelerator.

(dict) --
A complex type for the set of IP addresses for an accelerator.

IpFamily (string) --
The types of IP addresses included in this IP set.

IpAddresses (list) --
The array of IP addresses in the IP address set. An IP address set can have a maximum of two IP addresses.

(string) --






DnsName (string) --
The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator\'s static IP addresses.
The naming convention for the DNS name is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .awsglobalaccelerator.com. For example: a1234567890abcdef.awsglobalaccelerator.com.
For more information about the default DNS name, see Support for DNS Addressing in Global Accelerator in the AWS Global Accelerator Developer Guide .

Status (string) --
Describes the deployment status of the accelerator.

CreatedTime (datetime) --
The date and time that the accelerator was created.

LastModifiedTime (datetime) --
The date and time that the accelerator was last modified.





NextToken (string) --
The token for the next set of results. You receive this token from a previous call.







Exceptions

GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.InvalidNextTokenException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException


    :return: {
        'Accelerators': [
            {
                'AcceleratorArn': 'string',
                'Name': 'string',
                'IpAddressType': 'IPV4',
                'Enabled': True|False,
                'IpSets': [
                    {
                        'IpFamily': 'string',
                        'IpAddresses': [
                            'string',
                        ]
                    },
                ],
                'DnsName': 'string',
                'Status': 'DEPLOYED'|'IN_PROGRESS',
                'CreatedTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_byoip_cidrs(MaxResults=None, NextToken=None):
    """
    Lists the IP address ranges that were specified in calls to ProvisionByoipCidr , including the current state and a history of state changes.
    To see an AWS CLI example of listing BYOIP CIDR addresses, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_byoip_cidrs(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :type NextToken: string
    :param NextToken: The token for the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ByoipCidrs': [
        {
            'Cidr': 'string',
            'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
            'Events': [
                {
                    'Message': 'string',
                    'Timestamp': datetime(2015, 1, 1)
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ByoipCidrs (list) --
Information about your address ranges.

(dict) --
Information about an IP address range that is provisioned for use with your AWS resources through bring your own IP address (BYOIP).
The following describes each BYOIP State that your IP address range can be in.

PENDING_PROVISIONING \xe2\x80\x94 You\xe2\x80\x99ve submitted a request to provision an IP address range but it is not yet provisioned with AWS Global Accelerator.
READY \xe2\x80\x94 The address range is provisioned with AWS Global Accelerator and can be advertised.
PENDING_ADVERTISING \xe2\x80\x94 You\xe2\x80\x99ve submitted a request for AWS Global Accelerator to advertise an address range but it is not yet being advertised.
ADVERTISING \xe2\x80\x94 The address range is being advertised by AWS Global Accelerator.
PENDING_WITHDRAWING \xe2\x80\x94 You\xe2\x80\x99ve submitted a request to withdraw an address range from being advertised but it is still being advertised by AWS Global Accelerator.
PENDING_DEPROVISIONING \xe2\x80\x94 You\xe2\x80\x99ve submitted a request to deprovision an address range from AWS Global Accelerator but it is still provisioned.
DEPROVISIONED \xe2\x80\x94 The address range is deprovisioned from AWS Global Accelerator.
FAILED_PROVISION \xe2\x80\x94 The request to provision the address range from AWS Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
FAILED_ADVERTISING \xe2\x80\x94 The request for AWS Global Accelerator to advertise the address range was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
FAILED_WITHDRAW \xe2\x80\x94 The request to withdraw the address range from advertising by AWS Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
FAILED_DEPROVISION \xe2\x80\x94 The request to deprovision the address range from AWS Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.


Cidr (string) --
The address range, in CIDR notation.

State (string) --
The state of the address pool.

Events (list) --
A history of status changes for an IP address range that that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

(dict) --
A complex type that contains a Message and a Timestamp value for changes that you make in the status an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Message (string) --
A string that contains an Event message describing changes that you make in the status of an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Timestamp (datetime) --
A timestamp when you make a status change for an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).









NextToken (string) --
The token for the next page of results.







Exceptions

GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.AccessDeniedException
GlobalAccelerator.Client.exceptions.InvalidNextTokenException


    :return: {
        'ByoipCidrs': [
            {
                'Cidr': 'string',
                'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
                'Events': [
                    {
                        'Message': 'string',
                        'Timestamp': datetime(2015, 1, 1)
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    PENDING_PROVISIONING \xe2\x80\x94 You\xe2\x80\x99ve submitted a request to provision an IP address range but it is not yet provisioned with AWS Global Accelerator.
    READY \xe2\x80\x94 The address range is provisioned with AWS Global Accelerator and can be advertised.
    PENDING_ADVERTISING \xe2\x80\x94 You\xe2\x80\x99ve submitted a request for AWS Global Accelerator to advertise an address range but it is not yet being advertised.
    ADVERTISING \xe2\x80\x94 The address range is being advertised by AWS Global Accelerator.
    PENDING_WITHDRAWING \xe2\x80\x94 You\xe2\x80\x99ve submitted a request to withdraw an address range from being advertised but it is still being advertised by AWS Global Accelerator.
    PENDING_DEPROVISIONING \xe2\x80\x94 You\xe2\x80\x99ve submitted a request to deprovision an address range from AWS Global Accelerator but it is still provisioned.
    DEPROVISIONED \xe2\x80\x94 The address range is deprovisioned from AWS Global Accelerator.
    FAILED_PROVISION \xe2\x80\x94 The request to provision the address range from AWS Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
    FAILED_ADVERTISING \xe2\x80\x94 The request for AWS Global Accelerator to advertise the address range was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
    FAILED_WITHDRAW \xe2\x80\x94 The request to withdraw the address range from advertising by AWS Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
    FAILED_DEPROVISION \xe2\x80\x94 The request to deprovision the address range from AWS Global Accelerator was not successful. Please make sure that you provide all of the correct information, and try again. If the request fails a second time, contact AWS support.
    
    """
    pass

def list_endpoint_groups(ListenerArn=None, MaxResults=None, NextToken=None):
    """
    List the endpoint groups that are associated with a listener. To see an AWS CLI example of listing the endpoint groups for listener, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_endpoint_groups(
        ListenerArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener.\n

    :type MaxResults: integer
    :param MaxResults: The number of endpoint group objects that you want to return with this call. The default value is 10.

    :type NextToken: string
    :param NextToken: The token for the next set of results. You receive this token from a previous call.

    :rtype: dict

ReturnsResponse Syntax
{
    'EndpointGroups': [
        {
            'EndpointGroupArn': 'string',
            'EndpointGroupRegion': 'string',
            'EndpointDescriptions': [
                {
                    'EndpointId': 'string',
                    'Weight': 123,
                    'HealthState': 'INITIAL'|'HEALTHY'|'UNHEALTHY',
                    'HealthReason': 'string',
                    'ClientIPPreservationEnabled': True|False
                },
            ],
            'TrafficDialPercentage': ...,
            'HealthCheckPort': 123,
            'HealthCheckProtocol': 'TCP'|'HTTP'|'HTTPS',
            'HealthCheckPath': 'string',
            'HealthCheckIntervalSeconds': 123,
            'ThresholdCount': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

EndpointGroups (list) --
The list of the endpoint groups associated with a listener.

(dict) --
A complex type for the endpoint group. An AWS Region can have only one endpoint group for a specific listener.

EndpointGroupArn (string) --
The Amazon Resource Name (ARN) of the endpoint group.

EndpointGroupRegion (string) --
The AWS Region that this endpoint group belongs.

EndpointDescriptions (list) --
The list of endpoint objects.

(dict) --
A complex type for an endpoint. Each endpoint group can include one or more endpoints, such as load balancers.

EndpointId (string) --
An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For EC2 instances, this is the EC2 instance ID.
An Application Load Balancer can be either internal or internet-facing.

Weight (integer) --
The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see Endpoint Weights in the AWS Global Accelerator Developer Guide .

HealthState (string) --
The health status of the endpoint.

HealthReason (string) --
The reason code associated with why the endpoint is not healthy. If the endpoint state is healthy, a reason code is not provided.
If the endpoint state is unhealthy , the reason code can be one of the following values:

Timeout : The health check requests to the endpoint are timing out before returning a status.
Failed : The health check failed, for example because the endpoint response was invalid (malformed).

If the endpoint state is initial , the reason code can be one of the following values:

ProvisioningInProgress : The endpoint is in the process of being provisioned.
InitialHealthChecking : Global Accelerator is still setting up the minimum number of health checks for the endpoint that are required to determine its health status.


ClientIPPreservationEnabled (boolean) --
Indicates whether client IP address preservation is enabled for an Application Load Balancer endpoint. The value is true or false. The default value is true for new accelerators.
If the value is set to true, the client\'s IP address is preserved in the X-Forwarded-For request header as traffic travels to applications on the Application Load Balancer endpoint fronted by the accelerator.
For more information, see Viewing Client IP Addresses in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .





TrafficDialPercentage (float) --
The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.
Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.
The default value is 100.

HealthCheckPort (integer) --
The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.
The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.

HealthCheckProtocol (string) --
The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.

HealthCheckPath (string) --
If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).

HealthCheckIntervalSeconds (integer) --
The time\xe2\x80\x9410 seconds or 30 seconds\xe2\x80\x94between health checks for each endpoint. The default value is 30.

ThresholdCount (integer) --
The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.





NextToken (string) --
The token for the next set of results. You receive this token from a previous call.







Exceptions

GlobalAccelerator.Client.exceptions.ListenerNotFoundException
GlobalAccelerator.Client.exceptions.InvalidNextTokenException
GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException


    :return: {
        'EndpointGroups': [
            {
                'EndpointGroupArn': 'string',
                'EndpointGroupRegion': 'string',
                'EndpointDescriptions': [
                    {
                        'EndpointId': 'string',
                        'Weight': 123,
                        'HealthState': 'INITIAL'|'HEALTHY'|'UNHEALTHY',
                        'HealthReason': 'string',
                        'ClientIPPreservationEnabled': True|False
                    },
                ],
                'TrafficDialPercentage': ...,
                'HealthCheckPort': 123,
                'HealthCheckProtocol': 'TCP'|'HTTP'|'HTTPS',
                'HealthCheckPath': 'string',
                'HealthCheckIntervalSeconds': 123,
                'ThresholdCount': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Timeout : The health check requests to the endpoint are timing out before returning a status.
    Failed : The health check failed, for example because the endpoint response was invalid (malformed).
    
    """
    pass

def list_listeners(AcceleratorArn=None, MaxResults=None, NextToken=None):
    """
    List the listeners for an accelerator. To see an AWS CLI example of listing the listeners for an accelerator, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_listeners(
        AcceleratorArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AcceleratorArn: string
    :param AcceleratorArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the accelerator for which you want to list listener objects.\n

    :type MaxResults: integer
    :param MaxResults: The number of listener objects that you want to return with this call. The default value is 10.

    :type NextToken: string
    :param NextToken: The token for the next set of results. You receive this token from a previous call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Listeners': [
        {
            'ListenerArn': 'string',
            'PortRanges': [
                {
                    'FromPort': 123,
                    'ToPort': 123
                },
            ],
            'Protocol': 'TCP'|'UDP',
            'ClientAffinity': 'NONE'|'SOURCE_IP'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Listeners (list) --
The list of listeners for an accelerator.

(dict) --
A complex type for a listener.

ListenerArn (string) --
The Amazon Resource Name (ARN) of the listener.

PortRanges (list) --
The list of port ranges for the connections from clients to the accelerator.

(dict) --
A complex type for a range of ports for a listener.

FromPort (integer) --
The first port in the range of ports, inclusive.

ToPort (integer) --
The last port in the range of ports, inclusive.





Protocol (string) --
The protocol for the connections from clients to the accelerator.

ClientAffinity (string) --
Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Clienty affinity gives you control over whether to always route each client to the same specific endpoint.
AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is NONE , Global Accelerator uses the "five-tuple" (5-tuple) properties\xe2\x80\x94source IP address, source port, destination IP address, destination port, and protocol\xe2\x80\x94to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.
If you want a given client to always be routed to the same endpoint, set client affinity to SOURCE_IP instead. When you use the SOURCE_IP setting, Global Accelerator uses the "two-tuple" (2-tuple) properties\xe2\x80\x94 source (client) IP address and destination IP address\xe2\x80\x94to select the hash value.
The default value is NONE .





NextToken (string) --
The token for the next set of results. You receive this token from a previous call.







Exceptions

GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.InvalidNextTokenException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException


    :return: {
        'Listeners': [
            {
                'ListenerArn': 'string',
                'PortRanges': [
                    {
                        'FromPort': 123,
                        'ToPort': 123
                    },
                ],
                'Protocol': 'TCP'|'UDP',
                'ClientAffinity': 'NONE'|'SOURCE_IP'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    GlobalAccelerator.Client.exceptions.InvalidArgumentException
    GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
    GlobalAccelerator.Client.exceptions.InvalidNextTokenException
    GlobalAccelerator.Client.exceptions.InternalServiceErrorException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    List all tags for an accelerator. To see an AWS CLI example of listing tags for an accelerator, scroll down to Example .
    For more information, see Tagging in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the accelerator to list tags for. An ARN uniquely identifies an accelerator.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Tags (list) --Root level tag for the Tags parameters.

(dict) --A complex type that contains a Tag key and Tag value.

Key (string) --A string that contains a Tag key.

Value (string) --A string that contains a Tag value.










Exceptions

GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def provision_byoip_cidr(Cidr=None, CidrAuthorizationContext=None):
    """
    Provisions an IP address range to use with your AWS resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool. After the address range is provisioned, it is ready to be advertised using AdvertiseByoipCidr .
    To see an AWS CLI example of provisioning an address range for BYOIP, scroll down to Example .
    For more information, see Bring Your Own IP Addresses (BYOIP) in the AWS Global Accelerator Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.provision_byoip_cidr(
        Cidr='string',
        CidrAuthorizationContext={
            'Message': 'string',
            'Signature': 'string'
        }
    )
    
    
    :type Cidr: string
    :param Cidr: [REQUIRED]\nThe public IPv4 address range, in CIDR notation. The most specific IP prefix that you can specify is /24. The address range cannot overlap with another address range that you\'ve brought to this or another Region.\n

    :type CidrAuthorizationContext: dict
    :param CidrAuthorizationContext: [REQUIRED]\nA signed document that proves that you are authorized to bring the specified IP address range to Amazon using BYOIP.\n\nMessage (string) -- [REQUIRED]The plain-text authorization message for the prefix and account.\n\nSignature (string) -- [REQUIRED]The signed authorization message for the prefix and account.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ByoipCidr': {
        'Cidr': 'string',
        'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
        'Events': [
            {
                'Message': 'string',
                'Timestamp': datetime(2015, 1, 1)
            },
        ]
    }
}


Response Structure

(dict) --

ByoipCidr (dict) --
Information about the address range.

Cidr (string) --
The address range, in CIDR notation.

State (string) --
The state of the address pool.

Events (list) --
A history of status changes for an IP address range that that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

(dict) --
A complex type that contains a Message and a Timestamp value for changes that you make in the status an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Message (string) --
A string that contains an Event message describing changes that you make in the status of an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Timestamp (datetime) --
A timestamp when you make a status change for an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).













Exceptions

GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.LimitExceededException
GlobalAccelerator.Client.exceptions.AccessDeniedException
GlobalAccelerator.Client.exceptions.IncorrectCidrStateException


    :return: {
        'ByoipCidr': {
            'Cidr': 'string',
            'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
            'Events': [
                {
                    'Message': 'string',
                    'Timestamp': datetime(2015, 1, 1)
                },
            ]
        }
    }
    
    
    :returns: 
    GlobalAccelerator.Client.exceptions.InternalServiceErrorException
    GlobalAccelerator.Client.exceptions.InvalidArgumentException
    GlobalAccelerator.Client.exceptions.LimitExceededException
    GlobalAccelerator.Client.exceptions.AccessDeniedException
    GlobalAccelerator.Client.exceptions.IncorrectCidrStateException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Add tags to an accelerator resource. To see an AWS CLI example of adding tags to an accelerator, scroll down to Example .
    For more information, see Tagging in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Global Accelerator resource to add tags to. An ARN uniquely identifies a resource.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to add to a resource. A tag consists of a key and a value that you define.\n\n(dict) --A complex type that contains a Tag key and Tag value.\n\nKey (string) -- [REQUIRED]A string that contains a Tag key.\n\nValue (string) -- [REQUIRED]A string that contains a Tag value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Remove tags from a Global Accelerator resource. When you specify a tag key, the action removes both that key and its associated value. To see an AWS CLI example of removing tags from an accelerator, scroll down to Example . The operation succeeds even if you attempt to remove tags from an accelerator that was already removed.
    For more information, see Tagging in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Global Accelerator resource to remove tags from. An ARN uniquely identifies a resource.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag key pairs that you want to remove from the specified resources.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_accelerator(AcceleratorArn=None, Name=None, IpAddressType=None, Enabled=None):
    """
    Update an accelerator. To see an AWS CLI example of updating an accelerator, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_accelerator(
        AcceleratorArn='string',
        Name='string',
        IpAddressType='IPV4',
        Enabled=True|False
    )
    
    
    :type AcceleratorArn: string
    :param AcceleratorArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the accelerator to update.\n

    :type Name: string
    :param Name: The name of the accelerator. The name can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

    :type IpAddressType: string
    :param IpAddressType: The value for the address type must be IPv4.

    :type Enabled: boolean
    :param Enabled: Indicates whether an accelerator is enabled. The value is true or false. The default value is true.\nIf the value is set to true, the accelerator cannot be deleted. If set to false, the accelerator can be deleted.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Accelerator': {
        'AcceleratorArn': 'string',
        'Name': 'string',
        'IpAddressType': 'IPV4',
        'Enabled': True|False,
        'IpSets': [
            {
                'IpFamily': 'string',
                'IpAddresses': [
                    'string',
                ]
            },
        ],
        'DnsName': 'string',
        'Status': 'DEPLOYED'|'IN_PROGRESS',
        'CreatedTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

Accelerator (dict) --
Information about the updated accelerator.

AcceleratorArn (string) --
The Amazon Resource Name (ARN) of the accelerator.

Name (string) --
The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

IpAddressType (string) --
The value for the address type must be IPv4.

Enabled (boolean) --
Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.

IpSets (list) --
The static IP addresses that Global Accelerator associates with the accelerator.

(dict) --
A complex type for the set of IP addresses for an accelerator.

IpFamily (string) --
The types of IP addresses included in this IP set.

IpAddresses (list) --
The array of IP addresses in the IP address set. An IP address set can have a maximum of two IP addresses.

(string) --






DnsName (string) --
The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator\'s static IP addresses.
The naming convention for the DNS name is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .awsglobalaccelerator.com. For example: a1234567890abcdef.awsglobalaccelerator.com.
For more information about the default DNS name, see Support for DNS Addressing in Global Accelerator in the AWS Global Accelerator Developer Guide .

Status (string) --
Describes the deployment status of the accelerator.

CreatedTime (datetime) --
The date and time that the accelerator was created.

LastModifiedTime (datetime) --
The date and time that the accelerator was last modified.









Exceptions

GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException


    :return: {
        'Accelerator': {
            'AcceleratorArn': 'string',
            'Name': 'string',
            'IpAddressType': 'IPV4',
            'Enabled': True|False,
            'IpSets': [
                {
                    'IpFamily': 'string',
                    'IpAddresses': [
                        'string',
                    ]
                },
            ],
            'DnsName': 'string',
            'Status': 'DEPLOYED'|'IN_PROGRESS',
            'CreatedTime': datetime(2015, 1, 1),
            'LastModifiedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_accelerator_attributes(AcceleratorArn=None, FlowLogsEnabled=None, FlowLogsS3Bucket=None, FlowLogsS3Prefix=None):
    """
    Update the attributes for an accelerator. To see an AWS CLI example of updating an accelerator to enable flow logs, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_accelerator_attributes(
        AcceleratorArn='string',
        FlowLogsEnabled=True|False,
        FlowLogsS3Bucket='string',
        FlowLogsS3Prefix='string'
    )
    
    
    :type AcceleratorArn: string
    :param AcceleratorArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the accelerator that you want to update.\n

    :type FlowLogsEnabled: boolean
    :param FlowLogsEnabled: Update whether flow logs are enabled. The default value is false. If the value is true, FlowLogsS3Bucket and FlowLogsS3Prefix must be specified.\nFor more information, see Flow Logs in the AWS Global Accelerator Developer Guide .\n

    :type FlowLogsS3Bucket: string
    :param FlowLogsS3Bucket: The name of the Amazon S3 bucket for the flow logs. Attribute is required if FlowLogsEnabled is true . The bucket must exist and have a bucket policy that grants AWS Global Accelerator permission to write to the bucket.

    :type FlowLogsS3Prefix: string
    :param FlowLogsS3Prefix: Update the prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if FlowLogsEnabled is true .\nIf you don\xe2\x80\x99t specify a prefix, the flow logs are stored in the root of the bucket. If you specify slash (/) for the S3 bucket prefix, the log file bucket folder structure will include a double slash (//), like the following:\ns3-bucket_name//AWSLogs/aws_account_id\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AcceleratorAttributes': {
        'FlowLogsEnabled': True|False,
        'FlowLogsS3Bucket': 'string',
        'FlowLogsS3Prefix': 'string'
    }
}


Response Structure

(dict) --

AcceleratorAttributes (dict) --
Updated attributes for the accelerator.

FlowLogsEnabled (boolean) --
Indicates whether flow logs are enabled. The default value is false. If the value is true, FlowLogsS3Bucket and FlowLogsS3Prefix must be specified.
For more information, see Flow Logs in the AWS Global Accelerator Developer Guide .

FlowLogsS3Bucket (string) --
The name of the Amazon S3 bucket for the flow logs. Attribute is required if FlowLogsEnabled is true . The bucket must exist and have a bucket policy that grants AWS Global Accelerator permission to write to the bucket.

FlowLogsS3Prefix (string) --
The prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if FlowLogsEnabled is true .
If you don\xe2\x80\x99t specify a prefix, the flow logs are stored in the root of the bucket. If you specify slash (/) for the S3 bucket prefix, the log file bucket folder structure will include a double slash (//), like the following:
s3-bucket_name//AWSLogs/aws_account_id









Exceptions

GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.AccessDeniedException


    :return: {
        'AcceleratorAttributes': {
            'FlowLogsEnabled': True|False,
            'FlowLogsS3Bucket': 'string',
            'FlowLogsS3Prefix': 'string'
        }
    }
    
    
    :returns: 
    GlobalAccelerator.Client.exceptions.AcceleratorNotFoundException
    GlobalAccelerator.Client.exceptions.InternalServiceErrorException
    GlobalAccelerator.Client.exceptions.InvalidArgumentException
    GlobalAccelerator.Client.exceptions.AccessDeniedException
    
    """
    pass

def update_endpoint_group(EndpointGroupArn=None, EndpointConfigurations=None, TrafficDialPercentage=None, HealthCheckPort=None, HealthCheckProtocol=None, HealthCheckPath=None, HealthCheckIntervalSeconds=None, ThresholdCount=None):
    """
    Update an endpoint group. To see an AWS CLI example of updating an endpoint group, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_endpoint_group(
        EndpointGroupArn='string',
        EndpointConfigurations=[
            {
                'EndpointId': 'string',
                'Weight': 123,
                'ClientIPPreservationEnabled': True|False
            },
        ],
        TrafficDialPercentage=...,
        HealthCheckPort=123,
        HealthCheckProtocol='TCP'|'HTTP'|'HTTPS',
        HealthCheckPath='string',
        HealthCheckIntervalSeconds=123,
        ThresholdCount=123
    )
    
    
    :type EndpointGroupArn: string
    :param EndpointGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the endpoint group.\n

    :type EndpointConfigurations: list
    :param EndpointConfigurations: The list of endpoint objects.\n\n(dict) --A complex type for endpoints.\n\nEndpointId (string) --An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For EC2 instances, this is the EC2 instance ID.\nAn Application Load Balancer can be either internal or internet-facing.\n\nWeight (integer) --The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see Endpoint Weights in the AWS Global Accelerator Developer Guide .\n\nClientIPPreservationEnabled (boolean) --Indicates whether client IP address preservation is enabled for an Application Load Balancer endpoint. The value is true or false. The default value is true for new accelerators.\nIf the value is set to true, the client\'s IP address is preserved in the X-Forwarded-For request header as traffic travels to applications on the Application Load Balancer endpoint fronted by the accelerator.\nFor more information, see Preserve Client IP Addresses in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .\n\n\n\n\n

    :type TrafficDialPercentage: float
    :param TrafficDialPercentage: The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.\nUse this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.\nThe default value is 100.\n

    :type HealthCheckPort: integer
    :param HealthCheckPort: The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If the listener port is a list of ports, Global Accelerator uses the first port in the list.

    :type HealthCheckProtocol: string
    :param HealthCheckProtocol: The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.

    :type HealthCheckPath: string
    :param HealthCheckPath: If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).

    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: The time\xe2\x80\x9410 seconds or 30 seconds\xe2\x80\x94between each health check for an endpoint. The default value is 30.

    :type ThresholdCount: integer
    :param ThresholdCount: The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.

    :rtype: dict

ReturnsResponse Syntax
{
    'EndpointGroup': {
        'EndpointGroupArn': 'string',
        'EndpointGroupRegion': 'string',
        'EndpointDescriptions': [
            {
                'EndpointId': 'string',
                'Weight': 123,
                'HealthState': 'INITIAL'|'HEALTHY'|'UNHEALTHY',
                'HealthReason': 'string',
                'ClientIPPreservationEnabled': True|False
            },
        ],
        'TrafficDialPercentage': ...,
        'HealthCheckPort': 123,
        'HealthCheckProtocol': 'TCP'|'HTTP'|'HTTPS',
        'HealthCheckPath': 'string',
        'HealthCheckIntervalSeconds': 123,
        'ThresholdCount': 123
    }
}


Response Structure

(dict) --

EndpointGroup (dict) --
The information about the endpoint group that was updated.

EndpointGroupArn (string) --
The Amazon Resource Name (ARN) of the endpoint group.

EndpointGroupRegion (string) --
The AWS Region that this endpoint group belongs.

EndpointDescriptions (list) --
The list of endpoint objects.

(dict) --
A complex type for an endpoint. Each endpoint group can include one or more endpoints, such as load balancers.

EndpointId (string) --
An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For EC2 instances, this is the EC2 instance ID.
An Application Load Balancer can be either internal or internet-facing.

Weight (integer) --
The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see Endpoint Weights in the AWS Global Accelerator Developer Guide .

HealthState (string) --
The health status of the endpoint.

HealthReason (string) --
The reason code associated with why the endpoint is not healthy. If the endpoint state is healthy, a reason code is not provided.
If the endpoint state is unhealthy , the reason code can be one of the following values:

Timeout : The health check requests to the endpoint are timing out before returning a status.
Failed : The health check failed, for example because the endpoint response was invalid (malformed).

If the endpoint state is initial , the reason code can be one of the following values:

ProvisioningInProgress : The endpoint is in the process of being provisioned.
InitialHealthChecking : Global Accelerator is still setting up the minimum number of health checks for the endpoint that are required to determine its health status.


ClientIPPreservationEnabled (boolean) --
Indicates whether client IP address preservation is enabled for an Application Load Balancer endpoint. The value is true or false. The default value is true for new accelerators.
If the value is set to true, the client\'s IP address is preserved in the X-Forwarded-For request header as traffic travels to applications on the Application Load Balancer endpoint fronted by the accelerator.
For more information, see Viewing Client IP Addresses in AWS Global Accelerator in the AWS Global Accelerator Developer Guide .





TrafficDialPercentage (float) --
The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.
Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.
The default value is 100.

HealthCheckPort (integer) --
The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.
The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.

HealthCheckProtocol (string) --
The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.

HealthCheckPath (string) --
If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).

HealthCheckIntervalSeconds (integer) --
The time\xe2\x80\x9410 seconds or 30 seconds\xe2\x80\x94between health checks for each endpoint. The default value is 30.

ThresholdCount (integer) --
The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.









Exceptions

GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.EndpointGroupNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.LimitExceededException
GlobalAccelerator.Client.exceptions.AccessDeniedException


    :return: {
        'EndpointGroup': {
            'EndpointGroupArn': 'string',
            'EndpointGroupRegion': 'string',
            'EndpointDescriptions': [
                {
                    'EndpointId': 'string',
                    'Weight': 123,
                    'HealthState': 'INITIAL'|'HEALTHY'|'UNHEALTHY',
                    'HealthReason': 'string',
                    'ClientIPPreservationEnabled': True|False
                },
            ],
            'TrafficDialPercentage': ...,
            'HealthCheckPort': 123,
            'HealthCheckProtocol': 'TCP'|'HTTP'|'HTTPS',
            'HealthCheckPath': 'string',
            'HealthCheckIntervalSeconds': 123,
            'ThresholdCount': 123
        }
    }
    
    
    :returns: 
    Timeout : The health check requests to the endpoint are timing out before returning a status.
    Failed : The health check failed, for example because the endpoint response was invalid (malformed).
    
    """
    pass

def update_listener(ListenerArn=None, PortRanges=None, Protocol=None, ClientAffinity=None):
    """
    Update a listener. To see an AWS CLI example of updating listener, scroll down to Example .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_listener(
        ListenerArn='string',
        PortRanges=[
            {
                'FromPort': 123,
                'ToPort': 123
            },
        ],
        Protocol='TCP'|'UDP',
        ClientAffinity='NONE'|'SOURCE_IP'
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the listener to update.\n

    :type PortRanges: list
    :param PortRanges: The updated list of port ranges for the connections from clients to the accelerator.\n\n(dict) --A complex type for a range of ports for a listener.\n\nFromPort (integer) --The first port in the range of ports, inclusive.\n\nToPort (integer) --The last port in the range of ports, inclusive.\n\n\n\n\n

    :type Protocol: string
    :param Protocol: The updated protocol for the connections from clients to the accelerator.

    :type ClientAffinity: string
    :param ClientAffinity: Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Clienty affinity gives you control over whether to always route each client to the same specific endpoint.\nAWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is NONE , Global Accelerator uses the 'five-tuple' (5-tuple) properties\xe2\x80\x94source IP address, source port, destination IP address, destination port, and protocol\xe2\x80\x94to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.\nIf you want a given client to always be routed to the same endpoint, set client affinity to SOURCE_IP instead. When you use the SOURCE_IP setting, Global Accelerator uses the 'two-tuple' (2-tuple) properties\xe2\x80\x94 source (client) IP address and destination IP address\xe2\x80\x94to select the hash value.\nThe default value is NONE .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Listener': {
        'ListenerArn': 'string',
        'PortRanges': [
            {
                'FromPort': 123,
                'ToPort': 123
            },
        ],
        'Protocol': 'TCP'|'UDP',
        'ClientAffinity': 'NONE'|'SOURCE_IP'
    }
}


Response Structure

(dict) --

Listener (dict) --
Information for the updated listener.

ListenerArn (string) --
The Amazon Resource Name (ARN) of the listener.

PortRanges (list) --
The list of port ranges for the connections from clients to the accelerator.

(dict) --
A complex type for a range of ports for a listener.

FromPort (integer) --
The first port in the range of ports, inclusive.

ToPort (integer) --
The last port in the range of ports, inclusive.





Protocol (string) --
The protocol for the connections from clients to the accelerator.

ClientAffinity (string) --
Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Clienty affinity gives you control over whether to always route each client to the same specific endpoint.
AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is NONE , Global Accelerator uses the "five-tuple" (5-tuple) properties\xe2\x80\x94source IP address, source port, destination IP address, destination port, and protocol\xe2\x80\x94to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.
If you want a given client to always be routed to the same endpoint, set client affinity to SOURCE_IP instead. When you use the SOURCE_IP setting, Global Accelerator uses the "two-tuple" (2-tuple) properties\xe2\x80\x94 source (client) IP address and destination IP address\xe2\x80\x94to select the hash value.
The default value is NONE .









Exceptions

GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.InvalidPortRangeException
GlobalAccelerator.Client.exceptions.ListenerNotFoundException
GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.LimitExceededException


    :return: {
        'Listener': {
            'ListenerArn': 'string',
            'PortRanges': [
                {
                    'FromPort': 123,
                    'ToPort': 123
                },
            ],
            'Protocol': 'TCP'|'UDP',
            'ClientAffinity': 'NONE'|'SOURCE_IP'
        }
    }
    
    
    :returns: 
    GlobalAccelerator.Client.exceptions.InvalidArgumentException
    GlobalAccelerator.Client.exceptions.InvalidPortRangeException
    GlobalAccelerator.Client.exceptions.ListenerNotFoundException
    GlobalAccelerator.Client.exceptions.InternalServiceErrorException
    GlobalAccelerator.Client.exceptions.LimitExceededException
    
    """
    pass

def withdraw_byoip_cidr(Cidr=None):
    """
    Stops advertising an address range that is provisioned as an address pool. You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time. To see an AWS CLI example of withdrawing an address range for BYOIP so it will no longer be advertised by AWS, scroll down to Example .
    It can take a few minutes before traffic to the specified addresses stops routing to AWS because of propagation delays.
    For more information, see Bring Your Own IP Addresses (BYOIP) in the AWS Global Accelerator Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.withdraw_byoip_cidr(
        Cidr='string'
    )
    
    
    :type Cidr: string
    :param Cidr: [REQUIRED]\nThe address range, in CIDR notation.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ByoipCidr': {
        'Cidr': 'string',
        'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
        'Events': [
            {
                'Message': 'string',
                'Timestamp': datetime(2015, 1, 1)
            },
        ]
    }
}


Response Structure

(dict) --
ByoipCidr (dict) --Information about the address pool.

Cidr (string) --The address range, in CIDR notation.

State (string) --The state of the address pool.

Events (list) --A history of status changes for an IP address range that that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

(dict) --A complex type that contains a Message and a Timestamp value for changes that you make in the status an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Message (string) --A string that contains an Event message describing changes that you make in the status of an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).

Timestamp (datetime) --A timestamp when you make a status change for an IP address range that you bring to AWS Global Accelerator through bring your own IP address (BYOIP).












Exceptions

GlobalAccelerator.Client.exceptions.InternalServiceErrorException
GlobalAccelerator.Client.exceptions.InvalidArgumentException
GlobalAccelerator.Client.exceptions.AccessDeniedException
GlobalAccelerator.Client.exceptions.ByoipCidrNotFoundException
GlobalAccelerator.Client.exceptions.IncorrectCidrStateException


    :return: {
        'ByoipCidr': {
            'Cidr': 'string',
            'State': 'PENDING_PROVISIONING'|'READY'|'PENDING_ADVERTISING'|'ADVERTISING'|'PENDING_WITHDRAWING'|'PENDING_DEPROVISIONING'|'DEPROVISIONED'|'FAILED_PROVISION'|'FAILED_ADVERTISING'|'FAILED_WITHDRAW'|'FAILED_DEPROVISION',
            'Events': [
                {
                    'Message': 'string',
                    'Timestamp': datetime(2015, 1, 1)
                },
            ]
        }
    }
    
    
    """
    pass

