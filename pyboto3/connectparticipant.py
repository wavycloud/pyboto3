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

def create_participant_connection(Type=None, ParticipantToken=None):
    """
    Creates the participant\'s connection. Note that ParticipantToken is used for invoking this API instead of ConnectionToken.
    The participant token is valid for the lifetime of the participant \xe2\x80\x93 until the they are part of a contact.
    The response URL for WEBSOCKET Type has a connect expiry timeout of 100s. Clients must manually connect to the returned websocket URL and subscribe to the desired topic.
    For chat, you need to publish the following on the established websocket connection:
    Upon websocket URL expiry, as specified in the response ConnectionExpiry parameter, clients need to call this API again to obtain a new websocket URL and perform the same steps as before.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_participant_connection(
        Type=[
            'WEBSOCKET'|'CONNECTION_CREDENTIALS',
        ],
        ParticipantToken='string'
    )
    
    
    :type Type: list
    :param Type: [REQUIRED]\nType of connection information required.\n\n(string) --\n\n

    :type ParticipantToken: string
    :param ParticipantToken: [REQUIRED]\nParticipant Token as obtained from StartChatContact API response.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Websocket': {
        'Url': 'string',
        'ConnectionExpiry': 'string'
    },
    'ConnectionCredentials': {
        'ConnectionToken': 'string',
        'Expiry': 'string'
    }
}


Response Structure

(dict) --

Websocket (dict) --
Creates the participant\'s websocket connection.

Url (string) --
The URL of the websocket.

ConnectionExpiry (string) --
The URL expiration timestamp in ISO date format.
It\'s specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.



ConnectionCredentials (dict) --
Creates the participant\'s connection credentials. The authentication token associated with the participant\'s connection.

ConnectionToken (string) --
The connection token.

Expiry (string) --
The expiration of the token.
It\'s specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.









Exceptions

ConnectParticipant.Client.exceptions.AccessDeniedException
ConnectParticipant.Client.exceptions.InternalServerException
ConnectParticipant.Client.exceptions.ThrottlingException
ConnectParticipant.Client.exceptions.ValidationException


    :return: {
        'Websocket': {
            'Url': 'string',
            'ConnectionExpiry': 'string'
        },
        'ConnectionCredentials': {
            'ConnectionToken': 'string',
            'Expiry': 'string'
        }
    }
    
    
    :returns: 
    ConnectParticipant.Client.exceptions.AccessDeniedException
    ConnectParticipant.Client.exceptions.InternalServerException
    ConnectParticipant.Client.exceptions.ThrottlingException
    ConnectParticipant.Client.exceptions.ValidationException
    
    """
    pass

