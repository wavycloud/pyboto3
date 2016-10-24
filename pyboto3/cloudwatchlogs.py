'''

The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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

def cancel_export_task(taskId=None):
    """
    Cancels an export task if it is in PENDING or RUNNING state.
    
    
    :example: response = client.cancel_export_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]
            Id of the export task to cancel.
            

    """
    pass

def create_export_task(taskName=None, logGroupName=None, logStreamNamePrefix=None, fromTime=None, to=None, destination=None, destinationPrefix=None):
    """
    Creates an ExportTask which allows you to efficiently export data from a Log Group to your Amazon S3 bucket.
    This is an asynchronous call. If all the required information is provided, this API will initiate an export task and respond with the task Id. Once started, DescribeExportTasks can be used to get the status of an export task. You can only have one active (RUNNING or PENDING ) export task at a time, per account.
    You can export logs from multiple log groups or multiple time ranges to the same Amazon S3 bucket. To separate out log data for each export task, you can specify a prefix that will be used as the Amazon S3 key prefix for all exported objects.
    
    
    :example: response = client.create_export_task(
        taskName='string',
        logGroupName='string',
        logStreamNamePrefix='string',
        fromTime=123,
        to=123,
        destination='string',
        destinationPrefix='string'
    )
    
    
    :type taskName: string
    :param taskName: The name of the export task.

    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group to export.
            

    :type logStreamNamePrefix: string
    :param logStreamNamePrefix: Will only export log streams that match the provided logStreamNamePrefix. If you don't specify a value, no prefix filter is applied.

    :type fromTime: integer
    :param fromTime: [REQUIRED]
            A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. It indicates the start time of the range for the request. Events with a timestamp prior to this time will not be exported.
            

    :type to: integer
    :param to: [REQUIRED]
            A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. It indicates the end time of the range for the request. Events with a timestamp later than this time will not be exported.
            

    :type destination: string
    :param destination: [REQUIRED]
            Name of Amazon S3 bucket to which the log data will be exported.
            Note: Only buckets in the same AWS region are supported.
            

    :type destinationPrefix: string
    :param destinationPrefix: Prefix that will be used as the start of Amazon S3 key for every object exported. If not specified, this defaults to 'exportedlogs'.

    :rtype: dict
    :return: {
        'taskId': 'string'
    }
    
    
    """
    pass

def create_log_group(logGroupName=None):
    """
    Creates a new log group with the specified name. The name of the log group must be unique within a region for an AWS account. You can create up to 500 log groups per account.
    You must use the following guidelines when naming a log group:
    
    
    :example: response = client.create_log_group(
        logGroupName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group to create.
            

    """
    pass

def create_log_stream(logGroupName=None, logStreamName=None):
    """
    Creates a new log stream in the specified log group. The name of the log stream must be unique within the log group. There is no limit on the number of log streams that can exist in a log group.
    You must use the following guidelines when naming a log stream:
    
    
    :example: response = client.create_log_stream(
        logGroupName='string',
        logStreamName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group under which the log stream is to be created.
            

    :type logStreamName: string
    :param logStreamName: [REQUIRED]
            The name of the log stream to create.
            

    :returns: 
    logGroupName (string) -- [REQUIRED]
    The name of the log group under which the log stream is to be created.
    
    logStreamName (string) -- [REQUIRED]
    The name of the log stream to create.
    
    
    """
    pass

def delete_destination(destinationName=None):
    """
    Deletes the destination with the specified name and eventually disables all the subscription filters that publish to it. This will not delete the physical resource encapsulated by the destination.
    
    
    :example: response = client.delete_destination(
        destinationName='string'
    )
    
    
    :type destinationName: string
    :param destinationName: [REQUIRED]
            The name of destination to delete.
            

    """
    pass

def delete_log_group(logGroupName=None):
    """
    Deletes the log group with the specified name and permanently deletes all the archived log events associated with it.
    
    
    :example: response = client.delete_log_group(
        logGroupName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group to delete.
            

    """
    pass

def delete_log_stream(logGroupName=None, logStreamName=None):
    """
    Deletes a log stream and permanently deletes all the archived log events associated with it.
    
    
    :example: response = client.delete_log_stream(
        logGroupName='string',
        logStreamName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group under which the log stream to delete belongs.
            

    :type logStreamName: string
    :param logStreamName: [REQUIRED]
            The name of the log stream to delete.
            

    """
    pass

def delete_metric_filter(logGroupName=None, filterName=None):
    """
    Deletes a metric filter associated with the specified log group.
    
    
    :example: response = client.delete_metric_filter(
        logGroupName='string',
        filterName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group that is associated with the metric filter to delete.
            

    :type filterName: string
    :param filterName: [REQUIRED]
            The name of the metric filter to delete.
            

    """
    pass

def delete_retention_policy(logGroupName=None):
    """
    Deletes the retention policy of the specified log group. Log events would not expire if they belong to log groups without a retention policy.
    
    
    :example: response = client.delete_retention_policy(
        logGroupName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group that is associated with the retention policy to delete.
            

    """
    pass

def delete_subscription_filter(logGroupName=None, filterName=None):
    """
    Deletes a subscription filter associated with the specified log group.
    
    
    :example: response = client.delete_subscription_filter(
        logGroupName='string',
        filterName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group that is associated with the subscription filter to delete.
            

    :type filterName: string
    :param filterName: [REQUIRED]
            The name of the subscription filter to delete.
            

    """
    pass

def describe_destinations(DestinationNamePrefix=None, nextToken=None, limit=None):
    """
    Returns all the destinations that are associated with the AWS account making the request. The list returned in the response is ASCII-sorted by destination name.
    By default, this operation returns up to 50 destinations. If there are more destinations to list, the response would contain a nextToken value in the response body. You can also limit the number of destinations returned in the response by specifying the limit parameter in the request.
    
    
    :example: response = client.describe_destinations(
        DestinationNamePrefix='string',
        nextToken='string',
        limit=123
    )
    
    
    :type DestinationNamePrefix: string
    :param DestinationNamePrefix: Will only return destinations that match the provided destinationNamePrefix. If you don't specify a value, no prefix is applied.

    :type nextToken: string
    :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous request. The token expires after 24 hours.

    :type limit: integer
    :param limit: The maximum number of results to return.

    :rtype: dict
    :return: {
        'destinations': [
            {
                'destinationName': 'string',
                'targetArn': 'string',
                'roleArn': 'string',
                'accessPolicy': 'string',
                'arn': 'string',
                'creationTime': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_export_tasks(taskId=None, statusCode=None, nextToken=None, limit=None):
    """
    Returns all the export tasks that are associated with the AWS account making the request. The export tasks can be filtered based on TaskId or TaskStatus .
    By default, this operation returns up to 50 export tasks that satisfy the specified filters. If there are more export tasks to list, the response would contain a nextToken value in the response body. You can also limit the number of export tasks returned in the response by specifying the limit parameter in the request.
    
    
    :example: response = client.describe_export_tasks(
        taskId='string',
        statusCode='CANCELLED'|'COMPLETED'|'FAILED'|'PENDING'|'PENDING_CANCEL'|'RUNNING',
        nextToken='string',
        limit=123
    )
    
    
    :type taskId: string
    :param taskId: Export task that matches the specified task Id will be returned. This can result in zero or one export task.

    :type statusCode: string
    :param statusCode: All export tasks that matches the specified status code will be returned. This can return zero or more export tasks.

    :type nextToken: string
    :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous DescribeExportTasks request.

    :type limit: integer
    :param limit: The maximum number of items returned in the response. If you don't specify a value, the request would return up to 50 items.

    :rtype: dict
    :return: {
        'exportTasks': [
            {
                'taskId': 'string',
                'taskName': 'string',
                'logGroupName': 'string',
                'from': 123,
                'to': 123,
                'destination': 'string',
                'destinationPrefix': 'string',
                'status': {
                    'code': 'CANCELLED'|'COMPLETED'|'FAILED'|'PENDING'|'PENDING_CANCEL'|'RUNNING',
                    'message': 'string'
                },
                'executionInfo': {
                    'creationTime': 123,
                    'completionTime': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_log_groups(logGroupNamePrefix=None, nextToken=None, limit=None):
    """
    Returns all the log groups that are associated with the AWS account making the request. The list returned in the response is ASCII-sorted by log group name.
    By default, this operation returns up to 50 log groups. If there are more log groups to list, the response would contain a nextToken value in the response body. You can also limit the number of log groups returned in the response by specifying the limit parameter in the request.
    
    
    :example: response = client.describe_log_groups(
        logGroupNamePrefix='string',
        nextToken='string',
        limit=123
    )
    
    
    :type logGroupNamePrefix: string
    :param logGroupNamePrefix: Will only return log groups that match the provided logGroupNamePrefix. If you don't specify a value, no prefix filter is applied.

    :type nextToken: string
    :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous DescribeLogGroups request.

    :type limit: integer
    :param limit: The maximum number of items returned in the response. If you don't specify a value, the request would return up to 50 items.

    :rtype: dict
    :return: {
        'logGroups': [
            {
                'logGroupName': 'string',
                'creationTime': 123,
                'retentionInDays': 123,
                'metricFilterCount': 123,
                'arn': 'string',
                'storedBytes': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_log_streams(logGroupName=None, logStreamNamePrefix=None, orderBy=None, descending=None, nextToken=None, limit=None):
    """
    Returns all the log streams that are associated with the specified log group. The list returned in the response is ASCII-sorted by log stream name.
    By default, this operation returns up to 50 log streams. If there are more log streams to list, the response would contain a nextToken value in the response body. You can also limit the number of log streams returned in the response by specifying the limit parameter in the request. This operation has a limit of five transactions per second, after which transactions are throttled.
    
    
    :example: response = client.describe_log_streams(
        logGroupName='string',
        logStreamNamePrefix='string',
        orderBy='LogStreamName'|'LastEventTime',
        descending=True|False,
        nextToken='string',
        limit=123
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The log group name for which log streams are to be listed.
            

    :type logStreamNamePrefix: string
    :param logStreamNamePrefix: Will only return log streams that match the provided logStreamNamePrefix. If you don't specify a value, no prefix filter is applied.

    :type orderBy: string
    :param orderBy: Specifies what to order the returned log streams by. Valid arguments are 'LogStreamName' or 'LastEventTime'. If you don't specify a value, results are ordered by LogStreamName. If 'LastEventTime' is chosen, the request cannot also contain a logStreamNamePrefix.

    :type descending: boolean
    :param descending: If set to true, results are returned in descending order. If you don't specify a value or set it to false, results are returned in ascending order.

    :type nextToken: string
    :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous DescribeLogStreams request.

    :type limit: integer
    :param limit: The maximum number of items returned in the response. If you don't specify a value, the request would return up to 50 items.

    :rtype: dict
    :return: {
        'logStreams': [
            {
                'logStreamName': 'string',
                'creationTime': 123,
                'firstEventTimestamp': 123,
                'lastEventTimestamp': 123,
                'lastIngestionTime': 123,
                'uploadSequenceToken': 'string',
                'arn': 'string',
                'storedBytes': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_metric_filters(logGroupName=None, filterNamePrefix=None, nextToken=None, limit=None):
    """
    Returns all the metrics filters associated with the specified log group. The list returned in the response is ASCII-sorted by filter name.
    By default, this operation returns up to 50 metric filters. If there are more metric filters to list, the response would contain a nextToken value in the response body. You can also limit the number of metric filters returned in the response by specifying the limit parameter in the request.
    
    
    :example: response = client.describe_metric_filters(
        logGroupName='string',
        filterNamePrefix='string',
        nextToken='string',
        limit=123
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The log group name for which metric filters are to be listed.
            

    :type filterNamePrefix: string
    :param filterNamePrefix: Will only return metric filters that match the provided filterNamePrefix. If you don't specify a value, no prefix filter is applied.

    :type nextToken: string
    :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous DescribeMetricFilters request.

    :type limit: integer
    :param limit: The maximum number of items returned in the response. If you don't specify a value, the request would return up to 50 items.

    :rtype: dict
    :return: {
        'metricFilters': [
            {
                'filterName': 'string',
                'filterPattern': 'string',
                'metricTransformations': [
                    {
                        'metricName': 'string',
                        'metricNamespace': 'string',
                        'metricValue': 'string',
                        'defaultValue': 123.0
                    },
                ],
                'creationTime': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_subscription_filters(logGroupName=None, filterNamePrefix=None, nextToken=None, limit=None):
    """
    Returns all the subscription filters associated with the specified log group. The list returned in the response is ASCII-sorted by filter name.
    By default, this operation returns up to 50 subscription filters. If there are more subscription filters to list, the response would contain a nextToken value in the response body. You can also limit the number of subscription filters returned in the response by specifying the limit parameter in the request.
    
    
    :example: response = client.describe_subscription_filters(
        logGroupName='string',
        filterNamePrefix='string',
        nextToken='string',
        limit=123
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The log group name for which subscription filters are to be listed.
            

    :type filterNamePrefix: string
    :param filterNamePrefix: Will only return subscription filters that match the provided filterNamePrefix. If you don't specify a value, no prefix filter is applied.

    :type nextToken: string
    :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the response of the previous request. The token expires after 24 hours.

    :type limit: integer
    :param limit: The maximum number of results to return.

    :rtype: dict
    :return: {
        'subscriptionFilters': [
            {
                'filterName': 'string',
                'logGroupName': 'string',
                'filterPattern': 'string',
                'destinationArn': 'string',
                'roleArn': 'string',
                'creationTime': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def filter_log_events(logGroupName=None, logStreamNames=None, startTime=None, endTime=None, filterPattern=None, nextToken=None, limit=None, interleaved=None):
    """
    Retrieves log events, optionally filtered by a filter pattern from the specified log group. You can provide an optional time range to filter the results on the event timestamp . You can limit the streams searched to an explicit list of logStreamNames .
    By default, this operation returns as much matching log events as can fit in a response size of 1MB, up to 10,000 log events, or all the events found within a time-bounded scan window. If the response includes a nextToken , then there is more data to search, and the search can be resumed with a new request providing the nextToken. The response will contain a list of searchedLogStreams that contains information about which streams were searched in the request and whether they have been searched completely or require further pagination. The limit parameter in the request can be used to specify the maximum number of events to return in a page.
    
    
    :example: response = client.filter_log_events(
        logGroupName='string',
        logStreamNames=[
            'string',
        ],
        startTime=123,
        endTime=123,
        filterPattern='string',
        nextToken='string',
        limit=123,
        interleaved=True|False
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group to query.
            

    :type logStreamNames: list
    :param logStreamNames: Optional list of log stream names within the specified log group to search. Defaults to all the log streams in the log group.
            (string) --
            

    :type startTime: integer
    :param startTime: A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. If provided, events with a timestamp prior to this time are not returned.

    :type endTime: integer
    :param endTime: A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. If provided, events with a timestamp later than this time are not returned.

    :type filterPattern: string
    :param filterPattern: A valid CloudWatch Logs filter pattern to use for filtering the response. If not provided, all the events are matched.

    :type nextToken: string
    :param nextToken: A pagination token obtained from a FilterLogEvents response to continue paginating the FilterLogEvents results. This token is omitted from the response when there are no other events to display.

    :type limit: integer
    :param limit: The maximum number of events to return in a page of results. Default is 10,000 events.

    :type interleaved: boolean
    :param interleaved: If provided, the API will make a best effort to provide responses that contain events from multiple log streams within the log group interleaved in a single response. If not provided, all the matched log events in the first log stream will be searched first, then those in the next log stream, etc.

    :rtype: dict
    :return: {
        'events': [
            {
                'logStreamName': 'string',
                'timestamp': 123,
                'message': 'string',
                'ingestionTime': 123,
                'eventId': 'string'
            },
        ],
        'searchedLogStreams': [
            {
                'logStreamName': 'string',
                'searchedCompletely': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
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

def get_log_events(logGroupName=None, logStreamName=None, startTime=None, endTime=None, nextToken=None, limit=None, startFromHead=None):
    """
    Retrieves log events from the specified log stream. You can provide an optional time range to filter the results on the event timestamp .
    By default, this operation returns as much log events as can fit in a response size of 1MB, up to 10,000 log events. The response will always include a nextForwardToken and a nextBackwardToken in the response body. You can use any of these tokens in subsequent GetLogEvents requests to paginate through events in either forward or backward direction. You can also limit the number of log events returned in the response by specifying the limit parameter in the request.
    
    
    :example: response = client.get_log_events(
        logGroupName='string',
        logStreamName='string',
        startTime=123,
        endTime=123,
        nextToken='string',
        limit=123,
        startFromHead=True|False
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group to query.
            

    :type logStreamName: string
    :param logStreamName: [REQUIRED]
            The name of the log stream to query.
            

    :type startTime: integer
    :param startTime: A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.

    :type endTime: integer
    :param endTime: A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.

    :type nextToken: string
    :param nextToken: A string token used for pagination that points to the next page of results. It must be a value obtained from the nextForwardToken or nextBackwardToken fields in the response of the previous GetLogEvents request.

    :type limit: integer
    :param limit: The maximum number of log events returned in the response. If you don't specify a value, the request would return as many log events as can fit in a response size of 1MB, up to 10,000 log events.

    :type startFromHead: boolean
    :param startFromHead: If set to true, the earliest log events would be returned first. The default is false (the latest log events are returned first).

    :rtype: dict
    :return: {
        'events': [
            {
                'timestamp': 123,
                'message': 'string',
                'ingestionTime': 123
            },
        ],
        'nextForwardToken': 'string',
        'nextBackwardToken': 'string'
    }
    
    
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

def put_destination(destinationName=None, targetArn=None, roleArn=None):
    """
    Creates or updates a Destination . A destination encapsulates a physical resource (such as a Kinesis stream) and allows you to subscribe to a real-time stream of log events of a different account, ingested through PutLogEvents requests. Currently, the only supported physical resource is a Amazon Kinesis stream belonging to the same account as the destination.
    A destination controls what is written to its Amazon Kinesis stream through an access policy. By default, PutDestination does not set any access policy with the destination, which means a cross-account user will not be able to call PutSubscriptionFilter against this destination. To enable that, the destination owner must call PutDestinationPolicy after PutDestination.
    
    
    :example: response = client.put_destination(
        destinationName='string',
        targetArn='string',
        roleArn='string'
    )
    
    
    :type destinationName: string
    :param destinationName: [REQUIRED]
            A name for the destination.
            

    :type targetArn: string
    :param targetArn: [REQUIRED]
            The ARN of an Amazon Kinesis stream to deliver matching log events to.
            

    :type roleArn: string
    :param roleArn: [REQUIRED]
            The ARN of an IAM role that grants CloudWatch Logs permissions to do Amazon Kinesis PutRecord requests on the destination stream.
            

    :rtype: dict
    :return: {
        'destination': {
            'destinationName': 'string',
            'targetArn': 'string',
            'roleArn': 'string',
            'accessPolicy': 'string',
            'arn': 'string',
            'creationTime': 123
        }
    }
    
    
    """
    pass

def put_destination_policy(destinationName=None, accessPolicy=None):
    """
    Creates or updates an access policy associated with an existing Destination . An access policy is an IAM policy document that is used to authorize claims to register a subscription filter against a given destination.
    
    
    :example: response = client.put_destination_policy(
        destinationName='string',
        accessPolicy='string'
    )
    
    
    :type destinationName: string
    :param destinationName: [REQUIRED]
            A name for an existing destination.
            

    :type accessPolicy: string
    :param accessPolicy: [REQUIRED]
            An IAM policy document that authorizes cross-account users to deliver their log events to associated destination.
            

    """
    pass

def put_log_events(logGroupName=None, logStreamName=None, logEvents=None, sequenceToken=None):
    """
    Uploads a batch of log events to the specified log stream.
    Every PutLogEvents request must include the sequenceToken obtained from the response of the previous request. An upload in a newly created log stream does not require a sequenceToken . You can also get the sequenceToken using  DescribeLogStreams .
    The batch of events must satisfy the following constraints:
    
    
    :example: response = client.put_log_events(
        logGroupName='string',
        logStreamName='string',
        logEvents=[
            {
                'timestamp': 123,
                'message': 'string'
            },
        ],
        sequenceToken='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group to put log events to.
            

    :type logStreamName: string
    :param logStreamName: [REQUIRED]
            The name of the log stream to put log events to.
            

    :type logEvents: list
    :param logEvents: [REQUIRED]
            A list of log events belonging to a log stream.
            (dict) --A log event is a record of some activity that was recorded by the application or resource being monitored. The log event record that CloudWatch Logs understands contains two properties: the timestamp of when the event occurred, and the raw event message.
            timestamp (integer) -- [REQUIRED]A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
            message (string) -- [REQUIRED]
            

    :type sequenceToken: string
    :param sequenceToken: A string token that must be obtained from the response of the previous PutLogEvents request.

    :rtype: dict
    :return: {
        'nextSequenceToken': 'string',
        'rejectedLogEventsInfo': {
            'tooNewLogEventStartIndex': 123,
            'tooOldLogEventEndIndex': 123,
            'expiredLogEventEndIndex': 123
        }
    }
    
    
    :returns: 
    logGroupName (string) -- [REQUIRED]
    The name of the log group to put log events to.
    
    logStreamName (string) -- [REQUIRED]
    The name of the log stream to put log events to.
    
    logEvents (list) -- [REQUIRED]
    A list of log events belonging to a log stream.
    
    (dict) --A log event is a record of some activity that was recorded by the application or resource being monitored. The log event record that CloudWatch Logs understands contains two properties: the timestamp of when the event occurred, and the raw event message.
    
    timestamp (integer) -- [REQUIRED]A point in time expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
    
    message (string) -- [REQUIRED]
    
    
    
    
    sequenceToken (string) -- A string token that must be obtained from the response of the previous PutLogEvents request.
    
    """
    pass

def put_metric_filter(logGroupName=None, filterName=None, filterPattern=None, metricTransformations=None):
    """
    Creates or updates a metric filter and associates it with the specified log group. Metric filters allow you to configure rules to extract metric data from log events ingested through PutLogEvents requests.
    The maximum number of metric filters that can be associated with a log group is 100.
    
    
    :example: response = client.put_metric_filter(
        logGroupName='string',
        filterName='string',
        filterPattern='string',
        metricTransformations=[
            {
                'metricName': 'string',
                'metricNamespace': 'string',
                'metricValue': 'string',
                'defaultValue': 123.0
            },
        ]
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group to associate the metric filter with.
            

    :type filterName: string
    :param filterName: [REQUIRED]
            A name for the metric filter.
            

    :type filterPattern: string
    :param filterPattern: [REQUIRED]
            A valid CloudWatch Logs filter pattern for extracting metric data out of ingested log events.
            

    :type metricTransformations: list
    :param metricTransformations: [REQUIRED]
            A collection of information needed to define how metric data gets emitted.
            (dict) --
            metricName (string) -- [REQUIRED]Name of the metric.
            metricNamespace (string) -- [REQUIRED]Namespace to which the metric belongs.
            metricValue (string) -- [REQUIRED]A string representing a value to publish to this metric when a filter pattern matches a log event.
            defaultValue (float) --(Optional) A default value to emit when a filter pattern does not match a log event. Can be null.
            
            

    """
    pass

def put_retention_policy(logGroupName=None, retentionInDays=None):
    """
    Sets the retention of the specified log group. A retention policy allows you to configure the number of days you want to retain log events in the specified log group.
    
    
    :example: response = client.put_retention_policy(
        logGroupName='string',
        retentionInDays=123
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group to associate the retention policy with.
            

    :type retentionInDays: integer
    :param retentionInDays: [REQUIRED]
            Specifies the number of days you want to retain log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653.
            

    """
    pass

def put_subscription_filter(logGroupName=None, filterName=None, filterPattern=None, destinationArn=None, roleArn=None):
    """
    Creates or updates a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events ingested through PutLogEvents requests and have them delivered to a specific destination. Currently, the supported destinations are:
    Currently there can only be one subscription filter associated with a log group.
    
    
    :example: response = client.put_subscription_filter(
        logGroupName='string',
        filterName='string',
        filterPattern='string',
        destinationArn='string',
        roleArn='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group to associate the subscription filter with.
            

    :type filterName: string
    :param filterName: [REQUIRED]
            A name for the subscription filter.
            

    :type filterPattern: string
    :param filterPattern: [REQUIRED]
            A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.
            

    :type destinationArn: string
    :param destinationArn: [REQUIRED]
            The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:
            An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.
            A logical destination (used via an ARN of Destination ) belonging to a different account, for cross-account delivery.
            An Amazon Kinesis Firehose stream belonging to the same account as the subscription filter, for same-account delivery.
            An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery.
            

    :type roleArn: string
    :param roleArn: The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination (used via an ARN of Destination ) for cross-account delivery.

    :returns: 
    logGroupName (string) -- [REQUIRED]
    The name of the log group to associate the subscription filter with.
    
    filterName (string) -- [REQUIRED]
    A name for the subscription filter.
    
    filterPattern (string) -- [REQUIRED]
    A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.
    
    destinationArn (string) -- [REQUIRED]
    The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:
    
    An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.
    A logical destination (used via an ARN of Destination ) belonging to a different account, for cross-account delivery.
    An Amazon Kinesis Firehose stream belonging to the same account as the subscription filter, for same-account delivery.
    An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery.
    
    
    roleArn (string) -- The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination (used via an ARN of Destination ) for cross-account delivery.
    
    """
    pass

def test_metric_filter(filterPattern=None, logEventMessages=None):
    """
    Tests the filter pattern of a metric filter against a sample of log event messages. You can use this operation to validate the correctness of a metric filter pattern.
    
    
    :example: response = client.test_metric_filter(
        filterPattern='string',
        logEventMessages=[
            'string',
        ]
    )
    
    
    :type filterPattern: string
    :param filterPattern: [REQUIRED]
            A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain timestamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.
            

    :type logEventMessages: list
    :param logEventMessages: [REQUIRED]
            A list of log event messages to test.
            (string) --
            

    :rtype: dict
    :return: {
        'matches': [
            {
                'eventNumber': 123,
                'eventMessage': 'string',
                'extractedValues': {
                    'string': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (dict) --
    matches (list) --
    (dict) --
    eventNumber (integer) --
    eventMessage (string) --
    extractedValues (dict) --
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

