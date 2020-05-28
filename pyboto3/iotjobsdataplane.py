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

def describe_job_execution(jobId=None, thingName=None, includeJobDocument=None, executionNumber=None):
    """
    Gets details of a job execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_job_execution(
        jobId='string',
        thingName='string',
        includeJobDocument=True|False,
        executionNumber=123
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier assigned to this job when it was created.\n

    :type thingName: string
    :param thingName: [REQUIRED]\nThe thing name associated with the device the job execution is running on.\n

    :type includeJobDocument: boolean
    :param includeJobDocument: Optional. When set to true, the response contains the job document. The default is false.

    :type executionNumber: integer
    :param executionNumber: Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'execution': {
        'jobId': 'string',
        'thingName': 'string',
        'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
        'statusDetails': {
            'string': 'string'
        },
        'queuedAt': 123,
        'startedAt': 123,
        'lastUpdatedAt': 123,
        'approximateSecondsBeforeTimedOut': 123,
        'versionNumber': 123,
        'executionNumber': 123,
        'jobDocument': 'string'
    }
}


Response Structure

(dict) --

execution (dict) --
Contains data about a job execution.

jobId (string) --
The unique identifier you assigned to this job when it was created.

thingName (string) --
The name of the thing that is executing the job.

status (string) --
The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED", "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

statusDetails (dict) --
A collection of name/value pairs that describe the status of the job execution.

(string) --
(string) --




queuedAt (integer) --
The time, in milliseconds since the epoch, when the job execution was enqueued.

startedAt (integer) --
The time, in milliseconds since the epoch, when the job execution was started.

lastUpdatedAt (integer) --
The time, in milliseconds since the epoch, when the job execution was last updated.

approximateSecondsBeforeTimedOut (integer) --
The estimated number of seconds that remain before the job execution status will be changed to TIMED_OUT .

versionNumber (integer) --
The version of the job execution. Job execution versions are incremented each time they are updated by a device.

executionNumber (integer) --
A number that identifies a particular job execution on a particular device. It can be used later in commands that return or update job execution information.

jobDocument (string) --
The content of the job document.









Exceptions

IoTJobsDataPlane.Client.exceptions.InvalidRequestException
IoTJobsDataPlane.Client.exceptions.ResourceNotFoundException
IoTJobsDataPlane.Client.exceptions.ThrottlingException
IoTJobsDataPlane.Client.exceptions.ServiceUnavailableException
IoTJobsDataPlane.Client.exceptions.CertificateValidationException
IoTJobsDataPlane.Client.exceptions.TerminalStateException


    :return: {
        'execution': {
            'jobId': 'string',
            'thingName': 'string',
            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
            'statusDetails': {
                'string': 'string'
            },
            'queuedAt': 123,
            'startedAt': 123,
            'lastUpdatedAt': 123,
            'approximateSecondsBeforeTimedOut': 123,
            'versionNumber': 123,
            'executionNumber': 123,
            'jobDocument': 'string'
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

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_pending_job_executions(thingName=None):
    """
    Gets the list of all jobs for a thing that are not in a terminal status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_pending_job_executions(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing that is executing the job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'inProgressJobs': [
        {
            'jobId': 'string',
            'queuedAt': 123,
            'startedAt': 123,
            'lastUpdatedAt': 123,
            'versionNumber': 123,
            'executionNumber': 123
        },
    ],
    'queuedJobs': [
        {
            'jobId': 'string',
            'queuedAt': 123,
            'startedAt': 123,
            'lastUpdatedAt': 123,
            'versionNumber': 123,
            'executionNumber': 123
        },
    ]
}


Response Structure

(dict) --
inProgressJobs (list) --A list of JobExecutionSummary objects with status IN_PROGRESS.

(dict) --Contains a subset of information about a job execution.

jobId (string) --The unique identifier you assigned to this job when it was created.

queuedAt (integer) --The time, in milliseconds since the epoch, when the job execution was enqueued.

startedAt (integer) --The time, in milliseconds since the epoch, when the job execution started.

