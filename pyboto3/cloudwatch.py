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

def delete_dashboards(DashboardNames=None):
    """
    Deletes all dashboards that you specify. You may specify up to 100 dashboards to delete. If there is an error during this call, no dashboards are deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_dashboards(
        DashboardNames=[
            'string',
        ]
    )
    
    
    :type DashboardNames: list
    :param DashboardNames: [REQUIRED]
            The dashboards to be deleted. This parameter is required.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_alarm_history(AlarmName=None, HistoryItemType=None, StartDate=None, EndDate=None, MaxRecords=None, NextToken=None):
    """
    Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for all alarms are returned.
    CloudWatch retains the history of an alarm even if you delete the alarm.
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
    :param AlarmNamePrefix: The alarm name prefix. If this parameter is specified, you cannot specify AlarmNames .

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
                'DatapointsToAlarm': 123,
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
    Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period, or unit.
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
                'DatapointsToAlarm': 123,
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

def get_dashboard(DashboardName=None):
    """
    Displays the details of the dashboard that you specify.
    To copy an existing dashboard, use GetDashboard , and then use the data returned within DashboardBody as the template for the new dashboard when you call PutDashboard to create the copy.
    See also: AWS API Documentation
    
    
    :example: response = client.get_dashboard(
        DashboardName='string'
    )
    
    
    :type DashboardName: string
    :param DashboardName: [REQUIRED]
            The name of the dashboard to be described.
            

    :rtype: dict
    :return: {
        'DashboardArn': 'string',
        'DashboardBody': 'string',
        'DashboardName': 'string'
    }
    
    
    """
    pass

def get_metric_data(MetricDataQueries=None, StartTime=None, EndTime=None, NextToken=None, ScanBy=None, MaxDatapoints=None):
    """
    You can use the GetMetricData API to retrieve as many as 100 different metrics in a single request, with a total of as many as 100,800 datapoints. You can also optionally perform math expressions on the values of the returned statistics, to create new time series that represent new insights into your data. For example, using Lambda metrics, you could divide the Errors metric by the Invocations metric to get an error rate time series. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
    Calls to the GetMetricData API have a different pricing structure than calls to GetMetricStatistics . For more information about pricing, see Amazon CloudWatch Pricing .
    See also: AWS API Documentation
    
    
    :example: response = client.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'string',
                'MetricStat': {
                    'Metric': {
                        'Namespace': 'string',
                        'MetricName': 'string',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                    'Period': 123,
                    'Stat': 'string',
                    'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
                },
                'Expression': 'string',
                'Label': 'string',
                'ReturnData': True|False
            },
        ],
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        NextToken='string',
        ScanBy='TimestampDescending'|'TimestampAscending',
        MaxDatapoints=123
    )
    
    
    :type MetricDataQueries: list
    :param MetricDataQueries: [REQUIRED]
            The metric queries to be returned. A single GetMetricData call can include as many as 100 MetricDataQuery structures. Each of these structures can specify either a metric to retrieve, or a math expression to perform on retrieved data.
            (dict) --This structure indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single GetMetricData call can include up to 100 MetricDataQuery structures.
            Id (string) -- [REQUIRED]A short name used to tie this structure to the results in the response. This name must be unique within a single call to GetMetricData . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
            MetricStat (dict) --The metric to be returned, along with statistics, period, and units. Use this parameter only if this structure is performing a data retrieval and not performing a math expression on the returned data.
            Within one MetricDataQuery structure, you must specify either Expression or MetricStat but not both.
            Metric (dict) -- [REQUIRED]The metric to return, including the metric name, namespace, and dimensions.
            Namespace (string) --The namespace of the metric.
            MetricName (string) --The name of the metric.
            Dimensions (list) --The dimensions for the metric.
            (dict) --Expands the identity of a metric.
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement.
            
            Period (integer) -- [REQUIRED]The period to use when retrieving the metric.
            Stat (string) -- [REQUIRED]The statistic to return. It can include any CloudWatch statistic or extended statistic.
            Unit (string) --The unit to use for the returned data points.
            Expression (string) --The math expression to be performed on the returned data, if this structure is performing a math expression. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
            Within one MetricDataQuery structure, you must specify either Expression or MetricStat but not both.
            Label (string) --A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.
            ReturnData (boolean) --Indicates whether to return the time stamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify False . If you omit this, the default of True is used.
            
            

    :type StartTime: datetime
    :param StartTime: [REQUIRED]
            The time stamp indicating the earliest data to be returned.
            

    :type EndTime: datetime
    :param EndTime: [REQUIRED]
            The time stamp indicating the latest data to be returned.
            

    :type NextToken: string
    :param NextToken: Include this value, if it was returned by the previous call, to get the next set of data points.

    :type ScanBy: string
    :param ScanBy: The order in which data points should be returned. TimestampDescending returns the newest data first and paginates when the MaxDatapoints limit is reached. TimestampAscending returns the oldest data first and paginates when the MaxDatapoints limit is reached.

    :type MaxDatapoints: integer
    :param MaxDatapoints: The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used.

    :rtype: dict
    :return: {
        'MetricDataResults': [
            {
                'Id': 'string',
                'Label': 'string',
                'Timestamps': [
                    datetime(2015, 1, 1),
                ],
                'Values': [
                    123.0,
                ],
                'StatusCode': 'Complete'|'InternalError'|'PartialData',
                'Messages': [
                    {
                        'Code': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (datetime) --
    
    """
    pass

