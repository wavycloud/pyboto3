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

def delete_alarms(AlarmNames=None):
    """
    Deletes all specified alarms. In the event of an error, no alarms are deleted.
    
    
    :example: response = client.delete_alarms(
        AlarmNames=[
            'string',
        ]
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: [REQUIRED]
            A list of alarms to be deleted.
            (string) --
            

    """
    pass

def describe_alarm_history(AlarmName=None, HistoryItemType=None, StartDate=None, EndDate=None, MaxRecords=None, NextToken=None):
    """
    Retrieves history for the specified alarm. Filter alarms by date range or item type. If an alarm name is not specified, Amazon CloudWatch returns histories for all of the owner's alarms.
    
    
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
    Retrieves alarms with the specified names. If no name is specified, all alarms for the user are returned. Alarms can be retrieved by using only a prefix for the alarm name, the alarm state, or a prefix for any action.
    
    
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
    :param AlarmNames: A list of alarm names to retrieve information for.
            (string) --
            

    :type AlarmNamePrefix: string
    :param AlarmNamePrefix: The alarm name prefix. AlarmNames cannot be specified if this parameter is specified.

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
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_alarms_for_metric(MetricName=None, Namespace=None, Statistic=None, Dimensions=None, Period=None, Unit=None):
    """
    Retrieves all alarms for a single metric. Specify a statistic, period, or unit to filter the set of alarms further.
    
    
    :example: response = client.describe_alarms_for_metric(
        MetricName='string',
        Namespace='string',
        Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
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
    :param Statistic: The statistic for the metric.

    :type Dimensions: list
    :param Dimensions: The list of dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the DescribeAlarmsForMetric to succeed.
            (dict) --The Dimension data type further expands on the identity of a metric using a Name, Value pair.
            For examples that use one or more dimensions, see PutMetricData .
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement
            
            

    :type Period: integer
    :param Period: The period in seconds over which the statistic is applied.

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
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def disable_alarm_actions(AlarmNames=None):
    """
    Disables actions for the specified alarms. When an alarm's actions are disabled the alarm's state may change, but none of the alarm's actions will execute.
    
    
    :example: response = client.disable_alarm_actions(
        AlarmNames=[
            'string',
        ]
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: [REQUIRED]
            The names of the alarms to disable actions for.
            (string) --
            

    """
    pass

def enable_alarm_actions(AlarmNames=None):
    """
    Enables actions for the specified alarms.
    
    
    :example: response = client.enable_alarm_actions(
        AlarmNames=[
            'string',
        ]
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: [REQUIRED]
            The names of the alarms to enable actions for.
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

def get_metric_statistics(Namespace=None, MetricName=None, Dimensions=None, StartTime=None, EndTime=None, Period=None, Statistics=None, Unit=None):
    """
    Gets statistics for the specified metric.
    The maximum number of data points that can be queried is 50,850, whereas the maximum number of data points returned from a single GetMetricStatistics request is 1,440. If you make a request that generates more than 1,440 data points, Amazon CloudWatch returns an error. In such a case, you can alter the request by narrowing the specified time range or increasing the specified period. A period can be as short as one minute (60 seconds) or as long as one day (86,400 seconds). Alternatively, you can make multiple requests across adjacent time ranges. GetMetricStatistics does not return the data in chronological order.
    Amazon CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-minute granularity, Amazon CloudWatch aggregates data points with time stamps that fall within the same one-minute period. In such a case, the data points queried can greatly outnumber the data points returned.
    The following examples show various statistics allowed by the data point query maximum of 50,850 when you call GetMetricStatistics on Amazon EC2 instances with detailed (one-minute) monitoring enabled:
    For information about the namespace, metric names, and dimensions that other Amazon Web Services products use to send metrics to CloudWatch, go to Amazon CloudWatch Metrics, Namespaces, and Dimensions Reference in the Amazon CloudWatch Developer Guide .
    
    
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
        Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
    )
    
    
    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace of the metric, with or without spaces.
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            The name of the metric, with or without spaces.
            

    :type Dimensions: list
    :param Dimensions: A list of dimensions describing qualities of the metric.
            (dict) --The Dimension data type further expands on the identity of a metric using a Name, Value pair.
            For examples that use one or more dimensions, see PutMetricData .
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement
            
            

    :type StartTime: datetime
    :param StartTime: [REQUIRED]
            The time stamp to use for determining the first datapoint to return. The value specified is inclusive; results include datapoints with the time stamp specified. The time stamp must be in ISO 8601 UTC format (e.g., 2014-09-03T23:00:00Z).
            Note
            The specified start time is rounded down to the nearest value. Datapoints are returned for start times up to two weeks in the past. Specified start times that are more than two weeks in the past will not return datapoints for metrics that are older than two weeks.
            Data that is timestamped 24 hours or more in the past may take in excess of 48 hours to become available from submission time using GetMetricStatistics .
            

    :type EndTime: datetime
    :param EndTime: [REQUIRED]
            The time stamp to use for determining the last datapoint to return. The value specified is exclusive; results will include datapoints up to the time stamp specified. The time stamp must be in ISO 8601 UTC format (e.g., 2014-09-03T23:00:00Z).
            

    :type Period: integer
    :param Period: [REQUIRED]
            The granularity, in seconds, of the returned datapoints. A Period can be as short as one minute (60 seconds) or as long as one day (86,400 seconds), and must be a multiple of 60. The default value is 60.
            

    :type Statistics: list
    :param Statistics: [REQUIRED]
            The metric statistics to return. For information about specific statistics returned by GetMetricStatistics, see Statistics in the Amazon CloudWatch Developer Guide .
            (string) --
            

    :type Unit: string
    :param Unit: The specific unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If the metric only ever reports one unit, specifying a unit will have no effect.

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
                'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
            },
        ]
    }
    
    
    :returns: 
    Namespace (string) -- [REQUIRED]
    The namespace of the metric, with or without spaces.
    
    MetricName (string) -- [REQUIRED]
    The name of the metric, with or without spaces.
    
    Dimensions (list) -- A list of dimensions describing qualities of the metric.
    
    (dict) --The Dimension data type further expands on the identity of a metric using a Name, Value pair.
    For examples that use one or more dimensions, see  PutMetricData .
    
    Name (string) -- [REQUIRED]The name of the dimension.
    
    Value (string) -- [REQUIRED]The value representing the dimension measurement
    
    
    
    
    
    StartTime (datetime) -- [REQUIRED]
    The time stamp to use for determining the first datapoint to return. The value specified is inclusive; results include datapoints with the time stamp specified. The time stamp must be in ISO 8601 UTC format (e.g., 2014-09-03T23:00:00Z).
    
    Note
    The specified start time is rounded down to the nearest value. Datapoints are returned for start times up to two weeks in the past. Specified start times that are more than two weeks in the past will not return datapoints for metrics that are older than two weeks.
    Data that is timestamped 24 hours or more in the past may take in excess of 48 hours to become available from submission time using GetMetricStatistics .
    
    
    EndTime (datetime) -- [REQUIRED]
    The time stamp to use for determining the last datapoint to return. The value specified is exclusive; results will include datapoints up to the time stamp specified. The time stamp must be in ISO 8601 UTC format (e.g., 2014-09-03T23:00:00Z).
    
    Period (integer) -- [REQUIRED]
    The granularity, in seconds, of the returned datapoints. A Period can be as short as one minute (60 seconds) or as long as one day (86,400 seconds), and must be a multiple of 60. The default value is 60.
    
    Statistics (list) -- [REQUIRED]
    The metric statistics to return. For information about specific statistics returned by GetMetricStatistics, see Statistics in the Amazon CloudWatch Developer Guide .
    
    (string) --
    
    
    Unit (string) -- The specific unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If the metric only ever reports one unit, specifying a unit will have no effect.
    
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
    Returns a list of valid metrics stored for the AWS account owner. Returned metrics can be used with  GetMetricStatistics to obtain statistical data for a given metric.
    
    
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
    :param Dimensions: A list of dimensions to filter against.
            (dict) --The DimensionFilter data type is used to filter ListMetrics results.
            Name (string) -- [REQUIRED]The dimension name to be matched.
            Value (string) --The value of the dimension to be matched.
            Note
            Specifying a Name without specifying a Value returns all values associated with that Name .
            
            

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