def disconnect_participant(ClientToken=None, ConnectionToken=None):
    """
    Disconnects a participant. Note that ConnectionToken is used for invoking this API instead of ParticipantToken.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disconnect_participant(
        ClientToken='string',
        ConnectionToken='string'
    )
    
    
    :type ClientToken: string
    :param ClientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type ConnectionToken: string
    :param ConnectionToken: [REQUIRED]\nThe authentication token associated with the participant\'s connection.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ConnectParticipant.Client.exceptions.AccessDeniedException
ConnectParticipant.Client.exceptions.InternalServerException
ConnectParticipant.Client.exceptions.ThrottlingException
ConnectParticipant.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def get_transcript(ContactId=None, MaxResults=None, NextToken=None, ScanDirection=None, SortOrder=None, StartPosition=None, ConnectionToken=None):
    """
    Retrieves a transcript of the session. Note that ConnectionToken is used for invoking this API instead of ParticipantToken.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_transcript(
        ContactId='string',
        MaxResults=123,
        NextToken='string',
        ScanDirection='FORWARD'|'BACKWARD',
        SortOrder='DESCENDING'|'ASCENDING',
        StartPosition={
            'Id': 'string',
            'AbsoluteTime': 'string',
            'MostRecent': 123
        },
        ConnectionToken='string'
    )
    
    
    :type ContactId: string
    :param ContactId: The contactId from the current contact chain for which transcript is needed.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the page. Default: 10.

    :type NextToken: string
    :param NextToken: The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results.

    :type ScanDirection: string
    :param ScanDirection: The direction from StartPosition from which to retrieve message. Default: BACKWARD when no StartPosition is provided, FORWARD with StartPosition.

    :type SortOrder: string
    :param SortOrder: The sort order for the records. Default: DESCENDING.

    :type StartPosition: dict
    :param StartPosition: A filtering option for where to start.\n\nId (string) --The ID of the message or event where to start.\n\nAbsoluteTime (string) --The time in ISO format where to start.\nIt\'s specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.\n\nMostRecent (integer) --The start position of the most recent message where you want to start.\n\n\n

    :type ConnectionToken: string
    :param ConnectionToken: [REQUIRED]\nThe authentication token associated with the participant\'s connection.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'InitialContactId': 'string',
    'Transcript': [
        {
            'AbsoluteTime': 'string',
            'Content': 'string',
            'ContentType': 'string',
            'Id': 'string',
            'Type': 'MESSAGE'|'EVENT'|'CONNECTION_ACK',
            'ParticipantId': 'string',
            'DisplayName': 'string',
            'ParticipantRole': 'AGENT'|'CUSTOMER'|'SYSTEM'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

InitialContactId (string) --
The initial contact ID for the contact.

Transcript (list) --
The list of messages in the session.

(dict) --
An item - message or event - that has been sent.

AbsoluteTime (string) --
The time when the message or event was sent.
It\'s specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.

Content (string) --
The content of the message or event.

ContentType (string) --
The type of content of the item.

Id (string) --
The ID of the item.

Type (string) --
Type of the item: message or event.

ParticipantId (string) --
The ID of the sender in the session.

DisplayName (string) --
The chat display name of the sender.

ParticipantRole (string) --
The role of the sender. For example, is it a customer, agent, or system.





NextToken (string) --
The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results.







Exceptions

ConnectParticipant.Client.exceptions.AccessDeniedException
ConnectParticipant.Client.exceptions.InternalServerException
ConnectParticipant.Client.exceptions.ThrottlingException
ConnectParticipant.Client.exceptions.ValidationException


    :return: {
        'InitialContactId': 'string',
        'Transcript': [
            {
                'AbsoluteTime': 'string',
                'Content': 'string',
                'ContentType': 'string',
                'Id': 'string',
                'Type': 'MESSAGE'|'EVENT'|'CONNECTION_ACK',
                'ParticipantId': 'string',
                'DisplayName': 'string',
                'ParticipantRole': 'AGENT'|'CUSTOMER'|'SYSTEM'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConnectParticipant.Client.exceptions.AccessDeniedException
    ConnectParticipant.Client.exceptions.InternalServerException
    ConnectParticipant.Client.exceptions.ThrottlingException
    ConnectParticipant.Client.exceptions.ValidationException
    
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

def send_event(ContentType=None, Content=None, ClientToken=None, ConnectionToken=None):
    """
    Sends an event. Note that ConnectionToken is used for invoking this API instead of ParticipantToken.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_event(
        ContentType='string',
        Content='string',
        ClientToken='string',
        ConnectionToken='string'
    )
    
    
    :type ContentType: string
    :param ContentType: [REQUIRED]\nThe content type of the request. Supported types are:\n\napplication/vnd.amazonaws.connect.event.typing\napplication/vnd.amazonaws.connect.event.connection.acknowledged\n\n

    :type Content: string
    :param Content: The content of the event to be sent (for example, message text). This is not yet supported.

    :type ClientToken: string
    :param ClientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type ConnectionToken: string
    :param ConnectionToken: [REQUIRED]\nThe authentication token associated with the participant\'s connection.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string',
    'AbsoluteTime': 'string'
}


Response Structure

(dict) --

Id (string) --
The ID of the response.

AbsoluteTime (string) --
The time when the event was sent.
It\'s specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.







Exceptions

ConnectParticipant.Client.exceptions.AccessDeniedException
ConnectParticipant.Client.exceptions.InternalServerException
ConnectParticipant.Client.exceptions.ThrottlingException
ConnectParticipant.Client.exceptions.ValidationException


    :return: {
        'Id': 'string',
        'AbsoluteTime': 'string'
    }
    
    
    :returns: 
    ConnectParticipant.Client.exceptions.AccessDeniedException
    ConnectParticipant.Client.exceptions.InternalServerException
    ConnectParticipant.Client.exceptions.ThrottlingException
    ConnectParticipant.Client.exceptions.ValidationException
    
    """
    pass

def send_message(ContentType=None, Content=None, ClientToken=None, ConnectionToken=None):
    """
    Sends a message. Note that ConnectionToken is used for invoking this API instead of ParticipantToken.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_message(
        ContentType='string',
        Content='string',
        ClientToken='string',
        ConnectionToken='string'
    )
    
    
    :type ContentType: string
    :param ContentType: [REQUIRED]\nThe type of the content. Supported types are text/plain.\n

    :type Content: string
    :param Content: [REQUIRED]\nThe content of the message.\n

    :type ClientToken: string
    :param ClientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type ConnectionToken: string
    :param ConnectionToken: [REQUIRED]\nThe authentication token associated with the connection.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string',
    'AbsoluteTime': 'string'
}


Response Structure

(dict) --

Id (string) --
The ID of the message.

AbsoluteTime (string) --
The time when the message was sent.
It\'s specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.







Exceptions

ConnectParticipant.Client.exceptions.AccessDeniedException
ConnectParticipant.Client.exceptions.InternalServerException
ConnectParticipant.Client.exceptions.ThrottlingException
ConnectParticipant.Client.exceptions.ValidationException


    :return: {
        'Id': 'string',
        'AbsoluteTime': 'string'
    }
    
    
    :returns: 
    ConnectParticipant.Client.exceptions.AccessDeniedException
    ConnectParticipant.Client.exceptions.InternalServerException
    ConnectParticipant.Client.exceptions.ThrottlingException
    ConnectParticipant.Client.exceptions.ValidationException
    
    """
    pass