lastUpdatedAt (integer) --The time, in milliseconds since the epoch, when the job execution was last updated.

versionNumber (integer) --The version of the job execution. Job execution versions are incremented each time AWS IoT Jobs receives an update from a device.

executionNumber (integer) --A number that identifies a particular job execution on a particular device.





queuedJobs (list) --A list of JobExecutionSummary objects with status QUEUED.

(dict) --Contains a subset of information about a job execution.

jobId (string) --The unique identifier you assigned to this job when it was created.

queuedAt (integer) --The time, in milliseconds since the epoch, when the job execution was enqueued.

startedAt (integer) --The time, in milliseconds since the epoch, when the job execution started.

lastUpdatedAt (integer) --The time, in milliseconds since the epoch, when the job execution was last updated.

versionNumber (integer) --The version of the job execution. Job execution versions are incremented each time AWS IoT Jobs receives an update from a device.

executionNumber (integer) --A number that identifies a particular job execution on a particular device.










Exceptions

IoTJobsDataPlane.Client.exceptions.InvalidRequestException
IoTJobsDataPlane.Client.exceptions.ResourceNotFoundException
IoTJobsDataPlane.Client.exceptions.ThrottlingException
IoTJobsDataPlane.Client.exceptions.ServiceUnavailableException
IoTJobsDataPlane.Client.exceptions.CertificateValidationException


    :return: {
        'inProgressJobs': [
            {
                'jobId': 'string',
                'queuedAt': 123,
                'startedAt': 123,
                'lastUpdatedAt': 123,
                'versionNumber': 123,
                'executionNumber': 123
            },
        ],
        'queuedJobs': [
            {
                'jobId': 'string',
                'queuedAt': 123,
                'startedAt': 123,
                'lastUpdatedAt': 123,
                'versionNumber': 123,
                'executionNumber': 123
            },
        ]
    }
    
    
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

