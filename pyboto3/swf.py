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

def count_closed_workflow_executions(domain=None, startTimeFilter=None, closeTimeFilter=None, executionFilter=None, typeFilter=None, tagFilter=None, closeStatusFilter=None):
    """
    Returns the number of closed workflow executions within the given domain that meet the specified filtering criteria.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.count_closed_workflow_executions(
        domain='string',
        startTimeFilter={
            'oldestDate': datetime(2015, 1, 1),
            'latestDate': datetime(2015, 1, 1)
        },
        closeTimeFilter={
            'oldestDate': datetime(2015, 1, 1),
            'latestDate': datetime(2015, 1, 1)
        },
        executionFilter={
            'workflowId': 'string'
        },
        typeFilter={
            'name': 'string',
            'version': 'string'
        },
        tagFilter={
            'tag': 'string'
        },
        closeStatusFilter={
            'status': 'COMPLETED'|'FAILED'|'CANCELED'|'TERMINATED'|'CONTINUED_AS_NEW'|'TIMED_OUT'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain containing the workflow executions to count.\n

    :type startTimeFilter: dict
    :param startTimeFilter: If specified, only workflow executions that meet the start time criteria of the filter are counted.\n\nNote\nstartTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.\n\n\noldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.\n\nlatestDate (datetime) --Specifies the latest start or close date and time to return.\n\n\n

    :type closeTimeFilter: dict
    :param closeTimeFilter: If specified, only workflow executions that meet the close time criteria of the filter are counted.\n\nNote\nstartTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.\n\n\noldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.\n\nlatestDate (datetime) --Specifies the latest start or close date and time to return.\n\n\n

    :type executionFilter: dict
    :param executionFilter: If specified, only workflow executions matching the WorkflowId in the filter are counted.\n\nNote\ncloseStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nworkflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.\n\n\n

    :type typeFilter: dict
    :param typeFilter: If specified, indicates the type of the workflow executions to be counted.\n\nNote\ncloseStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nname (string) -- [REQUIRED]Name of the workflow type.\n\nversion (string) --Version of the workflow type.\n\n\n

    :type tagFilter: dict
    :param tagFilter: If specified, only executions that have a tag that matches the filter are counted.\n\nNote\ncloseStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\ntag (string) -- [REQUIRED]Specifies the tag that must be associated with the execution for it to meet the filter criteria.\nTags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .\n\n\n

    :type closeStatusFilter: dict
    :param closeStatusFilter: If specified, only workflow executions that match this close status are counted. This filter has an affect only if executionStatus is specified as CLOSED .\n\nNote\ncloseStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nstatus (string) -- [REQUIRED]The close status that must match the close status of an execution for it to meet the criteria of this filter.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'count': 123,
    'truncated': True|False
}


Response Structure

(dict) --
Contains the count of workflow executions returned from  CountOpenWorkflowExecutions or  CountClosedWorkflowExecutions

count (integer) --
The number of workflow executions.

truncated (boolean) --
If set to true, indicates that the actual count was more than the maximum supported by this API and the count returned is the truncated value.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'count': 123,
        'truncated': True|False
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain containing the workflow executions to count.
    
    startTimeFilter (dict) -- If specified, only workflow executions that meet the start time criteria of the filter are counted.
    
    Note
    startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
    
    
    oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
    
    latestDate (datetime) --Specifies the latest start or close date and time to return.
    
    
    
    closeTimeFilter (dict) -- If specified, only workflow executions that meet the close time criteria of the filter are counted.
    
    Note
    startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
    
    
    oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
    
    latestDate (datetime) --Specifies the latest start or close date and time to return.
    
    
    
    executionFilter (dict) -- If specified, only workflow executions matching the WorkflowId in the filter are counted.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
    
    
    
    typeFilter (dict) -- If specified, indicates the type of the workflow executions to be counted.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    name (string) -- [REQUIRED]Name of the workflow type.
    
    version (string) --Version of the workflow type.
    
    
    
    tagFilter (dict) -- If specified, only executions that have a tag that matches the filter are counted.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    tag (string) -- [REQUIRED]Specifies the tag that must be associated with the execution for it to meet the filter criteria.
    Tags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .
    
    
    
    closeStatusFilter (dict) -- If specified, only workflow executions that match this close status are counted. This filter has an affect only if executionStatus is specified as CLOSED .
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    status (string) -- [REQUIRED]The close status that must match the close status of an execution for it to meet the criteria of this filter.
    
    
    
    
    """
    pass

def count_open_workflow_executions(domain=None, startTimeFilter=None, typeFilter=None, tagFilter=None, executionFilter=None):
    """
    Returns the number of open workflow executions within the given domain that meet the specified filtering criteria.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.count_open_workflow_executions(
        domain='string',
        startTimeFilter={
            'oldestDate': datetime(2015, 1, 1),
            'latestDate': datetime(2015, 1, 1)
        },
        typeFilter={
            'name': 'string',
            'version': 'string'
        },
        tagFilter={
            'tag': 'string'
        },
        executionFilter={
            'workflowId': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain containing the workflow executions to count.\n

    :type startTimeFilter: dict
    :param startTimeFilter: [REQUIRED]\nSpecifies the start time criteria that workflow executions must meet in order to be counted.\n\noldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.\n\nlatestDate (datetime) --Specifies the latest start or close date and time to return.\n\n\n

    :type typeFilter: dict
    :param typeFilter: Specifies the type of the workflow executions to be counted.\n\nNote\nexecutionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nname (string) -- [REQUIRED]Name of the workflow type.\n\nversion (string) --Version of the workflow type.\n\n\n

    :type tagFilter: dict
    :param tagFilter: If specified, only executions that have a tag that matches the filter are counted.\n\nNote\nexecutionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\ntag (string) -- [REQUIRED]Specifies the tag that must be associated with the execution for it to meet the filter criteria.\nTags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .\n\n\n

    :type executionFilter: dict
    :param executionFilter: If specified, only workflow executions matching the WorkflowId in the filter are counted.\n\nNote\nexecutionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nworkflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'count': 123,
    'truncated': True|False
}


Response Structure

(dict) --
Contains the count of workflow executions returned from  CountOpenWorkflowExecutions or  CountClosedWorkflowExecutions

count (integer) --
The number of workflow executions.

truncated (boolean) --
If set to true, indicates that the actual count was more than the maximum supported by this API and the count returned is the truncated value.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'count': 123,
        'truncated': True|False
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain containing the workflow executions to count.
    
    startTimeFilter (dict) -- [REQUIRED]
    Specifies the start time criteria that workflow executions must meet in order to be counted.
    
    oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
    
    latestDate (datetime) --Specifies the latest start or close date and time to return.
    
    
    
    typeFilter (dict) -- Specifies the type of the workflow executions to be counted.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    name (string) -- [REQUIRED]Name of the workflow type.
    
    version (string) --Version of the workflow type.
    
    
    
    tagFilter (dict) -- If specified, only executions that have a tag that matches the filter are counted.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    tag (string) -- [REQUIRED]Specifies the tag that must be associated with the execution for it to meet the filter criteria.
    Tags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .
    
    
    
    executionFilter (dict) -- If specified, only workflow executions matching the WorkflowId in the filter are counted.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
    
    
    
    
    """
    pass

def count_pending_activity_tasks(domain=None, taskList=None):
    """
    Returns the estimated number of activity tasks in the specified task list. The count returned is an approximation and isn\'t guaranteed to be exact. If you specify a task list that no activity task was ever scheduled in then 0 is returned.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.count_pending_activity_tasks(
        domain='string',
        taskList={
            'name': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain that contains the task list.\n

    :type taskList: dict
    :param taskList: [REQUIRED]\nThe name of the task list.\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'count': 123,
    'truncated': True|False
}


Response Structure

(dict) --
Contains the count of tasks in a task list.

count (integer) --
The number of tasks in the task list.

truncated (boolean) --
If set to true, indicates that the actual count was more than the maximum supported by this API and the count returned is the truncated value.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'count': 123,
        'truncated': True|False
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain that contains the task list.
    
    taskList (dict) -- [REQUIRED]
    The name of the task list.
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    
    """
    pass

def count_pending_decision_tasks(domain=None, taskList=None):
    """
    Returns the estimated number of decision tasks in the specified task list. The count returned is an approximation and isn\'t guaranteed to be exact. If you specify a task list that no decision task was ever scheduled in then 0 is returned.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.count_pending_decision_tasks(
        domain='string',
        taskList={
            'name': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain that contains the task list.\n

    :type taskList: dict
    :param taskList: [REQUIRED]\nThe name of the task list.\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'count': 123,
    'truncated': True|False
}


Response Structure

(dict) --
Contains the count of tasks in a task list.

count (integer) --
The number of tasks in the task list.

truncated (boolean) --
If set to true, indicates that the actual count was more than the maximum supported by this API and the count returned is the truncated value.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'count': 123,
        'truncated': True|False
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain that contains the task list.
    
    taskList (dict) -- [REQUIRED]
    The name of the task list.
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    
    """
    pass

def deprecate_activity_type(domain=None, activityType=None):
    """
    Deprecates the specified activity type . After an activity type has been deprecated, you cannot create new tasks of that activity type. Tasks of this type that were scheduled before the type was deprecated continue to run.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deprecate_activity_type(
        domain='string',
        activityType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain in which the activity type is registered.\n

    :type activityType: dict
    :param activityType: [REQUIRED]\nThe activity type to deprecate.\n\nname (string) -- [REQUIRED]The name of this activity.\n\nNote\nThe combination of activity type name and version must be unique within a domain.\n\n\nversion (string) -- [REQUIRED]The version of this activity.\n\nNote\nThe combination of activity type name and version must be unique with in a domain.\n\n\n\n

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which the activity type is registered.
    
    activityType (dict) -- [REQUIRED]
    The activity type to deprecate.
    
    name (string) -- [REQUIRED]The name of this activity.
    
    Note
    The combination of activity type name and version must be unique within a domain.
    
    
    version (string) -- [REQUIRED]The version of this activity.
    
    Note
    The combination of activity type name and version must be unique with in a domain.
    
    
    
    
    
    """
    pass

def deprecate_domain(name=None):
    """
    Deprecates the specified domain. After a domain has been deprecated it cannot be used to create new workflow executions or register new types. However, you can still use visibility actions on this domain. Deprecating a domain also deprecates all activity and workflow types registered in the domain. Executions that were started before the domain was deprecated continues to run.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deprecate_domain(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the domain to deprecate.\n

    :returns: 
    SWF.Client.exceptions.UnknownResourceFault
    SWF.Client.exceptions.DomainDeprecatedFault
    SWF.Client.exceptions.OperationNotPermittedFault
    
    """
    pass

def deprecate_workflow_type(domain=None, workflowType=None):
    """
    Deprecates the specified workflow type . After a workflow type has been deprecated, you cannot create new executions of that type. Executions that were started before the type was deprecated continues to run. A deprecated workflow type may still be used when calling visibility actions.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deprecate_workflow_type(
        domain='string',
        workflowType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain in which the workflow type is registered.\n

    :type workflowType: dict
    :param workflowType: [REQUIRED]\nThe workflow type to deprecate.\n\nname (string) -- [REQUIRED]The name of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\nversion (string) -- [REQUIRED]The version of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\n\n

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which the workflow type is registered.
    
    workflowType (dict) -- [REQUIRED]
    The workflow type to deprecate.
    
    name (string) -- [REQUIRED]The name of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    version (string) -- [REQUIRED]The version of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    
    
    
    """
    pass

def describe_activity_type(domain=None, activityType=None):
    """
    Returns information about the specified activity type. This includes configuration settings provided when the type was registered and other general information about the type.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_activity_type(
        domain='string',
        activityType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain in which the activity type is registered.\n

    :type activityType: dict
    :param activityType: [REQUIRED]\nThe activity type to get information about. Activity types are identified by the name and version that were supplied when the activity was registered.\n\nname (string) -- [REQUIRED]The name of this activity.\n\nNote\nThe combination of activity type name and version must be unique within a domain.\n\n\nversion (string) -- [REQUIRED]The version of this activity.\n\nNote\nThe combination of activity type name and version must be unique with in a domain.\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'typeInfo': {
        'activityType': {
            'name': 'string',
            'version': 'string'
        },
        'status': 'REGISTERED'|'DEPRECATED',
        'description': 'string',
        'creationDate': datetime(2015, 1, 1),
        'deprecationDate': datetime(2015, 1, 1)
    },
    'configuration': {
        'defaultTaskStartToCloseTimeout': 'string',
        'defaultTaskHeartbeatTimeout': 'string',
        'defaultTaskList': {
            'name': 'string'
        },
        'defaultTaskPriority': 'string',
        'defaultTaskScheduleToStartTimeout': 'string',
        'defaultTaskScheduleToCloseTimeout': 'string'
    }
}


Response Structure

(dict) --
Detailed information about an activity type.

typeInfo (dict) --
General information about the activity type.
The status of activity type (returned in the ActivityTypeInfo structure) can be one of the following.

REGISTERED \xe2\x80\x93 The type is registered and available. Workers supporting this type should be running.
DEPRECATED \xe2\x80\x93 The type was deprecated using  DeprecateActivityType , but is still in use. You should keep workers supporting this type running. You cannot create new tasks of this type.


activityType (dict) --
The  ActivityType type structure representing the activity type.

name (string) --
The name of this activity.

Note
The combination of activity type name and version must be unique within a domain.


version (string) --
The version of this activity.

Note
The combination of activity type name and version must be unique with in a domain.




status (string) --
The current status of the activity type.

description (string) --
The description of the activity type provided in  RegisterActivityType .

creationDate (datetime) --
The date and time this activity type was created through  RegisterActivityType .

deprecationDate (datetime) --
If DEPRECATED, the date and time  DeprecateActivityType was called.



configuration (dict) --
The configuration settings registered with the activity type.

defaultTaskStartToCloseTimeout (string) --
The default maximum duration for tasks of an activity type specified when registering the activity type. You can override this default when scheduling a task through the ScheduleActivityTask   Decision .
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

defaultTaskHeartbeatTimeout (string) --
The default maximum time, in seconds, before which a worker processing a task must report progress by calling  RecordActivityTaskHeartbeat .
You can specify this value only when registering an activity type. The registered default value can be overridden when you schedule a task through the ScheduleActivityTask   Decision . If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an UnknownResource fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

defaultTaskList (dict) --
The default task list specified for this activity type at registration. This default is used if a task list isn\'t provided when a task is scheduled through the ScheduleActivityTask   Decision . You can override the default registered task list when scheduling a task through the ScheduleActivityTask   Decision .

name (string) --
The name of the task list.



defaultTaskPriority (string) --
The default task priority for tasks of this activity type, specified at registration. If not set, then 0 is used as the default priority. This default can be overridden when scheduling an activity task.
Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .

defaultTaskScheduleToStartTimeout (string) --
The default maximum duration, specified when registering the activity type, that a task of an activity type can wait before being assigned to a worker. You can override this default when scheduling a task through the ScheduleActivityTask   Decision .
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

defaultTaskScheduleToCloseTimeout (string) --
The default maximum duration, specified when registering the activity type, for tasks of this activity type. You can override this default when scheduling a task through the ScheduleActivityTask   Decision .
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.









Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'typeInfo': {
            'activityType': {
                'name': 'string',
                'version': 'string'
            },
            'status': 'REGISTERED'|'DEPRECATED',
            'description': 'string',
            'creationDate': datetime(2015, 1, 1),
            'deprecationDate': datetime(2015, 1, 1)
        },
        'configuration': {
            'defaultTaskStartToCloseTimeout': 'string',
            'defaultTaskHeartbeatTimeout': 'string',
            'defaultTaskList': {
                'name': 'string'
            },
            'defaultTaskPriority': 'string',
            'defaultTaskScheduleToStartTimeout': 'string',
            'defaultTaskScheduleToCloseTimeout': 'string'
        }
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which the activity type is registered.
    
    activityType (dict) -- [REQUIRED]
    The activity type to get information about. Activity types are identified by the name and version that were supplied when the activity was registered.
    
    name (string) -- [REQUIRED]The name of this activity.
    
    Note
    The combination of activity type name and version must be unique within a domain.
    
    
    version (string) -- [REQUIRED]The version of this activity.
    
    Note
    The combination of activity type name and version must be unique with in a domain.
    
    
    
    
    
    """
    pass

def describe_domain(name=None):
    """
    Returns information about the specified domain, including description and status.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_domain(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the domain to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'domainInfo': {
        'name': 'string',
        'status': 'REGISTERED'|'DEPRECATED',
        'description': 'string',
        'arn': 'string'
    },
    'configuration': {
        'workflowExecutionRetentionPeriodInDays': 'string'
    }
}


Response Structure

(dict) --Contains details of a domain.

domainInfo (dict) --The basic information about a domain, such as its name, status, and description.

name (string) --The name of the domain. This name is unique within the account.

status (string) --The status of the domain:

REGISTERED \xe2\x80\x93 The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions.
DEPRECATED \xe2\x80\x93 The domain was deprecated using  DeprecateDomain , but is still in use. You should not create new workflow executions in this domain.


description (string) --The description of the domain provided through  RegisterDomain .

arn (string) --The ARN of the domain.



configuration (dict) --The domain configuration. Currently, this includes only the domain\'s retention period.

workflowExecutionRetentionPeriodInDays (string) --The retention period for workflow executions in this domain.








Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'domainInfo': {
            'name': 'string',
            'status': 'REGISTERED'|'DEPRECATED',
            'description': 'string',
            'arn': 'string'
        },
        'configuration': {
            'workflowExecutionRetentionPeriodInDays': 'string'
        }
    }
    
    
    :returns: 
    REGISTERED \xe2\x80\x93 The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions.
    DEPRECATED \xe2\x80\x93 The domain was deprecated using  DeprecateDomain , but is still in use. You should not create new workflow executions in this domain.
    
    """
    pass

def describe_workflow_execution(domain=None, execution=None):
    """
    Returns information about the specified workflow execution including its type and some statistics.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_workflow_execution(
        domain='string',
        execution={
            'workflowId': 'string',
            'runId': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain containing the workflow execution.\n

    :type execution: dict
    :param execution: [REQUIRED]\nThe workflow execution to describe.\n\nworkflowId (string) -- [REQUIRED]The user defined identifier associated with the workflow execution.\n\nrunId (string) -- [REQUIRED]A system-generated unique identifier for the workflow execution.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'executionInfo': {
        'execution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'startTimestamp': datetime(2015, 1, 1),
        'closeTimestamp': datetime(2015, 1, 1),
        'executionStatus': 'OPEN'|'CLOSED',
        'closeStatus': 'COMPLETED'|'FAILED'|'CANCELED'|'TERMINATED'|'CONTINUED_AS_NEW'|'TIMED_OUT',
        'parent': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'tagList': [
            'string',
        ],
        'cancelRequested': True|False
    },
    'executionConfiguration': {
        'taskStartToCloseTimeout': 'string',
        'executionStartToCloseTimeout': 'string',
        'taskList': {
            'name': 'string'
        },
        'taskPriority': 'string',
        'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        'lambdaRole': 'string'
    },
    'openCounts': {
        'openActivityTasks': 123,
        'openDecisionTasks': 123,
        'openTimers': 123,
        'openChildWorkflowExecutions': 123,
        'openLambdaFunctions': 123
    },
    'latestActivityTaskTimestamp': datetime(2015, 1, 1),
    'latestExecutionContext': 'string'
}


Response Structure

(dict) --
Contains details about a workflow execution.

executionInfo (dict) --
Information about the workflow execution.

execution (dict) --
The workflow execution this information is about.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




startTimestamp (datetime) --
The time when the execution was started.

closeTimestamp (datetime) --
The time when the workflow execution was closed. Set only if the execution status is CLOSED.

executionStatus (string) --
The current status of the execution.

closeStatus (string) --
If the execution status is closed then this specifies how the execution was closed:

COMPLETED \xe2\x80\x93 the execution was successfully completed.
CANCELED \xe2\x80\x93 the execution was canceled.Cancellation allows the implementation to gracefully clean up before the execution is closed.
TERMINATED \xe2\x80\x93 the execution was force terminated.
FAILED \xe2\x80\x93 the execution failed to complete.
TIMED_OUT \xe2\x80\x93 the execution did not complete in the alloted time and was automatically timed out.
CONTINUED_AS_NEW \xe2\x80\x93 the execution is logically continued. This means the current execution was completed and a new execution was started to carry on the workflow.


parent (dict) --
If this workflow execution is a child of another execution then contains the workflow execution that started this execution.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



tagList (list) --
The list of tags associated with the workflow execution. Tags can be used to identify and list workflow executions of interest through the visibility APIs. A workflow execution can have a maximum of 5 tags.

(string) --


cancelRequested (boolean) --
Set to true if a cancellation is requested for this workflow execution.



executionConfiguration (dict) --
The configuration settings for this workflow execution including timeout values, tasklist etc.

taskStartToCloseTimeout (string) --
The maximum duration allowed for decision tasks for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

executionStartToCloseTimeout (string) --
The total duration for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

taskList (dict) --
The task list used for the decision tasks generated for this workflow execution.

name (string) --
The name of the task list.



taskPriority (string) --
The priority assigned to decision tasks for this workflow execution. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .

childPolicy (string) --
The policy to use for the child workflow executions if this workflow execution is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


lambdaRole (string) --
The IAM role attached to the child workflow execution.



openCounts (dict) --
The number of tasks for this workflow execution. This includes open and closed tasks of all types.

openActivityTasks (integer) --
The count of activity tasks whose status is OPEN .

openDecisionTasks (integer) --
The count of decision tasks whose status is OPEN. A workflow execution can have at most one open decision task.

openTimers (integer) --
The count of timers started by this workflow execution that have not fired yet.

openChildWorkflowExecutions (integer) --
The count of child workflow executions whose status is OPEN .

openLambdaFunctions (integer) --
The count of Lambda tasks whose status is OPEN .



latestActivityTaskTimestamp (datetime) --
The time when the last activity task was scheduled for this workflow execution. You can use this information to determine if the workflow has not made progress for an unusually long period of time and might require a corrective action.

latestExecutionContext (string) --
The latest executionContext provided by the decider for this workflow execution. A decider can provide an executionContext (a free-form string) when closing a decision task using  RespondDecisionTaskCompleted .







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'executionInfo': {
            'execution': {
                'workflowId': 'string',
                'runId': 'string'
            },
            'workflowType': {
                'name': 'string',
                'version': 'string'
            },
            'startTimestamp': datetime(2015, 1, 1),
            'closeTimestamp': datetime(2015, 1, 1),
            'executionStatus': 'OPEN'|'CLOSED',
            'closeStatus': 'COMPLETED'|'FAILED'|'CANCELED'|'TERMINATED'|'CONTINUED_AS_NEW'|'TIMED_OUT',
            'parent': {
                'workflowId': 'string',
                'runId': 'string'
            },
            'tagList': [
                'string',
            ],
            'cancelRequested': True|False
        },
        'executionConfiguration': {
            'taskStartToCloseTimeout': 'string',
            'executionStartToCloseTimeout': 'string',
            'taskList': {
                'name': 'string'
            },
            'taskPriority': 'string',
            'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
            'lambdaRole': 'string'
        },
        'openCounts': {
            'openActivityTasks': 123,
            'openDecisionTasks': 123,
            'openTimers': 123,
            'openChildWorkflowExecutions': 123,
            'openLambdaFunctions': 123
        },
        'latestActivityTaskTimestamp': datetime(2015, 1, 1),
        'latestExecutionContext': 'string'
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain containing the workflow execution.
    
    execution (dict) -- [REQUIRED]
    The workflow execution to describe.
    
    workflowId (string) -- [REQUIRED]The user defined identifier associated with the workflow execution.
    
    runId (string) -- [REQUIRED]A system-generated unique identifier for the workflow execution.
    
    
    
    
    """
    pass

