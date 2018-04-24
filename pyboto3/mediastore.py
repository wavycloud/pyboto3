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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def create_container(ContainerName=None):
    """
    Creates a storage container to hold objects. A container is similar to a bucket in the Amazon S3 service.
    See also: AWS API Documentation
    
    
    :example: response = client.create_container(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]
            The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named movies in every region, as long as you don t have an existing container with that name.
            

    :rtype: dict
    :return: {
        'Container': {
            'Endpoint': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'ARN': 'string',
            'Name': 'string',
            'Status': 'ACTIVE'|'CREATING'|'DELETING'
        }
    }
    
    
    """
    pass

def delete_container(ContainerName=None):
    """
    Deletes the specified container. Before you make a DeleteContainer request, delete any objects in the container or in any folders in the container. You can delete only empty containers.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_container(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]
            The name of the container to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_container_policy(ContainerName=None):
    """
    Deletes the access policy that is associated with the specified container.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_container_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]
            The name of the container that holds the policy.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_cors_policy(ContainerName=None):
    """
    Deletes the cross-origin resource sharing (CORS) configuration information that is set for the container.
    To use this operation, you must have permission to perform the MediaStore:DeleteCorsPolicy action. The container owner has this permission by default and can grant this permission to others.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cors_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]
            The name of the container to remove the policy from.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_container(ContainerName=None):
    """
    Retrieves the properties of the requested container. This request is commonly used to retrieve the endpoint of a container. An endpoint is a value assigned by the service when a new container is created. A container's endpoint does not change after it has been assigned. The DescribeContainer request returns a single Container object based on ContainerName . To return all Container objects that are associated with a specified AWS account, use  ListContainers .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_container(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: The name of the container to query.

    :rtype: dict
    :return: {
        'Container': {
            'Endpoint': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'ARN': 'string',
            'Name': 'string',
            'Status': 'ACTIVE'|'CREATING'|'DELETING'
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

def get_container_policy(ContainerName=None):
    """
    Retrieves the access policy for the specified container. For information about the data that is included in an access policy, see the AWS Identity and Access Management User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_container_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]
            The name of the container.
            

    :rtype: dict
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
    
    
    :example: response = client.get_cors_policy(
        ContainerName='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]
            The name of the container that the policy is assigned to.
            

    :rtype: dict
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

def list_containers(NextToken=None, MaxResults=None):
    """
    Lists the properties of all containers in AWS Elemental MediaStore.
    You can query to receive all the containers in one response. Or you can include the MaxResults parameter to receive a limited number of containers in each response. In this case, the response includes a token. To get the next set of containers, send the command again, this time with the NextToken parameter (with the returned token as its value). The next set of responses appears, with a token if there are still more containers to receive.
    See also  DescribeContainer , which gets the properties of one container.
    See also: AWS API Documentation
    
    
    :example: response = client.list_containers(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Only if you used MaxResults in the first command, enter the token (which was included in the previous response) to obtain the next set of containers. This token is included in a response only if there actually are more containers to list.

    :type MaxResults: integer
    :param MaxResults: Enter the maximum number of containers in the response. Use from 1 to 255 characters.

    :rtype: dict
    :return: {
        'Containers': [
            {
                'Endpoint': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'ARN': 'string',
                'Name': 'string',
                'Status': 'ACTIVE'|'CREATING'|'DELETING'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def put_container_policy(ContainerName=None, Policy=None):
    """
    Creates an access policy for the specified container to restrict the users and clients that can access it. For information about the data that is included in an access policy, see the AWS Identity and Access Management User Guide .
    For this release of the REST API, you can create only one policy for a container. If you enter PutContainerPolicy twice, the second command modifies the existing policy.
    See also: AWS API Documentation
    
    
    :example: response = client.put_container_policy(
        ContainerName='string',
        Policy='string'
    )
    
    
    :type ContainerName: string
    :param ContainerName: [REQUIRED]
            The name of the container.
            

    :type Policy: string
    :param Policy: [REQUIRED]
            The contents of the policy, which includes the following:
            One Version tag
            One Statement tag that contains the standard tags for the policy.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_cors_policy(ContainerName=None, CorsPolicy=None):
    """
    Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests. For example, you might want to enable a request whose origin is http://www.example.com to access your AWS Elemental MediaStore container at my.example.container.com by using the browser's XMLHttpRequest capability.
    To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.
    See also: AWS API Documentation
    
    
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
    :param ContainerName: [REQUIRED]
            The name of the container that you want to assign the CORS policy to.
            

    :type CorsPolicy: list
    :param CorsPolicy: [REQUIRED]
            The CORS policy to apply to the container.
            (dict) --A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.
            AllowedOrigins (list) --One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
            Each CORS rule must have at least one AllowedOrigin element. The string value can include only one wildcard character (*), for example, http://*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.
            (string) --
            AllowedMethods (list) --Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.
            Each CORS rule must contain at least one AllowedMethod and one AllowedOrigin element.
            (string) --
            AllowedHeaders (list) --Specifies which headers are allowed in a preflight OPTIONS request through the Access-Control-Request-Headers header. Each header name that is specified in Access-Control-Request-Headers must have a corresponding entry in the rule. Only the headers that were requested are sent back.
            This element can contain only one wildcard character (*).
            (string) --
            MaxAgeSeconds (integer) --The time in seconds that your browser caches the preflight response for the specified resource.
            A CORS rule can have only one MaxAgeSeconds element.
            ExposeHeaders (list) --One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
            This element is optional for each rule.
            (string) --
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

