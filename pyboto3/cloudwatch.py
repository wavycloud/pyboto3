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

def delete_alarms(AlarmNames=None):
    """
    Deletes the specified alarms. In the event of an error, no alarms are deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_alarms(
        AlarmNames=[
            'string',
        ]
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: [REQUIRED]
            The alarms to be deleted.
            (string) --
            

    """
    pass

def describe_alarm_history(AlarmName=None, HistoryItemType=None, StartDate=None, EndDate=None, MaxRecords=None, NextToken=None):
    """
    Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for all alarms are returned.
    Note that Amazon CloudWatch retains the history of an alarm even if you delete the alarm.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_alarm_history(
        AlarmName='string',
        HistoryItemType='ConfigurationUpdate'|'StateUpdate'|'Action',
        StartDate=datetime(2015, 1, 1),
        EndDate=datetime(2015, 1, 1),
        MaxRecords=123,
        NextToken='string'
    )
    
    
    :type AlarmName: string
    :param AlarmName: The name of the alarm.

    :type HistoryItemType: string
    :param HistoryItemType: The type of alarm histories to retrieve.

    :type StartDate: datetime
    :param StartDate: The starting date to retrieve alarm history.

    :type EndDate: datetime
    :param EndDate: The ending date to retrieve alarm history.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of alarm history records to retrieve.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :rtype: dict
    :return: {
        'AlarmHistoryItems': [
            {
                'AlarmName': 'string',
                'Timestamp': datetime(2015, 1, 1),
                'HistoryItemType': 'ConfigurationUpdate'|'StateUpdate'|'Action',
                'HistorySummary': 'string',
                'HistoryData': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_alarms(AlarmNames=None, AlarmNamePrefix=None, StateValue=None, ActionPrefix=None, MaxRecords=None, NextToken=None):
    """
    Retrieves the specified alarms. If no alarms are specified, all alarms are returned. Alarms can be retrieved by using only a prefix for the alarm name, the alarm state, or a prefix for any action.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_alarms(
        AlarmNames=[
            'string',
        ],
        AlarmNamePrefix='string',
        StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
        ActionPrefix='string',
        MaxRecords=123,
        NextToken='string'
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: The names of the alarms.
            (string) --
            

    :type AlarmNamePrefix: string
    :param AlarmNamePrefix: The alarm name prefix. You cannot specify AlarmNames if this parameter is specified.

    :type StateValue: string
    :param StateValue: The state value to be used in matching alarms.

    :type ActionPrefix: string
    :param ActionPrefix: The action name prefix.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of alarm descriptions to retrieve.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :rtype: dict
    :return: {
        'MetricAlarms': [
            {
                'AlarmName': 'string',
                'AlarmArn': 'string',
                'AlarmDescription': 'string',
                'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
                'ActionsEnabled': True|False,
                'OKActions': [
                    'string',
                ],
                'AlarmActions': [
                    'string',
                ],
                'InsufficientDataActions': [
                    'string',
                ],
                'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
                'StateReason': 'string',
                'StateReasonData': 'string',
                'StateUpdatedTimestamp': datetime(2015, 1, 1),
                'MetricName': 'string',
                'Namespace': 'string',
                'Statistic': 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
                'ExtendedStatistic': 'string',
                'Dimensions': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'Period': 123,
                'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                'EvaluationPeriods': 123,
                'Threshold': 123.0,
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                'TreatMissingData': 'string',
                'EvaluateLowSampleCountPercentile': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_alarms_for_metric(MetricName=None, Namespace=None, Statistic=None, ExtendedStatistic=None, Dimensions=None, Period=None, Unit=None):
    """
    Retrieves the alarms for the specified metric. Specify a statistic, period, or unit to filter the results.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_alarms_for_metric(
        MetricName='string',
        Namespace='string',
        Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
        ExtendedStatistic='string',
        Dimensions=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        Period=123,
        Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
    )
    
    
    :type MetricName: string
    :param MetricName: [REQUIRED]
            The name of the metric.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace of the metric.
            

    :type Statistic: string
    :param Statistic: The statistic for the metric, other than percentiles. For percentile statistics, use ExtendedStatistics .

    :type ExtendedStatistic: string
    :param ExtendedStatistic: The percentile statistic for the metric. Specify a value between p0.0 and p100.

    :type Dimensions: list
    :param Dimensions: The dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the call to succeed.
            (dict) --Expands the identity of a metric.
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement.
            
            

    :type Period: integer
    :param Period: The period, in seconds, over which the statistic is applied.

    :type Unit: string
    :param Unit: The unit for the metric.

    :rtype: dict
    :return: {
        'MetricAlarms': [
            {
                'AlarmName': 'string',
                'AlarmArn': 'string',
                'AlarmDescription': 'string',
                'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
                'ActionsEnabled': True|False,
                'OKActions': [
                    'string',
                ],
                'AlarmActions': [
                    'string',
                ],
                'InsufficientDataActions': [
                    'string',
                ],
                'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
                'StateReason': 'string',
                'StateReasonData': 'string',
                'StateUpdatedTimestamp': datetime(2015, 1, 1),
                'MetricName': 'string',
                'Namespace': 'string',
                'Statistic': 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
                'ExtendedStatistic': 'string',
                'Dimensions': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'Period': 123,
                'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                'EvaluationPeriods': 123,
                'Threshold': 123.0,
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                'TreatMissingData': 'string',
                'EvaluateLowSampleCountPercentile': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def disable_alarm_actions(AlarmNames=None):
    """
    Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions do not execute when the alarm state changes.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_alarm_actions(
        AlarmNames=[
            'string',
        ]
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: [REQUIRED]
            The names of the alarms.
            (string) --
            

    """
    pass

def enable_alarm_actions(AlarmNames=None):
    """
    Enables the actions for the specified alarms.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_alarm_actions(
        AlarmNames=[
            'string',
        ]
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: [REQUIRED]
            The names of the alarms.
            (string) --
            

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

def get_metric_statistics(Namespace=None, MetricName=None, Dimensions=None, StartTime=None, EndTime=None, Period=None, Statistics=None, ExtendedStatistics=None, Unit=None):
    """
    Gets statistics for the specified metric.
    Amazon CloudWatch retains metric data as follows:
    Note that CloudWatch started retaining 5-minute and 1-hour metric data as of 9 July 2016.
    The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, Amazon CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. A period can be as short as one minute (60 seconds). Note that data points are not returned in chronological order.
    Amazon CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, Amazon CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned.
    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you cannot retrieve percentile statistics for this data unless one of the following conditions is true:
    For a list of metrics and dimensions supported by AWS services, see the Amazon CloudWatch Metrics and Dimensions Reference in the Amazon CloudWatch User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_metric_statistics(
        Namespace='string',
        MetricName='string',
        Dimensions=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Period=123,
        Statistics=[
            'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
        ],
        ExtendedStatistics=[
            'string',
        ],
        Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
    )
    
    
    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace of the metric, with or without spaces.
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            The name of the metric, with or without spaces.
            

    :type Dimensions: list
    :param Dimensions: The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. You can't retrieve statistics using combinations of dimensions that were not specially published. You must specify the same dimensions that were used when the metrics were created. For an example, see Dimension Combinations in the Amazon CloudWatch User Guide . For more information on specifying dimensions, see Publishing Metrics in the Amazon CloudWatch User Guide .
            (dict) --Expands the identity of a metric.
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement.
            
            

    :type StartTime: datetime
    :param StartTime: [REQUIRED]
            The time stamp that determines the first data point to return. Note that start times are evaluated relative to the time that CloudWatch receives the request.
            The value specified is inclusive; results include data points with the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).
            CloudWatch rounds the specified time stamp as follows:
            Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.
            Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.
            Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.
            

    :type EndTime: datetime
    :param EndTime: [REQUIRED]
            The time stamp that determines the last data point to return.
            The value specified is exclusive; results will include data points up to the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).
            

    :type Period: integer
    :param Period: [REQUIRED]
            The granularity, in seconds, of the returned data points. A period can be as short as one minute (60 seconds) and must be a multiple of 60. The default value is 60.
            If the StartTime parameter specifies a time stamp that is greater than 15 days ago, you must specify the period as follows or no data points in that time range is returned:
            Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
            Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
            

    :type Statistics: list
    :param Statistics: The metric statistics, other than percentile. For percentile statistics, use ExtendedStatistic .
            (string) --
            

    :type ExtendedStatistics: list
    :param ExtendedStatistics: The percentile statistics. Specify values between p0.0 and p100.
            (string) --
            

    :type Unit: string
    :param Unit: The unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If the metric only ever reports one unit, specifying a unit has no effect.

    :rtype: dict
    :return: {
        'Label': 'string',
        'Datapoints': [
            {
                'Timestamp': datetime(2015, 1, 1),
                'SampleCount': 123.0,
                'Average': 123.0,
                'Sum': 123.0,
                'Minimum': 123.0,
                'Maximum': 123.0,
                'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                'ExtendedStatistics': {
                    'string': 123.0
                }
            },
        ]
    }
    
    
    :returns: 
    The SampleCount of the statistic set is 1
    The Min and the Max of the statistic set are equal
    
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

def list_metrics(Namespace=None, MetricName=None, Dimensions=None, NextToken=None):
    """
    List the specified metrics. You can use the returned metrics with  GetMetricStatistics to obtain statistical data.
    Up to 500 results are returned for any one call. To retrieve additional results, use the returned token with subsequent calls.
    After you create a metric, allow up to fifteen minutes before the metric appears. Statistics about the metric, however, are available sooner using  GetMetricStatistics .
    See also: AWS API Documentation
    
    
    :example: response = client.list_metrics(
        Namespace='string',
        MetricName='string',
        Dimensions=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        NextToken='string'
    )
    
    
    :type Namespace: string
    :param Namespace: The namespace to filter against.

    :type MetricName: string
    :param MetricName: The name of the metric to filter against.

    :type Dimensions: list
    :param Dimensions: The dimensions to filter against.
            (dict) --Represents filters for a dimension.
            Name (string) -- [REQUIRED]The dimension name to be matched.
            Value (string) --The value of the dimension to be matched.
            
            

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :rtype: dict
    :return: {
        'Metrics': [
            {
                'Namespace': 'string',
                'MetricName': 'string',
                'Dimensions': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def put_metric_alarm(AlarmName=None, AlarmDescription=None, ActionsEnabled=None, OKActions=None, AlarmActions=None, InsufficientDataActions=None, MetricName=None, Namespace=None, Statistic=None, ExtendedStatistic=None, Dimensions=None, Period=None, Unit=None, EvaluationPeriods=None, Threshold=None, ComparisonOperator=None, TreatMissingData=None, EvaluateLowSampleCountPercentile=None):
    """
    Creates or updates an alarm and associates it with the specified metric. Optionally, this operation can associate one or more Amazon SNS resources with the alarm.
    When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA . The alarm is evaluated and its state is set appropriately. Any actions associated with the state are then executed.
    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.
    If you are an AWS Identity and Access Management (IAM) user, you must have Amazon EC2 permissions for some operations:
    If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can still create an alarm, but the stop or terminate actions won't be performed. However, if you are later granted the required permissions, the alarm actions that you created earlier will be performed.
    If you are using an IAM role (for example, an Amazon EC2 instance profile), you cannot stop or terminate the instance using alarm actions. However, you can still see the alarm state and perform any other actions such as Amazon SNS notifications or Auto Scaling policies.
    If you are using temporary security credentials granted using the AWS Security Token Service (AWS STS), you cannot stop or terminate an Amazon EC2 instance using alarm actions.
    Note that you must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role. After this IAM role is created, you can create stop, terminate, or reboot alarms using a command-line interface or an API.
    See also: AWS API Documentation
    
    
    :example: response = client.put_metric_alarm(
        AlarmName='string',
        AlarmDescription='string',
        ActionsEnabled=True|False,
        OKActions=[
            'string',
        ],
        AlarmActions=[
            'string',
        ],
        InsufficientDataActions=[
            'string',
        ],
        MetricName='string',
        Namespace='string',
        Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
        ExtendedStatistic='string',
        Dimensions=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        Period=123,
        Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
        EvaluationPeriods=123,
        Threshold=123.0,
        ComparisonOperator='GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
        TreatMissingData='string',
        EvaluateLowSampleCountPercentile='string'
    )
    
    
    :type AlarmName: string
    :param AlarmName: [REQUIRED]
            The name for the alarm. This name must be unique within the AWS account.
            

    :type AlarmDescription: string
    :param AlarmDescription: The description for the alarm.

    :type ActionsEnabled: boolean
    :param ActionsEnabled: Indicates whether actions should be executed during any changes to the alarm state.

    :type OKActions: list
    :param OKActions: The actions to execute when this alarm transitions to an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover
            Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            (string) --
            

    :type AlarmActions: list
    :param AlarmActions: The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover
            Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            (string) --
            

    :type InsufficientDataActions: list
    :param InsufficientDataActions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover
            Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            (string) --
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            The name for the metric associated with the alarm.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace for the metric associated with the alarm.
            

    :type Statistic: string
    :param Statistic: The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ExtendedStatistic .

    :type ExtendedStatistic: string
    :param ExtendedStatistic: The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

    :type Dimensions: list
    :param Dimensions: The dimensions for the metric associated with the alarm.
            (dict) --Expands the identity of a metric.
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement.
            
            

    :type Period: integer
    :param Period: [REQUIRED]
            The period, in seconds, over which the specified statistic is applied.
            

    :type Unit: string
    :param Unit: The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.
            If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, the Amazon CloudWatch alarm can get stuck in the INSUFFICIENT DATA state.
            

    :type EvaluationPeriods: integer
    :param EvaluationPeriods: [REQUIRED]
            The number of periods over which data is compared to the specified threshold.
            

    :type Threshold: float
    :param Threshold: [REQUIRED]
            The value against which the specified statistic is compared.
            

    :type ComparisonOperator: string
    :param ComparisonOperator: [REQUIRED]
            The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
            

    :type TreatMissingData: string
    :param TreatMissingData: Sets how this alarm is to handle missing data points. If TreatMissingData is omitted, the default behavior of missing is used. For more information, see Configuring How CloudWatch Alarms Treats Missing Data .
            Valid Values: breaching | notBreaching | ignore | missing
            

    :type EvaluateLowSampleCountPercentile: string
    :param EvaluateLowSampleCountPercentile: Used only for alarms based on percentiles. If you specify ignore , the alarm state will not change during periods with too few data points to be statistically significant. If you specify evaluate or omit this parameter, the alarm will always be evaluated and possibly change state no matter how many data points are available. For more information, see Percentile-Based CloudWatch Alarms and Low Data Samples .
            Valid Values: evaluate | ignore
            

    :returns: 
    AlarmName (string) -- [REQUIRED]
    The name for the alarm. This name must be unique within the AWS account.
    
    AlarmDescription (string) -- The description for the alarm.
    ActionsEnabled (boolean) -- Indicates whether actions should be executed during any changes to the alarm state.
    OKActions (list) -- The actions to execute when this alarm transitions to an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover
    Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    (string) --
    
    
    AlarmActions (list) -- The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover
    Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    (string) --
    
    
    InsufficientDataActions (list) -- The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover
    Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    (string) --
    
    
    MetricName (string) -- [REQUIRED]
    The name for the metric associated with the alarm.
    
    Namespace (string) -- [REQUIRED]
    The namespace for the metric associated with the alarm.
    
    Statistic (string) -- The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ExtendedStatistic .
    ExtendedStatistic (string) -- The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
    Dimensions (list) -- The dimensions for the metric associated with the alarm.
    
    (dict) --Expands the identity of a metric.
    
    Name (string) -- [REQUIRED]The name of the dimension.
    
    Value (string) -- [REQUIRED]The value representing the dimension measurement.
    
    
    
    
    
    Period (integer) -- [REQUIRED]
    The period, in seconds, over which the specified statistic is applied.
    
    Unit (string) -- The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.
    If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, the Amazon CloudWatch alarm can get stuck in the INSUFFICIENT DATA state.
    
    EvaluationPeriods (integer) -- [REQUIRED]
    The number of periods over which data is compared to the specified threshold.
    
    Threshold (float) -- [REQUIRED]
    The value against which the specified statistic is compared.
    
    ComparisonOperator (string) -- [REQUIRED]
    The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
    
    TreatMissingData (string) -- Sets how this alarm is to handle missing data points. If TreatMissingData is omitted, the default behavior of missing is used. For more information, see Configuring How CloudWatch Alarms Treats Missing Data .
    Valid Values: breaching | notBreaching | ignore | missing
    
    EvaluateLowSampleCountPercentile (string) -- Used only for alarms based on percentiles. If you specify ignore , the alarm state will not change during periods with too few data points to be statistically significant. If you specify evaluate or omit this parameter, the alarm will always be evaluated and possibly change state no matter how many data points are available. For more information, see Percentile-Based CloudWatch Alarms and Low Data Samples .
    Valid Values: evaluate | ignore
    
    
    """
    pass

def put_metric_data(Namespace=None, MetricData=None):
    """
    Publishes metric data points to Amazon CloudWatch. Amazon CloudWatch associates the data points with the specified metric. If the specified metric does not exist, Amazon CloudWatch creates the metric. When Amazon CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to  ListMetrics .
    Each PutMetricData request is limited to 40 KB in size for HTTP POST requests.
    Although the Value parameter accepts numbers of type Double , Amazon CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (e.g., NaN, +Infinity, -Infinity) are not supported.
    You can use up to 10 dimensions per metric to further clarify what data the metric collects. For more information on specifying dimensions, see Publishing Metrics in the Amazon CloudWatch User Guide .
    Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for  GetMetricStatistics from the time they are submitted.
    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you cannot retrieve percentile statistics for this data unless one of the following conditions is true:
    See also: AWS API Documentation
    
    
    :example: response = client.put_metric_data(
        Namespace='string',
        MetricData=[
            {
                'MetricName': 'string',
                'Dimensions': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'Timestamp': datetime(2015, 1, 1),
                'Value': 123.0,
                'StatisticValues': {
                    'SampleCount': 123.0,
                    'Sum': 123.0,
                    'Minimum': 123.0,
                    'Maximum': 123.0
                },
                'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
            },
        ]
    )
    
    
    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace for the metric data.
            You cannot specify a namespace that begins with 'AWS/'. Namespaces that begin with 'AWS/' are reserved for use by Amazon Web Services products.
            

    :type MetricData: list
    :param MetricData: [REQUIRED]
            The data for the metric.
            (dict) --Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.
            MetricName (string) -- [REQUIRED]The name of the metric.
            Dimensions (list) --The dimensions associated with the metric.
            (dict) --Expands the identity of a metric.
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement.
            
            Timestamp (datetime) --The time the metric data was received, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
            Value (float) --The value for the metric.
            Although the parameter accepts numbers of type Double, Amazon CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.
            StatisticValues (dict) --The statistical values for the metric.
            SampleCount (float) -- [REQUIRED]The number of samples used for the statistic set.
            Sum (float) -- [REQUIRED]The sum of values for the sample set.
            Minimum (float) -- [REQUIRED]The minimum value of the sample set.
            Maximum (float) -- [REQUIRED]The maximum value of the sample set.
            Unit (string) --The unit of the metric.
            
            

    :returns: 
    Namespace (string) -- [REQUIRED]
    The namespace for the metric data.
    You cannot specify a namespace that begins with "AWS/". Namespaces that begin with "AWS/" are reserved for use by Amazon Web Services products.
    
    MetricData (list) -- [REQUIRED]
    The data for the metric.
    
    (dict) --Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.
    
    MetricName (string) -- [REQUIRED]The name of the metric.
    
    Dimensions (list) --The dimensions associated with the metric.
    
    (dict) --Expands the identity of a metric.
    
    Name (string) -- [REQUIRED]The name of the dimension.
    
    Value (string) -- [REQUIRED]The value representing the dimension measurement.
    
    
    
    
    
    Timestamp (datetime) --The time the metric data was received, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
    
    Value (float) --The value for the metric.
    Although the parameter accepts numbers of type Double, Amazon CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.
    
    StatisticValues (dict) --The statistical values for the metric.
    
    SampleCount (float) -- [REQUIRED]The number of samples used for the statistic set.
    
    Sum (float) -- [REQUIRED]The sum of values for the sample set.
    
    Minimum (float) -- [REQUIRED]The minimum value of the sample set.
    
    Maximum (float) -- [REQUIRED]The maximum value of the sample set.
    
    
    
    Unit (string) --The unit of the metric.
    
    
    
    
    
    
    """
    pass

def set_alarm_state(AlarmName=None, StateValue=None, StateReason=None, StateReasonData=None):
    """
    Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to ALARM sends an Amazon SNS message. The alarm returns to its actual state (often within seconds). Because the alarm state change happens very quickly, it is typically only visible in the alarm's History tab in the Amazon CloudWatch console or through  DescribeAlarmHistory .
    See also: AWS API Documentation
    
    
    :example: response = client.set_alarm_state(
        AlarmName='string',
        StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
        StateReason='string',
        StateReasonData='string'
    )
    
    
    :type AlarmName: string
    :param AlarmName: [REQUIRED]
            The name for the alarm. This name must be unique within the AWS account. The maximum length is 255 characters.
            

    :type StateValue: string
    :param StateValue: [REQUIRED]
            The value of the state.
            

    :type StateReason: string
    :param StateReason: [REQUIRED]
            The reason that this alarm is set to this specific state, in text format.
            

    :type StateReasonData: string
    :param StateReasonData: The reason that this alarm is set to this specific state, in JSON format.

    """
    pass

