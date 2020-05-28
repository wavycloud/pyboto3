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
    
    Exceptions
    
    :example: response = client.batch_get_traces(
        TraceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type TraceIds: list
    :param TraceIds: [REQUIRED]\nSpecify the trace IDs of requests for which to retrieve segments.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: Pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Traces (list) --
Full traces for the specified requests.

(dict) --
A collection of segment documents with matching trace IDs.

Id (string) --
The unique identifier for the request that generated the trace\'s segments and subsegments.

Duration (float) --
The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.

Segments (list) --
Segment documents for the segments and subsegments that comprise the trace.

(dict) --
A segment from a trace that has been ingested by the X-Ray service. The segment can be compiled from documents uploaded with  PutTraceSegments , or an inferred segment for a downstream service, generated from a subsegment sent by the service that called it.
For the full segment document schema, see AWS X-Ray Segment Documents in the AWS X-Ray Developer Guide .

Id (string) --
The segment\'s ID.

Document (string) --
The segment document.









UnprocessedTraceIds (list) --
Trace IDs of requests that haven\'t been processed.

(string) --


NextToken (string) --
Pagination token.







Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


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
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_group(GroupName=None, FilterExpression=None):
    """
    Creates a group resource with a name and a filter expression.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_group(
        GroupName='string',
        FilterExpression='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe case-sensitive name of the new group. Default is a reserved name and names must be unique.\n

    :type FilterExpression: string
    :param FilterExpression: The filter expression defining criteria by which to group traces.

    :rtype: dict

ReturnsResponse Syntax
{
    'Group': {
        'GroupName': 'string',
        'GroupARN': 'string',
        'FilterExpression': 'string'
    }
}


Response Structure

(dict) --

Group (dict) --
The group that was created. Contains the name of the group that was created, the ARN of the group that was generated based on the group name, and the filter expression that was assigned to the group.

GroupName (string) --
The unique case-sensitive name of the group.

GroupARN (string) --
The ARN of the group generated based on the GroupName.

FilterExpression (string) --
The filter expression defining the parameters to include traces.









Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'Group': {
            'GroupName': 'string',
            'GroupARN': 'string',
            'FilterExpression': 'string'
        }
    }
    
    
    :returns: 
    XRay.Client.exceptions.InvalidRequestException
    XRay.Client.exceptions.ThrottledException
    
    """
    pass

def create_sampling_rule(SamplingRule=None):
    """
    Creates a rule to control sampling behavior for instrumented applications. Services retrieve rules with  GetSamplingRules , and evaluate each rule in ascending order of priority for each request. If a rule matches, the service records a trace, borrowing it from the reservoir size. After 10 seconds, the service reports back to X-Ray with  GetSamplingTargets to get updated versions of each in-use rule. The updated rule contains a trace quota that the service can use instead of borrowing from the reservoir.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_sampling_rule(
        SamplingRule={
            'RuleName': 'string',
            'RuleARN': 'string',
            'ResourceARN': 'string',
            'Priority': 123,
            'FixedRate': 123.0,
            'ReservoirSize': 123,
            'ServiceName': 'string',
            'ServiceType': 'string',
            'Host': 'string',
            'HTTPMethod': 'string',
            'URLPath': 'string',
            'Version': 123,
            'Attributes': {
                'string': 'string'
            }
        }
    )
    
    
    :type SamplingRule: dict
    :param SamplingRule: [REQUIRED]\nThe rule definition.\n\nRuleName (string) --The name of the sampling rule. Specify a rule by either name or ARN, but not both.\n\nRuleARN (string) --The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.\n\nResourceARN (string) -- [REQUIRED]Matches the ARN of the AWS resource on which the service runs.\n\nPriority (integer) -- [REQUIRED]The priority of the sampling rule.\n\nFixedRate (float) -- [REQUIRED]The percentage of matching requests to instrument, after the reservoir is exhausted.\n\nReservoirSize (integer) -- [REQUIRED]A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.\n\nServiceName (string) -- [REQUIRED]Matches the name that the service uses to identify itself in segments.\n\nServiceType (string) -- [REQUIRED]Matches the origin that the service uses to identify its type in segments.\n\nHost (string) -- [REQUIRED]Matches the hostname from a request URL.\n\nHTTPMethod (string) -- [REQUIRED]Matches the HTTP method of a request.\n\nURLPath (string) -- [REQUIRED]Matches the path from a request URL.\n\nVersion (integer) -- [REQUIRED]The version of the sampling rule format (1 ).\n\nAttributes (dict) --Matches attributes derived from the request.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'SamplingRuleRecord': {
        'SamplingRule': {
            'RuleName': 'string',
            'RuleARN': 'string',
            'ResourceARN': 'string',
            'Priority': 123,
            'FixedRate': 123.0,
            'ReservoirSize': 123,
            'ServiceName': 'string',
            'ServiceType': 'string',
            'Host': 'string',
            'HTTPMethod': 'string',
            'URLPath': 'string',
            'Version': 123,
            'Attributes': {
                'string': 'string'
            }
        },
        'CreatedAt': datetime(2015, 1, 1),
        'ModifiedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
SamplingRuleRecord (dict) --The saved rule definition and metadata.

SamplingRule (dict) --The sampling rule.

RuleName (string) --The name of the sampling rule. Specify a rule by either name or ARN, but not both.

RuleARN (string) --The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

ResourceARN (string) --Matches the ARN of the AWS resource on which the service runs.

Priority (integer) --The priority of the sampling rule.

FixedRate (float) --The percentage of matching requests to instrument, after the reservoir is exhausted.

ReservoirSize (integer) --A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.

ServiceName (string) --Matches the name that the service uses to identify itself in segments.

ServiceType (string) --Matches the origin that the service uses to identify its type in segments.

Host (string) --Matches the hostname from a request URL.

HTTPMethod (string) --Matches the HTTP method of a request.

URLPath (string) --Matches the path from a request URL.

Version (integer) --The version of the sampling rule format (1 ).

Attributes (dict) --Matches attributes derived from the request.

(string) --
(string) --






CreatedAt (datetime) --When the rule was created.

ModifiedAt (datetime) --When the rule was last modified.








Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException
XRay.Client.exceptions.RuleLimitExceededException


    :return: {
        'SamplingRuleRecord': {
            'SamplingRule': {
                'RuleName': 'string',
                'RuleARN': 'string',
                'ResourceARN': 'string',
                'Priority': 123,
                'FixedRate': 123.0,
                'ReservoirSize': 123,
                'ServiceName': 'string',
                'ServiceType': 'string',
                'Host': 'string',
                'HTTPMethod': 'string',
                'URLPath': 'string',
                'Version': 123,
                'Attributes': {
                    'string': 'string'
                }
            },
            'CreatedAt': datetime(2015, 1, 1),
            'ModifiedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_group(GroupName=None, GroupARN=None):
    """
    Deletes a group resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_group(
        GroupName='string',
        GroupARN='string'
    )
    
    
    :type GroupName: string
    :param GroupName: The case-sensitive name of the group.

    :type GroupARN: string
    :param GroupARN: The ARN of the group that was generated on creation.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_sampling_rule(RuleName=None, RuleARN=None):
    """
    Deletes a sampling rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_sampling_rule(
        RuleName='string',
        RuleARN='string'
    )
    
    
    :type RuleName: string
    :param RuleName: The name of the sampling rule. Specify a rule by either name or ARN, but not both.

    :type RuleARN: string
    :param RuleARN: The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

    :rtype: dict

ReturnsResponse Syntax
{
    'SamplingRuleRecord': {
        'SamplingRule': {
            'RuleName': 'string',
            'RuleARN': 'string',
            'ResourceARN': 'string',
            'Priority': 123,
            'FixedRate': 123.0,
            'ReservoirSize': 123,
            'ServiceName': 'string',
            'ServiceType': 'string',
            'Host': 'string',
            'HTTPMethod': 'string',
            'URLPath': 'string',
            'Version': 123,
            'Attributes': {
                'string': 'string'
            }
        },
        'CreatedAt': datetime(2015, 1, 1),
        'ModifiedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

SamplingRuleRecord (dict) --
The deleted rule definition and metadata.

SamplingRule (dict) --
The sampling rule.

RuleName (string) --
The name of the sampling rule. Specify a rule by either name or ARN, but not both.

RuleARN (string) --
The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

ResourceARN (string) --
Matches the ARN of the AWS resource on which the service runs.

Priority (integer) --
The priority of the sampling rule.

FixedRate (float) --
The percentage of matching requests to instrument, after the reservoir is exhausted.

ReservoirSize (integer) --
A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.

ServiceName (string) --
Matches the name that the service uses to identify itself in segments.

ServiceType (string) --
Matches the origin that the service uses to identify its type in segments.

Host (string) --
Matches the hostname from a request URL.

HTTPMethod (string) --
Matches the HTTP method of a request.

URLPath (string) --
Matches the path from a request URL.

Version (integer) --
The version of the sampling rule format (1 ).

Attributes (dict) --
Matches attributes derived from the request.

(string) --
(string) --






CreatedAt (datetime) --
When the rule was created.

ModifiedAt (datetime) --
When the rule was last modified.









Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'SamplingRuleRecord': {
            'SamplingRule': {
                'RuleName': 'string',
                'RuleARN': 'string',
                'ResourceARN': 'string',
                'Priority': 123,
                'FixedRate': 123.0,
                'ReservoirSize': 123,
                'ServiceName': 'string',
                'ServiceType': 'string',
                'Host': 'string',
                'HTTPMethod': 'string',
                'URLPath': 'string',
                'Version': 123,
                'Attributes': {
                    'string': 'string'
                }
            },
            'CreatedAt': datetime(2015, 1, 1),
            'ModifiedAt': datetime(2015, 1, 1)
        }
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

def get_encryption_config():
    """
    Retrieves the current encryption configuration for X-Ray data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_encryption_config()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'EncryptionConfig': {
        'KeyId': 'string',
        'Status': 'UPDATING'|'ACTIVE',
        'Type': 'NONE'|'KMS'
    }
}


