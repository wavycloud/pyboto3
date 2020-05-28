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

def cancel_job(jobId=None, reason=None):
    """
    Cancels a job in an AWS Batch job queue. Jobs that are in the SUBMITTED , PENDING , or RUNNABLE state are cancelled. Jobs that have progressed to STARTING or RUNNING are not cancelled (but the API operation still succeeds, even if no job is cancelled); these jobs must be terminated with the  TerminateJob operation.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example cancels a job with the specified job ID.
    Expected Output:
    
    :example: response = client.cancel_job(
        jobId='string',
        reason='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe AWS Batch job ID of the job to cancel.\n

    :type reason: string
    :param reason: [REQUIRED]\nA message to attach to the job that explains the reason for canceling it. This message is returned by future DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example cancels a job with the specified job ID.
response = client.cancel_job(
    jobId='1d828f65-7a4d-42e8-996d-3b900ed59dc4',
    reason='Cancelling job.',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_compute_environment(computeEnvironmentName=None, type=None, state=None, computeResources=None, serviceRole=None):
    """
    Creates an AWS Batch compute environment. You can create MANAGED or UNMANAGED compute environments.
    In a managed compute environment, AWS Batch manages the capacity and instance types of the compute resources within the environment. This is based on the compute resource specification that you define or the launch template that you specify when you create the compute environment. You can choose to use Amazon EC2 On-Demand Instances or Spot Instances in your managed compute environment. You can optionally set a maximum price so that Spot Instances only launch when the Spot Instance price is below a specified percentage of the On-Demand price.
    In an unmanaged compute environment, you can manage your own compute resources. This provides more compute resource configuration options, such as using a custom AMI, but you must ensure that your AMI meets the Amazon ECS container instance AMI specification. For more information, see Container Instance AMIs in the Amazon Elastic Container Service Developer Guide . After you have created your unmanaged compute environment, you can use the  DescribeComputeEnvironments operation to find the Amazon ECS cluster that is associated with it. Then, manually launch your container instances into that Amazon ECS cluster. For more information, see Launching an Amazon ECS Container Instance in the Amazon Elastic Container Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
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
            'allocationStrategy': 'BEST_FIT'|'BEST_FIT_PROGRESSIVE'|'SPOT_CAPACITY_OPTIMIZED',
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
            'placementGroup': 'string',
            'bidPercentage': 123,
            'spotIamFleetRole': 'string',
            'launchTemplate': {
                'launchTemplateId': 'string',
                'launchTemplateName': 'string',
                'version': 'string'
            }
        },
        serviceRole='string'
    )
    
    
    :type computeEnvironmentName: string
    :param computeEnvironmentName: [REQUIRED]\nThe name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.\n

    :type type: string
    :param type: [REQUIRED]\nThe type of the compute environment. For more information, see Compute Environments in the AWS Batch User Guide .\n

    :type state: string
    :param state: The state of the compute environment. If the state is ENABLED , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.

    :type computeResources: dict
    :param computeResources: Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. For more information, see Compute Environments in the AWS Batch User Guide .\n\ntype (string) -- [REQUIRED]The type of compute environment: EC2 or SPOT .\n\nallocationStrategy (string) --The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. This could be due to availability of the instance type in the region or Amazon EC2 service limits . If this is not specified, the default is BEST_FIT , which will use only the best fitting instance type, waiting for additional capacity if it\'s not available. This allocation strategy keeps costs lower but can limit scaling. If you are using Spot Fleets with BEST_FIT then the Spot Fleet IAM Role must be specified. BEST_FIT_PROGRESSIVE will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types with a lower cost per vCPU. SPOT_CAPACITY_OPTIMIZED is only available for Spot Instance compute resources and will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types that are less likely to be interrupted. For more information, see `Allocation Strategies <https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html >`__ in the AWS Batch User Guide .\n\nminvCpus (integer) -- [REQUIRED]The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the compute environment is DISABLED ).\n\nmaxvCpus (integer) -- [REQUIRED]The maximum number of Amazon EC2 vCPUs that an environment can reach.\n\ndesiredvCpus (integer) --The desired number of Amazon EC2 vCPUS in the compute environment.\n\ninstanceTypes (list) -- [REQUIRED]The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, c5 or p3 ), or you can specify specific sizes within a family (such as c5.8xlarge ). You can also choose optimal to pick instance types (from the C, M, and R instance families) on the fly that match the demand of your job queues.\n\n(string) --\n\n\nimageId (string) --The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.\n\nsubnets (list) -- [REQUIRED]The VPC subnets into which the compute resources are launched. For more information, see VPCs and Subnets in the Amazon VPC User Guide .\n\n(string) --\n\n\nsecurityGroupIds (list) --The Amazon EC2 security groups associated with instances launched in the compute environment. One or more security groups must be specified, either in securityGroupIds or using a launch template referenced in launchTemplate . If security groups are specified using both securityGroupIds and launchTemplate , the values in securityGroupIds will be used.\n\n(string) --\n\n\nec2KeyPair (string) --The Amazon EC2 key pair that is used for instances launched in the compute environment.\n\ninstanceRole (string) -- [REQUIRED]The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, `` ecsInstanceRole `` or ``arn:aws:iam::<aws_account_id> :instance-profile/ecsInstanceRole `` . For more information, see Amazon ECS Instance Role in the AWS Batch User Guide .\n\ntags (dict) --Key-value pair tags to be applied to resources that are launched in the compute environment. For AWS Batch, these take the form of 'String1': 'String2', where String1 is the tag key and String2 is the tag value\xe2\x80\x94for example, { 'Name': 'AWS Batch Instance - C4OnDemand' }.\n\n(string) --\n(string) --\n\n\n\n\nplacementGroup (string) --The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see Placement Groups in the Amazon EC2 User Guide for Linux Instances .\n\nbidPercentage (integer) --The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price.\n\nspotIamFleetRole (string) --The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This role is required if the allocation strategy set to BEST_FIT or if the allocation strategy is not specified. For more information, see Amazon EC2 Spot Fleet Role in the AWS Batch User Guide .\n\nlaunchTemplate (dict) --The launch template to use for your compute resources. Any other compute resource parameters that you specify in a CreateComputeEnvironment API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see Launch Template Support in the AWS Batch User Guide .\n\nlaunchTemplateId (string) --The ID of the launch template.\n\nlaunchTemplateName (string) --The name of the launch template.\n\nversion (string) --The version number of the launch template.\nDefault: The default version of the launch template.\n\n\n\n\n

    :type serviceRole: string
    :param serviceRole: [REQUIRED]\nThe full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.\nIf your specified role has a path other than / , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.\n\nNote\nDepending on how you created your AWS Batch service role, its ARN may contain the service-role path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the service-role path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'computeEnvironmentName': 'string',
    'computeEnvironmentArn': 'string'
}


Response Structure

(dict) --

computeEnvironmentName (string) --
The name of the compute environment.

computeEnvironmentArn (string) --
The Amazon Resource Name (ARN) of the compute environment.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example creates a managed compute environment with specific C4 instance types that are launched on demand. The compute environment is called C4OnDemand.
response = client.create_compute_environment(
    type='MANAGED',
    computeEnvironmentName='C4OnDemand',
    computeResources={
        'type': 'EC2',
        'desiredvCpus': 48,
        'ec2KeyPair': 'id_rsa',
        'instanceRole': 'ecsInstanceRole',
        'instanceTypes': [
            'c4.large',
            'c4.xlarge',
            'c4.2xlarge',
            'c4.4xlarge',
            'c4.8xlarge',
        ],
        'maxvCpus': 128,
        'minvCpus': 0,
        'securityGroupIds': [
            'sg-cf5093b2',
        ],
        'subnets': [
            'subnet-220c0e0a',
            'subnet-1a95556d',
            'subnet-978f6dce',
        ],
        'tags': {
            'Name': 'Batch Instance - C4OnDemand',
        },
    },
    serviceRole='arn:aws:iam::012345678910:role/AWSBatchServiceRole',
    state='ENABLED',
)

print(response)


