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

def create_mesh(clientToken=None, meshName=None, spec=None, tags=None):
    """
    Creates a service mesh.
    A service mesh is a logical boundary for network traffic between services that are represented by resources within the mesh. After you create your service mesh, you can create virtual services, virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.
    For more information about service meshes, see Service meshes .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_mesh(
        clientToken='string',
        meshName='string',
        spec={
            'egressFilter': {
                'type': 'ALLOW_ALL'|'DROP_ALL'
            }
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name to use for the service mesh.\n

    :type spec: dict
    :param spec: The service mesh specification to apply.\n\negressFilter (dict) --The egress filter rules for the service mesh.\n\ntype (string) -- [REQUIRED]The egress filter type. By default, the type is DROP_ALL , which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to *.amazonaws.com for AWS API calls). You can set the egress filter type to ALLOW_ALL to allow egress to any endpoint inside or outside of the service mesh.\n\n\n\n\n

    :type tags: list
    :param tags: Optional metadata that you can apply to the service mesh to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\n(dict) --Optional metadata that you apply to a resource to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nkey (string) -- [REQUIRED]One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nvalue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'mesh': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'egressFilter': {
                'type': 'ALLOW_ALL'|'DROP_ALL'
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        }
    }
}


Response Structure

(dict) --

mesh (dict) --
The full description of your service mesh following the create call.

meshName (string) --
The name of the service mesh.

metadata (dict) --
The associated metadata for the service mesh.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The associated specification for the service mesh.

egressFilter (dict) --
The egress filter rules for the service mesh.

type (string) --
The egress filter type. By default, the type is DROP_ALL , which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to *.amazonaws.com for AWS API calls). You can set the egress filter type to ALLOW_ALL to allow egress to any endpoint inside or outside of the service mesh.





status (dict) --
The status of the service mesh.

status (string) --
The current mesh status.











Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.LimitExceededException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'mesh': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'egressFilter': {
                    'type': 'ALLOW_ALL'|'DROP_ALL'
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            }
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ConflictException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.LimitExceededException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def create_route(clientToken=None, meshName=None, meshOwner=None, routeName=None, spec=None, tags=None, virtualRouterName=None):
    """
    Creates a route that is associated with a virtual router.
    You can route several different protocols and define a retry policy for a route. Traffic can be routed to one or more virtual nodes.
    For more information about routes, see Routes .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_route(
        clientToken='string',
        meshName='string',
        meshOwner='string',
        routeName='string',
        spec={
            'grpcRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'metadata': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'methodName': 'string',
                    'serviceName': 'string'
                },
                'retryPolicy': {
                    'grpcRetryEvents': [
                        'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                    ],
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'http2Route': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'httpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'priority': 123,
            'tcpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                }
            }
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        virtualRouterName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to create the route in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see Working with Shared Meshes .

    :type routeName: string
    :param routeName: [REQUIRED]\nThe name to use for the route.\n

    :type spec: dict
    :param spec: [REQUIRED]\nThe route specification to apply.\n\ngrpcRoute (dict) --An object that represents the specification of a gRPC route.\n\naction (dict) -- [REQUIRED]An object that represents the action to take if a match is determined.\n\nweightedTargets (list) -- [REQUIRED]An object that represents the targets that traffic is routed to when a request matches the route.\n\n(dict) --An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.\n\nvirtualNode (string) -- [REQUIRED]The virtual node to associate with the weighted target.\n\nweight (integer) -- [REQUIRED]The relative weight of the weighted target.\n\n\n\n\n\n\n\nmatch (dict) -- [REQUIRED]An object that represents the criteria for determining a request match.\n\nmetadata (list) --An object that represents the data to match from the request.\n\n(dict) --An object that represents the match metadata for the route.\n\ninvert (boolean) --Specify True to match anything except the match criteria. The default value is False .\n\nmatch (dict) --An object that represents the data to match from the request.\n\nexact (string) --The value sent by the client must match the specified value exactly.\n\nprefix (string) --The value sent by the client must begin with the specified characters.\n\nrange (dict) --An object that represents the range of values to match on.\n\nend (integer) -- [REQUIRED]The end of the range.\n\nstart (integer) -- [REQUIRED]The start of the range.\n\n\n\nregex (string) --The value sent by the client must include the specified characters.\n\nsuffix (string) --The value sent by the client must end with the specified characters.\n\n\n\nname (string) -- [REQUIRED]The name of the route.\n\n\n\n\n\nmethodName (string) --The method name to match from the request. If you specify a name, you must also specify a serviceName .\n\nserviceName (string) --The fully qualified domain name for the service to match from the request.\n\n\n\nretryPolicy (dict) --An object that represents a retry policy.\n\ngrpcRetryEvents (list) --Specify at least one of the valid values.\n\n(string) --\n\n\nhttpRetryEvents (list) --Specify at least one of the following values.\n\nserver-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511\ngateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504\nclient-error \xe2\x80\x93 HTTP status code 409\nstream-error \xe2\x80\x93 Retry on refused stream\n\n\n(string) --\n\n\nmaxRetries (integer) -- [REQUIRED]The maximum number of retry attempts.\n\nperRetryTimeout (dict) -- [REQUIRED]An object that represents a duration of time.\n\nunit (string) --A unit of time.\n\nvalue (integer) --A number of time units.\n\n\n\ntcpRetryEvents (list) --Specify a valid value.\n\n(string) --\n\n\n\n\n\n\nhttp2Route (dict) --An object that represents the specification of an HTTP/2 route.\n\naction (dict) -- [REQUIRED]An object that represents the action to take if a match is determined.\n\nweightedTargets (list) -- [REQUIRED]An object that represents the targets that traffic is routed to when a request matches the route.\n\n(dict) --An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.\n\nvirtualNode (string) -- [REQUIRED]The virtual node to associate with the weighted target.\n\nweight (integer) -- [REQUIRED]The relative weight of the weighted target.\n\n\n\n\n\n\n\nmatch (dict) -- [REQUIRED]An object that represents the criteria for determining a request match.\n\nheaders (list) --An object that represents the client request headers to match on.\n\n(dict) --An object that represents the HTTP header in the request.\n\ninvert (boolean) --Specify True to match anything except the match criteria. The default value is False .\n\nmatch (dict) --The HeaderMatchMethod object.\n\nexact (string) --The value sent by the client must match the specified value exactly.\n\nprefix (string) --The value sent by the client must begin with the specified characters.\n\nrange (dict) --An object that represents the range of values to match on.\n\nend (integer) -- [REQUIRED]The end of the range.\n\nstart (integer) -- [REQUIRED]The start of the range.\n\n\n\nregex (string) --The value sent by the client must include the specified characters.\n\nsuffix (string) --The value sent by the client must end with the specified characters.\n\n\n\nname (string) -- [REQUIRED]A name for the HTTP header in the client request that will be matched on.\n\n\n\n\n\nmethod (string) --The client request method to match on. Specify only one.\n\nprefix (string) -- [REQUIRED]Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .\n\nscheme (string) --The client request scheme to match on. Specify only one.\n\n\n\nretryPolicy (dict) --An object that represents a retry policy.\n\nhttpRetryEvents (list) --Specify at least one of the following values.\n\nserver-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511\ngateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504\nclient-error \xe2\x80\x93 HTTP status code 409\nstream-error \xe2\x80\x93 Retry on refused stream\n\n\n(string) --\n\n\nmaxRetries (integer) -- [REQUIRED]The maximum number of retry attempts.\n\nperRetryTimeout (dict) -- [REQUIRED]An object that represents a duration of time.\n\nunit (string) --A unit of time.\n\nvalue (integer) --A number of time units.\n\n\n\ntcpRetryEvents (list) --Specify a valid value.\n\n(string) --\n\n\n\n\n\n\nhttpRoute (dict) --An object that represents the specification of an HTTP route.\n\naction (dict) -- [REQUIRED]An object that represents the action to take if a match is determined.\n\nweightedTargets (list) -- [REQUIRED]An object that represents the targets that traffic is routed to when a request matches the route.\n\n(dict) --An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.\n\nvirtualNode (string) -- [REQUIRED]The virtual node to associate with the weighted target.\n\nweight (integer) -- [REQUIRED]The relative weight of the weighted target.\n\n\n\n\n\n\n\nmatch (dict) -- [REQUIRED]An object that represents the criteria for determining a request match.\n\nheaders (list) --An object that represents the client request headers to match on.\n\n(dict) --An object that represents the HTTP header in the request.\n\ninvert (boolean) --Specify True to match anything except the match criteria. The default value is False .\n\nmatch (dict) --The HeaderMatchMethod object.\n\nexact (string) --The value sent by the client must match the specified value exactly.\n\nprefix (string) --The value sent by the client must begin with the specified characters.\n\nrange (dict) --An object that represents the range of values to match on.\n\nend (integer) -- [REQUIRED]The end of the range.\n\nstart (integer) -- [REQUIRED]The start of the range.\n\n\n\nregex (string) --The value sent by the client must include the specified characters.\n\nsuffix (string) --The value sent by the client must end with the specified characters.\n\n\n\nname (string) -- [REQUIRED]A name for the HTTP header in the client request that will be matched on.\n\n\n\n\n\nmethod (string) --The client request method to match on. Specify only one.\n\nprefix (string) -- [REQUIRED]Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .\n\nscheme (string) --The client request scheme to match on. Specify only one.\n\n\n\nretryPolicy (dict) --An object that represents a retry policy.\n\nhttpRetryEvents (list) --Specify at least one of the following values.\n\nserver-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511\ngateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504\nclient-error \xe2\x80\x93 HTTP status code 409\nstream-error \xe2\x80\x93 Retry on refused stream\n\n\n(string) --\n\n\nmaxRetries (integer) -- [REQUIRED]The maximum number of retry attempts.\n\nperRetryTimeout (dict) -- [REQUIRED]An object that represents a duration of time.\n\nunit (string) --A unit of time.\n\nvalue (integer) --A number of time units.\n\n\n\ntcpRetryEvents (list) --Specify a valid value.\n\n(string) --\n\n\n\n\n\n\npriority (integer) --The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority.\n\ntcpRoute (dict) --An object that represents the specification of a TCP route.\n\naction (dict) -- [REQUIRED]The action to take if a match is determined.\n\nweightedTargets (list) -- [REQUIRED]An object that represents the targets that traffic is routed to when a request matches the route.\n\n(dict) --An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.\n\nvirtualNode (string) -- [REQUIRED]The virtual node to associate with the weighted target.\n\nweight (integer) -- [REQUIRED]The relative weight of the weighted target.\n\n\n\n\n\n\n\n\n\n\n

    :type tags: list
    :param tags: Optional metadata that you can apply to the route to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\n(dict) --Optional metadata that you apply to a resource to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nkey (string) -- [REQUIRED]One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nvalue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]\nThe name of the virtual router in which to create the route. If the virtual router is in a shared mesh, then you must be the owner of the virtual router resource.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'route': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'routeName': 'string',
        'spec': {
            'grpcRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'metadata': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'methodName': 'string',
                    'serviceName': 'string'
                },
                'retryPolicy': {
                    'grpcRetryEvents': [
                        'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                    ],
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'http2Route': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'httpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'priority': 123,
            'tcpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualRouterName': 'string'
    }
}


Response Structure

(dict) --

route (dict) --
The full description of your mesh following the create call.

meshName (string) --
The name of the service mesh that the route resides in.

metadata (dict) --
The associated metadata for the route.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



routeName (string) --
The name of the route.

spec (dict) --
The specifications of the route.

grpcRoute (dict) --
An object that represents the specification of a gRPC route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

metadata (list) --
An object that represents the data to match from the request.

(dict) --
An object that represents the match metadata for the route.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
An object that represents the data to match from the request.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
The name of the route.





methodName (string) --
The method name to match from the request. If you specify a name, you must also specify a serviceName .

serviceName (string) --
The fully qualified domain name for the service to match from the request.



retryPolicy (dict) --
An object that represents a retry policy.

grpcRetryEvents (list) --
Specify at least one of the valid values.

(string) --


httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






http2Route (dict) --
An object that represents the specification of an HTTP/2 route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

headers (list) --
An object that represents the client request headers to match on.

(dict) --
An object that represents the HTTP header in the request.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
The HeaderMatchMethod object.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
A name for the HTTP header in the client request that will be matched on.





method (string) --
The client request method to match on. Specify only one.

prefix (string) --
Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .

scheme (string) --
The client request scheme to match on. Specify only one.



retryPolicy (dict) --
An object that represents a retry policy.

httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






httpRoute (dict) --
An object that represents the specification of an HTTP route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

headers (list) --
An object that represents the client request headers to match on.

(dict) --
An object that represents the HTTP header in the request.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
The HeaderMatchMethod object.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
A name for the HTTP header in the client request that will be matched on.





method (string) --
The client request method to match on. Specify only one.

prefix (string) --
Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .

scheme (string) --
The client request scheme to match on. Specify only one.



retryPolicy (dict) --
An object that represents a retry policy.

httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






priority (integer) --
The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority.

tcpRoute (dict) --
An object that represents the specification of a TCP route.

action (dict) --
The action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.











status (dict) --
The status of the route.

status (string) --
The current status for the route.



virtualRouterName (string) --
The virtual router that the route is associated with.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.LimitExceededException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'route': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'routeName': 'string',
            'spec': {
                'grpcRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'metadata': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'methodName': 'string',
                        'serviceName': 'string'
                    },
                    'retryPolicy': {
                        'grpcRetryEvents': [
                            'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                        ],
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'http2Route': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'headers': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                        'prefix': 'string',
                        'scheme': 'http'|'https'
                    },
                    'retryPolicy': {
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'httpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'headers': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                        'prefix': 'string',
                        'scheme': 'http'|'https'
                    },
                    'retryPolicy': {
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'priority': 123,
                'tcpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_virtual_node(clientToken=None, meshName=None, meshOwner=None, spec=None, tags=None, virtualNodeName=None):
    """
    Creates a virtual node within a service mesh.
    A virtual node acts as a logical pointer to a particular task group, such as an Amazon ECS service or a Kubernetes deployment. When you create a virtual node, you can specify the service discovery information for your task group, and whether the proxy running in a task group will communicate with other proxies using Transport Layer Security (TLS).
    You define a listener for any inbound traffic that your virtual node expects. Any virtual service that your virtual node expects to communicate to is specified as a backend .
    The response metadata for your new virtual node contains the arn that is associated with the virtual node. Set this value (either the full ARN or the truncated resource name: for example, mesh/default/virtualNode/simpleapp ) as the APPMESH_VIRTUAL_NODE_NAME environment variable for your task group\'s Envoy proxy container in your task definition or pod spec. This is then mapped to the node.id and node.cluster Envoy parameters.
    For more information about virtual nodes, see Virtual nodes .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_virtual_node(
        clientToken='string',
        meshName='string',
        meshOwner='string',
        spec={
            'backendDefaults': {
                'clientPolicy': {
                    'tls': {
                        'enforce': True|False,
                        'ports': [
                            123,
                        ],
                        'validation': {
                            'trust': {
                                'acm': {
                                    'certificateAuthorityArns': [
                                        'string',
                                    ]
                                },
                                'file': {
                                    'certificateChain': 'string'
                                }
                            }
                        }
                    }
                }
            },
            'backends': [
                {
                    'virtualService': {
                        'clientPolicy': {
                            'tls': {
                                'enforce': True|False,
                                'ports': [
                                    123,
                                ],
                                'validation': {
                                    'trust': {
                                        'acm': {
                                            'certificateAuthorityArns': [
                                                'string',
                                            ]
                                        },
                                        'file': {
                                            'certificateChain': 'string'
                                        }
                                    }
                                }
                            }
                        },
                        'virtualServiceName': 'string'
                    }
                },
            ],
            'listeners': [
                {
                    'healthCheck': {
                        'healthyThreshold': 123,
                        'intervalMillis': 123,
                        'path': 'string',
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp',
                        'timeoutMillis': 123,
                        'unhealthyThreshold': 123
                    },
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    },
                    'tls': {
                        'certificate': {
                            'acm': {
                                'certificateArn': 'string'
                            },
                            'file': {
                                'certificateChain': 'string',
                                'privateKey': 'string'
                            }
                        },
                        'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                    }
                },
            ],
            'logging': {
                'accessLog': {
                    'file': {
                        'path': 'string'
                    }
                }
            },
            'serviceDiscovery': {
                'awsCloudMap': {
                    'attributes': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'namespaceName': 'string',
                    'serviceName': 'string'
                },
                'dns': {
                    'hostname': 'string'
                }
            }
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        virtualNodeName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to create the virtual node in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see Working with Shared Meshes .

    :type spec: dict
    :param spec: [REQUIRED]\nThe virtual node specification to apply.\n\nbackendDefaults (dict) --A reference to an object that represents the defaults for backends.\n\nclientPolicy (dict) --A reference to an object that represents a client policy.\n\ntls (dict) --A reference to an object that represents a Transport Layer Security (TLS) client policy.\n\nenforce (boolean) --Whether the policy is enforced. The default is True , if a value isn\'t specified.\n\nports (list) --One or more ports that the policy is enforced for.\n\n(integer) --\n\n\nvalidation (dict) -- [REQUIRED]A reference to an object that represents a TLS validation context.\n\ntrust (dict) -- [REQUIRED]A reference to an object that represents a TLS validation context trust.\n\nacm (dict) --A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.\n\ncertificateAuthorityArns (list) -- [REQUIRED]One or more ACM Amazon Resource Name (ARN)s.\n\n(string) --\n\n\n\n\nfile (dict) --An object that represents a TLS validation context trust for a local file.\n\ncertificateChain (string) -- [REQUIRED]The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.\n\n\n\n\n\n\n\n\n\n\n\n\n\nbackends (list) --The backends that the virtual node is expected to send outbound traffic to.\n\n(dict) --An object that represents the backends that a virtual node is expected to send outbound traffic to.\n\nvirtualService (dict) --Specifies a virtual service to use as a backend for a virtual node.\n\nclientPolicy (dict) --A reference to an object that represents the client policy for a backend.\n\ntls (dict) --A reference to an object that represents a Transport Layer Security (TLS) client policy.\n\nenforce (boolean) --Whether the policy is enforced. The default is True , if a value isn\'t specified.\n\nports (list) --One or more ports that the policy is enforced for.\n\n(integer) --\n\n\nvalidation (dict) -- [REQUIRED]A reference to an object that represents a TLS validation context.\n\ntrust (dict) -- [REQUIRED]A reference to an object that represents a TLS validation context trust.\n\nacm (dict) --A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.\n\ncertificateAuthorityArns (list) -- [REQUIRED]One or more ACM Amazon Resource Name (ARN)s.\n\n(string) --\n\n\n\n\nfile (dict) --An object that represents a TLS validation context trust for a local file.\n\ncertificateChain (string) -- [REQUIRED]The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.\n\n\n\n\n\n\n\n\n\n\n\nvirtualServiceName (string) -- [REQUIRED]The name of the virtual service that is acting as a virtual node backend.\n\n\n\n\n\n\n\nlisteners (list) --The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.\n\n(dict) --An object that represents a listener for a virtual node.\n\nhealthCheck (dict) --The health check information for the listener.\n\nhealthyThreshold (integer) -- [REQUIRED]The number of consecutive successful health checks that must occur before declaring listener healthy.\n\nintervalMillis (integer) -- [REQUIRED]The time period in milliseconds between each health check execution.\n\npath (string) --The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.\n\nport (integer) --The destination port for the health check request. This port must match the port defined in the PortMapping for the listener.\n\nprotocol (string) -- [REQUIRED]The protocol for the health check request. If you specify grpc , then your service must conform to the GRPC Health Checking Protocol .\n\ntimeoutMillis (integer) -- [REQUIRED]The amount of time to wait when receiving a response from the health check, in milliseconds.\n\nunhealthyThreshold (integer) -- [REQUIRED]The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.\n\n\n\nportMapping (dict) -- [REQUIRED]The port mapping information for the listener.\n\nport (integer) -- [REQUIRED]The port used for the port mapping.\n\nprotocol (string) -- [REQUIRED]The protocol used for the port mapping. Specify one protocol.\n\n\n\ntls (dict) --A reference to an object that represents the Transport Layer Security (TLS) properties for a listener.\n\ncertificate (dict) -- [REQUIRED]A reference to an object that represents a listener\'s TLS certificate.\n\nacm (dict) --A reference to an object that represents an AWS Certicate Manager (ACM) certificate.\n\ncertificateArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for the certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see Transport Layer Security (TLS) .\n\n\n\nfile (dict) --A reference to an object that represents a local file certificate.\n\ncertificateChain (string) -- [REQUIRED]The certificate chain for the certificate.\n\nprivateKey (string) -- [REQUIRED]The private key for a certificate stored on the file system of the virtual node that the proxy is running on.\n\n\n\n\n\nmode (string) -- [REQUIRED]Specify one of the following modes.\n\nSTRICT \xe2\x80\x93 Listener only accepts connections with TLS enabled.\nPERMISSIVE \xe2\x80\x93 Listener accepts connections with or without TLS enabled.\nDISABLED \xe2\x80\x93 Listener only accepts connections without TLS.\n\n\n\n\n\n\n\n\nlogging (dict) --The inbound and outbound access logging information for the virtual node.\n\naccessLog (dict) --The access log configuration for a virtual node.\n\nfile (dict) --The file object to send virtual node access logs to.\n\npath (string) -- [REQUIRED]The file path to write access logs to. You can use /dev/stdout to send access logs to standard out and configure your Envoy container to use a log driver, such as awslogs , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container\'s file system to write the files to disk.\n\nNote\nThe Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.\n\n\n\n\n\n\n\n\nserviceDiscovery (dict) --The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a listener , then you must specify service discovery information.\n\nawsCloudMap (dict) --Specifies any AWS Cloud Map information for the virtual node.\n\nattributes (list) --A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.\n\n(dict) --An object that represents the AWS Cloud Map attribute information for your virtual node.\n\nkey (string) -- [REQUIRED]The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.\n\nvalue (string) -- [REQUIRED]The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.\n\n\n\n\n\nnamespaceName (string) -- [REQUIRED]The name of the AWS Cloud Map namespace to use.\n\nserviceName (string) -- [REQUIRED]The name of the AWS Cloud Map service to use.\n\n\n\ndns (dict) --Specifies the DNS information for the virtual node.\n\nhostname (string) -- [REQUIRED]Specifies the DNS service discovery hostname for the virtual node.\n\n\n\n\n\n\n

    :type tags: list
    :param tags: Optional metadata that you can apply to the virtual node to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\n(dict) --Optional metadata that you apply to a resource to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nkey (string) -- [REQUIRED]One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nvalue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :type virtualNodeName: string
    :param virtualNodeName: [REQUIRED]\nThe name to use for the virtual node.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualNode': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'backendDefaults': {
                'clientPolicy': {
                    'tls': {
                        'enforce': True|False,
                        'ports': [
                            123,
                        ],
                        'validation': {
                            'trust': {
                                'acm': {
                                    'certificateAuthorityArns': [
                                        'string',
                                    ]
                                },
                                'file': {
                                    'certificateChain': 'string'
                                }
                            }
                        }
                    }
                }
            },
            'backends': [
                {
                    'virtualService': {
                        'clientPolicy': {
                            'tls': {
                                'enforce': True|False,
                                'ports': [
                                    123,
                                ],
                                'validation': {
                                    'trust': {
                                        'acm': {
                                            'certificateAuthorityArns': [
                                                'string',
                                            ]
                                        },
                                        'file': {
                                            'certificateChain': 'string'
                                        }
                                    }
                                }
                            }
                        },
                        'virtualServiceName': 'string'
                    }
                },
            ],
            'listeners': [
                {
                    'healthCheck': {
                        'healthyThreshold': 123,
                        'intervalMillis': 123,
                        'path': 'string',
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp',
                        'timeoutMillis': 123,
                        'unhealthyThreshold': 123
                    },
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    },
                    'tls': {
                        'certificate': {
                            'acm': {
                                'certificateArn': 'string'
                            },
                            'file': {
                                'certificateChain': 'string',
                                'privateKey': 'string'
                            }
                        },
                        'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                    }
                },
            ],
            'logging': {
                'accessLog': {
                    'file': {
                        'path': 'string'
                    }
                }
            },
            'serviceDiscovery': {
                'awsCloudMap': {
                    'attributes': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'namespaceName': 'string',
                    'serviceName': 'string'
                },
                'dns': {
                    'hostname': 'string'
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualNodeName': 'string'
    }
}


Response Structure

(dict) --

virtualNode (dict) --
The full description of your virtual node following the create call.

meshName (string) --
The name of the service mesh that the virtual node resides in.

metadata (dict) --
The associated metadata for the virtual node.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual node.

backendDefaults (dict) --
A reference to an object that represents the defaults for backends.

clientPolicy (dict) --
A reference to an object that represents a client policy.

tls (dict) --
A reference to an object that represents a Transport Layer Security (TLS) client policy.

enforce (boolean) --
Whether the policy is enforced. The default is True , if a value isn\'t specified.

ports (list) --
One or more ports that the policy is enforced for.

(integer) --


validation (dict) --
A reference to an object that represents a TLS validation context.

trust (dict) --
A reference to an object that represents a TLS validation context trust.

acm (dict) --
A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.

certificateAuthorityArns (list) --
One or more ACM Amazon Resource Name (ARN)s.

(string) --




file (dict) --
An object that represents a TLS validation context trust for a local file.

certificateChain (string) --
The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.













backends (list) --
The backends that the virtual node is expected to send outbound traffic to.

(dict) --
An object that represents the backends that a virtual node is expected to send outbound traffic to.

virtualService (dict) --
Specifies a virtual service to use as a backend for a virtual node.

clientPolicy (dict) --
A reference to an object that represents the client policy for a backend.

tls (dict) --
A reference to an object that represents a Transport Layer Security (TLS) client policy.

enforce (boolean) --
Whether the policy is enforced. The default is True , if a value isn\'t specified.

ports (list) --
One or more ports that the policy is enforced for.

(integer) --


validation (dict) --
A reference to an object that represents a TLS validation context.

trust (dict) --
A reference to an object that represents a TLS validation context trust.

acm (dict) --
A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.

certificateAuthorityArns (list) --
One or more ACM Amazon Resource Name (ARN)s.

(string) --




file (dict) --
An object that represents a TLS validation context trust for a local file.

certificateChain (string) --
The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.











virtualServiceName (string) --
The name of the virtual service that is acting as a virtual node backend.







listeners (list) --
The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.

(dict) --
An object that represents a listener for a virtual node.

healthCheck (dict) --
The health check information for the listener.

healthyThreshold (integer) --
The number of consecutive successful health checks that must occur before declaring listener healthy.

intervalMillis (integer) --
The time period in milliseconds between each health check execution.

path (string) --
The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.

port (integer) --
The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.

protocol (string) --
The protocol for the health check request. If you specify grpc , then your service must conform to the GRPC Health Checking Protocol .

timeoutMillis (integer) --
The amount of time to wait when receiving a response from the health check, in milliseconds.

unhealthyThreshold (integer) --
The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.



portMapping (dict) --
The port mapping information for the listener.

port (integer) --
The port used for the port mapping.

protocol (string) --
The protocol used for the port mapping. Specify one protocol.



tls (dict) --
A reference to an object that represents the Transport Layer Security (TLS) properties for a listener.

certificate (dict) --
A reference to an object that represents a listener\'s TLS certificate.

acm (dict) --
A reference to an object that represents an AWS Certicate Manager (ACM) certificate.

certificateArn (string) --
The Amazon Resource Name (ARN) for the certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see Transport Layer Security (TLS) .



file (dict) --
A reference to an object that represents a local file certificate.

certificateChain (string) --
The certificate chain for the certificate.

privateKey (string) --
The private key for a certificate stored on the file system of the virtual node that the proxy is running on.





mode (string) --
Specify one of the following modes.

STRICT \xe2\x80\x93 Listener only accepts connections with TLS enabled.
PERMISSIVE \xe2\x80\x93 Listener accepts connections with or without TLS enabled.
DISABLED \xe2\x80\x93 Listener only accepts connections without TLS.








logging (dict) --
The inbound and outbound access logging information for the virtual node.

accessLog (dict) --
The access log configuration for a virtual node.

file (dict) --
The file object to send virtual node access logs to.

path (string) --
The file path to write access logs to. You can use /dev/stdout to send access logs to standard out and configure your Envoy container to use a log driver, such as awslogs , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container\'s file system to write the files to disk.

Note
The Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.








serviceDiscovery (dict) --
The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a listener , then you must specify service discovery information.

awsCloudMap (dict) --
Specifies any AWS Cloud Map information for the virtual node.

attributes (list) --
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.

(dict) --
An object that represents the AWS Cloud Map attribute information for your virtual node.

key (string) --
The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.

value (string) --
The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.





namespaceName (string) --
The name of the AWS Cloud Map namespace to use.

serviceName (string) --
The name of the AWS Cloud Map service to use.



dns (dict) --
Specifies the DNS information for the virtual node.

hostname (string) --
Specifies the DNS service discovery hostname for the virtual node.







status (dict) --
The current status for the virtual node.

status (string) --
The current status of the virtual node.



virtualNodeName (string) --
The name of the virtual node.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.LimitExceededException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualNode': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'backendDefaults': {
                    'clientPolicy': {
                        'tls': {
                            'enforce': True|False,
                            'ports': [
                                123,
                            ],
                            'validation': {
                                'trust': {
                                    'acm': {
                                        'certificateAuthorityArns': [
                                            'string',
                                        ]
                                    },
                                    'file': {
                                        'certificateChain': 'string'
                                    }
                                }
                            }
                        }
                    }
                },
                'backends': [
                    {
                        'virtualService': {
                            'clientPolicy': {
                                'tls': {
                                    'enforce': True|False,
                                    'ports': [
                                        123,
                                    ],
                                    'validation': {
                                        'trust': {
                                            'acm': {
                                                'certificateAuthorityArns': [
                                                    'string',
                                                ]
                                            },
                                            'file': {
                                                'certificateChain': 'string'
                                            }
                                        }
                                    }
                                }
                            },
                            'virtualServiceName': 'string'
                        }
                    },
                ],
                'listeners': [
                    {
                        'healthCheck': {
                            'healthyThreshold': 123,
                            'intervalMillis': 123,
                            'path': 'string',
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp',
                            'timeoutMillis': 123,
                            'unhealthyThreshold': 123
                        },
                        'portMapping': {
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp'
                        },
                        'tls': {
                            'certificate': {
                                'acm': {
                                    'certificateArn': 'string'
                                },
                                'file': {
                                    'certificateChain': 'string',
                                    'privateKey': 'string'
                                }
                            },
                            'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                        }
                    },
                ],
                'logging': {
                    'accessLog': {
                        'file': {
                            'path': 'string'
                        }
                    }
                },
                'serviceDiscovery': {
                    'awsCloudMap': {
                        'attributes': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'namespaceName': 'string',
                        'serviceName': 'string'
                    },
                    'dns': {
                        'hostname': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualNodeName': 'string'
        }
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def create_virtual_router(clientToken=None, meshName=None, meshOwner=None, spec=None, tags=None, virtualRouterName=None):
    """
    Creates a virtual router within a service mesh.
    Specify a listener for any inbound traffic that your virtual router receives. Create a virtual router for each protocol and port that you need to route. Virtual routers handle traffic for one or more virtual services within your mesh. After you create your virtual router, create and associate routes for your virtual router that direct incoming requests to different virtual nodes.
    For more information about virtual routers, see Virtual routers .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_virtual_router(
        clientToken='string',
        meshName='string',
        meshOwner='string',
        spec={
            'listeners': [
                {
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    }
                },
            ]
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        virtualRouterName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to create the virtual router in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see Working with Shared Meshes .

    :type spec: dict
    :param spec: [REQUIRED]\nThe virtual router specification to apply.\n\nlisteners (list) --The listeners that the virtual router is expected to receive inbound traffic from. You can specify one listener.\n\n(dict) --An object that represents a virtual router listener.\n\nportMapping (dict) -- [REQUIRED]An object that represents a port mapping.\n\nport (integer) -- [REQUIRED]The port used for the port mapping.\n\nprotocol (string) -- [REQUIRED]The protocol used for the port mapping. Specify one protocol.\n\n\n\n\n\n\n\n\n

    :type tags: list
    :param tags: Optional metadata that you can apply to the virtual router to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\n(dict) --Optional metadata that you apply to a resource to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nkey (string) -- [REQUIRED]One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nvalue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]\nThe name to use for the virtual router.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualRouter': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'listeners': [
                {
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    }
                },
            ]
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualRouterName': 'string'
    }
}


