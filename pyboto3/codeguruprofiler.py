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

def configure_agent(fleetInstanceId=None, profilingGroupName=None):
    """
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.configure_agent(
        fleetInstanceId='string',
        profilingGroupName='string'
    )
    
    
    :type fleetInstanceId: string
    :param fleetInstanceId: 

    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]

    :rtype: dict

ReturnsResponse Syntax
{
    'configuration': {
        'periodInSeconds': 123,
        'shouldProfile': True|False
    }
}


Response Structure

(dict) --
The structure representing the configureAgentResponse.

configuration (dict) --
periodInSeconds (integer) --
shouldProfile (boolean) --








Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {
        'configuration': {
            'periodInSeconds': 123,
            'shouldProfile': True|False
        }
    }
    
    
    :returns: 
    configuration (dict) --
    periodInSeconds (integer) --
    shouldProfile (boolean) --
    
    
    
    """
    pass

def create_profiling_group(agentOrchestrationConfig=None, clientToken=None, profilingGroupName=None):
    """
    Creates a profiling group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_profiling_group(
        agentOrchestrationConfig={
            'profilingEnabled': True|False
        },
        clientToken='string',
        profilingGroupName='string'
    )
    
    
    :type agentOrchestrationConfig: dict
    :param agentOrchestrationConfig: The agent orchestration configuration.\n\nprofilingEnabled (boolean) -- [REQUIRED]\n\n

    :type clientToken: string
    :param clientToken: [REQUIRED]\nUnique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis parameter specifies a unique identifier for the new profiling group that helps ensure idempotency.\nThis field is autopopulated if not provided.\n

    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]\nThe name of the profiling group.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'profilingGroup': {
        'agentOrchestrationConfig': {
            'profilingEnabled': True|False
        },
        'arn': 'string',
        'createdAt': datetime(2015, 1, 1),
        'name': 'string',
        'profilingStatus': {
            'latestAgentOrchestratedAt': datetime(2015, 1, 1),
            'latestAgentProfileReportedAt': datetime(2015, 1, 1),
            'latestAggregatedProfile': {
                'period': 'P1D'|'PT1H'|'PT5M',
                'start': datetime(2015, 1, 1)
            }
        },
        'updatedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
The structure representing the createProfilingGroupResponse.

profilingGroup (dict) --
Information about the new profiling group

agentOrchestrationConfig (dict) --

profilingEnabled (boolean) --


arn (string) --
The Amazon Resource Name (ARN) identifying the profiling group.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the profiling group was created.

name (string) --
The name of the profiling group.

profilingStatus (dict) --
The status of the profiling group.

latestAgentOrchestratedAt (datetime) --
The time, in milliseconds since the epoch, when the latest agent was orchestrated.

latestAgentProfileReportedAt (datetime) --
The time, in milliseconds since the epoch, when the latest agent was reported..

latestAggregatedProfile (dict) --
The latest aggregated profile

period (string) --
The time period.

start (datetime) --
The start time.





updatedAt (datetime) --
The time, in milliseconds since the epoch, when the profiling group was last updated.









Exceptions

CodeGuruProfiler.Client.exceptions.ServiceQuotaExceededException
CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ConflictException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException


    :return: {
        'profilingGroup': {
            'agentOrchestrationConfig': {
                'profilingEnabled': True|False
            },
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'name': 'string',
            'profilingStatus': {
                'latestAgentOrchestratedAt': datetime(2015, 1, 1),
                'latestAgentProfileReportedAt': datetime(2015, 1, 1),
                'latestAggregatedProfile': {
                    'period': 'P1D'|'PT1H'|'PT5M',
                    'start': datetime(2015, 1, 1)
                }
            },
            'updatedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    profilingEnabled (boolean) --
    
    """
    pass

def delete_profiling_group(profilingGroupName=None):
    """
    Deletes a profiling group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_profiling_group(
        profilingGroupName='string'
    )
    
    
    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]\nThe profiling group name to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The structure representing the deleteProfilingGroupResponse.




Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    """
    pass