def put_metric_alarm(AlarmName=None, AlarmDescription=None, ActionsEnabled=None, OKActions=None, AlarmActions=None, InsufficientDataActions=None, MetricName=None, Namespace=None, Statistic=None, Dimensions=None, Period=None, Unit=None, EvaluationPeriods=None, Threshold=None, ComparisonOperator=None):
    """
    Creates or updates an alarm and associates it with the specified Amazon CloudWatch metric. Optionally, this operation can associate one or more Amazon SNS resources with the alarm.
    When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA . The alarm is evaluated and its StateValue is set appropriately. Any actions associated with the StateValue are then executed.
    
    
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
        ComparisonOperator='GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'
    )
    
    
    :type AlarmName: string
    :param AlarmName: [REQUIRED]
            The descriptive name for the alarm. This name must be unique within the user's AWS account
            

    :type AlarmDescription: string
    :param AlarmDescription: The description for the alarm.

    :type ActionsEnabled: boolean
    :param ActionsEnabled: Indicates whether or not actions should be executed during any changes to the alarm's state.

    :type OKActions: list
    :param OKActions: The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region (e.g., us-east-1) :ec2:stop | arn:aws:automate:region (e.g., us-east-1) :ec2:terminate | arn:aws:automate:region (e.g., us-east-1) :ec2:recover
            Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            Note: You must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role for the first time. After this IAM role is created, you can create stop, terminate, or reboot alarms using the CLI.
            (string) --
            

    :type AlarmActions: list
    :param AlarmActions: The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region (e.g., us-east-1) :ec2:stop | arn:aws:automate:region (e.g., us-east-1) :ec2:terminate | arn:aws:automate:region (e.g., us-east-1) :ec2:recover
            Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            Note: You must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role for the first time. After this IAM role is created, you can create stop, terminate, or reboot alarms using the CLI.
            (string) --
            

    :type InsufficientDataActions: list
    :param InsufficientDataActions: The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region (e.g., us-east-1) :ec2:stop | arn:aws:automate:region (e.g., us-east-1) :ec2:terminate | arn:aws:automate:region (e.g., us-east-1) :ec2:recover
            Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            Note: You must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role for the first time. After this IAM role is created, you can create stop, terminate, or reboot alarms using the CLI.
            (string) --
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            The name for the alarm's associated metric.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace for the alarm's associated metric.
            

    :type Statistic: string
    :param Statistic: [REQUIRED]
            The statistic to apply to the alarm's associated metric.
            

    :type Dimensions: list
    :param Dimensions: The dimensions for the alarm's associated metric.
            (dict) --The Dimension data type further expands on the identity of a metric using a Name, Value pair.
            For examples that use one or more dimensions, see PutMetricData .
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement
            
            

    :type Period: integer
    :param Period: [REQUIRED]
            The period in seconds over which the specified statistic is applied.
            

    :type Unit: string
    :param Unit: The statistic's unit of measure. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.
            Note: If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, this can cause an Amazon CloudWatch alarm to get stuck in the INSUFFICIENT DATA state.
            

    :type EvaluationPeriods: integer
    :param EvaluationPeriods: [REQUIRED]
            The number of periods over which data is compared to the specified threshold.
            

    :type Threshold: float
    :param Threshold: [REQUIRED]
            The value against which the specified statistic is compared.
            

    :type ComparisonOperator: string
    :param ComparisonOperator: [REQUIRED]
            The arithmetic operation to use when comparing the specified Statistic and Threshold . The specified Statistic value is used as the first operand.
            

    :returns: 
    AlarmName (string) -- [REQUIRED]
    The descriptive name for the alarm. This name must be unique within the user's AWS account
    
    AlarmDescription (string) -- The description for the alarm.
    ActionsEnabled (boolean) -- Indicates whether or not actions should be executed during any changes to the alarm's state.
    OKActions (list) -- The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:region (e.g., us-east-1) :ec2:stop | arn:aws:automate:region (e.g., us-east-1) :ec2:terminate | arn:aws:automate:region (e.g., us-east-1) :ec2:recover
    Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    Note: You must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role for the first time. After this IAM role is created, you can create stop, terminate, or reboot alarms using the CLI.
    
    (string) --
    
    
    AlarmActions (list) -- The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:region (e.g., us-east-1) :ec2:stop | arn:aws:automate:region (e.g., us-east-1) :ec2:terminate | arn:aws:automate:region (e.g., us-east-1) :ec2:recover
    Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    Note: You must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role for the first time. After this IAM role is created, you can create stop, terminate, or reboot alarms using the CLI.
    
    (string) --
    
    
    InsufficientDataActions (list) -- The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:region (e.g., us-east-1) :ec2:stop | arn:aws:automate:region (e.g., us-east-1) :ec2:terminate | arn:aws:automate:region (e.g., us-east-1) :ec2:recover
    Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    Note: You must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role for the first time. After this IAM role is created, you can create stop, terminate, or reboot alarms using the CLI.
    
    (string) --
    
    
    MetricName (string) -- [REQUIRED]
    The name for the alarm's associated metric.
    
    Namespace (string) -- [REQUIRED]
    The namespace for the alarm's associated metric.
    
    Statistic (string) -- [REQUIRED]
    The statistic to apply to the alarm's associated metric.
    
    Dimensions (list) -- The dimensions for the alarm's associated metric.
    
    (dict) --The Dimension data type further expands on the identity of a metric using a Name, Value pair.
    For examples that use one or more dimensions, see  PutMetricData .
    
    Name (string) -- [REQUIRED]The name of the dimension.
    
    Value (string) -- [REQUIRED]The value representing the dimension measurement
    
    
    
    
    
    Period (integer) -- [REQUIRED]
    The period in seconds over which the specified statistic is applied.
    
    Unit (string) -- The statistic's unit of measure. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.
    
    Note: If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, this can cause an Amazon CloudWatch alarm to get stuck in the INSUFFICIENT DATA state.
    
    EvaluationPeriods (integer) -- [REQUIRED]
    The number of periods over which data is compared to the specified threshold.
    
    Threshold (float) -- [REQUIRED]
    The value against which the specified statistic is compared.
    
    ComparisonOperator (string) -- [REQUIRED]
    The arithmetic operation to use when comparing the specified Statistic and Threshold . The specified Statistic value is used as the first operand.
    
    
    """
    pass

