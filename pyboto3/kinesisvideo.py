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

def create_signaling_channel(ChannelName=None, ChannelType=None, SingleMasterConfiguration=None, Tags=None):
    """
    Creates a signaling channel.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_signaling_channel(
        ChannelName='string',
        ChannelType='SINGLE_MASTER',
        SingleMasterConfiguration={
            'MessageTtlSeconds': 123
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ChannelName: string
    :param ChannelName: [REQUIRED]\nA name for the signaling channel that you are creating. It must be unique for each AWS account and AWS Region.\n

    :type ChannelType: string
    :param ChannelType: A type of the signaling channel that you are creating. Currently, SINGLE_MASTER is the only supported channel type.

    :type SingleMasterConfiguration: dict
    :param SingleMasterConfiguration: A structure containing the configuration for the SINGLE_MASTER channel type.\n\nMessageTtlSeconds (integer) --The period of time a signaling channel retains underlivered messages before they are discarded.\n\n\n

    :type Tags: list
    :param Tags: A set of tags (key-value pairs) that you want to associate with this channel.\n\n(dict) --A key and value pair that is associated with the specified signaling channel.\n\nKey (string) -- [REQUIRED]The key of the tag that is associated with the specified signaling channel.\n\nValue (string) -- [REQUIRED]The value of the tag that is associated with the specified signaling channel.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChannelARN': 'string'
}


Response Structure

(dict) --

ChannelARN (string) --
The Amazon Resource Name (ARN) of the created channel.







Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.AccountChannelLimitExceededException
KinesisVideo.Client.exceptions.ResourceInUseException
KinesisVideo.Client.exceptions.AccessDeniedException
KinesisVideo.Client.exceptions.TagsPerResourceExceededLimitException


    :return: {
        'ChannelARN': 'string'
    }
    
    
    :returns: 
    KinesisVideo.Client.exceptions.InvalidArgumentException
    KinesisVideo.Client.exceptions.ClientLimitExceededException
    KinesisVideo.Client.exceptions.AccountChannelLimitExceededException
    KinesisVideo.Client.exceptions.ResourceInUseException
    KinesisVideo.Client.exceptions.AccessDeniedException
    KinesisVideo.Client.exceptions.TagsPerResourceExceededLimitException
    
    """
    pass

def create_stream(DeviceName=None, StreamName=None, MediaType=None, KmsKeyId=None, DataRetentionInHours=None, Tags=None):
    """
    Creates a new Kinesis video stream.
    When you create a new stream, Kinesis Video Streams assigns it a version number. When you change the stream\'s metadata, Kinesis Video Streams updates the version.
    For information about how the service works, see How it Works .
    You must have permissions for the KinesisVideo:CreateStream action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_stream(
        DeviceName='string',
        StreamName='string',
        MediaType='string',
        KmsKeyId='string',
        DataRetentionInHours=123,
        Tags={
            'string': 'string'
        }
    )
    
    
    :type DeviceName: string
    :param DeviceName: The name of the device that is writing to the stream.\n\nNote\nIn the current implementation, Kinesis Video Streams does not use this name.\n\n

    :type StreamName: string
    :param StreamName: [REQUIRED]\nA name for the stream that you are creating.\nThe stream name is an identifier for the stream, and must be unique for each account and region.\n

    :type MediaType: string
    :param MediaType: The media type of the stream. Consumers of the stream can use this information when processing the stream. For more information about media types, see Media Types . If you choose to specify the MediaType , see Naming Requirements for guidelines.\nExample valid values include 'video/h264' and 'video/h264,audio/aac'.\nThis parameter is optional; the default value is null (or empty in JSON).\n

    :type KmsKeyId: string
    :param KmsKeyId: The ID of the AWS Key Management Service (AWS KMS) key that you want Kinesis Video Streams to use to encrypt stream data.\nIf no key ID is specified, the default, Kinesis Video-managed key (aws/kinesisvideo ) is used.\nFor more information, see DescribeKey .\n

    :type DataRetentionInHours: integer
    :param DataRetentionInHours: The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.\nThe default value is 0, indicating that the stream does not persist data.\nWhen the DataRetentionInHours value is 0, consumers can still consume the fragments that remain in the service host buffer, which has a retention time limit of 5 minutes and a retention memory limit of 200 MB. Fragments are removed from the buffer when either limit is reached.\n

    :type Tags: dict
    :param Tags: A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamARN': 'string'
}


Response Structure

(dict) --

StreamARN (string) --
The Amazon Resource Name (ARN) of the stream.







Exceptions

KinesisVideo.Client.exceptions.AccountStreamLimitExceededException
KinesisVideo.Client.exceptions.DeviceStreamLimitExceededException
KinesisVideo.Client.exceptions.ResourceInUseException
KinesisVideo.Client.exceptions.InvalidDeviceException
KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.TagsPerResourceExceededLimitException


    :return: {
        'StreamARN': 'string'
    }
    
    
    :returns: 
    KinesisVideo.Client.exceptions.AccountStreamLimitExceededException
    KinesisVideo.Client.exceptions.DeviceStreamLimitExceededException
    KinesisVideo.Client.exceptions.ResourceInUseException
    KinesisVideo.Client.exceptions.InvalidDeviceException
    KinesisVideo.Client.exceptions.InvalidArgumentException
    KinesisVideo.Client.exceptions.ClientLimitExceededException
    KinesisVideo.Client.exceptions.TagsPerResourceExceededLimitException
    
    """
    pass