def describe_profiling_group(profilingGroupName=None):
    """
    Describes a profiling group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_profiling_group(
        profilingGroupName='string'
    )
    
    
    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]\nThe profiling group name.\n

    :rtype: dict
ReturnsResponse Syntax{
    'profilingGroup': {
        'agentOrchestrationConfig': {
            'profilingEnabled': True|False
        },
        'arn': 'string',
        'createdAt': datetime(2015, 1, 1),
        'name': 'string',
        'profilingStatus': {
            'latestAgentOrchestratedAt': datetime(2015, 1, 1),
            'latestAgentProfileReportedAt': datetime(2015, 1, 1),
            'latestAggregatedProfile': {
                'period': 'P1D'|'PT1H'|'PT5M',
                'start': datetime(2015, 1, 1)
            }
        },
        'updatedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --The structure representing the describeProfilingGroupResponse.

profilingGroup (dict) --Information about a profiling group.

agentOrchestrationConfig (dict) --
profilingEnabled (boolean) --


arn (string) --The Amazon Resource Name (ARN) identifying the profiling group.

createdAt (datetime) --The time, in milliseconds since the epoch, when the profiling group was created.

name (string) --The name of the profiling group.

profilingStatus (dict) --The status of the profiling group.

latestAgentOrchestratedAt (datetime) --The time, in milliseconds since the epoch, when the latest agent was orchestrated.

latestAgentProfileReportedAt (datetime) --The time, in milliseconds since the epoch, when the latest agent was reported..

latestAggregatedProfile (dict) --The latest aggregated profile

period (string) --The time period.

start (datetime) --The start time.





updatedAt (datetime) --The time, in milliseconds since the epoch, when the profiling group was last updated.








Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {
        'profilingGroup': {
            'agentOrchestrationConfig': {
                'profilingEnabled': True|False
            },
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'name': 'string',
            'profilingStatus': {
                'latestAgentOrchestratedAt': datetime(2015, 1, 1),
                'latestAgentProfileReportedAt': datetime(2015, 1, 1),
                'latestAggregatedProfile': {
                    'period': 'P1D'|'PT1H'|'PT5M',
                    'start': datetime(2015, 1, 1)
                }
            },
            'updatedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CodeGuruProfiler.Client.exceptions.InternalServerException
    CodeGuruProfiler.Client.exceptions.ValidationException
    CodeGuruProfiler.Client.exceptions.ThrottlingException
    CodeGuruProfiler.Client.exceptions.ResourceNotFoundException
    
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

def get_policy(profilingGroupName=None):
    """
    Gets the profiling group policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_policy(
        profilingGroupName='string'
    )
    
    
    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]\nThe name of the profiling group.\n

    :rtype: dict
ReturnsResponse Syntax{
    'policy': 'string',
    'revisionId': 'string'
}


Response Structure

(dict) --The structure representing the getPolicyResponse.

policy (string) --The resource-based policy attached to the ProfilingGroup .

revisionId (string) --A unique identifier for the current revision of the policy.






Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {
        'policy': 'string',
        'revisionId': 'string'
    }
    
    
    """
    pass

def get_profile(accept=None, endTime=None, maxDepth=None, period=None, profilingGroupName=None, startTime=None):
    """
    Gets the aggregated profile of a profiling group for the specified time range. If the requested time range does not align with the available aggregated profiles, it is expanded to attain alignment. If aggregated profiles are available only for part of the period requested, the profile is returned from the earliest available to the latest within the requested time range.
    For example, if the requested time range is from 00:00 to 00:20 and the available profiles are from 00:15 to 00:25, the returned profile will be from 00:15 to 00:20.
    You must specify exactly two of the following parameters: startTime , period , and endTime .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_profile(
        accept='string',
        endTime=datetime(2015, 1, 1),
        maxDepth=123,
        period='string',
        profilingGroupName='string',
        startTime=datetime(2015, 1, 1)
    )
    
    
    :type accept: string
    :param accept: The format of the profile to return. You can choose application/json or the default application/x-amzn-ion .

    :type endTime: datetime
    :param endTime: You must specify exactly two of the following parameters: startTime , period , and endTime .

    :type maxDepth: integer
    :param maxDepth: The maximum depth of the graph.

    :type period: string
    :param period: The period of the profile to get. The time range must be in the past and not longer than one week.\nYou must specify exactly two of the following parameters: startTime , period , and endTime .\n

    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]\nThe name of the profiling group to get.\n

    :type startTime: datetime
    :param startTime: The start time of the profile to get.\nYou must specify exactly two of the following parameters: startTime , period , and endTime .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'contentEncoding': 'string',
    'contentType': 'string',
    'profile': StreamingBody()
}


