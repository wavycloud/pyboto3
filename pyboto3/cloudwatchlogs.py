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

def cancel_export_task(taskId=None):
    """
    Cancels the specified export task.
    The task must be in the PENDING or RUNNING state.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_export_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]
            The ID of the export task.
            

    """
    pass

def create_export_task(taskName=None, logGroupName=None, logStreamNamePrefix=None, fromTime=None, to=None, destination=None, destinationPrefix=None):
    """
    Creates an export task, which allows you to efficiently export data from a log group to an Amazon S3 bucket.
    This is an asynchronous call. If all the required information is provided, this operation initiates an export task and responds with the ID of the task. After the task has started, you can use  DescribeExportTasks to get the status of the export task. Each account can only have one active (RUNNING or PENDING ) export task at a time. To cancel an export task, use  CancelExportTask .
    You can export logs from multiple log groups or multiple time ranges to the same S3 bucket. To separate out log data for each export task, you can specify a prefix that will be used as the Amazon S3 key prefix for all exported objects.
    See also: AWS API Documentation
    
    
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
            The name of the log group.
            

    :type logStreamNamePrefix: string
    :param logStreamNamePrefix: Export only log streams that match the provided prefix. If you don't specify a value, no prefix filter is applied.

    :type fromTime: integer
    :param fromTime: [REQUIRED]
            The start time of the range for the request, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. Events with a timestamp earlier than this time are not exported.
            

    :type to: integer
    :param to: [REQUIRED]
            The end time of the range for the request, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. Events with a timestamp later than this time are not exported.
            

    :type destination: string
    :param destination: [REQUIRED]
            The name of S3 bucket for the exported log data. The bucket must be in the same AWS region.
            

    :type destinationPrefix: string
    :param destinationPrefix: The prefix used as the start of the key for every object exported. If you don't specify a value, the default is exportedlogs .

    :rtype: dict
    :return: {
        'taskId': 'string'
    }
    
    
    """
    pass

def create_log_group(logGroupName=None, tags=None):
    """
    Creates a log group with the specified name.
    You can create up to 5000 log groups per account.
    You must use the following guidelines when naming a log group:
    See also: AWS API Documentation
    
    
    :example: response = client.create_log_group(
        logGroupName='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type tags: dict
    :param tags: The key-value pairs to use for the tags.
            (string) --
            (string) --
            

    :returns: 
    logGroupName (string) -- [REQUIRED]
    The name of the log group.
    
    tags (dict) -- The key-value pairs to use for the tags.
    
    (string) --
    (string) --
    
    
    
    
    
    """
    pass

def create_log_stream(logGroupName=None, logStreamName=None):
    """
    Creates a log stream for the specified log group.
    There is no limit on the number of log streams that you can create for a log group.
    You must use the following guidelines when naming a log stream:
    See also: AWS API Documentation
    
    
    :example: response = client.create_log_stream(
        logGroupName='string',
        logStreamName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type logStreamName: string
    :param logStreamName: [REQUIRED]
            The name of the log stream.
            

    :returns: 
    logGroupName (string) -- [REQUIRED]
    The name of the log group.
    
    logStreamName (string) -- [REQUIRED]
    The name of the log stream.
    
    
    """
    pass

def delete_destination(destinationName=None):
    """
    Deletes the specified destination, and eventually disables all the subscription filters that publish to it. This operation does not delete the physical resource encapsulated by the destination.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_destination(
        destinationName='string'
    )
    
    
    :type destinationName: string
    :param destinationName: [REQUIRED]
            The name of the destination.
            

    """
    pass

def delete_log_group(logGroupName=None):
    """
    Deletes the specified log group and permanently deletes all the archived log events associated with the log group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_log_group(
        logGroupName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    """
    pass

def delete_log_stream(logGroupName=None, logStreamName=None):
    """
    Deletes the specified log stream and permanently deletes all the archived log events associated with the log stream.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_log_stream(
        logGroupName='string',
        logStreamName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type logStreamName: string
    :param logStreamName: [REQUIRED]
            The name of the log stream.
            

    """
    pass

