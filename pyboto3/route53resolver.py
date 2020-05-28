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

def associate_resolver_endpoint_ip_address(ResolverEndpointId=None, IpAddress=None):
    """
    Adds IP addresses to an inbound or an outbound resolver endpoint. If you want to adding more than one IP address, submit one AssociateResolverEndpointIpAddress request for each IP address.
    To remove an IP address from an endpoint, see  DisassociateResolverEndpointIpAddress .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_resolver_endpoint_ip_address(
        ResolverEndpointId='string',
        IpAddress={
            'IpId': 'string',
            'SubnetId': 'string',
            'Ip': 'string'
        }
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]\nThe ID of the resolver endpoint that you want to associate IP addresses with.\n

    :type IpAddress: dict
    :param IpAddress: [REQUIRED]\nEither the IPv4 address that you want to add to a resolver endpoint or a subnet ID. If you specify a subnet ID, Resolver chooses an IP address for you from the available IPs in the specified subnet.\n\nIpId (string) --\nOnly when removing an IP address from a resolver endpoint : The ID of the IP address that you want to remove. To get this ID, use GetResolverEndpoint .\n\nSubnetId (string) --The ID of the subnet that includes the IP address that you want to update. To get this ID, use GetResolverEndpoint .\n\nIp (string) --The new IP address.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResolverEndpoint': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'Name': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'Direction': 'INBOUND'|'OUTBOUND',
        'IpAddressCount': 123,
        'HostVPCId': 'string',
        'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
        'StatusMessage': 'string',
        'CreationTime': 'string',
        'ModificationTime': 'string'
    }
}


Response Structure

(dict) --

ResolverEndpoint (dict) --
The response to an AssociateResolverEndpointIpAddress request.

Id (string) --
The ID of the resolver endpoint.

CreatorRequestId (string) --
A unique string that identifies the request that created the resolver endpoint. The CreatorRequestId allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --
The ARN (Amazon Resource Name) for the resolver endpoint.

Name (string) --
The name that you assigned to the resolver endpoint when you submitted a  CreateResolverEndpoint request.

SecurityGroupIds (list) --
The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound resolver rules.

(string) --


Direction (string) --
Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

INBOUND : allows DNS queries to your VPC from your network or another VPC
OUTBOUND : allows DNS queries from your VPC to your network or another VPC


IpAddressCount (integer) --
The number of IP addresses that the resolver endpoint can use for DNS queries.

HostVPCId (string) --
The ID of the VPC that you want to create the resolver endpoint in.

Status (string) --
A code that specifies the current status of the resolver endpoint.

StatusMessage (string) --
A detailed description of the status of the resolver endpoint.

CreationTime (string) --
The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime (string) --
The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).









Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.ResourceExistsException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.LimitExceededException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def associate_resolver_rule(ResolverRuleId=None, Name=None, VPCId=None):
    """
    Associates a resolver rule with a VPC. When you associate a rule with a VPC, Resolver forwards all DNS queries for the domain name that is specified in the rule and that originate in the VPC. The queries are forwarded to the IP addresses for the DNS resolvers that are specified in the rule. For more information about rules, see  CreateResolverRule .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_resolver_rule(
        ResolverRuleId='string',
        Name='string',
        VPCId='string'
    )
    
    
    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]\nThe ID of the resolver rule that you want to associate with the VPC. To list the existing resolver rules, use ListResolverRules .\n

    :type Name: string
    :param Name: A name for the association that you\'re creating between a resolver rule and a VPC.

    :type VPCId: string
    :param VPCId: [REQUIRED]\nThe ID of the VPC that you want to associate the resolver rule with.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResolverRuleAssociation': {
        'Id': 'string',
        'ResolverRuleId': 'string',
        'Name': 'string',
        'VPCId': 'string',
        'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
        'StatusMessage': 'string'
    }
}


Response Structure

(dict) --

ResolverRuleAssociation (dict) --
Information about the AssociateResolverRule request, including the status of the request.

Id (string) --
The ID of the association between a resolver rule and a VPC. Resolver assigns this value when you submit an  AssociateResolverRule request.

ResolverRuleId (string) --
The ID of the resolver rule that you associated with the VPC that is specified by VPCId .

Name (string) --
The name of an association between a resolver rule and a VPC.

VPCId (string) --
The ID of the VPC that you associated the resolver rule with.

Status (string) --
A code that specifies the current status of the association between a resolver rule and a VPC.