def start_next_pending_job_execution(thingName=None, statusDetails=None, stepTimeoutInMinutes=None):
    """
    Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution for a thing.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_next_pending_job_execution(
        thingName='string',
        statusDetails={
            'string': 'string'
        },
        stepTimeoutInMinutes=123
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing associated with the device.\n

    :type statusDetails: dict
    :param statusDetails: A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.\n\n(string) --\n(string) --\n\n\n\n

    :type stepTimeoutInMinutes: integer
    :param stepTimeoutInMinutes: Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by calling UpdateJobExecution , setting the status to IN_PROGRESS and specifying a new timeout value in field stepTimeoutInMinutes ) the job execution status will be automatically set to TIMED_OUT . Note that setting this timeout has no effect on that job execution timeout which may have been specified when the job was created (CreateJob using field timeoutConfig ).

    :rtype: dict

ReturnsResponse Syntax
{
    'execution': {
        'jobId': 'string',
        'thingName': 'string',
        'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
        'statusDetails': {
            'string': 'string'
        },
        'queuedAt': 123,
        'startedAt': 123,
        'lastUpdatedAt': 123,
        'approximateSecondsBeforeTimedOut': 123,
        'versionNumber': 123,
        'executionNumber': 123,
        'jobDocument': 'string'
    }
}


Response Structure

(dict) --

execution (dict) --
A JobExecution object.

jobId (string) --
The unique identifier you assigned to this job when it was created.

thingName (string) --
The name of the thing that is executing the job.

status (string) --
The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED", "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

statusDetails (dict) --
A collection of name/value pairs that describe the status of the job execution.

(string) --
(string) --




queuedAt (integer) --
The time, in milliseconds since the epoch, when the job execution was enqueued.

startedAt (integer) --
The time, in milliseconds since the epoch, when the job execution was started.

lastUpdatedAt (integer) --
The time, in milliseconds since the epoch, when the job execution was last updated.

approximateSecondsBeforeTimedOut (integer) --
The estimated number of seconds that remain before the job execution status will be changed to TIMED_OUT .

versionNumber (integer) --
The version of the job execution. Job execution versions are incremented each time they are updated by a device.

executionNumber (integer) --
A number that identifies a particular job execution on a particular device. It can be used later in commands that return or update job execution information.

jobDocument (string) --
The content of the job document.









Exceptions

IoTJobsDataPlane.Client.exceptions.InvalidRequestException
IoTJobsDataPlane.Client.exceptions.ResourceNotFoundException
IoTJobsDataPlane.Client.exceptions.ThrottlingException
IoTJobsDataPlane.Client.exceptions.ServiceUnavailableException
IoTJobsDataPlane.Client.exceptions.CertificateValidationException


    :return: {
        'execution': {
            'jobId': 'string',
            'thingName': 'string',
            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
            'statusDetails': {
                'string': 'string'
            },
            'queuedAt': 123,
            'startedAt': 123,
            'lastUpdatedAt': 123,
            'approximateSecondsBeforeTimedOut': 123,
            'versionNumber': 123,
            'executionNumber': 123,
            'jobDocument': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_job_execution(jobId=None, thingName=None, status=None, statusDetails=None, stepTimeoutInMinutes=None, expectedVersion=None, includeJobExecutionState=None, includeJobDocument=None, executionNumber=None):
    """
    Updates the status of a job execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_job_execution(
        jobId='string',
        thingName='string',
        status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
        statusDetails={
            'string': 'string'
        },
        stepTimeoutInMinutes=123,
        expectedVersion=123,
        includeJobExecutionState=True|False,
        includeJobDocument=True|False,
        executionNumber=123
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier assigned to this job when it was created.\n

    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing associated with the device.\n

    :type status: string
    :param status: [REQUIRED]\nThe new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update.\n

    :type statusDetails: dict
    :param statusDetails: Optional. A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.\n\n(string) --\n(string) --\n\n\n\n

    :type stepTimeoutInMinutes: integer
    :param stepTimeoutInMinutes: Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by again calling UpdateJobExecution , setting the status to IN_PROGRESS and specifying a new timeout value in this field) the job execution status will be automatically set to TIMED_OUT . Note that setting or resetting this timeout has no effect on that job execution timeout which may have been specified when the job was created (CreateJob using field timeoutConfig ).

    :type expectedVersion: integer
    :param expectedVersion: Optional. The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)

    :type includeJobExecutionState: boolean
    :param includeJobExecutionState: Optional. When included and set to true, the response contains the JobExecutionState data. The default is false.

    :type includeJobDocument: boolean
    :param includeJobDocument: Optional. When set to true, the response contains the job document. The default is false.

    :type executionNumber: integer
    :param executionNumber: Optional. A number that identifies a particular job execution on a particular device.

    :rtype: dict

ReturnsResponse Syntax
{
    'executionState': {
        'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
        'statusDetails': {
            'string': 'string'
        },
        'versionNumber': 123
    },
    'jobDocument': 'string'
}


Response Structure

(dict) --

executionState (dict) --
A JobExecutionState object.

status (string) --
The status of the job execution. Can be one of: "QUEUED", "IN_PROGRESS", "FAILED", "SUCCESS", "CANCELED", "REJECTED", or "REMOVED".

statusDetails (dict) --
A collection of name/value pairs that describe the status of the job execution.

(string) --
(string) --




versionNumber (integer) --
The version of the job execution. Job execution versions are incremented each time they are updated by a device.



jobDocument (string) --
The contents of the Job Documents.







Exceptions

IoTJobsDataPlane.Client.exceptions.InvalidRequestException
IoTJobsDataPlane.Client.exceptions.ResourceNotFoundException
IoTJobsDataPlane.Client.exceptions.ThrottlingException
IoTJobsDataPlane.Client.exceptions.ServiceUnavailableException
IoTJobsDataPlane.Client.exceptions.CertificateValidationException
IoTJobsDataPlane.Client.exceptions.InvalidStateTransitionException


    :return: {
        'executionState': {
            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
            'statusDetails': {
                'string': 'string'
            },
            'versionNumber': 123
        },
        'jobDocument': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

