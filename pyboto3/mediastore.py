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

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_container(ContainerName=None, Tags=None):
    """
    Creates a storage container to hold objects. A container is similar to a bucket in the Amazon S3 service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_container(
        ContainerName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named movies in every region, as long as you don\xe2\x80\x99t have an existing container with that name.\n

    :type Tags: list
    :param Tags: An array of key:value pairs that you define. These values can be anything that you want. Typically, the tag key represents a category (such as 'environment') and the tag value represents a specific value within that category (such as 'test,' 'development,' or 'production'). You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see Tagging Resources in MediaStore .\n\n(dict) --A collection of tags associated with a container. Each tag consists of a key:value pair, which can be anything you define. Typically, the tag key represents a category (such as 'environment') and the tag value represents a specific value within that category (such as 'test,' 'development,' or 'production'). You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see Tagging Resources in MediaStore .\n\nKey (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as 'customer.' Tag keys are case-sensitive.\n\nValue (string) --Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as 'companyA' or 'companyB.' Tag values are case-sensitive.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Container': {
        'Endpoint': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'ARN': 'string',
        'Name': 'string',
        'Status': 'ACTIVE'|'CREATING'|'DELETING',
        'AccessLoggingEnabled': True|False
    }
}


Response Structure

(dict) --

Container (dict) --
ContainerARN: The Amazon Resource Name (ARN) of the newly created container. The ARN has the following format: arn:aws:<region>:<account that owns this container>:container/<name of container>. For example: arn:aws:mediastore:us-west-2:111122223333:container/movies
ContainerName: The container name as specified in the request.
CreationTime: Unix time stamp.
Status: The status of container creation or deletion. The status is one of the following: CREATING , ACTIVE , or DELETING . While the service is creating the container, the status is CREATING . When an endpoint is available, the status changes to ACTIVE .
The return value does not include the container\'s endpoint. To make downstream requests, you must obtain this value by using  DescribeContainer or  ListContainers .

Endpoint (string) --
The DNS endpoint of the container. Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.

CreationTime (datetime) --
Unix timestamp.

ARN (string) --
The Amazon Resource Name (ARN) of the container. The ARN has the following format:
arn:aws:<region>:<account that owns this container>:container/<name of container>
For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

Name (string) --
The name of the container.

Status (string) --
The status of container creation or deletion. The status is one of the following: CREATING , ACTIVE , or DELETING . While the service is creating the container, the status is CREATING . When the endpoint is available, the status changes to ACTIVE .

AccessLoggingEnabled (boolean) --
The state of access logging on the container. This value is false by default, indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch Logs. When you enable access logging on the container, MediaStore changes this value to true , indicating that the service delivers access logs for objects stored in that container to CloudWatch Logs.









Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.LimitExceededException
MediaStore.Client.exceptions.InternalServerError


    :return: {
        'Container': {
            'Endpoint': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'ARN': 'string',
            'Name': 'string',
            'Status': 'ACTIVE'|'CREATING'|'DELETING',
            'AccessLoggingEnabled': True|False
        }
    }
    
    
    :returns: 
    MediaStore.Client.exceptions.ContainerInUseException
    MediaStore.Client.exceptions.LimitExceededException
    MediaStore.Client.exceptions.InternalServerError
    
    """
    pass

def delete_container(ContainerName=None):
    """
    Deletes the specified container. Before you make a DeleteContainer request, delete any objects in the container or in any folders in the container. You can delete only empty containers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_container(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    MediaStore.Client.exceptions.ContainerInUseException
    MediaStore.Client.exceptions.ContainerNotFoundException
    MediaStore.Client.exceptions.InternalServerError
    
    """
    pass

def delete_container_policy(ContainerName=None):
    """
    Deletes the access policy that is associated with the specified container.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_container_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that holds the policy.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.PolicyNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    MediaStore.Client.exceptions.ContainerInUseException
    MediaStore.Client.exceptions.ContainerNotFoundException
    MediaStore.Client.exceptions.PolicyNotFoundException
    MediaStore.Client.exceptions.InternalServerError
    
    """
    pass

