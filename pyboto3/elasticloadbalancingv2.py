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


def add_tags(ResourceArns=None, Tags=None):
    """
    :param ResourceArns: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource.
            (string) --
            
    :type ResourceArns: list
    :param Tags: [REQUIRED]
            The tags. Each resource can have a maximum of 10 tags.
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            
    :type Tags: list
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


def create_listener(LoadBalancerArn=None, Protocol=None, Port=None, SslPolicy=None, Certificates=None,
                    DefaultActions=None):
    """
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            
    :type LoadBalancerArn: string
    :param Protocol: [REQUIRED]
            The protocol for connections from clients to the load balancer.
            
    :type Protocol: string
    :param Port: [REQUIRED]
            The port on which the load balancer is listening.
            
    :type Port: integer
    :param SslPolicy: The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.
    :type SslPolicy: string
    :param Certificates: The SSL server certificate. You must provide exactly one certificate if the protocol is HTTPS.
            (dict) --Information about an SSL server certificate deployed on a load balancer.
            CertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.
            
            
    :type Certificates: list
    :param DefaultActions: [REQUIRED]
            The default actions for the listener.
            (dict) --Information about an action.
            Type (string) -- [REQUIRED]The type of action.
            TargetGroupArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target group.
            
            
    :type DefaultActions: list
    """
    pass


def create_load_balancer(Name=None, Subnets=None, SecurityGroups=None, Scheme=None, Tags=None):
    """
    :param Name: [REQUIRED]
            The name of the load balancer.
            This name must be unique within your AWS account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
            
    :type Name: string
    :param Subnets: [REQUIRED]
            The IDs of the subnets to attach to the load balancer. You can specify only one subnet per Availability Zone. You must specify subnets from at least two Availability Zones.
            (string) --
            
    :type Subnets: list
    :param SecurityGroups: The IDs of the security groups to assign to the load balancer.
            (string) --
            
    :type SecurityGroups: list
    :param Scheme: The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the Internet.
            The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.
            The default is an Internet-facing load balancer.
            
    :type Scheme: string
    :param Tags: One or more tags to assign to the load balancer.
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            
    :type Tags: list
    """
    pass


def create_rule(ListenerArn=None, Conditions=None, Priority=None, Actions=None):
    """
    :param ListenerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the listener.
            
    :type ListenerArn: string
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
            
            
    :type Conditions: list
    :param Priority: [REQUIRED]
            The priority for the rule. A listener can't have multiple rules with the same priority.
            
    :type Priority: integer
    :param Actions: [REQUIRED]
            The actions for the rule.
            (dict) --Information about an action.
            Type (string) -- [REQUIRED]The type of action.
            TargetGroupArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target group.
            
            
    :type Actions: list
    """
    pass


def create_target_group(Name=None, Protocol=None, Port=None, VpcId=None, HealthCheckProtocol=None, HealthCheckPort=None,
                        HealthCheckPath=None, HealthCheckIntervalSeconds=None, HealthCheckTimeoutSeconds=None,
                        HealthyThresholdCount=None, UnhealthyThresholdCount=None, Matcher=None):
    """
    :param Name: [REQUIRED]
            The name of the target group.
            
    :type Name: string
    :param Protocol: [REQUIRED]
            The protocol to use for routing traffic to the targets.
            
    :type Protocol: string
    :param Port: [REQUIRED]
            The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target.
            
    :type Port: integer
    :param VpcId: [REQUIRED]
            The identifier of the virtual private cloud (VPC).
            
    :type VpcId: string
    :param HealthCheckProtocol: The protocol the load balancer uses when performing health checks on targets. The default is the HTTP protocol.
    :type HealthCheckProtocol: string
    :param HealthCheckPort: The port the load balancer uses when performing health checks on targets. The default is traffic-port , which indicates the port on which each target receives traffic from the load balancer.
    :type HealthCheckPort: string
    :param HealthCheckPath: The ping path that is the destination on the targets for health checks. The default is /.
    :type HealthCheckPath: string
    :param HealthCheckIntervalSeconds: The approximate amount of time, in seconds, between health checks of an individual target. The default is 30 seconds.
    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckTimeoutSeconds: The amount of time, in seconds, during which no response from a target means a failed health check. The default is 5 seconds.
    :type HealthCheckTimeoutSeconds: integer
    :param HealthyThresholdCount: The number of consecutive health checks successes required before considering an unhealthy target healthy. The default is 5.
    :type HealthyThresholdCount: integer
    :param UnhealthyThresholdCount: The number of consecutive health check failures required before considering a target unhealthy. The default is 2.
    :type UnhealthyThresholdCount: integer
    :param Matcher: The HTTP codes to use when checking for a successful response from a target. The default is 200.
            HttpCode (string) -- [REQUIRED]The HTTP codes. The default value is 200. You can specify multiple values (for example, '200,202') or a range of values (for example, '200-299').
            
    :type Matcher: dict
    """
    pass


def delete_listener(ListenerArn=None):
    """
    :param ListenerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the listener.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the output of DeleteListener.
            
            
    :type ListenerArn: string
    """
    pass


def delete_load_balancer(LoadBalancerArn=None):
    """
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the output of DeleteLoadBalancer.
            
            
    :type LoadBalancerArn: string
    """
    pass


def delete_rule(RuleArn=None):
    """
    :param RuleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the rule.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the output of DeleteRule.
            
            
    :type RuleArn: string
    """
    pass


def delete_target_group(TargetGroupArn=None):
    """
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the output of DeleteTargetGroup.
            
            
    :type TargetGroupArn: string
    """
    pass


def deregister_targets(TargetGroupArn=None, Targets=None):
    """
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            
    :type TargetGroupArn: string
    :param Targets: [REQUIRED]
            The targets.
            (dict) --Information about a target.
            Id (string) -- [REQUIRED]The ID of the target.
            Port (integer) --The port on which the target is listening.
            
            
    :type Targets: list
    """
    pass


def describe_listeners(LoadBalancerArn=None, ListenerArns=None, Marker=None, PageSize=None):
    """
    :param LoadBalancerArn: The Amazon Resource Name (ARN) of the load balancer.
    :type LoadBalancerArn: string
    :param ListenerArns: The Amazon Resource Names (ARN) of the listeners.
            (string) --
            
    :type ListenerArns: list
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type Marker: string
    :param PageSize: The maximum number of results to return with this call.
    :type PageSize: integer
    """
    pass


def describe_load_balancer_attributes(LoadBalancerArn=None):
    """
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            Return typedict
            ReturnsResponse Syntax{
              'Attributes': [
                {
                  'Key': 'string',
                  'Value': 'string'
                },
              ]
            }
            Response Structure
            (dict) --Contains the output of DescribeLoadBalancerAttributes.
            Attributes (list) --Information about the load balancer attributes.
            (dict) --Information about a load balancer attribute.
            Key (string) --The name of the attribute.
            access_logs.s3.enabled - Indicates whether access logs stored in Amazon S3 are enabled.
            access_logs.s3.bucket - The name of the S3 bucket for the access logs. This attribute is required if access logs in Amazon S3 are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket.
            access_logs.s3.prefix - The prefix for the location in the S3 bucket. If you don't specify a prefix, the access logs are stored in the root of the bucket.
            deletion_protection.enabled - Indicates whether deletion protection is enabled.
            idle_timeout.timeout_seconds - The idle timeout value, in seconds. The valid range is 1-3600. The default is 60 seconds.
            Value (string) --The value of the attribute.
            
            
            
    :type LoadBalancerArn: string
    """
    pass


def describe_load_balancers(LoadBalancerArns=None, Names=None, Marker=None, PageSize=None):
    """
    :param LoadBalancerArns: The Amazon Resource Names (ARN) of the load balancers.
            (string) --
            
    :type LoadBalancerArns: list
    :param Names: The names of the load balancers.
            (string) --
            
    :type Names: list
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type Marker: string
    :param PageSize: The maximum number of results to return with this call.
    :type PageSize: integer
    """
    pass


def describe_rules(ListenerArn=None, RuleArns=None):
    """
    :param ListenerArn: The Amazon Resource Name (ARN) of the listener.
    :type ListenerArn: string
    :param RuleArns: The Amazon Resource Names (ARN) of the rules.
            (string) --
            
    :type RuleArns: list
    """
    pass


def describe_ssl_policies(Names=None, Marker=None, PageSize=None):
    """
    :param Names: The names of the policies.
            (string) --
            
    :type Names: list
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type Marker: string
    :param PageSize: The maximum number of results to return with this call.
    :type PageSize: integer
    """
    pass


def describe_tags(ResourceArns=None):
    """
    :param ResourceArns: [REQUIRED]
            The Amazon Resource Names (ARN) of the resources.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Contains the output of DescribeTags.
            TagDescriptions (list) --Information about the tags.
            (dict) --The tags associated with a resource.
            ResourceArn (string) --The Amazon Resource Name (ARN) of the resource.
            Tags (list) --Information about the tags.
            (dict) --Information about a tag.
            Key (string) --The key of the tag.
            Value (string) --The value of the tag.
            
            
            
            
    :type ResourceArns: list
    """
    pass


def describe_target_group_attributes(TargetGroupArn=None):
    """
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            Return typedict
            ReturnsResponse Syntax{
              'Attributes': [
                {
                  'Key': 'string',
                  'Value': 'string'
                },
              ]
            }
            Response Structure
            (dict) --Contains the output of DescribeTargetGroupAttributes.
            Attributes (list) --Information about the target group attributes
            (dict) --Information about a target group attribute.
            Key (string) --The name of the attribute.
            deregistration_delay.timeout_seconds - The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused . The range is 0-3600 seconds. The default value is 300 seconds.
            stickiness.enabled - Indicates whether sticky sessions are enabled.
            stickiness.type - The type of sticky sessions. The possible value is lb_cookie .
            stickiness.lb_cookie.duration_seconds - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
            Value (string) --The value of the attribute.
            
            
            
    :type TargetGroupArn: string
    """
    pass


def describe_target_groups(LoadBalancerArn=None, TargetGroupArns=None, Names=None, Marker=None, PageSize=None):
    """
    :param LoadBalancerArn: The Amazon Resource Name (ARN) of the load balancer.
    :type LoadBalancerArn: string
    :param TargetGroupArns: The Amazon Resource Names (ARN) of the target groups.
            (string) --
            
    :type TargetGroupArns: list
    :param Names: The names of the target groups.
            (string) --
            
    :type Names: list
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type Marker: string
    :param PageSize: The maximum number of results to return with this call.
    :type PageSize: integer
    """
    pass


def describe_target_health(TargetGroupArn=None, Targets=None):
    """
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            
    :type TargetGroupArn: string
    :param Targets: The targets.
            (dict) --Information about a target.
            Id (string) -- [REQUIRED]The ID of the target.
            Port (integer) --The port on which the target is listening.
            
            
    :type Targets: list
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