Response Structure

(dict) --
The structure representing the getProfileResponse.

contentEncoding (string) --
The content encoding of the profile.

contentType (string) --
The content type of the profile in the payload. It is either application/json or the default application/x-amzn-ion .

profile (StreamingBody) --
Information about the profile.







Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {
        'contentEncoding': 'string',
        'contentType': 'string',
        'profile': StreamingBody()
    }
    
    
    :returns: 
    CodeGuruProfiler.Client.exceptions.InternalServerException
    CodeGuruProfiler.Client.exceptions.ValidationException
    CodeGuruProfiler.Client.exceptions.ThrottlingException
    CodeGuruProfiler.Client.exceptions.ResourceNotFoundException
    
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

def list_profile_times(endTime=None, maxResults=None, nextToken=None, orderBy=None, period=None, profilingGroupName=None, startTime=None):
    """
    List the start times of the available aggregated profiles of a profiling group for an aggregation period within the specified time range.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_profile_times(
        endTime=datetime(2015, 1, 1),
        maxResults=123,
        nextToken='string',
        orderBy='TimestampAscending'|'TimestampDescending',
        period='P1D'|'PT1H'|'PT5M',
        profilingGroupName='string',
        startTime=datetime(2015, 1, 1)
    )
    
    
    :type endTime: datetime
    :param endTime: [REQUIRED]\nThe end time of the time range from which to list the profiles.\n

    :type maxResults: integer
    :param maxResults: The maximum number of profile time results returned by ListProfileTimes in paginated output. When this parameter is used, ListProfileTimes only returns maxResults results in a single page with a nextToken response element. The remaining results of the initial request can be seen by sending another ListProfileTimes request with the returned nextToken value.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListProfileTimes request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :type orderBy: string
    :param orderBy: The order (ascending or descending by start time of the profile) to use when listing profiles. Defaults to TIMESTAMP_DESCENDING .

    :type period: string
    :param period: [REQUIRED]\nThe aggregation period.\n

    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]\nThe name of the profiling group.\n

    :type startTime: datetime
    :param startTime: [REQUIRED]\nThe start time of the time range from which to list the profiles.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'profileTimes': [
        {
            'start': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --
The structure representing the listProfileTimesResponse.

nextToken (string) --
The nextToken value to include in a future ListProfileTimes request. When the results of a ListProfileTimes request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.

profileTimes (list) --
The list of start times of the available profiles for the aggregation period in the specified time range.

(dict) --
Information about the profile time.

start (datetime) --
The start time of the profile.











Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {
        'nextToken': 'string',
        'profileTimes': [
            {
                'start': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    CodeGuruProfiler.Client.exceptions.InternalServerException
    CodeGuruProfiler.Client.exceptions.ValidationException
    CodeGuruProfiler.Client.exceptions.ThrottlingException
    CodeGuruProfiler.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_profiling_groups(includeDescription=None, maxResults=None, nextToken=None):
    """
    Lists profiling groups.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_profiling_groups(
        includeDescription=True|False,
        maxResults=123,
        nextToken='string'
    )
    
    
    :type includeDescription: boolean
    :param includeDescription: A Boolean value indicating whether to include a description.

    :type maxResults: integer
    :param maxResults: The maximum number of profiling groups results returned by ListProfilingGroups in paginated output. When this parameter is used, ListProfilingGroups only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListProfilingGroups request with the returned nextToken value.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListProfilingGroups request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'profilingGroupNames': [
        'string',
    ],
    'profilingGroups': [
        {
            'agentOrchestrationConfig': {
                'profilingEnabled': True|False
            },
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'name': 'string',
            'profilingStatus': {
                'latestAgentOrchestratedAt': datetime(2015, 1, 1),
                'latestAgentProfileReportedAt': datetime(2015, 1, 1),
                'latestAggregatedProfile': {
                    'period': 'P1D'|'PT1H'|'PT5M',
                    'start': datetime(2015, 1, 1)
                }
            },
            'updatedAt': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --
The structure representing the listProfilingGroupsResponse.

nextToken (string) --
The nextToken value to include in a future ListProfilingGroups request. When the results of a ListProfilingGroups request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.

profilingGroupNames (list) --
Information about profiling group names.

(string) --


profilingGroups (list) --
Information about profiling groups.

(dict) --
The description of a profiling group.

agentOrchestrationConfig (dict) --

profilingEnabled (boolean) --


arn (string) --
The Amazon Resource Name (ARN) identifying the profiling group.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the profiling group was created.

name (string) --
The name of the profiling group.

profilingStatus (dict) --
The status of the profiling group.

latestAgentOrchestratedAt (datetime) --
The time, in milliseconds since the epoch, when the latest agent was orchestrated.

latestAgentProfileReportedAt (datetime) --
The time, in milliseconds since the epoch, when the latest agent was reported..

latestAggregatedProfile (dict) --
The latest aggregated profile

period (string) --
The time period.

start (datetime) --
The start time.





updatedAt (datetime) --
The time, in milliseconds since the epoch, when the profiling group was last updated.











Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ThrottlingException


    :return: {
        'nextToken': 'string',
        'profilingGroupNames': [
            'string',
        ],
        'profilingGroups': [
            {
                'agentOrchestrationConfig': {
                    'profilingEnabled': True|False
                },
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'name': 'string',
                'profilingStatus': {
                    'latestAgentOrchestratedAt': datetime(2015, 1, 1),
                    'latestAgentProfileReportedAt': datetime(2015, 1, 1),
                    'latestAggregatedProfile': {
                        'period': 'P1D'|'PT1H'|'PT5M',
                        'start': datetime(2015, 1, 1)
                    }
                },
                'updatedAt': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def post_agent_profile(agentProfile=None, contentType=None, profileToken=None, profilingGroupName=None):
    """
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.post_agent_profile(
        agentProfile=b'bytes'|file,
        contentType='string',
        profileToken='string',
        profilingGroupName='string'
    )
    
    
    :type agentProfile: bytes or seekable file-like object
    :param agentProfile: [REQUIRED]

    :type contentType: string
    :param contentType: [REQUIRED]

    :type profileToken: string
    :param profileToken: This field is autopopulated if not provided.

    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The structure representing the postAgentProfileResponse.





Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    CodeGuruProfiler.Client.exceptions.InternalServerException
    CodeGuruProfiler.Client.exceptions.ValidationException
    CodeGuruProfiler.Client.exceptions.ThrottlingException
    CodeGuruProfiler.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def put_permission(actionGroup=None, principals=None, profilingGroupName=None, revisionId=None):
    """
    Provides permission to the principals. This overwrites the existing permissions, and is not additive.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_permission(
        actionGroup='agentPermissions',
        principals=[
            'string',
        ],
        profilingGroupName='string',
        revisionId='string'
    )
    
    
    :type actionGroup: string
    :param actionGroup: [REQUIRED]\nThe list of actions that the users and roles can perform on the profiling group.\n

    :type principals: list
    :param principals: [REQUIRED]\nThe list of role and user ARNs or the accountId that needs access (wildcards are not allowed).\n\n(string) --\n\n

    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]\nThe name of the profiling group.\n

    :type revisionId: string
    :param revisionId: A unique identifier for the current revision of the policy. This is required, if a policy exists for the profiling group. This is not required when creating the policy for the first time.

    :rtype: dict

ReturnsResponse Syntax
{
    'policy': 'string',
    'revisionId': 'string'
}


Response Structure

(dict) --
The structure representing the putPermissionResponse.

policy (string) --
The resource-based policy.

revisionId (string) --
A unique identifier for the current revision of the policy.







Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ConflictException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {
        'policy': 'string',
        'revisionId': 'string'
    }
    
    
    :returns: 
    CodeGuruProfiler.Client.exceptions.InternalServerException
    CodeGuruProfiler.Client.exceptions.ConflictException
    CodeGuruProfiler.Client.exceptions.ValidationException
    CodeGuruProfiler.Client.exceptions.ThrottlingException
    CodeGuruProfiler.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def remove_permission(actionGroup=None, profilingGroupName=None, revisionId=None):
    """
    Removes statement for the provided action group from the policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_permission(
        actionGroup='agentPermissions',
        profilingGroupName='string',
        revisionId='string'
    )
    
    
    :type actionGroup: string
    :param actionGroup: [REQUIRED]\nThe list of actions that the users and roles can perform on the profiling group.\n

    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]\nThe name of the profiling group.\n

    :type revisionId: string
    :param revisionId: [REQUIRED]\nA unique identifier for the current revision of the policy.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'policy': 'string',
    'revisionId': 'string'
}


Response Structure

(dict) --
The structure representing the removePermissionResponse.

policy (string) --
The resource-based policy.

revisionId (string) --
A unique identifier for the current revision of the policy.







Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ConflictException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {
        'policy': 'string',
        'revisionId': 'string'
    }
    
    
    :returns: 
    CodeGuruProfiler.Client.exceptions.InternalServerException
    CodeGuruProfiler.Client.exceptions.ConflictException
    CodeGuruProfiler.Client.exceptions.ValidationException
    CodeGuruProfiler.Client.exceptions.ThrottlingException
    CodeGuruProfiler.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_profiling_group(agentOrchestrationConfig=None, profilingGroupName=None):
    """
    Updates a profiling group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_profiling_group(
        agentOrchestrationConfig={
            'profilingEnabled': True|False
        },
        profilingGroupName='string'
    )
    
    
    :type agentOrchestrationConfig: dict
    :param agentOrchestrationConfig: [REQUIRED]\n\nprofilingEnabled (boolean) -- [REQUIRED]\n\n

    :type profilingGroupName: string
    :param profilingGroupName: [REQUIRED]\nThe name of the profiling group to update.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'profilingGroup': {
        'agentOrchestrationConfig': {
            'profilingEnabled': True|False
        },
        'arn': 'string',
        'createdAt': datetime(2015, 1, 1),
        'name': 'string',
        'profilingStatus': {
            'latestAgentOrchestratedAt': datetime(2015, 1, 1),
            'latestAgentProfileReportedAt': datetime(2015, 1, 1),
            'latestAggregatedProfile': {
                'period': 'P1D'|'PT1H'|'PT5M',
                'start': datetime(2015, 1, 1)
            }
        },
        'updatedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
The structure representing the updateProfilingGroupResponse.

profilingGroup (dict) --
Updated information about the profiling group.

agentOrchestrationConfig (dict) --

profilingEnabled (boolean) --


arn (string) --
The Amazon Resource Name (ARN) identifying the profiling group.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the profiling group was created.

name (string) --
The name of the profiling group.

profilingStatus (dict) --
The status of the profiling group.

latestAgentOrchestratedAt (datetime) --
The time, in milliseconds since the epoch, when the latest agent was orchestrated.

latestAgentProfileReportedAt (datetime) --
The time, in milliseconds since the epoch, when the latest agent was reported..

latestAggregatedProfile (dict) --
The latest aggregated profile

period (string) --
The time period.

start (datetime) --
The start time.





updatedAt (datetime) --
The time, in milliseconds since the epoch, when the profiling group was last updated.









Exceptions

CodeGuruProfiler.Client.exceptions.InternalServerException
CodeGuruProfiler.Client.exceptions.ConflictException
CodeGuruProfiler.Client.exceptions.ValidationException
CodeGuruProfiler.Client.exceptions.ThrottlingException
CodeGuruProfiler.Client.exceptions.ResourceNotFoundException


    :return: {
        'profilingGroup': {
            'agentOrchestrationConfig': {
                'profilingEnabled': True|False
            },
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'name': 'string',
            'profilingStatus': {
                'latestAgentOrchestratedAt': datetime(2015, 1, 1),
                'latestAgentProfileReportedAt': datetime(2015, 1, 1),
                'latestAggregatedProfile': {
                    'period': 'P1D'|'PT1H'|'PT5M',
                    'start': datetime(2015, 1, 1)
                }
            },
            'updatedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    profilingEnabled (boolean) --
    
    """
    pass

