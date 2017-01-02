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

def count_closed_workflow_executions(domain=None, startTimeFilter=None, closeTimeFilter=None, executionFilter=None, typeFilter=None, tagFilter=None, closeStatusFilter=None):
    """
    Returns the number of closed workflow executions within the given domain that meet the specified filtering criteria.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
    :param domain: [REQUIRED]
            The name of the domain containing the workflow executions to count.
            

    :type startTimeFilter: dict
    :param startTimeFilter: If specified, only workflow executions that meet the start time criteria of the filter are counted.
            Note
            startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            

    :type closeTimeFilter: dict
    :param closeTimeFilter: If specified, only workflow executions that meet the close time criteria of the filter are counted.
            Note
            startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            

    :type executionFilter: dict
    :param executionFilter: If specified, only workflow executions matching the WorkflowId in the filter are counted.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
            

    :type typeFilter: dict
    :param typeFilter: If specified, indicates the type of the workflow executions to be counted.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            name (string) -- [REQUIRED]Required. Name of the workflow type.
            version (string) --Version of the workflow type.
            

    :type tagFilter: dict
    :param tagFilter: If specified, only executions that have a tag that matches the filter are counted.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
            

    :type closeStatusFilter: dict
    :param closeStatusFilter: If specified, only workflow executions that match this close status are counted. This filter has an affect only if executionStatus is specified as CLOSED .
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            status (string) -- [REQUIRED]Required. The close status that must match the close status of an execution for it to meet the criteria of this filter.
            

    :rtype: dict
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
    
    
    name (string) -- [REQUIRED]Required. Name of the workflow type.
    
    version (string) --Version of the workflow type.
    
    
    
    tagFilter (dict) -- If specified, only executions that have a tag that matches the filter are counted.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
    
    
    
    closeStatusFilter (dict) -- If specified, only workflow executions that match this close status are counted. This filter has an affect only if executionStatus is specified as CLOSED .
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    status (string) -- [REQUIRED]Required. The close status that must match the close status of an execution for it to meet the criteria of this filter.
    
    
    
    
    """
    pass

def count_open_workflow_executions(domain=None, startTimeFilter=None, typeFilter=None, tagFilter=None, executionFilter=None):
    """
    Returns the number of open workflow executions within the given domain that meet the specified filtering criteria.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
    :param domain: [REQUIRED]
            The name of the domain containing the workflow executions to count.
            

    :type startTimeFilter: dict
    :param startTimeFilter: [REQUIRED]
            Specifies the start time criteria that workflow executions must meet in order to be counted.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            

    :type typeFilter: dict
    :param typeFilter: Specifies the type of the workflow executions to be counted.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            name (string) -- [REQUIRED]Required. Name of the workflow type.
            version (string) --Version of the workflow type.
            

    :type tagFilter: dict
    :param tagFilter: If specified, only executions that have a tag that matches the filter are counted.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
            

    :type executionFilter: dict
    :param executionFilter: If specified, only workflow executions matching the WorkflowId in the filter are counted.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
            

    :rtype: dict
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
    
    
    name (string) -- [REQUIRED]Required. Name of the workflow type.
    
    version (string) --Version of the workflow type.
    
    
    
    tagFilter (dict) -- If specified, only executions that have a tag that matches the filter are counted.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
    
    
    
    executionFilter (dict) -- If specified, only workflow executions matching the WorkflowId in the filter are counted.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
    
    
    
    
    """
    pass

def count_pending_activity_tasks(domain=None, taskList=None):
    """
    Returns the estimated number of activity tasks in the specified task list. The count returned is an approximation and is not guaranteed to be exact. If you specify a task list that no activity task was ever scheduled in then 0 will be returned.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.count_pending_activity_tasks(
        domain='string',
        taskList={
            'name': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain that contains the task list.
            

    :type taskList: dict
    :param taskList: [REQUIRED]
            The name of the task list.
            name (string) -- [REQUIRED]The name of the task list.
            

    :rtype: dict
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
    Returns the estimated number of decision tasks in the specified task list. The count returned is an approximation and is not guaranteed to be exact. If you specify a task list that no decision task was ever scheduled in then 0 will be returned.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.count_pending_decision_tasks(
        domain='string',
        taskList={
            'name': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain that contains the task list.
            

    :type taskList: dict
    :param taskList: [REQUIRED]
            The name of the task list.
            name (string) -- [REQUIRED]The name of the task list.
            

    :rtype: dict
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
    Deprecates the specified activity type . After an activity type has been deprecated, you cannot create new tasks of that activity type. Tasks of this type that were scheduled before the type was deprecated will continue to run.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.deprecate_activity_type(
        domain='string',
        activityType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain in which the activity type is registered.
            

    :type activityType: dict
    :param activityType: [REQUIRED]
            The activity type to deprecate.
            name (string) -- [REQUIRED]The name of this activity.
            Note
            The combination of activity type name and version must be unique within a domain.
            version (string) -- [REQUIRED]The version of this activity.
            Note
            The combination of activity type name and version must be unique with in a domain.
            

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
    Deprecates the specified domain. After a domain has been deprecated it cannot be used to create new workflow executions or register new types. However, you can still use visibility actions on this domain. Deprecating a domain also deprecates all activity and workflow types registered in the domain. Executions that were started before the domain was deprecated will continue to run.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.deprecate_domain(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the domain to deprecate.
            

    """
    pass

