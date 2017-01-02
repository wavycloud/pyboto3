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

def create_activity(name=None):
    """
    Creates an activity.
    See also: AWS API Documentation
    
    
    :example: response = client.create_activity(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the activity to create. This name must be unique for your AWS account and region.
            

    :rtype: dict
    :return: {
        'activityArn': 'string',
        'creationDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def create_state_machine(name=None, definition=None, roleArn=None):
    """
    Creates a state machine.
    See also: AWS API Documentation
    
    
    :example: response = client.create_state_machine(
        name='string',
        definition='string',
        roleArn='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the state machine. This name must be unique for your AWS account and region.
            

    :type definition: string
    :param definition: [REQUIRED]
            The Amazon States Language definition of the state machine.
            

    :type roleArn: string
    :param roleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
            

    :rtype: dict
    :return: {
        'stateMachineArn': 'string',
        'creationDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def delete_activity(activityArn=None):
    """
    Deletes an activity.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_activity(
        activityArn='string'
    )
    
    
    :type activityArn: string
    :param activityArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the activity to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_state_machine(stateMachineArn=None):
    """
    Deletes a state machine. This is an asynchronous operation-- it sets the state machine's status to "DELETING" and begins the delete process.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_state_machine(
        stateMachineArn='string'
    )
    
    
    :type stateMachineArn: string
    :param stateMachineArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the state machine to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_activity(activityArn=None):
    """
    Describes an activity.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_activity(
        activityArn='string'
    )
    
    
    :type activityArn: string
    :param activityArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the activity to describe.
            

    :rtype: dict
    :return: {
        'activityArn': 'string',
        'name': 'string',
        'creationDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_execution(executionArn=None):
    """
    Describes an execution.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_execution(
        executionArn='string'
    )
    
    
    :type executionArn: string
    :param executionArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the execution to describe.
            

    :rtype: dict
    :return: {
        'executionArn': 'string',
        'stateMachineArn': 'string',
        'name': 'string',
        'status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
        'startDate': datetime(2015, 1, 1),
        'stopDate': datetime(2015, 1, 1),
        'input': 'string',
        'output': 'string'
    }
    
    
    """
    pass

def describe_state_machine(stateMachineArn=None):
    """
    Describes a state machine.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_state_machine(
        stateMachineArn='string'
    )
    
    
    :type stateMachineArn: string
    :param stateMachineArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the state machine to describe.
            

    :rtype: dict
    :return: {
        'stateMachineArn': 'string',
        'name': 'string',
        'status': 'ACTIVE'|'DELETING',
        'definition': 'string',
        'roleArn': 'string',
        'creationDate': datetime(2015, 1, 1)
    }
    
    
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

def get_activity_task(activityArn=None, workerName=None):
    """
    Used by workers to retrieve a task (with the specified activity ARN) scheduled for execution by a running state machine. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available (i.e. an execution of a task of this type is needed.) The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll will return an empty result, that is, the taskToken returned is an empty string.
    See also: AWS API Documentation
    
    
    :example: response = client.get_activity_task(
        activityArn='string',
        workerName='string'
    )
    
    
    :type activityArn: string
    :param activityArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the activity to retrieve tasks from.
            

    :type workerName: string
    :param workerName: An arbitrary name may be provided in order to identify the worker that the task is assigned to. This name will be used when it is logged in the execution history.

    :rtype: dict
    :return: {
        'taskToken': 'string',
        'input': 'string'
    }
    
    
    """
    pass

def get_execution_history(executionArn=None, maxResults=None, reverseOrder=None, nextToken=None):
    """
    Returns the history of the specified execution as a list of events. By default, the results are returned in ascending order of the timeStamp of the events. Use the reverseOrder parameter to get the latest events first. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextToken returned by the previous call.
    See also: AWS API Documentation
    
    
    :example: response = client.get_execution_history(
        executionArn='string',
        maxResults=123,
        reverseOrder=True|False,
        nextToken='string'
    )
    
    
    :type executionArn: string
    :param executionArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the execution.
            

    :type maxResults: integer
    :param maxResults: The maximum number of results that will be returned per call. nextToken can be used to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type reverseOrder: boolean
    :param reverseOrder: Lists events in descending order of their timeStamp .

    :type nextToken: string
    :param nextToken: If a nextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextToken . Keep all other arguments unchanged.
            The configured maxResults determines how many results can be returned in a single call.
            

    :rtype: dict
    :return: {
        'events': [
            {
                'timestamp': datetime(2015, 1, 1),
                'type': 'ActivityFailed'|'ActivityScheduleFailed'|'ActivityScheduled'|'ActivityStarted'|'ActivitySucceeded'|'ActivityTimedOut'|'ChoiceStateEntered'|'ChoiceStateExited'|'ExecutionFailed'|'ExecutionStarted'|'ExecutionSucceeded'|'ExecutionAborted'|'ExecutionTimedOut'|'FailStateEntered'|'LambdaFunctionFailed'|'LambdaFunctionScheduleFailed'|'LambdaFunctionScheduled'|'LambdaFunctionStartFailed'|'LambdaFunctionStarted'|'LambdaFunctionSucceeded'|'LambdaFunctionTimedOut'|'SucceedStateEntered'|'SucceedStateExited'|'TaskStateEntered'|'TaskStateExited'|'PassStateEntered'|'PassStateExited'|'ParallelStateEntered'|'ParallelStateExited'|'WaitStateEntered'|'WaitStateExited',
                'id': 123,
                'previousEventId': 123,
                'activityFailedEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'activityScheduleFailedEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'activityScheduledEventDetails': {
                    'resource': 'string',
                    'input': 'string',
                    'timeoutInSeconds': 123,
                    'heartbeatInSeconds': 123
                },
                'activityStartedEventDetails': {
                    'workerName': 'string'
                },
                'activitySucceededEventDetails': {
                    'output': 'string'
                },
                'activityTimedOutEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'executionFailedEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'executionStartedEventDetails': {
                    'input': 'string',
                    'roleArn': 'string'
                },
                'executionSucceededEventDetails': {
                    'output': 'string'
                },
                'executionAbortedEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'executionTimedOutEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'lambdaFunctionFailedEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'lambdaFunctionScheduleFailedEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'lambdaFunctionScheduledEventDetails': {
                    'resource': 'string',
                    'input': 'string',
                    'timeoutInSeconds': 123
                },
                'lambdaFunctionStartFailedEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'lambdaFunctionSucceededEventDetails': {
                    'output': 'string'
                },
                'lambdaFunctionTimedOutEventDetails': {
                    'error': 'string',
                    'cause': 'string'
                },
                'stateEnteredEventDetails': {
                    'name': 'string',
                    'input': 'string'
                },
                'stateExitedEventDetails': {
                    'name': 'string',
                    'output': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
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

def list_activities(maxResults=None, nextToken=None):
    """
    Lists the existing activities. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextToken returned by the previous call.
    See also: AWS API Documentation
    
    
    :example: response = client.list_activities(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results that will be returned per call. nextToken can be used to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type nextToken: string
    :param nextToken: If a nextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextToken . Keep all other arguments unchanged.
            The configured maxResults determines how many results can be returned in a single call.
            

    :rtype: dict
    :return: {
        'activities': [
            {
                'activityArn': 'string',
                'name': 'string',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_executions(stateMachineArn=None, statusFilter=None, maxResults=None, nextToken=None):
    """
    Lists the executions of a state machine that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextToken returned by the previous call.
    See also: AWS API Documentation
    
    
    :example: response = client.list_executions(
        stateMachineArn='string',
        statusFilter='RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type stateMachineArn: string
    :param stateMachineArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the state machine whose executions will be listed.
            

    :type statusFilter: string
    :param statusFilter: If specified, only list the executions whose current execution status matches the given filter.

    :type maxResults: integer
    :param maxResults: The maximum number of results that will be returned per call. nextToken can be used to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type nextToken: string
    :param nextToken: If a nextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextToken . Keep all other arguments unchanged.
            The configured maxResults determines how many results can be returned in a single call.
            

    :rtype: dict
    :return: {
        'executions': [
            {
                'executionArn': 'string',
                'stateMachineArn': 'string',
                'name': 'string',
                'status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
                'startDate': datetime(2015, 1, 1),
                'stopDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_state_machines(maxResults=None, nextToken=None):
    """
    Lists the existing state machines. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextToken returned by the previous call.
    See also: AWS API Documentation
    
    
    :example: response = client.list_state_machines(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results that will be returned per call. nextToken can be used to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000.
            This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
            

    :type nextToken: string
    :param nextToken: If a nextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in nextToken . Keep all other arguments unchanged.
            The configured maxResults determines how many results can be returned in a single call.
            

    :rtype: dict
    :return: {
        'stateMachines': [
            {
                'stateMachineArn': 'string',
                'name': 'string',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def send_task_failure(taskToken=None, error=None, cause=None):
    """
    Used by workers to report that the task identified by the taskToken failed.
    See also: AWS API Documentation
    
    
    :example: response = client.send_task_failure(
        taskToken='string',
        error='string',
        cause='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]
            The token that represents this task. Task tokens are generated by the service when the tasks are assigned to a worker (see GetActivityTask::taskToken).
            

    :type error: string
    :param error: An arbitrary error code that identifies the cause of the failure.

    :type cause: string
    :param cause: A more detailed explanation of the cause of the failure.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def send_task_heartbeat(taskToken=None):
    """
    Used by workers to report to the service that the task represented by the specified taskToken is still making progress. This action resets the Heartbeat clock. The Heartbeat threshold is specified in the state machine's Amazon States Language definition. This action does not in itself create an event in the execution history. However, if the task times out, the execution history will contain an ActivityTimedOut event.
    See also: AWS API Documentation
    
    
    :example: response = client.send_task_heartbeat(
        taskToken='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]
            The token that represents this task. Task tokens are generated by the service when the tasks are assigned to a worker (see GetActivityTask::taskToken).
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def send_task_success(taskToken=None, output=None):
    """
    Used by workers to report that the task identified by the taskToken completed successfully.
    See also: AWS API Documentation
    
    
    :example: response = client.send_task_success(
        taskToken='string',
        output='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]
            The token that represents this task. Task tokens are generated by the service when the tasks are assigned to a worker (see GetActivityTask::taskToken).
            

    :type output: string
    :param output: [REQUIRED]
            The JSON output of the task.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_execution(stateMachineArn=None, name=None, input=None):
    """
    Starts a state machine execution.
    See also: AWS API Documentation
    
    
    :example: response = client.start_execution(
        stateMachineArn='string',
        name='string',
        input='string'
    )
    
    
    :type stateMachineArn: string
    :param stateMachineArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the state machine to execute.
            

    :type name: string
    :param name: The name of the execution. This name must be unique for your AWS account and region.

    :type input: string
    :param input: The JSON input data for the execution.

    :rtype: dict
    :return: {
        'executionArn': 'string',
        'startDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def stop_execution(executionArn=None, error=None, cause=None):
    """
    Stops an execution.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_execution(
        executionArn='string',
        error='string',
        cause='string'
    )
    
    
    :type executionArn: string
    :param executionArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the execution to stop.
            

    :type error: string
    :param error: An arbitrary error code that identifies the cause of the termination.

    :type cause: string
    :param cause: A more detailed explanation of the cause of the termination.

    :rtype: dict
    :return: {
        'stopDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