def modify_listener(ListenerArn=None, Port=None, Protocol=None, SslPolicy=None, Certificates=None, DefaultActions=None):
    """
    :param ListenerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the listener.
            
    :type ListenerArn: string
    :param Port: The port for connections from clients to the load balancer.
    :type Port: integer
    :param Protocol: The protocol for connections from clients to the load balancer.
    :type Protocol: string
    :param SslPolicy: The security policy that defines which ciphers and protocols are supported.
    :type SslPolicy: string
    :param Certificates: The SSL server certificate.
            (dict) --Information about an SSL server certificate deployed on a load balancer.
            CertificateArn (string) --The Amazon Resource Name (ARN) of the certificate.
            
            
    :type Certificates: list
    :param DefaultActions: The default actions.
            (dict) --Information about an action.
            Type (string) -- [REQUIRED]The type of action.
            TargetGroupArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target group.
            
            
    :type DefaultActions: list
    """
    pass


def modify_load_balancer_attributes(LoadBalancerArn=None, Attributes=None):
    """
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            
    :type LoadBalancerArn: string
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
            
            
    :type Attributes: list
    """
    pass


def modify_rule(RuleArn=None, Conditions=None, Actions=None):
    """
    :param RuleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the rule.
            
    :type RuleArn: string
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
            
            
    :type Conditions: list
    :param Actions: The actions.
            (dict) --Information about an action.
            Type (string) -- [REQUIRED]The type of action.
            TargetGroupArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target group.
            
            
    :type Actions: list
    """
    pass


