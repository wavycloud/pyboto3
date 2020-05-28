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

def delete_alarms(AlarmNames=None):
    """
    Deletes the specified alarms. You can delete up to 100 alarms in one operation. However, this total can include no more than one composite alarm. For example, you could delete 99 metric alarms and one composite alarms with one operation, but you can\'t delete two composite alarms with one operation.
    In the event of an error, no alarms are deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_alarms(
        AlarmNames=[
            'string',
        ]
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: [REQUIRED]\nThe alarms to be deleted.\n\n(string) --\n\n

    :returns: 
    CloudWatch.Client.exceptions.ResourceNotFound
    
    """
    pass

def delete_anomaly_detector(Namespace=None, MetricName=None, Dimensions=None, Stat=None):
    """
    Deletes the specified anomaly detection model from your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_anomaly_detector(
        Namespace='string',
        MetricName='string',
        Dimensions=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        Stat='string'
    )
    
    
    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace associated with the anomaly detection model to delete.\n

    :type MetricName: string
    :param MetricName: [REQUIRED]\nThe metric name associated with the anomaly detection model to delete.\n

    :type Dimensions: list
    :param Dimensions: The metric dimensions associated with the anomaly detection model to delete.\n\n(dict) --Expands the identity of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value representing the dimension measurement.\n\n\n\n\n

    :type Stat: string
    :param Stat: [REQUIRED]\nThe statistic associated with the anomaly detection model to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudWatch.Client.exceptions.ResourceNotFoundException
CloudWatch.Client.exceptions.InternalServiceFault
CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.MissingRequiredParameterException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_dashboards(DashboardNames=None):
    """
    Deletes all dashboards that you specify. You may specify up to 100 dashboards to delete. If there is an error during this call, no dashboards are deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dashboards(
        DashboardNames=[
            'string',
        ]
    )
    
    
    :type DashboardNames: list
    :param DashboardNames: [REQUIRED]\nThe dashboards to be deleted. This parameter is required.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.DashboardNotFoundError
CloudWatch.Client.exceptions.InternalServiceFault


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_insight_rules(RuleNames=None):
    """
    Permanently deletes the specified Contributor Insights rules.
    If you create a rule, delete it, and then re-create it with the same name, historical data from the first time the rule was created may or may not be available.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_insight_rules(
        RuleNames=[
            'string',
        ]
    )
    
    
    :type RuleNames: list
    :param RuleNames: [REQUIRED]\nAn array of the rule names to delete. If you need to find out the names of your rules, use DescribeInsightRules .\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Failures': [
        {
            'FailureResource': 'string',
            'ExceptionType': 'string',
            'FailureCode': 'string',
            'FailureDescription': 'string'
        },
    ]
}


Response Structure

(dict) --
Failures (list) --An array listing the rules that could not be deleted. You cannot delete built-in rules.

(dict) --This array is empty if the API operation was successful for all the rules specified in the request. If the operation could not process one of the rules, the following data is returned for each of those rules.

FailureResource (string) --The specified rule that could not be deleted.

ExceptionType (string) --The type of error.

FailureCode (string) --The code of the error.

FailureDescription (string) --A description of the error.










Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.MissingRequiredParameterException


    :return: {
        'Failures': [
            {
                'FailureResource': 'string',
                'ExceptionType': 'string',
                'FailureCode': 'string',
                'FailureDescription': 'string'
            },
        ]
    }
    
    
    :returns: 
    CloudWatch.Client.exceptions.InvalidParameterValueException
    CloudWatch.Client.exceptions.MissingRequiredParameterException
    
    """
    pass

def describe_alarm_history(AlarmName=None, AlarmTypes=None, HistoryItemType=None, StartDate=None, EndDate=None, MaxRecords=None, NextToken=None, ScanBy=None):
    """
    Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for either all metric alarms or all composite alarms are returned.
    CloudWatch retains the history of an alarm even if you delete the alarm.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_alarm_history(
        AlarmName='string',
        AlarmTypes=[
            'CompositeAlarm'|'MetricAlarm',
        ],
        HistoryItemType='ConfigurationUpdate'|'StateUpdate'|'Action',
        StartDate=datetime(2015, 1, 1),
        EndDate=datetime(2015, 1, 1),
        MaxRecords=123,
        NextToken='string',
        ScanBy='TimestampDescending'|'TimestampAscending'
    )
    
    
    :type AlarmName: string
    :param AlarmName: The name of the alarm.

    :type AlarmTypes: list
    :param AlarmTypes: Use this parameter to specify whether you want the operation to return metric alarms or composite alarms. If you omit this parameter, only metric alarms are returned.\n\n(string) --\n\n

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

    :type ScanBy: string
    :param ScanBy: Specified whether to return the newest or oldest alarm history first. Specify TimestampDescending to have the newest event history returned first, and specify TimestampAscending to have the oldest history returned first.

    :rtype: dict

ReturnsResponse Syntax
{
    'AlarmHistoryItems': [
        {
            'AlarmName': 'string',
            'AlarmType': 'CompositeAlarm'|'MetricAlarm',
            'Timestamp': datetime(2015, 1, 1),
            'HistoryItemType': 'ConfigurationUpdate'|'StateUpdate'|'Action',
            'HistorySummary': 'string',
            'HistoryData': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AlarmHistoryItems (list) --
The alarm histories, in JSON format.

(dict) --
Represents the history of a specific alarm.

AlarmName (string) --
The descriptive name for the alarm.

AlarmType (string) --
The type of alarm, either metric alarm or composite alarm.

Timestamp (datetime) --
The time stamp for the alarm history item.

HistoryItemType (string) --
The type of alarm history item.

HistorySummary (string) --
A summary of the alarm history, in text format.

HistoryData (string) --
Data about the alarm, in JSON format.





NextToken (string) --
The token that marks the start of the next batch of returned results.







Exceptions

CloudWatch.Client.exceptions.InvalidNextToken


    :return: {
        'AlarmHistoryItems': [
            {
                'AlarmName': 'string',
                'AlarmType': 'CompositeAlarm'|'MetricAlarm',
                'Timestamp': datetime(2015, 1, 1),
                'HistoryItemType': 'ConfigurationUpdate'|'StateUpdate'|'Action',
                'HistorySummary': 'string',
                'HistoryData': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CloudWatch.Client.exceptions.InvalidNextToken
    
    """
    pass

