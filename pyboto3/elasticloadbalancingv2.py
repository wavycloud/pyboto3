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

def add_listener_certificates(ListenerArn=None, Certificates=None):
    """
    Adds the specified certificate to the specified secure listener.
    If the certificate was already added, the call is successful but the certificate is not added again.
    To list the certificates for your listener, use  DescribeListenerCertificates . To remove certificates from your listener, use  RemoveListenerCertificates .
    See also: AWS API Documentation
    
    
    :example: response = client.add_listener_certificates(
        ListenerArn='string',
        Certificates=[
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ]
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the listener.
            

    :type Certificates: list
    :param Certificates: [REQUIRED]
            The certificate to add. You can specify one certificate per call.
            (dict) --Information about an SSL server certificate.
            CertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.
            IsDefault (boolean) --Indicates whether the certificate is the default certificate.
            
            

    :rtype: dict
    :return: {
        'Certificates': [
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ]
    }
    
    
    """
    pass

def add_tags(ResourceArns=None, Tags=None):
    """
    Adds the specified tags to the specified Elastic Load Balancing resource. You can tag your Application Load Balancers, Network Load Balancers, and your target groups.
    Each tag consists of a key and an optional value. If a resource already has a tag with the same key, AddTags updates its value.
    To list the current tags for your resources, use  DescribeTags . To remove tags from your resources, use  RemoveTags .
    See also: AWS API Documentation
    
    Examples
    This example adds the specified tags to the specified load balancer.
    Expected Output:
    
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
    
    
    :returns: 
    (dict) --
    
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
    Creates a listener for the specified Application Load Balancer or Network Load Balancer.
    To update a listener, use  ModifyListener . When you are finished with a listener, you can delete it using  DeleteListener . If you are finished with both the listener and the load balancer, you can delete them both using  DeleteLoadBalancer .
    This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple listeners with the same settings, each call succeeds.
    For more information, see Listeners for Your Application Load Balancers in the Application Load Balancers Guide and Listeners for Your Network Load Balancers in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates an HTTP listener for the specified load balancer that forwards requests to the specified target group.
    Expected Output:
    This example creates an HTTPS listener for the specified load balancer that forwards requests to the specified target group. Note that you must specify an SSL certificate for an HTTPS listener. You can create and manage certificates using AWS Certificate Manager (ACM). Alternatively, you can create a certificate using SSL/TLS tools, get the certificate signed by a certificate authority (CA), and upload the certificate to AWS Identity and Access Management (IAM).
    Expected Output:
    
    :example: response = client.create_listener(
        LoadBalancerArn='string',
        Protocol='HTTP'|'HTTPS'|'TCP',
        Port=123,
        SslPolicy='string',
        Certificates=[
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
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
            The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocol is TCP.
            

    :type Port: integer
    :param Port: [REQUIRED]
            The port on which the load balancer is listening.
            

    :type SslPolicy: string
    :param SslPolicy: [HTTPS listeners] The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.

    :type Certificates: list
    :param Certificates: [HTTPS listeners] The SSL server certificate. You must provide exactly one certificate.
            (dict) --Information about an SSL server certificate.
            CertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.
            IsDefault (boolean) --Indicates whether the certificate is the default certificate.
            
            

    :type DefaultActions: list
    :param DefaultActions: [REQUIRED]
            The default action for the listener. For Application Load Balancers, the protocol of the specified target group must be HTTP or HTTPS. For Network Load Balancers, the protocol of the specified target group must be TCP.
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
                'Protocol': 'HTTP'|'HTTPS'|'TCP',
                'Certificates': [
                    {
                        'CertificateArn': 'string',
                        'IsDefault': True|False
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

def create_load_balancer(Name=None, Subnets=None, SubnetMappings=None, SecurityGroups=None, Scheme=None, Tags=None, Type=None, IpAddressType=None):
    """
    Creates an Application Load Balancer or a Network Load Balancer.
    When you create a load balancer, you can specify security groups, public subnets, IP address type, and tags. Otherwise, you could do so later using  SetSecurityGroups ,  SetSubnets ,  SetIpAddressType , and  AddTags .
    To create listeners for your load balancer, use  CreateListener . To describe your current load balancers, see  DescribeLoadBalancers . When you are finished with a load balancer, you can delete it using  DeleteLoadBalancer .
    For limit information, see Limits for Your Application Load Balancer in the Application Load Balancers Guide and Limits for Your Network Load Balancer in the Network Load Balancers Guide .
    This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple load balancers with the same settings, each call succeeds.
    For more information, see Application Load Balancers in the Application Load Balancers Guide and Network Load Balancers in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates an Internet-facing load balancer and enables the Availability Zones for the specified subnets.
    Expected Output:
    This example creates an internal load balancer and enables the Availability Zones for the specified subnets.
    Expected Output:
    
    :example: response = client.create_load_balancer(
        Name='string',
        Subnets=[
            'string',
        ],
        SubnetMappings=[
            {
                'SubnetId': 'string',
                'AllocationId': 'string'
            },
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
        ],
        Type='application'|'network',
        IpAddressType='ipv4'|'dualstack'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the load balancer.
            This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
            

    :type Subnets: list
    :param Subnets: The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
            [Application Load Balancers] You must specify subnets from at least two Availability Zones.
            [Network Load Balancers] You can specify subnets from one or more Availability Zones.
            (string) --
            

    :type SubnetMappings: list
    :param SubnetMappings: The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
            [Application Load Balancers] You must specify subnets from at least two Availability Zones. You cannot specify Elastic IP addresses for your subnets.
            [Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet.
            (dict) --Information about a subnet mapping.
            SubnetId (string) --The ID of the subnet.
            AllocationId (string) --[Network Load Balancers] The allocation ID of the Elastic IP address.
            
            

    :type SecurityGroups: list
    :param SecurityGroups: [Application Load Balancers] The IDs of the security groups for the load balancer.
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
            
            

    :type Type: string
    :param Type: The type of load balancer. The default is application .

    :type IpAddressType: string
    :param IpAddressType: [Application Load Balancers] The type of IP addresses used by the subnets for your load balancer. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses). Internal load balancers must use ipv4 .

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
                    'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                    'Reason': 'string'
                },
                'Type': 'application'|'network',
                'AvailabilityZones': [
                    {
                        'ZoneName': 'string',
                        'SubnetId': 'string',
                        'LoadBalancerAddresses': [
                            {
                                'IpAddress': 'string',
                                'AllocationId': 'string'
                            },
                        ]
                    },
                ],
                'SecurityGroups': [
                    'string',
                ],
                'IpAddressType': 'ipv4'|'dualstack'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_rule(ListenerArn=None, Conditions=None, Priority=None, Actions=None):
    """
    Creates a rule for the specified listener. The listener must be associated with an Application Load Balancer.
    Rules are evaluated in priority order, from the lowest value to the highest value. When the condition for a rule is met, the specified action is taken. If no conditions are met, the action for the default rule is taken. For more information, see Listener Rules in the Application Load Balancers Guide .
    To view your current rules, use  DescribeRules . To update a rule, use  ModifyRule . To set the priorities of your rules, use  SetRulePriorities . To delete a rule, use  DeleteRule .
    See also: AWS API Documentation
    
    Examples
    This example creates a rule that forwards requests to the specified target group if the URL contains the specified pattern (for example, /img/*).
    Expected Output:
    
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
            The conditions. Each condition specifies a field name and a single value.
            If the field name is host-header , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.
            A-Z, a-z, 0-9
            .
            (matches 0 or more characters)
            ? (matches exactly 1 character)
            If the field name is path-pattern , you can specify a single path pattern. A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.
            A-Z, a-z, 0-9
            _ - . $ / ~ ' ' @ : +
            (using amp;)
            (matches 0 or more characters)
            ? (matches exactly 1 character)
            (dict) --Information about a condition for a rule.
            Field (string) --The name of the field. The possible values are host-header and path-pattern .
            Values (list) --The condition value.
            If the field name is host-header , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.
            A-Z, a-z, 0-9
            .
            (matches 0 or more characters)
            ? (matches exactly 1 character)
            If the field name is path-pattern , you can specify a single path pattern (for example, /img/*). A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.
            A-Z, a-z, 0-9
            _ - . $ / ~ ' ' @ : +
            (using amp;)
            (matches 0 or more characters)
            ? (matches exactly 1 character)
            (string) --
            
            

    :type Priority: integer
    :param Priority: [REQUIRED]
            The priority for the rule. A listener can't have multiple rules with the same priority.
            

    :type Actions: list
    :param Actions: [REQUIRED]
            An action. Each action has the type forward and specifies a target group.
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
    
    .
    
    
    
    (matches 0 or more characters)
    
    
    ? (matches exactly 1 character)
    
    """
    pass