StatusMessage (string) --
A detailed description of the status of the association between a resolver rule and a VPC.









Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.ResourceUnavailableException
Route53Resolver.Client.exceptions.ResourceExistsException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverRuleAssociation': {
            'Id': 'string',
            'ResolverRuleId': 'string',
            'Name': 'string',
            'VPCId': 'string',
            'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
            'StatusMessage': 'string'
        }
    }
    
    
    :returns: 
    Route53Resolver.Client.exceptions.ResourceNotFoundException
    Route53Resolver.Client.exceptions.InvalidRequestException
    Route53Resolver.Client.exceptions.InvalidParameterException
    Route53Resolver.Client.exceptions.ResourceUnavailableException
    Route53Resolver.Client.exceptions.ResourceExistsException
    Route53Resolver.Client.exceptions.InternalServiceErrorException
    Route53Resolver.Client.exceptions.ThrottlingException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_resolver_endpoint(CreatorRequestId=None, Name=None, SecurityGroupIds=None, Direction=None, IpAddresses=None, Tags=None):
    """
    Creates a resolver endpoint. There are two types of resolver endpoints, inbound and outbound:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_resolver_endpoint(
        CreatorRequestId='string',
        Name='string',
        SecurityGroupIds=[
            'string',
        ],
        Direction='INBOUND'|'OUTBOUND',
        IpAddresses=[
            {
                'SubnetId': 'string',
                'Ip': 'string'
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CreatorRequestId: string
    :param CreatorRequestId: [REQUIRED]\nA unique string that identifies the request and that allows failed requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.\n

    :type Name: string
    :param Name: A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.

    :type SecurityGroupIds: list
    :param SecurityGroupIds: [REQUIRED]\nThe ID of one or more security groups that you want to use to control access to this VPC. The security group that you specify must include one or more inbound rules (for inbound resolver endpoints) or outbound rules (for outbound resolver endpoints).\n\n(string) --\n\n

    :type Direction: string
    :param Direction: [REQUIRED]\nSpecify the applicable value:\n\nINBOUND : Resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC\nOUTBOUND : Resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC\n\n

    :type IpAddresses: list
    :param IpAddresses: [REQUIRED]\nThe subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound resolver endpoints).\n\n(dict) --In an CreateResolverEndpoint request, a subnet and IP address that you want to use for DNS queries.\n\nSubnetId (string) -- [REQUIRED]The subnet that contains the IP address.\n\nIp (string) --The IP address that you want to use for DNS queries.\n\n\n\n\n

    :type Tags: list
    :param Tags: A list of the tag keys and values that you want to associate with the endpoint.\n\n(dict) --One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .\n\nKey (string) --The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .\n\nValue (string) --The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that you\'re creating the resource for.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResolverEndpoint': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'Name': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'Direction': 'INBOUND'|'OUTBOUND',
        'IpAddressCount': 123,
        'HostVPCId': 'string',
        'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
        'StatusMessage': 'string',
        'CreationTime': 'string',
        'ModificationTime': 'string'
    }
}


Response Structure

(dict) --

ResolverEndpoint (dict) --
Information about the CreateResolverEndpoint request, including the status of the request.

Id (string) --
The ID of the resolver endpoint.

CreatorRequestId (string) --
A unique string that identifies the request that created the resolver endpoint. The CreatorRequestId allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --
The ARN (Amazon Resource Name) for the resolver endpoint.

Name (string) --
The name that you assigned to the resolver endpoint when you submitted a  CreateResolverEndpoint request.

SecurityGroupIds (list) --
The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound resolver rules.

(string) --


Direction (string) --
Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

INBOUND : allows DNS queries to your VPC from your network or another VPC
OUTBOUND : allows DNS queries from your VPC to your network or another VPC


IpAddressCount (integer) --
The number of IP addresses that the resolver endpoint can use for DNS queries.

HostVPCId (string) --
The ID of the VPC that you want to create the resolver endpoint in.

Status (string) --
A code that specifies the current status of the resolver endpoint.

StatusMessage (string) --
A detailed description of the status of the resolver endpoint.

CreationTime (string) --
The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime (string) --
The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).









Exceptions

Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.ResourceExistsException
Route53Resolver.Client.exceptions.LimitExceededException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    CreatorRequestId (string) -- [REQUIRED]
    A unique string that identifies the request and that allows failed requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
    
    Name (string) -- A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.
    SecurityGroupIds (list) -- [REQUIRED]
    The ID of one or more security groups that you want to use to control access to this VPC. The security group that you specify must include one or more inbound rules (for inbound resolver endpoints) or outbound rules (for outbound resolver endpoints).
    
    (string) --
    
    
    Direction (string) -- [REQUIRED]
    Specify the applicable value:
    
    INBOUND : Resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC
    OUTBOUND : Resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC
    
    
    IpAddresses (list) -- [REQUIRED]
    The subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound resolver endpoints).
    
    (dict) --In an  CreateResolverEndpoint request, a subnet and IP address that you want to use for DNS queries.
    
    SubnetId (string) -- [REQUIRED]The subnet that contains the IP address.
    
    Ip (string) --The IP address that you want to use for DNS queries.
    
    
    
    
    
    Tags (list) -- A list of the tag keys and values that you want to associate with the endpoint.
    
    (dict) --One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .
    
    Key (string) --The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .
    
    Value (string) --The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that you\'re creating the resource for.
    
    
    
    
    
    
    """
    pass

def create_resolver_rule(CreatorRequestId=None, Name=None, RuleType=None, DomainName=None, TargetIps=None, ResolverEndpointId=None, Tags=None):
    """
    For DNS queries that originate in your VPCs, specifies which resolver endpoint the queries pass through, one domain name that you want to forward to your network, and the IP addresses of the DNS resolvers in your network.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_resolver_rule(
        CreatorRequestId='string',
        Name='string',
        RuleType='FORWARD'|'SYSTEM'|'RECURSIVE',
        DomainName='string',
        TargetIps=[
            {
                'Ip': 'string',
                'Port': 123
            },
        ],
        ResolverEndpointId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type CreatorRequestId: string
    :param CreatorRequestId: [REQUIRED]\nA unique string that identifies the request and that allows failed requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.\n

    :type Name: string
    :param Name: A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.

    :type RuleType: string
    :param RuleType: [REQUIRED]\nSpecify FORWARD . Other resolver rule types aren\'t supported.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nDNS queries for this domain name are forwarded to the IP addresses that you specify in TargetIps . If a query matches multiple resolver rules (example.com and www.example.com), outbound DNS queries are routed using the resolver rule that contains the most specific domain name (www.example.com).\n

    :type TargetIps: list
    :param TargetIps: The IPs that you want Resolver to forward DNS queries to. You can specify only IPv4 addresses. Separate IP addresses with a comma.\n\n(dict) --In a CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.\n\nIp (string) -- [REQUIRED]One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.\n\nPort (integer) --The port at Ip that you want to forward DNS queries to.\n\n\n\n\n

    :type ResolverEndpointId: string
    :param ResolverEndpointId: The ID of the outbound resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in TargetIps .

    :type Tags: list
    :param Tags: A list of the tag keys and values that you want to associate with the endpoint.\n\n(dict) --One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .\n\nKey (string) --The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .\n\nValue (string) --The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that you\'re creating the resource for.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResolverRule': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'DomainName': 'string',
        'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
        'StatusMessage': 'string',
        'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
        'Name': 'string',
        'TargetIps': [
            {
                'Ip': 'string',
                'Port': 123
            },
        ],
        'ResolverEndpointId': 'string',
        'OwnerId': 'string',
        'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
    }
}


Response Structure

(dict) --

ResolverRule (dict) --
Information about the CreateResolverRule request, including the status of the request.

Id (string) --
The ID that Resolver assigned to the resolver rule when you created it.

CreatorRequestId (string) --
A unique string that you specified when you created the resolver rule. CreatorRequestId identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --
The ARN (Amazon Resource Name) for the resolver rule specified by Id .

DomainName (string) --
DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps . If a query matches multiple resolver rules (example.com and www.example.com), the query is routed using the resolver rule that contains the most specific domain name (www.example.com).

Status (string) --
A code that specifies the current status of the resolver rule.

StatusMessage (string) --
A detailed description of the status of a resolver rule.

RuleType (string) --
This value is always FORWARD . Other resolver rule types aren\'t supported.

Name (string) --
The name for the resolver rule, which you specified when you created the resolver rule.

TargetIps (list) --
An array that contains the IP addresses and ports that you want to forward

(dict) --
In a  CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.

Ip (string) --
One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.

Port (integer) --
The port at Ip that you want to forward DNS queries to.





ResolverEndpointId (string) --
The ID of the endpoint that the rule is associated with.

OwnerId (string) --
When a rule is shared with another AWS account, the account ID of the account that the rule is shared with.

ShareStatus (string) --
Whether the rules is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.









Exceptions

Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.LimitExceededException
Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.ResourceExistsException
Route53Resolver.Client.exceptions.ResourceUnavailableException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverRule': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'DomainName': 'string',
            'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
            'StatusMessage': 'string',
            'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string',
            'OwnerId': 'string',
            'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
        }
    }
    
    
    :returns: 
    Route53Resolver.Client.exceptions.InvalidParameterException
    Route53Resolver.Client.exceptions.InvalidRequestException
    Route53Resolver.Client.exceptions.LimitExceededException
    Route53Resolver.Client.exceptions.ResourceNotFoundException
    Route53Resolver.Client.exceptions.ResourceExistsException
    Route53Resolver.Client.exceptions.ResourceUnavailableException
    Route53Resolver.Client.exceptions.InternalServiceErrorException
    Route53Resolver.Client.exceptions.ThrottlingException
    
    """
    pass

