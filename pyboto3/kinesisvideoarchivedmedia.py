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

def get_media_for_fragment_list(StreamName=None, Fragments=None):
    """
    Gets media for a list of fragments (specified by fragment number) from the archived data in a Kinesis video stream.
    The following limits apply when using the GetMediaForFragmentList API:
    See also: AWS API Documentation
    
    
    :example: response = client.get_media_for_fragment_list(
        StreamName='string',
        Fragments=[
            'string',
        ]
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream from which to retrieve fragment media.
            

    :type Fragments: list
    :param Fragments: [REQUIRED]
            A list of the numbers of fragments for which to retrieve media. You retrieve these values with ListFragments .
            (string) --
            

    :rtype: dict
    :return: {
        'ContentType': 'string',
        'Payload': StreamingBody()
    }
    
    
    :returns: 
    StreamName (string) -- [REQUIRED]
    The name of the stream from which to retrieve fragment media.
    
    Fragments (list) -- [REQUIRED]
    A list of the numbers of fragments for which to retrieve media. You retrieve these values with  ListFragments .
    
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

def list_fragments(StreamName=None, MaxResults=None, NextToken=None, FragmentSelector=None):
    """
    Returns a list of  Fragment objects from the specified stream and start location within the archived data.
    See also: AWS API Documentation
    
    
    :example: response = client.list_fragments(
        StreamName='string',
        MaxResults=123,
        NextToken='string',
        FragmentSelector={
            'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
            'TimestampRange': {
                'StartTimestamp': datetime(2015, 1, 1),
                'EndTimestamp': datetime(2015, 1, 1)
            }
        }
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]
            The name of the stream from which to retrieve a fragment list.
            

    :type MaxResults: integer
    :param MaxResults: The total number of fragments to return. If the total number of fragments available is more than the value specified in max-results , then a ListFragmentsOutput$NextToken is provided in the output that you can use to resume pagination.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating. This is the ListFragmentsOutput$NextToken from a previously truncated response.

    :type FragmentSelector: dict
    :param FragmentSelector: Describes the time stamp range and time stamp origin for the range of fragments to return.
            FragmentSelectorType (string) -- [REQUIRED]The origin of the time stamps to use (Server or Producer).
            TimestampRange (dict) -- [REQUIRED]The range of time stamps to return.
            StartTimestamp (datetime) -- [REQUIRED]The starting time stamp in the range of time stamps for which to return fragments.
            EndTimestamp (datetime) -- [REQUIRED]The ending time stamp in the range of time stamps for which to return fragments.
            
            

    :rtype: dict
    :return: {
        'Fragments': [
            {
                'FragmentNumber': 'string',
                'FragmentSizeInBytes': 123,
                'ProducerTimestamp': datetime(2015, 1, 1),
                'ServerTimestamp': datetime(2015, 1, 1),
                'FragmentLengthInMilliseconds': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

