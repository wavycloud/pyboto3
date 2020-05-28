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

def get_media(StreamName=None, StreamARN=None, StartSelector=None):
    """
    Use this API to retrieve media content from a Kinesis video stream. In the request, you identify the stream name or stream Amazon Resource Name (ARN), and the starting chunk. Kinesis Video Streams then returns a stream of chunks in order by fragment number.
    When you put media data (fragments) on a stream, Kinesis Video Streams stores each incoming fragment and related metadata in what is called a "chunk." For more information, see PutMedia . The GetMedia API returns a stream of these chunks starting from the chunk that you specify in the request.
    The following limits apply when using the GetMedia API:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_media(
        StreamName='string',
        StreamARN='string',
        StartSelector={
            'StartSelectorType': 'FRAGMENT_NUMBER'|'SERVER_TIMESTAMP'|'PRODUCER_TIMESTAMP'|'NOW'|'EARLIEST'|'CONTINUATION_TOKEN',
            'AfterFragmentNumber': 'string',
            'StartTimestamp': datetime(2015, 1, 1),
            'ContinuationToken': 'string'
        }
    )
    
    
    :type StreamName: string
    :param StreamName: The Kinesis video stream name from where you want to get the media content. If you don\'t specify the streamName , you must specify the streamARN .

    :type StreamARN: string
    :param StreamARN: The ARN of the stream from where you want to get the media content. If you don\'t specify the streamARN , you must specify the streamName .

    :type StartSelector: dict
    :param StartSelector: [REQUIRED]\nIdentifies the starting chunk to get from the specified stream.\n\nStartSelectorType (string) -- [REQUIRED]Identifies the fragment on the Kinesis video stream where you want to start getting the data from.\n\nNOW - Start with the latest chunk on the stream.\nEARLIEST - Start with earliest available chunk on the stream.\nFRAGMENT_NUMBER - Start with the chunk after a specific fragment. You must also specify the AfterFragmentNumber parameter.\nPRODUCER_TIMESTAMP or SERVER_TIMESTAMP - Start with the chunk containing a fragment with the specified producer or server timestamp. You specify the timestamp by adding StartTimestamp .\nCONTINUATION_TOKEN - Read using the specified continuation token.\n\n\nNote\nIf you choose the NOW, EARLIEST, or CONTINUATION_TOKEN as the startSelectorType , you don\'t provide any additional information in the startSelector .\n\n\nAfterFragmentNumber (string) --Specifies the fragment number from where you want the GetMedia API to start returning the fragments.\n\nStartTimestamp (datetime) --A timestamp value. This value is required if you choose the PRODUCER_TIMESTAMP or the SERVER_TIMESTAMP as the startSelectorType . The GetMedia API then starts with the chunk containing the fragment that has the specified timestamp.\n\nContinuationToken (string) --Continuation token that Kinesis Video Streams returned in the previous GetMedia response. The GetMedia API then starts with the chunk identified by the continuation token.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentType': 'string',
    'Payload': StreamingBody()
}


Response Structure

(dict) --

ContentType (string) --
The content type of the requested media.

Payload (StreamingBody) --
The payload Kinesis Video Streams returns is a sequence of chunks from the specified stream. For information about the chunks, see . The chunks that Kinesis Video Streams returns in the GetMedia call also include the following additional Matroska (MKV) tags:

AWS_KINESISVIDEO_CONTINUATION_TOKEN (UTF-8 string) - In the event your GetMedia call terminates, you can use this continuation token in your next request to get the next chunk where the last request terminated.
AWS_KINESISVIDEO_MILLIS_BEHIND_NOW (UTF-8 string) - Client applications can use this tag value to determine how far behind the chunk returned in the response is from the latest chunk on the stream.
AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk.
AWS_KINESISVIDEO_SERVER_TIMESTAMP - Server timestamp of the fragment.
AWS_KINESISVIDEO_PRODUCER_TIMESTAMP - Producer timestamp of the fragment.

The following tags will be present if an error occurs:

AWS_KINESISVIDEO_ERROR_CODE - String description of an error that caused GetMedia to stop.
AWS_KINESISVIDEO_ERROR_ID: Integer code of the error.

The error codes are as follows:

3002 - Error writing to the stream
4000 - Requested fragment is not found
4500 - Access denied for the stream\'s KMS key
4501 - Stream\'s KMS key is disabled
4502 - Validation error on the stream\'s KMS key
4503 - KMS key specified in the stream is unavailable
4504 - Invalid usage of the KMS key specified in the stream
4505 - Invalid state of the KMS key specified in the stream
4506 - Unable to find the KMS key specified in the stream
5000 - Internal error








Exceptions

KinesisVideoMedia.Client.exceptions.ResourceNotFoundException
KinesisVideoMedia.Client.exceptions.NotAuthorizedException
KinesisVideoMedia.Client.exceptions.InvalidEndpointException
KinesisVideoMedia.Client.exceptions.ClientLimitExceededException
KinesisVideoMedia.Client.exceptions.ConnectionLimitExceededException
KinesisVideoMedia.Client.exceptions.InvalidArgumentException


    :return: {
        'ContentType': 'string',
        'Payload': StreamingBody()
    }
    
    
    :returns: 
    x-amz-ErrorType HTTP header \xe2\x80\x93 contains a more specific error type in addition to what the HTTP status code provides.
    x-amz-RequestId HTTP header \xe2\x80\x93 if you want to report an issue to AWS, the support team can better diagnose the problem if given the Request Id.
    
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

