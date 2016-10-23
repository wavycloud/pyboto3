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


def count_closed_workflow_executions(domain=None, startTimeFilter=None, closeTimeFilter=None, executionFilter=None,
                                     typeFilter=None, tagFilter=None, closeStatusFilter=None):
    """
    :param domain: [REQUIRED]
            The name of the domain containing the workflow executions to count.
            
    :type domain: string
    :param startTimeFilter: If specified, only workflow executions that meet the start time criteria of the filter are counted.
            Note
            startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            
    :type startTimeFilter: dict
    :param closeTimeFilter: If specified, only workflow executions that meet the close time criteria of the filter are counted.
            Note
            startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            
    :type closeTimeFilter: dict
    :param executionFilter: If specified, only workflow executions matching the WorkflowId in the filter are counted.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
            
    :type executionFilter: dict
    :param typeFilter: If specified, indicates the type of the workflow executions to be counted.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            name (string) -- [REQUIRED]Required. Name of the workflow type.
            version (string) --Version of the workflow type.
            
    :type typeFilter: dict
    :param tagFilter: If specified, only executions that have a tag that matches the filter are counted.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
            
    :type tagFilter: dict
    :param closeStatusFilter: If specified, only workflow executions that match this close status are counted. This filter has an affect only if executionStatus is specified as CLOSED .
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            status (string) -- [REQUIRED]Required. The close status that must match the close status of an execution for it to meet the criteria of this filter.
            
    :type closeStatusFilter: dict
    """
    pass


def count_open_workflow_executions(domain=None, startTimeFilter=None, typeFilter=None, tagFilter=None,
                                   executionFilter=None):
    """
    :param domain: [REQUIRED]
            The name of the domain containing the workflow executions to count.
            
    :type domain: string
    :param startTimeFilter: [REQUIRED]
            Specifies the start time criteria that workflow executions must meet in order to be counted.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            
    :type startTimeFilter: dict
    :param typeFilter: Specifies the type of the workflow executions to be counted.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            name (string) -- [REQUIRED]Required. Name of the workflow type.
            version (string) --Version of the workflow type.
            
    :type typeFilter: dict
    :param tagFilter: If specified, only executions that have a tag that matches the filter are counted.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
            
    :type tagFilter: dict
    :param executionFilter: If specified, only workflow executions matching the WorkflowId in the filter are counted.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
            
    :type executionFilter: dict
    """
    pass


def count_pending_activity_tasks(domain=None, taskList=None):
    """
    :param domain: [REQUIRED]
            The name of the domain that contains the task list.
            
    :type domain: string
    :param taskList: [REQUIRED]
            The name of the task list.
            name (string) -- [REQUIRED]The name of the task list.
            
    :type taskList: dict
    """
    pass


def count_pending_decision_tasks(domain=None, taskList=None):
    """
    :param domain: [REQUIRED]
            The name of the domain that contains the task list.
            
    :type domain: string
    :param taskList: [REQUIRED]
            The name of the task list.
            name (string) -- [REQUIRED]The name of the task list.
            
    :type taskList: dict
    """
    pass


def deprecate_activity_type(domain=None, activityType=None):
    """
    :param domain: [REQUIRED]
            The name of the domain in which the activity type is registered.
            
    :type domain: string
    :param activityType: [REQUIRED]
            The activity type to deprecate.
            name (string) -- [REQUIRED]The name of this activity.
            Note
            The combination of activity type name and version must be unique within a domain.
            version (string) -- [REQUIRED]The version of this activity.
            Note
            The combination of activity type name and version must be unique with in a domain.
            
    :type activityType: dict
    """
    pass


def deprecate_domain(name=None):
    """
    :param name: [REQUIRED]
            The name of the domain to deprecate.
            ReturnsNone
            
    :type name: string
    """
    pass


def deprecate_workflow_type(domain=None, workflowType=None):
    """
    :param domain: [REQUIRED]
            The name of the domain in which the workflow type is registered.
            
    :type domain: string
    :param workflowType: [REQUIRED]
            The workflow type to deprecate.
            name (string) -- [REQUIRED]Required. The name of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            version (string) -- [REQUIRED]Required. The version of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            
    :type workflowType: dict
    """
    pass


def describe_activity_type(domain=None, activityType=None):
    """
    :param domain: [REQUIRED]
            The name of the domain in which the activity type is registered.
            
    :type domain: string
    :param activityType: [REQUIRED]
            The activity type to get information about. Activity types are identified by the name and version that were supplied when the activity was registered.
            name (string) -- [REQUIRED]The name of this activity.
            Note
            The combination of activity type name and version must be unique within a domain.
            version (string) -- [REQUIRED]The version of this activity.
            Note
            The combination of activity type name and version must be unique with in a domain.
            
    :type activityType: dict
    """
    pass