def describe_alarms(AlarmNames=None, AlarmNamePrefix=None, AlarmTypes=None, ChildrenOfAlarmName=None, ParentsOfAlarmName=None, StateValue=None, ActionPrefix=None, MaxRecords=None, NextToken=None):
    """
    Retrieves the specified alarms. You can filter the results by specifying a a prefix for the alarm name, the alarm state, or a prefix for any action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_alarms(
        AlarmNames=[
            'string',
        ],
        AlarmNamePrefix='string',
        AlarmTypes=[
            'CompositeAlarm'|'MetricAlarm',
        ],
        ChildrenOfAlarmName='string',
        ParentsOfAlarmName='string',
        StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
        ActionPrefix='string',
        MaxRecords=123,
        NextToken='string'
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: The names of the alarms to retrieve information about.\n\n(string) --\n\n

    :type AlarmNamePrefix: string
    :param AlarmNamePrefix: An alarm name prefix. If you specify this parameter, you receive information about all alarms that have names that start with this prefix.\nIf this parameter is specified, you cannot specify AlarmNames .\n

    :type AlarmTypes: list
    :param AlarmTypes: Use this parameter to specify whether you want the operation to return metric alarms or composite alarms. If you omit this parameter, only metric alarms are returned.\n\n(string) --\n\n

    :type ChildrenOfAlarmName: string
    :param ChildrenOfAlarmName: If you use this parameter and specify the name of a composite alarm, the operation returns information about the 'children' alarms of the alarm you specify. These are the metric alarms and composite alarms referenced in the AlarmRule field of the composite alarm that you specify in ChildrenOfAlarmName . Information about the composite alarm that you name in ChildrenOfAlarmName is not returned.\nIf you specify ChildrenOfAlarmName , you cannot specify any other parameters in the request except for MaxRecords and NextToken . If you do so, you will receive a validation error.\n\nNote\nOnly the Alarm Name , ARN , StateValue (OK/ALARM/INSUFFICIENT_DATA), and StateUpdatedTimestamp information are returned by this operation when you use this parameter. To get complete information about these alarms, perform another DescribeAlarms operation and specify the parent alarm names in the AlarmNames parameter.\n\n

    :type ParentsOfAlarmName: string
    :param ParentsOfAlarmName: If you use this parameter and specify the name of a metric or composite alarm, the operation returns information about the 'parent' alarms of the alarm you specify. These are the composite alarms that have AlarmRule parameters that reference the alarm named in ParentsOfAlarmName . Information about the alarm that you specify in ParentsOfAlarmName is not returned.\nIf you specify ParentsOfAlarmName , you cannot specify any other parameters in the request except for MaxRecords and NextToken . If you do so, you will receive a validation error.\n\nNote\nOnly the Alarm Name and ARN are returned by this operation when you use this parameter. To get complete information about these alarms, perform another DescribeAlarms operation and specify the parent alarm names in the AlarmNames parameter.\n\n

    :type StateValue: string
    :param StateValue: Specify this parameter to receive information only about alarms that are currently in the state that you specify.

    :type ActionPrefix: string
    :param ActionPrefix: Use this parameter to filter the results of the operation to only those alarms that use a certain alarm action. For example, you could specify the ARN of an SNS topic to find all alarms that send notifications to that topic.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of alarm descriptions to retrieve.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :rtype: dict

ReturnsResponse Syntax
{
    'CompositeAlarms': [
        {
            'ActionsEnabled': True|False,
            'AlarmActions': [
                'string',
            ],
            'AlarmArn': 'string',
            'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
            'AlarmDescription': 'string',
            'AlarmName': 'string',
            'AlarmRule': 'string',
            'InsufficientDataActions': [
                'string',
            ],
            'OKActions': [
                'string',
            ],
            'StateReason': 'string',
            'StateReasonData': 'string',
            'StateUpdatedTimestamp': datetime(2015, 1, 1),
            'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA'
        },
    ],
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
            'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'|'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
            'TreatMissingData': 'string',
            'EvaluateLowSampleCountPercentile': 'string',
            'Metrics': [
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
                    'ReturnData': True|False,
                    'Period': 123
                },
            ],
            'ThresholdMetricId': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CompositeAlarms (list) --
The information about any composite alarms returned by the operation.

(dict) --
The details about a composite alarm.

ActionsEnabled (boolean) --
Indicates whether actions should be executed during any changes to the alarm state.

AlarmActions (list) --
The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string) --


AlarmArn (string) --
The Amazon Resource Name (ARN) of the alarm.

AlarmConfigurationUpdatedTimestamp (datetime) --
The time stamp of the last update to the alarm configuration.

AlarmDescription (string) --
The description of the alarm.

AlarmName (string) --
The name of the alarm.

AlarmRule (string) --
The rule that this alarm uses to evaluate its alarm state.

InsufficientDataActions (list) --
The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string) --


OKActions (list) --
The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string) --


StateReason (string) --
An explanation for the alarm state, in text format.

StateReasonData (string) --
An explanation for the alarm state, in JSON format.

StateUpdatedTimestamp (datetime) --
The time stamp of the last update to the alarm state.

StateValue (string) --
The state value for the alarm.





MetricAlarms (list) --
The information about any metric alarms returned by the operation.

(dict) --
The details about a metric alarm.

AlarmName (string) --
The name of the alarm.

AlarmArn (string) --
The Amazon Resource Name (ARN) of the alarm.

AlarmDescription (string) --
The description of the alarm.

AlarmConfigurationUpdatedTimestamp (datetime) --
The time stamp of the last update to the alarm configuration.

ActionsEnabled (boolean) --
Indicates whether actions should be executed during any changes to the alarm state.

OKActions (list) --
The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string) --


AlarmActions (list) --
The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string) --


InsufficientDataActions (list) --
The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string) --


StateValue (string) --
The state value for the alarm.

StateReason (string) --
An explanation for the alarm state, in text format.

StateReasonData (string) --
An explanation for the alarm state, in JSON format.

StateUpdatedTimestamp (datetime) --
The time stamp of the last update to the alarm state.

MetricName (string) --
The name of the metric associated with the alarm, if this is an alarm based on a single metric.

Namespace (string) --
The namespace of the metric associated with the alarm.

Statistic (string) --
The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ExtendedStatistic .

ExtendedStatistic (string) --
The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

Dimensions (list) --
The dimensions for the metric associated with the alarm.

(dict) --
Expands the identity of a metric.

Name (string) --
The name of the dimension.

Value (string) --
The value representing the dimension measurement.





Period (integer) --
The period, in seconds, over which the statistic is applied.

Unit (string) --
The unit of the metric associated with the alarm.

EvaluationPeriods (integer) --
The number of periods over which data is compared to the specified threshold.

DatapointsToAlarm (integer) --
The number of data points that must be breaching to trigger the alarm.

Threshold (float) --
The value to compare with the specified statistic.

ComparisonOperator (string) --
The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

TreatMissingData (string) --
Sets how this alarm is to handle missing data points. If this parameter is omitted, the default behavior of missing is used.

EvaluateLowSampleCountPercentile (string) --
Used only for alarms based on percentiles. If ignore , the alarm state does not change during periods with too few data points to be statistically significant. If evaluate or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

Metrics (list) --
An array of MetricDataQuery structures, used in an alarm based on a metric math expression. Each structure either retrieves a metric or performs a math expression. One item in the Metrics array is the math expression that the alarm watches. This expression by designated by having ReturnValue set to true.

(dict) --
This structure is used in both GetMetricData and PutMetricAlarm . The supported use of this structure is different for those two operations.
When used in GetMetricData , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single GetMetricData call can include up to 500 MetricDataQuery structures.
When used in PutMetricAlarm , it enables you to create an alarm based on a metric math expression. Each MetricDataQuery in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single PutMetricAlarm call can include up to 20 MetricDataQuery structures in the array. The 20 structures can include as many as 10 structures that contain a MetricStat parameter to retrieve a metric, and as many as 10 structures that contain the Expression parameter to perform a math expression. Of those Expression structures, one must have True as the value for ReturnData . The result of this expression is the value the alarm watches.
Any expression used in a PutMetricAlarm operation must return a single time series. For more information, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
Some of the parameters of this structure also have different uses whether you are using this structure in a GetMetricData operation or a PutMetricAlarm operation. These differences are explained in the following parameter list.

Id (string) --
A short name used to tie this object to the results in the response. This name must be unique within a single call to GetMetricData . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat (dict) --
The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
Within one MetricDataQuery object, you must specify either Expression or MetricStat but not both.

Metric (dict) --
The metric to return, including the metric name, namespace, and dimensions.

Namespace (string) --
The namespace of the metric.

MetricName (string) --
The name of the metric. This is a required field.

Dimensions (list) --
The dimensions for the metric.

(dict) --
Expands the identity of a metric.

Name (string) --
The name of the dimension.

Value (string) --
The value representing the dimension measurement.







Period (integer) --
The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second.
If the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).


Stat (string) --
The statistic to return. It can include any CloudWatch statistic or extended statistic.

Unit (string) --
When you are using a Put operation, this defines what unit you want to use when storing the metric.
In a Get operation, if you omit Unit then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.



Expression (string) --
The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the Id of the other metrics to refer to those metrics, and can also use the Id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
Within each MetricDataQuery object, you must specify either Expression or MetricStat but not both.

Label (string) --
A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.

ReturnData (boolean) --
When used in GetMetricData , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify False . If you omit this, the default of True is used.
When used in PutMetricAlarm , specify True for the one expression result to use as the alarm. For all other metrics and expressions in the same PutMetricAlarm operation, specify ReturnData as False.

Period (integer) --
The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData operation that includes a StorageResolution of 1 second .





ThresholdMetricId (string) --
In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.





NextToken (string) --
The token that marks the start of the next batch of returned results.







Exceptions

CloudWatch.Client.exceptions.InvalidNextToken


    :return: {
        'CompositeAlarms': [
            {
                'ActionsEnabled': True|False,
                'AlarmActions': [
                    'string',
                ],
                'AlarmArn': 'string',
                'AlarmConfigurationUpdatedTimestamp': datetime(2015, 1, 1),
                'AlarmDescription': 'string',
                'AlarmName': 'string',
                'AlarmRule': 'string',
                'InsufficientDataActions': [
                    'string',
                ],
                'OKActions': [
                    'string',
                ],
                'StateReason': 'string',
                'StateReasonData': 'string',
                'StateUpdatedTimestamp': datetime(2015, 1, 1),
                'StateValue': 'OK'|'ALARM'|'INSUFFICIENT_DATA'
            },
        ],
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
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'|'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
                'TreatMissingData': 'string',
                'EvaluateLowSampleCountPercentile': 'string',
                'Metrics': [
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
                        'ReturnData': True|False,
                        'Period': 123
                    },
                ],
                'ThresholdMetricId': 'string'
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
    :param MetricName: [REQUIRED]\nThe name of the metric.\n

    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace of the metric.\n

    :type Statistic: string
    :param Statistic: The statistic for the metric, other than percentiles. For percentile statistics, use ExtendedStatistics .

    :type ExtendedStatistic: string
    :param ExtendedStatistic: The percentile statistic for the metric. Specify a value between p0.0 and p100.

    :type Dimensions: list
    :param Dimensions: The dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the call to succeed.\n\n(dict) --Expands the identity of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value representing the dimension measurement.\n\n\n\n\n

    :type Period: integer
    :param Period: The period, in seconds, over which the statistic is applied.

    :type Unit: string
    :param Unit: The unit for the metric.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'|'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
            'TreatMissingData': 'string',
            'EvaluateLowSampleCountPercentile': 'string',
            'Metrics': [
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
                    'ReturnData': True|False,
                    'Period': 123
                },
            ],
            'ThresholdMetricId': 'string'
        },
    ]
}


Response Structure

(dict) --

MetricAlarms (list) --
The information for each alarm with the specified metric.

(dict) --
The details about a metric alarm.

AlarmName (string) --
The name of the alarm.

AlarmArn (string) --
The Amazon Resource Name (ARN) of the alarm.

AlarmDescription (string) --
The description of the alarm.

AlarmConfigurationUpdatedTimestamp (datetime) --
The time stamp of the last update to the alarm configuration.

ActionsEnabled (boolean) --
Indicates whether actions should be executed during any changes to the alarm state.

OKActions (list) --
The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string) --


AlarmActions (list) --
The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string) --


InsufficientDataActions (list) --
The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).

(string) --


StateValue (string) --
The state value for the alarm.

StateReason (string) --
An explanation for the alarm state, in text format.

StateReasonData (string) --
An explanation for the alarm state, in JSON format.

StateUpdatedTimestamp (datetime) --
The time stamp of the last update to the alarm state.

MetricName (string) --
The name of the metric associated with the alarm, if this is an alarm based on a single metric.

Namespace (string) --
The namespace of the metric associated with the alarm.

Statistic (string) --
The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ExtendedStatistic .

ExtendedStatistic (string) --
The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

Dimensions (list) --
The dimensions for the metric associated with the alarm.

(dict) --
Expands the identity of a metric.

Name (string) --
The name of the dimension.

Value (string) --
The value representing the dimension measurement.





Period (integer) --
The period, in seconds, over which the statistic is applied.

Unit (string) --
The unit of the metric associated with the alarm.

EvaluationPeriods (integer) --
The number of periods over which data is compared to the specified threshold.

DatapointsToAlarm (integer) --
The number of data points that must be breaching to trigger the alarm.

Threshold (float) --
The value to compare with the specified statistic.

ComparisonOperator (string) --
The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

TreatMissingData (string) --
Sets how this alarm is to handle missing data points. If this parameter is omitted, the default behavior of missing is used.

EvaluateLowSampleCountPercentile (string) --
Used only for alarms based on percentiles. If ignore , the alarm state does not change during periods with too few data points to be statistically significant. If evaluate or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

Metrics (list) --
An array of MetricDataQuery structures, used in an alarm based on a metric math expression. Each structure either retrieves a metric or performs a math expression. One item in the Metrics array is the math expression that the alarm watches. This expression by designated by having ReturnValue set to true.

(dict) --
This structure is used in both GetMetricData and PutMetricAlarm . The supported use of this structure is different for those two operations.
When used in GetMetricData , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single GetMetricData call can include up to 500 MetricDataQuery structures.
When used in PutMetricAlarm , it enables you to create an alarm based on a metric math expression. Each MetricDataQuery in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single PutMetricAlarm call can include up to 20 MetricDataQuery structures in the array. The 20 structures can include as many as 10 structures that contain a MetricStat parameter to retrieve a metric, and as many as 10 structures that contain the Expression parameter to perform a math expression. Of those Expression structures, one must have True as the value for ReturnData . The result of this expression is the value the alarm watches.
Any expression used in a PutMetricAlarm operation must return a single time series. For more information, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
Some of the parameters of this structure also have different uses whether you are using this structure in a GetMetricData operation or a PutMetricAlarm operation. These differences are explained in the following parameter list.

Id (string) --
A short name used to tie this object to the results in the response. This name must be unique within a single call to GetMetricData . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat (dict) --
The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
Within one MetricDataQuery object, you must specify either Expression or MetricStat but not both.

Metric (dict) --
The metric to return, including the metric name, namespace, and dimensions.

Namespace (string) --
The namespace of the metric.

MetricName (string) --
The name of the metric. This is a required field.

Dimensions (list) --
The dimensions for the metric.

(dict) --
Expands the identity of a metric.

Name (string) --
The name of the dimension.

Value (string) --
The value representing the dimension measurement.







Period (integer) --
The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second.
If the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).


Stat (string) --
The statistic to return. It can include any CloudWatch statistic or extended statistic.

Unit (string) --
When you are using a Put operation, this defines what unit you want to use when storing the metric.
In a Get operation, if you omit Unit then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.



Expression (string) --
The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the Id of the other metrics to refer to those metrics, and can also use the Id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
Within each MetricDataQuery object, you must specify either Expression or MetricStat but not both.

Label (string) --
A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.

ReturnData (boolean) --
When used in GetMetricData , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify False . If you omit this, the default of True is used.
When used in PutMetricAlarm , specify True for the one expression result to use as the alarm. For all other metrics and expressions in the same PutMetricAlarm operation, specify ReturnData as False.

Period (integer) --
The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData operation that includes a StorageResolution of 1 second .





ThresholdMetricId (string) --
In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.












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
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'|'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
                'TreatMissingData': 'string',
                'EvaluateLowSampleCountPercentile': 'string',
                'Metrics': [
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
                        'ReturnData': True|False,
                        'Period': 123
                    },
                ],
                'ThresholdMetricId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_anomaly_detectors(NextToken=None, MaxResults=None, Namespace=None, MetricName=None, Dimensions=None):
    """
    Lists the anomaly detection models that you have created in your account. You can list all models in your account or filter the results to only the models that are related to a certain namespace, metric name, or metric dimension.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_anomaly_detectors(
        NextToken='string',
        MaxResults=123,
        Namespace='string',
        MetricName='string',
        Dimensions=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: Use the token returned by the previous operation to request the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in one operation. The maximum value that you can specify is 100.\nTo retrieve the remaining results, make another call with the returned NextToken value.\n

    :type Namespace: string
    :param Namespace: Limits the results to only the anomaly detection models that are associated with the specified namespace.

    :type MetricName: string
    :param MetricName: Limits the results to only the anomaly detection models that are associated with the specified metric name. If there are multiple metrics with this name in different namespaces that have anomaly detection models, they\'re all returned.

    :type Dimensions: list
    :param Dimensions: Limits the results to only the anomaly detection models that are associated with the specified metric dimensions. If there are multiple metrics that have these dimensions and have anomaly detection models associated, they\'re all returned.\n\n(dict) --Expands the identity of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value representing the dimension measurement.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AnomalyDetectors': [
        {
            'Namespace': 'string',
            'MetricName': 'string',
            'Dimensions': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'Stat': 'string',
            'Configuration': {
                'ExcludedTimeRanges': [
                    {
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1)
                    },
                ],
                'MetricTimezone': 'string'
            },
            'StateValue': 'PENDING_TRAINING'|'TRAINED_INSUFFICIENT_DATA'|'TRAINED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AnomalyDetectors (list) --
The list of anomaly detection models returned by the operation.

(dict) --
An anomaly detection model associated with a particular CloudWatch metric and statistic. You can use the model to display a band of expected normal values when the metric is graphed.

Namespace (string) --
The namespace of the metric associated with the anomaly detection model.

MetricName (string) --
The name of the metric associated with the anomaly detection model.

Dimensions (list) --
The metric dimensions associated with the anomaly detection model.

(dict) --
Expands the identity of a metric.

Name (string) --
The name of the dimension.

Value (string) --
The value representing the dimension measurement.





Stat (string) --
The statistic associated with the anomaly detection model.

Configuration (dict) --
The configuration specifies details about how the anomaly detection model is to be trained, including time ranges to exclude from use for training the model, and the time zone to use for the metric.

ExcludedTimeRanges (list) --
An array of time ranges to exclude from use when the anomaly detection model is trained. Use this to make sure that events that could cause unusual values for the metric, such as deployments, aren\'t used when CloudWatch creates the model.

(dict) --
Specifies one range of days or times to exclude from use for training an anomaly detection model.

StartTime (datetime) --
The start time of the range to exclude. The format is yyyy-MM-dd\'T\'HH:mm:ss . For example, 2019-07-01T23:59:59 .

EndTime (datetime) --
The end time of the range to exclude. The format is yyyy-MM-dd\'T\'HH:mm:ss . For example, 2019-07-01T23:59:59 .





MetricTimezone (string) --
The time zone to use for the metric. This is useful to enable the model to automatically account for daylight savings time changes if the metric is sensitive to such time changes.
To specify a time zone, use the name of the time zone as specified in the standard tz database. For more information, see tz database .



StateValue (string) --
The current status of the anomaly detector\'s training. The possible values are TRAINED | PENDING_TRAINING | TRAINED_INSUFFICIENT_DATA





NextToken (string) --
A token that you can use in a subsequent operation to retrieve the next set of results.







Exceptions

CloudWatch.Client.exceptions.InvalidNextToken
CloudWatch.Client.exceptions.InternalServiceFault
CloudWatch.Client.exceptions.InvalidParameterValueException


    :return: {
        'AnomalyDetectors': [
            {
                'Namespace': 'string',
                'MetricName': 'string',
                'Dimensions': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'Stat': 'string',
                'Configuration': {
                    'ExcludedTimeRanges': [
                        {
                            'StartTime': datetime(2015, 1, 1),
                            'EndTime': datetime(2015, 1, 1)
                        },
                    ],
                    'MetricTimezone': 'string'
                },
                'StateValue': 'PENDING_TRAINING'|'TRAINED_INSUFFICIENT_DATA'|'TRAINED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CloudWatch.Client.exceptions.InvalidNextToken
    CloudWatch.Client.exceptions.InternalServiceFault
    CloudWatch.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def describe_insight_rules(NextToken=None, MaxResults=None):
    """
    Returns a list of all the Contributor Insights rules in your account. All rules in your account are returned with a single operation.
    For more information about Contributor Insights, see Using Contributor Insights to Analyze High-Cardinality Data .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_insight_rules(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Reserved for future use.

    :type MaxResults: integer
    :param MaxResults: This parameter is not currently used. Reserved for future use. If it is used in the future, the maximum value may be different.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'InsightRules': [
        {
            'Name': 'string',
            'State': 'string',
            'Schema': 'string',
            'Definition': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
Reserved for future use.

InsightRules (list) --
The rules returned by the operation.

(dict) --
This structure contains the definition for a Contributor Insights rule.

Name (string) --
The name of the rule.

State (string) --
Indicates whether the rule is enabled or disabled.

Schema (string) --
For rules that you create, this is always {"Name": "CloudWatchLogRule", "Version": 1} . For built-in rules, this is {"Name": "ServiceLogRule", "Version": 1}

Definition (string) --
The definition of the rule, as a JSON object. The definition contains the keywords used to define contributors, the value to aggregate on if this rule returns a sum instead of a count, and the filters. For details on the valid syntax, see Contributor Insights Rule Syntax .











Exceptions

CloudWatch.Client.exceptions.InvalidNextToken


    :return: {
        'NextToken': 'string',
        'InsightRules': [
            {
                'Name': 'string',
                'State': 'string',
                'Schema': 'string',
                'Definition': 'string'
            },
        ]
    }
    
    
    :returns: 
    CloudWatch.Client.exceptions.InvalidNextToken
    
    """
    pass

def disable_alarm_actions(AlarmNames=None):
    """
    Disables the actions for the specified alarms. When an alarm\'s actions are disabled, the alarm actions do not execute when the alarm state changes.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_alarm_actions(
        AlarmNames=[
            'string',
        ]
    )
    
    
    :type AlarmNames: list
    :param AlarmNames: [REQUIRED]\nThe names of the alarms.\n\n(string) --\n\n

    """
    pass

def disable_insight_rules(RuleNames=None):
    """
    Disables the specified Contributor Insights rules. When rules are disabled, they do not analyze log groups and do not incur costs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_insight_rules(
        RuleNames=[
            'string',
        ]
    )
    
    
    :type RuleNames: list
    :param RuleNames: [REQUIRED]\nAn array of the rule names to disable. If you need to find out the names of your rules, use DescribeInsightRules .\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Failures': [
        {
            'FailureResource': 'string',
            'ExceptionType': 'string',
            'FailureCode': 'string',
            'FailureDescription': 'string'
        },
    ]
}


Response Structure

(dict) --
Failures (list) --An array listing the rules that could not be disabled. You cannot disable built-in rules.

(dict) --This array is empty if the API operation was successful for all the rules specified in the request. If the operation could not process one of the rules, the following data is returned for each of those rules.

FailureResource (string) --The specified rule that could not be deleted.

ExceptionType (string) --The type of error.

FailureCode (string) --The code of the error.

FailureDescription (string) --A description of the error.










Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.MissingRequiredParameterException


    :return: {
        'Failures': [
            {
                'FailureResource': 'string',
                'ExceptionType': 'string',
                'FailureCode': 'string',
                'FailureDescription': 'string'
            },
        ]
    }
    
    
    :returns: 
    CloudWatch.Client.exceptions.InvalidParameterValueException
    CloudWatch.Client.exceptions.MissingRequiredParameterException
    
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
    :param AlarmNames: [REQUIRED]\nThe names of the alarms.\n\n(string) --\n\n

    """
    pass

def enable_insight_rules(RuleNames=None):
    """
    Enables the specified Contributor Insights rules. When rules are enabled, they immediately begin analyzing log data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_insight_rules(
        RuleNames=[
            'string',
        ]
    )
    
    
    :type RuleNames: list
    :param RuleNames: [REQUIRED]\nAn array of the rule names to enable. If you need to find out the names of your rules, use DescribeInsightRules .\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Failures': [
        {
            'FailureResource': 'string',
            'ExceptionType': 'string',
            'FailureCode': 'string',
            'FailureDescription': 'string'
        },
    ]
}


Response Structure

(dict) --
Failures (list) --An array listing the rules that could not be enabled. You cannot disable or enable built-in rules.

(dict) --This array is empty if the API operation was successful for all the rules specified in the request. If the operation could not process one of the rules, the following data is returned for each of those rules.

FailureResource (string) --The specified rule that could not be deleted.

ExceptionType (string) --The type of error.

FailureCode (string) --The code of the error.

FailureDescription (string) --A description of the error.










Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.MissingRequiredParameterException
CloudWatch.Client.exceptions.LimitExceededException


    :return: {
        'Failures': [
            {
                'FailureResource': 'string',
                'ExceptionType': 'string',
                'FailureCode': 'string',
                'FailureDescription': 'string'
            },
        ]
    }
    
    
    :returns: 
    CloudWatch.Client.exceptions.InvalidParameterValueException
    CloudWatch.Client.exceptions.MissingRequiredParameterException
    CloudWatch.Client.exceptions.LimitExceededException
    
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

def get_dashboard(DashboardName=None):
    """
    Displays the details of the dashboard that you specify.
    To copy an existing dashboard, use GetDashboard , and then use the data returned within DashboardBody as the template for the new dashboard when you call PutDashboard to create the copy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_dashboard(
        DashboardName='string'
    )
    
    
    :type DashboardName: string
    :param DashboardName: [REQUIRED]\nThe name of the dashboard to be described.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DashboardArn': 'string',
    'DashboardBody': 'string',
    'DashboardName': 'string'
}


Response Structure

(dict) --
DashboardArn (string) --The Amazon Resource Name (ARN) of the dashboard.

DashboardBody (string) --The detailed information about the dashboard, including what widgets are included and their location on the dashboard. For more information about the DashboardBody syntax, see Dashboard Body Structure and Syntax .

DashboardName (string) --The name of the dashboard.






Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.DashboardNotFoundError
CloudWatch.Client.exceptions.InternalServiceFault


    :return: {
        'DashboardArn': 'string',
        'DashboardBody': 'string',
        'DashboardName': 'string'
    }
    
    
    """
    pass

def get_insight_rule_report(RuleName=None, StartTime=None, EndTime=None, Period=None, MaxContributorCount=None, Metrics=None, OrderBy=None):
    """
    This operation returns the time series data collected by a Contributor Insights rule. The data includes the identity and number of contributors to the log group.
    You can also optionally return one or more statistics about each data point in the time series. These statistics can include the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_insight_rule_report(
        RuleName='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Period=123,
        MaxContributorCount=123,
        Metrics=[
            'string',
        ],
        OrderBy='string'
    )
    
    
    :type RuleName: string
    :param RuleName: [REQUIRED]\nThe name of the rule that you want to see data from.\n

    :type StartTime: datetime
    :param StartTime: [REQUIRED]\nThe start time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as yyyy-MM-dd\'T\'HH:mm:ss . For example, 2019-07-01T23:59:59 .\n

    :type EndTime: datetime
    :param EndTime: [REQUIRED]\nThe end time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as yyyy-MM-dd\'T\'HH:mm:ss . For example, 2019-07-01T23:59:59 .\n

    :type Period: integer
    :param Period: [REQUIRED]\nThe period, in seconds, to use for the statistics in the InsightRuleMetricDatapoint results.\n

    :type MaxContributorCount: integer
    :param MaxContributorCount: The maximum number of contributors to include in the report. The range is 1 to 100. If you omit this, the default of 10 is used.

    :type Metrics: list
    :param Metrics: Specifies which metrics to use for aggregation of contributor values for the report. You can specify one or more of the following metrics:\n\nUniqueContributors -- the number of unique contributors for each data point.\nMaxContributorValue -- the value of the top contributor for each data point. The identity of the contributor may change for each data point in the graph. If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the rule\'s Value , during that period.\nSampleCount -- the number of data points matched by the rule.\nSum -- the sum of the values from all contributors during the time period represented by that data point.\nMinimum -- the minimum value from a single observation during the time period represented by that data point.\nMaximum -- the maximum value from a single observation during the time period represented by that data point.\nAverage -- the average value from all contributors during the time period represented by that data point.\n\n\n(string) --\n\n

    :type OrderBy: string
    :param OrderBy: Determines what statistic to use to rank the contributors. Valid values are SUM and MAXIMUM.

    :rtype: dict

ReturnsResponse Syntax
{
    'KeyLabels': [
        'string',
    ],
    'AggregationStatistic': 'string',
    'AggregateValue': 123.0,
    'ApproximateUniqueCount': 123,
    'Contributors': [
        {
            'Keys': [
                'string',
            ],
            'ApproximateAggregateValue': 123.0,
            'Datapoints': [
                {
                    'Timestamp': datetime(2015, 1, 1),
                    'ApproximateValue': 123.0
                },
            ]
        },
    ],
    'MetricDatapoints': [
        {
            'Timestamp': datetime(2015, 1, 1),
            'UniqueContributors': 123.0,
            'MaxContributorValue': 123.0,
            'SampleCount': 123.0,
            'Average': 123.0,
            'Sum': 123.0,
            'Minimum': 123.0,
            'Maximum': 123.0
        },
    ]
}


Response Structure

(dict) --

KeyLabels (list) --
An array of the strings used as the keys for this rule. The keys are the dimensions used to classify contributors. If the rule contains more than one key, then each unique combination of values for the keys is counted as a unique contributor.

(string) --


AggregationStatistic (string) --
Specifies whether this rule aggregates contributor data by COUNT or SUM.

AggregateValue (float) --
The sum of the values from all individual contributors that match the rule.

ApproximateUniqueCount (integer) --
An approximate count of the unique contributors found by this rule in this time period.

Contributors (list) --
An array of the unique contributors found by this rule in this time period. If the rule contains multiple keys, each combination of values for the keys counts as a unique contributor.

(dict) --
One of the unique contributors found by a Contributor Insights rule. If the rule contains multiple keys, then a unique contributor is a unique combination of values from all the keys in the rule.
If the rule contains a single key, then each unique contributor is each unique value for this key.
For more information, see GetInsightRuleReport .

Keys (list) --
One of the log entry field keywords that is used to define contributors for this rule.

(string) --


ApproximateAggregateValue (float) --
An approximation of the aggregate value that comes from this contributor.

Datapoints (list) --
An array of the data points where this contributor is present. Only the data points when this contributor appeared are included in the array.

(dict) --
One data point related to one contributor.
For more information, see GetInsightRuleReport and InsightRuleContributor .

Timestamp (datetime) --
The timestamp of the data point.

ApproximateValue (float) --
The approximate value that this contributor added during this timestamp.









MetricDatapoints (list) --
A time series of metric data points that matches the time period in the rule request.

(dict) --
One data point from the metric time series returned in a Contributor Insights rule report.
For more information, see GetInsightRuleReport .

Timestamp (datetime) --
The timestamp of the data point.

UniqueContributors (float) --
The number of unique contributors who published data during this timestamp.
This statistic is returned only if you included it in the Metrics array in your request.

MaxContributorValue (float) --
The maximum value provided by one contributor during this timestamp. Each timestamp is evaluated separately, so the identity of the max contributor could be different for each timestamp.
This statistic is returned only if you included it in the Metrics array in your request.

SampleCount (float) --
The number of occurrences that matched the rule during this data point.
This statistic is returned only if you included it in the Metrics array in your request.

Average (float) --
The average value from all contributors during the time period represented by that data point.
This statistic is returned only if you included it in the Metrics array in your request.

Sum (float) --
The sum of the values from all contributors during the time period represented by that data point.
This statistic is returned only if you included it in the Metrics array in your request.

Minimum (float) --
The minimum value from a single contributor during the time period represented by that data point.
This statistic is returned only if you included it in the Metrics array in your request.

Maximum (float) --
The maximum value from a single occurence from a single contributor during the time period represented by that data point.
This statistic is returned only if you included it in the Metrics array in your request.











Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.MissingRequiredParameterException
CloudWatch.Client.exceptions.ResourceNotFoundException


    :return: {
        'KeyLabels': [
            'string',
        ],
        'AggregationStatistic': 'string',
        'AggregateValue': 123.0,
        'ApproximateUniqueCount': 123,
        'Contributors': [
            {
                'Keys': [
                    'string',
                ],
                'ApproximateAggregateValue': 123.0,
                'Datapoints': [
                    {
                        'Timestamp': datetime(2015, 1, 1),
                        'ApproximateValue': 123.0
                    },
                ]
            },
        ],
        'MetricDatapoints': [
            {
                'Timestamp': datetime(2015, 1, 1),
                'UniqueContributors': 123.0,
                'MaxContributorValue': 123.0,
                'SampleCount': 123.0,
                'Average': 123.0,
                'Sum': 123.0,
                'Minimum': 123.0,
                'Maximum': 123.0
            },
        ]
    }
    
    
    :returns: 
    RuleName (string) -- [REQUIRED]
    The name of the rule that you want to see data from.
    
    StartTime (datetime) -- [REQUIRED]
    The start time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as yyyy-MM-dd\'T\'HH:mm:ss . For example, 2019-07-01T23:59:59 .
    
    EndTime (datetime) -- [REQUIRED]
    The end time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as yyyy-MM-dd\'T\'HH:mm:ss . For example, 2019-07-01T23:59:59 .
    
    Period (integer) -- [REQUIRED]
    The period, in seconds, to use for the statistics in the InsightRuleMetricDatapoint results.
    
    MaxContributorCount (integer) -- The maximum number of contributors to include in the report. The range is 1 to 100. If you omit this, the default of 10 is used.
    Metrics (list) -- Specifies which metrics to use for aggregation of contributor values for the report. You can specify one or more of the following metrics:
    
    UniqueContributors -- the number of unique contributors for each data point.
    MaxContributorValue -- the value of the top contributor for each data point. The identity of the contributor may change for each data point in the graph. If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the rule\'s Value , during that period.
    SampleCount -- the number of data points matched by the rule.
    Sum -- the sum of the values from all contributors during the time period represented by that data point.
    Minimum -- the minimum value from a single observation during the time period represented by that data point.
    Maximum -- the maximum value from a single observation during the time period represented by that data point.
    Average -- the average value from all contributors during the time period represented by that data point.
    
    
    (string) --
    
    
    OrderBy (string) -- Determines what statistic to use to rank the contributors. Valid values are SUM and MAXIMUM.
    
    """
    pass

def get_metric_data(MetricDataQueries=None, StartTime=None, EndTime=None, NextToken=None, ScanBy=None, MaxDatapoints=None):
    """
    You can use the GetMetricData API to retrieve as many as 500 different metrics in a single request, with a total of as many as 100,800 data points. You can also optionally perform math expressions on the values of the returned statistics, to create new time series that represent new insights into your data. For example, using Lambda metrics, you could divide the Errors metric by the Invocations metric to get an error rate time series. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
    Calls to the GetMetricData API have a different pricing structure than calls to GetMetricStatistics . For more information about pricing, see Amazon CloudWatch Pricing .
    Amazon CloudWatch retains metric data as follows:
    Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.
    If you omit Unit in your request, all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.
    See also: AWS API Documentation
    
    Exceptions
    
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
                'ReturnData': True|False,
                'Period': 123
            },
        ],
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        NextToken='string',
        ScanBy='TimestampDescending'|'TimestampAscending',
        MaxDatapoints=123
    )
    
    
    :type MetricDataQueries: list
    :param MetricDataQueries: [REQUIRED]\nThe metric queries to be returned. A single GetMetricData call can include as many as 500 MetricDataQuery structures. Each of these structures can specify either a metric to retrieve, or a math expression to perform on retrieved data.\n\n(dict) --This structure is used in both GetMetricData and PutMetricAlarm . The supported use of this structure is different for those two operations.\nWhen used in GetMetricData , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single GetMetricData call can include up to 500 MetricDataQuery structures.\nWhen used in PutMetricAlarm , it enables you to create an alarm based on a metric math expression. Each MetricDataQuery in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single PutMetricAlarm call can include up to 20 MetricDataQuery structures in the array. The 20 structures can include as many as 10 structures that contain a MetricStat parameter to retrieve a metric, and as many as 10 structures that contain the Expression parameter to perform a math expression. Of those Expression structures, one must have True as the value for ReturnData . The result of this expression is the value the alarm watches.\nAny expression used in a PutMetricAlarm operation must return a single time series. For more information, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .\nSome of the parameters of this structure also have different uses whether you are using this structure in a GetMetricData operation or a PutMetricAlarm operation. These differences are explained in the following parameter list.\n\nId (string) -- [REQUIRED]A short name used to tie this object to the results in the response. This name must be unique within a single call to GetMetricData . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.\n\nMetricStat (dict) --The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.\nWithin one MetricDataQuery object, you must specify either Expression or MetricStat but not both.\n\nMetric (dict) -- [REQUIRED]The metric to return, including the metric name, namespace, and dimensions.\n\nNamespace (string) --The namespace of the metric.\n\nMetricName (string) --The name of the metric. This is a required field.\n\nDimensions (list) --The dimensions for the metric.\n\n(dict) --Expands the identity of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value representing the dimension measurement.\n\n\n\n\n\n\n\nPeriod (integer) -- [REQUIRED]The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second.\nIf the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:\n\nStart time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).\nStart time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).\nStart time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).\n\n\nStat (string) -- [REQUIRED]The statistic to return. It can include any CloudWatch statistic or extended statistic.\n\nUnit (string) --When you are using a Put operation, this defines what unit you want to use when storing the metric.\nIn a Get operation, if you omit Unit then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.\n\n\n\nExpression (string) --The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the Id of the other metrics to refer to those metrics, and can also use the Id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .\nWithin each MetricDataQuery object, you must specify either Expression or MetricStat but not both.\n\nLabel (string) --A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.\n\nReturnData (boolean) --When used in GetMetricData , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify False . If you omit this, the default of True is used.\nWhen used in PutMetricAlarm , specify True for the one expression result to use as the alarm. For all other metrics and expressions in the same PutMetricAlarm operation, specify ReturnData as False.\n\nPeriod (integer) --The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData operation that includes a StorageResolution of 1 second .\n\n\n\n\n

    :type StartTime: datetime
    :param StartTime: [REQUIRED]\nThe time stamp indicating the earliest data to be returned.\nThe value specified is inclusive; results include data points with the specified time stamp.\nCloudWatch rounds the specified time stamp as follows:\n\nStart time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.\nStart time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.\nStart time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.\n\nIf you set Period to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15.\nFor better performance, specify StartTime and EndTime values that align with the value of the metric\'s Period and sync up with the beginning and end of an hour. For example, if the Period of a metric is 5 minutes, specifying 12:05 or 12:30 as StartTime can get a faster response from CloudWatch than setting 12:07 or 12:29 as the StartTime .\n

    :type EndTime: datetime
    :param EndTime: [REQUIRED]\nThe time stamp indicating the latest data to be returned.\nThe value specified is exclusive; results include data points up to the specified time stamp.\nFor better performance, specify StartTime and EndTime values that align with the value of the metric\'s Period and sync up with the beginning and end of an hour. For example, if the Period of a metric is 5 minutes, specifying 12:05 or 12:30 as EndTime can get a faster response from CloudWatch than setting 12:07 or 12:29 as the EndTime .\n

    :type NextToken: string
    :param NextToken: Include this value, if it was returned by the previous call, to get the next set of data points.

    :type ScanBy: string
    :param ScanBy: The order in which data points should be returned. TimestampDescending returns the newest data first and paginates when the MaxDatapoints limit is reached. TimestampAscending returns the oldest data first and paginates when the MaxDatapoints limit is reached.

    :type MaxDatapoints: integer
    :param MaxDatapoints: The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used.

    :rtype: dict

