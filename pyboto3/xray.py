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

def batch_get_traces(TraceIds=None, NextToken=None):
    """
    Retrieves a list of traces specified by ID. Each trace is a collection of segment documents that originates from a single request. Use GetTraceSummaries to get a list of trace IDs.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_traces(
        TraceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type TraceIds: list
    :param TraceIds: [REQUIRED]
            Specify the trace IDs of requests for which to retrieve segments.
            (string) --
            

    :type NextToken: string
    :param NextToken: Pagination token. Not used.

    :rtype: dict
    :return: {
        'Traces': [
            {
                'Id': 'string',
                'Duration': 123.0,
                'Segments': [
                    {
                        'Id': 'string',
                        'Document': 'string'
                    },
                ]
            },
        ],
        'UnprocessedTraceIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

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

def get_service_graph(StartTime=None, EndTime=None, NextToken=None):
    """
    Retrieves a document that describes services that process incoming requests, and downstream services that they call as a result. Root services process incoming requests and make calls to downstream services. Root services are applications that use the AWS X-Ray SDK. Downstream services can be other applications, AWS resources, HTTP web APIs, or SQL databases.
    See also: AWS API Documentation
    
    
    :example: response = client.get_service_graph(
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        NextToken='string'
    )
    
    
    :type StartTime: datetime
    :param StartTime: [REQUIRED]
            The start of the time frame for which to generate a graph.
            

    :type EndTime: datetime
    :param EndTime: [REQUIRED]
            The end of the time frame for which to generate a graph.
            

    :type NextToken: string
    :param NextToken: Pagination token. Not used.

    :rtype: dict
    :return: {
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'Services': [
            {
                'ReferenceId': 123,
                'Name': 'string',
                'Names': [
                    'string',
                ],
                'Root': True|False,
                'AccountId': 'string',
                'Type': 'string',
                'State': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'Edges': [
                    {
                        'ReferenceId': 123,
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'SummaryStatistics': {
                            'OkCount': 123,
                            'ErrorStatistics': {
                                'ThrottleCount': 123,
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'FaultStatistics': {
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'TotalCount': 123,
                            'TotalResponseTime': 123.0
                        },
                        'ResponseTimeHistogram': [
                            {
                                'Value': 123.0,
                                'Count': 123
                            },
                        ],
                        'Aliases': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string'
                            },
                        ]
                    },
                ],
                'SummaryStatistics': {
                    'OkCount': 123,
                    'ErrorStatistics': {
                        'ThrottleCount': 123,
                        'OtherCount': 123,
                        'TotalCount': 123
                    },
                    'FaultStatistics': {
                        'OtherCount': 123,
                        'TotalCount': 123
                    },
                    'TotalCount': 123,
                    'TotalResponseTime': 123.0
                },
                'DurationHistogram': [
                    {
                        'Value': 123.0,
                        'Count': 123
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_trace_graph(TraceIds=None, NextToken=None):
    """
    Retrieves a service graph for one or more specific trace IDs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_trace_graph(
        TraceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type TraceIds: list
    :param TraceIds: [REQUIRED]
            Trace IDs of requests for which to generate a service graph.
            (string) --
            

    :type NextToken: string
    :param NextToken: Pagination token. Not used.

    :rtype: dict
    :return: {
        'Services': [
            {
                'ReferenceId': 123,
                'Name': 'string',
                'Names': [
                    'string',
                ],
                'Root': True|False,
                'AccountId': 'string',
                'Type': 'string',
                'State': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'Edges': [
                    {
                        'ReferenceId': 123,
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'SummaryStatistics': {
                            'OkCount': 123,
                            'ErrorStatistics': {
                                'ThrottleCount': 123,
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'FaultStatistics': {
                                'OtherCount': 123,
                                'TotalCount': 123
                            },
                            'TotalCount': 123,
                            'TotalResponseTime': 123.0
                        },
                        'ResponseTimeHistogram': [
                            {
                                'Value': 123.0,
                                'Count': 123
                            },
                        ],
                        'Aliases': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string'
                            },
                        ]
                    },
                ],
                'SummaryStatistics': {
                    'OkCount': 123,
                    'ErrorStatistics': {
                        'ThrottleCount': 123,
                        'OtherCount': 123,
                        'TotalCount': 123
                    },
                    'FaultStatistics': {
                        'OtherCount': 123,
                        'TotalCount': 123
                    },
                    'TotalCount': 123,
                    'TotalResponseTime': 123.0
                },
                'DurationHistogram': [
                    {
                        'Value': 123.0,
                        'Count': 123
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_trace_summaries(StartTime=None, EndTime=None, Sampling=None, FilterExpression=None, NextToken=None):
    """
    Retrieves IDs and metadata for traces available for a specified time frame using an optional filter. To get the full traces, pass the trace IDs to BatchGetTraces .
    See also: AWS API Documentation
    
    
    :example: response = client.get_trace_summaries(
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Sampling=True|False,
        FilterExpression='string',
        NextToken='string'
    )
    
    
    :type StartTime: datetime
    :param StartTime: [REQUIRED]
            The start of the time frame for which to retrieve traces.
            

    :type EndTime: datetime
    :param EndTime: [REQUIRED]
            The end of the time frame for which to retrieve traces.
            

    :type Sampling: boolean
    :param Sampling: Set to true to get summaries for only a subset of available traces.

    :type FilterExpression: string
    :param FilterExpression: Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.

    :type NextToken: string
    :param NextToken: Specify the pagination token returned by a previous request to retrieve the next page of results.

    :rtype: dict
    :return: {
        'TraceSummaries': [
            {
                'Id': 'string',
                'Duration': 123.0,
                'ResponseTime': 123.0,
                'HasFault': True|False,
                'HasError': True|False,
                'HasThrottle': True|False,
                'IsPartial': True|False,
                'Http': {
                    'HttpURL': 'string',
                    'HttpStatus': 123,
                    'HttpMethod': 'string',
                    'UserAgent': 'string',
                    'ClientIp': 'string'
                },
                'Annotations': {
                    'string': [
                        {
                            'AnnotationValue': {
                                'NumberValue': 123.0,
                                'BooleanValue': True|False,
                                'StringValue': 'string'
                            },
                            'ServiceIds': [
                                {
                                    'Name': 'string',
                                    'Names': [
                                        'string',
                                    ],
                                    'AccountId': 'string',
                                    'Type': 'string'
                                },
                            ]
                        },
                    ]
                },
                'Users': [
                    {
                        'UserName': 'string',
                        'ServiceIds': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'AccountId': 'string',
                                'Type': 'string'
                            },
                        ]
                    },
                ],
                'ServiceIds': [
                    {
                        'Name': 'string',
                        'Names': [
                            'string',
                        ],
                        'AccountId': 'string',
                        'Type': 'string'
                    },
                ]
            },
        ],
        'ApproximateTime': datetime(2015, 1, 1),
        'TracesProcessedCount': 123,
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    Name (string) --
    Names (list) --
    (string) --
    
    
    AccountId (string) --
    Type (string) --
    
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def put_telemetry_records(TelemetryRecords=None, EC2InstanceId=None, Hostname=None, ResourceARN=None):
    """
    Used by the AWS X-Ray daemon to upload telemetry.
    See also: AWS API Documentation
    
    
    :example: response = client.put_telemetry_records(
        TelemetryRecords=[
            {
                'Timestamp': datetime(2015, 1, 1),
                'SegmentsReceivedCount': 123,
                'SegmentsSentCount': 123,
                'SegmentsSpilloverCount': 123,
                'SegmentsRejectedCount': 123,
                'BackendConnectionErrors': {
                    'TimeoutCount': 123,
                    'ConnectionRefusedCount': 123,
                    'HTTPCode4XXCount': 123,
                    'HTTPCode5XXCount': 123,
                    'UnknownHostCount': 123,
                    'OtherCount': 123
                }
            },
        ],
        EC2InstanceId='string',
        Hostname='string',
        ResourceARN='string'
    )
    
    
    :type TelemetryRecords: list
    :param TelemetryRecords: [REQUIRED]
            (dict) --
            Timestamp (datetime) --
            SegmentsReceivedCount (integer) --
            SegmentsSentCount (integer) --
            SegmentsSpilloverCount (integer) --
            SegmentsRejectedCount (integer) --
            BackendConnectionErrors (dict) --
            TimeoutCount (integer) --
            ConnectionRefusedCount (integer) --
            HTTPCode4XXCount (integer) --
            HTTPCode5XXCount (integer) --
            UnknownHostCount (integer) --
            OtherCount (integer) --
            
            

    :type EC2InstanceId: string
    :param EC2InstanceId: 

    :type Hostname: string
    :param Hostname: 

    :type ResourceARN: string
    :param ResourceARN: 

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_trace_segments(TraceSegmentDocuments=None):
    """
    Uploads segment documents to AWS X-Ray. The X-Ray SDK generates segment documents and sends them to the X-Ray daemon, which uploads them in batches. A segment document can be a completed segment, an in-progress segment, or an array of subsegments.
    See also: AWS API Documentation
    
    
    :example: response = client.put_trace_segments(
        TraceSegmentDocuments=[
            'string',
        ]
    )
    
    
    :type TraceSegmentDocuments: list
    :param TraceSegmentDocuments: [REQUIRED]
            A JSON document defining one or more segments or subsegments. Segments must include the following fields.
            Required Segment Document Fields
            name - The name of the service that handled the request.
            id - A 64-bit identifier for the segment, unique among segments in the same trace, in 16 hexadecimal digits.
            trace_id - A unique identifier that connects all segments and subsegments originating from a single client request.
            start_time - Time the segment or subsegment was created, in floating point seconds in epoch time, accurate to milliseconds. For example, 1480615200.010 or 1.480615200010E9 .
            end_time - Time the segment or subsegment was closed. For example, 1480615200.090 or 1.480615200090E9 . Specify either an end_time or in_progress .
            in_progress - Set to true instead of specifying an end_time to record that a segment has been started, but is not complete. Send an in progress segment when your application receives a request that will take a long time to serve, to trace the fact that the request was received. When the response is sent, send the complete segment to overwrite the in-progress segment.
            A trace_id consists of three numbers separated by hyphens. For example, 1-58406520-a006649127e371903a2de979. This includes:
            Trace ID Format
            The version number, i.e. 1 .
            The time of the original request, in Unix epoch time, in 8 hexadecimal digits. For example, 10:00AM December 2nd, 2016 PST in epoch time is 1480615200 seconds, or 58406520 in hexadecimal.
            A 96-bit identifier for the trace, globally unique, in 24 hexadecimal digits.
            (string) --
            

    :rtype: dict
    :return: {
        'UnprocessedTraceSegments': [
            {
                'Id': 'string',
                'ErrorCode': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    :returns: 
    The version number, i.e. 1 .
    The time of the original request, in Unix epoch time, in 8 hexadecimal digits. For example, 10:00AM December 2nd, 2016 PST in epoch time is 1480615200 seconds, or 58406520 in hexadecimal.
    A 96-bit identifier for the trace, globally unique, in 24 hexadecimal digits.
    
    """
    pass