Response Structure

(dict) --

virtualRouter (dict) --
The full description of your virtual router following the create call.

meshName (string) --
The name of the service mesh that the virtual router resides in.

metadata (dict) --
The associated metadata for the virtual router.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual router.

listeners (list) --
The listeners that the virtual router is expected to receive inbound traffic from. You can specify one listener.

(dict) --
An object that represents a virtual router listener.

portMapping (dict) --
An object that represents a port mapping.

port (integer) --
The port used for the port mapping.

protocol (string) --
The protocol used for the port mapping. Specify one protocol.









status (dict) --
The current status of the virtual router.

status (string) --
The current status of the virtual router.



virtualRouterName (string) --
The name of the virtual router.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.LimitExceededException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualRouter': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'listeners': [
                    {
                        'portMapping': {
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp'
                        }
                    },
                ]
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ConflictException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.LimitExceededException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def create_virtual_service(clientToken=None, meshName=None, meshOwner=None, spec=None, tags=None, virtualServiceName=None):
    """
    Creates a virtual service within a service mesh.
    A virtual service is an abstraction of a real service that is provided by a virtual node directly or indirectly by means of a virtual router. Dependent services call your virtual service by its virtualServiceName , and those requests are routed to the virtual node or virtual router that is specified as the provider for the virtual service.
    For more information about virtual services, see Virtual services .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_virtual_service(
        clientToken='string',
        meshName='string',
        meshOwner='string',
        spec={
            'provider': {
                'virtualNode': {
                    'virtualNodeName': 'string'
                },
                'virtualRouter': {
                    'virtualRouterName': 'string'
                }
            }
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        virtualServiceName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to create the virtual service in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see Working with Shared Meshes .

    :type spec: dict
    :param spec: [REQUIRED]\nThe virtual service specification to apply.\n\nprovider (dict) --The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.\n\nvirtualNode (dict) --The virtual node associated with a virtual service.\n\nvirtualNodeName (string) -- [REQUIRED]The name of the virtual node that is acting as a service provider.\n\n\n\nvirtualRouter (dict) --The virtual router associated with a virtual service.\n\nvirtualRouterName (string) -- [REQUIRED]The name of the virtual router that is acting as a service provider.\n\n\n\n\n\n\n

    :type tags: list
    :param tags: Optional metadata that you can apply to the virtual service to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\n(dict) --Optional metadata that you apply to a resource to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nkey (string) -- [REQUIRED]One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nvalue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :type virtualServiceName: string
    :param virtualServiceName: [REQUIRED]\nThe name to use for the virtual service.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualService': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'provider': {
                'virtualNode': {
                    'virtualNodeName': 'string'
                },
                'virtualRouter': {
                    'virtualRouterName': 'string'
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualServiceName': 'string'
    }
}


Response Structure

(dict) --

virtualService (dict) --
The full description of your virtual service following the create call.

meshName (string) --
The name of the service mesh that the virtual service resides in.

metadata (dict) --
An object that represents metadata for a resource.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual service.

provider (dict) --
The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.

virtualNode (dict) --
The virtual node associated with a virtual service.

virtualNodeName (string) --
The name of the virtual node that is acting as a service provider.



virtualRouter (dict) --
The virtual router associated with a virtual service.

virtualRouterName (string) --
The name of the virtual router that is acting as a service provider.







status (dict) --
The current status of the virtual service.

status (string) --
The current status of the virtual service.



virtualServiceName (string) --
The name of the virtual service.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.LimitExceededException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualService': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'provider': {
                    'virtualNode': {
                        'virtualNodeName': 'string'
                    },
                    'virtualRouter': {
                        'virtualRouterName': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualServiceName': 'string'
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ConflictException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.LimitExceededException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_mesh(meshName=None):
    """
    Deletes an existing service mesh.
    You must delete all resources (virtual services, routes, virtual routers, and virtual nodes) in the service mesh before you can delete the mesh itself.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_mesh(
        meshName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'mesh': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'egressFilter': {
                'type': 'ALLOW_ALL'|'DROP_ALL'
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        }
    }
}