def deprecate_workflow_type(domain=None, workflowType=None):
    """
    Deprecates the specified workflow type . After a workflow type has been deprecated, you cannot create new executions of that type. Executions that were started before the type was deprecated will continue to run. A deprecated workflow type may still be used when calling visibility actions.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.deprecate_workflow_type(
        domain='string',
        workflowType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain in which the workflow type is registered.
            

    :type workflowType: dict
    :param workflowType: [REQUIRED]
            The workflow type to deprecate.
            name (string) -- [REQUIRED]Required. The name of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            version (string) -- [REQUIRED]Required. The version of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which the workflow type is registered.
    
    workflowType (dict) -- [REQUIRED]
    The workflow type to deprecate.
    
    name (string) -- [REQUIRED]Required. The name of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    version (string) -- [REQUIRED]Required. The version of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    
    
    
    """
    pass

def describe_activity_type(domain=None, activityType=None):
    """
    Returns information about the specified activity type. This includes configuration settings provided when the type was registered and other general information about the type.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_activity_type(
        domain='string',
        activityType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain in which the activity type is registered.
            

    :type activityType: dict
    :param activityType: [REQUIRED]
            The activity type to get information about. Activity types are identified by the name and version that were supplied when the activity was registered.
            name (string) -- [REQUIRED]The name of this activity.
            Note
            The combination of activity type name and version must be unique within a domain.
            version (string) -- [REQUIRED]The version of this activity.
            Note
            The combination of activity type name and version must be unique with in a domain.
            

    :rtype: dict
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
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_domain(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the domain to describe.
            

    :rtype: dict
    :return: {
        'domainInfo': {
            'name': 'string',
            'status': 'REGISTERED'|'DEPRECATED',
            'description': 'string'
        },
        'configuration': {
            'workflowExecutionRetentionPeriodInDays': 'string'
        }
    }
    
    
    :returns: 
    REGISTERED : The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions.
    DEPRECATED : The domain was deprecated using  DeprecateDomain , but is still in use. You should not create new workflow executions in this domain.
    
    """
    pass

def describe_workflow_execution(domain=None, execution=None):
    """
    Returns information about the specified workflow execution including its type and some statistics.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workflow_execution(
        domain='string',
        execution={
            'workflowId': 'string',
            'runId': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain containing the workflow execution.
            

    :type execution: dict
    :param execution: [REQUIRED]
            The workflow execution to describe.
            workflowId (string) -- [REQUIRED]The user defined identifier associated with the workflow execution.
            runId (string) -- [REQUIRED]A system-generated unique identifier for the workflow execution.
            

    :rtype: dict
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
    Returns information about the specified workflow type . This includes configuration settings specified when the type was registered and other information such as creation date, current status, and so on.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_workflow_type(
        domain='string',
        workflowType={
            'name': 'string',
            'version': 'string'
        }
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain in which this workflow type is registered.
            

    :type workflowType: dict
    :param workflowType: [REQUIRED]
            The workflow type to describe.
            name (string) -- [REQUIRED]Required. The name of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            version (string) -- [REQUIRED]Required. The version of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            

    :rtype: dict
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
    
    name (string) -- [REQUIRED]Required. The name of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    version (string) -- [REQUIRED]Required. The version of the workflow type.
    
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

def get_workflow_execution_history(domain=None, execution=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns the history of the specified workflow execution. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
    :param domain: [REQUIRED]
            The name of the domain containing the workflow execution.
            

    :type execution: dict
    :param execution: [REQUIRED]
            Specifies the workflow execution for which to return the history.
            workflowId (string) -- [REQUIRED]The user defined identifier associated with the workflow execution.
            runId (string) -- [REQUIRED]A system-generated unique identifier for the workflow execution.
            

    :type nextPageToken: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimeStamp of the events.

    :rtype: dict
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
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'tagList': [
                        'string',
                    ],
                    'taskPriority': 'string',
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
    
    
    
    nextPageToken (string) -- If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
    This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
    
    reverseOrder (boolean) -- When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimeStamp of the events.
    
    """
    pass

