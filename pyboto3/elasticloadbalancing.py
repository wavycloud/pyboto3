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

def add_tags(LoadBalancerNames=None, Tags=None):
    """
    Adds the specified tags to the specified load balancer. Each load balancer can have a maximum of 10 tags.
    Each tag consists of a key and an optional value. If a tag with the same key is already associated with the load balancer, AddTags updates its value.
    For more information, see Tag Your Classic Load Balancer in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example adds two tags to the specified load balancer.
    Expected Output:
    
    :example: response = client.add_tags(
        LoadBalancerNames=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]
            The name of the load balancer. You can specify one load balancer only.
            (string) --
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The tags.
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def apply_security_groups_to_load_balancer(LoadBalancerName=None, SecurityGroups=None):
    """
    Associates one or more security groups with your load balancer in a virtual private cloud (VPC). The specified security groups override the previously associated security groups.
    For more information, see Security Groups for Load Balancers in a VPC in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example associates a security group with the specified load balancer in a VPC.
    Expected Output:
    
    :example: response = client.apply_security_groups_to_load_balancer(
        LoadBalancerName='string',
        SecurityGroups=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type SecurityGroups: list
    :param SecurityGroups: [REQUIRED]
            The IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.
            (string) --
            

    :rtype: dict
    :return: {
        'SecurityGroups': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def attach_load_balancer_to_subnets(LoadBalancerName=None, Subnets=None):
    """
    Adds one or more subnets to the set of configured subnets for the specified load balancer.
    The load balancer evenly distributes requests across all registered subnets. For more information, see Add or Remove Subnets for Your Load Balancer in a VPC in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example adds the specified subnet to the set of configured subnets for the specified load balancer.
    Expected Output:
    
    :example: response = client.attach_load_balancer_to_subnets(
        LoadBalancerName='string',
        Subnets=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type Subnets: list
    :param Subnets: [REQUIRED]
            The IDs of the subnets to add. You can add only one subnet per Availability Zone.
            (string) --
            

    :rtype: dict
    :return: {
        'Subnets': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
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

def configure_health_check(LoadBalancerName=None, HealthCheck=None):
    """
    Specifies the health check settings to use when evaluating the health state of your EC2 instances.
    For more information, see Configure Health Checks for Your Load Balancer in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example specifies the health check settings used to evaluate the health of your backend EC2 instances.
    Expected Output:
    
    :example: response = client.configure_health_check(
        LoadBalancerName='string',
        HealthCheck={
            'Target': 'string',
            'Interval': 123,
            'Timeout': 123,
            'UnhealthyThreshold': 123,
            'HealthyThreshold': 123
        }
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type HealthCheck: dict
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
            

    :rtype: dict
    :return: {
        'HealthCheck': {
            'Target': 'string',
            'Interval': 123,
            'Timeout': 123,
            'UnhealthyThreshold': 123,
            'HealthyThreshold': 123
        }
    }
    
    
    """
    pass

def create_app_cookie_stickiness_policy(LoadBalancerName=None, PolicyName=None, CookieName=None):
    """
    Generates a stickiness policy with sticky session lifetimes that follow that of an application-generated cookie. This policy can be associated only with HTTP/HTTPS listeners.
    This policy is similar to the policy created by  CreateLBCookieStickinessPolicy , except that the lifetime of the special Elastic Load Balancing cookie, AWSELB , follows the lifetime of the application-generated cookie specified in the policy configuration. The load balancer only inserts a new stickiness cookie when the application response includes a new application cookie.
    If the application cookie is explicitly removed or expires, the session stops being sticky until a new application cookie is issued.
    For more information, see Application-Controlled Session Stickiness in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example generates a stickiness policy that follows the sticky session lifetimes of the application-generated cookie.
    Expected Output:
    
    :example: response = client.create_app_cookie_stickiness_policy(
        LoadBalancerName='string',
        PolicyName='string',
        CookieName='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
            

    :type CookieName: string
    :param CookieName: [REQUIRED]
            The name of the application cookie used for stickiness.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_lb_cookie_stickiness_policy(LoadBalancerName=None, PolicyName=None, CookieExpirationPeriod=None):
    """
    Generates a stickiness policy with sticky session lifetimes controlled by the lifetime of the browser (user-agent) or a specified expiration period. This policy can be associated only with HTTP/HTTPS listeners.
    When a load balancer implements this policy, the load balancer uses a special cookie to track the instance for each request. When the load balancer receives a request, it first checks to see if this cookie is present in the request. If so, the load balancer sends the request to the application server specified in the cookie. If not, the load balancer sends the request to a server that is chosen based on the existing load-balancing algorithm.
    A cookie is inserted into the response for binding subsequent requests from the same user to that server. The validity of the cookie is based on the cookie expiration time, which is specified in the policy configuration.
    For more information, see Duration-Based Session Stickiness in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example generates a stickiness policy with sticky session lifetimes controlled by the specified expiration period.
    Expected Output:
    
    :example: response = client.create_lb_cookie_stickiness_policy(
        LoadBalancerName='string',
        PolicyName='string',
        CookieExpirationPeriod=123
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
            

    :type CookieExpirationPeriod: integer
    :param CookieExpirationPeriod: The time period, in seconds, after which the cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_load_balancer(LoadBalancerName=None, Listeners=None, AvailabilityZones=None, Subnets=None, SecurityGroups=None, Scheme=None, Tags=None):
    """
    Creates a Classic Load Balancer.
    You can add listeners, security groups, subnets, and tags when you create your load balancer, or you can add them later using  CreateLoadBalancerListeners ,  ApplySecurityGroupsToLoadBalancer ,  AttachLoadBalancerToSubnets , and  AddTags .
    To describe your current load balancers, see  DescribeLoadBalancers . When you are finished with a load balancer, you can delete it using  DeleteLoadBalancer .
    You can create up to 20 load balancers per region per account. You can request an increase for the number of load balancers for your account. For more information, see Limits for Your Classic Load Balancer in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a load balancer with an HTTP listener in a VPC.
    Expected Output:
    This example creates a load balancer with an HTTP listener in EC2-Classic.
    Expected Output:
    This example creates a load balancer with an HTTPS listener in a VPC.
    Expected Output:
    This example creates a load balancer with an HTTPS listener in EC2-Classic.
    Expected Output:
    This example creates an internal load balancer with an HTTP listener in a VPC.
    Expected Output:
    
    :example: response = client.create_load_balancer(
        LoadBalancerName='string',
        Listeners=[
            {
                'Protocol': 'string',
                'LoadBalancerPort': 123,
                'InstanceProtocol': 'string',
                'InstancePort': 123,
                'SSLCertificateId': 'string'
            },
        ],
        AvailabilityZones=[
            'string',
        ],
        Subnets=[
            'string',
        ],
        SecurityGroups=[
            'string',
        ],
        Scheme='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            This name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen.
            

    :type Listeners: list
    :param Listeners: [REQUIRED]
            The listeners.
            For more information, see Listeners for Your Classic Load Balancer in the Classic Load Balancer Guide .
            (dict) --Information about a listener.
            For information about the protocols and the ports supported by Elastic Load Balancing, see Listeners for Your Classic Load Balancer in the Classic Load Balancer Guide .
            Protocol (string) -- [REQUIRED]The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
            LoadBalancerPort (integer) -- [REQUIRED]The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
            InstanceProtocol (string) --The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
            If the front-end protocol is HTTP, HTTPS, TCP, or SSL, InstanceProtocol must be at the same protocol.
            If there is another listener with the same InstancePort whose InstanceProtocol is secure, (HTTPS or SSL), the listener's InstanceProtocol must also be secure.
            If there is another listener with the same InstancePort whose InstanceProtocol is HTTP or TCP, the listener's InstanceProtocol must be HTTP or TCP.
            InstancePort (integer) -- [REQUIRED]The port on which the instance is listening.
            SSLCertificateId (string) --The Amazon Resource Name (ARN) of the server certificate.
            
            

    :type AvailabilityZones: list
    :param AvailabilityZones: One or more Availability Zones from the same region as the load balancer.
            You must specify at least one Availability Zone.
            You can add more Availability Zones after you create the load balancer using EnableAvailabilityZonesForLoadBalancer .
            (string) --
            

    :type Subnets: list
    :param Subnets: The IDs of the subnets in your VPC to attach to the load balancer. Specify one subnet per Availability Zone specified in AvailabilityZones .
            (string) --
            

    :type SecurityGroups: list
    :param SecurityGroups: The IDs of the security groups to assign to the load balancer.
            (string) --
            

    :type Scheme: string
    :param Scheme: The type of a load balancer. Valid only for load balancers in a VPC.
            By default, Elastic Load Balancing creates an Internet-facing load balancer with a DNS name that resolves to public IP addresses. For more information about Internet-facing and Internal load balancers, see Load Balancer Scheme in the Elastic Load Balancing User Guide .
            Specify internal to create a load balancer with a DNS name that resolves to private IP addresses.
            

    :type Tags: list
    :param Tags: A list of tags to assign to the load balancer.
            For more information about tagging your load balancer, see Tag Your Classic Load Balancer in the Classic Load Balancer Guide .
            (dict) --Information about a tag.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) --The value of the tag.
            
            

    :rtype: dict
    :return: {
        'DNSName': 'string'
    }
    
    
    """
    pass

def create_load_balancer_listeners(LoadBalancerName=None, Listeners=None):
    """
    Creates one or more listeners for the specified load balancer. If a listener with the specified port does not already exist, it is created; otherwise, the properties of the new listener must match the properties of the existing listener.
    For more information, see Listeners for Your Classic Load Balancer in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a listener for your load balancer at port 80 using the HTTP protocol.
    Expected Output:
    This example creates a listener for your load balancer at port 443 using the HTTPS protocol.
    Expected Output:
    
    :example: response = client.create_load_balancer_listeners(
        LoadBalancerName='string',
        Listeners=[
            {
                'Protocol': 'string',
                'LoadBalancerPort': 123,
                'InstanceProtocol': 'string',
                'InstancePort': 123,
                'SSLCertificateId': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type Listeners: list
    :param Listeners: [REQUIRED]
            The listeners.
            (dict) --Information about a listener.
            For information about the protocols and the ports supported by Elastic Load Balancing, see Listeners for Your Classic Load Balancer in the Classic Load Balancer Guide .
            Protocol (string) -- [REQUIRED]The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
            LoadBalancerPort (integer) -- [REQUIRED]The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
            InstanceProtocol (string) --The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
            If the front-end protocol is HTTP, HTTPS, TCP, or SSL, InstanceProtocol must be at the same protocol.
            If there is another listener with the same InstancePort whose InstanceProtocol is secure, (HTTPS or SSL), the listener's InstanceProtocol must also be secure.
            If there is another listener with the same InstancePort whose InstanceProtocol is HTTP or TCP, the listener's InstanceProtocol must be HTTP or TCP.
            InstancePort (integer) -- [REQUIRED]The port on which the instance is listening.
            SSLCertificateId (string) --The Amazon Resource Name (ARN) of the server certificate.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_load_balancer_policy(LoadBalancerName=None, PolicyName=None, PolicyTypeName=None, PolicyAttributes=None):
    """
    Creates a policy with the specified attributes for the specified load balancer.
    Policies are settings that are saved for your load balancer and that can be applied to the listener or the application server, depending on the policy type.
    See also: AWS API Documentation
    
    Examples
    This example creates a policy that enables Proxy Protocol on the specified load balancer.
    Expected Output:
    This example creates a public key policy.
    Expected Output:
    This example creates a backend server authentication policy that enables authentication on your backend instance using a public key policy.
    Expected Output:
    
    :example: response = client.create_load_balancer_policy(
        LoadBalancerName='string',
        PolicyName='string',
        PolicyTypeName='string',
        PolicyAttributes=[
            {
                'AttributeName': 'string',
                'AttributeValue': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the load balancer policy to be created. This name must be unique within the set of policies for this load balancer.
            

    :type PolicyTypeName: string
    :param PolicyTypeName: [REQUIRED]
            The name of the base policy type. To get the list of policy types, use DescribeLoadBalancerPolicyTypes .
            

    :type PolicyAttributes: list
    :param PolicyAttributes: The policy attributes.
            (dict) --Information about a policy attribute.
            AttributeName (string) --The name of the attribute.
            AttributeValue (string) --The value of the attribute.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_load_balancer(LoadBalancerName=None):
    """
    Deletes the specified load balancer.
    If you are attempting to recreate a load balancer, you must reconfigure all settings. The DNS name associated with a deleted load balancer are no longer usable. The name and associated DNS record of the deleted load balancer no longer exist and traffic sent to any of its IP addresses is no longer delivered to your instances.
    If the load balancer does not exist or has already been deleted, the call to DeleteLoadBalancer still succeeds.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified load balancer.
    Expected Output:
    
    :example: response = client.delete_load_balancer(
        LoadBalancerName='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_load_balancer_listeners(LoadBalancerName=None, LoadBalancerPorts=None):
    """
    Deletes the specified listeners from the specified load balancer.
    See also: AWS API Documentation
    
    Examples
    This example deletes the listener for the specified port from the specified load balancer.
    Expected Output:
    
    :example: response = client.delete_load_balancer_listeners(
        LoadBalancerName='string',
        LoadBalancerPorts=[
            123,
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type LoadBalancerPorts: list
    :param LoadBalancerPorts: [REQUIRED]
            The client port numbers of the listeners.
            (integer) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_load_balancer_policy(LoadBalancerName=None, PolicyName=None):
    """
    Deletes the specified policy from the specified load balancer. This policy must not be enabled for any listeners.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified policy from the specified load balancer. The policy must not be enabled on any listener.
    Expected Output:
    
    :example: response = client.delete_load_balancer_policy(
        LoadBalancerName='string',
        PolicyName='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def deregister_instances_from_load_balancer(LoadBalancerName=None, Instances=None):
    """
    Deregisters the specified instances from the specified load balancer. After the instance is deregistered, it no longer receives traffic from the load balancer.
    You can use  DescribeLoadBalancers to verify that the instance is deregistered from the load balancer.
    For more information, see Register or De-Register EC2 Instances in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example deregisters the specified instance from the specified load balancer.
    Expected Output:
    
    :example: response = client.deregister_instances_from_load_balancer(
        LoadBalancerName='string',
        Instances=[
            {
                'InstanceId': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type Instances: list
    :param Instances: [REQUIRED]
            The IDs of the instances.
            (dict) --The ID of an EC2 instance.
            InstanceId (string) --The instance ID.
            
            

    :rtype: dict
    :return: {
        'Instances': [
            {
                'InstanceId': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_account_limits(Marker=None, PageSize=None):
    """
    Describes the current Elastic Load Balancing resource limits for your AWS account.
    For more information, see Limits for Your Classic Load Balancer in the Classic Load Balancer Guide .
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
    classic-listeners
    classic-load-balancers
    
    """
    pass

def describe_instance_health(LoadBalancerName=None, Instances=None):
    """
    Describes the state of the specified instances with respect to the specified load balancer. If no instances are specified, the call describes the state of all instances that are currently registered with the load balancer. If instances are specified, their state is returned even if they are no longer registered with the load balancer. The state of terminated instances is not returned.
    See also: AWS API Documentation
    
    Examples
    This example describes the health of the instances for the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_instance_health(
        LoadBalancerName='string',
        Instances=[
            {
                'InstanceId': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type Instances: list
    :param Instances: The IDs of the instances.
            (dict) --The ID of an EC2 instance.
            InstanceId (string) --The instance ID.
            
            

    :rtype: dict
    :return: {
        'InstanceStates': [
            {
                'InstanceId': 'string',
                'State': 'string',
                'ReasonCode': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    :returns: 
    N/A
    A transient error occurred. Please try again later.
    Instance has failed at least the UnhealthyThreshold number of health checks consecutively.
    Instance has not passed the configured HealthyThreshold number of health checks consecutively.
    Instance registration is still in progress.
    Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to.
    Instance is not currently registered with the LoadBalancer.
    Instance deregistration currently in progress.
    Disable Availability Zone is currently in progress.
    Instance is in pending state.
    Instance is in stopped state.
    Instance is in terminated state.
    
    """
    pass

def describe_load_balancer_attributes(LoadBalancerName=None):
    """
    Describes the attributes for the specified load balancer.
    See also: AWS API Documentation
    
    Examples
    This example describes the attributes of the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_load_balancer_attributes(
        LoadBalancerName='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_load_balancer_policies(LoadBalancerName=None, PolicyNames=None):
    """
    Describes the specified policies.
    If you specify a load balancer name, the action returns the descriptions of all policies created for the load balancer. If you specify a policy name associated with your load balancer, the action returns the description of that policy. If you don't specify a load balancer name, the action returns descriptions of the specified sample policies, or descriptions of all sample policies. The names of the sample policies have the ELBSample- prefix.
    See also: AWS API Documentation
    
    Examples
    This example describes the specified policy associated with the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_load_balancer_policies(
        LoadBalancerName='string',
        PolicyNames=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: The name of the load balancer.

    :type PolicyNames: list
    :param PolicyNames: The names of the policies.
            (string) --
            

    :rtype: dict
    :return: {
        'PolicyDescriptions': [
            {
                'PolicyName': 'string',
                'PolicyTypeName': 'string',
                'PolicyAttributeDescriptions': [
                    {
                        'AttributeName': 'string',
                        'AttributeValue': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_load_balancer_policy_types(PolicyTypeNames=None):
    """
    Describes the specified load balancer policy types or all load balancer policy types.
    The description of each type indicates how it can be used. For example, some policies can be used only with layer 7 listeners, some policies can be used only with layer 4 listeners, and some policies can be used only with your EC2 instances.
    You can use  CreateLoadBalancerPolicy to create a policy configuration for any of these policy types. Then, depending on the policy type, use either  SetLoadBalancerPoliciesOfListener or  SetLoadBalancerPoliciesForBackendServer to set the policy.
    See also: AWS API Documentation
    
    Examples
    This example describes the specified load balancer policy type.
    Expected Output:
    
    :example: response = client.describe_load_balancer_policy_types(
        PolicyTypeNames=[
            'string',
        ]
    )
    
    
    :type PolicyTypeNames: list
    :param PolicyTypeNames: The names of the policy types. If no names are specified, describes all policy types defined by Elastic Load Balancing.
            (string) --
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
    ONE(1) : Single value required
    ZERO_OR_ONE(0..1) : Up to one value is allowed
    ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed
    ONE_OR_MORE(1..*0) : Required. Multiple values are allowed
    
    """
    pass

def describe_load_balancers(LoadBalancerNames=None, Marker=None, PageSize=None):
    """
    Describes the specified the load balancers. If no load balancers are specified, the call describes all of your load balancers.
    See also: AWS API Documentation
    
    Examples
    This example describes the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_load_balancers(
        LoadBalancerNames=[
            'string',
        ],
        Marker='string',
        PageSize=123
    )
    
    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: The names of the load balancers.
            (string) --
            

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type PageSize: integer
    :param PageSize: The maximum number of results to return with this call (a number from 1 to 400). The default is 400.

    :rtype: dict
    :return: {
        'LoadBalancerDescriptions': [
            {
                'LoadBalancerName': 'string',
                'DNSName': 'string',
                'CanonicalHostedZoneName': 'string',
                'CanonicalHostedZoneNameID': 'string',
                'ListenerDescriptions': [
                    {
                        'Listener': {
                            'Protocol': 'string',
                            'LoadBalancerPort': 123,
                            'InstanceProtocol': 'string',
                            'InstancePort': 123,
                            'SSLCertificateId': 'string'
                        },
                        'PolicyNames': [
                            'string',
                        ]
                    },
                ],
                'Policies': {
                    'AppCookieStickinessPolicies': [
                        {
                            'PolicyName': 'string',
                            'CookieName': 'string'
                        },
                    ],
                    'LBCookieStickinessPolicies': [
                        {
                            'PolicyName': 'string',
                            'CookieExpirationPeriod': 123
                        },
                    ],
                    'OtherPolicies': [
                        'string',
                    ]
                },
                'BackendServerDescriptions': [
                    {
                        'InstancePort': 123,
                        'PolicyNames': [
                            'string',
                        ]
                    },
                ],
                'AvailabilityZones': [
                    'string',
                ],
                'Subnets': [
                    'string',
                ],
                'VPCId': 'string',
                'Instances': [
                    {
                        'InstanceId': 'string'
                    },
                ],
                'HealthCheck': {
                    'Target': 'string',
                    'Interval': 123,
                    'Timeout': 123,
                    'UnhealthyThreshold': 123,
                    'HealthyThreshold': 123
                },
                'SourceSecurityGroup': {
                    'OwnerAlias': 'string',
                    'GroupName': 'string'
                },
                'SecurityGroups': [
                    'string',
                ],
                'CreatedTime': datetime(2015, 1, 1),
                'Scheme': 'string'
            },
        ],
        'NextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_tags(LoadBalancerNames=None):
    """
    Describes the tags associated with the specified load balancers.
    See also: AWS API Documentation
    
    Examples
    This example describes the tags for the specified load balancer.
    Expected Output:
    
    :example: response = client.describe_tags(
        LoadBalancerNames=[
            'string',
        ]
    )
    
    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]
            The names of the load balancers.
            (string) --
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def detach_load_balancer_from_subnets(LoadBalancerName=None, Subnets=None):
    """
    Removes the specified subnets from the set of configured subnets for the load balancer.
    After a subnet is removed, all EC2 instances registered with the load balancer in the removed subnet go into the OutOfService state. Then, the load balancer balances the traffic among the remaining routable subnets.
    See also: AWS API Documentation
    
    Examples
    This example detaches the specified load balancer from the specified subnet.
    Expected Output:
    
    :example: response = client.detach_load_balancer_from_subnets(
        LoadBalancerName='string',
        Subnets=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type Subnets: list
    :param Subnets: [REQUIRED]
            The IDs of the subnets.
            (string) --
            

    :rtype: dict
    :return: {
        'Subnets': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def disable_availability_zones_for_load_balancer(LoadBalancerName=None, AvailabilityZones=None):
    """
    Removes the specified Availability Zones from the set of Availability Zones for the specified load balancer.
    There must be at least one Availability Zone registered with a load balancer at all times. After an Availability Zone is removed, all instances registered with the load balancer that are in the removed Availability Zone go into the OutOfService state. Then, the load balancer attempts to equally balance the traffic among its remaining Availability Zones.
    For more information, see Add or Remove Availability Zones in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example removes the specified Availability Zone from the set of Availability Zones for the specified load balancer.
    Expected Output:
    
    :example: response = client.disable_availability_zones_for_load_balancer(
        LoadBalancerName='string',
        AvailabilityZones=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type AvailabilityZones: list
    :param AvailabilityZones: [REQUIRED]
            The Availability Zones.
            (string) --
            

    :rtype: dict
    :return: {
        'AvailabilityZones': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def enable_availability_zones_for_load_balancer(LoadBalancerName=None, AvailabilityZones=None):
    """
    Adds the specified Availability Zones to the set of Availability Zones for the specified load balancer.
    The load balancer evenly distributes requests across all its registered Availability Zones that contain instances.
    For more information, see Add or Remove Availability Zones in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example adds the specified Availability Zone to the specified load balancer.
    Expected Output:
    
    :example: response = client.enable_availability_zones_for_load_balancer(
        LoadBalancerName='string',
        AvailabilityZones=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type AvailabilityZones: list
    :param AvailabilityZones: [REQUIRED]
            The Availability Zones. These must be in the same region as the load balancer.
            (string) --
            

    :rtype: dict
    :return: {
        'AvailabilityZones': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
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

def modify_load_balancer_attributes(LoadBalancerName=None, LoadBalancerAttributes=None):
    """
    Modifies the attributes of the specified load balancer.
    You can modify the load balancer attributes, such as AccessLogs , ConnectionDraining , and CrossZoneLoadBalancing by either enabling or disabling them. Or, you can modify the load balancer attribute ConnectionSettings by specifying an idle connection timeout value for your load balancer.
    For more information, see the following in the Classic Load Balancer Guide :
    See also: AWS API Documentation
    
    Examples
    This example enables cross-zone load balancing for the specified load balancer.
    Expected Output:
    This example enables connection draining for the specified load balancer.
    Expected Output:
    
    :example: response = client.modify_load_balancer_attributes(
        LoadBalancerName='string',
        LoadBalancerAttributes={
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
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type LoadBalancerAttributes: dict
    :param LoadBalancerAttributes: [REQUIRED]
            The attributes for the load balancer.
            CrossZoneLoadBalancing (dict) --If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
            For more information, see Configure Cross-Zone Load Balancing in the Classic Load Balancer Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether cross-zone load balancing is enabled for the load balancer.
            AccessLog (dict) --If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
            For more information, see Enable Access Logs in the Classic Load Balancer Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether access logs are enabled for the load balancer.
            S3BucketName (string) --The name of the Amazon S3 bucket where the access logs are stored.
            EmitInterval (integer) --The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
            Default: 60 minutes
            S3BucketPrefix (string) --The logical hierarchy you created for your Amazon S3 bucket, for example my-bucket-prefix/prod . If the prefix is not provided, the log is placed at the root level of the bucket.
            ConnectionDraining (dict) --If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
            For more information, see Configure Connection Draining in the Classic Load Balancer Guide .
            Enabled (boolean) -- [REQUIRED]Specifies whether connection draining is enabled for the load balancer.
            Timeout (integer) --The maximum time, in seconds, to keep the existing connections open before deregistering the instances.
            ConnectionSettings (dict) --If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
            By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see Configure Idle Connection Timeout in the Classic Load Balancer Guide .
            IdleTimeout (integer) -- [REQUIRED]The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.
            AdditionalAttributes (list) --This parameter is reserved.
            (dict) --This data type is reserved.
            Key (string) --This parameter is reserved.
            Value (string) --This parameter is reserved.
            
            

    :rtype: dict
    :return: {
        'LoadBalancerName': 'string',
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
    
    
    :returns: 
    LoadBalancerName (string) -- [REQUIRED]
    The name of the load balancer.
    
    LoadBalancerAttributes (dict) -- [REQUIRED]
    The attributes for the load balancer.
    
    CrossZoneLoadBalancing (dict) --If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
    For more information, see Configure Cross-Zone Load Balancing in the Classic Load Balancer Guide .
    
    Enabled (boolean) -- [REQUIRED]Specifies whether cross-zone load balancing is enabled for the load balancer.
    
    
    
    AccessLog (dict) --If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
    For more information, see Enable Access Logs in the Classic Load Balancer Guide .
    
    Enabled (boolean) -- [REQUIRED]Specifies whether access logs are enabled for the load balancer.
    
    S3BucketName (string) --The name of the Amazon S3 bucket where the access logs are stored.
    
    EmitInterval (integer) --The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
    Default: 60 minutes
    
    S3BucketPrefix (string) --The logical hierarchy you created for your Amazon S3 bucket, for example my-bucket-prefix/prod . If the prefix is not provided, the log is placed at the root level of the bucket.
    
    
    
    ConnectionDraining (dict) --If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
    For more information, see Configure Connection Draining in the Classic Load Balancer Guide .
    
    Enabled (boolean) -- [REQUIRED]Specifies whether connection draining is enabled for the load balancer.
    
    Timeout (integer) --The maximum time, in seconds, to keep the existing connections open before deregistering the instances.
    
    
    
    ConnectionSettings (dict) --If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
    By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see Configure Idle Connection Timeout in the Classic Load Balancer Guide .
    
    IdleTimeout (integer) -- [REQUIRED]The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.
    
    
    
    AdditionalAttributes (list) --This parameter is reserved.
    
    (dict) --This data type is reserved.
    
    Key (string) --This parameter is reserved.
    
    Value (string) --This parameter is reserved.
    
    
    
    
    
    
    
    
    """
    pass

def register_instances_with_load_balancer(LoadBalancerName=None, Instances=None):
    """
    Adds the specified instances to the specified load balancer.
    The instance must be a running instance in the same network as the load balancer (EC2-Classic or the same VPC). If you have EC2-Classic instances and a load balancer in a VPC with ClassicLink enabled, you can link the EC2-Classic instances to that VPC and then register the linked EC2-Classic instances with the load balancer in the VPC.
    Note that RegisterInstanceWithLoadBalancer completes when the request has been registered. Instance registration takes a little time to complete. To check the state of the registered instances, use  DescribeLoadBalancers or  DescribeInstanceHealth .
    After the instance is registered, it starts receiving traffic and requests from the load balancer. Any instance that is not in one of the Availability Zones registered for the load balancer is moved to the OutOfService state. If an Availability Zone is added to the load balancer later, any instances registered with the load balancer move to the InService state.
    To deregister instances from a load balancer, use  DeregisterInstancesFromLoadBalancer .
    For more information, see Register or De-Register EC2 Instances in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example registers the specified instance with the specified load balancer.
    Expected Output:
    
    :example: response = client.register_instances_with_load_balancer(
        LoadBalancerName='string',
        Instances=[
            {
                'InstanceId': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type Instances: list
    :param Instances: [REQUIRED]
            The IDs of the instances.
            (dict) --The ID of an EC2 instance.
            InstanceId (string) --The instance ID.
            
            

    :rtype: dict
    :return: {
        'Instances': [
            {
                'InstanceId': 'string'
            },
        ]
    }
    
    
    """
    pass

def remove_tags(LoadBalancerNames=None, Tags=None):
    """
    Removes one or more tags from the specified load balancer.
    See also: AWS API Documentation
    
    Examples
    This example removes the specified tag from the specified load balancer.
    Expected Output:
    
    :example: response = client.remove_tags(
        LoadBalancerNames=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string'
            },
        ]
    )
    
    
    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]
            The name of the load balancer. You can specify a maximum of one load balancer name.
            (string) --
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The list of tag keys to remove.
            (dict) --The key of a tag.
            Key (string) --The name of the key.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def set_load_balancer_listener_ssl_certificate(LoadBalancerName=None, LoadBalancerPort=None, SSLCertificateId=None):
    """
    Sets the certificate that terminates the specified listener's SSL connections. The specified certificate replaces any prior certificate that was used on the same load balancer and port.
    For more information about updating your SSL certificate, see Replace the SSL Certificate for Your Load Balancer in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example replaces the existing SSL certificate for the specified HTTPS listener.
    Expected Output:
    
    :example: response = client.set_load_balancer_listener_ssl_certificate(
        LoadBalancerName='string',
        LoadBalancerPort=123,
        SSLCertificateId='string'
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type LoadBalancerPort: integer
    :param LoadBalancerPort: [REQUIRED]
            The port that uses the specified SSL certificate.
            

    :type SSLCertificateId: string
    :param SSLCertificateId: [REQUIRED]
            The Amazon Resource Name (ARN) of the SSL certificate.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def set_load_balancer_policies_for_backend_server(LoadBalancerName=None, InstancePort=None, PolicyNames=None):
    """
    Replaces the set of policies associated with the specified port on which the EC2 instance is listening with a new set of policies. At this time, only the back-end server authentication policy type can be applied to the instance ports; this policy type is composed of multiple public key policies.
    Each time you use SetLoadBalancerPoliciesForBackendServer to enable the policies, use the PolicyNames parameter to list the policies that you want to enable.
    You can use  DescribeLoadBalancers or  DescribeLoadBalancerPolicies to verify that the policy is associated with the EC2 instance.
    For more information about enabling back-end instance authentication, see Configure Back-end Instance Authentication in the Classic Load Balancer Guide . For more information about Proxy Protocol, see Configure Proxy Protocol Support in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example replaces the policies that are currently associated with the specified port.
    Expected Output:
    
    :example: response = client.set_load_balancer_policies_for_backend_server(
        LoadBalancerName='string',
        InstancePort=123,
        PolicyNames=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type InstancePort: integer
    :param InstancePort: [REQUIRED]
            The port number associated with the EC2 instance.
            

    :type PolicyNames: list
    :param PolicyNames: [REQUIRED]
            The names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def set_load_balancer_policies_of_listener(LoadBalancerName=None, LoadBalancerPort=None, PolicyNames=None):
    """
    Replaces the current set of policies for the specified load balancer port with the specified set of policies.
    To enable back-end server authentication, use  SetLoadBalancerPoliciesForBackendServer .
    For more information about setting policies, see Update the SSL Negotiation Configuration , Duration-Based Session Stickiness , and Application-Controlled Session Stickiness in the Classic Load Balancer Guide .
    See also: AWS API Documentation
    
    Examples
    This example replaces the policies that are currently associated with the specified listener.
    Expected Output:
    
    :example: response = client.set_load_balancer_policies_of_listener(
        LoadBalancerName='string',
        LoadBalancerPort=123,
        PolicyNames=[
            'string',
        ]
    )
    
    
    :type LoadBalancerName: string
    :param LoadBalancerName: [REQUIRED]
            The name of the load balancer.
            

    :type LoadBalancerPort: integer
    :param LoadBalancerPort: [REQUIRED]
            The external port of the load balancer.
            

    :type PolicyNames: list
    :param PolicyNames: [REQUIRED]
            The names of the policies. This list must include all policies to be enabled. If you omit a policy that is currently enabled, it is disabled. If the list is empty, all current policies are disabled.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