Response Structure

(dict) --
mesh (dict) --The service mesh that was deleted.

meshName (string) --The name of the service mesh.

metadata (dict) --The associated metadata for the service mesh.

arn (string) --The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --The unique identifier for the resource.

version (integer) --The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --The associated specification for the service mesh.

egressFilter (dict) --The egress filter rules for the service mesh.

type (string) --The egress filter type. By default, the type is DROP_ALL , which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to *.amazonaws.com for AWS API calls). You can set the egress filter type to ALLOW_ALL to allow egress to any endpoint inside or outside of the service mesh.





status (dict) --The status of the service mesh.

status (string) --The current mesh status.










Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ResourceInUseException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'mesh': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'egressFilter': {
                    'type': 'ALLOW_ALL'|'DROP_ALL'
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            }
        }
    }
    
    
    """
    pass

def delete_route(meshName=None, meshOwner=None, routeName=None, virtualRouterName=None):
    """
    Deletes an existing route.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_route(
        meshName='string',
        meshOwner='string',
        routeName='string',
        virtualRouterName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to delete the route in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type routeName: string
    :param routeName: [REQUIRED]\nThe name of the route to delete.\n

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]\nThe name of the virtual router to delete the route in.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'route': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'routeName': 'string',
        'spec': {
            'grpcRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'metadata': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'methodName': 'string',
                    'serviceName': 'string'
                },
                'retryPolicy': {
                    'grpcRetryEvents': [
                        'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                    ],
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'http2Route': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'httpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'priority': 123,
            'tcpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualRouterName': 'string'
    }
}


Response Structure

(dict) --

route (dict) --
The route that was deleted.

meshName (string) --
The name of the service mesh that the route resides in.

metadata (dict) --
The associated metadata for the route.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



routeName (string) --
The name of the route.

spec (dict) --
The specifications of the route.

grpcRoute (dict) --
An object that represents the specification of a gRPC route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

metadata (list) --
An object that represents the data to match from the request.

(dict) --
An object that represents the match metadata for the route.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
An object that represents the data to match from the request.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
The name of the route.





methodName (string) --
The method name to match from the request. If you specify a name, you must also specify a serviceName .

serviceName (string) --
The fully qualified domain name for the service to match from the request.



retryPolicy (dict) --
An object that represents a retry policy.

grpcRetryEvents (list) --
Specify at least one of the valid values.

(string) --


httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






http2Route (dict) --
An object that represents the specification of an HTTP/2 route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

headers (list) --
An object that represents the client request headers to match on.

(dict) --
An object that represents the HTTP header in the request.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
The HeaderMatchMethod object.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
A name for the HTTP header in the client request that will be matched on.





method (string) --
The client request method to match on. Specify only one.

prefix (string) --
Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .

scheme (string) --
The client request scheme to match on. Specify only one.



retryPolicy (dict) --
An object that represents a retry policy.

httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






httpRoute (dict) --
An object that represents the specification of an HTTP route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

headers (list) --
An object that represents the client request headers to match on.

(dict) --
An object that represents the HTTP header in the request.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
The HeaderMatchMethod object.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
A name for the HTTP header in the client request that will be matched on.





method (string) --
The client request method to match on. Specify only one.

prefix (string) --
Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .

scheme (string) --
The client request scheme to match on. Specify only one.



retryPolicy (dict) --
An object that represents a retry policy.

httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






priority (integer) --
The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority.

tcpRoute (dict) --
An object that represents the specification of a TCP route.

action (dict) --
The action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.











status (dict) --
The status of the route.

status (string) --
The current status for the route.