def describe_domain(name=None):
    """
    :param name: [REQUIRED]
            The name of the domain to describe.
            Return typedict
            ReturnsResponse Syntax{
              'domainInfo': {
                'name': 'string',
                'status': 'REGISTERED'|'DEPRECATED',
                'description': 'string'
              },
              'configuration': {
                'workflowExecutionRetentionPeriodInDays': 'string'
              }
            }
            Response Structure
            (dict) --Contains details of a domain.
            domainInfo (dict) --Contains general information about a domain.
            name (string) --The name of the domain. This name is unique within the account.
            status (string) --The status of the domain:
            REGISTERED : The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions.
            DEPRECATED : The domain was deprecated using DeprecateDomain , but is still in use. You should not create new workflow executions in this domain.
            description (string) --The description of the domain provided through RegisterDomain .
            configuration (dict) --Contains the configuration settings of a domain.
            workflowExecutionRetentionPeriodInDays (string) --The retention period for workflow executions in this domain.
            
            
            
    :type name: string
    """
    pass


def describe_workflow_execution(domain=None, execution=None):
    """
    :param domain: [REQUIRED]
            The name of the domain containing the workflow execution.
            
    :type domain: string
    :param execution: [REQUIRED]
            The workflow execution to describe.
            workflowId (string) -- [REQUIRED]The user defined identifier associated with the workflow execution.
            runId (string) -- [REQUIRED]A system-generated unique identifier for the workflow execution.
            
    :type execution: dict
    """
    pass


