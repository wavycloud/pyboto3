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

def delete_connection(ConnectionId=None):
    """
    Delete the connection with the provided id.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_connection(
        ConnectionId='string'
    )
    
    
    :type ConnectionId: string
    :param ConnectionId: [REQUIRED]

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

def get_connection(ConnectionId=None):
    """
    Get information about the connection with the provided id.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_connection(
        ConnectionId='string'
    )
    
    
    :type ConnectionId: string
    :param ConnectionId: [REQUIRED]

    :rtype: dict
ReturnsResponse Syntax{
    'ConnectedAt': datetime(2015, 1, 1),
    'Identity': {
        'SourceIp': 'string',
        'UserAgent': 'string'
    },
    'LastActiveAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
ConnectedAt (datetime) --The time in ISO 8601 format for when the connection was established.

Identity (dict) --
SourceIp (string) --The source IP address of the TCP connection making the request to API Gateway.

UserAgent (string) --The User Agent of the API caller.



LastActiveAt (datetime) --The time in ISO 8601 format for when the connection was last active.






Exceptions

ApiGatewayManagementApi.Client.exceptions.GoneException
ApiGatewayManagementApi.Client.exceptions.LimitExceededException
ApiGatewayManagementApi.Client.exceptions.ForbiddenException


    :return: {
        'ConnectedAt': datetime(2015, 1, 1),
        'Identity': {
            'SourceIp': 'string',
            'UserAgent': 'string'
        },
        'LastActiveAt': datetime(2015, 1, 1)
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

def post_to_connection(Data=None, ConnectionId=None):
    """
    Sends the provided data to the specified connection.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.post_to_connection(
        Data=b'bytes'|file,
        ConnectionId='string'
    )
    
    
    :type Data: bytes or seekable file-like object
    :param Data: [REQUIRED]\nThe data to be sent to the client specified by its connection id.\n

    :type ConnectionId: string
    :param ConnectionId: [REQUIRED]\nThe identifier of the connection that a specific client is using.\n

    :returns: 
    ApiGatewayManagementApi.Client.exceptions.GoneException
    ApiGatewayManagementApi.Client.exceptions.LimitExceededException
    ApiGatewayManagementApi.Client.exceptions.PayloadTooLargeException
    ApiGatewayManagementApi.Client.exceptions.ForbiddenException
    
    """
    pass