Expected Output:
{
    'computeEnvironmentArn': 'arn:aws:batch:us-east-1:012345678910:compute-environment/C4OnDemand',
    'computeEnvironmentName': 'C4OnDemand',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates a managed compute environment with the M4 instance type that is launched when the Spot bid price is at or below 20% of the On-Demand price for the instance type. The compute environment is called M4Spot.
response = client.create_compute_environment(
    type='MANAGED',
    computeEnvironmentName='M4Spot',
    computeResources={
        'type': 'SPOT',
        'bidPercentage': 20,
        'desiredvCpus': 4,
        'ec2KeyPair': 'id_rsa',
        'instanceRole': 'ecsInstanceRole',
        'instanceTypes': [
            'm4',
        ],
        'maxvCpus': 128,
        'minvCpus': 0,
        'securityGroupIds': [
            'sg-cf5093b2',
        ],
        'spotIamFleetRole': 'arn:aws:iam::012345678910:role/aws-ec2-spot-fleet-role',
        'subnets': [
            'subnet-220c0e0a',
            'subnet-1a95556d',
            'subnet-978f6dce',
        ],
        'tags': {
            'Name': 'Batch Instance - M4Spot',
        },
    },
    serviceRole='arn:aws:iam::012345678910:role/AWSBatchServiceRole',
    state='ENABLED',
)

print(response)


Expected Output:
{
    'computeEnvironmentArn': 'arn:aws:batch:us-east-1:012345678910:compute-environment/M4Spot',
    'computeEnvironmentName': 'M4Spot',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'computeEnvironmentName': 'string',
        'computeEnvironmentArn': 'string'
    }
    
    
    :returns: 
    computeEnvironmentName (string) -- [REQUIRED]
    The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
    
    type (string) -- [REQUIRED]
    The type of the compute environment. For more information, see Compute Environments in the AWS Batch User Guide .
    
    state (string) -- The state of the compute environment. If the state is ENABLED , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.
    computeResources (dict) -- Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. For more information, see Compute Environments in the AWS Batch User Guide .
    
    type (string) -- [REQUIRED]The type of compute environment: EC2 or SPOT .
    
    allocationStrategy (string) --The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. This could be due to availability of the instance type in the region or Amazon EC2 service limits . If this is not specified, the default is BEST_FIT , which will use only the best fitting instance type, waiting for additional capacity if it\'s not available. This allocation strategy keeps costs lower but can limit scaling. If you are using Spot Fleets with BEST_FIT then the Spot Fleet IAM Role must be specified. BEST_FIT_PROGRESSIVE will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types with a lower cost per vCPU. SPOT_CAPACITY_OPTIMIZED is only available for Spot Instance compute resources and will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types that are less likely to be interrupted. For more information, see `Allocation Strategies <https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html >`__ in the AWS Batch User Guide .
    
    minvCpus (integer) -- [REQUIRED]The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the compute environment is DISABLED ).
    
    maxvCpus (integer) -- [REQUIRED]The maximum number of Amazon EC2 vCPUs that an environment can reach.
    
    desiredvCpus (integer) --The desired number of Amazon EC2 vCPUS in the compute environment.
    
    instanceTypes (list) -- [REQUIRED]The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, c5 or p3 ), or you can specify specific sizes within a family (such as c5.8xlarge ). You can also choose optimal to pick instance types (from the C, M, and R instance families) on the fly that match the demand of your job queues.
    
    (string) --
    
    
    imageId (string) --The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.
    
    subnets (list) -- [REQUIRED]The VPC subnets into which the compute resources are launched. For more information, see VPCs and Subnets in the Amazon VPC User Guide .
    
    (string) --
    
    
    securityGroupIds (list) --The Amazon EC2 security groups associated with instances launched in the compute environment. One or more security groups must be specified, either in securityGroupIds or using a launch template referenced in launchTemplate . If security groups are specified using both securityGroupIds and launchTemplate , the values in securityGroupIds will be used.
    
    (string) --
    
    
    ec2KeyPair (string) --The Amazon EC2 key pair that is used for instances launched in the compute environment.
    
    instanceRole (string) -- [REQUIRED]The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, `` ecsInstanceRole `` or ``arn:aws:iam::<aws_account_id> :instance-profile/ecsInstanceRole `` . For more information, see Amazon ECS Instance Role in the AWS Batch User Guide .
    
    tags (dict) --Key-value pair tags to be applied to resources that are launched in the compute environment. For AWS Batch, these take the form of "String1": "String2", where String1 is the tag key and String2 is the tag value\xe2\x80\x94for example, { "Name": "AWS Batch Instance - C4OnDemand" }.
    
    (string) --
    (string) --
    
    
    
    
    placementGroup (string) --The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see Placement Groups in the Amazon EC2 User Guide for Linux Instances .
    
    bidPercentage (integer) --The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price.
    
    spotIamFleetRole (string) --The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This role is required if the allocation strategy set to BEST_FIT or if the allocation strategy is not specified. For more information, see Amazon EC2 Spot Fleet Role in the AWS Batch User Guide .
    
    launchTemplate (dict) --The launch template to use for your compute resources. Any other compute resource parameters that you specify in a  CreateComputeEnvironment API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see Launch Template Support in the AWS Batch User Guide .
    
    launchTemplateId (string) --The ID of the launch template.
    
    launchTemplateName (string) --The name of the launch template.
    
    version (string) --The version number of the launch template.
    Default: The default version of the launch template.
    
    
    
    
    
    serviceRole (string) -- [REQUIRED]
    The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
    If your specified role has a path other than / , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.
    
    Note
    Depending on how you created your AWS Batch service role, its ARN may contain the service-role path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the service-role path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
    
    
    
    """
    pass

def create_job_queue(jobQueueName=None, state=None, priority=None, computeEnvironmentOrder=None):
    """
    Creates an AWS Batch job queue. When you create a job queue, you associate one or more compute environments to the queue and assign an order of preference for the compute environments.
    You also set a priority to the job queue that determines the order in which the AWS Batch scheduler places jobs onto its associated compute environments. For example, if a compute environment is associated with more than one job queue, the job queue with a higher priority is given preference for scheduling jobs to that compute environment.
    See also: AWS API Documentation
    
    Exceptions
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
    :param jobQueueName: [REQUIRED]\nThe name of the job queue.\n

    :type state: string
    :param state: The state of the job queue. If the job queue state is ENABLED , it is able to accept jobs.

    :type priority: integer
    :param priority: [REQUIRED]\nThe priority of the job queue. Job queues with a higher priority (or a higher integer value for the priority parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order, for example, a job queue with a priority value of 10 is given scheduling preference over a job queue with a priority value of 1 .\n

    :type computeEnvironmentOrder: list
    :param computeEnvironmentOrder: [REQUIRED]\nThe set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment should execute a given job. Compute environments must be in the VALID state before you can associate them with a job queue. You can associate up to three compute environments with a job queue.\n\n(dict) --The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.\n\norder (integer) -- [REQUIRED]The order of the compute environment.\n\ncomputeEnvironment (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the compute environment.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobQueueName': 'string',
    'jobQueueArn': 'string'
}


Response Structure

(dict) --

jobQueueName (string) --
The name of the job queue.

jobQueueArn (string) --
The Amazon Resource Name (ARN) of the job queue.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example creates a job queue called LowPriority that uses the M4Spot compute environment.
response = client.create_job_queue(
    computeEnvironmentOrder=[
        {
            'computeEnvironment': 'M4Spot',
            'order': 1,
        },
    ],
    jobQueueName='LowPriority',
    priority=1,
    state='ENABLED',
)

print(response)


Expected Output:
{
    'jobQueueArn': 'arn:aws:batch:us-east-1:012345678910:job-queue/LowPriority',
    'jobQueueName': 'LowPriority',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example creates a job queue called HighPriority that uses the C4OnDemand compute environment with an order of 1 and the M4Spot compute environment with an order of 2.
response = client.create_job_queue(
    computeEnvironmentOrder=[
        {
            'computeEnvironment': 'C4OnDemand',
            'order': 1,
        },
        {
            'computeEnvironment': 'M4Spot',
            'order': 2,
        },
    ],
    jobQueueName='HighPriority',
    priority=10,
    state='ENABLED',
)

print(response)


Expected Output:
{
    'jobQueueArn': 'arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority',
    'jobQueueName': 'HighPriority',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'jobQueueName': 'string',
        'jobQueueArn': 'string'
    }
    
    
    :returns: 
    Batch.Client.exceptions.ClientException
    Batch.Client.exceptions.ServerException
    
    """
    pass

def delete_compute_environment(computeEnvironment=None):
    """
    Deletes an AWS Batch compute environment.
    Before you can delete a compute environment, you must set its state to DISABLED with the  UpdateComputeEnvironment API operation and disassociate it from any job queues with the  UpdateJobQueue API operation.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the P2OnDemand compute environment.
    Expected Output:
    
    :example: response = client.delete_compute_environment(
        computeEnvironment='string'
    )
    
    
    :type computeEnvironment: string
    :param computeEnvironment: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the compute environment to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example deletes the P2OnDemand compute environment.
response = client.delete_compute_environment(
    computeEnvironment='P2OnDemand',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    Batch.Client.exceptions.ClientException
    Batch.Client.exceptions.ServerException
    
    """
    pass

def delete_job_queue(jobQueue=None):
    """
    Deletes the specified job queue. You must first disable submissions for a queue with the  UpdateJobQueue operation. All jobs in the queue are terminated when you delete a job queue.
    It is not necessary to disassociate compute environments from a queue before submitting a DeleteJobQueue request.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the GPGPU job queue.
    Expected Output:
    
    :example: response = client.delete_job_queue(
        jobQueue='string'
    )
    
    
    :type jobQueue: string
    :param jobQueue: [REQUIRED]\nThe short name or full Amazon Resource Name (ARN) of the queue to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example deletes the GPGPU job queue.
response = client.delete_job_queue(
    jobQueue='GPGPU',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    Batch.Client.exceptions.ClientException
    Batch.Client.exceptions.ServerException
    
    """
    pass

def deregister_job_definition(jobDefinition=None):
    """
    Deregisters an AWS Batch job definition. Job definitions will be permanently deleted after 180 days.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deregisters a job definition called sleep10.
    Expected Output:
    
    :example: response = client.deregister_job_definition(
        jobDefinition='string'
    )
    
    
    :type jobDefinition: string
    :param jobDefinition: [REQUIRED]\nThe name and revision (name:revision ) or full Amazon Resource Name (ARN) of the job definition to deregister.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example deregisters a job definition called sleep10.
response = client.deregister_job_definition(
    jobDefinition='sleep10',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    Batch.Client.exceptions.ClientException
    Batch.Client.exceptions.ServerException
    
    """
    pass

def describe_compute_environments(computeEnvironments=None, maxResults=None, nextToken=None):
    """
    Describes one or more of your compute environments.
    If you are using an unmanaged compute environment, you can use the DescribeComputeEnvironment operation to determine the ecsClusterArn that you should launch your Amazon ECS container instances into.
    See also: AWS API Documentation
    
    Exceptions
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
    :param computeEnvironments: A list of up to 100 compute environment names or full Amazon Resource Name (ARN) entries.\n\n(string) --\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of cluster results returned by DescribeComputeEnvironments in paginated output. When this parameter is used, DescribeComputeEnvironments only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeComputeEnvironments request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeComputeEnvironments returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeComputeEnvironments request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                'allocationStrategy': 'BEST_FIT'|'BEST_FIT_PROGRESSIVE'|'SPOT_CAPACITY_OPTIMIZED',
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
                'placementGroup': 'string',
                'bidPercentage': 123,
                'spotIamFleetRole': 'string',
                'launchTemplate': {
                    'launchTemplateId': 'string',
                    'launchTemplateName': 'string',
                    'version': 'string'
                }
            },
            'serviceRole': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

computeEnvironments (list) --
The list of compute environments.

(dict) --
An object representing an AWS Batch compute environment.

computeEnvironmentName (string) --
The name of the compute environment.

computeEnvironmentArn (string) --
The Amazon Resource Name (ARN) of the compute environment.

ecsClusterArn (string) --
The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.

type (string) --
The type of the compute environment.

state (string) --
The state of the compute environment. The valid values are ENABLED or DISABLED .
If the state is ENABLED , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.
If the state is DISABLED , then the AWS Batch scheduler does not attempt to place jobs within the environment. Jobs in a STARTING or RUNNING state continue to progress normally. Managed compute environments in the DISABLED state do not scale out. However, they scale in to minvCpus value after instances become idle.

status (string) --
The current status of the compute environment (for example, CREATING or VALID ).

statusReason (string) --
A short, human-readable string to provide additional details about the current status of the compute environment.

computeResources (dict) --
The compute resources defined for the compute environment.

type (string) --
The type of compute environment: EC2 or SPOT .

allocationStrategy (string) --
The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. This could be due to availability of the instance type in the region or Amazon EC2 service limits . If this is not specified, the default is BEST_FIT , which will use only the best fitting instance type, waiting for additional capacity if it\'s not available. This allocation strategy keeps costs lower but can limit scaling. If you are using Spot Fleets with BEST_FIT then the Spot Fleet IAM Role must be specified. BEST_FIT_PROGRESSIVE will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types with a lower cost per vCPU. SPOT_CAPACITY_OPTIMIZED is only available for Spot Instance compute resources and will select additional instance types that are large enough to meet the requirements of the jobs in the queue, with a preference for instance types that are less likely to be interrupted. For more information, see `Allocation Strategies <https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html >`__ in the AWS Batch User Guide .

minvCpus (integer) --
The minimum number of Amazon EC2 vCPUs that an environment should maintain (even if the compute environment is DISABLED ).

maxvCpus (integer) --
The maximum number of Amazon EC2 vCPUs that an environment can reach.

desiredvCpus (integer) --
The desired number of Amazon EC2 vCPUS in the compute environment.

instanceTypes (list) --
The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, c5 or p3 ), or you can specify specific sizes within a family (such as c5.8xlarge ). You can also choose optimal to pick instance types (from the C, M, and R instance families) on the fly that match the demand of your job queues.

(string) --


imageId (string) --
The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.

subnets (list) --
The VPC subnets into which the compute resources are launched. For more information, see VPCs and Subnets in the Amazon VPC User Guide .

(string) --


securityGroupIds (list) --
The Amazon EC2 security groups associated with instances launched in the compute environment. One or more security groups must be specified, either in securityGroupIds or using a launch template referenced in launchTemplate . If security groups are specified using both securityGroupIds and launchTemplate , the values in securityGroupIds will be used.

(string) --


ec2KeyPair (string) --
The Amazon EC2 key pair that is used for instances launched in the compute environment.

instanceRole (string) --
The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, `` ecsInstanceRole `` or ``arn:aws:iam::<aws_account_id> :instance-profile/ecsInstanceRole `` . For more information, see Amazon ECS Instance Role in the AWS Batch User Guide .

tags (dict) --
Key-value pair tags to be applied to resources that are launched in the compute environment. For AWS Batch, these take the form of "String1": "String2", where String1 is the tag key and String2 is the tag value\xe2\x80\x94for example, { "Name": "AWS Batch Instance - C4OnDemand" }.

(string) --
(string) --




placementGroup (string) --
The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see Placement Groups in the Amazon EC2 User Guide for Linux Instances .

bidPercentage (integer) --
The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price.

spotIamFleetRole (string) --
The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This role is required if the allocation strategy set to BEST_FIT or if the allocation strategy is not specified. For more information, see Amazon EC2 Spot Fleet Role in the AWS Batch User Guide .

launchTemplate (dict) --
The launch template to use for your compute resources. Any other compute resource parameters that you specify in a  CreateComputeEnvironment API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see Launch Template Support in the AWS Batch User Guide .

launchTemplateId (string) --
The ID of the launch template.

launchTemplateName (string) --
The name of the launch template.

version (string) --
The version number of the launch template.
Default: The default version of the launch template.





serviceRole (string) --
The service role associated with the compute environment that allows AWS Batch to make calls to AWS API operations on your behalf.





nextToken (string) --
The nextToken value to include in a future DescribeComputeEnvironments request. When the results of a DescribeJobDefinitions request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example describes the P2OnDemand compute environment.
response = client.describe_compute_environments(
    computeEnvironments=[
        'P2OnDemand',
    ],
)

print(response)


Expected Output:
{
    'computeEnvironments': [
        {
            'type': 'MANAGED',
            'computeEnvironmentArn': 'arn:aws:batch:us-east-1:012345678910:compute-environment/P2OnDemand',
            'computeEnvironmentName': 'P2OnDemand',
            'computeResources': {
                'type': 'EC2',
                'desiredvCpus': 48,
                'ec2KeyPair': 'id_rsa',
                'instanceRole': 'ecsInstanceRole',
                'instanceTypes': [
                    'p2',
                ],
                'maxvCpus': 128,
                'minvCpus': 0,
                'securityGroupIds': [
                    'sg-cf5093b2',
                ],
                'subnets': [
                    'subnet-220c0e0a',
                    'subnet-1a95556d',
                    'subnet-978f6dce',
                ],
                'tags': {
                    'Name': 'Batch Instance - P2OnDemand',
                },
            },
            'ecsClusterArn': 'arn:aws:ecs:us-east-1:012345678910:cluster/P2OnDemand_Batch_2c06f29d-d1fe-3a49-879d-42394c86effc',
            'serviceRole': 'arn:aws:iam::012345678910:role/AWSBatchServiceRole',
            'state': 'ENABLED',
            'status': 'VALID',
            'statusReason': 'ComputeEnvironment Healthy',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                    'allocationStrategy': 'BEST_FIT'|'BEST_FIT_PROGRESSIVE'|'SPOT_CAPACITY_OPTIMIZED',
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
                    'placementGroup': 'string',
                    'bidPercentage': 123,
                    'spotIamFleetRole': 'string',
                    'launchTemplate': {
                        'launchTemplateId': 'string',
                        'launchTemplateName': 'string',
                        'version': 'string'
                    }
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
    
    Exceptions
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
    :param jobDefinitions: A list of up to 100 job definition names or full Amazon Resource Name (ARN) entries.\n\n(string) --\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of results returned by DescribeJobDefinitions in paginated output. When this parameter is used, DescribeJobDefinitions only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeJobDefinitions request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeJobDefinitions returns up to 100 results and a nextToken value if applicable.

    :type jobDefinitionName: string
    :param jobDefinitionName: The name of the job definition to describe.

    :type status: string
    :param status: The status with which to filter job definitions.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeJobDefinitions request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                'user': 'string',
                'instanceType': 'string',
                'resourceRequirements': [
                    {
                        'value': 'string',
                        'type': 'GPU'
                    },
                ],
                'linuxParameters': {
                    'devices': [
                        {
                            'hostPath': 'string',
                            'containerPath': 'string',
                            'permissions': [
                                'READ'|'WRITE'|'MKNOD',
                            ]
                        },
                    ]
                }
            },
            'timeout': {
                'attemptDurationSeconds': 123
            },
            'nodeProperties': {
                'numNodes': 123,
                'mainNode': 123,
                'nodeRangeProperties': [
                    {
                        'targetNodes': 'string',
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
                            'privileged': True|False,
                            'ulimits': [
                                {
                                    'hardLimit': 123,
                                    'name': 'string',
                                    'softLimit': 123
                                },
                            ],
                            'user': 'string',
                            'instanceType': 'string',
                            'resourceRequirements': [
                                {
                                    'value': 'string',
                                    'type': 'GPU'
                                },
                            ],
                            'linuxParameters': {
                                'devices': [
                                    {
                                        'hostPath': 'string',
                                        'containerPath': 'string',
                                        'permissions': [
                                            'READ'|'WRITE'|'MKNOD',
                                        ]
                                    },
                                ]
                            }
                        }
                    },
                ]
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

jobDefinitions (list) --
The list of job definitions.

(dict) --
An object representing an AWS Batch job definition.

jobDefinitionName (string) --
The name of the job definition.

jobDefinitionArn (string) --
The Amazon Resource Name (ARN) for the job definition.

revision (integer) --
The revision of the job definition.

status (string) --
The status of the job definition.

type (string) --
The type of job definition.

parameters (dict) --
Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a SubmitJob request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see Job Definition Parameters in the AWS Batch User Guide .

(string) --
(string) --




retryStrategy (dict) --
The retry strategy to use for failed jobs that are submitted with this job definition.

attempts (integer) --
The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If the value of attempts is greater than one, the job is retried on failure the same number of attempts as the value.



containerProperties (dict) --
An object with various properties specific to container-based jobs.

image (string) --
The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` repository-url /image :tag `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .

Images in Amazon ECR repositories use the full registry and repository URI (for example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name> ).
Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).


vcpus (integer) --
The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.

memory (integer) --
The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run . You must specify at least 4 MiB of memory for a job.

Note
If you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see Memory Management in the AWS Batch User Guide .


command (list) --
The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd .

(string) --


jobRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.

volumes (list) --
A list of data volumes used in a job.

(dict) --
A data volume used in a job\'s container properties.

host (dict) --
The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.

sourcePath (string) --
The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.



name (string) --
The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .





environment (list) --
The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .

Warning
We do not recommend using plaintext environment variables for sensitive information, such as credential data.


Note
Environment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.


(dict) --
A key-value pair object.

name (string) --
The name of the key-value pair. For environment variables, this is the name of the environment variable.

value (string) --
The value of the key-value pair. For environment variables, this is the value of the environment variable.





mountPoints (list) --
The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .

(dict) --
Details on a Docker volume mount point that is used in a job\'s container properties. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run.

containerPath (string) --
The path on the container at which to mount the host volume.

readOnly (boolean) --
If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false .

sourceVolume (string) --
The name of the volume to mount.





readonlyRootFilesystem (boolean) --
When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .

privileged (boolean) --
When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .

ulimits (list) --
A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run .

(dict) --
The ulimit settings to pass to the container.

hardLimit (integer) --
The hard limit for the ulimit type.

name (string) --
The type of the ulimit .

softLimit (integer) --
The soft limit for the ulimit type.





user (string) --
The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .

instanceType (string) --
The instance type to use for a multi-node parallel job. Currently all node groups in a multi-node parallel job must use the same instance type. This parameter is not valid for single-node container jobs.

resourceRequirements (list) --
The type and amount of a resource to assign to a container. Currently, the only supported resource is GPU .

(dict) --
The type and amount of a resource to assign to a container. Currently, the only supported resource type is GPU .

value (string) --
The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.

type (string) --
The type of resource to assign to a container. Currently, the only supported resource type is GPU .





linuxParameters (dict) --
Linux-specific modifications that are applied to the container, such as details for device mappings.

devices (list) --
Any host devices to expose to the container. This parameter maps to Devices in the Create a container section of the Docker Remote API and the --device option to docker run .

(dict) --
An object representing a container instance host device.

hostPath (string) --
The path for the device on the host container instance.

containerPath (string) --
The path inside the container at which to expose the host device. By default the hostPath value is used.

permissions (list) --
The explicit permissions to provide to the container for the device. By default, the container has permissions for read , write , and mknod for the device.

(string) --










timeout (dict) --
The timeout configuration for jobs that are submitted with this job definition. You can specify a timeout duration after which AWS Batch terminates your jobs if they have not finished.

attemptDurationSeconds (integer) --
The time duration in seconds (measured from the job attempt\'s startedAt timestamp) after which AWS Batch terminates your jobs if they have not finished.



nodeProperties (dict) --
An object with various properties specific to multi-node parallel jobs.

numNodes (integer) --
The number of nodes associated with a multi-node parallel job.

mainNode (integer) --
Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.

nodeRangeProperties (list) --
A list of node ranges and their properties associated with a multi-node parallel job.

(dict) --
An object representing the properties of the node range for a multi-node parallel job.

targetNodes (string) --
The range of nodes, using node index values. A range of 0:3 indicates nodes with index values of 0 through 3 . If the starting range value is omitted (:n ), then 0 is used to start the range. If the ending range value is omitted (n: ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes (0:n). You may nest node ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override the 0:10 properties.

container (dict) --
The container details for the node range.

image (string) --
The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` repository-url /image :tag `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .

Images in Amazon ECR repositories use the full registry and repository URI (for example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name> ).
Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).


vcpus (integer) --
The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.

memory (integer) --
The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run . You must specify at least 4 MiB of memory for a job.

Note
If you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see Memory Management in the AWS Batch User Guide .


command (list) --
The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd .

(string) --


jobRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.

volumes (list) --
A list of data volumes used in a job.

(dict) --
A data volume used in a job\'s container properties.

host (dict) --
The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.

sourcePath (string) --
The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.



name (string) --
The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .





environment (list) --
The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .

Warning
We do not recommend using plaintext environment variables for sensitive information, such as credential data.


Note
Environment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.


(dict) --
A key-value pair object.

name (string) --
The name of the key-value pair. For environment variables, this is the name of the environment variable.

value (string) --
The value of the key-value pair. For environment variables, this is the value of the environment variable.





mountPoints (list) --
The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .

(dict) --
Details on a Docker volume mount point that is used in a job\'s container properties. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run.

containerPath (string) --
The path on the container at which to mount the host volume.

readOnly (boolean) --
If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false .

sourceVolume (string) --
The name of the volume to mount.





readonlyRootFilesystem (boolean) --
When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .

privileged (boolean) --
When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .

ulimits (list) --
A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run .

(dict) --
The ulimit settings to pass to the container.

hardLimit (integer) --
The hard limit for the ulimit type.

name (string) --
The type of the ulimit .

softLimit (integer) --
The soft limit for the ulimit type.





user (string) --
The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .

instanceType (string) --
The instance type to use for a multi-node parallel job. Currently all node groups in a multi-node parallel job must use the same instance type. This parameter is not valid for single-node container jobs.

resourceRequirements (list) --
The type and amount of a resource to assign to a container. Currently, the only supported resource is GPU .

(dict) --
The type and amount of a resource to assign to a container. Currently, the only supported resource type is GPU .

value (string) --
The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.

type (string) --
The type of resource to assign to a container. Currently, the only supported resource type is GPU .





linuxParameters (dict) --
Linux-specific modifications that are applied to the container, such as details for device mappings.

devices (list) --
Any host devices to expose to the container. This parameter maps to Devices in the Create a container section of the Docker Remote API and the --device option to docker run .

(dict) --
An object representing a container instance host device.

hostPath (string) --
The path for the device on the host container instance.

containerPath (string) --
The path inside the container at which to expose the host device. By default the hostPath value is used.

permissions (list) --
The explicit permissions to provide to the container for the device. By default, the container has permissions for read , write , and mknod for the device.

(string) --




















nextToken (string) --
The nextToken value to include in a future DescribeJobDefinitions request. When the results of a DescribeJobDefinitions request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example describes all of your active job definitions.
response = client.describe_job_definitions(
    status='ACTIVE',
)

print(response)


Expected Output:
{
    'jobDefinitions': [
        {
            'type': 'container',
            'containerProperties': {
                'command': [
                    'sleep',
                    '60',
                ],
                'environment': [
                ],
                'image': 'busybox',
                'memory': 128,
                'mountPoints': [
                ],
                'ulimits': [
                ],
                'vcpus': 1,
                'volumes': [
                ],
            },
            'jobDefinitionArn': 'arn:aws:batch:us-east-1:012345678910:job-definition/sleep60:1',
            'jobDefinitionName': 'sleep60',
            'revision': 1,
            'status': 'ACTIVE',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                    'user': 'string',
                    'instanceType': 'string',
                    'resourceRequirements': [
                        {
                            'value': 'string',
                            'type': 'GPU'
                        },
                    ],
                    'linuxParameters': {
                        'devices': [
                            {
                                'hostPath': 'string',
                                'containerPath': 'string',
                                'permissions': [
                                    'READ'|'WRITE'|'MKNOD',
                                ]
                            },
                        ]
                    }
                },
                'timeout': {
                    'attemptDurationSeconds': 123
                },
                'nodeProperties': {
                    'numNodes': 123,
                    'mainNode': 123,
                    'nodeRangeProperties': [
                        {
                            'targetNodes': 'string',
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
                                'privileged': True|False,
                                'ulimits': [
                                    {
                                        'hardLimit': 123,
                                        'name': 'string',
                                        'softLimit': 123
                                    },
                                ],
                                'user': 'string',
                                'instanceType': 'string',
                                'resourceRequirements': [
                                    {
                                        'value': 'string',
                                        'type': 'GPU'
                                    },
                                ],
                                'linuxParameters': {
                                    'devices': [
                                        {
                                            'hostPath': 'string',
                                            'containerPath': 'string',
                                            'permissions': [
                                                'READ'|'WRITE'|'MKNOD',
                                            ]
                                        },
                                    ]
                                }
                            }
                        },
                    ]
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
    
    Exceptions
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
    :param jobQueues: A list of up to 100 queue names or full queue Amazon Resource Name (ARN) entries.\n\n(string) --\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of results returned by DescribeJobQueues in paginated output. When this parameter is used, DescribeJobQueues only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another DescribeJobQueues request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then DescribeJobQueues returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated DescribeJobQueues request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

jobQueues (list) --
The list of job queues.

(dict) --
An object representing the details of an AWS Batch job queue.

jobQueueName (string) --
The name of the job queue.

jobQueueArn (string) --
The Amazon Resource Name (ARN) of the job queue.

state (string) --
Describes the ability of the queue to accept new jobs.

status (string) --
The status of the job queue (for example, CREATING or VALID ).

statusReason (string) --
A short, human-readable string to provide additional details about the current status of the job queue.

priority (integer) --
The priority of the job queue.

computeEnvironmentOrder (list) --
The compute environments that are attached to the job queue and the order in which job placement is preferred. Compute environments are selected for job placement in ascending order.

(dict) --
The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.

order (integer) --
The order of the compute environment.

computeEnvironment (string) --
The Amazon Resource Name (ARN) of the compute environment.









nextToken (string) --
The nextToken value to include in a future DescribeJobQueues request. When the results of a DescribeJobQueues request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example describes the HighPriority job queue.
response = client.describe_job_queues(
    jobQueues=[
        'HighPriority',
    ],
)

print(response)


Expected Output:
{
    'jobQueues': [
        {
            'computeEnvironmentOrder': [
                {
                    'computeEnvironment': 'arn:aws:batch:us-east-1:012345678910:compute-environment/C4OnDemand',
                    'order': 1,
                },
            ],
            'jobQueueArn': 'arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority',
            'jobQueueName': 'HighPriority',
            'priority': 1,
            'state': 'ENABLED',
            'status': 'VALID',
            'statusReason': 'JobQueue Healthy',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    Batch.Client.exceptions.ClientException
    Batch.Client.exceptions.ServerException
    
    """
    pass

def describe_jobs(jobs=None):
    """
    Describes a list of AWS Batch jobs.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes a job with the specified job ID.
    Expected Output:
    
    :example: response = client.describe_jobs(
        jobs=[
            'string',
        ]
    )
    
    
    :type jobs: list
    :param jobs: [REQUIRED]\nA list of up to 100 job IDs.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
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
                        'reason': 'string',
                        'logStreamName': 'string',
                        'networkInterfaces': [
                            {
                                'attachmentId': 'string',
                                'ipv6Address': 'string',
                                'privateIpv4Address': 'string'
                            },
                        ]
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
                    'jobId': 'string',
                    'type': 'N_TO_N'|'SEQUENTIAL'
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
                'taskArn': 'string',
                'logStreamName': 'string',
                'instanceType': 'string',
                'networkInterfaces': [
                    {
                        'attachmentId': 'string',
                        'ipv6Address': 'string',
                        'privateIpv4Address': 'string'
                    },
                ],
                'resourceRequirements': [
                    {
                        'value': 'string',
                        'type': 'GPU'
                    },
                ],
                'linuxParameters': {
                    'devices': [
                        {
                            'hostPath': 'string',
                            'containerPath': 'string',
                            'permissions': [
                                'READ'|'WRITE'|'MKNOD',
                            ]
                        },
                    ]
                }
            },
            'nodeDetails': {
                'nodeIndex': 123,
                'isMainNode': True|False
            },
            'nodeProperties': {
                'numNodes': 123,
                'mainNode': 123,
                'nodeRangeProperties': [
                    {
                        'targetNodes': 'string',
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
                            'privileged': True|False,
                            'ulimits': [
                                {
                                    'hardLimit': 123,
                                    'name': 'string',
                                    'softLimit': 123
                                },
                            ],
                            'user': 'string',
                            'instanceType': 'string',
                            'resourceRequirements': [
                                {
                                    'value': 'string',
                                    'type': 'GPU'
                                },
                            ],
                            'linuxParameters': {
                                'devices': [
                                    {
                                        'hostPath': 'string',
                                        'containerPath': 'string',
                                        'permissions': [
                                            'READ'|'WRITE'|'MKNOD',
                                        ]
                                    },
                                ]
                            }
                        }
                    },
                ]
            },
            'arrayProperties': {
                'statusSummary': {
                    'string': 123
                },
                'size': 123,
                'index': 123
            },
            'timeout': {
                'attemptDurationSeconds': 123
            }
        },
    ]
}


Response Structure

(dict) --
jobs (list) --The list of jobs.

(dict) --An object representing an AWS Batch job.

jobName (string) --The name of the job.

jobId (string) --The ID for the job.

jobQueue (string) --The Amazon Resource Name (ARN) of the job queue with which the job is associated.

status (string) --The current status for the job.

Note
If your jobs do not progress to STARTING , see Jobs Stuck in RUNNABLE Status in the troubleshooting section of the AWS Batch User Guide .


attempts (list) --A list of job attempts associated with this job.

(dict) --An object representing a job attempt.

container (dict) --Details about the container in this job attempt.

containerInstanceArn (string) --The Amazon Resource Name (ARN) of the Amazon ECS container instance that hosts the job attempt.

taskArn (string) --The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the job attempt. Each container attempt receives a task ARN when they reach the STARTING status.

exitCode (integer) --The exit code for the job attempt. A non-zero exit code is considered a failure.

reason (string) --A short (255 max characters) human-readable string to provide additional details about a running or stopped container.

logStreamName (string) --The name of the CloudWatch Logs log stream associated with the container. The log group for AWS Batch jobs is /aws/batch/job . Each container attempt receives a log stream name when they reach the RUNNING status.

networkInterfaces (list) --The network interfaces associated with the job attempt.

(dict) --An object representing the elastic network interface for a multi-node parallel job node.

attachmentId (string) --The attachment ID for the network interface.

ipv6Address (string) --The private IPv6 address for the network interface.

privateIpv4Address (string) --The private IPv4 address for the network interface.







startedAt (integer) --The Unix timestamp (in seconds and milliseconds) for when the attempt was started (when the attempt transitioned from the STARTING state to the RUNNING state).

stoppedAt (integer) --The Unix timestamp (in seconds and milliseconds) for when the attempt was stopped (when the attempt transitioned from the RUNNING state to a terminal state, such as SUCCEEDED or FAILED ).

statusReason (string) --A short, human-readable string to provide additional details about the current status of the job attempt.





statusReason (string) --A short, human-readable string to provide additional details about the current status of the job.

createdAt (integer) --The Unix timestamp (in seconds and milliseconds) for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the SUBMITTED state (at the time  SubmitJob was called). For array child jobs, this is when the child job was spawned by its parent and entered the PENDING state.

retryStrategy (dict) --The retry strategy to use for this job if an attempt fails.

attempts (integer) --The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If the value of attempts is greater than one, the job is retried on failure the same number of attempts as the value.



startedAt (integer) --The Unix timestamp (in seconds and milliseconds) for when the job was started (when the job transitioned from the STARTING state to the RUNNING state).

stoppedAt (integer) --The Unix timestamp (in seconds and milliseconds) for when the job was stopped (when the job transitioned from the RUNNING state to a terminal state, such as SUCCEEDED or FAILED ).

dependsOn (list) --A list of job IDs on which this job depends.

(dict) --An object representing an AWS Batch job dependency.

jobId (string) --The job ID of the AWS Batch job associated with this dependency.

type (string) --The type of the job dependency.





jobDefinition (string) --The job definition that is used by this job.

parameters (dict) --Additional parameters passed to the job that replace parameter substitution placeholders or override any corresponding parameter defaults from the job definition.

(string) --
(string) --




container (dict) --An object representing the details of the container that is associated with the job.

image (string) --The image used to start the container.

vcpus (integer) --The number of VCPUs allocated for the job.

memory (integer) --The number of MiB of memory reserved for the job.

command (list) --The command that is passed to the container.

(string) --


jobRoleArn (string) --The Amazon Resource Name (ARN) associated with the job upon execution.

volumes (list) --A list of volumes associated with the job.

(dict) --A data volume used in a job\'s container properties.

host (dict) --The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.

sourcePath (string) --The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.



name (string) --The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .





environment (list) --The environment variables to pass to a container.

Note
Environment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.


(dict) --A key-value pair object.

name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.

value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.





mountPoints (list) --The mount points for data volumes in your container.

(dict) --Details on a Docker volume mount point that is used in a job\'s container properties. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run.

containerPath (string) --The path on the container at which to mount the host volume.

readOnly (boolean) --If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false .

sourceVolume (string) --The name of the volume to mount.





readonlyRootFilesystem (boolean) --When this parameter is true, the container is given read-only access to its root file system.

ulimits (list) --A list of ulimit values to set in the container.

(dict) --The ulimit settings to pass to the container.

hardLimit (integer) --The hard limit for the ulimit type.

name (string) --The type of the ulimit .

softLimit (integer) --The soft limit for the ulimit type.





privileged (boolean) --When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user).

user (string) --The user name to use inside the container.

exitCode (integer) --The exit code to return upon completion.

reason (string) --A short (255 max characters) human-readable string to provide additional details about a running or stopped container.

containerInstanceArn (string) --The Amazon Resource Name (ARN) of the container instance on which the container is running.

taskArn (string) --The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the container job. Each container attempt receives a task ARN when they reach the STARTING status.

logStreamName (string) --The name of the CloudWatch Logs log stream associated with the container. The log group for AWS Batch jobs is /aws/batch/job . Each container attempt receives a log stream name when they reach the RUNNING status.

instanceType (string) --The instance type of the underlying host infrastructure of a multi-node parallel job.

networkInterfaces (list) --The network interfaces associated with the job.

(dict) --An object representing the elastic network interface for a multi-node parallel job node.

attachmentId (string) --The attachment ID for the network interface.

ipv6Address (string) --The private IPv6 address for the network interface.

privateIpv4Address (string) --The private IPv4 address for the network interface.





resourceRequirements (list) --The type and amount of a resource to assign to a container. Currently, the only supported resource is GPU .

(dict) --The type and amount of a resource to assign to a container. Currently, the only supported resource type is GPU .

value (string) --The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.

type (string) --The type of resource to assign to a container. Currently, the only supported resource type is GPU .





linuxParameters (dict) --Linux-specific modifications that are applied to the container, such as details for device mappings.

devices (list) --Any host devices to expose to the container. This parameter maps to Devices in the Create a container section of the Docker Remote API and the --device option to docker run .

(dict) --An object representing a container instance host device.

hostPath (string) --The path for the device on the host container instance.

containerPath (string) --The path inside the container at which to expose the host device. By default the hostPath value is used.

permissions (list) --The explicit permissions to provide to the container for the device. By default, the container has permissions for read , write , and mknod for the device.

(string) --










nodeDetails (dict) --An object representing the details of a node that is associated with a multi-node parallel job.

nodeIndex (integer) --The node index for the node. Node index numbering begins at zero. This index is also available on the node with the AWS_BATCH_JOB_NODE_INDEX environment variable.

isMainNode (boolean) --Specifies whether the current node is the main node for a multi-node parallel job.



nodeProperties (dict) --An object representing the node properties of a multi-node parallel job.

numNodes (integer) --The number of nodes associated with a multi-node parallel job.

mainNode (integer) --Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.

nodeRangeProperties (list) --A list of node ranges and their properties associated with a multi-node parallel job.

(dict) --An object representing the properties of the node range for a multi-node parallel job.

targetNodes (string) --The range of nodes, using node index values. A range of 0:3 indicates nodes with index values of 0 through 3 . If the starting range value is omitted (:n ), then 0 is used to start the range. If the ending range value is omitted (n: ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes (0:n). You may nest node ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override the 0:10 properties.

container (dict) --The container details for the node range.

image (string) --The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` repository-url /image :tag `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .

Images in Amazon ECR repositories use the full registry and repository URI (for example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name> ).
Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).


vcpus (integer) --The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.

memory (integer) --The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run . You must specify at least 4 MiB of memory for a job.

Note
If you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see Memory Management in the AWS Batch User Guide .


command (list) --The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd .

(string) --


jobRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.

volumes (list) --A list of data volumes used in a job.

(dict) --A data volume used in a job\'s container properties.

host (dict) --The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.

sourcePath (string) --The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.



name (string) --The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .





environment (list) --The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .

Warning
We do not recommend using plaintext environment variables for sensitive information, such as credential data.


Note
Environment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.


(dict) --A key-value pair object.

name (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.

value (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.





mountPoints (list) --The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .

(dict) --Details on a Docker volume mount point that is used in a job\'s container properties. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run.

containerPath (string) --The path on the container at which to mount the host volume.

readOnly (boolean) --If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false .

sourceVolume (string) --The name of the volume to mount.





readonlyRootFilesystem (boolean) --When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .

privileged (boolean) --When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .

ulimits (list) --A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run .

(dict) --The ulimit settings to pass to the container.

hardLimit (integer) --The hard limit for the ulimit type.

name (string) --The type of the ulimit .

softLimit (integer) --The soft limit for the ulimit type.





user (string) --The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .

instanceType (string) --The instance type to use for a multi-node parallel job. Currently all node groups in a multi-node parallel job must use the same instance type. This parameter is not valid for single-node container jobs.

resourceRequirements (list) --The type and amount of a resource to assign to a container. Currently, the only supported resource is GPU .

(dict) --The type and amount of a resource to assign to a container. Currently, the only supported resource type is GPU .

value (string) --The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.

type (string) --The type of resource to assign to a container. Currently, the only supported resource type is GPU .





linuxParameters (dict) --Linux-specific modifications that are applied to the container, such as details for device mappings.

devices (list) --Any host devices to expose to the container. This parameter maps to Devices in the Create a container section of the Docker Remote API and the --device option to docker run .

(dict) --An object representing a container instance host device.

hostPath (string) --The path for the device on the host container instance.

containerPath (string) --The path inside the container at which to expose the host device. By default the hostPath value is used.

permissions (list) --The explicit permissions to provide to the container for the device. By default, the container has permissions for read , write , and mknod for the device.

(string) --
















arrayProperties (dict) --The array properties of the job, if it is an array job.

statusSummary (dict) --A summary of the number of array job children in each available job status. This parameter is returned for parent array jobs.

(string) --
(integer) --




size (integer) --The size of the array job. This parameter is returned for parent array jobs.

index (integer) --The job index within the array that is associated with this job. This parameter is returned for array job children.



timeout (dict) --The timeout configuration for the job.

attemptDurationSeconds (integer) --The time duration in seconds (measured from the job attempt\'s startedAt timestamp) after which AWS Batch terminates your jobs if they have not finished.












Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example describes a job with the specified job ID.
response = client.describe_jobs(
    jobs=[
        '24fa2d7a-64c4-49d2-8b47-f8da4fbde8e9',
    ],
)

print(response)


Expected Output:
{
    'jobs': [
        {
            'container': {
                'command': [
                    'sleep',
                    '60',
                ],
                'containerInstanceArn': 'arn:aws:ecs:us-east-1:012345678910:container-instance/5406d7cd-58bd-4b8f-9936-48d7c6b1526c',
                'environment': [
                ],
                'exitCode': 0,
                'image': 'busybox',
                'memory': 128,
                'mountPoints': [
                ],
                'ulimits': [
                ],
                'vcpus': 1,
                'volumes': [
                ],
            },
            'createdAt': 1480460782010,
            'dependsOn': [
            ],
            'jobDefinition': 'sleep60',
            'jobId': '24fa2d7a-64c4-49d2-8b47-f8da4fbde8e9',
            'jobName': 'example',
            'jobQueue': 'arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority',
            'parameters': {
            },
            'startedAt': 1480460816500,
            'status': 'SUCCEEDED',
            'stoppedAt': 1480460880699,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                            'reason': 'string',
                            'logStreamName': 'string',
                            'networkInterfaces': [
                                {
                                    'attachmentId': 'string',
                                    'ipv6Address': 'string',
                                    'privateIpv4Address': 'string'
                                },
                            ]
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
                        'jobId': 'string',
                        'type': 'N_TO_N'|'SEQUENTIAL'
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
                    'taskArn': 'string',
                    'logStreamName': 'string',
                    'instanceType': 'string',
                    'networkInterfaces': [
                        {
                            'attachmentId': 'string',
                            'ipv6Address': 'string',
                            'privateIpv4Address': 'string'
                        },
                    ],
                    'resourceRequirements': [
                        {
                            'value': 'string',
                            'type': 'GPU'
                        },
                    ],
                    'linuxParameters': {
                        'devices': [
                            {
                                'hostPath': 'string',
                                'containerPath': 'string',
                                'permissions': [
                                    'READ'|'WRITE'|'MKNOD',
                                ]
                            },
                        ]
                    }
                },
                'nodeDetails': {
                    'nodeIndex': 123,
                    'isMainNode': True|False
                },
                'nodeProperties': {
                    'numNodes': 123,
                    'mainNode': 123,
                    'nodeRangeProperties': [
                        {
                            'targetNodes': 'string',
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
                                'privileged': True|False,
                                'ulimits': [
                                    {
                                        'hardLimit': 123,
                                        'name': 'string',
                                        'softLimit': 123
                                    },
                                ],
                                'user': 'string',
                                'instanceType': 'string',
                                'resourceRequirements': [
                                    {
                                        'value': 'string',
                                        'type': 'GPU'
                                    },
                                ],
                                'linuxParameters': {
                                    'devices': [
                                        {
                                            'hostPath': 'string',
                                            'containerPath': 'string',
                                            'permissions': [
                                                'READ'|'WRITE'|'MKNOD',
                                            ]
                                        },
                                    ]
                                }
                            }
                        },
                    ]
                },
                'arrayProperties': {
                    'statusSummary': {
                        'string': 123
                    },
                    'size': 123,
                    'index': 123
                },
                'timeout': {
                    'attemptDurationSeconds': 123
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

def list_jobs(jobQueue=None, arrayJobId=None, multiNodeJobId=None, jobStatus=None, maxResults=None, nextToken=None):
    """
    Returns a list of AWS Batch jobs.
    You must specify only one of the following:
    You can filter the results by job status with the jobStatus parameter. If you do not specify a status, only RUNNING jobs are returned.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example lists the running jobs in the HighPriority job queue.
    Expected Output:
    This example lists jobs in the HighPriority job queue that are in the SUBMITTED job status.
    Expected Output:
    
    :example: response = client.list_jobs(
        jobQueue='string',
        arrayJobId='string',
        multiNodeJobId='string',
        jobStatus='SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type jobQueue: string
    :param jobQueue: The name or full Amazon Resource Name (ARN) of the job queue with which to list jobs.

    :type arrayJobId: string
    :param arrayJobId: The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.

    :type multiNodeJobId: string
    :param multiNodeJobId: The job ID for a multi-node parallel job. Specifying a multi-node parallel job ID with this parameter lists all nodes that are associated with the specified job.

    :type jobStatus: string
    :param jobStatus: The job status with which to filter jobs in the specified queue. If you do not specify a status, only RUNNING jobs are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of results returned by ListJobs in paginated output. When this parameter is used, ListJobs only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListJobs request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListJobs returns up to 100 results and a nextToken value if applicable.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListJobs request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobSummaryList': [
        {
            'jobId': 'string',
            'jobName': 'string',
            'createdAt': 123,
            'status': 'SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
            'statusReason': 'string',
            'startedAt': 123,
            'stoppedAt': 123,
            'container': {
                'exitCode': 123,
                'reason': 'string'
            },
            'arrayProperties': {
                'size': 123,
                'index': 123
            },
            'nodeProperties': {
                'isMainNode': True|False,
                'numNodes': 123,
                'nodeIndex': 123
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

jobSummaryList (list) --
A list of job summaries that match the request.

(dict) --
An object representing summary details of a job.

jobId (string) --
The ID of the job.

jobName (string) --
The name of the job.

createdAt (integer) --
The Unix timestamp for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the SUBMITTED state (at the time  SubmitJob was called). For array child jobs, this is when the child job was spawned by its parent and entered the PENDING state.

status (string) --
The current status for the job.

statusReason (string) --
A short, human-readable string to provide additional details about the current status of the job.

startedAt (integer) --
The Unix timestamp for when the job was started (when the job transitioned from the STARTING state to the RUNNING state).

stoppedAt (integer) --
The Unix timestamp for when the job was stopped (when the job transitioned from the RUNNING state to a terminal state, such as SUCCEEDED or FAILED ).

container (dict) --
An object representing the details of the container that is associated with the job.

exitCode (integer) --
The exit code to return upon completion.

reason (string) --
A short (255 max characters) human-readable string to provide additional details about a running or stopped container.



arrayProperties (dict) --
The array properties of the job, if it is an array job.

size (integer) --
The size of the array job. This parameter is returned for parent array jobs.

index (integer) --
The job index within the array that is associated with this job. This parameter is returned for children of array jobs.



nodeProperties (dict) --
The node properties for a single node in a job summary list.

isMainNode (boolean) --
Specifies whether the current node is the main node for a multi-node parallel job.

numNodes (integer) --
The number of nodes associated with a multi-node parallel job.

nodeIndex (integer) --
The node index for the node. Node index numbering begins at zero. This index is also available on the node with the AWS_BATCH_JOB_NODE_INDEX environment variable.







nextToken (string) --
The nextToken value to include in a future ListJobs request. When the results of a ListJobs request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example lists the running jobs in the HighPriority job queue.
response = client.list_jobs(
    jobQueue='HighPriority',
)

print(response)


Expected Output:
{
    'jobSummaryList': [
        {
            'jobId': 'e66ff5fd-a1ff-4640-b1a2-0b0a142f49bb',
            'jobName': 'example',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}


This example lists jobs in the HighPriority job queue that are in the SUBMITTED job status.
response = client.list_jobs(
    jobQueue='HighPriority',
    jobStatus='SUBMITTED',
)

print(response)


Expected Output:
{
    'jobSummaryList': [
        {
            'jobId': '68f0c163-fbd4-44e6-9fd1-25b14a434786',
            'jobName': 'example',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'jobSummaryList': [
            {
                'jobId': 'string',
                'jobName': 'string',
                'createdAt': 123,
                'status': 'SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
                'statusReason': 'string',
                'startedAt': 123,
                'stoppedAt': 123,
                'container': {
                    'exitCode': 123,
                    'reason': 'string'
                },
                'arrayProperties': {
                    'size': 123,
                    'index': 123
                },
                'nodeProperties': {
                    'isMainNode': True|False,
                    'numNodes': 123,
                    'nodeIndex': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    jobQueue (string) -- The name or full Amazon Resource Name (ARN) of the job queue with which to list jobs.
    arrayJobId (string) -- The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.
    multiNodeJobId (string) -- The job ID for a multi-node parallel job. Specifying a multi-node parallel job ID with this parameter lists all nodes that are associated with the specified job.
    jobStatus (string) -- The job status with which to filter jobs in the specified queue. If you do not specify a status, only RUNNING jobs are returned.
    maxResults (integer) -- The maximum number of results returned by ListJobs in paginated output. When this parameter is used, ListJobs only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListJobs request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListJobs returns up to 100 results and a nextToken value if applicable.
    nextToken (string) -- The nextToken value returned from a previous paginated ListJobs request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value. This value is null when there are no more results to return.
    
    Note
    This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
    
    
    
    """
    pass

def register_job_definition(jobDefinitionName=None, type=None, parameters=None, containerProperties=None, nodeProperties=None, retryStrategy=None, timeout=None):
    """
    Registers an AWS Batch job definition.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example registers a job definition for a simple container job.
    Expected Output:
    
    :example: response = client.register_job_definition(
        jobDefinitionName='string',
        type='container'|'multinode',
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
            'user': 'string',
            'instanceType': 'string',
            'resourceRequirements': [
                {
                    'value': 'string',
                    'type': 'GPU'
                },
            ],
            'linuxParameters': {
                'devices': [
                    {
                        'hostPath': 'string',
                        'containerPath': 'string',
                        'permissions': [
                            'READ'|'WRITE'|'MKNOD',
                        ]
                    },
                ]
            }
        },
        nodeProperties={
            'numNodes': 123,
            'mainNode': 123,
            'nodeRangeProperties': [
                {
                    'targetNodes': 'string',
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
                        'privileged': True|False,
                        'ulimits': [
                            {
                                'hardLimit': 123,
                                'name': 'string',
                                'softLimit': 123
                            },
                        ],
                        'user': 'string',
                        'instanceType': 'string',
                        'resourceRequirements': [
                            {
                                'value': 'string',
                                'type': 'GPU'
                            },
                        ],
                        'linuxParameters': {
                            'devices': [
                                {
                                    'hostPath': 'string',
                                    'containerPath': 'string',
                                    'permissions': [
                                        'READ'|'WRITE'|'MKNOD',
                                    ]
                                },
                            ]
                        }
                    }
                },
            ]
        },
        retryStrategy={
            'attempts': 123
        },
        timeout={
            'attemptDurationSeconds': 123
        }
    )
    
    
    :type jobDefinitionName: string
    :param jobDefinitionName: [REQUIRED]\nThe name of the job definition to register. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.\n

    :type type: string
    :param type: [REQUIRED]\nThe type of job definition.\n

    :type parameters: dict
    :param parameters: Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a SubmitJob request override any corresponding parameter defaults from the job definition.\n\n(string) --\n(string) --\n\n\n\n

    :type containerProperties: dict
    :param containerProperties: An object with various properties specific to single-node container-based jobs. If the job definition\'s type parameter is container , then you must specify either containerProperties or nodeProperties .\n\nimage (string) --The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` repository-url /image :tag `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .\n\nImages in Amazon ECR repositories use the full registry and repository URI (for example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name> ).\nImages in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).\nImages in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).\nImages in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).\n\n\nvcpus (integer) --The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.\n\nmemory (integer) --The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run . You must specify at least 4 MiB of memory for a job.\n\nNote\nIf you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see Memory Management in the AWS Batch User Guide .\n\n\ncommand (list) --The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd .\n\n(string) --\n\n\njobRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.\n\nvolumes (list) --A list of data volumes used in a job.\n\n(dict) --A data volume used in a job\'s container properties.\n\nhost (dict) --The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.\n\nsourcePath (string) --The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.\n\n\n\nname (string) --The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .\n\n\n\n\n\nenvironment (list) --The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .\n\nWarning\nWe do not recommend using plaintext environment variables for sensitive information, such as credential data.\n\n\nNote\nEnvironment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.\n\n\n(dict) --A key-value pair object.\n\nname (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.\n\nvalue (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.\n\n\n\n\n\nmountPoints (list) --The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .\n\n(dict) --Details on a Docker volume mount point that is used in a job\'s container properties. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run.\n\ncontainerPath (string) --The path on the container at which to mount the host volume.\n\nreadOnly (boolean) --If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false .\n\nsourceVolume (string) --The name of the volume to mount.\n\n\n\n\n\nreadonlyRootFilesystem (boolean) --When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .\n\nprivileged (boolean) --When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .\n\nulimits (list) --A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run .\n\n(dict) --The ulimit settings to pass to the container.\n\nhardLimit (integer) -- [REQUIRED]The hard limit for the ulimit type.\n\nname (string) -- [REQUIRED]The type of the ulimit .\n\nsoftLimit (integer) -- [REQUIRED]The soft limit for the ulimit type.\n\n\n\n\n\nuser (string) --The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .\n\ninstanceType (string) --The instance type to use for a multi-node parallel job. Currently all node groups in a multi-node parallel job must use the same instance type. This parameter is not valid for single-node container jobs.\n\nresourceRequirements (list) --The type and amount of a resource to assign to a container. Currently, the only supported resource is GPU .\n\n(dict) --The type and amount of a resource to assign to a container. Currently, the only supported resource type is GPU .\n\nvalue (string) -- [REQUIRED]The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.\n\ntype (string) -- [REQUIRED]The type of resource to assign to a container. Currently, the only supported resource type is GPU .\n\n\n\n\n\nlinuxParameters (dict) --Linux-specific modifications that are applied to the container, such as details for device mappings.\n\ndevices (list) --Any host devices to expose to the container. This parameter maps to Devices in the Create a container section of the Docker Remote API and the --device option to docker run .\n\n(dict) --An object representing a container instance host device.\n\nhostPath (string) -- [REQUIRED]The path for the device on the host container instance.\n\ncontainerPath (string) --The path inside the container at which to expose the host device. By default the hostPath value is used.\n\npermissions (list) --The explicit permissions to provide to the container for the device. By default, the container has permissions for read , write , and mknod for the device.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type nodeProperties: dict
    :param nodeProperties: An object with various properties specific to multi-node parallel jobs. If you specify node properties for a job, it becomes a multi-node parallel job. For more information, see Multi-node Parallel Jobs in the AWS Batch User Guide . If the job definition\'s type parameter is container , then you must specify either containerProperties or nodeProperties .\n\nnumNodes (integer) -- [REQUIRED]The number of nodes associated with a multi-node parallel job.\n\nmainNode (integer) -- [REQUIRED]Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.\n\nnodeRangeProperties (list) -- [REQUIRED]A list of node ranges and their properties associated with a multi-node parallel job.\n\n(dict) --An object representing the properties of the node range for a multi-node parallel job.\n\ntargetNodes (string) -- [REQUIRED]The range of nodes, using node index values. A range of 0:3 indicates nodes with index values of 0 through 3 . If the starting range value is omitted (:n ), then 0 is used to start the range. If the ending range value is omitted (n: ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes (0:n). You may nest node ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override the 0:10 properties.\n\ncontainer (dict) --The container details for the node range.\n\nimage (string) --The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` repository-url /image :tag `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .\n\nImages in Amazon ECR repositories use the full registry and repository URI (for example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name> ).\nImages in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).\nImages in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).\nImages in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).\n\n\nvcpus (integer) --The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.\n\nmemory (integer) --The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run . You must specify at least 4 MiB of memory for a job.\n\nNote\nIf you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see Memory Management in the AWS Batch User Guide .\n\n\ncommand (list) --The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd .\n\n(string) --\n\n\njobRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.\n\nvolumes (list) --A list of data volumes used in a job.\n\n(dict) --A data volume used in a job\'s container properties.\n\nhost (dict) --The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.\n\nsourcePath (string) --The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.\n\n\n\nname (string) --The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints .\n\n\n\n\n\nenvironment (list) --The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .\n\nWarning\nWe do not recommend using plaintext environment variables for sensitive information, such as credential data.\n\n\nNote\nEnvironment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.\n\n\n(dict) --A key-value pair object.\n\nname (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.\n\nvalue (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.\n\n\n\n\n\nmountPoints (list) --The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .\n\n(dict) --Details on a Docker volume mount point that is used in a job\'s container properties. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run.\n\ncontainerPath (string) --The path on the container at which to mount the host volume.\n\nreadOnly (boolean) --If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false .\n\nsourceVolume (string) --The name of the volume to mount.\n\n\n\n\n\nreadonlyRootFilesystem (boolean) --When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .\n\nprivileged (boolean) --When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .\n\nulimits (list) --A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run .\n\n(dict) --The ulimit settings to pass to the container.\n\nhardLimit (integer) -- [REQUIRED]The hard limit for the ulimit type.\n\nname (string) -- [REQUIRED]The type of the ulimit .\n\nsoftLimit (integer) -- [REQUIRED]The soft limit for the ulimit type.\n\n\n\n\n\nuser (string) --The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .\n\ninstanceType (string) --The instance type to use for a multi-node parallel job. Currently all node groups in a multi-node parallel job must use the same instance type. This parameter is not valid for single-node container jobs.\n\nresourceRequirements (list) --The type and amount of a resource to assign to a container. Currently, the only supported resource is GPU .\n\n(dict) --The type and amount of a resource to assign to a container. Currently, the only supported resource type is GPU .\n\nvalue (string) -- [REQUIRED]The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.\n\ntype (string) -- [REQUIRED]The type of resource to assign to a container. Currently, the only supported resource type is GPU .\n\n\n\n\n\nlinuxParameters (dict) --Linux-specific modifications that are applied to the container, such as details for device mappings.\n\ndevices (list) --Any host devices to expose to the container. This parameter maps to Devices in the Create a container section of the Docker Remote API and the --device option to docker run .\n\n(dict) --An object representing a container instance host device.\n\nhostPath (string) -- [REQUIRED]The path for the device on the host container instance.\n\ncontainerPath (string) --The path inside the container at which to expose the host device. By default the hostPath value is used.\n\npermissions (list) --The explicit permissions to provide to the container for the device. By default, the container has permissions for read , write , and mknod for the device.\n\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type retryStrategy: dict
    :param retryStrategy: The retry strategy to use for failed jobs that are submitted with this job definition. Any retry strategy that is specified during a SubmitJob operation overrides the retry strategy defined here. If a job is terminated due to a timeout, it is not retried.\n\nattempts (integer) --The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If the value of attempts is greater than one, the job is retried on failure the same number of attempts as the value.\n\n\n

    :type timeout: dict
    :param timeout: The timeout configuration for jobs that are submitted with this job definition, after which AWS Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it is not retried. The minimum value for the timeout is 60 seconds. Any timeout configuration that is specified during a SubmitJob operation overrides the timeout configuration defined here. For more information, see Job Timeouts in the Amazon Elastic Container Service Developer Guide .\n\nattemptDurationSeconds (integer) --The time duration in seconds (measured from the job attempt\'s startedAt timestamp) after which AWS Batch terminates your jobs if they have not finished.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobDefinitionName': 'string',
    'jobDefinitionArn': 'string',
    'revision': 123
}


Response Structure

(dict) --

jobDefinitionName (string) --
The name of the job definition.

jobDefinitionArn (string) --
The Amazon Resource Name (ARN) of the job definition.

revision (integer) --
The revision of the job definition.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example registers a job definition for a simple container job.
response = client.register_job_definition(
    type='container',
    containerProperties={
        'command': [
            'sleep',
            '10',
        ],
        'image': 'busybox',
        'memory': 128,
        'vcpus': 1,
    },
    jobDefinitionName='sleep10',
)

print(response)


Expected Output:
{
    'jobDefinitionArn': 'arn:aws:batch:us-east-1:012345678910:job-definition/sleep10:1',
    'jobDefinitionName': 'sleep10',
    'revision': 1,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'jobDefinitionName': 'string',
        'jobDefinitionArn': 'string',
        'revision': 123
    }
    
    
    :returns: 
    Batch.Client.exceptions.ClientException
    Batch.Client.exceptions.ServerException
    
    """
    pass

def submit_job(jobName=None, jobQueue=None, arrayProperties=None, dependsOn=None, jobDefinition=None, parameters=None, containerOverrides=None, nodeOverrides=None, retryStrategy=None, timeout=None):
    """
    Submits an AWS Batch job from a job definition. Parameters specified during  SubmitJob override parameters defined in the job definition.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example submits a simple container job called example to the HighPriority job queue.
    Expected Output:
    
    :example: response = client.submit_job(
        jobName='string',
        jobQueue='string',
        arrayProperties={
            'size': 123
        },
        dependsOn=[
            {
                'jobId': 'string',
                'type': 'N_TO_N'|'SEQUENTIAL'
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
            'instanceType': 'string',
            'environment': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'resourceRequirements': [
                {
                    'value': 'string',
                    'type': 'GPU'
                },
            ]
        },
        nodeOverrides={
            'numNodes': 123,
            'nodePropertyOverrides': [
                {
                    'targetNodes': 'string',
                    'containerOverrides': {
                        'vcpus': 123,
                        'memory': 123,
                        'command': [
                            'string',
                        ],
                        'instanceType': 'string',
                        'environment': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'resourceRequirements': [
                            {
                                'value': 'string',
                                'type': 'GPU'
                            },
                        ]
                    }
                },
            ]
        },
        retryStrategy={
            'attempts': 123
        },
        timeout={
            'attemptDurationSeconds': 123
        }
    )
    
    
    :type jobName: string
    :param jobName: [REQUIRED]\nThe name of the job. The first character must be alphanumeric, and up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.\n

    :type jobQueue: string
    :param jobQueue: [REQUIRED]\nThe job queue into which the job is submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue.\n

    :type arrayProperties: dict
    :param arrayProperties: The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For more information, see Array Jobs in the AWS Batch User Guide .\n\nsize (integer) --The size of the array job.\n\n\n

    :type dependsOn: list
    :param dependsOn: A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a SEQUENTIAL type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an N_TO_N type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.\n\n(dict) --An object representing an AWS Batch job dependency.\n\njobId (string) --The job ID of the AWS Batch job associated with this dependency.\n\ntype (string) --The type of the job dependency.\n\n\n\n\n

    :type jobDefinition: string
    :param jobDefinition: [REQUIRED]\nThe job definition used by this job. This value can be one of name , name:revision , or the Amazon Resource Name (ARN) for the job definition. If name is specified without a revision then the latest active revision is used.\n

    :type parameters: dict
    :param parameters: Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters in a SubmitJob request override any corresponding parameter defaults from the job definition.\n\n(string) --\n(string) --\n\n\n\n

    :type containerOverrides: dict
    :param containerOverrides: A list of container overrides in JSON format that specify the name of a container in the specified job definition and the overrides it should receive. You can override the default command for a container (that is specified in the job definition or the Docker image) with a command override. You can also override existing environment variables (that are specified in the job definition or Docker image) on a container or add new environment variables to it with an environment override.\n\nvcpus (integer) --The number of vCPUs to reserve for the container. This value overrides the value set in the job definition.\n\nmemory (integer) --The number of MiB of memory reserved for the job. This value overrides the value set in the job definition.\n\ncommand (list) --The command to send to the container that overrides the default command from the Docker image or the job definition.\n\n(string) --\n\n\ninstanceType (string) --The instance type to use for a multi-node parallel job. This parameter is not valid for single-node container jobs.\n\nenvironment (list) --The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.\n\nNote\nEnvironment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.\n\n\n(dict) --A key-value pair object.\n\nname (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.\n\nvalue (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.\n\n\n\n\n\nresourceRequirements (list) --The type and amount of a resource to assign to a container. This value overrides the value set in the job definition. Currently, the only supported resource is GPU .\n\n(dict) --The type and amount of a resource to assign to a container. Currently, the only supported resource type is GPU .\n\nvalue (string) -- [REQUIRED]The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.\n\ntype (string) -- [REQUIRED]The type of resource to assign to a container. Currently, the only supported resource type is GPU .\n\n\n\n\n\n\n

    :type nodeOverrides: dict
    :param nodeOverrides: A list of node overrides in JSON format that specify the node range to target and the container overrides for that node range.\n\nnumNodes (integer) --The number of nodes to use with a multi-node parallel job. This value overrides the number of nodes that are specified in the job definition. To use this override:\n\nThere must be at least one node range in your job definition that has an open upper boundary (such as : or n: ).\nThe lower boundary of the node range specified in the job definition must be fewer than the number of nodes specified in the override.\nThe main node index specified in the job definition must be fewer than the number of nodes specified in the override.\n\n\nnodePropertyOverrides (list) --The node property overrides for the job.\n\n(dict) --Object representing any node overrides to a job definition that is used in a SubmitJob API operation.\n\ntargetNodes (string) -- [REQUIRED]The range of nodes, using node index values, with which to override. A range of 0:3 indicates nodes with index values of 0 through 3 . If the starting range value is omitted (:n ), then 0 is used to start the range. If the ending range value is omitted (n: ), then the highest possible node index is used to end the range.\n\ncontainerOverrides (dict) --The overrides that should be sent to a node range.\n\nvcpus (integer) --The number of vCPUs to reserve for the container. This value overrides the value set in the job definition.\n\nmemory (integer) --The number of MiB of memory reserved for the job. This value overrides the value set in the job definition.\n\ncommand (list) --The command to send to the container that overrides the default command from the Docker image or the job definition.\n\n(string) --\n\n\ninstanceType (string) --The instance type to use for a multi-node parallel job. This parameter is not valid for single-node container jobs.\n\nenvironment (list) --The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.\n\nNote\nEnvironment variables must not start with AWS_BATCH ; this naming convention is reserved for variables that are set by the AWS Batch service.\n\n\n(dict) --A key-value pair object.\n\nname (string) --The name of the key-value pair. For environment variables, this is the name of the environment variable.\n\nvalue (string) --The value of the key-value pair. For environment variables, this is the value of the environment variable.\n\n\n\n\n\nresourceRequirements (list) --The type and amount of a resource to assign to a container. This value overrides the value set in the job definition. Currently, the only supported resource is GPU .\n\n(dict) --The type and amount of a resource to assign to a container. Currently, the only supported resource type is GPU .\n\nvalue (string) -- [REQUIRED]The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.\n\ntype (string) -- [REQUIRED]The type of resource to assign to a container. Currently, the only supported resource type is GPU .\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type retryStrategy: dict
    :param retryStrategy: The retry strategy to use for failed jobs from this SubmitJob operation. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.\n\nattempts (integer) --The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If the value of attempts is greater than one, the job is retried on failure the same number of attempts as the value.\n\n\n

    :type timeout: dict
    :param timeout: The timeout configuration for this SubmitJob operation. You can specify a timeout duration after which AWS Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it is not retried. The minimum value for the timeout is 60 seconds. This configuration overrides any timeout configuration specified in the job definition. For array jobs, child jobs have the same timeout configuration as the parent job. For more information, see Job Timeouts in the Amazon Elastic Container Service Developer Guide .\n\nattemptDurationSeconds (integer) --The time duration in seconds (measured from the job attempt\'s startedAt timestamp) after which AWS Batch terminates your jobs if they have not finished.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobName': 'string',
    'jobId': 'string'
}


Response Structure

(dict) --

jobName (string) --
The name of the job.

jobId (string) --
The unique identifier for the job.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example submits a simple container job called example to the HighPriority job queue.
response = client.submit_job(
    jobDefinition='sleep60',
    jobName='example',
    jobQueue='HighPriority',
)

print(response)


Expected Output:
{
    'jobId': '876da822-4198-45f2-a252-6cea32512ea8',
    'jobName': 'example',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'jobName': 'string',
        'jobId': 'string'
    }
    
    
    :returns: 
    Batch.Client.exceptions.ClientException
    Batch.Client.exceptions.ServerException
    
    """
    pass

def terminate_job(jobId=None, reason=None):
    """
    Terminates a job in a job queue. Jobs that are in the STARTING or RUNNING state are terminated, which causes them to transition to FAILED . Jobs that have not progressed to the STARTING state are cancelled.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example terminates a job with the specified job ID.
    Expected Output:
    
    :example: response = client.terminate_job(
        jobId='string',
        reason='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe AWS Batch job ID of the job to terminate.\n

    :type reason: string
    :param reason: [REQUIRED]\nA message to attach to the job that explains the reason for canceling it. This message is returned by future DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example terminates a job with the specified job ID.
response = client.terminate_job(
    jobId='61e743ed-35e4-48da-b2de-5c8333821c84',
    reason='Terminating job.',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_compute_environment(computeEnvironment=None, state=None, computeResources=None, serviceRole=None):
    """
    Updates an AWS Batch compute environment.
    See also: AWS API Documentation
    
    Exceptions
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
    :param computeEnvironment: [REQUIRED]\nThe name or full Amazon Resource Name (ARN) of the compute environment to update.\n

    :type state: string
    :param state: The state of the compute environment. Compute environments in the ENABLED state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.

    :type computeResources: dict
    :param computeResources: Details of the compute resources managed by the compute environment. Required for a managed compute environment.\n\nminvCpus (integer) --The minimum number of Amazon EC2 vCPUs that an environment should maintain.\n\nmaxvCpus (integer) --The maximum number of Amazon EC2 vCPUs that an environment can reach.\n\ndesiredvCpus (integer) --The desired number of Amazon EC2 vCPUS in the compute environment.\n\n\n

    :type serviceRole: string
    :param serviceRole: The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.\nIf your specified role has a path other than / , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.\n\nNote\nDepending on how you created your AWS Batch service role, its ARN may contain the service-role path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the service-role path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'computeEnvironmentName': 'string',
    'computeEnvironmentArn': 'string'
}


Response Structure

(dict) --

computeEnvironmentName (string) --
The name of the compute environment.

computeEnvironmentArn (string) --
The Amazon Resource Name (ARN) of the compute environment.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example disables the P2OnDemand compute environment so it can be deleted.
response = client.update_compute_environment(
    computeEnvironment='P2OnDemand',
    state='DISABLED',
)

print(response)


Expected Output:
{
    'computeEnvironmentArn': 'arn:aws:batch:us-east-1:012345678910:compute-environment/P2OnDemand',
    'computeEnvironmentName': 'P2OnDemand',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'computeEnvironmentName': 'string',
        'computeEnvironmentArn': 'string'
    }
    
    
    :returns: 
    Batch.Client.exceptions.ClientException
    Batch.Client.exceptions.ServerException
    
    """
    pass

def update_job_queue(jobQueue=None, state=None, priority=None, computeEnvironmentOrder=None):
    """
    Updates a job queue.
    See also: AWS API Documentation
    
    Exceptions
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
    :param jobQueue: [REQUIRED]\nThe name or the Amazon Resource Name (ARN) of the job queue.\n

    :type state: string
    :param state: Describes the queue\'s ability to accept new jobs.

    :type priority: integer
    :param priority: The priority of the job queue. Job queues with a higher priority (or a higher integer value for the priority parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order, for example, a job queue with a priority value of 10 is given scheduling preference over a job queue with a priority value of 1 .

    :type computeEnvironmentOrder: list
    :param computeEnvironmentOrder: Details the set of compute environments mapped to a job queue and their order relative to each other. This is one of the parameters used by the job scheduler to determine which compute environment should execute a given job.\n\n(dict) --The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.\n\norder (integer) -- [REQUIRED]The order of the compute environment.\n\ncomputeEnvironment (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the compute environment.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobQueueName': 'string',
    'jobQueueArn': 'string'
}


Response Structure

(dict) --

jobQueueName (string) --
The name of the job queue.

jobQueueArn (string) --
The Amazon Resource Name (ARN) of the job queue.







Exceptions

Batch.Client.exceptions.ClientException
Batch.Client.exceptions.ServerException

Examples
This example disables a job queue so that it can be deleted.
response = client.update_job_queue(
    jobQueue='GPGPU',
    state='DISABLED',
)

print(response)


Expected Output:
{
    'jobQueueArn': 'arn:aws:batch:us-east-1:012345678910:job-queue/GPGPU',
    'jobQueueName': 'GPGPU',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'jobQueueName': 'string',
        'jobQueueArn': 'string'
    }
    
    
    :returns: 
    Batch.Client.exceptions.ClientException
    Batch.Client.exceptions.ServerException
    
    """
    pass