ReturnsResponse Syntax
{
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
    'NextToken': 'string',
    'Messages': [
        {
            'Code': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

MetricDataResults (list) --
The metrics that are returned, including the metric name, namespace, and dimensions.

(dict) --
A GetMetricData call returns an array of MetricDataResult structures. Each of these structures includes the data points for that metric, along with the timestamps of those data points and other identifying information.

Id (string) --
The short name you specified to represent this metric.

Label (string) --
The human-readable label associated with the data.

Timestamps (list) --
The timestamps for the data points, formatted in Unix timestamp format. The number of timestamps always matches the number of values and the value for Timestamps[x] is Values[x].

(datetime) --


Values (list) --
The data points for the metric corresponding to Timestamps . The number of values always matches the number of timestamps and the timestamp for Values[x] is Timestamps[x].

(float) --


StatusCode (string) --
The status of the returned data. Complete indicates that all data points in the requested time range were returned. PartialData means that an incomplete set of data points were returned. You can use the NextToken value that was returned and repeat your request to get more data points. NextToken is not returned if you are performing a math expression. InternalError indicates that an error occurred. Retry your request using NextToken , if present.

Messages (list) --
A list of messages with additional information about the data returned.

(dict) --
A message returned by the GetMetricData API, including a code and a description.

Code (string) --
The error code or status code associated with the message.

Value (string) --
The message text.









NextToken (string) --
A token that marks the next batch of returned results.

Messages (list) --
Contains a message about this GetMetricData operation, if the operation results in such a message. An example of a message that may be returned is Maximum number of allowed metrics exceeded . If there is a message, as much of the operation as possible is still executed.
A message appears here only if it is related to the global GetMetricData operation. Any message about a specific metric returned by the operation appears in the MetricDataResult object returned for that metric.

(dict) --
A message returned by the GetMetricData API, including a code and a description.

Code (string) --
The error code or status code associated with the message.

Value (string) --
The message text.











Exceptions

CloudWatch.Client.exceptions.InvalidNextToken


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
        'NextToken': 'string',
        'Messages': [
            {
                'Code': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    MetricDataQueries (list) -- [REQUIRED]
    The metric queries to be returned. A single GetMetricData call can include as many as 500 MetricDataQuery structures. Each of these structures can specify either a metric to retrieve, or a math expression to perform on retrieved data.
    
    (dict) --This structure is used in both GetMetricData and PutMetricAlarm . The supported use of this structure is different for those two operations.
    When used in GetMetricData , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single GetMetricData call can include up to 500 MetricDataQuery structures.
    When used in PutMetricAlarm , it enables you to create an alarm based on a metric math expression. Each MetricDataQuery in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single PutMetricAlarm call can include up to 20 MetricDataQuery structures in the array. The 20 structures can include as many as 10 structures that contain a MetricStat parameter to retrieve a metric, and as many as 10 structures that contain the Expression parameter to perform a math expression. Of those Expression structures, one must have True as the value for ReturnData . The result of this expression is the value the alarm watches.
    Any expression used in a PutMetricAlarm operation must return a single time series. For more information, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
    Some of the parameters of this structure also have different uses whether you are using this structure in a GetMetricData operation or a PutMetricAlarm operation. These differences are explained in the following parameter list.
    
    Id (string) -- [REQUIRED]A short name used to tie this object to the results in the response. This name must be unique within a single call to GetMetricData . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
    
    MetricStat (dict) --The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
    Within one MetricDataQuery object, you must specify either Expression or MetricStat but not both.
    
    Metric (dict) -- [REQUIRED]The metric to return, including the metric name, namespace, and dimensions.
    
    Namespace (string) --The namespace of the metric.
    
    MetricName (string) --The name of the metric. This is a required field.
    
    Dimensions (list) --The dimensions for the metric.
    
    (dict) --Expands the identity of a metric.
    
    Name (string) -- [REQUIRED]The name of the dimension.
    
    Value (string) -- [REQUIRED]The value representing the dimension measurement.
    
    
    
    
    
    
    
    Period (integer) -- [REQUIRED]The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second.
    If the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:
    
    Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
    Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
    Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
    
    
    Stat (string) -- [REQUIRED]The statistic to return. It can include any CloudWatch statistic or extended statistic.
    
    Unit (string) --When you are using a Put operation, this defines what unit you want to use when storing the metric.
    In a Get operation, if you omit Unit then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.
    
    
    
    Expression (string) --The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the Id of the other metrics to refer to those metrics, and can also use the Id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
    Within each MetricDataQuery object, you must specify either Expression or MetricStat but not both.
    
    Label (string) --A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.
    
    ReturnData (boolean) --When used in GetMetricData , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify False . If you omit this, the default of True is used.
    When used in PutMetricAlarm , specify True for the one expression result to use as the alarm. For all other metrics and expressions in the same PutMetricAlarm operation, specify ReturnData as False.
    
    Period (integer) --The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData operation that includes a StorageResolution of 1 second .
    
    
    
    
    
    StartTime (datetime) -- [REQUIRED]
    The time stamp indicating the earliest data to be returned.
    The value specified is inclusive; results include data points with the specified time stamp.
    CloudWatch rounds the specified time stamp as follows:
    
    Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.
    Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.
    Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.
    
    If you set Period to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15.
    For better performance, specify StartTime and EndTime values that align with the value of the metric\'s Period and sync up with the beginning and end of an hour. For example, if the Period of a metric is 5 minutes, specifying 12:05 or 12:30 as StartTime can get a faster response from CloudWatch than setting 12:07 or 12:29 as the StartTime .
    
    EndTime (datetime) -- [REQUIRED]
    The time stamp indicating the latest data to be returned.
    The value specified is exclusive; results include data points up to the specified time stamp.
    For better performance, specify StartTime and EndTime values that align with the value of the metric\'s Period and sync up with the beginning and end of an hour. For example, if the Period of a metric is 5 minutes, specifying 12:05 or 12:30 as EndTime can get a faster response from CloudWatch than setting 12:07 or 12:29 as the EndTime .
    
    NextToken (string) -- Include this value, if it was returned by the previous call, to get the next set of data points.
    ScanBy (string) -- The order in which data points should be returned. TimestampDescending returns the newest data first and paginates when the MaxDatapoints limit is reached. TimestampAscending returns the oldest data first and paginates when the MaxDatapoints limit is reached.
    MaxDatapoints (integer) -- The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used.
    
    """
    pass

def get_metric_statistics(Namespace=None, MetricName=None, Dimensions=None, StartTime=None, EndTime=None, Period=None, Statistics=None, ExtendedStatistics=None, Unit=None):
    """
    Gets statistics for the specified metric.
    The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. Data points are not returned in chronological order.
    CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned.
    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:
    Percentile statistics are not available for metrics when any of the metric values are negative numbers.
    Amazon CloudWatch retains metric data as follows:
    Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.
    CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.
    For information about metrics and dimensions supported by AWS services, see the Amazon CloudWatch Metrics and Dimensions Reference in the Amazon CloudWatch User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Namespace: [REQUIRED]\nThe namespace of the metric, with or without spaces.\n

    :type MetricName: string
    :param MetricName: [REQUIRED]\nThe name of the metric, with or without spaces.\n

    :type Dimensions: list
    :param Dimensions: The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a specific combination of dimensions was not published, you can\'t retrieve statistics for it. You must specify the same dimensions that were used when the metrics were created. For an example, see Dimension Combinations in the Amazon CloudWatch User Guide . For more information about specifying dimensions, see Publishing Metrics in the Amazon CloudWatch User Guide .\n\n(dict) --Expands the identity of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value representing the dimension measurement.\n\n\n\n\n

    :type StartTime: datetime
    :param StartTime: [REQUIRED]\nThe time stamp that determines the first data point to return. Start times are evaluated relative to the time that CloudWatch receives the request.\nThe value specified is inclusive; results include data points with the specified time stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).\nCloudWatch rounds the specified time stamp as follows:\n\nStart time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.\nStart time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.\nStart time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.\n\nIf you set Period to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15.\n

    :type EndTime: datetime
    :param EndTime: [REQUIRED]\nThe time stamp that determines the last data point to return.\nThe value specified is exclusive; results include data points up to the specified time stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).\n

    :type Period: integer
    :param Period: [REQUIRED]\nThe granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second.\nIf the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:\n\nStart time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).\nStart time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).\nStart time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).\n\n

    :type Statistics: list
    :param Statistics: The metric statistics, other than percentile. For percentile statistics, use ExtendedStatistics . When calling GetMetricStatistics , you must specify either Statistics or ExtendedStatistics , but not both.\n\n(string) --\n\n

    :type ExtendedStatistics: list
    :param ExtendedStatistics: The percentile statistics. Specify values between p0.0 and p100. When calling GetMetricStatistics , you must specify either Statistics or ExtendedStatistics , but not both. Percentile statistics are not available for metrics when any of the metric values are negative numbers.\n\n(string) --\n\n

    :type Unit: string
    :param Unit: The unit for a given metric. If you omit Unit , all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Label (string) --