def delete_signaling_channel(ChannelARN=None, CurrentVersion=None):
    """
    Deletes a specified signaling channel. DeleteSignalingChannel is an asynchronous operation. If you don\'t specify the channel\'s current version, the most recent version is deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_signaling_channel(
        ChannelARN='string',
        CurrentVersion='string'
    )
    
    
    :type ChannelARN: string
    :param ChannelARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the signaling channel that you want to delete.\n

    :type CurrentVersion: string
    :param CurrentVersion: The current version of the signaling channel that you want to delete. You can obtain the current version by invoking the DescribeSignalingChannel or ListSignalingChannels API operations.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.AccessDeniedException
KinesisVideo.Client.exceptions.VersionMismatchException
KinesisVideo.Client.exceptions.ResourceInUseException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_stream(StreamARN=None, CurrentVersion=None):
    """
    Deletes a Kinesis video stream and the data contained in the stream.
    This method marks the stream for deletion, and makes the data in the stream inaccessible immediately.
    To ensure that you have the latest version of the stream before deleting it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the DescribeStream API.
    This operation requires permission for the KinesisVideo:DeleteStream action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stream(
        StreamARN='string',
        CurrentVersion='string'
    )
    
    
    :type StreamARN: string
    :param StreamARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the stream that you want to delete.\n

    :type CurrentVersion: string
    :param CurrentVersion: Optional: The version of the stream that you want to delete.\nSpecify the version as a safeguard to ensure that your are deleting the correct stream. To get the stream version, use the DescribeStream API.\nIf not specified, only the CreationTime is checked before deleting the stream.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.NotAuthorizedException
KinesisVideo.Client.exceptions.VersionMismatchException
KinesisVideo.Client.exceptions.ResourceInUseException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_signaling_channel(ChannelName=None, ChannelARN=None):
    """
    Returns the most current information about the signaling channel. You must specify either the name or the Amazon Resource Name (ARN) of the channel that you want to describe.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_signaling_channel(
        ChannelName='string',
        ChannelARN='string'
    )
    
    
    :type ChannelName: string
    :param ChannelName: The name of the signaling channel that you want to describe.

    :type ChannelARN: string
    :param ChannelARN: The ARN of the signaling channel that you want to describe.

    :rtype: dict

ReturnsResponse Syntax
{
    'ChannelInfo': {
        'ChannelName': 'string',
        'ChannelARN': 'string',
        'ChannelType': 'SINGLE_MASTER',
        'ChannelStatus': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
        'CreationTime': datetime(2015, 1, 1),
        'SingleMasterConfiguration': {
            'MessageTtlSeconds': 123
        },
        'Version': 'string'
    }
}


Response Structure

(dict) --

ChannelInfo (dict) --
A structure that encapsulates the specified signaling channel\'s metadata and properties.

ChannelName (string) --
The name of the signaling channel.

ChannelARN (string) --
The Amazon Resource Name (ARN) of the signaling channel.

ChannelType (string) --
The type of the signaling channel.

ChannelStatus (string) --
Current status of the signaling channel.

CreationTime (datetime) --
The time at which the signaling channel was created.

SingleMasterConfiguration (dict) --
A structure that contains the configuration for the SINGLE_MASTER channel type.

MessageTtlSeconds (integer) --
The period of time a signaling channel retains underlivered messages before they are discarded.



Version (string) --
The current version of the signaling channel.









Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.AccessDeniedException


    :return: {
        'ChannelInfo': {
            'ChannelName': 'string',
            'ChannelARN': 'string',
            'ChannelType': 'SINGLE_MASTER',
            'ChannelStatus': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
            'CreationTime': datetime(2015, 1, 1),
            'SingleMasterConfiguration': {
                'MessageTtlSeconds': 123
            },
            'Version': 'string'
        }
    }
    
    
    :returns: 
    KinesisVideo.Client.exceptions.InvalidArgumentException
    KinesisVideo.Client.exceptions.ClientLimitExceededException
    KinesisVideo.Client.exceptions.ResourceNotFoundException
    KinesisVideo.Client.exceptions.AccessDeniedException
    
    """
    pass

