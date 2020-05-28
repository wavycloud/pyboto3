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

def create_activity(name=None, tags=None):
    """
    Creates an activity. An activity is a task that you write in any programming language and host on any machine that has access to AWS Step Functions. Activities must poll Step Functions using the GetActivityTask API action and respond using SendTask* API actions. This function lets Step Functions know the existence of your activity and returns an identifier for use in a state machine and when polling from the activity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_activity(
        name='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the activity to create. This name must be unique for your AWS account and region for 90 days. For more information, see Limits Related to State Machine Executions in the AWS Step Functions Developer Guide .\nA name must not contain:\n\nwhite space\nbrackets < > { } [ ]\nwildcard characters ? *\nspecial characters ' # % \\ ^ | ~ ` $ & , ; : /\ncontrol characters (U+0000-001F , U+007F-009F )\n\nTo enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.\n

    :type tags: list
    :param tags: The list of tags to add to a resource.\nAn array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide , and Controlling Access Using IAM Tags .\nTags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .\n\n(dict) --Tags are key-value pairs that can be associated with Step Functions state machines and activities.\nAn array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide , and Controlling Access Using IAM Tags .\nTags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .\n\nkey (string) --The key of a tag.\n\nvalue (string) --The value of a tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'activityArn': 'string',
    'creationDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

activityArn (string) --
The Amazon Resource Name (ARN) that identifies the created activity.

creationDate (datetime) --
The date the activity is created.







Exceptions

SFN.Client.exceptions.ActivityLimitExceeded
SFN.Client.exceptions.InvalidName
SFN.Client.exceptions.TooManyTags


    :return: {
        'activityArn': 'string',
        'creationDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    SFN.Client.exceptions.ActivityLimitExceeded
    SFN.Client.exceptions.InvalidName
    SFN.Client.exceptions.TooManyTags
    
    """
    pass

def create_state_machine(name=None, definition=None, roleArn=None, type=None, loggingConfiguration=None, tags=None):
    """
    Creates a state machine. A state machine consists of a collection of states that can do work (Task states), determine to which states to transition next (Choice states), stop an execution with an error (Fail states), and so on. State machines are specified using a JSON-based, structured language. For more information, see Amazon States Language in the AWS Step Functions User Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_state_machine(
        name='string',
        definition='string',
        roleArn='string',
        type='STANDARD'|'EXPRESS',
        loggingConfiguration={
            'level': 'ALL'|'ERROR'|'FATAL'|'OFF',
            'includeExecutionData': True|False,
            'destinations': [
                {
                    'cloudWatchLogsLogGroup': {
                        'logGroupArn': 'string'
                    }
                },
            ]
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the state machine.\nA name must not contain:\n\nwhite space\nbrackets < > { } [ ]\nwildcard characters ? *\nspecial characters ' # % \\ ^ | ~ ` $ & , ; : /\ncontrol characters (U+0000-001F , U+007F-009F )\n\nTo enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.\n

    :type definition: string
    :param definition: [REQUIRED]\nThe Amazon States Language definition of the state machine. See Amazon States Language .\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM role to use for this state machine.\n

    :type type: string
    :param type: Determines whether a Standard or Express state machine is created. The default is STANDARD . You cannot update the type of a state machine once it has been created.

    :type loggingConfiguration: dict
    :param loggingConfiguration: Defines what execution history events are logged and where they are logged.\n\nNote\nBy default, the level is set to OFF . For more information see Log Levels in the AWS Step Functions User Guide.\n\n\nlevel (string) --Defines which category of execution history events are logged.\n\nincludeExecutionData (boolean) --Determines whether execution data is included in your log. When set to FALSE , data is excluded.\n\ndestinations (list) --An array of objects that describes where your execution history events will be logged. Limited to size 1. Required, if your log level is not set to OFF .\n\n(dict) --\ncloudWatchLogsLogGroup (dict) --An object describing a CloudWatch log group. For more information, see AWS::Logs::LogGroup in the AWS CloudFormation User Guide.\n\nlogGroupArn (string) --The ARN of the the CloudWatch log group to which you want your logs emitted to. The ARN must end with :*\n\n\n\n\n\n\n\n\n

    :type tags: list
    :param tags: Tags to be added when creating a state machine.\nAn array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide , and Controlling Access Using IAM Tags .\nTags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .\n\n(dict) --Tags are key-value pairs that can be associated with Step Functions state machines and activities.\nAn array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide , and Controlling Access Using IAM Tags .\nTags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .\n\nkey (string) --The key of a tag.\n\nvalue (string) --The value of a tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'stateMachineArn': 'string',
    'creationDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

stateMachineArn (string) --
The Amazon Resource Name (ARN) that identifies the created state machine.

creationDate (datetime) --
The date the state machine is created.







Exceptions

SFN.Client.exceptions.InvalidArn
SFN.Client.exceptions.InvalidDefinition
SFN.Client.exceptions.InvalidName
SFN.Client.exceptions.InvalidLoggingConfiguration
SFN.Client.exceptions.StateMachineAlreadyExists
SFN.Client.exceptions.StateMachineDeleting
SFN.Client.exceptions.StateMachineLimitExceeded
SFN.Client.exceptions.StateMachineTypeNotSupported
SFN.Client.exceptions.TooManyTags


    :return: {
        'stateMachineArn': 'string',
        'creationDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    SFN.Client.exceptions.InvalidArn
    SFN.Client.exceptions.InvalidDefinition
    SFN.Client.exceptions.InvalidName
    SFN.Client.exceptions.InvalidLoggingConfiguration
    SFN.Client.exceptions.StateMachineAlreadyExists
    SFN.Client.exceptions.StateMachineDeleting
    SFN.Client.exceptions.StateMachineLimitExceeded
    SFN.Client.exceptions.StateMachineTypeNotSupported
    SFN.Client.exceptions.TooManyTags
    
    """
    pass