A label for the specified metric.

Datapoints (list) --
The data points for the specified metric.

(dict) --
Encapsulates the statistical data that CloudWatch computes from metric data.

Timestamp (datetime) --
The time stamp used for the data point.

SampleCount (float) --
The number of metric values that contributed to the aggregate value of this data point.

Average (float) --
The average of the metric values that correspond to the data point.

Sum (float) --
The sum of the metric values for the data point.

Minimum (float) --
The minimum metric value for the data point.

Maximum (float) --
The maximum metric value for the data point.

Unit (string) --
The standard unit for the data point.

ExtendedStatistics (dict) --
The percentile statistic for the data point.

(string) --
(float) --














Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.MissingRequiredParameterException
CloudWatch.Client.exceptions.InvalidParameterCombinationException
CloudWatch.Client.exceptions.InternalServiceFault


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

def get_metric_widget_image(MetricWidget=None, OutputFormat=None):
    """
    You can use the GetMetricWidgetImage API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image. You can then embed this image into your services and products, such as wiki pages, reports, and documents. You could also retrieve images regularly, such as every minute, and create your own custom live dashboard.
    The graph you retrieve can include all CloudWatch metric graph features, including metric math and horizontal and vertical annotations.
    There is a limit of 20 transactions per second for this API. Each GetMetricWidgetImage action has the following limits:
    See also: AWS API Documentation
    
    
    :example: response = client.get_metric_widget_image(
        MetricWidget='string',
        OutputFormat='string'
    )
    
    
    :type MetricWidget: string
    :param MetricWidget: [REQUIRED]\nA JSON string that defines the bitmap graph to be retrieved. The string includes the metrics to include in the graph, statistics, annotations, title, axis limits, and so on. You can include only one MetricWidget parameter in each GetMetricWidgetImage call.\nFor more information about the syntax of MetricWidget see GetMetricWidgetImage: Metric Widget Structure and Syntax .\nIf any metric on the graph could not load all the requested data points, an orange triangle with an exclamation point appears next to the graph legend.\n

    :type OutputFormat: string
    :param OutputFormat: The format of the resulting image. Only PNG images are supported.\nThe default is png . If you specify png , the API returns an HTTP response with the content-type set to text/xml . The image data is in a MetricWidgetImage field. For example:\n\n<GetMetricWidgetImageResponse xmlns=<URLstring>><GetMetricWidgetImageResult>\n<MetricWidgetImage>\niVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip...\n</MetricWidgetImage>\n</GetMetricWidgetImageResult>\n<ResponseMetadata>\n<RequestId>6f0d4192-4d42-11e8-82c1-f539a07e0e3b</RequestId>\n</ResponseMetadata>\n</GetMetricWidgetImageResponse>\n\nThe image/png setting is intended only for custom HTTP requests. For most use cases, and all actions using an AWS SDK, you should use png . If you specify image/png , the HTTP response has a content-type set to image/png , and the body of the response is a PNG image.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'MetricWidgetImage': b'bytes'
}


Response Structure

(dict) --

MetricWidgetImage (bytes) --
The image of the graph, in the output format specified.








    :return: {
        'MetricWidgetImage': b'bytes'
    }
    
    
    :returns: 
    MetricWidget (string) -- [REQUIRED]
    A JSON string that defines the bitmap graph to be retrieved. The string includes the metrics to include in the graph, statistics, annotations, title, axis limits, and so on. You can include only one MetricWidget parameter in each GetMetricWidgetImage call.
    For more information about the syntax of MetricWidget see GetMetricWidgetImage: Metric Widget Structure and Syntax .
    If any metric on the graph could not load all the requested data points, an orange triangle with an exclamation point appears next to the graph legend.
    
    OutputFormat (string) -- The format of the resulting image. Only PNG images are supported.
    The default is png . If you specify png , the API returns an HTTP response with the content-type set to text/xml . The image data is in a MetricWidgetImage field. For example:
    
    <GetMetricWidgetImageResponse xmlns=<URLstring>><GetMetricWidgetImageResult>
    <MetricWidgetImage>
    iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip...
    </MetricWidgetImage>
    </GetMetricWidgetImageResult>
    <ResponseMetadata>
    <RequestId>6f0d4192-4d42-11e8-82c1-f539a07e0e3b</RequestId>
    </ResponseMetadata>
    </GetMetricWidgetImageResponse>
    
    The image/png setting is intended only for custom HTTP requests. For most use cases, and all actions using an AWS SDK, you should use png . If you specify image/png , the HTTP response has a content-type set to image/png , and the body of the response is a PNG image.
    
    
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

def list_dashboards(DashboardNamePrefix=None, NextToken=None):
    """
    Returns a list of the dashboards for your account. If you include DashboardNamePrefix , only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_dashboards(
        DashboardNamePrefix='string',
        NextToken='string'
    )
    
    
    :type DashboardNamePrefix: string
    :param DashboardNamePrefix: If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, '.', '-', and '_'.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