def list_activity_types(domain=None, name=None, registrationStatus=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns information about all activities registered in the specified domain that match the specified name and registration status. The result includes information like creation date, current status of the activity, etc. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.list_activity_types(
        domain='string',
        name='string',
        registrationStatus='REGISTERED'|'DEPRECATED',
        nextPageToken='string',
        maximumPageSize=123,
        reverseOrder=True|False
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain in which the activity types have been registered.
            

    :type name: string
    :param name: If specified, only lists the activity types that have this name.

    :type registrationStatus: string
    :param registrationStatus: [REQUIRED]
            Specifies the registration status of the activity types to list.
            

    :type nextPageToken: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the activity types.

    :rtype: dict
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
    
    nextPageToken (string) -- If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
    This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
    
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the activity types.
    
    """
    pass

def list_closed_workflow_executions(domain=None, startTimeFilter=None, closeTimeFilter=None, executionFilter=None, closeStatusFilter=None, typeFilter=None, tagFilter=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns a list of closed workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
    :param domain: [REQUIRED]
            The name of the domain that contains the workflow executions to list.
            

    :type startTimeFilter: dict
    :param startTimeFilter: If specified, the workflow executions are included in the returned results based on whether their start times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their start times.
            Note
            startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            

    :type closeTimeFilter: dict
    :param closeTimeFilter: If specified, the workflow executions are included in the returned results based on whether their close times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their close times.
            Note
            startTimeFilter and closeTimeFilter are mutually exclusive. You must specify one of these in a request but not both.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            

    :type executionFilter: dict
    :param executionFilter: If specified, only workflow executions matching the workflow ID specified in the filter are returned.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
            

    :type closeStatusFilter: dict
    :param closeStatusFilter: If specified, only workflow executions that match this close status are listed. For example, if TERMINATED is specified, then only TERMINATED workflow executions are listed.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            status (string) -- [REQUIRED]Required. The close status that must match the close status of an execution for it to meet the criteria of this filter.
            

    :type typeFilter: dict
    :param typeFilter: If specified, only executions of the type specified in the filter are returned.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            name (string) -- [REQUIRED]Required. Name of the workflow type.
            version (string) --Version of the workflow type.
            

    :type tagFilter: dict
    :param tagFilter: If specified, only executions that have the matching tag are listed.
            Note
            closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
            

    :type nextPageToken: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.

    :rtype: dict
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
    
    
    status (string) -- [REQUIRED]Required. The close status that must match the close status of an execution for it to meet the criteria of this filter.
    
    
    
    typeFilter (dict) -- If specified, only executions of the type specified in the filter are returned.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    name (string) -- [REQUIRED]Required. Name of the workflow type.
    
    version (string) --Version of the workflow type.
    
    
    
    tagFilter (dict) -- If specified, only executions that have the matching tag are listed.
    
    Note
    closeStatusFilter , executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
    
    
    
    nextPageToken (string) -- If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
    This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
    
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.
    
    """
    pass

def list_domains(nextPageToken=None, registrationStatus=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns the list of domains registered in the account. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.list_domains(
        nextPageToken='string',
        registrationStatus='REGISTERED'|'DEPRECATED',
        maximumPageSize=123,
        reverseOrder=True|False
    )
    
    
    :type nextPageToken: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            

    :type registrationStatus: string
    :param registrationStatus: [REQUIRED]
            Specifies the registration status of the domains to list.
            

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the domains.

    :rtype: dict
    :return: {
        'domainInfos': [
            {
                'name': 'string',
                'status': 'REGISTERED'|'DEPRECATED',
                'description': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    nextPageToken (string) -- If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    registrationStatus (string) -- [REQUIRED]
    Specifies the registration status of the domains to list.
    
    maximumPageSize (integer) -- The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
    This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
    
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default, the results are returned in ascending alphabetical order by name of the domains.
    
    """
    pass

def list_open_workflow_executions(domain=None, startTimeFilter=None, typeFilter=None, tagFilter=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None, executionFilter=None):
    """
    Returns a list of open workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
    :param domain: [REQUIRED]
            The name of the domain that contains the workflow executions to list.
            

    :type startTimeFilter: dict
    :param startTimeFilter: [REQUIRED]
            Workflow executions are included in the returned results based on whether their start times are within the range specified by this filter.
            oldestDate (datetime) -- [REQUIRED]Specifies the oldest start or close date and time to return.
            latestDate (datetime) --Specifies the latest start or close date and time to return.
            

    :type typeFilter: dict
    :param typeFilter: If specified, only executions of the type specified in the filter are returned.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            name (string) -- [REQUIRED]Required. Name of the workflow type.
            version (string) --Version of the workflow type.
            

    :type tagFilter: dict
    :param tagFilter: If specified, only executions that have the matching tag are listed.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
            

    :type nextPageToken: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default the results are returned in descending order of the start time of the executions.

    :type executionFilter: dict
    :param executionFilter: If specified, only workflow executions matching the workflow ID specified in the filter are returned.
            Note
            executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
            workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
            

    :rtype: dict
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
    
    
    name (string) -- [REQUIRED]Required. Name of the workflow type.
    
    version (string) --Version of the workflow type.
    
    
    
    tagFilter (dict) -- If specified, only executions that have the matching tag are listed.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    tag (string) -- [REQUIRED]Required. Specifies the tag that must be associated with the execution for it to meet the filter criteria.
    
    
    
    nextPageToken (string) -- If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
    This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
    
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default the results are returned in descending order of the start time of the executions.
    executionFilter (dict) -- If specified, only workflow executions matching the workflow ID specified in the filter are returned.
    
    Note
    executionFilter , typeFilter and tagFilter are mutually exclusive. You can specify at most one of these in a request.
    
    
    workflowId (string) -- [REQUIRED]The workflowId to pass of match the criteria of this filter.
    
    
    
    
    """
    pass

def list_workflow_types(domain=None, name=None, registrationStatus=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Returns information about workflow types in the specified domain. The results may be split into multiple pages that can be retrieved by making the call repeatedly.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.list_workflow_types(
        domain='string',
        name='string',
        registrationStatus='REGISTERED'|'DEPRECATED',
        nextPageToken='string',
        maximumPageSize=123,
        reverseOrder=True|False
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain in which the workflow types have been registered.
            

    :type name: string
    :param name: If specified, lists the workflow type with this name.

    :type registrationStatus: string
    :param registrationStatus: [REQUIRED]
            Specifies the registration status of the workflow types to list.
            

    :type nextPageToken: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the results in reverse order. By default the results are returned in ascending alphabetical order of the name of the workflow types.

    :rtype: dict
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
    
    nextPageToken (string) -- If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    maximumPageSize (integer) -- The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
    This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
    
    reverseOrder (boolean) -- When set to true , returns the results in reverse order. By default the results are returned in ascending alphabetical order of the name of the workflow types.
    
    """
    pass

def poll_for_activity_task(domain=None, taskList=None, identity=None):
    """
    Used by workers to get an  ActivityTask from the specified activity taskList . This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available. The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll will return an empty result. An empty result, in this context, means that an ActivityTask is returned, but that the value of taskToken is an empty string. If a task is returned, the worker should use its type to identify and process it correctly.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.poll_for_activity_task(
        domain='string',
        taskList={
            'name': 'string'
        },
        identity='string'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain that contains the task lists being polled.
            

    :type taskList: dict
    :param taskList: [REQUIRED]
            Specifies the task list to poll for activity tasks.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            name (string) -- [REQUIRED]The name of the task list.
            

    :type identity: string
    :param identity: Identity of the worker making the request, recorded in the ActivityTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.

    :rtype: dict
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
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    identity (string) -- Identity of the worker making the request, recorded in the ActivityTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
    
    """
    pass

def poll_for_decision_task(domain=None, taskList=None, identity=None, nextPageToken=None, maximumPageSize=None, reverseOrder=None):
    """
    Used by deciders to get a  DecisionTask from the specified decision taskList . A decision task may be returned for any open workflow execution that is using the specified task list. The task includes a paginated view of the history of the workflow execution. The decider should use the workflow type and the history to determine how to properly handle the task.
    This action initiates a long poll, where the service holds the HTTP connection open and responds as soon a task becomes available. If no decision task is available in the specified task list before the timeout of 60 seconds expires, an empty result is returned. An empty result, in this context, means that a DecisionTask is returned, but that the value of taskToken is an empty string.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
    :param domain: [REQUIRED]
            The name of the domain containing the task lists to poll.
            

    :type taskList: dict
    :param taskList: [REQUIRED]
            Specifies the task list to poll for decision tasks.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            name (string) -- [REQUIRED]The name of the task list.
            

    :type identity: string
    :param identity: Identity of the decider making the request, which is recorded in the DecisionTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.

    :type nextPageToken: string
    :param nextPageToken: If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
            The configured maximumPageSize determines how many results can be returned in a single call.
            Note
            The nextPageToken returned by this action cannot be used with GetWorkflowExecutionHistory to get the next page. You must call PollForDecisionTask again (with the nextPageToken ) to retrieve the next page of history records. Calling PollForDecisionTask with a nextPageToken will not return a new decision task.
            .
            

    :type maximumPageSize: integer
    :param maximumPageSize: The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type reverseOrder: boolean
    :param reverseOrder: When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimestamp of the events.

    :rtype: dict
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
                    'workflowType': {
                        'name': 'string',
                        'version': 'string'
                    },
                    'tagList': [
                        'string',
                    ],
                    'taskPriority': 'string',
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
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    identity (string) -- Identity of the decider making the request, which is recorded in the DecisionTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
    nextPageToken (string) -- If a NextPageToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextPageToken . Keep all other arguments unchanged.
    The configured maximumPageSize determines how many results can be returned in a single call.
    
    Note
    The nextPageToken returned by this action cannot be used with  GetWorkflowExecutionHistory to get the next page. You must call  PollForDecisionTask again (with the nextPageToken ) to retrieve the next page of history records. Calling  PollForDecisionTask with a nextPageToken will not return a new decision task.
    
    .
    
    maximumPageSize (integer) -- The maximum number of results that will be returned per call. nextPageToken can be used to obtain futher pages of results. The default is 1000, which is the maximum allowed page size. You can, however, specify a page size smaller than the maximum.
    This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
    
    reverseOrder (boolean) -- When set to true , returns the events in reverse order. By default the results are returned in ascending order of the eventTimestamp of the events.
    
    """
    pass

def record_activity_task_heartbeat(taskToken=None, details=None):
    """
    Used by activity workers to report to the service that the  ActivityTask represented by the specified taskToken is still making progress. The worker can also (optionally) specify details of the progress, for example percent complete, using the details parameter. This action can also be used by the worker as a mechanism to check if cancellation is being requested for the activity task. If a cancellation is being attempted for the specified task, then the boolean cancelRequested flag returned by the service is set to true .
    This action resets the taskHeartbeatTimeout clock. The taskHeartbeatTimeout is specified in  RegisterActivityType .
    This action does not in itself create an event in the workflow execution history. However, if the task times out, the workflow execution history will contain a ActivityTaskTimedOut event that contains the information from the last heartbeat generated by the activity worker.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.record_activity_task_heartbeat(
        taskToken='string',
        details='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]
            The taskToken of the ActivityTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            

    :type details: string
    :param details: If specified, contains details about the progress of the task.

    :rtype: dict
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
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
    :param domain: [REQUIRED]
            The name of the domain in which this activity is to be registered.
            

    :type name: string
    :param name: [REQUIRED]
            The name of the activity type within the domain.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            

    :type version: string
    :param version: [REQUIRED]
            The version of the activity type.
            Note
            The activity type consists of the name and version, the combination of which must be unique within the domain.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            

    :type description: string
    :param description: A textual description of the activity type.

    :type defaultTaskStartToCloseTimeout: string
    :param defaultTaskStartToCloseTimeout: If set, specifies the default maximum duration that a worker can take to process tasks of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            

    :type defaultTaskHeartbeatTimeout: string
    :param defaultTaskHeartbeatTimeout: If set, specifies the default maximum time before which a worker processing a task of this type must report progress by calling RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision. If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an UnknownResource fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            

    :type defaultTaskList: dict
    :param defaultTaskList: If set, specifies the default task list to use for scheduling tasks of this activity type. This default task list is used if a task list is not provided when a task is scheduled through the ScheduleActivityTask decision.
            name (string) -- [REQUIRED]The name of the task list.
            

    :type defaultTaskPriority: string
    :param defaultTaskPriority: The default task priority to assign to the activity type. If not assigned, then '0' will be used. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
            For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
            

    :type defaultTaskScheduleToStartTimeout: string
    :param defaultTaskScheduleToStartTimeout: If set, specifies the default maximum duration that a task of this activity type can wait before being assigned to a worker. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            

    :type defaultTaskScheduleToCloseTimeout: string
    :param defaultTaskScheduleToCloseTimeout: If set, specifies the default maximum duration for a task of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which this activity is to be registered.
    
    name (string) -- [REQUIRED]
    The name of the activity type within the domain.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
    
    version (string) -- [REQUIRED]
    The version of the activity type.
    
    Note
    The activity type consists of the name and version, the combination of which must be unique within the domain.
    
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
    
    description (string) -- A textual description of the activity type.
    defaultTaskStartToCloseTimeout (string) -- If set, specifies the default maximum duration that a worker can take to process tasks of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision.
    The duration is specified in seconds; an integer greater than or equal to 0. The value "NONE" can be used to specify unlimited duration.
    
    defaultTaskHeartbeatTimeout (string) -- If set, specifies the default maximum time before which a worker processing a task of this type must report progress by calling  RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision. If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an UnknownResource fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.
    The duration is specified in seconds; an integer greater than or equal to 0. The value "NONE" can be used to specify unlimited duration.
    
    defaultTaskList (dict) -- If set, specifies the default task list to use for scheduling tasks of this activity type. This default task list is used if a task list is not provided when a task is scheduled through the ScheduleActivityTask decision.
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    defaultTaskPriority (string) -- The default task priority to assign to the activity type. If not assigned, then "0" will be used. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
    For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
    
    defaultTaskScheduleToStartTimeout (string) -- If set, specifies the default maximum duration that a task of this activity type can wait before being assigned to a worker. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision.
    The duration is specified in seconds; an integer greater than or equal to 0. The value "NONE" can be used to specify unlimited duration.
    
    defaultTaskScheduleToCloseTimeout (string) -- If set, specifies the default maximum duration for a task of this activity type. This default can be overridden when scheduling an activity task using the ScheduleActivityTask decision.
    The duration is specified in seconds; an integer greater than or equal to 0. The value "NONE" can be used to specify unlimited duration.
    
    
    """
    pass

def register_domain(name=None, description=None, workflowExecutionRetentionPeriodInDays=None):
    """
    Registers a new domain.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.register_domain(
        name='string',
        description='string',
        workflowExecutionRetentionPeriodInDays='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            Name of the domain to register. The name must be unique in the region that the domain is registered in.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            

    :type description: string
    :param description: A text description of the domain.

    :type workflowExecutionRetentionPeriodInDays: string
    :param workflowExecutionRetentionPeriodInDays: [REQUIRED]
            The duration (in days) that records and histories of workflow executions on the domain should be kept by the service. After the retention period, the workflow execution is not available in the results of visibility calls.
            If you pass the value NONE or 0 (zero), then the workflow execution history will not be retained. As soon as the workflow execution completes, the execution record and its history are deleted.
            The maximum workflow execution retention period is 90 days. For more information about Amazon SWF service limits, see: Amazon SWF Service Limits in the Amazon SWF Developer Guide .
            

    :returns: 
    name (string) -- [REQUIRED]
    Name of the domain to register. The name must be unique in the region that the domain is registered in.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
    
    description (string) -- A text description of the domain.
    workflowExecutionRetentionPeriodInDays (string) -- [REQUIRED]
    The duration (in days) that records and histories of workflow executions on the domain should be kept by the service. After the retention period, the workflow execution is not available in the results of visibility calls.
    If you pass the value NONE or 0 (zero), then the workflow execution history will not be retained. As soon as the workflow execution completes, the execution record and its history are deleted.
    The maximum workflow execution retention period is 90 days. For more information about Amazon SWF service limits, see: Amazon SWF Service Limits in the Amazon SWF Developer Guide .
    
    
    """
    pass

def register_workflow_type(domain=None, name=None, version=None, description=None, defaultTaskStartToCloseTimeout=None, defaultExecutionStartToCloseTimeout=None, defaultTaskList=None, defaultTaskPriority=None, defaultChildPolicy=None, defaultLambdaRole=None):
    """
    Registers a new workflow type and its configuration settings in the specified domain.
    The retention period for the workflow history is set by the  RegisterDomain action.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
    :param domain: [REQUIRED]
            The name of the domain in which to register the workflow type.
            

    :type name: string
    :param name: [REQUIRED]
            The name of the workflow type.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            

    :type version: string
    :param version: [REQUIRED]
            The version of the workflow type.
            Note
            The workflow type consists of the name and version, the combination of which must be unique within the domain. To get a list of all currently registered workflow types, use the ListWorkflowTypes action.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            

    :type description: string
    :param description: Textual description of the workflow type.

    :type defaultTaskStartToCloseTimeout: string
    :param defaultTaskStartToCloseTimeout: If set, specifies the default maximum duration of decision tasks for this workflow type. This default can be overridden when starting a workflow execution using the StartWorkflowExecution action or the StartChildWorkflowExecution decision.
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            

    :type defaultExecutionStartToCloseTimeout: string
    :param defaultExecutionStartToCloseTimeout: If set, specifies the default maximum duration for executions of this workflow type. You can override this default when starting an execution through the StartWorkflowExecution action or StartChildWorkflowExecution decision.
            The duration is specified in seconds; an integer greater than or equal to 0. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of 'NONE' for defaultExecutionStartToCloseTimeout ; there is a one-year max limit on the time that a workflow execution can run. Exceeding this limit will always cause the workflow execution to time out.
            

    :type defaultTaskList: dict
    :param defaultTaskList: If set, specifies the default task list to use for scheduling decision tasks for executions of this workflow type. This default is used only if a task list is not provided when starting the execution through the StartWorkflowExecution action or StartChildWorkflowExecution decision.
            name (string) -- [REQUIRED]The name of the task list.
            

    :type defaultTaskPriority: string
    :param defaultTaskPriority: The default task priority to assign to the workflow type. If not assigned, then '0' will be used. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
            For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
            

    :type defaultChildPolicy: string
    :param defaultChildPolicy: If set, specifies the default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the StartWorkflowExecution action or the StartChildWorkflowExecution decision.
            The supported child policies are:
            TERMINATE: the child executions will be terminated.
            REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
            ABANDON: no action will be taken. The child executions will continue to run.
            

    :type defaultLambdaRole: string
    :param defaultLambdaRole: The ARN of the default IAM role to use when a workflow execution of this type invokes AWS Lambda functions.
            This default can be overridden when starting a workflow execution using the StartWorkflowExecution action or the StartChildWorkflowExecution and ContinueAsNewWorkflowExecution decision.
            

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which to register the workflow type.
    
    name (string) -- [REQUIRED]
    The name of the workflow type.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
    
    version (string) -- [REQUIRED]
    The version of the workflow type.
    
    Note
    The workflow type consists of the name and version, the combination of which must be unique within the domain. To get a list of all currently registered workflow types, use the  ListWorkflowTypes action.
    
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
    
    description (string) -- Textual description of the workflow type.
    defaultTaskStartToCloseTimeout (string) -- If set, specifies the default maximum duration of decision tasks for this workflow type. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution decision.
    The duration is specified in seconds; an integer greater than or equal to 0. The value "NONE" can be used to specify unlimited duration.
    
    defaultExecutionStartToCloseTimeout (string) -- If set, specifies the default maximum duration for executions of this workflow type. You can override this default when starting an execution through the  StartWorkflowExecution action or StartChildWorkflowExecution decision.
    The duration is specified in seconds; an integer greater than or equal to 0. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of "NONE" for defaultExecutionStartToCloseTimeout ; there is a one-year max limit on the time that a workflow execution can run. Exceeding this limit will always cause the workflow execution to time out.
    
    defaultTaskList (dict) -- If set, specifies the default task list to use for scheduling decision tasks for executions of this workflow type. This default is used only if a task list is not provided when starting the execution through the  StartWorkflowExecution action or StartChildWorkflowExecution decision.
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    defaultTaskPriority (string) -- The default task priority to assign to the workflow type. If not assigned, then "0" will be used. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
    For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
    
    defaultChildPolicy (string) -- If set, specifies the default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution decision.
    The supported child policies are:
    
    TERMINATE: the child executions will be terminated.
    REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
    ABANDON: no action will be taken. The child executions will continue to run.
    
    
    defaultLambdaRole (string) -- The ARN of the default IAM role to use when a workflow execution of this type invokes AWS Lambda functions.
    This default can be overridden when starting a workflow execution using the  StartWorkflowExecution action or the StartChildWorkflowExecution and ContinueAsNewWorkflowExecution decision.
    
    
    """
    pass

def request_cancel_workflow_execution(domain=None, workflowId=None, runId=None):
    """
    Records a WorkflowExecutionCancelRequested event in the currently running workflow execution identified by the given domain, workflowId, and runId. This logically requests the cancellation of the workflow execution as a whole. It is up to the decider to take appropriate actions when it receives an execution history with this event.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.request_cancel_workflow_execution(
        domain='string',
        workflowId='string',
        runId='string'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain containing the workflow execution to cancel.
            

    :type workflowId: string
    :param workflowId: [REQUIRED]
            The workflowId of the workflow execution to cancel.
            

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
    Used by workers to tell the service that the  ActivityTask identified by the taskToken was successfully canceled. Additional details can be optionally provided using the details argument.
    These details (if provided) appear in the ActivityTaskCanceled event added to the workflow history.
    A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to  RespondActivityTaskCompleted , RespondActivityTaskCanceled,  RespondActivityTaskFailed , or the task has timed out .
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.respond_activity_task_canceled(
        taskToken='string',
        details='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]
            The taskToken of the ActivityTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            

    :type details: string
    :param details: Optional. Information about the cancellation.

    :returns: 
    taskToken (string) -- [REQUIRED]
    The taskToken of the  ActivityTask .
    
    Warning
    taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
    
    
    details (string) -- Optional. Information about the cancellation.
    
    """
    pass

def respond_activity_task_completed(taskToken=None, result=None):
    """
    Used by workers to tell the service that the  ActivityTask identified by the taskToken completed successfully with a result (if provided). The result appears in the ActivityTaskCompleted event in the workflow history.
    A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to RespondActivityTaskCompleted,  RespondActivityTaskCanceled ,  RespondActivityTaskFailed , or the task has timed out .
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.respond_activity_task_completed(
        taskToken='string',
        result='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]
            The taskToken of the ActivityTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            

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
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.respond_activity_task_failed(
        taskToken='string',
        reason='string',
        details='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]
            The taskToken of the ActivityTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            

    :type reason: string
    :param reason: Description of the error that may assist in diagnostics.

    :type details: string
    :param details: Optional. Detailed information about the failure.

    :returns: 
    taskToken (string) -- [REQUIRED]
    The taskToken of the  ActivityTask .
    
    Warning
    taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
    
    
    reason (string) -- Description of the error that may assist in diagnostics.
    details (string) -- Optional. Detailed information about the failure.
    
    """
    pass

def respond_decision_task_completed(taskToken=None, decisions=None, executionContext=None):
    """
    Used by deciders to tell the service that the  DecisionTask identified by the taskToken has successfully completed. The decisions argument specifies the list of decisions made while processing the task.
    A DecisionTaskCompleted event is added to the workflow history. The executionContext specified is attached to the event in the workflow execution history.
    Access Control
    If an IAM policy grants permission to use RespondDecisionTaskCompleted , it can express permissions for the list of decisions in the decisions parameter. Each of the decisions has one or more parameters, much like a regular API call. To allow for policies to be as readable as possible, you can express permissions on decisions as if they were actual API calls, including applying conditions to some parameters. For more information, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
                    'input': 'string',
                    'startToCloseTimeout': 'string'
                }
            },
        ],
        executionContext='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]
            The taskToken from the DecisionTask .
            Warning
            taskToken is generated by the service and should be treated as an opaque value. If the task is passed to another process, its taskToken must also be passed. This enables it to provide its progress and respond with results.
            

    :type decisions: list
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
            
            

    :type executionContext: string
    :param executionContext: User defined context to add to workflow execution.

    """
    pass

def signal_workflow_execution(domain=None, workflowId=None, runId=None, signalName=None, input=None):
    """
    Records a WorkflowExecutionSignaled event in the workflow execution history and creates a decision task for the workflow execution identified by the given domain, workflowId and runId. The event is recorded with the specified user defined signalName and input (if provided).
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.signal_workflow_execution(
        domain='string',
        workflowId='string',
        runId='string',
        signalName='string',
        input='string'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The name of the domain containing the workflow execution to signal.
            

    :type workflowId: string
    :param workflowId: [REQUIRED]
            The workflowId of the workflow execution to signal.
            

    :type runId: string
    :param runId: The runId of the workflow execution to signal.

    :type signalName: string
    :param signalName: [REQUIRED]
            The name of the signal. This name must be meaningful to the target workflow.
            

    :type input: string
    :param input: Data to attach to the WorkflowExecutionSignaled event in the target workflow execution's history.

    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain containing the workflow execution to signal.
    
    workflowId (string) -- [REQUIRED]
    The workflowId of the workflow execution to signal.
    
    runId (string) -- The runId of the workflow execution to signal.
    signalName (string) -- [REQUIRED]
    The name of the signal. This name must be meaningful to the target workflow.
    
    input (string) -- Data to attach to the WorkflowExecutionSignaled event in the target workflow execution's history.
    
    """
    pass

def start_workflow_execution(domain=None, workflowId=None, workflowType=None, taskList=None, taskPriority=None, input=None, executionStartToCloseTimeout=None, tagList=None, taskStartToCloseTimeout=None, childPolicy=None, lambdaRole=None):
    """
    Starts an execution of the workflow type in the specified domain using the provided workflowId and input data.
    This action returns the newly started workflow execution.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
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
    :param domain: [REQUIRED]
            The name of the domain in which the workflow execution is created.
            

    :type workflowId: string
    :param workflowId: [REQUIRED]
            The user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a restart of a previous execution. You cannot have two open workflow executions with the same workflowId at the same time.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            

    :type workflowType: dict
    :param workflowType: [REQUIRED]
            The type of the workflow to start.
            name (string) -- [REQUIRED]Required. The name of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            version (string) -- [REQUIRED]Required. The version of the workflow type.
            Note
            The combination of workflow type name and version must be unique with in a domain.
            

    :type taskList: dict
    :param taskList: The task list to use for the decision tasks generated for this workflow execution. This overrides the defaultTaskList specified when registering the workflow type.
            Note
            A task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault will be returned.
            The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
            name (string) -- [REQUIRED]The name of the task list.
            

    :type taskPriority: string
    :param taskPriority: The task priority to use for this workflow execution. This will override any default priority that was assigned when the workflow type was registered. If not set, then the default task priority for the workflow type will be used. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
            For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
            

    :type input: string
    :param input: The input for the workflow execution. This is a free form string which should be meaningful to the workflow you are starting. This input is made available to the new workflow execution in the WorkflowExecutionStarted history event.

    :type executionStartToCloseTimeout: string
    :param executionStartToCloseTimeout: The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.
            The duration is specified in seconds; an integer greater than or equal to 0. Exceeding this limit will cause the workflow execution to time out. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of 'NONE' for this timeout; there is a one-year max limit on the time that a workflow execution can run.
            Note
            An execution start-to-close timeout must be specified either through this parameter or as a default when the workflow type is registered. If neither this parameter nor a default execution start-to-close timeout is specified, a fault is returned.
            

    :type tagList: list
    :param tagList: The list of tags to associate with the workflow execution. You can specify a maximum of 5 tags. You can list workflow executions with a specific tag by calling ListOpenWorkflowExecutions or ListClosedWorkflowExecutions and specifying a TagFilter .
            (string) --
            

    :type taskStartToCloseTimeout: string
    :param taskStartToCloseTimeout: Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the defaultTaskStartToCloseTimout specified when registering the workflow type using RegisterWorkflowType .
            The duration is specified in seconds; an integer greater than or equal to 0. The value 'NONE' can be used to specify unlimited duration.
            Note
            A task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault will be returned.
            

    :type childPolicy: string
    :param childPolicy: If set, specifies the policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using RegisterWorkflowType .
            The supported child policies are:
            TERMINATE: the child executions will be terminated.
            REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
            ABANDON: no action will be taken. The child executions will continue to run.
            Note
            A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault will be returned.
            

    :type lambdaRole: string
    :param lambdaRole: The ARN of an IAM role that authorizes Amazon SWF to invoke AWS Lambda functions.
            Note
            In order for this workflow execution to invoke AWS Lambda functions, an appropriate IAM role must be specified either as a default for the workflow type or through this field.
            

    :rtype: dict
    :return: {
        'runId': 'string'
    }
    
    
    :returns: 
    domain (string) -- [REQUIRED]
    The name of the domain in which the workflow execution is created.
    
    workflowId (string) -- [REQUIRED]
    The user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a restart of a previous execution. You cannot have two open workflow executions with the same workflowId at the same time.
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
    
    workflowType (dict) -- [REQUIRED]
    The type of the workflow to start.
    
    name (string) -- [REQUIRED]Required. The name of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    version (string) -- [REQUIRED]Required. The version of the workflow type.
    
    Note
    The combination of workflow type name and version must be unique with in a domain.
    
    
    
    
    taskList (dict) -- The task list to use for the decision tasks generated for this workflow execution. This overrides the defaultTaskList specified when registering the workflow type.
    
    Note
    A task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault will be returned.
    
    The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (u0000-u001f | u007f - u009f). Also, it must not contain the literal string quotarnquot.
    
    name (string) -- [REQUIRED]The name of the task list.
    
    
    
    taskPriority (string) -- The task priority to use for this workflow execution. This will override any default priority that was assigned when the workflow type was registered. If not set, then the default task priority for the workflow type will be used. Valid values are integers that range from Java's Integer.MIN_VALUE (-2147483648) to Integer.MAX_VALUE (2147483647). Higher numbers indicate higher priority.
    For more information about setting task priority, see Setting Task Priority in the Amazon Simple Workflow Developer Guide .
    
    input (string) -- The input for the workflow execution. This is a free form string which should be meaningful to the workflow you are starting. This input is made available to the new workflow execution in the WorkflowExecutionStarted history event.
    executionStartToCloseTimeout (string) -- The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.
    The duration is specified in seconds; an integer greater than or equal to 0. Exceeding this limit will cause the workflow execution to time out. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of "NONE" for this timeout; there is a one-year max limit on the time that a workflow execution can run.
    
    Note
    An execution start-to-close timeout must be specified either through this parameter or as a default when the workflow type is registered. If neither this parameter nor a default execution start-to-close timeout is specified, a fault is returned.
    
    
    tagList (list) -- The list of tags to associate with the workflow execution. You can specify a maximum of 5 tags. You can list workflow executions with a specific tag by calling  ListOpenWorkflowExecutions or  ListClosedWorkflowExecutions and specifying a  TagFilter .
    
    (string) --
    
    
    taskStartToCloseTimeout (string) -- Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the defaultTaskStartToCloseTimout specified when registering the workflow type using  RegisterWorkflowType .
    The duration is specified in seconds; an integer greater than or equal to 0. The value "NONE" can be used to specify unlimited duration.
    
    Note
    A task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault will be returned.
    
    
    childPolicy (string) -- If set, specifies the policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the  TerminateWorkflowExecution action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using  RegisterWorkflowType .
    The supported child policies are:
    
    TERMINATE: the child executions will be terminated.
    REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
    ABANDON: no action will be taken. The child executions will continue to run.
    
    
    Note
    A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault will be returned.
    
    
    lambdaRole (string) -- The ARN of an IAM role that authorizes Amazon SWF to invoke AWS Lambda functions.
    
    Note
    In order for this workflow execution to invoke AWS Lambda functions, an appropriate IAM role must be specified either as a default for the workflow type or through this field.
    
    
    
    """
    pass

def terminate_workflow_execution(domain=None, workflowId=None, runId=None, reason=None, details=None, childPolicy=None):
    """
    Records a WorkflowExecutionTerminated event and forces closure of the workflow execution identified by the given domain, runId, and workflowId. The child policy, registered with the workflow type or specified when starting this execution, is applied to any open child workflow executions of this workflow execution.
    Access Control
    You can use IAM policies to control this action's access to Amazon SWF resources as follows:
    If the caller does not have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's cause parameter will be set to OPERATION_NOT_PERMITTED. For details and example IAM policies, see Using IAM to Manage Access to Amazon SWF Workflows .
    See also: AWS API Documentation
    
    
    :example: response = client.terminate_workflow_execution(
        domain='string',
        workflowId='string',
        runId='string',
        reason='string',
        details='string',
        childPolicy='TERMINATE'|'REQUEST_CANCEL'|'ABANDON'
    )
    
    
    :type domain: string
    :param domain: [REQUIRED]
            The domain of the workflow execution to terminate.
            

    :type workflowId: string
    :param workflowId: [REQUIRED]
            The workflowId of the workflow execution to terminate.
            

    :type runId: string
    :param runId: The runId of the workflow execution to terminate.

    :type reason: string
    :param reason: Optional. A descriptive reason for terminating the workflow execution.

    :type details: string
    :param details: Optional. Details for terminating the workflow execution.

    :type childPolicy: string
    :param childPolicy: If set, specifies the policy to use for the child workflow executions of the workflow execution being terminated. This policy overrides the child policy specified for the workflow execution at registration time or when starting the execution.
            The supported child policies are:
            TERMINATE: the child executions will be terminated.
            REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
            ABANDON: no action will be taken. The child executions will continue to run.
            Note
            A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault will be returned.
            

    :returns: 
    domain (string) -- [REQUIRED]
    The domain of the workflow execution to terminate.
    
    workflowId (string) -- [REQUIRED]
    The workflowId of the workflow execution to terminate.
    
    runId (string) -- The runId of the workflow execution to terminate.
    reason (string) -- Optional. A descriptive reason for terminating the workflow execution.
    details (string) -- Optional. Details for terminating the workflow execution.
    childPolicy (string) -- If set, specifies the policy to use for the child workflow executions of the workflow execution being terminated. This policy overrides the child policy specified for the workflow execution at registration time or when starting the execution.
    The supported child policies are:
    
    TERMINATE: the child executions will be terminated.
    REQUEST_CANCEL: a request to cancel will be attempted for each child execution by recording a WorkflowExecutionCancelRequested event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
    ABANDON: no action will be taken. The child executions will continue to run.
    
    
    Note
    A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault will be returned.
    
    
    
    """
    pass