def delete_resolver_endpoint(ResolverEndpointId=None):
    """
    Deletes a resolver endpoint. The effect of deleting a resolver endpoint depends on whether it\'s an inbound or an outbound resolver endpoint:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resolver_endpoint(
        ResolverEndpointId='string'
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]\nThe ID of the resolver endpoint that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ResolverEndpoint': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'Name': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'Direction': 'INBOUND'|'OUTBOUND',
        'IpAddressCount': 123,
        'HostVPCId': 'string',
        'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
        'StatusMessage': 'string',
        'CreationTime': 'string',
        'ModificationTime': 'string'
    }
}


Response Structure

(dict) --
ResolverEndpoint (dict) --Information about the DeleteResolverEndpoint request, including the status of the request.

Id (string) --The ID of the resolver endpoint.

CreatorRequestId (string) --A unique string that identifies the request that created the resolver endpoint. The CreatorRequestId allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --The ARN (Amazon Resource Name) for the resolver endpoint.

Name (string) --The name that you assigned to the resolver endpoint when you submitted a  CreateResolverEndpoint request.

SecurityGroupIds (list) --The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound resolver rules.

(string) --


Direction (string) --Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

INBOUND : allows DNS queries to your VPC from your network or another VPC
OUTBOUND : allows DNS queries from your VPC to your network or another VPC


IpAddressCount (integer) --The number of IP addresses that the resolver endpoint can use for DNS queries.

HostVPCId (string) --The ID of the VPC that you want to create the resolver endpoint in.

Status (string) --A code that specifies the current status of the resolver endpoint.

StatusMessage (string) --A detailed description of the status of the resolver endpoint.

CreationTime (string) --The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime (string) --The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).








Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_resolver_rule(ResolverRuleId=None):
    """
    Deletes a resolver rule. Before you can delete a resolver rule, you must disassociate it from all the VPCs that you associated the resolver rule with. For more infomation, see  DisassociateResolverRule .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resolver_rule(
        ResolverRuleId='string'
    )
    
    
    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]\nThe ID of the resolver rule that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ResolverRule': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'DomainName': 'string',
        'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
        'StatusMessage': 'string',
        'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
        'Name': 'string',
        'TargetIps': [
            {
                'Ip': 'string',
                'Port': 123
            },
        ],
        'ResolverEndpointId': 'string',
        'OwnerId': 'string',
        'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
    }
}


Response Structure

(dict) --
ResolverRule (dict) --Information about the DeleteResolverRule request, including the status of the request.

Id (string) --The ID that Resolver assigned to the resolver rule when you created it.

CreatorRequestId (string) --A unique string that you specified when you created the resolver rule. CreatorRequestId identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --The ARN (Amazon Resource Name) for the resolver rule specified by Id .

DomainName (string) --DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps . If a query matches multiple resolver rules (example.com and www.example.com), the query is routed using the resolver rule that contains the most specific domain name (www.example.com).

Status (string) --A code that specifies the current status of the resolver rule.

StatusMessage (string) --A detailed description of the status of a resolver rule.

RuleType (string) --This value is always FORWARD . Other resolver rule types aren\'t supported.

Name (string) --The name for the resolver rule, which you specified when you created the resolver rule.

TargetIps (list) --An array that contains the IP addresses and ports that you want to forward

(dict) --In a  CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.

Ip (string) --One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.

Port (integer) --The port at Ip that you want to forward DNS queries to.





ResolverEndpointId (string) --The ID of the endpoint that the rule is associated with.

OwnerId (string) --When a rule is shared with another AWS account, the account ID of the account that the rule is shared with.

ShareStatus (string) --Whether the rules is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.








Exceptions

Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.ResourceInUseException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverRule': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'DomainName': 'string',
            'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
            'StatusMessage': 'string',
            'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string',
            'OwnerId': 'string',
            'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
        }
    }
    
    
    """
    pass

def disassociate_resolver_endpoint_ip_address(ResolverEndpointId=None, IpAddress=None):
    """
    Removes IP addresses from an inbound or an outbound resolver endpoint. If you want to remove more than one IP address, submit one DisassociateResolverEndpointIpAddress request for each IP address.
    To add an IP address to an endpoint, see  AssociateResolverEndpointIpAddress .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_resolver_endpoint_ip_address(
        ResolverEndpointId='string',
        IpAddress={
            'IpId': 'string',
            'SubnetId': 'string',
            'Ip': 'string'
        }
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]\nThe ID of the resolver endpoint that you want to disassociate an IP address from.\n

    :type IpAddress: dict
    :param IpAddress: [REQUIRED]\nThe IPv4 address that you want to remove from a resolver endpoint.\n\nIpId (string) --\nOnly when removing an IP address from a resolver endpoint : The ID of the IP address that you want to remove. To get this ID, use GetResolverEndpoint .\n\nSubnetId (string) --The ID of the subnet that includes the IP address that you want to update. To get this ID, use GetResolverEndpoint .\n\nIp (string) --The new IP address.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResolverEndpoint': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'Name': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'Direction': 'INBOUND'|'OUTBOUND',
        'IpAddressCount': 123,
        'HostVPCId': 'string',
        'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
        'StatusMessage': 'string',
        'CreationTime': 'string',
        'ModificationTime': 'string'
    }
}


Response Structure

(dict) --

ResolverEndpoint (dict) --
The response to an DisassociateResolverEndpointIpAddress request.

Id (string) --
The ID of the resolver endpoint.

CreatorRequestId (string) --
A unique string that identifies the request that created the resolver endpoint. The CreatorRequestId allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --
The ARN (Amazon Resource Name) for the resolver endpoint.

Name (string) --
The name that you assigned to the resolver endpoint when you submitted a  CreateResolverEndpoint request.

SecurityGroupIds (list) --
The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound resolver rules.

(string) --


Direction (string) --
Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

