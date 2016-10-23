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


def add_tags(LoadBalancerNames=None, Tags=None):
    """
    :param LoadBalancerNames: [REQUIRED]
            The name of the load balancer. You can specify one load balancer only.
            (string) --
            
    :type LoadBalancerNames: list
    :param Tags: [REQUIRED]
            The tags.
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            
    :type Tags: list
    """
    pass


def apply_security_groups_to_load_balancer(LoadBalancerName=None, SecurityGroups=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param SecurityGroups: [REQUIRED]
            The IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.
            (string) --
            
    :type SecurityGroups: list
    """
    pass


def attach_load_balancer_to_subnets(LoadBalancerName=None, Subnets=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param Subnets: [REQUIRED]
            The IDs of the subnets to add. You can add only one subnet per Availability Zone.
            (string) --
            
    :type Subnets: list
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


def configure_health_check(LoadBalancerName=None, HealthCheck=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param HealthCheck: [REQUIRED]
            The configuration information.
            Target (string) -- [REQUIRED]The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.
            TCP is the default, specified as a TCP: port pair, for example 'TCP:5000'. In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.
            SSL is also specified as SSL: port pair, for example, SSL:5000.
            For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a HTTP:port;/;PathToPing; grouping, for example 'HTTP:80/weather/us/wa/seattle'. In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than '200 OK' within the timeout period is considered unhealthy.
            The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.
            Interval (integer) -- [REQUIRED]The approximate interval, in seconds, between health checks of an individual instance.
            Timeout (integer) -- [REQUIRED]The amount of time, in seconds, during which no response means a failed health check.
            This value must be less than the Interval value.
            UnhealthyThreshold (integer) -- [REQUIRED]The number of consecutive health check failures required before moving the instance to the Unhealthy state.
            HealthyThreshold (integer) -- [REQUIRED]The number of consecutive health checks successes required before moving the instance to the Healthy state.
            
    :type HealthCheck: dict
    """
    pass


def create_app_cookie_stickiness_policy(LoadBalancerName=None, PolicyName=None, CookieName=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param PolicyName: [REQUIRED]
            The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
            
    :type PolicyName: string
    :param CookieName: [REQUIRED]
            The name of the application cookie used for stickiness.
            
    :type CookieName: string
    """
    pass


def create_lb_cookie_stickiness_policy(LoadBalancerName=None, PolicyName=None, CookieExpirationPeriod=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param PolicyName: [REQUIRED]
            The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
            
    :type PolicyName: string
    :param CookieExpirationPeriod: The time period, in seconds, after which the cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.
    :type CookieExpirationPeriod: integer
    """
    pass


def create_load_balancer(LoadBalancerName=None, Listeners=None, AvailabilityZones=None, Subnets=None,
                         SecurityGroups=None, Scheme=None, Tags=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            This name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen.
            
    :type LoadBalancerName: string
    :param Listeners: [REQUIRED]
            The listeners.
            For more information, see Listeners for Your Classic Load Balancer in the Classic Load Balancers Guide .
            (dict) --Information about a listener.
            For information about the protocols and the ports supported by Elastic Load Balancing, see Listeners for Your Classic Load Balancer in the Classic Load Balancers Guide .
            Protocol (string) -- [REQUIRED]The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
            LoadBalancerPort (integer) -- [REQUIRED]The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
            InstanceProtocol (string) --The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
            If the front-end protocol is HTTP, HTTPS, TCP, or SSL, InstanceProtocol must be at the same protocol.
            If there is another listener with the same InstancePort whose InstanceProtocol is secure, (HTTPS or SSL), the listener's InstanceProtocol must also be secure.
            If there is another listener with the same InstancePort whose InstanceProtocol is HTTP or TCP, the listener's InstanceProtocol must be HTTP or TCP.
            InstancePort (integer) -- [REQUIRED]The port on which the instance is listening.
            SSLCertificateId (string) --The Amazon Resource Name (ARN) of the server certificate.
            
            
    :type Listeners: list
    :param AvailabilityZones: One or more Availability Zones from the same region as the load balancer.
            You must specify at least one Availability Zone.
            You can add more Availability Zones after you create the load balancer using EnableAvailabilityZonesForLoadBalancer .
            (string) --
            
    :type AvailabilityZones: list
    :param Subnets: The IDs of the subnets in your VPC to attach to the load balancer. Specify one subnet per Availability Zone specified in AvailabilityZones .
            (string) --
            
    :type Subnets: list
    :param SecurityGroups: The IDs of the security groups to assign to the load balancer.
            (string) --
            
    :type SecurityGroups: list
    :param Scheme: The type of a load balancer. Valid only for load balancers in a VPC.
            By default, Elastic Load Balancing creates an Internet-facing load balancer with a DNS name that resolves to public IP addresses. For more information about Internet-facing and Internal load balancers, see Load Balancer Scheme in the Elastic Load Balancing User Guide .
            Specify internal to create a load balancer with a DNS name that resolves to private IP addresses.
            
    :type Scheme: string
    :param Tags: A list of tags to assign to the load balancer.
            For more information about tagging your load balancer, see Tag Your Classic Load Balancer in the Classic Load Balancers Guide .
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            
    :type Tags: list
    """
    pass


def create_load_balancer_listeners(LoadBalancerName=None, Listeners=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param Listeners: [REQUIRED]
            The listeners.
            (dict) --Information about a listener.
            For information about the protocols and the ports supported by Elastic Load Balancing, see Listeners for Your Classic Load Balancer in the Classic Load Balancers Guide .
            Protocol (string) -- [REQUIRED]The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
            LoadBalancerPort (integer) -- [REQUIRED]The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
            InstanceProtocol (string) --The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
            If the front-end protocol is HTTP, HTTPS, TCP, or SSL, InstanceProtocol must be at the same protocol.
            If there is another listener with the same InstancePort whose InstanceProtocol is secure, (HTTPS or SSL), the listener's InstanceProtocol must also be secure.
            If there is another listener with the same InstancePort whose InstanceProtocol is HTTP or TCP, the listener's InstanceProtocol must be HTTP or TCP.
            InstancePort (integer) -- [REQUIRED]The port on which the instance is listening.
            SSLCertificateId (string) --The Amazon Resource Name (ARN) of the server certificate.
            
            
    :type Listeners: list
    """
    pass


def create_load_balancer_policy(LoadBalancerName=None, PolicyName=None, PolicyTypeName=None, PolicyAttributes=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param PolicyName: [REQUIRED]
            The name of the load balancer policy to be created. This name must be unique within the set of policies for this load balancer.
            
    :type PolicyName: string
    :param PolicyTypeName: [REQUIRED]
            The name of the base policy type. To get the list of policy types, use DescribeLoadBalancerPolicyTypes .
            
    :type PolicyTypeName: string
    :param PolicyAttributes: The policy attributes.
            (dict) --Information about a policy attribute.
            AttributeName (string) --The name of the attribute.
            AttributeValue (string) --The value of the attribute.
            
            
    :type PolicyAttributes: list
    """
    pass


def delete_load_balancer(LoadBalancerName=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Contains the output of DeleteLoadBalancer.
            
            
    :type LoadBalancerName: string
    """
    pass


def delete_load_balancer_listeners(LoadBalancerName=None, LoadBalancerPorts=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param LoadBalancerPorts: [REQUIRED]
            The client port numbers of the listeners.
            (integer) --
            
    :type LoadBalancerPorts: list
    """
    pass


def delete_load_balancer_policy(LoadBalancerName=None, PolicyName=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param PolicyName: [REQUIRED]
            The name of the policy.
            
    :type PolicyName: string
    """
    pass


def deregister_instances_from_load_balancer(LoadBalancerName=None, Instances=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param Instances: [REQUIRED]
            The IDs of the instances.
            (dict) --The ID of an EC2 instance.
            InstanceId (string) --The instance ID.
            
            
    :type Instances: list
    """
    pass


def describe_instance_health(LoadBalancerName=None, Instances=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param Instances: The IDs of the instances.
            (dict) --The ID of an EC2 instance.
            InstanceId (string) --The instance ID.
            
            
    :type Instances: list
    """
    pass


def describe_load_balancer_attributes(LoadBalancerName=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            Return typedict
            ReturnsResponse Syntax{
              'LoadBalancerAttributes': {
                'CrossZoneLoadBalancing': {
                  'Enabled': True|False
                },
                'AccessLog': {
                  'Enabled': True|False,
                  'S3BucketName': 'string',
                  'EmitInterval': 123,
                  'S3BucketPrefix': 'string'
                },
                'ConnectionDraining': {
                  'Enabled': True|False,
                  'Timeout': 123
                },
                'ConnectionSettings': {
                  'IdleTimeout': 123
                },
                'AdditionalAttributes': [
                  {
                    'Key': 'string',
                    'Value': 'string'
                  },
                ]
              }
            }
            Response Structure
            (dict) --Contains the output of DescribeLoadBalancerAttributes.
            LoadBalancerAttributes (dict) --Information about the load balancer attributes.
            CrossZoneLoadBalancing (dict) --If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
            For more information, see Configure Cross-Zone Load Balancing in the Classic Load Balancers Guide .
            Enabled (boolean) --Specifies whether cross-zone load balancing is enabled for the load balancer.
            AccessLog (dict) --If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
            For more information, see Enable Access Logs in the Classic Load Balancers Guide .
            Enabled (boolean) --Specifies whether access logs are enabled for the load balancer.
            S3BucketName (string) --The name of the Amazon S3 bucket where the access logs are stored.
            EmitInterval (integer) --The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
            Default: 60 minutes
            S3BucketPrefix (string) --The logical hierarchy you created for your Amazon S3 bucket, for example my-bucket-prefix/prod . If the prefix is not provided, the log is placed at the root level of the bucket.
            ConnectionDraining (dict) --If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
            For more information, see Configure Connection Draining in the Classic Load Balancers Guide .
            Enabled (boolean) --Specifies whether connection draining is enabled for the load balancer.
            Timeout (integer) --The maximum time, in seconds, to keep the existing connections open before deregistering the instances.
            ConnectionSettings (dict) --If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
            By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see Configure Idle Connection Timeout in the Classic Load Balancers Guide .
            IdleTimeout (integer) --The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.
            AdditionalAttributes (list) --This parameter is reserved.
            (dict) --This data type is reserved.
            Key (string) --This parameter is reserved.
            Value (string) --This parameter is reserved.
            
            
            
            
    :type LoadBalancerName: string
    """
    pass


def describe_load_balancer_policies(LoadBalancerName=None, PolicyNames=None):
    """
    :param LoadBalancerName: The name of the load balancer.
    :type LoadBalancerName: string
    :param PolicyNames: The names of the policies.
            (string) --
            
    :type PolicyNames: list
    """
    pass


def describe_load_balancer_policy_types(PolicyTypeNames=None):
    """
    :param PolicyTypeNames: The names of the policy types. If no names are specified, describes all policy types defined by Elastic Load Balancing.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'PolicyTypeDescriptions': [
                {
                  'PolicyTypeName': 'string',
                  'Description': 'string',
                  'PolicyAttributeTypeDescriptions': [
                    {
                      'AttributeName': 'string',
                      'AttributeType': 'string',
                      'Description': 'string',
                      'DefaultValue': 'string',
                      'Cardinality': 'string'
                    },
                  ]
                },
              ]
            }
            Response Structure
            (dict) --Contains the output of DescribeLoadBalancerPolicyTypes.
            PolicyTypeDescriptions (list) --Information about the policy types.
            (dict) --Information about a policy type.
            PolicyTypeName (string) --The name of the policy type.
            Description (string) --A description of the policy type.
            PolicyAttributeTypeDescriptions (list) --The description of the policy attributes associated with the policies defined by Elastic Load Balancing.
            (dict) --Information about a policy attribute type.
            AttributeName (string) --The name of the attribute.
            AttributeType (string) --The type of the attribute. For example, Boolean or Integer .
            Description (string) --A description of the attribute.
            DefaultValue (string) --The default value of the attribute, if applicable.
            Cardinality (string) --The cardinality of the attribute.
            Valid values:
            ONE(1) : Single value required
            ZERO_OR_ONE(0..1) : Up to one value is allowed
            ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed
            ONE_OR_MORE(1..*0) : Required. Multiple values are allowed
            
            
            
            
    :type PolicyTypeNames: list
    """
    pass


def describe_load_balancers(LoadBalancerNames=None, Marker=None, PageSize=None):
    """
    :param LoadBalancerNames: The names of the load balancers.
            (string) --
            
    :type LoadBalancerNames: list
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type Marker: string
    :param PageSize: The maximum number of results to return with this call (a number from 1 to 400). The default is 400.
    :type PageSize: integer
    """
    pass


def describe_tags(LoadBalancerNames=None):
    """
    :param LoadBalancerNames: [REQUIRED]
            The names of the load balancers.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'TagDescriptions': [
                {
                  'LoadBalancerName': 'string',
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
            (dict) --Contains the output for DescribeTags.
            TagDescriptions (list) --Information about the tags.
            (dict) --The tags associated with a load balancer.
            LoadBalancerName (string) --The name of the load balancer.
            Tags (list) --The tags.
            (dict) --Information about a tag.
            Key (string) --The key of the tag.
            Value (string) --The value of the tag.
            
            
            
            
    :type LoadBalancerNames: list
    """
    pass


def detach_load_balancer_from_subnets(LoadBalancerName=None, Subnets=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param Subnets: [REQUIRED]
            The IDs of the subnets.
            (string) --
            
    :type Subnets: list
    """
    pass


def disable_availability_zones_for_load_balancer(LoadBalancerName=None, AvailabilityZones=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param AvailabilityZones: [REQUIRED]
            The Availability Zones.
            (string) --
            
    :type AvailabilityZones: list
    """
    pass


def enable_availability_zones_for_load_balancer(LoadBalancerName=None, AvailabilityZones=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param AvailabilityZones: [REQUIRED]
            The Availability Zones. These must be in the same region as the load balancer.
            (string) --
            
    :type AvailabilityZones: list
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


def modify_load_balancer_attributes(LoadBalancerName=None, LoadBalancerAttributes=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param LoadBalancerAttributes: [REQUIRED]
            The attributes of the load balancer.
            CrossZoneLoadBalancing (dict) --If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
            For more information, see Configure Cross-Zone Load Balancing in the Classic Load Balancers Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether cross-zone load balancing is enabled for the load balancer.
            AccessLog (dict) --If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
            For more information, see Enable Access Logs in the Classic Load Balancers Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether access logs are enabled for the load balancer.
            S3BucketName (string) --The name of the Amazon S3 bucket where the access logs are stored.
            EmitInterval (integer) --The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
            Default: 60 minutes
            S3BucketPrefix (string) --The logical hierarchy you created for your Amazon S3 bucket, for example my-bucket-prefix/prod . If the prefix is not provided, the log is placed at the root level of the bucket.
            ConnectionDraining (dict) --If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
            For more information, see Configure Connection Draining in the Classic Load Balancers Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether connection draining is enabled for the load balancer.
            Timeout (integer) --The maximum time, in seconds, to keep the existing connections open before deregistering the instances.
            ConnectionSettings (dict) --If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
            By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see Configure Idle Connection Timeout in the Classic Load Balancers Guide .
            IdleTimeout (integer) -- [REQUIRED]The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.
            AdditionalAttributes (list) --This parameter is reserved.
            (dict) --This data type is reserved.
            Key (string) --This parameter is reserved.
            Value (string) --This parameter is reserved.
            
            
    :type LoadBalancerAttributes: dict
    """
    pass


def register_instances_with_load_balancer(LoadBalancerName=None, Instances=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param Instances: [REQUIRED]
            The IDs of the instances.
            (dict) --The ID of an EC2 instance.
            InstanceId (string) --The instance ID.
            
            
    :type Instances: list
    """
    pass


def remove_tags(LoadBalancerNames=None, Tags=None):
    """
    :param LoadBalancerNames: [REQUIRED]
            The name of the load balancer. You can specify a maximum of one load balancer name.
            (string) --
            
    :type LoadBalancerNames: list
    :param Tags: [REQUIRED]
            The list of tag keys to remove.
            (dict) --The key of a tag.
            Key (string) --The name of the key.
            
            
    :type Tags: list
    """
    pass


def set_load_balancer_listener_ssl_certificate(LoadBalancerName=None, LoadBalancerPort=None, SSLCertificateId=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param LoadBalancerPort: [REQUIRED]
            The port that uses the specified SSL certificate.
            
    :type LoadBalancerPort: integer
    :param SSLCertificateId: [REQUIRED]
            The Amazon Resource Name (ARN) of the SSL certificate.
            
    :type SSLCertificateId: string
    """
    pass


def set_load_balancer_policies_for_backend_server(LoadBalancerName=None, InstancePort=None, PolicyNames=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param InstancePort: [REQUIRED]
            The port number associated with the EC2 instance.
            
    :type InstancePort: integer
    :param PolicyNames: [REQUIRED]
            The names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.
            (string) --
            
    :type PolicyNames: list
    """
    pass


def set_load_balancer_policies_of_listener(LoadBalancerName=None, LoadBalancerPort=None, PolicyNames=None):
    """
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            
    :type LoadBalancerName: string
    :param LoadBalancerPort: [REQUIRED]
            The external port of the load balancer.
            
    :type LoadBalancerPort: integer
    :param PolicyNames: [REQUIRED]
            The names of the policies. This list must include all policies to be enabled. If you omit a policy that is currently enabled, it is disabled. If the list is empty, all current policies are disabled.
            (string) --
            
    :type PolicyNames: list
    """
    pass
