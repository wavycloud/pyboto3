"""
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
"""


def can_paginate(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
    :type operation_name: string
    """
    pass


def delete_alarms(AlarmNames=None):
    """
    :param AlarmNames: [REQUIRED]
            A list of alarms to be deleted.
            (string) --
            ReturnsNone
            
    :type AlarmNames: list
    """
    pass


def describe_alarm_history(AlarmName=None, HistoryItemType=None, StartDate=None, EndDate=None, MaxRecords=None,
                           NextToken=None):
    """
    :param AlarmName: The name of the alarm.
    :type AlarmName: string
    :param HistoryItemType: The type of alarm histories to retrieve.
    :type HistoryItemType: string
    :param StartDate: The starting date to retrieve alarm history.
    :type StartDate: datetime
    :param EndDate: The ending date to retrieve alarm history.
    :type EndDate: datetime
    :param MaxRecords: The maximum number of alarm history records to retrieve.
    :type MaxRecords: integer
    :param NextToken: The token returned by a previous call to indicate that there is more data available.
    :type NextToken: string
    """
    pass


def describe_alarms(AlarmNames=None, AlarmNamePrefix=None, StateValue=None, ActionPrefix=None, MaxRecords=None,
                    NextToken=None):
    """
    :param AlarmNames: A list of alarm names to retrieve information for.
            (string) --
            
    :type AlarmNames: list
    :param AlarmNamePrefix: The alarm name prefix. AlarmNames cannot be specified if this parameter is specified.
    :type AlarmNamePrefix: string
    :param StateValue: The state value to be used in matching alarms.
    :type StateValue: string
    :param ActionPrefix: The action name prefix.
    :type ActionPrefix: string
    :param MaxRecords: The maximum number of alarm descriptions to retrieve.
    :type MaxRecords: integer
    :param NextToken: The token returned by a previous call to indicate that there is more data available.
    :type NextToken: string
    """
    pass


def describe_alarms_for_metric(MetricName=None, Namespace=None, Statistic=None, Dimensions=None, Period=None,
                               Unit=None):
    """
    :param MetricName: [REQUIRED]
            The name of the metric.
            
    :type MetricName: string
    :param Namespace: [REQUIRED]
            The namespace of the metric.
            
    :type Namespace: string
    :param Statistic: The statistic for the metric.
    :type Statistic: string
    :param Dimensions: The list of dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the DescribeAlarmsForMetric to succeed.
            (dict) --The Dimension data type further expands on the identity of a metric using a Name, Value pair.
            For examples that use one or more dimensions, see PutMetricData .
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement
            
            
    :type Dimensions: list
    :param Period: The period in seconds over which the statistic is applied.
    :type Period: integer
    :param Unit: The unit for the metric.
    :type Unit: string
    """
    pass


def disable_alarm_actions(AlarmNames=None):
    """
    :param AlarmNames: [REQUIRED]
            The names of the alarms to disable actions for.
            (string) --
            ReturnsNone
            
    :type AlarmNames: list
    """
    pass


def enable_alarm_actions(AlarmNames=None):
    """
    :param AlarmNames: [REQUIRED]
            The names of the alarms to enable actions for.
            (string) --
            ReturnsNone
            
    :type AlarmNames: list
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    :param ClientMethod: The client method to presign for
    :type ClientMethod: string
    :param Params: The parameters normally passed to
            ClientMethod.
    :type Params: dict
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
    :type ExpiresIn: int
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
    :type HttpMethod: string
    """
    pass


def get_metric_statistics(Namespace=None, MetricName=None, Dimensions=None, StartTime=None, EndTime=None, Period=None,
                          Statistics=None, Unit=None):
    """
    :param Namespace: [REQUIRED]
            The namespace of the metric, with or without spaces.
            
    :type Namespace: string
    :param MetricName: [REQUIRED]
            The name of the metric, with or without spaces.
            
    :type MetricName: string
    :param Dimensions: A list of dimensions describing qualities of the metric.
            (dict) --The Dimension data type further expands on the identity of a metric using a Name, Value pair.
            For examples that use one or more dimensions, see PutMetricData .
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement
            
            
    :type Dimensions: list
    :param StartTime: [REQUIRED]
            The time stamp to use for determining the first datapoint to return. The value specified is inclusive; results include datapoints with the time stamp specified. The time stamp must be in ISO 8601 UTC format (e.g., 2014-09-03T23:00:00Z).
            Note
            The specified start time is rounded down to the nearest value. Datapoints are returned for start times up to two weeks in the past. Specified start times that are more than two weeks in the past will not return datapoints for metrics that are older than two weeks.
            Data that is timestamped 24 hours or more in the past may take in excess of 48 hours to become available from submission time using GetMetricStatistics .
            
    :type StartTime: datetime
    :param EndTime: [REQUIRED]
            The time stamp to use for determining the last datapoint to return. The value specified is exclusive; results will include datapoints up to the time stamp specified. The time stamp must be in ISO 8601 UTC format (e.g., 2014-09-03T23:00:00Z).
            
    :type EndTime: datetime
    :param Period: [REQUIRED]
            The granularity, in seconds, of the returned datapoints. A Period can be as short as one minute (60 seconds) or as long as one day (86,400 seconds), and must be a multiple of 60. The default value is 60.
            
    :type Period: integer
    :param Statistics: [REQUIRED]
            The metric statistics to return. For information about specific statistics returned by GetMetricStatistics, see Statistics in the Amazon CloudWatch Developer Guide .
            (string) --
            
    :type Statistics: list
    :param Unit: The specific unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If the metric only ever reports one unit, specifying a unit will have no effect.
    :type Unit: string
    """
    pass


def get_paginator(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
    :type operation_name: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_metrics(Namespace=None, MetricName=None, Dimensions=None, NextToken=None):
    """
    :param Namespace: The namespace to filter against.
    :type Namespace: string
    :param MetricName: The name of the metric to filter against.
    :type MetricName: string
    :param Dimensions: A list of dimensions to filter against.
            (dict) --The DimensionFilter data type is used to filter ListMetrics results.
            Name (string) -- [REQUIRED]The dimension name to be matched.
            Value (string) --The value of the dimension to be matched.
            Note
            Specifying a Name without specifying a Value returns all values associated with that Name .
            
            
    :type Dimensions: list
    :param NextToken: The token returned by a previous call to indicate that there is more data available.
    :type NextToken: string
    """
    pass


def put_metric_alarm(AlarmName=None, AlarmDescription=None, ActionsEnabled=None, OKActions=None, AlarmActions=None,
                     InsufficientDataActions=None, MetricName=None, Namespace=None, Statistic=None, Dimensions=None,
                     Period=None, Unit=None, EvaluationPeriods=None, Threshold=None, ComparisonOperator=None):
    """
    :param AlarmName: [REQUIRED]
            The descriptive name for the alarm. This name must be unique within the user's AWS account
            
    :type AlarmName: string
    :param AlarmDescription: The description for the alarm.
    :type AlarmDescription: string
    :param ActionsEnabled: Indicates whether or not actions should be executed during any changes to the alarm's state.
    :type ActionsEnabled: boolean
    :param OKActions: The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region (e.g., us-east-1) :ec2:stop | arn:aws:automate:region (e.g., us-east-1) :ec2:terminate | arn:aws:automate:region (e.g., us-east-1) :ec2:recover
            Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            Note: You must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role for the first time. After this IAM role is created, you can create stop, terminate, or reboot alarms using the CLI.
            (string) --
            
    :type OKActions: list
    :param AlarmActions: The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region (e.g., us-east-1) :ec2:stop | arn:aws:automate:region (e.g., us-east-1) :ec2:terminate | arn:aws:automate:region (e.g., us-east-1) :ec2:recover
            Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            Note: You must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role for the first time. After this IAM role is created, you can create stop, terminate, or reboot alarms using the CLI.
            (string) --
            
    :type AlarmActions: list
    :param InsufficientDataActions: The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
            Valid Values: arn:aws:automate:region (e.g., us-east-1) :ec2:stop | arn:aws:automate:region (e.g., us-east-1) :ec2:terminate | arn:aws:automate:region (e.g., us-east-1) :ec2:recover
            Valid Values (for use with IAM roles): arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:us-east-1:{customer-account }:action/actions/AWS_EC2.InstanceId.Reboot/1.0
            Note: You must create at least one stop, terminate, or reboot alarm using the Amazon EC2 or CloudWatch console to create the EC2ActionsAccess IAM role for the first time. After this IAM role is created, you can create stop, terminate, or reboot alarms using the CLI.
            (string) --
            
    :type InsufficientDataActions: list
    :param MetricName: [REQUIRED]
            The name for the alarm's associated metric.
            
    :type MetricName: string
    :param Namespace: [REQUIRED]
            The namespace for the alarm's associated metric.
            
    :type Namespace: string
    :param Statistic: [REQUIRED]
            The statistic to apply to the alarm's associated metric.
            
    :type Statistic: string
    :param Dimensions: The dimensions for the alarm's associated metric.
            (dict) --The Dimension data type further expands on the identity of a metric using a Name, Value pair.
            For examples that use one or more dimensions, see PutMetricData .
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value representing the dimension measurement
            
            
    :type Dimensions: list
    :param Period: [REQUIRED]
            The period in seconds over which the specified statistic is applied.
            
    :type Period: integer
    :param Unit: The statistic's unit of measure. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.
            Note: If you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, this can cause an Amazon CloudWatch alarm to get stuck in the INSUFFICIENT DATA state.
            
    :type Unit: string
    :param EvaluationPeriods: [REQUIRED]
            The number of periods over which data is compared to the specified threshold.
            
    :type EvaluationPeriods: integer
    :param Threshold: [REQUIRED]
            The value against which the specified statistic is compared.
            
    :type Threshold: float
    :param ComparisonOperator: [REQUIRED]
            The arithmetic operation to use when comparing the specified Statistic and Threshold . The specified Statistic value is used as the first operand.
            
    :type ComparisonOperator: string
    """
    pass


def put_metric_data(Namespace=None, MetricData=None):
    """
    :param Namespace: [REQUIRED]
            The namespace for the metric data.
            Note
            You cannot specify a namespace that begins with 'AWS/'. Namespaces that begin with 'AWS/' are reserved for other Amazon Web Services products that send metrics to Amazon CloudWatch.
            
    :type Namespace: string
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
            
            
    :type MetricData: list
    """
    pass


def set_alarm_state(AlarmName=None, StateValue=None, StateReason=None, StateReasonData=None):
    """
    :param AlarmName: [REQUIRED]
            The descriptive name for the alarm. This name must be unique within the user's AWS account. The maximum length is 255 characters.
            
    :type AlarmName: string
    :param StateValue: [REQUIRED]
            The value of the state.
            
    :type StateValue: string
    :param StateReason: [REQUIRED]
            The reason that this alarm is set to this specific state (in human-readable text format)
            
    :type StateReason: string
    :param StateReasonData: The reason that this alarm is set to this specific state (in machine-readable JSON format)
    :type StateReasonData: string
    """
    pass