INBOUND : allows DNS queries to your VPC from your network or another VPC
OUTBOUND : allows DNS queries from your VPC to your network or another VPC


IpAddressCount (integer) --
The number of IP addresses that the resolver endpoint can use for DNS queries.

HostVPCId (string) --
The ID of the VPC that you want to create the resolver endpoint in.

Status (string) --
A code that specifies the current status of the resolver endpoint.

StatusMessage (string) --
A detailed description of the status of the resolver endpoint.

CreationTime (string) --
The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime (string) --
The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).









Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.ResourceExistsException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def disassociate_resolver_rule(VPCId=None, ResolverRuleId=None):
    """
    Removes the association between a specified resolver rule and a specified VPC.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_resolver_rule(
        VPCId='string',
        ResolverRuleId='string'
    )
    
    
    :type VPCId: string
    :param VPCId: [REQUIRED]\nThe ID of the VPC that you want to disassociate the resolver rule from.\n

    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]\nThe ID of the resolver rule that you want to disassociate from the specified VPC.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResolverRuleAssociation': {
        'Id': 'string',
        'ResolverRuleId': 'string',
        'Name': 'string',
        'VPCId': 'string',
        'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
        'StatusMessage': 'string'
    }
}


Response Structure

(dict) --

ResolverRuleAssociation (dict) --
Information about the DisassociateResolverRule request, including the status of the request.

Id (string) --
The ID of the association between a resolver rule and a VPC. Resolver assigns this value when you submit an  AssociateResolverRule request.

ResolverRuleId (string) --
The ID of the resolver rule that you associated with the VPC that is specified by VPCId .

Name (string) --
The name of an association between a resolver rule and a VPC.

VPCId (string) --
The ID of the VPC that you associated the resolver rule with.

Status (string) --
A code that specifies the current status of the association between a resolver rule and a VPC.

StatusMessage (string) --
A detailed description of the status of the association between a resolver rule and a VPC.









Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverRuleAssociation': {
            'Id': 'string',
            'ResolverRuleId': 'string',
            'Name': 'string',
            'VPCId': 'string',
            'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
            'StatusMessage': 'string'
        }
    }
    
    
    :returns: 
    Route53Resolver.Client.exceptions.ResourceNotFoundException
    Route53Resolver.Client.exceptions.InvalidParameterException
    Route53Resolver.Client.exceptions.InternalServiceErrorException
    Route53Resolver.Client.exceptions.ThrottlingException
    
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

def get_resolver_endpoint(ResolverEndpointId=None):
    """
    Gets information about a specified resolver endpoint, such as whether it\'s an inbound or an outbound resolver endpoint, and the current status of the endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resolver_endpoint(
        ResolverEndpointId='string'
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]\nThe ID of the resolver endpoint that you want to get information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ResolverEndpoint': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'Name': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'Direction': 'INBOUND'|'OUTBOUND',
        'IpAddressCount': 123,
        'HostVPCId': 'string',
        'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
        'StatusMessage': 'string',
        'CreationTime': 'string',
        'ModificationTime': 'string'
    }
}


Response Structure

(dict) --
ResolverEndpoint (dict) --Information about the resolver endpoint that you specified in a GetResolverEndpoint request.

Id (string) --The ID of the resolver endpoint.

CreatorRequestId (string) --A unique string that identifies the request that created the resolver endpoint. The CreatorRequestId allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --The ARN (Amazon Resource Name) for the resolver endpoint.

Name (string) --The name that you assigned to the resolver endpoint when you submitted a  CreateResolverEndpoint request.

SecurityGroupIds (list) --The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound resolver rules.

(string) --


Direction (string) --Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

INBOUND : allows DNS queries to your VPC from your network or another VPC
OUTBOUND : allows DNS queries from your VPC to your network or another VPC


IpAddressCount (integer) --The number of IP addresses that the resolver endpoint can use for DNS queries.

HostVPCId (string) --The ID of the VPC that you want to create the resolver endpoint in.

Status (string) --A code that specifies the current status of the resolver endpoint.

StatusMessage (string) --A detailed description of the status of the resolver endpoint.

CreationTime (string) --The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime (string) --The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).








Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    INBOUND : allows DNS queries to your VPC from your network or another VPC
    OUTBOUND : allows DNS queries from your VPC to your network or another VPC
    
    """
    pass

def get_resolver_rule(ResolverRuleId=None):
    """
    Gets information about a specified resolver rule, such as the domain name that the rule forwards DNS queries for and the ID of the outbound resolver endpoint that the rule is associated with.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resolver_rule(
        ResolverRuleId='string'
    )
    
    
    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]\nThe ID of the resolver rule that you want to get information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ResolverRule': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'DomainName': 'string',
        'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
        'StatusMessage': 'string',
        'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
        'Name': 'string',
        'TargetIps': [
            {
                'Ip': 'string',
                'Port': 123
            },
        ],
        'ResolverEndpointId': 'string',
        'OwnerId': 'string',
        'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
    }
}


Response Structure

(dict) --
ResolverRule (dict) --Information about the resolver rule that you specified in a GetResolverRule request.

Id (string) --The ID that Resolver assigned to the resolver rule when you created it.

CreatorRequestId (string) --A unique string that you specified when you created the resolver rule. CreatorRequestId identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --The ARN (Amazon Resource Name) for the resolver rule specified by Id .

DomainName (string) --DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps . If a query matches multiple resolver rules (example.com and www.example.com), the query is routed using the resolver rule that contains the most specific domain name (www.example.com).

Status (string) --A code that specifies the current status of the resolver rule.

StatusMessage (string) --A detailed description of the status of a resolver rule.

RuleType (string) --This value is always FORWARD . Other resolver rule types aren\'t supported.

Name (string) --The name for the resolver rule, which you specified when you created the resolver rule.

TargetIps (list) --An array that contains the IP addresses and ports that you want to forward

(dict) --In a  CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.

Ip (string) --One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.

Port (integer) --The port at Ip that you want to forward DNS queries to.





ResolverEndpointId (string) --The ID of the endpoint that the rule is associated with.

OwnerId (string) --When a rule is shared with another AWS account, the account ID of the account that the rule is shared with.

ShareStatus (string) --Whether the rules is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.








Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverRule': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'DomainName': 'string',
            'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
            'StatusMessage': 'string',
            'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string',
            'OwnerId': 'string',
            'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
        }
    }
    
    
    """
    pass

def get_resolver_rule_association(ResolverRuleAssociationId=None):
    """
    Gets information about an association between a specified resolver rule and a VPC. You associate a resolver rule and a VPC using  AssociateResolverRule .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resolver_rule_association(
        ResolverRuleAssociationId='string'
    )
    
    
    :type ResolverRuleAssociationId: string
    :param ResolverRuleAssociationId: [REQUIRED]\nThe ID of the resolver rule association that you want to get information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ResolverRuleAssociation': {
        'Id': 'string',
        'ResolverRuleId': 'string',
        'Name': 'string',
        'VPCId': 'string',
        'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
        'StatusMessage': 'string'
    }
}