def describe_stream(StreamName=None, StreamARN=None):
    """
    Returns the most current information about the specified stream. You must specify either the StreamName or the StreamARN .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stream(
        StreamName='string',
        StreamARN='string'
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream.

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream.

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamInfo': {
        'DeviceName': 'string',
        'StreamName': 'string',
        'StreamARN': 'string',
        'MediaType': 'string',
        'KmsKeyId': 'string',
        'Version': 'string',
        'Status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
        'CreationTime': datetime(2015, 1, 1),
        'DataRetentionInHours': 123
    }
}


Response Structure

(dict) --

StreamInfo (dict) --
An object that describes the stream.

DeviceName (string) --
The name of the device that is associated with the stream.

StreamName (string) --
The name of the stream.

StreamARN (string) --
The Amazon Resource Name (ARN) of the stream.

MediaType (string) --
The MediaType of the stream.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to encrypt data on the stream.

Version (string) --
The version of the stream.

Status (string) --
The status of the stream.

CreationTime (datetime) --
A time stamp that indicates when the stream was created.

DataRetentionInHours (integer) --
How long the stream retains data, in hours.









Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.NotAuthorizedException


    :return: {
        'StreamInfo': {
            'DeviceName': 'string',
            'StreamName': 'string',
            'StreamARN': 'string',
            'MediaType': 'string',
            'KmsKeyId': 'string',
            'Version': 'string',
            'Status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
            'CreationTime': datetime(2015, 1, 1),
            'DataRetentionInHours': 123
        }
    }
    
    
    :returns: 
    KinesisVideo.Client.exceptions.InvalidArgumentException
    KinesisVideo.Client.exceptions.ResourceNotFoundException
    KinesisVideo.Client.exceptions.ClientLimitExceededException
    KinesisVideo.Client.exceptions.NotAuthorizedException
    
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

def get_data_endpoint(StreamName=None, StreamARN=None, APIName=None):
    """
    Gets an endpoint for a specified stream for either reading or writing. Use this endpoint in your application to read from the specified stream (using the GetMedia or GetMediaForFragmentList operations) or write to it (using the PutMedia operation).
    In the request, specify the stream either by StreamName or StreamARN .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_data_endpoint(
        StreamName='string',
        StreamARN='string',
        APIName='PUT_MEDIA'|'GET_MEDIA'|'LIST_FRAGMENTS'|'GET_MEDIA_FOR_FRAGMENT_LIST'|'GET_HLS_STREAMING_SESSION_URL'|'GET_DASH_STREAMING_SESSION_URL'|'GET_CLIP'
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream that you want to get the endpoint for. You must specify either this parameter or a StreamARN in the request.

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream that you want to get the endpoint for. You must specify either this parameter or a StreamName in the request.

    :type APIName: string
    :param APIName: [REQUIRED]\nThe name of the API action for which to get an endpoint.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DataEndpoint': 'string'
}


Response Structure

(dict) --

DataEndpoint (string) --
The endpoint value. To read data from the stream or to write data to it, specify this endpoint in your application.







Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.NotAuthorizedException


    :return: {
        'DataEndpoint': 'string'
    }
    
    
    :returns: 
    KinesisVideo.Client.exceptions.InvalidArgumentException
    KinesisVideo.Client.exceptions.ResourceNotFoundException
    KinesisVideo.Client.exceptions.ClientLimitExceededException
    KinesisVideo.Client.exceptions.NotAuthorizedException
    
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

