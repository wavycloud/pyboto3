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

def describe_dimension_keys(ServiceType=None, Identifier=None, StartTime=None, EndTime=None, Metric=None, PeriodInSeconds=None, GroupBy=None, PartitionBy=None, Filter=None, MaxResults=None, NextToken=None):
    """
    For a specific time period, retrieve the top N dimension keys for a metric.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_dimension_keys(
        ServiceType='RDS',
        Identifier='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Metric='string',
        PeriodInSeconds=123,
        GroupBy={
            'Group': 'string',
            'Dimensions': [
                'string',
            ],
            'Limit': 123
        },
        PartitionBy={
            'Group': 'string',
            'Dimensions': [
                'string',
            ],
            'Limit': 123
        },
        Filter={
            'string': 'string'
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ServiceType: string
    :param ServiceType: [REQUIRED]\nThe AWS service for which Performance Insights will return metrics. The only valid value for ServiceType is: RDS\n

    :type Identifier: string
    :param Identifier: [REQUIRED]\nAn immutable, AWS Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.\nTo use an Amazon RDS instance as a data source, you specify its DbiResourceId value - for example: db-FAIHNTYBKTGAUSUZQYPDS2GW4A\n

    :type StartTime: datetime
    :param StartTime: [REQUIRED]\nThe date and time specifying the beginning of the requested time series data. You can\'t specify a StartTime that\'s earlier than 7 days ago. The value specified is inclusive - data points equal to or greater than StartTime will be returned.\nThe value for StartTime must be earlier than the value for EndTime .\n

    :type EndTime: datetime
    :param EndTime: [REQUIRED]\nThe date and time specifying the end of the requested time series data. The value specified is exclusive - data points less than (but not equal to) EndTime will be returned.\nThe value for EndTime must be later than the value for StartTime .\n

    :type Metric: string
    :param Metric: [REQUIRED]\nThe name of a Performance Insights metric to be measured.\nValid values for Metric are:\n\ndb.load.avg - a scaled representation of the number of active sessions for the database engine.\ndb.sampledload.avg - the raw number of active sessions for the database engine.\n\n

    :type PeriodInSeconds: integer
    :param PeriodInSeconds: The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:\n\n1 (one second)\n60 (one minute)\n300 (five minutes)\n3600 (one hour)\n86400 (twenty-four hours)\n\nIf you don\'t specify PeriodInSeconds , then Performance Insights will choose a value for you, with a goal of returning roughly 100-200 data points in the response.\n

    :type GroupBy: dict
    :param GroupBy: [REQUIRED]\nA specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.\n\nGroup (string) -- [REQUIRED]The name of the dimension group. Valid values are:\n\ndb.user\ndb.host\ndb.sql\ndb.sql_tokenized\ndb.wait_event\ndb.wait_event_type\n\n\nDimensions (list) --A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested, or are present in the response.\nValid values for elements in the Dimensions array are:\n\ndb.user.id\ndb.user.name\ndb.host.id\ndb.host.name\ndb.sql.id\ndb.sql.db_id\ndb.sql.statement\ndb.sql.tokenized_id\ndb.sql_tokenized.id\ndb.sql_tokenized.db_id\ndb.sql_tokenized.statement\ndb.wait_event.name\ndb.wait_event.type\ndb.wait_event_type.name\n\n\n(string) --\n\n\nLimit (integer) --The maximum number of items to fetch for this dimension group.\n\n\n

    :type PartitionBy: dict
    :param PartitionBy: For each dimension specified in GroupBy , specify a secondary dimension to further subdivide the partition keys in the response.\n\nGroup (string) -- [REQUIRED]The name of the dimension group. Valid values are:\n\ndb.user\ndb.host\ndb.sql\ndb.sql_tokenized\ndb.wait_event\ndb.wait_event_type\n\n\nDimensions (list) --A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested, or are present in the response.\nValid values for elements in the Dimensions array are:\n\ndb.user.id\ndb.user.name\ndb.host.id\ndb.host.name\ndb.sql.id\ndb.sql.db_id\ndb.sql.statement\ndb.sql.tokenized_id\ndb.sql_tokenized.id\ndb.sql_tokenized.db_id\ndb.sql_tokenized.statement\ndb.wait_event.name\ndb.wait_event.type\ndb.wait_event_type.name\n\n\n(string) --\n\n\nLimit (integer) --The maximum number of items to fetch for this dimension group.\n\n\n

    :type Filter: dict
    :param Filter: One or more filters to apply in the request. Restrictions:\n\nAny number of filters by the same dimension, as specified in the GroupBy or Partition parameters.\nA single filter for any other dimension in this dimension group.\n\n\n(string) --\n(string) --\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return in the response. If more items exist than the specified MaxRecords value, a pagination token is included in the response so that the remaining results can be retrieved.

    :type NextToken: string
    :param NextToken: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'AlignedStartTime': datetime(2015, 1, 1),
    'AlignedEndTime': datetime(2015, 1, 1),
    'PartitionKeys': [
        {
            'Dimensions': {
                'string': 'string'
            }
        },
    ],
    'Keys': [
        {
            'Dimensions': {
                'string': 'string'
            },
            'Total': 123.0,
            'Partitions': [
                123.0,
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AlignedStartTime (datetime) --
The start time for the returned dimension keys, after alignment to a granular boundary (as specified by PeriodInSeconds ). AlignedStartTime will be less than or equal to the value of the user-specified StartTime .

AlignedEndTime (datetime) --
The end time for the returned dimension keys, after alignment to a granular boundary (as specified by PeriodInSeconds ). AlignedEndTime will be greater than or equal to the value of the user-specified Endtime .

PartitionKeys (list) --
If PartitionBy was present in the request, PartitionKeys contains the breakdown of dimension keys by the specified partitions.

(dict) --
If PartitionBy was specified in a DescribeDimensionKeys request, the dimensions are returned in an array. Each element in the array specifies one dimension.

Dimensions (dict) --
A dimension map that contains the dimension(s) for this partition.

(string) --
(string) --








Keys (list) --
The dimension keys that were requested.

(dict) --
An array of descriptions and aggregated values for each dimension within a dimension group.

Dimensions (dict) --
A map of name-value pairs for the dimensions in the group.

(string) --
(string) --




Total (float) --
The aggregated metric value for the dimension(s), over the requested time range.

Partitions (list) --
If PartitionBy was specified, PartitionKeys contains the dimensions that were.

(float) --






NextToken (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by MaxRecords .







Exceptions

PI.Client.exceptions.InvalidArgumentException
PI.Client.exceptions.InternalServiceError
PI.Client.exceptions.NotAuthorizedException


    :return: {
        'AlignedStartTime': datetime(2015, 1, 1),
        'AlignedEndTime': datetime(2015, 1, 1),
        'PartitionKeys': [
            {
                'Dimensions': {
                    'string': 'string'
                }
            },
        ],
        'Keys': [
            {
                'Dimensions': {
                    'string': 'string'
                },
                'Total': 123.0,
                'Partitions': [
                    123.0,
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_resource_metrics(ServiceType=None, Identifier=None, MetricQueries=None, StartTime=None, EndTime=None, PeriodInSeconds=None, MaxResults=None, NextToken=None):
    """
    Retrieve Performance Insights metrics for a set of data sources, over a time period. You can provide specific dimension groups and dimensions, and provide aggregation and filtering criteria for each group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resource_metrics(
        ServiceType='RDS',
        Identifier='string',
        MetricQueries=[
            {
                'Metric': 'string',
                'GroupBy': {
                    'Group': 'string',
                    'Dimensions': [
                        'string',
                    ],
                    'Limit': 123
                },
                'Filter': {
                    'string': 'string'
                }
            },
        ],
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        PeriodInSeconds=123,
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ServiceType: string
    :param ServiceType: [REQUIRED]\nThe AWS service for which Performance Insights will return metrics. The only valid value for ServiceType is: RDS\n

    :type Identifier: string
    :param Identifier: [REQUIRED]\nAn immutable, AWS Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.\nTo use an Amazon RDS instance as a data source, you specify its DbiResourceId value - for example: db-FAIHNTYBKTGAUSUZQYPDS2GW4A\n

    :type MetricQueries: list
    :param MetricQueries: [REQUIRED]\nAn array of one or more queries to perform. Each query must specify a Performance Insights metric, and can optionally specify aggregation and filtering criteria.\n\n(dict) --A single query to be processed. You must provide the metric to query. If no other parameters are specified, Performance Insights returns all of the data points for that metric. You can optionally request that the data points be aggregated by dimension group ( GroupBy ), and return only those data points that match your criteria (Filter ).\n\nMetric (string) -- [REQUIRED]The name of a Performance Insights metric to be measured.\nValid values for Metric are:\n\ndb.load.avg - a scaled representation of the number of active sessions for the database engine.\ndb.sampledload.avg - the raw number of active sessions for the database engine.\n\n\nGroupBy (dict) --A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.\n\nGroup (string) -- [REQUIRED]The name of the dimension group. Valid values are:\n\ndb.user\ndb.host\ndb.sql\ndb.sql_tokenized\ndb.wait_event\ndb.wait_event_type\n\n\nDimensions (list) --A list of specific dimensions from a dimension group. If this parameter is not present, then it signifies that all of the dimensions in the group were requested, or are present in the response.\nValid values for elements in the Dimensions array are:\n\ndb.user.id\ndb.user.name\ndb.host.id\ndb.host.name\ndb.sql.id\ndb.sql.db_id\ndb.sql.statement\ndb.sql.tokenized_id\ndb.sql_tokenized.id\ndb.sql_tokenized.db_id\ndb.sql_tokenized.statement\ndb.wait_event.name\ndb.wait_event.type\ndb.wait_event_type.name\n\n\n(string) --\n\n\nLimit (integer) --The maximum number of items to fetch for this dimension group.\n\n\n\nFilter (dict) --One or more filters to apply in the request. Restrictions:\n\nAny number of filters by the same dimension, as specified in the GroupBy parameter.\nA single filter for any other dimension in this dimension group.\n\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :type StartTime: datetime
    :param StartTime: [REQUIRED]\nThe date and time specifying the beginning of the requested time series data. You can\'t specify a StartTime that\'s earlier than 7 days ago. The value specified is inclusive - data points equal to or greater than StartTime will be returned.\nThe value for StartTime must be earlier than the value for EndTime .\n

    :type EndTime: datetime
    :param EndTime: [REQUIRED]\nThe date and time specifiying the end of the requested time series data. The value specified is exclusive - data points less than (but not equal to) EndTime will be returned.\nThe value for EndTime must be later than the value for StartTime .\n

    :type PeriodInSeconds: integer
    :param PeriodInSeconds: The granularity, in seconds, of the data points returned from Performance Insights. A period can be as short as one second, or as long as one day (86400 seconds). Valid values are:\n\n1 (one second)\n60 (one minute)\n300 (five minutes)\n3600 (one hour)\n86400 (twenty-four hours)\n\nIf you don\'t specify PeriodInSeconds , then Performance Insights will choose a value for you, with a goal of returning roughly 100-200 data points in the response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return in the response. If more items exist than the specified MaxRecords value, a pagination token is included in the response so that the remaining results can be retrieved.

    :type NextToken: string
    :param NextToken: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by MaxRecords .

    :rtype: dict

ReturnsResponse Syntax
{
    'AlignedStartTime': datetime(2015, 1, 1),
    'AlignedEndTime': datetime(2015, 1, 1),
    'Identifier': 'string',
    'MetricList': [
        {
            'Key': {
                'Metric': 'string',
                'Dimensions': {
                    'string': 'string'
                }
            },
            'DataPoints': [
                {
                    'Timestamp': datetime(2015, 1, 1),
                    'Value': 123.0
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AlignedStartTime (datetime) --
The start time for the returned metrics, after alignment to a granular boundary (as specified by PeriodInSeconds ). AlignedStartTime will be less than or equal to the value of the user-specified StartTime .

AlignedEndTime (datetime) --
The end time for the returned metrics, after alignment to a granular boundary (as specified by PeriodInSeconds ). AlignedEndTime will be greater than or equal to the value of the user-specified Endtime .

Identifier (string) --
An immutable, AWS Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.
To use an Amazon RDS instance as a data source, you specify its DbiResourceId value - for example: db-FAIHNTYBKTGAUSUZQYPDS2GW4A

MetricList (list) --
An array of metric results,, where each array element contains all of the data points for a particular dimension.

(dict) --
A time-ordered series of data points, correpsonding to a dimension of a Performance Insights metric.

Key (dict) --
The dimension(s) to which the data points apply.

Metric (string) --
The name of a Performance Insights metric to be measured.
Valid values for Metric are:

db.load.avg - a scaled representation of the number of active sessions for the database engine.
db.sampledload.avg - the raw number of active sessions for the database engine.


Dimensions (dict) --
The valid dimensions for the metric.

(string) --
(string) --






DataPoints (list) --
An array of timestamp-value pairs, representing measurements over a period of time.

(dict) --
A timestamp, and a single numerical value, which together represent a measurement at a particular point in time.

Timestamp (datetime) --
The time, in epoch format, associated with a particular Value .

Value (float) --
The actual value associated with a particular Timestamp .









NextToken (string) --
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by MaxRecords .







Exceptions

PI.Client.exceptions.InvalidArgumentException
PI.Client.exceptions.InternalServiceError
PI.Client.exceptions.NotAuthorizedException


    :return: {
        'AlignedStartTime': datetime(2015, 1, 1),
        'AlignedEndTime': datetime(2015, 1, 1),
        'Identifier': 'string',
        'MetricList': [
            {
                'Key': {
                    'Metric': 'string',
                    'Dimensions': {
                        'string': 'string'
                    }
                },
                'DataPoints': [
                    {
                        'Timestamp': datetime(2015, 1, 1),
                        'Value': 123.0
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    db.load.avg - a scaled representation of the number of active sessions for the database engine.
    db.sampledload.avg - the raw number of active sessions for the database engine.
    
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