def delete_activity(activityArn=None):
    """
    Deletes an activity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_activity(
        activityArn='string'
    )
    
    
    :type activityArn: string
    :param activityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the activity to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SFN.Client.exceptions.InvalidArn


    :return: {}
    
    
    :returns: 
    SFN.Client.exceptions.InvalidArn
    
    """
    pass

def delete_state_machine(stateMachineArn=None):
    """
    Deletes a state machine. This is an asynchronous operation: It sets the state machine\'s status to DELETING and begins the deletion process.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_state_machine(
        stateMachineArn='string'
    )
    
    
    :type stateMachineArn: string
    :param stateMachineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the state machine to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SFN.Client.exceptions.InvalidArn


    :return: {}
    
    
    :returns: 
    SFN.Client.exceptions.InvalidArn
    
    """
    pass

def describe_activity(activityArn=None):
    """
    Describes an activity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_activity(
        activityArn='string'
    )
    
    
    :type activityArn: string
    :param activityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the activity to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'activityArn': 'string',
    'name': 'string',
    'creationDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
activityArn (string) --The Amazon Resource Name (ARN) that identifies the activity.

name (string) --The name of the activity.
A name must not contain:

white space
brackets < > { } [ ]
wildcard characters ? *
special characters " # % \\ ^ | ~ ` $ & , ; : /
control characters (U+0000-001F , U+007F-009F )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

creationDate (datetime) --The date the activity is created.






Exceptions

SFN.Client.exceptions.ActivityDoesNotExist
SFN.Client.exceptions.InvalidArn


    :return: {
        'activityArn': 'string',
        'name': 'string',
        'creationDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    SFN.Client.exceptions.ActivityDoesNotExist
    SFN.Client.exceptions.InvalidArn
    
    """
    pass

def describe_execution(executionArn=None):
    """
    Describes an execution.
    This API action is not supported by EXPRESS state machines.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_execution(
        executionArn='string'
    )
    
    
    :type executionArn: string
    :param executionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the execution to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'executionArn': 'string',
    'stateMachineArn': 'string',
    'name': 'string',
    'status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
    'startDate': datetime(2015, 1, 1),
    'stopDate': datetime(2015, 1, 1),
    'input': 'string',
    'output': 'string'
}


Response Structure

(dict) --
executionArn (string) --The Amazon Resource Name (ARN) that id entifies the execution.

stateMachineArn (string) --The Amazon Resource Name (ARN) of the executed stated machine.

name (string) --The name of the execution.
A name must not contain:

white space
brackets < > { } [ ]
wildcard characters ? *
special characters " # % \\ ^ | ~ ` $ & , ; : /
control characters (U+0000-001F , U+007F-009F )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

status (string) --The current status of the execution.

startDate (datetime) --The date the execution is started.

stopDate (datetime) --If the execution has already ended, the date the execution stopped.

input (string) --The string that contains the JSON input data of the execution.

output (string) --The JSON output data of the execution.

Note
This field is set only if the execution succeeds. If the execution fails, this field is null.







Exceptions

SFN.Client.exceptions.ExecutionDoesNotExist
SFN.Client.exceptions.InvalidArn


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
    
    
    :returns: 
    SFN.Client.exceptions.ExecutionDoesNotExist
    SFN.Client.exceptions.InvalidArn
    
    """
    pass

def describe_state_machine(stateMachineArn=None):
    """
    Describes a state machine.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_state_machine(
        stateMachineArn='string'
    )
    
    
    :type stateMachineArn: string
    :param stateMachineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the state machine to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'stateMachineArn': 'string',
    'name': 'string',
    'status': 'ACTIVE'|'DELETING',
    'definition': 'string',
    'roleArn': 'string',
    'type': 'STANDARD'|'EXPRESS',
    'creationDate': datetime(2015, 1, 1),
    'loggingConfiguration': {
        'level': 'ALL'|'ERROR'|'FATAL'|'OFF',
        'includeExecutionData': True|False,
        'destinations': [
            {
                'cloudWatchLogsLogGroup': {
                    'logGroupArn': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --
stateMachineArn (string) --The Amazon Resource Name (ARN) that identifies the state machine.

name (string) --The name of the state machine.
A name must not contain:

white space
brackets < > { } [ ]
wildcard characters ? *
special characters " # % \\ ^ | ~ ` $ & , ; : /
control characters (U+0000-001F , U+007F-009F )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

status (string) --The current status of the state machine.

definition (string) --The Amazon States Language definition of the state machine. See Amazon States Language .

roleArn (string) --The Amazon Resource Name (ARN) of the IAM role used when creating this state machine. (The IAM role maintains security by granting Step Functions access to AWS resources.)

type (string) --The type of the state machine (STANDARD or EXPRESS ).

creationDate (datetime) --The date the state machine is created.

loggingConfiguration (dict) --The LoggingConfiguration data type is used to set CloudWatch Logs options.

level (string) --Defines which category of execution history events are logged.

includeExecutionData (boolean) --Determines whether execution data is included in your log. When set to FALSE , data is excluded.

destinations (list) --An array of objects that describes where your execution history events will be logged. Limited to size 1. Required, if your log level is not set to OFF .

(dict) --
cloudWatchLogsLogGroup (dict) --An object describing a CloudWatch log group. For more information, see AWS::Logs::LogGroup in the AWS CloudFormation User Guide.

logGroupArn (string) --The ARN of the the CloudWatch log group to which you want your logs emitted to. The ARN must end with :*














Exceptions

SFN.Client.exceptions.InvalidArn
SFN.Client.exceptions.StateMachineDoesNotExist


    :return: {
        'stateMachineArn': 'string',
        'name': 'string',
        'status': 'ACTIVE'|'DELETING',
        'definition': 'string',
        'roleArn': 'string',
        'type': 'STANDARD'|'EXPRESS',
        'creationDate': datetime(2015, 1, 1),
        'loggingConfiguration': {
            'level': 'ALL'|'ERROR'|'FATAL'|'OFF',
            'includeExecutionData': True|False,
            'destinations': [
                {
                    'cloudWatchLogsLogGroup': {
                        'logGroupArn': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    SFN.Client.exceptions.InvalidArn
    SFN.Client.exceptions.StateMachineDoesNotExist
    
    """
    pass

