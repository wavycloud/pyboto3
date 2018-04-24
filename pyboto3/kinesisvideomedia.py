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

def get_media(StreamName=None, StreamARN=None, StartSelector=None):
    """
    Use this API to retrieve media content from a Kinesis video stream. In the request, you identify stream name or stream Amazon Resource Name (ARN), and the starting chunk. Kinesis Video Streams then returns a stream of chunks in order by fragment number.
    When you put media data (fragments) on a stream, Kinesis Video Streams stores each incoming fragment and related metadata in what is called a "chunk." For more information, see . The GetMedia API returns a stream of these chunks starting from the chunk that you specify in the request.
    The following limits apply when using the GetMedia API:
    See also: AWS API Documentation
    
    
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
    :param StreamName: The Kinesis video stream name from where you want to get the media content. If you don't specify the streamName , you must specify the streamARN .

    :type StreamARN: string
    :param StreamARN: The ARN of the stream from where you want to get the media content. If you don't specify the streamARN , you must specify the streamName .

    :type StartSelector: dict
    :param StartSelector: [REQUIRED]
            Identifies the starting chunk to get from the specified stream.
            StartSelectorType (string) -- [REQUIRED]Identifies the fragment on the Kinesis video stream where you want to start getting the data from.
            NOW - Start with the latest chunk on the stream.
            EARLIEST - Start with earliest available chunk on the stream.
            FRAGMENT_NUMBER - Start with the chunk containing the specific fragment. You must also specify the StartFragmentNumber .
            PRODUCER_TIMESTAMP or SERVER_TIMESTAMP - Start with the chunk containing a fragment with the specified producer or server time stamp. You specify the time stamp by adding StartTimestamp .
            CONTINUATION_TOKEN - Read using the specified continuation token.
            Note
            If you choose the NOW, EARLIEST, or CONTINUATION_TOKEN as the startSelectorType , you don't provide any additional information in the startSelector .
            AfterFragmentNumber (string) --Specifies the fragment number from where you want the GetMedia API to start returning the fragments.
            StartTimestamp (datetime) --A time stamp value. This value is required if you choose the PRODUCER_TIMESTAMP or the SERVER_TIMESTAMP as the startSelectorType . The GetMedia API then starts with the chunk containing the fragment that has the specified time stamp.
            ContinuationToken (string) --Continuation token that Kinesis Video Streams returned in the previous GetMedia response. The GetMedia API then starts with the chunk identified by the continuation token.
            

    :rtype: dict
    :return: {
        'ContentType': 'string',
        'Payload': StreamingBody()
    }
    
    
    :returns: 
    StreamName (string) -- The Kinesis video stream name from where you want to get the media content. If you don't specify the streamName , you must specify the streamARN .
    StreamARN (string) -- The ARN of the stream from where you want to get the media content. If you don't specify the streamARN , you must specify the streamName .
    StartSelector (dict) -- [REQUIRED]
    Identifies the starting chunk to get from the specified stream.
    
    StartSelectorType (string) -- [REQUIRED]Identifies the fragment on the Kinesis video stream where you want to start getting the data from.
    
    NOW - Start with the latest chunk on the stream.
    EARLIEST - Start with earliest available chunk on the stream.
    FRAGMENT_NUMBER - Start with the chunk containing the specific fragment. You must also specify the StartFragmentNumber .
    PRODUCER_TIMESTAMP or SERVER_TIMESTAMP - Start with the chunk containing a fragment with the specified producer or server time stamp. You specify the time stamp by adding StartTimestamp .
    CONTINUATION_TOKEN - Read using the specified continuation token.
    
    
    Note
    If you choose the NOW, EARLIEST, or CONTINUATION_TOKEN as the startSelectorType , you don't provide any additional information in the startSelector .
    
    
    AfterFragmentNumber (string) --Specifies the fragment number from where you want the GetMedia API to start returning the fragments.
    
    StartTimestamp (datetime) --A time stamp value. This value is required if you choose the PRODUCER_TIMESTAMP or the SERVER_TIMESTAMP as the startSelectorType . The GetMedia API then starts with the chunk containing the fragment that has the specified time stamp.
    
    ContinuationToken (string) --Continuation token that Kinesis Video Streams returned in the previous GetMedia response. The GetMedia API then starts with the chunk identified by the continuation token.
    
    
    
    
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