def describe_workflow_type(domain=None, workflowType=None):
    """
    :param domain: [REQUIRED]
            The name of the domain in which this workflow type is registered.
            
    :type domain: string
    :param workflowType: [REQUIRED]
            The workflow type to describe.
            name (string) -- [REQUIRED]Required. The name of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            version (string) -- [REQUIRED]Required. The version of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            
    :type workflowType: dict
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


def get_workflow_execution_history(domain=None, execution=None, nextPageToken=None, maximumPageSize=None,
                                   reverseOrder=None):
    """
    :param domain: [REQUIRED]
            The name of the domain containing the workflow execution.
            
    :type domain: string
    :param execution: [REQUIRED]
            Specifies the workflow execution for which to return the history.
            workflowId (string) -- [REQUIRED]The user defined identifier associated with the workflow execution.
            runId (string) -- [REQUIRED]A system-generated unique identifier for the workflow execution.
            
    :type execution: dict
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            
    :type nextPageToken: string
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            
    :type maximumPageSize: integer
    :param reverseOrder: When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimeStamp of the events.
    :type reverseOrder: boolean
    """
    pass


def list_activity_types(domain=None, name=None, registrationStatus=None, nextPageToken=None, maximumPageSize=None,
                        reverseOrder=None):
    """
    :param domain: [REQUIRED]
            The name of the domain in which the activity types have been registered.
            
    :type domain: string
    :param name: If specified, only lists the activity types that have this name.
    :type name: string
    :param registrationStatus: [REQUIRED]
            Specifies the registration status of the activity types to list.
            
    :type registrationStatus: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            
    :type nextPageToken: string
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            
    :type maximumPageSize: integer
    :param reverseOrder: When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the activity types.
    :type reverseOrder: boolean
    """
    pass


def list_closed_workflow_executions(domain=None, startTimeFilter=None, closeTimeFilter=None, executionFilter=None,
                                    closeStatusFilter=None, typeFilter=None, tagFilter=None, nextPageToken=None,
                                    maximumPageSize=None, reverseOrder=None):
    """
    :param domain: [REQUIRED]
            The name of the domain that contains the workflow executions to list.
            
    :type domain: string
    :param startTimeFilter: If specified, the workflow executions are included in the returned results based on whether their start times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their start times.
            Note
            startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            
    :type startTimeFilter: dict
    :param closeTimeFilter: If specified, the workflow executions are included in the returned results based on whether their close times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their close times.
            Note
            startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            
    :type closeTimeFilter: dict
    :param executionFilter: If specified, only workflow executions matching the workflow ID specified in the filter are returned.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
            
    :type executionFilter: dict
    :param closeStatusFilter: If specified, only workflow executions that match this close status are listed. For example, if TERMINATED is specified, then only TERMINATED workflow executions are listed.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            status (string) -- [REQUIRED]Required. The close status that must match the close status of an execution for it to meet the criteria of this filter.
            
    :type closeStatusFilter: dict
    :param typeFilter: If specified, only executions of the type specified in the filter are returned.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            name (string) -- [REQUIRED]Required. Name of the workflow type.
            version (string) --Version of the workflow type.
            
    :type typeFilter: dict
    :param tagFilter: If specified, only executions that have the matching tag are listed.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
            
    :type tagFilter: dict
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            
    :type nextPageToken: string
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            
    :type maximumPageSize: integer
    :param reverseOrder: When set to true , returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.
    :type reverseOrder: boolean
    """
    pass


def list_domains(nextPageToken=None, registrationStatus=None, maximumPageSize=None, reverseOrder=None):
    """
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            
    :type nextPageToken: string
    :param registrationStatus: [REQUIRED]
            Specifies the registration status of the domains to list.
            
    :type registrationStatus: string
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            
    :type maximumPageSize: integer
    :param reverseOrder: When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the domains.
    :type reverseOrder: boolean
    """
    pass


def list_open_workflow_executions(domain=None, startTimeFilter=None, typeFilter=None, tagFilter=None,
                                  nextPageToken=None, maximumPageSize=None, reverseOrder=None, executionFilter=None):
    """
    :param domain: [REQUIRED]
            The name of the domain that contains the workflow executions to list.
            
    :type domain: string
    :param startTimeFilter: [REQUIRED]
            Workflow executions are included in the returned results based on whether their start times are within the range specified by this filter.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            
    :type startTimeFilter: dict
    :param typeFilter: If specified, only executions of the type specified in the filter are returned.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            name (string) -- [REQUIRED]Required. Name of the workflow type.
            version (string) --Version of the workflow type.
            
    :type typeFilter: dict
    :param tagFilter: If specified, only executions that have the matching tag are listed.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
            
    :type tagFilter: dict
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            
    :type nextPageToken: string
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            
    :type maximumPageSize: integer
    :param reverseOrder: When set to true , returns the results in reverse order. By default the results are returned in descending order of the start time of the executions.
    :type reverseOrder: boolean
    :param executionFilter: If specified, only workflow executions matching the workflow ID specified in the filter are returned.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
            
    :type executionFilter: dict
    """
    pass


def list_workflow_types(domain=None, name=None, registrationStatus=None, nextPageToken=None, maximumPageSize=None,
                        reverseOrder=None):
    """
    :param domain: [REQUIRED]
            The name of the domain in which the workflow types have been registered.
            
    :type domain: string
    :param name: If specified, lists the workflow type with this name.
    :type name: string
    :param registrationStatus: [REQUIRED]
            Specifies the registration status of the workflow types to list.
            
    :type registrationStatus: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            
    :type nextPageToken: string
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            
    :type maximumPageSize: integer
    :param reverseOrder: When set to true , returns the results in reverse order. By default the results are returned in ascending alphabetical order of the name of the workflow types.
    :type reverseOrder: boolean
    """
    pass


def poll_for_activity_task(domain=None, taskList=None, identity=None):
    """
    :param domain: [REQUIRED]
            The name of the domain that contains the task lists being polled.
            
    :type domain: string
    :param taskList: [REQUIRED]
            Specifies the task list to poll for activity tasks.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            name (string) -- [REQUIRED]The name of the task list.
            
    :type taskList: dict
    :param identity: Identity of the worker making the request, recorded in the ActivityTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
    :type identity: string
    """
    pass


def poll_for_decision_task(domain=None, taskList=None, identity=None, nextPageToken=None, maximumPageSize=None,
                           reverseOrder=None):
    """
    :param domain: [REQUIRED]
            The name of the domain containing the task lists to poll.
            
    :type domain: string
    :param taskList: [REQUIRED]
            Specifies the task list to poll for decision tasks.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            name (string) -- [REQUIRED]The name of the task list.
            
    :type taskList: dict
    :param identity: Identity of the decider making the request, which is recorded in the DecisionTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
    :type identity: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            Note
            The nextPageToken returned by this action cannot be used with GetWorkflowExecutionHistory to get the next page. You must call PollForDecisionTask again (with the nextPageToken ) to retrieve the next page of history records. Calling PollForDecisionTask with a nextPageToken will not return a new decision task.
            .
            
    :type nextPageToken: string
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            
    :type maximumPageSize: integer
    :param reverseOrder: When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimestamp of the events.
    :type reverseOrder: boolean
    """
    pass


def record_activity_task_heartbeat(taskToken=None, details=None):
    """
    :param taskToken: [REQUIRED]
            The taskToken of the ActivityTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            
    :type taskToken: string
    :param details: If specified, contains details about the progress of the task.
    :type details: string
    """
    pass


def register_activity_type(domain=None, name=None, version=None, description=None, defaultTaskStartToCloseTimeout=None,
                           defaultTaskHeartbeatTimeout=None, defaultTaskList=None, defaultTaskPriority=None,
                           defaultTaskScheduleToStartTimeout=None, defaultTaskScheduleToCloseTimeout=None):
    """
    :param domain: [REQUIRED]
            The name of the domain in which this activity is to be registered.
            
    :type domain: string
    :param name: [REQUIRED]
            The name of the activity type within the domain.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            
    :type name: string
    :param version: [REQUIRED]
            The version of the activity type.
            Note
            The activity type consists of the name and version, the combination of which must be unique within the domain.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            
    :type version: string
    :param description: A textual description of the activity type.
    :type description: string
    :param defaultTaskStartToCloseTimeout: If set, specifies the default maximum duration that a worker can take to process tasks of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            
    :type defaultTaskStartToCloseTimeout: string
    :param defaultTaskHeartbeatTimeout: If set, specifies the default maximum time before which a worker processing a task of this type must report progress by calling RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision. If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an UnknownResource fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            
    :type defaultTaskHeartbeatTimeout: string
    :param defaultTaskList: If set, specifies the default task list to use for scheduling tasks of this activity type. This default task list is used if a task list is not provided when a task is scheduled through the ScheduleActivityTask decision.
            name (string) -- [REQUIRED]The name of the task list.
            
    :type defaultTaskList: dict
    :param defaultTaskPriority: The default task priority to assign to the activity type. If not assigned, then '0' will be used. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
            For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
            
    :type defaultTaskPriority: string
    :param defaultTaskScheduleToStartTimeout: If set, specifies the default maximum duration that a task of this activity type can wait before being assigned to a worker. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            
    :type defaultTaskScheduleToStartTimeout: string
    :param defaultTaskScheduleToCloseTimeout: If set, specifies the default maximum duration for a task of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            
    :type defaultTaskScheduleToCloseTimeout: string
    """
    pass


def register_domain(name=None, description=None, workflowExecutionRetentionPeriodInDays=None):
    """
    :param name: [REQUIRED]
            Name of the domain to register. The name must be unique in the region that the domain is registered in.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            
    :type name: string
    :param description: A text description of the domain.
    :type description: string
    :param workflowExecutionRetentionPeriodInDays: [REQUIRED]
            The duration (in days) that records and histories of workflow executions on the domain should be kept by the service. After the retention period, the workflow execution is not available in the results of visibility calls.
            If you pass the value NONE or 0 (zero), then the workflow execution history will not be retained. As soon as the workflow execution completes, the execution record and its history are deleted.
            The maximum workflow execution retention period is 90 days. For more information about Amazon SWF service limits, see: Amazon SWF Service Limits in the Amazon SWF Developer Guide .
            
    :type workflowExecutionRetentionPeriodInDays: string
    """
    pass


def register_workflow_type(domain=None, name=None, version=None, description=None, defaultTaskStartToCloseTimeout=None,
                           defaultExecutionStartToCloseTimeout=None, defaultTaskList=None, defaultTaskPriority=None,
                           defaultChildPolicy=None, defaultLambdaRole=None):
    """
    :param domain: [REQUIRED]
            The name of the domain in which to register the workflow type.
            
    :type domain: string
    :param name: [REQUIRED]
            The name of the workflow type.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            
    :type name: string
    :param version: [REQUIRED]
            The version of the workflow type.
            Note
            The workflow type consists of the name and version, the combination of which must be unique within the domain. To get a list of all currently registered workflow types, use the ListWorkflowTypes action.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            
    :type version: string
    :param description: Textual description of the workflow type.
    :type description: string
    :param defaultTaskStartToCloseTimeout: If set, specifies the default maximum duration of decision tasks for this workflow type. This default can be overridden when starting a workflow execution using the StartWorkflowExecution action or the StartChildWorkflowExecution decision.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            
    :type defaultTaskStartToCloseTimeout: string
    :param defaultExecutionStartToCloseTimeout: If set, specifies the default maximum duration for executions of this workflow type. You can override this default when starting an execution through the StartWorkflowExecution action or StartChildWorkflowExecution decision.
            The duration is specified in seconds; an integer greater than or equal to 0. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of 'NONE' for defaultExecutionStartToCloseTimeout ; there is a one-year max limit on the time that a workflow execution can run. Exceeding this limit will always cause the workflow execution to time out.
            
    :type defaultExecutionStartToCloseTimeout: string
    :param defaultTaskList: If set, specifies the default task list to use for scheduling decision tasks for executions of this workflow type. This default is used only if a task list is not provided when starting the execution through the StartWorkflowExecution action or StartChildWorkflowExecution decision.
            name (string) -- [REQUIRED]The name of the task list.
            
    :type defaultTaskList: dict
    :param defaultTaskPriority: The default task priority to assign to the workflow type. If not assigned, then '0' will be used. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
            For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
            
    :type defaultTaskPriority: string
    :param defaultChildPolicy: If set, specifies the default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the StartWorkflowExecution action or the StartChildWorkflowExecution decision.
            The supported child policies are:
            TERMINATE: the child executions will be terminated.
            REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
            ABANDON: no action will be taken. The child executions will continue to run.
            
    :type defaultChildPolicy: string
    :param defaultLambdaRole: The ARN of the default IAM role to use when a workflow execution of this type invokes AWS Lambda functions.
            This default can be overridden when starting a workflow execution using the StartWorkflowExecution action or the StartChildWorkflowExecution and ContinueAsNewWorkflowExecution decision.
            
    :type defaultLambdaRole: string
    """
    pass


def request_cancel_workflow_execution(domain=None, workflowId=None, runId=None):
    """
    :param domain: [REQUIRED]
            The name of the domain containing the workflow execution to cancel.
            
    :type domain: string
    :param workflowId: [REQUIRED]
            The workflowId of the workflow execution to cancel.
            
    :type workflowId: string
    :param runId: The runId of the workflow execution to cancel.
    :type runId: string
    """
    pass


def respond_activity_task_canceled(taskToken=None, details=None):
    """
    :param taskToken: [REQUIRED]
            The taskToken of the ActivityTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            
    :type taskToken: string
    :param details: Optional. Information about the cancellation.
    :type details: string
    """
    pass


def respond_activity_task_completed(taskToken=None, result=None):
    """
    :param taskToken: [REQUIRED]
            The taskToken of the ActivityTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            
    :type taskToken: string
    :param result: The result of the activity task. It is a free form string that is implementation specific.
    :type result: string
    """
    pass


def respond_activity_task_failed(taskToken=None, reason=None, details=None):
    """
    :param taskToken: [REQUIRED]
            The taskToken of the ActivityTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            
    :type taskToken: string
    :param reason: Description of the error that may assist in diagnostics.
    :type reason: string
    :param details: Optional. Detailed information about the failure.
    :type details: string
    """
    pass


def respond_decision_task_completed(taskToken=None, decisions=None, executionContext=None):
    """
    :param taskToken: [REQUIRED]
            The taskToken from the DecisionTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            
    :type taskToken: string
    :param decisions: The list of decisions (possibly empty) made by the decider while processing this decision task. See the docs for the decision structure for details.
            (dict) --Specifies a decision made by the decider. A decision can be one of these types:
            CancelTimer : cancels a previously started timer and records a TimerCanceled event in the history.
            CancelWorkflowExecution : closes the workflow execution and records a WorkflowExecutionCanceled event in the history.
            CompleteWorkflowExecution : closes the workflow execution and records a WorkflowExecutionCompleted event in the history .
            ContinueAsNewWorkflowExecution : closes the workflow execution and starts a new workflow execution of the same type using the same workflow ID and a unique run ID. A WorkflowExecutionContinuedAsNew event is recorded in the history.
            FailWorkflowExecution : closes the workflow execution and records a WorkflowExecutionFailed event in the history.
            RecordMarker : records a MarkerRecorded event in the history. Markers can be used for adding custom information in the history for instance to let deciders know that they do not need to look at the history beyond the marker event.
            RequestCancelActivityTask : attempts to cancel a previously scheduled activity task. If the activity task was scheduled but has not been assigned to a worker, then it will be canceled. If the activity task was already assigned to a worker, then the worker will be informed that cancellation has been requested in the response to RecordActivityTaskHeartbeat .
            RequestCancelExternalWorkflowExecution : requests that a request be made to cancel the specified external workflow execution and records a RequestCancelExternalWorkflowExecutionInitiated event in the history.
            ScheduleActivityTask : schedules an activity task.
            ScheduleLambdaFunction : schedules a AWS Lambda function.
            SignalExternalWorkflowExecution : requests a signal to be delivered to the specified external workflow execution and records a SignalExternalWorkflowExecutionInitiated event in the history.
            StartChildWorkflowExecution : requests that a child workflow execution be started and records a StartChildWorkflowExecutionInitiated event in the history. The child workflow execution is a separate workflow execution with its own history.
            StartTimer : starts a timer for this workflow execution and records a TimerStarted event in the history. This timer will fire after the specified delay and record a TimerFired event.
            Access Control
            If you grant permission to use RespondDecisionTaskCompleted , you can use IAM policies to express permissions for the list of decisions returned by this action as if they were members of the API. Treating decisions as a pseudo API maintains a uniform conceptual model and helps keep policies readable. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
            Decision Failure
            Decisions can fail for several reasons
            The ordering of decisions should follow a logical flow. Some decisions might not make sense in the current context of the workflow execution and will therefore fail.
            A limit on your account was reached.
            The decision lacks sufficient permissions.
            One of the following events might be added to the history to indicate an error. The event attribute's cause parameter indicates the cause. If cause is set to OPERATION_NOT_PERMITTED, the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
            ScheduleActivityTaskFailed : a ScheduleActivityTask decision failed. This could happen if the activity type specified in the decision is not registered, is in a deprecated state, or the decision is not properly configured.
            ScheduleLambdaFunctionFailed : a ScheduleLambdaFunctionFailed decision failed. This could happen if the AWS Lambda function specified in the decision does not exist, or the AWS Lambda service's limits are exceeded.
            RequestCancelActivityTaskFailed : a RequestCancelActivityTask decision failed. This could happen if there is no open activity task with the specified activityId.
            StartTimerFailed : a StartTimer decision failed. This could happen if there is another open timer with the same timerId.
            CancelTimerFailed : a CancelTimer decision failed. This could happen if there is no open timer with the specified timerId.
            StartChildWorkflowExecutionFailed : a StartChildWorkflowExecution decision failed. This could happen if the workflow type specified is not registered, is deprecated, or the decision is not properly configured.
            SignalExternalWorkflowExecutionFailed : a SignalExternalWorkflowExecution decision failed. This could happen if the workflowID specified in the decision was incorrect.
            RequestCancelExternalWorkflowExecutionFailed : a RequestCancelExternalWorkflowExecution decision failed. This could happen if the workflowID specified in the decision was incorrect.
            CancelWorkflowExecutionFailed : a CancelWorkflowExecution decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.
            CompleteWorkflowExecutionFailed : a CompleteWorkflowExecution decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.
            ContinueAsNewWorkflowExecutionFailed : a ContinueAsNewWorkflowExecution decision failed. This could happen if there is an unhandled decision task pending in the workflow execution or the ContinueAsNewWorkflowExecution decision was not configured correctly.
            FailWorkflowExecutionFailed : a FailWorkflowExecution decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.
            The preceding error events might occur due to an error in the decider logic, which might put the workflow execution in an unstable state The cause field in the event structure for the error event indicates the cause of the error.
            Note
            A workflow execution may be closed by the decider by returning one of the following decisions when completing a decision task: CompleteWorkflowExecution , FailWorkflowExecution , CancelWorkflowExecution and ContinueAsNewWorkflowExecution . An UnhandledDecision fault will be returned if a workflow closing decision is specified and a signal or activity event had been added to the history while the decision task was being performed by the decider. Unlike the above situations which are logic issues, this fault is always possible because of race conditions in a distributed system. The right action here is to call RespondDecisionTaskCompleted without any decisions. This would result in another decision task with these new events included in the history. The decider should handle the new events and may decide to close the workflow execution.
            How to code a decision
            You code a decision by first setting the decision type field to one of the above decision values, and then set the corresponding attributes field shown below:
            ScheduleActivityTaskDecisionAttributes
            ScheduleLambdaFunctionDecisionAttributes
            RequestCancelActivityTaskDecisionAttributes
            CompleteWorkflowExecutionDecisionAttributes
            FailWorkflowExecutionDecisionAttributes
            CancelWorkflowExecutionDecisionAttributes
            ContinueAsNewWorkflowExecutionDecisionAttributes
            RecordMarkerDecisionAttributes
            StartTimerDecisionAttributes
            CancelTimerDecisionAttributes
            SignalExternalWorkflowExecutionDecisionAttributes
            RequestCancelExternalWorkflowExecutionDecisionAttributes
            StartChildWorkflowExecutionDecisionAttributes
            decisionType (string) -- [REQUIRED]Specifies the type of the decision.
            scheduleActivityTaskDecisionAttributes (dict) --Provides details of the ScheduleActivityTask decision. It is not set for other decision types.
            activityType (dict) -- [REQUIRED]Required. The type of the activity task to schedule.
            name (string) -- [REQUIRED]The name of this activity.
            Note
            The combination of activity type name and version must be unique within a domain.
            version (string) -- [REQUIRED]The version of this activity.
            Note
            The combination of activity type name and version must be unique with in a domain.
            
            activityId (string) -- [REQUIRED]Required. The activityId of the activity task.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            control (string) --Optional. Data attached to the event that can be used by the decider in subsequent workflow tasks. This data is not sent to the activity.
            input (string) --The input provided to the activity task.
            scheduleToCloseTimeout (string) --The maximum duration for this activity task.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            Note
            A schedule-to-close timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default schedule-to-close timeout was specified at registration time then a fault will be returned.
            taskList (dict) --If set, specifies the name of the task list in which to schedule the activity task. If not specified, the defaultTaskList registered with the activity type will be used.
            Note
            A task list for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default task list was specified at registration time then a fault will be returned.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            name (string) -- [REQUIRED]The name of the task list.
            taskPriority (string) --Optional. If set, specifies the priority with which the activity task is to be assigned to a worker. This overrides the defaultTaskPriority specified when registering the activity type using RegisterActivityType . Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
            For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
            scheduleToStartTimeout (string) --Optional. If set, specifies the maximum duration the activity task can wait to be assigned to a worker. This overrides the default schedule-to-start timeout specified when registering the activity type using RegisterActivityType .
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            Note
            A schedule-to-start timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default schedule-to-start timeout was specified at registration time then a fault will be returned.
            startToCloseTimeout (string) --If set, specifies the maximum duration a worker may take to process this activity task. This overrides the default start-to-close timeout specified when registering the activity type using RegisterActivityType .
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            Note
            A start-to-close timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default start-to-close timeout was specified at registration time then a fault will be returned.
            heartbeatTimeout (string) --If set, specifies the maximum time before which a worker processing a task of this type must report progress by calling RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or returns a result, it will be ignored. This overrides the default heartbeat timeout specified when registering the activity type using RegisterActivityType .
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            requestCancelActivityTaskDecisionAttributes (dict) --Provides details of the RequestCancelActivityTask decision. It is not set for other decision types.
            activityId (string) -- [REQUIRED]The activityId of the activity task to be canceled.
            completeWorkflowExecutionDecisionAttributes (dict) --Provides details of the CompleteWorkflowExecution decision. It is not set for other decision types.
            result (string) --The result of the workflow execution. The form of the result is implementation defined.
            failWorkflowExecutionDecisionAttributes (dict) --Provides details of the FailWorkflowExecution decision. It is not set for other decision types.
            reason (string) --A descriptive reason for the failure that may help in diagnostics.
            details (string) --Optional. Details of the failure.
            cancelWorkflowExecutionDecisionAttributes (dict) --Provides details of the CancelWorkflowExecution decision. It is not set for other decision types.
            details (string) --Optional. details of the cancellation.
            continueAsNewWorkflowExecutionDecisionAttributes (dict) --Provides details of the ContinueAsNewWorkflowExecution decision. It is not set for other decision types.
            input (string) --The input provided to the new workflow execution.
            executionStartToCloseTimeout (string) --If set, specifies the total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            Note
            An execution start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this field. If neither this field is set nor a default execution start-to-close timeout was specified at registration time then a fault will be returned.
            taskList (dict) --Represents a task list.
            name (string) -- [REQUIRED]The name of the task list.
            taskPriority (string) --Optional. The task priority that, if set, specifies the priority for the decision tasks for this workflow execution. This overrides the defaultTaskPriority specified when registering the workflow type. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
            For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
            taskStartToCloseTimeout (string) --Specifies the maximum duration of decision tasks for the new workflow execution. This parameter overrides the defaultTaskStartToCloseTimout specified when registering the workflow type using RegisterWorkflowType .
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            Note
            A task start-to-close timeout for the new workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault will be returned.
            childPolicy (string) --If set, specifies the policy to use for the child workflow executions of the new execution if it is terminated by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using RegisterWorkflowType .
            The supported child policies are:
            TERMINATE: the child executions will be terminated.
            REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
            ABANDON: no action will be taken. The child executions will continue to run.
            Note
            A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault will be returned.
            tagList (list) --The list of tags to associate with the new workflow execution. A maximum of 5 tags can be specified. You can list workflow executions with a specific tag by calling ListOpenWorkflowExecutions or ListClosedWorkflowExecutions and specifying a TagFilter .
            (string) --
            workflowTypeVersion (string) --
            lambdaRole (string) --The ARN of an IAM role that authorizes Amazon SWF to invoke AWS Lambda functions.
            Note
            In order for this workflow execution to invoke AWS Lambda functions, an appropriate IAM role must be specified either as a default for the workflow type or through this field.
            
            recordMarkerDecisionAttributes (dict) --Provides details of the RecordMarker decision. It is not set for other decision types.
            markerName (string) -- [REQUIRED]Required. The name of the marker.
            details (string) --Optional. details of the marker.
            startTimerDecisionAttributes (dict) --Provides details of the StartTimer decision. It is not set for other decision types.
            timerId (string) -- [REQUIRED]Required. The unique ID of the timer.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            control (string) --Optional. Data attached to the event that can be used by the decider in subsequent workflow tasks.
            startToFireTimeout (string) -- [REQUIRED]Required. The duration to wait before firing the timer.
            The duration is specified in seconds; an integer greater than or equal to 0.
            cancelTimerDecisionAttributes (dict) --Provides details of the CancelTimer decision. It is not set for other decision types.
            timerId (string) -- [REQUIRED]Required. The unique ID of the timer to cancel.
            signalExternalWorkflowExecutionDecisionAttributes (dict) --Provides details of the SignalExternalWorkflowExecution decision. It is not set for other decision types.
            workflowId (string) -- [REQUIRED]Required. The workflowId of the workflow execution to be signaled.
            runId (string) --The runId of the workflow execution to be signaled.
            signalName (string) -- [REQUIRED]Required. The name of the signal.The target workflow execution will use the signal name and input to process the signal.
            input (string) --Optional. Input data to be provided with the signal. The target workflow execution will use the signal name and input data to process the signal.
            control (string) --Optional. Data attached to the event that can be used by the decider in subsequent decision tasks.
            requestCancelExternalWorkflowExecutionDecisionAttributes (dict) --Provides details of the RequestCancelExternalWorkflowExecution decision. It is not set for other decision types.
            workflowId (string) -- [REQUIRED]Required. The workflowId of the external workflow execution to cancel.
            runId (string) --The runId of the external workflow execution to cancel.
            control (string) --Optional. Data attached to the event that can be used by the decider in subsequent workflow tasks.
            startChildWorkflowExecutionDecisionAttributes (dict) --Provides details of the StartChildWorkflowExecution decision. It is not set for other decision types.
            workflowType (dict) -- [REQUIRED]Required. The type of the workflow execution to be started.
            name (string) -- [REQUIRED]Required. The name of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            version (string) -- [REQUIRED]Required. The version of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            
            workflowId (string) -- [REQUIRED]Required. The workflowId of the workflow execution.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            control (string) --Optional. Data attached to the event that can be used by the decider in subsequent workflow tasks. This data is not sent to the child workflow execution.
            input (string) --The input to be provided to the workflow execution.
            executionStartToCloseTimeout (string) --The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            Note
            An execution start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default execution start-to-close timeout was specified at registration time then a fault will be returned.
            taskList (dict) --The name of the task list to be used for decision tasks of the child workflow execution.
            Note
            A task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault will be returned.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            name (string) -- [REQUIRED]The name of the task list.
            taskPriority (string) --Optional. A task priority that, if set, specifies the priority for a decision task of this workflow execution. This overrides the defaultTaskPriority specified when registering the workflow type. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
            For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
            taskStartToCloseTimeout (string) --Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the defaultTaskStartToCloseTimout specified when registering the workflow type using RegisterWorkflowType .
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            Note
            A task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault will be returned.
            childPolicy (string) --Optional. If set, specifies the policy to use for the child workflow executions if the workflow execution being started is terminated by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using RegisterWorkflowType .
            The supported child policies are:
            TERMINATE: the child executions will be terminated.
            REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
            ABANDON: no action will be taken. The child executions will continue to run.
            Note
            A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault will be returned.
            tagList (list) --The list of tags to associate with the child workflow execution. A maximum of 5 tags can be specified. You can list workflow executions with a specific tag by calling ListOpenWorkflowExecutions or ListClosedWorkflowExecutions and specifying a TagFilter .
            (string) --
            lambdaRole (string) --The ARN of an IAM role that authorizes Amazon SWF to invoke AWS Lambda functions.
            Note
            In order for this workflow execution to invoke AWS Lambda functions, an appropriate IAM role must be specified either as a default for the workflow type or through this field.
            
            scheduleLambdaFunctionDecisionAttributes (dict) --Provides details of the ScheduleLambdaFunction decision.
            Access Control
            You can use IAM policies to control this decision's access to Amazon SWF resources as follows:
            Use a Resource element with the domain name to limit the action to only specified domains.
            Use an Action element to allow or deny permission to call this action.
            Constrain the following parameters by using a Condition element with the appropriate keys.
            activityType.name : String constraint. The key is swf:activityType.name .
            activityType.version : String constraint. The key is swf:activityType.version .
            taskList : String constraint. The key is swf:taskList.name .
            If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
            id (string) -- [REQUIRED]Required. The SWF id of the AWS Lambda task.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            name (string) -- [REQUIRED]Required. The name of the AWS Lambda function to invoke.
            input (string) --The input provided to the AWS Lambda function.
            startToCloseTimeout (string) --If set, specifies the maximum duration the function may take to execute.
            
            
    :type decisions: list
    :param executionContext: User defined context to add to workflow execution.
    :type executionContext: string
    """
    pass


def signal_workflow_execution(domain=None, workflowId=None, runId=None, signalName=None, input=None):
    """
    :param domain: [REQUIRED]
            The name of the domain containing the workflow execution to signal.
            
    :type domain: string
    :param workflowId: [REQUIRED]
            The workflowId of the workflow execution to signal.
            
    :type workflowId: string
    :param runId: The runId of the workflow execution to signal.
    :type runId: string
    :param signalName: [REQUIRED]
            The name of the signal. This name must be meaningful to the target workflow.
            
    :type signalName: string
    :param input: Data to attach to the WorkflowExecutionSignaled event in the target workflow execution's history.
    :type input: string
    """
    pass


def start_workflow_execution(domain=None, workflowId=None, workflowType=None, taskList=None, taskPriority=None,
                             input=None, executionStartToCloseTimeout=None, tagList=None, taskStartToCloseTimeout=None,
                             childPolicy=None, lambdaRole=None):
    """
    :param domain: [REQUIRED]
            The name of the domain in which the workflow execution is created.
            
    :type domain: string
    :param workflowId: [REQUIRED]
            The user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a restart of a previous execution. You cannot have two open workflow executions with the same workflowId at the same time.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            
    :type workflowId: string
    :param workflowType: [REQUIRED]
            The type of the workflow to start.
            name (string) -- [REQUIRED]Required. The name of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            version (string) -- [REQUIRED]Required. The version of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            
    :type workflowType: dict
    :param taskList: The task list to use for the decision tasks generated for this workflow execution. This overrides the defaultTaskList specified when registering the workflow type.
            Note
            A task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault will be returned.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            name (string) -- [REQUIRED]The name of the task list.
            
    :type taskList: dict
    :param taskPriority: The task priority to use for this workflow execution. This will override any default priority that was assigned when the workflow type was registered. If not set, then the default task priority for the workflow type will be used. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
            For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
            
    :type taskPriority: string
    :param input: The input for the workflow execution. This is a free form string which should be meaningful to the workflow you are starting. This input is made available to the new workflow execution in the WorkflowExecutionStarted history event.
    :type input: string
    :param executionStartToCloseTimeout: The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.
            The duration is specified in seconds; an integer greater than or equal to 0. Exceeding this limit will cause the workflow execution to time out. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of 'NONE' for this timeout; there is a one-year max limit on the time that a workflow execution can run.
            Note
            An execution start-to-close timeout must be specified either through this parameter or as a default when the workflow type is registered. If neither this parameter nor a default execution start-to-close timeout is specified, a fault is returned.
            
    :type executionStartToCloseTimeout: string
    :param tagList: The list of tags to associate with the workflow execution. You can specify a maximum of 5 tags. You can list workflow executions with a specific tag by calling ListOpenWorkflowExecutions or ListClosedWorkflowExecutions and specifying a TagFilter .
            (string) --
            
    :type tagList: list
    :param taskStartToCloseTimeout: Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the defaultTaskStartToCloseTimout specified when registering the workflow type using RegisterWorkflowType .
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            Note
            A task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault will be returned.
            
    :type taskStartToCloseTimeout: string
    :param childPolicy: If set, specifies the policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using RegisterWorkflowType .
            The supported child policies are:
            TERMINATE: the child executions will be terminated.
            REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
            ABANDON: no action will be taken. The child executions will continue to run.
            Note
            A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault will be returned.
            
    :type childPolicy: string
    :param lambdaRole: The ARN of an IAM role that authorizes Amazon SWF to invoke AWS Lambda functions.
            Note
            In order for this workflow execution to invoke AWS Lambda functions, an appropriate IAM role must be specified either as a default for the workflow type or through this field.
            
    :type lambdaRole: string
    """
    pass


def terminate_workflow_execution(domain=None, workflowId=None, runId=None, reason=None, details=None, childPolicy=None):
    """
    :param domain: [REQUIRED]
            The domain of the workflow execution to terminate.
            
    :type domain: string
    :param workflowId: [REQUIRED]
            The workflowId of the workflow execution to terminate.
            
    :type workflowId: string
    :param runId: The runId of the workflow execution to terminate.
    :type runId: string
    :param reason: Optional. A descriptive reason for terminating the workflow execution.
    :type reason: string
    :param details: Optional. Details for terminating the workflow execution.
    :type details: string
    :param childPolicy: If set, specifies the policy to use for the child workflow executions of the workflow execution being terminated. This policy overrides the child policy specified for the workflow execution at registration time or when starting the execution.
            The supported child policies are:
            TERMINATE: the child executions will be terminated.
            REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
            ABANDON: no action will be taken. The child executions will continue to run.
            Note
            A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault will be returned.
            
    :type childPolicy: string
    """
    pass