def modify_target_group(TargetGroupArn=None, HealthCheckProtocol=None, HealthCheckPort=None, HealthCheckPath=None,
                        HealthCheckIntervalSeconds=None, HealthCheckTimeoutSeconds=None, HealthyThresholdCount=None,
                        UnhealthyThresholdCount=None, Matcher=None):
    """
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            
    :type TargetGroupArn: string
    :param HealthCheckProtocol: The protocol to use to connect with the target.
    :type HealthCheckProtocol: string
    :param HealthCheckPort: The port to use to connect with the target.
    :type HealthCheckPort: string
    :param HealthCheckPath: The ping path that is the destination for the health check request.
    :type HealthCheckPath: string
    :param HealthCheckIntervalSeconds: The approximate amount of time, in seconds, between health checks of an individual target.
    :type HealthCheckIntervalSeconds: integer
    :param HealthCheckTimeoutSeconds: The amount of time, in seconds, during which no response means a failed health check.
    :type HealthCheckTimeoutSeconds: integer
    :param HealthyThresholdCount: The number of consecutive health checks successes required before considering an unhealthy target healthy.
    :type HealthyThresholdCount: integer
    :param UnhealthyThresholdCount: The number of consecutive health check failures required before considering the target unhealthy.
    :type UnhealthyThresholdCount: integer
    :param Matcher: The HTTP codes to use when checking for a successful response from a target.
            HttpCode (string) -- [REQUIRED]The HTTP codes. The default value is 200. You can specify multiple values (for example, '200,202') or a range of values (for example, '200-299').
            
    :type Matcher: dict
    """
    pass