def describe_workflow_type(domain=None, workflowType=None):
    """
    Returns information about the specified workflow type . This includes configuration settings specified when the type was registered and other information such as creation date, current status, etc.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_workflow_type(
        domain='string',
        workflowType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain in which this workflow type is registered.\n

    :type workflowType: dict
    :param workflowType: [REQUIRED]\nThe workflow type to describe.\n\nname (string) -- [REQUIRED]The name of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\nversion (string) -- [REQUIRED]The version of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'typeInfo': {
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'status': 'REGISTERED'|'DEPRECATED',
        'description': 'string',
        'creationDate': datetime(2015, 1, 1),
        'deprecationDate': datetime(2015, 1, 1)
    },
    'configuration': {
        'defaultTaskStartToCloseTimeout': 'string',
        'defaultExecutionStartToCloseTimeout': 'string',
        'defaultTaskList': {
            'name': 'string'
        },
        'defaultTaskPriority': 'string',
        'defaultChildPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        'defaultLambdaRole': 'string'
    }
}


Response Structure

(dict) --
Contains details about a workflow type.

typeInfo (dict) --
General information about the workflow type.
The status of the workflow type (returned in the WorkflowTypeInfo structure) can be one of the following.

REGISTERED \xe2\x80\x93 The type is registered and available. Workers supporting this type should be running.
DEPRECATED \xe2\x80\x93 The type was deprecated using  DeprecateWorkflowType , but is still in use. You should keep workers supporting this type running. You cannot create new workflow executions of this type.


workflowType (dict) --
The workflow type this information is about.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




status (string) --
The current status of the workflow type.

description (string) --
The description of the type registered through  RegisterWorkflowType .

creationDate (datetime) --
The date when this type was registered.

deprecationDate (datetime) --
If the type is in deprecated state, then it is set to the date when the type was deprecated.



configuration (dict) --
Configuration settings of the workflow type registered through  RegisterWorkflowType

defaultTaskStartToCloseTimeout (string) --
The default maximum duration, specified when registering the workflow type, that a decision task for executions of this workflow type might take before returning completion or failure. If the task doesn\'tdo close in the specified time then the task is automatically timed out and rescheduled. If the decider eventually reports a completion or failure, it is ignored. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution   Decision .
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

defaultExecutionStartToCloseTimeout (string) --
The default maximum duration, specified when registering the workflow type, for executions of this workflow type. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution   Decision .
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

defaultTaskList (dict) --
The default task list, specified when registering the workflow type, for decisions tasks scheduled for workflow executions of this type. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution   Decision .

name (string) --
The name of the task list.



defaultTaskPriority (string) --
The default task priority, specified when registering the workflow type, for all decision tasks of this workflow type. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution decision.
Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .

defaultChildPolicy (string) --
The default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution   Decision .
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


defaultLambdaRole (string) --
The default IAM role attached to this workflow type.

Note
Executions of this workflow type need IAM roles to invoke Lambda functions. If you don\'t specify an IAM role when starting this workflow type, the default Lambda role is attached to the execution. For more information, see https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html in the Amazon SWF Developer Guide .










Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'typeInfo': {
            'workflowType': {
                'name': 'string',
                'version': 'string'
            },
            'status': 'REGISTERED'|'DEPRECATED',
            'description': 'string',
            'creationDate': datetime(2015, 1, 1),
            'deprecationDate': datetime(2015, 1, 1)
        },
        'configuration': {
            'defaultTaskStartToCloseTimeout': 'string',
            'defaultExecutionStartToCloseTimeout': 'string',
            'defaultTaskList': {
                'name': 'string'
            },
            'defaultTaskPriority': 'string',
            'defaultChildPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
            'defaultLambdaRole': 'string'
        }
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which this workflow type is registered.
    
    workflowType (dict) -- [REQUIRED]
    The workflow type to describe.
    
    name (string) -- [REQUIRED]The name of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    version (string) -- [REQUIRED]The version of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    
    
    
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def get_workflow_execution_history(domain=None, execution=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns the history of the specified workflow execution. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_workflow_execution_history(
        domain='string',
        execution={
            'workflowId': 'string',
            'runId': 'string'
        },
        nextPageToken='string',
        maximumPageSize=123,
        reverseOrder=True|False
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain containing the workflow execution.\n

    :type execution: dict
    :param execution: [REQUIRED]\nSpecifies the workflow execution for which to return the history.\n\nworkflowId (string) -- [REQUIRED]The user defined identifier associated with the workflow execution.\n\nrunId (string) -- [REQUIRED]A system-generated unique identifier for the workflow execution.\n\n\n

    :type nextPageToken: string
    :param nextPageToken: If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: 'Specified token has exceeded its maximum lifetime '.\nThe configured maximumPageSize determines how many results can be returned in a single call.\n

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimeStamp of the events.

    :rtype: dict

ReturnsResponse Syntax
{
    'events': [
        {
            'eventTimestamp': datetime(2015, 1, 1),
            'eventType': 'WorkflowExecutionStarted'|'WorkflowExecutionCancelRequested'|'WorkflowExecutionCompleted'|'CompleteWorkflowExecutionFailed'|'WorkflowExecutionFailed'|'FailWorkflowExecutionFailed'|'WorkflowExecutionTimedOut'|'WorkflowExecutionCanceled'|'CancelWorkflowExecutionFailed'|'WorkflowExecutionContinuedAsNew'|'ContinueAsNewWorkflowExecutionFailed'|'WorkflowExecutionTerminated'|'DecisionTaskScheduled'|'DecisionTaskStarted'|'DecisionTaskCompleted'|'DecisionTaskTimedOut'|'ActivityTaskScheduled'|'ScheduleActivityTaskFailed'|'ActivityTaskStarted'|'ActivityTaskCompleted'|'ActivityTaskFailed'|'ActivityTaskTimedOut'|'ActivityTaskCanceled'|'ActivityTaskCancelRequested'|'RequestCancelActivityTaskFailed'|'WorkflowExecutionSignaled'|'MarkerRecorded'|'RecordMarkerFailed'|'TimerStarted'|'StartTimerFailed'|'TimerFired'|'TimerCanceled'|'CancelTimerFailed'|'StartChildWorkflowExecutionInitiated'|'StartChildWorkflowExecutionFailed'|'ChildWorkflowExecutionStarted'|'ChildWorkflowExecutionCompleted'|'ChildWorkflowExecutionFailed'|'ChildWorkflowExecutionTimedOut'|'ChildWorkflowExecutionCanceled'|'ChildWorkflowExecutionTerminated'|'SignalExternalWorkflowExecutionInitiated'|'SignalExternalWorkflowExecutionFailed'|'ExternalWorkflowExecutionSignaled'|'RequestCancelExternalWorkflowExecutionInitiated'|'RequestCancelExternalWorkflowExecutionFailed'|'ExternalWorkflowExecutionCancelRequested'|'LambdaFunctionScheduled'|'LambdaFunctionStarted'|'LambdaFunctionCompleted'|'LambdaFunctionFailed'|'LambdaFunctionTimedOut'|'ScheduleLambdaFunctionFailed'|'StartLambdaFunctionFailed',
            'eventId': 123,
            'workflowExecutionStartedEventAttributes': {
                'input': 'string',
                'executionStartToCloseTimeout': 'string',
                'taskStartToCloseTimeout': 'string',
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'tagList': [
                    'string',
                ],
                'continuedExecutionRunId': 'string',
                'parentWorkflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'parentInitiatedEventId': 123,
                'lambdaRole': 'string'
            },
            'workflowExecutionCompletedEventAttributes': {
                'result': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'completeWorkflowExecutionFailedEventAttributes': {
                'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'workflowExecutionFailedEventAttributes': {
                'reason': 'string',
                'details': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'failWorkflowExecutionFailedEventAttributes': {
                'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'workflowExecutionTimedOutEventAttributes': {
                'timeoutType': 'START_TO_CLOSE',
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON'
            },
            'workflowExecutionCanceledEventAttributes': {
                'details': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'cancelWorkflowExecutionFailedEventAttributes': {
                'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'workflowExecutionContinuedAsNewEventAttributes': {
                'input': 'string',
                'decisionTaskCompletedEventId': 123,
                'newExecutionRunId': 'string',
                'executionStartToCloseTimeout': 'string',
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'taskStartToCloseTimeout': 'string',
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                'tagList': [
                    'string',
                ],
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'lambdaRole': 'string'
            },
            'continueAsNewWorkflowExecutionFailedEventAttributes': {
                'cause': 'UNHANDLED_DECISION'|'WORKFLOW_TYPE_DEPRECATED'|'WORKFLOW_TYPE_DOES_NOT_EXIST'|'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_CHILD_POLICY_UNDEFINED'|'CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'workflowExecutionTerminatedEventAttributes': {
                'reason': 'string',
                'details': 'string',
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                'cause': 'CHILD_POLICY_APPLIED'|'EVENT_LIMIT_EXCEEDED'|'OPERATOR_INITIATED'
            },
            'workflowExecutionCancelRequestedEventAttributes': {
                'externalWorkflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'externalInitiatedEventId': 123,
                'cause': 'CHILD_POLICY_APPLIED'
            },
            'decisionTaskScheduledEventAttributes': {
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'startToCloseTimeout': 'string'
            },
            'decisionTaskStartedEventAttributes': {
                'identity': 'string',
                'scheduledEventId': 123
            },
            'decisionTaskCompletedEventAttributes': {
                'executionContext': 'string',
                'scheduledEventId': 123,
                'startedEventId': 123
            },
            'decisionTaskTimedOutEventAttributes': {
                'timeoutType': 'START_TO_CLOSE',
                'scheduledEventId': 123,
                'startedEventId': 123
            },
            'activityTaskScheduledEventAttributes': {
                'activityType': {
                    'name': 'string',
                    'version': 'string'
                },
                'activityId': 'string',
                'input': 'string',
                'control': 'string',
                'scheduleToStartTimeout': 'string',
                'scheduleToCloseTimeout': 'string',
                'startToCloseTimeout': 'string',
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'decisionTaskCompletedEventId': 123,
                'heartbeatTimeout': 'string'
            },
            'activityTaskStartedEventAttributes': {
                'identity': 'string',
                'scheduledEventId': 123
            },
            'activityTaskCompletedEventAttributes': {
                'result': 'string',
                'scheduledEventId': 123,
                'startedEventId': 123
            },
            'activityTaskFailedEventAttributes': {
                'reason': 'string',
                'details': 'string',
                'scheduledEventId': 123,
                'startedEventId': 123
            },
            'activityTaskTimedOutEventAttributes': {
                'timeoutType': 'START_TO_CLOSE'|'SCHEDULE_TO_START'|'SCHEDULE_TO_CLOSE'|'HEARTBEAT',
                'scheduledEventId': 123,
                'startedEventId': 123,
                'details': 'string'
            },
            'activityTaskCanceledEventAttributes': {
                'details': 'string',
                'scheduledEventId': 123,
                'startedEventId': 123,
                'latestCancelRequestedEventId': 123
            },
            'activityTaskCancelRequestedEventAttributes': {
                'decisionTaskCompletedEventId': 123,
                'activityId': 'string'
            },
            'workflowExecutionSignaledEventAttributes': {
                'signalName': 'string',
                'input': 'string',
                'externalWorkflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'externalInitiatedEventId': 123
            },
            'markerRecordedEventAttributes': {
                'markerName': 'string',
                'details': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'recordMarkerFailedEventAttributes': {
                'markerName': 'string',
                'cause': 'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'timerStartedEventAttributes': {
                'timerId': 'string',
                'control': 'string',
                'startToFireTimeout': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'timerFiredEventAttributes': {
                'timerId': 'string',
                'startedEventId': 123
            },
            'timerCanceledEventAttributes': {
                'timerId': 'string',
                'startedEventId': 123,
                'decisionTaskCompletedEventId': 123
            },
            'startChildWorkflowExecutionInitiatedEventAttributes': {
                'workflowId': 'string',
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'control': 'string',
                'input': 'string',
                'executionStartToCloseTimeout': 'string',
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'decisionTaskCompletedEventId': 123,
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                'taskStartToCloseTimeout': 'string',
                'tagList': [
                    'string',
                ],
                'lambdaRole': 'string'
            },
            'childWorkflowExecutionStartedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'initiatedEventId': 123
            },
            'childWorkflowExecutionCompletedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'result': 'string',
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'childWorkflowExecutionFailedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'reason': 'string',
                'details': 'string',
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'childWorkflowExecutionTimedOutEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'timeoutType': 'START_TO_CLOSE',
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'childWorkflowExecutionCanceledEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'details': 'string',
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'childWorkflowExecutionTerminatedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'signalExternalWorkflowExecutionInitiatedEventAttributes': {
                'workflowId': 'string',
                'runId': 'string',
                'signalName': 'string',
                'input': 'string',
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'externalWorkflowExecutionSignaledEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'initiatedEventId': 123
            },
            'signalExternalWorkflowExecutionFailedEventAttributes': {
                'workflowId': 'string',
                'runId': 'string',
                'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                'initiatedEventId': 123,
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'externalWorkflowExecutionCancelRequestedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'initiatedEventId': 123
            },
            'requestCancelExternalWorkflowExecutionInitiatedEventAttributes': {
                'workflowId': 'string',
                'runId': 'string',
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'requestCancelExternalWorkflowExecutionFailedEventAttributes': {
                'workflowId': 'string',
                'runId': 'string',
                'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                'initiatedEventId': 123,
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'scheduleActivityTaskFailedEventAttributes': {
                'activityType': {
                    'name': 'string',
                    'version': 'string'
                },
                'activityId': 'string',
                'cause': 'ACTIVITY_TYPE_DEPRECATED'|'ACTIVITY_TYPE_DOES_NOT_EXIST'|'ACTIVITY_ID_ALREADY_IN_USE'|'OPEN_ACTIVITIES_LIMIT_EXCEEDED'|'ACTIVITY_CREATION_RATE_EXCEEDED'|'DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED'|'DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'requestCancelActivityTaskFailedEventAttributes': {
                'activityId': 'string',
                'cause': 'ACTIVITY_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'startTimerFailedEventAttributes': {
                'timerId': 'string',
                'cause': 'TIMER_ID_ALREADY_IN_USE'|'OPEN_TIMERS_LIMIT_EXCEEDED'|'TIMER_CREATION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'cancelTimerFailedEventAttributes': {
                'timerId': 'string',
                'cause': 'TIMER_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'startChildWorkflowExecutionFailedEventAttributes': {
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'cause': 'WORKFLOW_TYPE_DOES_NOT_EXIST'|'WORKFLOW_TYPE_DEPRECATED'|'OPEN_CHILDREN_LIMIT_EXCEEDED'|'OPEN_WORKFLOWS_LIMIT_EXCEEDED'|'CHILD_CREATION_RATE_EXCEEDED'|'WORKFLOW_ALREADY_RUNNING'|'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_CHILD_POLICY_UNDEFINED'|'OPERATION_NOT_PERMITTED',
                'workflowId': 'string',
                'initiatedEventId': 123,
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'lambdaFunctionScheduledEventAttributes': {
                'id': 'string',
                'name': 'string',
                'control': 'string',
                'input': 'string',
                'startToCloseTimeout': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'lambdaFunctionStartedEventAttributes': {
                'scheduledEventId': 123
            },
            'lambdaFunctionCompletedEventAttributes': {
                'scheduledEventId': 123,
                'startedEventId': 123,
                'result': 'string'
            },
            'lambdaFunctionFailedEventAttributes': {
                'scheduledEventId': 123,
                'startedEventId': 123,
                'reason': 'string',
                'details': 'string'
            },
            'lambdaFunctionTimedOutEventAttributes': {
                'scheduledEventId': 123,
                'startedEventId': 123,
                'timeoutType': 'START_TO_CLOSE'
            },
            'scheduleLambdaFunctionFailedEventAttributes': {
                'id': 'string',
                'name': 'string',
                'cause': 'ID_ALREADY_IN_USE'|'OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED'|'LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED'|'LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION',
                'decisionTaskCompletedEventId': 123
            },
            'startLambdaFunctionFailedEventAttributes': {
                'scheduledEventId': 123,
                'cause': 'ASSUME_ROLE_FAILED',
                'message': 'string'
            }
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
Paginated representation of a workflow history for a workflow execution. This is the up to date, complete and authoritative record of the events related to all tasks and events in the life of the workflow execution.

events (list) --
The list of history events.

(dict) --
Event within a workflow execution. A history event can be one of these types:

ActivityTaskCancelRequested \xe2\x80\x93 A RequestCancelActivityTask decision was received by the system.
ActivityTaskCanceled \xe2\x80\x93 The activity task was successfully canceled.
ActivityTaskCompleted \xe2\x80\x93 An activity worker successfully completed an activity task by calling  RespondActivityTaskCompleted .
ActivityTaskFailed \xe2\x80\x93 An activity worker failed an activity task by calling  RespondActivityTaskFailed .
ActivityTaskScheduled \xe2\x80\x93 An activity task was scheduled for execution.
ActivityTaskStarted \xe2\x80\x93 The scheduled activity task was dispatched to a worker.
ActivityTaskTimedOut \xe2\x80\x93 The activity task timed out.
CancelTimerFailed \xe2\x80\x93 Failed to process CancelTimer decision. This happens when the decision isn\'t configured properly, for example no timer exists with the specified timer Id.
CancelWorkflowExecutionFailed \xe2\x80\x93 A request to cancel a workflow execution failed.
ChildWorkflowExecutionCanceled \xe2\x80\x93 A child workflow execution, started by this workflow execution, was canceled and closed.
ChildWorkflowExecutionCompleted \xe2\x80\x93 A child workflow execution, started by this workflow execution, completed successfully and was closed.
ChildWorkflowExecutionFailed \xe2\x80\x93 A child workflow execution, started by this workflow execution, failed to complete successfully and was closed.
ChildWorkflowExecutionStarted \xe2\x80\x93 A child workflow execution was successfully started.
ChildWorkflowExecutionTerminated \xe2\x80\x93 A child workflow execution, started by this workflow execution, was terminated.
ChildWorkflowExecutionTimedOut \xe2\x80\x93 A child workflow execution, started by this workflow execution, timed out and was closed.
CompleteWorkflowExecutionFailed \xe2\x80\x93 The workflow execution failed to complete.
ContinueAsNewWorkflowExecutionFailed \xe2\x80\x93 The workflow execution failed to complete after being continued as a new workflow execution.
DecisionTaskCompleted \xe2\x80\x93 The decider successfully completed a decision task by calling  RespondDecisionTaskCompleted .
DecisionTaskScheduled \xe2\x80\x93 A decision task was scheduled for the workflow execution.
DecisionTaskStarted \xe2\x80\x93 The decision task was dispatched to a decider.
DecisionTaskTimedOut \xe2\x80\x93 The decision task timed out.
ExternalWorkflowExecutionCancelRequested \xe2\x80\x93 Request to cancel an external workflow execution was successfully delivered to the target execution.
ExternalWorkflowExecutionSignaled \xe2\x80\x93 A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution.
FailWorkflowExecutionFailed \xe2\x80\x93 A request to mark a workflow execution as failed, itself failed.
MarkerRecorded \xe2\x80\x93 A marker was recorded in the workflow history as the result of a RecordMarker decision.
RecordMarkerFailed \xe2\x80\x93 A RecordMarker decision was returned as failed.
RequestCancelActivityTaskFailed \xe2\x80\x93 Failed to process RequestCancelActivityTask decision. This happens when the decision isn\'t configured properly.
RequestCancelExternalWorkflowExecutionFailed \xe2\x80\x93 Request to cancel an external workflow execution failed.
RequestCancelExternalWorkflowExecutionInitiated \xe2\x80\x93 A request was made to request the cancellation of an external workflow execution.
ScheduleActivityTaskFailed \xe2\x80\x93 Failed to process ScheduleActivityTask decision. This happens when the decision isn\'t configured properly, for example the activity type specified isn\'t registered.
SignalExternalWorkflowExecutionFailed \xe2\x80\x93 The request to signal an external workflow execution failed.
SignalExternalWorkflowExecutionInitiated \xe2\x80\x93 A request to signal an external workflow was made.
StartActivityTaskFailed \xe2\x80\x93 A scheduled activity task failed to start.
StartChildWorkflowExecutionFailed \xe2\x80\x93 Failed to process StartChildWorkflowExecution decision. This happens when the decision isn\'t configured properly, for example the workflow type specified isn\'t registered.
StartChildWorkflowExecutionInitiated \xe2\x80\x93 A request was made to start a child workflow execution.
StartTimerFailed \xe2\x80\x93 Failed to process StartTimer decision. This happens when the decision isn\'t configured properly, for example a timer already exists with the specified timer Id.
TimerCanceled \xe2\x80\x93 A timer, previously started for this workflow execution, was successfully canceled.
TimerFired \xe2\x80\x93 A timer, previously started for this workflow execution, fired.
TimerStarted \xe2\x80\x93 A timer was started for the workflow execution due to a StartTimer decision.
WorkflowExecutionCancelRequested \xe2\x80\x93 A request to cancel this workflow execution was made.
WorkflowExecutionCanceled \xe2\x80\x93 The workflow execution was successfully canceled and closed.
WorkflowExecutionCompleted \xe2\x80\x93 The workflow execution was closed due to successful completion.
WorkflowExecutionContinuedAsNew \xe2\x80\x93 The workflow execution was closed and a new execution of the same type was created with the same workflowId.
WorkflowExecutionFailed \xe2\x80\x93 The workflow execution closed due to a failure.
WorkflowExecutionSignaled \xe2\x80\x93 An external signal was received for the workflow execution.
WorkflowExecutionStarted \xe2\x80\x93 The workflow execution was started.
WorkflowExecutionTerminated \xe2\x80\x93 The workflow execution was terminated.
WorkflowExecutionTimedOut \xe2\x80\x93 The workflow execution was closed because a time out was exceeded.


eventTimestamp (datetime) --
The date and time when the event occurred.

eventType (string) --
The type of the history event.

eventId (integer) --
The system generated ID of the event. This ID uniquely identifies the event with in the workflow execution history.

workflowExecutionStartedEventAttributes (dict) --
If the event is of type WorkflowExecutionStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

input (string) --
The input provided to the workflow execution.

executionStartToCloseTimeout (string) --
The maximum duration for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

taskStartToCloseTimeout (string) --
The maximum duration of decision tasks for this workflow type.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

childPolicy (string) --
The policy to use for the child workflow executions if this workflow execution is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


taskList (dict) --
The name of the task list for scheduling the decision tasks for this workflow execution.

name (string) --
The name of the task list.



taskPriority (string) --
The priority of the decision tasks in the workflow execution.

workflowType (dict) --
The workflow type of this execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




tagList (list) --
The list of tags associated with this workflow execution. An execution can have up to 5 tags.

(string) --


continuedExecutionRunId (string) --
If this workflow execution was started due to a ContinueAsNewWorkflowExecution decision, then it contains the runId of the previous workflow execution that was closed and continued as this execution.

parentWorkflowExecution (dict) --
The source workflow execution that started this workflow execution. The member isn\'t set if the workflow execution was not started by a workflow.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



parentInitiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this workflow execution. The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

lambdaRole (string) --
The IAM role attached to the workflow execution.



workflowExecutionCompletedEventAttributes (dict) --
If the event is of type WorkflowExecutionCompleted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

result (string) --
The result produced by the workflow execution upon successful completion.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CompleteWorkflowExecution decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



completeWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type CompleteWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CompleteWorkflowExecution decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



workflowExecutionFailedEventAttributes (dict) --
If the event is of type WorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

reason (string) --
The descriptive reason provided for the failure.

details (string) --
The details of the failure.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the FailWorkflowExecution decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



failWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type FailWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the FailWorkflowExecution decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



workflowExecutionTimedOutEventAttributes (dict) --
If the event is of type WorkflowExecutionTimedOut then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timeoutType (string) --
The type of timeout that caused this event.

childPolicy (string) --
The policy used for the child workflow executions of this workflow execution.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.




workflowExecutionCanceledEventAttributes (dict) --
If the event is of type WorkflowExecutionCanceled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

details (string) --
The details of the cancellation.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



cancelWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type CancelWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



workflowExecutionContinuedAsNewEventAttributes (dict) --
If the event is of type WorkflowExecutionContinuedAsNew then this member is set and provides detailed information about the event. It isn\'t set for other event types.

input (string) --
The input provided to the new workflow execution.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the ContinueAsNewWorkflowExecution decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

newExecutionRunId (string) --
The runId of the new workflow execution.

executionStartToCloseTimeout (string) --
The total duration allowed for the new workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

taskList (dict) --
The task list to use for the decisions of the new (continued) workflow execution.

name (string) --
The name of the task list.



taskPriority (string) --
The priority of the task to use for the decisions of the new (continued) workflow execution.

taskStartToCloseTimeout (string) --
The maximum duration of decision tasks for the new workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

childPolicy (string) --
The policy to use for the child workflow executions of the new execution if it is terminated by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


tagList (list) --
The list of tags associated with the new workflow execution.

(string) --


workflowType (dict) --
The workflow type of this execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




lambdaRole (string) --
The IAM role to attach to the new (continued) workflow execution.



continueAsNewWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type ContinueAsNewWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the ContinueAsNewWorkflowExecution decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



workflowExecutionTerminatedEventAttributes (dict) --
If the event is of type WorkflowExecutionTerminated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

reason (string) --
The reason provided for the termination.

details (string) --
The details provided for the termination.

childPolicy (string) --
The policy used for the child workflow executions of this workflow execution.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


cause (string) --
If set, indicates that the workflow execution was automatically terminated, and specifies the cause. This happens if the parent workflow execution times out or is terminated and the child policy is set to terminate child executions.



workflowExecutionCancelRequestedEventAttributes (dict) --
If the event is of type WorkflowExecutionCancelRequested then this member is set and provides detailed information about the event. It isn\'t set for other event types.

externalWorkflowExecution (dict) --
The external workflow execution for which the cancellation was requested.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



externalInitiatedEventId (integer) --
The ID of the RequestCancelExternalWorkflowExecutionInitiated event corresponding to the RequestCancelExternalWorkflowExecution decision to cancel this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

cause (string) --
If set, indicates that the request to cancel the workflow execution was automatically generated, and specifies the cause. This happens if the parent workflow execution times out or is terminated, and the child policy is set to cancel child executions.



decisionTaskScheduledEventAttributes (dict) --
If the event is of type DecisionTaskScheduled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

taskList (dict) --
The name of the task list in which the decision task was scheduled.

name (string) --
The name of the task list.



taskPriority (string) --
A task priority that, if set, specifies the priority for this decision task. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .

startToCloseTimeout (string) --
The maximum duration for this decision task. The task is considered timed out if it doesn\'t completed within this duration.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.



decisionTaskStartedEventAttributes (dict) --
If the event is of type DecisionTaskStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

identity (string) --
Identity of the decider making the request. This enables diagnostic tracing when problems arise. The form of this identity is user defined.

scheduledEventId (integer) --
The ID of the DecisionTaskScheduled event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



decisionTaskCompletedEventAttributes (dict) --
If the event is of type DecisionTaskCompleted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

executionContext (string) --
User defined context for the workflow execution.

scheduledEventId (integer) --
The ID of the DecisionTaskScheduled event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the DecisionTaskStarted event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



decisionTaskTimedOutEventAttributes (dict) --
If the event is of type DecisionTaskTimedOut then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timeoutType (string) --
The type of timeout that expired before the decision task could be completed.

scheduledEventId (integer) --
The ID of the DecisionTaskScheduled event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the DecisionTaskStarted event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskScheduledEventAttributes (dict) --
If the event is of type ActivityTaskScheduled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

activityType (dict) --
The type of the activity task.

name (string) --
The name of this activity.

Note
The combination of activity type name and version must be unique within a domain.


version (string) --
The version of this activity.

Note
The combination of activity type name and version must be unique with in a domain.




activityId (string) --
The unique ID of the activity task.

input (string) --
The input provided to the activity task.

control (string) --
Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn\'t sent to the activity.

scheduleToStartTimeout (string) --
The maximum amount of time the activity task can wait to be assigned to a worker.

scheduleToCloseTimeout (string) --
The maximum amount of time for this activity task.

startToCloseTimeout (string) --
The maximum amount of time a worker may take to process the activity task.

taskList (dict) --
The task list in which the activity task has been scheduled.

name (string) --
The name of the task list.



taskPriority (string) --
The priority to assign to the scheduled activity task. If set, this overrides any default priority value that was assigned when the activity type was registered.
Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

heartbeatTimeout (string) --
The maximum time before which the worker processing this task must report progress by calling  RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or return a result, it is ignored.



activityTaskStartedEventAttributes (dict) --
If the event is of type ActivityTaskStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

identity (string) --
Identity of the worker that was assigned this task. This aids diagnostics when problems arise. The form of this identity is user defined.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskCompletedEventAttributes (dict) --
If the event is of type ActivityTaskCompleted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

result (string) --
The results of the activity task.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskFailedEventAttributes (dict) --
If the event is of type ActivityTaskFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

reason (string) --
The reason provided for the failure.

details (string) --
The details of the failure.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskTimedOutEventAttributes (dict) --
If the event is of type ActivityTaskTimedOut then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timeoutType (string) --
The type of the timeout that caused this event.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

details (string) --
Contains the content of the details parameter for the last call made by the activity to RecordActivityTaskHeartbeat .



activityTaskCanceledEventAttributes (dict) --
If the event is of type ActivityTaskCanceled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

details (string) --
Details of the cancellation.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

latestCancelRequestedEventId (integer) --
If set, contains the ID of the last ActivityTaskCancelRequested event recorded for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskCancelRequestedEventAttributes (dict) --
If the event is of type ActivityTaskcancelRequested then this member is set and provides detailed information about the event. It isn\'t set for other event types.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelActivityTask decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

activityId (string) --
The unique ID of the task.



workflowExecutionSignaledEventAttributes (dict) --
If the event is of type WorkflowExecutionSignaled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

signalName (string) --
The name of the signal received. The decider can use the signal name and inputs to determine how to the process the signal.

input (string) --
The inputs provided with the signal. The decider can use the signal name and inputs to determine how to process the signal.

externalWorkflowExecution (dict) --
The workflow execution that sent the signal. This is set only of the signal was sent by another workflow execution.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



externalInitiatedEventId (integer) --
The ID of the SignalExternalWorkflowExecutionInitiated event corresponding to the SignalExternalWorkflow decision to signal this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event. This field is set only if the signal was initiated by another workflow execution.



markerRecordedEventAttributes (dict) --
If the event is of type MarkerRecorded then this member is set and provides detailed information about the event. It isn\'t set for other event types.

markerName (string) --
The name of the marker.

details (string) --
The details of the marker.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RecordMarker decision that requested this marker. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



recordMarkerFailedEventAttributes (dict) --
If the event is of type DecisionTaskFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

markerName (string) --
The marker\'s name.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RecordMarkerFailed decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



timerStartedEventAttributes (dict) --
If the event is of type TimerStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The unique ID of the timer that was started.

control (string) --
Data attached to the event that can be used by the decider in subsequent workflow tasks.

startToFireTimeout (string) --
The duration of time after which the timer fires.
The duration is specified in seconds, an integer greater than or equal to 0 .

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartTimer decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



timerFiredEventAttributes (dict) --
If the event is of type TimerFired then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The unique ID of the timer that fired.

startedEventId (integer) --
The ID of the TimerStarted event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



timerCanceledEventAttributes (dict) --
If the event is of type TimerCanceled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The unique ID of the timer that was canceled.

startedEventId (integer) --
The ID of the TimerStarted event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelTimer decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



startChildWorkflowExecutionInitiatedEventAttributes (dict) --
If the event is of type StartChildWorkflowExecutionInitiated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the child workflow execution.

workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




control (string) --
Data attached to the event that can be used by the decider in subsequent decision tasks. This data isn\'t sent to the activity.

input (string) --
The inputs provided to the child workflow execution.

executionStartToCloseTimeout (string) --
The maximum duration for the child workflow execution. If the workflow execution isn\'t closed within this duration, it is timed out and force-terminated.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

taskList (dict) --
The name of the task list used for the decision tasks of the child workflow execution.

name (string) --
The name of the task list.



taskPriority (string) --
The priority assigned for the decision tasks for this workflow execution. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartChildWorkflowExecution   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the cause of events.

childPolicy (string) --
The policy to use for the child workflow executions if this execution gets terminated by explicitly calling the  TerminateWorkflowExecution action or due to an expired timeout.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


taskStartToCloseTimeout (string) --
The maximum duration allowed for the decision tasks for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

tagList (list) --
The list of tags to associated with the child workflow execution.

(string) --


lambdaRole (string) --
The IAM role to attach to the child workflow execution.



childWorkflowExecutionStartedEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that was started.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionCompletedEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionCompleted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that was completed.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




result (string) --
The result of the child workflow execution.

initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that failed.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




reason (string) --
The reason for the failure (if provided).

details (string) --
The details of the failure (if provided).

initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionTimedOutEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionTimedOut then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that timed out.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




timeoutType (string) --
The type of the timeout that caused the child workflow execution to time out.

initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionCanceledEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionCanceled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that was canceled.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




details (string) --
Details of the cancellation (if provided).

initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionTerminatedEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionTerminated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that was terminated.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



signalExternalWorkflowExecutionInitiatedEventAttributes (dict) --
If the event is of type SignalExternalWorkflowExecutionInitiated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the external workflow execution.

runId (string) --
The runId of the external workflow execution to send the signal to.

signalName (string) --
The name of the signal.

input (string) --
The input provided to the signal.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the SignalExternalWorkflowExecution decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control (string) --
Data attached to the event that can be used by the decider in subsequent decision tasks.



externalWorkflowExecutionSignaledEventAttributes (dict) --
If the event is of type ExternalWorkflowExecutionSignaled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The external workflow execution that the signal was delivered to.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



initiatedEventId (integer) --
The ID of the SignalExternalWorkflowExecutionInitiated event corresponding to the SignalExternalWorkflowExecution decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



signalExternalWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type SignalExternalWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the external workflow execution that the signal was being delivered to.

runId (string) --
The runId of the external workflow execution that the signal was being delivered to.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


initiatedEventId (integer) --
The ID of the SignalExternalWorkflowExecutionInitiated event corresponding to the SignalExternalWorkflowExecution decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the SignalExternalWorkflowExecution decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control (string) --
The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the workflow execution.



externalWorkflowExecutionCancelRequestedEventAttributes (dict) --
If the event is of type ExternalWorkflowExecutionCancelRequested then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The external workflow execution to which the cancellation request was delivered.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



initiatedEventId (integer) --
The ID of the RequestCancelExternalWorkflowExecutionInitiated event corresponding to the RequestCancelExternalWorkflowExecution decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



requestCancelExternalWorkflowExecutionInitiatedEventAttributes (dict) --
If the event is of type RequestCancelExternalWorkflowExecutionInitiated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the external workflow execution to be canceled.

runId (string) --
The runId of the external workflow execution to be canceled.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelExternalWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control (string) --
Data attached to the event that can be used by the decider in subsequent workflow tasks.



requestCancelExternalWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type RequestCancelExternalWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the external workflow to which the cancel request was to be delivered.

runId (string) --
The runId of the external workflow execution.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


initiatedEventId (integer) --
The ID of the RequestCancelExternalWorkflowExecutionInitiated event corresponding to the RequestCancelExternalWorkflowExecution decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelExternalWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control (string) --
The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the workflow execution.



scheduleActivityTaskFailedEventAttributes (dict) --
If the event is of type ScheduleActivityTaskFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

activityType (dict) --
The activity type provided in the ScheduleActivityTask decision that failed.

name (string) --
The name of this activity.

Note
The combination of activity type name and version must be unique within a domain.


version (string) --
The version of this activity.

Note
The combination of activity type name and version must be unique with in a domain.




activityId (string) --
The activityId provided in the ScheduleActivityTask decision that failed.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



requestCancelActivityTaskFailedEventAttributes (dict) --
If the event is of type RequestCancelActivityTaskFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

activityId (string) --
The activityId provided in the RequestCancelActivityTask decision that failed.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelActivityTask decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



startTimerFailedEventAttributes (dict) --
If the event is of type StartTimerFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The timerId provided in the StartTimer decision that failed.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartTimer decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



cancelTimerFailedEventAttributes (dict) --
If the event is of type CancelTimerFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The timerId provided in the CancelTimer decision that failed.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelTimer decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



startChildWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type StartChildWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowType (dict) --
The workflow type provided in the StartChildWorkflowExecution   Decision that failed.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
When cause is set to OPERATION_NOT_PERMITTED , the decision fails because it lacks sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


workflowId (string) --
The workflowId of the child workflow execution.

initiatedEventId (integer) --
When the cause is WORKFLOW_ALREADY_RUNNING , initiatedEventId is the ID of the StartChildWorkflowExecutionInitiated event that corresponds to the StartChildWorkflowExecution   Decision to start the workflow execution. You can use this information to diagnose problems by tracing back the chain of events leading up to this event.
When the cause isn\'t WORKFLOW_ALREADY_RUNNING , initiatedEventId is set to 0 because the StartChildWorkflowExecutionInitiated event doesn\'t exist.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartChildWorkflowExecution   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events.

control (string) --
The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the child workflow execution.



lambdaFunctionScheduledEventAttributes (dict) --
Provides the details of the LambdaFunctionScheduled event. It isn\'t set for other event types.

id (string) --
The unique ID of the Lambda task.

name (string) --
The name of the Lambda function.

control (string) --
Data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the Lambda task.

input (string) --
The input provided to the Lambda task.

startToCloseTimeout (string) --
The maximum amount of time a worker can take to process the Lambda task.

decisionTaskCompletedEventId (integer) --
The ID of the LambdaFunctionCompleted event corresponding to the decision that resulted in scheduling this activity task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.



lambdaFunctionStartedEventAttributes (dict) --
Provides the details of the LambdaFunctionStarted event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the LambdaFunctionScheduled event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.



lambdaFunctionCompletedEventAttributes (dict) --
Provides the details of the LambdaFunctionCompleted event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the LambdaFunctionScheduled event that was recorded when this Lambda task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the LambdaFunctionStarted event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

result (string) --
The results of the Lambda task.



lambdaFunctionFailedEventAttributes (dict) --
Provides the details of the LambdaFunctionFailed event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the LambdaFunctionScheduled event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the LambdaFunctionStarted event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

reason (string) --
The reason provided for the failure.

details (string) --
The details of the failure.



lambdaFunctionTimedOutEventAttributes (dict) --
Provides the details of the LambdaFunctionTimedOut event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the LambdaFunctionScheduled event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event that was recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

timeoutType (string) --
The type of the timeout that caused this event.



scheduleLambdaFunctionFailedEventAttributes (dict) --
Provides the details of the ScheduleLambdaFunctionFailed event. It isn\'t set for other event types.

id (string) --
The ID provided in the ScheduleLambdaFunction decision that failed.

name (string) --
The name of the Lambda function.

cause (string) --
The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the LambdaFunctionCompleted event corresponding to the decision that resulted in scheduling this Lambda task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.



startLambdaFunctionFailedEventAttributes (dict) --
Provides the details of the StartLambdaFunctionFailed event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

cause (string) --
The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because the IAM role attached to the execution lacked sufficient permissions. For details and example IAM policies, see Lambda Tasks in the Amazon SWF Developer Guide .


message (string) --
A description that can help diagnose the cause of the fault.







nextPageToken (string) --
If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
The configured maximumPageSize determines how many results can be returned in a single call.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'events': [
            {
                'eventTimestamp': datetime(2015, 1, 1),
                'eventType': 'WorkflowExecutionStarted'|'WorkflowExecutionCancelRequested'|'WorkflowExecutionCompleted'|'CompleteWorkflowExecutionFailed'|'WorkflowExecutionFailed'|'FailWorkflowExecutionFailed'|'WorkflowExecutionTimedOut'|'WorkflowExecutionCanceled'|'CancelWorkflowExecutionFailed'|'WorkflowExecutionContinuedAsNew'|'ContinueAsNewWorkflowExecutionFailed'|'WorkflowExecutionTerminated'|'DecisionTaskScheduled'|'DecisionTaskStarted'|'DecisionTaskCompleted'|'DecisionTaskTimedOut'|'ActivityTaskScheduled'|'ScheduleActivityTaskFailed'|'ActivityTaskStarted'|'ActivityTaskCompleted'|'ActivityTaskFailed'|'ActivityTaskTimedOut'|'ActivityTaskCanceled'|'ActivityTaskCancelRequested'|'RequestCancelActivityTaskFailed'|'WorkflowExecutionSignaled'|'MarkerRecorded'|'RecordMarkerFailed'|'TimerStarted'|'StartTimerFailed'|'TimerFired'|'TimerCanceled'|'CancelTimerFailed'|'StartChildWorkflowExecutionInitiated'|'StartChildWorkflowExecutionFailed'|'ChildWorkflowExecutionStarted'|'ChildWorkflowExecutionCompleted'|'ChildWorkflowExecutionFailed'|'ChildWorkflowExecutionTimedOut'|'ChildWorkflowExecutionCanceled'|'ChildWorkflowExecutionTerminated'|'SignalExternalWorkflowExecutionInitiated'|'SignalExternalWorkflowExecutionFailed'|'ExternalWorkflowExecutionSignaled'|'RequestCancelExternalWorkflowExecutionInitiated'|'RequestCancelExternalWorkflowExecutionFailed'|'ExternalWorkflowExecutionCancelRequested'|'LambdaFunctionScheduled'|'LambdaFunctionStarted'|'LambdaFunctionCompleted'|'LambdaFunctionFailed'|'LambdaFunctionTimedOut'|'ScheduleLambdaFunctionFailed'|'StartLambdaFunctionFailed',
                'eventId': 123,
                'workflowExecutionStartedEventAttributes': {
                    'input': 'string',
                    'executionStartToCloseTimeout': 'string',
                    'taskStartToCloseTimeout': 'string',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'tagList': [
                        'string',
                    ],
                    'continuedExecutionRunId': 'string',
                    'parentWorkflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'parentInitiatedEventId': 123,
                    'lambdaRole': 'string'
                },
                'workflowExecutionCompletedEventAttributes': {
                    'result': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'completeWorkflowExecutionFailedEventAttributes': {
                    'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'workflowExecutionFailedEventAttributes': {
                    'reason': 'string',
                    'details': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'failWorkflowExecutionFailedEventAttributes': {
                    'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'workflowExecutionTimedOutEventAttributes': {
                    'timeoutType': 'START_TO_CLOSE',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON'
                },
                'workflowExecutionCanceledEventAttributes': {
                    'details': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'cancelWorkflowExecutionFailedEventAttributes': {
                    'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'workflowExecutionContinuedAsNewEventAttributes': {
                    'input': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'newExecutionRunId': 'string',
                    'executionStartToCloseTimeout': 'string',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'taskStartToCloseTimeout': 'string',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'tagList': [
                        'string',
                    ],
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'lambdaRole': 'string'
                },
                'continueAsNewWorkflowExecutionFailedEventAttributes': {
                    'cause': 'UNHANDLED_DECISION'|'WORKFLOW_TYPE_DEPRECATED'|'WORKFLOW_TYPE_DOES_NOT_EXIST'|'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_CHILD_POLICY_UNDEFINED'|'CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'workflowExecutionTerminatedEventAttributes': {
                    'reason': 'string',
                    'details': 'string',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'cause': 'CHILD_POLICY_APPLIED'|'EVENT_LIMIT_EXCEEDED'|'OPERATOR_INITIATED'
                },
                'workflowExecutionCancelRequestedEventAttributes': {
                    'externalWorkflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'externalInitiatedEventId': 123,
                    'cause': 'CHILD_POLICY_APPLIED'
                },
                'decisionTaskScheduledEventAttributes': {
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'startToCloseTimeout': 'string'
                },
                'decisionTaskStartedEventAttributes': {
                    'identity': 'string',
                    'scheduledEventId': 123
                },
                'decisionTaskCompletedEventAttributes': {
                    'executionContext': 'string',
                    'scheduledEventId': 123,
                    'startedEventId': 123
                },
                'decisionTaskTimedOutEventAttributes': {
                    'timeoutType': 'START_TO_CLOSE',
                    'scheduledEventId': 123,
                    'startedEventId': 123
                },
                'activityTaskScheduledEventAttributes': {
                    'activityType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'activityId': 'string',
                    'input': 'string',
                    'control': 'string',
                    'scheduleToStartTimeout': 'string',
                    'scheduleToCloseTimeout': 'string',
                    'startToCloseTimeout': 'string',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'heartbeatTimeout': 'string'
                },
                'activityTaskStartedEventAttributes': {
                    'identity': 'string',
                    'scheduledEventId': 123
                },
                'activityTaskCompletedEventAttributes': {
                    'result': 'string',
                    'scheduledEventId': 123,
                    'startedEventId': 123
                },
                'activityTaskFailedEventAttributes': {
                    'reason': 'string',
                    'details': 'string',
                    'scheduledEventId': 123,
                    'startedEventId': 123
                },
                'activityTaskTimedOutEventAttributes': {
                    'timeoutType': 'START_TO_CLOSE'|'SCHEDULE_TO_START'|'SCHEDULE_TO_CLOSE'|'HEARTBEAT',
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'details': 'string'
                },
                'activityTaskCanceledEventAttributes': {
                    'details': 'string',
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'latestCancelRequestedEventId': 123
                },
                'activityTaskCancelRequestedEventAttributes': {
                    'decisionTaskCompletedEventId': 123,
                    'activityId': 'string'
                },
                'workflowExecutionSignaledEventAttributes': {
                    'signalName': 'string',
                    'input': 'string',
                    'externalWorkflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'externalInitiatedEventId': 123
                },
                'markerRecordedEventAttributes': {
                    'markerName': 'string',
                    'details': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'recordMarkerFailedEventAttributes': {
                    'markerName': 'string',
                    'cause': 'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'timerStartedEventAttributes': {
                    'timerId': 'string',
                    'control': 'string',
                    'startToFireTimeout': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'timerFiredEventAttributes': {
                    'timerId': 'string',
                    'startedEventId': 123
                },
                'timerCanceledEventAttributes': {
                    'timerId': 'string',
                    'startedEventId': 123,
                    'decisionTaskCompletedEventId': 123
                },
                'startChildWorkflowExecutionInitiatedEventAttributes': {
                    'workflowId': 'string',
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'control': 'string',
                    'input': 'string',
                    'executionStartToCloseTimeout': 'string',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'taskStartToCloseTimeout': 'string',
                    'tagList': [
                        'string',
                    ],
                    'lambdaRole': 'string'
                },
                'childWorkflowExecutionStartedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'initiatedEventId': 123
                },
                'childWorkflowExecutionCompletedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'result': 'string',
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'childWorkflowExecutionFailedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'reason': 'string',
                    'details': 'string',
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'childWorkflowExecutionTimedOutEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'timeoutType': 'START_TO_CLOSE',
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'childWorkflowExecutionCanceledEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'details': 'string',
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'childWorkflowExecutionTerminatedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'signalExternalWorkflowExecutionInitiatedEventAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'signalName': 'string',
                    'input': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'externalWorkflowExecutionSignaledEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'initiatedEventId': 123
                },
                'signalExternalWorkflowExecutionFailedEventAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                    'initiatedEventId': 123,
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'externalWorkflowExecutionCancelRequestedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'initiatedEventId': 123
                },
                'requestCancelExternalWorkflowExecutionInitiatedEventAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'requestCancelExternalWorkflowExecutionFailedEventAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                    'initiatedEventId': 123,
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'scheduleActivityTaskFailedEventAttributes': {
                    'activityType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'activityId': 'string',
                    'cause': 'ACTIVITY_TYPE_DEPRECATED'|'ACTIVITY_TYPE_DOES_NOT_EXIST'|'ACTIVITY_ID_ALREADY_IN_USE'|'OPEN_ACTIVITIES_LIMIT_EXCEEDED'|'ACTIVITY_CREATION_RATE_EXCEEDED'|'DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED'|'DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'requestCancelActivityTaskFailedEventAttributes': {
                    'activityId': 'string',
                    'cause': 'ACTIVITY_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'startTimerFailedEventAttributes': {
                    'timerId': 'string',
                    'cause': 'TIMER_ID_ALREADY_IN_USE'|'OPEN_TIMERS_LIMIT_EXCEEDED'|'TIMER_CREATION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'cancelTimerFailedEventAttributes': {
                    'timerId': 'string',
                    'cause': 'TIMER_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'startChildWorkflowExecutionFailedEventAttributes': {
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'cause': 'WORKFLOW_TYPE_DOES_NOT_EXIST'|'WORKFLOW_TYPE_DEPRECATED'|'OPEN_CHILDREN_LIMIT_EXCEEDED'|'OPEN_WORKFLOWS_LIMIT_EXCEEDED'|'CHILD_CREATION_RATE_EXCEEDED'|'WORKFLOW_ALREADY_RUNNING'|'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_CHILD_POLICY_UNDEFINED'|'OPERATION_NOT_PERMITTED',
                    'workflowId': 'string',
                    'initiatedEventId': 123,
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'lambdaFunctionScheduledEventAttributes': {
                    'id': 'string',
                    'name': 'string',
                    'control': 'string',
                    'input': 'string',
                    'startToCloseTimeout': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'lambdaFunctionStartedEventAttributes': {
                    'scheduledEventId': 123
                },
                'lambdaFunctionCompletedEventAttributes': {
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'result': 'string'
                },
                'lambdaFunctionFailedEventAttributes': {
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'reason': 'string',
                    'details': 'string'
                },
                'lambdaFunctionTimedOutEventAttributes': {
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'timeoutType': 'START_TO_CLOSE'
                },
                'scheduleLambdaFunctionFailedEventAttributes': {
                    'id': 'string',
                    'name': 'string',
                    'cause': 'ID_ALREADY_IN_USE'|'OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED'|'LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED'|'LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION',
                    'decisionTaskCompletedEventId': 123
                },
                'startLambdaFunctionFailedEventAttributes': {
                    'scheduledEventId': 123,
                    'cause': 'ASSUME_ROLE_FAILED',
                    'message': 'string'
                }
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain containing the workflow execution.
    
    execution (dict) -- [REQUIRED]
    Specifies the workflow execution for which to return the history.
    
    workflowId (string) -- [REQUIRED]The user defined identifier associated with the workflow execution.
    
    runId (string) -- [REQUIRED]A system-generated unique identifier for the workflow execution.
    
    
    
    nextPageToken (string) -- If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: "Specified token has exceeded its maximum lifetime ".
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.
    reverseOrder (boolean) -- When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimeStamp of the events.
    
    """
    pass

