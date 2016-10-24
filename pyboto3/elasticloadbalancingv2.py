'''

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

'''

def add_tags(ResourceArns=None, Tags=None):
    """
    Adds the specified tags to the specified resource. You can tag your Application load balancers and your target groups.
    Each tag consists of a key and an optional value. If a resource already has a tag with the same key, AddTags updates its value.
    To list the current tags for your resources, use  DescribeTags . To remove tags from your resources, use  RemoveTags .
    
    
    :example: response = client.add_tags(
        ResourceArns=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArns: list
    :param ResourceArns: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource.
            (string) --
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags. Each resource can have a maximum of 10 tags.
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            

    :rtype: dict
    :return: {}
    
    
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

def create_listener(LoadBalancerArn=None, Protocol=None, Port=None, SslPolicy=None, Certificates=None, DefaultActions=None):
    """
    Creates a listener for the specified Application load balancer.
    To update a listener, use  ModifyListener . When you are finished with a listener, you can delete it using  DeleteListener . If you are finished with both the listener and the load balancer, you can delete them both using  DeleteLoadBalancer .
    For more information, see Listeners for Your Application Load Balancers in the Application Load Balancers Guide .
    
    
    :example: response = client.create_listener(
        LoadBalancerArn='string',
        Protocol='HTTP'|'HTTPS',
        Port=123,
        SslPolicy='string',
        Certificates=[
            {
                'CertificateArn': 'string'
            },
        ],
        DefaultActions=[
            {
                'Type': 'forward',
                'TargetGroupArn': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            

    :type Protocol: string
    :param Protocol: [REQUIRED]
            The protocol for connections from clients to the load balancer.
            

    :type Port: integer
    :param Port: [REQUIRED]
            The port on which the load balancer is listening.
            

    :type SslPolicy: string
    :param SslPolicy: The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.

    :type Certificates: list
    :param Certificates: The SSL server certificate. You must provide exactly one certificate if the protocol is HTTPS.
            (dict) --Information about an SSL server certificate deployed on a load balancer.
            CertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.
            
            

    :type DefaultActions: list
    :param DefaultActions: [REQUIRED]
            The default actions for the listener.
            (dict) --Information about an action.
            Type (string) -- [REQUIRED]The type of action.
            TargetGroupArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target group.
            
            

    :rtype: dict
    :return: {
        'Listeners': [
            {
                'ListenerArn': 'string',
                'LoadBalancerArn': 'string',
                'Port': 123,
                'Protocol': 'HTTP'|'HTTPS',
                'Certificates': [
                    {
                        'CertificateArn': 'string'
                    },
                ],
                'SslPolicy': 'string',
                'DefaultActions': [
                    {
                        'Type': 'forward',
                        'TargetGroupArn': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def create_load_balancer(Name=None, Subnets=None, SecurityGroups=None, Scheme=None, Tags=None):
    """
    Creates an Application load balancer.
    To create listeners for your load balancer, use  CreateListener . You can add security groups, subnets, and tags when you create your load balancer, or you can add them later using  SetSecurityGroups ,  SetSubnets , and  AddTags .
    To describe your current load balancers, see  DescribeLoadBalancers . When you are finished with a load balancer, you can delete it using  DeleteLoadBalancer .
    You can create up to 20 load balancers per region per account. You can request an increase for the number of load balancers for your account. For more information, see Limits for Your Application Load Balancer in the Application Load Balancers Guide .
    
    
    :example: response = client.create_load_balancer(
        Name='string',
        Subnets=[
            'string',
        ],
        SecurityGroups=[
            'string',
        ],
        Scheme='internet-facing'|'internal',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the load balancer.
            This name must be unique within your AWS account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
            

    :type Subnets: list
    :param Subnets: [REQUIRED]
            The IDs of the subnets to attach to the load balancer. You can specify only one subnet per Availability Zone. You must specify subnets from at least two Availability Zones.
            (string) --
            

    :type SecurityGroups: list
    :param SecurityGroups: The IDs of the security groups to assign to the load balancer.
            (string) --
            

    :type Scheme: string
    :param Scheme: The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the Internet.
            The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.
            The default is an Internet-facing load balancer.
            

    :type Tags: list
    :param Tags: One or more tags to assign to the load balancer.
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            

    :rtype: dict
    :return: {
        'LoadBalancers': [
            {
                'LoadBalancerArn': 'string',
                'DNSName': 'string',
                'CanonicalHostedZoneId': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LoadBalancerName': 'string',
                'Scheme': 'internet-facing'|'internal',
                'VpcId': 'string',
                'State': {
                    'Code': 'active'|'provisioning'|'failed',
                    'Reason': 'string'
                },
                'Type': 'application',
                'AvailabilityZones': [
                    {
                        'ZoneName': 'string',
                        'SubnetId': 'string'
                    },
                ],
                'SecurityGroups': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_rule(ListenerArn=None, Conditions=None, Priority=None, Actions=None):
    """
    Creates a rule for the specified listener.
    A rule consists conditions and actions. Rules are evaluated in priority order, from the lowest value to the highest value. When the conditions for a rule are met, the specified actions are taken. If no rule's conditions are met, the default actions for the listener are taken.
    To view your current rules, use  DescribeRules . To update a rule, use  ModifyRule . To set the priorities of your rules, use  SetRulePriorities . To delete a rule, use  DeleteRule .
    
    
    :example: response = client.create_rule(
        ListenerArn='string',
        Conditions=[
            {
                'Field': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        Priority=123,
        Actions=[
            {
                'Type': 'forward',
                'TargetGroupArn': 'string'
            },
        ]
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the listener.
            

    :type Conditions: list
    :param Conditions: [REQUIRED]
            The conditions.
            (dict) --Information about a condition for a rule.
            Field (string) --The name of the field. The possible value is path-pattern .
            Values (list) --The values for the field.
            A path pattern is case sensitive, can be up to 255 characters in length, and can contain any of the following characters:
            A-Z, a-z, 0-9
            _ - . $ / ~ ' ' @ : +
            amp; (using amp;amp;)
            (matches 0 or more characters)
            ? (matches exactly 1 character)
            (string) --
            
            

    :type Priority: integer
    :param Priority: [REQUIRED]
            The priority for the rule. A listener can't have multiple rules with the same priority.
            

    :type Actions: list
    :param Actions: [REQUIRED]
            The actions for the rule.
            (dict) --Information about an action.
            Type (string) -- [REQUIRED]The type of action.
            TargetGroupArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target group.
            
            

    :rtype: dict
    :return: {
        'Rules': [
            {
                'RuleArn': 'string',
                'Priority': 'string',
                'Conditions': [
                    {
                        'Field': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'Actions': [
                    {
                        'Type': 'forward',
                        'TargetGroupArn': 'string'
                    },
                ],
                'IsDefault': True|False
            },
        ]
    }
    
    
    :returns: 
    A-Z, a-z, 0-9
    _ - . $ / ~ " ' @ : +
    amp; (using amp;amp;)
    
    (matches 0 or more characters)
    
    
    ? (matches exactly 1 character)
    
    """
    pass

def create_target_group(Name=None, Protocol=None, Port=None, VpcId=None, HealthCheckProtocol=None, HealthCheckPort=None, HealthCheckPath=None, HealthCheckIntervalSeconds=None, HealthCheckTimeoutSeconds=None, HealthyThresholdCount=None, UnhealthyThresholdCount=None, Matcher=None):
    """
    Creates a target group.
    To register targets with the target group, use  RegisterTargets . To update the health check settings for the target group, use  ModifyTargetGroup . To monitor the health of targets in the target group, use  DescribeTargetHealth .
    To route traffic to the targets in a target group, specify the target group in an action using  CreateListener or  CreateRule .
    To delete a target group, use  DeleteTargetGroup .
    For more information, see Target Groups for Your Application Load Balancers in the Application Load Balancers Guide .
    
    
    :example: response = client.create_target_group(
        Name='string',
        Protocol='HTTP'|'HTTPS',
        Port=123,
        VpcId='string',
        HealthCheckProtocol='HTTP'|'HTTPS',
        HealthCheckPort='string',
        HealthCheckPath='string',
        HealthCheckIntervalSeconds=123,
        HealthCheckTimeoutSeconds=123,
        HealthyThresholdCount=123,
        UnhealthyThresholdCount=123,
        Matcher={
            'HttpCode': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the target group.
            

    :type Protocol: string
    :param Protocol: [REQUIRED]
            The protocol to use for routing traffic to the targets.
            

    :type Port: integer
    :param Port: [REQUIRED]
            The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target.
            

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The identifier of the virtual private cloud (VPC).
            

    :type HealthCheckProtocol: string
    :param HealthCheckProtocol: The protocol the load balancer uses when performing health checks on targets. The default is the HTTP protocol.

    :type HealthCheckPort: string
    :param HealthCheckPort: The port the load balancer uses when performing health checks on targets. The default is traffic-port , which indicates the port on which each target receives traffic from the load balancer.

    :type HealthCheckPath: string
    :param HealthCheckPath: The ping path that is the destination on the targets for health checks. The default is /.

    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: The approximate amount of time, in seconds, between health checks of an individual target. The default is 30 seconds.

    :type HealthCheckTimeoutSeconds: integer
    :param HealthCheckTimeoutSeconds: The amount of time, in seconds, during which no response from a target means a failed health check. The default is 5 seconds.

    :type HealthyThresholdCount: integer
    :param HealthyThresholdCount: The number of consecutive health checks successes required before considering an unhealthy target healthy. The default is 5.

    :type UnhealthyThresholdCount: integer
    :param UnhealthyThresholdCount: The number of consecutive health check failures required before considering a target unhealthy. The default is 2.

    :type Matcher: dict
    :param Matcher: The HTTP codes to use when checking for a successful response from a target. The default is 200.
            HttpCode (string) -- [REQUIRED]The HTTP codes. The default value is 200. You can specify multiple values (for example, '200,202') or a range of values (for example, '200-299').
            

    :rtype: dict
    :return: {
        'TargetGroups': [
            {
                'TargetGroupArn': 'string',
                'TargetGroupName': 'string',
                'Protocol': 'HTTP'|'HTTPS',
                'Port': 123,
                'VpcId': 'string',
                'HealthCheckProtocol': 'HTTP'|'HTTPS',
                'HealthCheckPort': 'string',
                'HealthCheckIntervalSeconds': 123,
                'HealthCheckTimeoutSeconds': 123,
                'HealthyThresholdCount': 123,
                'UnhealthyThresholdCount': 123,
                'HealthCheckPath': 'string',
                'Matcher': {
                    'HttpCode': 'string'
                },
                'LoadBalancerArns': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_listener(ListenerArn=None):
    """
    Deletes the specified listener.
    Alternatively, your listener is deleted when you delete the load balancer it is attached to using  DeleteLoadBalancer .
    
    
    :example: response = client.delete_listener(
        ListenerArn='string'
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the listener.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_load_balancer(LoadBalancerArn=None):
    """
    Deletes the specified load balancer and its attached listeners.
    You can't delete a load balancer if deletion protection is enabled. If the load balancer does not exist or has already been deleted, the call succeeds.
    Deleting a load balancer does not affect its registered targets. For example, your EC2 instances continue to run and are still registered to their target groups. If you no longer need these EC2 instances, you can stop or terminate them.
    
    
    :example: response = client.delete_load_balancer(
        LoadBalancerArn='string'
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_rule(RuleArn=None):
    """
    Deletes the specified rule.
    
    
    :example: response = client.delete_rule(
        RuleArn='string'
    )
    
    
    :type RuleArn: string
    :param RuleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the rule.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_target_group(TargetGroupArn=None):
    """
    Deletes the specified target group.
    You can delete a target group if it is not referenced by any actions. Deleting a target group also deletes any associated health checks.
    
    
    :example: response = client.delete_target_group(
        TargetGroupArn='string'
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def deregister_targets(TargetGroupArn=None, Targets=None):
    """
    Deregisters the specified targets from the specified target group. After the targets are deregistered, they no longer receive traffic from the load balancer.
    
    
    :example: response = client.deregister_targets(
        TargetGroupArn='string',
        Targets=[
            {
                'Id': 'string',
                'Port': 123
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            

    :type Targets: list
    :param Targets: [REQUIRED]
            The targets.
            (dict) --Information about a target.
            Id (string) -- [REQUIRED]The ID of the target.
            Port (integer) --The port on which the target is listening.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_listeners(LoadBalancerArn=None, ListenerArns=None, Marker=None, PageSize=None):
    """
    Describes the specified listeners or the listeners for the specified load balancer. You must specify either a load balancer or one or more listeners.
    
    
    :example: response = client.describe_listeners(
        LoadBalancerArn='string',
        ListenerArns=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: The Amazon Resource Name (ARN) of the load balancer.

    :type ListenerArns: list
    :param ListenerArns: The Amazon Resource Names (ARN) of the listeners.
            (string) --
            

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict
    :return: {
        'Listeners': [
            {
                'ListenerArn': 'string',
                'LoadBalancerArn': 'string',
                'Port': 123,
                'Protocol': 'HTTP'|'HTTPS',
                'Certificates': [
                    {
                        'CertificateArn': 'string'
                    },
                ],
                'SslPolicy': 'string',
                'DefaultActions': [
                    {
                        'Type': 'forward',
                        'TargetGroupArn': 'string'
                    },
                ]
            },
        ],
        'NextMarker': 'string'
    }
    
    
    """
    pass

def describe_load_balancer_attributes(LoadBalancerArn=None):
    """
    Describes the attributes for the specified load balancer.
    
    
    :example: response = client.describe_load_balancer_attributes(
        LoadBalancerArn='string'
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            

    :rtype: dict
    :return: {
        'Attributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_load_balancers(LoadBalancerArns=None, Names=None, Marker=None, PageSize=None):
    """
    Describes the specified Application load balancers or all of your Application load balancers.
    To describe the listeners for a load balancer, use  DescribeListeners . To describe the attributes for a load balancer, use  DescribeLoadBalancerAttributes .
    
    
    :example: response = client.describe_load_balancers(
        LoadBalancerArns=[
            'string',
        ],
        Names=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type LoadBalancerArns: list
    :param LoadBalancerArns: The Amazon Resource Names (ARN) of the load balancers.
            (string) --
            

    :type Names: list
    :param Names: The names of the load balancers.
            (string) --
            

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict
    :return: {
        'LoadBalancers': [
            {
                'LoadBalancerArn': 'string',
                'DNSName': 'string',
                'CanonicalHostedZoneId': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LoadBalancerName': 'string',
                'Scheme': 'internet-facing'|'internal',
                'VpcId': 'string',
                'State': {
                    'Code': 'active'|'provisioning'|'failed',
                    'Reason': 'string'
                },
                'Type': 'application',
                'AvailabilityZones': [
                    {
                        'ZoneName': 'string',
                        'SubnetId': 'string'
                    },
                ],
                'SecurityGroups': [
                    'string',
                ]
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_rules(ListenerArn=None, RuleArns=None):
    """
    Describes the specified rules or the rules for the specified listener. You must specify either a listener or one or more rules.
    
    
    :example: response = client.describe_rules(
        ListenerArn='string',
        RuleArns=[
            'string',
        ]
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: The Amazon Resource Name (ARN) of the listener.

    :type RuleArns: list
    :param RuleArns: The Amazon Resource Names (ARN) of the rules.
            (string) --
            

    :rtype: dict
    :return: {
        'Rules': [
            {
                'RuleArn': 'string',
                'Priority': 'string',
                'Conditions': [
                    {
                        'Field': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'Actions': [
                    {
                        'Type': 'forward',
                        'TargetGroupArn': 'string'
                    },
                ],
                'IsDefault': True|False
            },
        ]
    }
    
    
    :returns: 
    A-Z, a-z, 0-9
    _ - . $ / ~ " ' @ : +
    amp; (using amp;amp;)
    
    (matches 0 or more characters)
    
    
    ? (matches exactly 1 character)
    
    """
    pass

def describe_ssl_policies(Names=None, Marker=None, PageSize=None):
    """
    Describes the specified policies or all policies used for SSL negotiation.
    Note that the only supported policy at this time is ELBSecurityPolicy-2015-05.
    
    
    :example: response = client.describe_ssl_policies(
        Names=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type Names: list
    :param Names: The names of the policies.
            (string) --
            

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict
    :return: {
        'SslPolicies': [
            {
                'SslProtocols': [
                    'string',
                ],
                'Ciphers': [
                    {
                        'Name': 'string',
                        'Priority': 123
                    },
                ],
                'Name': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_tags(ResourceArns=None):
    """
    Describes the tags for the specified resources.
    
    
    :example: response = client.describe_tags(
        ResourceArns=[
            'string',
        ]
    )
    
    
    :type ResourceArns: list
    :param ResourceArns: [REQUIRED]
            The Amazon Resource Names (ARN) of the resources.
            (string) --
            

    :rtype: dict
    :return: {
        'TagDescriptions': [
            {
                'ResourceArn': 'string',
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

def describe_target_group_attributes(TargetGroupArn=None):
    """
    Describes the attributes for the specified target group.
    
    
    :example: response = client.describe_target_group_attributes(
        TargetGroupArn='string'
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            

    :rtype: dict
    :return: {
        'Attributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_target_groups(LoadBalancerArn=None, TargetGroupArns=None, Names=None, Marker=None, PageSize=None):
    """
    Describes the specified target groups or all of your target groups. By default, all target groups are described. Alternatively, you can specify one of the following to filter the results: the ARN of the load balancer, the names of one or more target groups, or the ARNs of one or more target groups.
    To describe the targets for a target group, use  DescribeTargetHealth . To describe the attributes of a target group, use  DescribeTargetGroupAttributes .
    
    
    :example: response = client.describe_target_groups(
        LoadBalancerArn='string',
        TargetGroupArns=[
            'string',
        ],
        Names=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: The Amazon Resource Name (ARN) of the load balancer.

    :type TargetGroupArns: list
    :param TargetGroupArns: The Amazon Resource Names (ARN) of the target groups.
            (string) --
            

    :type Names: list
    :param Names: The names of the target groups.
            (string) --
            

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict
    :return: {
        'TargetGroups': [
            {
                'TargetGroupArn': 'string',
                'TargetGroupName': 'string',
                'Protocol': 'HTTP'|'HTTPS',
                'Port': 123,
                'VpcId': 'string',
                'HealthCheckProtocol': 'HTTP'|'HTTPS',
                'HealthCheckPort': 'string',
                'HealthCheckIntervalSeconds': 123,
                'HealthCheckTimeoutSeconds': 123,
                'HealthyThresholdCount': 123,
                'UnhealthyThresholdCount': 123,
                'HealthCheckPath': 'string',
                'Matcher': {
                    'HttpCode': 'string'
                },
                'LoadBalancerArns': [
                    'string',
                ]
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_target_health(TargetGroupArn=None, Targets=None):
    """
    Describes the health of the specified targets or all of your targets.
    
    
    :example: response = client.describe_target_health(
        TargetGroupArn='string',
        Targets=[
            {
                'Id': 'string',
                'Port': 123
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            

    :type Targets: list
    :param Targets: The targets.
            (dict) --Information about a target.
            Id (string) -- [REQUIRED]The ID of the target.
            Port (integer) --The port on which the target is listening.
            
            

    :rtype: dict
    :return: {
        'TargetHealthDescriptions': [
            {
                'Target': {
                    'Id': 'string',
                    'Port': 123
                },
                'HealthCheckPort': 'string',
                'TargetHealth': {
                    'State': 'initial'|'healthy'|'unhealthy'|'unused'|'draining',
                    'Reason': 'Elb.RegistrationInProgress'|'Elb.InitialHealthChecking'|'Target.ResponseCodeMismatch'|'Target.Timeout'|'Target.FailedHealthChecks'|'Target.NotRegistered'|'Target.NotInUse'|'Target.DeregistrationInProgress'|'Target.InvalidState'|'Elb.InternalError',
                    'Description': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    Elb.RegistrationInProgress - The target is in the process of being registered with the load balancer.
    Elb.InitialHealthChecking - The load balancer is still sending the target the minimum number of health checks required to determine its health status.
    
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

def modify_listener(ListenerArn=None, Port=None, Protocol=None, SslPolicy=None, Certificates=None, DefaultActions=None):
    """
    Modifies the specified properties of the specified listener.
    Any properties that you do not specify retain their current values. However, changing the protocol from HTTPS to HTTP removes the security policy and SSL certificate properties. If you change the protocol from HTTP to HTTPS, you must add the security policy.
    
    
    :example: response = client.modify_listener(
        ListenerArn='string',
        Port=123,
        Protocol='HTTP'|'HTTPS',
        SslPolicy='string',
        Certificates=[
            {
                'CertificateArn': 'string'
            },
        ],
        DefaultActions=[
            {
                'Type': 'forward',
                'TargetGroupArn': 'string'
            },
        ]
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the listener.
            

    :type Port: integer
    :param Port: The port for connections from clients to the load balancer.

    :type Protocol: string
    :param Protocol: The protocol for connections from clients to the load balancer.

    :type SslPolicy: string
    :param SslPolicy: The security policy that defines which ciphers and protocols are supported.

    :type Certificates: list
    :param Certificates: The SSL server certificate.
            (dict) --Information about an SSL server certificate deployed on a load balancer.
            CertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.
            
            

    :type DefaultActions: list
    :param DefaultActions: The default actions.
            (dict) --Information about an action.
            Type (string) -- [REQUIRED]The type of action.
            TargetGroupArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target group.
            
            

    :rtype: dict
    :return: {
        'Listeners': [
            {
                'ListenerArn': 'string',
                'LoadBalancerArn': 'string',
                'Port': 123,
                'Protocol': 'HTTP'|'HTTPS',
                'Certificates': [
                    {
                        'CertificateArn': 'string'
                    },
                ],
                'SslPolicy': 'string',
                'DefaultActions': [
                    {
                        'Type': 'forward',
                        'TargetGroupArn': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def modify_load_balancer_attributes(LoadBalancerArn=None, Attributes=None):
    """
    Modifies the specified attributes of the specified load balancer.
    If any of the specified attributes can't be modified as requested, the call fails. Any existing attributes that you do not modify retain their current values.
    
    
    :example: response = client.modify_load_balancer_attributes(
        LoadBalancerArn='string',
        Attributes=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            

    :type Attributes: list
    :param Attributes: [REQUIRED]
            The load balancer attributes.
            (dict) --Information about a load balancer attribute.
            Key (string) --The name of the attribute.
            access_logs.s3.enabled - Indicates whether access logs stored in Amazon S3 are enabled.
            access_logs.s3.bucket - The name of the S3 bucket for the access logs. This attribute is required if access logs in Amazon S3 are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket.
            access_logs.s3.prefix - The prefix for the location in the S3 bucket. If you don't specify a prefix, the access logs are stored in the root of the bucket.
            deletion_protection.enabled - Indicates whether deletion protection is enabled.
            idle_timeout.timeout_seconds - The idle timeout value, in seconds. The valid range is 1-3600. The default is 60 seconds.
            Value (string) --The value of the attribute.
            
            

    :rtype: dict
    :return: {
        'Attributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    access_logs.s3.enabled - Indicates whether access logs stored in Amazon S3 are enabled.
    access_logs.s3.bucket - The name of the S3 bucket for the access logs. This attribute is required if access logs in Amazon S3 are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket.
    access_logs.s3.prefix - The prefix for the location in the S3 bucket. If you don't specify a prefix, the access logs are stored in the root of the bucket.
    deletion_protection.enabled - Indicates whether deletion protection is enabled.
    idle_timeout.timeout_seconds - The idle timeout value, in seconds. The valid range is 1-3600. The default is 60 seconds.
    
    """
    pass

def modify_rule(RuleArn=None, Conditions=None, Actions=None):
    """
    Modifies the specified rule.
    Any existing properties that you do not modify retain their current values.
    To modify the default action, use  ModifyListener .
    
    
    :example: response = client.modify_rule(
        RuleArn='string',
        Conditions=[
            {
                'Field': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        Actions=[
            {
                'Type': 'forward',
                'TargetGroupArn': 'string'
            },
        ]
    )
    
    
    :type RuleArn: string
    :param RuleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the rule.
            

    :type Conditions: list
    :param Conditions: The conditions.
            (dict) --Information about a condition for a rule.
            Field (string) --The name of the field. The possible value is path-pattern .
            Values (list) --The values for the field.
            A path pattern is case sensitive, can be up to 255 characters in length, and can contain any of the following characters:
            A-Z, a-z, 0-9
            _ - . $ / ~ ' ' @ : +
            amp; (using amp;amp;)
            (matches 0 or more characters)
            ? (matches exactly 1 character)
            (string) --
            
            

    :type Actions: list
    :param Actions: The actions.
            (dict) --Information about an action.
            Type (string) -- [REQUIRED]The type of action.
            TargetGroupArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target group.
            
            

    :rtype: dict
    :return: {
        'Rules': [
            {
                'RuleArn': 'string',
                'Priority': 'string',
                'Conditions': [
                    {
                        'Field': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'Actions': [
                    {
                        'Type': 'forward',
                        'TargetGroupArn': 'string'
                    },
                ],
                'IsDefault': True|False
            },
        ]
    }
    
    
    :returns: 
    A-Z, a-z, 0-9
    _ - . $ / ~ " ' @ : +
    amp; (using amp;amp;)
    
    (matches 0 or more characters)
    
    
    ? (matches exactly 1 character)
    
    """
    pass

def modify_target_group(TargetGroupArn=None, HealthCheckProtocol=None, HealthCheckPort=None, HealthCheckPath=None, HealthCheckIntervalSeconds=None, HealthCheckTimeoutSeconds=None, HealthyThresholdCount=None, UnhealthyThresholdCount=None, Matcher=None):
    """
    Modifies the health checks used when evaluating the health state of the targets in the specified target group.
    To monitor the health of the targets, use  DescribeTargetHealth .
    
    
    :example: response = client.modify_target_group(
        TargetGroupArn='string',
        HealthCheckProtocol='HTTP'|'HTTPS',
        HealthCheckPort='string',
        HealthCheckPath='string',
        HealthCheckIntervalSeconds=123,
        HealthCheckTimeoutSeconds=123,
        HealthyThresholdCount=123,
        UnhealthyThresholdCount=123,
        Matcher={
            'HttpCode': 'string'
        }
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            

    :type HealthCheckProtocol: string
    :param HealthCheckProtocol: The protocol to use to connect with the target.

    :type HealthCheckPort: string
    :param HealthCheckPort: The port to use to connect with the target.

    :type HealthCheckPath: string
    :param HealthCheckPath: The ping path that is the destination for the health check request.

    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: The approximate amount of time, in seconds, between health checks of an individual target.

    :type HealthCheckTimeoutSeconds: integer
    :param HealthCheckTimeoutSeconds: The amount of time, in seconds, during which no response means a failed health check.

    :type HealthyThresholdCount: integer
    :param HealthyThresholdCount: The number of consecutive health checks successes required before considering an unhealthy target healthy.

    :type UnhealthyThresholdCount: integer
    :param UnhealthyThresholdCount: The number of consecutive health check failures required before considering the target unhealthy.

    :type Matcher: dict
    :param Matcher: The HTTP codes to use when checking for a successful response from a target.
            HttpCode (string) -- [REQUIRED]The HTTP codes. The default value is 200. You can specify multiple values (for example, '200,202') or a range of values (for example, '200-299').
            

    :rtype: dict
    :return: {
        'TargetGroups': [
            {
                'TargetGroupArn': 'string',
                'TargetGroupName': 'string',
                'Protocol': 'HTTP'|'HTTPS',
                'Port': 123,
                'VpcId': 'string',
                'HealthCheckProtocol': 'HTTP'|'HTTPS',
                'HealthCheckPort': 'string',
                'HealthCheckIntervalSeconds': 123,
                'HealthCheckTimeoutSeconds': 123,
                'HealthyThresholdCount': 123,
                'UnhealthyThresholdCount': 123,
                'HealthCheckPath': 'string',
                'Matcher': {
                    'HttpCode': 'string'
                },
                'LoadBalancerArns': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def modify_target_group_attributes(TargetGroupArn=None, Attributes=None):
    """
    Modifies the specified attributes of the specified target group.
    
    
    :example: response = client.modify_target_group_attributes(
        TargetGroupArn='string',
        Attributes=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            

    :type Attributes: list
    :param Attributes: [REQUIRED]
            The attributes.
            (dict) --Information about a target group attribute.
            Key (string) --The name of the attribute.
            deregistration_delay.timeout_seconds - The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused . The range is 0-3600 seconds. The default value is 300 seconds.
            stickiness.enabled - Indicates whether sticky sessions are enabled.
            stickiness.type - The type of sticky sessions. The possible value is lb_cookie .
            stickiness.lb_cookie.duration_seconds - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
            Value (string) --The value of the attribute.
            
            

    :rtype: dict
    :return: {
        'Attributes': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    deregistration_delay.timeout_seconds - The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused . The range is 0-3600 seconds. The default value is 300 seconds.
    stickiness.enabled - Indicates whether sticky sessions are enabled.
    stickiness.type - The type of sticky sessions. The possible value is lb_cookie .
    stickiness.lb_cookie.duration_seconds - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
    
    """
    pass

def register_targets(TargetGroupArn=None, Targets=None):
    """
    Registers the specified targets with the specified target group.
    The target must be in the virtual private cloud (VPC) that you specified for the target group.
    To remove a target from a target group, use  DeregisterTargets .
    
    
    :example: response = client.register_targets(
        TargetGroupArn='string',
        Targets=[
            {
                'Id': 'string',
                'Port': 123
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            

    :type Targets: list
    :param Targets: [REQUIRED]
            The targets.
            (dict) --Information about a target.
            Id (string) -- [REQUIRED]The ID of the target.
            Port (integer) --The port on which the target is listening.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def remove_tags(ResourceArns=None, TagKeys=None):
    """
    Removes the specified tags from the specified resource.
    To list the current tags for your resources, use  DescribeTags .
    
    
    :example: response = client.remove_tags(
        ResourceArns=[
            'string',
        ],
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArns: list
    :param ResourceArns: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource.
            (string) --
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The tag keys for the tags to remove.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def set_rule_priorities(RulePriorities=None):
    """
    Sets the priorities of the specified rules.
    You can reorder the rules as long as there are no priority conflicts in the new order. Any existing rules that you do not specify retain their current priority.
    
    
    :example: response = client.set_rule_priorities(
        RulePriorities=[
            {
                'RuleArn': 'string',
                'Priority': 123
            },
        ]
    )
    
    
    :type RulePriorities: list
    :param RulePriorities: [REQUIRED]
            The rule priorities.
            (dict) --Information about the priorities for the rules for a listener.
            RuleArn (string) --The Amazon Resource Name (ARN) of the rule.
            Priority (integer) --The rule priority.
            
            

    :rtype: dict
    :return: {
        'Rules': [
            {
                'RuleArn': 'string',
                'Priority': 'string',
                'Conditions': [
                    {
                        'Field': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'Actions': [
                    {
                        'Type': 'forward',
                        'TargetGroupArn': 'string'
                    },
                ],
                'IsDefault': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def set_security_groups(LoadBalancerArn=None, SecurityGroups=None):
    """
    Associates the specified security groups with the specified load balancer. The specified security groups override the previously associated security groups.
    
    
    :example: response = client.set_security_groups(
        LoadBalancerArn='string',
        SecurityGroups=[
            'string',
        ]
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            

    :type SecurityGroups: list
    :param SecurityGroups: [REQUIRED]
            The IDs of the security groups.
            (string) --
            

    :rtype: dict
    :return: {
        'SecurityGroupIds': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def set_subnets(LoadBalancerArn=None, Subnets=None):
    """
    Enables the Availability Zone for the specified subnets for the specified load balancer. The specified subnets replace the previously enabled subnets.
    
    
    :example: response = client.set_subnets(
        LoadBalancerArn='string',
        Subnets=[
            'string',
        ]
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            

    :type Subnets: list
    :param Subnets: [REQUIRED]
            The IDs of the subnets. You must specify at least two subnets. You can add only one subnet per Availability Zone.
            (string) --
            

    :rtype: dict
    :return: {
        'AvailabilityZones': [
            {
                'ZoneName': 'string',
                'SubnetId': 'string'
            },
        ]
    }
    
    
    """
    pass