def describe_state_machine_for_execution(executionArn=None):
    """
    Describes the state machine associated with a specific execution.
    This API action is not supported by EXPRESS state machines.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_state_machine_for_execution(
        executionArn='string'
    )
    
    
    :type executionArn: string
    :param executionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the execution you want state machine information for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'stateMachineArn': 'string',
    'name': 'string',
    'definition': 'string',
    'roleArn': 'string',
    'updateDate': datetime(2015, 1, 1),
    'loggingConfiguration': {
        'level': 'ALL'|'ERROR'|'FATAL'|'OFF',
        'includeExecutionData': True|False,
        'destinations': [
            {
                'cloudWatchLogsLogGroup': {
                    'logGroupArn': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --
stateMachineArn (string) --The Amazon Resource Name (ARN) of the state machine associated with the execution.

name (string) --The name of the state machine associated with the execution.

definition (string) --The Amazon States Language definition of the state machine. See Amazon States Language .

roleArn (string) --The Amazon Resource Name (ARN) of the IAM role of the State Machine for the execution.

updateDate (datetime) --The date and time the state machine associated with an execution was updated. For a newly created state machine, this is the creation date.

loggingConfiguration (dict) --The LoggingConfiguration data type is used to set CloudWatch Logs options.

level (string) --Defines which category of execution history events are logged.

includeExecutionData (boolean) --Determines whether execution data is included in your log. When set to FALSE , data is excluded.

destinations (list) --An array of objects that describes where your execution history events will be logged. Limited to size 1. Required, if your log level is not set to OFF .

(dict) --
cloudWatchLogsLogGroup (dict) --An object describing a CloudWatch log group. For more information, see AWS::Logs::LogGroup in the AWS CloudFormation User Guide.

logGroupArn (string) --The ARN of the the CloudWatch log group to which you want your logs emitted to. The ARN must end with :*














Exceptions

SFN.Client.exceptions.ExecutionDoesNotExist
SFN.Client.exceptions.InvalidArn


    :return: {
        'stateMachineArn': 'string',
        'name': 'string',
        'definition': 'string',
        'roleArn': 'string',
        'updateDate': datetime(2015, 1, 1),
        'loggingConfiguration': {
            'level': 'ALL'|'ERROR'|'FATAL'|'OFF',
            'includeExecutionData': True|False,
            'destinations': [
                {
                    'cloudWatchLogsLogGroup': {
                        'logGroupArn': 'string'
                    }
                },
            ]
        }
    }
    
    
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

def get_activity_task(activityArn=None, workerName=None):
    """
    Used by workers to retrieve a task (with the specified activity ARN) which has been scheduled for execution by a running state machine. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available (i.e. an execution of a task of this type is needed.) The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns a taskToken with a null string.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_activity_task(
        activityArn='string',
        workerName='string'
    )
    
    
    :type activityArn: string
    :param activityArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the activity to retrieve tasks from (assigned when you create the task using CreateActivity .)\n

    :type workerName: string
    :param workerName: You can provide an arbitrary name in order to identify the worker that the task is assigned to. This name is used when it is logged in the execution history.

    :rtype: dict

ReturnsResponse Syntax
{
    'taskToken': 'string',
    'input': 'string'
}


Response Structure

(dict) --

taskToken (string) --
A token that identifies the scheduled task. This token must be copied and included in subsequent calls to  SendTaskHeartbeat ,  SendTaskSuccess or  SendTaskFailure in order to report the progress or completion of the task.

input (string) --
The string that contains the JSON input data for the task.







Exceptions

SFN.Client.exceptions.ActivityDoesNotExist
SFN.Client.exceptions.ActivityWorkerLimitExceeded
SFN.Client.exceptions.InvalidArn


    :return: {
        'taskToken': 'string',
        'input': 'string'
    }
    
    
    :returns: 
    SFN.Client.exceptions.ActivityDoesNotExist
    SFN.Client.exceptions.ActivityWorkerLimitExceeded
    SFN.Client.exceptions.InvalidArn
    
    """
    pass

def get_execution_history(executionArn=None, maxResults=None, reverseOrder=None, nextToken=None):
    """
    Returns the history of the specified execution as a list of events. By default, the results are returned in ascending order of the timeStamp of the events. Use the reverseOrder parameter to get the latest events first.
    If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.
    This API action is not supported by EXPRESS state machines.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_execution_history(
        executionArn='string',
        maxResults=123,
        reverseOrder=True|False,
        nextToken='string'
    )
    
    
    :type executionArn: string
    :param executionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the execution.\n

    :type maxResults: integer
    :param maxResults: The maximum number of results that are returned per call. You can use nextToken to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.\nThis is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.\n

    :type reverseOrder: boolean
    :param reverseOrder: Lists events in descending order of their timeStamp .

    :type nextToken: string
    :param nextToken: If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.

    :rtype: dict

