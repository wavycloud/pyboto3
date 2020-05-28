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

def create_canary(Name=None, Code=None, ArtifactS3Location=None, ExecutionRoleArn=None, Schedule=None, RunConfig=None, SuccessRetentionPeriodInDays=None, FailureRetentionPeriodInDays=None, RuntimeVersion=None, VpcConfig=None, Tags=None):
    """
    Creates a canary. Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once.
    Do not use CreateCanary to modify an existing canary. Use UpdateCanary instead.
    To create canaries, you must have the CloudWatchSyntheticsFullAccess policy. If you are creating a new IAM role for the canary, you also need the the iam:CreateRole , iam:CreatePolicy and iam:AttachRolePolicy permissions. For more information, see Necessary Roles and Permissions .
    Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see Security Considerations for Synthetics Canaries .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_canary(
        Name='string',
        Code={
            'S3Bucket': 'string',
            'S3Key': 'string',
            'S3Version': 'string',
            'ZipFile': b'bytes',
            'Handler': 'string'
        },
        ArtifactS3Location='string',
        ExecutionRoleArn='string',
        Schedule={
            'Expression': 'string',
            'DurationInSeconds': 123
        },
        RunConfig={
            'TimeoutInSeconds': 123,
            'MemoryInMB': 123
        },
        SuccessRetentionPeriodInDays=123,
        FailureRetentionPeriodInDays=123,
        RuntimeVersion='string',
        VpcConfig={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account.\nDo not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see Security Considerations for Synthetics Canaries .\n

    :type Code: dict
    :param Code: [REQUIRED]\nA structure that includes the entry point from which the canary should start running your script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included.\n\nS3Bucket (string) --If your canary script is located in S3, specify the full bucket name here. The bucket must already exist. Specify the full bucket name, including s3:// as the start of the bucket name.\n\nS3Key (string) --The S3 key of your script. For more information, see Working with Amazon S3 Objects .\n\nS3Version (string) --The S3 version ID of your script.\n\nZipFile (bytes) --If you input your canary script directly into the canary instead of referring to an S3 location, the value of this parameter is the .zip file that contains the script. It can be up to 5 MB.\n\nHandler (string) -- [REQUIRED]The entry point to use for the source code when running the canary. This value must end with the string .handler .\n\n\n

    :type ArtifactS3Location: string
    :param ArtifactS3Location: [REQUIRED]\nThe location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files.\n

    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: [REQUIRED]\nThe ARN of the IAM role to be used to run the canary. This role must already exist, and must include lambda.amazonaws.com as a principal in the trust policy. The role must also have the following permissions:\n\ns3:PutObject\ns3:GetBucketLocation\ns3:ListAllMyBuckets\ncloudwatch:PutMetricData\nlogs:CreateLogGroup\nlogs:CreateLogStream\nlogs:CreateLogStream\n\n

    :type Schedule: dict
    :param Schedule: [REQUIRED]\nA structure that contains information about how often the canary is to run and when these test runs are to stop.\n\nExpression (string) -- [REQUIRED]A rate expression that defines how often the canary is to run. The syntax is rate(*number unit* ) . unit can be minute , minutes , or hour .\nFor example, rate(1 minute) runs the canary once a minute, rate(10 minutes) runs it once every 10 minutes, and rate(1 hour) runs it once every hour. You can specify a frequency between rate(1 minute) and rate(1 hour) .\nSpecifying rate(0 minute) or rate(0 hour) is a special value that causes the canary to run only once when it is started.\n\nDurationInSeconds (integer) --How long, in seconds, for the canary to continue making regular runs according to the schedule in the Expression value. If you specify 0, the canary continues making runs until you stop it. If you omit this field, the default of 0 is used.\n\n\n

    :type RunConfig: dict
    :param RunConfig: A structure that contains the configuration for individual canary runs, such as timeout value.\n\nTimeoutInSeconds (integer) -- [REQUIRED]How long the canary is allowed to run before it must stop. If you omit this field, the frequency of the canary is used as this value, up to a maximum of 14 minutes.\n\nMemoryInMB (integer) --The maximum amount of memory available to the canary while it is running, in MB. The value you specify must be a multiple of 64.\n\n\n

    :type SuccessRetentionPeriodInDays: integer
    :param SuccessRetentionPeriodInDays: The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.

    :type FailureRetentionPeriodInDays: integer
    :param FailureRetentionPeriodInDays: The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.

    :type RuntimeVersion: string
    :param RuntimeVersion: [REQUIRED]\nSpecifies the runtime version to use for the canary. Currently, the only valid value is syn-1.0 . For more information about runtime versions, see Canary Runtime Versions .\n

    :type VpcConfig: dict
    :param VpcConfig: If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see Running a Canary in a VPC .\n\nSubnetIds (list) --The IDs of the subnets where this canary is to run.\n\n(string) --\n\n\nSecurityGroupIds (list) --The IDs of the security groups for this canary.\n\n(string) --\n\n\n\n

    :type Tags: dict
    :param Tags: A list of key-value pairs to associate with the canary. You can associate as many as 50 tags with a canary.\nTags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Canary': {
        'Id': 'string',
        'Name': 'string',
        'Code': {
            'SourceLocationArn': 'string',
            'Handler': 'string'
        },
        'ExecutionRoleArn': 'string',
        'Schedule': {
            'Expression': 'string',
            'DurationInSeconds': 123
        },
        'RunConfig': {
            'TimeoutInSeconds': 123,
            'MemoryInMB': 123
        },
        'SuccessRetentionPeriodInDays': 123,
        'FailureRetentionPeriodInDays': 123,
        'Status': {
            'State': 'CREATING'|'READY'|'STARTING'|'RUNNING'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR'|'DELETING',
            'StateReason': 'string',
            'StateReasonCode': 'INVALID_PERMISSIONS'
        },
        'Timeline': {
            'Created': datetime(2015, 1, 1),
            'LastModified': datetime(2015, 1, 1),
            'LastStarted': datetime(2015, 1, 1),
            'LastStopped': datetime(2015, 1, 1)
        },
        'ArtifactS3Location': 'string',
        'EngineArn': 'string',
        'RuntimeVersion': 'string',
        'VpcConfig': {
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        'Tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

Canary (dict) --
The full details about the canary you have created.

Id (string) --
The unique ID of this canary.

Name (string) --
The name of the canary.

Code (dict) --
This structure contains information about the canary\'s Lambda handler and where its code is stored by CloudWatch Synthetics.

SourceLocationArn (string) --
The ARN of the Lambda layer where Synthetics stores the canary script code.

Handler (string) --
The entry point to use for the source code when running the canary.



ExecutionRoleArn (string) --
The ARN of the IAM role used to run the canary. This role must include lambda.amazonaws.com as a principal in the trust policy.

Schedule (dict) --
A structure that contains information about how often the canary is to run, and when these runs are to stop.

Expression (string) --
A rate expression that defines how often the canary is to run. The syntax is rate(*number unit* ) . unit can be minute , minutes , or hour .
For example, rate(1 minute) runs the canary once a minute, rate(10 minutes) runs it once every 10 minutes, and rate(1 hour) runs it once every hour.
Specifying rate(0 minute) or rate(0 hour) is a special value that causes the canary to run only once when it is started.

DurationInSeconds (integer) --
How long, in seconds, for the canary to continue making regular runs after it was created. The runs are performed according to the schedule in the Expression value.



RunConfig (dict) --
A structure that contains information for a canary run.

TimeoutInSeconds (integer) --
How long the canary is allowed to run before it must stop.

MemoryInMB (integer) --
The maximum amount of memory available to the canary while it is running, in MB. The value you must be a multiple of 64.



SuccessRetentionPeriodInDays (integer) --
The number of days to retain data about successful runs of this canary.

FailureRetentionPeriodInDays (integer) --
The number of days to retain data about failed runs of this canary.

Status (dict) --
A structure that contains information about the canary\'s status.

State (string) --
The current state of the canary.

StateReason (string) --
If the canary has insufficient permissions to run, this field provides more details.

StateReasonCode (string) --
If the canary cannot run or has failed, this field displays the reason.



Timeline (dict) --
A structure that contains information about when the canary was created, modified, and most recently run.

Created (datetime) --
The date and time the canary was created.

LastModified (datetime) --
The date and time the canary was most recently modified.

LastStarted (datetime) --
The date and time that the canary\'s most recent run started.

LastStopped (datetime) --
The date and time that the canary\'s most recent run ended.



ArtifactS3Location (string) --
The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files.

EngineArn (string) --
The ARN of the Lambda function that is used as your canary\'s engine. For more information about Lambda ARN format, see Resources and Conditions for Lambda Actions .

RuntimeVersion (string) --
Specifies the runtime version to use for the canary. Currently, the only valid value is syn-1.0 . For more information about runtime versions, see Canary Runtime Versions .

VpcConfig (dict) --
If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see Running a Canary in a VPC .

VpcId (string) --
The IDs of the VPC where this canary is to run.

SubnetIds (list) --
The IDs of the subnets where this canary is to run.

(string) --


SecurityGroupIds (list) --
The IDs of the security groups for this canary.

(string) --




Tags (dict) --
The list of key-value pairs that are associated with the canary.

(string) --
(string) --












Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException


    :return: {
        'Canary': {
            'Id': 'string',
            'Name': 'string',
            'Code': {
                'SourceLocationArn': 'string',
                'Handler': 'string'
            },
            'ExecutionRoleArn': 'string',
            'Schedule': {
                'Expression': 'string',
                'DurationInSeconds': 123
            },
            'RunConfig': {
                'TimeoutInSeconds': 123,
                'MemoryInMB': 123
            },
            'SuccessRetentionPeriodInDays': 123,
            'FailureRetentionPeriodInDays': 123,
            'Status': {
                'State': 'CREATING'|'READY'|'STARTING'|'RUNNING'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR'|'DELETING',
                'StateReason': 'string',
                'StateReasonCode': 'INVALID_PERMISSIONS'
            },
            'Timeline': {
                'Created': datetime(2015, 1, 1),
                'LastModified': datetime(2015, 1, 1),
                'LastStarted': datetime(2015, 1, 1),
                'LastStopped': datetime(2015, 1, 1)
            },
            'ArtifactS3Location': 'string',
            'EngineArn': 'string',
            'RuntimeVersion': 'string',
            'VpcConfig': {
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'Tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_canary(Name=None):
    """
    Permanently deletes the specified canary.
    When you delete a canary, resources used and created by the canary are not automatically deleted. After you delete a canary that you do not intend to use again, you should also delete the following:
    Before you delete a canary, you might want to use GetCanary to display the information about this canary. Make note of the information returned by this operation so that you can delete these resources after you delete the canary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_canary(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the canary that you want to delete. To find the names of your canaries, use DescribeCanaries .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException
Synthetics.Client.exceptions.ResourceNotFoundException
Synthetics.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_canaries(NextToken=None, MaxResults=None):
    """
    This operation returns a list of the canaries in your account, along with full details about each canary.
    This operation does not have resource-level authorization, so if a user is able to use DescribeCanaries , the user can see all of the canaries in the account. A deny policy can only be used to restrict access to all canaries. It cannot be used on specific resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_canaries(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: Specify this parameter to limit how many canaries are returned each time you use the DescribeCanaries operation. If you omit this parameter, the default of 100 is used.

    :rtype: dict

ReturnsResponse Syntax
{
    'Canaries': [
        {
            'Id': 'string',
            'Name': 'string',
            'Code': {
                'SourceLocationArn': 'string',
                'Handler': 'string'
            },
            'ExecutionRoleArn': 'string',
            'Schedule': {
                'Expression': 'string',
                'DurationInSeconds': 123
            },
            'RunConfig': {
                'TimeoutInSeconds': 123,
                'MemoryInMB': 123
            },
            'SuccessRetentionPeriodInDays': 123,
            'FailureRetentionPeriodInDays': 123,
            'Status': {
                'State': 'CREATING'|'READY'|'STARTING'|'RUNNING'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR'|'DELETING',
                'StateReason': 'string',
                'StateReasonCode': 'INVALID_PERMISSIONS'
            },
            'Timeline': {
                'Created': datetime(2015, 1, 1),
                'LastModified': datetime(2015, 1, 1),
                'LastStarted': datetime(2015, 1, 1),
                'LastStopped': datetime(2015, 1, 1)
            },
            'ArtifactS3Location': 'string',
            'EngineArn': 'string',
            'RuntimeVersion': 'string',
            'VpcConfig': {
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'Tags': {
                'string': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Canaries (list) --
Returns an array. Each item in the array contains the full information about one canary.

(dict) --
This structure contains all information about one canary in your account.

Id (string) --
The unique ID of this canary.

Name (string) --
The name of the canary.

Code (dict) --
This structure contains information about the canary\'s Lambda handler and where its code is stored by CloudWatch Synthetics.

SourceLocationArn (string) --
The ARN of the Lambda layer where Synthetics stores the canary script code.

Handler (string) --
The entry point to use for the source code when running the canary.



ExecutionRoleArn (string) --
The ARN of the IAM role used to run the canary. This role must include lambda.amazonaws.com as a principal in the trust policy.

Schedule (dict) --
A structure that contains information about how often the canary is to run, and when these runs are to stop.

Expression (string) --
A rate expression that defines how often the canary is to run. The syntax is rate(*number unit* ) . unit can be minute , minutes , or hour .
For example, rate(1 minute) runs the canary once a minute, rate(10 minutes) runs it once every 10 minutes, and rate(1 hour) runs it once every hour.
Specifying rate(0 minute) or rate(0 hour) is a special value that causes the canary to run only once when it is started.

DurationInSeconds (integer) --
How long, in seconds, for the canary to continue making regular runs after it was created. The runs are performed according to the schedule in the Expression value.



RunConfig (dict) --
A structure that contains information for a canary run.

TimeoutInSeconds (integer) --
How long the canary is allowed to run before it must stop.

MemoryInMB (integer) --
The maximum amount of memory available to the canary while it is running, in MB. The value you must be a multiple of 64.



SuccessRetentionPeriodInDays (integer) --
The number of days to retain data about successful runs of this canary.

FailureRetentionPeriodInDays (integer) --
The number of days to retain data about failed runs of this canary.

Status (dict) --
A structure that contains information about the canary\'s status.

State (string) --
The current state of the canary.

StateReason (string) --
If the canary has insufficient permissions to run, this field provides more details.

StateReasonCode (string) --
If the canary cannot run or has failed, this field displays the reason.



Timeline (dict) --
A structure that contains information about when the canary was created, modified, and most recently run.

Created (datetime) --
The date and time the canary was created.

LastModified (datetime) --
The date and time the canary was most recently modified.

LastStarted (datetime) --
The date and time that the canary\'s most recent run started.

LastStopped (datetime) --
The date and time that the canary\'s most recent run ended.



ArtifactS3Location (string) --
The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files.

EngineArn (string) --
The ARN of the Lambda function that is used as your canary\'s engine. For more information about Lambda ARN format, see Resources and Conditions for Lambda Actions .

RuntimeVersion (string) --
Specifies the runtime version to use for the canary. Currently, the only valid value is syn-1.0 . For more information about runtime versions, see Canary Runtime Versions .

VpcConfig (dict) --
If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see Running a Canary in a VPC .

VpcId (string) --
The IDs of the VPC where this canary is to run.

SubnetIds (list) --
The IDs of the subnets where this canary is to run.

(string) --


SecurityGroupIds (list) --
The IDs of the security groups for this canary.

(string) --




Tags (dict) --
The list of key-value pairs that are associated with the canary.

(string) --
(string) --








NextToken (string) --
A token that indicates that there is more data available. You can use this token in a subsequent DescribeCanaries operation to retrieve the next set of results.







Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException


    :return: {
        'Canaries': [
            {
                'Id': 'string',
                'Name': 'string',
                'Code': {
                    'SourceLocationArn': 'string',
                    'Handler': 'string'
                },
                'ExecutionRoleArn': 'string',
                'Schedule': {
                    'Expression': 'string',
                    'DurationInSeconds': 123
                },
                'RunConfig': {
                    'TimeoutInSeconds': 123,
                    'MemoryInMB': 123
                },
                'SuccessRetentionPeriodInDays': 123,
                'FailureRetentionPeriodInDays': 123,
                'Status': {
                    'State': 'CREATING'|'READY'|'STARTING'|'RUNNING'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR'|'DELETING',
                    'StateReason': 'string',
                    'StateReasonCode': 'INVALID_PERMISSIONS'
                },
                'Timeline': {
                    'Created': datetime(2015, 1, 1),
                    'LastModified': datetime(2015, 1, 1),
                    'LastStarted': datetime(2015, 1, 1),
                    'LastStopped': datetime(2015, 1, 1)
                },
                'ArtifactS3Location': 'string',
                'EngineArn': 'string',
                'RuntimeVersion': 'string',
                'VpcConfig': {
                    'VpcId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'Tags': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_canaries_last_run(NextToken=None, MaxResults=None):
    """
    Use this operation to see information from the most recent run of each canary that you have created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_canaries_last_run(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token that indicates that there is more data available. You can use this token in a subsequent DescribeCanaries operation to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: Specify this parameter to limit how many runs are returned each time you use the DescribeLastRun operation. If you omit this parameter, the default of 100 is used.

    :rtype: dict

ReturnsResponse Syntax
{
    'CanariesLastRun': [
        {
            'CanaryName': 'string',
            'LastRun': {
                'Name': 'string',
                'Status': {
                    'State': 'RUNNING'|'PASSED'|'FAILED',
                    'StateReason': 'string',
                    'StateReasonCode': 'CANARY_FAILURE'|'EXECUTION_FAILURE'
                },
                'Timeline': {
                    'Started': datetime(2015, 1, 1),
                    'Completed': datetime(2015, 1, 1)
                },
                'ArtifactS3Location': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CanariesLastRun (list) --
An array that contains the information from the most recent run of each canary.

(dict) --
This structure contains information about the most recent run of a single canary.

CanaryName (string) --
The name of the canary.

LastRun (dict) --
The results from this canary\'s most recent run.

Name (string) --
The name of the canary.

Status (dict) --
The status of this run.

State (string) --
The current state of the run.

StateReason (string) --
If run of the canary failed, this field contains the reason for the error.

StateReasonCode (string) --
If this value is CANARY_FAILURE , an exception occurred in the canary code. If this value is EXECUTION_FAILURE , an exception occurred in CloudWatch Synthetics.



Timeline (dict) --
A structure that contains the start and end times of this run.

Started (datetime) --
The start time of the run.

Completed (datetime) --
The end time of the run.



ArtifactS3Location (string) --
The location where the canary stored artifacts from the run. Artifacts include the log file, screenshots, and HAR files.







NextToken (string) --
A token that indicates that there is more data available. You can use this token in a subsequent DescribeCanariesLastRun operation to retrieve the next set of results.







Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException


    :return: {
        'CanariesLastRun': [
            {
                'CanaryName': 'string',
                'LastRun': {
                    'Name': 'string',
                    'Status': {
                        'State': 'RUNNING'|'PASSED'|'FAILED',
                        'StateReason': 'string',
                        'StateReasonCode': 'CANARY_FAILURE'|'EXECUTION_FAILURE'
                    },
                    'Timeline': {
                        'Started': datetime(2015, 1, 1),
                        'Completed': datetime(2015, 1, 1)
                    },
                    'ArtifactS3Location': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Synthetics.Client.exceptions.InternalServerException
    Synthetics.Client.exceptions.ValidationException
    
    """
    pass

def describe_runtime_versions(NextToken=None, MaxResults=None):
    """
    Returns a list of Synthetics canary runtime versions. For more information, see Canary Runtime Versions .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_runtime_versions(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token that indicates that there is more data available. You can use this token in a subsequent DescribeRuntimeVersions operation to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: Specify this parameter to limit how many runs are returned each time you use the DescribeRuntimeVersions operation. If you omit this parameter, the default of 100 is used.

    :rtype: dict

ReturnsResponse Syntax
{
    'RuntimeVersions': [
        {
            'VersionName': 'string',
            'Description': 'string',
            'ReleaseDate': datetime(2015, 1, 1),
            'DeprecationDate': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RuntimeVersions (list) --
An array of objects that display the details about each Synthetics canary runtime version.

(dict) --
This structure contains information about one canary runtime version. For more information about runtime versions, see Canary Runtime Versions .

VersionName (string) --
The name of the runtime version. Currently, the only valid value is syn-1.0 .
Specifies the runtime version to use for the canary. Currently, the only valid value is syn-1.0 .

Description (string) --
A description of the runtime version, created by Amazon.

ReleaseDate (datetime) --
The date that the runtime version was released.

DeprecationDate (datetime) --
If this runtime version is deprecated, this value is the date of deprecation.





NextToken (string) --
A token that indicates that there is more data available. You can use this token in a subsequent DescribeRuntimeVersions operation to retrieve the next set of results.







Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException


    :return: {
        'RuntimeVersions': [
            {
                'VersionName': 'string',
                'Description': 'string',
                'ReleaseDate': datetime(2015, 1, 1),
                'DeprecationDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Synthetics.Client.exceptions.InternalServerException
    Synthetics.Client.exceptions.ValidationException
    
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

def get_canary(Name=None):
    """
    Retrieves complete information about one canary. You must specify the name of the canary that you want. To get a list of canaries and their names, use DescribeCanaries .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_canary(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the canary that you want details for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Canary': {
        'Id': 'string',
        'Name': 'string',
        'Code': {
            'SourceLocationArn': 'string',
            'Handler': 'string'
        },
        'ExecutionRoleArn': 'string',
        'Schedule': {
            'Expression': 'string',
            'DurationInSeconds': 123
        },
        'RunConfig': {
            'TimeoutInSeconds': 123,
            'MemoryInMB': 123
        },
        'SuccessRetentionPeriodInDays': 123,
        'FailureRetentionPeriodInDays': 123,
        'Status': {
            'State': 'CREATING'|'READY'|'STARTING'|'RUNNING'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR'|'DELETING',
            'StateReason': 'string',
            'StateReasonCode': 'INVALID_PERMISSIONS'
        },
        'Timeline': {
            'Created': datetime(2015, 1, 1),
            'LastModified': datetime(2015, 1, 1),
            'LastStarted': datetime(2015, 1, 1),
            'LastStopped': datetime(2015, 1, 1)
        },
        'ArtifactS3Location': 'string',
        'EngineArn': 'string',
        'RuntimeVersion': 'string',
        'VpcConfig': {
            'VpcId': 'string',
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        },
        'Tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --
Canary (dict) --A strucure that contains the full information about the canary.

Id (string) --The unique ID of this canary.

Name (string) --The name of the canary.

Code (dict) --This structure contains information about the canary\'s Lambda handler and where its code is stored by CloudWatch Synthetics.

SourceLocationArn (string) --The ARN of the Lambda layer where Synthetics stores the canary script code.

Handler (string) --The entry point to use for the source code when running the canary.



ExecutionRoleArn (string) --The ARN of the IAM role used to run the canary. This role must include lambda.amazonaws.com as a principal in the trust policy.

Schedule (dict) --A structure that contains information about how often the canary is to run, and when these runs are to stop.

Expression (string) --A rate expression that defines how often the canary is to run. The syntax is rate(*number unit* ) . unit can be minute , minutes , or hour .
For example, rate(1 minute) runs the canary once a minute, rate(10 minutes) runs it once every 10 minutes, and rate(1 hour) runs it once every hour.
Specifying rate(0 minute) or rate(0 hour) is a special value that causes the canary to run only once when it is started.

DurationInSeconds (integer) --How long, in seconds, for the canary to continue making regular runs after it was created. The runs are performed according to the schedule in the Expression value.



RunConfig (dict) --A structure that contains information for a canary run.

TimeoutInSeconds (integer) --How long the canary is allowed to run before it must stop.

MemoryInMB (integer) --The maximum amount of memory available to the canary while it is running, in MB. The value you must be a multiple of 64.



SuccessRetentionPeriodInDays (integer) --The number of days to retain data about successful runs of this canary.

FailureRetentionPeriodInDays (integer) --The number of days to retain data about failed runs of this canary.

Status (dict) --A structure that contains information about the canary\'s status.

State (string) --The current state of the canary.

StateReason (string) --If the canary has insufficient permissions to run, this field provides more details.

StateReasonCode (string) --If the canary cannot run or has failed, this field displays the reason.



Timeline (dict) --A structure that contains information about when the canary was created, modified, and most recently run.

Created (datetime) --The date and time the canary was created.

LastModified (datetime) --The date and time the canary was most recently modified.

LastStarted (datetime) --The date and time that the canary\'s most recent run started.

LastStopped (datetime) --The date and time that the canary\'s most recent run ended.



ArtifactS3Location (string) --The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files.

EngineArn (string) --The ARN of the Lambda function that is used as your canary\'s engine. For more information about Lambda ARN format, see Resources and Conditions for Lambda Actions .

RuntimeVersion (string) --Specifies the runtime version to use for the canary. Currently, the only valid value is syn-1.0 . For more information about runtime versions, see Canary Runtime Versions .

VpcConfig (dict) --If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see Running a Canary in a VPC .

VpcId (string) --The IDs of the VPC where this canary is to run.

SubnetIds (list) --The IDs of the subnets where this canary is to run.

(string) --


SecurityGroupIds (list) --The IDs of the security groups for this canary.

(string) --




Tags (dict) --The list of key-value pairs that are associated with the canary.

(string) --
(string) --











Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException


    :return: {
        'Canary': {
            'Id': 'string',
            'Name': 'string',
            'Code': {
                'SourceLocationArn': 'string',
                'Handler': 'string'
            },
            'ExecutionRoleArn': 'string',
            'Schedule': {
                'Expression': 'string',
                'DurationInSeconds': 123
            },
            'RunConfig': {
                'TimeoutInSeconds': 123,
                'MemoryInMB': 123
            },
            'SuccessRetentionPeriodInDays': 123,
            'FailureRetentionPeriodInDays': 123,
            'Status': {
                'State': 'CREATING'|'READY'|'STARTING'|'RUNNING'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR'|'DELETING',
                'StateReason': 'string',
                'StateReasonCode': 'INVALID_PERMISSIONS'
            },
            'Timeline': {
                'Created': datetime(2015, 1, 1),
                'LastModified': datetime(2015, 1, 1),
                'LastStarted': datetime(2015, 1, 1),
                'LastStopped': datetime(2015, 1, 1)
            },
            'ArtifactS3Location': 'string',
            'EngineArn': 'string',
            'RuntimeVersion': 'string',
            'VpcConfig': {
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            },
            'Tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_canary_runs(Name=None, NextToken=None, MaxResults=None):
    """
    Retrieves a list of runs for a specified canary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_canary_runs(
        Name='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the canary that you want to see runs for.\n

    :type NextToken: string
    :param NextToken: A token that indicates that there is more data available. You can use this token in a subsequent GetCanaryRuns operation to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: Specify this parameter to limit how many runs are returned each time you use the GetCanaryRuns operation. If you omit this parameter, the default of 100 is used.

    :rtype: dict

ReturnsResponse Syntax
{
    'CanaryRuns': [
        {
            'Name': 'string',
            'Status': {
                'State': 'RUNNING'|'PASSED'|'FAILED',
                'StateReason': 'string',
                'StateReasonCode': 'CANARY_FAILURE'|'EXECUTION_FAILURE'
            },
            'Timeline': {
                'Started': datetime(2015, 1, 1),
                'Completed': datetime(2015, 1, 1)
            },
            'ArtifactS3Location': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CanaryRuns (list) --
An array of structures. Each structure contains the details of one of the retrieved canary runs.

(dict) --
This structure contains the details about one run of one canary.

Name (string) --
The name of the canary.

Status (dict) --
The status of this run.

State (string) --
The current state of the run.

StateReason (string) --
If run of the canary failed, this field contains the reason for the error.

StateReasonCode (string) --
If this value is CANARY_FAILURE , an exception occurred in the canary code. If this value is EXECUTION_FAILURE , an exception occurred in CloudWatch Synthetics.



Timeline (dict) --
A structure that contains the start and end times of this run.

Started (datetime) --
The start time of the run.

Completed (datetime) --
The end time of the run.



ArtifactS3Location (string) --
The location where the canary stored artifacts from the run. Artifacts include the log file, screenshots, and HAR files.





NextToken (string) --
A token that indicates that there is more data available. You can use this token in a subsequent GetCanaryRuns operation to retrieve the next set of results.







Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException
Synthetics.Client.exceptions.ResourceNotFoundException


    :return: {
        'CanaryRuns': [
            {
                'Name': 'string',
                'Status': {
                    'State': 'RUNNING'|'PASSED'|'FAILED',
                    'StateReason': 'string',
                    'StateReasonCode': 'CANARY_FAILURE'|'EXECUTION_FAILURE'
                },
                'Timeline': {
                    'Started': datetime(2015, 1, 1),
                    'Completed': datetime(2015, 1, 1)
                },
                'ArtifactS3Location': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Synthetics.Client.exceptions.InternalServerException
    Synthetics.Client.exceptions.ValidationException
    Synthetics.Client.exceptions.ResourceNotFoundException
    
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

def list_tags_for_resource(ResourceArn=None):
    """
    Displays the tags associated with a canary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the canary that you want to view tags for.\nThe ARN format of a canary is ``arn:aws:synthetics:Region :account-id :canary:canary-name `` .\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The list of tag keys and values associated with the canary that you specified.

(string) --
(string) --









Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ResourceNotFoundException
Synthetics.Client.exceptions.ValidationException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    Synthetics.Client.exceptions.InternalServerException
    Synthetics.Client.exceptions.ResourceNotFoundException
    Synthetics.Client.exceptions.ValidationException
    
    """
    pass

def start_canary(Name=None):
    """
    Use this operation to run a canary that has already been created. The frequency of the canary runs is determined by the value of the canary\'s Schedule . To see a canary\'s schedule, use GetCanary .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_canary(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the canary that you want to run. To find canary names, use DescribeCanaries .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException
Synthetics.Client.exceptions.ResourceNotFoundException
Synthetics.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Synthetics.Client.exceptions.InternalServerException
    Synthetics.Client.exceptions.ValidationException
    Synthetics.Client.exceptions.ResourceNotFoundException
    Synthetics.Client.exceptions.ConflictException
    
    """
    pass

def stop_canary(Name=None):
    """
    Stops the canary to prevent all future runs. If the canary is currently running, Synthetics stops waiting for the current run of the specified canary to complete. The run that is in progress completes on its own, publishes metrics, and uploads artifacts, but it is not recorded in Synthetics as a completed run.
    You can use StartCanary to start it running again with the canary\xe2\x80\x99s current schedule at any point in the future.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_canary(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the canary that you want to stop. To find the names of your canaries, use DescribeCanaries .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException
Synthetics.Client.exceptions.ResourceNotFoundException
Synthetics.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Synthetics.Client.exceptions.InternalServerException
    Synthetics.Client.exceptions.ValidationException
    Synthetics.Client.exceptions.ResourceNotFoundException
    Synthetics.Client.exceptions.ConflictException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Assigns one or more tags (key-value pairs) to the specified canary.
    Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.
    Tags don\'t have any semantic meaning to AWS and are interpreted strictly as strings of characters.
    You can use the TagResource action with a canary that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.
    You can associate as many as 50 tags with a canary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the canary that you\'re adding tags to.\nThe ARN format of a canary is ``arn:aws:synthetics:Region :account-id :canary:canary-name `` .\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe list of key-value pairs to associate with the canary.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ResourceNotFoundException
Synthetics.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes one or more tags from the specified canary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the canary that you\'re removing tags from.\nThe ARN format of a canary is ``arn:aws:synthetics:Region :account-id :canary:canary-name `` .\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe list of tag keys to remove from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ResourceNotFoundException
Synthetics.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_canary(Name=None, Code=None, ExecutionRoleArn=None, RuntimeVersion=None, Schedule=None, RunConfig=None, SuccessRetentionPeriodInDays=None, FailureRetentionPeriodInDays=None, VpcConfig=None):
    """
    Use this operation to change the settings of a canary that has already been created.
    You can\'t use this operation to update the tags of an existing canary. To change the tags of an existing canary, use TagResource .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_canary(
        Name='string',
        Code={
            'S3Bucket': 'string',
            'S3Key': 'string',
            'S3Version': 'string',
            'ZipFile': b'bytes',
            'Handler': 'string'
        },
        ExecutionRoleArn='string',
        RuntimeVersion='string',
        Schedule={
            'Expression': 'string',
            'DurationInSeconds': 123
        },
        RunConfig={
            'TimeoutInSeconds': 123,
            'MemoryInMB': 123
        },
        SuccessRetentionPeriodInDays=123,
        FailureRetentionPeriodInDays=123,
        VpcConfig={
            'SubnetIds': [
                'string',
            ],
            'SecurityGroupIds': [
                'string',
            ]
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the canary that you want to update. To find the names of your canaries, use DescribeCanaries .\nYou cannot change the name of a canary that has already been created.\n

    :type Code: dict
    :param Code: A structure that includes the entry point from which the canary should start running your script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included.\n\nS3Bucket (string) --If your canary script is located in S3, specify the full bucket name here. The bucket must already exist. Specify the full bucket name, including s3:// as the start of the bucket name.\n\nS3Key (string) --The S3 key of your script. For more information, see Working with Amazon S3 Objects .\n\nS3Version (string) --The S3 version ID of your script.\n\nZipFile (bytes) --If you input your canary script directly into the canary instead of referring to an S3 location, the value of this parameter is the .zip file that contains the script. It can be up to 5 MB.\n\nHandler (string) -- [REQUIRED]The entry point to use for the source code when running the canary. This value must end with the string .handler .\n\n\n

    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: The ARN of the IAM role to be used to run the canary. This role must already exist, and must include lambda.amazonaws.com as a principal in the trust policy. The role must also have the following permissions:\n\ns3:PutObject\ns3:GetBucketLocation\ns3:ListAllMyBuckets\ncloudwatch:PutMetricData\nlogs:CreateLogGroup\nlogs:CreateLogStream\nlogs:CreateLogStream\n\n

    :type RuntimeVersion: string
    :param RuntimeVersion: Specifies the runtime version to use for the canary. Currently, the only valid value is syn-1.0 . For more information about runtime versions, see Canary Runtime Versions .

    :type Schedule: dict
    :param Schedule: A structure that contains information about how often the canary is to run, and when these runs are to stop.\n\nExpression (string) -- [REQUIRED]A rate expression that defines how often the canary is to run. The syntax is rate(*number unit* ) . unit can be minute , minutes , or hour .\nFor example, rate(1 minute) runs the canary once a minute, rate(10 minutes) runs it once every 10 minutes, and rate(1 hour) runs it once every hour. You can specify a frequency between rate(1 minute) and rate(1 hour) .\nSpecifying rate(0 minute) or rate(0 hour) is a special value that causes the canary to run only once when it is started.\n\nDurationInSeconds (integer) --How long, in seconds, for the canary to continue making regular runs according to the schedule in the Expression value. If you specify 0, the canary continues making runs until you stop it. If you omit this field, the default of 0 is used.\n\n\n

    :type RunConfig: dict
    :param RunConfig: A structure that contains the timeout value that is used for each individual run of the canary.\n\nTimeoutInSeconds (integer) -- [REQUIRED]How long the canary is allowed to run before it must stop. If you omit this field, the frequency of the canary is used as this value, up to a maximum of 14 minutes.\n\nMemoryInMB (integer) --The maximum amount of memory available to the canary while it is running, in MB. The value you specify must be a multiple of 64.\n\n\n

    :type SuccessRetentionPeriodInDays: integer
    :param SuccessRetentionPeriodInDays: The number of days to retain data about successful runs of this canary.

    :type FailureRetentionPeriodInDays: integer
    :param FailureRetentionPeriodInDays: The number of days to retain data about failed runs of this canary.

    :type VpcConfig: dict
    :param VpcConfig: If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see Running a Canary in a VPC .\n\nSubnetIds (list) --The IDs of the subnets where this canary is to run.\n\n(string) --\n\n\nSecurityGroupIds (list) --The IDs of the security groups for this canary.\n\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Synthetics.Client.exceptions.InternalServerException
Synthetics.Client.exceptions.ValidationException
Synthetics.Client.exceptions.ResourceNotFoundException
Synthetics.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