def get_signaling_channel_endpoint(ChannelARN=None, SingleMasterChannelEndpointConfiguration=None):
    """
    Provides an endpoint for the specified signaling channel to send and receive messages. This API uses the SingleMasterChannelEndpointConfiguration input parameter, which consists of the Protocols and Role properties.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_signaling_channel_endpoint(
        ChannelARN='string',
        SingleMasterChannelEndpointConfiguration={
            'Protocols': [
                'WSS'|'HTTPS',
            ],
            'Role': 'MASTER'|'VIEWER'
        }
    )
    
    
    :type ChannelARN: string
    :param ChannelARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the signalling channel for which you want to get an endpoint.\n

    :type SingleMasterChannelEndpointConfiguration: dict
    :param SingleMasterChannelEndpointConfiguration: A structure containing the endpoint configuration for the SINGLE_MASTER channel type.\n\nProtocols (list) --This property is used to determine the nature of communication over this SINGLE_MASTER signaling channel. If WSS is specified, this API returns a websocket endpoint. If HTTPS is specified, this API returns an HTTPS endpoint.\n\n(string) --\n\n\nRole (string) --This property is used to determine messaging permissions in this SINGLE_MASTER signaling channel. If MASTER is specified, this API returns an endpoint that a client can use to receive offers from and send answers to any of the viewers on this signaling channel. If VIEWER is specified, this API returns an endpoint that a client can use only to send offers to another MASTER client on this signaling channel.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceEndpointList': [
        {
            'Protocol': 'WSS'|'HTTPS',
            'ResourceEndpoint': 'string'
        },
    ]
}


Response Structure

(dict) --

ResourceEndpointList (list) --
A list of endpoints for the specified signaling channel.

(dict) --
An object that describes the endpoint of the signaling channel returned by the GetSignalingChannelEndpoint API.

Protocol (string) --
The protocol of the signaling channel returned by the GetSignalingChannelEndpoint API.

ResourceEndpoint (string) --
The endpoint of the signaling channel returned by the GetSignalingChannelEndpoint API.











Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.ResourceInUseException
KinesisVideo.Client.exceptions.AccessDeniedException


    :return: {
        'ResourceEndpointList': [
            {
                'Protocol': 'WSS'|'HTTPS',
                'ResourceEndpoint': 'string'
            },
        ]
    }
    
    
    :returns: 
    KinesisVideo.Client.exceptions.InvalidArgumentException
    KinesisVideo.Client.exceptions.ClientLimitExceededException
    KinesisVideo.Client.exceptions.ResourceNotFoundException
    KinesisVideo.Client.exceptions.ResourceInUseException
    KinesisVideo.Client.exceptions.AccessDeniedException
    
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

def list_signaling_channels(MaxResults=None, NextToken=None, ChannelNameCondition=None):
    """
    Returns an array of ChannelInfo objects. Each object describes a signaling channel. To retrieve only those channels that satisfy a specific condition, you can specify a ChannelNameCondition .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_signaling_channels(
        MaxResults=123,
        NextToken='string',
        ChannelNameCondition={
            'ComparisonOperator': 'BEGINS_WITH',
            'ComparisonValue': 'string'
        }
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of channels to return in the response. The default is 500.

    :type NextToken: string
    :param NextToken: If you specify this parameter, when the result of a ListSignalingChannels operation is truncated, the call returns the NextToken in the response. To get another batch of channels, provide this token in your next request.

    :type ChannelNameCondition: dict
    :param ChannelNameCondition: Optional: Returns only the channels that satisfy a specific condition.\n\nComparisonOperator (string) --A comparison operator. Currently, you can only specify the BEGINS_WITH operator, which finds signaling channels whose names begin with a given prefix.\n\nComparisonValue (string) --A value to compare.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChannelInfoList': [
        {
            'ChannelName': 'string',
            'ChannelARN': 'string',
            'ChannelType': 'SINGLE_MASTER',
            'ChannelStatus': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
            'CreationTime': datetime(2015, 1, 1),
            'SingleMasterConfiguration': {
                'MessageTtlSeconds': 123
            },
            'Version': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ChannelInfoList (list) --
An array of ChannelInfo objects.

(dict) --
A structure that encapsulates a signaling channel\'s metadata and properties.

ChannelName (string) --
The name of the signaling channel.

ChannelARN (string) --
The Amazon Resource Name (ARN) of the signaling channel.

ChannelType (string) --
The type of the signaling channel.

ChannelStatus (string) --
Current status of the signaling channel.

CreationTime (datetime) --
The time at which the signaling channel was created.

SingleMasterConfiguration (dict) --
A structure that contains the configuration for the SINGLE_MASTER channel type.

MessageTtlSeconds (integer) --
The period of time a signaling channel retains underlivered messages before they are discarded.



Version (string) --
The current version of the signaling channel.





NextToken (string) --
If the response is truncated, the call returns this element with a token. To get the next batch of streams, use this token in your next request.







Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.AccessDeniedException


    :return: {
        'ChannelInfoList': [
            {
                'ChannelName': 'string',
                'ChannelARN': 'string',
                'ChannelType': 'SINGLE_MASTER',
                'ChannelStatus': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
                'CreationTime': datetime(2015, 1, 1),
                'SingleMasterConfiguration': {
                    'MessageTtlSeconds': 123
                },
                'Version': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    KinesisVideo.Client.exceptions.InvalidArgumentException
    KinesisVideo.Client.exceptions.ClientLimitExceededException
    KinesisVideo.Client.exceptions.AccessDeniedException
    
    """
    pass

def list_streams(MaxResults=None, NextToken=None, StreamNameCondition=None):
    """
    Returns an array of StreamInfo objects. Each object describes a stream. To retrieve only streams that satisfy a specific condition, you can specify a StreamNameCondition .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_streams(
        MaxResults=123,
        NextToken='string',
        StreamNameCondition={
            'ComparisonOperator': 'BEGINS_WITH',
            'ComparisonValue': 'string'
        }
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of streams to return in the response. The default is 10,000.

    :type NextToken: string
    :param NextToken: If you specify this parameter, when the result of a ListStreams operation is truncated, the call returns the NextToken in the response. To get another batch of streams, provide this token in your next request.

    :type StreamNameCondition: dict
    :param StreamNameCondition: Optional: Returns only streams that satisfy a specific condition. Currently, you can specify only the prefix of a stream name as a condition.\n\nComparisonOperator (string) --A comparison operator. Currently, you can specify only the BEGINS_WITH operator, which finds streams whose names start with a given prefix.\n\nComparisonValue (string) --A value to compare.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamInfoList': [
        {
            'DeviceName': 'string',
            'StreamName': 'string',
            'StreamARN': 'string',
            'MediaType': 'string',
            'KmsKeyId': 'string',
            'Version': 'string',
            'Status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
            'CreationTime': datetime(2015, 1, 1),
            'DataRetentionInHours': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

StreamInfoList (list) --
An array of StreamInfo objects.

(dict) --
An object describing a Kinesis video stream.

DeviceName (string) --
The name of the device that is associated with the stream.

StreamName (string) --
The name of the stream.

StreamARN (string) --
The Amazon Resource Name (ARN) of the stream.

MediaType (string) --
The MediaType of the stream.

KmsKeyId (string) --
The ID of the AWS Key Management Service (AWS KMS) key that Kinesis Video Streams uses to encrypt data on the stream.

Version (string) --
The version of the stream.

Status (string) --
The status of the stream.

CreationTime (datetime) --
A time stamp that indicates when the stream was created.

DataRetentionInHours (integer) --
How long the stream retains data, in hours.





NextToken (string) --
If the response is truncated, the call returns this element with a token. To get the next batch of streams, use this token in your next request.







Exceptions

KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.InvalidArgumentException


    :return: {
        'StreamInfoList': [
            {
                'DeviceName': 'string',
                'StreamName': 'string',
                'StreamARN': 'string',
                'MediaType': 'string',
                'KmsKeyId': 'string',
                'Version': 'string',
                'Status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
                'CreationTime': datetime(2015, 1, 1),
                'DataRetentionInHours': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    KinesisVideo.Client.exceptions.ClientLimitExceededException
    KinesisVideo.Client.exceptions.InvalidArgumentException
    
    """
    pass

def list_tags_for_resource(NextToken=None, ResourceARN=None):
    """
    Returns a list of tags associated with the specified signaling channel.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        NextToken='string',
        ResourceARN='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If you specify this parameter and the result of a ListTagsForResource call is truncated, the response includes a token that you can use in the next request to fetch the next batch of tags.

    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the signaling channel for which you want to list tags.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

NextToken (string) --
If you specify this parameter and the result of a ListTagsForResource call is truncated, the response includes a token that you can use in the next request to fetch the next set of tags.

Tags (dict) --
A map of tag keys and values associated with the specified signaling channel.

(string) --
(string) --










Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.AccessDeniedException


    :return: {
        'NextToken': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_tags_for_stream(NextToken=None, StreamARN=None, StreamName=None):
    """
    Returns a list of tags associated with the specified stream.
    In the request, you must specify either the StreamName or the StreamARN .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_stream(
        NextToken='string',
        StreamARN='string',
        StreamName='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If you specify this parameter and the result of a ListTagsForStream call is truncated, the response includes a token that you can use in the next request to fetch the next batch of tags.

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream that you want to list tags for.

    :type StreamName: string
    :param StreamName: The name of the stream that you want to list tags for.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

NextToken (string) --
If you specify this parameter and the result of a ListTags call is truncated, the response includes a token that you can use in the next request to fetch the next set of tags.

Tags (dict) --
A map of tag keys and values associated with the specified stream.

(string) --
(string) --










Exceptions

KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.NotAuthorizedException
KinesisVideo.Client.exceptions.InvalidResourceFormatException


    :return: {
        'NextToken': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Adds one or more tags to a signaling channel. A tag is a key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the signaling channel to which you want to add tags.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA list of tags to associate with the specified signaling channel. Each tag is a key-value pair.\n\n(dict) --A key and value pair that is associated with the specified signaling channel.\n\nKey (string) -- [REQUIRED]The key of the tag that is associated with the specified signaling channel.\n\nValue (string) -- [REQUIRED]The value of the tag that is associated with the specified signaling channel.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.AccessDeniedException
KinesisVideo.Client.exceptions.TagsPerResourceExceededLimitException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def tag_stream(StreamARN=None, StreamName=None, Tags=None):
    """
    Adds one or more tags to a stream. A tag is a key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    You must provide either the StreamName or the StreamARN .
    This operation requires permission for the KinesisVideo:TagStream action.
    Kinesis video streams support up to 50 tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_stream(
        StreamARN='string',
        StreamName='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the resource that you want to add the tag or tags to.

    :type StreamName: string
    :param StreamName: The name of the stream that you want to add the tag or tags to.

    :type Tags: dict
    :param Tags: [REQUIRED]\nA list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.NotAuthorizedException
KinesisVideo.Client.exceptions.InvalidResourceFormatException
KinesisVideo.Client.exceptions.TagsPerResourceExceededLimitException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeyList=None):
    """
    Removes one or more tags from a signaling channel. In the request, specify only a tag key or keys; don\'t specify the value. If you specify a tag key that does not exist, it\'s ignored.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeyList=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the signaling channel from which you want to remove tags.\n

    :type TagKeyList: list
    :param TagKeyList: [REQUIRED]\nA list of the keys of the tags that you want to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_stream(StreamARN=None, StreamName=None, TagKeyList=None):
    """
    Removes one or more tags from a stream. In the request, specify only a tag key or keys; don\'t specify the value. If you specify a tag key that does not exist, it\'s ignored.
    In the request, you must provide the StreamName or StreamARN .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_stream(
        StreamARN='string',
        StreamName='string',
        TagKeyList=[
            'string',
        ]
    )
    
    
    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream that you want to remove tags from.

    :type StreamName: string
    :param StreamName: The name of the stream that you want to remove tags from.

    :type TagKeyList: list
    :param TagKeyList: [REQUIRED]\nA list of the keys of the tags that you want to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.NotAuthorizedException
KinesisVideo.Client.exceptions.InvalidResourceFormatException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_data_retention(StreamName=None, StreamARN=None, CurrentVersion=None, Operation=None, DataRetentionChangeInHours=None):
    """
    Increases or decreases the stream\'s data retention period by the value that you specify. To indicate whether you want to increase or decrease the data retention period, specify the Operation parameter in the request body. In the request, you must specify either the StreamName or the StreamARN .
    This operation requires permission for the KinesisVideo:UpdateDataRetention action.
    Changing the data retention period affects the data in the stream as follows:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_data_retention(
        StreamName='string',
        StreamARN='string',
        CurrentVersion='string',
        Operation='INCREASE_DATA_RETENTION'|'DECREASE_DATA_RETENTION',
        DataRetentionChangeInHours=123
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream whose retention period you want to change.

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream whose retention period you want to change.

    :type CurrentVersion: string
    :param CurrentVersion: [REQUIRED]\nThe version of the stream whose retention period you want to change. To get the version, call either the DescribeStream or the ListStreams API.\n

    :type Operation: string
    :param Operation: [REQUIRED]\nIndicates whether you want to increase or decrease the retention period.\n

    :type DataRetentionChangeInHours: integer
    :param DataRetentionChangeInHours: [REQUIRED]\nThe retention period, in hours. The value you specify replaces the current value. The maximum value for this parameter is 87600 (ten years).\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.ResourceInUseException
KinesisVideo.Client.exceptions.NotAuthorizedException
KinesisVideo.Client.exceptions.VersionMismatchException


    :return: {}
    
    
    :returns: 
    StreamName (string) -- The name of the stream whose retention period you want to change.
    StreamARN (string) -- The Amazon Resource Name (ARN) of the stream whose retention period you want to change.
    CurrentVersion (string) -- [REQUIRED]
    The version of the stream whose retention period you want to change. To get the version, call either the DescribeStream or the ListStreams API.
    
    Operation (string) -- [REQUIRED]
    Indicates whether you want to increase or decrease the retention period.
    
    DataRetentionChangeInHours (integer) -- [REQUIRED]
    The retention period, in hours. The value you specify replaces the current value. The maximum value for this parameter is 87600 (ten years).
    
    
    """
    pass

def update_signaling_channel(ChannelARN=None, CurrentVersion=None, SingleMasterConfiguration=None):
    """
    Updates the existing signaling channel. This is an asynchronous operation and takes time to complete.
    If the MessageTtlSeconds value is updated (either increased or reduced), it only applies to new messages sent via this channel after it\'s been updated. Existing messages are still expired as per the previous MessageTtlSeconds value.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_signaling_channel(
        ChannelARN='string',
        CurrentVersion='string',
        SingleMasterConfiguration={
            'MessageTtlSeconds': 123
        }
    )
    
    
    :type ChannelARN: string
    :param ChannelARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the signaling channel that you want to update.\n

    :type CurrentVersion: string
    :param CurrentVersion: [REQUIRED]\nThe current version of the signaling channel that you want to update.\n

    :type SingleMasterConfiguration: dict
    :param SingleMasterConfiguration: The structure containing the configuration for the SINGLE_MASTER type of the signaling channel that you want to update.\n\nMessageTtlSeconds (integer) --The period of time a signaling channel retains underlivered messages before they are discarded.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.ResourceInUseException
KinesisVideo.Client.exceptions.AccessDeniedException
KinesisVideo.Client.exceptions.VersionMismatchException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_stream(StreamName=None, StreamARN=None, CurrentVersion=None, DeviceName=None, MediaType=None):
    """
    Updates stream metadata, such as the device name and media type.
    You must provide the stream name or the Amazon Resource Name (ARN) of the stream.
    To make sure that you have the latest version of the stream before updating it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the DescribeStream API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_stream(
        StreamName='string',
        StreamARN='string',
        CurrentVersion='string',
        DeviceName='string',
        MediaType='string'
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream whose metadata you want to update.\nThe stream name is an identifier for the stream, and must be unique for each account and region.\n

    :type StreamARN: string
    :param StreamARN: The ARN of the stream whose metadata you want to update.

    :type CurrentVersion: string
    :param CurrentVersion: [REQUIRED]\nThe version of the stream whose metadata you want to update.\n

    :type DeviceName: string
    :param DeviceName: The name of the device that is writing to the stream.\n\nNote\nIn the current implementation, Kinesis Video Streams does not use this name.\n\n

    :type MediaType: string
    :param MediaType: The stream\'s media type. Use MediaType to specify the type of content that the stream contains to the consumers of the stream. For more information about media types, see Media Types . If you choose to specify the MediaType , see Naming Requirements .\nTo play video on the console, you must specify the correct video type. For example, if the video in the stream is H.264, specify video/h264 as the MediaType .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

KinesisVideo.Client.exceptions.ClientLimitExceededException
KinesisVideo.Client.exceptions.InvalidArgumentException
KinesisVideo.Client.exceptions.ResourceNotFoundException
KinesisVideo.Client.exceptions.ResourceInUseException
KinesisVideo.Client.exceptions.NotAuthorizedException
KinesisVideo.Client.exceptions.VersionMismatchException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

