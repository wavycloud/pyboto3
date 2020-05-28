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

def get_ice_server_config(ChannelARN=None, ClientId=None, Service=None, Username=None):
    """
    Gets the Interactive Connectivity Establishment (ICE) server configuration information, including URIs, username, and password which can be used to configure the WebRTC connection. The ICE component uses this configuration information to setup the WebRTC connection, including authenticating with the Traversal Using Relays around NAT (TURN) relay server.
    TURN is a protocol that is used to improve the connectivity of peer-to-peer applications. By providing a cloud-based relay service, TURN ensures that a connection can be established even when one or more peers are incapable of a direct peer-to-peer connection. For more information, see A REST API For Access To TURN Services .
    You can invoke this API to establish a fallback mechanism in case either of the peers is unable to establish a direct peer-to-peer connection over a signaling channel. You must specify either a signaling channel ARN or the client ID in order to invoke this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ice_server_config(
        ChannelARN='string',
        ClientId='string',
        Service='TURN',
        Username='string'
    )
    
    
    :type ChannelARN: string
    :param ChannelARN: [REQUIRED]\nThe ARN of the signaling channel to be used for the peer-to-peer connection between configured peers.\n

    :type ClientId: string
    :param ClientId: Unique identifier for the viewer. Must be unique within the signaling channel.

    :type Service: string
    :param Service: Specifies the desired service. Currently, TURN is the only valid value.

    :type Username: string
    :param Username: An optional user ID to be associated with the credentials.

    :rtype: dict

ReturnsResponse Syntax
{
    'IceServerList': [
        {
            'Uris': [
                'string',
            ],
            'Username': 'string',
            'Password': 'string',
            'Ttl': 123
        },
    ]
}


Response Structure

(dict) --

IceServerList (list) --
The list of ICE server information objects.

(dict) --
A structure for the ICE server connection data.

Uris (list) --
An array of URIs, in the form specified in the I-D.petithuguenin-behave-turn-uris spec. These URIs provide the different addresses and/or protocols that can be used to reach the TURN server.

(string) --


Username (string) --
A username to login to the ICE server.

Password (string) --
A password to login to the ICE server.

Ttl (integer) --
The period of time, in seconds, during which the username and password are valid.











Exceptions

KinesisVideoSignalingChannels.Client.exceptions.InvalidClientException
KinesisVideoSignalingChannels.Client.exceptions.SessionExpiredException
KinesisVideoSignalingChannels.Client.exceptions.ClientLimitExceededException
KinesisVideoSignalingChannels.Client.exceptions.ResourceNotFoundException
KinesisVideoSignalingChannels.Client.exceptions.InvalidArgumentException
KinesisVideoSignalingChannels.Client.exceptions.NotAuthorizedException


    :return: {
        'IceServerList': [
            {
                'Uris': [
                    'string',
                ],
                'Username': 'string',
                'Password': 'string',
                'Ttl': 123
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

def send_alexa_offer_to_master(ChannelARN=None, SenderClientId=None, MessagePayload=None):
    """
    This API allows you to connect WebRTC-enabled devices with Alexa display devices. When invoked, it sends the Alexa Session Description Protocol (SDP) offer to the master peer. The offer is delivered as soon as the master is connected to the specified signaling channel. This API returns the SDP answer from the connected master. If the master is not connected to the signaling channel, redelivery requests are made until the message expires.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_alexa_offer_to_master(
        ChannelARN='string',
        SenderClientId='string',
        MessagePayload='string'
    )
    
    
    :type ChannelARN: string
    :param ChannelARN: [REQUIRED]\nThe ARN of the signaling channel by which Alexa and the master peer communicate.\n

    :type SenderClientId: string
    :param SenderClientId: [REQUIRED]\nThe unique identifier for the sender client.\n

    :type MessagePayload: string
    :param MessagePayload: [REQUIRED]\nThe base64-encoded SDP offer content.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Answer': 'string'
}


Response Structure

(dict) --

Answer (string) --
The base64-encoded SDP answer content.







Exceptions

KinesisVideoSignalingChannels.Client.exceptions.ClientLimitExceededException
KinesisVideoSignalingChannels.Client.exceptions.ResourceNotFoundException
KinesisVideoSignalingChannels.Client.exceptions.InvalidArgumentException
KinesisVideoSignalingChannels.Client.exceptions.NotAuthorizedException


    :return: {
        'Answer': 'string'
    }
    
    
    :returns: 
    KinesisVideoSignalingChannels.Client.exceptions.ClientLimitExceededException
    KinesisVideoSignalingChannels.Client.exceptions.ResourceNotFoundException
    KinesisVideoSignalingChannels.Client.exceptions.InvalidArgumentException
    KinesisVideoSignalingChannels.Client.exceptions.NotAuthorizedException
    
    """
    pass