DashboardEntries (list) --
The list of matching dashboards.

(dict) --
Represents a specific dashboard.

DashboardName (string) --
The name of the dashboard.

DashboardArn (string) --
The Amazon Resource Name (ARN) of the dashboard.

LastModified (datetime) --
The time stamp of when the dashboard was last modified, either by an API call or through the console. This number is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.

Size (integer) --
The size of the dashboard, in bytes.





NextToken (string) --
The token that marks the start of the next batch of returned results.







Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.InternalServiceFault


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
    
    
    :returns: 
    CloudWatch.Client.exceptions.InvalidParameterValueException
    CloudWatch.Client.exceptions.InternalServiceFault
    
    """
    pass

def list_metrics(Namespace=None, MetricName=None, Dimensions=None, NextToken=None):
    """
    List the specified metrics. You can use the returned metrics with GetMetricData or GetMetricStatistics to obtain statistical data.
    Up to 500 results are returned for any one call. To retrieve additional results, use the returned token with subsequent calls.
    After you create a metric, allow up to fifteen minutes before the metric appears. Statistics about the metric, however, are available sooner using GetMetricData or GetMetricStatistics .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Dimensions: The dimensions to filter against.\n\n(dict) --Represents filters for a dimension.\n\nName (string) -- [REQUIRED]The dimension name to be matched.\n\nValue (string) --The value of the dimension to be matched.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Metrics (list) --
The metrics.

(dict) --
Represents a specific metric.

Namespace (string) --
The namespace of the metric.

MetricName (string) --
The name of the metric. This is a required field.

Dimensions (list) --
The dimensions for the metric.

(dict) --
Expands the identity of a metric.

Name (string) --
The name of the dimension.

Value (string) --
The value representing the dimension measurement.









NextToken (string) --
The token that marks the start of the next batch of returned results.







Exceptions

CloudWatch.Client.exceptions.InternalServiceFault
CloudWatch.Client.exceptions.InvalidParameterValueException


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
    
    
    :returns: 
    CloudWatch.Client.exceptions.InternalServiceFault
    CloudWatch.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def list_tags_for_resource(ResourceARN=None):
    """
    Displays the tags associated with a CloudWatch resource. Currently, alarms and Contributor Insights rules support tagging.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe ARN of the CloudWatch resource that you want to view tags for.\nThe ARN format of an alarm is ``arn:aws:cloudwatch:Region :account-id :alarm:alarm-name ``\nThe ARN format of a Contributor Insights rule is ``arn:aws:cloudwatch:Region :account-id :insight-rule:insight-rule-name ``\nFor more information on ARN format, see Resource Types Defined by Amazon CloudWatch in the Amazon Web Services General Reference .\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Tags (list) --The list of tag keys and values associated with the resource you specified.

(dict) --A key-value pair associated with a CloudWatch resource.

Key (string) --A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.

Value (string) --The value for the specified tag key.










Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.ResourceNotFoundException
CloudWatch.Client.exceptions.InternalServiceFault


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def put_anomaly_detector(Namespace=None, MetricName=None, Dimensions=None, Stat=None, Configuration=None):
    """
    Creates an anomaly detection model for a CloudWatch metric. You can use the model to display a band of expected normal values when the metric is graphed.
    For more information, see CloudWatch Anomaly Detection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_anomaly_detector(
        Namespace='string',
        MetricName='string',
        Dimensions=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        Stat='string',
        Configuration={
            'ExcludedTimeRanges': [
                {
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1)
                },
            ],
            'MetricTimezone': 'string'
        }
    )
    
    
    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace of the metric to create the anomaly detection model for.\n

    :type MetricName: string
    :param MetricName: [REQUIRED]\nThe name of the metric to create the anomaly detection model for.\n

    :type Dimensions: list
    :param Dimensions: The metric dimensions to create the anomaly detection model for.\n\n(dict) --Expands the identity of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value representing the dimension measurement.\n\n\n\n\n

    :type Stat: string
    :param Stat: [REQUIRED]\nThe statistic to use for the metric and the anomaly detection model.\n

    :type Configuration: dict
    :param Configuration: The configuration specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model. You can specify as many as 10 time ranges.\nThe configuration can also include the time zone to use for the metric.\nYou can in\n\nExcludedTimeRanges (list) --An array of time ranges to exclude from use when the anomaly detection model is trained. Use this to make sure that events that could cause unusual values for the metric, such as deployments, aren\'t used when CloudWatch creates the model.\n\n(dict) --Specifies one range of days or times to exclude from use for training an anomaly detection model.\n\nStartTime (datetime) -- [REQUIRED]The start time of the range to exclude. The format is yyyy-MM-dd\'T\'HH:mm:ss . For example, 2019-07-01T23:59:59 .\n\nEndTime (datetime) -- [REQUIRED]The end time of the range to exclude. The format is yyyy-MM-dd\'T\'HH:mm:ss . For example, 2019-07-01T23:59:59 .\n\n\n\n\n\nMetricTimezone (string) --The time zone to use for the metric. This is useful to enable the model to automatically account for daylight savings time changes if the metric is sensitive to such time changes.\nTo specify a time zone, use the name of the time zone as specified in the standard tz database. For more information, see tz database .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudWatch.Client.exceptions.LimitExceededException