def get_metric_statistics(Namespace=None, MetricName=None, Dimensions=None, StartTime=None, EndTime=None, Period=None, Statistics=None, ExtendedStatistics=None, Unit=None):
    """
    Gets statistics for the specified metric.
    The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. Data points are not returned in chronological order.
    CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned.
    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:
    Amazon CloudWatch retains metric data as follows:
    Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.
    CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.
    For information about metrics and dimensions supported by AWS services, see the Amazon CloudWatch Metrics and Dimensions Reference in the Amazon CloudWatch User Guide .
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
    :param Dimensions: The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a specific combination of dimensions was not published, you can't retrieve statistics for it. You must specify the same dimensions that were used when the metrics were created. For an example, see Dimension Combinations in the Amazon CloudWatch User Guide . For more information about specifying dimensions, see Publishing Metrics in the Amazon CloudWatch User Guide .
            (dict) --Expands the identity of a metric.
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement.
            
            

    :type StartTime: datetime
    :param StartTime: [REQUIRED]
            The time stamp that determines the first data point to return. Start times are evaluated relative to the time that CloudWatch receives the request.
            The value specified is inclusive; results include data points with the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).
            CloudWatch rounds the specified time stamp as follows:
            Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.
            Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.
            Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.
            If you set Period to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15.
            

    :type EndTime: datetime
    :param EndTime: [REQUIRED]
            The time stamp that determines the last data point to return.
            The value specified is exclusive; results include data points up to the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).
            

    :type Period: integer
    :param Period: [REQUIRED]
            The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second.
            If the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:
            Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
            Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
            Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
            

    :type Statistics: list
    :param Statistics: The metric statistics, other than percentile. For percentile statistics, use ExtendedStatistics . When calling GetMetricStatistics , you must specify either Statistics or ExtendedStatistics , but not both.
            (string) --
            

    :type ExtendedStatistics: list
    :param ExtendedStatistics: The percentile statistics. Specify values between p0.0 and p100. When calling GetMetricStatistics , you must specify either Statistics or ExtendedStatistics , but not both.
            (string) --
            

    :type Unit: string
    :param Unit: The unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If you specify only a unit that the metric does not report, the results of the call are null.

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
    Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a StorageResolution of 1.
    Data points with a period of 60 seconds (1-minute) are available for 15 days.
    Data points with a period of 300 seconds (5-minute) are available for 63 days.
    Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).
    
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

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_dashboards(DashboardNamePrefix=None, NextToken=None):
    """
    Returns a list of the dashboards for your account. If you include DashboardNamePrefix , only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed.
    See also: AWS API Documentation
    
    
    :example: response = client.list_dashboards(
        DashboardNamePrefix='string',
        NextToken='string'
    )
    
    
    :type DashboardNamePrefix: string
    :param DashboardNamePrefix: If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, '.', '-', and '_'.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :rtype: dict
    :return: {
        'DashboardEntries': [
            {
                'DashboardName': 'string',
                'DashboardArn': 'string',
                'LastModified': datetime(2015, 1, 1),
                'Size': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
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

def put_dashboard(DashboardName=None, DashboardBody=None):
    """
    Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a dashboard, the entire contents are replaced with what you specify here.
    You can have up to 500 dashboards per account. All dashboards in your account are global, not region-specific.
    A simple way to create a dashboard using PutDashboard is to copy an existing dashboard. To copy an existing dashboard using the console, you can load the dashboard and then use the View/edit source command in the Actions menu to display the JSON block for that dashboard. Another way to copy a dashboard is to use GetDashboard , and then use the data returned within DashboardBody as the template for the new dashboard when you call PutDashboard .
    When you create a dashboard with PutDashboard , a good practice is to add a text widget at the top of the dashboard with a message that the dashboard was created by script and should not be changed in the console. This message could also point console users to the location of the DashboardBody script or the CloudFormation template used to create the dashboard.
    See also: AWS API Documentation
    
    
    :example: response = client.put_dashboard(
        DashboardName='string',
        DashboardBody='string'
    )
    
    
    :type DashboardName: string
    :param DashboardName: [REQUIRED]
            The name of the dashboard. If a dashboard with this name already exists, this call modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, '-', and '_'. This parameter is required.
            

    :type DashboardBody: string
    :param DashboardBody: [REQUIRED]
            The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required.
            For more information about the syntax, see CloudWatch-Dashboard-Body-Structure .
            

    :rtype: dict
    :return: {
        'DashboardValidationMessages': [
            {
                'DataPath': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    """
    pass

def put_metric_alarm(AlarmName=None, AlarmDescription=None, ActionsEnabled=None, OKActions=None, AlarmActions=None, InsufficientDataActions=None, MetricName=None, Namespace=None, Statistic=None, ExtendedStatistic=None, Dimensions=None, Period=None, Unit=None, EvaluationPeriods=None, DatapointsToAlarm=None, Threshold=None, ComparisonOperator=None, TreatMissingData=None, EvaluateLowSampleCountPercentile=None):
    """
    Creates or updates an alarm and associates it with the specified metric. Optionally, this operation can associate one or more Amazon SNS resources with the alarm.
    When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA . The alarm is evaluated and its state is set appropriately. Any actions associated with the state are then executed.
    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.
    If you are an IAM user, you must have Amazon EC2 permissions for some operations:
    If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can still create an alarm, but the stop or terminate actions are not performed. However, if you are later granted the required permissions, the alarm actions that you created earlier are performed.
    If you are using an IAM role (for example, an EC2 instance profile), you cannot stop or terminate the instance using alarm actions. However, you can still see the alarm state and perform any other actions such as Amazon SNS notifications or Auto Scaling policies.
    If you are using temporary security credentials granted using AWS STS, you cannot stop or terminate an EC2 instance using alarm actions.
    You must create at least one stop, terminate, or reboot alarm using either the Amazon EC2 or CloudWatch consoles to create the EC2ActionsAccess IAM role. After this IAM role is created, you can create stop, terminate, or reboot alarms using a command-line interface or API.
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
        DatapointsToAlarm=123,
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
            Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover | arn:aws:sns:region :account-id :sns-topic-name | arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name
            Valid Values (for use with IAM roles): arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            (string) --
            

    :type AlarmActions: list
    :param AlarmActions: The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover | arn:aws:sns:region :account-id :sns-topic-name | arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name
            Valid Values (for use with IAM roles): arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            (string) --
            

    :type InsufficientDataActions: list
    :param InsufficientDataActions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover | arn:aws:sns:region :account-id :sns-topic-name | arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name
            Valid Values (for use with IAM roles): arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            (string) --
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            The name for the metric associated with the alarm.
            

    :type Namespace: string
    :param Namespace: [REQUIRED]
            The namespace for the metric associated with the alarm.
            

    :type Statistic: string
    :param Statistic: The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ExtendedStatistic . When you call PutMetricAlarm , you must specify either Statistic or ExtendedStatistic, but not both.

    :type ExtendedStatistic: string
    :param ExtendedStatistic: The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. When you call PutMetricAlarm , you must specify either Statistic or ExtendedStatistic, but not both.

    :type Dimensions: list
    :param Dimensions: The dimensions for the metric associated with the alarm.
            (dict) --Expands the identity of a metric.
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement.
            
            

    :type Period: integer
    :param Period: [REQUIRED]
            The period, in seconds, over which the specified statistic is applied. Valid values are 10, 30, and any multiple of 60.
            Be sure to specify 10 or 30 only for metrics that are stored by a PutMetricData call with a StorageResolution of 1. If you specify a period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see Amazon CloudWatch Pricing .
            An alarm's total current evaluation period can be no longer than one day, so Period multiplied by EvaluationPeriods cannot be more than 86,400 seconds.
            

    :type Unit: string
    :param Unit: The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.
            If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, the CloudWatch alarm can get stuck in the INSUFFICIENT DATA state.
            

    :type EvaluationPeriods: integer
    :param EvaluationPeriods: [REQUIRED]
            The number of periods over which data is compared to the specified threshold. If you are setting an alarm which requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an 'M out of N' alarm, this value is the N.
            An alarm's total current evaluation period can be no longer than one day, so this number multiplied by Period cannot be more than 86,400 seconds.
            

    :type DatapointsToAlarm: integer
    :param DatapointsToAlarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an 'M out of N' alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide .

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
    :param EvaluateLowSampleCountPercentile: Used only for alarms based on percentiles. If you specify ignore , the alarm state does not change during periods with too few data points to be statistically significant. If you specify evaluate or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see Percentile-Based CloudWatch Alarms and Low Data Samples .
            Valid Values: evaluate | ignore
            

    :returns: 
    AlarmName (string) -- [REQUIRED]
    The name for the alarm. This name must be unique within the AWS account.
    
    AlarmDescription (string) -- The description for the alarm.
    ActionsEnabled (boolean) -- Indicates whether actions should be executed during any changes to the alarm state.
    OKActions (list) -- The actions to execute when this alarm transitions to an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover | arn:aws:sns:region :account-id :sns-topic-name | arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name
    Valid Values (for use with IAM roles): arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    (string) --
    
    
    AlarmActions (list) -- The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover | arn:aws:sns:region :account-id :sns-topic-name | arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name
    Valid Values (for use with IAM roles): arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    (string) --
    
    
    InsufficientDataActions (list) -- The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:region :ec2:stop | arn:aws:automate:region :ec2:terminate | arn:aws:automate:region :ec2:recover | arn:aws:sns:region :account-id :sns-topic-name | arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name
    Valid Values (for use with IAM roles): arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:region :{account-id }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    (string) --
    
    
    MetricName (string) -- [REQUIRED]
    The name for the metric associated with the alarm.
    
    Namespace (string) -- [REQUIRED]
    The namespace for the metric associated with the alarm.
    
    Statistic (string) -- The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ExtendedStatistic . When you call PutMetricAlarm , you must specify either Statistic or ExtendedStatistic, but not both.
    ExtendedStatistic (string) -- The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. When you call PutMetricAlarm , you must specify either Statistic or ExtendedStatistic, but not both.
    Dimensions (list) -- The dimensions for the metric associated with the alarm.
    
    (dict) --Expands the identity of a metric.
    
    Name (string) -- [REQUIRED]The name of the dimension.
    
    Value (string) -- [REQUIRED]The value representing the dimension measurement.
    
    
    
    
    
    Period (integer) -- [REQUIRED]
    The period, in seconds, over which the specified statistic is applied. Valid values are 10, 30, and any multiple of 60.
    Be sure to specify 10 or 30 only for metrics that are stored by a PutMetricData call with a StorageResolution of 1. If you specify a period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see Amazon CloudWatch Pricing .
    An alarm's total current evaluation period can be no longer than one day, so Period multiplied by EvaluationPeriods cannot be more than 86,400 seconds.
    
    Unit (string) -- The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.
    If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, the CloudWatch alarm can get stuck in the INSUFFICIENT DATA state.
    
    EvaluationPeriods (integer) -- [REQUIRED]
    The number of periods over which data is compared to the specified threshold. If you are setting an alarm which requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N.
    An alarm's total current evaluation period can be no longer than one day, so this number multiplied by Period cannot be more than 86,400 seconds.
    
    DatapointsToAlarm (integer) -- The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide .
    Threshold (float) -- [REQUIRED]
    The value against which the specified statistic is compared.
    
    ComparisonOperator (string) -- [REQUIRED]
    The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
    
    TreatMissingData (string) -- Sets how this alarm is to handle missing data points. If TreatMissingData is omitted, the default behavior of missing is used. For more information, see Configuring How CloudWatch Alarms Treats Missing Data .
    Valid Values: breaching | notBreaching | ignore | missing
    
    EvaluateLowSampleCountPercentile (string) -- Used only for alarms based on percentiles. If you specify ignore , the alarm state does not change during periods with too few data points to be statistically significant. If you specify evaluate or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see Percentile-Based CloudWatch Alarms and Low Data Samples .
    Valid Values: evaluate | ignore
    
    
    """
    pass

def put_metric_data(Namespace=None, MetricData=None):
    """
    Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to  ListMetrics .
    Each PutMetricData request is limited to 40 KB in size for HTTP POST requests.
    Although the Value parameter accepts numbers of type Double , CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.
    You can use up to 10 dimensions per metric to further clarify what data the metric collects. For more information about specifying dimensions, see Publishing Metrics in the Amazon CloudWatch User Guide .
    Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for  GetMetricStatistics from the time they are submitted.
    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:
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
                'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                'StorageResolution': 123
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
            Although the parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.
            StatisticValues (dict) --The statistical values for the metric.
            SampleCount (float) -- [REQUIRED]The number of samples used for the statistic set.
            Sum (float) -- [REQUIRED]The sum of values for the sample set.
            Minimum (float) -- [REQUIRED]The minimum value of the sample set.
            Maximum (float) -- [REQUIRED]The maximum value of the sample set.
            Unit (string) --The unit of the metric.
            StorageResolution (integer) --Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see High-Resolution Metrics in the Amazon CloudWatch User Guide .
            This field is optional, if you do not specify it the default of 60 is used.
            
            

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
    Although the parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.
    
    StatisticValues (dict) --The statistical values for the metric.
    
    SampleCount (float) -- [REQUIRED]The number of samples used for the statistic set.
    
    Sum (float) -- [REQUIRED]The sum of values for the sample set.
    
    Minimum (float) -- [REQUIRED]The minimum value of the sample set.
    
    Maximum (float) -- [REQUIRED]The maximum value of the sample set.
    
    
    
    Unit (string) --The unit of the metric.
    
    StorageResolution (integer) --Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see High-Resolution Metrics in the Amazon CloudWatch User Guide .
    This field is optional, if you do not specify it the default of 60 is used.
    
    
    
    
    
    
    """
    pass

def set_alarm_state(AlarmName=None, StateValue=None, StateReason=None, StateReasonData=None):
    """
    Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to ALARM sends an SNS message. The alarm returns to its actual state (often within seconds). Because the alarm state change happens quickly, it is typically only visible in the alarm's History tab in the Amazon CloudWatch console or through  DescribeAlarmHistory .
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

