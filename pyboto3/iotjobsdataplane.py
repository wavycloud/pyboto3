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

def describe_job_execution(jobId=None, thingName=None, includeJobDocument=None, executionNumber=None):
    """
    Gets details of a job execution.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_job_execution(
        jobId='string',
        thingName='string',
        includeJobDocument=True|False,
        executionNumber=123
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique identifier assigned to this job when it was created.
            

    :type thingName: string
    :param thingName: [REQUIRED]
            The thing name associated with the device the job execution is running on.
            

    :type includeJobDocument: boolean
    :param includeJobDocument: Optional. When set to true, the response contains the job document. The default is false.

    :type executionNumber: integer
    :param executionNumber: Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned.

    :rtype: dict
    :return: {
        'execution': {
            'jobId': 'string',
            'thingName': 'string',
            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
            'statusDetails': {
                'string': 'string'
            },
            'queuedAt': 123,
            'startedAt': 123,
            'lastUpdatedAt': 123,
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

def get_pending_job_executions(thingName=None):
    """
    Gets the list of all jobs for a thing that are not in a terminal status.
    See also: AWS API Documentation
    
    
    :example: response = client.get_pending_job_executions(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing that is executing the job.
            

    :rtype: dict
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

def get_waiter():
    """
    
    """
    pass

def start_next_pending_job_execution(thingName=None, statusDetails=None):
    """
    Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution for a thing.
    See also: AWS API Documentation
    
    
    :example: response = client.start_next_pending_job_execution(
        thingName='string',
        statusDetails={
            'string': 'string'
        }
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing associated with the device.
            

    :type statusDetails: dict
    :param statusDetails: A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'execution': {
            'jobId': 'string',
            'thingName': 'string',
            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
            'statusDetails': {
                'string': 'string'
            },
            'queuedAt': 123,
            'startedAt': 123,
            'lastUpdatedAt': 123,
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

def update_job_execution(jobId=None, thingName=None, status=None, statusDetails=None, expectedVersion=None, includeJobExecutionState=None, includeJobDocument=None, executionNumber=None):
    """
    Updates the status of a job execution.
    See also: AWS API Documentation
    
    
    :example: response = client.update_job_execution(
        jobId='string',
        thingName='string',
        status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
        statusDetails={
            'string': 'string'
        },
        expectedVersion=123,
        includeJobExecutionState=True|False,
        includeJobDocument=True|False,
        executionNumber=123
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            The unique identifier assigned to this job when it was created.
            

    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing associated with the device.
            

    :type status: string
    :param status: [REQUIRED]
            The new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update.
            

    :type statusDetails: dict
    :param statusDetails: Optional. A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.
            (string) --
            (string) --
            

    :type expectedVersion: integer
    :param expectedVersion: Optional. The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)

    :type includeJobExecutionState: boolean
    :param includeJobExecutionState: Optional. When included and set to true, the response contains the JobExecutionState data. The default is false.

    :type includeJobDocument: boolean
    :param includeJobDocument: Optional. When set to true, the response contains the job document. The default is false.

    :type executionNumber: integer
    :param executionNumber: Optional. A number that identifies a particular job execution on a particular device.

    :rtype: dict
    :return: {
        'executionState': {
            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
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