Response Structure

(dict) --
EncryptionConfig (dict) --The encryption configuration document.

KeyId (string) --The ID of the customer master key (CMK) used for encryption, if applicable.

Status (string) --The encryption status. While the status is UPDATING , X-Ray may encrypt data with a combination of the new and old settings.

Type (string) --The type of encryption. Set to KMS for encryption with CMKs. Set to NONE for default encryption.








Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'EncryptionConfig': {
            'KeyId': 'string',
            'Status': 'UPDATING'|'ACTIVE',
            'Type': 'NONE'|'KMS'
        }
    }
    
    
    """
    pass

def get_group(GroupName=None, GroupARN=None):
    """
    Retrieves group resource details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_group(
        GroupName='string',
        GroupARN='string'
    )
    
    
    :type GroupName: string
    :param GroupName: The case-sensitive name of the group.

    :type GroupARN: string
    :param GroupARN: The ARN of the group that was generated on creation.

    :rtype: dict

ReturnsResponse Syntax
{
    'Group': {
        'GroupName': 'string',
        'GroupARN': 'string',
        'FilterExpression': 'string'
    }
}


Response Structure

(dict) --

Group (dict) --
The group that was requested. Contains the name of the group, the ARN of the group, and the filter expression that assigned to the group.

GroupName (string) --
The unique case-sensitive name of the group.

GroupARN (string) --
The ARN of the group generated based on the GroupName.