def list_activity_types(domain=None, name=None, registrationStatus=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns information about all activities registered in the specified domain that match the specified name and registration status. The result includes information like creation date, current status of the activity, etc. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_activity_types(
        domain='string',
        name='string',
        registrationStatus='REGISTERED'|'DEPRECATED',
        nextPageToken='string',
        maximumPageSize=123,
        reverseOrder=True|False
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain in which the activity types have been registered.\n

    :type name: string
    :param name: If specified, only lists the activity types that have this name.

    :type registrationStatus: string
    :param registrationStatus: [REQUIRED]\nSpecifies the registration status of the activity types to list.\n

    :type nextPageToken: string
    :param nextPageToken: If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: 'Specified token has exceeded its maximum lifetime '.\nThe configured maximumPageSize determines how many results can be returned in a single call.\n

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the activity types.

    :rtype: dict

ReturnsResponse Syntax
{
    'typeInfos': [
        {
            'activityType': {
                'name': 'string',
                'version': 'string'
            },
            'status': 'REGISTERED'|'DEPRECATED',
            'description': 'string',
            'creationDate': datetime(2015, 1, 1),
            'deprecationDate': datetime(2015, 1, 1)
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
Contains a paginated list of activity type information structures.

typeInfos (list) --
List of activity type information.

(dict) --
Detailed information about an activity type.

activityType (dict) --
The  ActivityType type structure representing the activity type.

name (string) --
The name of this activity.

Note
The combination of activity type name and version must be unique within a domain.


version (string) --
The version of this activity.

Note
The combination of activity type name and version must be unique with in a domain.




status (string) --
The current status of the activity type.

description (string) --
The description of the activity type provided in  RegisterActivityType .

creationDate (datetime) --
The date and time this activity type was created through  RegisterActivityType .

deprecationDate (datetime) --
If DEPRECATED, the date and time  DeprecateActivityType was called.





nextPageToken (string) --
If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
The configured maximumPageSize determines how many results can be returned in a single call.







Exceptions

SWF.Client.exceptions.OperationNotPermittedFault
SWF.Client.exceptions.UnknownResourceFault


    :return: {
        'typeInfos': [
            {
                'activityType': {
                    'name': 'string',
                    'version': 'string'
                },
                'status': 'REGISTERED'|'DEPRECATED',
                'description': 'string',
                'creationDate': datetime(2015, 1, 1),
                'deprecationDate': datetime(2015, 1, 1)
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which the activity types have been registered.
    
    name (string) -- If specified, only lists the activity types that have this name.
    registrationStatus (string) -- [REQUIRED]
    Specifies the registration status of the activity types to list.
    
    nextPageToken (string) -- If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: "Specified token has exceeded its maximum lifetime ".
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the activity types.
    
    """
    pass

def list_closed_workflow_executions(domain=None, startTimeFilter=None, closeTimeFilter=None, executionFilter=None, closeStatusFilter=None, typeFilter=None, tagFilter=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns a list of closed workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_closed_workflow_executions(
        domain='string',
        startTimeFilter={
            'oldestDate': datetime(2015, 1, 1),
            'latestDate': datetime(2015, 1, 1)
        },
        closeTimeFilter={
            'oldestDate': datetime(2015, 1, 1),
            'latestDate': datetime(2015, 1, 1)
        },
        executionFilter={
            'workflowId': 'string'
        },
        closeStatusFilter={
            'status': 'COMPLETED'|'FAILED'|'CANCELED'|'TERMINATED'|'CONTINUED_AS_NEW'|'TIMED_OUT'
        },
        typeFilter={
            'name': 'string',
            'version': 'string'
        },
        tagFilter={
            'tag': 'string'
        },
        nextPageToken='string',
        maximumPageSize=123,
        reverseOrder=True|False
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain that contains the workflow executions to list.\n

    :type startTimeFilter: dict
    :param startTimeFilter: If specified, the workflow executions are included in the returned results based on whether their start times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their start times.\n\nNote\nstartTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.\n\n\noldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.\n\nlatestDate (datetime) --Specifies the latest start or close date and time to return.\n\n\n

    :type closeTimeFilter: dict
    :param closeTimeFilter: If specified, the workflow executions are included in the returned results based on whether their close times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their close times.\n\nNote\nstartTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.\n\n\noldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.\n\nlatestDate (datetime) --Specifies the latest start or close date and time to return.\n\n\n

    :type executionFilter: dict
    :param executionFilter: If specified, only workflow executions matching the workflow ID specified in the filter are returned.\n\nNote\ncloseStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nworkflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.\n\n\n

    :type closeStatusFilter: dict
    :param closeStatusFilter: If specified, only workflow executions that match this close status are listed. For example, if TERMINATED is specified, then only TERMINATED workflow executions are listed.\n\nNote\ncloseStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nstatus (string) -- [REQUIRED]The close status that must match the close status of an execution for it to meet the criteria of this filter.\n\n\n

    :type typeFilter: dict
    :param typeFilter: If specified, only executions of the type specified in the filter are returned.\n\nNote\ncloseStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nname (string) -- [REQUIRED]Name of the workflow type.\n\nversion (string) --Version of the workflow type.\n\n\n

    :type tagFilter: dict
    :param tagFilter: If specified, only executions that have the matching tag are listed.\n\nNote\ncloseStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\ntag (string) -- [REQUIRED]Specifies the tag that must be associated with the execution for it to meet the filter criteria.\nTags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .\n\n\n

    :type nextPageToken: string
    :param nextPageToken: If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: 'Specified token has exceeded its maximum lifetime '.\nThe configured maximumPageSize determines how many results can be returned in a single call.\n

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.

    :rtype: dict

ReturnsResponse Syntax
{
    'executionInfos': [
        {
            'execution': {
                'workflowId': 'string',
                'runId': 'string'
            },
            'workflowType': {
                'name': 'string',
                'version': 'string'
            },
            'startTimestamp': datetime(2015, 1, 1),
            'closeTimestamp': datetime(2015, 1, 1),
            'executionStatus': 'OPEN'|'CLOSED',
            'closeStatus': 'COMPLETED'|'FAILED'|'CANCELED'|'TERMINATED'|'CONTINUED_AS_NEW'|'TIMED_OUT',
            'parent': {
                'workflowId': 'string',
                'runId': 'string'
            },
            'tagList': [
                'string',
            ],
            'cancelRequested': True|False
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
Contains a paginated list of information about workflow executions.

executionInfos (list) --
The list of workflow information structures.

(dict) --
Contains information about a workflow execution.

execution (dict) --
The workflow execution this information is about.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




startTimestamp (datetime) --
The time when the execution was started.

closeTimestamp (datetime) --
The time when the workflow execution was closed. Set only if the execution status is CLOSED.

executionStatus (string) --
The current status of the execution.

closeStatus (string) --
If the execution status is closed then this specifies how the execution was closed:

COMPLETED \xe2\x80\x93 the execution was successfully completed.
CANCELED \xe2\x80\x93 the execution was canceled.Cancellation allows the implementation to gracefully clean up before the execution is closed.
TERMINATED \xe2\x80\x93 the execution was force terminated.
FAILED \xe2\x80\x93 the execution failed to complete.
TIMED_OUT \xe2\x80\x93 the execution did not complete in the alloted time and was automatically timed out.
CONTINUED_AS_NEW \xe2\x80\x93 the execution is logically continued. This means the current execution was completed and a new execution was started to carry on the workflow.


parent (dict) --
If this workflow execution is a child of another execution then contains the workflow execution that started this execution.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



tagList (list) --
The list of tags associated with the workflow execution. Tags can be used to identify and list workflow executions of interest through the visibility APIs. A workflow execution can have a maximum of 5 tags.

(string) --


cancelRequested (boolean) --
Set to true if a cancellation is requested for this workflow execution.





nextPageToken (string) --
If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
The configured maximumPageSize determines how many results can be returned in a single call.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'executionInfos': [
            {
                'execution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'startTimestamp': datetime(2015, 1, 1),
                'closeTimestamp': datetime(2015, 1, 1),
                'executionStatus': 'OPEN'|'CLOSED',
                'closeStatus': 'COMPLETED'|'FAILED'|'CANCELED'|'TERMINATED'|'CONTINUED_AS_NEW'|'TIMED_OUT',
                'parent': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'tagList': [
                    'string',
                ],
                'cancelRequested': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain that contains the workflow executions to list.
    
    startTimeFilter (dict) -- If specified, the workflow executions are included in the returned results based on whether their start times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their start times.
    
    Note
    startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
    
    
    oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
    
    latestDate (datetime) --Specifies the latest start or close date and time to return.
    
    
    
    closeTimeFilter (dict) -- If specified, the workflow executions are included in the returned results based on whether their close times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their close times.
    
    Note
    startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
    
    
    oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
    
    latestDate (datetime) --Specifies the latest start or close date and time to return.
    
    
    
    executionFilter (dict) -- If specified, only workflow executions matching the workflow ID specified in the filter are returned.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
    
    
    
    closeStatusFilter (dict) -- If specified, only workflow executions that match this close status are listed. For example, if TERMINATED is specified, then only TERMINATED workflow executions are listed.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    status (string) -- [REQUIRED]The close status that must match the close status of an execution for it to meet the criteria of this filter.
    
    
    
    typeFilter (dict) -- If specified, only executions of the type specified in the filter are returned.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    name (string) -- [REQUIRED]Name of the workflow type.
    
    version (string) --Version of the workflow type.
    
    
    
    tagFilter (dict) -- If specified, only executions that have the matching tag are listed.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    tag (string) -- [REQUIRED]Specifies the tag that must be associated with the execution for it to meet the filter criteria.
    Tags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .
    
    
    
    nextPageToken (string) -- If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: "Specified token has exceeded its maximum lifetime ".
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.
    
    """
    pass

def list_domains(nextPageToken=None, registrationStatus=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns the list of domains registered in the account. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_domains(
        nextPageToken='string',
        registrationStatus='REGISTERED'|'DEPRECATED',
        maximumPageSize=123,
        reverseOrder=True|False
    )
    
    
    :type nextPageToken: string
    :param nextPageToken: If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: 'Specified token has exceeded its maximum lifetime '.\nThe configured maximumPageSize determines how many results can be returned in a single call.\n

    :type registrationStatus: string
    :param registrationStatus: [REQUIRED]\nSpecifies the registration status of the domains to list.\n

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the domains.

    :rtype: dict

ReturnsResponse Syntax
{
    'domainInfos': [
        {
            'name': 'string',
            'status': 'REGISTERED'|'DEPRECATED',
            'description': 'string',
            'arn': 'string'
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
Contains a paginated collection of DomainInfo structures.

domainInfos (list) --
A list of DomainInfo structures.

(dict) --
Contains general information about a domain.

name (string) --
The name of the domain. This name is unique within the account.

status (string) --
The status of the domain:

REGISTERED \xe2\x80\x93 The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions.
DEPRECATED \xe2\x80\x93 The domain was deprecated using  DeprecateDomain , but is still in use. You should not create new workflow executions in this domain.


description (string) --
The description of the domain provided through  RegisterDomain .

arn (string) --
The ARN of the domain.





nextPageToken (string) --
If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
The configured maximumPageSize determines how many results can be returned in a single call.







Exceptions

SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'domainInfos': [
            {
                'name': 'string',
                'status': 'REGISTERED'|'DEPRECATED',
                'description': 'string',
                'arn': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    nextPageToken (string) -- If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: "Specified token has exceeded its maximum lifetime ".
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    registrationStatus (string) -- [REQUIRED]
    Specifies the registration status of the domains to list.
    
    maximumPageSize (integer) -- The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the domains.
    
    """
    pass

def list_open_workflow_executions(domain=None, startTimeFilter=None, typeFilter=None, tagFilter=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None, executionFilter=None):
    """
    Returns a list of open workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_open_workflow_executions(
        domain='string',
        startTimeFilter={
            'oldestDate': datetime(2015, 1, 1),
            'latestDate': datetime(2015, 1, 1)
        },
        typeFilter={
            'name': 'string',
            'version': 'string'
        },
        tagFilter={
            'tag': 'string'
        },
        nextPageToken='string',
        maximumPageSize=123,
        reverseOrder=True|False,
        executionFilter={
            'workflowId': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain that contains the workflow executions to list.\n

    :type startTimeFilter: dict
    :param startTimeFilter: [REQUIRED]\nWorkflow executions are included in the returned results based on whether their start times are within the range specified by this filter.\n\noldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.\n\nlatestDate (datetime) --Specifies the latest start or close date and time to return.\n\n\n

    :type typeFilter: dict
    :param typeFilter: If specified, only executions of the type specified in the filter are returned.\n\nNote\nexecutionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nname (string) -- [REQUIRED]Name of the workflow type.\n\nversion (string) --Version of the workflow type.\n\n\n

    :type tagFilter: dict
    :param tagFilter: If specified, only executions that have the matching tag are listed.\n\nNote\nexecutionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\ntag (string) -- [REQUIRED]Specifies the tag that must be associated with the execution for it to meet the filter criteria.\nTags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .\n\n\n

    :type nextPageToken: string
    :param nextPageToken: If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: 'Specified token has exceeded its maximum lifetime '.\nThe configured maximumPageSize determines how many results can be returned in a single call.\n

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default the results are returned in descending order of the start time of the executions.

    :type executionFilter: dict
    :param executionFilter: If specified, only workflow executions matching the workflow ID specified in the filter are returned.\n\nNote\nexecutionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.\n\n\nworkflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'executionInfos': [
        {
            'execution': {
                'workflowId': 'string',
                'runId': 'string'
            },
            'workflowType': {
                'name': 'string',
                'version': 'string'
            },
            'startTimestamp': datetime(2015, 1, 1),
            'closeTimestamp': datetime(2015, 1, 1),
            'executionStatus': 'OPEN'|'CLOSED',
            'closeStatus': 'COMPLETED'|'FAILED'|'CANCELED'|'TERMINATED'|'CONTINUED_AS_NEW'|'TIMED_OUT',
            'parent': {
                'workflowId': 'string',
                'runId': 'string'
            },
            'tagList': [
                'string',
            ],
            'cancelRequested': True|False
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
Contains a paginated list of information about workflow executions.

executionInfos (list) --
The list of workflow information structures.

(dict) --
Contains information about a workflow execution.

execution (dict) --
The workflow execution this information is about.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




startTimestamp (datetime) --
The time when the execution was started.

closeTimestamp (datetime) --
The time when the workflow execution was closed. Set only if the execution status is CLOSED.

executionStatus (string) --
The current status of the execution.

closeStatus (string) --
If the execution status is closed then this specifies how the execution was closed:

COMPLETED \xe2\x80\x93 the execution was successfully completed.
CANCELED \xe2\x80\x93 the execution was canceled.Cancellation allows the implementation to gracefully clean up before the execution is closed.
TERMINATED \xe2\x80\x93 the execution was force terminated.
FAILED \xe2\x80\x93 the execution failed to complete.
TIMED_OUT \xe2\x80\x93 the execution did not complete in the alloted time and was automatically timed out.
CONTINUED_AS_NEW \xe2\x80\x93 the execution is logically continued. This means the current execution was completed and a new execution was started to carry on the workflow.


parent (dict) --
If this workflow execution is a child of another execution then contains the workflow execution that started this execution.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



tagList (list) --
The list of tags associated with the workflow execution. Tags can be used to identify and list workflow executions of interest through the visibility APIs. A workflow execution can have a maximum of 5 tags.

(string) --


cancelRequested (boolean) --
Set to true if a cancellation is requested for this workflow execution.





nextPageToken (string) --
If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
The configured maximumPageSize determines how many results can be returned in a single call.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'executionInfos': [
            {
                'execution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'startTimestamp': datetime(2015, 1, 1),
                'closeTimestamp': datetime(2015, 1, 1),
                'executionStatus': 'OPEN'|'CLOSED',
                'closeStatus': 'COMPLETED'|'FAILED'|'CANCELED'|'TERMINATED'|'CONTINUED_AS_NEW'|'TIMED_OUT',
                'parent': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'tagList': [
                    'string',
                ],
                'cancelRequested': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain that contains the workflow executions to list.
    
    startTimeFilter (dict) -- [REQUIRED]
    Workflow executions are included in the returned results based on whether their start times are within the range specified by this filter.
    
    oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
    
    latestDate (datetime) --Specifies the latest start or close date and time to return.
    
    
    
    typeFilter (dict) -- If specified, only executions of the type specified in the filter are returned.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    name (string) -- [REQUIRED]Name of the workflow type.
    
    version (string) --Version of the workflow type.
    
    
    
    tagFilter (dict) -- If specified, only executions that have the matching tag are listed.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    tag (string) -- [REQUIRED]Specifies the tag that must be associated with the execution for it to meet the filter criteria.
    Tags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .
    
    
    
    nextPageToken (string) -- If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: "Specified token has exceeded its maximum lifetime ".
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default the results are returned in descending order of the start time of the executions.
    executionFilter (dict) -- If specified, only workflow executions matching the workflow ID specified in the filter are returned.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
    
    
    
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    List tags for a given domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the Amazon SWF domain.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
tags (list) --An array of tags associated with the domain.

(dict) --Tags are key-value pairs that can be associated with Amazon SWF state machines and activities.
Tags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .

key (string) --The key of a tag.

value (string) --The value of a tag.










Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.LimitExceededFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_workflow_types(domain=None, name=None, registrationStatus=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns information about workflow types in the specified domain. The results may be split into multiple pages that can be retrieved by making the call repeatedly.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_workflow_types(
        domain='string',
        name='string',
        registrationStatus='REGISTERED'|'DEPRECATED',
        nextPageToken='string',
        maximumPageSize=123,
        reverseOrder=True|False
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain in which the workflow types have been registered.\n

    :type name: string
    :param name: If specified, lists the workflow type with this name.

    :type registrationStatus: string
    :param registrationStatus: [REQUIRED]\nSpecifies the registration status of the workflow types to list.\n

    :type nextPageToken: string
    :param nextPageToken: If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: 'Specified token has exceeded its maximum lifetime '.\nThe configured maximumPageSize determines how many results can be returned in a single call.\n

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default the results are returned in ascending alphabetical order of the name of the workflow types.

    :rtype: dict

ReturnsResponse Syntax
{
    'typeInfos': [
        {
            'workflowType': {
                'name': 'string',
                'version': 'string'
            },
            'status': 'REGISTERED'|'DEPRECATED',
            'description': 'string',
            'creationDate': datetime(2015, 1, 1),
            'deprecationDate': datetime(2015, 1, 1)
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
Contains a paginated list of information structures about workflow types.

typeInfos (list) --
The list of workflow type information.

(dict) --
Contains information about a workflow type.

workflowType (dict) --
The workflow type this information is about.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




status (string) --
The current status of the workflow type.

description (string) --
The description of the type registered through  RegisterWorkflowType .

creationDate (datetime) --
The date when this type was registered.

deprecationDate (datetime) --
If the type is in deprecated state, then it is set to the date when the type was deprecated.





nextPageToken (string) --
If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
The configured maximumPageSize determines how many results can be returned in a single call.







Exceptions

SWF.Client.exceptions.OperationNotPermittedFault
SWF.Client.exceptions.UnknownResourceFault


    :return: {
        'typeInfos': [
            {
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'status': 'REGISTERED'|'DEPRECATED',
                'description': 'string',
                'creationDate': datetime(2015, 1, 1),
                'deprecationDate': datetime(2015, 1, 1)
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which the workflow types have been registered.
    
    name (string) -- If specified, lists the workflow type with this name.
    registrationStatus (string) -- [REQUIRED]
    Specifies the registration status of the workflow types to list.
    
    nextPageToken (string) -- If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: "Specified token has exceeded its maximum lifetime ".
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default the results are returned in ascending alphabetical order of the name of the workflow types.
    
    """
    pass

def poll_for_activity_task(domain=None, taskList=None, identity=None):
    """
    Used by workers to get an  ActivityTask from the specified activity taskList . This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available. The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns an empty result. An empty result, in this context, means that an ActivityTask is returned, but that the value of taskToken is an empty string. If a task is returned, the worker should use its type to identify and process it correctly.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.poll_for_activity_task(
        domain='string',
        taskList={
            'name': 'string'
        },
        identity='string'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain that contains the task lists being polled.\n

    :type taskList: dict
    :param taskList: [REQUIRED]\nSpecifies the task list to poll for activity tasks.\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n

    :type identity: string
    :param identity: Identity of the worker making the request, recorded in the ActivityTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.

    :rtype: dict

ReturnsResponse Syntax
{
    'taskToken': 'string',
    'activityId': 'string',
    'startedEventId': 123,
    'workflowExecution': {
        'workflowId': 'string',
        'runId': 'string'
    },
    'activityType': {
        'name': 'string',
        'version': 'string'
    },
    'input': 'string'
}


Response Structure

(dict) --
Unit of work sent to an activity worker.

taskToken (string) --
The opaque string used as a handle on the task. This token is used by workers to communicate progress and response information back to the system about the task.

activityId (string) --
The unique ID of the task.

startedEventId (integer) --
The ID of the ActivityTaskStarted event recorded in the history.

workflowExecution (dict) --
The workflow execution that started this activity task.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



activityType (dict) --
The type of this activity task.

name (string) --
The name of this activity.

Note
The combination of activity type name and version must be unique within a domain.


version (string) --
The version of this activity.

Note
The combination of activity type name and version must be unique with in a domain.




input (string) --
The inputs provided when the activity task was scheduled. The form of the input is user defined and should be meaningful to the activity implementation.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault
SWF.Client.exceptions.LimitExceededFault


    :return: {
        'taskToken': 'string',
        'activityId': 'string',
        'startedEventId': 123,
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'activityType': {
            'name': 'string',
            'version': 'string'
        },
        'input': 'string'
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain that contains the task lists being polled.
    
    taskList (dict) -- [REQUIRED]
    Specifies the task list to poll for activity tasks.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    identity (string) -- Identity of the worker making the request, recorded in the ActivityTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
    
    """
    pass

def poll_for_decision_task(domain=None, taskList=None, identity=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Used by deciders to get a  DecisionTask from the specified decision taskList . A decision task may be returned for any open workflow execution that is using the specified task list. The task includes a paginated view of the history of the workflow execution. The decider should use the workflow type and the history to determine how to properly handle the task.
    This action initiates a long poll, where the service holds the HTTP connection open and responds as soon a task becomes available. If no decision task is available in the specified task list before the timeout of 60 seconds expires, an empty result is returned. An empty result, in this context, means that a DecisionTask is returned, but that the value of taskToken is an empty string.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.poll_for_decision_task(
        domain='string',
        taskList={
            'name': 'string'
        },
        identity='string',
        nextPageToken='string',
        maximumPageSize=123,
        reverseOrder=True|False
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain containing the task lists to poll.\n

    :type taskList: dict
    :param taskList: [REQUIRED]\nSpecifies the task list to poll for decision tasks.\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n

    :type identity: string
    :param identity: Identity of the decider making the request, which is recorded in the DecisionTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.

    :type nextPageToken: string
    :param nextPageToken: If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: 'Specified token has exceeded its maximum lifetime '.\nThe configured maximumPageSize determines how many results can be returned in a single call.\n\nNote\nThe nextPageToken returned by this action cannot be used with GetWorkflowExecutionHistory to get the next page. You must call PollForDecisionTask again (with the nextPageToken ) to retrieve the next page of history records. Calling PollForDecisionTask with a nextPageToken doesn\'t return a new decision task.\n\n

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.\nThis is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.\n

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimestamp of the events.

    :rtype: dict

ReturnsResponse Syntax
{
    'taskToken': 'string',
    'startedEventId': 123,
    'workflowExecution': {
        'workflowId': 'string',
        'runId': 'string'
    },
    'workflowType': {
        'name': 'string',
        'version': 'string'
    },
    'events': [
        {
            'eventTimestamp': datetime(2015, 1, 1),
            'eventType': 'WorkflowExecutionStarted'|'WorkflowExecutionCancelRequested'|'WorkflowExecutionCompleted'|'CompleteWorkflowExecutionFailed'|'WorkflowExecutionFailed'|'FailWorkflowExecutionFailed'|'WorkflowExecutionTimedOut'|'WorkflowExecutionCanceled'|'CancelWorkflowExecutionFailed'|'WorkflowExecutionContinuedAsNew'|'ContinueAsNewWorkflowExecutionFailed'|'WorkflowExecutionTerminated'|'DecisionTaskScheduled'|'DecisionTaskStarted'|'DecisionTaskCompleted'|'DecisionTaskTimedOut'|'ActivityTaskScheduled'|'ScheduleActivityTaskFailed'|'ActivityTaskStarted'|'ActivityTaskCompleted'|'ActivityTaskFailed'|'ActivityTaskTimedOut'|'ActivityTaskCanceled'|'ActivityTaskCancelRequested'|'RequestCancelActivityTaskFailed'|'WorkflowExecutionSignaled'|'MarkerRecorded'|'RecordMarkerFailed'|'TimerStarted'|'StartTimerFailed'|'TimerFired'|'TimerCanceled'|'CancelTimerFailed'|'StartChildWorkflowExecutionInitiated'|'StartChildWorkflowExecutionFailed'|'ChildWorkflowExecutionStarted'|'ChildWorkflowExecutionCompleted'|'ChildWorkflowExecutionFailed'|'ChildWorkflowExecutionTimedOut'|'ChildWorkflowExecutionCanceled'|'ChildWorkflowExecutionTerminated'|'SignalExternalWorkflowExecutionInitiated'|'SignalExternalWorkflowExecutionFailed'|'ExternalWorkflowExecutionSignaled'|'RequestCancelExternalWorkflowExecutionInitiated'|'RequestCancelExternalWorkflowExecutionFailed'|'ExternalWorkflowExecutionCancelRequested'|'LambdaFunctionScheduled'|'LambdaFunctionStarted'|'LambdaFunctionCompleted'|'LambdaFunctionFailed'|'LambdaFunctionTimedOut'|'ScheduleLambdaFunctionFailed'|'StartLambdaFunctionFailed',
            'eventId': 123,
            'workflowExecutionStartedEventAttributes': {
                'input': 'string',
                'executionStartToCloseTimeout': 'string',
                'taskStartToCloseTimeout': 'string',
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'tagList': [
                    'string',
                ],
                'continuedExecutionRunId': 'string',
                'parentWorkflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'parentInitiatedEventId': 123,
                'lambdaRole': 'string'
            },
            'workflowExecutionCompletedEventAttributes': {
                'result': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'completeWorkflowExecutionFailedEventAttributes': {
                'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'workflowExecutionFailedEventAttributes': {
                'reason': 'string',
                'details': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'failWorkflowExecutionFailedEventAttributes': {
                'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'workflowExecutionTimedOutEventAttributes': {
                'timeoutType': 'START_TO_CLOSE',
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON'
            },
            'workflowExecutionCanceledEventAttributes': {
                'details': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'cancelWorkflowExecutionFailedEventAttributes': {
                'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'workflowExecutionContinuedAsNewEventAttributes': {
                'input': 'string',
                'decisionTaskCompletedEventId': 123,
                'newExecutionRunId': 'string',
                'executionStartToCloseTimeout': 'string',
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'taskStartToCloseTimeout': 'string',
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                'tagList': [
                    'string',
                ],
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'lambdaRole': 'string'
            },
            'continueAsNewWorkflowExecutionFailedEventAttributes': {
                'cause': 'UNHANDLED_DECISION'|'WORKFLOW_TYPE_DEPRECATED'|'WORKFLOW_TYPE_DOES_NOT_EXIST'|'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_CHILD_POLICY_UNDEFINED'|'CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'workflowExecutionTerminatedEventAttributes': {
                'reason': 'string',
                'details': 'string',
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                'cause': 'CHILD_POLICY_APPLIED'|'EVENT_LIMIT_EXCEEDED'|'OPERATOR_INITIATED'
            },
            'workflowExecutionCancelRequestedEventAttributes': {
                'externalWorkflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'externalInitiatedEventId': 123,
                'cause': 'CHILD_POLICY_APPLIED'
            },
            'decisionTaskScheduledEventAttributes': {
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'startToCloseTimeout': 'string'
            },
            'decisionTaskStartedEventAttributes': {
                'identity': 'string',
                'scheduledEventId': 123
            },
            'decisionTaskCompletedEventAttributes': {
                'executionContext': 'string',
                'scheduledEventId': 123,
                'startedEventId': 123
            },
            'decisionTaskTimedOutEventAttributes': {
                'timeoutType': 'START_TO_CLOSE',
                'scheduledEventId': 123,
                'startedEventId': 123
            },
            'activityTaskScheduledEventAttributes': {
                'activityType': {
                    'name': 'string',
                    'version': 'string'
                },
                'activityId': 'string',
                'input': 'string',
                'control': 'string',
                'scheduleToStartTimeout': 'string',
                'scheduleToCloseTimeout': 'string',
                'startToCloseTimeout': 'string',
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'decisionTaskCompletedEventId': 123,
                'heartbeatTimeout': 'string'
            },
            'activityTaskStartedEventAttributes': {
                'identity': 'string',
                'scheduledEventId': 123
            },
            'activityTaskCompletedEventAttributes': {
                'result': 'string',
                'scheduledEventId': 123,
                'startedEventId': 123
            },
            'activityTaskFailedEventAttributes': {
                'reason': 'string',
                'details': 'string',
                'scheduledEventId': 123,
                'startedEventId': 123
            },
            'activityTaskTimedOutEventAttributes': {
                'timeoutType': 'START_TO_CLOSE'|'SCHEDULE_TO_START'|'SCHEDULE_TO_CLOSE'|'HEARTBEAT',
                'scheduledEventId': 123,
                'startedEventId': 123,
                'details': 'string'
            },
            'activityTaskCanceledEventAttributes': {
                'details': 'string',
                'scheduledEventId': 123,
                'startedEventId': 123,
                'latestCancelRequestedEventId': 123
            },
            'activityTaskCancelRequestedEventAttributes': {
                'decisionTaskCompletedEventId': 123,
                'activityId': 'string'
            },
            'workflowExecutionSignaledEventAttributes': {
                'signalName': 'string',
                'input': 'string',
                'externalWorkflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'externalInitiatedEventId': 123
            },
            'markerRecordedEventAttributes': {
                'markerName': 'string',
                'details': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'recordMarkerFailedEventAttributes': {
                'markerName': 'string',
                'cause': 'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'timerStartedEventAttributes': {
                'timerId': 'string',
                'control': 'string',
                'startToFireTimeout': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'timerFiredEventAttributes': {
                'timerId': 'string',
                'startedEventId': 123
            },
            'timerCanceledEventAttributes': {
                'timerId': 'string',
                'startedEventId': 123,
                'decisionTaskCompletedEventId': 123
            },
            'startChildWorkflowExecutionInitiatedEventAttributes': {
                'workflowId': 'string',
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'control': 'string',
                'input': 'string',
                'executionStartToCloseTimeout': 'string',
                'taskList': {
                    'name': 'string'
                },
                'taskPriority': 'string',
                'decisionTaskCompletedEventId': 123,
                'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                'taskStartToCloseTimeout': 'string',
                'tagList': [
                    'string',
                ],
                'lambdaRole': 'string'
            },
            'childWorkflowExecutionStartedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'initiatedEventId': 123
            },
            'childWorkflowExecutionCompletedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'result': 'string',
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'childWorkflowExecutionFailedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'reason': 'string',
                'details': 'string',
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'childWorkflowExecutionTimedOutEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'timeoutType': 'START_TO_CLOSE',
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'childWorkflowExecutionCanceledEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'details': 'string',
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'childWorkflowExecutionTerminatedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'initiatedEventId': 123,
                'startedEventId': 123
            },
            'signalExternalWorkflowExecutionInitiatedEventAttributes': {
                'workflowId': 'string',
                'runId': 'string',
                'signalName': 'string',
                'input': 'string',
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'externalWorkflowExecutionSignaledEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'initiatedEventId': 123
            },
            'signalExternalWorkflowExecutionFailedEventAttributes': {
                'workflowId': 'string',
                'runId': 'string',
                'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                'initiatedEventId': 123,
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'externalWorkflowExecutionCancelRequestedEventAttributes': {
                'workflowExecution': {
                    'workflowId': 'string',
                    'runId': 'string'
                },
                'initiatedEventId': 123
            },
            'requestCancelExternalWorkflowExecutionInitiatedEventAttributes': {
                'workflowId': 'string',
                'runId': 'string',
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'requestCancelExternalWorkflowExecutionFailedEventAttributes': {
                'workflowId': 'string',
                'runId': 'string',
                'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                'initiatedEventId': 123,
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'scheduleActivityTaskFailedEventAttributes': {
                'activityType': {
                    'name': 'string',
                    'version': 'string'
                },
                'activityId': 'string',
                'cause': 'ACTIVITY_TYPE_DEPRECATED'|'ACTIVITY_TYPE_DOES_NOT_EXIST'|'ACTIVITY_ID_ALREADY_IN_USE'|'OPEN_ACTIVITIES_LIMIT_EXCEEDED'|'ACTIVITY_CREATION_RATE_EXCEEDED'|'DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED'|'DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'requestCancelActivityTaskFailedEventAttributes': {
                'activityId': 'string',
                'cause': 'ACTIVITY_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'startTimerFailedEventAttributes': {
                'timerId': 'string',
                'cause': 'TIMER_ID_ALREADY_IN_USE'|'OPEN_TIMERS_LIMIT_EXCEEDED'|'TIMER_CREATION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'cancelTimerFailedEventAttributes': {
                'timerId': 'string',
                'cause': 'TIMER_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
                'decisionTaskCompletedEventId': 123
            },
            'startChildWorkflowExecutionFailedEventAttributes': {
                'workflowType': {
                    'name': 'string',
                    'version': 'string'
                },
                'cause': 'WORKFLOW_TYPE_DOES_NOT_EXIST'|'WORKFLOW_TYPE_DEPRECATED'|'OPEN_CHILDREN_LIMIT_EXCEEDED'|'OPEN_WORKFLOWS_LIMIT_EXCEEDED'|'CHILD_CREATION_RATE_EXCEEDED'|'WORKFLOW_ALREADY_RUNNING'|'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_CHILD_POLICY_UNDEFINED'|'OPERATION_NOT_PERMITTED',
                'workflowId': 'string',
                'initiatedEventId': 123,
                'decisionTaskCompletedEventId': 123,
                'control': 'string'
            },
            'lambdaFunctionScheduledEventAttributes': {
                'id': 'string',
                'name': 'string',
                'control': 'string',
                'input': 'string',
                'startToCloseTimeout': 'string',
                'decisionTaskCompletedEventId': 123
            },
            'lambdaFunctionStartedEventAttributes': {
                'scheduledEventId': 123
            },
            'lambdaFunctionCompletedEventAttributes': {
                'scheduledEventId': 123,
                'startedEventId': 123,
                'result': 'string'
            },
            'lambdaFunctionFailedEventAttributes': {
                'scheduledEventId': 123,
                'startedEventId': 123,
                'reason': 'string',
                'details': 'string'
            },
            'lambdaFunctionTimedOutEventAttributes': {
                'scheduledEventId': 123,
                'startedEventId': 123,
                'timeoutType': 'START_TO_CLOSE'
            },
            'scheduleLambdaFunctionFailedEventAttributes': {
                'id': 'string',
                'name': 'string',
                'cause': 'ID_ALREADY_IN_USE'|'OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED'|'LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED'|'LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION',
                'decisionTaskCompletedEventId': 123
            },
            'startLambdaFunctionFailedEventAttributes': {
                'scheduledEventId': 123,
                'cause': 'ASSUME_ROLE_FAILED',
                'message': 'string'
            }
        },
    ],
    'nextPageToken': 'string',
    'previousStartedEventId': 123
}


Response Structure

(dict) --
A structure that represents a decision task. Decision tasks are sent to deciders in order for them to make decisions.

taskToken (string) --
The opaque string used as a handle on the task. This token is used by workers to communicate progress and response information back to the system about the task.

startedEventId (integer) --
The ID of the DecisionTaskStarted event recorded in the history.

workflowExecution (dict) --
The workflow execution for which this decision task was created.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the workflow execution for which this decision task was created.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




events (list) --
A paginated list of history events of the workflow execution. The decider uses this during the processing of the decision task.

(dict) --
Event within a workflow execution. A history event can be one of these types:

ActivityTaskCancelRequested \xe2\x80\x93 A RequestCancelActivityTask decision was received by the system.
ActivityTaskCanceled \xe2\x80\x93 The activity task was successfully canceled.
ActivityTaskCompleted \xe2\x80\x93 An activity worker successfully completed an activity task by calling  RespondActivityTaskCompleted .
ActivityTaskFailed \xe2\x80\x93 An activity worker failed an activity task by calling  RespondActivityTaskFailed .
ActivityTaskScheduled \xe2\x80\x93 An activity task was scheduled for execution.
ActivityTaskStarted \xe2\x80\x93 The scheduled activity task was dispatched to a worker.
ActivityTaskTimedOut \xe2\x80\x93 The activity task timed out.
CancelTimerFailed \xe2\x80\x93 Failed to process CancelTimer decision. This happens when the decision isn\'t configured properly, for example no timer exists with the specified timer Id.
CancelWorkflowExecutionFailed \xe2\x80\x93 A request to cancel a workflow execution failed.
ChildWorkflowExecutionCanceled \xe2\x80\x93 A child workflow execution, started by this workflow execution, was canceled and closed.
ChildWorkflowExecutionCompleted \xe2\x80\x93 A child workflow execution, started by this workflow execution, completed successfully and was closed.
ChildWorkflowExecutionFailed \xe2\x80\x93 A child workflow execution, started by this workflow execution, failed to complete successfully and was closed.
ChildWorkflowExecutionStarted \xe2\x80\x93 A child workflow execution was successfully started.
ChildWorkflowExecutionTerminated \xe2\x80\x93 A child workflow execution, started by this workflow execution, was terminated.
ChildWorkflowExecutionTimedOut \xe2\x80\x93 A child workflow execution, started by this workflow execution, timed out and was closed.
CompleteWorkflowExecutionFailed \xe2\x80\x93 The workflow execution failed to complete.
ContinueAsNewWorkflowExecutionFailed \xe2\x80\x93 The workflow execution failed to complete after being continued as a new workflow execution.
DecisionTaskCompleted \xe2\x80\x93 The decider successfully completed a decision task by calling  RespondDecisionTaskCompleted .
DecisionTaskScheduled \xe2\x80\x93 A decision task was scheduled for the workflow execution.
DecisionTaskStarted \xe2\x80\x93 The decision task was dispatched to a decider.
DecisionTaskTimedOut \xe2\x80\x93 The decision task timed out.
ExternalWorkflowExecutionCancelRequested \xe2\x80\x93 Request to cancel an external workflow execution was successfully delivered to the target execution.
ExternalWorkflowExecutionSignaled \xe2\x80\x93 A signal, requested by this workflow execution, was successfully delivered to the target external workflow execution.
FailWorkflowExecutionFailed \xe2\x80\x93 A request to mark a workflow execution as failed, itself failed.
MarkerRecorded \xe2\x80\x93 A marker was recorded in the workflow history as the result of a RecordMarker decision.
RecordMarkerFailed \xe2\x80\x93 A RecordMarker decision was returned as failed.
RequestCancelActivityTaskFailed \xe2\x80\x93 Failed to process RequestCancelActivityTask decision. This happens when the decision isn\'t configured properly.
RequestCancelExternalWorkflowExecutionFailed \xe2\x80\x93 Request to cancel an external workflow execution failed.
RequestCancelExternalWorkflowExecutionInitiated \xe2\x80\x93 A request was made to request the cancellation of an external workflow execution.
ScheduleActivityTaskFailed \xe2\x80\x93 Failed to process ScheduleActivityTask decision. This happens when the decision isn\'t configured properly, for example the activity type specified isn\'t registered.
SignalExternalWorkflowExecutionFailed \xe2\x80\x93 The request to signal an external workflow execution failed.
SignalExternalWorkflowExecutionInitiated \xe2\x80\x93 A request to signal an external workflow was made.
StartActivityTaskFailed \xe2\x80\x93 A scheduled activity task failed to start.
StartChildWorkflowExecutionFailed \xe2\x80\x93 Failed to process StartChildWorkflowExecution decision. This happens when the decision isn\'t configured properly, for example the workflow type specified isn\'t registered.
StartChildWorkflowExecutionInitiated \xe2\x80\x93 A request was made to start a child workflow execution.
StartTimerFailed \xe2\x80\x93 Failed to process StartTimer decision. This happens when the decision isn\'t configured properly, for example a timer already exists with the specified timer Id.
TimerCanceled \xe2\x80\x93 A timer, previously started for this workflow execution, was successfully canceled.
TimerFired \xe2\x80\x93 A timer, previously started for this workflow execution, fired.
TimerStarted \xe2\x80\x93 A timer was started for the workflow execution due to a StartTimer decision.
WorkflowExecutionCancelRequested \xe2\x80\x93 A request to cancel this workflow execution was made.
WorkflowExecutionCanceled \xe2\x80\x93 The workflow execution was successfully canceled and closed.
WorkflowExecutionCompleted \xe2\x80\x93 The workflow execution was closed due to successful completion.
WorkflowExecutionContinuedAsNew \xe2\x80\x93 The workflow execution was closed and a new execution of the same type was created with the same workflowId.
WorkflowExecutionFailed \xe2\x80\x93 The workflow execution closed due to a failure.
WorkflowExecutionSignaled \xe2\x80\x93 An external signal was received for the workflow execution.
WorkflowExecutionStarted \xe2\x80\x93 The workflow execution was started.
WorkflowExecutionTerminated \xe2\x80\x93 The workflow execution was terminated.
WorkflowExecutionTimedOut \xe2\x80\x93 The workflow execution was closed because a time out was exceeded.


eventTimestamp (datetime) --
The date and time when the event occurred.

eventType (string) --
The type of the history event.

eventId (integer) --
The system generated ID of the event. This ID uniquely identifies the event with in the workflow execution history.

workflowExecutionStartedEventAttributes (dict) --
If the event is of type WorkflowExecutionStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

input (string) --
The input provided to the workflow execution.

executionStartToCloseTimeout (string) --
The maximum duration for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

taskStartToCloseTimeout (string) --
The maximum duration of decision tasks for this workflow type.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

childPolicy (string) --
The policy to use for the child workflow executions if this workflow execution is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


taskList (dict) --
The name of the task list for scheduling the decision tasks for this workflow execution.

name (string) --
The name of the task list.



taskPriority (string) --
The priority of the decision tasks in the workflow execution.

workflowType (dict) --
The workflow type of this execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




tagList (list) --
The list of tags associated with this workflow execution. An execution can have up to 5 tags.

(string) --


continuedExecutionRunId (string) --
If this workflow execution was started due to a ContinueAsNewWorkflowExecution decision, then it contains the runId of the previous workflow execution that was closed and continued as this execution.

parentWorkflowExecution (dict) --
The source workflow execution that started this workflow execution. The member isn\'t set if the workflow execution was not started by a workflow.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



parentInitiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this workflow execution. The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

lambdaRole (string) --
The IAM role attached to the workflow execution.



workflowExecutionCompletedEventAttributes (dict) --
If the event is of type WorkflowExecutionCompleted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

result (string) --
The result produced by the workflow execution upon successful completion.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CompleteWorkflowExecution decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



completeWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type CompleteWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CompleteWorkflowExecution decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



workflowExecutionFailedEventAttributes (dict) --
If the event is of type WorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

reason (string) --
The descriptive reason provided for the failure.

details (string) --
The details of the failure.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the FailWorkflowExecution decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



failWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type FailWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the FailWorkflowExecution decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



workflowExecutionTimedOutEventAttributes (dict) --
If the event is of type WorkflowExecutionTimedOut then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timeoutType (string) --
The type of timeout that caused this event.

childPolicy (string) --
The policy used for the child workflow executions of this workflow execution.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.




workflowExecutionCanceledEventAttributes (dict) --
If the event is of type WorkflowExecutionCanceled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

details (string) --
The details of the cancellation.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



cancelWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type CancelWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



workflowExecutionContinuedAsNewEventAttributes (dict) --
If the event is of type WorkflowExecutionContinuedAsNew then this member is set and provides detailed information about the event. It isn\'t set for other event types.

input (string) --
The input provided to the new workflow execution.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the ContinueAsNewWorkflowExecution decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

newExecutionRunId (string) --
The runId of the new workflow execution.

executionStartToCloseTimeout (string) --
The total duration allowed for the new workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

taskList (dict) --
The task list to use for the decisions of the new (continued) workflow execution.

name (string) --
The name of the task list.



taskPriority (string) --
The priority of the task to use for the decisions of the new (continued) workflow execution.

taskStartToCloseTimeout (string) --
The maximum duration of decision tasks for the new workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

childPolicy (string) --
The policy to use for the child workflow executions of the new execution if it is terminated by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


tagList (list) --
The list of tags associated with the new workflow execution.

(string) --


workflowType (dict) --
The workflow type of this execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




lambdaRole (string) --
The IAM role to attach to the new (continued) workflow execution.



continueAsNewWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type ContinueAsNewWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the ContinueAsNewWorkflowExecution decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



workflowExecutionTerminatedEventAttributes (dict) --
If the event is of type WorkflowExecutionTerminated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

reason (string) --
The reason provided for the termination.

details (string) --
The details provided for the termination.

childPolicy (string) --
The policy used for the child workflow executions of this workflow execution.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


cause (string) --
If set, indicates that the workflow execution was automatically terminated, and specifies the cause. This happens if the parent workflow execution times out or is terminated and the child policy is set to terminate child executions.



workflowExecutionCancelRequestedEventAttributes (dict) --
If the event is of type WorkflowExecutionCancelRequested then this member is set and provides detailed information about the event. It isn\'t set for other event types.

externalWorkflowExecution (dict) --
The external workflow execution for which the cancellation was requested.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



externalInitiatedEventId (integer) --
The ID of the RequestCancelExternalWorkflowExecutionInitiated event corresponding to the RequestCancelExternalWorkflowExecution decision to cancel this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

cause (string) --
If set, indicates that the request to cancel the workflow execution was automatically generated, and specifies the cause. This happens if the parent workflow execution times out or is terminated, and the child policy is set to cancel child executions.



decisionTaskScheduledEventAttributes (dict) --
If the event is of type DecisionTaskScheduled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

taskList (dict) --
The name of the task list in which the decision task was scheduled.

name (string) --
The name of the task list.



taskPriority (string) --
A task priority that, if set, specifies the priority for this decision task. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .

startToCloseTimeout (string) --
The maximum duration for this decision task. The task is considered timed out if it doesn\'t completed within this duration.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.



decisionTaskStartedEventAttributes (dict) --
If the event is of type DecisionTaskStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

identity (string) --
Identity of the decider making the request. This enables diagnostic tracing when problems arise. The form of this identity is user defined.

scheduledEventId (integer) --
The ID of the DecisionTaskScheduled event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



decisionTaskCompletedEventAttributes (dict) --
If the event is of type DecisionTaskCompleted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

executionContext (string) --
User defined context for the workflow execution.

scheduledEventId (integer) --
The ID of the DecisionTaskScheduled event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the DecisionTaskStarted event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



decisionTaskTimedOutEventAttributes (dict) --
If the event is of type DecisionTaskTimedOut then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timeoutType (string) --
The type of timeout that expired before the decision task could be completed.

scheduledEventId (integer) --
The ID of the DecisionTaskScheduled event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the DecisionTaskStarted event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskScheduledEventAttributes (dict) --
If the event is of type ActivityTaskScheduled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

activityType (dict) --
The type of the activity task.

name (string) --
The name of this activity.

Note
The combination of activity type name and version must be unique within a domain.


version (string) --
The version of this activity.

Note
The combination of activity type name and version must be unique with in a domain.




activityId (string) --
The unique ID of the activity task.

input (string) --
The input provided to the activity task.

control (string) --
Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn\'t sent to the activity.

scheduleToStartTimeout (string) --
The maximum amount of time the activity task can wait to be assigned to a worker.

scheduleToCloseTimeout (string) --
The maximum amount of time for this activity task.

startToCloseTimeout (string) --
The maximum amount of time a worker may take to process the activity task.

taskList (dict) --
The task list in which the activity task has been scheduled.

name (string) --
The name of the task list.



taskPriority (string) --
The priority to assign to the scheduled activity task. If set, this overrides any default priority value that was assigned when the activity type was registered.
Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

heartbeatTimeout (string) --
The maximum time before which the worker processing this task must report progress by calling  RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or return a result, it is ignored.



activityTaskStartedEventAttributes (dict) --
If the event is of type ActivityTaskStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

identity (string) --
Identity of the worker that was assigned this task. This aids diagnostics when problems arise. The form of this identity is user defined.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskCompletedEventAttributes (dict) --
If the event is of type ActivityTaskCompleted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

result (string) --
The results of the activity task.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskFailedEventAttributes (dict) --
If the event is of type ActivityTaskFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

reason (string) --
The reason provided for the failure.

details (string) --
The details of the failure.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskTimedOutEventAttributes (dict) --
If the event is of type ActivityTaskTimedOut then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timeoutType (string) --
The type of the timeout that caused this event.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

details (string) --
Contains the content of the details parameter for the last call made by the activity to RecordActivityTaskHeartbeat .



activityTaskCanceledEventAttributes (dict) --
If the event is of type ActivityTaskCanceled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

details (string) --
Details of the cancellation.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

latestCancelRequestedEventId (integer) --
If set, contains the ID of the last ActivityTaskCancelRequested event recorded for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



activityTaskCancelRequestedEventAttributes (dict) --
If the event is of type ActivityTaskcancelRequested then this member is set and provides detailed information about the event. It isn\'t set for other event types.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelActivityTask decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

activityId (string) --
The unique ID of the task.



workflowExecutionSignaledEventAttributes (dict) --
If the event is of type WorkflowExecutionSignaled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

signalName (string) --
The name of the signal received. The decider can use the signal name and inputs to determine how to the process the signal.

input (string) --
The inputs provided with the signal. The decider can use the signal name and inputs to determine how to process the signal.

externalWorkflowExecution (dict) --
The workflow execution that sent the signal. This is set only of the signal was sent by another workflow execution.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



externalInitiatedEventId (integer) --
The ID of the SignalExternalWorkflowExecutionInitiated event corresponding to the SignalExternalWorkflow decision to signal this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event. This field is set only if the signal was initiated by another workflow execution.



markerRecordedEventAttributes (dict) --
If the event is of type MarkerRecorded then this member is set and provides detailed information about the event. It isn\'t set for other event types.

markerName (string) --
The name of the marker.

details (string) --
The details of the marker.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RecordMarker decision that requested this marker. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



recordMarkerFailedEventAttributes (dict) --
If the event is of type DecisionTaskFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

markerName (string) --
The marker\'s name.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RecordMarkerFailed decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



timerStartedEventAttributes (dict) --
If the event is of type TimerStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The unique ID of the timer that was started.

control (string) --
Data attached to the event that can be used by the decider in subsequent workflow tasks.

startToFireTimeout (string) --
The duration of time after which the timer fires.
The duration is specified in seconds, an integer greater than or equal to 0 .

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartTimer decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



timerFiredEventAttributes (dict) --
If the event is of type TimerFired then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The unique ID of the timer that fired.

startedEventId (integer) --
The ID of the TimerStarted event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



timerCanceledEventAttributes (dict) --
If the event is of type TimerCanceled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The unique ID of the timer that was canceled.

startedEventId (integer) --
The ID of the TimerStarted event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelTimer decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



startChildWorkflowExecutionInitiatedEventAttributes (dict) --
If the event is of type StartChildWorkflowExecutionInitiated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the child workflow execution.

workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




control (string) --
Data attached to the event that can be used by the decider in subsequent decision tasks. This data isn\'t sent to the activity.

input (string) --
The inputs provided to the child workflow execution.

executionStartToCloseTimeout (string) --
The maximum duration for the child workflow execution. If the workflow execution isn\'t closed within this duration, it is timed out and force-terminated.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

taskList (dict) --
The name of the task list used for the decision tasks of the child workflow execution.

name (string) --
The name of the task list.



taskPriority (string) --
The priority assigned for the decision tasks for this workflow execution. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartChildWorkflowExecution   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the cause of events.

childPolicy (string) --
The policy to use for the child workflow executions if this execution gets terminated by explicitly calling the  TerminateWorkflowExecution action or due to an expired timeout.
The supported child policies are:

TERMINATE \xe2\x80\x93 The child executions are terminated.
REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.


taskStartToCloseTimeout (string) --
The maximum duration allowed for the decision tasks for this workflow execution.
The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.

tagList (list) --
The list of tags to associated with the child workflow execution.

(string) --


lambdaRole (string) --
The IAM role to attach to the child workflow execution.



childWorkflowExecutionStartedEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionStarted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that was started.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionCompletedEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionCompleted then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that was completed.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




result (string) --
The result of the child workflow execution.

initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that failed.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




reason (string) --
The reason for the failure (if provided).

details (string) --
The details of the failure (if provided).

initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionTimedOutEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionTimedOut then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that timed out.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




timeoutType (string) --
The type of the timeout that caused the child workflow execution to time out.

initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionCanceledEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionCanceled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that was canceled.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




details (string) --
Details of the cancellation (if provided).

initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



childWorkflowExecutionTerminatedEventAttributes (dict) --
If the event is of type ChildWorkflowExecutionTerminated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The child workflow execution that was terminated.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



workflowType (dict) --
The type of the child workflow execution.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




initiatedEventId (integer) --
The ID of the StartChildWorkflowExecutionInitiated event corresponding to the StartChildWorkflowExecution   Decision to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ChildWorkflowExecutionStarted event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



signalExternalWorkflowExecutionInitiatedEventAttributes (dict) --
If the event is of type SignalExternalWorkflowExecutionInitiated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the external workflow execution.

runId (string) --
The runId of the external workflow execution to send the signal to.

signalName (string) --
The name of the signal.

input (string) --
The input provided to the signal.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the SignalExternalWorkflowExecution decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control (string) --
Data attached to the event that can be used by the decider in subsequent decision tasks.



externalWorkflowExecutionSignaledEventAttributes (dict) --
If the event is of type ExternalWorkflowExecutionSignaled then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The external workflow execution that the signal was delivered to.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



initiatedEventId (integer) --
The ID of the SignalExternalWorkflowExecutionInitiated event corresponding to the SignalExternalWorkflowExecution decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



signalExternalWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type SignalExternalWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the external workflow execution that the signal was being delivered to.

runId (string) --
The runId of the external workflow execution that the signal was being delivered to.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


initiatedEventId (integer) --
The ID of the SignalExternalWorkflowExecutionInitiated event corresponding to the SignalExternalWorkflowExecution decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the SignalExternalWorkflowExecution decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control (string) --
The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the workflow execution.



externalWorkflowExecutionCancelRequestedEventAttributes (dict) --
If the event is of type ExternalWorkflowExecutionCancelRequested then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowExecution (dict) --
The external workflow execution to which the cancellation request was delivered.

workflowId (string) --
The user defined identifier associated with the workflow execution.

runId (string) --
A system-generated unique identifier for the workflow execution.



initiatedEventId (integer) --
The ID of the RequestCancelExternalWorkflowExecutionInitiated event corresponding to the RequestCancelExternalWorkflowExecution decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



requestCancelExternalWorkflowExecutionInitiatedEventAttributes (dict) --
If the event is of type RequestCancelExternalWorkflowExecutionInitiated then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the external workflow execution to be canceled.

runId (string) --
The runId of the external workflow execution to be canceled.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelExternalWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control (string) --
Data attached to the event that can be used by the decider in subsequent workflow tasks.



requestCancelExternalWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type RequestCancelExternalWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowId (string) --
The workflowId of the external workflow to which the cancel request was to be delivered.

runId (string) --
The runId of the external workflow execution.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


initiatedEventId (integer) --
The ID of the RequestCancelExternalWorkflowExecutionInitiated event corresponding to the RequestCancelExternalWorkflowExecution decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelExternalWorkflowExecution decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.

control (string) --
The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the workflow execution.



scheduleActivityTaskFailedEventAttributes (dict) --
If the event is of type ScheduleActivityTaskFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

activityType (dict) --
The activity type provided in the ScheduleActivityTask decision that failed.

name (string) --
The name of this activity.

Note
The combination of activity type name and version must be unique within a domain.


version (string) --
The version of this activity.

Note
The combination of activity type name and version must be unique with in a domain.




activityId (string) --
The activityId provided in the ScheduleActivityTask decision that failed.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



requestCancelActivityTaskFailedEventAttributes (dict) --
If the event is of type RequestCancelActivityTaskFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

activityId (string) --
The activityId provided in the RequestCancelActivityTask decision that failed.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the RequestCancelActivityTask decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



startTimerFailedEventAttributes (dict) --
If the event is of type StartTimerFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The timerId provided in the StartTimer decision that failed.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartTimer decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



cancelTimerFailedEventAttributes (dict) --
If the event is of type CancelTimerFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

timerId (string) --
The timerId provided in the CancelTimer decision that failed.

cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the CancelTimer decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.



startChildWorkflowExecutionFailedEventAttributes (dict) --
If the event is of type StartChildWorkflowExecutionFailed then this member is set and provides detailed information about the event. It isn\'t set for other event types.

workflowType (dict) --
The workflow type provided in the StartChildWorkflowExecution   Decision that failed.

name (string) --
The name of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.


version (string) --
The version of the workflow type.

Note
The combination of workflow type name and version must be unique with in a domain.




cause (string) --
The cause of the failure. This information is generated by the system and can be useful for diagnostic purposes.

Note
When cause is set to OPERATION_NOT_PERMITTED , the decision fails because it lacks sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


workflowId (string) --
The workflowId of the child workflow execution.

initiatedEventId (integer) --
When the cause is WORKFLOW_ALREADY_RUNNING , initiatedEventId is the ID of the StartChildWorkflowExecutionInitiated event that corresponds to the StartChildWorkflowExecution   Decision to start the workflow execution. You can use this information to diagnose problems by tracing back the chain of events leading up to this event.
When the cause isn\'t WORKFLOW_ALREADY_RUNNING , initiatedEventId is set to 0 because the StartChildWorkflowExecutionInitiated event doesn\'t exist.

decisionTaskCompletedEventId (integer) --
The ID of the DecisionTaskCompleted event corresponding to the decision task that resulted in the StartChildWorkflowExecution   Decision to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events.

control (string) --
The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the child workflow execution.



lambdaFunctionScheduledEventAttributes (dict) --
Provides the details of the LambdaFunctionScheduled event. It isn\'t set for other event types.

id (string) --
The unique ID of the Lambda task.

name (string) --
The name of the Lambda function.

control (string) --
Data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the Lambda task.

input (string) --
The input provided to the Lambda task.

startToCloseTimeout (string) --
The maximum amount of time a worker can take to process the Lambda task.

decisionTaskCompletedEventId (integer) --
The ID of the LambdaFunctionCompleted event corresponding to the decision that resulted in scheduling this activity task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.



lambdaFunctionStartedEventAttributes (dict) --
Provides the details of the LambdaFunctionStarted event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the LambdaFunctionScheduled event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.



lambdaFunctionCompletedEventAttributes (dict) --
Provides the details of the LambdaFunctionCompleted event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the LambdaFunctionScheduled event that was recorded when this Lambda task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the LambdaFunctionStarted event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

result (string) --
The results of the Lambda task.



lambdaFunctionFailedEventAttributes (dict) --
Provides the details of the LambdaFunctionFailed event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the LambdaFunctionScheduled event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the LambdaFunctionStarted event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

reason (string) --
The reason provided for the failure.

details (string) --
The details of the failure.



lambdaFunctionTimedOutEventAttributes (dict) --
Provides the details of the LambdaFunctionTimedOut event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the LambdaFunctionScheduled event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

startedEventId (integer) --
The ID of the ActivityTaskStarted event that was recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

timeoutType (string) --
The type of the timeout that caused this event.



scheduleLambdaFunctionFailedEventAttributes (dict) --
Provides the details of the ScheduleLambdaFunctionFailed event. It isn\'t set for other event types.

id (string) --
The ID provided in the ScheduleLambdaFunction decision that failed.

name (string) --
The name of the Lambda function.

cause (string) --
The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .


decisionTaskCompletedEventId (integer) --
The ID of the LambdaFunctionCompleted event corresponding to the decision that resulted in scheduling this Lambda task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.



startLambdaFunctionFailedEventAttributes (dict) --
Provides the details of the StartLambdaFunctionFailed event. It isn\'t set for other event types.

scheduledEventId (integer) --
The ID of the ActivityTaskScheduled event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

cause (string) --
The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.

Note
If cause is set to OPERATION_NOT_PERMITTED , the decision failed because the IAM role attached to the execution lacked sufficient permissions. For details and example IAM policies, see Lambda Tasks in the Amazon SWF Developer Guide .


message (string) --
A description that can help diagnose the cause of the fault.







nextPageToken (string) --
If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
The configured maximumPageSize determines how many results can be returned in a single call.

previousStartedEventId (integer) --
The ID of the DecisionTaskStarted event of the previous decision task of this workflow execution that was processed by the decider. This can be used to determine the events in the history new since the last decision task received by the decider.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault
SWF.Client.exceptions.LimitExceededFault


    :return: {
        'taskToken': 'string',
        'startedEventId': 123,
        'workflowExecution': {
            'workflowId': 'string',
            'runId': 'string'
        },
        'workflowType': {
            'name': 'string',
            'version': 'string'
        },
        'events': [
            {
                'eventTimestamp': datetime(2015, 1, 1),
                'eventType': 'WorkflowExecutionStarted'|'WorkflowExecutionCancelRequested'|'WorkflowExecutionCompleted'|'CompleteWorkflowExecutionFailed'|'WorkflowExecutionFailed'|'FailWorkflowExecutionFailed'|'WorkflowExecutionTimedOut'|'WorkflowExecutionCanceled'|'CancelWorkflowExecutionFailed'|'WorkflowExecutionContinuedAsNew'|'ContinueAsNewWorkflowExecutionFailed'|'WorkflowExecutionTerminated'|'DecisionTaskScheduled'|'DecisionTaskStarted'|'DecisionTaskCompleted'|'DecisionTaskTimedOut'|'ActivityTaskScheduled'|'ScheduleActivityTaskFailed'|'ActivityTaskStarted'|'ActivityTaskCompleted'|'ActivityTaskFailed'|'ActivityTaskTimedOut'|'ActivityTaskCanceled'|'ActivityTaskCancelRequested'|'RequestCancelActivityTaskFailed'|'WorkflowExecutionSignaled'|'MarkerRecorded'|'RecordMarkerFailed'|'TimerStarted'|'StartTimerFailed'|'TimerFired'|'TimerCanceled'|'CancelTimerFailed'|'StartChildWorkflowExecutionInitiated'|'StartChildWorkflowExecutionFailed'|'ChildWorkflowExecutionStarted'|'ChildWorkflowExecutionCompleted'|'ChildWorkflowExecutionFailed'|'ChildWorkflowExecutionTimedOut'|'ChildWorkflowExecutionCanceled'|'ChildWorkflowExecutionTerminated'|'SignalExternalWorkflowExecutionInitiated'|'SignalExternalWorkflowExecutionFailed'|'ExternalWorkflowExecutionSignaled'|'RequestCancelExternalWorkflowExecutionInitiated'|'RequestCancelExternalWorkflowExecutionFailed'|'ExternalWorkflowExecutionCancelRequested'|'LambdaFunctionScheduled'|'LambdaFunctionStarted'|'LambdaFunctionCompleted'|'LambdaFunctionFailed'|'LambdaFunctionTimedOut'|'ScheduleLambdaFunctionFailed'|'StartLambdaFunctionFailed',
                'eventId': 123,
                'workflowExecutionStartedEventAttributes': {
                    'input': 'string',
                    'executionStartToCloseTimeout': 'string',
                    'taskStartToCloseTimeout': 'string',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'tagList': [
                        'string',
                    ],
                    'continuedExecutionRunId': 'string',
                    'parentWorkflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'parentInitiatedEventId': 123,
                    'lambdaRole': 'string'
                },
                'workflowExecutionCompletedEventAttributes': {
                    'result': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'completeWorkflowExecutionFailedEventAttributes': {
                    'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'workflowExecutionFailedEventAttributes': {
                    'reason': 'string',
                    'details': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'failWorkflowExecutionFailedEventAttributes': {
                    'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'workflowExecutionTimedOutEventAttributes': {
                    'timeoutType': 'START_TO_CLOSE',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON'
                },
                'workflowExecutionCanceledEventAttributes': {
                    'details': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'cancelWorkflowExecutionFailedEventAttributes': {
                    'cause': 'UNHANDLED_DECISION'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'workflowExecutionContinuedAsNewEventAttributes': {
                    'input': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'newExecutionRunId': 'string',
                    'executionStartToCloseTimeout': 'string',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'taskStartToCloseTimeout': 'string',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'tagList': [
                        'string',
                    ],
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'lambdaRole': 'string'
                },
                'continueAsNewWorkflowExecutionFailedEventAttributes': {
                    'cause': 'UNHANDLED_DECISION'|'WORKFLOW_TYPE_DEPRECATED'|'WORKFLOW_TYPE_DOES_NOT_EXIST'|'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_CHILD_POLICY_UNDEFINED'|'CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'workflowExecutionTerminatedEventAttributes': {
                    'reason': 'string',
                    'details': 'string',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'cause': 'CHILD_POLICY_APPLIED'|'EVENT_LIMIT_EXCEEDED'|'OPERATOR_INITIATED'
                },
                'workflowExecutionCancelRequestedEventAttributes': {
                    'externalWorkflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'externalInitiatedEventId': 123,
                    'cause': 'CHILD_POLICY_APPLIED'
                },
                'decisionTaskScheduledEventAttributes': {
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'startToCloseTimeout': 'string'
                },
                'decisionTaskStartedEventAttributes': {
                    'identity': 'string',
                    'scheduledEventId': 123
                },
                'decisionTaskCompletedEventAttributes': {
                    'executionContext': 'string',
                    'scheduledEventId': 123,
                    'startedEventId': 123
                },
                'decisionTaskTimedOutEventAttributes': {
                    'timeoutType': 'START_TO_CLOSE',
                    'scheduledEventId': 123,
                    'startedEventId': 123
                },
                'activityTaskScheduledEventAttributes': {
                    'activityType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'activityId': 'string',
                    'input': 'string',
                    'control': 'string',
                    'scheduleToStartTimeout': 'string',
                    'scheduleToCloseTimeout': 'string',
                    'startToCloseTimeout': 'string',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'heartbeatTimeout': 'string'
                },
                'activityTaskStartedEventAttributes': {
                    'identity': 'string',
                    'scheduledEventId': 123
                },
                'activityTaskCompletedEventAttributes': {
                    'result': 'string',
                    'scheduledEventId': 123,
                    'startedEventId': 123
                },
                'activityTaskFailedEventAttributes': {
                    'reason': 'string',
                    'details': 'string',
                    'scheduledEventId': 123,
                    'startedEventId': 123
                },
                'activityTaskTimedOutEventAttributes': {
                    'timeoutType': 'START_TO_CLOSE'|'SCHEDULE_TO_START'|'SCHEDULE_TO_CLOSE'|'HEARTBEAT',
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'details': 'string'
                },
                'activityTaskCanceledEventAttributes': {
                    'details': 'string',
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'latestCancelRequestedEventId': 123
                },
                'activityTaskCancelRequestedEventAttributes': {
                    'decisionTaskCompletedEventId': 123,
                    'activityId': 'string'
                },
                'workflowExecutionSignaledEventAttributes': {
                    'signalName': 'string',
                    'input': 'string',
                    'externalWorkflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'externalInitiatedEventId': 123
                },
                'markerRecordedEventAttributes': {
                    'markerName': 'string',
                    'details': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'recordMarkerFailedEventAttributes': {
                    'markerName': 'string',
                    'cause': 'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'timerStartedEventAttributes': {
                    'timerId': 'string',
                    'control': 'string',
                    'startToFireTimeout': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'timerFiredEventAttributes': {
                    'timerId': 'string',
                    'startedEventId': 123
                },
                'timerCanceledEventAttributes': {
                    'timerId': 'string',
                    'startedEventId': 123,
                    'decisionTaskCompletedEventId': 123
                },
                'startChildWorkflowExecutionInitiatedEventAttributes': {
                    'workflowId': 'string',
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'control': 'string',
                    'input': 'string',
                    'executionStartToCloseTimeout': 'string',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'taskStartToCloseTimeout': 'string',
                    'tagList': [
                        'string',
                    ],
                    'lambdaRole': 'string'
                },
                'childWorkflowExecutionStartedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'initiatedEventId': 123
                },
                'childWorkflowExecutionCompletedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'result': 'string',
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'childWorkflowExecutionFailedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'reason': 'string',
                    'details': 'string',
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'childWorkflowExecutionTimedOutEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'timeoutType': 'START_TO_CLOSE',
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'childWorkflowExecutionCanceledEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'details': 'string',
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'childWorkflowExecutionTerminatedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'initiatedEventId': 123,
                    'startedEventId': 123
                },
                'signalExternalWorkflowExecutionInitiatedEventAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'signalName': 'string',
                    'input': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'externalWorkflowExecutionSignaledEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'initiatedEventId': 123
                },
                'signalExternalWorkflowExecutionFailedEventAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                    'initiatedEventId': 123,
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'externalWorkflowExecutionCancelRequestedEventAttributes': {
                    'workflowExecution': {
                        'workflowId': 'string',
                        'runId': 'string'
                    },
                    'initiatedEventId': 123
                },
                'requestCancelExternalWorkflowExecutionInitiatedEventAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'requestCancelExternalWorkflowExecutionFailedEventAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'cause': 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION'|'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                    'initiatedEventId': 123,
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'scheduleActivityTaskFailedEventAttributes': {
                    'activityType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'activityId': 'string',
                    'cause': 'ACTIVITY_TYPE_DEPRECATED'|'ACTIVITY_TYPE_DOES_NOT_EXIST'|'ACTIVITY_ID_ALREADY_IN_USE'|'OPEN_ACTIVITIES_LIMIT_EXCEEDED'|'ACTIVITY_CREATION_RATE_EXCEEDED'|'DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED'|'DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'requestCancelActivityTaskFailedEventAttributes': {
                    'activityId': 'string',
                    'cause': 'ACTIVITY_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'startTimerFailedEventAttributes': {
                    'timerId': 'string',
                    'cause': 'TIMER_ID_ALREADY_IN_USE'|'OPEN_TIMERS_LIMIT_EXCEEDED'|'TIMER_CREATION_RATE_EXCEEDED'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'cancelTimerFailedEventAttributes': {
                    'timerId': 'string',
                    'cause': 'TIMER_ID_UNKNOWN'|'OPERATION_NOT_PERMITTED',
                    'decisionTaskCompletedEventId': 123
                },
                'startChildWorkflowExecutionFailedEventAttributes': {
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'cause': 'WORKFLOW_TYPE_DOES_NOT_EXIST'|'WORKFLOW_TYPE_DEPRECATED'|'OPEN_CHILDREN_LIMIT_EXCEEDED'|'OPEN_WORKFLOWS_LIMIT_EXCEEDED'|'CHILD_CREATION_RATE_EXCEEDED'|'WORKFLOW_ALREADY_RUNNING'|'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_TASK_LIST_UNDEFINED'|'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED'|'DEFAULT_CHILD_POLICY_UNDEFINED'|'OPERATION_NOT_PERMITTED',
                    'workflowId': 'string',
                    'initiatedEventId': 123,
                    'decisionTaskCompletedEventId': 123,
                    'control': 'string'
                },
                'lambdaFunctionScheduledEventAttributes': {
                    'id': 'string',
                    'name': 'string',
                    'control': 'string',
                    'input': 'string',
                    'startToCloseTimeout': 'string',
                    'decisionTaskCompletedEventId': 123
                },
                'lambdaFunctionStartedEventAttributes': {
                    'scheduledEventId': 123
                },
                'lambdaFunctionCompletedEventAttributes': {
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'result': 'string'
                },
                'lambdaFunctionFailedEventAttributes': {
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'reason': 'string',
                    'details': 'string'
                },
                'lambdaFunctionTimedOutEventAttributes': {
                    'scheduledEventId': 123,
                    'startedEventId': 123,
                    'timeoutType': 'START_TO_CLOSE'
                },
                'scheduleLambdaFunctionFailedEventAttributes': {
                    'id': 'string',
                    'name': 'string',
                    'cause': 'ID_ALREADY_IN_USE'|'OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED'|'LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED'|'LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION',
                    'decisionTaskCompletedEventId': 123
                },
                'startLambdaFunctionFailedEventAttributes': {
                    'scheduledEventId': 123,
                    'cause': 'ASSUME_ROLE_FAILED',
                    'message': 'string'
                }
            },
        ],
        'nextPageToken': 'string',
        'previousStartedEventId': 123
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain containing the task lists to poll.
    
    taskList (dict) -- [REQUIRED]
    Specifies the task list to poll for decision tasks.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    identity (string) -- Identity of the decider making the request, which is recorded in the DecisionTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
    nextPageToken (string) -- If NextPageToken is returned there are more results available. The value of NextPageToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 60 seconds. Using an expired pagination token will return a 400 error: "Specified token has exceeded its maximum lifetime ".
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    Note
    The nextPageToken returned by this action cannot be used with  GetWorkflowExecutionHistory to get the next page. You must call  PollForDecisionTask again (with the nextPageToken ) to retrieve the next page of history records. Calling  PollForDecisionTask with a nextPageToken doesn\'t return a new decision task.
    
    
    maximumPageSize (integer) -- The maximum number of results that are returned per call. Use nextPageToken to obtain further pages of results.
    This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
    
    reverseOrder (boolean) -- When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimestamp of the events.
    
    """
    pass

def record_activity_task_heartbeat(taskToken=None, details=None):
    """
    Used by activity workers to report to the service that the  ActivityTask represented by the specified taskToken is still making progress. The worker can also specify details of the progress, for example percent complete, using the details parameter. This action can also be used by the worker as a mechanism to check if cancellation is being requested for the activity task. If a cancellation is being attempted for the specified task, then the boolean cancelRequested flag returned by the service is set to true .
    This action resets the taskHeartbeatTimeout clock. The taskHeartbeatTimeout is specified in  RegisterActivityType .
    This action doesn\'t in itself create an event in the workflow execution history. However, if the task times out, the workflow execution history contains a ActivityTaskTimedOut event that contains the information from the last heartbeat generated by the activity worker.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.record_activity_task_heartbeat(
        taskToken='string',
        details='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]\nThe taskToken of the ActivityTask .\n\nWarning\ntaskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.\n\n

    :type details: string
    :param details: If specified, contains details about the progress of the task.

    :rtype: dict

ReturnsResponse Syntax
{
    'cancelRequested': True|False
}


Response Structure

(dict) --
Status information about an activity task.

cancelRequested (boolean) --
Set to true if cancellation of the task is requested.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.OperationNotPermittedFault


    :return: {
        'cancelRequested': True|False
    }
    
    
    :returns: 
    taskToken (string) -- [REQUIRED]
    The taskToken of the  ActivityTask .
    
    Warning
    taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
    
    
    details (string) -- If specified, contains details about the progress of the task.
    
    """
    pass

def register_activity_type(domain=None, name=None, version=None, description=None, defaultTaskStartToCloseTimeout=None, defaultTaskHeartbeatTimeout=None, defaultTaskList=None, defaultTaskPriority=None, defaultTaskScheduleToStartTimeout=None, defaultTaskScheduleToCloseTimeout=None):
    """
    Registers a new activity type along with its configuration settings in the specified domain.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_activity_type(
        domain='string',
        name='string',
        version='string',
        description='string',
        defaultTaskStartToCloseTimeout='string',
        defaultTaskHeartbeatTimeout='string',
        defaultTaskList={
            'name': 'string'
        },
        defaultTaskPriority='string',
        defaultTaskScheduleToStartTimeout='string',
        defaultTaskScheduleToCloseTimeout='string'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain in which this activity is to be registered.\n

    :type name: string
    :param name: [REQUIRED]\nThe name of the activity type within the domain.\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .\n

    :type version: string
    :param version: [REQUIRED]\nThe version of the activity type.\n\nNote\nThe activity type consists of the name and version, the combination of which must be unique within the domain.\n\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .\n

    :type description: string
    :param description: A textual description of the activity type.

    :type defaultTaskStartToCloseTimeout: string
    :param defaultTaskStartToCloseTimeout: If set, specifies the default maximum duration that a worker can take to process tasks of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask  Decision .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n

    :type defaultTaskHeartbeatTimeout: string
    :param defaultTaskHeartbeatTimeout: If set, specifies the default maximum time before which a worker processing a task of this type must report progress by calling RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. This default can be overridden when scheduling an activity task using the ScheduleActivityTask  Decision . If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an UnknownResource fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n

    :type defaultTaskList: dict
    :param defaultTaskList: If set, specifies the default task list to use for scheduling tasks of this activity type. This default task list is used if a task list isn\'t provided when a task is scheduled through the ScheduleActivityTask  Decision .\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n

    :type defaultTaskPriority: string
    :param defaultTaskPriority: The default task priority to assign to the activity type. If not assigned, then 0 is used. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.\nFor more information about setting task priority, see Setting Task Priority in the in the *Amazon SWF Developer Guide .* .\n

    :type defaultTaskScheduleToStartTimeout: string
    :param defaultTaskScheduleToStartTimeout: If set, specifies the default maximum duration that a task of this activity type can wait before being assigned to a worker. This default can be overridden when scheduling an activity task using the ScheduleActivityTask  Decision .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n

    :type defaultTaskScheduleToCloseTimeout: string
    :param defaultTaskScheduleToCloseTimeout: If set, specifies the default maximum duration for a task of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask  Decision .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which this activity is to be registered.
    
    name (string) -- [REQUIRED]
    The name of the activity type within the domain.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .
    
    version (string) -- [REQUIRED]
    The version of the activity type.
    
    Note
    The activity type consists of the name and version, the combination of which must be unique within the domain.
    
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .
    
    description (string) -- A textual description of the activity type.
    defaultTaskStartToCloseTimeout (string) -- If set, specifies the default maximum duration that a worker can take to process tasks of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask   Decision .
    The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
    defaultTaskHeartbeatTimeout (string) -- If set, specifies the default maximum time before which a worker processing a task of this type must report progress by calling  RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. This default can be overridden when scheduling an activity task using the ScheduleActivityTask   Decision . If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an UnknownResource fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.
    The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
    defaultTaskList (dict) -- If set, specifies the default task list to use for scheduling tasks of this activity type. This default task list is used if a task list isn\'t provided when a task is scheduled through the ScheduleActivityTask   Decision .
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    defaultTaskPriority (string) -- The default task priority to assign to the activity type. If not assigned, then 0 is used. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
    For more information about setting task priority, see Setting Task Priority in the in the *Amazon SWF Developer Guide .* .
    
    defaultTaskScheduleToStartTimeout (string) -- If set, specifies the default maximum duration that a task of this activity type can wait before being assigned to a worker. This default can be overridden when scheduling an activity task using the ScheduleActivityTask   Decision .
    The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
    defaultTaskScheduleToCloseTimeout (string) -- If set, specifies the default maximum duration for a task of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask   Decision .
    The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
    
    """
    pass

def register_domain(name=None, description=None, workflowExecutionRetentionPeriodInDays=None, tags=None):
    """
    Registers a new domain.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_domain(
        name='string',
        description='string',
        workflowExecutionRetentionPeriodInDays='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nName of the domain to register. The name must be unique in the region that the domain is registered in.\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .\n

    :type description: string
    :param description: A text description of the domain.

    :type workflowExecutionRetentionPeriodInDays: string
    :param workflowExecutionRetentionPeriodInDays: [REQUIRED]\nThe duration (in days) that records and histories of workflow executions on the domain should be kept by the service. After the retention period, the workflow execution isn\'t available in the results of visibility calls.\nIf you pass the value NONE or 0 (zero), then the workflow execution history isn\'t retained. As soon as the workflow execution completes, the execution record and its history are deleted.\nThe maximum workflow execution retention period is 90 days. For more information about Amazon SWF service limits, see: Amazon SWF Service Limits in the Amazon SWF Developer Guide .\n

    :type tags: list
    :param tags: Tags to be added when registering a domain.\nTags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .\n\n(dict) --Tags are key-value pairs that can be associated with Amazon SWF state machines and activities.\nTags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .\n\nkey (string) -- [REQUIRED]The key of a tag.\n\nvalue (string) --The value of a tag.\n\n\n\n\n

    :returns: 
    name (string) -- [REQUIRED]
    Name of the domain to register. The name must be unique in the region that the domain is registered in.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .
    
    description (string) -- A text description of the domain.
    workflowExecutionRetentionPeriodInDays (string) -- [REQUIRED]
    The duration (in days) that records and histories of workflow executions on the domain should be kept by the service. After the retention period, the workflow execution isn\'t available in the results of visibility calls.
    If you pass the value NONE or 0 (zero), then the workflow execution history isn\'t retained. As soon as the workflow execution completes, the execution record and its history are deleted.
    The maximum workflow execution retention period is 90 days. For more information about Amazon SWF service limits, see: Amazon SWF Service Limits in the Amazon SWF Developer Guide .
    
    tags (list) -- Tags to be added when registering a domain.
    Tags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .
    
    (dict) --Tags are key-value pairs that can be associated with Amazon SWF state machines and activities.
    Tags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .
    
    key (string) -- [REQUIRED]The key of a tag.
    
    value (string) --The value of a tag.
    
    
    
    
    
    
    """
    pass

def register_workflow_type(domain=None, name=None, version=None, description=None, defaultTaskStartToCloseTimeout=None, defaultExecutionStartToCloseTimeout=None, defaultTaskList=None, defaultTaskPriority=None, defaultChildPolicy=None, defaultLambdaRole=None):
    """
    Registers a new workflow type and its configuration settings in the specified domain.
    The retention period for the workflow history is set by the  RegisterDomain action.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_workflow_type(
        domain='string',
        name='string',
        version='string',
        description='string',
        defaultTaskStartToCloseTimeout='string',
        defaultExecutionStartToCloseTimeout='string',
        defaultTaskList={
            'name': 'string'
        },
        defaultTaskPriority='string',
        defaultChildPolicy='TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        defaultLambdaRole='string'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain in which to register the workflow type.\n

    :type name: string
    :param name: [REQUIRED]\nThe name of the workflow type.\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .\n

    :type version: string
    :param version: [REQUIRED]\nThe version of the workflow type.\n\nNote\nThe workflow type consists of the name and version, the combination of which must be unique within the domain. To get a list of all currently registered workflow types, use the ListWorkflowTypes action.\n\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .\n

    :type description: string
    :param description: Textual description of the workflow type.

    :type defaultTaskStartToCloseTimeout: string
    :param defaultTaskStartToCloseTimeout: If set, specifies the default maximum duration of decision tasks for this workflow type. This default can be overridden when starting a workflow execution using the StartWorkflowExecution action or the StartChildWorkflowExecution  Decision .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n

    :type defaultExecutionStartToCloseTimeout: string
    :param defaultExecutionStartToCloseTimeout: If set, specifies the default maximum duration for executions of this workflow type. You can override this default when starting an execution through the StartWorkflowExecution Action or StartChildWorkflowExecution  Decision .\nThe duration is specified in seconds; an integer greater than or equal to 0. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of 'NONE' for defaultExecutionStartToCloseTimeout ; there is a one-year max limit on the time that a workflow execution can run. Exceeding this limit always causes the workflow execution to time out.\n

    :type defaultTaskList: dict
    :param defaultTaskList: If set, specifies the default task list to use for scheduling decision tasks for executions of this workflow type. This default is used only if a task list isn\'t provided when starting the execution through the StartWorkflowExecution Action or StartChildWorkflowExecution  Decision .\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n

    :type defaultTaskPriority: string
    :param defaultTaskPriority: The default task priority to assign to the workflow type. If not assigned, then 0 is used. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.\nFor more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .\n

    :type defaultChildPolicy: string
    :param defaultChildPolicy: If set, specifies the default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the StartWorkflowExecution action or the StartChildWorkflowExecution  Decision .\nThe supported child policies are:\n\nTERMINATE \xe2\x80\x93 The child executions are terminated.\nREQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.\nABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.\n\n

    :type defaultLambdaRole: string
    :param defaultLambdaRole: The default IAM role attached to this workflow type.\n\nNote\nExecutions of this workflow type need IAM roles to invoke Lambda functions. If you don\'t specify an IAM role when you start this workflow type, the default Lambda role is attached to the execution. For more information, see https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html in the Amazon SWF Developer Guide .\n\n

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which to register the workflow type.
    
    name (string) -- [REQUIRED]
    The name of the workflow type.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .
    
    version (string) -- [REQUIRED]
    The version of the workflow type.
    
    Note
    The workflow type consists of the name and version, the combination of which must be unique within the domain. To get a list of all currently registered workflow types, use the  ListWorkflowTypes action.
    
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .
    
    description (string) -- Textual description of the workflow type.
    defaultTaskStartToCloseTimeout (string) -- If set, specifies the default maximum duration of decision tasks for this workflow type. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution   Decision .
    The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
    defaultExecutionStartToCloseTimeout (string) -- If set, specifies the default maximum duration for executions of this workflow type. You can override this default when starting an execution through the  StartWorkflowExecution Action or StartChildWorkflowExecution   Decision .
    The duration is specified in seconds; an integer greater than or equal to 0. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of "NONE" for defaultExecutionStartToCloseTimeout ; there is a one-year max limit on the time that a workflow execution can run. Exceeding this limit always causes the workflow execution to time out.
    
    defaultTaskList (dict) -- If set, specifies the default task list to use for scheduling decision tasks for executions of this workflow type. This default is used only if a task list isn\'t provided when starting the execution through the  StartWorkflowExecution Action or StartChildWorkflowExecution   Decision .
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    defaultTaskPriority (string) -- The default task priority to assign to the workflow type. If not assigned, then 0 is used. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
    For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .
    
    defaultChildPolicy (string) -- If set, specifies the default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution   Decision .
    The supported child policies are:
    
    TERMINATE \xe2\x80\x93 The child executions are terminated.
    REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
    ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.
    
    
    defaultLambdaRole (string) -- The default IAM role attached to this workflow type.
    
    Note
    Executions of this workflow type need IAM roles to invoke Lambda functions. If you don\'t specify an IAM role when you start this workflow type, the default Lambda role is attached to the execution. For more information, see https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html in the Amazon SWF Developer Guide .
    
    
    
    """
    pass

def request_cancel_workflow_execution(domain=None, workflowId=None, runId=None):
    """
    Records a WorkflowExecutionCancelRequested event in the currently running workflow execution identified by the given domain, workflowId, and runId. This logically requests the cancellation of the workflow execution as a whole. It is up to the decider to take appropriate actions when it receives an execution history with this event.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.request_cancel_workflow_execution(
        domain='string',
        workflowId='string',
        runId='string'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain containing the workflow execution to cancel.\n

    :type workflowId: string
    :param workflowId: [REQUIRED]\nThe workflowId of the workflow execution to cancel.\n

    :type runId: string
    :param runId: The runId of the workflow execution to cancel.

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain containing the workflow execution to cancel.
    
    workflowId (string) -- [REQUIRED]
    The workflowId of the workflow execution to cancel.
    
    runId (string) -- The runId of the workflow execution to cancel.
    
    """
    pass

def respond_activity_task_canceled(taskToken=None, details=None):
    """
    Used by workers to tell the service that the  ActivityTask identified by the taskToken was successfully canceled. Additional details can be provided using the details argument.
    These details (if provided) appear in the ActivityTaskCanceled event added to the workflow history.
    A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to  RespondActivityTaskCompleted , RespondActivityTaskCanceled,  RespondActivityTaskFailed , or the task has timed out .
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.respond_activity_task_canceled(
        taskToken='string',
        details='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]\nThe taskToken of the ActivityTask .\n\nWarning\ntaskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.\n\n

    :type details: string
    :param details: Information about the cancellation.

    :returns: 
    taskToken (string) -- [REQUIRED]
    The taskToken of the  ActivityTask .
    
    Warning
    taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
    
    
    details (string) -- Information about the cancellation.
    
    """
    pass

def respond_activity_task_completed(taskToken=None, result=None):
    """
    Used by workers to tell the service that the  ActivityTask identified by the taskToken completed successfully with a result (if provided). The result appears in the ActivityTaskCompleted event in the workflow history.
    A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to RespondActivityTaskCompleted,  RespondActivityTaskCanceled ,  RespondActivityTaskFailed , or the task has timed out .
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.respond_activity_task_completed(
        taskToken='string',
        result='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]\nThe taskToken of the ActivityTask .\n\nWarning\ntaskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.\n\n

    :type result: string
    :param result: The result of the activity task. It is a free form string that is implementation specific.

    :returns: 
    taskToken (string) -- [REQUIRED]
    The taskToken of the  ActivityTask .
    
    Warning
    taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
    
    
    result (string) -- The result of the activity task. It is a free form string that is implementation specific.
    
    """
    pass

def respond_activity_task_failed(taskToken=None, reason=None, details=None):
    """
    Used by workers to tell the service that the  ActivityTask identified by the taskToken has failed with reason (if specified). The reason and details appear in the ActivityTaskFailed event added to the workflow history.
    A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to  RespondActivityTaskCompleted ,  RespondActivityTaskCanceled , RespondActivityTaskFailed, or the task has timed out .
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.respond_activity_task_failed(
        taskToken='string',
        reason='string',
        details='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]\nThe taskToken of the ActivityTask .\n\nWarning\ntaskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.\n\n

    :type reason: string
    :param reason: Description of the error that may assist in diagnostics.

    :type details: string
    :param details: Detailed information about the failure.

    :returns: 
    taskToken (string) -- [REQUIRED]
    The taskToken of the  ActivityTask .
    
    Warning
    taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
    
    
    reason (string) -- Description of the error that may assist in diagnostics.
    details (string) -- Detailed information about the failure.
    
    """
    pass

def respond_decision_task_completed(taskToken=None, decisions=None, executionContext=None):
    """
    Used by deciders to tell the service that the  DecisionTask identified by the taskToken has successfully completed. The decisions argument specifies the list of decisions made while processing the task.
    A DecisionTaskCompleted event is added to the workflow history. The executionContext specified is attached to the event in the workflow execution history.
    If an IAM policy grants permission to use RespondDecisionTaskCompleted , it can express permissions for the list of decisions in the decisions parameter. Each of the decisions has one or more parameters, much like a regular API call. To allow for policies to be as readable as possible, you can express permissions on decisions as if they were actual API calls, including applying conditions to some parameters. For more information, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.respond_decision_task_completed(
        taskToken='string',
        decisions=[
            {
                'decisionType': 'ScheduleActivityTask'|'RequestCancelActivityTask'|'CompleteWorkflowExecution'|'FailWorkflowExecution'|'CancelWorkflowExecution'|'ContinueAsNewWorkflowExecution'|'RecordMarker'|'StartTimer'|'CancelTimer'|'SignalExternalWorkflowExecution'|'RequestCancelExternalWorkflowExecution'|'StartChildWorkflowExecution'|'ScheduleLambdaFunction',
                'scheduleActivityTaskDecisionAttributes': {
                    'activityType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'activityId': 'string',
                    'control': 'string',
                    'input': 'string',
                    'scheduleToCloseTimeout': 'string',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'scheduleToStartTimeout': 'string',
                    'startToCloseTimeout': 'string',
                    'heartbeatTimeout': 'string'
                },
                'requestCancelActivityTaskDecisionAttributes': {
                    'activityId': 'string'
                },
                'completeWorkflowExecutionDecisionAttributes': {
                    'result': 'string'
                },
                'failWorkflowExecutionDecisionAttributes': {
                    'reason': 'string',
                    'details': 'string'
                },
                'cancelWorkflowExecutionDecisionAttributes': {
                    'details': 'string'
                },
                'continueAsNewWorkflowExecutionDecisionAttributes': {
                    'input': 'string',
                    'executionStartToCloseTimeout': 'string',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'taskStartToCloseTimeout': 'string',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'tagList': [
                        'string',
                    ],
                    'workflowTypeVersion': 'string',
                    'lambdaRole': 'string'
                },
                'recordMarkerDecisionAttributes': {
                    'markerName': 'string',
                    'details': 'string'
                },
                'startTimerDecisionAttributes': {
                    'timerId': 'string',
                    'control': 'string',
                    'startToFireTimeout': 'string'
                },
                'cancelTimerDecisionAttributes': {
                    'timerId': 'string'
                },
                'signalExternalWorkflowExecutionDecisionAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'signalName': 'string',
                    'input': 'string',
                    'control': 'string'
                },
                'requestCancelExternalWorkflowExecutionDecisionAttributes': {
                    'workflowId': 'string',
                    'runId': 'string',
                    'control': 'string'
                },
                'startChildWorkflowExecutionDecisionAttributes': {
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'workflowId': 'string',
                    'control': 'string',
                    'input': 'string',
                    'executionStartToCloseTimeout': 'string',
                    'taskList': {
                        'name': 'string'
                    },
                    'taskPriority': 'string',
                    'taskStartToCloseTimeout': 'string',
                    'childPolicy': 'TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
                    'tagList': [
                        'string',
                    ],
                    'lambdaRole': 'string'
                },
                'scheduleLambdaFunctionDecisionAttributes': {
                    'id': 'string',
                    'name': 'string',
                    'control': 'string',
                    'input': 'string',
                    'startToCloseTimeout': 'string'
                }
            },
        ],
        executionContext='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]\nThe taskToken from the DecisionTask .\n\nWarning\ntaskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.\n\n

    :type decisions: list
    :param decisions: The list of decisions (possibly empty) made by the decider while processing this decision task. See the docs for the Decision structure for details.\n\n(dict) --Specifies a decision made by the decider. A decision can be one of these types:\n\nCancelTimer \xe2\x80\x93 Cancels a previously started timer and records a TimerCanceled event in the history.\nCancelWorkflowExecution \xe2\x80\x93 Closes the workflow execution and records a WorkflowExecutionCanceled event in the history.\nCompleteWorkflowExecution \xe2\x80\x93 Closes the workflow execution and records a WorkflowExecutionCompleted event in the history .\nContinueAsNewWorkflowExecution \xe2\x80\x93 Closes the workflow execution and starts a new workflow execution of the same type using the same workflow ID and a unique run Id. A WorkflowExecutionContinuedAsNew event is recorded in the history.\nFailWorkflowExecution \xe2\x80\x93 Closes the workflow execution and records a WorkflowExecutionFailed event in the history.\nRecordMarker \xe2\x80\x93 Records a MarkerRecorded event in the history. Markers can be used for adding custom information in the history for instance to let deciders know that they don\'t need to look at the history beyond the marker event.\nRequestCancelActivityTask \xe2\x80\x93 Attempts to cancel a previously scheduled activity task. If the activity task was scheduled but has not been assigned to a worker, then it is canceled. If the activity task was already assigned to a worker, then the worker is informed that cancellation has been requested in the response to RecordActivityTaskHeartbeat .\nRequestCancelExternalWorkflowExecution \xe2\x80\x93 Requests that a request be made to cancel the specified external workflow execution and records a RequestCancelExternalWorkflowExecutionInitiated event in the history.\nScheduleActivityTask \xe2\x80\x93 Schedules an activity task.\nSignalExternalWorkflowExecution \xe2\x80\x93 Requests a signal to be delivered to the specified external workflow execution and records a SignalExternalWorkflowExecutionInitiated event in the history.\nStartChildWorkflowExecution \xe2\x80\x93 Requests that a child workflow execution be started and records a StartChildWorkflowExecutionInitiated event in the history. The child workflow execution is a separate workflow execution with its own history.\nStartTimer \xe2\x80\x93 Starts a timer for this workflow execution and records a TimerStarted event in the history. This timer fires after the specified delay and record a TimerFired event.\n\n\nAccess Control\nIf you grant permission to use RespondDecisionTaskCompleted , you can use IAM policies to express permissions for the list of decisions returned by this action as if they were members of the API. Treating decisions as a pseudo API maintains a uniform conceptual model and helps keep policies readable. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .\n\nDecision Failure\nDecisions can fail for several reasons\n\nThe ordering of decisions should follow a logical flow. Some decisions might not make sense in the current context of the workflow execution and therefore fails.\nA limit on your account was reached.\nThe decision lacks sufficient permissions.\n\nOne of the following events might be added to the history to indicate an error. The event attribute\'s cause parameter indicates the cause. If cause is set to OPERATION_NOT_PERMITTED , the decision failed because it lacked sufficient permissions. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .\n\nScheduleActivityTaskFailed \xe2\x80\x93 A ScheduleActivityTask decision failed. This could happen if the activity type specified in the decision isn\'t registered, is in a deprecated state, or the decision isn\'t properly configured.\nRequestCancelActivityTaskFailed \xe2\x80\x93 A RequestCancelActivityTask decision failed. This could happen if there is no open activity task with the specified activityId.\nStartTimerFailed \xe2\x80\x93 A StartTimer decision failed. This could happen if there is another open timer with the same timerId.\nCancelTimerFailed \xe2\x80\x93 A CancelTimer decision failed. This could happen if there is no open timer with the specified timerId.\nStartChildWorkflowExecutionFailed \xe2\x80\x93 A StartChildWorkflowExecution decision failed. This could happen if the workflow type specified isn\'t registered, is deprecated, or the decision isn\'t properly configured.\nSignalExternalWorkflowExecutionFailed \xe2\x80\x93 A SignalExternalWorkflowExecution decision failed. This could happen if the workflowID specified in the decision was incorrect.\nRequestCancelExternalWorkflowExecutionFailed \xe2\x80\x93 A RequestCancelExternalWorkflowExecution decision failed. This could happen if the workflowID specified in the decision was incorrect.\nCancelWorkflowExecutionFailed \xe2\x80\x93 A CancelWorkflowExecution decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.\nCompleteWorkflowExecutionFailed \xe2\x80\x93 A CompleteWorkflowExecution decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.\nContinueAsNewWorkflowExecutionFailed \xe2\x80\x93 A ContinueAsNewWorkflowExecution decision failed. This could happen if there is an unhandled decision task pending in the workflow execution or the ContinueAsNewWorkflowExecution decision was not configured correctly.\nFailWorkflowExecutionFailed \xe2\x80\x93 A FailWorkflowExecution decision failed. This could happen if there is an unhandled decision task pending in the workflow execution.\n\nThe preceding error events might occur due to an error in the decider logic, which might put the workflow execution in an unstable state The cause field in the event structure for the error event indicates the cause of the error.\n\nNote\n\nA workflow execution may be closed by the decider by returning one of the following decisions when completing a decision task: CompleteWorkflowExecution , FailWorkflowExecution , CancelWorkflowExecution and ContinueAsNewWorkflowExecution . An UnhandledDecision fault is returned if a workflow closing decision is specified and a signal or activity event had been added to the history while the decision task was being performed by the decider. Unlike the above situations which are logic issues, this fault is always possible because of race conditions in a distributed system. The right action here is to call RespondDecisionTaskCompleted without any decisions. This would result in another decision task with these new events included in the history. The decider should handle the new events and may decide to close the workflow execution.\nHow to Code a Decision\n\nYou code a decision by first setting the decision type field to one of the above decision values, and then set the corresponding attributes field shown below:\n\n`` ScheduleActivityTaskDecisionAttributes ``\n`` RequestCancelActivityTaskDecisionAttributes ``\n`` CompleteWorkflowExecutionDecisionAttributes ``\n`` FailWorkflowExecutionDecisionAttributes ``\n`` CancelWorkflowExecutionDecisionAttributes ``\n`` ContinueAsNewWorkflowExecutionDecisionAttributes ``\n`` RecordMarkerDecisionAttributes ``\n`` StartTimerDecisionAttributes ``\n`` CancelTimerDecisionAttributes ``\n`` SignalExternalWorkflowExecutionDecisionAttributes ``\n`` RequestCancelExternalWorkflowExecutionDecisionAttributes ``\n`` StartChildWorkflowExecutionDecisionAttributes ``\n\n\ndecisionType (string) -- [REQUIRED]Specifies the type of the decision.\n\nscheduleActivityTaskDecisionAttributes (dict) --Provides the details of the ScheduleActivityTask decision. It isn\'t set for other decision types.\n\nactivityType (dict) -- [REQUIRED]The type of the activity task to schedule.\n\nname (string) -- [REQUIRED]The name of this activity.\n\nNote\nThe combination of activity type name and version must be unique within a domain.\n\n\nversion (string) -- [REQUIRED]The version of this activity.\n\nNote\nThe combination of activity type name and version must be unique with in a domain.\n\n\n\n\nactivityId (string) -- [REQUIRED]The activityId of the activity task.\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not contain the literal string arn .\n\ncontrol (string) --Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn\'t sent to the activity.\n\ninput (string) --The input provided to the activity task.\n\nscheduleToCloseTimeout (string) --The maximum duration for this activity task.\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n\nNote\nA schedule-to-close timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default schedule-to-close timeout was specified at registration time then a fault is returned.\n\n\ntaskList (dict) --If set, specifies the name of the task list in which to schedule the activity task. If not specified, the defaultTaskList registered with the activity type is used.\n\nNote\nA task list for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default task list was specified at registration time then a fault is returned.\n\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not contain the literal string arn .\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n\ntaskPriority (string) --If set, specifies the priority with which the activity task is to be assigned to a worker. This overrides the defaultTaskPriority specified when registering the activity type using RegisterActivityType . Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.\nFor more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .\n\nscheduleToStartTimeout (string) --If set, specifies the maximum duration the activity task can wait to be assigned to a worker. This overrides the default schedule-to-start timeout specified when registering the activity type using RegisterActivityType .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n\nNote\nA schedule-to-start timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default schedule-to-start timeout was specified at registration time then a fault is returned.\n\n\nstartToCloseTimeout (string) --If set, specifies the maximum duration a worker may take to process this activity task. This overrides the default start-to-close timeout specified when registering the activity type using RegisterActivityType .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n\nNote\nA start-to-close timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default start-to-close timeout was specified at registration time then a fault is returned.\n\n\nheartbeatTimeout (string) --If set, specifies the maximum time before which a worker processing a task of this type must report progress by calling RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or returns a result, it is ignored. This overrides the default heartbeat timeout specified when registering the activity type using RegisterActivityType .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n\n\n\nrequestCancelActivityTaskDecisionAttributes (dict) --Provides the details of the RequestCancelActivityTask decision. It isn\'t set for other decision types.\n\nactivityId (string) -- [REQUIRED]The activityId of the activity task to be canceled.\n\n\n\ncompleteWorkflowExecutionDecisionAttributes (dict) --Provides the details of the CompleteWorkflowExecution decision. It isn\'t set for other decision types.\n\nresult (string) --The result of the workflow execution. The form of the result is implementation defined.\n\n\n\nfailWorkflowExecutionDecisionAttributes (dict) --Provides the details of the FailWorkflowExecution decision. It isn\'t set for other decision types.\n\nreason (string) --A descriptive reason for the failure that may help in diagnostics.\n\ndetails (string) --Details of the failure.\n\n\n\ncancelWorkflowExecutionDecisionAttributes (dict) --Provides the details of the CancelWorkflowExecution decision. It isn\'t set for other decision types.\n\ndetails (string) --Details of the cancellation.\n\n\n\ncontinueAsNewWorkflowExecutionDecisionAttributes (dict) --Provides the details of the ContinueAsNewWorkflowExecution decision. It isn\'t set for other decision types.\n\ninput (string) --The input provided to the new workflow execution.\n\nexecutionStartToCloseTimeout (string) --If set, specifies the total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n\nNote\nAn execution start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this field. If neither this field is set nor a default execution start-to-close timeout was specified at registration time then a fault is returned.\n\n\ntaskList (dict) --The task list to use for the decisions of the new (continued) workflow execution.\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n\ntaskPriority (string) --The task priority that, if set, specifies the priority for the decision tasks for this workflow execution. This overrides the defaultTaskPriority specified when registering the workflow type. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.\nFor more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .\n\ntaskStartToCloseTimeout (string) --Specifies the maximum duration of decision tasks for the new workflow execution. This parameter overrides the defaultTaskStartToCloseTimout specified when registering the workflow type using RegisterWorkflowType .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n\nNote\nA task start-to-close timeout for the new workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault is returned.\n\n\nchildPolicy (string) --If set, specifies the policy to use for the child workflow executions of the new execution if it is terminated by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using RegisterWorkflowType .\nThe supported child policies are:\n\nTERMINATE \xe2\x80\x93 The child executions are terminated.\nREQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.\nABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.\n\n\nNote\nA child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.\n\n\ntagList (list) --The list of tags to associate with the new workflow execution. A maximum of 5 tags can be specified. You can list workflow executions with a specific tag by calling ListOpenWorkflowExecutions or ListClosedWorkflowExecutions and specifying a TagFilter .\n\n(string) --\n\n\nworkflowTypeVersion (string) --The version of the workflow to start.\n\nlambdaRole (string) --The IAM role to attach to the new (continued) execution.\n\n\n\nrecordMarkerDecisionAttributes (dict) --Provides the details of the RecordMarker decision. It isn\'t set for other decision types.\n\nmarkerName (string) -- [REQUIRED]The name of the marker.\n\ndetails (string) --The details of the marker.\n\n\n\nstartTimerDecisionAttributes (dict) --Provides the details of the StartTimer decision. It isn\'t set for other decision types.\n\ntimerId (string) -- [REQUIRED]The unique ID of the timer.\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not contain the literal string arn .\n\ncontrol (string) --The data attached to the event that can be used by the decider in subsequent workflow tasks.\n\nstartToFireTimeout (string) -- [REQUIRED]The duration to wait before firing the timer.\nThe duration is specified in seconds, an integer greater than or equal to 0 .\n\n\n\ncancelTimerDecisionAttributes (dict) --Provides the details of the CancelTimer decision. It isn\'t set for other decision types.\n\ntimerId (string) -- [REQUIRED]The unique ID of the timer to cancel.\n\n\n\nsignalExternalWorkflowExecutionDecisionAttributes (dict) --Provides the details of the SignalExternalWorkflowExecution decision. It isn\'t set for other decision types.\n\nworkflowId (string) -- [REQUIRED]The workflowId of the workflow execution to be signaled.\n\nrunId (string) --The runId of the workflow execution to be signaled.\n\nsignalName (string) -- [REQUIRED]The name of the signal.The target workflow execution uses the signal name and input to process the signal.\n\ninput (string) --The input data to be provided with the signal. The target workflow execution uses the signal name and input data to process the signal.\n\ncontrol (string) --The data attached to the event that can be used by the decider in subsequent decision tasks.\n\n\n\nrequestCancelExternalWorkflowExecutionDecisionAttributes (dict) --Provides the details of the RequestCancelExternalWorkflowExecution decision. It isn\'t set for other decision types.\n\nworkflowId (string) -- [REQUIRED]The workflowId of the external workflow execution to cancel.\n\nrunId (string) --The runId of the external workflow execution to cancel.\n\ncontrol (string) --The data attached to the event that can be used by the decider in subsequent workflow tasks.\n\n\n\nstartChildWorkflowExecutionDecisionAttributes (dict) --Provides the details of the StartChildWorkflowExecution decision. It isn\'t set for other decision types.\n\nworkflowType (dict) -- [REQUIRED]The type of the workflow execution to be started.\n\nname (string) -- [REQUIRED]The name of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\nversion (string) -- [REQUIRED]The version of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\n\n\nworkflowId (string) -- [REQUIRED]The workflowId of the workflow execution.\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not contain the literal string arn .\n\ncontrol (string) --The data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn\'t sent to the child workflow execution.\n\ninput (string) --The input to be provided to the workflow execution.\n\nexecutionStartToCloseTimeout (string) --The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n\nNote\nAn execution start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default execution start-to-close timeout was specified at registration time then a fault is returned.\n\n\ntaskList (dict) --The name of the task list to be used for decision tasks of the child workflow execution.\n\nNote\nA task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault is returned.\n\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not contain the literal string arn .\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n\ntaskPriority (string) --A task priority that, if set, specifies the priority for a decision task of this workflow execution. This overrides the defaultTaskPriority specified when registering the workflow type. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.\nFor more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .\n\ntaskStartToCloseTimeout (string) --Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the defaultTaskStartToCloseTimout specified when registering the workflow type using RegisterWorkflowType .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n\nNote\nA task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault is returned.\n\n\nchildPolicy (string) --If set, specifies the policy to use for the child workflow executions if the workflow execution being started is terminated by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using RegisterWorkflowType .\nThe supported child policies are:\n\nTERMINATE \xe2\x80\x93 The child executions are terminated.\nREQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.\nABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.\n\n\nNote\nA child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.\n\n\ntagList (list) --The list of tags to associate with the child workflow execution. A maximum of 5 tags can be specified. You can list workflow executions with a specific tag by calling ListOpenWorkflowExecutions or ListClosedWorkflowExecutions and specifying a TagFilter .\n\n(string) --\n\n\nlambdaRole (string) --The IAM role attached to the child workflow execution.\n\n\n\nscheduleLambdaFunctionDecisionAttributes (dict) --Provides the details of the ScheduleLambdaFunction decision. It isn\'t set for other decision types.\n\nid (string) -- [REQUIRED]A string that identifies the Lambda function execution in the event history.\n\nname (string) -- [REQUIRED]The name, or ARN, of the Lambda function to schedule.\n\ncontrol (string) --The data attached to the event that the decider can use in subsequent workflow tasks. This data isn\'t sent to the Lambda task.\n\ninput (string) --The optional input data to be supplied to the Lambda function.\n\nstartToCloseTimeout (string) --The timeout value, in seconds, after which the Lambda function is considered to be failed once it has started. This can be any integer from 1-300 (1s-5m). If no value is supplied, than a default value of 300s is assumed.\n\n\n\n\n\n\n

    :type executionContext: string
    :param executionContext: User defined context to add to workflow execution.

    :returns: 
    SWF.Client.exceptions.UnknownResourceFault
    SWF.Client.exceptions.OperationNotPermittedFault
    
    """
    pass

def signal_workflow_execution(domain=None, workflowId=None, runId=None, signalName=None, input=None):
    """
    Records a WorkflowExecutionSignaled event in the workflow execution history and creates a decision task for the workflow execution identified by the given domain, workflowId and runId. The event is recorded with the specified user defined signalName and input (if provided).
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.signal_workflow_execution(
        domain='string',
        workflowId='string',
        runId='string',
        signalName='string',
        input='string'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain containing the workflow execution to signal.\n

    :type workflowId: string
    :param workflowId: [REQUIRED]\nThe workflowId of the workflow execution to signal.\n

    :type runId: string
    :param runId: The runId of the workflow execution to signal.

    :type signalName: string
    :param signalName: [REQUIRED]\nThe name of the signal. This name must be meaningful to the target workflow.\n

    :type input: string
    :param input: Data to attach to the WorkflowExecutionSignaled event in the target workflow execution\'s history.

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain containing the workflow execution to signal.
    
    workflowId (string) -- [REQUIRED]
    The workflowId of the workflow execution to signal.
    
    runId (string) -- The runId of the workflow execution to signal.
    signalName (string) -- [REQUIRED]
    The name of the signal. This name must be meaningful to the target workflow.
    
    input (string) -- Data to attach to the WorkflowExecutionSignaled event in the target workflow execution\'s history.
    
    """
    pass

def start_workflow_execution(domain=None, workflowId=None, workflowType=None, taskList=None, taskPriority=None, input=None, executionStartToCloseTimeout=None, tagList=None, taskStartToCloseTimeout=None, childPolicy=None, lambdaRole=None):
    """
    Starts an execution of the workflow type in the specified domain using the provided workflowId and input data.
    This action returns the newly started workflow execution.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_workflow_execution(
        domain='string',
        workflowId='string',
        workflowType={
            'name': 'string',
            'version': 'string'
        },
        taskList={
            'name': 'string'
        },
        taskPriority='string',
        input='string',
        executionStartToCloseTimeout='string',
        tagList=[
            'string',
        ],
        taskStartToCloseTimeout='string',
        childPolicy='TERMINATE'|'REQUEST_CANCEL'|'ABANDON',
        lambdaRole='string'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain in which the workflow execution is created.\n

    :type workflowId: string
    :param workflowId: [REQUIRED]\nThe user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a restart of a previous execution. You cannot have two open workflow executions with the same workflowId at the same time within the same domain.\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .\n

    :type workflowType: dict
    :param workflowType: [REQUIRED]\nThe type of the workflow to start.\n\nname (string) -- [REQUIRED]The name of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\nversion (string) -- [REQUIRED]The version of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\n\n

    :type taskList: dict
    :param taskList: The task list to use for the decision tasks generated for this workflow execution. This overrides the defaultTaskList specified when registering the workflow type.\n\nNote\nA task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault is returned.\n\nThe specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .\n\nname (string) -- [REQUIRED]The name of the task list.\n\n\n

    :type taskPriority: string
    :param taskPriority: The task priority to use for this workflow execution. This overrides any default priority that was assigned when the workflow type was registered. If not set, then the default task priority for the workflow type is used. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.\nFor more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .\n

    :type input: string
    :param input: The input for the workflow execution. This is a free form string which should be meaningful to the workflow you are starting. This input is made available to the new workflow execution in the WorkflowExecutionStarted history event.

    :type executionStartToCloseTimeout: string
    :param executionStartToCloseTimeout: The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.\nThe duration is specified in seconds; an integer greater than or equal to 0 . Exceeding this limit causes the workflow execution to time out. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of 'NONE' for this timeout; there is a one-year max limit on the time that a workflow execution can run.\n\nNote\nAn execution start-to-close timeout must be specified either through this parameter or as a default when the workflow type is registered. If neither this parameter nor a default execution start-to-close timeout is specified, a fault is returned.\n\n

    :type tagList: list
    :param tagList: The list of tags to associate with the workflow execution. You can specify a maximum of 5 tags. You can list workflow executions with a specific tag by calling ListOpenWorkflowExecutions or ListClosedWorkflowExecutions and specifying a TagFilter .\n\n(string) --\n\n

    :type taskStartToCloseTimeout: string
    :param taskStartToCloseTimeout: Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the defaultTaskStartToCloseTimout specified when registering the workflow type using RegisterWorkflowType .\nThe duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.\n\nNote\nA task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault is returned.\n\n

    :type childPolicy: string
    :param childPolicy: If set, specifies the policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using RegisterWorkflowType .\nThe supported child policies are:\n\nTERMINATE \xe2\x80\x93 The child executions are terminated.\nREQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.\nABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.\n\n\nNote\nA child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.\n\n

    :type lambdaRole: string
    :param lambdaRole: The IAM role to attach to this workflow execution.\n\nNote\nExecutions of this workflow type need IAM roles to invoke Lambda functions. If you don\'t attach an IAM role, any attempt to schedule a Lambda task fails. This results in a ScheduleLambdaFunctionFailed history event. For more information, see https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html in the Amazon SWF Developer Guide .\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'runId': 'string'
}


Response Structure

(dict) --
Specifies the runId of a workflow execution.

runId (string) --
The runId of a workflow execution. This ID is generated by the service and can be used to uniquely identify the workflow execution within a domain.







Exceptions

SWF.Client.exceptions.UnknownResourceFault
SWF.Client.exceptions.TypeDeprecatedFault
SWF.Client.exceptions.WorkflowExecutionAlreadyStartedFault
SWF.Client.exceptions.LimitExceededFault
SWF.Client.exceptions.OperationNotPermittedFault
SWF.Client.exceptions.DefaultUndefinedFault


    :return: {
        'runId': 'string'
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which the workflow execution is created.
    
    workflowId (string) -- [REQUIRED]
    The user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a restart of a previous execution. You cannot have two open workflow executions with the same workflowId at the same time within the same domain.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .
    
    workflowType (dict) -- [REQUIRED]
    The type of the workflow to start.
    
    name (string) -- [REQUIRED]The name of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    version (string) -- [REQUIRED]The version of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    
    
    taskList (dict) -- The task list to use for the decision tasks generated for this workflow execution. This overrides the defaultTaskList specified when registering the workflow type.
    
    Note
    A task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault is returned.
    
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\\u0000-\\u001f | \\u007f-\\u009f ). Also, it must not be the literal string arn .
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    taskPriority (string) -- The task priority to use for this workflow execution. This overrides any default priority that was assigned when the workflow type was registered. If not set, then the default task priority for the workflow type is used. Valid values are integers that range from Java\'s Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
    For more information about setting task priority, see Setting Task Priority in the Amazon SWF Developer Guide .
    
    input (string) -- The input for the workflow execution. This is a free form string which should be meaningful to the workflow you are starting. This input is made available to the new workflow execution in the WorkflowExecutionStarted history event.
    executionStartToCloseTimeout (string) -- The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.
    The duration is specified in seconds; an integer greater than or equal to 0 . Exceeding this limit causes the workflow execution to time out. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of "NONE" for this timeout; there is a one-year max limit on the time that a workflow execution can run.
    
    Note
    An execution start-to-close timeout must be specified either through this parameter or as a default when the workflow type is registered. If neither this parameter nor a default execution start-to-close timeout is specified, a fault is returned.
    
    
    tagList (list) -- The list of tags to associate with the workflow execution. You can specify a maximum of 5 tags. You can list workflow executions with a specific tag by calling  ListOpenWorkflowExecutions or  ListClosedWorkflowExecutions and specifying a  TagFilter .
    
    (string) --
    
    
    taskStartToCloseTimeout (string) -- Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the defaultTaskStartToCloseTimout specified when registering the workflow type using  RegisterWorkflowType .
    The duration is specified in seconds, an integer greater than or equal to 0 . You can use NONE to specify unlimited duration.
    
    Note
    A task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault is returned.
    
    
    childPolicy (string) -- If set, specifies the policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using  RegisterWorkflowType .
    The supported child policies are:
    
    TERMINATE \xe2\x80\x93 The child executions are terminated.
    REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
    ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.
    
    
    Note
    A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.
    
    
    lambdaRole (string) -- The IAM role to attach to this workflow execution.
    
    Note
    Executions of this workflow type need IAM roles to invoke Lambda functions. If you don\'t attach an IAM role, any attempt to schedule a Lambda task fails. This results in a ScheduleLambdaFunctionFailed history event. For more information, see https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html in the Amazon SWF Developer Guide .
    
    
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Add a tag to a Amazon SWF domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the Amazon SWF domain.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe list of tags to add to a domain.\nTags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .\n\n(dict) --Tags are key-value pairs that can be associated with Amazon SWF state machines and activities.\nTags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .\n\nkey (string) -- [REQUIRED]The key of a tag.\n\nvalue (string) --The value of a tag.\n\n\n\n\n

    :returns: 
    SWF.Client.exceptions.UnknownResourceFault
    SWF.Client.exceptions.TooManyTagsFault
    SWF.Client.exceptions.LimitExceededFault
    SWF.Client.exceptions.OperationNotPermittedFault
    
    """
    pass

def terminate_workflow_execution(domain=None, workflowId=None, runId=None, reason=None, details=None, childPolicy=None):
    """
    Records a WorkflowExecutionTerminated event and forces closure of the workflow execution identified by the given domain, runId, and workflowId. The child policy, registered with the workflow type or specified when starting this execution, is applied to any open child workflow executions of this workflow execution.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.terminate_workflow_execution(
        domain='string',
        workflowId='string',
        runId='string',
        reason='string',
        details='string',
        childPolicy='TERMINATE'|'REQUEST_CANCEL'|'ABANDON'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe domain of the workflow execution to terminate.\n

    :type workflowId: string
    :param workflowId: [REQUIRED]\nThe workflowId of the workflow execution to terminate.\n

    :type runId: string
    :param runId: The runId of the workflow execution to terminate.

    :type reason: string
    :param reason: A descriptive reason for terminating the workflow execution.

    :type details: string
    :param details: Details for terminating the workflow execution.

    :type childPolicy: string
    :param childPolicy: If set, specifies the policy to use for the child workflow executions of the workflow execution being terminated. This policy overrides the child policy specified for the workflow execution at registration time or when starting the execution.\nThe supported child policies are:\n\nTERMINATE \xe2\x80\x93 The child executions are terminated.\nREQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.\nABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.\n\n\nNote\nA child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.\n\n

    :returns: 
    domain (string) -- [REQUIRED]
    The domain of the workflow execution to terminate.
    
    workflowId (string) -- [REQUIRED]
    The workflowId of the workflow execution to terminate.
    
    runId (string) -- The runId of the workflow execution to terminate.
    reason (string) -- A descriptive reason for terminating the workflow execution.
    details (string) -- Details for terminating the workflow execution.
    childPolicy (string) -- If set, specifies the policy to use for the child workflow executions of the workflow execution being terminated. This policy overrides the child policy specified for the workflow execution at registration time or when starting the execution.
    The supported child policies are:
    
    TERMINATE \xe2\x80\x93 The child executions are terminated.
    REQUEST_CANCEL \xe2\x80\x93 A request to cancel is attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
    ABANDON \xe2\x80\x93 No action is taken. The child executions continue to run.
    
    
    Note
    A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.
    
    
    
    """
    pass

def undeprecate_activity_type(domain=None, activityType=None):
    """
    Undeprecates a previously deprecated activity type . After an activity type has been undeprecated, you can create new tasks of that activity type.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.undeprecate_activity_type(
        domain='string',
        activityType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain of the deprecated activity type.\n

    :type activityType: dict
    :param activityType: [REQUIRED]\nThe activity type to undeprecate.\n\nname (string) -- [REQUIRED]The name of this activity.\n\nNote\nThe combination of activity type name and version must be unique within a domain.\n\n\nversion (string) -- [REQUIRED]The version of this activity.\n\nNote\nThe combination of activity type name and version must be unique with in a domain.\n\n\n\n

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain of the deprecated activity type.
    
    activityType (dict) -- [REQUIRED]
    The activity type to undeprecate.
    
    name (string) -- [REQUIRED]The name of this activity.
    
    Note
    The combination of activity type name and version must be unique within a domain.
    
    
    version (string) -- [REQUIRED]The version of this activity.
    
    Note
    The combination of activity type name and version must be unique with in a domain.
    
    
    
    
    
    """
    pass

def undeprecate_domain(name=None):
    """
    Undeprecates a previously deprecated domain. After a domain has been undeprecated it can be used to create new workflow executions or register new types.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.undeprecate_domain(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the domain of the deprecated workflow type.\n

    :returns: 
    SWF.Client.exceptions.UnknownResourceFault
    SWF.Client.exceptions.DomainAlreadyExistsFault
    SWF.Client.exceptions.OperationNotPermittedFault
    
    """
    pass

def undeprecate_workflow_type(domain=None, workflowType=None):
    """
    Undeprecates a previously deprecated workflow type . After a workflow type has been undeprecated, you can create new executions of that type.
    You can use IAM policies to control this action\'s access to Amazon SWF resources as follows:
    If the caller doesn\'t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute\'s cause parameter is set to OPERATION_NOT_PERMITTED . For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows in the Amazon SWF Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.undeprecate_workflow_type(
        domain='string',
        workflowType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]\nThe name of the domain of the deprecated workflow type.\n

    :type workflowType: dict
    :param workflowType: [REQUIRED]\nThe name of the domain of the deprecated workflow type.\n\nname (string) -- [REQUIRED]The name of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\nversion (string) -- [REQUIRED]The version of the workflow type.\n\nNote\nThe combination of workflow type name and version must be unique with in a domain.\n\n\n\n

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain of the deprecated workflow type.
    
    workflowType (dict) -- [REQUIRED]
    The name of the domain of the deprecated workflow type.
    
    name (string) -- [REQUIRED]The name of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    version (string) -- [REQUIRED]The version of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    
    
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Remove a tag from a Amazon SWF domain.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the Amazon SWF domain.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe list of tags to remove from the Amazon SWF domain.\n\n(string) --\n\n

    :returns: 
    SWF.Client.exceptions.UnknownResourceFault
    SWF.Client.exceptions.LimitExceededFault
    SWF.Client.exceptions.OperationNotPermittedFault
    
    """
    pass