virtualRouterName (string) --
The virtual router that the route is associated with.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ResourceInUseException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'route': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'routeName': 'string',
            'spec': {
                'grpcRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'metadata': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'methodName': 'string',
                        'serviceName': 'string'
                    },
                    'retryPolicy': {
                        'grpcRetryEvents': [
                            'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                        ],
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'http2Route': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'headers': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                        'prefix': 'string',
                        'scheme': 'http'|'https'
                    },
                    'retryPolicy': {
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'httpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'headers': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                        'prefix': 'string',
                        'scheme': 'http'|'https'
                    },
                    'retryPolicy': {
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'priority': 123,
                'tcpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_virtual_node(meshName=None, meshOwner=None, virtualNodeName=None):
    """
    Deletes an existing virtual node.
    You must delete any virtual services that list a virtual node as a service provider before you can delete the virtual node itself.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_virtual_node(
        meshName='string',
        meshOwner='string',
        virtualNodeName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to delete the virtual node in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type virtualNodeName: string
    :param virtualNodeName: [REQUIRED]\nThe name of the virtual node to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualNode': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'backendDefaults': {
                'clientPolicy': {
                    'tls': {
                        'enforce': True|False,
                        'ports': [
                            123,
                        ],
                        'validation': {
                            'trust': {
                                'acm': {
                                    'certificateAuthorityArns': [
                                        'string',
                                    ]
                                },
                                'file': {
                                    'certificateChain': 'string'
                                }
                            }
                        }
                    }
                }
            },
            'backends': [
                {
                    'virtualService': {
                        'clientPolicy': {
                            'tls': {
                                'enforce': True|False,
                                'ports': [
                                    123,
                                ],
                                'validation': {
                                    'trust': {
                                        'acm': {
                                            'certificateAuthorityArns': [
                                                'string',
                                            ]
                                        },
                                        'file': {
                                            'certificateChain': 'string'
                                        }
                                    }
                                }
                            }
                        },
                        'virtualServiceName': 'string'
                    }
                },
            ],
            'listeners': [
                {
                    'healthCheck': {
                        'healthyThreshold': 123,
                        'intervalMillis': 123,
                        'path': 'string',
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp',
                        'timeoutMillis': 123,
                        'unhealthyThreshold': 123
                    },
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    },
                    'tls': {
                        'certificate': {
                            'acm': {
                                'certificateArn': 'string'
                            },
                            'file': {
                                'certificateChain': 'string',
                                'privateKey': 'string'
                            }
                        },
                        'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                    }
                },
            ],
            'logging': {
                'accessLog': {
                    'file': {
                        'path': 'string'
                    }
                }
            },
            'serviceDiscovery': {
                'awsCloudMap': {
                    'attributes': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'namespaceName': 'string',
                    'serviceName': 'string'
                },
                'dns': {
                    'hostname': 'string'
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualNodeName': 'string'
    }
}


Response Structure

(dict) --

virtualNode (dict) --
The virtual node that was deleted.

meshName (string) --
The name of the service mesh that the virtual node resides in.

metadata (dict) --
The associated metadata for the virtual node.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual node.

backendDefaults (dict) --
A reference to an object that represents the defaults for backends.

clientPolicy (dict) --
A reference to an object that represents a client policy.

tls (dict) --
A reference to an object that represents a Transport Layer Security (TLS) client policy.

enforce (boolean) --
Whether the policy is enforced. The default is True , if a value isn\'t specified.

ports (list) --
One or more ports that the policy is enforced for.

(integer) --


validation (dict) --
A reference to an object that represents a TLS validation context.

trust (dict) --
A reference to an object that represents a TLS validation context trust.

acm (dict) --
A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.

certificateAuthorityArns (list) --
One or more ACM Amazon Resource Name (ARN)s.

(string) --




file (dict) --
An object that represents a TLS validation context trust for a local file.

certificateChain (string) --
The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.













backends (list) --
The backends that the virtual node is expected to send outbound traffic to.

(dict) --
An object that represents the backends that a virtual node is expected to send outbound traffic to.

virtualService (dict) --
Specifies a virtual service to use as a backend for a virtual node.

clientPolicy (dict) --
A reference to an object that represents the client policy for a backend.

tls (dict) --
A reference to an object that represents a Transport Layer Security (TLS) client policy.

enforce (boolean) --
Whether the policy is enforced. The default is True , if a value isn\'t specified.

ports (list) --
One or more ports that the policy is enforced for.

(integer) --


validation (dict) --
A reference to an object that represents a TLS validation context.

trust (dict) --
A reference to an object that represents a TLS validation context trust.

acm (dict) --
A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.

certificateAuthorityArns (list) --
One or more ACM Amazon Resource Name (ARN)s.

(string) --




file (dict) --
An object that represents a TLS validation context trust for a local file.

certificateChain (string) --
The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.











virtualServiceName (string) --
The name of the virtual service that is acting as a virtual node backend.







listeners (list) --
The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.

(dict) --
An object that represents a listener for a virtual node.

healthCheck (dict) --
The health check information for the listener.

healthyThreshold (integer) --
The number of consecutive successful health checks that must occur before declaring listener healthy.

intervalMillis (integer) --
The time period in milliseconds between each health check execution.

path (string) --
The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.

port (integer) --
The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.

protocol (string) --
The protocol for the health check request. If you specify grpc , then your service must conform to the GRPC Health Checking Protocol .

timeoutMillis (integer) --
The amount of time to wait when receiving a response from the health check, in milliseconds.

unhealthyThreshold (integer) --
The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.



portMapping (dict) --
The port mapping information for the listener.

port (integer) --
The port used for the port mapping.

protocol (string) --
The protocol used for the port mapping. Specify one protocol.



tls (dict) --
A reference to an object that represents the Transport Layer Security (TLS) properties for a listener.

certificate (dict) --
A reference to an object that represents a listener\'s TLS certificate.

acm (dict) --
A reference to an object that represents an AWS Certicate Manager (ACM) certificate.

certificateArn (string) --
The Amazon Resource Name (ARN) for the certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see Transport Layer Security (TLS) .



file (dict) --
A reference to an object that represents a local file certificate.

certificateChain (string) --
The certificate chain for the certificate.

privateKey (string) --
The private key for a certificate stored on the file system of the virtual node that the proxy is running on.





mode (string) --
Specify one of the following modes.

STRICT \xe2\x80\x93 Listener only accepts connections with TLS enabled.
PERMISSIVE \xe2\x80\x93 Listener accepts connections with or without TLS enabled.
DISABLED \xe2\x80\x93 Listener only accepts connections without TLS.








logging (dict) --
The inbound and outbound access logging information for the virtual node.

accessLog (dict) --
The access log configuration for a virtual node.

file (dict) --
The file object to send virtual node access logs to.

path (string) --
The file path to write access logs to. You can use /dev/stdout to send access logs to standard out and configure your Envoy container to use a log driver, such as awslogs , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container\'s file system to write the files to disk.

Note
The Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.








serviceDiscovery (dict) --
The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a listener , then you must specify service discovery information.

awsCloudMap (dict) --
Specifies any AWS Cloud Map information for the virtual node.

attributes (list) --
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.

(dict) --
An object that represents the AWS Cloud Map attribute information for your virtual node.

key (string) --
The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.

value (string) --
The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.





namespaceName (string) --
The name of the AWS Cloud Map namespace to use.

serviceName (string) --
The name of the AWS Cloud Map service to use.



dns (dict) --
Specifies the DNS information for the virtual node.

hostname (string) --
Specifies the DNS service discovery hostname for the virtual node.







status (dict) --
The current status for the virtual node.

status (string) --
The current status of the virtual node.



virtualNodeName (string) --
The name of the virtual node.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ResourceInUseException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualNode': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'backendDefaults': {
                    'clientPolicy': {
                        'tls': {
                            'enforce': True|False,
                            'ports': [
                                123,
                            ],
                            'validation': {
                                'trust': {
                                    'acm': {
                                        'certificateAuthorityArns': [
                                            'string',
                                        ]
                                    },
                                    'file': {
                                        'certificateChain': 'string'
                                    }
                                }
                            }
                        }
                    }
                },
                'backends': [
                    {
                        'virtualService': {
                            'clientPolicy': {
                                'tls': {
                                    'enforce': True|False,
                                    'ports': [
                                        123,
                                    ],
                                    'validation': {
                                        'trust': {
                                            'acm': {
                                                'certificateAuthorityArns': [
                                                    'string',
                                                ]
                                            },
                                            'file': {
                                                'certificateChain': 'string'
                                            }
                                        }
                                    }
                                }
                            },
                            'virtualServiceName': 'string'
                        }
                    },
                ],
                'listeners': [
                    {
                        'healthCheck': {
                            'healthyThreshold': 123,
                            'intervalMillis': 123,
                            'path': 'string',
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp',
                            'timeoutMillis': 123,
                            'unhealthyThreshold': 123
                        },
                        'portMapping': {
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp'
                        },
                        'tls': {
                            'certificate': {
                                'acm': {
                                    'certificateArn': 'string'
                                },
                                'file': {
                                    'certificateChain': 'string',
                                    'privateKey': 'string'
                                }
                            },
                            'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                        }
                    },
                ],
                'logging': {
                    'accessLog': {
                        'file': {
                            'path': 'string'
                        }
                    }
                },
                'serviceDiscovery': {
                    'awsCloudMap': {
                        'attributes': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'namespaceName': 'string',
                        'serviceName': 'string'
                    },
                    'dns': {
                        'hostname': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualNodeName': 'string'
        }
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def delete_virtual_router(meshName=None, meshOwner=None, virtualRouterName=None):
    """
    Deletes an existing virtual router.
    You must delete any routes associated with the virtual router before you can delete the router itself.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_virtual_router(
        meshName='string',
        meshOwner='string',
        virtualRouterName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to delete the virtual router in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]\nThe name of the virtual router to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualRouter': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'listeners': [
                {
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    }
                },
            ]
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualRouterName': 'string'
    }
}


Response Structure

(dict) --

virtualRouter (dict) --
The virtual router that was deleted.

meshName (string) --
The name of the service mesh that the virtual router resides in.

metadata (dict) --
The associated metadata for the virtual router.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual router.

listeners (list) --
The listeners that the virtual router is expected to receive inbound traffic from. You can specify one listener.

(dict) --
An object that represents a virtual router listener.

portMapping (dict) --
An object that represents a port mapping.

port (integer) --
The port used for the port mapping.

protocol (string) --
The protocol used for the port mapping. Specify one protocol.









status (dict) --
The current status of the virtual router.

status (string) --
The current status of the virtual router.



virtualRouterName (string) --
The name of the virtual router.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ResourceInUseException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualRouter': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'listeners': [
                    {
                        'portMapping': {
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp'
                        }
                    },
                ]
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ResourceInUseException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_virtual_service(meshName=None, meshOwner=None, virtualServiceName=None):
    """
    Deletes an existing virtual service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_virtual_service(
        meshName='string',
        meshOwner='string',
        virtualServiceName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to delete the virtual service in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type virtualServiceName: string
    :param virtualServiceName: [REQUIRED]\nThe name of the virtual service to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualService': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'provider': {
                'virtualNode': {
                    'virtualNodeName': 'string'
                },
                'virtualRouter': {
                    'virtualRouterName': 'string'
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualServiceName': 'string'
    }
}


Response Structure

(dict) --

virtualService (dict) --
The virtual service that was deleted.

meshName (string) --
The name of the service mesh that the virtual service resides in.

metadata (dict) --
An object that represents metadata for a resource.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual service.

provider (dict) --
The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.

virtualNode (dict) --
The virtual node associated with a virtual service.

virtualNodeName (string) --
The name of the virtual node that is acting as a service provider.



virtualRouter (dict) --
The virtual router associated with a virtual service.

virtualRouterName (string) --
The name of the virtual router that is acting as a service provider.







status (dict) --
The current status of the virtual service.

status (string) --
The current status of the virtual service.



virtualServiceName (string) --
The name of the virtual service.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ResourceInUseException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualService': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'provider': {
                    'virtualNode': {
                        'virtualNodeName': 'string'
                    },
                    'virtualRouter': {
                        'virtualRouterName': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualServiceName': 'string'
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ResourceInUseException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_mesh(meshName=None, meshOwner=None):
    """
    Describes an existing service mesh.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_mesh(
        meshName='string',
        meshOwner='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to describe.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :rtype: dict

ReturnsResponse Syntax
{
    'mesh': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'egressFilter': {
                'type': 'ALLOW_ALL'|'DROP_ALL'
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        }
    }
}


Response Structure

(dict) --

mesh (dict) --
The full description of your service mesh.

meshName (string) --
The name of the service mesh.

metadata (dict) --
The associated metadata for the service mesh.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The associated specification for the service mesh.

egressFilter (dict) --
The egress filter rules for the service mesh.

type (string) --
The egress filter type. By default, the type is DROP_ALL , which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to *.amazonaws.com for AWS API calls). You can set the egress filter type to ALLOW_ALL to allow egress to any endpoint inside or outside of the service mesh.





status (dict) --
The status of the service mesh.

status (string) --
The current mesh status.











Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'mesh': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'egressFilter': {
                    'type': 'ALLOW_ALL'|'DROP_ALL'
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            }
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_route(meshName=None, meshOwner=None, routeName=None, virtualRouterName=None):
    """
    Describes an existing route.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_route(
        meshName='string',
        meshOwner='string',
        routeName='string',
        virtualRouterName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh that the route resides in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type routeName: string
    :param routeName: [REQUIRED]\nThe name of the route to describe.\n

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]\nThe name of the virtual router that the route is associated with.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'route': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'routeName': 'string',
        'spec': {
            'grpcRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'metadata': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'methodName': 'string',
                    'serviceName': 'string'
                },
                'retryPolicy': {
                    'grpcRetryEvents': [
                        'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                    ],
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'http2Route': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'httpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'priority': 123,
            'tcpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualRouterName': 'string'
    }
}


Response Structure

(dict) --

route (dict) --
The full description of your route.

meshName (string) --
The name of the service mesh that the route resides in.

metadata (dict) --
The associated metadata for the route.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



routeName (string) --
The name of the route.

spec (dict) --
The specifications of the route.

grpcRoute (dict) --
An object that represents the specification of a gRPC route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

metadata (list) --
An object that represents the data to match from the request.

(dict) --
An object that represents the match metadata for the route.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
An object that represents the data to match from the request.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
The name of the route.





methodName (string) --
The method name to match from the request. If you specify a name, you must also specify a serviceName .

serviceName (string) --
The fully qualified domain name for the service to match from the request.



retryPolicy (dict) --
An object that represents a retry policy.

grpcRetryEvents (list) --
Specify at least one of the valid values.

(string) --


httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






http2Route (dict) --
An object that represents the specification of an HTTP/2 route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

headers (list) --
An object that represents the client request headers to match on.

(dict) --
An object that represents the HTTP header in the request.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
The HeaderMatchMethod object.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
A name for the HTTP header in the client request that will be matched on.





method (string) --
The client request method to match on. Specify only one.

prefix (string) --
Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .

scheme (string) --
The client request scheme to match on. Specify only one.



retryPolicy (dict) --
An object that represents a retry policy.

httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






httpRoute (dict) --
An object that represents the specification of an HTTP route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

headers (list) --
An object that represents the client request headers to match on.

(dict) --
An object that represents the HTTP header in the request.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
The HeaderMatchMethod object.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
A name for the HTTP header in the client request that will be matched on.





method (string) --
The client request method to match on. Specify only one.

prefix (string) --
Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .

scheme (string) --
The client request scheme to match on. Specify only one.



retryPolicy (dict) --
An object that represents a retry policy.

httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






priority (integer) --
The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority.

tcpRoute (dict) --
An object that represents the specification of a TCP route.

action (dict) --
The action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.











status (dict) --
The status of the route.

status (string) --
The current status for the route.



virtualRouterName (string) --
The virtual router that the route is associated with.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'route': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'routeName': 'string',
            'spec': {
                'grpcRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'metadata': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'methodName': 'string',
                        'serviceName': 'string'
                    },
                    'retryPolicy': {
                        'grpcRetryEvents': [
                            'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                        ],
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'http2Route': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'headers': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                        'prefix': 'string',
                        'scheme': 'http'|'https'
                    },
                    'retryPolicy': {
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'httpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'headers': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                        'prefix': 'string',
                        'scheme': 'http'|'https'
                    },
                    'retryPolicy': {
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'priority': 123,
                'tcpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_virtual_node(meshName=None, meshOwner=None, virtualNodeName=None):
    """
    Describes an existing virtual node.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_virtual_node(
        meshName='string',
        meshOwner='string',
        virtualNodeName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh that the virtual node resides in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type virtualNodeName: string
    :param virtualNodeName: [REQUIRED]\nThe name of the virtual node to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualNode': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'backendDefaults': {
                'clientPolicy': {
                    'tls': {
                        'enforce': True|False,
                        'ports': [
                            123,
                        ],
                        'validation': {
                            'trust': {
                                'acm': {
                                    'certificateAuthorityArns': [
                                        'string',
                                    ]
                                },
                                'file': {
                                    'certificateChain': 'string'
                                }
                            }
                        }
                    }
                }
            },
            'backends': [
                {
                    'virtualService': {
                        'clientPolicy': {
                            'tls': {
                                'enforce': True|False,
                                'ports': [
                                    123,
                                ],
                                'validation': {
                                    'trust': {
                                        'acm': {
                                            'certificateAuthorityArns': [
                                                'string',
                                            ]
                                        },
                                        'file': {
                                            'certificateChain': 'string'
                                        }
                                    }
                                }
                            }
                        },
                        'virtualServiceName': 'string'
                    }
                },
            ],
            'listeners': [
                {
                    'healthCheck': {
                        'healthyThreshold': 123,
                        'intervalMillis': 123,
                        'path': 'string',
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp',
                        'timeoutMillis': 123,
                        'unhealthyThreshold': 123
                    },
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    },
                    'tls': {
                        'certificate': {
                            'acm': {
                                'certificateArn': 'string'
                            },
                            'file': {
                                'certificateChain': 'string',
                                'privateKey': 'string'
                            }
                        },
                        'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                    }
                },
            ],
            'logging': {
                'accessLog': {
                    'file': {
                        'path': 'string'
                    }
                }
            },
            'serviceDiscovery': {
                'awsCloudMap': {
                    'attributes': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'namespaceName': 'string',
                    'serviceName': 'string'
                },
                'dns': {
                    'hostname': 'string'
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualNodeName': 'string'
    }
}