def delete_metric_filter(logGroupName=None, filterName=None):
    """
    Deletes the specified metric filter.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_metric_filter(
        logGroupName='string',
        filterName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type filterName: string
    :param filterName: [REQUIRED]
            The name of the metric filter.
            

    """
    pass

def delete_retention_policy(logGroupName=None):
    """
    Deletes the specified retention policy.
    Log events do not expire if they belong to log groups without a retention policy.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_retention_policy(
        logGroupName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    """
    pass

def delete_subscription_filter(logGroupName=None, filterName=None):
    """
    Deletes the specified subscription filter.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_subscription_filter(
        logGroupName='string',
        filterName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type filterName: string
    :param filterName: [REQUIRED]
            The name of the subscription filter.
            

    """
    pass

def describe_destinations(DestinationNamePrefix=None, nextToken=None, limit=None):
    """
    Lists all your destinations. The results are ASCII-sorted by destination name.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_destinations(
        DestinationNamePrefix='string',
        nextToken='string',
        limit=123
    )
    
    
    :type DestinationNamePrefix: string
    :param DestinationNamePrefix: The prefix to match. If you don't specify a value, no prefix filter is applied.

    :type nextToken: string
    :param nextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type limit: integer
    :param limit: The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

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
    Lists the specified export tasks. You can list all your export tasks or filter the results based on task ID or task status.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_export_tasks(
        taskId='string',
        statusCode='CANCELLED'|'COMPLETED'|'FAILED'|'PENDING'|'PENDING_CANCEL'|'RUNNING',
        nextToken='string',
        limit=123
    )
    
    
    :type taskId: string
    :param taskId: The ID of the export task. Specifying a task ID filters the results to zero or one export tasks.

    :type statusCode: string
    :param statusCode: The status code of the export task. Specifying a status code filters the results to zero or more export tasks.

    :type nextToken: string
    :param nextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type limit: integer
    :param limit: The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

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
    Lists the specified log groups. You can list all your log groups or filter the results by prefix. The results are ASCII-sorted by log group name.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_log_groups(
        logGroupNamePrefix='string',
        nextToken='string',
        limit=123
    )
    
    
    :type logGroupNamePrefix: string
    :param logGroupNamePrefix: The prefix to match.

    :type nextToken: string
    :param nextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type limit: integer
    :param limit: The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

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
    Lists the log streams for the specified log group. You can list all the log streams or filter the results by prefix. You can also control how the results are ordered.
    This operation has a limit of five transactions per second, after which transactions are throttled.
    See also: AWS API Documentation
    
    
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
            The name of the log group.
            

    :type logStreamNamePrefix: string
    :param logStreamNamePrefix: The prefix to match.
            You cannot specify this parameter if orderBy is LastEventTime .
            

    :type orderBy: string
    :param orderBy: If the value is LogStreamName , the results are ordered by log stream name. If the value is LastEventTime , the results are ordered by the event time. The default value is LogStreamName .
            If you order the results by event time, you cannot specify the logStreamNamePrefix parameter.
            lastEventTimestamp represents the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. lastEventTimeStamp updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but may take longer in some rare situations.
            

    :type descending: boolean
    :param descending: If the value is true, results are returned in descending order. If the value is to false, results are returned in ascending order. The default value is false.

    :type nextToken: string
    :param nextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type limit: integer
    :param limit: The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

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

def describe_metric_filters(logGroupName=None, filterNamePrefix=None, nextToken=None, limit=None, metricName=None, metricNamespace=None):
    """
    Lists the specified metric filters. You can list all the metric filters or filter the results by log name, prefix, metric name, and metric namespace. The results are ASCII-sorted by filter name.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_metric_filters(
        logGroupName='string',
        filterNamePrefix='string',
        nextToken='string',
        limit=123,
        metricName='string',
        metricNamespace='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: The name of the log group.

    :type filterNamePrefix: string
    :param filterNamePrefix: The prefix to match.

    :type nextToken: string
    :param nextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type limit: integer
    :param limit: The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

    :type metricName: string
    :param metricName: The name of the CloudWatch metric.

    :type metricNamespace: string
    :param metricNamespace: The namespace of the CloudWatch metric.

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
                'creationTime': 123,
                'logGroupName': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_subscription_filters(logGroupName=None, filterNamePrefix=None, nextToken=None, limit=None):
    """
    Lists the subscription filters for the specified log group. You can list all the subscription filters or filter the results by prefix. The results are ASCII-sorted by filter name.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_subscription_filters(
        logGroupName='string',
        filterNamePrefix='string',
        nextToken='string',
        limit=123
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type filterNamePrefix: string
    :param filterNamePrefix: The prefix to match. If you don't specify a value, no prefix filter is applied.

    :type nextToken: string
    :param nextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type limit: integer
    :param limit: The maximum number of items returned. If you don't specify a value, the default is up to 50 items.

    :rtype: dict
    :return: {
        'subscriptionFilters': [
            {
                'filterName': 'string',
                'logGroupName': 'string',
                'filterPattern': 'string',
                'destinationArn': 'string',
                'roleArn': 'string',
                'distribution': 'Random'|'ByLogStream',
                'creationTime': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def filter_log_events(logGroupName=None, logStreamNames=None, startTime=None, endTime=None, filterPattern=None, nextToken=None, limit=None, interleaved=None):
    """
    Lists log events from the specified log group. You can list all the log events or filter the results using a filter pattern, a time range, and the name of the log stream.
    By default, this operation returns as many log events as can fit in 1MB (up to 10,000 log events), or all the events found within the time range that you specify. If the results include a token, then there are more log events available, and you can get additional results by specifying the token in a subsequent call.
    See also: AWS API Documentation
    
    
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
            The name of the log group.
            

    :type logStreamNames: list
    :param logStreamNames: Optional list of log stream names.
            (string) --
            

    :type startTime: integer
    :param startTime: The start of the time range, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. Events with a timestamp prior to this time are not returned.

    :type endTime: integer
    :param endTime: The end of the time range, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. Events with a timestamp later than this time are not returned.

    :type filterPattern: string
    :param filterPattern: The filter pattern to use. If not provided, all the events are matched.

    :type nextToken: string
    :param nextToken: The token for the next set of events to return. (You received this token from a previous call.)

    :type limit: integer
    :param limit: The maximum number of events to return. The default is 10,000 events.

    :type interleaved: boolean
    :param interleaved: If the value is true, the operation makes a best effort to provide responses that contain events from multiple log streams within the log group interleaved in a single response. If the value is false all the matched log events in the first log stream are searched first, then those in the next log stream, and so on. The default is false.

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
    Lists log events from the specified log stream. You can list all the log events or filter using a time range.
    By default, this operation returns as many log events as can fit in a response size of 1MB (up to 10,000 log events). If the results include tokens, there are more log events available. You can get additional log events by specifying one of the tokens in a subsequent call.
    See also: AWS API Documentation
    
    
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
            The name of the log group.
            

    :type logStreamName: string
    :param logStreamName: [REQUIRED]
            The name of the log stream.
            

    :type startTime: integer
    :param startTime: The start of the time range, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. Events with a timestamp earlier than this time are not included.

    :type endTime: integer
    :param endTime: The end of the time range, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC. Events with a timestamp later than this time are not included.

    :type nextToken: string
    :param nextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type limit: integer
    :param limit: The maximum number of log events returned. If you don't specify a value, the maximum is as many log events as can fit in a response size of 1MB, up to 10,000 log events.

    :type startFromHead: boolean
    :param startFromHead: If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. The default value is false.

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

def list_tags_log_group(logGroupName=None):
    """
    Lists the tags for the specified log group.
    To add tags, use  TagLogGroup . To remove tags, use  UntagLogGroup .
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_log_group(
        logGroupName='string'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :rtype: dict
    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def put_destination(destinationName=None, targetArn=None, roleArn=None):
    """
    Creates or updates a destination. A destination encapsulates a physical resource (such as a Kinesis stream) and enables you to subscribe to a real-time stream of log events of a different account, ingested using  PutLogEvents . Currently, the only supported physical resource is a Amazon Kinesis stream belonging to the same account as the destination.
    A destination controls what is written to its Amazon Kinesis stream through an access policy. By default, PutDestination does not set any access policy with the destination, which means a cross-account user cannot call  PutSubscriptionFilter against this destination. To enable this, the destination owner must call  PutDestinationPolicy after PutDestination .
    See also: AWS API Documentation
    
    
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
            The ARN of an IAM role that grants CloudWatch Logs permissions to call Amazon Kinesis PutRecord on the destination stream.
            

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
    Creates or updates an access policy associated with an existing destination. An access policy is an IAM policy document that is used to authorize claims to register a subscription filter against a given destination.
    See also: AWS API Documentation
    
    
    :example: response = client.put_destination_policy(
        destinationName='string',
        accessPolicy='string'
    )
    
    
    :type destinationName: string
    :param destinationName: [REQUIRED]
            A name for an existing destination.
            

    :type accessPolicy: string
    :param accessPolicy: [REQUIRED]
            An IAM policy document that authorizes cross-account users to deliver their log events to the associated destination.
            

    """
    pass

def put_log_events(logGroupName=None, logStreamName=None, logEvents=None, sequenceToken=None):
    """
    Uploads a batch of log events to the specified log stream.
    You must include the sequence token obtained from the response of the previous call. An upload in a newly created log stream does not require a sequence token. You can also get the sequence token using  DescribeLogStreams .
    The batch of events must satisfy the following constraints:
    See also: AWS API Documentation
    
    
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
            The name of the log group.
            

    :type logStreamName: string
    :param logStreamName: [REQUIRED]
            The name of the log stream.
            

    :type logEvents: list
    :param logEvents: [REQUIRED]
            The log events.
            (dict) --Represents a log event, which is a record of activity that was recorded by the application or resource being monitored.
            timestamp (integer) -- [REQUIRED]The time the event occurred, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
            message (string) -- [REQUIRED]The raw event message.
            
            

    :type sequenceToken: string
    :param sequenceToken: The sequence token.

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
    The name of the log group.
    
    logStreamName (string) -- [REQUIRED]
    The name of the log stream.
    
    logEvents (list) -- [REQUIRED]
    The log events.
    
    (dict) --Represents a log event, which is a record of activity that was recorded by the application or resource being monitored.
    
    timestamp (integer) -- [REQUIRED]The time the event occurred, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
    
    message (string) -- [REQUIRED]The raw event message.
    
    
    
    
    
    sequenceToken (string) -- The sequence token.
    
    """
    pass

def put_metric_filter(logGroupName=None, filterName=None, filterPattern=None, metricTransformations=None):
    """
    Creates or updates a metric filter and associates it with the specified log group. Metric filters allow you to configure rules to extract metric data from log events ingested through  PutLogEvents .
    The maximum number of metric filters that can be associated with a log group is 100.
    See also: AWS API Documentation
    
    
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
            The name of the log group.
            

    :type filterName: string
    :param filterName: [REQUIRED]
            A name for the metric filter.
            

    :type filterPattern: string
    :param filterPattern: [REQUIRED]
            A filter pattern for extracting metric data out of ingested log events.
            

    :type metricTransformations: list
    :param metricTransformations: [REQUIRED]
            A collection of information needed to define how metric data gets emitted.
            (dict) --Indicates how to transform ingested log events into metric data in a CloudWatch metric.
            metricName (string) -- [REQUIRED]The name of the CloudWatch metric.
            metricNamespace (string) -- [REQUIRED]The namespace of the CloudWatch metric.
            metricValue (string) -- [REQUIRED]The value to publish to the CloudWatch metric when a filter pattern matches a log event.
            defaultValue (float) --(Optional) The value to emit when a filter pattern does not match a log event. This value can be null.
            
            

    """
    pass

def put_retention_policy(logGroupName=None, retentionInDays=None):
    """
    Sets the retention of the specified log group. A retention policy allows you to configure the number of days you want to retain log events in the specified log group.
    See also: AWS API Documentation
    
    
    :example: response = client.put_retention_policy(
        logGroupName='string',
        retentionInDays=123
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type retentionInDays: integer
    :param retentionInDays: [REQUIRED]
            The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.
            

    """
    pass

def put_subscription_filter(logGroupName=None, filterName=None, filterPattern=None, destinationArn=None, roleArn=None, distribution=None):
    """
    Creates or updates a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events ingested through  PutLogEvents and have them delivered to a specific destination. Currently, the supported destinations are:
    There can only be one subscription filter associated with a log group. If you are updating an existing filter, you must specify the correct name in filterName . Otherwise, the call will fail because you cannot associate a second filter with a log group.
    See also: AWS API Documentation
    
    
    :example: response = client.put_subscription_filter(
        logGroupName='string',
        filterName='string',
        filterPattern='string',
        destinationArn='string',
        roleArn='string',
        distribution='Random'|'ByLogStream'
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type filterName: string
    :param filterName: [REQUIRED]
            A name for the subscription filter. If you are updating an existing filter, you must specify the correct name in filterName . Otherwise, the call will fail because you cannot associate a second filter with a log group. To find the name of the filter currently associated with a log group, use DescribeSubscriptionFilters .
            

    :type filterPattern: string
    :param filterPattern: [REQUIRED]
            A filter pattern for subscribing to a filtered stream of log events.
            

    :type destinationArn: string
    :param destinationArn: [REQUIRED]
            The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:
            An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.
            A logical destination (specified using an ARN) belonging to a different account, for cross-account delivery.
            An Amazon Kinesis Firehose stream belonging to the same account as the subscription filter, for same-account delivery.
            An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery.
            

    :type roleArn: string
    :param roleArn: The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.

    :type distribution: string
    :param distribution: The method used to distribute log data to the destination, when the destination is an Amazon Kinesis stream. By default, log data is grouped by log stream. For a more even distribution, you can group log data randomly.

    :returns: 
    logGroupName (string) -- [REQUIRED]
    The name of the log group.
    
    filterName (string) -- [REQUIRED]
    A name for the subscription filter. If you are updating an existing filter, you must specify the correct name in filterName . Otherwise, the call will fail because you cannot associate a second filter with a log group. To find the name of the filter currently associated with a log group, use  DescribeSubscriptionFilters .
    
    filterPattern (string) -- [REQUIRED]
    A filter pattern for subscribing to a filtered stream of log events.
    
    destinationArn (string) -- [REQUIRED]
    The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:
    
    An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.
    A logical destination (specified using an ARN) belonging to a different account, for cross-account delivery.
    An Amazon Kinesis Firehose stream belonging to the same account as the subscription filter, for same-account delivery.
    An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery.
    
    
    roleArn (string) -- The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
    distribution (string) -- The method used to distribute log data to the destination, when the destination is an Amazon Kinesis stream. By default, log data is grouped by log stream. For a more even distribution, you can group log data randomly.
    
    """
    pass

def tag_log_group(logGroupName=None, tags=None):
    """
    Adds or updates the specified tags for the specified log group.
    To list the tags for a log group, use  ListTagsLogGroup . To remove tags, use  UntagLogGroup .
    For more information about tags, see Tag Log Groups in Amazon CloudWatch Logs in the Amazon CloudWatch Logs User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.tag_log_group(
        logGroupName='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type tags: dict
    :param tags: [REQUIRED]
            The key-value pairs to use for the tags.
            (string) --
            (string) --
            

    """
    pass

def test_metric_filter(filterPattern=None, logEventMessages=None):
    """
    Tests the filter pattern of a metric filter against a sample of log event messages. You can use this operation to validate the correctness of a metric filter pattern.
    See also: AWS API Documentation
    
    
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
            The log event messages to test.
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
    (string) --
    (string) --
    
    
    
    """
    pass

def untag_log_group(logGroupName=None, tags=None):
    """
    Removes the specified tags from the specified log group.
    To list the tags for a log group, use  ListTagsLogGroup . To add tags, use  UntagLogGroup .
    See also: AWS API Documentation
    
    
    :example: response = client.untag_log_group(
        logGroupName='string',
        tags=[
            'string',
        ]
    )
    
    
    :type logGroupName: string
    :param logGroupName: [REQUIRED]
            The name of the log group.
            

    :type tags: list
    :param tags: [REQUIRED]
            The tag keys. The corresponding tags are removed from the log group.
            (string) --
            

    """
    pass