def delete_cors_policy(ContainerName=None):
    """
    Deletes the cross-origin resource sharing (CORS) configuration information that is set for the container.
    To use this operation, you must have permission to perform the MediaStore:DeleteCorsPolicy action. The container owner has this permission by default and can grant this permission to others.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cors_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container to remove the policy from.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.CorsPolicyNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    MediaStore.Client.exceptions.ContainerInUseException
    MediaStore.Client.exceptions.ContainerNotFoundException
    MediaStore.Client.exceptions.CorsPolicyNotFoundException
    MediaStore.Client.exceptions.InternalServerError
    
    """
    pass

def delete_lifecycle_policy(ContainerName=None):
    """
    Removes an object lifecycle policy from a container. It takes up to 20 minutes for the change to take effect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_lifecycle_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that holds the object lifecycle policy.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.PolicyNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    MediaStore.Client.exceptions.ContainerInUseException
    MediaStore.Client.exceptions.ContainerNotFoundException
    MediaStore.Client.exceptions.PolicyNotFoundException
    MediaStore.Client.exceptions.InternalServerError
    
    """
    pass

def delete_metric_policy(ContainerName=None):
    """
    Deletes the metric policy that is associated with the specified container. If there is no metric policy associated with the container, MediaStore doesn\'t send metrics to CloudWatch.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_metric_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that is associated with the metric policy that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.PolicyNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    MediaStore.Client.exceptions.ContainerInUseException
    MediaStore.Client.exceptions.ContainerNotFoundException
    MediaStore.Client.exceptions.PolicyNotFoundException
    MediaStore.Client.exceptions.InternalServerError
    
    """
    pass

def describe_container(ContainerName=None):
    """
    Retrieves the properties of the requested container. This request is commonly used to retrieve the endpoint of a container. An endpoint is a value assigned by the service when a new container is created. A container\'s endpoint does not change after it has been assigned. The DescribeContainer request returns a single Container object based on ContainerName . To return all Container objects that are associated with a specified AWS account, use  ListContainers .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_container(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: The name of the container to query.

    :rtype: dict
ReturnsResponse Syntax{
    'Container': {
        'Endpoint': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'ARN': 'string',
        'Name': 'string',
        'Status': 'ACTIVE'|'CREATING'|'DELETING',
        'AccessLoggingEnabled': True|False
    }
}


Response Structure

(dict) --
Container (dict) --The name of the queried container.

Endpoint (string) --The DNS endpoint of the container. Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.

CreationTime (datetime) --Unix timestamp.

ARN (string) --The Amazon Resource Name (ARN) of the container. The ARN has the following format:
arn:aws:<region>:<account that owns this container>:container/<name of container>
For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

Name (string) --The name of the container.

Status (string) --The status of container creation or deletion. The status is one of the following: CREATING , ACTIVE , or DELETING . While the service is creating the container, the status is CREATING . When the endpoint is available, the status changes to ACTIVE .

AccessLoggingEnabled (boolean) --The state of access logging on the container. This value is false by default, indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch Logs. When you enable access logging on the container, MediaStore changes this value to true , indicating that the service delivers access logs for objects stored in that container to CloudWatch Logs.








Exceptions

MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {
        'Container': {
            'Endpoint': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'ARN': 'string',
            'Name': 'string',
            'Status': 'ACTIVE'|'CREATING'|'DELETING',
            'AccessLoggingEnabled': True|False
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

def get_container_policy(ContainerName=None):
    """
    Retrieves the access policy for the specified container. For information about the data that is included in an access policy, see the AWS Identity and Access Management User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_container_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Policy': 'string'
}


Response Structure