Response Structure

(dict) --

virtualNode (dict) --
The full description of your virtual node.

meshName (string) --
The name of the service mesh that the virtual node resides in.

metadata (dict) --
The associated metadata for the virtual node.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual node.

backendDefaults (dict) --
A reference to an object that represents the defaults for backends.

clientPolicy (dict) --
A reference to an object that represents a client policy.

tls (dict) --
A reference to an object that represents a Transport Layer Security (TLS) client policy.

enforce (boolean) --
Whether the policy is enforced. The default is True , if a value isn\'t specified.

ports (list) --
One or more ports that the policy is enforced for.

(integer) --


validation (dict) --
A reference to an object that represents a TLS validation context.

trust (dict) --
A reference to an object that represents a TLS validation context trust.

acm (dict) --
A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.

certificateAuthorityArns (list) --
One or more ACM Amazon Resource Name (ARN)s.

(string) --




file (dict) --
An object that represents a TLS validation context trust for a local file.

certificateChain (string) --
The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.













backends (list) --
The backends that the virtual node is expected to send outbound traffic to.

(dict) --
An object that represents the backends that a virtual node is expected to send outbound traffic to.

virtualService (dict) --
Specifies a virtual service to use as a backend for a virtual node.

clientPolicy (dict) --
A reference to an object that represents the client policy for a backend.

tls (dict) --
A reference to an object that represents a Transport Layer Security (TLS) client policy.

enforce (boolean) --
Whether the policy is enforced. The default is True , if a value isn\'t specified.

ports (list) --
One or more ports that the policy is enforced for.

(integer) --


validation (dict) --
A reference to an object that represents a TLS validation context.

trust (dict) --
A reference to an object that represents a TLS validation context trust.

acm (dict) --
A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.

certificateAuthorityArns (list) --
One or more ACM Amazon Resource Name (ARN)s.

(string) --




file (dict) --
An object that represents a TLS validation context trust for a local file.

certificateChain (string) --
The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.











virtualServiceName (string) --
The name of the virtual service that is acting as a virtual node backend.







listeners (list) --
The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.

(dict) --
An object that represents a listener for a virtual node.

healthCheck (dict) --
The health check information for the listener.

healthyThreshold (integer) --
The number of consecutive successful health checks that must occur before declaring listener healthy.

intervalMillis (integer) --
The time period in milliseconds between each health check execution.

path (string) --
The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.

port (integer) --
The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.

protocol (string) --
The protocol for the health check request. If you specify grpc , then your service must conform to the GRPC Health Checking Protocol .

timeoutMillis (integer) --
The amount of time to wait when receiving a response from the health check, in milliseconds.

unhealthyThreshold (integer) --
The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.



portMapping (dict) --
The port mapping information for the listener.

port (integer) --
The port used for the port mapping.

protocol (string) --
The protocol used for the port mapping. Specify one protocol.



tls (dict) --
A reference to an object that represents the Transport Layer Security (TLS) properties for a listener.

certificate (dict) --
A reference to an object that represents a listener\'s TLS certificate.

acm (dict) --
A reference to an object that represents an AWS Certicate Manager (ACM) certificate.

certificateArn (string) --
The Amazon Resource Name (ARN) for the certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see Transport Layer Security (TLS) .



file (dict) --
A reference to an object that represents a local file certificate.

certificateChain (string) --
The certificate chain for the certificate.

privateKey (string) --
The private key for a certificate stored on the file system of the virtual node that the proxy is running on.





mode (string) --
Specify one of the following modes.

STRICT \xe2\x80\x93 Listener only accepts connections with TLS enabled.
PERMISSIVE \xe2\x80\x93 Listener accepts connections with or without TLS enabled.
DISABLED \xe2\x80\x93 Listener only accepts connections without TLS.








logging (dict) --
The inbound and outbound access logging information for the virtual node.

accessLog (dict) --
The access log configuration for a virtual node.

file (dict) --
The file object to send virtual node access logs to.

path (string) --
The file path to write access logs to. You can use /dev/stdout to send access logs to standard out and configure your Envoy container to use a log driver, such as awslogs , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container\'s file system to write the files to disk.

Note
The Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.








serviceDiscovery (dict) --
The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a listener , then you must specify service discovery information.

awsCloudMap (dict) --
Specifies any AWS Cloud Map information for the virtual node.

attributes (list) --
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.

(dict) --
An object that represents the AWS Cloud Map attribute information for your virtual node.

key (string) --
The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.

value (string) --
The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.





namespaceName (string) --
The name of the AWS Cloud Map namespace to use.

serviceName (string) --
The name of the AWS Cloud Map service to use.



dns (dict) --
Specifies the DNS information for the virtual node.

hostname (string) --
Specifies the DNS service discovery hostname for the virtual node.







status (dict) --
The current status for the virtual node.

status (string) --
The current status of the virtual node.