FilterExpression (string) --
The filter expression defining the parameters to include traces.









Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'Group': {
            'GroupName': 'string',
            'GroupARN': 'string',
            'FilterExpression': 'string'
        }
    }
    
    
    :returns: 
    XRay.Client.exceptions.InvalidRequestException
    XRay.Client.exceptions.ThrottledException
    
    """
    pass

def get_groups(NextToken=None):
    """
    Retrieves all active group details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_groups(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token.

    :rtype: dict
ReturnsResponse Syntax{
    'Groups': [
        {
            'GroupName': 'string',
            'GroupARN': 'string',
            'FilterExpression': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Groups (list) --The collection of all active groups.

(dict) --Details for a group without metadata.

GroupName (string) --The unique case-sensitive name of the group.

GroupARN (string) --The ARN of the group generated based on the GroupName.

FilterExpression (string) --The filter expression defining the parameters to include traces.





NextToken (string) --Pagination token.






Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'Groups': [
            {
                'GroupName': 'string',
                'GroupARN': 'string',
                'FilterExpression': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
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

def get_sampling_rules(NextToken=None):
    """
    Retrieves all sampling rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_sampling_rules(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token.

    :rtype: dict
ReturnsResponse Syntax{
    'SamplingRuleRecords': [
        {
            'SamplingRule': {
                'RuleName': 'string',
                'RuleARN': 'string',
                'ResourceARN': 'string',
                'Priority': 123,
                'FixedRate': 123.0,
                'ReservoirSize': 123,
                'ServiceName': 'string',
                'ServiceType': 'string',
                'Host': 'string',
                'HTTPMethod': 'string',
                'URLPath': 'string',
                'Version': 123,
                'Attributes': {
                    'string': 'string'
                }
            },
            'CreatedAt': datetime(2015, 1, 1),
            'ModifiedAt': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
SamplingRuleRecords (list) --Rule definitions and metadata.

(dict) --A  SamplingRule and its metadata.

SamplingRule (dict) --The sampling rule.

RuleName (string) --The name of the sampling rule. Specify a rule by either name or ARN, but not both.

RuleARN (string) --The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

ResourceARN (string) --Matches the ARN of the AWS resource on which the service runs.

Priority (integer) --The priority of the sampling rule.

FixedRate (float) --The percentage of matching requests to instrument, after the reservoir is exhausted.

ReservoirSize (integer) --A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.

ServiceName (string) --Matches the name that the service uses to identify itself in segments.

ServiceType (string) --Matches the origin that the service uses to identify its type in segments.

Host (string) --Matches the hostname from a request URL.

HTTPMethod (string) --Matches the HTTP method of a request.

URLPath (string) --Matches the path from a request URL.

Version (integer) --The version of the sampling rule format (1 ).

Attributes (dict) --Matches attributes derived from the request.

(string) --
(string) --






CreatedAt (datetime) --When the rule was created.

ModifiedAt (datetime) --When the rule was last modified.





NextToken (string) --Pagination token.






Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'SamplingRuleRecords': [
            {
                'SamplingRule': {
                    'RuleName': 'string',
                    'RuleARN': 'string',
                    'ResourceARN': 'string',
                    'Priority': 123,
                    'FixedRate': 123.0,
                    'ReservoirSize': 123,
                    'ServiceName': 'string',
                    'ServiceType': 'string',
                    'Host': 'string',
                    'HTTPMethod': 'string',
                    'URLPath': 'string',
                    'Version': 123,
                    'Attributes': {
                        'string': 'string'
                    }
                },
                'CreatedAt': datetime(2015, 1, 1),
                'ModifiedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    XRay.Client.exceptions.InvalidRequestException
    XRay.Client.exceptions.ThrottledException
    
    """
    pass

def get_sampling_statistic_summaries(NextToken=None):
    """
    Retrieves information about recent sampling results for all sampling rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_sampling_statistic_summaries(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token.

    :rtype: dict
ReturnsResponse Syntax{
    'SamplingStatisticSummaries': [
        {
            'RuleName': 'string',
            'Timestamp': datetime(2015, 1, 1),
            'RequestCount': 123,
            'BorrowCount': 123,
            'SampledCount': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
SamplingStatisticSummaries (list) --Information about the number of requests instrumented for each sampling rule.

(dict) --Aggregated request sampling data for a sampling rule across all services for a 10 second window.

RuleName (string) --The name of the sampling rule.

Timestamp (datetime) --The start time of the reporting window.

RequestCount (integer) --The number of requests that matched the rule.

BorrowCount (integer) --The number of requests recorded with borrowed reservoir quota.

SampledCount (integer) --The number of requests recorded.





NextToken (string) --Pagination token.






Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'SamplingStatisticSummaries': [
            {
                'RuleName': 'string',
                'Timestamp': datetime(2015, 1, 1),
                'RequestCount': 123,
                'BorrowCount': 123,
                'SampledCount': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_sampling_targets(SamplingStatisticsDocuments=None):
    """
    Requests a sampling quota for rules that the service is using to sample requests.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_sampling_targets(
        SamplingStatisticsDocuments=[
            {
                'RuleName': 'string',
                'ClientID': 'string',
                'Timestamp': datetime(2015, 1, 1),
                'RequestCount': 123,
                'SampledCount': 123,
                'BorrowCount': 123
            },
        ]
    )
    
    
    :type SamplingStatisticsDocuments: list
    :param SamplingStatisticsDocuments: [REQUIRED]\nInformation about rules that the service is using to sample requests.\n\n(dict) --Request sampling results for a single rule from a service. Results are for the last 10 seconds unless the service has been assigned a longer reporting interval after a previous call to GetSamplingTargets .\n\nRuleName (string) -- [REQUIRED]The name of the sampling rule.\n\nClientID (string) -- [REQUIRED]A unique identifier for the service in hexadecimal.\n\nTimestamp (datetime) -- [REQUIRED]The current time.\n\nRequestCount (integer) -- [REQUIRED]The number of requests that matched the rule.\n\nSampledCount (integer) -- [REQUIRED]The number of requests recorded.\n\nBorrowCount (integer) --The number of requests recorded with borrowed reservoir quota.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'SamplingTargetDocuments': [
        {
            'RuleName': 'string',
            'FixedRate': 123.0,
            'ReservoirQuota': 123,
            'ReservoirQuotaTTL': datetime(2015, 1, 1),
            'Interval': 123
        },
    ],
    'LastRuleModification': datetime(2015, 1, 1),
    'UnprocessedStatistics': [
        {
            'RuleName': 'string',
            'ErrorCode': 'string',
            'Message': 'string'
        },
    ]
}


Response Structure

(dict) --
SamplingTargetDocuments (list) --Updated rules that the service should use to sample requests.

(dict) --Temporary changes to a sampling rule configuration. To meet the global sampling target for a rule, X-Ray calculates a new reservoir for each service based on the recent sampling results of all services that called  GetSamplingTargets .

RuleName (string) --The name of the sampling rule.

FixedRate (float) --The percentage of matching requests to instrument, after the reservoir is exhausted.

ReservoirQuota (integer) --The number of requests per second that X-Ray allocated this service.

ReservoirQuotaTTL (datetime) --When the reservoir quota expires.

Interval (integer) --The number of seconds for the service to wait before getting sampling targets again.





LastRuleModification (datetime) --The last time a user changed the sampling rule configuration. If the sampling rule configuration changed since the service last retrieved it, the service should call  GetSamplingRules to get the latest version.

UnprocessedStatistics (list) --Information about  SamplingStatisticsDocument that X-Ray could not process.

(dict) --Sampling statistics from a call to  GetSamplingTargets that X-Ray could not process.

RuleName (string) --The name of the sampling rule.

ErrorCode (string) --The error code.

Message (string) --The error message.










Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'SamplingTargetDocuments': [
            {
                'RuleName': 'string',
                'FixedRate': 123.0,
                'ReservoirQuota': 123,
                'ReservoirQuotaTTL': datetime(2015, 1, 1),
                'Interval': 123
            },
        ],
        'LastRuleModification': datetime(2015, 1, 1),
        'UnprocessedStatistics': [
            {
                'RuleName': 'string',
                'ErrorCode': 'string',
                'Message': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_service_graph(StartTime=None, EndTime=None, GroupName=None, GroupARN=None, NextToken=None):
    """
    Retrieves a document that describes services that process incoming requests, and downstream services that they call as a result. Root services process incoming requests and make calls to downstream services. Root services are applications that use the AWS X-Ray SDK . Downstream services can be other applications, AWS resources, HTTP web APIs, or SQL databases.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_service_graph(
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        GroupName='string',
        GroupARN='string',
        NextToken='string'
    )
    
    
    :type StartTime: datetime
    :param StartTime: [REQUIRED]\nThe start of the time frame for which to generate a graph.\n

    :type EndTime: datetime
    :param EndTime: [REQUIRED]\nThe end of the timeframe for which to generate a graph.\n

    :type GroupName: string
    :param GroupName: The name of a group to generate a graph based on.

    :type GroupARN: string
    :param GroupARN: The ARN of a group to generate a graph based on.

    :type NextToken: string
    :param NextToken: Pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
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
            ],
            'ResponseTimeHistogram': [
                {
                    'Value': 123.0,
                    'Count': 123
                },
            ]
        },
    ],
    'ContainsOldGroupVersions': True|False,
    'NextToken': 'string'
}


Response Structure

(dict) --

StartTime (datetime) --
The start of the time frame for which the graph was generated.

EndTime (datetime) --
The end of the time frame for which the graph was generated.

Services (list) --
The services that have processed a traced request during the specified time frame.

(dict) --
Information about an application that processed requests, users that made requests, or downstream services, resources and applications that an application used.

ReferenceId (integer) --
Identifier for the service. Unique within the service map.

Name (string) --
The canonical name of the service.

Names (list) --
A list of names for the service, including the canonical name.

(string) --


Root (boolean) --
Indicates that the service was the first service to process a request.

AccountId (string) --
Identifier of the AWS account in which the service runs.

Type (string) --
The type of service.

AWS Resource - The type of an AWS resource. For example, AWS::EC2::Instance for a application running on Amazon EC2 or AWS::DynamoDB::Table for an Amazon DynamoDB table that the application used.
AWS Service - The type of an AWS service. For example, AWS::DynamoDB for downstream calls to Amazon DynamoDB that didn\'t target a specific table.
client - Represents the clients that sent requests to a root service.
remote - A downstream service of indeterminate type.


State (string) --
The service\'s state.

StartTime (datetime) --
The start time of the first segment that the service generated.

EndTime (datetime) --
The end time of the last segment that the service generated.

Edges (list) --
Connections to downstream services.

(dict) --
Information about a connection between two services.

ReferenceId (integer) --
Identifier of the edge. Unique within a service map.

StartTime (datetime) --
The start time of the first segment on the edge.

EndTime (datetime) --
The end time of the last segment on the edge.

SummaryStatistics (dict) --
Response statistics for segments on the edge.

OkCount (integer) --
The number of requests that completed with a 2xx Success status code.

ErrorStatistics (dict) --
Information about requests that failed with a 4xx Client Error status code.

ThrottleCount (integer) --
The number of requests that failed with a 419 throttling status code.

OtherCount (integer) --
The number of requests that failed with untracked 4xx Client Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 4xx Client Error status code.



FaultStatistics (dict) --
Information about requests that failed with a 5xx Server Error status code.

OtherCount (integer) --
The number of requests that failed with untracked 5xx Server Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 5xx Server Error status code.



TotalCount (integer) --
The total number of completed requests.

TotalResponseTime (float) --
The aggregate response time of completed requests.



ResponseTimeHistogram (list) --
A histogram that maps the spread of client response times on an edge.

(dict) --
An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value (float) --
The value of the entry.

Count (integer) --
The prevalence of the entry.





Aliases (list) --
Aliases for the edge.

(dict) --
An alias for an edge.

Name (string) --
The canonical name of the alias.

Names (list) --
A list of names for the alias, including the canonical name.

(string) --


Type (string) --
The type of the alias.









SummaryStatistics (dict) --
Aggregated statistics for the service.

OkCount (integer) --
The number of requests that completed with a 2xx Success status code.

ErrorStatistics (dict) --
Information about requests that failed with a 4xx Client Error status code.

ThrottleCount (integer) --
The number of requests that failed with a 419 throttling status code.

OtherCount (integer) --
The number of requests that failed with untracked 4xx Client Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 4xx Client Error status code.



FaultStatistics (dict) --
Information about requests that failed with a 5xx Server Error status code.

OtherCount (integer) --
The number of requests that failed with untracked 5xx Server Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 5xx Server Error status code.



TotalCount (integer) --
The total number of completed requests.

TotalResponseTime (float) --
The aggregate response time of completed requests.



DurationHistogram (list) --
A histogram that maps the spread of service durations.

(dict) --
An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value (float) --
The value of the entry.

Count (integer) --
The prevalence of the entry.





ResponseTimeHistogram (list) --
A histogram that maps the spread of service response times.

(dict) --
An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value (float) --
The value of the entry.

Count (integer) --
The prevalence of the entry.









ContainsOldGroupVersions (boolean) --
A flag indicating whether the group\'s filter expression has been consistent, or if the returned service graph may show traces from an older version of the group\'s filter expression.

NextToken (string) --
Pagination token.







Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


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
                ],
                'ResponseTimeHistogram': [
                    {
                        'Value': 123.0,
                        'Count': 123
                    },
                ]
            },
        ],
        'ContainsOldGroupVersions': True|False,
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_time_series_service_statistics(StartTime=None, EndTime=None, GroupName=None, GroupARN=None, EntitySelectorExpression=None, Period=None, NextToken=None):
    """
    Get an aggregation of service statistics defined by a specific time range.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_time_series_service_statistics(
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        GroupName='string',
        GroupARN='string',
        EntitySelectorExpression='string',
        Period=123,
        NextToken='string'
    )
    
    
    :type StartTime: datetime
    :param StartTime: [REQUIRED]\nThe start of the time frame for which to aggregate statistics.\n

    :type EndTime: datetime
    :param EndTime: [REQUIRED]\nThe end of the time frame for which to aggregate statistics.\n

    :type GroupName: string
    :param GroupName: The case-sensitive name of the group for which to pull statistics from.

    :type GroupARN: string
    :param GroupARN: The ARN of the group for which to pull statistics from.

    :type EntitySelectorExpression: string
    :param EntitySelectorExpression: A filter expression defining entities that will be aggregated for statistics. Supports ID, service, and edge functions. If no selector expression is specified, edge statistics are returned.

    :type Period: integer
    :param Period: Aggregation period in seconds.

    :type NextToken: string
    :param NextToken: Pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
    'TimeSeriesServiceStatistics': [
        {
            'Timestamp': datetime(2015, 1, 1),
            'EdgeSummaryStatistics': {
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
            'ServiceSummaryStatistics': {
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
            ]
        },
    ],
    'ContainsOldGroupVersions': True|False,
    'NextToken': 'string'
}


Response Structure

(dict) --

TimeSeriesServiceStatistics (list) --
The collection of statistics.

(dict) --
A list of TimeSeriesStatistic structures.

Timestamp (datetime) --
Timestamp of the window for which statistics are aggregated.

EdgeSummaryStatistics (dict) --
Response statistics for an edge.

OkCount (integer) --
The number of requests that completed with a 2xx Success status code.

ErrorStatistics (dict) --
Information about requests that failed with a 4xx Client Error status code.

ThrottleCount (integer) --
The number of requests that failed with a 419 throttling status code.

OtherCount (integer) --
The number of requests that failed with untracked 4xx Client Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 4xx Client Error status code.



FaultStatistics (dict) --
Information about requests that failed with a 5xx Server Error status code.

OtherCount (integer) --
The number of requests that failed with untracked 5xx Server Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 5xx Server Error status code.



TotalCount (integer) --
The total number of completed requests.

TotalResponseTime (float) --
The aggregate response time of completed requests.



ServiceSummaryStatistics (dict) --
Response statistics for a service.

OkCount (integer) --
The number of requests that completed with a 2xx Success status code.

ErrorStatistics (dict) --
Information about requests that failed with a 4xx Client Error status code.

ThrottleCount (integer) --
The number of requests that failed with a 419 throttling status code.

OtherCount (integer) --
The number of requests that failed with untracked 4xx Client Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 4xx Client Error status code.



FaultStatistics (dict) --
Information about requests that failed with a 5xx Server Error status code.

OtherCount (integer) --
The number of requests that failed with untracked 5xx Server Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 5xx Server Error status code.



TotalCount (integer) --
The total number of completed requests.

TotalResponseTime (float) --
The aggregate response time of completed requests.



ResponseTimeHistogram (list) --
The response time histogram for the selected entities.

(dict) --
An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value (float) --
The value of the entry.

Count (integer) --
The prevalence of the entry.









ContainsOldGroupVersions (boolean) --
A flag indicating whether or not a group\'s filter expression has been consistent, or if a returned aggregation may show statistics from an older version of the group\'s filter expression.

NextToken (string) --
Pagination token.







Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'TimeSeriesServiceStatistics': [
            {
                'Timestamp': datetime(2015, 1, 1),
                'EdgeSummaryStatistics': {
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
                'ServiceSummaryStatistics': {
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
                ]
            },
        ],
        'ContainsOldGroupVersions': True|False,
        'NextToken': 'string'
    }
    
    
    :returns: 
    XRay.Client.exceptions.InvalidRequestException
    XRay.Client.exceptions.ThrottledException
    
    """
    pass

def get_trace_graph(TraceIds=None, NextToken=None):
    """
    Retrieves a service graph for one or more specific trace IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_trace_graph(
        TraceIds=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type TraceIds: list
    :param TraceIds: [REQUIRED]\nTrace IDs of requests for which to generate a service graph.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: Pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
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
            ],
            'ResponseTimeHistogram': [
                {
                    'Value': 123.0,
                    'Count': 123
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Services (list) --
The services that have processed one of the specified requests.

(dict) --
Information about an application that processed requests, users that made requests, or downstream services, resources and applications that an application used.

ReferenceId (integer) --
Identifier for the service. Unique within the service map.

Name (string) --
The canonical name of the service.

Names (list) --
A list of names for the service, including the canonical name.

(string) --


Root (boolean) --
Indicates that the service was the first service to process a request.

AccountId (string) --
Identifier of the AWS account in which the service runs.

Type (string) --
The type of service.

AWS Resource - The type of an AWS resource. For example, AWS::EC2::Instance for a application running on Amazon EC2 or AWS::DynamoDB::Table for an Amazon DynamoDB table that the application used.
AWS Service - The type of an AWS service. For example, AWS::DynamoDB for downstream calls to Amazon DynamoDB that didn\'t target a specific table.
client - Represents the clients that sent requests to a root service.
remote - A downstream service of indeterminate type.


State (string) --
The service\'s state.

StartTime (datetime) --
The start time of the first segment that the service generated.

EndTime (datetime) --
The end time of the last segment that the service generated.

Edges (list) --
Connections to downstream services.

(dict) --
Information about a connection between two services.

ReferenceId (integer) --
Identifier of the edge. Unique within a service map.

StartTime (datetime) --
The start time of the first segment on the edge.

EndTime (datetime) --
The end time of the last segment on the edge.

SummaryStatistics (dict) --
Response statistics for segments on the edge.

OkCount (integer) --
The number of requests that completed with a 2xx Success status code.

ErrorStatistics (dict) --
Information about requests that failed with a 4xx Client Error status code.

ThrottleCount (integer) --
The number of requests that failed with a 419 throttling status code.

OtherCount (integer) --
The number of requests that failed with untracked 4xx Client Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 4xx Client Error status code.



FaultStatistics (dict) --
Information about requests that failed with a 5xx Server Error status code.

OtherCount (integer) --
The number of requests that failed with untracked 5xx Server Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 5xx Server Error status code.



TotalCount (integer) --
The total number of completed requests.

TotalResponseTime (float) --
The aggregate response time of completed requests.



ResponseTimeHistogram (list) --
A histogram that maps the spread of client response times on an edge.

(dict) --
An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value (float) --
The value of the entry.

Count (integer) --
The prevalence of the entry.





Aliases (list) --
Aliases for the edge.

(dict) --
An alias for an edge.

Name (string) --
The canonical name of the alias.

Names (list) --
A list of names for the alias, including the canonical name.

(string) --


Type (string) --
The type of the alias.









SummaryStatistics (dict) --
Aggregated statistics for the service.

OkCount (integer) --
The number of requests that completed with a 2xx Success status code.

ErrorStatistics (dict) --
Information about requests that failed with a 4xx Client Error status code.

ThrottleCount (integer) --
The number of requests that failed with a 419 throttling status code.

OtherCount (integer) --
The number of requests that failed with untracked 4xx Client Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 4xx Client Error status code.



FaultStatistics (dict) --
Information about requests that failed with a 5xx Server Error status code.

OtherCount (integer) --
The number of requests that failed with untracked 5xx Server Error status codes.

TotalCount (integer) --
The total number of requests that failed with a 5xx Server Error status code.



TotalCount (integer) --
The total number of completed requests.

TotalResponseTime (float) --
The aggregate response time of completed requests.



DurationHistogram (list) --
A histogram that maps the spread of service durations.

(dict) --
An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value (float) --
The value of the entry.

Count (integer) --
The prevalence of the entry.





ResponseTimeHistogram (list) --
A histogram that maps the spread of service response times.

(dict) --
An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value (float) --
The value of the entry.

Count (integer) --
The prevalence of the entry.









NextToken (string) --
Pagination token.







Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


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
                ],
                'ResponseTimeHistogram': [
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

def get_trace_summaries(StartTime=None, EndTime=None, TimeRangeType=None, Sampling=None, SamplingStrategy=None, FilterExpression=None, NextToken=None):
    """
    Retrieves IDs and annotations for traces available for a specified time frame using an optional filter. To get the full traces, pass the trace IDs to BatchGetTraces .
    A filter expression can target traced requests that hit specific service nodes or edges, have errors, or come from a known user. For example, the following filter expression targets traces that pass through api.example.com :
    This filter expression finds traces that have an annotation named account with the value 12345 :
    For a full list of indexed fields and keywords that you can use in filter expressions, see Using Filter Expressions in the AWS X-Ray Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_trace_summaries(
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        TimeRangeType='TraceId'|'Event',
        Sampling=True|False,
        SamplingStrategy={
            'Name': 'PartialScan'|'FixedRate',
            'Value': 123.0
        },
        FilterExpression='string',
        NextToken='string'
    )
    
    
    :type StartTime: datetime
    :param StartTime: [REQUIRED]\nThe start of the time frame for which to retrieve traces.\n

    :type EndTime: datetime
    :param EndTime: [REQUIRED]\nThe end of the time frame for which to retrieve traces.\n

    :type TimeRangeType: string
    :param TimeRangeType: A parameter to indicate whether to query trace summaries by TraceId or Event time.

    :type Sampling: boolean
    :param Sampling: Set to true to get summaries for only a subset of available traces.

    :type SamplingStrategy: dict
    :param SamplingStrategy: A paramater to indicate whether to enable sampling on trace summaries. Input parameters are Name and Value.\n\nName (string) --The name of a sampling rule.\n\nValue (float) --The value of a sampling rule.\n\n\n

    :type FilterExpression: string
    :param FilterExpression: Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.

    :type NextToken: string
    :param NextToken: Specify the pagination token returned by a previous request to retrieve the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
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
            ],
            'ResourceARNs': [
                {
                    'ARN': 'string'
                },
            ],
            'InstanceIds': [
                {
                    'Id': 'string'
                },
            ],
            'AvailabilityZones': [
                {
                    'Name': 'string'
                },
            ],
            'EntryPoint': {
                'Name': 'string',
                'Names': [
                    'string',
                ],
                'AccountId': 'string',
                'Type': 'string'
            },
            'FaultRootCauses': [
                {
                    'Services': [
                        {
                            'Name': 'string',
                            'Names': [
                                'string',
                            ],
                            'Type': 'string',
                            'AccountId': 'string',
                            'EntityPath': [
                                {
                                    'Name': 'string',
                                    'Exceptions': [
                                        {
                                            'Name': 'string',
                                            'Message': 'string'
                                        },
                                    ],
                                    'Remote': True|False
                                },
                            ],
                            'Inferred': True|False
                        },
                    ],
                    'ClientImpacting': True|False
                },
            ],
            'ErrorRootCauses': [
                {
                    'Services': [
                        {
                            'Name': 'string',
                            'Names': [
                                'string',
                            ],
                            'Type': 'string',
                            'AccountId': 'string',
                            'EntityPath': [
                                {
                                    'Name': 'string',
                                    'Exceptions': [
                                        {
                                            'Name': 'string',
                                            'Message': 'string'
                                        },
                                    ],
                                    'Remote': True|False
                                },
                            ],
                            'Inferred': True|False
                        },
                    ],
                    'ClientImpacting': True|False
                },
            ],
            'ResponseTimeRootCauses': [
                {
                    'Services': [
                        {
                            'Name': 'string',
                            'Names': [
                                'string',
                            ],
                            'Type': 'string',
                            'AccountId': 'string',
                            'EntityPath': [
                                {
                                    'Name': 'string',
                                    'Coverage': 123.0,
                                    'Remote': True|False
                                },
                            ],
                            'Inferred': True|False
                        },
                    ],
                    'ClientImpacting': True|False
                },
            ],
            'Revision': 123,
            'MatchedEventTime': datetime(2015, 1, 1)
        },
    ],
    'ApproximateTime': datetime(2015, 1, 1),
    'TracesProcessedCount': 123,
    'NextToken': 'string'
}


Response Structure

(dict) --

TraceSummaries (list) --
Trace IDs and annotations for traces that were found in the specified time frame.

(dict) --
Metadata generated from the segment documents in a trace.

Id (string) --
The unique identifier for the request that generated the trace\'s segments and subsegments.

Duration (float) --
The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.

ResponseTime (float) --
The length of time in seconds between the start and end times of the root segment. If the service performs work asynchronously, the response time measures the time before the response is sent to the user, while the duration measures the amount of time before the last traced activity completes.

HasFault (boolean) --
The root segment document has a 500 series error.

HasError (boolean) --
The root segment document has a 400 series error.

HasThrottle (boolean) --
One or more of the segment documents has a 429 throttling error.

IsPartial (boolean) --
One or more of the segment documents is in progress.

Http (dict) --
Information about the HTTP request served by the trace.

HttpURL (string) --
The request URL.

HttpStatus (integer) --
The response status.

HttpMethod (string) --
The request method.

UserAgent (string) --
The request\'s user agent string.

ClientIp (string) --
The IP address of the requestor.



Annotations (dict) --
Annotations from the trace\'s segment documents.

(string) --

(list) --

(dict) --
Information about a segment annotation.

AnnotationValue (dict) --
Values of the annotation.

NumberValue (float) --
Value for a Number annotation.

BooleanValue (boolean) --
Value for a Boolean annotation.

StringValue (string) --
Value for a String annotation.



ServiceIds (list) --
Services to which the annotation applies.

(dict) --
Name (string) --
Names (list) --
(string) --


AccountId (string) --
Type (string) --












Users (list) --
Users from the trace\'s segment documents.

(dict) --
Information about a user recorded in segment documents.

UserName (string) --
The user\'s name.

ServiceIds (list) --
Services that the user\'s request hit.

(dict) --
Name (string) --
Names (list) --
(string) --


AccountId (string) --
Type (string) --








ServiceIds (list) --
Service IDs from the trace\'s segment documents.

(dict) --
Name (string) --
Names (list) --
(string) --


AccountId (string) --
Type (string) --




ResourceARNs (list) --
A list of resource ARNs for any resource corresponding to the trace segments.

(dict) --
A list of resources ARNs corresponding to the segments in a trace.

ARN (string) --
The ARN of a corresponding resource.





InstanceIds (list) --
A list of EC2 instance IDs for any instance corresponding to the trace segments.

(dict) --
A list of EC2 instance IDs corresponding to the segments in a trace.

Id (string) --
The ID of a corresponding EC2 instance.





AvailabilityZones (list) --
A list of availability zones for any zone corresponding to the trace segments.

(dict) --
A list of availability zones corresponding to the segments in a trace.

Name (string) --
The name of a corresponding availability zone.





EntryPoint (dict) --
The root of a trace.

Name (string) --
Names (list) --
(string) --


AccountId (string) --
Type (string) --


FaultRootCauses (list) --
A collection of FaultRootCause structures corresponding to the the trace segments.

(dict) --
The root cause information for a trace summary fault.

Services (list) --
A list of corresponding services. A service identifies a segment and it contains a name, account ID, type, and inferred flag.

(dict) --
A collection of fields identifying the services in a trace summary fault.

Name (string) --
The service name.

Names (list) --
A collection of associated service names.

(string) --


Type (string) --
The type associated to the service.

AccountId (string) --
The account ID associated to the service.

EntityPath (list) --
The path of root cause entities found on the service.

(dict) --
A collection of segments and corresponding subsegments associated to a trace summary fault error.

Name (string) --
The name of the entity.

Exceptions (list) --
The types and messages of the exceptions.

(dict) --
The exception associated with a root cause.

Name (string) --
The name of the exception.

Message (string) --
The message of the exception.





Remote (boolean) --
A flag that denotes a remote subsegment.





Inferred (boolean) --
A Boolean value indicating if the service is inferred from the trace.





ClientImpacting (boolean) --
A flag that denotes that the root cause impacts the trace client.





ErrorRootCauses (list) --
A collection of ErrorRootCause structures corresponding to the trace segments.

(dict) --
The root cause of a trace summary error.

Services (list) --
A list of services corresponding to an error. A service identifies a segment and it contains a name, account ID, type, and inferred flag.

(dict) --
A collection of fields identifying the services in a trace summary error.

Name (string) --
The service name.

Names (list) --
A collection of associated service names.

(string) --


Type (string) --
The type associated to the service.

AccountId (string) --
The account ID associated to the service.

EntityPath (list) --
The path of root cause entities found on the service.

(dict) --
A collection of segments and corresponding subsegments associated to a trace summary error.

Name (string) --
The name of the entity.

Exceptions (list) --
The types and messages of the exceptions.

(dict) --
The exception associated with a root cause.

Name (string) --
The name of the exception.

Message (string) --
The message of the exception.





Remote (boolean) --
A flag that denotes a remote subsegment.





Inferred (boolean) --
A Boolean value indicating if the service is inferred from the trace.





ClientImpacting (boolean) --
A flag that denotes that the root cause impacts the trace client.





ResponseTimeRootCauses (list) --
A collection of ResponseTimeRootCause structures corresponding to the trace segments.

(dict) --
The root cause information for a response time warning.

Services (list) --
A list of corresponding services. A service identifies a segment and contains a name, account ID, type, and inferred flag.

(dict) --
A collection of fields identifying the service in a response time warning.

Name (string) --
The service name.

Names (list) --
A collection of associated service names.

(string) --


Type (string) --
The type associated to the service.

AccountId (string) --
The account ID associated to the service.

EntityPath (list) --
The path of root cause entities found on the service.

(dict) --
A collection of segments and corresponding subsegments associated to a response time warning.

Name (string) --
The name of the entity.

Coverage (float) --
The types and messages of the exceptions.

Remote (boolean) --
A flag that denotes a remote subsegment.





Inferred (boolean) --
A Boolean value indicating if the service is inferred from the trace.





ClientImpacting (boolean) --
A flag that denotes that the root cause impacts the trace client.





Revision (integer) --
The revision number of a trace.

MatchedEventTime (datetime) --
The matched time stamp of a defined event.





ApproximateTime (datetime) --
The start time of this page of results.

TracesProcessedCount (integer) --
The total number of traces processed, including traces that did not match the specified filter expression.

NextToken (string) --
If the requested time frame contained more than one page of results, you can use this token to retrieve the next page. The first page contains the most most recent results, closest to the end of the time frame.







Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


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
                ],
                'ResourceARNs': [
                    {
                        'ARN': 'string'
                    },
                ],
                'InstanceIds': [
                    {
                        'Id': 'string'
                    },
                ],
                'AvailabilityZones': [
                    {
                        'Name': 'string'
                    },
                ],
                'EntryPoint': {
                    'Name': 'string',
                    'Names': [
                        'string',
                    ],
                    'AccountId': 'string',
                    'Type': 'string'
                },
                'FaultRootCauses': [
                    {
                        'Services': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string',
                                'AccountId': 'string',
                                'EntityPath': [
                                    {
                                        'Name': 'string',
                                        'Exceptions': [
                                            {
                                                'Name': 'string',
                                                'Message': 'string'
                                            },
                                        ],
                                        'Remote': True|False
                                    },
                                ],
                                'Inferred': True|False
                            },
                        ],
                        'ClientImpacting': True|False
                    },
                ],
                'ErrorRootCauses': [
                    {
                        'Services': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string',
                                'AccountId': 'string',
                                'EntityPath': [
                                    {
                                        'Name': 'string',
                                        'Exceptions': [
                                            {
                                                'Name': 'string',
                                                'Message': 'string'
                                            },
                                        ],
                                        'Remote': True|False
                                    },
                                ],
                                'Inferred': True|False
                            },
                        ],
                        'ClientImpacting': True|False
                    },
                ],
                'ResponseTimeRootCauses': [
                    {
                        'Services': [
                            {
                                'Name': 'string',
                                'Names': [
                                    'string',
                                ],
                                'Type': 'string',
                                'AccountId': 'string',
                                'EntityPath': [
                                    {
                                        'Name': 'string',
                                        'Coverage': 123.0,
                                        'Remote': True|False
                                    },
                                ],
                                'Inferred': True|False
                            },
                        ],
                        'ClientImpacting': True|False
                    },
                ],
                'Revision': 123,
                'MatchedEventTime': datetime(2015, 1, 1)
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def put_encryption_config(KeyId=None, Type=None):
    """
    Updates the encryption configuration for X-Ray data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_encryption_config(
        KeyId='string',
        Type='NONE'|'KMS'
    )
    
    
    :type KeyId: string
    :param KeyId: An AWS KMS customer master key (CMK) in one of the following formats:\n\nAlias - The name of the key. For example, alias/MyKey .\nKey ID - The KMS key ID of the key. For example, ae4aa6d49-a4d8-9df9-a475-4ff6d7898456 . AWS X-Ray does not support asymmetric CMKs.\nARN - The full Amazon Resource Name of the key ID or alias. For example, arn:aws:kms:us-east-2:123456789012:key/ae4aa6d49-a4d8-9df9-a475-4ff6d7898456 . Use this format to specify a key in a different account.\n\nOmit this key if you set Type to NONE .\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of encryption. Set to KMS to use your own key for encryption. Set to NONE for default encryption.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EncryptionConfig': {
        'KeyId': 'string',
        'Status': 'UPDATING'|'ACTIVE',
        'Type': 'NONE'|'KMS'
    }
}


Response Structure

(dict) --

EncryptionConfig (dict) --
The new encryption configuration.

KeyId (string) --
The ID of the customer master key (CMK) used for encryption, if applicable.

Status (string) --
The encryption status. While the status is UPDATING , X-Ray may encrypt data with a combination of the new and old settings.

Type (string) --
The type of encryption. Set to KMS for encryption with CMKs. Set to NONE for default encryption.









Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'EncryptionConfig': {
            'KeyId': 'string',
            'Status': 'UPDATING'|'ACTIVE',
            'Type': 'NONE'|'KMS'
        }
    }
    
    
    :returns: 
    XRay.Client.exceptions.InvalidRequestException
    XRay.Client.exceptions.ThrottledException
    
    """
    pass

def put_telemetry_records(TelemetryRecords=None, EC2InstanceId=None, Hostname=None, ResourceARN=None):
    """
    Used by the AWS X-Ray daemon to upload telemetry.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param TelemetryRecords: [REQUIRED]\n\n(dict) --\nTimestamp (datetime) -- [REQUIRED]\nSegmentsReceivedCount (integer) --\nSegmentsSentCount (integer) --\nSegmentsSpilloverCount (integer) --\nSegmentsRejectedCount (integer) --\nBackendConnectionErrors (dict) --\nTimeoutCount (integer) --\nConnectionRefusedCount (integer) --\nHTTPCode4XXCount (integer) --\nHTTPCode5XXCount (integer) --\nUnknownHostCount (integer) --\nOtherCount (integer) --\n\n\n\n\n\n

    :type EC2InstanceId: string
    :param EC2InstanceId: 

    :type Hostname: string
    :param Hostname: 

    :type ResourceARN: string
    :param ResourceARN: 

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_trace_segments(TraceSegmentDocuments=None):
    """
    Uploads segment documents to AWS X-Ray. The X-Ray SDK generates segment documents and sends them to the X-Ray daemon, which uploads them in batches. A segment document can be a completed segment, an in-progress segment, or an array of subsegments.
    Segments must include the following fields. For the full segment document schema, see AWS X-Ray Segment Documents in the AWS X-Ray Developer Guide .
    A trace_id consists of three numbers separated by hyphens. For example, 1-58406520-a006649127e371903a2de979. This includes:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_trace_segments(
        TraceSegmentDocuments=[
            'string',
        ]
    )
    
    
    :type TraceSegmentDocuments: list
    :param TraceSegmentDocuments: [REQUIRED]\nA string containing a JSON document defining one or more segments or subsegments.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnprocessedTraceSegments': [
        {
            'Id': 'string',
            'ErrorCode': 'string',
            'Message': 'string'
        },
    ]
}


Response Structure

(dict) --
UnprocessedTraceSegments (list) --Segments that failed processing.

(dict) --Information about a segment that failed processing.

Id (string) --The segment\'s ID.

ErrorCode (string) --The error that caused processing to fail.

Message (string) --The error message.










Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


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

def update_group(GroupName=None, GroupARN=None, FilterExpression=None):
    """
    Updates a group resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_group(
        GroupName='string',
        GroupARN='string',
        FilterExpression='string'
    )
    
    
    :type GroupName: string
    :param GroupName: The case-sensitive name of the group.

    :type GroupARN: string
    :param GroupARN: The ARN that was generated upon creation.

    :type FilterExpression: string
    :param FilterExpression: The updated filter expression defining criteria by which to group traces.

    :rtype: dict

ReturnsResponse Syntax
{
    'Group': {
        'GroupName': 'string',
        'GroupARN': 'string',
        'FilterExpression': 'string'
    }
}


Response Structure

(dict) --

Group (dict) --
The group that was updated. Contains the name of the group that was updated, the ARN of the group that was updated, and the updated filter expression assigned to the group.

GroupName (string) --
The unique case-sensitive name of the group.

GroupARN (string) --
The ARN of the group generated based on the GroupName.

FilterExpression (string) --
The filter expression defining the parameters to include traces.









Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'Group': {
            'GroupName': 'string',
            'GroupARN': 'string',
            'FilterExpression': 'string'
        }
    }
    
    
    :returns: 
    XRay.Client.exceptions.InvalidRequestException
    XRay.Client.exceptions.ThrottledException
    
    """
    pass

def update_sampling_rule(SamplingRuleUpdate=None):
    """
    Modifies a sampling rule\'s configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_sampling_rule(
        SamplingRuleUpdate={
            'RuleName': 'string',
            'RuleARN': 'string',
            'ResourceARN': 'string',
            'Priority': 123,
            'FixedRate': 123.0,
            'ReservoirSize': 123,
            'Host': 'string',
            'ServiceName': 'string',
            'ServiceType': 'string',
            'HTTPMethod': 'string',
            'URLPath': 'string',
            'Attributes': {
                'string': 'string'
            }
        }
    )
    
    
    :type SamplingRuleUpdate: dict
    :param SamplingRuleUpdate: [REQUIRED]\nThe rule and fields to change.\n\nRuleName (string) --The name of the sampling rule. Specify a rule by either name or ARN, but not both.\n\nRuleARN (string) --The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.\n\nResourceARN (string) --Matches the ARN of the AWS resource on which the service runs.\n\nPriority (integer) --The priority of the sampling rule.\n\nFixedRate (float) --The percentage of matching requests to instrument, after the reservoir is exhausted.\n\nReservoirSize (integer) --A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.\n\nHost (string) --Matches the hostname from a request URL.\n\nServiceName (string) --Matches the name that the service uses to identify itself in segments.\n\nServiceType (string) --Matches the origin that the service uses to identify its type in segments.\n\nHTTPMethod (string) --Matches the HTTP method of a request.\n\nURLPath (string) --Matches the path from a request URL.\n\nAttributes (dict) --Matches attributes derived from the request.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'SamplingRuleRecord': {
        'SamplingRule': {
            'RuleName': 'string',
            'RuleARN': 'string',
            'ResourceARN': 'string',
            'Priority': 123,
            'FixedRate': 123.0,
            'ReservoirSize': 123,
            'ServiceName': 'string',
            'ServiceType': 'string',
            'Host': 'string',
            'HTTPMethod': 'string',
            'URLPath': 'string',
            'Version': 123,
            'Attributes': {
                'string': 'string'
            }
        },
        'CreatedAt': datetime(2015, 1, 1),
        'ModifiedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
SamplingRuleRecord (dict) --The updated rule definition and metadata.

SamplingRule (dict) --The sampling rule.

RuleName (string) --The name of the sampling rule. Specify a rule by either name or ARN, but not both.

RuleARN (string) --The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.

ResourceARN (string) --Matches the ARN of the AWS resource on which the service runs.

Priority (integer) --The priority of the sampling rule.

FixedRate (float) --The percentage of matching requests to instrument, after the reservoir is exhausted.

ReservoirSize (integer) --A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.

ServiceName (string) --Matches the name that the service uses to identify itself in segments.

ServiceType (string) --Matches the origin that the service uses to identify its type in segments.

Host (string) --Matches the hostname from a request URL.

HTTPMethod (string) --Matches the HTTP method of a request.

URLPath (string) --Matches the path from a request URL.

Version (integer) --The version of the sampling rule format (1 ).

Attributes (dict) --Matches attributes derived from the request.

(string) --
(string) --






CreatedAt (datetime) --When the rule was created.

ModifiedAt (datetime) --When the rule was last modified.








Exceptions

XRay.Client.exceptions.InvalidRequestException
XRay.Client.exceptions.ThrottledException


    :return: {
        'SamplingRuleRecord': {
            'SamplingRule': {
                'RuleName': 'string',
                'RuleARN': 'string',
                'ResourceARN': 'string',
                'Priority': 123,
                'FixedRate': 123.0,
                'ReservoirSize': 123,
                'ServiceName': 'string',
                'ServiceType': 'string',
                'Host': 'string',
                'HTTPMethod': 'string',
                'URLPath': 'string',
                'Version': 123,
                'Attributes': {
                    'string': 'string'
                }
            },
            'CreatedAt': datetime(2015, 1, 1),
            'ModifiedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