(dict) --
Policy (string) --The contents of the access policy.






Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.PolicyNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {
        'Policy': 'string'
    }
    
    
    """
    pass

def get_cors_policy(ContainerName=None):
    """
    Returns the cross-origin resource sharing (CORS) configuration information that is set for the container.
    To use this operation, you must have permission to perform the MediaStore:GetCorsPolicy action. By default, the container owner has this permission and can grant it to others.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cors_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that the policy is assigned to.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CorsPolicy': [
        {
            'AllowedOrigins': [
                'string',
            ],
            'AllowedMethods': [
                'PUT'|'GET'|'DELETE'|'HEAD',
            ],
            'AllowedHeaders': [
                'string',
            ],
            'MaxAgeSeconds': 123,
            'ExposeHeaders': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
CorsPolicy (list) --The CORS policy assigned to the container.

(dict) --A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.

AllowedOrigins (list) --One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
Each CORS rule must have at least one AllowedOrigins element. The string value can include only one wildcard character (*), for example, http://*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.

(string) --


AllowedMethods (list) --Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.
Each CORS rule must contain at least one AllowedMethods and one AllowedOrigins element.

(string) --


AllowedHeaders (list) --Specifies which headers are allowed in a preflight OPTIONS request through the Access-Control-Request-Headers header. Each header name that is specified in Access-Control-Request-Headers must have a corresponding entry in the rule. Only the headers that were requested are sent back.
This element can contain only one wildcard character (*).

(string) --


MaxAgeSeconds (integer) --The time in seconds that your browser caches the preflight response for the specified resource.
A CORS rule can have only one MaxAgeSeconds element.

ExposeHeaders (list) --One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
This element is optional for each rule.

(string) --











Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.CorsPolicyNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {
        'CorsPolicy': [
            {
                'AllowedOrigins': [
                    'string',
                ],
                'AllowedMethods': [
                    'PUT'|'GET'|'DELETE'|'HEAD',
                ],
                'AllowedHeaders': [
                    'string',
                ],
                'MaxAgeSeconds': 123,
                'ExposeHeaders': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_lifecycle_policy(ContainerName=None):
    """
    Retrieves the object lifecycle policy that is assigned to a container.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_lifecycle_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that the object lifecycle policy is assigned to.\n

    :rtype: dict
ReturnsResponse Syntax{
    'LifecyclePolicy': 'string'
}


Response Structure

(dict) --
LifecyclePolicy (string) --The object lifecycle policy that is assigned to the container.






Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.PolicyNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {
        'LifecyclePolicy': 'string'
    }
    
    
    """
    pass

def get_metric_policy(ContainerName=None):
    """
    Returns the metric policy for the specified container.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_metric_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that is associated with the metric policy.\n

    :rtype: dict
ReturnsResponse Syntax{
    'MetricPolicy': {
        'ContainerLevelMetrics': 'ENABLED'|'DISABLED',
        'MetricPolicyRules': [
            {
                'ObjectGroup': 'string',
                'ObjectGroupName': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
MetricPolicy (dict) --The metric policy that is associated with the specific container.

ContainerLevelMetrics (string) --A setting to enable or disable metrics at the container level.

MetricPolicyRules (list) --A parameter that holds an array of rules that enable metrics at the object level. This parameter is optional, but if you choose to include it, you must also include at least one rule. By default, you can include up to five rules. You can also request a quota increase to allow up to 300 rules per policy.

(dict) --A setting that enables metrics at the object level. Each rule contains an object group and an object group name. If the policy includes the MetricPolicyRules parameter, you must include at least one rule. Each metric policy can include up to five rules by default. You can also request a quota increase to allow up to 300 rules per policy.

ObjectGroup (string) --A path or file name that defines which objects to include in the group. Wildcards (*) are acceptable.

ObjectGroupName (string) --A name that allows you to refer to the object group.












Exceptions

MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.PolicyNotFoundException
MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.InternalServerError


    :return: {
        'MetricPolicy': {
            'ContainerLevelMetrics': 'ENABLED'|'DISABLED',
            'MetricPolicyRules': [
                {
                    'ObjectGroup': 'string',
                    'ObjectGroupName': 'string'
                },
            ]
        }
    }
    
    
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

def list_containers(NextToken=None, MaxResults=None):
    """
    Lists the properties of all containers in AWS Elemental MediaStore.
    You can query to receive all the containers in one response. Or you can include the MaxResults parameter to receive a limited number of containers in each response. In this case, the response includes a token. To get the next set of containers, send the command again, this time with the NextToken parameter (with the returned token as its value). The next set of responses appears, with a token if there are still more containers to receive.
    See also  DescribeContainer , which gets the properties of one container.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_containers(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Only if you used MaxResults in the first command, enter the token (which was included in the previous response) to obtain the next set of containers. This token is included in a response only if there actually are more containers to list.

    :type MaxResults: integer
    :param MaxResults: Enter the maximum number of containers in the response. Use from 1 to 255 characters.

    :rtype: dict

ReturnsResponse Syntax
{
    'Containers': [
        {
            'Endpoint': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'ARN': 'string',
            'Name': 'string',
            'Status': 'ACTIVE'|'CREATING'|'DELETING',
            'AccessLoggingEnabled': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Containers (list) --
The names of the containers.

(dict) --
This section describes operations that you can perform on an AWS Elemental MediaStore container.

Endpoint (string) --
The DNS endpoint of the container. Use the endpoint to identify the specific container when sending requests to the data plane. The service assigns this value when the container is created. Once the value has been assigned, it does not change.

CreationTime (datetime) --
Unix timestamp.

ARN (string) --
The Amazon Resource Name (ARN) of the container. The ARN has the following format:
arn:aws:<region>:<account that owns this container>:container/<name of container>
For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

Name (string) --
The name of the container.

Status (string) --
The status of container creation or deletion. The status is one of the following: CREATING , ACTIVE , or DELETING . While the service is creating the container, the status is CREATING . When the endpoint is available, the status changes to ACTIVE .

AccessLoggingEnabled (boolean) --
The state of access logging on the container. This value is false by default, indicating that AWS Elemental MediaStore does not send access logs to Amazon CloudWatch Logs. When you enable access logging on the container, MediaStore changes this value to true , indicating that the service delivers access logs for objects stored in that container to CloudWatch Logs.





NextToken (string) --

NextToken is the token to use in the next call to ListContainers . This token is returned only if you included the MaxResults tag in the original command, and only if there are still containers to return.








Exceptions

MediaStore.Client.exceptions.InternalServerError


    :return: {
        'Containers': [
            {
                'Endpoint': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'ARN': 'string',
                'Name': 'string',
                'Status': 'ACTIVE'|'CREATING'|'DELETING',
                'AccessLoggingEnabled': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    MediaStore.Client.exceptions.InternalServerError
    
    """
    pass

def list_tags_for_resource(Resource=None):
    """
    Returns a list of the tags assigned to the specified container.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        Resource='string'
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]\nThe Amazon Resource Name (ARN) for the container.\n

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
Tags (list) --An array of key:value pairs that are assigned to the container.

(dict) --A collection of tags associated with a container. Each tag consists of a key:value pair, which can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see Tagging Resources in MediaStore .

Key (string) --Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.

Value (string) --Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.










Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.InternalServerError


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

def put_container_policy(ContainerName=None, Policy=None):
    """
    Creates an access policy for the specified container to restrict the users and clients that can access it. For information about the data that is included in an access policy, see the AWS Identity and Access Management User Guide .
    For this release of the REST API, you can create only one policy for a container. If you enter PutContainerPolicy twice, the second command modifies the existing policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_container_policy(
        ContainerName='string',
        Policy='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container.\n

    :type Policy: string
    :param Policy: [REQUIRED]\nThe contents of the policy, which includes the following:\n\nOne Version tag\nOne Statement tag that contains the standard tags for the policy.\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_cors_policy(ContainerName=None, CorsPolicy=None):
    """
    Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests. For example, you might want to enable a request whose origin is http://www.example.com to access your AWS Elemental MediaStore container at my.example.container.com by using the browser\'s XMLHttpRequest capability.
    To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.
    To learn more about CORS, see Cross-Origin Resource Sharing (CORS) in AWS Elemental MediaStore .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_cors_policy(
        ContainerName='string',
        CorsPolicy=[
            {
                'AllowedOrigins': [
                    'string',
                ],
                'AllowedMethods': [
                    'PUT'|'GET'|'DELETE'|'HEAD',
                ],
                'AllowedHeaders': [
                    'string',
                ],
                'MaxAgeSeconds': 123,
                'ExposeHeaders': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that you want to assign the CORS policy to.\n

    :type CorsPolicy: list
    :param CorsPolicy: [REQUIRED]\nThe CORS policy to apply to the container.\n\n(dict) --A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.\n\nAllowedOrigins (list) -- [REQUIRED]One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).\nEach CORS rule must have at least one AllowedOrigins element. The string value can include only one wildcard character (*), for example, http://*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.\n\n(string) --\n\n\nAllowedMethods (list) --Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.\nEach CORS rule must contain at least one AllowedMethods and one AllowedOrigins element.\n\n(string) --\n\n\nAllowedHeaders (list) -- [REQUIRED]Specifies which headers are allowed in a preflight OPTIONS request through the Access-Control-Request-Headers header. Each header name that is specified in Access-Control-Request-Headers must have a corresponding entry in the rule. Only the headers that were requested are sent back.\nThis element can contain only one wildcard character (*).\n\n(string) --\n\n\nMaxAgeSeconds (integer) --The time in seconds that your browser caches the preflight response for the specified resource.\nA CORS rule can have only one MaxAgeSeconds element.\n\nExposeHeaders (list) --One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).\nThis element is optional for each rule.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_lifecycle_policy(ContainerName=None, LifecyclePolicy=None):
    """
    Writes an object lifecycle policy to a container. If the container already has an object lifecycle policy, the service replaces the existing policy with the new policy. It takes up to 20 minutes for the change to take effect.
    For information about how to construct an object lifecycle policy, see Components of an Object Lifecycle Policy .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_lifecycle_policy(
        ContainerName='string',
        LifecyclePolicy='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that you want to assign the object lifecycle policy to.\n

    :type LifecyclePolicy: string
    :param LifecyclePolicy: [REQUIRED]\nThe object lifecycle policy to apply to the container.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_metric_policy(ContainerName=None, MetricPolicy=None):
    """
    The metric policy that you want to add to the container. A metric policy allows AWS Elemental MediaStore to send metrics to Amazon CloudWatch. It takes up to 20 minutes for the new policy to take effect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_metric_policy(
        ContainerName='string',
        MetricPolicy={
            'ContainerLevelMetrics': 'ENABLED'|'DISABLED',
            'MetricPolicyRules': [
                {
                    'ObjectGroup': 'string',
                    'ObjectGroupName': 'string'
                },
            ]
        }
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that you want to add the metric policy to.\n

    :type MetricPolicy: dict
    :param MetricPolicy: [REQUIRED]\nThe metric policy that you want to associate with the container. In the policy, you must indicate whether you want MediaStore to send container-level metrics. You can also include up to five rules to define groups of objects that you want MediaStore to send object-level metrics for. If you include rules in the policy, construct each rule with both of the following:\n\nAn object group that defines which objects to include in the group. The definition can be a path or a file name, but it can\'t have more than 900 characters. Valid characters are: a-z, A-Z, 0-9, _ (underscore), = (equal), : (colon), . (period), - (hyphen), ~ (tilde), / (forward slash), and * (asterisk). Wildcards (*) are acceptable.\nAn object group name that allows you to refer to the object group. The name can\'t have more than 30 characters. Valid characters are: a-z, A-Z, 0-9, and _ (underscore).\n\n\nContainerLevelMetrics (string) -- [REQUIRED]A setting to enable or disable metrics at the container level.\n\nMetricPolicyRules (list) --A parameter that holds an array of rules that enable metrics at the object level. This parameter is optional, but if you choose to include it, you must also include at least one rule. By default, you can include up to five rules. You can also request a quota increase to allow up to 300 rules per policy.\n\n(dict) --A setting that enables metrics at the object level. Each rule contains an object group and an object group name. If the policy includes the MetricPolicyRules parameter, you must include at least one rule. Each metric policy can include up to five rules by default. You can also request a quota increase to allow up to 300 rules per policy.\n\nObjectGroup (string) -- [REQUIRED]A path or file name that defines which objects to include in the group. Wildcards (*) are acceptable.\n\nObjectGroupName (string) -- [REQUIRED]A name that allows you to refer to the object group.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_access_logging(ContainerName=None):
    """
    Starts access logging on the specified container. When you enable access logging on a container, MediaStore delivers access logs for objects stored in that container to Amazon CloudWatch Logs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_access_logging(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that you want to start access logging on.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    MediaStore.Client.exceptions.ContainerInUseException
    MediaStore.Client.exceptions.ContainerNotFoundException
    MediaStore.Client.exceptions.InternalServerError
    
    """
    pass

def stop_access_logging(ContainerName=None):
    """
    Stops access logging on the specified container. When you stop access logging on a container, MediaStore stops sending access logs to Amazon CloudWatch Logs. These access logs are not saved and are not retrievable.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_access_logging(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]\nThe name of the container that you want to stop access logging on.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    MediaStore.Client.exceptions.ContainerInUseException
    MediaStore.Client.exceptions.ContainerNotFoundException
    MediaStore.Client.exceptions.InternalServerError
    
    """
    pass

def tag_resource(Resource=None, Tags=None):
    """
    Adds tags to the specified AWS Elemental MediaStore container. Tags are key:value pairs that you can associate with AWS resources. For example, the tag key might be "customer" and the tag value might be "companyA." You can specify one or more tags to add to each container. You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see Tagging Resources in MediaStore .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        Resource='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]\nThe Amazon Resource Name (ARN) for the container.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nAn array of key:value pairs that you want to add to the container. You need to specify only the tags that you want to add or update. For example, suppose a container already has two tags (customer:CompanyA and priority:High). You want to change the priority tag and also add a third tag (type:Contract). For TagResource, you specify the following tags: priority:Medium, type:Contract. The result is that your container has three tags: customer:CompanyA, priority:Medium, and type:Contract.\n\n(dict) --A collection of tags associated with a container. Each tag consists of a key:value pair, which can be anything you define. Typically, the tag key represents a category (such as 'environment') and the tag value represents a specific value within that category (such as 'test,' 'development,' or 'production'). You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see Tagging Resources in MediaStore .\n\nKey (string) -- [REQUIRED]Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as 'customer.' Tag keys are case-sensitive.\n\nValue (string) --Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as 'companyA' or 'companyB.' Tag values are case-sensitive.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(Resource=None, TagKeys=None):
    """
    Removes tags from the specified container. You can specify one or more tags to remove.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        Resource='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type Resource: string
    :param Resource: [REQUIRED]\nThe Amazon Resource Name (ARN) for the container.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA comma-separated list of keys for tags that you want to remove from the container. For example, if your container has two tags (customer:CompanyA and priority:High) and you want to remove one of the tags (priority:High), you specify the key for the tag that you want to remove (priority).\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MediaStore.Client.exceptions.ContainerInUseException
MediaStore.Client.exceptions.ContainerNotFoundException
MediaStore.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