def modify_target_group_attributes(TargetGroupArn=None, Attributes=None):
    """
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            
    :type TargetGroupArn: string
    :param Attributes: [REQUIRED]
            The attributes.
            (dict) --Information about a target group attribute.
            Key (string) --The name of the attribute.
            deregistration_delay.timeout_seconds - The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused . The range is 0-3600 seconds. The default value is 300 seconds.
            stickiness.enabled - Indicates whether sticky sessions are enabled.
            stickiness.type - The type of sticky sessions. The possible value is lb_cookie .
            stickiness.lb_cookie.duration_seconds - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
            Value (string) --The value of the attribute.
            
            
    :type Attributes: list
    """
    pass


def register_targets(TargetGroupArn=None, Targets=None):
    """
    :param TargetGroupArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target group.
            
    :type TargetGroupArn: string
    :param Targets: [REQUIRED]
            The targets.
            (dict) --Information about a target.
            Id (string) -- [REQUIRED]The ID of the target.
            Port (integer) --The port on which the target is listening.
            
            
    :type Targets: list
    """
    pass


def remove_tags(ResourceArns=None, TagKeys=None):
    """
    :param ResourceArns: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource.
            (string) --
            
    :type ResourceArns: list
    :param TagKeys: [REQUIRED]
            The tag keys for the tags to remove.
            (string) --
            
    :type TagKeys: list
    """
    pass


def set_rule_priorities(RulePriorities=None):
    """
    :param RulePriorities: [REQUIRED]
            The rule priorities.
            (dict) --Information about the priorities for the rules for a listener.
            RuleArn (string) --The Amazon Resource Name (ARN) of the rule.
            Priority (integer) --The rule priority.
            
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Contains the output of SetRulePriorities.
            Rules (list) --Information about the rules.
            (dict) --Information about a rule.
            RuleArn (string) --The Amazon Resource Name (ARN) of the rule.
            Priority (string) --The priority.
            Conditions (list) --The conditions.
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
            
            Actions (list) --The actions.
            (dict) --Information about an action.
            Type (string) --The type of action.
            TargetGroupArn (string) --The Amazon Resource Name (ARN) of the target group.
            
            IsDefault (boolean) --Indicates whether this is the default rule.
            
            
            
    :type RulePriorities: list
    """
    pass


def set_security_groups(LoadBalancerArn=None, SecurityGroups=None):
    """
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            
    :type LoadBalancerArn: string
    :param SecurityGroups: [REQUIRED]
            The IDs of the security groups.
            (string) --
            
    :type SecurityGroups: list
    """
    pass


def set_subnets(LoadBalancerArn=None, Subnets=None):
    """
    :param LoadBalancerArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the load balancer.
            
    :type LoadBalancerArn: string
    :param Subnets: [REQUIRED]
            The IDs of the subnets. You must specify at least two subnets. You can add only one subnet per Availability Zone.
            (string) --
            
    :type Subnets: list
    """
    pass