def put_metric_data(Namespace=None, MetricData=None):
    """
    Publishes metric data points to Amazon CloudWatch. Amazon CloudWatch associates the data points with the specified metric. If the specified metric does not exist, Amazon CloudWatch creates the metric. When Amazon CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to  ListMetrics .
    Each PutMetricData request is limited to 8 KB in size for HTTP GET requests and is limited to 40 KB in size for HTTP POST requests.
    Data that is timestamped 24 hours or more in the past may take in excess of 48 hours to become available from submission time using GetMetricStatistics .
    
    
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
            Note
            You cannot specify a namespace that begins with 'AWS/'. Namespaces that begin with 'AWS/' are reserved for other Amazon Web Services products that send metrics to Amazon CloudWatch.
            

    :type MetricData: list
    :param MetricData: [REQUIRED]
            A list of data describing the metric.
            (dict) --The MetricDatum data type encapsulates the information sent with PutMetricData to either create a new metric or add new values to be aggregated into an existing metric.
            MetricName (string) -- [REQUIRED]The name of the metric.
            Dimensions (list) --A list of dimensions associated with the metric. Note, when using the Dimensions value in a query, you need to append .member.N to it (e.g., Dimensions.member.N).
            (dict) --The Dimension data type further expands on the identity of a metric using a Name, Value pair.
            For examples that use one or more dimensions, see PutMetricData .
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement
            
            Timestamp (datetime) --The time stamp used for the metric in ISO 8601 Universal Coordinated Time (UTC) format. If not specified, the default value is set to the time the metric data was received.
            Value (float) --The value for the metric.
            Warning
            Although the Value parameter accepts numbers of type Double , Amazon CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (e.g., NaN, +Infinity, -Infinity) are not supported.
            StatisticValues (dict) --A set of statistical values describing the metric.
            SampleCount (float) -- [REQUIRED]The number of samples used for the statistic set.
            Sum (float) -- [REQUIRED]The sum of values for the sample set.
            Minimum (float) -- [REQUIRED]The minimum value of the sample set.
            Maximum (float) -- [REQUIRED]The maximum value of the sample set.
            Unit (string) --The unit of the metric.
            
            

    """
    pass

def set_alarm_state(AlarmName=None, StateValue=None, StateReason=None, StateReasonData=None):
    """
    Temporarily sets the state of an alarm for testing purposes. When the updated StateValue differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm's state to ALARM sends an Amazon SNS message. The alarm returns to its actual state (often within seconds). Because the alarm state change happens very quickly, it is typically only visible in the alarm's History tab in the Amazon CloudWatch console or through DescribeAlarmHistory .
    
    
    :example: response = client.set_alarm_state(
        AlarmName='string',
        StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
        StateReason='string',
        StateReasonData='string'
    )
    
    
    :type AlarmName: string
    :param AlarmName: [REQUIRED]
            The descriptive name for the alarm. This name must be unique within the user's AWS account. The maximum length is 255 characters.
            

    :type StateValue: string
    :param StateValue: [REQUIRED]
            The value of the state.
            

    :type StateReason: string
    :param StateReason: [REQUIRED]
            The reason that this alarm is set to this specific state (in human-readable text format)
            

    :type StateReasonData: string
    :param StateReasonData: The reason that this alarm is set to this specific state (in machine-readable JSON format)

    """
    pass

