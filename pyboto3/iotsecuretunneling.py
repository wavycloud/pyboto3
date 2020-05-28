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

def close_tunnel(tunnelId=None, delete=None):
    """
    Closes a tunnel identified by the unique tunnel id. When a CloseTunnel request is received, we close the WebSocket connections between the client and proxy server so no data can be transmitted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.close_tunnel(
        tunnelId='string',
        delete=True|False
    )
    
    
    :type tunnelId: string
    :param tunnelId: [REQUIRED]\nThe ID of the tunnel to close.\n

    :type delete: boolean
    :param delete: When set to true, AWS IoT Secure Tunneling deletes the tunnel data immediately.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSecureTunneling.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_tunnel(tunnelId=None):
    """
    Gets information about a tunnel identified by the unique tunnel id.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_tunnel(
        tunnelId='string'
    )
    
    
    :type tunnelId: string
    :param tunnelId: [REQUIRED]\nThe tunnel to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tunnel': {
        'tunnelId': 'string',
        'tunnelArn': 'string',
        'status': 'OPEN'|'CLOSED',
        'sourceConnectionState': {
            'status': 'CONNECTED'|'DISCONNECTED',
            'lastUpdatedAt': datetime(2015, 1, 1)
        },
        'destinationConnectionState': {
            'status': 'CONNECTED'|'DISCONNECTED',
            'lastUpdatedAt': datetime(2015, 1, 1)
        },
        'description': 'string',
        'destinationConfig': {
            'thingName': 'string',
            'services': [
                'string',
            ]
        },
        'timeoutConfig': {
            'maxLifetimeTimeoutMinutes': 123
        },
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'createdAt': datetime(2015, 1, 1),
        'lastUpdatedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
tunnel (dict) --The tunnel being described.

tunnelId (string) --A unique alpha-numeric ID that identifies a tunnel.

tunnelArn (string) --The Amazon Resource Name (ARN) of a tunnel. The tunnel ARN format is arn:aws:tunnel:<region>:<account-id>:tunnel/<tunnel-id>

status (string) --The status of a tunnel. Valid values are: Open and Closed.

sourceConnectionState (dict) --The connection state of the source application.

status (string) --The connection status of the tunnel. Valid values are CONNECTED and DISCONNECTED .

lastUpdatedAt (datetime) --The last time the connection status was updated.



destinationConnectionState (dict) --The connection state of the destination application.

status (string) --The connection status of the tunnel. Valid values are CONNECTED and DISCONNECTED .

lastUpdatedAt (datetime) --The last time the connection status was updated.



description (string) --A description of the tunnel.

destinationConfig (dict) --The destination configuration that specifies the thing name of the destination device and a service name that the local proxy uses to connect to the destination application.

thingName (string) --The name of the IoT thing to which you want to connect.

services (list) --A list of service names that identity the target application. Currently, you can only specify a single name. The AWS IoT client running on the destination device reads this value and uses it to look up a port or an IP address and a port. The AWS IoT client instantiates the local proxy which uses this information to connect to the destination application.

(string) --




timeoutConfig (dict) --Timeout configuration for the tunnel.

maxLifetimeTimeoutMinutes (integer) --The maximum amount of time (in minutes) a tunnel can remain open. If not specified, maxLifetimeTimeoutMinutes defaults to 720 minutes. Valid values are from 1 minute to 12 hours (720 minutes)



tags (list) --A list of tag metadata associated with the secure tunnel.

(dict) --An arbitary key/value pair used to add searchable metadata to secure tunnel resources.

key (string) --The key of the tag.

value (string) --The value of the tag.





createdAt (datetime) --The time when the tunnel was created.

lastUpdatedAt (datetime) --The last time the tunnel was updated.








Exceptions

