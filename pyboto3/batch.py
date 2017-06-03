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

def cancel_job(jobId=None, reason=None):
    """
    Cancels jobs in an AWS Batch job queue. Jobs that are in the SUBMITTED , PENDING , or RUNNABLE state are cancelled. Jobs that have progressed to STARTING or RUNNING are not cancelled (but the API operation still succeeds, even if no jobs are cancelled); these jobs must be terminated with the  TerminateJob operation.
    See also: AWS API Documentation
    
    Examples
    This example cancels a job with the specified job ID.
    Expected Output:
    
    :example: response = client.cancel_job(
        jobId='string',
        reason='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            A list of up to 100 job IDs to cancel.
            

    :type reason: string
    :param reason: [REQUIRED]
            A message to attach to the job that explains the reason for cancelling it. This message is returned by future DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_compute_environment(computeEnvironmentName=None, type=None, state=None, computeResources=None, serviceRole=None):
    """
    Creates an AWS Batch compute environment. You can create MANAGED or UNMANAGED compute environments.
    In a managed compute environment, AWS Batch manages the compute resources within the environment, based on the compute resources that you specify. Instances launched into a managed compute environment use the latest Amazon ECS-optimized AMI. You can choose to use Amazon EC2 On-Demand instances in your managed compute environment, or you can use Amazon EC2 Spot instances that only launch when the Spot bid price is below a specified percentage of the On-Demand price.
    In an unmanaged compute environment, you can manage your own compute resources. This provides more compute resource configuration options, such as using a custom AMI, but you must ensure that your AMI meets the Amazon ECS container instance AMI specification. For more information, see Container Instance AMIs in the Amazon EC2 Container Service Developer Guide . After you have created your unmanaged compute environment, you can use the  DescribeComputeEnvironments operation to find the Amazon ECS cluster that is associated with it and then manually launch your container instances into that Amazon ECS cluster. For more information, see Launching an Amazon ECS Container Instance in the Amazon EC2 Container Service Developer Guide .
    See also: AWS API Documentation
    
    Examples
    This example creates a managed compute environment with specific C4 instance types that are launched on demand. The compute environment is called C4OnDemand.
    Expected Output:
    This example creates a managed compute environment with the M4 instance type that is launched when the Spot bid price is at or below 20% of the On-Demand price for the instance type. The compute environment is called M4Spot.
    Expected Output:
    
    :example: response = client.create_compute_environment(
        computeEnvironmentName='string',
        type='MANAGED'|'UNMANAGED',
        state='ENABLED'|'DISABLED',
        computeResources={
            'type': 'EC2'|'SPOT',
            'minvCpus': 123,
            'maxvCpus': 123,
            'desiredvCpus': 123,
            'instanceTypes': [
                'string',
            ],
            'imageId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ],
            'ec2KeyPair': 'string',
            'instanceRole': 'string',
            'tags': {
                'string': 'string'
            },
            'bidPercentage': 123,
            'spotIamFleetRole': 'string'
        },
        serviceRole='string'
    )
    
    
    :type computeEnvironmentName: string
    :param computeEnvironmentName: [REQUIRED]
            The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.
            

    :type type: string
    :param type: [REQUIRED]
            The type of the compute environment.
            

    :type state: string
    :param state: The state of the compute environment. If the state is ENABLED , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.

    :type computeResources: dict
    :param computeResources: Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments.
            type (string) -- [REQUIRED]The type of compute environment.
            minvCpus (integer) -- [REQUIRED]The minimum number of EC2 vCPUs that an environment should maintain.
            maxvCpus (integer) -- [REQUIRED]The maximum number of EC2 vCPUs that an environment can reach.
            desiredvCpus (integer) --The desired number of EC2 vCPUS in the compute environment.
            instanceTypes (list) -- [REQUIRED]The instances types that may launched.
            (string) --
            imageId (string) --The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.
            subnets (list) -- [REQUIRED]The VPC subnets into which the compute resources are launched.
            (string) --
            securityGroupIds (list) -- [REQUIRED]The EC2 security group that is associated with instances launched in the compute environment.
            (string) --
            ec2KeyPair (string) --The EC2 key pair that is used for instances launched in the compute environment.
            instanceRole (string) -- [REQUIRED]The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.
            tags (dict) --Key-value pair tags to be applied to resources that are launched in the compute environment.
            (string) --
            (string) --
            
            bidPercentage (integer) --The minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance.
            spotIamFleetRole (string) --The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment.
            

    :type serviceRole: string
    :param serviceRole: [REQUIRED]
            The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
            

    :rtype: dict
    :return: {
        'computeEnvironmentName': 'string',
        'computeEnvironmentArn': 'string'
    }
    
    
    """
    pass

def create_job_queue(jobQueueName=None, state=None, priority=None, computeEnvironmentOrder=None):
    """
    Creates an AWS Batch job queue. When you create a job queue, you associate one or more compute environments to the queue and assign an order of preference for the compute environments.
    You also set a priority to the job queue that determines the order in which the AWS Batch scheduler places jobs onto its associated compute environments. For example, if a compute environment is associated with more than one job queue, the job queue with a higher priority is given preference for scheduling jobs to that compute environment.
    See also: AWS API Documentation
    
    Examples
    This example creates a job queue called LowPriority that uses the M4Spot compute environment.
    Expected Output:
    This example creates a job queue called HighPriority that uses the C4OnDemand compute environment with an order of 1 and the M4Spot compute environment with an order of 2.
    Expected Output:
    
    :example: response = client.create_job_queue(
        jobQueueName='string',
        state='ENABLED'|'DISABLED',
        priority=123,
        computeEnvironmentOrder=[
            {
                'order': 123,
                'computeEnvironment': 'string'
            },
        ]
    )
    
    
    :type jobQueueName: string
    :param jobQueueName: [REQUIRED]
            The name of the job queue.
            

    :type state: string
    :param state: The state of the job queue. If the job queue state is ENABLED , it is able to accept jobs.

    :type priority: integer
    :param priority: [REQUIRED]
            The priority of the job queue. Job queues with a higher priority (or a lower integer value for the priority parameter) are evaluated first when associated with same compute environment. Priority is determined in ascending order, for example, a job queue with a priority value of 1 is given scheduling preference over a job queue with a priority value of 10 .
            

    :type computeEnvironmentOrder: list
    :param computeEnvironmentOrder: [REQUIRED]
            The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment should execute a given job. Compute environments must be in the VALID state before you can associate them with a job queue. You can associate up to 3 compute environments with a job queue.
            (dict) --The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.
            order (integer) -- [REQUIRED]The order of the compute environment.
            computeEnvironment (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the compute environment.
            
            

    :rtype: dict
    :return: {
        'jobQueueName': 'string',
        'jobQueueArn': 'string'
    }
    
    
    """
    pass

def delete_compute_environment(computeEnvironment=None):
    """
    Deletes an AWS Batch compute environment.
    Before you can delete a compute environment, you must set its state to DISABLED with the  UpdateComputeEnvironment API operation and disassociate it from any job queues with the  UpdateJobQueue API operation.
    See also: AWS API Documentation
    
    Examples
    This example deletes the P2OnDemand compute environment.
    Expected Output:
    
    :example: response = client.delete_compute_environment(
        computeEnvironment='string'
    )
    
    
    :type computeEnvironment: string
    :param computeEnvironment: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the compute environment to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_job_queue(jobQueue=None):
    """
    Deletes the specified job queue. You must first disable submissions for a queue with the  UpdateJobQueue operation and terminate any jobs that have not completed with the  TerminateJob .
    It is not necessary to disassociate compute environments from a queue before submitting a DeleteJobQueue request.
    See also: AWS API Documentation
    
    Examples
    This example deletes the GPGPU job queue.
    Expected Output:
    
    :example: response = client.delete_job_queue(
        jobQueue='string'
    )
    
    
    :type jobQueue: string
    :param jobQueue: [REQUIRED]
            The short name or full Amazon Resource Name (ARN) of the queue to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def deregister_job_definition(jobDefinition=None):
    """
    Deregisters an AWS Batch job definition.
    See also: AWS API Documentation
    
    Examples
    This example deregisters a job definition called sleep10.
    Expected Output:
    
    :example: response = client.deregister_job_definition(
        jobDefinition='string'
    )
    
    
    :type jobDefinition: string
    :param jobDefinition: [REQUIRED]
            The name and revision (name:revision ) or full Amazon Resource Name (ARN) of the job definition to deregister.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_compute_environments(computeEnvironments=None, maxResults=None, nextToken=None):
    """
    Describes one or more of your compute environments.
    If you are using an unmanaged compute environment, you can use the DescribeComputeEnvironment operation to determine the ecsClusterArn that you should launch your Amazon ECS container instances into.
    See also: AWS API Documentation
    
    Examples
    This example describes the P2OnDemand compute environment.
    Expected Output:
    
    :example: response = client.describe_compute_environments(
        computeEnvironments=[
            'string',
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type computeEnvironments: list
    :param computeEnvironments: A list of up to 100 compute environment names or full Amazon Resource Name (ARN) entries.
            (string) --
            

    :type maxResults: integer
    :param maxResults: The maximum number of cluster results returned by DescribeComputeEnvironments in paginated output. When this parameter is used, DescribeComputeEnvironments only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeComputeEnvironments request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeComputeEnvironments returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeComputeEnvironments request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'computeEnvironments': [
            {
                'computeEnvironmentName': 'string',
                'computeEnvironmentArn': 'string',
                'ecsClusterArn': 'string',
                'type': 'MANAGED'|'UNMANAGED',
                'state': 'ENABLED'|'DISABLED',
                'status': 'CREATING'|'UPDATING'|'DELETING'|'DELETED'|'VALID'|'INVALID',
                'statusReason': 'string',
                'computeResources': {
                    'type': 'EC2'|'SPOT',
                    'minvCpus': 123,
                    'maxvCpus': 123,
                    'desiredvCpus': 123,
                    'instanceTypes': [
                        'string',
                    ],
                    'imageId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ],
                    'ec2KeyPair': 'string',
                    'instanceRole': 'string',
                    'tags': {
                        'string': 'string'
                    },
                    'bidPercentage': 123,
                    'spotIamFleetRole': 'string'
                },
                'serviceRole': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_job_definitions(jobDefinitions=None, maxResults=None, jobDefinitionName=None, status=None, nextToken=None):
    """
    Describes a list of job definitions. You can specify a status (such as ACTIVE ) to only return job definitions that match that status.
    See also: AWS API Documentation
    
    Examples
    This example describes all of your active job definitions.
    Expected Output:
    
    :example: response = client.describe_job_definitions(
        jobDefinitions=[
            'string',
        ],
        maxResults=123,
        jobDefinitionName='string',
        status='string',
        nextToken='string'
    )
    
    
    :type jobDefinitions: list
    :param jobDefinitions: A space-separated list of up to 100 job definition names or full Amazon Resource Name (ARN) entries.
            (string) --
            

    :type maxResults: integer
    :param maxResults: The maximum number of results returned by DescribeJobDefinitions in paginated output. When this parameter is used, DescribeJobDefinitions only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeJobDefinitions request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeJobDefinitions returns up to 100 results and a nextToken value if applicable.

    :type jobDefinitionName: string
    :param jobDefinitionName: The name of the job definition to describe.

    :type status: string
    :param status: The status with which to filter job definitions.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeJobDefinitions request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'jobDefinitions': [
            {
                'jobDefinitionName': 'string',
                'jobDefinitionArn': 'string',
                'revision': 123,
                'status': 'string',
                'type': 'string',
                'parameters': {
                    'string': 'string'
                },
                'retryStrategy': {
                    'attempts': 123
                },
                'containerProperties': {
                    'image': 'string',
                    'vcpus': 123,
                    'memory': 123,
                    'command': [
                        'string',
                    ],
                    'jobRoleArn': 'string',
                    'volumes': [
                        {
                            'host': {
                                'sourcePath': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'environment': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'mountPoints': [
                        {
                            'containerPath': 'string',
                            'readOnly': True|False,
                            'sourceVolume': 'string'
                        },
                    ],
                    'readonlyRootFilesystem': True|False,
                    'privileged': True|False,
                    'ulimits': [
                        {
                            'hardLimit': 123,
                            'name': 'string',
                            'softLimit': 123
                        },
                    ],
                    'user': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_job_queues(jobQueues=None, maxResults=None, nextToken=None):
    """
    Describes one or more of your job queues.
    See also: AWS API Documentation
    
    Examples
    This example describes the HighPriority job queue.
    Expected Output:
    
    :example: response = client.describe_job_queues(
        jobQueues=[
            'string',
        ],
        maxResults=123,
        nextToken='string'
    )
    
    
    :type jobQueues: list
    :param jobQueues: A list of up to 100 queue names or full queue Amazon Resource Name (ARN) entries.
            (string) --
            

    :type maxResults: integer
    :param maxResults: The maximum number of results returned by DescribeJobQueues in paginated output. When this parameter is used, DescribeJobQueues only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeJobQueues request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeJobQueues returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeJobQueues request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'jobQueues': [
            {
                'jobQueueName': 'string',
                'jobQueueArn': 'string',
                'state': 'ENABLED'|'DISABLED',
                'status': 'CREATING'|'UPDATING'|'DELETING'|'DELETED'|'VALID'|'INVALID',
                'statusReason': 'string',
                'priority': 123,
                'computeEnvironmentOrder': [
                    {
                        'order': 123,
                        'computeEnvironment': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_jobs(jobs=None):
    """
    Describes a list of AWS Batch jobs.
    See also: AWS API Documentation
    
    Examples
    This example describes a job with the specified job ID.
    Expected Output:
    
    :example: response = client.describe_jobs(
        jobs=[
            'string',
        ]
    )
    
    
    :type jobs: list
    :param jobs: [REQUIRED]
            A space-separated list of up to 100 job IDs.
            (string) --
            

    :rtype: dict
    :return: {
        'jobs': [
            {
                'jobName': 'string',
                'jobId': 'string',
                'jobQueue': 'string',
                'status': 'SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
                'attempts': [
                    {
                        'container': {
                            'containerInstanceArn': 'string',
                            'taskArn': 'string',
                            'exitCode': 123,
                            'reason': 'string'
                        },
                        'startedAt': 123,
                        'stoppedAt': 123,
                        'statusReason': 'string'
                    },
                ],
                'statusReason': 'string',
                'createdAt': 123,
                'retryStrategy': {
                    'attempts': 123
                },
                'startedAt': 123,
                'stoppedAt': 123,
                'dependsOn': [
                    {
                        'jobId': 'string'
                    },
                ],
                'jobDefinition': 'string',
                'parameters': {
                    'string': 'string'
                },
                'container': {
                    'image': 'string',
                    'vcpus': 123,
                    'memory': 123,
                    'command': [
                        'string',
                    ],
                    'jobRoleArn': 'string',
                    'volumes': [
                        {
                            'host': {
                                'sourcePath': 'string'
                            },
                            'name': 'string'
                        },
                    ],
                    'environment': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'mountPoints': [
                        {
                            'containerPath': 'string',
                            'readOnly': True|False,
                            'sourceVolume': 'string'
                        },
                    ],
                    'readonlyRootFilesystem': True|False,
                    'ulimits': [
                        {
                            'hardLimit': 123,
                            'name': 'string',
                            'softLimit': 123
                        },
                    ],
                    'privileged': True|False,
                    'user': 'string',
                    'exitCode': 123,
                    'reason': 'string',
                    'containerInstanceArn': 'string',
                    'taskArn': 'string'
                }
            },
        ]
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

def get_waiter():
    """
    
    """
    pass

def list_jobs(jobQueue=None, jobStatus=None, maxResults=None, nextToken=None):
    """
    Returns a list of task jobs for a specified job queue. You can filter the results by job status with the jobStatus parameter.
    See also: AWS API Documentation
    
    Examples
    This example lists the running jobs in the HighPriority job queue.
    Expected Output:
    This example lists jobs in the HighPriority job queue that are in the SUBMITTED job status.
    Expected Output:
    
    :example: response = client.list_jobs(
        jobQueue='string',
        jobStatus='SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type jobQueue: string
    :param jobQueue: [REQUIRED]
            The name or full Amazon Resource Name (ARN) of the job queue with which to list jobs.
            

    :type jobStatus: string
    :param jobStatus: The job status with which to filter jobs in the specified queue.

    :type maxResults: integer
    :param maxResults: The maximum number of results returned by ListJobs in paginated output. When this parameter is used, ListJobs only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListJobs request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListJobs returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListJobs request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
            Note
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
            

    :rtype: dict
    :return: {
        'jobSummaryList': [
            {
                'jobId': 'string',
                'jobName': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def register_job_definition(jobDefinitionName=None, type=None, parameters=None, containerProperties=None, retryStrategy=None):
    """
    Registers an AWS Batch job definition.
    See also: AWS API Documentation
    
    Examples
    This example registers a job definition for a simple container job.
    Expected Output:
    
    :example: response = client.register_job_definition(
        jobDefinitionName='string',
        type='container',
        parameters={
            'string': 'string'
        },
        containerProperties={
            'image': 'string',
            'vcpus': 123,
            'memory': 123,
            'command': [
                'string',
            ],
            'jobRoleArn': 'string',
            'volumes': [
                {
                    'host': {
                        'sourcePath': 'string'
                    },
                    'name': 'string'
                },
            ],
            'environment': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'mountPoints': [
                {
                    'containerPath': 'string',
                    'readOnly': True|False,
                    'sourceVolume': 'string'
                },
            ],
            'readonlyRootFilesystem': True|False,
            'privileged': True|False,
            'ulimits': [
                {
                    'hardLimit': 123,
                    'name': 'string',
                    'softLimit': 123
                },
            ],
            'user': 'string'
        },
        retryStrategy={
            'attempts': 123
        }
    )
    
    
    :type jobDefinitionName: string
    :param jobDefinitionName: [REQUIRED]
            The name of the job definition to register.
            

    :type type: string
    :param type: [REQUIRED]
            The type of job definition.
            

    :type parameters: dict
    :param parameters: Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a SubmitJob request override any corresponding parameter defaults from the job definition.
            (string) --
            (string) --
            

    :type containerProperties: dict
    :param containerProperties: An object with various properties specific for container-based jobs. This parameter is required if the type parameter is container .
            image (string) -- [REQUIRED]The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` repository-url /image :tag `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .
            Images in Amazon ECR repositories use the full registry and repository URI (for example, 012345678910.dkr.ecr.region-name.amazonaws.com/repository-name ).
            Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
            Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
            Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).
            vcpus (integer) -- [REQUIRED]The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run . Each vCPU is equivalent to 1,024 CPU shares.
            memory (integer) -- [REQUIRED]The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run .
            command (list) --The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd .
            (string) --
            jobRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.
            volumes (list) --A list of data volumes used in a job.
            (dict) --A data volume used in a job's container properties.
            host (dict) --The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume, but the data is not guaranteed to persist after the containers associated with it stop running.
            sourcePath (string) --The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the host parameter contains a sourcePath file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the sourcePath value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
            name (string) --The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .
            
            environment (list) --The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .
            Warning
            We do not recommend using plain text environment variables for sensitive information, such as credential data.
            (dict) --A key-value pair object.
            name (string) --The name of the key value pair. For environment variables, this is the name of the environment variable.
            value (string) --The value of the key value pair. For environment variables, this is the value of the environment variable.
            
            mountPoints (list) --The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .
            (dict) --Details on a Docker volume mount point that is used in a job's container properties.
            containerPath (string) --The path on the container at which to mount the host volume.
            readOnly (boolean) --If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false .
            sourceVolume (string) --The name of the volume to mount.
            
            readonlyRootFilesystem (boolean) --When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .
            privileged (boolean) --When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .
            ulimits (list) --A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run .
            (dict) --The ulimit settings to pass to the container.
            hardLimit (integer) -- [REQUIRED]The hard limit for the ulimit type.
            name (string) -- [REQUIRED]The type of the ulimit .
            softLimit (integer) -- [REQUIRED]The soft limit for the ulimit type.
            
            user (string) --The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .
            

    :type retryStrategy: dict
    :param retryStrategy: The retry strategy to use for failed jobs that are submitted with this job definition. Any retry strategy that is specified during a SubmitJob operation overrides the retry strategy defined here.
            attempts (integer) --The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If attempts is greater than one, the job is retried if it fails until it has moved to RUNNABLE that many times.
            

    :rtype: dict
    :return: {
        'jobDefinitionName': 'string',
        'jobDefinitionArn': 'string',
        'revision': 123
    }
    
    
    """
    pass

def submit_job(jobName=None, jobQueue=None, dependsOn=None, jobDefinition=None, parameters=None, containerOverrides=None, retryStrategy=None):
    """
    Submits an AWS Batch job from a job definition. Parameters specified during  SubmitJob override parameters defined in the job definition.
    See also: AWS API Documentation
    
    Examples
    This example submits a simple container job called example to the HighPriority job queue.
    Expected Output:
    
    :example: response = client.submit_job(
        jobName='string',
        jobQueue='string',
        dependsOn=[
            {
                'jobId': 'string'
            },
        ],
        jobDefinition='string',
        parameters={
            'string': 'string'
        },
        containerOverrides={
            'vcpus': 123,
            'memory': 123,
            'command': [
                'string',
            ],
            'environment': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ]
        },
        retryStrategy={
            'attempts': 123
        }
    )
    
    
    :type jobName: string
    :param jobName: [REQUIRED]
            The name of the job. A name must be 1 to 128 characters in length.
            Pattern: ^[a-zA-Z0-9_]+$
            

    :type jobQueue: string
    :param jobQueue: [REQUIRED]
            The job queue into which the job will be submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue.
            

    :type dependsOn: list
    :param dependsOn: A list of job IDs on which this job depends. A job can depend upon a maximum of 100 jobs.
            (dict) --An object representing an AWS Batch job dependency.
            jobId (string) --The job ID of the AWS Batch job associated with this dependency.
            
            

    :type jobDefinition: string
    :param jobDefinition: [REQUIRED]
            The job definition used by this job. This value can be either a name:revision or the Amazon Resource Name (ARN) for the job definition.
            

    :type parameters: dict
    :param parameters: Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters in a SubmitJob request override any corresponding parameter defaults from the job definition.
            (string) --
            (string) --
            

    :type containerOverrides: dict
    :param containerOverrides: A list of container overrides in JSON format that specify the name of a container in the specified job definition and the overrides it should receive. You can override the default command for a container (that is specified in the job definition or the Docker image) with a command override. You can also override existing environment variables (that are specified in the job definition or Docker image) on a container or add new environment variables to it with an environment override.
            vcpus (integer) --The number of vCPUs to reserve for the container. This value overrides the value set in the job definition.
            memory (integer) --The number of MiB of memory reserved for the job. This value overrides the value set in the job definition.
            command (list) --The command to send to the container that overrides the default command from the Docker image or the job definition.
            (string) --
            environment (list) --The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.
            (dict) --A key-value pair object.
            name (string) --The name of the key value pair. For environment variables, this is the name of the environment variable.
            value (string) --The value of the key value pair. For environment variables, this is the value of the environment variable.
            
            

    :type retryStrategy: dict
    :param retryStrategy: The retry strategy to use for failed jobs from this SubmitJob operation. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.
            attempts (integer) --The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If attempts is greater than one, the job is retried if it fails until it has moved to RUNNABLE that many times.
            

    :rtype: dict
    :return: {
        'jobName': 'string',
        'jobId': 'string'
    }
    
    
    """
    pass

def terminate_job(jobId=None, reason=None):
    """
    Terminates jobs in a job queue. Jobs that are in the STARTING or RUNNING state are terminated, which causes them to transition to FAILED . Jobs that have not progressed to the STARTING state are cancelled.
    See also: AWS API Documentation
    
    Examples
    This example terminates a job with the specified job ID.
    Expected Output:
    
    :example: response = client.terminate_job(
        jobId='string',
        reason='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]
            Job IDs to be terminated. Up to 100 jobs can be specified.
            

    :type reason: string
    :param reason: [REQUIRED]
            A message to attach to the job that explains the reason for cancelling it. This message is returned by future DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_compute_environment(computeEnvironment=None, state=None, computeResources=None, serviceRole=None):
    """
    Updates an AWS Batch compute environment.
    See also: AWS API Documentation
    
    Examples
    This example disables the P2OnDemand compute environment so it can be deleted.
    Expected Output:
    
    :example: response = client.update_compute_environment(
        computeEnvironment='string',
        state='ENABLED'|'DISABLED',
        computeResources={
            'minvCpus': 123,
            'maxvCpus': 123,
            'desiredvCpus': 123
        },
        serviceRole='string'
    )
    
    
    :type computeEnvironment: string
    :param computeEnvironment: [REQUIRED]
            The name or full Amazon Resource Name (ARN) of the compute environment to update.
            

    :type state: string
    :param state: The state of the compute environment. Compute environments in the ENABLED state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.

    :type computeResources: dict
    :param computeResources: Details of the compute resources managed by the compute environment. Required for a managed compute environment.
            minvCpus (integer) --The minimum number of EC2 vCPUs that an environment should maintain.
            maxvCpus (integer) --The maximum number of EC2 vCPUs that an environment can reach.
            desiredvCpus (integer) --The desired number of EC2 vCPUS in the compute environment.
            

    :type serviceRole: string
    :param serviceRole: The name or full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to ECS, Auto Scaling, and EC2 on your behalf.

    :rtype: dict
    :return: {
        'computeEnvironmentName': 'string',
        'computeEnvironmentArn': 'string'
    }
    
    
    """
    pass

def update_job_queue(jobQueue=None, state=None, priority=None, computeEnvironmentOrder=None):
    """
    Updates a job queue.
    See also: AWS API Documentation
    
    Examples
    This example disables a job queue so that it can be deleted.
    Expected Output:
    
    :example: response = client.update_job_queue(
        jobQueue='string',
        state='ENABLED'|'DISABLED',
        priority=123,
        computeEnvironmentOrder=[
            {
                'order': 123,
                'computeEnvironment': 'string'
            },
        ]
    )
    
    
    :type jobQueue: string
    :param jobQueue: [REQUIRED]
            The name or the Amazon Resource Name (ARN) of the job queue.
            

    :type state: string
    :param state: Describes the queue's ability to accept new jobs.

    :type priority: integer
    :param priority: The priority of the job queue. Job queues with a higher priority (or a lower integer value for the priority parameter) are evaluated first when associated with same compute environment. Priority is determined in ascending order, for example, a job queue with a priority value of 1 is given scheduling preference over a job queue with a priority value of 10 .

    :type computeEnvironmentOrder: list
    :param computeEnvironmentOrder: Details the set of compute environments mapped to a job queue and their order relative to each other. This is one of the parameters used by the job scheduler to determine which compute environment should execute a given job.
            (dict) --The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.
            order (integer) -- [REQUIRED]The order of the compute environment.
            computeEnvironment (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the compute environment.
            
            

    :rtype: dict
    :return: {
        'jobQueueName': 'string',
        'jobQueueArn': 'string'
    }
    
    
    """
    pass