ReturnsResponse Syntax
{
    'events': [
        {
            'timestamp': datetime(2015, 1, 1),
            'type': 'ActivityFailed'|'ActivityScheduled'|'ActivityScheduleFailed'|'ActivityStarted'|'ActivitySucceeded'|'ActivityTimedOut'|'ChoiceStateEntered'|'ChoiceStateExited'|'ExecutionAborted'|'ExecutionFailed'|'ExecutionStarted'|'ExecutionSucceeded'|'ExecutionTimedOut'|'FailStateEntered'|'LambdaFunctionFailed'|'LambdaFunctionScheduled'|'LambdaFunctionScheduleFailed'|'LambdaFunctionStarted'|'LambdaFunctionStartFailed'|'LambdaFunctionSucceeded'|'LambdaFunctionTimedOut'|'MapIterationAborted'|'MapIterationFailed'|'MapIterationStarted'|'MapIterationSucceeded'|'MapStateAborted'|'MapStateEntered'|'MapStateExited'|'MapStateFailed'|'MapStateStarted'|'MapStateSucceeded'|'ParallelStateAborted'|'ParallelStateEntered'|'ParallelStateExited'|'ParallelStateFailed'|'ParallelStateStarted'|'ParallelStateSucceeded'|'PassStateEntered'|'PassStateExited'|'SucceedStateEntered'|'SucceedStateExited'|'TaskFailed'|'TaskScheduled'|'TaskStarted'|'TaskStartFailed'|'TaskStateAborted'|'TaskStateEntered'|'TaskStateExited'|'TaskSubmitFailed'|'TaskSubmitted'|'TaskSucceeded'|'TaskTimedOut'|'WaitStateAborted'|'WaitStateEntered'|'WaitStateExited',
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
            'taskFailedEventDetails': {
                'resourceType': 'string',
                'resource': 'string',
                'error': 'string',
                'cause': 'string'
            },
            'taskScheduledEventDetails': {
                'resourceType': 'string',
                'resource': 'string',
                'region': 'string',
                'parameters': 'string',
                'timeoutInSeconds': 123
            },
            'taskStartFailedEventDetails': {
                'resourceType': 'string',
                'resource': 'string',
                'error': 'string',
                'cause': 'string'
            },
            'taskStartedEventDetails': {
                'resourceType': 'string',
                'resource': 'string'
            },
            'taskSubmitFailedEventDetails': {
                'resourceType': 'string',
                'resource': 'string',
                'error': 'string',
                'cause': 'string'
            },
            'taskSubmittedEventDetails': {
                'resourceType': 'string',
                'resource': 'string',
                'output': 'string'
            },
            'taskSucceededEventDetails': {
                'resourceType': 'string',
                'resource': 'string',
                'output': 'string'
            },
            'taskTimedOutEventDetails': {
                'resourceType': 'string',
                'resource': 'string',
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
            'mapStateStartedEventDetails': {
                'length': 123
            },
            'mapIterationStartedEventDetails': {
                'name': 'string',
                'index': 123
            },
            'mapIterationSucceededEventDetails': {
                'name': 'string',
                'index': 123
            },
            'mapIterationFailedEventDetails': {
                'name': 'string',
                'index': 123
            },
            'mapIterationAbortedEventDetails': {
                'name': 'string',
                'index': 123
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


Response Structure

(dict) --

events (list) --
The list of events that occurred in the execution.

(dict) --
Contains details about the events of an execution.

timestamp (datetime) --
The date and time the event occurred.

type (string) --
The type of the event.

id (integer) --
The id of the event. Events are numbered sequentially, starting at one.

previousEventId (integer) --
The id of the previous event.

activityFailedEventDetails (dict) --
Contains details about an activity that failed during an execution.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



activityScheduleFailedEventDetails (dict) --
Contains details about an activity schedule event that failed during an execution.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



activityScheduledEventDetails (dict) --
Contains details about an activity scheduled during an execution.

resource (string) --
The Amazon Resource Name (ARN) of the scheduled activity.

input (string) --
The JSON data input to the activity task.

timeoutInSeconds (integer) --
The maximum allowed duration of the activity task.

heartbeatInSeconds (integer) --
The maximum allowed duration between two heartbeats for the activity task.



activityStartedEventDetails (dict) --
Contains details about the start of an activity during an execution.

workerName (string) --
The name of the worker that the task is assigned to. These names are provided by the workers when calling  GetActivityTask .



activitySucceededEventDetails (dict) --
Contains details about an activity that successfully terminated during an execution.

output (string) --
The JSON data output by the activity task.



activityTimedOutEventDetails (dict) --
Contains details about an activity timeout that occurred during an execution.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the timeout.



taskFailedEventDetails (dict) --
Contains details about the failure of a task.

resourceType (string) --
The action of the resource called by a task state.

resource (string) --
The service name of the resource in a task state.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



taskScheduledEventDetails (dict) --
Contains details about a task that was scheduled.

resourceType (string) --
The action of the resource called by a task state.

resource (string) --
The service name of the resource in a task state.

region (string) --
The region of the scheduled task

parameters (string) --
The JSON data passed to the resource referenced in a task state.

timeoutInSeconds (integer) --
The maximum allowed duration of the task.



taskStartFailedEventDetails (dict) --
Contains details about a task that failed to start.

resourceType (string) --
The action of the resource called by a task state.

resource (string) --
The service name of the resource in a task state.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



taskStartedEventDetails (dict) --
Contains details about a task that was started.

resourceType (string) --
The action of the resource called by a task state.

resource (string) --
The service name of the resource in a task state.



taskSubmitFailedEventDetails (dict) --
Contains details about a task that where the submit failed.

resourceType (string) --
The action of the resource called by a task state.

resource (string) --
The service name of the resource in a task state.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



taskSubmittedEventDetails (dict) --
Contains details about a submitted task.

resourceType (string) --
The action of the resource called by a task state.

resource (string) --
The service name of the resource in a task state.

output (string) --
The response from a resource when a task has started.



taskSucceededEventDetails (dict) --
Contains details about a task that succeeded.

resourceType (string) --
The action of the resource called by a task state.

resource (string) --
The service name of the resource in a task state.

output (string) --
The full JSON response from a resource when a task has succeeded. This response becomes the output of the related task.



taskTimedOutEventDetails (dict) --
Contains details about a task that timed out.

resourceType (string) --
The action of the resource called by a task state.

resource (string) --
The service name of the resource in a task state.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



executionFailedEventDetails (dict) --
Contains details about an execution failure event.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



executionStartedEventDetails (dict) --
Contains details about the start of the execution.

input (string) --
The JSON data input to the execution.

roleArn (string) --
The Amazon Resource Name (ARN) of the IAM role used for executing AWS Lambda tasks.



executionSucceededEventDetails (dict) --
Contains details about the successful termination of the execution.

output (string) --
The JSON data output by the execution.



executionAbortedEventDetails (dict) --
Contains details about an abort of an execution.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



executionTimedOutEventDetails (dict) --
Contains details about the execution timeout that occurred during the execution.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the timeout.



mapStateStartedEventDetails (dict) --
Contains details about Map state that was started.

length (integer) --
The size of the array for Map state iterations.



mapIterationStartedEventDetails (dict) --
Contains details about an iteration of a Map state that was started.

name (string) --
The name of the iteration\xe2\x80\x99s parent Map state.

index (integer) --
The index of the array belonging to the Map state iteration.



mapIterationSucceededEventDetails (dict) --
Contains details about an iteration of a Map state that succeeded.

name (string) --
The name of the iteration\xe2\x80\x99s parent Map state.

index (integer) --
The index of the array belonging to the Map state iteration.



mapIterationFailedEventDetails (dict) --
Contains details about an iteration of a Map state that failed.

name (string) --
The name of the iteration\xe2\x80\x99s parent Map state.

index (integer) --
The index of the array belonging to the Map state iteration.



mapIterationAbortedEventDetails (dict) --
Contains details about an iteration of a Map state that was aborted.

name (string) --
The name of the iteration\xe2\x80\x99s parent Map state.

index (integer) --
The index of the array belonging to the Map state iteration.



lambdaFunctionFailedEventDetails (dict) --
Contains details about a lambda function that failed during an execution.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



lambdaFunctionScheduleFailedEventDetails (dict) --
Contains details about a failed lambda function schedule event that occurred during an execution.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



lambdaFunctionScheduledEventDetails (dict) --
Contains details about a lambda function scheduled during an execution.

resource (string) --
The Amazon Resource Name (ARN) of the scheduled lambda function.

input (string) --
The JSON data input to the lambda function.

timeoutInSeconds (integer) --
The maximum allowed duration of the lambda function.



lambdaFunctionStartFailedEventDetails (dict) --
Contains details about a lambda function that failed to start during an execution.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the failure.



lambdaFunctionSucceededEventDetails (dict) --
Contains details about a lambda function that terminated successfully during an execution.

output (string) --
The JSON data output by the lambda function.



lambdaFunctionTimedOutEventDetails (dict) --
Contains details about a lambda function timeout that occurred during an execution.

error (string) --
The error code of the failure.

cause (string) --
A more detailed explanation of the cause of the timeout.



stateEnteredEventDetails (dict) --
Contains details about a state entered during an execution.

name (string) --
The name of the state.

input (string) --
The string that contains the JSON input data for the state.



stateExitedEventDetails (dict) --
Contains details about an exit from a state during an execution.

name (string) --
The name of the state.
A name must not contain:

white space
brackets < > { } [ ]
wildcard characters ? *
special characters " # % \\ ^ | ~ ` $ & , ; : /
control characters (U+0000-001F , U+007F-009F )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

output (string) --
The JSON output data of the state.







nextToken (string) --
If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.







Exceptions

SFN.Client.exceptions.ExecutionDoesNotExist
SFN.Client.exceptions.InvalidArn
SFN.Client.exceptions.InvalidToken


    :return: {
        'events': [
            {
                'timestamp': datetime(2015, 1, 1),
                'type': 'ActivityFailed'|'ActivityScheduled'|'ActivityScheduleFailed'|'ActivityStarted'|'ActivitySucceeded'|'ActivityTimedOut'|'ChoiceStateEntered'|'ChoiceStateExited'|'ExecutionAborted'|'ExecutionFailed'|'ExecutionStarted'|'ExecutionSucceeded'|'ExecutionTimedOut'|'FailStateEntered'|'LambdaFunctionFailed'|'LambdaFunctionScheduled'|'LambdaFunctionScheduleFailed'|'LambdaFunctionStarted'|'LambdaFunctionStartFailed'|'LambdaFunctionSucceeded'|'LambdaFunctionTimedOut'|'MapIterationAborted'|'MapIterationFailed'|'MapIterationStarted'|'MapIterationSucceeded'|'MapStateAborted'|'MapStateEntered'|'MapStateExited'|'MapStateFailed'|'MapStateStarted'|'MapStateSucceeded'|'ParallelStateAborted'|'ParallelStateEntered'|'ParallelStateExited'|'ParallelStateFailed'|'ParallelStateStarted'|'ParallelStateSucceeded'|'PassStateEntered'|'PassStateExited'|'SucceedStateEntered'|'SucceedStateExited'|'TaskFailed'|'TaskScheduled'|'TaskStarted'|'TaskStartFailed'|'TaskStateAborted'|'TaskStateEntered'|'TaskStateExited'|'TaskSubmitFailed'|'TaskSubmitted'|'TaskSucceeded'|'TaskTimedOut'|'WaitStateAborted'|'WaitStateEntered'|'WaitStateExited',
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
                'taskFailedEventDetails': {
                    'resourceType': 'string',
                    'resource': 'string',
                    'error': 'string',
                    'cause': 'string'
                },
                'taskScheduledEventDetails': {
                    'resourceType': 'string',
                    'resource': 'string',
                    'region': 'string',
                    'parameters': 'string',
                    'timeoutInSeconds': 123
                },
                'taskStartFailedEventDetails': {
                    'resourceType': 'string',
                    'resource': 'string',
                    'error': 'string',
                    'cause': 'string'
                },
                'taskStartedEventDetails': {
                    'resourceType': 'string',
                    'resource': 'string'
                },
                'taskSubmitFailedEventDetails': {
                    'resourceType': 'string',
                    'resource': 'string',
                    'error': 'string',
                    'cause': 'string'
                },
                'taskSubmittedEventDetails': {
                    'resourceType': 'string',
                    'resource': 'string',
                    'output': 'string'
                },
                'taskSucceededEventDetails': {
                    'resourceType': 'string',
                    'resource': 'string',
                    'output': 'string'
                },
                'taskTimedOutEventDetails': {
                    'resourceType': 'string',
                    'resource': 'string',
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
                'mapStateStartedEventDetails': {
                    'length': 123
                },
                'mapIterationStartedEventDetails': {
                    'name': 'string',
                    'index': 123
                },
                'mapIterationSucceededEventDetails': {
                    'name': 'string',
                    'index': 123
                },
                'mapIterationFailedEventDetails': {
                    'name': 'string',
                    'index': 123
                },
                'mapIterationAbortedEventDetails': {
                    'name': 'string',
                    'index': 123
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
    
    
    :returns: 
    white space
    brackets < > { } [ ]
    wildcard characters ? *
    special characters " # % \\ ^ | ~ ` $ & , ; : /
    control characters (U+0000-001F , U+007F-009F )
    
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

def list_activities(maxResults=None, nextToken=None):
    """
    Lists the existing activities.
    If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_activities(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results that are returned per call. You can use nextToken to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.\nThis is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.\n

    :type nextToken: string
    :param nextToken: If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.

    :rtype: dict

ReturnsResponse Syntax
{
    'activities': [
        {
            'activityArn': 'string',
            'name': 'string',
            'creationDate': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

activities (list) --
The list of activities.

(dict) --
Contains details about an activity.

activityArn (string) --
The Amazon Resource Name (ARN) that identifies the activity.

name (string) --
The name of the activity.
A name must not contain:

white space
brackets < > { } [ ]
wildcard characters ? *
special characters " # % \\ ^ | ~ ` $ & , ; : /
control characters (U+0000-001F , U+007F-009F )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

creationDate (datetime) --
The date the activity is created.





nextToken (string) --
If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.







Exceptions

SFN.Client.exceptions.InvalidToken


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
    
    
    :returns: 
    white space
    brackets < > { } [ ]
    wildcard characters ? *
    special characters " # % \\ ^ | ~ ` $ & , ; : /
    control characters (U+0000-001F , U+007F-009F )
    
    """
    pass

def list_executions(stateMachineArn=None, statusFilter=None, maxResults=None, nextToken=None):
    """
    Lists the executions of a state machine that meet the filtering criteria. Results are sorted by time, with the most recent execution first.
    If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.
    This API action is not supported by EXPRESS state machines.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_executions(
        stateMachineArn='string',
        statusFilter='RUNNING'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'ABORTED',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type stateMachineArn: string
    :param stateMachineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the state machine whose executions is listed.\n

    :type statusFilter: string
    :param statusFilter: If specified, only list the executions whose current execution status matches the given filter.

    :type maxResults: integer
    :param maxResults: The maximum number of results that are returned per call. You can use nextToken to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.\nThis is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.\n

    :type nextToken: string
    :param nextToken: If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

executions (list) --
The list of matching executions.

(dict) --
Contains details about an execution.

executionArn (string) --
The Amazon Resource Name (ARN) that id entifies the execution.

stateMachineArn (string) --
The Amazon Resource Name (ARN) of the executed state machine.

name (string) --
The name of the execution.
A name must not contain:

white space
brackets < > { } [ ]
wildcard characters ? *
special characters " # % \\ ^ | ~ ` $ & , ; : /
control characters (U+0000-001F , U+007F-009F )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

status (string) --
The current status of the execution.

startDate (datetime) --
The date the execution started.

stopDate (datetime) --
If the execution already ended, the date the execution stopped.





nextToken (string) --
If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.







Exceptions

SFN.Client.exceptions.InvalidArn
SFN.Client.exceptions.InvalidToken
SFN.Client.exceptions.StateMachineDoesNotExist
SFN.Client.exceptions.StateMachineTypeNotSupported


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
    
    
    :returns: 
    white space
    brackets < > { } [ ]
    wildcard characters ? *
    special characters " # % \\ ^ | ~ ` $ & , ; : /
    control characters (U+0000-001F , U+007F-009F )
    
    """
    pass

def list_state_machines(maxResults=None, nextToken=None):
    """
    Lists the existing state machines.
    If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_state_machines(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results that are returned per call. You can use nextToken to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.\nThis is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.\n

    :type nextToken: string
    :param nextToken: If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.

    :rtype: dict

ReturnsResponse Syntax
{
    'stateMachines': [
        {
            'stateMachineArn': 'string',
            'name': 'string',
            'type': 'STANDARD'|'EXPRESS',
            'creationDate': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

stateMachines (list) --

(dict) --
Contains details about the state machine.

stateMachineArn (string) --
The Amazon Resource Name (ARN) that identifies the state machine.

name (string) --
The name of the state machine.
A name must not contain:

white space
brackets < > { } [ ]
wildcard characters ? *
special characters " # % \\ ^ | ~ ` $ & , ; : /
control characters (U+0000-001F , U+007F-009F )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

type (string) --

creationDate (datetime) --
The date the state machine is created.





nextToken (string) --
If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.







Exceptions

SFN.Client.exceptions.InvalidToken


    :return: {
        'stateMachines': [
            {
                'stateMachineArn': 'string',
                'name': 'string',
                'type': 'STANDARD'|'EXPRESS',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    white space
    brackets < > { } [ ]
    wildcard characters ? *
    special characters " # % \\ ^ | ~ ` $ & , ; : /
    control characters (U+0000-001F , U+007F-009F )
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    List tags for a given resource.
    Tags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the Step Functions state machine or activity.\n

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
tags (list) --An array of tags associated with the resource.

(dict) --Tags are key-value pairs that can be associated with Step Functions state machines and activities.
An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide , and Controlling Access Using IAM Tags .
Tags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .

key (string) --The key of a tag.

value (string) --The value of a tag.










Exceptions

SFN.Client.exceptions.InvalidArn
SFN.Client.exceptions.ResourceNotFound


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

def send_task_failure(taskToken=None, error=None, cause=None):
    """
    Used by activity workers and task states using the callback pattern to report that the task identified by the taskToken failed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_task_failure(
        taskToken='string',
        error='string',
        cause='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]\nThe token that represents this task. Task tokens are generated by Step Functions when tasks are assigned to a worker, or in the context object when a workflow enters a task state. See GetActivityTaskOutput$taskToken .\n

    :type error: string
    :param error: The error code of the failure.

    :type cause: string
    :param cause: A more detailed explanation of the cause of the failure.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SFN.Client.exceptions.TaskDoesNotExist
SFN.Client.exceptions.InvalidToken
SFN.Client.exceptions.TaskTimedOut


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def send_task_heartbeat(taskToken=None):
    """
    Used by activity workers and task states using the callback pattern to report to Step Functions that the task represented by the specified taskToken is still making progress. This action resets the Heartbeat clock. The Heartbeat threshold is specified in the state machine\'s Amazon States Language definition (HeartbeatSeconds ). This action does not in itself create an event in the execution history. However, if the task times out, the execution history contains an ActivityTimedOut entry for activities, or a TaskTimedOut entry for for tasks using the job run or callback pattern.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_task_heartbeat(
        taskToken='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]\nThe token that represents this task. Task tokens are generated by Step Functions when tasks are assigned to a worker, or in the context object when a workflow enters a task state. See GetActivityTaskOutput$taskToken .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SFN.Client.exceptions.TaskDoesNotExist
SFN.Client.exceptions.InvalidToken
SFN.Client.exceptions.TaskTimedOut


    :return: {}
    
    
    :returns: 
    SFN.Client.exceptions.TaskDoesNotExist
    SFN.Client.exceptions.InvalidToken
    SFN.Client.exceptions.TaskTimedOut
    
    """
    pass

def send_task_success(taskToken=None, output=None):
    """
    Used by activity workers and task states using the callback pattern to report that the task identified by the taskToken completed successfully.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_task_success(
        taskToken='string',
        output='string'
    )
    
    
    :type taskToken: string
    :param taskToken: [REQUIRED]\nThe token that represents this task. Task tokens are generated by Step Functions when tasks are assigned to a worker, or in the context object when a workflow enters a task state. See GetActivityTaskOutput$taskToken .\n

    :type output: string
    :param output: [REQUIRED]\nThe JSON output of the task.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SFN.Client.exceptions.TaskDoesNotExist
SFN.Client.exceptions.InvalidOutput
SFN.Client.exceptions.InvalidToken
SFN.Client.exceptions.TaskTimedOut


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_execution(stateMachineArn=None, name=None, input=None):
    """
    Starts a state machine execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_execution(
        stateMachineArn='string',
        name='string',
        input='string'
    )
    
    
    :type stateMachineArn: string
    :param stateMachineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the state machine to execute.\n

    :type name: string
    :param name: The name of the execution. This name must be unique for your AWS account, region, and state machine for 90 days. For more information, see Limits Related to State Machine Executions in the AWS Step Functions Developer Guide .\nA name must not contain:\n\nwhite space\nbrackets < > { } [ ]\nwildcard characters ? *\nspecial characters ' # % \\ ^ | ~ ` $ & , ; : /\ncontrol characters (U+0000-001F , U+007F-009F )\n\nTo enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.\n

    :type input: string
    :param input: The string that contains the JSON input data for the execution, for example:\n\n'input': '{\\'first_name\\' : \\'test\\'}'\n\nNote\nIf you don\'t include any JSON input data, you still must include the two braces, for example: 'input': '{}'\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'executionArn': 'string',
    'startDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

executionArn (string) --
The Amazon Resource Name (ARN) that id entifies the execution.

startDate (datetime) --
The date the execution is started.







Exceptions

SFN.Client.exceptions.ExecutionLimitExceeded
SFN.Client.exceptions.ExecutionAlreadyExists
SFN.Client.exceptions.InvalidArn
SFN.Client.exceptions.InvalidExecutionInput
SFN.Client.exceptions.InvalidName
SFN.Client.exceptions.StateMachineDoesNotExist
SFN.Client.exceptions.StateMachineDeleting


    :return: {
        'executionArn': 'string',
        'startDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    SFN.Client.exceptions.ExecutionLimitExceeded
    SFN.Client.exceptions.ExecutionAlreadyExists
    SFN.Client.exceptions.InvalidArn
    SFN.Client.exceptions.InvalidExecutionInput
    SFN.Client.exceptions.InvalidName
    SFN.Client.exceptions.StateMachineDoesNotExist
    SFN.Client.exceptions.StateMachineDeleting
    
    """
    pass

def stop_execution(executionArn=None, error=None, cause=None):
    """
    Stops an execution.
    This API action is not supported by EXPRESS state machines.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_execution(
        executionArn='string',
        error='string',
        cause='string'
    )
    
    
    :type executionArn: string
    :param executionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the execution to stop.\n

    :type error: string
    :param error: The error code of the failure.

    :type cause: string
    :param cause: A more detailed explanation of the cause of the failure.

    :rtype: dict

ReturnsResponse Syntax
{
    'stopDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

stopDate (datetime) --
The date the execution is stopped.







Exceptions

SFN.Client.exceptions.ExecutionDoesNotExist
SFN.Client.exceptions.InvalidArn


    :return: {
        'stopDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    SFN.Client.exceptions.ExecutionDoesNotExist
    SFN.Client.exceptions.InvalidArn
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Add a tag to a Step Functions resource.
    An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide , and Controlling Access Using IAM Tags .
    Tags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .
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
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the Step Functions state machine or activity.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe list of tags to add to a resource.\nTags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .\n\n(dict) --Tags are key-value pairs that can be associated with Step Functions state machines and activities.\nAn array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide , and Controlling Access Using IAM Tags .\nTags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .\n\nkey (string) --The key of a tag.\n\nvalue (string) --The value of a tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SFN.Client.exceptions.InvalidArn
SFN.Client.exceptions.ResourceNotFound
SFN.Client.exceptions.TooManyTags


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Remove a tag from a Step Functions resource
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the Step Functions state machine or activity.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe list of tags to remove from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SFN.Client.exceptions.InvalidArn
SFN.Client.exceptions.ResourceNotFound


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_state_machine(stateMachineArn=None, definition=None, roleArn=None, loggingConfiguration=None):
    """
    Updates an existing state machine by modifying its definition , roleArn , or loggingConfiguration . Running executions will continue to use the previous definition and roleArn . You must include at least one of definition or roleArn or you will receive a MissingRequiredParameter error.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_state_machine(
        stateMachineArn='string',
        definition='string',
        roleArn='string',
        loggingConfiguration={
            'level': 'ALL'|'ERROR'|'FATAL'|'OFF',
            'includeExecutionData': True|False,
            'destinations': [
                {
                    'cloudWatchLogsLogGroup': {
                        'logGroupArn': 'string'
                    }
                },
            ]
        }
    )
    
    
    :type stateMachineArn: string
    :param stateMachineArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the state machine.\n

    :type definition: string
    :param definition: The Amazon States Language definition of the state machine. See Amazon States Language .

    :type roleArn: string
    :param roleArn: The Amazon Resource Name (ARN) of the IAM role of the state machine.

    :type loggingConfiguration: dict
    :param loggingConfiguration: The LoggingConfiguration data type is used to set CloudWatch Logs options.\n\nlevel (string) --Defines which category of execution history events are logged.\n\nincludeExecutionData (boolean) --Determines whether execution data is included in your log. When set to FALSE , data is excluded.\n\ndestinations (list) --An array of objects that describes where your execution history events will be logged. Limited to size 1. Required, if your log level is not set to OFF .\n\n(dict) --\ncloudWatchLogsLogGroup (dict) --An object describing a CloudWatch log group. For more information, see AWS::Logs::LogGroup in the AWS CloudFormation User Guide.\n\nlogGroupArn (string) --The ARN of the the CloudWatch log group to which you want your logs emitted to. The ARN must end with :*\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'updateDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

updateDate (datetime) --
The date and time the state machine was updated.







Exceptions

SFN.Client.exceptions.InvalidArn
SFN.Client.exceptions.InvalidDefinition
SFN.Client.exceptions.InvalidLoggingConfiguration
SFN.Client.exceptions.MissingRequiredParameter
SFN.Client.exceptions.StateMachineDeleting
SFN.Client.exceptions.StateMachineDoesNotExist


    :return: {
        'updateDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    SFN.Client.exceptions.InvalidArn
    SFN.Client.exceptions.InvalidDefinition
    SFN.Client.exceptions.InvalidLoggingConfiguration
    SFN.Client.exceptions.MissingRequiredParameter
    SFN.Client.exceptions.StateMachineDeleting
    SFN.Client.exceptions.StateMachineDoesNotExist
    
    """
    pass

