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

def create_connection(ProviderType=None, ConnectionName=None, Tags=None):
    """
    Creates a connection that can then be given to other AWS services like CodePipeline so that it can access third-party code repositories. The connection is in pending status until the third-party connection handshake is completed from the console.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_connection(
        ProviderType='Bitbucket',
        ConnectionName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ProviderType: string
    :param ProviderType: [REQUIRED]\nThe name of the external provider where your third-party code repository is configured. Currently, the valid provider type is Bitbucket.\n

    :type ConnectionName: string
    :param ConnectionName: [REQUIRED]\nThe name of the connection to be created. The name must be unique in the calling AWS account.\n

    :type Tags: list
    :param Tags: The key-value pair to use when tagging the resource.\n\n(dict) --A tag is a key-value pair that is used to manage the resource.\nThis tag is available for use by AWS services that support tags.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) -- [REQUIRED]The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConnectionArn': 'string',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

ConnectionArn (string) --
The Amazon Resource Name (ARN) of the connection to be created. The ARN is used as the connection reference when the connection is shared between AWS services.

Note
The ARN is never reused if the connection is deleted.


Tags (list) --
Specifies the tags applied to the resource.

(dict) --
A tag is a key-value pair that is used to manage the resource.
This tag is available for use by AWS services that support tags.

Key (string) --
The tag\'s key.

Value (string) --
The tag\'s value.











Exceptions

CodeStarconnections.Client.exceptions.LimitExceededException


    :return: {
        'ConnectionArn': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    CodeStarconnections.Client.exceptions.LimitExceededException
    
    """
    pass

def delete_connection(ConnectionArn=None):
    """
    The connection to be deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_connection(
        ConnectionArn='string'
    )
    
    
    :type ConnectionArn: string
    :param ConnectionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the connection to be deleted.\n\nNote\nThe ARN is never reused if the connection is deleted.\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodeStarconnections.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    CodeStarconnections.Client.exceptions.ResourceNotFoundException
    
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

def get_connection(ConnectionArn=None):
    """
    Returns the connection ARN and details such as status, owner, and provider type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_connection(
        ConnectionArn='string'
    )
    
    
    :type ConnectionArn: string
    :param ConnectionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of a connection.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Connection': {
        'ConnectionName': 'string',
        'ConnectionArn': 'string',
        'ProviderType': 'Bitbucket',
        'OwnerAccountId': 'string',
        'ConnectionStatus': 'PENDING'|'AVAILABLE'|'ERROR'
    }
}


Response Structure

(dict) --
Connection (dict) --The connection details, such as status, owner, and provider type.

ConnectionName (string) --The name of the connection. Connection names must be unique in an AWS user account.

ConnectionArn (string) --The Amazon Resource Name (ARN) of the connection. The ARN is used as the connection reference when the connection is shared between AWS services.

Note
The ARN is never reused if the connection is deleted.


ProviderType (string) --The name of the external provider where your third-party code repository is configured. Currently, the valid provider type is Bitbucket.

OwnerAccountId (string) --The identifier of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.

ConnectionStatus (string) --The current status of the connection.








Exceptions

CodeStarconnections.Client.exceptions.ResourceNotFoundException


    :return: {
        'Connection': {
            'ConnectionName': 'string',
            'ConnectionArn': 'string',
            'ProviderType': 'Bitbucket',
            'OwnerAccountId': 'string',
            'ConnectionStatus': 'PENDING'|'AVAILABLE'|'ERROR'
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

def list_connections(ProviderTypeFilter=None, MaxResults=None, NextToken=None):
    """
    Lists the connections associated with your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_connections(
        ProviderTypeFilter='Bitbucket',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ProviderTypeFilter: string
    :param ProviderTypeFilter: Filters the list of connections to those associated with a specified provider, such as Bitbucket.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :type NextToken: string
    :param NextToken: The token that was returned from the previous ListConnections call, which can be used to return the next set of connections in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'Connections': [
        {
            'ConnectionName': 'string',
            'ConnectionArn': 'string',
            'ProviderType': 'Bitbucket',
            'OwnerAccountId': 'string',
            'ConnectionStatus': 'PENDING'|'AVAILABLE'|'ERROR'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Connections (list) --
A list of connections and the details for each connection, such as status, owner, and provider type.

(dict) --
The AWS::CodeStarConnections::Connection resource can be used to connect external source providers with services like AWS CodePipeline.
Note: A connection created through CloudFormation is in PENDING status by default. You can make its status AVAILABLE by editing the connection in the CodePipeline console.

ConnectionName (string) --
The name of the connection. Connection names must be unique in an AWS user account.

ConnectionArn (string) --
The Amazon Resource Name (ARN) of the connection. The ARN is used as the connection reference when the connection is shared between AWS services.

Note
The ARN is never reused if the connection is deleted.


ProviderType (string) --
The name of the external provider where your third-party code repository is configured. Currently, the valid provider type is Bitbucket.

OwnerAccountId (string) --
The identifier of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.

ConnectionStatus (string) --
The current status of the connection.





NextToken (string) --
A token that can be used in the next ListConnections call. To view all items in the list, continue to call this operation with each subsequent token until no more nextToken values are returned.








    :return: {
        'Connections': [
            {
                'ConnectionName': 'string',
                'ConnectionArn': 'string',
                'ProviderType': 'Bitbucket',
                'OwnerAccountId': 'string',
                'ConnectionStatus': 'PENDING'|'AVAILABLE'|'ERROR'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Gets the set of key-value pairs (metadata) that are used to manage the resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource for which you want to get information about tags, if any.\n

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
Tags (list) --A list of tag key and value pairs associated with the specified resource.

(dict) --A tag is a key-value pair that is used to manage the resource.
This tag is available for use by AWS services that support tags.

Key (string) --The tag\'s key.

Value (string) --The tag\'s value.










Exceptions

CodeStarconnections.Client.exceptions.ResourceNotFoundException


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

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to which you want to add or update tags.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags you want to modify or add to the resource.\n\n(dict) --A tag is a key-value pair that is used to manage the resource.\nThis tag is available for use by AWS services that support tags.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) -- [REQUIRED]The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeStarconnections.Client.exceptions.ResourceNotFoundException
CodeStarconnections.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes tags from an AWS resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to remove tags from.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe list of keys for the tags to be removed from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeStarconnections.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