def create_target_group(Name=None, Protocol=None, Port=None, VpcId=None, HealthCheckProtocol=None, HealthCheckPort=None, HealthCheckPath=None, HealthCheckIntervalSeconds=None, HealthCheckTimeoutSeconds=None, HealthyThresholdCount=None, UnhealthyThresholdCount=None, Matcher=None, TargetType=None):
    """
    Creates a target group.
    To register targets with the target group, use  RegisterTargets . To update the health check settings for the target group, use  ModifyTargetGroup . To monitor the health of targets in the target group, use  DescribeTargetHealth .
    To route traffic to the targets in a target group, specify the target group in an action using  CreateListener or  CreateRule .
    To delete a target group, use  DeleteTargetGroup .
    This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple target groups with the same settings, each call succeeds.
    For more information, see Target Groups for Your Application Load Balancers in the Application Load Balancers Guide or Target Groups for Your Network Load Balancers in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a target group that you can use to route traffic to targets using HTTP on port 80. This target group uses the default health check configuration.
    Expected Output:
    
    :example: response = client.create_target_group(
        Name='string',
        Protocol='HTTP'|'HTTPS'|'TCP',
        Port=123,
        VpcId='string',
        HealthCheckProtocol='HTTP'|'HTTPS'|'TCP',
        HealthCheckPort='string',
        HealthCheckPath='string',
        HealthCheckIntervalSeconds=123,
        HealthCheckTimeoutSeconds=123,
        HealthyThresholdCount=123,
        UnhealthyThresholdCount=123,
        Matcher={
            'HttpCode': 'string'
        },
        TargetType='instance'|'ip'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the target group.
            This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
            

    :type Protocol: string
    :param Protocol: [REQUIRED]
            The protocol to use for routing traffic to the targets. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocol is TCP.
            

    :type Port: integer
    :param Port: [REQUIRED]
            The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target.
            

    :type VpcId: string
    :param VpcId: [REQUIRED]
            The identifier of the virtual private cloud (VPC).
            

    :type HealthCheckProtocol: string
    :param HealthCheckProtocol: The protocol the load balancer uses when performing health checks on targets. The TCP protocol is supported only if the protocol of the target group is TCP. For Application Load Balancers, the default is HTTP. For Network Load Balancers, the default is TCP.

    :type HealthCheckPort: string
    :param HealthCheckPort: The port the load balancer uses when performing health checks on targets. The default is traffic-port , which is the port on which each target receives traffic from the load balancer.

    :type HealthCheckPath: string
    :param HealthCheckPath: [HTTP/HTTPS health checks] The ping path that is the destination on the targets for health checks. The default is /.

    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: The approximate amount of time, in seconds, between health checks of an individual target. For Application Load Balancers, the range is 5 to 300 seconds. For Network Load Balancers, the supported values are 10 or 30 seconds. The default is 30 seconds.

    :type HealthCheckTimeoutSeconds: integer
    :param HealthCheckTimeoutSeconds: The amount of time, in seconds, during which no response from a target means a failed health check. For Application Load Balancers, the range is 2 to 60 seconds and the default is 5 seconds. For Network Load Balancers, this is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.

    :type HealthyThresholdCount: integer
    :param HealthyThresholdCount: The number of consecutive health checks successes required before considering an unhealthy target healthy. For Application Load Balancers, the default is 5. For Network Load Balancers, the default is 3.

    :type UnhealthyThresholdCount: integer
    :param UnhealthyThresholdCount: The number of consecutive health check failures required before considering a target unhealthy. For Application Load Balancers, the default is 2. For Network Load Balancers, this value must be the same as the healthy threshold count.

    :type Matcher: dict
    :param Matcher: [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a target.
            HttpCode (string) -- [REQUIRED]The HTTP codes.
            For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, '200,202') or a range of values (for example, '200-299').
            For Network Load Balancers, this is 200 to 399.
            

    :type TargetType: string
    :param TargetType: The type of target that you must specify when registering targets with this target group. The possible values are instance (targets are specified by instance ID) or ip (targets are specified by IP address). The default is instance . Note that you can't specify targets for a target group using both instance IDs and IP addresses.
            If the target type is ip , specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify publicly routable IP addresses.
            

    :rtype: dict
    :return: {
        'TargetGroups': [
            {
                'TargetGroupArn': 'string',
                'TargetGroupName': 'string',
                'Protocol': 'HTTP'|'HTTPS'|'TCP',
                'Port': 123,
                'VpcId': 'string',
                'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP',
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
                ],
                'TargetType': 'instance'|'ip'
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
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified listener.
    Expected Output:
    
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
    Deletes the specified Application Load Balancer or Network Load Balancer and its attached listeners.
    You can't delete a load balancer if deletion protection is enabled. If the load balancer does not exist or has already been deleted, the call succeeds.
    Deleting a load balancer does not affect its registered targets. For example, your EC2 instances continue to run and are still registered to their target groups. If you no longer need these EC2 instances, you can stop or terminate them.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified load balancer.
    Expected Output:
    
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
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified rule.
    Expected Output:
    
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
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified target group.
    Expected Output:
    
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
    See also: AWS API Documentation
    
    Examples
    This example deregisters the specified instance from the specified target group.
    Expected Output:
    
    :example: response = client.deregister_targets(
        TargetGroupArn='string',
        Targets=[
            {
                'Id': 'string',
                'Port': 123,
                'AvailabilityZone': 'string'
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            

    :type Targets: list
    :param Targets: [REQUIRED]
            The targets. If you specified a port override when you registered a target, you must specify both the target ID and the port when you deregister it.
            (dict) --Information about a target.
            Id (string) -- [REQUIRED]The ID of the target. If the target type of the target group is instance , specify an instance ID. If the target type is ip , specify an IP address.
            Port (integer) --The port on which the target is listening.
            AvailabilityZone (string) --An Availability Zone or all . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
            This parameter is not supported if the target type of the target group is instance . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
            With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is all .
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_account_limits(Marker=None, PageSize=None):
    """
    Describes the current Elastic Load Balancing resource limits for your AWS account.
    For more information, see Limits for Your Application Load Balancers in the Application Load Balancer Guide or Limits for Your Network Load Balancers in the Network Load Balancers Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_limits(
        Marker='string',
        PageSize=123
    )
    
    
    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict
    :return: {
        'Limits': [
            {
                'Name': 'string',
                'Max': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    application-load-balancers
    listeners-per-application-load-balancer
    listeners-per-network-load-balancer
    network-load-balancers
    rules-per-application-load-balancer
    target-groups
    targets-per-application-load-balancer
    targets-per-availability-zone-per-network-load-balancer
    targets-per-network-load-balancer
    
    """
    pass

def describe_listener_certificates(ListenerArn=None, Marker=None, PageSize=None):
    """
    Describes the certificates for the specified secure listener.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_listener_certificates(
        ListenerArn='string',
        Marker='string',
        PageSize=123
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]
            The Amazon Resource Names (ARN) of the listener.
            

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

    :rtype: dict
    :return: {
        'Certificates': [
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ],
        'NextMarker': 'string'
    }
    
    
    """
    pass

def describe_listeners(LoadBalancerArn=None, ListenerArns=None, Marker=None, PageSize=None):
    """
    Describes the specified listeners or the listeners for the specified Application Load Balancer or Network Load Balancer. You must specify either a load balancer or one or more listeners.
    See also: AWS API Documentation
    
    Examples
    This example describes the specified listener.
    Expected Output:
    
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
                'Protocol': 'HTTP'|'HTTPS'|'TCP',
                'Certificates': [
                    {
                        'CertificateArn': 'string',
                        'IsDefault': True|False
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
    Describes the attributes for the specified Application Load Balancer or Network Load Balancer.
    See also: AWS API Documentation
    
    Examples
    This example describes the attributes of the specified load balancer.
    Expected Output:
    
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
    Describes the specified load balancers or all of your load balancers.
    To describe the listeners for a load balancer, use  DescribeListeners . To describe the attributes for a load balancer, use  DescribeLoadBalancerAttributes .
    See also: AWS API Documentation
    
    Examples
    This example describes the specified load balancer.
    Expected Output:
    
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
    :param LoadBalancerArns: The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.
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
                    'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                    'Reason': 'string'
                },
                'Type': 'application'|'network',
                'AvailabilityZones': [
                    {
                        'ZoneName': 'string',
                        'SubnetId': 'string',
                        'LoadBalancerAddresses': [
                            {
                                'IpAddress': 'string',
                                'AllocationId': 'string'
                            },
                        ]
                    },
                ],
                'SecurityGroups': [
                    'string',
                ],
                'IpAddressType': 'ipv4'|'dualstack'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_rules(ListenerArn=None, RuleArns=None, Marker=None, PageSize=None):
    """
    Describes the specified rules or the rules for the specified listener. You must specify either a listener or one or more rules.
    See also: AWS API Documentation
    
    Examples
    This example describes the specified rule.
    Expected Output:
    
    :example: response = client.describe_rules(
        ListenerArn='string',
        RuleArns=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: The Amazon Resource Name (ARN) of the listener.

    :type RuleArns: list
    :param RuleArns: The Amazon Resource Names (ARN) of the rules.
            (string) --
            

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call.

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
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    A-Z, a-z, 0-9
    
    .
    
    
    
    (matches 0 or more characters)
    
    
    ? (matches exactly 1 character)
    
    """
    pass

def describe_ssl_policies(Names=None, Marker=None, PageSize=None):
    """
    Describes the specified policies or all policies used for SSL negotiation.
    For more information, see Security Policies in the Application Load Balancers Guide .
    See also: AWS API Documentation
    
    Examples
    This example describes the specified policy used for SSL negotiation.
    Expected Output:
    
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
    Describes the tags for the specified resources. You can describe the tags for one or more Application Load Balancers, Network Load Balancers, and target groups.
    See also: AWS API Documentation
    
    Examples
    This example describes the tags assigned to the specified load balancer.
    Expected Output:
    
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
    See also: AWS API Documentation
    
    Examples
    This example describes the attributes of the specified target group.
    Expected Output:
    
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
    See also: AWS API Documentation
    
    Examples
    This example describes the specified target group.
    Expected Output:
    
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
                'Protocol': 'HTTP'|'HTTPS'|'TCP',
                'Port': 123,
                'VpcId': 'string',
                'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP',
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
                ],
                'TargetType': 'instance'|'ip'
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
    See also: AWS API Documentation
    
    Examples
    This example describes the health of the targets for the specified target group. One target is healthy but the other is not specified in an action, so it can't receive traffic from the load balancer.
    Expected Output:
    This example describes the health of the specified target. This target is healthy.
    Expected Output:
    
    :example: response = client.describe_target_health(
        TargetGroupArn='string',
        Targets=[
            {
                'Id': 'string',
                'Port': 123,
                'AvailabilityZone': 'string'
            },
        ]
    )
    
    
    :type TargetGroupArn: string
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            

    :type Targets: list
    :param Targets: The targets.
            (dict) --Information about a target.
            Id (string) -- [REQUIRED]The ID of the target. If the target type of the target group is instance , specify an instance ID. If the target type is ip , specify an IP address.
            Port (integer) --The port on which the target is listening.
            AvailabilityZone (string) --An Availability Zone or all . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
            This parameter is not supported if the target type of the target group is instance . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
            With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is all .
            
            

    :rtype: dict
    :return: {
        'TargetHealthDescriptions': [
            {
                'Target': {
                    'Id': 'string',
                    'Port': 123,
                    'AvailabilityZone': 'string'
                },
                'HealthCheckPort': 'string',
                'TargetHealth': {
                    'State': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                    'Reason': 'Elb.RegistrationInProgress'|'Elb.InitialHealthChecking'|'Target.ResponseCodeMismatch'|'Target.Timeout'|'Target.FailedHealthChecks'|'Target.NotRegistered'|'Target.NotInUse'|'Target.DeregistrationInProgress'|'Target.InvalidState'|'Target.IpUnusable'|'Elb.InternalError',
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
    Any properties that you do not specify retain their current values. However, changing the protocol from HTTPS to HTTP removes the security policy and SSL certificate properties. If you change the protocol from HTTP to HTTPS, you must add the security policy and server certificate.
    See also: AWS API Documentation
    
    Examples
    This example changes the default action for the specified listener.
    Expected Output:
    This example changes the server certificate for the specified HTTPS listener.
    Expected Output:
    
    :example: response = client.modify_listener(
        ListenerArn='string',
        Port=123,
        Protocol='HTTP'|'HTTPS'|'TCP',
        SslPolicy='string',
        Certificates=[
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
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
    :param Protocol: The protocol for connections from clients to the load balancer. Application Load Balancers support HTTP and HTTPS and Network Load Balancers support TCP.

    :type SslPolicy: string
    :param SslPolicy: The security policy that defines which protocols and ciphers are supported. For more information, see Security Policies in the Application Load Balancers Guide .

    :type Certificates: list
    :param Certificates: The default SSL server certificate.
            (dict) --Information about an SSL server certificate.
            CertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.
            IsDefault (boolean) --Indicates whether the certificate is the default certificate.
            
            

    :type DefaultActions: list
    :param DefaultActions: The default action. For Application Load Balancers, the protocol of the specified target group must be HTTP or HTTPS. For Network Load Balancers, the protocol of the specified target group must be TCP.
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
                'Protocol': 'HTTP'|'HTTPS'|'TCP',
                'Certificates': [
                    {
                        'CertificateArn': 'string',
                        'IsDefault': True|False
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
    Modifies the specified attributes of the specified Application Load Balancer or Network Load Balancer.
    If any of the specified attributes can't be modified as requested, the call fails. Any existing attributes that you do not modify retain their current values.
    See also: AWS API Documentation
    
    Examples
    This example enables deletion protection for the specified load balancer.
    Expected Output:
    This example changes the idle timeout value for the specified load balancer.
    Expected Output:
    This example enables access logs for the specified load balancer. Note that the S3 bucket must exist in the same region as the load balancer and must have a policy attached that grants access to the Elastic Load Balancing service.
    Expected Output:
    
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
            access_logs.s3.enabled - [Application Load Balancers] Indicates whether access logs stored in Amazon S3 are enabled. The value is true or false .
            access_logs.s3.bucket - [Application Load Balancers] The name of the S3 bucket for the access logs. This attribute is required if access logs in Amazon S3 are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket.
            access_logs.s3.prefix - [Application Load Balancers] The prefix for the location in the S3 bucket. If you don't specify a prefix, the access logs are stored in the root of the bucket.
            deletion_protection.enabled - Indicates whether deletion protection is enabled. The value is true or false .
            idle_timeout.timeout_seconds - [Application Load Balancers] The idle timeout value, in seconds. The valid range is 1-4000. The default is 60 seconds.
            load_balancing.cross_zone.enabled - [Network Load Balancers] Indicates whether cross-zone load balancing is enabled. The value is true or false . The default is false .
            routing.http2.enabled - [Application Load Balancers] Indicates whether HTTP/2 is enabled. The value is true or false . The default is true .
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
    access_logs.s3.enabled - [Application Load Balancers] Indicates whether access logs stored in Amazon S3 are enabled. The value is true or false .
    access_logs.s3.bucket - [Application Load Balancers] The name of the S3 bucket for the access logs. This attribute is required if access logs in Amazon S3 are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket.
    access_logs.s3.prefix - [Application Load Balancers] The prefix for the location in the S3 bucket. If you don't specify a prefix, the access logs are stored in the root of the bucket.
    deletion_protection.enabled - Indicates whether deletion protection is enabled. The value is true or false .
    idle_timeout.timeout_seconds - [Application Load Balancers] The idle timeout value, in seconds. The valid range is 1-4000. The default is 60 seconds.
    load_balancing.cross_zone.enabled - [Network Load Balancers] Indicates whether cross-zone load balancing is enabled. The value is true or false . The default is false .
    routing.http2.enabled - [Application Load Balancers] Indicates whether HTTP/2 is enabled. The value is true or false . The default is true .
    
    """
    pass

def modify_rule(RuleArn=None, Conditions=None, Actions=None):
    """
    Modifies the specified rule.
    Any existing properties that you do not modify retain their current values.
    To modify the default action, use  ModifyListener .
    See also: AWS API Documentation
    
    Examples
    This example modifies the condition for the specified rule.
    Expected Output:
    
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
            Field (string) --The name of the field. The possible values are host-header and path-pattern .
            Values (list) --The condition value.
            If the field name is host-header , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.
            A-Z, a-z, 0-9
            .
            (matches 0 or more characters)
            ? (matches exactly 1 character)
            If the field name is path-pattern , you can specify a single path pattern (for example, /img/*). A path pattern is case sensitive, can be up to 128 characters in length, and can contain any of the following characters. Note that you can include up to three wildcard characters.
            A-Z, a-z, 0-9
            _ - . $ / ~ ' ' @ : +
            (using amp;)
            (matches 0 or more characters)
            ? (matches exactly 1 character)
            (string) --
            
            

    :type Actions: list
    :param Actions: The actions. The target group must use the HTTP or HTTPS protocol.
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
    
    .
    
    
    
    (matches 0 or more characters)
    
    
    ? (matches exactly 1 character)
    
    """
    pass

def modify_target_group(TargetGroupArn=None, HealthCheckProtocol=None, HealthCheckPort=None, HealthCheckPath=None, HealthCheckIntervalSeconds=None, HealthCheckTimeoutSeconds=None, HealthyThresholdCount=None, UnhealthyThresholdCount=None, Matcher=None):
    """
    Modifies the health checks used when evaluating the health state of the targets in the specified target group.
    To monitor the health of the targets, use  DescribeTargetHealth .
    See also: AWS API Documentation
    
    Examples
    This example changes the configuration of the health checks used to evaluate the health of the targets for the specified target group.
    Expected Output:
    
    :example: response = client.modify_target_group(
        TargetGroupArn='string',
        HealthCheckProtocol='HTTP'|'HTTPS'|'TCP',
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
    :param HealthCheckProtocol: The protocol the load balancer uses when performing health checks on targets. The TCP protocol is supported only if the protocol of the target group is TCP.

    :type HealthCheckPort: string
    :param HealthCheckPort: The port the load balancer uses when performing health checks on targets.

    :type HealthCheckPath: string
    :param HealthCheckPath: [HTTP/HTTPS health checks] The ping path that is the destination for the health check request.

    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckIntervalSeconds: The approximate amount of time, in seconds, between health checks of an individual target. For Application Load Balancers, the range is 5 to 300 seconds. For Network Load Balancers, the supported values are 10 or 30 seconds.

    :type HealthCheckTimeoutSeconds: integer
    :param HealthCheckTimeoutSeconds: [HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a failed health check.

    :type HealthyThresholdCount: integer
    :param HealthyThresholdCount: The number of consecutive health checks successes required before considering an unhealthy target healthy.

    :type UnhealthyThresholdCount: integer
    :param UnhealthyThresholdCount: The number of consecutive health check failures required before considering the target unhealthy. For Network Load Balancers, this value must be the same as the healthy threshold count.

    :type Matcher: dict
    :param Matcher: [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a target.
            HttpCode (string) -- [REQUIRED]The HTTP codes.
            For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, '200,202') or a range of values (for example, '200-299').
            For Network Load Balancers, this is 200 to 399.
            

    :rtype: dict
    :return: {
        'TargetGroups': [
            {
                'TargetGroupArn': 'string',
                'TargetGroupName': 'string',
                'Protocol': 'HTTP'|'HTTPS'|'TCP',
                'Port': 123,
                'VpcId': 'string',
                'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP',
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
                ],
                'TargetType': 'instance'|'ip'
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
    See also: AWS API Documentation
    
    Examples
    This example sets the deregistration delay timeout to the specified value for the specified target group.
    Expected Output:
    
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
            proxy_protocol_v2.enabled - [Network Load Balancers] Indicates whether Proxy Protocol version 2 is enabled.
            stickiness.enabled - [Application Load Balancers] Indicates whether sticky sessions are enabled. The value is true or false .
            stickiness.type - [Application Load Balancers] The type of sticky sessions. The possible value is lb_cookie .
            stickiness.lb_cookie.duration_seconds - [Application Load Balancers] The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
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
    proxy_protocol_v2.enabled - [Network Load Balancers] Indicates whether Proxy Protocol version 2 is enabled.
    stickiness.enabled - [Application Load Balancers] Indicates whether sticky sessions are enabled. The value is true or false .
    stickiness.type - [Application Load Balancers] The type of sticky sessions. The possible value is lb_cookie .
    stickiness.lb_cookie.duration_seconds - [Application Load Balancers] The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
    
    """
    pass

def register_targets(TargetGroupArn=None, Targets=None):
    """
    Registers the specified targets with the specified target group.
    You can register targets by instance ID or by IP address. If the target is an EC2 instance, it must be in the running state when you register it.
    By default, the load balancer routes requests to registered targets using the protocol and port for the target group. Alternatively, you can override the port for a target when you register it. You can register each EC2 instance or IP address with the same target group multiple times using different ports.
    With a Network Load Balancer, you cannot register instances by instance ID if they have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1. You can register instances of these types by IP address.
    To remove a target from a target group, use  DeregisterTargets .
    See also: AWS API Documentation
    
    Examples
    This example registers the specified instances with the specified target group.
    Expected Output:
    This example registers the specified instance with the specified target group using multiple ports. This enables you to register ECS containers on the same instance as targets in the target group.
    Expected Output:
    
    :example: response = client.register_targets(
        TargetGroupArn='string',
        Targets=[
            {
                'Id': 'string',
                'Port': 123,
                'AvailabilityZone': 'string'
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
            Id (string) -- [REQUIRED]The ID of the target. If the target type of the target group is instance , specify an instance ID. If the target type is ip , specify an IP address.
            Port (integer) --The port on which the target is listening.
            AvailabilityZone (string) --An Availability Zone or all . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
            This parameter is not supported if the target type of the target group is instance . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
            With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is all .
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_listener_certificates(ListenerArn=None, Certificates=None):
    """
    Removes the specified certificate from the specified secure listener.
    You can't remove the default certificate for a listener. To replace the default certificate, call  ModifyListener .
    To list the certificates for your listener, use  DescribeListenerCertificates .
    See also: AWS API Documentation
    
    
    :example: response = client.remove_listener_certificates(
        ListenerArn='string',
        Certificates=[
            {
                'CertificateArn': 'string',
                'IsDefault': True|False
            },
        ]
    )
    
    
    :type ListenerArn: string
    :param ListenerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the listener.
            

    :type Certificates: list
    :param Certificates: [REQUIRED]
            The certificate to remove. You can specify one certificate per call.
            (dict) --Information about an SSL server certificate.
            CertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.
            IsDefault (boolean) --Indicates whether the certificate is the default certificate.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_tags(ResourceArns=None, TagKeys=None):
    """
    Removes the specified tags from the specified Elastic Load Balancing resource.
    To list the current tags for your resources, use  DescribeTags .
    See also: AWS API Documentation
    
    Examples
    This example removes the specified tags from the specified load balancer.
    Expected Output:
    
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
    
    
    :returns: 
    (dict) --
    
    """
    pass

def set_ip_address_type(LoadBalancerArn=None, IpAddressType=None):
    """
    Sets the type of IP addresses used by the subnets of the specified Application Load Balancer or Network Load Balancer.
    Note that Network Load Balancers must use ipv4 .
    See also: AWS API Documentation
    
    
    :example: response = client.set_ip_address_type(
        LoadBalancerArn='string',
        IpAddressType='ipv4'|'dualstack'
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            

    :type IpAddressType: string
    :param IpAddressType: [REQUIRED]
            The IP address type. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses). Internal load balancers must use ipv4 .
            

    :rtype: dict
    :return: {
        'IpAddressType': 'ipv4'|'dualstack'
    }
    
    
    """
    pass

def set_rule_priorities(RulePriorities=None):
    """
    Sets the priorities of the specified rules.
    You can reorder the rules as long as there are no priority conflicts in the new order. Any existing rules that you do not specify retain their current priority.
    See also: AWS API Documentation
    
    Examples
    This example sets the priority of the specified rule.
    Expected Output:
    
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
    A-Z, a-z, 0-9
    _ - . $ / ~ " ' @ : +
    (using amp;)
    
    (matches 0 or more characters)
    
    
    ? (matches exactly 1 character)
    
    """
    pass

def set_security_groups(LoadBalancerArn=None, SecurityGroups=None):
    """
    Associates the specified security groups with the specified Application Load Balancer. The specified security groups override the previously associated security groups.
    Note that you can't specify a security group for a Network Load Balancer.
    See also: AWS API Documentation
    
    Examples
    This example associates the specified security group with the specified load balancer.
    Expected Output:
    
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

def set_subnets(LoadBalancerArn=None, Subnets=None, SubnetMappings=None):
    """
    Enables the Availability Zone for the specified public subnets for the specified Application Load Balancer. The specified subnets replace the previously enabled subnets.
    Note that you can't change the subnets for a Network Load Balancer.
    See also: AWS API Documentation
    
    Examples
    This example enables the Availability Zones for the specified subnets for the specified load balancer.
    Expected Output:
    
    :example: response = client.set_subnets(
        LoadBalancerArn='string',
        Subnets=[
            'string',
        ],
        SubnetMappings=[
            {
                'SubnetId': 'string',
                'AllocationId': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerArn: string
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            

    :type Subnets: list
    :param Subnets: [REQUIRED]
            The IDs of the public subnets. You must specify subnets from at least two Availability Zones. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
            (string) --
            

    :type SubnetMappings: list
    :param SubnetMappings: The IDs of the public subnets. You must specify subnets from at least two Availability Zones. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
            You cannot specify Elastic IP addresses for your subnets.
            (dict) --Information about a subnet mapping.
            SubnetId (string) --The ID of the subnet.
            AllocationId (string) --[Network Load Balancers] The allocation ID of the Elastic IP address.
            
            

    :rtype: dict
    :return: {
        'AvailabilityZones': [
            {
                'ZoneName': 'string',
                'SubnetId': 'string',
                'LoadBalancerAddresses': [
                    {
                        'IpAddress': 'string',
                        'AllocationId': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