CloudWatch.Client.exceptions.InternalServiceFault
CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.MissingRequiredParameterException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_composite_alarm(ActionsEnabled=None, AlarmActions=None, AlarmDescription=None, AlarmName=None, AlarmRule=None, InsufficientDataActions=None, OKActions=None, Tags=None):
    """
    Creates or updates a composite alarm . When you create a composite alarm, you specify a rule expression for the alarm that takes into account the alarm states of other alarms that you have created. The composite alarm goes into ALARM state only if all conditions of the rule are met.
    The alarms specified in a composite alarm\'s rule expression can include metric alarms and other composite alarms.
    Using composite alarms can reduce alarm noise. You can create multiple metric alarms, and also create a composite alarm and set up alerts only for the composite alarm. For example, you could create a composite alarm that goes into ALARM state only when more than one of the underlying metric alarms are in ALARM state.
    Currently, the only alarm actions that can be taken by composite alarms are notifying SNS topics.
    When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA . The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed. For a composite alarm, this initial time after creation is the only time that the alarm can be in INSUFFICIENT_DATA state.
    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_composite_alarm(
        ActionsEnabled=True|False,
        AlarmActions=[
            'string',
        ],
        AlarmDescription='string',
        AlarmName='string',
        AlarmRule='string',
        InsufficientDataActions=[
            'string',
        ],
        OKActions=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ActionsEnabled: boolean
    :param ActionsEnabled: Indicates whether actions should be executed during any changes to the alarm state of the composite alarm. The default is TRUE .

    :type AlarmActions: list
    :param AlarmActions: The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).\nValid Values: ``arn:aws:sns:region :account-id :sns-topic-name ``\n\n(string) --\n\n

    :type AlarmDescription: string
    :param AlarmDescription: The description for the composite alarm.

    :type AlarmName: string
    :param AlarmName: [REQUIRED]\nThe name for the composite alarm. This name must be unique within your AWS account.\n

    :type AlarmRule: string
    :param AlarmRule: [REQUIRED]\nAn expression that specifies which other alarms are to be evaluated to determine this composite alarm\'s state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression.\nYou can use either alarm names or ARNs to reference the other alarms that are to be evaluated.\nFunctions can include the following:\n\nALARM('*alarm-name* or *alarm-ARN* ') is TRUE if the named alarm is in ALARM state.\nOK('*alarm-name* or *alarm-ARN* ') is TRUE if the named alarm is in OK state.\nINSUFFICIENT_DATA('*alarm-name* or *alarm-ARN* ') is TRUE if the named alarm is in INSUFFICIENT_DATA state.\nTRUE always evaluates to TRUE.\nFALSE always evaluates to FALSE.\n\nTRUE and FALSE are useful for testing a complex AlarmRule structure, and for testing your alarm actions.\nAlarm names specified in AlarmRule can be surrounded with double-quotes ('), but do not have to be.\nThe following are some examples of AlarmRule :\n\nALARM(CPUUtilizationTooHigh) AND ALARM(DiskReadOpsTooHigh) specifies that the composite alarm goes into ALARM state only if both CPUUtilizationTooHigh and DiskReadOpsTooHigh alarms are in ALARM state.\nALARM(CPUUtilizationTooHigh) AND NOT ALARM(DeploymentInProgress) specifies that the alarm goes to ALARM state if CPUUtilizationTooHigh is in ALARM state and DeploymentInProgress is not in ALARM state. This example reduces alarm noise during a known deployment window.\n(ALARM(CPUUtilizationTooHigh) OR ALARM(DiskReadOpsTooHigh)) AND OK(NetworkOutTooHigh) goes into ALARM state if CPUUtilizationTooHigh OR DiskReadOpsTooHigh is in ALARM state, and if NetworkOutTooHigh is in OK state. This provides another example of using a composite alarm to prevent noise. This rule ensures that you are not notified with an alarm action on high CPU or disk usage if a known network problem is also occurring.\n\nThe AlarmRule can specify as many as 100 'children' alarms. The AlarmRule expression can have as many as 500 elements. Elements are child alarms, TRUE or FALSE statements, and parentheses.\n

    :type InsufficientDataActions: list
    :param InsufficientDataActions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).\nValid Values: ``arn:aws:sns:region :account-id :sns-topic-name ``\n\n(string) --\n\n

    :type OKActions: list
    :param OKActions: The actions to execute when this alarm transitions to an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).\nValid Values: ``arn:aws:sns:region :account-id :sns-topic-name ``\n\n(string) --\n\n

    :type Tags: list
    :param Tags: A list of key-value pairs to associate with the composite alarm. You can associate as many as 50 tags with an alarm.\nTags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.\n\n(dict) --A key-value pair associated with a CloudWatch resource.\n\nKey (string) -- [REQUIRED]A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.\n\nValue (string) -- [REQUIRED]The value for the specified tag key.\n\n\n\n\n

    :returns: 
    CloudWatch.Client.exceptions.LimitExceededFault
    
    """
    pass

def put_dashboard(DashboardName=None, DashboardBody=None):
    """
    Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a dashboard, the entire contents are replaced with what you specify here.
    All dashboards in your account are global, not region-specific.
    A simple way to create a dashboard using PutDashboard is to copy an existing dashboard. To copy an existing dashboard using the console, you can load the dashboard and then use the View/edit source command in the Actions menu to display the JSON block for that dashboard. Another way to copy a dashboard is to use GetDashboard , and then use the data returned within DashboardBody as the template for the new dashboard when you call PutDashboard .
    When you create a dashboard with PutDashboard , a good practice is to add a text widget at the top of the dashboard with a message that the dashboard was created by script and should not be changed in the console. This message could also point console users to the location of the DashboardBody script or the CloudFormation template used to create the dashboard.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_dashboard(
        DashboardName='string',
        DashboardBody='string'
    )
    
    
    :type DashboardName: string
    :param DashboardName: [REQUIRED]\nThe name of the dashboard. If a dashboard with this name already exists, this call modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, '-', and '_'. This parameter is required.\n

    :type DashboardBody: string
    :param DashboardBody: [REQUIRED]\nThe detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required.\nFor more information about the syntax, see Dashboard Body Structure and Syntax .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DashboardValidationMessages': [
        {
            'DataPath': 'string',
            'Message': 'string'
        },
    ]
}


Response Structure

(dict) --

DashboardValidationMessages (list) --
If the input for PutDashboard was correct and the dashboard was successfully created or modified, this result is empty.
If this result includes only warning messages, then the input was valid enough for the dashboard to be created or modified, but some elements of the dashboard may not render.
If this result includes error messages, the input was not valid and the operation failed.

(dict) --
An error or warning for the operation.

DataPath (string) --
The data path related to the message.

Message (string) --
A message describing the error or warning.











Exceptions

CloudWatch.Client.exceptions.DashboardInvalidInputError
CloudWatch.Client.exceptions.InternalServiceFault


    :return: {
        'DashboardValidationMessages': [
            {
                'DataPath': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    :returns: 
    CloudWatch.Client.exceptions.DashboardInvalidInputError
    CloudWatch.Client.exceptions.InternalServiceFault
    
    """
    pass

