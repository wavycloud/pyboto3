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

def batch_describe_simulation_job(jobs=None):
    """
    Describes one or more simulation jobs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_describe_simulation_job(
        jobs=[
            'string',
        ]
    )
    
    
    :type jobs: list
    :param jobs: [REQUIRED]\nA list of Amazon Resource Names (ARNs) of simulation jobs to describe.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'jobs': [
        {
            'arn': 'string',
            'name': 'string',
            'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
            'lastStartedAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'failureBehavior': 'Fail'|'Continue',
            'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
            'failureReason': 'string',
            'clientRequestToken': 'string',
            'outputLocation': {
                's3Bucket': 'string',
                's3Prefix': 'string'
            },
            'loggingConfig': {
                'recordAllRosTopics': True|False
            },
            'maxJobDurationInSeconds': 123,
            'simulationTimeMillis': 123,
            'iamRole': 'string',
            'robotApplications': [
                {
                    'application': 'string',
                    'applicationVersion': 'string',
                    'launchConfig': {
                        'packageName': 'string',
                        'launchFile': 'string',
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'portForwardingConfig': {
                            'portMappings': [
                                {
                                    'jobPort': 123,
                                    'applicationPort': 123,
                                    'enableOnPublicIp': True|False
                                },
                            ]
                        },
                        'streamUI': True|False
                    }
                },
            ],
            'simulationApplications': [
                {
                    'application': 'string',
                    'applicationVersion': 'string',
                    'launchConfig': {
                        'packageName': 'string',
                        'launchFile': 'string',
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'portForwardingConfig': {
                            'portMappings': [
                                {
                                    'jobPort': 123,
                                    'applicationPort': 123,
                                    'enableOnPublicIp': True|False
                                },
                            ]
                        },
                        'streamUI': True|False
                    }
                },
            ],
            'dataSources': [
                {
                    'name': 'string',
                    's3Bucket': 'string',
                    's3Keys': [
                        {
                            's3Key': 'string',
                            'etag': 'string'
                        },
                    ]
                },
            ],
            'tags': {
                'string': 'string'
            },
            'vpcConfig': {
                'subnets': [
                    'string',
                ],
                'securityGroups': [
                    'string',
                ],
                'vpcId': 'string',
                'assignPublicIp': True|False
            },
            'networkInterface': {
                'networkInterfaceId': 'string',
                'privateIpAddress': 'string',
                'publicIpAddress': 'string'
            },
            'compute': {
                'simulationUnitLimit': 123
            }
        },
    ],
    'unprocessedJobs': [
        'string',
    ]
}


Response Structure

(dict) --
jobs (list) --A list of simulation jobs.

(dict) --Information about a simulation job.

arn (string) --The Amazon Resource Name (ARN) of the simulation job.

name (string) --The name of the simulation job.

status (string) --Status of the simulation job.

lastStartedAt (datetime) --The time, in milliseconds since the epoch, when the simulation job was last started.

lastUpdatedAt (datetime) --The time, in milliseconds since the epoch, when the simulation job was last updated.

failureBehavior (string) --The failure behavior the simulation job.

Continue
Restart the simulation job in the same host instance.

Fail
Stop the simulation job and terminate the instance.

failureCode (string) --The failure code of the simulation job if it failed.

failureReason (string) --The reason why the simulation job failed.

clientRequestToken (string) --A unique identifier for this SimulationJob request.

outputLocation (dict) --Location for output files generated by the simulation job.

s3Bucket (string) --The S3 bucket for output.

s3Prefix (string) --The S3 folder in the s3Bucket where output files will be placed.



loggingConfig (dict) --The logging configuration.

recordAllRosTopics (boolean) --A boolean indicating whether to record all ROS topics.



maxJobDurationInSeconds (integer) --The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.

simulationTimeMillis (integer) --The simulation job execution duration in milliseconds.

iamRole (string) --The IAM role that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

robotApplications (list) --A list of robot applications.

(dict) --Application configuration information for a robot.

application (string) --The application information for the robot application.

applicationVersion (string) --The version of the robot application.

launchConfig (dict) --The launch configuration for the robot application.

packageName (string) --The package name.

launchFile (string) --The launch file name.

environmentVariables (dict) --The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --The port forwarding configuration.

portMappings (list) --The port mappings for the configuration.

(dict) --An object representing a port mapping.

jobPort (integer) --The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --The port number on the application.

enableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







simulationApplications (list) --A list of simulation applications.

(dict) --Information about a simulation application configuration.

application (string) --The application information for the simulation application.

applicationVersion (string) --The version of the simulation application.

launchConfig (dict) --The launch configuration for the simulation application.

packageName (string) --The package name.

launchFile (string) --The launch file name.

environmentVariables (dict) --The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --The port forwarding configuration.

portMappings (list) --The port mappings for the configuration.

(dict) --An object representing a port mapping.

jobPort (integer) --The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --The port number on the application.

enableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







dataSources (list) --The data sources for the simulation job.

(dict) --Information about a data source.

name (string) --The name of the data source.

s3Bucket (string) --The S3 bucket where the data files are located.

s3Keys (list) --The list of S3 keys identifying the data source files.

(dict) --Information about S3 keys.

s3Key (string) --The S3 key.

etag (string) --The etag for the object.









tags (dict) --A map that contains tag keys and tag values that are attached to the simulation job.

(string) --
(string) --




vpcConfig (dict) --VPC configuration information.

subnets (list) --A list of subnet IDs associated with the simulation job.

(string) --


securityGroups (list) --A list of security group IDs associated with the simulation job.

(string) --


vpcId (string) --The VPC ID associated with your simulation job.

assignPublicIp (boolean) --A boolean indicating if a public IP was assigned.



networkInterface (dict) --Information about a network interface.

networkInterfaceId (string) --The ID of the network interface.

privateIpAddress (string) --The IPv4 address of the network interface within the subnet.

publicIpAddress (string) --The IPv4 public address of the network interface.



compute (dict) --Compute information for the simulation job

simulationUnitLimit (integer) --The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided.







unprocessedJobs (list) --A list of unprocessed simulation job Amazon Resource Names (ARNs).

(string) --







Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'jobs': [
            {
                'arn': 'string',
                'name': 'string',
                'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                'lastStartedAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'failureBehavior': 'Fail'|'Continue',
                'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
                'failureReason': 'string',
                'clientRequestToken': 'string',
                'outputLocation': {
                    's3Bucket': 'string',
                    's3Prefix': 'string'
                },
                'loggingConfig': {
                    'recordAllRosTopics': True|False
                },
                'maxJobDurationInSeconds': 123,
                'simulationTimeMillis': 123,
                'iamRole': 'string',
                'robotApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'simulationApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'dataSources': [
                    {
                        'name': 'string',
                        's3Bucket': 'string',
                        's3Keys': [
                            {
                                's3Key': 'string',
                                'etag': 'string'
                            },
                        ]
                    },
                ],
                'tags': {
                    'string': 'string'
                },
                'vpcConfig': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'vpcId': 'string',
                    'assignPublicIp': True|False
                },
                'networkInterface': {
                    'networkInterfaceId': 'string',
                    'privateIpAddress': 'string',
                    'publicIpAddress': 'string'
                },
                'compute': {
                    'simulationUnitLimit': 123
                }
            },
        ],
        'unprocessedJobs': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_deployment_job(job=None):
    """
    Cancels the specified deployment job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_deployment_job(
        job='string'
    )
    
    
    :type job: string
    :param job: [REQUIRED]\nThe deployment job ARN to cancel.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def cancel_simulation_job(job=None):
    """
    Cancels the specified simulation job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_simulation_job(
        job='string'
    )
    
    
    :type job: string
    :param job: [REQUIRED]\nThe simulation job ARN to cancel.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def cancel_simulation_job_batch(batch=None):
    """
    Cancels a simulation job batch. When you cancel a simulation job batch, you are also cancelling all of the active simulation jobs created as part of the batch.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_simulation_job_batch(
        batch='string'
    )
    
    
    :type batch: string
    :param batch: [REQUIRED]\nThe id of the batch to cancel.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def create_deployment_job(deploymentConfig=None, clientRequestToken=None, fleet=None, deploymentApplicationConfigs=None, tags=None):
    """
    Deploys a specific version of a robot application to robots in a fleet.
    The robot application must have a numbered applicationVersion for consistency reasons. To create a new version, use CreateRobotApplicationVersion or see Creating a Robot Application Version .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_deployment_job(
        deploymentConfig={
            'concurrentDeploymentPercentage': 123,
            'failureThresholdPercentage': 123,
            'robotDeploymentTimeoutInSeconds': 123,
            'downloadConditionFile': {
                'bucket': 'string',
                'key': 'string',
                'etag': 'string'
            }
        },
        clientRequestToken='string',
        fleet='string',
        deploymentApplicationConfigs=[
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'preLaunchFile': 'string',
                    'launchFile': 'string',
                    'postLaunchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        tags={
            'string': 'string'
        }
    )
    
    
    :type deploymentConfig: dict
    :param deploymentConfig: The requested deployment configuration.\n\nconcurrentDeploymentPercentage (integer) --The percentage of robots receiving the deployment at the same time.\n\nfailureThresholdPercentage (integer) --The percentage of deployments that need to fail before stopping deployment.\n\nrobotDeploymentTimeoutInSeconds (integer) --The amount of time, in seconds, to wait for deployment to a single robot to complete. Choose a time between 1 minute and 7 days. The default is 5 hours.\n\ndownloadConditionFile (dict) --The download condition file.\n\nbucket (string) -- [REQUIRED]The bucket containing the object.\n\nkey (string) -- [REQUIRED]The key of the object.\n\netag (string) --The etag of the object.\n\n\n\n\n

    :type clientRequestToken: string
    :param clientRequestToken: [REQUIRED]\nUnique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type fleet: string
    :param fleet: [REQUIRED]\nThe Amazon Resource Name (ARN) of the fleet to deploy.\n

    :type deploymentApplicationConfigs: list
    :param deploymentApplicationConfigs: [REQUIRED]\nThe deployment application configuration.\n\n(dict) --Information about a deployment application configuration.\n\napplication (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the robot application.\n\napplicationVersion (string) -- [REQUIRED]The version of the application.\n\nlaunchConfig (dict) -- [REQUIRED]The launch configuration.\n\npackageName (string) -- [REQUIRED]The package name.\n\npreLaunchFile (string) --The deployment pre-launch file. This file will be executed prior to the launch file.\n\nlaunchFile (string) -- [REQUIRED]The launch file name.\n\npostLaunchFile (string) --The deployment post-launch file. This file will be executed after the launch file.\n\nenvironmentVariables (dict) --An array of key/value pairs specifying environment variables for the robot application\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type tags: dict
    :param tags: A map that contains tag keys and tag values that are attached to the deployment job.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'fleet': 'string',
    'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
    'deploymentApplicationConfigs': [
        {
            'application': 'string',
            'applicationVersion': 'string',
            'launchConfig': {
                'packageName': 'string',
                'preLaunchFile': 'string',
                'launchFile': 'string',
                'postLaunchFile': 'string',
                'environmentVariables': {
                    'string': 'string'
                }
            }
        },
    ],
    'failureReason': 'string',
    'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError',
    'createdAt': datetime(2015, 1, 1),
    'deploymentConfig': {
        'concurrentDeploymentPercentage': 123,
        'failureThresholdPercentage': 123,
        'robotDeploymentTimeoutInSeconds': 123,
        'downloadConditionFile': {
            'bucket': 'string',
            'key': 'string',
            'etag': 'string'
        }
    },
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the deployment job.

fleet (string) --
The target fleet for the deployment job.

status (string) --
The status of the deployment job.

deploymentApplicationConfigs (list) --
The deployment application configuration.

(dict) --
Information about a deployment application configuration.

application (string) --
The Amazon Resource Name (ARN) of the robot application.

applicationVersion (string) --
The version of the application.

launchConfig (dict) --
The launch configuration.

packageName (string) --
The package name.

preLaunchFile (string) --
The deployment pre-launch file. This file will be executed prior to the launch file.

launchFile (string) --
The launch file name.

postLaunchFile (string) --
The deployment post-launch file. This file will be executed after the launch file.

environmentVariables (dict) --
An array of key/value pairs specifying environment variables for the robot application

(string) --
(string) --










failureReason (string) --
The failure reason of the deployment job if it failed.

failureCode (string) --
The failure code of the simulation job if it failed:

BadPermissionError

AWS Greengrass requires a service-level role permission to access other services. The role must include the ` AWSGreengrassResourceAccessRolePolicy managed policy <https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy$jsonEditor>`__ .

ExtractingBundleFailure

The robot application could not be extracted from the bundle.

FailureThresholdBreached

The percentage of robots that could not be updated exceeded the percentage set for the deployment.

GreengrassDeploymentFailed

The robot application could not be deployed to the robot.

GreengrassGroupVersionDoesNotExist

The AWS Greengrass group or version associated with a robot is missing.

InternalServerError

An internal error has occurred. Retry your request, but if the problem persists, contact us with details.

MissingRobotApplicationArchitecture

The robot application does not have a source that matches the architecture of the robot.

MissingRobotDeploymentResource

One or more of the resources specified for the robot application are missing. For example, does the robot application have the correct launch package and launch file?

PostLaunchFileFailure

The post-launch script failed.

PreLaunchFileFailure

The pre-launch script failed.

ResourceNotFound

One or more deployment resources are missing. For example, do robot application source bundles still exist?

RobotDeploymentNoResponse

There is no response from the robot. It might not be powered on or connected to the internet.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the fleet was created.

deploymentConfig (dict) --
The deployment configuration.

concurrentDeploymentPercentage (integer) --
The percentage of robots receiving the deployment at the same time.

failureThresholdPercentage (integer) --
The percentage of deployments that need to fail before stopping deployment.

robotDeploymentTimeoutInSeconds (integer) --
The amount of time, in seconds, to wait for deployment to a single robot to complete. Choose a time between 1 minute and 7 days. The default is 5 hours.

downloadConditionFile (dict) --
The download condition file.

bucket (string) --
The bucket containing the object.

key (string) --
The key of the object.

etag (string) --
The etag of the object.





tags (dict) --
The list of all tags added to the deployment job.

(string) --
(string) --










Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ConcurrentDeploymentException
RoboMaker.Client.exceptions.IdempotentParameterMismatchException


    :return: {
        'arn': 'string',
        'fleet': 'string',
        'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
        'deploymentApplicationConfigs': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'preLaunchFile': 'string',
                    'launchFile': 'string',
                    'postLaunchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'failureReason': 'string',
        'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError',
        'createdAt': datetime(2015, 1, 1),
        'deploymentConfig': {
            'concurrentDeploymentPercentage': 123,
            'failureThresholdPercentage': 123,
            'robotDeploymentTimeoutInSeconds': 123,
            'downloadConditionFile': {
                'bucket': 'string',
                'key': 'string',
                'etag': 'string'
            }
        },
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_fleet(name=None, tags=None):
    """
    Creates a fleet, a logical group of robots running the same robot application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_fleet(
        name='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the fleet.\n

    :type tags: dict
    :param tags: A map that contains tag keys and tag values that are attached to the fleet.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'createdAt': datetime(2015, 1, 1),
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the fleet.

name (string) --
The name of the fleet.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the fleet was created.

tags (dict) --
The list of all tags added to the fleet.

(string) --
(string) --










Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.LimitExceededException


    :return: {
        'arn': 'string',
        'name': 'string',
        'createdAt': datetime(2015, 1, 1),
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_robot(name=None, architecture=None, greengrassGroupId=None, tags=None):
    """
    Creates a robot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_robot(
        name='string',
        architecture='X86_64'|'ARM64'|'ARMHF',
        greengrassGroupId='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name for the robot.\n

    :type architecture: string
    :param architecture: [REQUIRED]\nThe target architecture of the robot.\n

    :type greengrassGroupId: string
    :param greengrassGroupId: [REQUIRED]\nThe Greengrass group id.\n

    :type tags: dict
    :param tags: A map that contains tag keys and tag values that are attached to the robot.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'createdAt': datetime(2015, 1, 1),
    'greengrassGroupId': 'string',
    'architecture': 'X86_64'|'ARM64'|'ARMHF',
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the robot.

name (string) --
The name of the robot.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the robot was created.

greengrassGroupId (string) --
The Amazon Resource Name (ARN) of the Greengrass group associated with the robot.

architecture (string) --
The target architecture of the robot.

tags (dict) --
The list of all tags added to the robot.

(string) --
(string) --










Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ResourceAlreadyExistsException


    :return: {
        'arn': 'string',
        'name': 'string',
        'createdAt': datetime(2015, 1, 1),
        'greengrassGroupId': 'string',
        'architecture': 'X86_64'|'ARM64'|'ARMHF',
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_robot_application(name=None, sources=None, robotSoftwareSuite=None, tags=None):
    """
    Creates a robot application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_robot_application(
        name='string',
        sources=[
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        robotSoftwareSuite={
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        tags={
            'string': 'string'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the robot application.\n

    :type sources: list
    :param sources: [REQUIRED]\nThe sources of the robot application.\n\n(dict) --Information about a source configuration.\n\ns3Bucket (string) --The Amazon S3 bucket name.\n\ns3Key (string) --The s3 object key.\n\narchitecture (string) --The target processor architecture for the application.\n\n\n\n\n

    :type robotSoftwareSuite: dict
    :param robotSoftwareSuite: [REQUIRED]\nThe robot software suite (ROS distribuition) used by the robot application.\n\nname (string) --The name of the robot software suite (ROS distribution).\n\nversion (string) --The version of the robot software suite (ROS distribution).\n\n\n

    :type tags: dict
    :param tags: A map that contains tag keys and tag values that are attached to the robot application.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'version': 'string',
    'sources': [
        {
            's3Bucket': 'string',
            's3Key': 'string',
            'etag': 'string',
            'architecture': 'X86_64'|'ARM64'|'ARMHF'
        },
    ],
    'robotSoftwareSuite': {
        'name': 'ROS'|'ROS2',
        'version': 'Kinetic'|'Melodic'|'Dashing'
    },
    'lastUpdatedAt': datetime(2015, 1, 1),
    'revisionId': 'string',
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the robot application.

name (string) --
The name of the robot application.

version (string) --
The version of the robot application.

sources (list) --
The sources of the robot application.

(dict) --
Information about a source.

s3Bucket (string) --
The s3 bucket name.

s3Key (string) --
The s3 object key.

etag (string) --
A hash of the object specified by s3Bucket and s3Key .

architecture (string) --
The taget processor architecture for the application.





robotSoftwareSuite (dict) --
The robot software suite (ROS distribution) used by the robot application.

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).



lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the robot application was last updated.

revisionId (string) --
The revision id of the robot application.

tags (dict) --
The list of all tags added to the robot application.

(string) --
(string) --










Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ResourceAlreadyExistsException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.IdempotentParameterMismatchException


    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'robotSoftwareSuite': {
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string',
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_robot_application_version(application=None, currentRevisionId=None):
    """
    Creates a version of a robot application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_robot_application_version(
        application='string',
        currentRevisionId='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]\nThe application information for the robot application.\n

    :type currentRevisionId: string
    :param currentRevisionId: The current revision id for the robot application. If you provide a value and it matches the latest revision ID, a new version will be created.

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'version': 'string',
    'sources': [
        {
            's3Bucket': 'string',
            's3Key': 'string',
            'etag': 'string',
            'architecture': 'X86_64'|'ARM64'|'ARMHF'
        },
    ],
    'robotSoftwareSuite': {
        'name': 'ROS'|'ROS2',
        'version': 'Kinetic'|'Melodic'|'Dashing'
    },
    'lastUpdatedAt': datetime(2015, 1, 1),
    'revisionId': 'string'
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the robot application.

name (string) --
The name of the robot application.

version (string) --
The version of the robot application.

sources (list) --
The sources of the robot application.

(dict) --
Information about a source.

s3Bucket (string) --
The s3 bucket name.

s3Key (string) --
The s3 object key.

etag (string) --
A hash of the object specified by s3Bucket and s3Key .

architecture (string) --
The taget processor architecture for the application.





robotSoftwareSuite (dict) --
The robot software suite (ROS distribution) used by the robot application.

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).



lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the robot application was last updated.

revisionId (string) --
The revision id of the robot application.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.IdempotentParameterMismatchException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'robotSoftwareSuite': {
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.IdempotentParameterMismatchException
    RoboMaker.Client.exceptions.LimitExceededException
    RoboMaker.Client.exceptions.ThrottlingException
    RoboMaker.Client.exceptions.InternalServerException
    
    """
    pass

def create_simulation_application(name=None, sources=None, simulationSoftwareSuite=None, robotSoftwareSuite=None, renderingEngine=None, tags=None):
    """
    Creates a simulation application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_simulation_application(
        name='string',
        sources=[
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        simulationSoftwareSuite={
            'name': 'Gazebo'|'RosbagPlay',
            'version': 'string'
        },
        robotSoftwareSuite={
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        renderingEngine={
            'name': 'OGRE',
            'version': 'string'
        },
        tags={
            'string': 'string'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the simulation application.\n

    :type sources: list
    :param sources: [REQUIRED]\nThe sources of the simulation application.\n\n(dict) --Information about a source configuration.\n\ns3Bucket (string) --The Amazon S3 bucket name.\n\ns3Key (string) --The s3 object key.\n\narchitecture (string) --The target processor architecture for the application.\n\n\n\n\n

    :type simulationSoftwareSuite: dict
    :param simulationSoftwareSuite: [REQUIRED]\nThe simulation software suite used by the simulation application.\n\nname (string) --The name of the simulation software suite.\n\nversion (string) --The version of the simulation software suite.\n\n\n

    :type robotSoftwareSuite: dict
    :param robotSoftwareSuite: [REQUIRED]\nThe robot software suite (ROS distribution) used by the simulation application.\n\nname (string) --The name of the robot software suite (ROS distribution).\n\nversion (string) --The version of the robot software suite (ROS distribution).\n\n\n

    :type renderingEngine: dict
    :param renderingEngine: The rendering engine for the simulation application.\n\nname (string) --The name of the rendering engine.\n\nversion (string) --The version of the rendering engine.\n\n\n

    :type tags: dict
    :param tags: A map that contains tag keys and tag values that are attached to the simulation application.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'version': 'string',
    'sources': [
        {
            's3Bucket': 'string',
            's3Key': 'string',
            'etag': 'string',
            'architecture': 'X86_64'|'ARM64'|'ARMHF'
        },
    ],
    'simulationSoftwareSuite': {
        'name': 'Gazebo'|'RosbagPlay',
        'version': 'string'
    },
    'robotSoftwareSuite': {
        'name': 'ROS'|'ROS2',
        'version': 'Kinetic'|'Melodic'|'Dashing'
    },
    'renderingEngine': {
        'name': 'OGRE',
        'version': 'string'
    },
    'lastUpdatedAt': datetime(2015, 1, 1),
    'revisionId': 'string',
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the simulation application.

name (string) --
The name of the simulation application.

version (string) --
The version of the simulation application.

sources (list) --
The sources of the simulation application.

(dict) --
Information about a source.

s3Bucket (string) --
The s3 bucket name.

s3Key (string) --
The s3 object key.

etag (string) --
A hash of the object specified by s3Bucket and s3Key .

architecture (string) --
The taget processor architecture for the application.





simulationSoftwareSuite (dict) --
The simulation software suite used by the simulation application.

name (string) --
The name of the simulation software suite.

version (string) --
The version of the simulation software suite.



robotSoftwareSuite (dict) --
Information about the robot software suite (ROS distribution).

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).



renderingEngine (dict) --
The rendering engine for the simulation application.

name (string) --
The name of the rendering engine.

version (string) --
The version of the rendering engine.



lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation application was last updated.

revisionId (string) --
The revision id of the simulation application.

tags (dict) --
The list of all tags added to the simulation application.

(string) --
(string) --










Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ResourceAlreadyExistsException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.IdempotentParameterMismatchException


    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'simulationSoftwareSuite': {
            'name': 'Gazebo'|'RosbagPlay',
            'version': 'string'
        },
        'robotSoftwareSuite': {
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        'renderingEngine': {
            'name': 'OGRE',
            'version': 'string'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string',
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_simulation_application_version(application=None, currentRevisionId=None):
    """
    Creates a simulation application with a specific revision id.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_simulation_application_version(
        application='string',
        currentRevisionId='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]\nThe application information for the simulation application.\n

    :type currentRevisionId: string
    :param currentRevisionId: The current revision id for the simulation application. If you provide a value and it matches the latest revision ID, a new version will be created.

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'version': 'string',
    'sources': [
        {
            's3Bucket': 'string',
            's3Key': 'string',
            'etag': 'string',
            'architecture': 'X86_64'|'ARM64'|'ARMHF'
        },
    ],
    'simulationSoftwareSuite': {
        'name': 'Gazebo'|'RosbagPlay',
        'version': 'string'
    },
    'robotSoftwareSuite': {
        'name': 'ROS'|'ROS2',
        'version': 'Kinetic'|'Melodic'|'Dashing'
    },
    'renderingEngine': {
        'name': 'OGRE',
        'version': 'string'
    },
    'lastUpdatedAt': datetime(2015, 1, 1),
    'revisionId': 'string'
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the simulation application.

name (string) --
The name of the simulation application.

version (string) --
The version of the simulation application.

sources (list) --
The sources of the simulation application.

(dict) --
Information about a source.

s3Bucket (string) --
The s3 bucket name.

s3Key (string) --
The s3 object key.

etag (string) --
A hash of the object specified by s3Bucket and s3Key .

architecture (string) --
The taget processor architecture for the application.





simulationSoftwareSuite (dict) --
The simulation software suite used by the simulation application.

name (string) --
The name of the simulation software suite.

version (string) --
The version of the simulation software suite.



robotSoftwareSuite (dict) --
Information about the robot software suite (ROS distribution).

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).



renderingEngine (dict) --
The rendering engine for the simulation application.

name (string) --
The name of the rendering engine.

version (string) --
The version of the rendering engine.



lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation application was last updated.

revisionId (string) --
The revision ID of the simulation application.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.IdempotentParameterMismatchException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'simulationSoftwareSuite': {
            'name': 'Gazebo'|'RosbagPlay',
            'version': 'string'
        },
        'robotSoftwareSuite': {
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        'renderingEngine': {
            'name': 'OGRE',
            'version': 'string'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.IdempotentParameterMismatchException
    RoboMaker.Client.exceptions.LimitExceededException
    RoboMaker.Client.exceptions.ThrottlingException
    RoboMaker.Client.exceptions.InternalServerException
    
    """
    pass

def create_simulation_job(clientRequestToken=None, outputLocation=None, loggingConfig=None, maxJobDurationInSeconds=None, iamRole=None, failureBehavior=None, robotApplications=None, simulationApplications=None, dataSources=None, tags=None, vpcConfig=None, compute=None):
    """
    Creates a simulation job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_simulation_job(
        clientRequestToken='string',
        outputLocation={
            's3Bucket': 'string',
            's3Prefix': 'string'
        },
        loggingConfig={
            'recordAllRosTopics': True|False
        },
        maxJobDurationInSeconds=123,
        iamRole='string',
        failureBehavior='Fail'|'Continue',
        robotApplications=[
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    },
                    'portForwardingConfig': {
                        'portMappings': [
                            {
                                'jobPort': 123,
                                'applicationPort': 123,
                                'enableOnPublicIp': True|False
                            },
                        ]
                    },
                    'streamUI': True|False
                }
            },
        ],
        simulationApplications=[
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    },
                    'portForwardingConfig': {
                        'portMappings': [
                            {
                                'jobPort': 123,
                                'applicationPort': 123,
                                'enableOnPublicIp': True|False
                            },
                        ]
                    },
                    'streamUI': True|False
                }
            },
        ],
        dataSources=[
            {
                'name': 'string',
                's3Bucket': 'string',
                's3Keys': [
                    'string',
                ]
            },
        ],
        tags={
            'string': 'string'
        },
        vpcConfig={
            'subnets': [
                'string',
            ],
            'securityGroups': [
                'string',
            ],
            'assignPublicIp': True|False
        },
        compute={
            'simulationUnitLimit': 123
        }
    )
    
    
    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type outputLocation: dict
    :param outputLocation: Location for output files generated by the simulation job.\n\ns3Bucket (string) --The S3 bucket for output.\n\ns3Prefix (string) --The S3 folder in the s3Bucket where output files will be placed.\n\n\n

    :type loggingConfig: dict
    :param loggingConfig: The logging configuration.\n\nrecordAllRosTopics (boolean) -- [REQUIRED]A boolean indicating whether to record all ROS topics.\n\n\n

    :type maxJobDurationInSeconds: integer
    :param maxJobDurationInSeconds: [REQUIRED]\nThe maximum simulation job duration in seconds (up to 14 days or 1,209,600 seconds. When maxJobDurationInSeconds is reached, the simulation job will status will transition to Completed .\n

    :type iamRole: string
    :param iamRole: [REQUIRED]\nThe IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.\n

    :type failureBehavior: string
    :param failureBehavior: The failure behavior the simulation job.\n\nContinue\nRestart the simulation job in the same host instance.\n\nFail\nStop the simulation job and terminate the instance.\n

    :type robotApplications: list
    :param robotApplications: The robot application to use in the simulation job.\n\n(dict) --Application configuration information for a robot.\n\napplication (string) -- [REQUIRED]The application information for the robot application.\n\napplicationVersion (string) --The version of the robot application.\n\nlaunchConfig (dict) -- [REQUIRED]The launch configuration for the robot application.\n\npackageName (string) -- [REQUIRED]The package name.\n\nlaunchFile (string) -- [REQUIRED]The launch file name.\n\nenvironmentVariables (dict) --The environment variables for the application launch.\n\n(string) --\n(string) --\n\n\n\n\nportForwardingConfig (dict) --The port forwarding configuration.\n\nportMappings (list) --The port mappings for the configuration.\n\n(dict) --An object representing a port mapping.\n\njobPort (integer) -- [REQUIRED]The port number on the simulation job instance to use as a remote connection point.\n\napplicationPort (integer) -- [REQUIRED]The port number on the application.\n\nenableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.\n\n\n\n\n\n\n\nstreamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.\n\n\n\n\n\n\n

    :type simulationApplications: list
    :param simulationApplications: The simulation application to use in the simulation job.\n\n(dict) --Information about a simulation application configuration.\n\napplication (string) -- [REQUIRED]The application information for the simulation application.\n\napplicationVersion (string) --The version of the simulation application.\n\nlaunchConfig (dict) -- [REQUIRED]The launch configuration for the simulation application.\n\npackageName (string) -- [REQUIRED]The package name.\n\nlaunchFile (string) -- [REQUIRED]The launch file name.\n\nenvironmentVariables (dict) --The environment variables for the application launch.\n\n(string) --\n(string) --\n\n\n\n\nportForwardingConfig (dict) --The port forwarding configuration.\n\nportMappings (list) --The port mappings for the configuration.\n\n(dict) --An object representing a port mapping.\n\njobPort (integer) -- [REQUIRED]The port number on the simulation job instance to use as a remote connection point.\n\napplicationPort (integer) -- [REQUIRED]The port number on the application.\n\nenableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.\n\n\n\n\n\n\n\nstreamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.\n\n\n\n\n\n\n

    :type dataSources: list
    :param dataSources: Specify data sources to mount read-only files from S3 into your simulation. These files are available under /opt/robomaker/datasources/data_source_name .\n\nNote\nThere is a limit of 100 files and a combined size of 25GB for all DataSourceConfig objects.\n\n\n(dict) --Information about a data source.\n\nname (string) -- [REQUIRED]The name of the data source.\n\ns3Bucket (string) -- [REQUIRED]The S3 bucket where the data files are located.\n\ns3Keys (list) -- [REQUIRED]The list of S3 keys identifying the data source files.\n\n(string) --\n\n\n\n\n\n

    :type tags: dict
    :param tags: A map that contains tag keys and tag values that are attached to the simulation job.\n\n(string) --\n(string) --\n\n\n\n

    :type vpcConfig: dict
    :param vpcConfig: If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and one subnet ID.\n\nsubnets (list) -- [REQUIRED]A list of one or more subnet IDs in your VPC.\n\n(string) --\n\n\nsecurityGroups (list) --A list of one or more security groups IDs in your VPC.\n\n(string) --\n\n\nassignPublicIp (boolean) --A boolean indicating whether to assign a public IP address.\n\n\n

    :type compute: dict
    :param compute: Compute information for the simulation job.\n\nsimulationUnitLimit (integer) --The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
    'lastStartedAt': datetime(2015, 1, 1),
    'lastUpdatedAt': datetime(2015, 1, 1),
    'failureBehavior': 'Fail'|'Continue',
    'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
    'clientRequestToken': 'string',
    'outputLocation': {
        's3Bucket': 'string',
        's3Prefix': 'string'
    },
    'loggingConfig': {
        'recordAllRosTopics': True|False
    },
    'maxJobDurationInSeconds': 123,
    'simulationTimeMillis': 123,
    'iamRole': 'string',
    'robotApplications': [
        {
            'application': 'string',
            'applicationVersion': 'string',
            'launchConfig': {
                'packageName': 'string',
                'launchFile': 'string',
                'environmentVariables': {
                    'string': 'string'
                },
                'portForwardingConfig': {
                    'portMappings': [
                        {
                            'jobPort': 123,
                            'applicationPort': 123,
                            'enableOnPublicIp': True|False
                        },
                    ]
                },
                'streamUI': True|False
            }
        },
    ],
    'simulationApplications': [
        {
            'application': 'string',
            'applicationVersion': 'string',
            'launchConfig': {
                'packageName': 'string',
                'launchFile': 'string',
                'environmentVariables': {
                    'string': 'string'
                },
                'portForwardingConfig': {
                    'portMappings': [
                        {
                            'jobPort': 123,
                            'applicationPort': 123,
                            'enableOnPublicIp': True|False
                        },
                    ]
                },
                'streamUI': True|False
            }
        },
    ],
    'dataSources': [
        {
            'name': 'string',
            's3Bucket': 'string',
            's3Keys': [
                {
                    's3Key': 'string',
                    'etag': 'string'
                },
            ]
        },
    ],
    'tags': {
        'string': 'string'
    },
    'vpcConfig': {
        'subnets': [
            'string',
        ],
        'securityGroups': [
            'string',
        ],
        'vpcId': 'string',
        'assignPublicIp': True|False
    },
    'compute': {
        'simulationUnitLimit': 123
    }
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the simulation job.

status (string) --
The status of the simulation job.

lastStartedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation job was last started.

lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation job was last updated.

failureBehavior (string) --
the failure behavior for the simulation job.

failureCode (string) --
The failure code of the simulation job if it failed:

InternalServiceError

Internal service error.

RobotApplicationCrash

Robot application exited abnormally.

SimulationApplicationCrash

Simulation application exited abnormally.

BadPermissionsRobotApplication

Robot application bundle could not be downloaded.

BadPermissionsSimulationApplication

Simulation application bundle could not be downloaded.

BadPermissionsS3Output

Unable to publish outputs to customer-provided S3 bucket.

BadPermissionsCloudwatchLogs

Unable to publish logs to customer-provided CloudWatch Logs resource.

SubnetIpLimitExceeded

Subnet IP limit exceeded.

ENILimitExceeded

ENI limit exceeded.

BadPermissionsUserCredentials

Unable to use the Role provided.

InvalidBundleRobotApplication

Robot bundle cannot be extracted (invalid format, bundling error, or other issue).

InvalidBundleSimulationApplication

Simulation bundle cannot be extracted (invalid format, bundling error, or other issue).

RobotApplicationVersionMismatchedEtag

Etag for RobotApplication does not match value during version creation.

SimulationApplicationVersionMismatchedEtag

Etag for SimulationApplication does not match value during version creation.

clientRequestToken (string) --
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

outputLocation (dict) --
Simulation job output files location.

s3Bucket (string) --
The S3 bucket for output.

s3Prefix (string) --
The S3 folder in the s3Bucket where output files will be placed.



loggingConfig (dict) --
The logging configuration.

recordAllRosTopics (boolean) --
A boolean indicating whether to record all ROS topics.



maxJobDurationInSeconds (integer) --
The maximum simulation job duration in seconds.

simulationTimeMillis (integer) --
The simulation job execution duration in milliseconds.

iamRole (string) --
The IAM role that allows the simulation job to call the AWS APIs that are specified in its associated policies on your behalf.

robotApplications (list) --
The robot application used by the simulation job.

(dict) --
Application configuration information for a robot.

application (string) --
The application information for the robot application.

applicationVersion (string) --
The version of the robot application.

launchConfig (dict) --
The launch configuration for the robot application.

packageName (string) --
The package name.

launchFile (string) --
The launch file name.

environmentVariables (dict) --
The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --
The port forwarding configuration.

portMappings (list) --
The port mappings for the configuration.

(dict) --
An object representing a port mapping.

jobPort (integer) --
The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --
The port number on the application.

enableOnPublicIp (boolean) --
A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --
Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







simulationApplications (list) --
The simulation application used by the simulation job.

(dict) --
Information about a simulation application configuration.

application (string) --
The application information for the simulation application.

applicationVersion (string) --
The version of the simulation application.

launchConfig (dict) --
The launch configuration for the simulation application.

packageName (string) --
The package name.

launchFile (string) --
The launch file name.

environmentVariables (dict) --
The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --
The port forwarding configuration.

portMappings (list) --
The port mappings for the configuration.

(dict) --
An object representing a port mapping.

jobPort (integer) --
The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --
The port number on the application.

enableOnPublicIp (boolean) --
A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --
Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







dataSources (list) --
The data sources for the simulation job.

(dict) --
Information about a data source.

name (string) --
The name of the data source.

s3Bucket (string) --
The S3 bucket where the data files are located.

s3Keys (list) --
The list of S3 keys identifying the data source files.

(dict) --
Information about S3 keys.

s3Key (string) --
The S3 key.

etag (string) --
The etag for the object.









tags (dict) --
The list of all tags added to the simulation job.

(string) --
(string) --




vpcConfig (dict) --
Information about the vpc configuration.

subnets (list) --
A list of subnet IDs associated with the simulation job.

(string) --


securityGroups (list) --
A list of security group IDs associated with the simulation job.

(string) --


vpcId (string) --
The VPC ID associated with your simulation job.

assignPublicIp (boolean) --
A boolean indicating if a public IP was assigned.



compute (dict) --
Compute information for the simulation job.

simulationUnitLimit (integer) --
The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided.









Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.IdempotentParameterMismatchException
RoboMaker.Client.exceptions.ServiceUnavailableException


    :return: {
        'arn': 'string',
        'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
        'lastStartedAt': datetime(2015, 1, 1),
        'lastUpdatedAt': datetime(2015, 1, 1),
        'failureBehavior': 'Fail'|'Continue',
        'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
        'clientRequestToken': 'string',
        'outputLocation': {
            's3Bucket': 'string',
            's3Prefix': 'string'
        },
        'loggingConfig': {
            'recordAllRosTopics': True|False
        },
        'maxJobDurationInSeconds': 123,
        'simulationTimeMillis': 123,
        'iamRole': 'string',
        'robotApplications': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    },
                    'portForwardingConfig': {
                        'portMappings': [
                            {
                                'jobPort': 123,
                                'applicationPort': 123,
                                'enableOnPublicIp': True|False
                            },
                        ]
                    },
                    'streamUI': True|False
                }
            },
        ],
        'simulationApplications': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    },
                    'portForwardingConfig': {
                        'portMappings': [
                            {
                                'jobPort': 123,
                                'applicationPort': 123,
                                'enableOnPublicIp': True|False
                            },
                        ]
                    },
                    'streamUI': True|False
                }
            },
        ],
        'dataSources': [
            {
                'name': 'string',
                's3Bucket': 'string',
                's3Keys': [
                    {
                        's3Key': 'string',
                        'etag': 'string'
                    },
                ]
            },
        ],
        'tags': {
            'string': 'string'
        },
        'vpcConfig': {
            'subnets': [
                'string',
            ],
            'securityGroups': [
                'string',
            ],
            'vpcId': 'string',
            'assignPublicIp': True|False
        },
        'compute': {
            'simulationUnitLimit': 123
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_fleet(fleet=None):
    """
    Deletes a fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_fleet(
        fleet='string'
    )
    
    
    :type fleet: string
    :param fleet: [REQUIRED]\nThe Amazon Resource Name (ARN) of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def delete_robot(robot=None):
    """
    Deletes a robot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_robot(
        robot='string'
    )
    
    
    :type robot: string
    :param robot: [REQUIRED]\nThe Amazon Resource Name (ARN) of the robot.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def delete_robot_application(application=None, applicationVersion=None):
    """
    Deletes a robot application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_robot_application(
        application='string',
        applicationVersion='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]\nThe Amazon Resource Name (ARN) of the the robot application.\n

    :type applicationVersion: string
    :param applicationVersion: The version of the robot application to delete.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_simulation_application(application=None, applicationVersion=None):
    """
    Deletes a simulation application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_simulation_application(
        application='string',
        applicationVersion='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]\nThe application information for the simulation application to delete.\n

    :type applicationVersion: string
    :param applicationVersion: The version of the simulation application to delete.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def deregister_robot(fleet=None, robot=None):
    """
    Deregisters a robot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_robot(
        fleet='string',
        robot='string'
    )
    
    
    :type fleet: string
    :param fleet: [REQUIRED]\nThe Amazon Resource Name (ARN) of the fleet.\n

    :type robot: string
    :param robot: [REQUIRED]\nThe Amazon Resource Name (ARN) of the robot.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'fleet': 'string',
    'robot': 'string'
}


Response Structure

(dict) --

fleet (string) --
The Amazon Resource Name (ARN) of the fleet.

robot (string) --
The Amazon Resource Name (ARN) of the robot.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.ResourceNotFoundException


    :return: {
        'fleet': 'string',
        'robot': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    RoboMaker.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_deployment_job(job=None):
    """
    Describes a deployment job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_deployment_job(
        job='string'
    )
    
    
    :type job: string
    :param job: [REQUIRED]\nThe Amazon Resource Name (ARN) of the deployment job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'arn': 'string',
    'fleet': 'string',
    'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
    'deploymentConfig': {
        'concurrentDeploymentPercentage': 123,
        'failureThresholdPercentage': 123,
        'robotDeploymentTimeoutInSeconds': 123,
        'downloadConditionFile': {
            'bucket': 'string',
            'key': 'string',
            'etag': 'string'
        }
    },
    'deploymentApplicationConfigs': [
        {
            'application': 'string',
            'applicationVersion': 'string',
            'launchConfig': {
                'packageName': 'string',
                'preLaunchFile': 'string',
                'launchFile': 'string',
                'postLaunchFile': 'string',
                'environmentVariables': {
                    'string': 'string'
                }
            }
        },
    ],
    'failureReason': 'string',
    'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError',
    'createdAt': datetime(2015, 1, 1),
    'robotDeploymentSummary': [
        {
            'arn': 'string',
            'deploymentStartTime': datetime(2015, 1, 1),
            'deploymentFinishTime': datetime(2015, 1, 1),
            'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
            'progressDetail': {
                'currentProgress': 'Validating'|'DownloadingExtracting'|'ExecutingDownloadCondition'|'ExecutingPreLaunch'|'Launching'|'ExecutingPostLaunch'|'Finished',
                'percentDone': ...,
                'estimatedTimeRemainingSeconds': 123,
                'targetResource': 'string'
            },
            'failureReason': 'string',
            'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError'
        },
    ],
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
arn (string) --The Amazon Resource Name (ARN) of the deployment job.

fleet (string) --The Amazon Resource Name (ARN) of the fleet.

status (string) --The status of the deployment job.

deploymentConfig (dict) --The deployment configuration.

concurrentDeploymentPercentage (integer) --The percentage of robots receiving the deployment at the same time.

failureThresholdPercentage (integer) --The percentage of deployments that need to fail before stopping deployment.

robotDeploymentTimeoutInSeconds (integer) --The amount of time, in seconds, to wait for deployment to a single robot to complete. Choose a time between 1 minute and 7 days. The default is 5 hours.

downloadConditionFile (dict) --The download condition file.

bucket (string) --The bucket containing the object.

key (string) --The key of the object.

etag (string) --The etag of the object.





deploymentApplicationConfigs (list) --The deployment application configuration.

(dict) --Information about a deployment application configuration.

application (string) --The Amazon Resource Name (ARN) of the robot application.

applicationVersion (string) --The version of the application.

launchConfig (dict) --The launch configuration.

packageName (string) --The package name.

preLaunchFile (string) --The deployment pre-launch file. This file will be executed prior to the launch file.

launchFile (string) --The launch file name.

postLaunchFile (string) --The deployment post-launch file. This file will be executed after the launch file.

environmentVariables (dict) --An array of key/value pairs specifying environment variables for the robot application

(string) --
(string) --










failureReason (string) --A short description of the reason why the deployment job failed.

failureCode (string) --The deployment job failure code.

createdAt (datetime) --The time, in milliseconds since the epoch, when the deployment job was created.

robotDeploymentSummary (list) --A list of robot deployment summaries.

(dict) --Information about a robot deployment.

arn (string) --The robot deployment Amazon Resource Name (ARN).

deploymentStartTime (datetime) --The time, in milliseconds since the epoch, when the deployment was started.

deploymentFinishTime (datetime) --The time, in milliseconds since the epoch, when the deployment finished.

status (string) --The status of the robot deployment.

progressDetail (dict) --Information about how the deployment is progressing.

currentProgress (string) --The current progress status.

Validating
Validating the deployment.

DownloadingExtracting
Downloading and extracting the bundle on the robot.

ExecutingPreLaunch
Executing pre-launch script(s) if provided.

Launching
Launching the robot application.

ExecutingPostLaunch
Executing post-launch script(s) if provided.

Finished
Deployment is complete.

percentDone (float) --Precentage of the step that is done. This currently only applies to the Downloading/Extracting step of the deployment. It is empty for other steps.

estimatedTimeRemainingSeconds (integer) --Estimated amount of time in seconds remaining in the step. This currently only applies to the Downloading/Extracting step of the deployment. It is empty for other steps.

targetResource (string) --The Amazon Resource Name (ARN) of the deployment job.



failureReason (string) --A short description of the reason why the robot deployment failed.

failureCode (string) --The robot deployment failure code.





tags (dict) --The list of all tags added to the specified deployment job.

(string) --
(string) --









Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'arn': 'string',
        'fleet': 'string',
        'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
        'deploymentConfig': {
            'concurrentDeploymentPercentage': 123,
            'failureThresholdPercentage': 123,
            'robotDeploymentTimeoutInSeconds': 123,
            'downloadConditionFile': {
                'bucket': 'string',
                'key': 'string',
                'etag': 'string'
            }
        },
        'deploymentApplicationConfigs': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'preLaunchFile': 'string',
                    'launchFile': 'string',
                    'postLaunchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'failureReason': 'string',
        'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError',
        'createdAt': datetime(2015, 1, 1),
        'robotDeploymentSummary': [
            {
                'arn': 'string',
                'deploymentStartTime': datetime(2015, 1, 1),
                'deploymentFinishTime': datetime(2015, 1, 1),
                'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                'progressDetail': {
                    'currentProgress': 'Validating'|'DownloadingExtracting'|'ExecutingDownloadCondition'|'ExecutingPreLaunch'|'Launching'|'ExecutingPostLaunch'|'Finished',
                    'percentDone': ...,
                    'estimatedTimeRemainingSeconds': 123,
                    'targetResource': 'string'
                },
                'failureReason': 'string',
                'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError'
            },
        ],
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_fleet(fleet=None):
    """
    Describes a fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_fleet(
        fleet='string'
    )
    
    
    :type fleet: string
    :param fleet: [REQUIRED]\nThe Amazon Resource Name (ARN) of the fleet.\n

    :rtype: dict
ReturnsResponse Syntax{
    'name': 'string',
    'arn': 'string',
    'robots': [
        {
            'arn': 'string',
            'name': 'string',
            'fleetArn': 'string',
            'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
            'greenGrassGroupId': 'string',
            'createdAt': datetime(2015, 1, 1),
            'architecture': 'X86_64'|'ARM64'|'ARMHF',
            'lastDeploymentJob': 'string',
            'lastDeploymentTime': datetime(2015, 1, 1)
        },
    ],
    'createdAt': datetime(2015, 1, 1),
    'lastDeploymentStatus': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
    'lastDeploymentJob': 'string',
    'lastDeploymentTime': datetime(2015, 1, 1),
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
name (string) --The name of the fleet.

arn (string) --The Amazon Resource Name (ARN) of the fleet.

robots (list) --A list of robots.

(dict) --Information about a robot.

arn (string) --The Amazon Resource Name (ARN) of the robot.

name (string) --The name of the robot.

fleetArn (string) --The Amazon Resource Name (ARN) of the fleet.

status (string) --The status of the robot.

greenGrassGroupId (string) --The Greengrass group associated with the robot.

createdAt (datetime) --The time, in milliseconds since the epoch, when the robot was created.

architecture (string) --The architecture of the robot.

lastDeploymentJob (string) --The Amazon Resource Name (ARN) of the last deployment job.

lastDeploymentTime (datetime) --The time of the last deployment.





createdAt (datetime) --The time, in milliseconds since the epoch, when the fleet was created.

lastDeploymentStatus (string) --The status of the last deployment.

lastDeploymentJob (string) --The Amazon Resource Name (ARN) of the last deployment job.

lastDeploymentTime (datetime) --The time of the last deployment.

tags (dict) --The list of all tags added to the specified fleet.

(string) --
(string) --









Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'name': 'string',
        'arn': 'string',
        'robots': [
            {
                'arn': 'string',
                'name': 'string',
                'fleetArn': 'string',
                'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                'greenGrassGroupId': 'string',
                'createdAt': datetime(2015, 1, 1),
                'architecture': 'X86_64'|'ARM64'|'ARMHF',
                'lastDeploymentJob': 'string',
                'lastDeploymentTime': datetime(2015, 1, 1)
            },
        ],
        'createdAt': datetime(2015, 1, 1),
        'lastDeploymentStatus': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
        'lastDeploymentJob': 'string',
        'lastDeploymentTime': datetime(2015, 1, 1),
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def describe_robot(robot=None):
    """
    Describes a robot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_robot(
        robot='string'
    )
    
    
    :type robot: string
    :param robot: [REQUIRED]\nThe Amazon Resource Name (ARN) of the robot to be described.\n

    :rtype: dict
ReturnsResponse Syntax{
    'arn': 'string',
    'name': 'string',
    'fleetArn': 'string',
    'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
    'greengrassGroupId': 'string',
    'createdAt': datetime(2015, 1, 1),
    'architecture': 'X86_64'|'ARM64'|'ARMHF',
    'lastDeploymentJob': 'string',
    'lastDeploymentTime': datetime(2015, 1, 1),
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
arn (string) --The Amazon Resource Name (ARN) of the robot.

name (string) --The name of the robot.

fleetArn (string) --The Amazon Resource Name (ARN) of the fleet.

status (string) --The status of the fleet.

greengrassGroupId (string) --The Greengrass group id.

createdAt (datetime) --The time, in milliseconds since the epoch, when the robot was created.

architecture (string) --The target architecture of the robot application.

lastDeploymentJob (string) --The Amazon Resource Name (ARN) of the last deployment job.

lastDeploymentTime (datetime) --The time of the last deployment job.

tags (dict) --The list of all tags added to the specified robot.

(string) --
(string) --









Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'arn': 'string',
        'name': 'string',
        'fleetArn': 'string',
        'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
        'greengrassGroupId': 'string',
        'createdAt': datetime(2015, 1, 1),
        'architecture': 'X86_64'|'ARM64'|'ARMHF',
        'lastDeploymentJob': 'string',
        'lastDeploymentTime': datetime(2015, 1, 1),
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def describe_robot_application(application=None, applicationVersion=None):
    """
    Describes a robot application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_robot_application(
        application='string',
        applicationVersion='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]\nThe Amazon Resource Name (ARN) of the robot application.\n

    :type applicationVersion: string
    :param applicationVersion: The version of the robot application to describe.

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'version': 'string',
    'sources': [
        {
            's3Bucket': 'string',
            's3Key': 'string',
            'etag': 'string',
            'architecture': 'X86_64'|'ARM64'|'ARMHF'
        },
    ],
    'robotSoftwareSuite': {
        'name': 'ROS'|'ROS2',
        'version': 'Kinetic'|'Melodic'|'Dashing'
    },
    'revisionId': 'string',
    'lastUpdatedAt': datetime(2015, 1, 1),
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the robot application.

name (string) --
The name of the robot application.

version (string) --
The version of the robot application.

sources (list) --
The sources of the robot application.

(dict) --
Information about a source.

s3Bucket (string) --
The s3 bucket name.

s3Key (string) --
The s3 object key.

etag (string) --
A hash of the object specified by s3Bucket and s3Key .

architecture (string) --
The taget processor architecture for the application.





robotSoftwareSuite (dict) --
The robot software suite (ROS distribution) used by the robot application.

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).



revisionId (string) --
The revision id of the robot application.

lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the robot application was last updated.

tags (dict) --
The list of all tags added to the specified robot application.

(string) --
(string) --










Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'robotSoftwareSuite': {
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        'revisionId': 'string',
        'lastUpdatedAt': datetime(2015, 1, 1),
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_simulation_application(application=None, applicationVersion=None):
    """
    Describes a simulation application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_simulation_application(
        application='string',
        applicationVersion='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]\nThe application information for the simulation application.\n

    :type applicationVersion: string
    :param applicationVersion: The version of the simulation application to describe.

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'version': 'string',
    'sources': [
        {
            's3Bucket': 'string',
            's3Key': 'string',
            'etag': 'string',
            'architecture': 'X86_64'|'ARM64'|'ARMHF'
        },
    ],
    'simulationSoftwareSuite': {
        'name': 'Gazebo'|'RosbagPlay',
        'version': 'string'
    },
    'robotSoftwareSuite': {
        'name': 'ROS'|'ROS2',
        'version': 'Kinetic'|'Melodic'|'Dashing'
    },
    'renderingEngine': {
        'name': 'OGRE',
        'version': 'string'
    },
    'revisionId': 'string',
    'lastUpdatedAt': datetime(2015, 1, 1),
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the robot simulation application.

name (string) --
The name of the simulation application.

version (string) --
The version of the simulation application.

sources (list) --
The sources of the simulation application.

(dict) --
Information about a source.

s3Bucket (string) --
The s3 bucket name.

s3Key (string) --
The s3 object key.

etag (string) --
A hash of the object specified by s3Bucket and s3Key .

architecture (string) --
The taget processor architecture for the application.





simulationSoftwareSuite (dict) --
The simulation software suite used by the simulation application.

name (string) --
The name of the simulation software suite.

version (string) --
The version of the simulation software suite.



robotSoftwareSuite (dict) --
Information about the robot software suite (ROS distribution).

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).



renderingEngine (dict) --
The rendering engine for the simulation application.

name (string) --
The name of the rendering engine.

version (string) --
The version of the rendering engine.



revisionId (string) --
The revision id of the simulation application.

lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation application was last updated.

tags (dict) --
The list of all tags added to the specified simulation application.

(string) --
(string) --










Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'simulationSoftwareSuite': {
            'name': 'Gazebo'|'RosbagPlay',
            'version': 'string'
        },
        'robotSoftwareSuite': {
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        'renderingEngine': {
            'name': 'OGRE',
            'version': 'string'
        },
        'revisionId': 'string',
        'lastUpdatedAt': datetime(2015, 1, 1),
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_simulation_job(job=None):
    """
    Describes a simulation job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_simulation_job(
        job='string'
    )
    
    
    :type job: string
    :param job: [REQUIRED]\nThe Amazon Resource Name (ARN) of the simulation job to be described.\n

    :rtype: dict
ReturnsResponse Syntax{
    'arn': 'string',
    'name': 'string',
    'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
    'lastStartedAt': datetime(2015, 1, 1),
    'lastUpdatedAt': datetime(2015, 1, 1),
    'failureBehavior': 'Fail'|'Continue',
    'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
    'failureReason': 'string',
    'clientRequestToken': 'string',
    'outputLocation': {
        's3Bucket': 'string',
        's3Prefix': 'string'
    },
    'loggingConfig': {
        'recordAllRosTopics': True|False
    },
    'maxJobDurationInSeconds': 123,
    'simulationTimeMillis': 123,
    'iamRole': 'string',
    'robotApplications': [
        {
            'application': 'string',
            'applicationVersion': 'string',
            'launchConfig': {
                'packageName': 'string',
                'launchFile': 'string',
                'environmentVariables': {
                    'string': 'string'
                },
                'portForwardingConfig': {
                    'portMappings': [
                        {
                            'jobPort': 123,
                            'applicationPort': 123,
                            'enableOnPublicIp': True|False
                        },
                    ]
                },
                'streamUI': True|False
            }
        },
    ],
    'simulationApplications': [
        {
            'application': 'string',
            'applicationVersion': 'string',
            'launchConfig': {
                'packageName': 'string',
                'launchFile': 'string',
                'environmentVariables': {
                    'string': 'string'
                },
                'portForwardingConfig': {
                    'portMappings': [
                        {
                            'jobPort': 123,
                            'applicationPort': 123,
                            'enableOnPublicIp': True|False
                        },
                    ]
                },
                'streamUI': True|False
            }
        },
    ],
    'dataSources': [
        {
            'name': 'string',
            's3Bucket': 'string',
            's3Keys': [
                {
                    's3Key': 'string',
                    'etag': 'string'
                },
            ]
        },
    ],
    'tags': {
        'string': 'string'
    },
    'vpcConfig': {
        'subnets': [
            'string',
        ],
        'securityGroups': [
            'string',
        ],
        'vpcId': 'string',
        'assignPublicIp': True|False
    },
    'networkInterface': {
        'networkInterfaceId': 'string',
        'privateIpAddress': 'string',
        'publicIpAddress': 'string'
    },
    'compute': {
        'simulationUnitLimit': 123
    }
}


Response Structure

(dict) --
arn (string) --The Amazon Resource Name (ARN) of the simulation job.

name (string) --The name of the simulation job.

status (string) --The status of the simulation job.

lastStartedAt (datetime) --The time, in milliseconds since the epoch, when the simulation job was last started.

lastUpdatedAt (datetime) --The time, in milliseconds since the epoch, when the simulation job was last updated.

failureBehavior (string) --The failure behavior for the simulation job.

failureCode (string) --The failure code of the simulation job if it failed:

InternalServiceError
Internal service error.

RobotApplicationCrash
Robot application exited abnormally.

SimulationApplicationCrash
Simulation application exited abnormally.

BadPermissionsRobotApplication
Robot application bundle could not be downloaded.

BadPermissionsSimulationApplication
Simulation application bundle could not be downloaded.

BadPermissionsS3Output
Unable to publish outputs to customer-provided S3 bucket.

BadPermissionsCloudwatchLogs
Unable to publish logs to customer-provided CloudWatch Logs resource.

SubnetIpLimitExceeded
Subnet IP limit exceeded.

ENILimitExceeded
ENI limit exceeded.

BadPermissionsUserCredentials
Unable to use the Role provided.

InvalidBundleRobotApplication
Robot bundle cannot be extracted (invalid format, bundling error, or other issue).

InvalidBundleSimulationApplication
Simulation bundle cannot be extracted (invalid format, bundling error, or other issue).

RobotApplicationVersionMismatchedEtag
Etag for RobotApplication does not match value during version creation.

SimulationApplicationVersionMismatchedEtag
Etag for SimulationApplication does not match value during version creation.

failureReason (string) --Details about why the simulation job failed. For more information about troubleshooting, see Troubleshooting .

clientRequestToken (string) --Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

outputLocation (dict) --Location for output files generated by the simulation job.

s3Bucket (string) --The S3 bucket for output.

s3Prefix (string) --The S3 folder in the s3Bucket where output files will be placed.



loggingConfig (dict) --The logging configuration.

recordAllRosTopics (boolean) --A boolean indicating whether to record all ROS topics.



maxJobDurationInSeconds (integer) --The maximum job duration in seconds. The value must be 8 days (691,200 seconds) or less.

simulationTimeMillis (integer) --The simulation job execution duration in milliseconds.

iamRole (string) --The IAM role that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf.

robotApplications (list) --A list of robot applications.

(dict) --Application configuration information for a robot.

application (string) --The application information for the robot application.

applicationVersion (string) --The version of the robot application.

launchConfig (dict) --The launch configuration for the robot application.

packageName (string) --The package name.

launchFile (string) --The launch file name.

environmentVariables (dict) --The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --The port forwarding configuration.

portMappings (list) --The port mappings for the configuration.

(dict) --An object representing a port mapping.

jobPort (integer) --The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --The port number on the application.

enableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







simulationApplications (list) --A list of simulation applications.

(dict) --Information about a simulation application configuration.

application (string) --The application information for the simulation application.

applicationVersion (string) --The version of the simulation application.

launchConfig (dict) --The launch configuration for the simulation application.

packageName (string) --The package name.

launchFile (string) --The launch file name.

environmentVariables (dict) --The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --The port forwarding configuration.

portMappings (list) --The port mappings for the configuration.

(dict) --An object representing a port mapping.

jobPort (integer) --The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --The port number on the application.

enableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







dataSources (list) --The data sources for the simulation job.

(dict) --Information about a data source.

name (string) --The name of the data source.

s3Bucket (string) --The S3 bucket where the data files are located.

s3Keys (list) --The list of S3 keys identifying the data source files.

(dict) --Information about S3 keys.

s3Key (string) --The S3 key.

etag (string) --The etag for the object.









tags (dict) --The list of all tags added to the specified simulation job.

(string) --
(string) --




vpcConfig (dict) --The VPC configuration.

subnets (list) --A list of subnet IDs associated with the simulation job.

(string) --


securityGroups (list) --A list of security group IDs associated with the simulation job.

(string) --


vpcId (string) --The VPC ID associated with your simulation job.

assignPublicIp (boolean) --A boolean indicating if a public IP was assigned.



networkInterface (dict) --The network interface information for the simulation job.

networkInterfaceId (string) --The ID of the network interface.

privateIpAddress (string) --The IPv4 address of the network interface within the subnet.

publicIpAddress (string) --The IPv4 public address of the network interface.



compute (dict) --Compute information for the simulation job.

simulationUnitLimit (integer) --The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided.








Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'arn': 'string',
        'name': 'string',
        'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
        'lastStartedAt': datetime(2015, 1, 1),
        'lastUpdatedAt': datetime(2015, 1, 1),
        'failureBehavior': 'Fail'|'Continue',
        'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
        'failureReason': 'string',
        'clientRequestToken': 'string',
        'outputLocation': {
            's3Bucket': 'string',
            's3Prefix': 'string'
        },
        'loggingConfig': {
            'recordAllRosTopics': True|False
        },
        'maxJobDurationInSeconds': 123,
        'simulationTimeMillis': 123,
        'iamRole': 'string',
        'robotApplications': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    },
                    'portForwardingConfig': {
                        'portMappings': [
                            {
                                'jobPort': 123,
                                'applicationPort': 123,
                                'enableOnPublicIp': True|False
                            },
                        ]
                    },
                    'streamUI': True|False
                }
            },
        ],
        'simulationApplications': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'launchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    },
                    'portForwardingConfig': {
                        'portMappings': [
                            {
                                'jobPort': 123,
                                'applicationPort': 123,
                                'enableOnPublicIp': True|False
                            },
                        ]
                    },
                    'streamUI': True|False
                }
            },
        ],
        'dataSources': [
            {
                'name': 'string',
                's3Bucket': 'string',
                's3Keys': [
                    {
                        's3Key': 'string',
                        'etag': 'string'
                    },
                ]
            },
        ],
        'tags': {
            'string': 'string'
        },
        'vpcConfig': {
            'subnets': [
                'string',
            ],
            'securityGroups': [
                'string',
            ],
            'vpcId': 'string',
            'assignPublicIp': True|False
        },
        'networkInterface': {
            'networkInterfaceId': 'string',
            'privateIpAddress': 'string',
            'publicIpAddress': 'string'
        },
        'compute': {
            'simulationUnitLimit': 123
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_simulation_job_batch(batch=None):
    """
    Describes a simulation job batch.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_simulation_job_batch(
        batch='string'
    )
    
    
    :type batch: string
    :param batch: [REQUIRED]\nThe id of the batch to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'arn': 'string',
    'status': 'Pending'|'InProgress'|'Failed'|'Completed'|'Canceled'|'Canceling'|'Completing'|'TimingOut'|'TimedOut',
    'lastUpdatedAt': datetime(2015, 1, 1),
    'createdAt': datetime(2015, 1, 1),
    'clientRequestToken': 'string',
    'batchPolicy': {
        'timeoutInSeconds': 123,
        'maxConcurrency': 123
    },
    'failureCode': 'InternalServiceError',
    'failureReason': 'string',
    'failedRequests': [
        {
            'request': {
                'outputLocation': {
                    's3Bucket': 'string',
                    's3Prefix': 'string'
                },
                'loggingConfig': {
                    'recordAllRosTopics': True|False
                },
                'maxJobDurationInSeconds': 123,
                'iamRole': 'string',
                'failureBehavior': 'Fail'|'Continue',
                'useDefaultApplications': True|False,
                'robotApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'simulationApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'dataSources': [
                    {
                        'name': 'string',
                        's3Bucket': 'string',
                        's3Keys': [
                            'string',
                        ]
                    },
                ],
                'vpcConfig': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'assignPublicIp': True|False
                },
                'compute': {
                    'simulationUnitLimit': 123
                },
                'tags': {
                    'string': 'string'
                }
            },
            'failureReason': 'string',
            'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
            'failedAt': datetime(2015, 1, 1)
        },
    ],
    'pendingRequests': [
        {
            'outputLocation': {
                's3Bucket': 'string',
                's3Prefix': 'string'
            },
            'loggingConfig': {
                'recordAllRosTopics': True|False
            },
            'maxJobDurationInSeconds': 123,
            'iamRole': 'string',
            'failureBehavior': 'Fail'|'Continue',
            'useDefaultApplications': True|False,
            'robotApplications': [
                {
                    'application': 'string',
                    'applicationVersion': 'string',
                    'launchConfig': {
                        'packageName': 'string',
                        'launchFile': 'string',
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'portForwardingConfig': {
                            'portMappings': [
                                {
                                    'jobPort': 123,
                                    'applicationPort': 123,
                                    'enableOnPublicIp': True|False
                                },
                            ]
                        },
                        'streamUI': True|False
                    }
                },
            ],
            'simulationApplications': [
                {
                    'application': 'string',
                    'applicationVersion': 'string',
                    'launchConfig': {
                        'packageName': 'string',
                        'launchFile': 'string',
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'portForwardingConfig': {
                            'portMappings': [
                                {
                                    'jobPort': 123,
                                    'applicationPort': 123,
                                    'enableOnPublicIp': True|False
                                },
                            ]
                        },
                        'streamUI': True|False
                    }
                },
            ],
            'dataSources': [
                {
                    'name': 'string',
                    's3Bucket': 'string',
                    's3Keys': [
                        'string',
                    ]
                },
            ],
            'vpcConfig': {
                'subnets': [
                    'string',
                ],
                'securityGroups': [
                    'string',
                ],
                'assignPublicIp': True|False
            },
            'compute': {
                'simulationUnitLimit': 123
            },
            'tags': {
                'string': 'string'
            }
        },
    ],
    'createdRequests': [
        {
            'arn': 'string',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'name': 'string',
            'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
            'simulationApplicationNames': [
                'string',
            ],
            'robotApplicationNames': [
                'string',
            ],
            'dataSourceNames': [
                'string',
            ]
        },
    ],
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
arn (string) --The Amazon Resource Name (ARN) of the batch.

status (string) --The status of the batch.

Pending
The simulation job batch request is pending.

InProgress
The simulation job batch is in progress.

Failed
The simulation job batch failed. One or more simulation job requests could not be completed due to an internal failure (like InternalServiceError ). See failureCode and failureReason for more information.

Completed
The simulation batch job completed. A batch is complete when (1) there are no pending simulation job requests in the batch and none of the failed simulation job requests are due to InternalServiceError and (2) when all created simulation jobs have reached a terminal state (for example, Completed or Failed ).

Canceled
The simulation batch job was cancelled.

Canceling
The simulation batch job is being cancelled.

Completing
The simulation batch job is completing.

TimingOut
The simulation job batch is timing out.
If a batch timing out, and there are pending requests that were failing due to an internal failure (like InternalServiceError ), the batch status will be Failed . If there are no such failing request, the batch status will be TimedOut .

TimedOut
The simulation batch job timed out.

lastUpdatedAt (datetime) --The time, in milliseconds since the epoch, when the simulation job batch was last updated.

createdAt (datetime) --The time, in milliseconds since the epoch, when the simulation job batch was created.

clientRequestToken (string) --Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

batchPolicy (dict) --The batch policy.

timeoutInSeconds (integer) --The amount of time, in seconds, to wait for the batch to complete.
If a batch times out, and there are pending requests that were failing due to an internal failure (like InternalServiceError ), they will be moved to the failed list and the batch status will be Failed . If the pending requests were failing for any other reason, the failed pending requests will be moved to the failed list and the batch status will be TimedOut .

maxConcurrency (integer) --The number of active simulation jobs create as part of the batch that can be in an active state at the same time.
Active states include: Pending ,``Preparing`` , Running , Restarting , RunningFailed and Terminating . All other states are terminal states.



failureCode (string) --The failure code of the simulation job batch.

failureReason (string) --The reason the simulation job batch failed.

failedRequests (list) --A list of failed create simulation job requests. The request failed to be created into a simulation job. Failed requests do not have a simulation job ID.

(dict) --Information about a failed create simulation job request.

request (dict) --The simulation job request.

outputLocation (dict) --The output location.

s3Bucket (string) --The S3 bucket for output.

s3Prefix (string) --The S3 folder in the s3Bucket where output files will be placed.



loggingConfig (dict) --The logging configuration.

recordAllRosTopics (boolean) --A boolean indicating whether to record all ROS topics.



maxJobDurationInSeconds (integer) --The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.

iamRole (string) --The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

failureBehavior (string) --The failure behavior the simulation job.

Continue
Restart the simulation job in the same host instance.

Fail
Stop the simulation job and terminate the instance.

useDefaultApplications (boolean) --Boolean indicating whether to use default simulation tool applications.

robotApplications (list) --The robot applications to use in the simulation job.

(dict) --Application configuration information for a robot.

application (string) --The application information for the robot application.

applicationVersion (string) --The version of the robot application.

launchConfig (dict) --The launch configuration for the robot application.

packageName (string) --The package name.

launchFile (string) --The launch file name.

environmentVariables (dict) --The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --The port forwarding configuration.

portMappings (list) --The port mappings for the configuration.

(dict) --An object representing a port mapping.

jobPort (integer) --The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --The port number on the application.

enableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







simulationApplications (list) --The simulation applications to use in the simulation job.

(dict) --Information about a simulation application configuration.

application (string) --The application information for the simulation application.

applicationVersion (string) --The version of the simulation application.

launchConfig (dict) --The launch configuration for the simulation application.

packageName (string) --The package name.

launchFile (string) --The launch file name.

environmentVariables (dict) --The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --The port forwarding configuration.

portMappings (list) --The port mappings for the configuration.

(dict) --An object representing a port mapping.

jobPort (integer) --The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --The port number on the application.

enableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







dataSources (list) --Specify data sources to mount read-only files from S3 into your simulation. These files are available under /opt/robomaker/datasources/data_source_name .

Note
There is a limit of 100 files and a combined size of 25GB for all DataSourceConfig objects.


(dict) --Information about a data source.

name (string) --The name of the data source.

s3Bucket (string) --The S3 bucket where the data files are located.

s3Keys (list) --The list of S3 keys identifying the data source files.

(string) --






vpcConfig (dict) --If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.

subnets (list) --A list of one or more subnet IDs in your VPC.

(string) --


securityGroups (list) --A list of one or more security groups IDs in your VPC.

(string) --


assignPublicIp (boolean) --A boolean indicating whether to assign a public IP address.



compute (dict) --Compute information for the simulation job

simulationUnitLimit (integer) --The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided.



tags (dict) --A map that contains tag keys and tag values that are attached to the simulation job request.

(string) --
(string) --






failureReason (string) --The failure reason of the simulation job request.

failureCode (string) --The failure code.

failedAt (datetime) --The time, in milliseconds since the epoch, when the simulation job batch failed.





pendingRequests (list) --A list of pending simulation job requests. These requests have not yet been created into simulation jobs.

(dict) --Information about a simulation job request.

outputLocation (dict) --The output location.

s3Bucket (string) --The S3 bucket for output.

s3Prefix (string) --The S3 folder in the s3Bucket where output files will be placed.



loggingConfig (dict) --The logging configuration.

recordAllRosTopics (boolean) --A boolean indicating whether to record all ROS topics.



maxJobDurationInSeconds (integer) --The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.

iamRole (string) --The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

failureBehavior (string) --The failure behavior the simulation job.

Continue
Restart the simulation job in the same host instance.

Fail
Stop the simulation job and terminate the instance.

useDefaultApplications (boolean) --Boolean indicating whether to use default simulation tool applications.

robotApplications (list) --The robot applications to use in the simulation job.

(dict) --Application configuration information for a robot.

application (string) --The application information for the robot application.

applicationVersion (string) --The version of the robot application.

launchConfig (dict) --The launch configuration for the robot application.

packageName (string) --The package name.

launchFile (string) --The launch file name.

environmentVariables (dict) --The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --The port forwarding configuration.

portMappings (list) --The port mappings for the configuration.

(dict) --An object representing a port mapping.

jobPort (integer) --The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --The port number on the application.

enableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







simulationApplications (list) --The simulation applications to use in the simulation job.

(dict) --Information about a simulation application configuration.

application (string) --The application information for the simulation application.

applicationVersion (string) --The version of the simulation application.

launchConfig (dict) --The launch configuration for the simulation application.

packageName (string) --The package name.

launchFile (string) --The launch file name.

environmentVariables (dict) --The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --The port forwarding configuration.

portMappings (list) --The port mappings for the configuration.

(dict) --An object representing a port mapping.

jobPort (integer) --The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --The port number on the application.

enableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







dataSources (list) --Specify data sources to mount read-only files from S3 into your simulation. These files are available under /opt/robomaker/datasources/data_source_name .

Note
There is a limit of 100 files and a combined size of 25GB for all DataSourceConfig objects.


(dict) --Information about a data source.

name (string) --The name of the data source.

s3Bucket (string) --The S3 bucket where the data files are located.

s3Keys (list) --The list of S3 keys identifying the data source files.

(string) --






vpcConfig (dict) --If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.

subnets (list) --A list of one or more subnet IDs in your VPC.

(string) --


securityGroups (list) --A list of one or more security groups IDs in your VPC.

(string) --


assignPublicIp (boolean) --A boolean indicating whether to assign a public IP address.



compute (dict) --Compute information for the simulation job

simulationUnitLimit (integer) --The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided.



tags (dict) --A map that contains tag keys and tag values that are attached to the simulation job request.

(string) --
(string) --








createdRequests (list) --A list of created simulation job summaries.

(dict) --Summary information for a simulation job.

arn (string) --The Amazon Resource Name (ARN) of the simulation job.

lastUpdatedAt (datetime) --The time, in milliseconds since the epoch, when the simulation job was last updated.

name (string) --The name of the simulation job.

status (string) --The status of the simulation job.

simulationApplicationNames (list) --A list of simulation job simulation application names.

(string) --


robotApplicationNames (list) --A list of simulation job robot application names.

(string) --


dataSourceNames (list) --The names of the data sources.

(string) --






tags (dict) --A map that contains tag keys and tag values that are attached to the simulation job batch.

(string) --
(string) --









Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'arn': 'string',
        'status': 'Pending'|'InProgress'|'Failed'|'Completed'|'Canceled'|'Canceling'|'Completing'|'TimingOut'|'TimedOut',
        'lastUpdatedAt': datetime(2015, 1, 1),
        'createdAt': datetime(2015, 1, 1),
        'clientRequestToken': 'string',
        'batchPolicy': {
            'timeoutInSeconds': 123,
            'maxConcurrency': 123
        },
        'failureCode': 'InternalServiceError',
        'failureReason': 'string',
        'failedRequests': [
            {
                'request': {
                    'outputLocation': {
                        's3Bucket': 'string',
                        's3Prefix': 'string'
                    },
                    'loggingConfig': {
                        'recordAllRosTopics': True|False
                    },
                    'maxJobDurationInSeconds': 123,
                    'iamRole': 'string',
                    'failureBehavior': 'Fail'|'Continue',
                    'useDefaultApplications': True|False,
                    'robotApplications': [
                        {
                            'application': 'string',
                            'applicationVersion': 'string',
                            'launchConfig': {
                                'packageName': 'string',
                                'launchFile': 'string',
                                'environmentVariables': {
                                    'string': 'string'
                                },
                                'portForwardingConfig': {
                                    'portMappings': [
                                        {
                                            'jobPort': 123,
                                            'applicationPort': 123,
                                            'enableOnPublicIp': True|False
                                        },
                                    ]
                                },
                                'streamUI': True|False
                            }
                        },
                    ],
                    'simulationApplications': [
                        {
                            'application': 'string',
                            'applicationVersion': 'string',
                            'launchConfig': {
                                'packageName': 'string',
                                'launchFile': 'string',
                                'environmentVariables': {
                                    'string': 'string'
                                },
                                'portForwardingConfig': {
                                    'portMappings': [
                                        {
                                            'jobPort': 123,
                                            'applicationPort': 123,
                                            'enableOnPublicIp': True|False
                                        },
                                    ]
                                },
                                'streamUI': True|False
                            }
                        },
                    ],
                    'dataSources': [
                        {
                            'name': 'string',
                            's3Bucket': 'string',
                            's3Keys': [
                                'string',
                            ]
                        },
                    ],
                    'vpcConfig': {
                        'subnets': [
                            'string',
                        ],
                        'securityGroups': [
                            'string',
                        ],
                        'assignPublicIp': True|False
                    },
                    'compute': {
                        'simulationUnitLimit': 123
                    },
                    'tags': {
                        'string': 'string'
                    }
                },
                'failureReason': 'string',
                'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
                'failedAt': datetime(2015, 1, 1)
            },
        ],
        'pendingRequests': [
            {
                'outputLocation': {
                    's3Bucket': 'string',
                    's3Prefix': 'string'
                },
                'loggingConfig': {
                    'recordAllRosTopics': True|False
                },
                'maxJobDurationInSeconds': 123,
                'iamRole': 'string',
                'failureBehavior': 'Fail'|'Continue',
                'useDefaultApplications': True|False,
                'robotApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'simulationApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'dataSources': [
                    {
                        'name': 'string',
                        's3Bucket': 'string',
                        's3Keys': [
                            'string',
                        ]
                    },
                ],
                'vpcConfig': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'assignPublicIp': True|False
                },
                'compute': {
                    'simulationUnitLimit': 123
                },
                'tags': {
                    'string': 'string'
                }
            },
        ],
        'createdRequests': [
            {
                'arn': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'name': 'string',
                'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                'simulationApplicationNames': [
                    'string',
                ],
                'robotApplicationNames': [
                    'string',
                ],
                'dataSourceNames': [
                    'string',
                ]
            },
        ],
        'tags': {
            'string': 'string'
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def list_deployment_jobs(filters=None, nextToken=None, maxResults=None):
    """
    Returns a list of deployment jobs for a fleet. You can optionally provide filters to retrieve specific deployment jobs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_deployment_jobs(
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type filters: list
    :param filters: Optional filters to limit results.\nThe filter names status and fleetName are supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters, but they must be for the same named item. For example, if you are looking for items with the status InProgress or the status Pending .\n\n(dict) --Information about a filter.\n\nname (string) --The name of the filter.\n\nvalues (list) --A list of values.\n\n(string) --\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListDeploymentJobs request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type maxResults: integer
    :param maxResults: When this parameter is used, ListDeploymentJobs only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListDeploymentJobs request with the returned nextToken value. This value can be between 1 and 200. If this parameter is not used, then ListDeploymentJobs returns up to 200 results and a nextToken value if applicable.

    :rtype: dict

ReturnsResponse Syntax
{
    'deploymentJobs': [
        {
            'arn': 'string',
            'fleet': 'string',
            'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
            'deploymentApplicationConfigs': [
                {
                    'application': 'string',
                    'applicationVersion': 'string',
                    'launchConfig': {
                        'packageName': 'string',
                        'preLaunchFile': 'string',
                        'launchFile': 'string',
                        'postLaunchFile': 'string',
                        'environmentVariables': {
                            'string': 'string'
                        }
                    }
                },
            ],
            'deploymentConfig': {
                'concurrentDeploymentPercentage': 123,
                'failureThresholdPercentage': 123,
                'robotDeploymentTimeoutInSeconds': 123,
                'downloadConditionFile': {
                    'bucket': 'string',
                    'key': 'string',
                    'etag': 'string'
                }
            },
            'failureReason': 'string',
            'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError',
            'createdAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

deploymentJobs (list) --
A list of deployment jobs that meet the criteria of the request.

(dict) --
Information about a deployment job.

arn (string) --
The Amazon Resource Name (ARN) of the deployment job.

fleet (string) --
The Amazon Resource Name (ARN) of the fleet.

status (string) --
The status of the deployment job.

deploymentApplicationConfigs (list) --
The deployment application configuration.

(dict) --
Information about a deployment application configuration.

application (string) --
The Amazon Resource Name (ARN) of the robot application.

applicationVersion (string) --
The version of the application.

launchConfig (dict) --
The launch configuration.

packageName (string) --
The package name.

preLaunchFile (string) --
The deployment pre-launch file. This file will be executed prior to the launch file.

launchFile (string) --
The launch file name.

postLaunchFile (string) --
The deployment post-launch file. This file will be executed after the launch file.

environmentVariables (dict) --
An array of key/value pairs specifying environment variables for the robot application

(string) --
(string) --










deploymentConfig (dict) --
The deployment configuration.

concurrentDeploymentPercentage (integer) --
The percentage of robots receiving the deployment at the same time.

failureThresholdPercentage (integer) --
The percentage of deployments that need to fail before stopping deployment.

robotDeploymentTimeoutInSeconds (integer) --
The amount of time, in seconds, to wait for deployment to a single robot to complete. Choose a time between 1 minute and 7 days. The default is 5 hours.

downloadConditionFile (dict) --
The download condition file.

bucket (string) --
The bucket containing the object.

key (string) --
The key of the object.

etag (string) --
The etag of the object.





failureReason (string) --
A short description of the reason why the deployment job failed.

failureCode (string) --
The deployment job failure code.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the deployment job was created.





nextToken (string) --
The nextToken value to include in a future ListDeploymentJobs request. When the results of a ListDeploymentJobs request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'deploymentJobs': [
            {
                'arn': 'string',
                'fleet': 'string',
                'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
                'deploymentApplicationConfigs': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'preLaunchFile': 'string',
                            'launchFile': 'string',
                            'postLaunchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'deploymentConfig': {
                    'concurrentDeploymentPercentage': 123,
                    'failureThresholdPercentage': 123,
                    'robotDeploymentTimeoutInSeconds': 123,
                    'downloadConditionFile': {
                        'bucket': 'string',
                        'key': 'string',
                        'etag': 'string'
                    }
                },
                'failureReason': 'string',
                'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError',
                'createdAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_fleets(nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of fleets. You can optionally provide filters to retrieve specific fleets.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_fleets(
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListFleets request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :type maxResults: integer
    :param maxResults: When this parameter is used, ListFleets only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListFleets request with the returned nextToken value. This value can be between 1 and 200. If this parameter is not used, then ListFleets returns up to 200 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional filters to limit results.\nThe filter name name is supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters.\n\n(dict) --Information about a filter.\n\nname (string) --The name of the filter.\n\nvalues (list) --A list of values.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'fleetDetails': [
        {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastDeploymentStatus': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
            'lastDeploymentJob': 'string',
            'lastDeploymentTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

fleetDetails (list) --
A list of fleet details meeting the request criteria.

(dict) --
Information about a fleet.

name (string) --
The name of the fleet.

arn (string) --
The Amazon Resource Name (ARN) of the fleet.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the fleet was created.

lastDeploymentStatus (string) --
The status of the last fleet deployment.

lastDeploymentJob (string) --
The Amazon Resource Name (ARN) of the last deployment job.

lastDeploymentTime (datetime) --
The time of the last deployment.





nextToken (string) --
The nextToken value to include in a future ListDeploymentJobs request. When the results of a ListFleets request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'fleetDetails': [
            {
                'name': 'string',
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastDeploymentStatus': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
                'lastDeploymentJob': 'string',
                'lastDeploymentTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def list_robot_applications(versionQualifier=None, nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of robot application. You can optionally provide filters to retrieve specific robot applications.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_robot_applications(
        versionQualifier='string',
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type versionQualifier: string
    :param versionQualifier: The version qualifier of the robot application.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListRobotApplications request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type maxResults: integer
    :param maxResults: When this parameter is used, ListRobotApplications only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListRobotApplications request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListRobotApplications returns up to 100 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional filters to limit results.\nThe filter name name is supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters.\n\n(dict) --Information about a filter.\n\nname (string) --The name of the filter.\n\nvalues (list) --A list of values.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'robotApplicationSummaries': [
        {
            'name': 'string',
            'arn': 'string',
            'version': 'string',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'robotSoftwareSuite': {
                'name': 'ROS'|'ROS2',
                'version': 'Kinetic'|'Melodic'|'Dashing'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

robotApplicationSummaries (list) --
A list of robot application summaries that meet the criteria of the request.

(dict) --
Summary information for a robot application.

name (string) --
The name of the robot application.

arn (string) --
The Amazon Resource Name (ARN) of the robot.

version (string) --
The version of the robot application.

lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the robot application was last updated.

robotSoftwareSuite (dict) --
Information about a robot software suite (ROS distribution).

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).







nextToken (string) --
The nextToken value to include in a future ListRobotApplications request. When the results of a ListRobotApplications request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'robotApplicationSummaries': [
            {
                'name': 'string',
                'arn': 'string',
                'version': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'robotSoftwareSuite': {
                    'name': 'ROS'|'ROS2',
                    'version': 'Kinetic'|'Melodic'|'Dashing'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.ThrottlingException
    RoboMaker.Client.exceptions.InternalServerException
    
    """
    pass

def list_robots(nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of robots. You can optionally provide filters to retrieve specific robots.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_robots(
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListRobots request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type maxResults: integer
    :param maxResults: When this parameter is used, ListRobots only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListRobots request with the returned nextToken value. This value can be between 1 and 200. If this parameter is not used, then ListRobots returns up to 200 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional filters to limit results.\nThe filter names status and fleetName are supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters, but they must be for the same named item. For example, if you are looking for items with the status Registered or the status Available .\n\n(dict) --Information about a filter.\n\nname (string) --The name of the filter.\n\nvalues (list) --A list of values.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'robots': [
        {
            'arn': 'string',
            'name': 'string',
            'fleetArn': 'string',
            'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
            'greenGrassGroupId': 'string',
            'createdAt': datetime(2015, 1, 1),
            'architecture': 'X86_64'|'ARM64'|'ARMHF',
            'lastDeploymentJob': 'string',
            'lastDeploymentTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

robots (list) --
A list of robots that meet the criteria of the request.

(dict) --
Information about a robot.

arn (string) --
The Amazon Resource Name (ARN) of the robot.

name (string) --
The name of the robot.

fleetArn (string) --
The Amazon Resource Name (ARN) of the fleet.

status (string) --
The status of the robot.

greenGrassGroupId (string) --
The Greengrass group associated with the robot.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the robot was created.

architecture (string) --
The architecture of the robot.

lastDeploymentJob (string) --
The Amazon Resource Name (ARN) of the last deployment job.

lastDeploymentTime (datetime) --
The time of the last deployment.





nextToken (string) --
The nextToken value to include in a future ListRobots request. When the results of a ListRobot request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'robots': [
            {
                'arn': 'string',
                'name': 'string',
                'fleetArn': 'string',
                'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                'greenGrassGroupId': 'string',
                'createdAt': datetime(2015, 1, 1),
                'architecture': 'X86_64'|'ARM64'|'ARMHF',
                'lastDeploymentJob': 'string',
                'lastDeploymentTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def list_simulation_applications(versionQualifier=None, nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of simulation applications. You can optionally provide filters to retrieve specific simulation applications.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_simulation_applications(
        versionQualifier='string',
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type versionQualifier: string
    :param versionQualifier: The version qualifier of the simulation application.

    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListSimulationApplications request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type maxResults: integer
    :param maxResults: When this parameter is used, ListSimulationApplications only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListSimulationApplications request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListSimulationApplications returns up to 100 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional list of filters to limit results.\nThe filter name name is supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters.\n\n(dict) --Information about a filter.\n\nname (string) --The name of the filter.\n\nvalues (list) --A list of values.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'simulationApplicationSummaries': [
        {
            'name': 'string',
            'arn': 'string',
            'version': 'string',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'robotSoftwareSuite': {
                'name': 'ROS'|'ROS2',
                'version': 'Kinetic'|'Melodic'|'Dashing'
            },
            'simulationSoftwareSuite': {
                'name': 'Gazebo'|'RosbagPlay',
                'version': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

simulationApplicationSummaries (list) --
A list of simulation application summaries that meet the criteria of the request.

(dict) --
Summary information for a simulation application.

name (string) --
The name of the simulation application.

arn (string) --
The Amazon Resource Name (ARN) of the simulation application.

version (string) --
The version of the simulation application.

lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation application was last updated.

robotSoftwareSuite (dict) --
Information about a robot software suite (ROS distribution).

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).



simulationSoftwareSuite (dict) --
Information about a simulation software suite.

name (string) --
The name of the simulation software suite.

version (string) --
The version of the simulation software suite.







nextToken (string) --
The nextToken value to include in a future ListSimulationApplications request. When the results of a ListRobot request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'simulationApplicationSummaries': [
            {
                'name': 'string',
                'arn': 'string',
                'version': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'robotSoftwareSuite': {
                    'name': 'ROS'|'ROS2',
                    'version': 'Kinetic'|'Melodic'|'Dashing'
                },
                'simulationSoftwareSuite': {
                    'name': 'Gazebo'|'RosbagPlay',
                    'version': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.ThrottlingException
    RoboMaker.Client.exceptions.InternalServerException
    
    """
    pass

def list_simulation_job_batches(nextToken=None, maxResults=None, filters=None):
    """
    Returns a list simulation job batches. You can optionally provide filters to retrieve specific simulation batch jobs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_simulation_job_batches(
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListSimulationJobBatches request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.

    :type maxResults: integer
    :param maxResults: When this parameter is used, ListSimulationJobBatches only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListSimulationJobBatches request with the returned nextToken value.

    :type filters: list
    :param filters: Optional filters to limit results.\n\n(dict) --Information about a filter.\n\nname (string) --The name of the filter.\n\nvalues (list) --A list of values.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'simulationJobBatchSummaries': [
        {
            'arn': 'string',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'createdAt': datetime(2015, 1, 1),
            'status': 'Pending'|'InProgress'|'Failed'|'Completed'|'Canceled'|'Canceling'|'Completing'|'TimingOut'|'TimedOut',
            'failedRequestCount': 123,
            'pendingRequestCount': 123,
            'createdRequestCount': 123
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

simulationJobBatchSummaries (list) --
A list of simulation job batch summaries.

(dict) --
Information about a simulation job batch.

arn (string) --
The Amazon Resource Name (ARN) of the batch.

lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation job batch was last updated.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the simulation job batch was created.

status (string) --
The status of the simulation job batch.

Pending

The simulation job batch request is pending.

InProgress

The simulation job batch is in progress.

Failed

The simulation job batch failed. One or more simulation job requests could not be completed due to an internal failure (like InternalServiceError ). See failureCode and failureReason for more information.

Completed

The simulation batch job completed. A batch is complete when (1) there are no pending simulation job requests in the batch and none of the failed simulation job requests are due to InternalServiceError and (2) when all created simulation jobs have reached a terminal state (for example, Completed or Failed ).

Canceled

The simulation batch job was cancelled.

Canceling

The simulation batch job is being cancelled.

Completing

The simulation batch job is completing.

TimingOut

The simulation job batch is timing out.
If a batch timing out, and there are pending requests that were failing due to an internal failure (like InternalServiceError ), the batch status will be Failed . If there are no such failing request, the batch status will be TimedOut .

TimedOut

The simulation batch job timed out.

failedRequestCount (integer) --
The number of failed simulation job requests.

pendingRequestCount (integer) --
The number of pending simulation job requests.

createdRequestCount (integer) --
The number of created simulation job requests.





nextToken (string) --
The nextToken value to include in a future ListSimulationJobBatches request. When the results of a ListSimulationJobBatches request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'simulationJobBatchSummaries': [
            {
                'arn': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'createdAt': datetime(2015, 1, 1),
                'status': 'Pending'|'InProgress'|'Failed'|'Completed'|'Canceled'|'Canceling'|'Completing'|'TimingOut'|'TimedOut',
                'failedRequestCount': 123,
                'pendingRequestCount': 123,
                'createdRequestCount': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    
    """
    pass

def list_simulation_jobs(nextToken=None, maxResults=None, filters=None):
    """
    Returns a list of simulation jobs. You can optionally provide filters to retrieve specific simulation jobs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_simulation_jobs(
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'string',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type nextToken: string
    :param nextToken: The nextToken value returned from a previous paginated ListSimulationJobs request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.\n\nNote\nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :type maxResults: integer
    :param maxResults: When this parameter is used, ListSimulationJobs only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListSimulationJobs request with the returned nextToken value. This value can be between 1 and 1000. If this parameter is not used, then ListSimulationJobs returns up to 1000 results and a nextToken value if applicable.

    :type filters: list
    :param filters: Optional filters to limit results.\nThe filter names status and simulationApplicationName and robotApplicationName are supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters, but they must be for the same named item. For example, if you are looking for items with the status Preparing or the status Running .\n\n(dict) --Information about a filter.\n\nname (string) --The name of the filter.\n\nvalues (list) --A list of values.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'simulationJobSummaries': [
        {
            'arn': 'string',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'name': 'string',
            'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
            'simulationApplicationNames': [
                'string',
            ],
            'robotApplicationNames': [
                'string',
            ],
            'dataSourceNames': [
                'string',
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

simulationJobSummaries (list) --
A list of simulation job summaries that meet the criteria of the request.

(dict) --
Summary information for a simulation job.

arn (string) --
The Amazon Resource Name (ARN) of the simulation job.

lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation job was last updated.

name (string) --
The name of the simulation job.

status (string) --
The status of the simulation job.

simulationApplicationNames (list) --
A list of simulation job simulation application names.

(string) --


robotApplicationNames (list) --
A list of simulation job robot application names.

(string) --


dataSourceNames (list) --
The names of the data sources.

(string) --






nextToken (string) --
The nextToken value to include in a future ListSimulationJobs request. When the results of a ListRobot request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'simulationJobSummaries': [
            {
                'arn': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'name': 'string',
                'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                'simulationApplicationNames': [
                    'string',
                ],
                'robotApplicationNames': [
                    'string',
                ],
                'dataSourceNames': [
                    'string',
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Lists all tags on a AWS RoboMaker resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe AWS RoboMaker Amazon Resource Name (ARN) with tags to be listed.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --The list of all tags added to the specified resource.

(string) --
(string) --









Exceptions

RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.ThrottlingException
    
    """
    pass

def register_robot(fleet=None, robot=None):
    """
    Registers a robot with a fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_robot(
        fleet='string',
        robot='string'
    )
    
    
    :type fleet: string
    :param fleet: [REQUIRED]\nThe Amazon Resource Name (ARN) of the fleet.\n

    :type robot: string
    :param robot: [REQUIRED]\nThe Amazon Resource Name (ARN) of the robot.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'fleet': 'string',
    'robot': 'string'
}


Response Structure

(dict) --

fleet (string) --
The Amazon Resource Name (ARN) of the fleet that the robot will join.

robot (string) --
Information about the robot registration.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ResourceNotFoundException


    :return: {
        'fleet': 'string',
        'robot': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    RoboMaker.Client.exceptions.ThrottlingException
    RoboMaker.Client.exceptions.LimitExceededException
    RoboMaker.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def restart_simulation_job(job=None):
    """
    Restarts a running simulation job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restart_simulation_job(
        job='string'
    )
    
    
    :type job: string
    :param job: [REQUIRED]\nThe Amazon Resource Name (ARN) of the simulation job.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.ThrottlingException
    RoboMaker.Client.exceptions.LimitExceededException
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.InternalServerException
    
    """
    pass

def start_simulation_job_batch(clientRequestToken=None, batchPolicy=None, createSimulationJobRequests=None, tags=None):
    """
    Starts a new simulation job batch. The batch is defined using one or more SimulationJobRequest objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_simulation_job_batch(
        clientRequestToken='string',
        batchPolicy={
            'timeoutInSeconds': 123,
            'maxConcurrency': 123
        },
        createSimulationJobRequests=[
            {
                'outputLocation': {
                    's3Bucket': 'string',
                    's3Prefix': 'string'
                },
                'loggingConfig': {
                    'recordAllRosTopics': True|False
                },
                'maxJobDurationInSeconds': 123,
                'iamRole': 'string',
                'failureBehavior': 'Fail'|'Continue',
                'useDefaultApplications': True|False,
                'robotApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'simulationApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'dataSources': [
                    {
                        'name': 'string',
                        's3Bucket': 'string',
                        's3Keys': [
                            'string',
                        ]
                    },
                ],
                'vpcConfig': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'assignPublicIp': True|False
                },
                'compute': {
                    'simulationUnitLimit': 123
                },
                'tags': {
                    'string': 'string'
                }
            },
        ],
        tags={
            'string': 'string'
        }
    )
    
    
    :type clientRequestToken: string
    :param clientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type batchPolicy: dict
    :param batchPolicy: The batch policy.\n\ntimeoutInSeconds (integer) --The amount of time, in seconds, to wait for the batch to complete.\nIf a batch times out, and there are pending requests that were failing due to an internal failure (like InternalServiceError ), they will be moved to the failed list and the batch status will be Failed . If the pending requests were failing for any other reason, the failed pending requests will be moved to the failed list and the batch status will be TimedOut .\n\nmaxConcurrency (integer) --The number of active simulation jobs create as part of the batch that can be in an active state at the same time.\nActive states include: Pending ,``Preparing`` , Running , Restarting , RunningFailed and Terminating . All other states are terminal states.\n\n\n

    :type createSimulationJobRequests: list
    :param createSimulationJobRequests: [REQUIRED]\nA list of simulation job requests to create in the batch.\n\n(dict) --Information about a simulation job request.\n\noutputLocation (dict) --The output location.\n\ns3Bucket (string) --The S3 bucket for output.\n\ns3Prefix (string) --The S3 folder in the s3Bucket where output files will be placed.\n\n\n\nloggingConfig (dict) --The logging configuration.\n\nrecordAllRosTopics (boolean) -- [REQUIRED]A boolean indicating whether to record all ROS topics.\n\n\n\nmaxJobDurationInSeconds (integer) -- [REQUIRED]The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.\n\niamRole (string) --The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.\n\nfailureBehavior (string) --The failure behavior the simulation job.\n\nContinue\nRestart the simulation job in the same host instance.\n\nFail\nStop the simulation job and terminate the instance.\n\nuseDefaultApplications (boolean) --Boolean indicating whether to use default simulation tool applications.\n\nrobotApplications (list) --The robot applications to use in the simulation job.\n\n(dict) --Application configuration information for a robot.\n\napplication (string) -- [REQUIRED]The application information for the robot application.\n\napplicationVersion (string) --The version of the robot application.\n\nlaunchConfig (dict) -- [REQUIRED]The launch configuration for the robot application.\n\npackageName (string) -- [REQUIRED]The package name.\n\nlaunchFile (string) -- [REQUIRED]The launch file name.\n\nenvironmentVariables (dict) --The environment variables for the application launch.\n\n(string) --\n(string) --\n\n\n\n\nportForwardingConfig (dict) --The port forwarding configuration.\n\nportMappings (list) --The port mappings for the configuration.\n\n(dict) --An object representing a port mapping.\n\njobPort (integer) -- [REQUIRED]The port number on the simulation job instance to use as a remote connection point.\n\napplicationPort (integer) -- [REQUIRED]The port number on the application.\n\nenableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.\n\n\n\n\n\n\n\nstreamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.\n\n\n\n\n\n\n\nsimulationApplications (list) --The simulation applications to use in the simulation job.\n\n(dict) --Information about a simulation application configuration.\n\napplication (string) -- [REQUIRED]The application information for the simulation application.\n\napplicationVersion (string) --The version of the simulation application.\n\nlaunchConfig (dict) -- [REQUIRED]The launch configuration for the simulation application.\n\npackageName (string) -- [REQUIRED]The package name.\n\nlaunchFile (string) -- [REQUIRED]The launch file name.\n\nenvironmentVariables (dict) --The environment variables for the application launch.\n\n(string) --\n(string) --\n\n\n\n\nportForwardingConfig (dict) --The port forwarding configuration.\n\nportMappings (list) --The port mappings for the configuration.\n\n(dict) --An object representing a port mapping.\n\njobPort (integer) -- [REQUIRED]The port number on the simulation job instance to use as a remote connection point.\n\napplicationPort (integer) -- [REQUIRED]The port number on the application.\n\nenableOnPublicIp (boolean) --A Boolean indicating whether to enable this port mapping on public IP.\n\n\n\n\n\n\n\nstreamUI (boolean) --Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.\n\n\n\n\n\n\n\ndataSources (list) --Specify data sources to mount read-only files from S3 into your simulation. These files are available under /opt/robomaker/datasources/data_source_name .\n\nNote\nThere is a limit of 100 files and a combined size of 25GB for all DataSourceConfig objects.\n\n\n(dict) --Information about a data source.\n\nname (string) -- [REQUIRED]The name of the data source.\n\ns3Bucket (string) -- [REQUIRED]The S3 bucket where the data files are located.\n\ns3Keys (list) -- [REQUIRED]The list of S3 keys identifying the data source files.\n\n(string) --\n\n\n\n\n\n\nvpcConfig (dict) --If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.\n\nsubnets (list) -- [REQUIRED]A list of one or more subnet IDs in your VPC.\n\n(string) --\n\n\nsecurityGroups (list) --A list of one or more security groups IDs in your VPC.\n\n(string) --\n\n\nassignPublicIp (boolean) --A boolean indicating whether to assign a public IP address.\n\n\n\ncompute (dict) --Compute information for the simulation job\n\nsimulationUnitLimit (integer) --The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided.\n\n\n\ntags (dict) --A map that contains tag keys and tag values that are attached to the simulation job request.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :type tags: dict
    :param tags: A map that contains tag keys and tag values that are attached to the deployment job batch.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'status': 'Pending'|'InProgress'|'Failed'|'Completed'|'Canceled'|'Canceling'|'Completing'|'TimingOut'|'TimedOut',
    'createdAt': datetime(2015, 1, 1),
    'clientRequestToken': 'string',
    'batchPolicy': {
        'timeoutInSeconds': 123,
        'maxConcurrency': 123
    },
    'failureCode': 'InternalServiceError',
    'failureReason': 'string',
    'failedRequests': [
        {
            'request': {
                'outputLocation': {
                    's3Bucket': 'string',
                    's3Prefix': 'string'
                },
                'loggingConfig': {
                    'recordAllRosTopics': True|False
                },
                'maxJobDurationInSeconds': 123,
                'iamRole': 'string',
                'failureBehavior': 'Fail'|'Continue',
                'useDefaultApplications': True|False,
                'robotApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'simulationApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'dataSources': [
                    {
                        'name': 'string',
                        's3Bucket': 'string',
                        's3Keys': [
                            'string',
                        ]
                    },
                ],
                'vpcConfig': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'assignPublicIp': True|False
                },
                'compute': {
                    'simulationUnitLimit': 123
                },
                'tags': {
                    'string': 'string'
                }
            },
            'failureReason': 'string',
            'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
            'failedAt': datetime(2015, 1, 1)
        },
    ],
    'pendingRequests': [
        {
            'outputLocation': {
                's3Bucket': 'string',
                's3Prefix': 'string'
            },
            'loggingConfig': {
                'recordAllRosTopics': True|False
            },
            'maxJobDurationInSeconds': 123,
            'iamRole': 'string',
            'failureBehavior': 'Fail'|'Continue',
            'useDefaultApplications': True|False,
            'robotApplications': [
                {
                    'application': 'string',
                    'applicationVersion': 'string',
                    'launchConfig': {
                        'packageName': 'string',
                        'launchFile': 'string',
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'portForwardingConfig': {
                            'portMappings': [
                                {
                                    'jobPort': 123,
                                    'applicationPort': 123,
                                    'enableOnPublicIp': True|False
                                },
                            ]
                        },
                        'streamUI': True|False
                    }
                },
            ],
            'simulationApplications': [
                {
                    'application': 'string',
                    'applicationVersion': 'string',
                    'launchConfig': {
                        'packageName': 'string',
                        'launchFile': 'string',
                        'environmentVariables': {
                            'string': 'string'
                        },
                        'portForwardingConfig': {
                            'portMappings': [
                                {
                                    'jobPort': 123,
                                    'applicationPort': 123,
                                    'enableOnPublicIp': True|False
                                },
                            ]
                        },
                        'streamUI': True|False
                    }
                },
            ],
            'dataSources': [
                {
                    'name': 'string',
                    's3Bucket': 'string',
                    's3Keys': [
                        'string',
                    ]
                },
            ],
            'vpcConfig': {
                'subnets': [
                    'string',
                ],
                'securityGroups': [
                    'string',
                ],
                'assignPublicIp': True|False
            },
            'compute': {
                'simulationUnitLimit': 123
            },
            'tags': {
                'string': 'string'
            }
        },
    ],
    'createdRequests': [
        {
            'arn': 'string',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'name': 'string',
            'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
            'simulationApplicationNames': [
                'string',
            ],
            'robotApplicationNames': [
                'string',
            ],
            'dataSourceNames': [
                'string',
            ]
        },
    ],
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (arn) of the batch.

status (string) --
The status of the simulation job batch.

Pending

The simulation job batch request is pending.

InProgress

The simulation job batch is in progress.

Failed

The simulation job batch failed. One or more simulation job requests could not be completed due to an internal failure (like InternalServiceError ). See failureCode and failureReason for more information.

Completed

The simulation batch job completed. A batch is complete when (1) there are no pending simulation job requests in the batch and none of the failed simulation job requests are due to InternalServiceError and (2) when all created simulation jobs have reached a terminal state (for example, Completed or Failed ).

Canceled

The simulation batch job was cancelled.

Canceling

The simulation batch job is being cancelled.

Completing

The simulation batch job is completing.

TimingOut

The simulation job batch is timing out.
If a batch timing out, and there are pending requests that were failing due to an internal failure (like InternalServiceError ), the batch status will be Failed . If there are no such failing request, the batch status will be TimedOut .

TimedOut

The simulation batch job timed out.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the simulation job batch was created.

clientRequestToken (string) --
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

batchPolicy (dict) --
The batch policy.

timeoutInSeconds (integer) --
The amount of time, in seconds, to wait for the batch to complete.
If a batch times out, and there are pending requests that were failing due to an internal failure (like InternalServiceError ), they will be moved to the failed list and the batch status will be Failed . If the pending requests were failing for any other reason, the failed pending requests will be moved to the failed list and the batch status will be TimedOut .

maxConcurrency (integer) --
The number of active simulation jobs create as part of the batch that can be in an active state at the same time.
Active states include: Pending ,``Preparing`` , Running , Restarting , RunningFailed and Terminating . All other states are terminal states.



failureCode (string) --
The failure code if the simulation job batch failed.

failureReason (string) --
The reason the simulation job batch failed.

failedRequests (list) --
A list of failed simulation job requests. The request failed to be created into a simulation job. Failed requests do not have a simulation job ID.

(dict) --
Information about a failed create simulation job request.

request (dict) --
The simulation job request.

outputLocation (dict) --
The output location.

s3Bucket (string) --
The S3 bucket for output.

s3Prefix (string) --
The S3 folder in the s3Bucket where output files will be placed.



loggingConfig (dict) --
The logging configuration.

recordAllRosTopics (boolean) --
A boolean indicating whether to record all ROS topics.



maxJobDurationInSeconds (integer) --
The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.

iamRole (string) --
The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

failureBehavior (string) --
The failure behavior the simulation job.

Continue

Restart the simulation job in the same host instance.

Fail

Stop the simulation job and terminate the instance.

useDefaultApplications (boolean) --
Boolean indicating whether to use default simulation tool applications.

robotApplications (list) --
The robot applications to use in the simulation job.

(dict) --
Application configuration information for a robot.

application (string) --
The application information for the robot application.

applicationVersion (string) --
The version of the robot application.

launchConfig (dict) --
The launch configuration for the robot application.

packageName (string) --
The package name.

launchFile (string) --
The launch file name.

environmentVariables (dict) --
The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --
The port forwarding configuration.

portMappings (list) --
The port mappings for the configuration.

(dict) --
An object representing a port mapping.

jobPort (integer) --
The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --
The port number on the application.

enableOnPublicIp (boolean) --
A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --
Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







simulationApplications (list) --
The simulation applications to use in the simulation job.

(dict) --
Information about a simulation application configuration.

application (string) --
The application information for the simulation application.

applicationVersion (string) --
The version of the simulation application.

launchConfig (dict) --
The launch configuration for the simulation application.

packageName (string) --
The package name.

launchFile (string) --
The launch file name.

environmentVariables (dict) --
The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --
The port forwarding configuration.

portMappings (list) --
The port mappings for the configuration.

(dict) --
An object representing a port mapping.

jobPort (integer) --
The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --
The port number on the application.

enableOnPublicIp (boolean) --
A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --
Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







dataSources (list) --
Specify data sources to mount read-only files from S3 into your simulation. These files are available under /opt/robomaker/datasources/data_source_name .

Note
There is a limit of 100 files and a combined size of 25GB for all DataSourceConfig objects.


(dict) --
Information about a data source.

name (string) --
The name of the data source.

s3Bucket (string) --
The S3 bucket where the data files are located.

s3Keys (list) --
The list of S3 keys identifying the data source files.

(string) --






vpcConfig (dict) --
If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.

subnets (list) --
A list of one or more subnet IDs in your VPC.

(string) --


securityGroups (list) --
A list of one or more security groups IDs in your VPC.

(string) --


assignPublicIp (boolean) --
A boolean indicating whether to assign a public IP address.



compute (dict) --
Compute information for the simulation job

simulationUnitLimit (integer) --
The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided.



tags (dict) --
A map that contains tag keys and tag values that are attached to the simulation job request.

(string) --
(string) --






failureReason (string) --
The failure reason of the simulation job request.

failureCode (string) --
The failure code.

failedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation job batch failed.





pendingRequests (list) --
A list of pending simulation job requests. These requests have not yet been created into simulation jobs.

(dict) --
Information about a simulation job request.

outputLocation (dict) --
The output location.

s3Bucket (string) --
The S3 bucket for output.

s3Prefix (string) --
The S3 folder in the s3Bucket where output files will be placed.



loggingConfig (dict) --
The logging configuration.

recordAllRosTopics (boolean) --
A boolean indicating whether to record all ROS topics.



maxJobDurationInSeconds (integer) --
The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.

iamRole (string) --
The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

failureBehavior (string) --
The failure behavior the simulation job.

Continue

Restart the simulation job in the same host instance.

Fail

Stop the simulation job and terminate the instance.

useDefaultApplications (boolean) --
Boolean indicating whether to use default simulation tool applications.

robotApplications (list) --
The robot applications to use in the simulation job.

(dict) --
Application configuration information for a robot.

application (string) --
The application information for the robot application.

applicationVersion (string) --
The version of the robot application.

launchConfig (dict) --
The launch configuration for the robot application.

packageName (string) --
The package name.

launchFile (string) --
The launch file name.

environmentVariables (dict) --
The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --
The port forwarding configuration.

portMappings (list) --
The port mappings for the configuration.

(dict) --
An object representing a port mapping.

jobPort (integer) --
The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --
The port number on the application.

enableOnPublicIp (boolean) --
A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --
Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







simulationApplications (list) --
The simulation applications to use in the simulation job.

(dict) --
Information about a simulation application configuration.

application (string) --
The application information for the simulation application.

applicationVersion (string) --
The version of the simulation application.

launchConfig (dict) --
The launch configuration for the simulation application.

packageName (string) --
The package name.

launchFile (string) --
The launch file name.

environmentVariables (dict) --
The environment variables for the application launch.

(string) --
(string) --




portForwardingConfig (dict) --
The port forwarding configuration.

portMappings (list) --
The port mappings for the configuration.

(dict) --
An object representing a port mapping.

jobPort (integer) --
The port number on the simulation job instance to use as a remote connection point.

applicationPort (integer) --
The port number on the application.

enableOnPublicIp (boolean) --
A Boolean indicating whether to enable this port mapping on public IP.







streamUI (boolean) --
Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.







dataSources (list) --
Specify data sources to mount read-only files from S3 into your simulation. These files are available under /opt/robomaker/datasources/data_source_name .

Note
There is a limit of 100 files and a combined size of 25GB for all DataSourceConfig objects.


(dict) --
Information about a data source.

name (string) --
The name of the data source.

s3Bucket (string) --
The S3 bucket where the data files are located.

s3Keys (list) --
The list of S3 keys identifying the data source files.

(string) --






vpcConfig (dict) --
If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.

subnets (list) --
A list of one or more subnet IDs in your VPC.

(string) --


securityGroups (list) --
A list of one or more security groups IDs in your VPC.

(string) --


assignPublicIp (boolean) --
A boolean indicating whether to assign a public IP address.



compute (dict) --
Compute information for the simulation job

simulationUnitLimit (integer) --
The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided.



tags (dict) --
A map that contains tag keys and tag values that are attached to the simulation job request.

(string) --
(string) --








createdRequests (list) --
A list of created simulation job request summaries.

(dict) --
Summary information for a simulation job.

arn (string) --
The Amazon Resource Name (ARN) of the simulation job.

lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation job was last updated.

name (string) --
The name of the simulation job.

status (string) --
The status of the simulation job.

simulationApplicationNames (list) --
A list of simulation job simulation application names.

(string) --


robotApplicationNames (list) --
A list of simulation job robot application names.

(string) --


dataSourceNames (list) --
The names of the data sources.

(string) --






tags (dict) --
A map that contains tag keys and tag values that are attached to the deployment job batch.

(string) --
(string) --










Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.IdempotentParameterMismatchException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'arn': 'string',
        'status': 'Pending'|'InProgress'|'Failed'|'Completed'|'Canceled'|'Canceling'|'Completing'|'TimingOut'|'TimedOut',
        'createdAt': datetime(2015, 1, 1),
        'clientRequestToken': 'string',
        'batchPolicy': {
            'timeoutInSeconds': 123,
            'maxConcurrency': 123
        },
        'failureCode': 'InternalServiceError',
        'failureReason': 'string',
        'failedRequests': [
            {
                'request': {
                    'outputLocation': {
                        's3Bucket': 'string',
                        's3Prefix': 'string'
                    },
                    'loggingConfig': {
                        'recordAllRosTopics': True|False
                    },
                    'maxJobDurationInSeconds': 123,
                    'iamRole': 'string',
                    'failureBehavior': 'Fail'|'Continue',
                    'useDefaultApplications': True|False,
                    'robotApplications': [
                        {
                            'application': 'string',
                            'applicationVersion': 'string',
                            'launchConfig': {
                                'packageName': 'string',
                                'launchFile': 'string',
                                'environmentVariables': {
                                    'string': 'string'
                                },
                                'portForwardingConfig': {
                                    'portMappings': [
                                        {
                                            'jobPort': 123,
                                            'applicationPort': 123,
                                            'enableOnPublicIp': True|False
                                        },
                                    ]
                                },
                                'streamUI': True|False
                            }
                        },
                    ],
                    'simulationApplications': [
                        {
                            'application': 'string',
                            'applicationVersion': 'string',
                            'launchConfig': {
                                'packageName': 'string',
                                'launchFile': 'string',
                                'environmentVariables': {
                                    'string': 'string'
                                },
                                'portForwardingConfig': {
                                    'portMappings': [
                                        {
                                            'jobPort': 123,
                                            'applicationPort': 123,
                                            'enableOnPublicIp': True|False
                                        },
                                    ]
                                },
                                'streamUI': True|False
                            }
                        },
                    ],
                    'dataSources': [
                        {
                            'name': 'string',
                            's3Bucket': 'string',
                            's3Keys': [
                                'string',
                            ]
                        },
                    ],
                    'vpcConfig': {
                        'subnets': [
                            'string',
                        ],
                        'securityGroups': [
                            'string',
                        ],
                        'assignPublicIp': True|False
                    },
                    'compute': {
                        'simulationUnitLimit': 123
                    },
                    'tags': {
                        'string': 'string'
                    }
                },
                'failureReason': 'string',
                'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Object'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'InvalidS3Resource'|'LimitExceeded'|'MismatchedEtag'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'ResourceNotFound'|'RequestThrottled'|'BatchTimedOut'|'BatchCanceled'|'InvalidInput'|'WrongRegionS3Bucket'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
                'failedAt': datetime(2015, 1, 1)
            },
        ],
        'pendingRequests': [
            {
                'outputLocation': {
                    's3Bucket': 'string',
                    's3Prefix': 'string'
                },
                'loggingConfig': {
                    'recordAllRosTopics': True|False
                },
                'maxJobDurationInSeconds': 123,
                'iamRole': 'string',
                'failureBehavior': 'Fail'|'Continue',
                'useDefaultApplications': True|False,
                'robotApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'simulationApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            },
                            'portForwardingConfig': {
                                'portMappings': [
                                    {
                                        'jobPort': 123,
                                        'applicationPort': 123,
                                        'enableOnPublicIp': True|False
                                    },
                                ]
                            },
                            'streamUI': True|False
                        }
                    },
                ],
                'dataSources': [
                    {
                        'name': 'string',
                        's3Bucket': 'string',
                        's3Keys': [
                            'string',
                        ]
                    },
                ],
                'vpcConfig': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'assignPublicIp': True|False
                },
                'compute': {
                    'simulationUnitLimit': 123
                },
                'tags': {
                    'string': 'string'
                }
            },
        ],
        'createdRequests': [
            {
                'arn': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'name': 'string',
                'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                'simulationApplicationNames': [
                    'string',
                ],
                'robotApplicationNames': [
                    'string',
                ],
                'dataSourceNames': [
                    'string',
                ]
            },
        ],
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def sync_deployment_job(clientRequestToken=None, fleet=None):
    """
    Syncrhonizes robots in a fleet to the latest deployment. This is helpful if robots were added after a deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.sync_deployment_job(
        clientRequestToken='string',
        fleet='string'
    )
    
    
    :type clientRequestToken: string
    :param clientRequestToken: [REQUIRED]\nUnique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type fleet: string
    :param fleet: [REQUIRED]\nThe target fleet for the synchronization.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'fleet': 'string',
    'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
    'deploymentConfig': {
        'concurrentDeploymentPercentage': 123,
        'failureThresholdPercentage': 123,
        'robotDeploymentTimeoutInSeconds': 123,
        'downloadConditionFile': {
            'bucket': 'string',
            'key': 'string',
            'etag': 'string'
        }
    },
    'deploymentApplicationConfigs': [
        {
            'application': 'string',
            'applicationVersion': 'string',
            'launchConfig': {
                'packageName': 'string',
                'preLaunchFile': 'string',
                'launchFile': 'string',
                'postLaunchFile': 'string',
                'environmentVariables': {
                    'string': 'string'
                }
            }
        },
    ],
    'failureReason': 'string',
    'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError',
    'createdAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the synchronization request.

fleet (string) --
The Amazon Resource Name (ARN) of the fleet.

status (string) --
The status of the synchronization job.

deploymentConfig (dict) --
Information about the deployment configuration.

concurrentDeploymentPercentage (integer) --
The percentage of robots receiving the deployment at the same time.

failureThresholdPercentage (integer) --
The percentage of deployments that need to fail before stopping deployment.

robotDeploymentTimeoutInSeconds (integer) --
The amount of time, in seconds, to wait for deployment to a single robot to complete. Choose a time between 1 minute and 7 days. The default is 5 hours.

downloadConditionFile (dict) --
The download condition file.

bucket (string) --
The bucket containing the object.

key (string) --
The key of the object.

etag (string) --
The etag of the object.





deploymentApplicationConfigs (list) --
Information about the deployment application configurations.

(dict) --
Information about a deployment application configuration.

application (string) --
The Amazon Resource Name (ARN) of the robot application.

applicationVersion (string) --
The version of the application.

launchConfig (dict) --
The launch configuration.

packageName (string) --
The package name.

preLaunchFile (string) --
The deployment pre-launch file. This file will be executed prior to the launch file.

launchFile (string) --
The launch file name.

postLaunchFile (string) --
The deployment post-launch file. This file will be executed after the launch file.

environmentVariables (dict) --
An array of key/value pairs specifying environment variables for the robot application

(string) --
(string) --










failureReason (string) --
The failure reason if the job fails.

failureCode (string) --
The failure code if the job fails:

InternalServiceError

Internal service error.

RobotApplicationCrash

Robot application exited abnormally.

SimulationApplicationCrash

Simulation application exited abnormally.

BadPermissionsRobotApplication

Robot application bundle could not be downloaded.

BadPermissionsSimulationApplication

Simulation application bundle could not be downloaded.

BadPermissionsS3Output

Unable to publish outputs to customer-provided S3 bucket.

BadPermissionsCloudwatchLogs

Unable to publish logs to customer-provided CloudWatch Logs resource.

SubnetIpLimitExceeded

Subnet IP limit exceeded.

ENILimitExceeded

ENI limit exceeded.

BadPermissionsUserCredentials

Unable to use the Role provided.

InvalidBundleRobotApplication

Robot bundle cannot be extracted (invalid format, bundling error, or other issue).

InvalidBundleSimulationApplication

Simulation bundle cannot be extracted (invalid format, bundling error, or other issue).

RobotApplicationVersionMismatchedEtag

Etag for RobotApplication does not match value during version creation.

SimulationApplicationVersionMismatchedEtag

Etag for SimulationApplication does not match value during version creation.

createdAt (datetime) --
The time, in milliseconds since the epoch, when the fleet was created.







Exceptions

RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ConcurrentDeploymentException
RoboMaker.Client.exceptions.IdempotentParameterMismatchException


    :return: {
        'arn': 'string',
        'fleet': 'string',
        'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded'|'Canceled',
        'deploymentConfig': {
            'concurrentDeploymentPercentage': 123,
            'failureThresholdPercentage': 123,
            'robotDeploymentTimeoutInSeconds': 123,
            'downloadConditionFile': {
                'bucket': 'string',
                'key': 'string',
                'etag': 'string'
            }
        },
        'deploymentApplicationConfigs': [
            {
                'application': 'string',
                'applicationVersion': 'string',
                'launchConfig': {
                    'packageName': 'string',
                    'preLaunchFile': 'string',
                    'launchFile': 'string',
                    'postLaunchFile': 'string',
                    'environmentVariables': {
                        'string': 'string'
                    }
                }
            },
        ],
        'failureReason': 'string',
        'failureCode': 'ResourceNotFound'|'EnvironmentSetupError'|'EtagMismatch'|'FailureThresholdBreached'|'RobotDeploymentAborted'|'RobotDeploymentNoResponse'|'RobotAgentConnectionTimeout'|'GreengrassDeploymentFailed'|'InvalidGreengrassGroup'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'LambdaDeleted'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'DownloadConditionFailed'|'InternalServerError',
        'createdAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds or edits tags for a AWS RoboMaker resource.
    Each tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty strings.
    For information about the rules that apply to tag keys and tag values, see User-Defined Tag Restrictions in the AWS Billing and Cost Management User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS RoboMaker resource you are tagging.\n

    :type tags: dict
    :param tags: [REQUIRED]\nA map that contains tag keys and tag values that are attached to the resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes the specified tags from the specified AWS RoboMaker resource.
    To remove a tag, specify the tag key. To change the tag value of an existing tag key, use ` TagResource https://docs.aws.amazon.com/robomaker/latest/dg/API_TagResource.html`__ .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS RoboMaker resource you are removing tags.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nA map that contains tag keys and tag values that will be unattached from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

RoboMaker.Client.exceptions.InternalServerException
RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_robot_application(application=None, sources=None, robotSoftwareSuite=None, currentRevisionId=None):
    """
    Updates a robot application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_robot_application(
        application='string',
        sources=[
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        robotSoftwareSuite={
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        currentRevisionId='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]\nThe application information for the robot application.\n

    :type sources: list
    :param sources: [REQUIRED]\nThe sources of the robot application.\n\n(dict) --Information about a source configuration.\n\ns3Bucket (string) --The Amazon S3 bucket name.\n\ns3Key (string) --The s3 object key.\n\narchitecture (string) --The target processor architecture for the application.\n\n\n\n\n

    :type robotSoftwareSuite: dict
    :param robotSoftwareSuite: [REQUIRED]\nThe robot software suite (ROS distribution) used by the robot application.\n\nname (string) --The name of the robot software suite (ROS distribution).\n\nversion (string) --The version of the robot software suite (ROS distribution).\n\n\n

    :type currentRevisionId: string
    :param currentRevisionId: The revision id for the robot application.

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'version': 'string',
    'sources': [
        {
            's3Bucket': 'string',
            's3Key': 'string',
            'etag': 'string',
            'architecture': 'X86_64'|'ARM64'|'ARMHF'
        },
    ],
    'robotSoftwareSuite': {
        'name': 'ROS'|'ROS2',
        'version': 'Kinetic'|'Melodic'|'Dashing'
    },
    'lastUpdatedAt': datetime(2015, 1, 1),
    'revisionId': 'string'
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the updated robot application.

name (string) --
The name of the robot application.

version (string) --
The version of the robot application.

sources (list) --
The sources of the robot application.

(dict) --
Information about a source.

s3Bucket (string) --
The s3 bucket name.

s3Key (string) --
The s3 object key.

etag (string) --
A hash of the object specified by s3Bucket and s3Key .

architecture (string) --
The taget processor architecture for the application.





robotSoftwareSuite (dict) --
The robot software suite (ROS distribution) used by the robot application.

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).



lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the robot application was last updated.

revisionId (string) --
The revision id of the robot application.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'robotSoftwareSuite': {
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.LimitExceededException
    RoboMaker.Client.exceptions.ThrottlingException
    RoboMaker.Client.exceptions.InternalServerException
    
    """
    pass

def update_simulation_application(application=None, sources=None, simulationSoftwareSuite=None, robotSoftwareSuite=None, renderingEngine=None, currentRevisionId=None):
    """
    Updates a simulation application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_simulation_application(
        application='string',
        sources=[
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        simulationSoftwareSuite={
            'name': 'Gazebo'|'RosbagPlay',
            'version': 'string'
        },
        robotSoftwareSuite={
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        renderingEngine={
            'name': 'OGRE',
            'version': 'string'
        },
        currentRevisionId='string'
    )
    
    
    :type application: string
    :param application: [REQUIRED]\nThe application information for the simulation application.\n

    :type sources: list
    :param sources: [REQUIRED]\nThe sources of the simulation application.\n\n(dict) --Information about a source configuration.\n\ns3Bucket (string) --The Amazon S3 bucket name.\n\ns3Key (string) --The s3 object key.\n\narchitecture (string) --The target processor architecture for the application.\n\n\n\n\n

    :type simulationSoftwareSuite: dict
    :param simulationSoftwareSuite: [REQUIRED]\nThe simulation software suite used by the simulation application.\n\nname (string) --The name of the simulation software suite.\n\nversion (string) --The version of the simulation software suite.\n\n\n

    :type robotSoftwareSuite: dict
    :param robotSoftwareSuite: [REQUIRED]\nInformation about the robot software suite (ROS distribution).\n\nname (string) --The name of the robot software suite (ROS distribution).\n\nversion (string) --The version of the robot software suite (ROS distribution).\n\n\n

    :type renderingEngine: dict
    :param renderingEngine: The rendering engine for the simulation application.\n\nname (string) --The name of the rendering engine.\n\nversion (string) --The version of the rendering engine.\n\n\n

    :type currentRevisionId: string
    :param currentRevisionId: The revision id for the robot application.

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'name': 'string',
    'version': 'string',
    'sources': [
        {
            's3Bucket': 'string',
            's3Key': 'string',
            'etag': 'string',
            'architecture': 'X86_64'|'ARM64'|'ARMHF'
        },
    ],
    'simulationSoftwareSuite': {
        'name': 'Gazebo'|'RosbagPlay',
        'version': 'string'
    },
    'robotSoftwareSuite': {
        'name': 'ROS'|'ROS2',
        'version': 'Kinetic'|'Melodic'|'Dashing'
    },
    'renderingEngine': {
        'name': 'OGRE',
        'version': 'string'
    },
    'lastUpdatedAt': datetime(2015, 1, 1),
    'revisionId': 'string'
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the updated simulation application.

name (string) --
The name of the simulation application.

version (string) --
The version of the robot application.

sources (list) --
The sources of the simulation application.

(dict) --
Information about a source.

s3Bucket (string) --
The s3 bucket name.

s3Key (string) --
The s3 object key.

etag (string) --
A hash of the object specified by s3Bucket and s3Key .

architecture (string) --
The taget processor architecture for the application.





simulationSoftwareSuite (dict) --
The simulation software suite used by the simulation application.

name (string) --
The name of the simulation software suite.

version (string) --
The version of the simulation software suite.



robotSoftwareSuite (dict) --
Information about the robot software suite (ROS distribution).

name (string) --
The name of the robot software suite (ROS distribution).

version (string) --
The version of the robot software suite (ROS distribution).



renderingEngine (dict) --
The rendering engine for the simulation application.

name (string) --
The name of the rendering engine.

version (string) --
The version of the rendering engine.



lastUpdatedAt (datetime) --
The time, in milliseconds since the epoch, when the simulation application was last updated.

revisionId (string) --
The revision id of the simulation application.







Exceptions

RoboMaker.Client.exceptions.InvalidParameterException
RoboMaker.Client.exceptions.ResourceNotFoundException
RoboMaker.Client.exceptions.LimitExceededException
RoboMaker.Client.exceptions.ThrottlingException
RoboMaker.Client.exceptions.InternalServerException


    :return: {
        'arn': 'string',
        'name': 'string',
        'version': 'string',
        'sources': [
            {
                's3Bucket': 'string',
                's3Key': 'string',
                'etag': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF'
            },
        ],
        'simulationSoftwareSuite': {
            'name': 'Gazebo'|'RosbagPlay',
            'version': 'string'
        },
        'robotSoftwareSuite': {
            'name': 'ROS'|'ROS2',
            'version': 'Kinetic'|'Melodic'|'Dashing'
        },
        'renderingEngine': {
            'name': 'OGRE',
            'version': 'string'
        },
        'lastUpdatedAt': datetime(2015, 1, 1),
        'revisionId': 'string'
    }
    
    
    :returns: 
    RoboMaker.Client.exceptions.InvalidParameterException
    RoboMaker.Client.exceptions.ResourceNotFoundException
    RoboMaker.Client.exceptions.LimitExceededException
    RoboMaker.Client.exceptions.ThrottlingException
    RoboMaker.Client.exceptions.InternalServerException
    
    """
    pass