IoTSecureTunneling.Client.exceptions.ResourceNotFoundException


    :return: {
        'tunnel': {
            'tunnelId': 'string',
            'tunnelArn': 'string',
            'status': 'OPEN'|'CLOSED',
            'sourceConnectionState': {
                'status': 'CONNECTED'|'DISCONNECTED',
                'lastUpdatedAt': datetime(2015, 1, 1)
            },
            'destinationConnectionState': {
                'status': 'CONNECTED'|'DISCONNECTED',
                'lastUpdatedAt': datetime(2015, 1, 1)
            },
            'description': 'string',
            'destinationConfig': {
                'thingName': 'string',
                'services': [
                    'string',
                ]
            },
            'timeoutConfig': {
                'maxLifetimeTimeoutMinutes': 123
            },
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IoTSecureTunneling.Client.exceptions.ResourceNotFoundException
    
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

def list_tags_for_resource(resourceArn=None):
    """
    Lists the tags for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe resource ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
tags (list) --The tags for the specified resource.

(dict) --An arbitary key/value pair used to add searchable metadata to secure tunnel resources.

key (string) --The key of the tag.

value (string) --The value of the tag.










Exceptions

IoTSecureTunneling.Client.exceptions.ResourceNotFoundException


    :return: {
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_tunnels(thingName=None, maxResults=None, nextToken=None):
    """
    List all tunnels for an AWS account. Tunnels are listed by creation time in descending order, newer tunnels will be listed before older tunnels.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tunnels(
        thingName='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type thingName: string
    :param thingName: The name of the IoT thing associated with the destination device.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at once.

    :type nextToken: string
    :param nextToken: A token to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'tunnelSummaries': [
        {
            'tunnelId': 'string',
            'tunnelArn': 'string',
            'status': 'OPEN'|'CLOSED',
            'description': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

tunnelSummaries (list) --
A short description of the tunnels in an AWS account.

(dict) --
Information about the tunnel.

tunnelId (string) --
The unique alpha-numeric identifier for the tunnel.

tunnelArn (string) --
The Amazon Resource Name of the tunnel. The tunnel ARN format is arn:aws:tunnel:<region>:<account-id>:tunnel/<tunnel-id>

status (string) --
The status of a tunnel. Valid values are: Open and Closed.

description (string) --
A description of the tunnel.

createdAt (datetime) --
The time the tunnel was created.

lastUpdatedAt (datetime) --
The time the tunnel was last updated.





nextToken (string) --
A token to used to retrieve the next set of results.








    :return: {
        'tunnelSummaries': [
            {
                'tunnelId': 'string',
                'tunnelArn': 'string',
                'status': 'OPEN'|'CLOSED',
                'description': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def open_tunnel(description=None, tags=None, destinationConfig=None, timeoutConfig=None):
    """
    Creates a new tunnel, and returns two client access tokens for clients to use to connect to the AWS IoT Secure Tunneling proxy server. .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.open_tunnel(
        description='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        destinationConfig={
            'thingName': 'string',
            'services': [
                'string',
            ]
        },
        timeoutConfig={
            'maxLifetimeTimeoutMinutes': 123
        }
    )
    
    
    :type description: string
    :param description: A short text description of the tunnel.

    :type tags: list
    :param tags: A collection of tag metadata.\n\n(dict) --An arbitary key/value pair used to add searchable metadata to secure tunnel resources.\n\nkey (string) -- [REQUIRED]The key of the tag.\n\nvalue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :type destinationConfig: dict
    :param destinationConfig: The destination configuration for the OpenTunnel request.\n\nthingName (string) -- [REQUIRED]The name of the IoT thing to which you want to connect.\n\nservices (list) -- [REQUIRED]A list of service names that identity the target application. Currently, you can only specify a single name. The AWS IoT client running on the destination device reads this value and uses it to look up a port or an IP address and a port. The AWS IoT client instantiates the local proxy which uses this information to connect to the destination application.\n\n(string) --\n\n\n\n

    :type timeoutConfig: dict
    :param timeoutConfig: Timeout configuration for a tunnel.\n\nmaxLifetimeTimeoutMinutes (integer) --The maximum amount of time (in minutes) a tunnel can remain open. If not specified, maxLifetimeTimeoutMinutes defaults to 720 minutes. Valid values are from 1 minute to 12 hours (720 minutes)\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'tunnelId': 'string',
    'tunnelArn': 'string',
    'sourceAccessToken': 'string',
    'destinationAccessToken': 'string'
}


Response Structure

(dict) --

tunnelId (string) --
A unique alpha-numeric tunnel ID.

tunnelArn (string) --
The Amazon Resource Name for the tunnel. The tunnel ARN format is arn:aws:tunnel:<region>:<account-id>:tunnel/<tunnel-id>

sourceAccessToken (string) --
The access token the source local proxy uses to connect to AWS IoT Secure Tunneling.

destinationAccessToken (string) --
The access token the destination local proxy uses to connect to AWS IoT Secure Tunneling.







Exceptions

IoTSecureTunneling.Client.exceptions.LimitExceededException


    :return: {
        'tunnelId': 'string',
        'tunnelArn': 'string',
        'sourceAccessToken': 'string',
        'destinationAccessToken': 'string'
    }
    
    
    :returns: 
    IoTSecureTunneling.Client.exceptions.LimitExceededException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    A resource tag.
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
    :param resourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe tags for the resource.\n\n(dict) --An arbitary key/value pair used to add searchable metadata to secure tunnel resources.\n\nkey (string) -- [REQUIRED]The key of the tag.\n\nvalue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSecureTunneling.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes a tag from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe resource ARN.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe keys of the tags to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSecureTunneling.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