Response Structure

(dict) --
ResolverRuleAssociation (dict) --Information about the resolver rule association that you specified in a GetResolverRuleAssociation request.

Id (string) --The ID of the association between a resolver rule and a VPC. Resolver assigns this value when you submit an  AssociateResolverRule request.

ResolverRuleId (string) --The ID of the resolver rule that you associated with the VPC that is specified by VPCId .

Name (string) --The name of an association between a resolver rule and a VPC.

VPCId (string) --The ID of the VPC that you associated the resolver rule with.

Status (string) --A code that specifies the current status of the association between a resolver rule and a VPC.

StatusMessage (string) --A detailed description of the status of the association between a resolver rule and a VPC.








Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverRuleAssociation': {
            'Id': 'string',
            'ResolverRuleId': 'string',
            'Name': 'string',
            'VPCId': 'string',
            'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
            'StatusMessage': 'string'
        }
    }
    
    
    """
    pass

def get_resolver_rule_policy(Arn=None):
    """
    Gets information about a resolver rule policy. A resolver rule policy specifies the Resolver operations and resources that you want to allow another AWS account to be able to use.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resolver_rule_policy(
        Arn='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe ID of the resolver rule policy that you want to get information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ResolverRulePolicy': 'string'
}


Response Structure

(dict) --
ResolverRulePolicy (string) --Information about the resolver rule policy that you specified in a GetResolverRulePolicy request.