def put_insight_rule(RuleName=None, RuleState=None, RuleDefinition=None, Tags=None):
    """
    Creates a Contributor Insights rule. Rules evaluate log events in a CloudWatch Logs log group, enabling you to find contributor data for the log events in that log group. For more information, see Using Contributor Insights to Analyze High-Cardinality Data .
    If you create a rule, delete it, and then re-create it with the same name, historical data from the first time the rule was created may or may not be available.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_insight_rule(
        RuleName='string',
        RuleState='string',
        RuleDefinition='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type RuleName: string
    :param RuleName: [REQUIRED]\nA unique name for the rule.\n

    :type RuleState: string
    :param RuleState: The state of the rule. Valid values are ENABLED and DISABLED.

    :type RuleDefinition: string
    :param RuleDefinition: [REQUIRED]\nThe definition of the rule, as a JSON object. For details on the valid syntax, see Contributor Insights Rule Syntax .\n

    :type Tags: list
    :param Tags: A list of key-value pairs to associate with the Contributor Insights rule. You can associate as many as 50 tags with a rule.\nTags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.\nTo be able to associate tags with a rule, you must have the cloudwatch:TagResource permission in addition to the cloudwatch:PutInsightRule permission.\nIf you are using this operation to update an existing Contributor Insights rule, any tags you specify in this parameter are ignored. To change the tags of an existing rule, use TagResource .\n\n(dict) --A key-value pair associated with a CloudWatch resource.\n\nKey (string) -- [REQUIRED]A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.\n\nValue (string) -- [REQUIRED]The value for the specified tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.MissingRequiredParameterException
CloudWatch.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_metric_alarm(AlarmName=None, AlarmDescription=None, ActionsEnabled=None, OKActions=None, AlarmActions=None, InsufficientDataActions=None, MetricName=None, Namespace=None, Statistic=None, ExtendedStatistic=None, Dimensions=None, Period=None, Unit=None, EvaluationPeriods=None, DatapointsToAlarm=None, Threshold=None, ComparisonOperator=None, TreatMissingData=None, EvaluateLowSampleCountPercentile=None, Metrics=None, Tags=None, ThresholdMetricId=None):
    """
    Creates or updates an alarm and associates it with the specified metric, metric math expression, or anomaly detection model.
    Alarms based on anomaly detection models cannot have Auto Scaling actions.
    When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA . The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.
    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.
    If you are an IAM user, you must have Amazon EC2 permissions for some alarm operations:
    If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can still create an alarm, but the stop or terminate actions are not performed. However, if you are later granted the required permissions, the alarm actions that you created earlier are performed.
    If you are using an IAM role (for example, an EC2 instance profile), you cannot stop or terminate the instance using alarm actions. However, you can still see the alarm state and perform any other actions such as Amazon SNS notifications or Auto Scaling policies.
    If you are using temporary security credentials granted using AWS STS, you cannot stop or terminate an EC2 instance using alarm actions.
    The first time you create an alarm in the AWS Management Console, the CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The service-linked role is called AWSServiceRoleForCloudWatchEvents . For more information, see AWS service-linked role .
    See also: AWS API Documentation
    
    Exceptions
    
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
        ComparisonOperator='GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'|'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
        TreatMissingData='string',
        EvaluateLowSampleCountPercentile='string',
        Metrics=[
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
                'ReturnData': True|False,
                'Period': 123
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        ThresholdMetricId='string'
    )
    
    
    :type AlarmName: string
    :param AlarmName: [REQUIRED]\nThe name for the alarm. This name must be unique within your AWS account.\n

    :type AlarmDescription: string
    :param AlarmDescription: The description for the alarm.

    :type ActionsEnabled: boolean
    :param ActionsEnabled: Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE .

    :type OKActions: list
    :param OKActions: The actions to execute when this alarm transitions to an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).\nValid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:automate:*region* :ec2:reboot | ``arn:aws:sns:region :account-id :sns-topic-name `` | ``arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id :autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name ``\nValid Values (for use with IAM roles): arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0\n\n(string) --\n\n

    :type AlarmActions: list
    :param AlarmActions: The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).\nValid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:automate:*region* :ec2:reboot | ``arn:aws:sns:region :account-id :sns-topic-name `` | ``arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id :autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name ``\nValid Values (for use with IAM roles): arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0\n\n(string) --\n\n

    :type InsufficientDataActions: list
    :param InsufficientDataActions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).\nValid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:automate:*region* :ec2:reboot | ``arn:aws:sns:region :account-id :sns-topic-name `` | ``arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id :autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name ``\nValid Values (for use with IAM roles): >arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0\n\n(string) --\n\n

    :type MetricName: string
    :param MetricName: The name for the metric associated with the alarm. For each PutMetricAlarm operation, you must specify either MetricName or a Metrics array.\nIf you are creating an alarm based on a math expression, you cannot specify this parameter, or any of the Dimensions , Period , Namespace , Statistic , or ExtendedStatistic parameters. Instead, you specify all this information in the Metrics array.\n

    :type Namespace: string
    :param Namespace: The namespace for the metric associated specified in MetricName .

    :type Statistic: string
    :param Statistic: The statistic for the metric specified in MetricName , other than percentile. For percentile statistics, use ExtendedStatistic . When you call PutMetricAlarm and specify a MetricName , you must specify either Statistic or ExtendedStatistic, but not both.

    :type ExtendedStatistic: string
    :param ExtendedStatistic: The percentile statistic for the metric specified in MetricName . Specify a value between p0.0 and p100. When you call PutMetricAlarm and specify a MetricName , you must specify either Statistic or ExtendedStatistic, but not both.

    :type Dimensions: list
    :param Dimensions: The dimensions for the metric specified in MetricName .\n\n(dict) --Expands the identity of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value representing the dimension measurement.\n\n\n\n\n

    :type Period: integer
    :param Period: The length, in seconds, used each time the metric specified in MetricName is evaluated. Valid values are 10, 30, and any multiple of 60.\n\nPeriod is required for alarms based on static thresholds. If you are creating an alarm based on a metric math expression, you specify the period for each metric within the objects in the Metrics array.\nBe sure to specify 10 or 30 only for metrics that are stored by a PutMetricData call with a StorageResolution of 1. If you specify a period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see Amazon CloudWatch Pricing .\nAn alarm\'s total current evaluation period can be no longer than one day, so Period multiplied by EvaluationPeriods cannot be more than 86,400 seconds.\n

    :type Unit: string
    :param Unit: The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.\nIf you don\'t specify Unit , CloudWatch retrieves all unit types that have been published for the metric and attempts to evaluate the alarm. Usually metrics are published with only one unit, so the alarm will work as intended.\nHowever, if the metric is published with multiple types of units and you don\'t specify a unit, the alarm\'s behavior is not defined and will behave un-predictably.\nWe recommend omitting Unit so that you don\'t inadvertently specify an incorrect unit that is not published for this metric. Doing so causes the alarm to be stuck in the INSUFFICIENT DATA state.\n

    :type EvaluationPeriods: integer
    :param EvaluationPeriods: [REQUIRED]\nThe number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an 'M out of N' alarm, this value is the N.\nAn alarm\'s total current evaluation period can be no longer than one day, so this number multiplied by Period cannot be more than 86,400 seconds.\n

    :type DatapointsToAlarm: integer
    :param DatapointsToAlarm: The number of data points that must be breaching to trigger the alarm. This is used only if you are setting an 'M out of N' alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide .

    :type Threshold: float
    :param Threshold: The value against which the specified statistic is compared.\nThis parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.\n

    :type ComparisonOperator: string
    :param ComparisonOperator: [REQUIRED]\nThe arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.\nThe values LessThanLowerOrGreaterThanUpperThreshold , LessThanLowerThreshold , and GreaterThanUpperThreshold are used only for alarms based on anomaly detection models.\n

    :type TreatMissingData: string
    :param TreatMissingData: Sets how this alarm is to handle missing data points. If TreatMissingData is omitted, the default behavior of missing is used. For more information, see Configuring How CloudWatch Alarms Treats Missing Data .\nValid Values: breaching | notBreaching | ignore | missing\n

    :type EvaluateLowSampleCountPercentile: string
    :param EvaluateLowSampleCountPercentile: Used only for alarms based on percentiles. If you specify ignore , the alarm state does not change during periods with too few data points to be statistically significant. If you specify evaluate or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see Percentile-Based CloudWatch Alarms and Low Data Samples .\nValid Values: evaluate | ignore\n

    :type Metrics: list
    :param Metrics: An array of MetricDataQuery structures that enable you to create an alarm based on the result of a metric math expression. For each PutMetricAlarm operation, you must specify either MetricName or a Metrics array.\nEach item in the Metrics array either retrieves a metric or performs a math expression.\nOne item in the Metrics array is the expression that the alarm watches. You designate this expression by setting ReturnValue to true for this object in the array. For more information, see MetricDataQuery .\nIf you use the Metrics parameter, you cannot include the MetricName , Dimensions , Period , Namespace , Statistic , or ExtendedStatistic parameters of PutMetricAlarm in the same operation. Instead, you retrieve the metrics you are using in your math expression as part of the Metrics array.\n\n(dict) --This structure is used in both GetMetricData and PutMetricAlarm . The supported use of this structure is different for those two operations.\nWhen used in GetMetricData , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single GetMetricData call can include up to 500 MetricDataQuery structures.\nWhen used in PutMetricAlarm , it enables you to create an alarm based on a metric math expression. Each MetricDataQuery in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single PutMetricAlarm call can include up to 20 MetricDataQuery structures in the array. The 20 structures can include as many as 10 structures that contain a MetricStat parameter to retrieve a metric, and as many as 10 structures that contain the Expression parameter to perform a math expression. Of those Expression structures, one must have True as the value for ReturnData . The result of this expression is the value the alarm watches.\nAny expression used in a PutMetricAlarm operation must return a single time series. For more information, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .\nSome of the parameters of this structure also have different uses whether you are using this structure in a GetMetricData operation or a PutMetricAlarm operation. These differences are explained in the following parameter list.\n\nId (string) -- [REQUIRED]A short name used to tie this object to the results in the response. This name must be unique within a single call to GetMetricData . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.\n\nMetricStat (dict) --The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.\nWithin one MetricDataQuery object, you must specify either Expression or MetricStat but not both.\n\nMetric (dict) -- [REQUIRED]The metric to return, including the metric name, namespace, and dimensions.\n\nNamespace (string) --The namespace of the metric.\n\nMetricName (string) --The name of the metric. This is a required field.\n\nDimensions (list) --The dimensions for the metric.\n\n(dict) --Expands the identity of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value representing the dimension measurement.\n\n\n\n\n\n\n\nPeriod (integer) -- [REQUIRED]The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second.\nIf the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:\n\nStart time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).\nStart time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).\nStart time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).\n\n\nStat (string) -- [REQUIRED]The statistic to return. It can include any CloudWatch statistic or extended statistic.\n\nUnit (string) --When you are using a Put operation, this defines what unit you want to use when storing the metric.\nIn a Get operation, if you omit Unit then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.\n\n\n\nExpression (string) --The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the Id of the other metrics to refer to those metrics, and can also use the Id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .\nWithin each MetricDataQuery object, you must specify either Expression or MetricStat but not both.\n\nLabel (string) --A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.\n\nReturnData (boolean) --When used in GetMetricData , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify False . If you omit this, the default of True is used.\nWhen used in PutMetricAlarm , specify True for the one expression result to use as the alarm. For all other metrics and expressions in the same PutMetricAlarm operation, specify ReturnData as False.\n\nPeriod (integer) --The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData operation that includes a StorageResolution of 1 second .\n\n\n\n\n

    :type Tags: list
    :param Tags: A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm.\nTags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.\n\n(dict) --A key-value pair associated with a CloudWatch resource.\n\nKey (string) -- [REQUIRED]A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.\n\nValue (string) -- [REQUIRED]The value for the specified tag key.\n\n\n\n\n

    :type ThresholdMetricId: string
    :param ThresholdMetricId: If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.\nFor an example of how to use this parameter, see the Anomaly Detection Model Alarm example on this page.\nIf your alarm uses this parameter, it cannot have Auto Scaling actions.\n

    :returns: 
    AlarmName (string) -- [REQUIRED]
    The name for the alarm. This name must be unique within your AWS account.
    
    AlarmDescription (string) -- The description for the alarm.
    ActionsEnabled (boolean) -- Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE .
    OKActions (list) -- The actions to execute when this alarm transitions to an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:automate:*region* :ec2:reboot | ``arn:aws:sns:region :account-id :sns-topic-name `` | ``arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id :autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name ``
    Valid Values (for use with IAM roles): arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    (string) --
    
    
    AlarmActions (list) -- The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:automate:*region* :ec2:reboot | ``arn:aws:sns:region :account-id :sns-topic-name `` | ``arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id :autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name ``
    Valid Values (for use with IAM roles): arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    (string) --
    
    
    InsufficientDataActions (list) -- The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
    Valid Values: arn:aws:automate:*region* :ec2:stop | arn:aws:automate:*region* :ec2:terminate | arn:aws:automate:*region* :ec2:recover | arn:aws:automate:*region* :ec2:reboot | ``arn:aws:sns:region :account-id :sns-topic-name `` | ``arn:aws:autoscaling:region :account-id :scalingPolicy:policy-id :autoScalingGroupName/group-friendly-name :policyName/policy-friendly-name ``
    Valid Values (for use with IAM roles): >arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:*region* :*account-id* :action/actions/AWS_EC2.InstanceId.Reboot/1.0
    
    (string) --
    
    
    MetricName (string) -- The name for the metric associated with the alarm. For each PutMetricAlarm operation, you must specify either MetricName or a Metrics array.
    If you are creating an alarm based on a math expression, you cannot specify this parameter, or any of the Dimensions , Period , Namespace , Statistic , or ExtendedStatistic parameters. Instead, you specify all this information in the Metrics array.
    
    Namespace (string) -- The namespace for the metric associated specified in MetricName .
    Statistic (string) -- The statistic for the metric specified in MetricName , other than percentile. For percentile statistics, use ExtendedStatistic . When you call PutMetricAlarm and specify a MetricName , you must specify either Statistic or ExtendedStatistic, but not both.
    ExtendedStatistic (string) -- The percentile statistic for the metric specified in MetricName . Specify a value between p0.0 and p100. When you call PutMetricAlarm and specify a MetricName , you must specify either Statistic or ExtendedStatistic, but not both.
    Dimensions (list) -- The dimensions for the metric specified in MetricName .
    
    (dict) --Expands the identity of a metric.
    
    Name (string) -- [REQUIRED]The name of the dimension.
    
    Value (string) -- [REQUIRED]The value representing the dimension measurement.
    
    
    
    
    
    Period (integer) -- The length, in seconds, used each time the metric specified in MetricName is evaluated. Valid values are 10, 30, and any multiple of 60.
    
    Period is required for alarms based on static thresholds. If you are creating an alarm based on a metric math expression, you specify the period for each metric within the objects in the Metrics array.
    Be sure to specify 10 or 30 only for metrics that are stored by a PutMetricData call with a StorageResolution of 1. If you specify a period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see Amazon CloudWatch Pricing .
    An alarm\'s total current evaluation period can be no longer than one day, so Period multiplied by EvaluationPeriods cannot be more than 86,400 seconds.
    
    Unit (string) -- The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.
    If you don\'t specify Unit , CloudWatch retrieves all unit types that have been published for the metric and attempts to evaluate the alarm. Usually metrics are published with only one unit, so the alarm will work as intended.
    However, if the metric is published with multiple types of units and you don\'t specify a unit, the alarm\'s behavior is not defined and will behave un-predictably.
    We recommend omitting Unit so that you don\'t inadvertently specify an incorrect unit that is not published for this metric. Doing so causes the alarm to be stuck in the INSUFFICIENT DATA state.
    
    EvaluationPeriods (integer) -- [REQUIRED]
    The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N.
    An alarm\'s total current evaluation period can be no longer than one day, so this number multiplied by Period cannot be more than 86,400 seconds.
    
    DatapointsToAlarm (integer) -- The number of data points that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide .
    Threshold (float) -- The value against which the specified statistic is compared.
    This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.
    
    ComparisonOperator (string) -- [REQUIRED]
    The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
    The values LessThanLowerOrGreaterThanUpperThreshold , LessThanLowerThreshold , and GreaterThanUpperThreshold are used only for alarms based on anomaly detection models.
    
    TreatMissingData (string) -- Sets how this alarm is to handle missing data points. If TreatMissingData is omitted, the default behavior of missing is used. For more information, see Configuring How CloudWatch Alarms Treats Missing Data .
    Valid Values: breaching | notBreaching | ignore | missing
    
    EvaluateLowSampleCountPercentile (string) -- Used only for alarms based on percentiles. If you specify ignore , the alarm state does not change during periods with too few data points to be statistically significant. If you specify evaluate or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see Percentile-Based CloudWatch Alarms and Low Data Samples .
    Valid Values: evaluate | ignore
    
    Metrics (list) -- An array of MetricDataQuery structures that enable you to create an alarm based on the result of a metric math expression. For each PutMetricAlarm operation, you must specify either MetricName or a Metrics array.
    Each item in the Metrics array either retrieves a metric or performs a math expression.
    One item in the Metrics array is the expression that the alarm watches. You designate this expression by setting ReturnValue to true for this object in the array. For more information, see MetricDataQuery .
    If you use the Metrics parameter, you cannot include the MetricName , Dimensions , Period , Namespace , Statistic , or ExtendedStatistic parameters of PutMetricAlarm in the same operation. Instead, you retrieve the metrics you are using in your math expression as part of the Metrics array.
    
    (dict) --This structure is used in both GetMetricData and PutMetricAlarm . The supported use of this structure is different for those two operations.
    When used in GetMetricData , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single GetMetricData call can include up to 500 MetricDataQuery structures.
    When used in PutMetricAlarm , it enables you to create an alarm based on a metric math expression. Each MetricDataQuery in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single PutMetricAlarm call can include up to 20 MetricDataQuery structures in the array. The 20 structures can include as many as 10 structures that contain a MetricStat parameter to retrieve a metric, and as many as 10 structures that contain the Expression parameter to perform a math expression. Of those Expression structures, one must have True as the value for ReturnData . The result of this expression is the value the alarm watches.
    Any expression used in a PutMetricAlarm operation must return a single time series. For more information, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
    Some of the parameters of this structure also have different uses whether you are using this structure in a GetMetricData operation or a PutMetricAlarm operation. These differences are explained in the following parameter list.
    
    Id (string) -- [REQUIRED]A short name used to tie this object to the results in the response. This name must be unique within a single call to GetMetricData . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
    
    MetricStat (dict) --The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
    Within one MetricDataQuery object, you must specify either Expression or MetricStat but not both.
    
    Metric (dict) -- [REQUIRED]The metric to return, including the metric name, namespace, and dimensions.
    
    Namespace (string) --The namespace of the metric.
    
    MetricName (string) --The name of the metric. This is a required field.
    
    Dimensions (list) --The dimensions for the metric.
    
    (dict) --Expands the identity of a metric.
    
    Name (string) -- [REQUIRED]The name of the dimension.
    
    Value (string) -- [REQUIRED]The value representing the dimension measurement.
    
    
    
    
    
    
    
    Period (integer) -- [REQUIRED]The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second.
    If the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:
    
    Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
    Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
    Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
    
    
    Stat (string) -- [REQUIRED]The statistic to return. It can include any CloudWatch statistic or extended statistic.
    
    Unit (string) --When you are using a Put operation, this defines what unit you want to use when storing the metric.
    In a Get operation, if you omit Unit then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.
    
    
    
    Expression (string) --The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the Id of the other metrics to refer to those metrics, and can also use the Id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
    Within each MetricDataQuery object, you must specify either Expression or MetricStat but not both.
    
    Label (string) --A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.
    
    ReturnData (boolean) --When used in GetMetricData , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify False . If you omit this, the default of True is used.
    When used in PutMetricAlarm , specify True for the one expression result to use as the alarm. For all other metrics and expressions in the same PutMetricAlarm operation, specify ReturnData as False.
    
    Period (integer) --The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData operation that includes a StorageResolution of 1 second .
    
    
    
    
    
    Tags (list) -- A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm.
    Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.
    
    (dict) --A key-value pair associated with a CloudWatch resource.
    
    Key (string) -- [REQUIRED]A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.
    
    Value (string) -- [REQUIRED]The value for the specified tag key.
    
    
    
    
    
    ThresholdMetricId (string) -- If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.
    For an example of how to use this parameter, see the Anomaly Detection Model Alarm example on this page.
    If your alarm uses this parameter, it cannot have Auto Scaling actions.
    
    
    """
    pass

def put_metric_data(Namespace=None, MetricData=None):
    """
    Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to ListMetrics .
    You can publish either individual data points in the Value field, or arrays of values and the number of times each value occurred during the period by using the Values and Counts fields in the MetricDatum structure. Using the Values and Counts method enables you to publish up to 150 values per metric with one PutMetricData request, and supports retrieving percentile statistics on this data.
    Each PutMetricData request is limited to 40 KB in size for HTTP POST requests. You can send a payload compressed by gzip. Each request is also limited to no more than 20 different metrics.
    Although the Value parameter accepts numbers of type Double , CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.
    You can use up to 10 dimensions per metric to further clarify what data the metric collects. Each dimension consists of a Name and Value pair. For more information about specifying dimensions, see Publishing Metrics in the Amazon CloudWatch User Guide .
    Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for GetMetricData or GetMetricStatistics from the time they are submitted. Data points with time stamps between 3 and 24 hours ago can take as much as 2 hours to become available for for GetMetricData or GetMetricStatistics .
    CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:
    See also: AWS API Documentation
    
    Exceptions
    
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
                'Values': [
                    123.0,
                ],
                'Counts': [
                    123.0,
                ],
                'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                'StorageResolution': 123
            },
        ]
    )
    
    
    :type Namespace: string
    :param Namespace: [REQUIRED]\nThe namespace for the metric data.\nTo avoid conflicts with AWS service namespaces, you should not specify a namespace that begins with AWS/\n

    :type MetricData: list
    :param MetricData: [REQUIRED]\nThe data for the metric. The array can include no more than 20 metrics per call.\n\n(dict) --Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.\n\nMetricName (string) -- [REQUIRED]The name of the metric.\n\nDimensions (list) --The dimensions associated with the metric.\n\n(dict) --Expands the identity of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value representing the dimension measurement.\n\n\n\n\n\nTimestamp (datetime) --The time the metric data was received, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.\n\nValue (float) --The value for the metric.\nAlthough the parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.\n\nStatisticValues (dict) --The statistical values for the metric.\n\nSampleCount (float) -- [REQUIRED]The number of samples used for the statistic set.\n\nSum (float) -- [REQUIRED]The sum of values for the sample set.\n\nMinimum (float) -- [REQUIRED]The minimum value of the sample set.\n\nMaximum (float) -- [REQUIRED]The maximum value of the sample set.\n\n\n\nValues (list) --Array of numbers representing the values for the metric during the period. Each unique value is listed just once in this array, and the corresponding number in the Counts array specifies the number of times that value occurred during the period. You can include up to 150 unique values in each PutMetricData action that specifies a Values array.\nAlthough the Values array accepts numbers of type Double , CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.\n\n(float) --\n\n\nCounts (list) --Array of numbers that is used along with the Values array. Each number in the Count array is the number of times the corresponding value in the Values array occurred during the period.\nIf you omit the Counts array, the default of 1 is used as the value for each count. If you include a Counts array, it must include the same amount of values as the Values array.\n\n(float) --\n\n\nUnit (string) --When you are using a Put operation, this defines what unit you want to use when storing the metric.\nIn a Get operation, this displays the unit that is used for the metric.\n\nStorageResolution (integer) --Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see High-Resolution Metrics in the Amazon CloudWatch User Guide .\nThis field is optional, if you do not specify it the default of 60 is used.\n\n\n\n\n

    :returns: 
    Namespace (string) -- [REQUIRED]
    The namespace for the metric data.
    To avoid conflicts with AWS service namespaces, you should not specify a namespace that begins with AWS/
    
    MetricData (list) -- [REQUIRED]
    The data for the metric. The array can include no more than 20 metrics per call.
    
    (dict) --Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.
    
    MetricName (string) -- [REQUIRED]The name of the metric.
    
    Dimensions (list) --The dimensions associated with the metric.
    
    (dict) --Expands the identity of a metric.
    
    Name (string) -- [REQUIRED]The name of the dimension.
    
    Value (string) -- [REQUIRED]The value representing the dimension measurement.
    
    
    
    
    
    Timestamp (datetime) --The time the metric data was received, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
    
    Value (float) --The value for the metric.
    Although the parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.
    
    StatisticValues (dict) --The statistical values for the metric.
    
    SampleCount (float) -- [REQUIRED]The number of samples used for the statistic set.
    
    Sum (float) -- [REQUIRED]The sum of values for the sample set.
    
    Minimum (float) -- [REQUIRED]The minimum value of the sample set.
    
    Maximum (float) -- [REQUIRED]The maximum value of the sample set.
    
    
    
    Values (list) --Array of numbers representing the values for the metric during the period. Each unique value is listed just once in this array, and the corresponding number in the Counts array specifies the number of times that value occurred during the period. You can include up to 150 unique values in each PutMetricData action that specifies a Values array.
    Although the Values array accepts numbers of type Double , CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.
    
    (float) --
    
    
    Counts (list) --Array of numbers that is used along with the Values array. Each number in the Count array is the number of times the corresponding value in the Values array occurred during the period.
    If you omit the Counts array, the default of 1 is used as the value for each count. If you include a Counts array, it must include the same amount of values as the Values array.
    
    (float) --
    
    
    Unit (string) --When you are using a Put operation, this defines what unit you want to use when storing the metric.
    In a Get operation, this displays the unit that is used for the metric.
    
    StorageResolution (integer) --Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see High-Resolution Metrics in the Amazon CloudWatch User Guide .
    This field is optional, if you do not specify it the default of 60 is used.
    
    
    
    
    
    
    """
    pass

def set_alarm_state(AlarmName=None, StateValue=None, StateReason=None, StateReasonData=None):
    """
    Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to ALARM sends an SNS message.
    Metric alarms returns to their actual state quickly, often within seconds. Because the metric alarm state change happens quickly, it is typically only visible in the alarm\'s History tab in the Amazon CloudWatch console or through DescribeAlarmHistory .
    If you use SetAlarmState on a composite alarm, the composite alarm is not guaranteed to return to its actual state. It will return to its actual state only once any of its children alarms change state. It is also re-evaluated if you update its configuration.
    If an alarm triggers EC2 Auto Scaling policies or application Auto Scaling policies, you must include information in the StateReasonData parameter to enable the policy to take the correct action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_alarm_state(
        AlarmName='string',
        StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
        StateReason='string',
        StateReasonData='string'
    )
    
    
    :type AlarmName: string
    :param AlarmName: [REQUIRED]\nThe name for the alarm. This name must be unique within the AWS account. The maximum length is 255 characters.\n

    :type StateValue: string
    :param StateValue: [REQUIRED]\nThe value of the state.\n

    :type StateReason: string
    :param StateReason: [REQUIRED]\nThe reason that this alarm is set to this specific state, in text format.\n

    :type StateReasonData: string
    :param StateReasonData: The reason that this alarm is set to this specific state, in JSON format.\nFor SNS or EC2 alarm actions, this is just informational. But for EC2 Auto Scaling or application Auto Scaling alarm actions, the Auto Scaling policy uses the information in this field to take the correct action.\n

    :returns: 
    CloudWatch.Client.exceptions.ResourceNotFound
    CloudWatch.Client.exceptions.InvalidFormatFault
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Assigns one or more tags (key-value pairs) to the specified CloudWatch resource. Currently, the only CloudWatch resources that can be tagged are alarms and Contributor Insights rules.
    Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.
    Tags don\'t have any semantic meaning to AWS and are interpreted strictly as strings of characters.
    You can use the TagResource action with an alarm that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.
    You can associate as many as 50 tags with a CloudWatch resource.
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
    :param ResourceARN: [REQUIRED]\nThe ARN of the CloudWatch resource that you\'re adding tags to.\nThe ARN format of an alarm is ``arn:aws:cloudwatch:Region :account-id :alarm:alarm-name ``\nThe ARN format of a Contributor Insights rule is ``arn:aws:cloudwatch:Region :account-id :insight-rule:insight-rule-name ``\nFor more information on ARN format, see Resource Types Defined by Amazon CloudWatch in the Amazon Web Services General Reference .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe list of key-value pairs to associate with the alarm.\n\n(dict) --A key-value pair associated with a CloudWatch resource.\n\nKey (string) -- [REQUIRED]A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.\n\nValue (string) -- [REQUIRED]The value for the specified tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.ResourceNotFoundException
CloudWatch.Client.exceptions.ConcurrentModificationException
CloudWatch.Client.exceptions.InternalServiceFault


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Removes one or more tags from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe ARN of the CloudWatch resource that you\'re removing tags from.\nThe ARN format of an alarm is ``arn:aws:cloudwatch:Region :account-id :alarm:alarm-name ``\nThe ARN format of a Contributor Insights rule is ``arn:aws:cloudwatch:Region :account-id :insight-rule:insight-rule-name ``\nFor more information on ARN format, see Resource Types Defined by Amazon CloudWatch in the Amazon Web Services General Reference .\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe list of tag keys to remove from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudWatch.Client.exceptions.InvalidParameterValueException
CloudWatch.Client.exceptions.ResourceNotFoundException
CloudWatch.Client.exceptions.ConcurrentModificationException
CloudWatch.Client.exceptions.InternalServiceFault


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