virtualNodeName (string) --
The name of the virtual node.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualNode': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'backendDefaults': {
                    'clientPolicy': {
                        'tls': {
                            'enforce': True|False,
                            'ports': [
                                123,
                            ],
                            'validation': {
                                'trust': {
                                    'acm': {
                                        'certificateAuthorityArns': [
                                            'string',
                                        ]
                                    },
                                    'file': {
                                        'certificateChain': 'string'
                                    }
                                }
                            }
                        }
                    }
                },
                'backends': [
                    {
                        'virtualService': {
                            'clientPolicy': {
                                'tls': {
                                    'enforce': True|False,
                                    'ports': [
                                        123,
                                    ],
                                    'validation': {
                                        'trust': {
                                            'acm': {
                                                'certificateAuthorityArns': [
                                                    'string',
                                                ]
                                            },
                                            'file': {
                                                'certificateChain': 'string'
                                            }
                                        }
                                    }
                                }
                            },
                            'virtualServiceName': 'string'
                        }
                    },
                ],
                'listeners': [
                    {
                        'healthCheck': {
                            'healthyThreshold': 123,
                            'intervalMillis': 123,
                            'path': 'string',
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp',
                            'timeoutMillis': 123,
                            'unhealthyThreshold': 123
                        },
                        'portMapping': {
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp'
                        },
                        'tls': {
                            'certificate': {
                                'acm': {
                                    'certificateArn': 'string'
                                },
                                'file': {
                                    'certificateChain': 'string',
                                    'privateKey': 'string'
                                }
                            },
                            'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                        }
                    },
                ],
                'logging': {
                    'accessLog': {
                        'file': {
                            'path': 'string'
                        }
                    }
                },
                'serviceDiscovery': {
                    'awsCloudMap': {
                        'attributes': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'namespaceName': 'string',
                        'serviceName': 'string'
                    },
                    'dns': {
                        'hostname': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualNodeName': 'string'
        }
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def describe_virtual_router(meshName=None, meshOwner=None, virtualRouterName=None):
    """
    Describes an existing virtual router.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_virtual_router(
        meshName='string',
        meshOwner='string',
        virtualRouterName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh that the virtual router resides in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]\nThe name of the virtual router to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualRouter': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'listeners': [
                {
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    }
                },
            ]
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualRouterName': 'string'
    }
}


Response Structure

(dict) --

virtualRouter (dict) --
The full description of your virtual router.

meshName (string) --
The name of the service mesh that the virtual router resides in.

metadata (dict) --
The associated metadata for the virtual router.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual router.

listeners (list) --
The listeners that the virtual router is expected to receive inbound traffic from. You can specify one listener.

(dict) --
An object that represents a virtual router listener.

portMapping (dict) --
An object that represents a port mapping.

port (integer) --
The port used for the port mapping.

protocol (string) --
The protocol used for the port mapping. Specify one protocol.









status (dict) --
The current status of the virtual router.

status (string) --
The current status of the virtual router.



virtualRouterName (string) --
The name of the virtual router.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualRouter': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'listeners': [
                    {
                        'portMapping': {
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp'
                        }
                    },
                ]
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_virtual_service(meshName=None, meshOwner=None, virtualServiceName=None):
    """
    Describes an existing virtual service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_virtual_service(
        meshName='string',
        meshOwner='string',
        virtualServiceName='string'
    )
    
    
    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh that the virtual service resides in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type virtualServiceName: string
    :param virtualServiceName: [REQUIRED]\nThe name of the virtual service to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualService': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'provider': {
                'virtualNode': {
                    'virtualNodeName': 'string'
                },
                'virtualRouter': {
                    'virtualRouterName': 'string'
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualServiceName': 'string'
    }
}


Response Structure

(dict) --

virtualService (dict) --
The full description of your virtual service.

meshName (string) --
The name of the service mesh that the virtual service resides in.

metadata (dict) --
An object that represents metadata for a resource.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual service.

provider (dict) --
The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.

virtualNode (dict) --
The virtual node associated with a virtual service.

virtualNodeName (string) --
The name of the virtual node that is acting as a service provider.



virtualRouter (dict) --
The virtual router associated with a virtual service.

virtualRouterName (string) --
The name of the virtual router that is acting as a service provider.







status (dict) --
The current status of the virtual service.

status (string) --
The current status of the virtual service.



virtualServiceName (string) --
The name of the virtual service.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualService': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'provider': {
                    'virtualNode': {
                        'virtualNodeName': 'string'
                    },
                    'virtualRouter': {
                        'virtualRouterName': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualServiceName': 'string'
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
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

def list_meshes(limit=None, nextToken=None):
    """
    Returns a list of existing service meshes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_meshes(
        limit=123,
        nextToken='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of results returned by ListMeshes in paginated output. When you use this parameter, ListMeshes returns only limit results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListMeshes request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListMeshes returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListMeshes request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.\n\nNote\nThis token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'meshes': [
        {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshName': 'string',
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'version': 123
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

meshes (list) --
The list of existing service meshes.

(dict) --
An object that represents a service mesh returned by a list operation.

arn (string) --
The full Amazon Resource Name (ARN) of the service mesh.

createdAt (datetime) --

lastUpdatedAt (datetime) --

meshName (string) --
The name of the service mesh.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

version (integer) --





nextToken (string) --
The nextToken value to include in a future ListMeshes request. When the results of a ListMeshes request exceed limit , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'meshes': [
            {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshName': 'string',
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'version': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_routes(limit=None, meshName=None, meshOwner=None, nextToken=None, virtualRouterName=None):
    """
    Returns a list of existing routes in a service mesh.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_routes(
        limit=123,
        meshName='string',
        meshOwner='string',
        nextToken='string',
        virtualRouterName='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of results returned by ListRoutes in paginated output. When you use this parameter, ListRoutes returns only limit results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListRoutes request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListRoutes returns up to 100 results and a nextToken value if applicable.

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to list routes in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListRoutes request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]\nThe name of the virtual router to list routes in.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'routes': [
        {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshName': 'string',
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'routeName': 'string',
            'version': 123,
            'virtualRouterName': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The nextToken value to include in a future ListRoutes request. When the results of a ListRoutes request exceed limit , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.

routes (list) --
The list of existing routes for the specified service mesh and virtual router.

(dict) --
An object that represents a route returned by a list operation.

arn (string) --
The full Amazon Resource Name (ARN) for the route.

createdAt (datetime) --

lastUpdatedAt (datetime) --

meshName (string) --
The name of the service mesh that the route resides in.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

routeName (string) --
The name of the route.

version (integer) --

virtualRouterName (string) --
The virtual router that the route is associated with.











Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'nextToken': 'string',
        'routes': [
            {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshName': 'string',
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'routeName': 'string',
                'version': 123,
                'virtualRouterName': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_tags_for_resource(limit=None, nextToken=None, resourceArn=None):
    """
    List the tags for an App Mesh resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        limit=123,
        nextToken='string',
        resourceArn='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of tag results returned by ListTagsForResource in paginated output. When this parameter is used, ListTagsForResource returns only limit results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListTagsForResource request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListTagsForResource returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListTagsForResource request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that identifies the resource to list the tags for.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The nextToken value to include in a future ListTagsForResource request. When the results of a ListTagsForResource request exceed limit , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.

tags (list) --
The tags for the resource.

(dict) --
Optional metadata that you apply to a resource to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

key (string) --
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

value (string) --
The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).











Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'nextToken': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_virtual_nodes(limit=None, meshName=None, meshOwner=None, nextToken=None):
    """
    Returns a list of existing virtual nodes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_virtual_nodes(
        limit=123,
        meshName='string',
        meshOwner='string',
        nextToken='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of results returned by ListVirtualNodes in paginated output. When you use this parameter, ListVirtualNodes returns only limit results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListVirtualNodes request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListVirtualNodes returns up to 100 results and a nextToken value if applicable.

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to list virtual nodes in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListVirtualNodes request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'virtualNodes': [
        {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshName': 'string',
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'version': 123,
            'virtualNodeName': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The nextToken value to include in a future ListVirtualNodes request. When the results of a ListVirtualNodes request exceed limit , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.

virtualNodes (list) --
The list of existing virtual nodes for the specified service mesh.

(dict) --
An object that represents a virtual node returned by a list operation.

arn (string) --
The full Amazon Resource Name (ARN) for the virtual node.

createdAt (datetime) --

lastUpdatedAt (datetime) --

meshName (string) --
The name of the service mesh that the virtual node resides in.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

version (integer) --

virtualNodeName (string) --
The name of the virtual node.











Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'nextToken': 'string',
        'virtualNodes': [
            {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshName': 'string',
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'version': 123,
                'virtualNodeName': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_virtual_routers(limit=None, meshName=None, meshOwner=None, nextToken=None):
    """
    Returns a list of existing virtual routers in a service mesh.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_virtual_routers(
        limit=123,
        meshName='string',
        meshOwner='string',
        nextToken='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of results returned by ListVirtualRouters in paginated output. When you use this parameter, ListVirtualRouters returns only limit results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListVirtualRouters request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListVirtualRouters returns up to 100 results and a nextToken value if applicable.

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to list virtual routers in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListVirtualRouters request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'virtualRouters': [
        {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshName': 'string',
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'version': 123,
            'virtualRouterName': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The nextToken value to include in a future ListVirtualRouters request. When the results of a ListVirtualRouters request exceed limit , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.

virtualRouters (list) --
The list of existing virtual routers for the specified service mesh.

(dict) --
An object that represents a virtual router returned by a list operation.

arn (string) --
The full Amazon Resource Name (ARN) for the virtual router.

createdAt (datetime) --

lastUpdatedAt (datetime) --

meshName (string) --
The name of the service mesh that the virtual router resides in.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

version (integer) --

virtualRouterName (string) --
The name of the virtual router.











Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'nextToken': 'string',
        'virtualRouters': [
            {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshName': 'string',
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'version': 123,
                'virtualRouterName': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_virtual_services(limit=None, meshName=None, meshOwner=None, nextToken=None):
    """
    Returns a list of existing virtual services in a service mesh.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_virtual_services(
        limit=123,
        meshName='string',
        meshOwner='string',
        nextToken='string'
    )
    
    
    :type limit: integer
    :param limit: The maximum number of results returned by ListVirtualServices in paginated output. When you use this parameter, ListVirtualServices returns only limit results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListVirtualServices request with the returned nextToken value. This value can be between 1 and 100. If you don\'t use this parameter, ListVirtualServices returns up to 100 results and a nextToken value if applicable.

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to list virtual services in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListVirtualServices request where limit was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'virtualServices': [
        {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshName': 'string',
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'version': 123,
            'virtualServiceName': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The nextToken value to include in a future ListVirtualServices request. When the results of a ListVirtualServices request exceed limit , you can use this value to retrieve the next page of results. This value is null when there are no more results to return.

virtualServices (list) --
The list of existing virtual services for the specified service mesh.

(dict) --
An object that represents a virtual service returned by a list operation.

arn (string) --
The full Amazon Resource Name (ARN) for the virtual service.

createdAt (datetime) --

lastUpdatedAt (datetime) --

meshName (string) --
The name of the service mesh that the virtual service resides in.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

version (integer) --

virtualServiceName (string) --
The name of the virtual service.











Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'nextToken': 'string',
        'virtualServices': [
            {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshName': 'string',
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'version': 123,
                'virtualServiceName': 'string'
            },
        ]
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Associates the specified tags to a resource with the specified resourceArn . If existing tags on a resource aren\'t specified in the request parameters, they aren\'t changed. When a resource is deleted, the tags associated with that resource are also deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to add tags to.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\n(dict) --Optional metadata that you apply to a resource to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nkey (string) -- [REQUIRED]One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nvalue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException
AppMesh.Client.exceptions.TooManyTagsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Deletes specified tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to delete tags from.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe keys of the tags to be removed.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_mesh(clientToken=None, meshName=None, spec=None):
    """
    Updates an existing service mesh.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_mesh(
        clientToken='string',
        meshName='string',
        spec={
            'egressFilter': {
                'type': 'ALLOW_ALL'|'DROP_ALL'
            }
        }
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh to update.\n

    :type spec: dict
    :param spec: The service mesh specification to apply.\n\negressFilter (dict) --The egress filter rules for the service mesh.\n\ntype (string) -- [REQUIRED]The egress filter type. By default, the type is DROP_ALL , which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to *.amazonaws.com for AWS API calls). You can set the egress filter type to ALLOW_ALL to allow egress to any endpoint inside or outside of the service mesh.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'mesh': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'egressFilter': {
                'type': 'ALLOW_ALL'|'DROP_ALL'
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        }
    }
}


Response Structure

(dict) --

mesh (dict) --
An object that represents a service mesh returned by a describe operation.

meshName (string) --
The name of the service mesh.

metadata (dict) --
The associated metadata for the service mesh.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The associated specification for the service mesh.

egressFilter (dict) --
The egress filter rules for the service mesh.

type (string) --
The egress filter type. By default, the type is DROP_ALL , which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to *.amazonaws.com for AWS API calls). You can set the egress filter type to ALLOW_ALL to allow egress to any endpoint inside or outside of the service mesh.





status (dict) --
The status of the service mesh.

status (string) --
The current mesh status.











Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'mesh': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'egressFilter': {
                    'type': 'ALLOW_ALL'|'DROP_ALL'
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            }
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ConflictException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def update_route(clientToken=None, meshName=None, meshOwner=None, routeName=None, spec=None, virtualRouterName=None):
    """
    Updates an existing route for a specified service mesh and virtual router.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_route(
        clientToken='string',
        meshName='string',
        meshOwner='string',
        routeName='string',
        spec={
            'grpcRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'metadata': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'methodName': 'string',
                    'serviceName': 'string'
                },
                'retryPolicy': {
                    'grpcRetryEvents': [
                        'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                    ],
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'http2Route': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'httpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'priority': 123,
            'tcpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                }
            }
        },
        virtualRouterName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh that the route resides in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type routeName: string
    :param routeName: [REQUIRED]\nThe name of the route to update.\n

    :type spec: dict
    :param spec: [REQUIRED]\nThe new route specification to apply. This overwrites the existing data.\n\ngrpcRoute (dict) --An object that represents the specification of a gRPC route.\n\naction (dict) -- [REQUIRED]An object that represents the action to take if a match is determined.\n\nweightedTargets (list) -- [REQUIRED]An object that represents the targets that traffic is routed to when a request matches the route.\n\n(dict) --An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.\n\nvirtualNode (string) -- [REQUIRED]The virtual node to associate with the weighted target.\n\nweight (integer) -- [REQUIRED]The relative weight of the weighted target.\n\n\n\n\n\n\n\nmatch (dict) -- [REQUIRED]An object that represents the criteria for determining a request match.\n\nmetadata (list) --An object that represents the data to match from the request.\n\n(dict) --An object that represents the match metadata for the route.\n\ninvert (boolean) --Specify True to match anything except the match criteria. The default value is False .\n\nmatch (dict) --An object that represents the data to match from the request.\n\nexact (string) --The value sent by the client must match the specified value exactly.\n\nprefix (string) --The value sent by the client must begin with the specified characters.\n\nrange (dict) --An object that represents the range of values to match on.\n\nend (integer) -- [REQUIRED]The end of the range.\n\nstart (integer) -- [REQUIRED]The start of the range.\n\n\n\nregex (string) --The value sent by the client must include the specified characters.\n\nsuffix (string) --The value sent by the client must end with the specified characters.\n\n\n\nname (string) -- [REQUIRED]The name of the route.\n\n\n\n\n\nmethodName (string) --The method name to match from the request. If you specify a name, you must also specify a serviceName .\n\nserviceName (string) --The fully qualified domain name for the service to match from the request.\n\n\n\nretryPolicy (dict) --An object that represents a retry policy.\n\ngrpcRetryEvents (list) --Specify at least one of the valid values.\n\n(string) --\n\n\nhttpRetryEvents (list) --Specify at least one of the following values.\n\nserver-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511\ngateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504\nclient-error \xe2\x80\x93 HTTP status code 409\nstream-error \xe2\x80\x93 Retry on refused stream\n\n\n(string) --\n\n\nmaxRetries (integer) -- [REQUIRED]The maximum number of retry attempts.\n\nperRetryTimeout (dict) -- [REQUIRED]An object that represents a duration of time.\n\nunit (string) --A unit of time.\n\nvalue (integer) --A number of time units.\n\n\n\ntcpRetryEvents (list) --Specify a valid value.\n\n(string) --\n\n\n\n\n\n\nhttp2Route (dict) --An object that represents the specification of an HTTP/2 route.\n\naction (dict) -- [REQUIRED]An object that represents the action to take if a match is determined.\n\nweightedTargets (list) -- [REQUIRED]An object that represents the targets that traffic is routed to when a request matches the route.\n\n(dict) --An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.\n\nvirtualNode (string) -- [REQUIRED]The virtual node to associate with the weighted target.\n\nweight (integer) -- [REQUIRED]The relative weight of the weighted target.\n\n\n\n\n\n\n\nmatch (dict) -- [REQUIRED]An object that represents the criteria for determining a request match.\n\nheaders (list) --An object that represents the client request headers to match on.\n\n(dict) --An object that represents the HTTP header in the request.\n\ninvert (boolean) --Specify True to match anything except the match criteria. The default value is False .\n\nmatch (dict) --The HeaderMatchMethod object.\n\nexact (string) --The value sent by the client must match the specified value exactly.\n\nprefix (string) --The value sent by the client must begin with the specified characters.\n\nrange (dict) --An object that represents the range of values to match on.\n\nend (integer) -- [REQUIRED]The end of the range.\n\nstart (integer) -- [REQUIRED]The start of the range.\n\n\n\nregex (string) --The value sent by the client must include the specified characters.\n\nsuffix (string) --The value sent by the client must end with the specified characters.\n\n\n\nname (string) -- [REQUIRED]A name for the HTTP header in the client request that will be matched on.\n\n\n\n\n\nmethod (string) --The client request method to match on. Specify only one.\n\nprefix (string) -- [REQUIRED]Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .\n\nscheme (string) --The client request scheme to match on. Specify only one.\n\n\n\nretryPolicy (dict) --An object that represents a retry policy.\n\nhttpRetryEvents (list) --Specify at least one of the following values.\n\nserver-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511\ngateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504\nclient-error \xe2\x80\x93 HTTP status code 409\nstream-error \xe2\x80\x93 Retry on refused stream\n\n\n(string) --\n\n\nmaxRetries (integer) -- [REQUIRED]The maximum number of retry attempts.\n\nperRetryTimeout (dict) -- [REQUIRED]An object that represents a duration of time.\n\nunit (string) --A unit of time.\n\nvalue (integer) --A number of time units.\n\n\n\ntcpRetryEvents (list) --Specify a valid value.\n\n(string) --\n\n\n\n\n\n\nhttpRoute (dict) --An object that represents the specification of an HTTP route.\n\naction (dict) -- [REQUIRED]An object that represents the action to take if a match is determined.\n\nweightedTargets (list) -- [REQUIRED]An object that represents the targets that traffic is routed to when a request matches the route.\n\n(dict) --An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.\n\nvirtualNode (string) -- [REQUIRED]The virtual node to associate with the weighted target.\n\nweight (integer) -- [REQUIRED]The relative weight of the weighted target.\n\n\n\n\n\n\n\nmatch (dict) -- [REQUIRED]An object that represents the criteria for determining a request match.\n\nheaders (list) --An object that represents the client request headers to match on.\n\n(dict) --An object that represents the HTTP header in the request.\n\ninvert (boolean) --Specify True to match anything except the match criteria. The default value is False .\n\nmatch (dict) --The HeaderMatchMethod object.\n\nexact (string) --The value sent by the client must match the specified value exactly.\n\nprefix (string) --The value sent by the client must begin with the specified characters.\n\nrange (dict) --An object that represents the range of values to match on.\n\nend (integer) -- [REQUIRED]The end of the range.\n\nstart (integer) -- [REQUIRED]The start of the range.\n\n\n\nregex (string) --The value sent by the client must include the specified characters.\n\nsuffix (string) --The value sent by the client must end with the specified characters.\n\n\n\nname (string) -- [REQUIRED]A name for the HTTP header in the client request that will be matched on.\n\n\n\n\n\nmethod (string) --The client request method to match on. Specify only one.\n\nprefix (string) -- [REQUIRED]Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .\n\nscheme (string) --The client request scheme to match on. Specify only one.\n\n\n\nretryPolicy (dict) --An object that represents a retry policy.\n\nhttpRetryEvents (list) --Specify at least one of the following values.\n\nserver-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511\ngateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504\nclient-error \xe2\x80\x93 HTTP status code 409\nstream-error \xe2\x80\x93 Retry on refused stream\n\n\n(string) --\n\n\nmaxRetries (integer) -- [REQUIRED]The maximum number of retry attempts.\n\nperRetryTimeout (dict) -- [REQUIRED]An object that represents a duration of time.\n\nunit (string) --A unit of time.\n\nvalue (integer) --A number of time units.\n\n\n\ntcpRetryEvents (list) --Specify a valid value.\n\n(string) --\n\n\n\n\n\n\npriority (integer) --The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority.\n\ntcpRoute (dict) --An object that represents the specification of a TCP route.\n\naction (dict) -- [REQUIRED]The action to take if a match is determined.\n\nweightedTargets (list) -- [REQUIRED]An object that represents the targets that traffic is routed to when a request matches the route.\n\n(dict) --An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.\n\nvirtualNode (string) -- [REQUIRED]The virtual node to associate with the weighted target.\n\nweight (integer) -- [REQUIRED]The relative weight of the weighted target.\n\n\n\n\n\n\n\n\n\n\n

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]\nThe name of the virtual router that the route is associated with.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'route': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'routeName': 'string',
        'spec': {
            'grpcRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'metadata': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'methodName': 'string',
                    'serviceName': 'string'
                },
                'retryPolicy': {
                    'grpcRetryEvents': [
                        'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                    ],
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'http2Route': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'httpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'headers': [
                        {
                            'invert': True|False,
                            'match': {
                                'exact': 'string',
                                'prefix': 'string',
                                'range': {
                                    'end': 123,
                                    'start': 123
                                },
                                'regex': 'string',
                                'suffix': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                    'prefix': 'string',
                    'scheme': 'http'|'https'
                },
                'retryPolicy': {
                    'httpRetryEvents': [
                        'string',
                    ],
                    'maxRetries': 123,
                    'perRetryTimeout': {
                        'unit': 'ms'|'s',
                        'value': 123
                    },
                    'tcpRetryEvents': [
                        'connection-error',
                    ]
                }
            },
            'priority': 123,
            'tcpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualRouterName': 'string'
    }
}


Response Structure

(dict) --

route (dict) --
A full description of the route that was updated.

meshName (string) --
The name of the service mesh that the route resides in.

metadata (dict) --
The associated metadata for the route.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



routeName (string) --
The name of the route.

spec (dict) --
The specifications of the route.

grpcRoute (dict) --
An object that represents the specification of a gRPC route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

metadata (list) --
An object that represents the data to match from the request.

(dict) --
An object that represents the match metadata for the route.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
An object that represents the data to match from the request.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
The name of the route.





methodName (string) --
The method name to match from the request. If you specify a name, you must also specify a serviceName .

serviceName (string) --
The fully qualified domain name for the service to match from the request.



retryPolicy (dict) --
An object that represents a retry policy.

grpcRetryEvents (list) --
Specify at least one of the valid values.

(string) --


httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






http2Route (dict) --
An object that represents the specification of an HTTP/2 route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

headers (list) --
An object that represents the client request headers to match on.

(dict) --
An object that represents the HTTP header in the request.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
The HeaderMatchMethod object.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
A name for the HTTP header in the client request that will be matched on.





method (string) --
The client request method to match on. Specify only one.

prefix (string) --
Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .

scheme (string) --
The client request scheme to match on. Specify only one.



retryPolicy (dict) --
An object that represents a retry policy.

httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






httpRoute (dict) --
An object that represents the specification of an HTTP route.

action (dict) --
An object that represents the action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.







match (dict) --
An object that represents the criteria for determining a request match.

headers (list) --
An object that represents the client request headers to match on.

(dict) --
An object that represents the HTTP header in the request.

invert (boolean) --
Specify True to match anything except the match criteria. The default value is False .

match (dict) --
The HeaderMatchMethod object.

exact (string) --
The value sent by the client must match the specified value exactly.

prefix (string) --
The value sent by the client must begin with the specified characters.

range (dict) --
An object that represents the range of values to match on.

end (integer) --
The end of the range.

start (integer) --
The start of the range.



regex (string) --
The value sent by the client must include the specified characters.

suffix (string) --
The value sent by the client must end with the specified characters.



name (string) --
A name for the HTTP header in the client request that will be matched on.





method (string) --
The client request method to match on. Specify only one.

prefix (string) --
Specifies the path to match requests with. This parameter must always start with / , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is my-service.local and you want the route to match requests to my-service.local/metrics , your prefix should be /metrics .

scheme (string) --
The client request scheme to match on. Specify only one.



retryPolicy (dict) --
An object that represents a retry policy.

httpRetryEvents (list) --
Specify at least one of the following values.

server-error \xe2\x80\x93 HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
gateway-error \xe2\x80\x93 HTTP status codes 502, 503, and 504
client-error \xe2\x80\x93 HTTP status code 409
stream-error \xe2\x80\x93 Retry on refused stream


(string) --


maxRetries (integer) --
The maximum number of retry attempts.

perRetryTimeout (dict) --
An object that represents a duration of time.

unit (string) --
A unit of time.

value (integer) --
A number of time units.



tcpRetryEvents (list) --
Specify a valid value.

(string) --






priority (integer) --
The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority.

tcpRoute (dict) --
An object that represents the specification of a TCP route.

action (dict) --
The action to take if a match is determined.

weightedTargets (list) --
An object that represents the targets that traffic is routed to when a request matches the route.

(dict) --
An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

virtualNode (string) --
The virtual node to associate with the weighted target.

weight (integer) --
The relative weight of the weighted target.











status (dict) --
The status of the route.

status (string) --
The current status for the route.



virtualRouterName (string) --
The virtual router that the route is associated with.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.LimitExceededException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'route': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'routeName': 'string',
            'spec': {
                'grpcRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'metadata': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'methodName': 'string',
                        'serviceName': 'string'
                    },
                    'retryPolicy': {
                        'grpcRetryEvents': [
                            'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                        ],
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'http2Route': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'headers': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                        'prefix': 'string',
                        'scheme': 'http'|'https'
                    },
                    'retryPolicy': {
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'httpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    },
                    'match': {
                        'headers': [
                            {
                                'invert': True|False,
                                'match': {
                                    'exact': 'string',
                                    'prefix': 'string',
                                    'range': {
                                        'end': 123,
                                        'start': 123
                                    },
                                    'regex': 'string',
                                    'suffix': 'string'
                                },
                                'name': 'string'
                            },
                        ],
                        'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                        'prefix': 'string',
                        'scheme': 'http'|'https'
                    },
                    'retryPolicy': {
                        'httpRetryEvents': [
                            'string',
                        ],
                        'maxRetries': 123,
                        'perRetryTimeout': {
                            'unit': 'ms'|'s',
                            'value': 123
                        },
                        'tcpRetryEvents': [
                            'connection-error',
                        ]
                    }
                },
                'priority': 123,
                'tcpRoute': {
                    'action': {
                        'weightedTargets': [
                            {
                                'virtualNode': 'string',
                                'weight': 123
                            },
                        ]
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_virtual_node(clientToken=None, meshName=None, meshOwner=None, spec=None, virtualNodeName=None):
    """
    Updates an existing virtual node in a specified service mesh.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_virtual_node(
        clientToken='string',
        meshName='string',
        meshOwner='string',
        spec={
            'backendDefaults': {
                'clientPolicy': {
                    'tls': {
                        'enforce': True|False,
                        'ports': [
                            123,
                        ],
                        'validation': {
                            'trust': {
                                'acm': {
                                    'certificateAuthorityArns': [
                                        'string',
                                    ]
                                },
                                'file': {
                                    'certificateChain': 'string'
                                }
                            }
                        }
                    }
                }
            },
            'backends': [
                {
                    'virtualService': {
                        'clientPolicy': {
                            'tls': {
                                'enforce': True|False,
                                'ports': [
                                    123,
                                ],
                                'validation': {
                                    'trust': {
                                        'acm': {
                                            'certificateAuthorityArns': [
                                                'string',
                                            ]
                                        },
                                        'file': {
                                            'certificateChain': 'string'
                                        }
                                    }
                                }
                            }
                        },
                        'virtualServiceName': 'string'
                    }
                },
            ],
            'listeners': [
                {
                    'healthCheck': {
                        'healthyThreshold': 123,
                        'intervalMillis': 123,
                        'path': 'string',
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp',
                        'timeoutMillis': 123,
                        'unhealthyThreshold': 123
                    },
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    },
                    'tls': {
                        'certificate': {
                            'acm': {
                                'certificateArn': 'string'
                            },
                            'file': {
                                'certificateChain': 'string',
                                'privateKey': 'string'
                            }
                        },
                        'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                    }
                },
            ],
            'logging': {
                'accessLog': {
                    'file': {
                        'path': 'string'
                    }
                }
            },
            'serviceDiscovery': {
                'awsCloudMap': {
                    'attributes': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'namespaceName': 'string',
                    'serviceName': 'string'
                },
                'dns': {
                    'hostname': 'string'
                }
            }
        },
        virtualNodeName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh that the virtual node resides in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type spec: dict
    :param spec: [REQUIRED]\nThe new virtual node specification to apply. This overwrites the existing data.\n\nbackendDefaults (dict) --A reference to an object that represents the defaults for backends.\n\nclientPolicy (dict) --A reference to an object that represents a client policy.\n\ntls (dict) --A reference to an object that represents a Transport Layer Security (TLS) client policy.\n\nenforce (boolean) --Whether the policy is enforced. The default is True , if a value isn\'t specified.\n\nports (list) --One or more ports that the policy is enforced for.\n\n(integer) --\n\n\nvalidation (dict) -- [REQUIRED]A reference to an object that represents a TLS validation context.\n\ntrust (dict) -- [REQUIRED]A reference to an object that represents a TLS validation context trust.\n\nacm (dict) --A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.\n\ncertificateAuthorityArns (list) -- [REQUIRED]One or more ACM Amazon Resource Name (ARN)s.\n\n(string) --\n\n\n\n\nfile (dict) --An object that represents a TLS validation context trust for a local file.\n\ncertificateChain (string) -- [REQUIRED]The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.\n\n\n\n\n\n\n\n\n\n\n\n\n\nbackends (list) --The backends that the virtual node is expected to send outbound traffic to.\n\n(dict) --An object that represents the backends that a virtual node is expected to send outbound traffic to.\n\nvirtualService (dict) --Specifies a virtual service to use as a backend for a virtual node.\n\nclientPolicy (dict) --A reference to an object that represents the client policy for a backend.\n\ntls (dict) --A reference to an object that represents a Transport Layer Security (TLS) client policy.\n\nenforce (boolean) --Whether the policy is enforced. The default is True , if a value isn\'t specified.\n\nports (list) --One or more ports that the policy is enforced for.\n\n(integer) --\n\n\nvalidation (dict) -- [REQUIRED]A reference to an object that represents a TLS validation context.\n\ntrust (dict) -- [REQUIRED]A reference to an object that represents a TLS validation context trust.\n\nacm (dict) --A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.\n\ncertificateAuthorityArns (list) -- [REQUIRED]One or more ACM Amazon Resource Name (ARN)s.\n\n(string) --\n\n\n\n\nfile (dict) --An object that represents a TLS validation context trust for a local file.\n\ncertificateChain (string) -- [REQUIRED]The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.\n\n\n\n\n\n\n\n\n\n\n\nvirtualServiceName (string) -- [REQUIRED]The name of the virtual service that is acting as a virtual node backend.\n\n\n\n\n\n\n\nlisteners (list) --The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.\n\n(dict) --An object that represents a listener for a virtual node.\n\nhealthCheck (dict) --The health check information for the listener.\n\nhealthyThreshold (integer) -- [REQUIRED]The number of consecutive successful health checks that must occur before declaring listener healthy.\n\nintervalMillis (integer) -- [REQUIRED]The time period in milliseconds between each health check execution.\n\npath (string) --The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.\n\nport (integer) --The destination port for the health check request. This port must match the port defined in the PortMapping for the listener.\n\nprotocol (string) -- [REQUIRED]The protocol for the health check request. If you specify grpc , then your service must conform to the GRPC Health Checking Protocol .\n\ntimeoutMillis (integer) -- [REQUIRED]The amount of time to wait when receiving a response from the health check, in milliseconds.\n\nunhealthyThreshold (integer) -- [REQUIRED]The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.\n\n\n\nportMapping (dict) -- [REQUIRED]The port mapping information for the listener.\n\nport (integer) -- [REQUIRED]The port used for the port mapping.\n\nprotocol (string) -- [REQUIRED]The protocol used for the port mapping. Specify one protocol.\n\n\n\ntls (dict) --A reference to an object that represents the Transport Layer Security (TLS) properties for a listener.\n\ncertificate (dict) -- [REQUIRED]A reference to an object that represents a listener\'s TLS certificate.\n\nacm (dict) --A reference to an object that represents an AWS Certicate Manager (ACM) certificate.\n\ncertificateArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) for the certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see Transport Layer Security (TLS) .\n\n\n\nfile (dict) --A reference to an object that represents a local file certificate.\n\ncertificateChain (string) -- [REQUIRED]The certificate chain for the certificate.\n\nprivateKey (string) -- [REQUIRED]The private key for a certificate stored on the file system of the virtual node that the proxy is running on.\n\n\n\n\n\nmode (string) -- [REQUIRED]Specify one of the following modes.\n\nSTRICT \xe2\x80\x93 Listener only accepts connections with TLS enabled.\nPERMISSIVE \xe2\x80\x93 Listener accepts connections with or without TLS enabled.\nDISABLED \xe2\x80\x93 Listener only accepts connections without TLS.\n\n\n\n\n\n\n\n\nlogging (dict) --The inbound and outbound access logging information for the virtual node.\n\naccessLog (dict) --The access log configuration for a virtual node.\n\nfile (dict) --The file object to send virtual node access logs to.\n\npath (string) -- [REQUIRED]The file path to write access logs to. You can use /dev/stdout to send access logs to standard out and configure your Envoy container to use a log driver, such as awslogs , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container\'s file system to write the files to disk.\n\nNote\nThe Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.\n\n\n\n\n\n\n\n\nserviceDiscovery (dict) --The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a listener , then you must specify service discovery information.\n\nawsCloudMap (dict) --Specifies any AWS Cloud Map information for the virtual node.\n\nattributes (list) --A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.\n\n(dict) --An object that represents the AWS Cloud Map attribute information for your virtual node.\n\nkey (string) -- [REQUIRED]The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.\n\nvalue (string) -- [REQUIRED]The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.\n\n\n\n\n\nnamespaceName (string) -- [REQUIRED]The name of the AWS Cloud Map namespace to use.\n\nserviceName (string) -- [REQUIRED]The name of the AWS Cloud Map service to use.\n\n\n\ndns (dict) --Specifies the DNS information for the virtual node.\n\nhostname (string) -- [REQUIRED]Specifies the DNS service discovery hostname for the virtual node.\n\n\n\n\n\n\n

    :type virtualNodeName: string
    :param virtualNodeName: [REQUIRED]\nThe name of the virtual node to update.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualNode': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'backendDefaults': {
                'clientPolicy': {
                    'tls': {
                        'enforce': True|False,
                        'ports': [
                            123,
                        ],
                        'validation': {
                            'trust': {
                                'acm': {
                                    'certificateAuthorityArns': [
                                        'string',
                                    ]
                                },
                                'file': {
                                    'certificateChain': 'string'
                                }
                            }
                        }
                    }
                }
            },
            'backends': [
                {
                    'virtualService': {
                        'clientPolicy': {
                            'tls': {
                                'enforce': True|False,
                                'ports': [
                                    123,
                                ],
                                'validation': {
                                    'trust': {
                                        'acm': {
                                            'certificateAuthorityArns': [
                                                'string',
                                            ]
                                        },
                                        'file': {
                                            'certificateChain': 'string'
                                        }
                                    }
                                }
                            }
                        },
                        'virtualServiceName': 'string'
                    }
                },
            ],
            'listeners': [
                {
                    'healthCheck': {
                        'healthyThreshold': 123,
                        'intervalMillis': 123,
                        'path': 'string',
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp',
                        'timeoutMillis': 123,
                        'unhealthyThreshold': 123
                    },
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    },
                    'tls': {
                        'certificate': {
                            'acm': {
                                'certificateArn': 'string'
                            },
                            'file': {
                                'certificateChain': 'string',
                                'privateKey': 'string'
                            }
                        },
                        'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                    }
                },
            ],
            'logging': {
                'accessLog': {
                    'file': {
                        'path': 'string'
                    }
                }
            },
            'serviceDiscovery': {
                'awsCloudMap': {
                    'attributes': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'namespaceName': 'string',
                    'serviceName': 'string'
                },
                'dns': {
                    'hostname': 'string'
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualNodeName': 'string'
    }
}


Response Structure

(dict) --

virtualNode (dict) --
A full description of the virtual node that was updated.

meshName (string) --
The name of the service mesh that the virtual node resides in.

metadata (dict) --
The associated metadata for the virtual node.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual node.

backendDefaults (dict) --
A reference to an object that represents the defaults for backends.

clientPolicy (dict) --
A reference to an object that represents a client policy.

tls (dict) --
A reference to an object that represents a Transport Layer Security (TLS) client policy.

enforce (boolean) --
Whether the policy is enforced. The default is True , if a value isn\'t specified.

ports (list) --
One or more ports that the policy is enforced for.

(integer) --


validation (dict) --
A reference to an object that represents a TLS validation context.

trust (dict) --
A reference to an object that represents a TLS validation context trust.

acm (dict) --
A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.

certificateAuthorityArns (list) --
One or more ACM Amazon Resource Name (ARN)s.

(string) --




file (dict) --
An object that represents a TLS validation context trust for a local file.

certificateChain (string) --
The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.













backends (list) --
The backends that the virtual node is expected to send outbound traffic to.

(dict) --
An object that represents the backends that a virtual node is expected to send outbound traffic to.

virtualService (dict) --
Specifies a virtual service to use as a backend for a virtual node.

clientPolicy (dict) --
A reference to an object that represents the client policy for a backend.

tls (dict) --
A reference to an object that represents a Transport Layer Security (TLS) client policy.

enforce (boolean) --
Whether the policy is enforced. The default is True , if a value isn\'t specified.

ports (list) --
One or more ports that the policy is enforced for.

(integer) --


validation (dict) --
A reference to an object that represents a TLS validation context.

trust (dict) --
A reference to an object that represents a TLS validation context trust.

acm (dict) --
A reference to an object that represents a TLS validation context trust for an AWS Certicate Manager (ACM) certificate.

certificateAuthorityArns (list) --
One or more ACM Amazon Resource Name (ARN)s.

(string) --




file (dict) --
An object that represents a TLS validation context trust for a local file.

certificateChain (string) --
The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.











virtualServiceName (string) --
The name of the virtual service that is acting as a virtual node backend.







listeners (list) --
The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.

(dict) --
An object that represents a listener for a virtual node.

healthCheck (dict) --
The health check information for the listener.

healthyThreshold (integer) --
The number of consecutive successful health checks that must occur before declaring listener healthy.

intervalMillis (integer) --
The time period in milliseconds between each health check execution.

path (string) --
The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.

port (integer) --
The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.

protocol (string) --
The protocol for the health check request. If you specify grpc , then your service must conform to the GRPC Health Checking Protocol .

timeoutMillis (integer) --
The amount of time to wait when receiving a response from the health check, in milliseconds.

unhealthyThreshold (integer) --
The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.



portMapping (dict) --
The port mapping information for the listener.

port (integer) --
The port used for the port mapping.

protocol (string) --
The protocol used for the port mapping. Specify one protocol.



tls (dict) --
A reference to an object that represents the Transport Layer Security (TLS) properties for a listener.

certificate (dict) --
A reference to an object that represents a listener\'s TLS certificate.

acm (dict) --
A reference to an object that represents an AWS Certicate Manager (ACM) certificate.

certificateArn (string) --
The Amazon Resource Name (ARN) for the certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see Transport Layer Security (TLS) .



file (dict) --
A reference to an object that represents a local file certificate.

certificateChain (string) --
The certificate chain for the certificate.

privateKey (string) --
The private key for a certificate stored on the file system of the virtual node that the proxy is running on.





mode (string) --
Specify one of the following modes.

STRICT \xe2\x80\x93 Listener only accepts connections with TLS enabled.
PERMISSIVE \xe2\x80\x93 Listener accepts connections with or without TLS enabled.
DISABLED \xe2\x80\x93 Listener only accepts connections without TLS.








logging (dict) --
The inbound and outbound access logging information for the virtual node.

accessLog (dict) --
The access log configuration for a virtual node.

file (dict) --
The file object to send virtual node access logs to.

path (string) --
The file path to write access logs to. You can use /dev/stdout to send access logs to standard out and configure your Envoy container to use a log driver, such as awslogs , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container\'s file system to write the files to disk.

Note
The Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.








serviceDiscovery (dict) --
The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a listener , then you must specify service discovery information.

awsCloudMap (dict) --
Specifies any AWS Cloud Map information for the virtual node.

attributes (list) --
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.

(dict) --
An object that represents the AWS Cloud Map attribute information for your virtual node.

key (string) --
The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.

value (string) --
The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service instance that contains the specified key and value is returned.





namespaceName (string) --
The name of the AWS Cloud Map namespace to use.

serviceName (string) --
The name of the AWS Cloud Map service to use.



dns (dict) --
Specifies the DNS information for the virtual node.

hostname (string) --
Specifies the DNS service discovery hostname for the virtual node.







status (dict) --
The current status for the virtual node.

status (string) --
The current status of the virtual node.



virtualNodeName (string) --
The name of the virtual node.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.LimitExceededException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualNode': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'backendDefaults': {
                    'clientPolicy': {
                        'tls': {
                            'enforce': True|False,
                            'ports': [
                                123,
                            ],
                            'validation': {
                                'trust': {
                                    'acm': {
                                        'certificateAuthorityArns': [
                                            'string',
                                        ]
                                    },
                                    'file': {
                                        'certificateChain': 'string'
                                    }
                                }
                            }
                        }
                    }
                },
                'backends': [
                    {
                        'virtualService': {
                            'clientPolicy': {
                                'tls': {
                                    'enforce': True|False,
                                    'ports': [
                                        123,
                                    ],
                                    'validation': {
                                        'trust': {
                                            'acm': {
                                                'certificateAuthorityArns': [
                                                    'string',
                                                ]
                                            },
                                            'file': {
                                                'certificateChain': 'string'
                                            }
                                        }
                                    }
                                }
                            },
                            'virtualServiceName': 'string'
                        }
                    },
                ],
                'listeners': [
                    {
                        'healthCheck': {
                            'healthyThreshold': 123,
                            'intervalMillis': 123,
                            'path': 'string',
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp',
                            'timeoutMillis': 123,
                            'unhealthyThreshold': 123
                        },
                        'portMapping': {
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp'
                        },
                        'tls': {
                            'certificate': {
                                'acm': {
                                    'certificateArn': 'string'
                                },
                                'file': {
                                    'certificateChain': 'string',
                                    'privateKey': 'string'
                                }
                            },
                            'mode': 'DISABLED'|'PERMISSIVE'|'STRICT'
                        }
                    },
                ],
                'logging': {
                    'accessLog': {
                        'file': {
                            'path': 'string'
                        }
                    }
                },
                'serviceDiscovery': {
                    'awsCloudMap': {
                        'attributes': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'namespaceName': 'string',
                        'serviceName': 'string'
                    },
                    'dns': {
                        'hostname': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualNodeName': 'string'
        }
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def update_virtual_router(clientToken=None, meshName=None, meshOwner=None, spec=None, virtualRouterName=None):
    """
    Updates an existing virtual router in a specified service mesh.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_virtual_router(
        clientToken='string',
        meshName='string',
        meshOwner='string',
        spec={
            'listeners': [
                {
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    }
                },
            ]
        },
        virtualRouterName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh that the virtual router resides in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type spec: dict
    :param spec: [REQUIRED]\nThe new virtual router specification to apply. This overwrites the existing data.\n\nlisteners (list) --The listeners that the virtual router is expected to receive inbound traffic from. You can specify one listener.\n\n(dict) --An object that represents a virtual router listener.\n\nportMapping (dict) -- [REQUIRED]An object that represents a port mapping.\n\nport (integer) -- [REQUIRED]The port used for the port mapping.\n\nprotocol (string) -- [REQUIRED]The protocol used for the port mapping. Specify one protocol.\n\n\n\n\n\n\n\n\n

    :type virtualRouterName: string
    :param virtualRouterName: [REQUIRED]\nThe name of the virtual router to update.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualRouter': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'listeners': [
                {
                    'portMapping': {
                        'port': 123,
                        'protocol': 'grpc'|'http'|'http2'|'tcp'
                    }
                },
            ]
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualRouterName': 'string'
    }
}


Response Structure

(dict) --

virtualRouter (dict) --
A full description of the virtual router that was updated.

meshName (string) --
The name of the service mesh that the virtual router resides in.

metadata (dict) --
The associated metadata for the virtual router.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual router.

listeners (list) --
The listeners that the virtual router is expected to receive inbound traffic from. You can specify one listener.

(dict) --
An object that represents a virtual router listener.

portMapping (dict) --
An object that represents a port mapping.

port (integer) --
The port used for the port mapping.

protocol (string) --
The protocol used for the port mapping. Specify one protocol.









status (dict) --
The current status of the virtual router.

status (string) --
The current status of the virtual router.



virtualRouterName (string) --
The name of the virtual router.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.LimitExceededException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualRouter': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'listeners': [
                    {
                        'portMapping': {
                            'port': 123,
                            'protocol': 'grpc'|'http'|'http2'|'tcp'
                        }
                    },
                ]
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualRouterName': 'string'
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ConflictException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.LimitExceededException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

def update_virtual_service(clientToken=None, meshName=None, meshOwner=None, spec=None, virtualServiceName=None):
    """
    Updates an existing virtual service in a specified service mesh.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_virtual_service(
        clientToken='string',
        meshName='string',
        meshOwner='string',
        spec={
            'provider': {
                'virtualNode': {
                    'virtualNodeName': 'string'
                },
                'virtualRouter': {
                    'virtualRouterName': 'string'
                }
            }
        },
        virtualServiceName='string'
    )
    
    
    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.\nThis field is autopopulated if not provided.\n

    :type meshName: string
    :param meshName: [REQUIRED]\nThe name of the service mesh that the virtual service resides in.\n

    :type meshOwner: string
    :param meshOwner: The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

    :type spec: dict
    :param spec: [REQUIRED]\nThe new virtual service specification to apply. This overwrites the existing data.\n\nprovider (dict) --The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.\n\nvirtualNode (dict) --The virtual node associated with a virtual service.\n\nvirtualNodeName (string) -- [REQUIRED]The name of the virtual node that is acting as a service provider.\n\n\n\nvirtualRouter (dict) --The virtual router associated with a virtual service.\n\nvirtualRouterName (string) -- [REQUIRED]The name of the virtual router that is acting as a service provider.\n\n\n\n\n\n\n

    :type virtualServiceName: string
    :param virtualServiceName: [REQUIRED]\nThe name of the virtual service to update.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'virtualService': {
        'meshName': 'string',
        'metadata': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'meshOwner': 'string',
            'resourceOwner': 'string',
            'uid': 'string',
            'version': 123
        },
        'spec': {
            'provider': {
                'virtualNode': {
                    'virtualNodeName': 'string'
                },
                'virtualRouter': {
                    'virtualRouterName': 'string'
                }
            }
        },
        'status': {
            'status': 'ACTIVE'|'DELETED'|'INACTIVE'
        },
        'virtualServiceName': 'string'
    }
}


Response Structure

(dict) --

virtualService (dict) --
A full description of the virtual service that was updated.

meshName (string) --
The name of the service mesh that the virtual service resides in.

metadata (dict) --
An object that represents metadata for a resource.

arn (string) --
The full Amazon Resource Name (ARN) for the resource.

createdAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt (datetime) --
The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner (string) --
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it\'s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see Working with Shared Meshes .

resourceOwner (string) --
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it\'s the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see Working with Shared Meshes .

uid (string) --
The unique identifier for the resource.

version (integer) --
The version of the resource. Resources are created at version 1, and this version is incremented each time that they\'re updated.



spec (dict) --
The specifications of the virtual service.

provider (dict) --
The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.

virtualNode (dict) --
The virtual node associated with a virtual service.

virtualNodeName (string) --
The name of the virtual node that is acting as a service provider.



virtualRouter (dict) --
The virtual router associated with a virtual service.

virtualRouterName (string) --
The name of the virtual router that is acting as a service provider.







status (dict) --
The current status of the virtual service.

status (string) --
The current status of the virtual service.



virtualServiceName (string) --
The name of the virtual service.









Exceptions

AppMesh.Client.exceptions.BadRequestException
AppMesh.Client.exceptions.ConflictException
AppMesh.Client.exceptions.ForbiddenException
AppMesh.Client.exceptions.InternalServerErrorException
AppMesh.Client.exceptions.LimitExceededException
AppMesh.Client.exceptions.NotFoundException
AppMesh.Client.exceptions.ServiceUnavailableException
AppMesh.Client.exceptions.TooManyRequestsException


    :return: {
        'virtualService': {
            'meshName': 'string',
            'metadata': {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'meshOwner': 'string',
                'resourceOwner': 'string',
                'uid': 'string',
                'version': 123
            },
            'spec': {
                'provider': {
                    'virtualNode': {
                        'virtualNodeName': 'string'
                    },
                    'virtualRouter': {
                        'virtualRouterName': 'string'
                    }
                }
            },
            'status': {
                'status': 'ACTIVE'|'DELETED'|'INACTIVE'
            },
            'virtualServiceName': 'string'
        }
    }
    
    
    :returns: 
    AppMesh.Client.exceptions.BadRequestException
    AppMesh.Client.exceptions.ConflictException
    AppMesh.Client.exceptions.ForbiddenException
    AppMesh.Client.exceptions.InternalServerErrorException
    AppMesh.Client.exceptions.LimitExceededException
    AppMesh.Client.exceptions.NotFoundException
    AppMesh.Client.exceptions.ServiceUnavailableException
    AppMesh.Client.exceptions.TooManyRequestsException
    
    """
    pass