Exceptions

Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.UnknownResourceException
Route53Resolver.Client.exceptions.InternalServiceErrorException


    :return: {
        'ResolverRulePolicy': 'string'
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

def list_resolver_endpoint_ip_addresses(ResolverEndpointId=None, MaxResults=None, NextToken=None):
    """
    Gets the IP addresses for a specified resolver endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resolver_endpoint_ip_addresses(
        ResolverEndpointId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]\nThe ID of the resolver endpoint that you want to get IP addresses for.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of IP addresses that you want to return in the response to a ListResolverEndpointIpAddresses request. If you don\'t specify a value for MaxResults , Resolver returns up to 100 IP addresses.

    :type NextToken: string
    :param NextToken: For the first ListResolverEndpointIpAddresses request, omit this value.\nIf the specified resolver endpoint has more than MaxResults IP addresses, you can submit another ListResolverEndpointIpAddresses request to get the next group of IP addresses. In the next request, specify the value of NextToken from the previous response.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'MaxResults': 123,
    'IpAddresses': [
        {
            'IpId': 'string',
            'SubnetId': 'string',
            'Ip': 'string',
            'Status': 'CREATING'|'FAILED_CREATION'|'ATTACHING'|'ATTACHED'|'REMAP_DETACHING'|'REMAP_ATTACHING'|'DETACHING'|'FAILED_RESOURCE_GONE'|'DELETING'|'DELETE_FAILED_FAS_EXPIRED',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If the specified endpoint has more than MaxResults IP addresses, you can submit another ListResolverEndpointIpAddresses request to get the next group of IP addresses. In the next request, specify the value of NextToken from the previous response.

MaxResults (integer) --
The value that you specified for MaxResults in the request.

IpAddresses (list) --
The IP addresses that DNS queries pass through on their way to your network (outbound endpoint) or on the way to Resolver (inbound endpoint).

(dict) --
In the response to a  GetResolverEndpoint request, information about the IP addresses that the resolver endpoint uses for DNS queries.

IpId (string) --
The ID of one IP address.

SubnetId (string) --
The ID of one subnet.

Ip (string) --
One IP address that the resolver endpoint uses for DNS queries.

Status (string) --
A status code that gives the current status of the request.

StatusMessage (string) --
A message that provides additional information about the status of the request.

CreationTime (string) --
The date and time that the IP address was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime (string) --
The date and time that the IP address was last modified, in Unix time format and Coordinated Universal Time (UTC).











Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.InvalidNextTokenException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'NextToken': 'string',
        'MaxResults': 123,
        'IpAddresses': [
            {
                'IpId': 'string',
                'SubnetId': 'string',
                'Ip': 'string',
                'Status': 'CREATING'|'FAILED_CREATION'|'ATTACHING'|'ATTACHED'|'REMAP_DETACHING'|'REMAP_ATTACHING'|'DETACHING'|'FAILED_RESOURCE_GONE'|'DELETING'|'DELETE_FAILED_FAS_EXPIRED',
                'StatusMessage': 'string',
                'CreationTime': 'string',
                'ModificationTime': 'string'
            },
        ]
    }
    
    
    :returns: 
    Route53Resolver.Client.exceptions.ResourceNotFoundException
    Route53Resolver.Client.exceptions.InvalidParameterException
    Route53Resolver.Client.exceptions.InternalServiceErrorException
    Route53Resolver.Client.exceptions.InvalidNextTokenException
    Route53Resolver.Client.exceptions.ThrottlingException
    
    """
    pass

def list_resolver_endpoints(MaxResults=None, NextToken=None, Filters=None):
    """
    Lists all the resolver endpoints that were created using the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resolver_endpoints(
        MaxResults=123,
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
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of resolver endpoints that you want to return in the response to a ListResolverEndpoints request. If you don\'t specify a value for MaxResults , Resolver returns up to 100 resolver endpoints.

    :type NextToken: string
    :param NextToken: For the first ListResolverEndpoints request, omit this value.\nIf you have more than MaxResults resolver endpoints, you can submit another ListResolverEndpoints request to get the next group of resolver endpoints. In the next request, specify the value of NextToken from the previous response.\n

    :type Filters: list
    :param Filters: An optional specification to return a subset of resolver endpoints, such as all inbound resolver endpoints.\n\nNote\nIf you submit a second or subsequent ListResolverEndpoints request and specify the NextToken parameter, you must use the same values for Filters , if any, as in the previous request.\n\n\n(dict) --For List operations, an optional specification to return a subset of objects, such as resolver endpoints or resolver rules.\n\nName (string) --When you\'re using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the name of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify Direction for the value of Name .\n\nValues (list) --When you\'re using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the value of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify INBOUND for the value of Values .\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'MaxResults': 123,
    'ResolverEndpoints': [
        {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If more than MaxResults IP addresses match the specified criteria, you can submit another ListResolverEndpoint request to get the next group of results. In the next request, specify the value of NextToken from the previous response.

MaxResults (integer) --
The value that you specified for MaxResults in the request.

ResolverEndpoints (list) --
The resolver endpoints that were created by using the current AWS account, and that match the specified filters, if any.

(dict) --
In the response to a  CreateResolverEndpoint ,  DeleteResolverEndpoint ,  GetResolverEndpoint ,  ListResolverEndpoints , or  UpdateResolverEndpoint request, a complex type that contains settings for an existing inbound or outbound resolver endpoint.

Id (string) --
The ID of the resolver endpoint.

CreatorRequestId (string) --
A unique string that identifies the request that created the resolver endpoint. The CreatorRequestId allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --
The ARN (Amazon Resource Name) for the resolver endpoint.

Name (string) --
The name that you assigned to the resolver endpoint when you submitted a  CreateResolverEndpoint request.

SecurityGroupIds (list) --
The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound resolver rules.

(string) --


Direction (string) --
Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

INBOUND : allows DNS queries to your VPC from your network or another VPC
OUTBOUND : allows DNS queries from your VPC to your network or another VPC


IpAddressCount (integer) --
The number of IP addresses that the resolver endpoint can use for DNS queries.

HostVPCId (string) --
The ID of the VPC that you want to create the resolver endpoint in.

Status (string) --
A code that specifies the current status of the resolver endpoint.

StatusMessage (string) --
A detailed description of the status of the resolver endpoint.

CreationTime (string) --
The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime (string) --
The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).











Exceptions

Route53Resolver.Client.exceptions.InvalidNextTokenException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'NextToken': 'string',
        'MaxResults': 123,
        'ResolverEndpoints': [
            {
                'Id': 'string',
                'CreatorRequestId': 'string',
                'Arn': 'string',
                'Name': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'Direction': 'INBOUND'|'OUTBOUND',
                'IpAddressCount': 123,
                'HostVPCId': 'string',
                'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
                'StatusMessage': 'string',
                'CreationTime': 'string',
                'ModificationTime': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_resolver_rule_associations(MaxResults=None, NextToken=None, Filters=None):
    """
    Lists the associations that were created between resolver rules and VPCs using the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resolver_rule_associations(
        MaxResults=123,
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
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of rule associations that you want to return in the response to a ListResolverRuleAssociations request. If you don\'t specify a value for MaxResults , Resolver returns up to 100 rule associations.

    :type NextToken: string
    :param NextToken: For the first ListResolverRuleAssociation request, omit this value.\nIf you have more than MaxResults rule associations, you can submit another ListResolverRuleAssociation request to get the next group of rule associations. In the next request, specify the value of NextToken from the previous response.\n

    :type Filters: list
    :param Filters: An optional specification to return a subset of resolver rules, such as resolver rules that are associated with the same VPC ID.\n\nNote\nIf you submit a second or subsequent ListResolverRuleAssociations request and specify the NextToken parameter, you must use the same values for Filters , if any, as in the previous request.\n\n\n(dict) --For List operations, an optional specification to return a subset of objects, such as resolver endpoints or resolver rules.\n\nName (string) --When you\'re using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the name of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify Direction for the value of Name .\n\nValues (list) --When you\'re using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the value of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify INBOUND for the value of Values .\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'MaxResults': 123,
    'ResolverRuleAssociations': [
        {
            'Id': 'string',
            'ResolverRuleId': 'string',
            'Name': 'string',
            'VPCId': 'string',
            'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
            'StatusMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If more than MaxResults rule associations match the specified criteria, you can submit another ListResolverRuleAssociation request to get the next group of results. In the next request, specify the value of NextToken from the previous response.

MaxResults (integer) --
The value that you specified for MaxResults in the request.

ResolverRuleAssociations (list) --
The associations that were created between resolver rules and VPCs using the current AWS account, and that match the specified filters, if any.

(dict) --
In the response to an  AssociateResolverRule ,  DisassociateResolverRule , or  ListResolverRuleAssociations request, information about an association between a resolver rule and a VPC.

Id (string) --
The ID of the association between a resolver rule and a VPC. Resolver assigns this value when you submit an  AssociateResolverRule request.

ResolverRuleId (string) --
The ID of the resolver rule that you associated with the VPC that is specified by VPCId .

Name (string) --
The name of an association between a resolver rule and a VPC.

VPCId (string) --
The ID of the VPC that you associated the resolver rule with.

Status (string) --
A code that specifies the current status of the association between a resolver rule and a VPC.

StatusMessage (string) --
A detailed description of the status of the association between a resolver rule and a VPC.











Exceptions

Route53Resolver.Client.exceptions.InvalidNextTokenException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'NextToken': 'string',
        'MaxResults': 123,
        'ResolverRuleAssociations': [
            {
                'Id': 'string',
                'ResolverRuleId': 'string',
                'Name': 'string',
                'VPCId': 'string',
                'Status': 'CREATING'|'COMPLETE'|'DELETING'|'FAILED'|'OVERRIDDEN',
                'StatusMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Route53Resolver.Client.exceptions.InvalidNextTokenException
    Route53Resolver.Client.exceptions.InvalidRequestException
    Route53Resolver.Client.exceptions.InvalidParameterException
    Route53Resolver.Client.exceptions.InternalServiceErrorException
    Route53Resolver.Client.exceptions.ThrottlingException
    
    """
    pass

def list_resolver_rules(MaxResults=None, NextToken=None, Filters=None):
    """
    Lists the resolver rules that were created using the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resolver_rules(
        MaxResults=123,
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
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of resolver rules that you want to return in the response to a ListResolverRules request. If you don\'t specify a value for MaxResults , Resolver returns up to 100 resolver rules.

    :type NextToken: string
    :param NextToken: For the first ListResolverRules request, omit this value.\nIf you have more than MaxResults resolver rules, you can submit another ListResolverRules request to get the next group of resolver rules. In the next request, specify the value of NextToken from the previous response.\n

    :type Filters: list
    :param Filters: An optional specification to return a subset of resolver rules, such as all resolver rules that are associated with the same resolver endpoint.\n\nNote\nIf you submit a second or subsequent ListResolverRules request and specify the NextToken parameter, you must use the same values for Filters , if any, as in the previous request.\n\n\n(dict) --For List operations, an optional specification to return a subset of objects, such as resolver endpoints or resolver rules.\n\nName (string) --When you\'re using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the name of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify Direction for the value of Name .\n\nValues (list) --When you\'re using a List operation and you want the operation to return a subset of objects, such as resolver endpoints or resolver rules, the value of the parameter that you want to use to filter objects. For example, to list only inbound resolver endpoints, specify INBOUND for the value of Values .\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'MaxResults': 123,
    'ResolverRules': [
        {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'DomainName': 'string',
            'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
            'StatusMessage': 'string',
            'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string',
            'OwnerId': 'string',
            'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If more than MaxResults resolver rules match the specified criteria, you can submit another ListResolverRules request to get the next group of results. In the next request, specify the value of NextToken from the previous response.

MaxResults (integer) --
The value that you specified for MaxResults in the request.

ResolverRules (list) --
The resolver rules that were created using the current AWS account and that match the specified filters, if any.

(dict) --
For queries that originate in your VPC, detailed information about a resolver rule, which specifies how to route DNS queries out of the VPC. The ResolverRule parameter appears in the response to a  CreateResolverRule ,  DeleteResolverRule ,  GetResolverRule ,  ListResolverRules , or  UpdateResolverRule request.

Id (string) --
The ID that Resolver assigned to the resolver rule when you created it.

CreatorRequestId (string) --
A unique string that you specified when you created the resolver rule. CreatorRequestId identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --
The ARN (Amazon Resource Name) for the resolver rule specified by Id .

DomainName (string) --
DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps . If a query matches multiple resolver rules (example.com and www.example.com), the query is routed using the resolver rule that contains the most specific domain name (www.example.com).

Status (string) --
A code that specifies the current status of the resolver rule.

StatusMessage (string) --
A detailed description of the status of a resolver rule.

RuleType (string) --
This value is always FORWARD . Other resolver rule types aren\'t supported.

Name (string) --
The name for the resolver rule, which you specified when you created the resolver rule.

TargetIps (list) --
An array that contains the IP addresses and ports that you want to forward

(dict) --
In a  CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.

Ip (string) --
One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.

Port (integer) --
The port at Ip that you want to forward DNS queries to.





ResolverEndpointId (string) --
The ID of the endpoint that the rule is associated with.

OwnerId (string) --
When a rule is shared with another AWS account, the account ID of the account that the rule is shared with.

ShareStatus (string) --
Whether the rules is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.











Exceptions

Route53Resolver.Client.exceptions.InvalidNextTokenException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'NextToken': 'string',
        'MaxResults': 123,
        'ResolverRules': [
            {
                'Id': 'string',
                'CreatorRequestId': 'string',
                'Arn': 'string',
                'DomainName': 'string',
                'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
                'StatusMessage': 'string',
                'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
                'Name': 'string',
                'TargetIps': [
                    {
                        'Ip': 'string',
                        'Port': 123
                    },
                ],
                'ResolverEndpointId': 'string',
                'OwnerId': 'string',
                'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
            },
        ]
    }
    
    
    :returns: 
    Route53Resolver.Client.exceptions.InvalidNextTokenException
    Route53Resolver.Client.exceptions.InvalidRequestException
    Route53Resolver.Client.exceptions.InvalidParameterException
    Route53Resolver.Client.exceptions.InternalServiceErrorException
    Route53Resolver.Client.exceptions.ThrottlingException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None, MaxResults=None, NextToken=None):
    """
    Lists the tags that you associated with the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the resource that you want to list tags for.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of tags that you want to return in the response to a ListTagsForResource request. If you don\'t specify a value for MaxResults , Resolver returns up to 100 tags.

    :type NextToken: string
    :param NextToken: For the first ListTagsForResource request, omit this value.\nIf you have more than MaxResults tags, you can submit another ListTagsForResource request to get the next group of tags for the resource. In the next request, specify the value of NextToken from the previous response.\n

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
The tags that are associated with the resource that you specified in the ListTagsForResource request.

(dict) --
One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .

Key (string) --
The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .

Value (string) --
The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that you\'re creating the resource for.





NextToken (string) --
If more than MaxResults tags match the specified criteria, you can submit another ListTagsForResource request to get the next group of results. In the next request, specify the value of NextToken from the previous response.







Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InvalidNextTokenException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


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
    Route53Resolver.Client.exceptions.ResourceNotFoundException
    Route53Resolver.Client.exceptions.InvalidParameterException
    Route53Resolver.Client.exceptions.InvalidNextTokenException
    Route53Resolver.Client.exceptions.InvalidRequestException
    Route53Resolver.Client.exceptions.InternalServiceErrorException
    Route53Resolver.Client.exceptions.ThrottlingException
    
    """
    pass

def put_resolver_rule_policy(Arn=None, ResolverRulePolicy=None):
    """
    Specifies the Resolver operations and resources that you want to allow another AWS account to be able to use.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_resolver_rule_policy(
        Arn='string',
        ResolverRulePolicy='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the account that you want to grant permissions to.\n

    :type ResolverRulePolicy: string
    :param ResolverRulePolicy: [REQUIRED]\nAn AWS Identity and Access Management policy statement that lists the permissions that you want to grant to another AWS account.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ReturnValue': True|False
}


Response Structure

(dict) --
The response to a PutResolverRulePolicy request.

ReturnValue (boolean) --
Whether the PutResolverRulePolicy request was successful.







Exceptions

Route53Resolver.Client.exceptions.InvalidPolicyDocument
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.UnknownResourceException
Route53Resolver.Client.exceptions.InternalServiceErrorException


    :return: {
        'ReturnValue': True|False
    }
    
    
    :returns: 
    Route53Resolver.Client.exceptions.InvalidPolicyDocument
    Route53Resolver.Client.exceptions.InvalidParameterException
    Route53Resolver.Client.exceptions.UnknownResourceException
    Route53Resolver.Client.exceptions.InternalServiceErrorException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds one or more tags to a specified resource.
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
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the resource that you want to add tags to. To get the ARN for a resource, use the applicable Get or List command:\n\nGetResolverEndpoint\nGetResolverRule\nGetResolverRuleAssociation\nListResolverEndpoints\nListResolverRuleAssociations\nListResolverRules\n\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags that you want to add to the specified resource.\n\n(dict) --One tag that you want to add to the specified resource. A tag consists of a Key (a name for the tag) and a Value .\n\nKey (string) --The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of Key might be account-id .\n\nValue (string) --The value for the tag. For example, if Key is account-id , then Value might be the ID of the customer account that you\'re creating the resource for.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Route53Resolver.Client.exceptions.LimitExceededException
Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InvalidTagException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes one or more tags from a specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the resource that you want to remove tags from. To get the ARN for a resource, use the applicable Get or List command:\n\nGetResolverEndpoint\nGetResolverRule\nGetResolverRuleAssociation\nListResolverEndpoints\nListResolverRuleAssociations\nListResolverRules\n\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tags that you want to remove to the specified resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_resolver_endpoint(ResolverEndpointId=None, Name=None):
    """
    Updates the name of an inbound or an outbound resolver endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_resolver_endpoint(
        ResolverEndpointId='string',
        Name='string'
    )
    
    
    :type ResolverEndpointId: string
    :param ResolverEndpointId: [REQUIRED]\nThe ID of the resolver endpoint that you want to update.\n

    :type Name: string
    :param Name: The name of the resolver endpoint that you want to update.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResolverEndpoint': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'Name': 'string',
        'SecurityGroupIds': [
            'string',
        ],
        'Direction': 'INBOUND'|'OUTBOUND',
        'IpAddressCount': 123,
        'HostVPCId': 'string',
        'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
        'StatusMessage': 'string',
        'CreationTime': 'string',
        'ModificationTime': 'string'
    }
}


Response Structure

(dict) --

ResolverEndpoint (dict) --
The response to an UpdateResolverEndpoint request.

Id (string) --
The ID of the resolver endpoint.

CreatorRequestId (string) --
A unique string that identifies the request that created the resolver endpoint. The CreatorRequestId allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --
The ARN (Amazon Resource Name) for the resolver endpoint.

Name (string) --
The name that you assigned to the resolver endpoint when you submitted a  CreateResolverEndpoint request.

SecurityGroupIds (list) --
The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound resolver rules.

(string) --


Direction (string) --
Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

INBOUND : allows DNS queries to your VPC from your network or another VPC
OUTBOUND : allows DNS queries from your VPC to your network or another VPC


IpAddressCount (integer) --
The number of IP addresses that the resolver endpoint can use for DNS queries.

HostVPCId (string) --
The ID of the VPC that you want to create the resolver endpoint in.

Status (string) --
A code that specifies the current status of the resolver endpoint.

StatusMessage (string) --
A detailed description of the status of the resolver endpoint.

CreationTime (string) --
The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime (string) --
The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).









Exceptions

Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverEndpoint': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'Name': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'Direction': 'INBOUND'|'OUTBOUND',
            'IpAddressCount': 123,
            'HostVPCId': 'string',
            'Status': 'CREATING'|'OPERATIONAL'|'UPDATING'|'AUTO_RECOVERING'|'ACTION_NEEDED'|'DELETING',
            'StatusMessage': 'string',
            'CreationTime': 'string',
            'ModificationTime': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_resolver_rule(ResolverRuleId=None, Config=None):
    """
    Updates settings for a specified resolver rule. ResolverRuleId is required, and all other parameters are optional. If you don\'t specify a parameter, it retains its current value.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_resolver_rule(
        ResolverRuleId='string',
        Config={
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string'
        }
    )
    
    
    :type ResolverRuleId: string
    :param ResolverRuleId: [REQUIRED]\nThe ID of the resolver rule that you want to update.\n

    :type Config: dict
    :param Config: [REQUIRED]\nThe new settings for the resolver rule.\n\nName (string) --The new name for the resolver rule. The name that you specify appears in the Resolver dashboard in the Route 53 console.\n\nTargetIps (list) --For DNS queries that originate in your VPC, the new IP addresses that you want to route outbound DNS queries to.\n\n(dict) --In a CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.\n\nIp (string) -- [REQUIRED]One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.\n\nPort (integer) --The port at Ip that you want to forward DNS queries to.\n\n\n\n\n\nResolverEndpointId (string) --The ID of the new outbound resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in TargetIps .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResolverRule': {
        'Id': 'string',
        'CreatorRequestId': 'string',
        'Arn': 'string',
        'DomainName': 'string',
        'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
        'StatusMessage': 'string',
        'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
        'Name': 'string',
        'TargetIps': [
            {
                'Ip': 'string',
                'Port': 123
            },
        ],
        'ResolverEndpointId': 'string',
        'OwnerId': 'string',
        'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
    }
}


Response Structure

(dict) --

ResolverRule (dict) --
The response to an UpdateResolverRule request.

Id (string) --
The ID that Resolver assigned to the resolver rule when you created it.

CreatorRequestId (string) --
A unique string that you specified when you created the resolver rule. CreatorRequestId identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

Arn (string) --
The ARN (Amazon Resource Name) for the resolver rule specified by Id .

DomainName (string) --
DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps . If a query matches multiple resolver rules (example.com and www.example.com), the query is routed using the resolver rule that contains the most specific domain name (www.example.com).

Status (string) --
A code that specifies the current status of the resolver rule.

StatusMessage (string) --
A detailed description of the status of a resolver rule.

RuleType (string) --
This value is always FORWARD . Other resolver rule types aren\'t supported.

Name (string) --
The name for the resolver rule, which you specified when you created the resolver rule.

TargetIps (list) --
An array that contains the IP addresses and ports that you want to forward

(dict) --
In a  CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.

Ip (string) --
One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.

Port (integer) --
The port at Ip that you want to forward DNS queries to.





ResolverEndpointId (string) --
The ID of the endpoint that the rule is associated with.

OwnerId (string) --
When a rule is shared with another AWS account, the account ID of the account that the rule is shared with.

ShareStatus (string) --
Whether the rules is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.









Exceptions

Route53Resolver.Client.exceptions.InvalidRequestException
Route53Resolver.Client.exceptions.InvalidParameterException
Route53Resolver.Client.exceptions.ResourceNotFoundException
Route53Resolver.Client.exceptions.ResourceUnavailableException
Route53Resolver.Client.exceptions.LimitExceededException
Route53Resolver.Client.exceptions.InternalServiceErrorException
Route53Resolver.Client.exceptions.ThrottlingException


    :return: {
        'ResolverRule': {
            'Id': 'string',
            'CreatorRequestId': 'string',
            'Arn': 'string',
            'DomainName': 'string',
            'Status': 'COMPLETE'|'DELETING'|'UPDATING'|'FAILED',
            'StatusMessage': 'string',
            'RuleType': 'FORWARD'|'SYSTEM'|'RECURSIVE',
            'Name': 'string',
            'TargetIps': [
                {
                    'Ip': 'string',
                    'Port': 123
                },
            ],
            'ResolverEndpointId': 'string',
            'OwnerId': 'string',
            'ShareStatus': 'NOT_SHARED'|'SHARED_WITH_ME'|'SHARED_BY_ME'
        }
    }
    
    
    :returns: 
    Route53Resolver.Client.exceptions.InvalidRequestException
    Route53Resolver.Client.exceptions.InvalidParameterException
    Route53Resolver.Client.exceptions.ResourceNotFoundException
    Route53Resolver.Client.exceptions.ResourceUnavailableException
    Route53Resolver.Client.exceptions.LimitExceededException
    Route53Resolver.Client.exceptions.InternalServiceErrorException
    Route53Resolver.Client.exceptions.ThrottlingException
    
    """
    pass

