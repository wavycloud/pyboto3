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

def add_tags_to_on_premises_instances(tags=None, instanceNames=None):
    """
    Adds tags to on-premises instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_tags_to_on_premises_instances(
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        instanceNames=[
            'string',
        ]
    )
    
    
    :type tags: list
    :param tags: [REQUIRED]\nThe tag key-value pairs to add to the on-premises instances.\nKeys and values are both required. Keys cannot be null or empty strings. Value-only tags are not allowed.\n\n(dict) --Information about a tag.\n\nKey (string) --The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :type instanceNames: list
    :param instanceNames: [REQUIRED]\nThe names of the on-premises instances to which to add tags.\n\n(string) --\n\n

    :returns: 
    CodeDeploy.Client.exceptions.InstanceNameRequiredException
    CodeDeploy.Client.exceptions.InvalidInstanceNameException
    CodeDeploy.Client.exceptions.TagRequiredException
    CodeDeploy.Client.exceptions.InvalidTagException
    CodeDeploy.Client.exceptions.TagLimitExceededException
    CodeDeploy.Client.exceptions.InstanceLimitExceededException
    CodeDeploy.Client.exceptions.InstanceNotRegisteredException
    
    """
    pass

def batch_get_application_revisions(applicationName=None, revisions=None):
    """
    Gets information about one or more application revisions. The maximum number of application revisions that can be returned is 25.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_application_revisions(
        applicationName='string',
        revisions=[
            {
                'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                },
                'appSpecContent': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
        ]
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application about which to get revision information.\n

    :type revisions: list
    :param revisions: [REQUIRED]\nAn array of RevisionLocation objects that specify information to get about the application revisions, including type and location. The maximum number of RevisionLocation objects you can specify is 25.\n\n(dict) --Information about the location of an application revision.\n\nrevisionType (string) --The type of application revision:\n\nS3: An application revision stored in Amazon S3.\nGitHub: An application revision stored in GitHub (EC2/On-premises deployments only).\nString: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).\nAppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.\n\n\ns3Location (dict) --Information about the location of a revision stored in Amazon S3.\n\nbucket (string) --The name of the Amazon S3 bucket where the application revision is stored.\n\nkey (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.\n\nbundleType (string) --The file type of the application revision. Must be one of the following:\n\ntar : A tar archive file.\ntgz : A compressed tar archive file.\nzip : A zip archive file.\n\n\nversion (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.\nIf the version is not specified, the system uses the most recent version by default.\n\neTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.\nIf the ETag is not specified as an input parameter, ETag validation of the object is skipped.\n\n\n\ngitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.\n\nrepository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.\nSpecified as account/repository.\n\ncommitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.\n\n\n\nstring (dict) --Information about the location of an AWS Lambda deployment revision stored as a RawString.\n\ncontent (string) --The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.\n\nsha256 (string) --The SHA256 hash value of the revision content.\n\n\n\nappSpecContent (dict) --The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.\n\ncontent (string) --The YAML-formatted or JSON-formatted revision string.\nFor an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.\nFor an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.\nFor both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.\n\nsha256 (string) --The SHA256 hash value of the revision content.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'applicationName': 'string',
    'errorMessage': 'string',
    'revisions': [
        {
            'revisionLocation': {
                'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                },
                'appSpecContent': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
            'genericRevisionInfo': {
                'description': 'string',
                'deploymentGroups': [
                    'string',
                ],
                'firstUsedTime': datetime(2015, 1, 1),
                'lastUsedTime': datetime(2015, 1, 1),
                'registerTime': datetime(2015, 1, 1)
            }
        },
    ]
}


Response Structure

(dict) --
Represents the output of a BatchGetApplicationRevisions operation.

applicationName (string) --
The name of the application that corresponds to the revisions.

errorMessage (string) --
Information about errors that might have occurred during the API call.

revisions (list) --
Additional information about the revisions, including the type and location.

(dict) --
Information about an application revision.

revisionLocation (dict) --
Information about the location and type of an application revision.

revisionType (string) --
The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location (dict) --
Information about the location of a revision stored in Amazon S3.

bucket (string) --
The name of the Amazon S3 bucket where the application revision is stored.

key (string) --
The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType (string) --
The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version (string) --
A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag (string) --
The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.



gitHubLocation (dict) --
Information about the location of application artifacts stored in GitHub.

repository (string) --
The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId (string) --
The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.



string (dict) --
Information about the location of an AWS Lambda deployment revision stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 (string) --
The SHA256 hash value of the revision content.



appSpecContent (dict) --
The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 (string) --
The SHA256 hash value of the revision content.





genericRevisionInfo (dict) --
Information about an application revision, including usage details and associated deployment groups.

description (string) --
A comment about the revision.

deploymentGroups (list) --
The deployment groups for which this is the current target revision.

(string) --


firstUsedTime (datetime) --
When the revision was first used by AWS CodeDeploy.

lastUsedTime (datetime) --
When the revision was last used by AWS CodeDeploy.

registerTime (datetime) --
When the revision was registered with AWS CodeDeploy.













Exceptions

CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.RevisionRequiredException
CodeDeploy.Client.exceptions.InvalidRevisionException
CodeDeploy.Client.exceptions.BatchLimitExceededException


    :return: {
        'applicationName': 'string',
        'errorMessage': 'string',
        'revisions': [
            {
                'revisionLocation': {
                    'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    },
                    'appSpecContent': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
                'genericRevisionInfo': {
                    'description': 'string',
                    'deploymentGroups': [
                        'string',
                    ],
                    'firstUsedTime': datetime(2015, 1, 1),
                    'lastUsedTime': datetime(2015, 1, 1),
                    'registerTime': datetime(2015, 1, 1)
                }
            },
        ]
    }
    
    
    :returns: 
    S3: An application revision stored in Amazon S3.
    GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
    String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.
    
    """
    pass

def batch_get_applications(applicationNames=None):
    """
    Gets information about one or more applications. The maximum number of applications that can be returned is 100.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_applications(
        applicationNames=[
            'string',
        ]
    )
    
    
    :type applicationNames: list
    :param applicationNames: [REQUIRED]\nA list of application names separated by spaces. The maximum number of application names you can specify is 100.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'applicationsInfo': [
        {
            'applicationId': 'string',
            'applicationName': 'string',
            'createTime': datetime(2015, 1, 1),
            'linkedToGitHub': True|False,
            'gitHubAccountName': 'string',
            'computePlatform': 'Server'|'Lambda'|'ECS'
        },
    ]
}


Response Structure

(dict) --Represents the output of a BatchGetApplications operation.

applicationsInfo (list) --Information about the applications.

(dict) --Information about an application.

applicationId (string) --The application ID.

applicationName (string) --The application name.

createTime (datetime) --The time at which the application was created.

linkedToGitHub (boolean) --True if the user has authenticated with GitHub for the specified application. Otherwise, false.

gitHubAccountName (string) --The name for a connection to a GitHub account.

computePlatform (string) --The destination platform type for deployment of the application (Lambda or Server ).










Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.BatchLimitExceededException


    :return: {
        'applicationsInfo': [
            {
                'applicationId': 'string',
                'applicationName': 'string',
                'createTime': datetime(2015, 1, 1),
                'linkedToGitHub': True|False,
                'gitHubAccountName': 'string',
                'computePlatform': 'Server'|'Lambda'|'ECS'
            },
        ]
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.ApplicationNameRequiredException
    CodeDeploy.Client.exceptions.InvalidApplicationNameException
    CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
    CodeDeploy.Client.exceptions.BatchLimitExceededException
    
    """
    pass

def batch_get_deployment_groups(applicationName=None, deploymentGroupNames=None):
    """
    Gets information about one or more deployment groups.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_deployment_groups(
        applicationName='string',
        deploymentGroupNames=[
            'string',
        ]
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.\n

    :type deploymentGroupNames: list
    :param deploymentGroupNames: [REQUIRED]\nThe names of the deployment groups.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'deploymentGroupsInfo': [
        {
            'applicationName': 'string',
            'deploymentGroupId': 'string',
            'deploymentGroupName': 'string',
            'deploymentConfigName': 'string',
            'ec2TagFilters': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                },
            ],
            'onPremisesInstanceTagFilters': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                },
            ],
            'autoScalingGroups': [
                {
                    'name': 'string',
                    'hook': 'string'
                },
            ],
            'serviceRoleArn': 'string',
            'targetRevision': {
                'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                },
                'appSpecContent': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
            'triggerConfigurations': [
                {
                    'triggerName': 'string',
                    'triggerTargetArn': 'string',
                    'triggerEvents': [
                        'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                    ]
                },
            ],
            'alarmConfiguration': {
                'enabled': True|False,
                'ignorePollAlarmFailure': True|False,
                'alarms': [
                    {
                        'name': 'string'
                    },
                ]
            },
            'autoRollbackConfiguration': {
                'enabled': True|False,
                'events': [
                    'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                ]
            },
            'deploymentStyle': {
                'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
            },
            'blueGreenDeploymentConfiguration': {
                'terminateBlueInstancesOnDeploymentSuccess': {
                    'action': 'TERMINATE'|'KEEP_ALIVE',
                    'terminationWaitTimeInMinutes': 123
                },
                'deploymentReadyOption': {
                    'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                    'waitTimeInMinutes': 123
                },
                'greenFleetProvisioningOption': {
                    'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                }
            },
            'loadBalancerInfo': {
                'elbInfoList': [
                    {
                        'name': 'string'
                    },
                ],
                'targetGroupInfoList': [
                    {
                        'name': 'string'
                    },
                ],
                'targetGroupPairInfoList': [
                    {
                        'targetGroups': [
                            {
                                'name': 'string'
                            },
                        ],
                        'prodTrafficRoute': {
                            'listenerArns': [
                                'string',
                            ]
                        },
                        'testTrafficRoute': {
                            'listenerArns': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'lastSuccessfulDeployment': {
                'deploymentId': 'string',
                'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                'endTime': datetime(2015, 1, 1),
                'createTime': datetime(2015, 1, 1)
            },
            'lastAttemptedDeployment': {
                'deploymentId': 'string',
                'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                'endTime': datetime(2015, 1, 1),
                'createTime': datetime(2015, 1, 1)
            },
            'ec2TagSet': {
                'ec2TagSetList': [
                    [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                ]
            },
            'onPremisesTagSet': {
                'onPremisesTagSetList': [
                    [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                ]
            },
            'computePlatform': 'Server'|'Lambda'|'ECS',
            'ecsServices': [
                {
                    'serviceName': 'string',
                    'clusterName': 'string'
                },
            ]
        },
    ],
    'errorMessage': 'string'
}


Response Structure

(dict) --
Represents the output of a BatchGetDeploymentGroups operation.

deploymentGroupsInfo (list) --
Information about the deployment groups.

(dict) --
Information about a deployment group.

applicationName (string) --
The application name.

deploymentGroupId (string) --
The deployment group ID.

deploymentGroupName (string) --
The deployment group name.

deploymentConfigName (string) --
The deployment configuration name.

ec2TagFilters (list) --
The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with any of the specified tags.

(dict) --
Information about an EC2 tag filter.

Key (string) --
The tag filter key.

Value (string) --
The tag filter value.

Type (string) --
The tag filter type:

KEY_ONLY : Key only.
VALUE_ONLY : Value only.
KEY_AND_VALUE : Key and value.






onPremisesInstanceTagFilters (list) --
The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags.

(dict) --
Information about an on-premises instance tag filter.

Key (string) --
The on-premises instance tag filter key.

Value (string) --
The on-premises instance tag filter value.

Type (string) --
The on-premises instance tag filter type:

KEY_ONLY: Key only.
VALUE_ONLY: Value only.
KEY_AND_VALUE: Key and value.






autoScalingGroups (list) --
A list of associated Auto Scaling groups.

(dict) --
Information about an Auto Scaling group.

name (string) --
The Auto Scaling group name.

hook (string) --
An Auto Scaling lifecycle event hook name.





serviceRoleArn (string) --
A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls to AWS services on your behalf. For more information, see Create a Service Role for AWS CodeDeploy in the AWS CodeDeploy User Guide .

targetRevision (dict) --
Information about the deployment group\'s target revision, including type and location.

revisionType (string) --
The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location (dict) --
Information about the location of a revision stored in Amazon S3.

bucket (string) --
The name of the Amazon S3 bucket where the application revision is stored.

key (string) --
The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType (string) --
The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version (string) --
A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag (string) --
The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.



gitHubLocation (dict) --
Information about the location of application artifacts stored in GitHub.

repository (string) --
The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId (string) --
The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.



string (dict) --
Information about the location of an AWS Lambda deployment revision stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 (string) --
The SHA256 hash value of the revision content.



appSpecContent (dict) --
The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 (string) --
The SHA256 hash value of the revision content.





triggerConfigurations (list) --
Information about triggers associated with the deployment group.

(dict) --
Information about notification triggers for the deployment group.

triggerName (string) --
The name of the notification trigger.

triggerTargetArn (string) --
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.

triggerEvents (list) --
The event type or types for which notifications are triggered.

(string) --






alarmConfiguration (dict) --
A list of alarms associated with the deployment group.

enabled (boolean) --
Indicates whether the alarm configuration is enabled.

ignorePollAlarmFailure (boolean) --
Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

true : The deployment proceeds even if alarm status information can\'t be retrieved from Amazon CloudWatch.
false : The deployment stops if alarm status information can\'t be retrieved from Amazon CloudWatch.


alarms (list) --
A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.

(dict) --
Information about an alarm.

name (string) --
The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.







autoRollbackConfiguration (dict) --
Information about the automatic rollback configuration associated with the deployment group.

enabled (boolean) --
Indicates whether a defined automatic rollback configuration is currently enabled.

events (list) --
The event type or types that trigger a rollback.

(string) --




deploymentStyle (dict) --
Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

deploymentType (string) --
Indicates whether to run an in-place deployment or a blue/green deployment.

deploymentOption (string) --
Indicates whether to route deployment traffic behind a load balancer.



blueGreenDeploymentConfiguration (dict) --
Information about blue/green deployment options for a deployment group.

terminateBlueInstancesOnDeploymentSuccess (dict) --
Information about whether to terminate instances in the original fleet during a blue/green deployment.

action (string) --
The action to take on instances in the original environment after a successful blue/green deployment.

TERMINATE : Instances are terminated after a specified wait time.
KEEP_ALIVE : Instances are left running after they are deregistered from the load balancer and removed from the deployment group.


terminationWaitTimeInMinutes (integer) --
For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set.
The maximum setting is 2880 minutes (2 days).



deploymentReadyOption (dict) --
Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

actionOnTimeout (string) --
Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using  ContinueDeployment . If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.


waitTimeInMinutes (integer) --
The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout .



greenFleetProvisioningOption (dict) --
Information about how instances are provisioned for a replacement environment in a blue/green deployment.

action (string) --
The method used to add instances to a replacement environment.

DISCOVER_EXISTING : Use instances that already exist or will be created manually.
COPY_AUTO_SCALING_GROUP : Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.






loadBalancerInfo (dict) --
Information about the load balancer to use in a deployment.

elbInfoList (list) --
An array that contains information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

Note
Adding more than one load balancer to the array is not supported.


(dict) --
Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

name (string) --
For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





targetGroupInfoList (list) --
An array that contains information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

Note
Adding more than one target group to the array is not supported.


(dict) --
Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name (string) --
For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





targetGroupPairInfoList (list) --
The target group pair information. This is an array of TargeGroupPairInfo objects with a maximum size of one.

(dict) --
Information about two target groups and how traffic is routed during an Amazon ECS deployment. An optional test traffic route can be specified.

targetGroups (list) --
One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete.

(dict) --
Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name (string) --
For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





prodTrafficRoute (dict) --
The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete.

listenerArns (list) --
The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string) --




testTrafficRoute (dict) --
An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment.

listenerArns (list) --
The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string) --










lastSuccessfulDeployment (dict) --
Information about the most recent successful deployment to the deployment group.

deploymentId (string) --
The unique ID of a deployment.

status (string) --
The status of the most recent deployment.

endTime (datetime) --
A timestamp that indicates when the most recent deployment to the deployment group was complete.

createTime (datetime) --
A timestamp that indicates when the most recent deployment to the deployment group started.



lastAttemptedDeployment (dict) --
Information about the most recent attempted deployment to the deployment group.

deploymentId (string) --
The unique ID of a deployment.

status (string) --
The status of the most recent deployment.

endTime (datetime) --
A timestamp that indicates when the most recent deployment to the deployment group was complete.

createTime (datetime) --
A timestamp that indicates when the most recent deployment to the deployment group started.



ec2TagSet (dict) --
Information about groups of tags applied to an EC2 instance. The deployment group includes only EC2 instances identified by all of the tag groups. Cannot be used in the same call as ec2TagFilters.

ec2TagSetList (list) --
A list that contains other lists of EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

(list) --

(dict) --
Information about an EC2 tag filter.

Key (string) --
The tag filter key.

Value (string) --
The tag filter value.

Type (string) --
The tag filter type:

KEY_ONLY : Key only.
VALUE_ONLY : Value only.
KEY_AND_VALUE : Key and value.










onPremisesTagSet (dict) --
Information about groups of tags applied to an on-premises instance. The deployment group includes only on-premises instances identified by all the tag groups. Cannot be used in the same call as onPremisesInstanceTagFilters.

onPremisesTagSetList (list) --
A list that contains other lists of on-premises instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

(list) --

(dict) --
Information about an on-premises instance tag filter.

Key (string) --
The on-premises instance tag filter key.

Value (string) --
The on-premises instance tag filter value.

Type (string) --
The on-premises instance tag filter type:

KEY_ONLY: Key only.
VALUE_ONLY: Value only.
KEY_AND_VALUE: Key and value.










computePlatform (string) --
The destination platform type for the deployment (Lambda , Server , or ECS ).

ecsServices (list) --
The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <clustername>:<servicename> .

(dict) --
Contains the service and cluster names used to identify an Amazon ECS deployment\'s target.

serviceName (string) --
The name of the target Amazon ECS service.

clusterName (string) --
The name of the cluster that the Amazon ECS service is associated with.









errorMessage (string) --
Information about errors that might have occurred during the API call.







Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
CodeDeploy.Client.exceptions.BatchLimitExceededException
CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException


    :return: {
        'deploymentGroupsInfo': [
            {
                'applicationName': 'string',
                'deploymentGroupId': 'string',
                'deploymentGroupName': 'string',
                'deploymentConfigName': 'string',
                'ec2TagFilters': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
                'onPremisesInstanceTagFilters': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
                'autoScalingGroups': [
                    {
                        'name': 'string',
                        'hook': 'string'
                    },
                ],
                'serviceRoleArn': 'string',
                'targetRevision': {
                    'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    },
                    'appSpecContent': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
                'triggerConfigurations': [
                    {
                        'triggerName': 'string',
                        'triggerTargetArn': 'string',
                        'triggerEvents': [
                            'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                        ]
                    },
                ],
                'alarmConfiguration': {
                    'enabled': True|False,
                    'ignorePollAlarmFailure': True|False,
                    'alarms': [
                        {
                            'name': 'string'
                        },
                    ]
                },
                'autoRollbackConfiguration': {
                    'enabled': True|False,
                    'events': [
                        'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                    ]
                },
                'deploymentStyle': {
                    'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                    'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                },
                'blueGreenDeploymentConfiguration': {
                    'terminateBlueInstancesOnDeploymentSuccess': {
                        'action': 'TERMINATE'|'KEEP_ALIVE',
                        'terminationWaitTimeInMinutes': 123
                    },
                    'deploymentReadyOption': {
                        'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                        'waitTimeInMinutes': 123
                    },
                    'greenFleetProvisioningOption': {
                        'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                    }
                },
                'loadBalancerInfo': {
                    'elbInfoList': [
                        {
                            'name': 'string'
                        },
                    ],
                    'targetGroupInfoList': [
                        {
                            'name': 'string'
                        },
                    ],
                    'targetGroupPairInfoList': [
                        {
                            'targetGroups': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'prodTrafficRoute': {
                                'listenerArns': [
                                    'string',
                                ]
                            },
                            'testTrafficRoute': {
                                'listenerArns': [
                                    'string',
                                ]
                            }
                        },
                    ]
                },
                'lastSuccessfulDeployment': {
                    'deploymentId': 'string',
                    'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                    'endTime': datetime(2015, 1, 1),
                    'createTime': datetime(2015, 1, 1)
                },
                'lastAttemptedDeployment': {
                    'deploymentId': 'string',
                    'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                    'endTime': datetime(2015, 1, 1),
                    'createTime': datetime(2015, 1, 1)
                },
                'ec2TagSet': {
                    'ec2TagSetList': [
                        [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                    ]
                },
                'onPremisesTagSet': {
                    'onPremisesTagSetList': [
                        [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                    ]
                },
                'computePlatform': 'Server'|'Lambda'|'ECS',
                'ecsServices': [
                    {
                        'serviceName': 'string',
                        'clusterName': 'string'
                    },
                ]
            },
        ],
        'errorMessage': 'string'
    }
    
    
    :returns: 
    KEY_ONLY : Key only.
    VALUE_ONLY : Value only.
    KEY_AND_VALUE : Key and value.
    
    """
    pass

def batch_get_deployment_instances(deploymentId=None, instanceIds=None):
    """
    Returns an array of one or more instances associated with a deployment. This method works with EC2/On-premises and AWS Lambda compute platforms. The newer BatchGetDeploymentTargets works with all compute platforms. The maximum number of instances that can be returned is 25.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_deployment_instances(
        deploymentId='string',
        instanceIds=[
            'string',
        ]
    )
    
    
    :type deploymentId: string
    :param deploymentId: [REQUIRED]\nThe unique ID of a deployment.\n

    :type instanceIds: list
    :param instanceIds: [REQUIRED]\nThe unique IDs of instances used in the deployment. The maximum number of instance IDs you can specify is 25.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'instancesSummary': [
        {
            'deploymentId': 'string',
            'instanceId': 'string',
            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'lifecycleEvents': [
                {
                    'lifecycleEventName': 'string',
                    'diagnostics': {
                        'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                        'scriptName': 'string',
                        'message': 'string',
                        'logTail': 'string'
                    },
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                },
            ],
            'instanceType': 'Blue'|'Green'
        },
    ],
    'errorMessage': 'string'
}


Response Structure

(dict) --
Represents the output of a BatchGetDeploymentInstances operation.

instancesSummary (list) --
Information about the instance.

(dict) --
Information about an instance in a deployment.

deploymentId (string) --
The unique ID of a deployment.

instanceId (string) --
The instance ID.

status (string) --
The deployment status for this instance:

Pending : The deployment is pending for this instance.
In Progress : The deployment is in progress for this instance.
Succeeded : The deployment has succeeded for this instance.
Failed : The deployment has failed for this instance.
Skipped : The deployment has been skipped for this instance.
Unknown : The deployment status is unknown for this instance.


lastUpdatedAt (datetime) --
A timestamp that indicates when the instance information was last updated.

lifecycleEvents (list) --
A list of lifecycle events for this instance.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






instanceType (string) --
Information about which environment an instance belongs to in a blue/green deployment.

BLUE: The instance is part of the original environment.
GREEN: The instance is part of the replacement environment.






errorMessage (string) --
Information about errors that might have occurred during the API call.







Exceptions

CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
CodeDeploy.Client.exceptions.InstanceIdRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.InvalidInstanceNameException
CodeDeploy.Client.exceptions.BatchLimitExceededException
CodeDeploy.Client.exceptions.InvalidComputePlatformException


    :return: {
        'instancesSummary': [
            {
                'deploymentId': 'string',
                'instanceId': 'string',
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'instanceType': 'Blue'|'Green'
            },
        ],
        'errorMessage': 'string'
    }
    
    
    :returns: 
    Pending : The deployment is pending for this instance.
    In Progress : The deployment is in progress for this instance.
    Succeeded : The deployment has succeeded for this instance.
    Failed : The deployment has failed for this instance.
    Skipped : The deployment has been skipped for this instance.
    Unknown : The deployment status is unknown for this instance.
    
    """
    pass

def batch_get_deployment_targets(deploymentId=None, targetIds=None):
    """
    Returns an array of one or more targets associated with a deployment. This method works with all compute types and should be used instead of the deprecated BatchGetDeploymentInstances . The maximum number of targets that can be returned is 25.
    The type of targets returned depends on the deployment\'s compute platform or deployment method:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_deployment_targets(
        deploymentId='string',
        targetIds=[
            'string',
        ]
    )
    
    
    :type deploymentId: string
    :param deploymentId: The unique ID of a deployment.

    :type targetIds: list
    :param targetIds: The unique IDs of the deployment targets. The compute platform of the deployment determines the type of the targets and their formats. The maximum number of deployment target IDs you can specify is 25.\n\nFor deployments that use the EC2/On-premises compute platform, the target IDs are EC2 or on-premises instances IDs, and their target type is instanceTarget .\nFor deployments that use the AWS Lambda compute platform, the target IDs are the names of Lambda functions, and their target type is instanceTarget .\nFor deployments that use the Amazon ECS compute platform, the target IDs are pairs of Amazon ECS clusters and services specified using the format <clustername>:<servicename> . Their target type is ecsTarget .\nFor deployments that are deployed with AWS CloudFormation, the target IDs are CloudFormation stack IDs. Their target type is cloudFormationTarget .\n\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'deploymentTargets': [
        {
            'deploymentTargetType': 'InstanceTarget'|'LambdaTarget'|'ECSTarget'|'CloudFormationTarget',
            'instanceTarget': {
                'deploymentId': 'string',
                'targetId': 'string',
                'targetArn': 'string',
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'instanceLabel': 'Blue'|'Green'
            },
            'lambdaTarget': {
                'deploymentId': 'string',
                'targetId': 'string',
                'targetArn': 'string',
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'lambdaFunctionInfo': {
                    'functionName': 'string',
                    'functionAlias': 'string',
                    'currentVersion': 'string',
                    'targetVersion': 'string',
                    'targetVersionWeight': 123.0
                }
            },
            'ecsTarget': {
                'deploymentId': 'string',
                'targetId': 'string',
                'targetArn': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'taskSetsInfo': [
                    {
                        'identifer': 'string',
                        'desiredCount': 123,
                        'pendingCount': 123,
                        'runningCount': 123,
                        'status': 'string',
                        'trafficWeight': 123.0,
                        'targetGroup': {
                            'name': 'string'
                        },
                        'taskSetLabel': 'Blue'|'Green'
                    },
                ]
            },
            'cloudFormationTarget': {
                'deploymentId': 'string',
                'targetId': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'resourceType': 'string',
                'targetVersionWeight': 123.0
            }
        },
    ]
}


Response Structure

(dict) --

deploymentTargets (list) --
A list of target objects for a deployment. Each target object contains details about the target, such as its status and lifecycle events. The type of the target objects depends on the deployment\' compute platform.

EC2/On-premises : Each target object is an EC2 or on-premises instance.
AWS Lambda : The target object is a specific version of an AWS Lambda function.
Amazon ECS : The target object is an Amazon ECS service.
CloudFormation : The target object is an AWS CloudFormation blue/green deployment.


(dict) --
Information about the deployment target.

deploymentTargetType (string) --
The deployment type that is specific to the deployment\'s compute platform or deployments initiated by a CloudFormation stack update.

instanceTarget (dict) --
Information about the target for a deployment that uses the EC2/On-premises compute platform.

deploymentId (string) --
The unique ID of a deployment.

targetId (string) --
The unique ID of a deployment target that has a type of instanceTarget .

targetArn (string) --
The Amazon Resource Name (ARN) of the target.

status (string) --
The status an EC2/On-premises deployment\'s target instance.

lastUpdatedAt (datetime) --
The date and time when the target instance was updated by a deployment.

lifecycleEvents (list) --
The lifecycle events of the deployment to this target instance.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






instanceLabel (string) --
A label that identifies whether the instance is an original target (BLUE ) or a replacement target (GREEN ).



lambdaTarget (dict) --
Information about the target for a deployment that uses the AWS Lambda compute platform.

deploymentId (string) --
The unique ID of a deployment.

targetId (string) --
The unique ID of a deployment target that has a type of lambdaTarget .

targetArn (string) --
The Amazon Resource Name (ARN) of the target.

status (string) --
The status an AWS Lambda deployment\'s target Lambda function.

lastUpdatedAt (datetime) --
The date and time when the target Lambda function was updated by a deployment.

lifecycleEvents (list) --
The lifecycle events of the deployment to this target Lambda function.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






lambdaFunctionInfo (dict) --
A LambdaFunctionInfo object that describes a target Lambda function.

functionName (string) --
The name of a Lambda function.

functionAlias (string) --
The alias of a Lambda function. For more information, see AWS Lambda Function Aliases in the AWS Lambda Developer Guide .

currentVersion (string) --
The version of a Lambda function that production traffic points to.

targetVersion (string) --
The version of a Lambda function that production traffic points to after the Lambda function is deployed.

targetVersionWeight (float) --
The percentage of production traffic that the target version of a Lambda function receives.





ecsTarget (dict) --
Information about the target for a deployment that uses the Amazon ECS compute platform.

deploymentId (string) --
The unique ID of a deployment.

targetId (string) --
The unique ID of a deployment target that has a type of ecsTarget .

targetArn (string) --
The Amazon Resource Name (ARN) of the target.

lastUpdatedAt (datetime) --
The date and time when the target Amazon ECS application was updated by a deployment.

lifecycleEvents (list) --
The lifecycle events of the deployment to this target Amazon ECS application.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






status (string) --
The status an Amazon ECS deployment\'s target ECS application.

taskSetsInfo (list) --
The ECSTaskSet objects associated with the ECS target.

(dict) --
Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic. An AWS CodeDeploy application that uses the Amazon ECS compute platform deploys a containerized application in an Amazon ECS service as a task set.

identifer (string) --
A unique ID of an ECSTaskSet .

desiredCount (integer) --
The number of tasks in a task set. During a deployment that uses the Amazon ECS compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses this value to determine how many tasks to create. After the updated task set is created, CodeDeploy shifts traffic to the new task set.

pendingCount (integer) --
The number of tasks in the task set that are in the PENDING status during an Amazon ECS deployment. A task in the PENDING state is preparing to enter the RUNNING state. A task set enters the PENDING status when it launches for the first time, or when it is restarted after being in the STOPPED state.

runningCount (integer) --
The number of tasks in the task set that are in the RUNNING status during an Amazon ECS deployment. A task in the RUNNING state is running and ready for use.

status (string) --
The status of the task set. There are three valid task set statuses:

PRIMARY : Indicates the task set is serving production traffic.
ACTIVE : Indicates the task set is not serving production traffic.
DRAINING : Indicates the tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.


trafficWeight (float) --
The percentage of traffic served by this task set.

targetGroup (dict) --
The target group associated with the task set. The target group is used by AWS CodeDeploy to manage traffic to a task set.

name (string) --
For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.



taskSetLabel (string) --
A label that identifies whether the ECS task set is an original target (BLUE ) or a replacement target (GREEN ).







cloudFormationTarget (dict) --
Information about the target to be updated by an AWS CloudFormation blue/green deployment. This target type is used for all deployments initiated by a CloudFormation stack update.

deploymentId (string) --
The unique ID of an AWS CloudFormation blue/green deployment.

targetId (string) --
The unique ID of a deployment target that has a type of CloudFormationTarget .

lastUpdatedAt (datetime) --
The date and time when the target application was updated by an AWS CloudFormation blue/green deployment.

lifecycleEvents (list) --
The lifecycle events of the AWS CloudFormation blue/green deployment to this target application.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






status (string) --
The status of an AWS CloudFormation blue/green deployment\'s target application.

resourceType (string) --
The resource type for the AWS CloudFormation blue/green deployment.

targetVersionWeight (float) --
The percentage of production traffic that the target version of an AWS CloudFormation blue/green deployment receives.













Exceptions

CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentNotStartedException
CodeDeploy.Client.exceptions.DeploymentTargetIdRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentTargetIdException
CodeDeploy.Client.exceptions.DeploymentTargetDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentTargetListSizeExceededException
CodeDeploy.Client.exceptions.InstanceDoesNotExistException


    :return: {
        'deploymentTargets': [
            {
                'deploymentTargetType': 'InstanceTarget'|'LambdaTarget'|'ECSTarget'|'CloudFormationTarget',
                'instanceTarget': {
                    'deploymentId': 'string',
                    'targetId': 'string',
                    'targetArn': 'string',
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'lifecycleEvents': [
                        {
                            'lifecycleEventName': 'string',
                            'diagnostics': {
                                'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                                'scriptName': 'string',
                                'message': 'string',
                                'logTail': 'string'
                            },
                            'startTime': datetime(2015, 1, 1),
                            'endTime': datetime(2015, 1, 1),
                            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                        },
                    ],
                    'instanceLabel': 'Blue'|'Green'
                },
                'lambdaTarget': {
                    'deploymentId': 'string',
                    'targetId': 'string',
                    'targetArn': 'string',
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'lifecycleEvents': [
                        {
                            'lifecycleEventName': 'string',
                            'diagnostics': {
                                'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                                'scriptName': 'string',
                                'message': 'string',
                                'logTail': 'string'
                            },
                            'startTime': datetime(2015, 1, 1),
                            'endTime': datetime(2015, 1, 1),
                            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                        },
                    ],
                    'lambdaFunctionInfo': {
                        'functionName': 'string',
                        'functionAlias': 'string',
                        'currentVersion': 'string',
                        'targetVersion': 'string',
                        'targetVersionWeight': 123.0
                    }
                },
                'ecsTarget': {
                    'deploymentId': 'string',
                    'targetId': 'string',
                    'targetArn': 'string',
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'lifecycleEvents': [
                        {
                            'lifecycleEventName': 'string',
                            'diagnostics': {
                                'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                                'scriptName': 'string',
                                'message': 'string',
                                'logTail': 'string'
                            },
                            'startTime': datetime(2015, 1, 1),
                            'endTime': datetime(2015, 1, 1),
                            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                        },
                    ],
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                    'taskSetsInfo': [
                        {
                            'identifer': 'string',
                            'desiredCount': 123,
                            'pendingCount': 123,
                            'runningCount': 123,
                            'status': 'string',
                            'trafficWeight': 123.0,
                            'targetGroup': {
                                'name': 'string'
                            },
                            'taskSetLabel': 'Blue'|'Green'
                        },
                    ]
                },
                'cloudFormationTarget': {
                    'deploymentId': 'string',
                    'targetId': 'string',
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'lifecycleEvents': [
                        {
                            'lifecycleEventName': 'string',
                            'diagnostics': {
                                'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                                'scriptName': 'string',
                                'message': 'string',
                                'logTail': 'string'
                            },
                            'startTime': datetime(2015, 1, 1),
                            'endTime': datetime(2015, 1, 1),
                            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                        },
                    ],
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                    'resourceType': 'string',
                    'targetVersionWeight': 123.0
                }
            },
        ]
    }
    
    
    :returns: 
    deploymentId (string) -- The unique ID of a deployment.
    targetIds (list) -- The unique IDs of the deployment targets. The compute platform of the deployment determines the type of the targets and their formats. The maximum number of deployment target IDs you can specify is 25.
    
    For deployments that use the EC2/On-premises compute platform, the target IDs are EC2 or on-premises instances IDs, and their target type is instanceTarget .
    For deployments that use the AWS Lambda compute platform, the target IDs are the names of Lambda functions, and their target type is instanceTarget .
    For deployments that use the Amazon ECS compute platform, the target IDs are pairs of Amazon ECS clusters and services specified using the format <clustername>:<servicename> . Their target type is ecsTarget .
    For deployments that are deployed with AWS CloudFormation, the target IDs are CloudFormation stack IDs. Their target type is cloudFormationTarget .
    
    
    (string) --
    
    
    
    """
    pass

def batch_get_deployments(deploymentIds=None):
    """
    Gets information about one or more deployments. The maximum number of deployments that can be returned is 25.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_deployments(
        deploymentIds=[
            'string',
        ]
    )
    
    
    :type deploymentIds: list
    :param deploymentIds: [REQUIRED]\nA list of deployment IDs, separated by spaces. The maximum number of deployment IDs you can specify is 25.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'deploymentsInfo': [
        {
            'applicationName': 'string',
            'deploymentGroupName': 'string',
            'deploymentConfigName': 'string',
            'deploymentId': 'string',
            'previousRevision': {
                'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                },
                'appSpecContent': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
            'revision': {
                'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                },
                'appSpecContent': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
            'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
            'errorInformation': {
                'code': 'AGENT_ISSUE'|'ALARM_ACTIVE'|'APPLICATION_MISSING'|'AUTOSCALING_VALIDATION_ERROR'|'AUTO_SCALING_CONFIGURATION'|'AUTO_SCALING_IAM_ROLE_PERMISSIONS'|'CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND'|'CUSTOMER_APPLICATION_UNHEALTHY'|'DEPLOYMENT_GROUP_MISSING'|'ECS_UPDATE_ERROR'|'ELASTIC_LOAD_BALANCING_INVALID'|'ELB_INVALID_INSTANCE'|'HEALTH_CONSTRAINTS'|'HEALTH_CONSTRAINTS_INVALID'|'HOOK_EXECUTION_FAILURE'|'IAM_ROLE_MISSING'|'IAM_ROLE_PERMISSIONS'|'INTERNAL_ERROR'|'INVALID_ECS_SERVICE'|'INVALID_LAMBDA_CONFIGURATION'|'INVALID_LAMBDA_FUNCTION'|'INVALID_REVISION'|'MANUAL_STOP'|'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION'|'MISSING_ELB_INFORMATION'|'MISSING_GITHUB_TOKEN'|'NO_EC2_SUBSCRIPTION'|'NO_INSTANCES'|'OVER_MAX_INSTANCES'|'RESOURCE_LIMIT_EXCEEDED'|'REVISION_MISSING'|'THROTTLED'|'TIMEOUT'|'CLOUDFORMATION_STACK_FAILURE',
                'message': 'string'
            },
            'createTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'completeTime': datetime(2015, 1, 1),
            'deploymentOverview': {
                'Pending': 123,
                'InProgress': 123,
                'Succeeded': 123,
                'Failed': 123,
                'Skipped': 123,
                'Ready': 123
            },
            'description': 'string',
            'creator': 'user'|'autoscaling'|'codeDeployRollback'|'CodeDeploy'|'CloudFormation'|'CloudFormationRollback',
            'ignoreApplicationStopFailures': True|False,
            'autoRollbackConfiguration': {
                'enabled': True|False,
                'events': [
                    'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                ]
            },
            'updateOutdatedInstancesOnly': True|False,
            'rollbackInfo': {
                'rollbackDeploymentId': 'string',
                'rollbackTriggeringDeploymentId': 'string',
                'rollbackMessage': 'string'
            },
            'deploymentStyle': {
                'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
            },
            'targetInstances': {
                'tagFilters': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
                'autoScalingGroups': [
                    'string',
                ],
                'ec2TagSet': {
                    'ec2TagSetList': [
                        [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                    ]
                }
            },
            'instanceTerminationWaitTimeStarted': True|False,
            'blueGreenDeploymentConfiguration': {
                'terminateBlueInstancesOnDeploymentSuccess': {
                    'action': 'TERMINATE'|'KEEP_ALIVE',
                    'terminationWaitTimeInMinutes': 123
                },
                'deploymentReadyOption': {
                    'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                    'waitTimeInMinutes': 123
                },
                'greenFleetProvisioningOption': {
                    'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                }
            },
            'loadBalancerInfo': {
                'elbInfoList': [
                    {
                        'name': 'string'
                    },
                ],
                'targetGroupInfoList': [
                    {
                        'name': 'string'
                    },
                ],
                'targetGroupPairInfoList': [
                    {
                        'targetGroups': [
                            {
                                'name': 'string'
                            },
                        ],
                        'prodTrafficRoute': {
                            'listenerArns': [
                                'string',
                            ]
                        },
                        'testTrafficRoute': {
                            'listenerArns': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'additionalDeploymentStatusInfo': 'string',
            'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN',
            'deploymentStatusMessages': [
                'string',
            ],
            'computePlatform': 'Server'|'Lambda'|'ECS',
            'externalId': 'string'
        },
    ]
}


Response Structure

(dict) --Represents the output of a BatchGetDeployments operation.

deploymentsInfo (list) --Information about the deployments.

(dict) --Information about a deployment.

applicationName (string) --The application name.

deploymentGroupName (string) --The deployment group name.

deploymentConfigName (string) --The deployment configuration name.

deploymentId (string) --The unique ID of a deployment.

previousRevision (dict) --Information about the application revision that was deployed to the deployment group before the most recent successful deployment.

revisionType (string) --The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location (dict) --Information about the location of a revision stored in Amazon S3.

bucket (string) --The name of the Amazon S3 bucket where the application revision is stored.

key (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType (string) --The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.



gitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.

repository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.



string (dict) --Information about the location of an AWS Lambda deployment revision stored as a RawString.

content (string) --The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 (string) --The SHA256 hash value of the revision content.



appSpecContent (dict) --The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content (string) --The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 (string) --The SHA256 hash value of the revision content.





revision (dict) --Information about the location of stored application artifacts and the service from which to retrieve them.

revisionType (string) --The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location (dict) --Information about the location of a revision stored in Amazon S3.

bucket (string) --The name of the Amazon S3 bucket where the application revision is stored.

key (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType (string) --The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.



gitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.

repository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.



string (dict) --Information about the location of an AWS Lambda deployment revision stored as a RawString.

content (string) --The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 (string) --The SHA256 hash value of the revision content.



appSpecContent (dict) --The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content (string) --The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 (string) --The SHA256 hash value of the revision content.





status (string) --The current state of the deployment as a whole.

errorInformation (dict) --Information about any error associated with this deployment.

code (string) --For more information, see Error Codes for AWS CodeDeploy in the AWS CodeDeploy User Guide .
The error code:

APPLICATION_MISSING: The application was missing. This error code is most likely raised if the application is deleted after the deployment is created, but before it is started.
DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most likely raised if the deployment group is deleted after the deployment is created, but before it is started.
HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified.
HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the instance health constraints specified.
IAM_ROLE_MISSING: The service role cannot be accessed.
IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.
INTERNAL_ERROR: There was an internal error.
NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.
NO_INSTANCES: No instances were specified, or no instances can be found.
OVER_MAX_INSTANCES: The maximum number of instances was exceeded.
THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more AWS services.
TIMEOUT: The deployment has timed out.
REVISION_MISSING: The revision ID was missing. This error code is most likely raised if the revision is deleted after the deployment is created, but before it is started.


message (string) --An accompanying error message.



createTime (datetime) --A timestamp that indicates when the deployment was created.

startTime (datetime) --A timestamp that indicates when the deployment was deployed to the deployment group.
In some cases, the reported value of the start time might be later than the complete time. This is due to differences in the clock settings of backend servers that participate in the deployment process.

completeTime (datetime) --A timestamp that indicates when the deployment was complete.

deploymentOverview (dict) --A summary of the deployment status of the instances in the deployment.

Pending (integer) --The number of instances in the deployment in a pending state.

InProgress (integer) --The number of instances in which the deployment is in progress.

Succeeded (integer) --The number of instances in the deployment to which revisions have been successfully deployed.

Failed (integer) --The number of instances in the deployment in a failed state.

Skipped (integer) --The number of instances in the deployment in a skipped state.

Ready (integer) --The number of instances in a replacement environment ready to receive traffic in a blue/green deployment.



description (string) --A comment about the deployment.

creator (string) --The means by which the deployment was created:

user : A user created the deployment.
autoscaling : Amazon EC2 Auto Scaling created the deployment.
codeDeployRollback : A rollback process created the deployment.


ignoreApplicationStopFailures (boolean) --If true, then if an ApplicationStop , BeforeBlockTraffic , or AfterBlockTraffic deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if ApplicationStop fails, the deployment continues with DownloadBundle. If BeforeBlockTraffic fails, the deployment continues with BlockTraffic . If AfterBlockTraffic fails, the deployment continues with ApplicationStop .
If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted.
During a deployment, the AWS CodeDeploy agent runs the scripts specified for ApplicationStop , BeforeBlockTraffic , and AfterBlockTraffic in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail.
If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use ignoreApplicationStopFailures to specify that the ApplicationStop , BeforeBlockTraffic , and AfterBlockTraffic failures should be ignored.

autoRollbackConfiguration (dict) --Information about the automatic rollback configuration associated with the deployment.

enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.

events (list) --The event type or types that trigger a rollback.

(string) --




updateOutdatedInstancesOnly (boolean) --Indicates whether only instances that are not running the latest application revision are to be deployed to.

rollbackInfo (dict) --Information about a deployment rollback.

rollbackDeploymentId (string) --The ID of the deployment rollback.

rollbackTriggeringDeploymentId (string) --The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.

rollbackMessage (string) --Information that describes the status of a deployment rollback (for example, whether the deployment can\'t be rolled back, is in progress, failed, or succeeded).



deploymentStyle (dict) --Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

deploymentType (string) --Indicates whether to run an in-place deployment or a blue/green deployment.

deploymentOption (string) --Indicates whether to route deployment traffic behind a load balancer.



targetInstances (dict) --Information about the instances that belong to the replacement environment in a blue/green deployment.

tagFilters (list) --The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as ec2TagSet .

(dict) --Information about an EC2 tag filter.

Key (string) --The tag filter key.

Value (string) --The tag filter value.

Type (string) --The tag filter type:

KEY_ONLY : Key only.
VALUE_ONLY : Value only.
KEY_AND_VALUE : Key and value.






autoScalingGroups (list) --The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.

(string) --


ec2TagSet (dict) --Information about the groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as tagFilters .

ec2TagSetList (list) --A list that contains other lists of EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

(list) --
(dict) --Information about an EC2 tag filter.

Key (string) --The tag filter key.

Value (string) --The tag filter value.

Type (string) --The tag filter type:

KEY_ONLY : Key only.
VALUE_ONLY : Value only.
KEY_AND_VALUE : Key and value.












instanceTerminationWaitTimeStarted (boolean) --Indicates whether the wait period set for the termination of instances in the original environment has started. Status is \'false\' if the KEEP_ALIVE option is specified. Otherwise, \'true\' as soon as the termination wait period starts.

blueGreenDeploymentConfiguration (dict) --Information about blue/green deployment options for this deployment.

terminateBlueInstancesOnDeploymentSuccess (dict) --Information about whether to terminate instances in the original fleet during a blue/green deployment.

action (string) --The action to take on instances in the original environment after a successful blue/green deployment.

TERMINATE : Instances are terminated after a specified wait time.
KEEP_ALIVE : Instances are left running after they are deregistered from the load balancer and removed from the deployment group.


terminationWaitTimeInMinutes (integer) --For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set.
The maximum setting is 2880 minutes (2 days).



deploymentReadyOption (dict) --Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

actionOnTimeout (string) --Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using  ContinueDeployment . If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.


waitTimeInMinutes (integer) --The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout .



greenFleetProvisioningOption (dict) --Information about how instances are provisioned for a replacement environment in a blue/green deployment.

action (string) --The method used to add instances to a replacement environment.

DISCOVER_EXISTING : Use instances that already exist or will be created manually.
COPY_AUTO_SCALING_GROUP : Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.






loadBalancerInfo (dict) --Information about the load balancer used in the deployment.

elbInfoList (list) --An array that contains information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

Note
Adding more than one load balancer to the array is not supported.


(dict) --Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

name (string) --For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





targetGroupInfoList (list) --An array that contains information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

Note
Adding more than one target group to the array is not supported.


(dict) --Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name (string) --For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





targetGroupPairInfoList (list) --The target group pair information. This is an array of TargeGroupPairInfo objects with a maximum size of one.

(dict) --Information about two target groups and how traffic is routed during an Amazon ECS deployment. An optional test traffic route can be specified.

targetGroups (list) --One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete.

(dict) --Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name (string) --For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





prodTrafficRoute (dict) --The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete.

listenerArns (list) --The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string) --




testTrafficRoute (dict) --An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment.

listenerArns (list) --The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string) --










additionalDeploymentStatusInfo (string) --Provides information about the results of a deployment, such as whether instances in the original environment in a blue/green deployment were not terminated.

fileExistsBehavior (string) --Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren\'t part of the previous successful deployment.

DISALLOW : The deployment fails. This is also the default behavior if no option is specified.
OVERWRITE : The version of the file from the application revision currently being deployed replaces the version already on the instance.
RETAIN : The version of the file already on the instance is kept and used as part of the new deployment.


deploymentStatusMessages (list) --Messages that contain information about the status of a deployment.

(string) --


computePlatform (string) --The destination platform type for the deployment (Lambda , Server , or ECS ).

externalId (string) --The unique ID for an external resource (for example, a CloudFormation stack ID) that is linked to this deployment.










Exceptions

CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.BatchLimitExceededException


    :return: {
        'deploymentsInfo': [
            {
                'applicationName': 'string',
                'deploymentGroupName': 'string',
                'deploymentConfigName': 'string',
                'deploymentId': 'string',
                'previousRevision': {
                    'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    },
                    'appSpecContent': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
                'revision': {
                    'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    },
                    'appSpecContent': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
                'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                'errorInformation': {
                    'code': 'AGENT_ISSUE'|'ALARM_ACTIVE'|'APPLICATION_MISSING'|'AUTOSCALING_VALIDATION_ERROR'|'AUTO_SCALING_CONFIGURATION'|'AUTO_SCALING_IAM_ROLE_PERMISSIONS'|'CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND'|'CUSTOMER_APPLICATION_UNHEALTHY'|'DEPLOYMENT_GROUP_MISSING'|'ECS_UPDATE_ERROR'|'ELASTIC_LOAD_BALANCING_INVALID'|'ELB_INVALID_INSTANCE'|'HEALTH_CONSTRAINTS'|'HEALTH_CONSTRAINTS_INVALID'|'HOOK_EXECUTION_FAILURE'|'IAM_ROLE_MISSING'|'IAM_ROLE_PERMISSIONS'|'INTERNAL_ERROR'|'INVALID_ECS_SERVICE'|'INVALID_LAMBDA_CONFIGURATION'|'INVALID_LAMBDA_FUNCTION'|'INVALID_REVISION'|'MANUAL_STOP'|'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION'|'MISSING_ELB_INFORMATION'|'MISSING_GITHUB_TOKEN'|'NO_EC2_SUBSCRIPTION'|'NO_INSTANCES'|'OVER_MAX_INSTANCES'|'RESOURCE_LIMIT_EXCEEDED'|'REVISION_MISSING'|'THROTTLED'|'TIMEOUT'|'CLOUDFORMATION_STACK_FAILURE',
                    'message': 'string'
                },
                'createTime': datetime(2015, 1, 1),
                'startTime': datetime(2015, 1, 1),
                'completeTime': datetime(2015, 1, 1),
                'deploymentOverview': {
                    'Pending': 123,
                    'InProgress': 123,
                    'Succeeded': 123,
                    'Failed': 123,
                    'Skipped': 123,
                    'Ready': 123
                },
                'description': 'string',
                'creator': 'user'|'autoscaling'|'codeDeployRollback'|'CodeDeploy'|'CloudFormation'|'CloudFormationRollback',
                'ignoreApplicationStopFailures': True|False,
                'autoRollbackConfiguration': {
                    'enabled': True|False,
                    'events': [
                        'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                    ]
                },
                'updateOutdatedInstancesOnly': True|False,
                'rollbackInfo': {
                    'rollbackDeploymentId': 'string',
                    'rollbackTriggeringDeploymentId': 'string',
                    'rollbackMessage': 'string'
                },
                'deploymentStyle': {
                    'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                    'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                },
                'targetInstances': {
                    'tagFilters': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                    'autoScalingGroups': [
                        'string',
                    ],
                    'ec2TagSet': {
                        'ec2TagSetList': [
                            [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                },
                            ],
                        ]
                    }
                },
                'instanceTerminationWaitTimeStarted': True|False,
                'blueGreenDeploymentConfiguration': {
                    'terminateBlueInstancesOnDeploymentSuccess': {
                        'action': 'TERMINATE'|'KEEP_ALIVE',
                        'terminationWaitTimeInMinutes': 123
                    },
                    'deploymentReadyOption': {
                        'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                        'waitTimeInMinutes': 123
                    },
                    'greenFleetProvisioningOption': {
                        'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                    }
                },
                'loadBalancerInfo': {
                    'elbInfoList': [
                        {
                            'name': 'string'
                        },
                    ],
                    'targetGroupInfoList': [
                        {
                            'name': 'string'
                        },
                    ],
                    'targetGroupPairInfoList': [
                        {
                            'targetGroups': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'prodTrafficRoute': {
                                'listenerArns': [
                                    'string',
                                ]
                            },
                            'testTrafficRoute': {
                                'listenerArns': [
                                    'string',
                                ]
                            }
                        },
                    ]
                },
                'additionalDeploymentStatusInfo': 'string',
                'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN',
                'deploymentStatusMessages': [
                    'string',
                ],
                'computePlatform': 'Server'|'Lambda'|'ECS',
                'externalId': 'string'
            },
        ]
    }
    
    
    :returns: 
    S3: An application revision stored in Amazon S3.
    GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
    String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.
    
    """
    pass

def batch_get_on_premises_instances(instanceNames=None):
    """
    Gets information about one or more on-premises instances. The maximum number of on-premises instances that can be returned is 25.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_on_premises_instances(
        instanceNames=[
            'string',
        ]
    )
    
    
    :type instanceNames: list
    :param instanceNames: [REQUIRED]\nThe names of the on-premises instances about which to get information. The maximum number of instance names you can specify is 25.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'instanceInfos': [
        {
            'instanceName': 'string',
            'iamSessionArn': 'string',
            'iamUserArn': 'string',
            'instanceArn': 'string',
            'registerTime': datetime(2015, 1, 1),
            'deregisterTime': datetime(2015, 1, 1),
            'tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --Represents the output of a BatchGetOnPremisesInstances operation.

instanceInfos (list) --Information about the on-premises instances.

(dict) --Information about an on-premises instance.

instanceName (string) --The name of the on-premises instance.

iamSessionArn (string) --The ARN of the IAM session associated with the on-premises instance.

iamUserArn (string) --The IAM user ARN associated with the on-premises instance.

instanceArn (string) --The ARN of the on-premises instance.

registerTime (datetime) --The time at which the on-premises instance was registered.

deregisterTime (datetime) --If the on-premises instance was deregistered, the time at which the on-premises instance was deregistered.

tags (list) --The tags currently associated with the on-premises instance.

(dict) --Information about a tag.

Key (string) --The tag\'s key.

Value (string) --The tag\'s value.














Exceptions

CodeDeploy.Client.exceptions.InstanceNameRequiredException
CodeDeploy.Client.exceptions.InvalidInstanceNameException
CodeDeploy.Client.exceptions.BatchLimitExceededException


    :return: {
        'instanceInfos': [
            {
                'instanceName': 'string',
                'iamSessionArn': 'string',
                'iamUserArn': 'string',
                'instanceArn': 'string',
                'registerTime': datetime(2015, 1, 1),
                'deregisterTime': datetime(2015, 1, 1),
                'tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.InstanceNameRequiredException
    CodeDeploy.Client.exceptions.InvalidInstanceNameException
    CodeDeploy.Client.exceptions.BatchLimitExceededException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def continue_deployment(deploymentId=None, deploymentWaitType=None):
    """
    For a blue/green deployment, starts the process of rerouting traffic from instances in the original environment to instances in the replacement environment without waiting for a specified wait time to elapse. (Traffic rerouting, which is achieved by registering instances in the replacement environment with the load balancer, can start as soon as all instances have a status of Ready.)
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.continue_deployment(
        deploymentId='string',
        deploymentWaitType='READY_WAIT'|'TERMINATION_WAIT'
    )
    
    
    :type deploymentId: string
    :param deploymentId: The unique ID of a blue/green deployment for which you want to start rerouting traffic to the replacement environment.

    :type deploymentWaitType: string
    :param deploymentWaitType: The status of the deployment\'s waiting period. READY_WAIT indicates that the deployment is ready to start shifting traffic. TERMINATION_WAIT indicates that the traffic is shifted, but the original target is not terminated.

    :returns: 
    CodeDeploy.Client.exceptions.DeploymentIdRequiredException
    CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
    CodeDeploy.Client.exceptions.DeploymentAlreadyCompletedException
    CodeDeploy.Client.exceptions.InvalidDeploymentIdException
    CodeDeploy.Client.exceptions.DeploymentIsNotInReadyStateException
    CodeDeploy.Client.exceptions.UnsupportedActionForDeploymentTypeException
    CodeDeploy.Client.exceptions.InvalidDeploymentWaitTypeException
    CodeDeploy.Client.exceptions.InvalidDeploymentStatusException
    
    """
    pass

def create_application(applicationName=None, computePlatform=None, tags=None):
    """
    Creates an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_application(
        applicationName='string',
        computePlatform='Server'|'Lambda'|'ECS',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of the application. This name must be unique with the applicable IAM user or AWS account.\n

    :type computePlatform: string
    :param computePlatform: The destination platform type for the deployment (Lambda , Server , or ECS ).

    :type tags: list
    :param tags: The metadata that you apply to CodeDeploy applications to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define.\n\n(dict) --Information about a tag.\n\nKey (string) --The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'applicationId': 'string'
}


Response Structure

(dict) --
Represents the output of a CreateApplication operation.

applicationId (string) --
A unique application ID.







Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationAlreadyExistsException
CodeDeploy.Client.exceptions.ApplicationLimitExceededException
CodeDeploy.Client.exceptions.InvalidComputePlatformException
CodeDeploy.Client.exceptions.InvalidTagsToAddException


    :return: {
        'applicationId': 'string'
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.ApplicationNameRequiredException
    CodeDeploy.Client.exceptions.InvalidApplicationNameException
    CodeDeploy.Client.exceptions.ApplicationAlreadyExistsException
    CodeDeploy.Client.exceptions.ApplicationLimitExceededException
    CodeDeploy.Client.exceptions.InvalidComputePlatformException
    CodeDeploy.Client.exceptions.InvalidTagsToAddException
    
    """
    pass

def create_deployment(applicationName=None, deploymentGroupName=None, revision=None, deploymentConfigName=None, description=None, ignoreApplicationStopFailures=None, targetInstances=None, autoRollbackConfiguration=None, updateOutdatedInstancesOnly=None, fileExistsBehavior=None):
    """
    Deploys an application revision through the specified deployment group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_deployment(
        applicationName='string',
        deploymentGroupName='string',
        revision={
            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            },
            'string': {
                'content': 'string',
                'sha256': 'string'
            },
            'appSpecContent': {
                'content': 'string',
                'sha256': 'string'
            }
        },
        deploymentConfigName='string',
        description='string',
        ignoreApplicationStopFailures=True|False,
        targetInstances={
            'tagFilters': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                },
            ],
            'autoScalingGroups': [
                'string',
            ],
            'ec2TagSet': {
                'ec2TagSetList': [
                    [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                ]
            }
        },
        autoRollbackConfiguration={
            'enabled': True|False,
            'events': [
                'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
            ]
        },
        updateOutdatedInstancesOnly=True|False,
        fileExistsBehavior='DISALLOW'|'OVERWRITE'|'RETAIN'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n

    :type deploymentGroupName: string
    :param deploymentGroupName: The name of the deployment group.

    :type revision: dict
    :param revision: The type and location of the revision to deploy.\n\nrevisionType (string) --The type of application revision:\n\nS3: An application revision stored in Amazon S3.\nGitHub: An application revision stored in GitHub (EC2/On-premises deployments only).\nString: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).\nAppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.\n\n\ns3Location (dict) --Information about the location of a revision stored in Amazon S3.\n\nbucket (string) --The name of the Amazon S3 bucket where the application revision is stored.\n\nkey (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.\n\nbundleType (string) --The file type of the application revision. Must be one of the following:\n\ntar : A tar archive file.\ntgz : A compressed tar archive file.\nzip : A zip archive file.\n\n\nversion (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.\nIf the version is not specified, the system uses the most recent version by default.\n\neTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.\nIf the ETag is not specified as an input parameter, ETag validation of the object is skipped.\n\n\n\ngitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.\n\nrepository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.\nSpecified as account/repository.\n\ncommitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.\n\n\n\nstring (dict) --Information about the location of an AWS Lambda deployment revision stored as a RawString.\n\ncontent (string) --The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.\n\nsha256 (string) --The SHA256 hash value of the revision content.\n\n\n\nappSpecContent (dict) --The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.\n\ncontent (string) --The YAML-formatted or JSON-formatted revision string.\nFor an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.\nFor an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.\nFor both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.\n\nsha256 (string) --The SHA256 hash value of the revision content.\n\n\n\n\n

    :type deploymentConfigName: string
    :param deploymentConfigName: The name of a deployment configuration associated with the IAM user or AWS account.\nIf not specified, the value configured in the deployment group is used as the default. If the deployment group does not have a deployment configuration associated with it, CodeDeployDefault .``OneAtATime`` is used by default.\n

    :type description: string
    :param description: A comment about the deployment.

    :type ignoreApplicationStopFailures: boolean
    :param ignoreApplicationStopFailures: If true, then if an ApplicationStop , BeforeBlockTraffic , or AfterBlockTraffic deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if ApplicationStop fails, the deployment continues with DownloadBundle . If BeforeBlockTraffic fails, the deployment continues with BlockTraffic . If AfterBlockTraffic fails, the deployment continues with ApplicationStop .\nIf false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted.\nDuring a deployment, the AWS CodeDeploy agent runs the scripts specified for ApplicationStop , BeforeBlockTraffic , and AfterBlockTraffic in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail.\nIf the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use ignoreApplicationStopFailures to specify that the ApplicationStop , BeforeBlockTraffic , and AfterBlockTraffic failures should be ignored.\n

    :type targetInstances: dict
    :param targetInstances: Information about the instances that belong to the replacement environment in a blue/green deployment.\n\ntagFilters (list) --The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as ec2TagSet .\n\n(dict) --Information about an EC2 tag filter.\n\nKey (string) --The tag filter key.\n\nValue (string) --The tag filter value.\n\nType (string) --The tag filter type:\n\nKEY_ONLY : Key only.\nVALUE_ONLY : Value only.\nKEY_AND_VALUE : Key and value.\n\n\n\n\n\n\nautoScalingGroups (list) --The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.\n\n(string) --\n\n\nec2TagSet (dict) --Information about the groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as tagFilters .\n\nec2TagSetList (list) --A list that contains other lists of EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.\n\n(list) --\n(dict) --Information about an EC2 tag filter.\n\nKey (string) --The tag filter key.\n\nValue (string) --The tag filter value.\n\nType (string) --The tag filter type:\n\nKEY_ONLY : Key only.\nVALUE_ONLY : Value only.\nKEY_AND_VALUE : Key and value.\n\n\n\n\n\n\n\n\n\n\n\n

    :type autoRollbackConfiguration: dict
    :param autoRollbackConfiguration: Configuration information for an automatic rollback that is added when a deployment is created.\n\nenabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.\n\nevents (list) --The event type or types that trigger a rollback.\n\n(string) --\n\n\n\n

    :type updateOutdatedInstancesOnly: boolean
    :param updateOutdatedInstancesOnly: Indicates whether to deploy to all instances or only to instances that are not running the latest application revision.

    :type fileExistsBehavior: string
    :param fileExistsBehavior: Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren\'t part of the previous successful deployment.\nThe fileExistsBehavior parameter takes any of the following values:\n\nDISALLOW: The deployment fails. This is also the default behavior if no option is specified.\nOVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance.\nRETAIN: The version of the file already on the instance is kept and used as part of the new deployment.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'deploymentId': 'string'
}


Response Structure

(dict) --
Represents the output of a CreateDeployment operation.

deploymentId (string) --
The unique ID of a deployment.







Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
CodeDeploy.Client.exceptions.DeploymentGroupDoesNotExistException
CodeDeploy.Client.exceptions.RevisionRequiredException
CodeDeploy.Client.exceptions.RevisionDoesNotExistException
CodeDeploy.Client.exceptions.InvalidRevisionException
CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
CodeDeploy.Client.exceptions.DescriptionTooLongException
CodeDeploy.Client.exceptions.DeploymentLimitExceededException
CodeDeploy.Client.exceptions.InvalidTargetInstancesException
CodeDeploy.Client.exceptions.InvalidAutoRollbackConfigException
CodeDeploy.Client.exceptions.InvalidLoadBalancerInfoException
CodeDeploy.Client.exceptions.InvalidFileExistsBehaviorException
CodeDeploy.Client.exceptions.InvalidRoleException
CodeDeploy.Client.exceptions.InvalidAutoScalingGroupException
CodeDeploy.Client.exceptions.ThrottlingException
CodeDeploy.Client.exceptions.InvalidUpdateOutdatedInstancesOnlyValueException
CodeDeploy.Client.exceptions.InvalidIgnoreApplicationStopFailuresValueException
CodeDeploy.Client.exceptions.InvalidGitHubAccountTokenException
CodeDeploy.Client.exceptions.InvalidTrafficRoutingConfigurationException


    :return: {
        'deploymentId': 'string'
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.ApplicationNameRequiredException
    CodeDeploy.Client.exceptions.InvalidApplicationNameException
    CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
    CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
    CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
    CodeDeploy.Client.exceptions.DeploymentGroupDoesNotExistException
    CodeDeploy.Client.exceptions.RevisionRequiredException
    CodeDeploy.Client.exceptions.RevisionDoesNotExistException
    CodeDeploy.Client.exceptions.InvalidRevisionException
    CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
    CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
    CodeDeploy.Client.exceptions.DescriptionTooLongException
    CodeDeploy.Client.exceptions.DeploymentLimitExceededException
    CodeDeploy.Client.exceptions.InvalidTargetInstancesException
    CodeDeploy.Client.exceptions.InvalidAutoRollbackConfigException
    CodeDeploy.Client.exceptions.InvalidLoadBalancerInfoException
    CodeDeploy.Client.exceptions.InvalidFileExistsBehaviorException
    CodeDeploy.Client.exceptions.InvalidRoleException
    CodeDeploy.Client.exceptions.InvalidAutoScalingGroupException
    CodeDeploy.Client.exceptions.ThrottlingException
    CodeDeploy.Client.exceptions.InvalidUpdateOutdatedInstancesOnlyValueException
    CodeDeploy.Client.exceptions.InvalidIgnoreApplicationStopFailuresValueException
    CodeDeploy.Client.exceptions.InvalidGitHubAccountTokenException
    CodeDeploy.Client.exceptions.InvalidTrafficRoutingConfigurationException
    
    """
    pass

def create_deployment_config(deploymentConfigName=None, minimumHealthyHosts=None, trafficRoutingConfig=None, computePlatform=None):
    """
    Creates a deployment configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_deployment_config(
        deploymentConfigName='string',
        minimumHealthyHosts={
            'value': 123,
            'type': 'HOST_COUNT'|'FLEET_PERCENT'
        },
        trafficRoutingConfig={
            'type': 'TimeBasedCanary'|'TimeBasedLinear'|'AllAtOnce',
            'timeBasedCanary': {
                'canaryPercentage': 123,
                'canaryInterval': 123
            },
            'timeBasedLinear': {
                'linearPercentage': 123,
                'linearInterval': 123
            }
        },
        computePlatform='Server'|'Lambda'|'ECS'
    )
    
    
    :type deploymentConfigName: string
    :param deploymentConfigName: [REQUIRED]\nThe name of the deployment configuration to create.\n

    :type minimumHealthyHosts: dict
    :param minimumHealthyHosts: The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.\nThe type parameter takes either of the following values:\n\nHOST_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value.\nFLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of instances and rounds up fractional instances.\n\nThe value parameter takes an integer.\nFor example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a value of 95.\n\nvalue (integer) --The minimum healthy instance value.\n\ntype (string) --The minimum healthy instance type:\n\nHOST_COUNT : The minimum number of healthy instances as an absolute value.\nFLEET_PERCENT : The minimum number of healthy instances as a percentage of the total number of instances in the deployment.\n\nIn an example of nine instances, if a HOST_COUNT of six is specified, deploy to up to three instances at a time. The deployment is successful if six or more instances are deployed to successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to five instances at a time. The deployment is successful if four or more instances are deployed to successfully. Otherwise, the deployment fails.\n\nNote\nIn a call to the GetDeploymentConfig , CodeDeployDefault.OneAtATime returns a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment is still successful.\n\nFor more information, see AWS CodeDeploy Instance Health in the AWS CodeDeploy User Guide .\n\n\n

    :type trafficRoutingConfig: dict
    :param trafficRoutingConfig: The configuration that specifies how the deployment traffic is routed.\n\ntype (string) --The type of traffic shifting (TimeBasedCanary or TimeBasedLinear ) used by a deployment configuration.\n\ntimeBasedCanary (dict) --A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in two increments. The original and target Lambda function versions or ECS task sets are specified in the deployment\'s AppSpec file.\n\ncanaryPercentage (integer) --The percentage of traffic to shift in the first increment of a TimeBasedCanary deployment.\n\ncanaryInterval (integer) --The number of minutes between the first and second traffic shifts of a TimeBasedCanary deployment.\n\n\n\ntimeBasedLinear (dict) --A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions or ECS task sets are specified in the deployment\'s AppSpec file.\n\nlinearPercentage (integer) --The percentage of traffic that is shifted at the start of each increment of a TimeBasedLinear deployment.\n\nlinearInterval (integer) --The number of minutes between each incremental traffic shift of a TimeBasedLinear deployment.\n\n\n\n\n

    :type computePlatform: string
    :param computePlatform: The destination platform type for the deployment (Lambda , Server , or ECS ).

    :rtype: dict

ReturnsResponse Syntax
{
    'deploymentConfigId': 'string'
}


Response Structure

(dict) --
Represents the output of a CreateDeploymentConfig operation.

deploymentConfigId (string) --
A unique deployment configuration ID.







Exceptions

CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
CodeDeploy.Client.exceptions.DeploymentConfigNameRequiredException
CodeDeploy.Client.exceptions.DeploymentConfigAlreadyExistsException
CodeDeploy.Client.exceptions.InvalidMinimumHealthyHostValueException
CodeDeploy.Client.exceptions.DeploymentConfigLimitExceededException
CodeDeploy.Client.exceptions.InvalidComputePlatformException
CodeDeploy.Client.exceptions.InvalidTrafficRoutingConfigurationException


    :return: {
        'deploymentConfigId': 'string'
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
    CodeDeploy.Client.exceptions.DeploymentConfigNameRequiredException
    CodeDeploy.Client.exceptions.DeploymentConfigAlreadyExistsException
    CodeDeploy.Client.exceptions.InvalidMinimumHealthyHostValueException
    CodeDeploy.Client.exceptions.DeploymentConfigLimitExceededException
    CodeDeploy.Client.exceptions.InvalidComputePlatformException
    CodeDeploy.Client.exceptions.InvalidTrafficRoutingConfigurationException
    
    """
    pass

def create_deployment_group(applicationName=None, deploymentGroupName=None, deploymentConfigName=None, ec2TagFilters=None, onPremisesInstanceTagFilters=None, autoScalingGroups=None, serviceRoleArn=None, triggerConfigurations=None, alarmConfiguration=None, autoRollbackConfiguration=None, deploymentStyle=None, blueGreenDeploymentConfiguration=None, loadBalancerInfo=None, ec2TagSet=None, ecsServices=None, onPremisesTagSet=None, tags=None):
    """
    Creates a deployment group to which application revisions are deployed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_deployment_group(
        applicationName='string',
        deploymentGroupName='string',
        deploymentConfigName='string',
        ec2TagFilters=[
            {
                'Key': 'string',
                'Value': 'string',
                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
            },
        ],
        onPremisesInstanceTagFilters=[
            {
                'Key': 'string',
                'Value': 'string',
                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
            },
        ],
        autoScalingGroups=[
            'string',
        ],
        serviceRoleArn='string',
        triggerConfigurations=[
            {
                'triggerName': 'string',
                'triggerTargetArn': 'string',
                'triggerEvents': [
                    'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                ]
            },
        ],
        alarmConfiguration={
            'enabled': True|False,
            'ignorePollAlarmFailure': True|False,
            'alarms': [
                {
                    'name': 'string'
                },
            ]
        },
        autoRollbackConfiguration={
            'enabled': True|False,
            'events': [
                'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
            ]
        },
        deploymentStyle={
            'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
            'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
        },
        blueGreenDeploymentConfiguration={
            'terminateBlueInstancesOnDeploymentSuccess': {
                'action': 'TERMINATE'|'KEEP_ALIVE',
                'terminationWaitTimeInMinutes': 123
            },
            'deploymentReadyOption': {
                'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                'waitTimeInMinutes': 123
            },
            'greenFleetProvisioningOption': {
                'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
            }
        },
        loadBalancerInfo={
            'elbInfoList': [
                {
                    'name': 'string'
                },
            ],
            'targetGroupInfoList': [
                {
                    'name': 'string'
                },
            ],
            'targetGroupPairInfoList': [
                {
                    'targetGroups': [
                        {
                            'name': 'string'
                        },
                    ],
                    'prodTrafficRoute': {
                        'listenerArns': [
                            'string',
                        ]
                    },
                    'testTrafficRoute': {
                        'listenerArns': [
                            'string',
                        ]
                    }
                },
            ]
        },
        ec2TagSet={
            'ec2TagSetList': [
                [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
            ]
        },
        ecsServices=[
            {
                'serviceName': 'string',
                'clusterName': 'string'
            },
        ],
        onPremisesTagSet={
            'onPremisesTagSetList': [
                [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
            ]
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n

    :type deploymentGroupName: string
    :param deploymentGroupName: [REQUIRED]\nThe name of a new deployment group for the specified application.\n

    :type deploymentConfigName: string
    :param deploymentConfigName: If specified, the deployment configuration name can be either one of the predefined configurations provided with AWS CodeDeploy or a custom deployment configuration that you create by calling the create deployment configuration operation.\n\nCodeDeployDefault.OneAtATime is the default deployment configuration. It is used if a configuration isn\'t specified for the deployment or deployment group.\nFor more information about the predefined deployment configurations in AWS CodeDeploy, see Working with Deployment Configurations in CodeDeploy in the AWS CodeDeploy User Guide .\n

    :type ec2TagFilters: list
    :param ec2TagFilters: The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with any of the specified tags. Cannot be used in the same call as ec2TagSet.\n\n(dict) --Information about an EC2 tag filter.\n\nKey (string) --The tag filter key.\n\nValue (string) --The tag filter value.\n\nType (string) --The tag filter type:\n\nKEY_ONLY : Key only.\nVALUE_ONLY : Value only.\nKEY_AND_VALUE : Key and value.\n\n\n\n\n\n

    :type onPremisesInstanceTagFilters: list
    :param onPremisesInstanceTagFilters: The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags. Cannot be used in the same call as OnPremisesTagSet .\n\n(dict) --Information about an on-premises instance tag filter.\n\nKey (string) --The on-premises instance tag filter key.\n\nValue (string) --The on-premises instance tag filter value.\n\nType (string) --The on-premises instance tag filter type:\n\nKEY_ONLY: Key only.\nVALUE_ONLY: Value only.\nKEY_AND_VALUE: Key and value.\n\n\n\n\n\n

    :type autoScalingGroups: list
    :param autoScalingGroups: A list of associated Amazon EC2 Auto Scaling groups.\n\n(string) --\n\n

    :type serviceRoleArn: string
    :param serviceRoleArn: [REQUIRED]\nA service role Amazon Resource Name (ARN) that allows AWS CodeDeploy to act on the user\'s behalf when interacting with AWS services.\n

    :type triggerConfigurations: list
    :param triggerConfigurations: Information about triggers to create when the deployment group is created. For examples, see Create a Trigger for an AWS CodeDeploy Event in the AWS CodeDeploy User Guide .\n\n(dict) --Information about notification triggers for the deployment group.\n\ntriggerName (string) --The name of the notification trigger.\n\ntriggerTargetArn (string) --The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.\n\ntriggerEvents (list) --The event type or types for which notifications are triggered.\n\n(string) --\n\n\n\n\n\n

    :type alarmConfiguration: dict
    :param alarmConfiguration: Information to add about Amazon CloudWatch alarms when the deployment group is created.\n\nenabled (boolean) --Indicates whether the alarm configuration is enabled.\n\nignorePollAlarmFailure (boolean) --Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.\n\ntrue : The deployment proceeds even if alarm status information can\'t be retrieved from Amazon CloudWatch.\nfalse : The deployment stops if alarm status information can\'t be retrieved from Amazon CloudWatch.\n\n\nalarms (list) --A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.\n\n(dict) --Information about an alarm.\n\nname (string) --The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.\n\n\n\n\n\n\n

    :type autoRollbackConfiguration: dict
    :param autoRollbackConfiguration: Configuration information for an automatic rollback that is added when a deployment group is created.\n\nenabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.\n\nevents (list) --The event type or types that trigger a rollback.\n\n(string) --\n\n\n\n

    :type deploymentStyle: dict
    :param deploymentStyle: Information about the type of deployment, in-place or blue/green, that you want to run and whether to route deployment traffic behind a load balancer.\n\ndeploymentType (string) --Indicates whether to run an in-place deployment or a blue/green deployment.\n\ndeploymentOption (string) --Indicates whether to route deployment traffic behind a load balancer.\n\n\n

    :type blueGreenDeploymentConfiguration: dict
    :param blueGreenDeploymentConfiguration: Information about blue/green deployment options for a deployment group.\n\nterminateBlueInstancesOnDeploymentSuccess (dict) --Information about whether to terminate instances in the original fleet during a blue/green deployment.\n\naction (string) --The action to take on instances in the original environment after a successful blue/green deployment.\n\nTERMINATE : Instances are terminated after a specified wait time.\nKEEP_ALIVE : Instances are left running after they are deregistered from the load balancer and removed from the deployment group.\n\n\nterminationWaitTimeInMinutes (integer) --For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.\nFor an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set.\nThe maximum setting is 2880 minutes (2 days).\n\n\n\ndeploymentReadyOption (dict) --Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.\n\nactionOnTimeout (string) --Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.\n\nCONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.\nSTOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using ContinueDeployment . If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.\n\n\nwaitTimeInMinutes (integer) --The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout .\n\n\n\ngreenFleetProvisioningOption (dict) --Information about how instances are provisioned for a replacement environment in a blue/green deployment.\n\naction (string) --The method used to add instances to a replacement environment.\n\nDISCOVER_EXISTING : Use instances that already exist or will be created manually.\nCOPY_AUTO_SCALING_GROUP : Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.\n\n\n\n\n\n

    :type loadBalancerInfo: dict
    :param loadBalancerInfo: Information about the load balancer used in a deployment.\n\nelbInfoList (list) --An array that contains information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.\n\nNote\nAdding more than one load balancer to the array is not supported.\n\n\n(dict) --Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.\n\nname (string) --For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.\n\n\n\n\n\ntargetGroupInfoList (list) --An array that contains information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.\n\nNote\nAdding more than one target group to the array is not supported.\n\n\n(dict) --Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.\n\nname (string) --For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.\n\n\n\n\n\ntargetGroupPairInfoList (list) --The target group pair information. This is an array of TargeGroupPairInfo objects with a maximum size of one.\n\n(dict) --Information about two target groups and how traffic is routed during an Amazon ECS deployment. An optional test traffic route can be specified.\n\ntargetGroups (list) --One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete.\n\n(dict) --Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.\n\nname (string) --For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.\n\n\n\n\n\nprodTrafficRoute (dict) --The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete.\n\nlistenerArns (list) --The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.\n\n(string) --\n\n\n\n\ntestTrafficRoute (dict) --An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment.\n\nlistenerArns (list) --The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type ec2TagSet: dict
    :param ec2TagSet: Information about groups of tags applied to EC2 instances. The deployment group includes only EC2 instances identified by all the tag groups. Cannot be used in the same call as ec2TagFilters .\n\nec2TagSetList (list) --A list that contains other lists of EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.\n\n(list) --\n(dict) --Information about an EC2 tag filter.\n\nKey (string) --The tag filter key.\n\nValue (string) --The tag filter value.\n\nType (string) --The tag filter type:\n\nKEY_ONLY : Key only.\nVALUE_ONLY : Value only.\nKEY_AND_VALUE : Key and value.\n\n\n\n\n\n\n\n\n\n

    :type ecsServices: list
    :param ecsServices: The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <clustername>:<servicename> .\n\n(dict) --Contains the service and cluster names used to identify an Amazon ECS deployment\'s target.\n\nserviceName (string) --The name of the target Amazon ECS service.\n\nclusterName (string) --The name of the cluster that the Amazon ECS service is associated with.\n\n\n\n\n

    :type onPremisesTagSet: dict
    :param onPremisesTagSet: Information about groups of tags applied to on-premises instances. The deployment group includes only on-premises instances identified by all of the tag groups. Cannot be used in the same call as onPremisesInstanceTagFilters .\n\nonPremisesTagSetList (list) --A list that contains other lists of on-premises instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.\n\n(list) --\n(dict) --Information about an on-premises instance tag filter.\n\nKey (string) --The on-premises instance tag filter key.\n\nValue (string) --The on-premises instance tag filter value.\n\nType (string) --The on-premises instance tag filter type:\n\nKEY_ONLY: Key only.\nVALUE_ONLY: Value only.\nKEY_AND_VALUE: Key and value.\n\n\n\n\n\n\n\n\n\n

    :type tags: list
    :param tags: The metadata that you apply to CodeDeploy deployment groups to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define.\n\n(dict) --Information about a tag.\n\nKey (string) --The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'deploymentGroupId': 'string'
}


Response Structure

(dict) --
Represents the output of a CreateDeploymentGroup operation.

deploymentGroupId (string) --
A unique deployment group ID.







Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
CodeDeploy.Client.exceptions.DeploymentGroupAlreadyExistsException
CodeDeploy.Client.exceptions.InvalidEC2TagException
CodeDeploy.Client.exceptions.InvalidTagException
CodeDeploy.Client.exceptions.InvalidAutoScalingGroupException
CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
CodeDeploy.Client.exceptions.RoleRequiredException
CodeDeploy.Client.exceptions.InvalidRoleException
CodeDeploy.Client.exceptions.DeploymentGroupLimitExceededException
CodeDeploy.Client.exceptions.LifecycleHookLimitExceededException
CodeDeploy.Client.exceptions.InvalidTriggerConfigException
CodeDeploy.Client.exceptions.TriggerTargetsLimitExceededException
CodeDeploy.Client.exceptions.InvalidAlarmConfigException
CodeDeploy.Client.exceptions.AlarmsLimitExceededException
CodeDeploy.Client.exceptions.InvalidAutoRollbackConfigException
CodeDeploy.Client.exceptions.InvalidLoadBalancerInfoException
CodeDeploy.Client.exceptions.InvalidDeploymentStyleException
CodeDeploy.Client.exceptions.InvalidBlueGreenDeploymentConfigurationException
CodeDeploy.Client.exceptions.InvalidEC2TagCombinationException
CodeDeploy.Client.exceptions.InvalidOnPremisesTagCombinationException
CodeDeploy.Client.exceptions.TagSetListLimitExceededException
CodeDeploy.Client.exceptions.InvalidInputException
CodeDeploy.Client.exceptions.ThrottlingException
CodeDeploy.Client.exceptions.InvalidECSServiceException
CodeDeploy.Client.exceptions.InvalidTargetGroupPairException
CodeDeploy.Client.exceptions.ECSServiceMappingLimitExceededException
CodeDeploy.Client.exceptions.InvalidTagsToAddException
CodeDeploy.Client.exceptions.InvalidTrafficRoutingConfigurationException


    :return: {
        'deploymentGroupId': 'string'
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.ApplicationNameRequiredException
    CodeDeploy.Client.exceptions.InvalidApplicationNameException
    CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
    CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
    CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
    CodeDeploy.Client.exceptions.DeploymentGroupAlreadyExistsException
    CodeDeploy.Client.exceptions.InvalidEC2TagException
    CodeDeploy.Client.exceptions.InvalidTagException
    CodeDeploy.Client.exceptions.InvalidAutoScalingGroupException
    CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
    CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
    CodeDeploy.Client.exceptions.RoleRequiredException
    CodeDeploy.Client.exceptions.InvalidRoleException
    CodeDeploy.Client.exceptions.DeploymentGroupLimitExceededException
    CodeDeploy.Client.exceptions.LifecycleHookLimitExceededException
    CodeDeploy.Client.exceptions.InvalidTriggerConfigException
    CodeDeploy.Client.exceptions.TriggerTargetsLimitExceededException
    CodeDeploy.Client.exceptions.InvalidAlarmConfigException
    CodeDeploy.Client.exceptions.AlarmsLimitExceededException
    CodeDeploy.Client.exceptions.InvalidAutoRollbackConfigException
    CodeDeploy.Client.exceptions.InvalidLoadBalancerInfoException
    CodeDeploy.Client.exceptions.InvalidDeploymentStyleException
    CodeDeploy.Client.exceptions.InvalidBlueGreenDeploymentConfigurationException
    CodeDeploy.Client.exceptions.InvalidEC2TagCombinationException
    CodeDeploy.Client.exceptions.InvalidOnPremisesTagCombinationException
    CodeDeploy.Client.exceptions.TagSetListLimitExceededException
    CodeDeploy.Client.exceptions.InvalidInputException
    CodeDeploy.Client.exceptions.ThrottlingException
    CodeDeploy.Client.exceptions.InvalidECSServiceException
    CodeDeploy.Client.exceptions.InvalidTargetGroupPairException
    CodeDeploy.Client.exceptions.ECSServiceMappingLimitExceededException
    CodeDeploy.Client.exceptions.InvalidTagsToAddException
    CodeDeploy.Client.exceptions.InvalidTrafficRoutingConfigurationException
    
    """
    pass

def delete_application(applicationName=None):
    """
    Deletes an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application(
        applicationName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n

    """
    pass

def delete_deployment_config(deploymentConfigName=None):
    """
    Deletes a deployment configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_deployment_config(
        deploymentConfigName='string'
    )
    
    
    :type deploymentConfigName: string
    :param deploymentConfigName: [REQUIRED]\nThe name of a deployment configuration associated with the IAM user or AWS account.\n

    """
    pass

def delete_deployment_group(applicationName=None, deploymentGroupName=None):
    """
    Deletes a deployment group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_deployment_group(
        applicationName='string',
        deploymentGroupName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n

    :type deploymentGroupName: string
    :param deploymentGroupName: [REQUIRED]\nThe name of a deployment group for the specified application.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'hooksNotCleanedUp': [
        {
            'name': 'string',
            'hook': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a DeleteDeploymentGroup operation.

hooksNotCleanedUp (list) --
If the output contains no data, and the corresponding deployment group contained at least one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group. If the output contains data, AWS CodeDeploy could not remove some Auto Scaling lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group.

(dict) --
Information about an Auto Scaling group.

name (string) --
The Auto Scaling group name.

hook (string) --
An Auto Scaling lifecycle event hook name.











Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
CodeDeploy.Client.exceptions.InvalidRoleException


    :return: {
        'hooksNotCleanedUp': [
            {
                'name': 'string',
                'hook': 'string'
            },
        ]
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.ApplicationNameRequiredException
    CodeDeploy.Client.exceptions.InvalidApplicationNameException
    CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
    CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
    CodeDeploy.Client.exceptions.InvalidRoleException
    
    """
    pass

def delete_git_hub_account_token(tokenName=None):
    """
    Deletes a GitHub account connection.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_git_hub_account_token(
        tokenName='string'
    )
    
    
    :type tokenName: string
    :param tokenName: The name of the GitHub account connection to delete.

    :rtype: dict
ReturnsResponse Syntax{
    'tokenName': 'string'
}


Response Structure

(dict) --Represents the output of a DeleteGitHubAccountToken operation.

tokenName (string) --The name of the GitHub account connection that was deleted.






Exceptions

CodeDeploy.Client.exceptions.GitHubAccountTokenNameRequiredException
CodeDeploy.Client.exceptions.GitHubAccountTokenDoesNotExistException
CodeDeploy.Client.exceptions.InvalidGitHubAccountTokenNameException
CodeDeploy.Client.exceptions.ResourceValidationException
CodeDeploy.Client.exceptions.OperationNotSupportedException


    :return: {
        'tokenName': 'string'
    }
    
    
    """
    pass

def delete_resources_by_external_id(externalId=None):
    """
    Deletes resources linked to an external ID.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_resources_by_external_id(
        externalId='string'
    )
    
    
    :type externalId: string
    :param externalId: The unique ID of an external resource (for example, a CloudFormation stack ID) that is linked to one or more CodeDeploy resources.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --




    :return: {}
    
    
    """
    pass

def deregister_on_premises_instance(instanceName=None):
    """
    Deregisters an on-premises instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_on_premises_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the on-premises instance to deregister.\n

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

def get_application(applicationName=None):
    """
    Gets information about an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_application(
        applicationName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n

    :rtype: dict
ReturnsResponse Syntax{
    'application': {
        'applicationId': 'string',
        'applicationName': 'string',
        'createTime': datetime(2015, 1, 1),
        'linkedToGitHub': True|False,
        'gitHubAccountName': 'string',
        'computePlatform': 'Server'|'Lambda'|'ECS'
    }
}


Response Structure

(dict) --Represents the output of a GetApplication operation.

application (dict) --Information about the application.

applicationId (string) --The application ID.

applicationName (string) --The application name.

createTime (datetime) --The time at which the application was created.

linkedToGitHub (boolean) --True if the user has authenticated with GitHub for the specified application. Otherwise, false.

gitHubAccountName (string) --The name for a connection to a GitHub account.

computePlatform (string) --The destination platform type for deployment of the application (Lambda or Server ).








Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException


    :return: {
        'application': {
            'applicationId': 'string',
            'applicationName': 'string',
            'createTime': datetime(2015, 1, 1),
            'linkedToGitHub': True|False,
            'gitHubAccountName': 'string',
            'computePlatform': 'Server'|'Lambda'|'ECS'
        }
    }
    
    
    """
    pass

def get_application_revision(applicationName=None, revision=None):
    """
    Gets information about an application revision.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_application_revision(
        applicationName='string',
        revision={
            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            },
            'string': {
                'content': 'string',
                'sha256': 'string'
            },
            'appSpecContent': {
                'content': 'string',
                'sha256': 'string'
            }
        }
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of the application that corresponds to the revision.\n

    :type revision: dict
    :param revision: [REQUIRED]\nInformation about the application revision to get, including type and location.\n\nrevisionType (string) --The type of application revision:\n\nS3: An application revision stored in Amazon S3.\nGitHub: An application revision stored in GitHub (EC2/On-premises deployments only).\nString: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).\nAppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.\n\n\ns3Location (dict) --Information about the location of a revision stored in Amazon S3.\n\nbucket (string) --The name of the Amazon S3 bucket where the application revision is stored.\n\nkey (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.\n\nbundleType (string) --The file type of the application revision. Must be one of the following:\n\ntar : A tar archive file.\ntgz : A compressed tar archive file.\nzip : A zip archive file.\n\n\nversion (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.\nIf the version is not specified, the system uses the most recent version by default.\n\neTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.\nIf the ETag is not specified as an input parameter, ETag validation of the object is skipped.\n\n\n\ngitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.\n\nrepository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.\nSpecified as account/repository.\n\ncommitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.\n\n\n\nstring (dict) --Information about the location of an AWS Lambda deployment revision stored as a RawString.\n\ncontent (string) --The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.\n\nsha256 (string) --The SHA256 hash value of the revision content.\n\n\n\nappSpecContent (dict) --The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.\n\ncontent (string) --The YAML-formatted or JSON-formatted revision string.\nFor an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.\nFor an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.\nFor both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.\n\nsha256 (string) --The SHA256 hash value of the revision content.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'applicationName': 'string',
    'revision': {
        'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
        's3Location': {
            'bucket': 'string',
            'key': 'string',
            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
            'version': 'string',
            'eTag': 'string'
        },
        'gitHubLocation': {
            'repository': 'string',
            'commitId': 'string'
        },
        'string': {
            'content': 'string',
            'sha256': 'string'
        },
        'appSpecContent': {
            'content': 'string',
            'sha256': 'string'
        }
    },
    'revisionInfo': {
        'description': 'string',
        'deploymentGroups': [
            'string',
        ],
        'firstUsedTime': datetime(2015, 1, 1),
        'lastUsedTime': datetime(2015, 1, 1),
        'registerTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Represents the output of a GetApplicationRevision operation.

applicationName (string) --
The name of the application that corresponds to the revision.

revision (dict) --
Additional information about the revision, including type and location.

revisionType (string) --
The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location (dict) --
Information about the location of a revision stored in Amazon S3.

bucket (string) --
The name of the Amazon S3 bucket where the application revision is stored.

key (string) --
The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType (string) --
The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version (string) --
A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag (string) --
The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.



gitHubLocation (dict) --
Information about the location of application artifacts stored in GitHub.

repository (string) --
The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId (string) --
The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.



string (dict) --
Information about the location of an AWS Lambda deployment revision stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 (string) --
The SHA256 hash value of the revision content.



appSpecContent (dict) --
The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 (string) --
The SHA256 hash value of the revision content.





revisionInfo (dict) --
General information about the revision.

description (string) --
A comment about the revision.

deploymentGroups (list) --
The deployment groups for which this is the current target revision.

(string) --


firstUsedTime (datetime) --
When the revision was first used by AWS CodeDeploy.

lastUsedTime (datetime) --
When the revision was last used by AWS CodeDeploy.

registerTime (datetime) --
When the revision was registered with AWS CodeDeploy.









Exceptions

CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.RevisionDoesNotExistException
CodeDeploy.Client.exceptions.RevisionRequiredException
CodeDeploy.Client.exceptions.InvalidRevisionException


    :return: {
        'applicationName': 'string',
        'revision': {
            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            },
            'string': {
                'content': 'string',
                'sha256': 'string'
            },
            'appSpecContent': {
                'content': 'string',
                'sha256': 'string'
            }
        },
        'revisionInfo': {
            'description': 'string',
            'deploymentGroups': [
                'string',
            ],
            'firstUsedTime': datetime(2015, 1, 1),
            'lastUsedTime': datetime(2015, 1, 1),
            'registerTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    S3: An application revision stored in Amazon S3.
    GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
    String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.
    
    """
    pass

def get_deployment(deploymentId=None):
    """
    Gets information about a deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployment(
        deploymentId='string'
    )
    
    
    :type deploymentId: string
    :param deploymentId: [REQUIRED]\nThe unique ID of a deployment associated with the IAM user or AWS account.\n

    :rtype: dict
ReturnsResponse Syntax{
    'deploymentInfo': {
        'applicationName': 'string',
        'deploymentGroupName': 'string',
        'deploymentConfigName': 'string',
        'deploymentId': 'string',
        'previousRevision': {
            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            },
            'string': {
                'content': 'string',
                'sha256': 'string'
            },
            'appSpecContent': {
                'content': 'string',
                'sha256': 'string'
            }
        },
        'revision': {
            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            },
            'string': {
                'content': 'string',
                'sha256': 'string'
            },
            'appSpecContent': {
                'content': 'string',
                'sha256': 'string'
            }
        },
        'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
        'errorInformation': {
            'code': 'AGENT_ISSUE'|'ALARM_ACTIVE'|'APPLICATION_MISSING'|'AUTOSCALING_VALIDATION_ERROR'|'AUTO_SCALING_CONFIGURATION'|'AUTO_SCALING_IAM_ROLE_PERMISSIONS'|'CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND'|'CUSTOMER_APPLICATION_UNHEALTHY'|'DEPLOYMENT_GROUP_MISSING'|'ECS_UPDATE_ERROR'|'ELASTIC_LOAD_BALANCING_INVALID'|'ELB_INVALID_INSTANCE'|'HEALTH_CONSTRAINTS'|'HEALTH_CONSTRAINTS_INVALID'|'HOOK_EXECUTION_FAILURE'|'IAM_ROLE_MISSING'|'IAM_ROLE_PERMISSIONS'|'INTERNAL_ERROR'|'INVALID_ECS_SERVICE'|'INVALID_LAMBDA_CONFIGURATION'|'INVALID_LAMBDA_FUNCTION'|'INVALID_REVISION'|'MANUAL_STOP'|'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION'|'MISSING_ELB_INFORMATION'|'MISSING_GITHUB_TOKEN'|'NO_EC2_SUBSCRIPTION'|'NO_INSTANCES'|'OVER_MAX_INSTANCES'|'RESOURCE_LIMIT_EXCEEDED'|'REVISION_MISSING'|'THROTTLED'|'TIMEOUT'|'CLOUDFORMATION_STACK_FAILURE',
            'message': 'string'
        },
        'createTime': datetime(2015, 1, 1),
        'startTime': datetime(2015, 1, 1),
        'completeTime': datetime(2015, 1, 1),
        'deploymentOverview': {
            'Pending': 123,
            'InProgress': 123,
            'Succeeded': 123,
            'Failed': 123,
            'Skipped': 123,
            'Ready': 123
        },
        'description': 'string',
        'creator': 'user'|'autoscaling'|'codeDeployRollback'|'CodeDeploy'|'CloudFormation'|'CloudFormationRollback',
        'ignoreApplicationStopFailures': True|False,
        'autoRollbackConfiguration': {
            'enabled': True|False,
            'events': [
                'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
            ]
        },
        'updateOutdatedInstancesOnly': True|False,
        'rollbackInfo': {
            'rollbackDeploymentId': 'string',
            'rollbackTriggeringDeploymentId': 'string',
            'rollbackMessage': 'string'
        },
        'deploymentStyle': {
            'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
            'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
        },
        'targetInstances': {
            'tagFilters': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                },
            ],
            'autoScalingGroups': [
                'string',
            ],
            'ec2TagSet': {
                'ec2TagSetList': [
                    [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                ]
            }
        },
        'instanceTerminationWaitTimeStarted': True|False,
        'blueGreenDeploymentConfiguration': {
            'terminateBlueInstancesOnDeploymentSuccess': {
                'action': 'TERMINATE'|'KEEP_ALIVE',
                'terminationWaitTimeInMinutes': 123
            },
            'deploymentReadyOption': {
                'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                'waitTimeInMinutes': 123
            },
            'greenFleetProvisioningOption': {
                'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
            }
        },
        'loadBalancerInfo': {
            'elbInfoList': [
                {
                    'name': 'string'
                },
            ],
            'targetGroupInfoList': [
                {
                    'name': 'string'
                },
            ],
            'targetGroupPairInfoList': [
                {
                    'targetGroups': [
                        {
                            'name': 'string'
                        },
                    ],
                    'prodTrafficRoute': {
                        'listenerArns': [
                            'string',
                        ]
                    },
                    'testTrafficRoute': {
                        'listenerArns': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'additionalDeploymentStatusInfo': 'string',
        'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN',
        'deploymentStatusMessages': [
            'string',
        ],
        'computePlatform': 'Server'|'Lambda'|'ECS',
        'externalId': 'string'
    }
}


Response Structure

(dict) --Represents the output of a GetDeployment operation.

deploymentInfo (dict) --Information about the deployment.

applicationName (string) --The application name.

deploymentGroupName (string) --The deployment group name.

deploymentConfigName (string) --The deployment configuration name.

deploymentId (string) --The unique ID of a deployment.

previousRevision (dict) --Information about the application revision that was deployed to the deployment group before the most recent successful deployment.

revisionType (string) --The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location (dict) --Information about the location of a revision stored in Amazon S3.

bucket (string) --The name of the Amazon S3 bucket where the application revision is stored.

key (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType (string) --The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.



gitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.

repository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.



string (dict) --Information about the location of an AWS Lambda deployment revision stored as a RawString.

content (string) --The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 (string) --The SHA256 hash value of the revision content.



appSpecContent (dict) --The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content (string) --The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 (string) --The SHA256 hash value of the revision content.





revision (dict) --Information about the location of stored application artifacts and the service from which to retrieve them.

revisionType (string) --The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location (dict) --Information about the location of a revision stored in Amazon S3.

bucket (string) --The name of the Amazon S3 bucket where the application revision is stored.

key (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType (string) --The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.



gitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.

repository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.



string (dict) --Information about the location of an AWS Lambda deployment revision stored as a RawString.

content (string) --The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 (string) --The SHA256 hash value of the revision content.



appSpecContent (dict) --The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content (string) --The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 (string) --The SHA256 hash value of the revision content.





status (string) --The current state of the deployment as a whole.

errorInformation (dict) --Information about any error associated with this deployment.

code (string) --For more information, see Error Codes for AWS CodeDeploy in the AWS CodeDeploy User Guide .
The error code:

APPLICATION_MISSING: The application was missing. This error code is most likely raised if the application is deleted after the deployment is created, but before it is started.
DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most likely raised if the deployment group is deleted after the deployment is created, but before it is started.
HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified.
HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the instance health constraints specified.
IAM_ROLE_MISSING: The service role cannot be accessed.
IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.
INTERNAL_ERROR: There was an internal error.
NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.
NO_INSTANCES: No instances were specified, or no instances can be found.
OVER_MAX_INSTANCES: The maximum number of instances was exceeded.
THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more AWS services.
TIMEOUT: The deployment has timed out.
REVISION_MISSING: The revision ID was missing. This error code is most likely raised if the revision is deleted after the deployment is created, but before it is started.


message (string) --An accompanying error message.



createTime (datetime) --A timestamp that indicates when the deployment was created.

startTime (datetime) --A timestamp that indicates when the deployment was deployed to the deployment group.
In some cases, the reported value of the start time might be later than the complete time. This is due to differences in the clock settings of backend servers that participate in the deployment process.

completeTime (datetime) --A timestamp that indicates when the deployment was complete.

deploymentOverview (dict) --A summary of the deployment status of the instances in the deployment.

Pending (integer) --The number of instances in the deployment in a pending state.

InProgress (integer) --The number of instances in which the deployment is in progress.

Succeeded (integer) --The number of instances in the deployment to which revisions have been successfully deployed.

Failed (integer) --The number of instances in the deployment in a failed state.

Skipped (integer) --The number of instances in the deployment in a skipped state.

Ready (integer) --The number of instances in a replacement environment ready to receive traffic in a blue/green deployment.



description (string) --A comment about the deployment.

creator (string) --The means by which the deployment was created:

user : A user created the deployment.
autoscaling : Amazon EC2 Auto Scaling created the deployment.
codeDeployRollback : A rollback process created the deployment.


ignoreApplicationStopFailures (boolean) --If true, then if an ApplicationStop , BeforeBlockTraffic , or AfterBlockTraffic deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if ApplicationStop fails, the deployment continues with DownloadBundle. If BeforeBlockTraffic fails, the deployment continues with BlockTraffic . If AfterBlockTraffic fails, the deployment continues with ApplicationStop .
If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted.
During a deployment, the AWS CodeDeploy agent runs the scripts specified for ApplicationStop , BeforeBlockTraffic , and AfterBlockTraffic in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail.
If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use ignoreApplicationStopFailures to specify that the ApplicationStop , BeforeBlockTraffic , and AfterBlockTraffic failures should be ignored.

autoRollbackConfiguration (dict) --Information about the automatic rollback configuration associated with the deployment.

enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.

events (list) --The event type or types that trigger a rollback.

(string) --




updateOutdatedInstancesOnly (boolean) --Indicates whether only instances that are not running the latest application revision are to be deployed to.

rollbackInfo (dict) --Information about a deployment rollback.

rollbackDeploymentId (string) --The ID of the deployment rollback.

rollbackTriggeringDeploymentId (string) --The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.

rollbackMessage (string) --Information that describes the status of a deployment rollback (for example, whether the deployment can\'t be rolled back, is in progress, failed, or succeeded).



deploymentStyle (dict) --Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

deploymentType (string) --Indicates whether to run an in-place deployment or a blue/green deployment.

deploymentOption (string) --Indicates whether to route deployment traffic behind a load balancer.



targetInstances (dict) --Information about the instances that belong to the replacement environment in a blue/green deployment.

tagFilters (list) --The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as ec2TagSet .

(dict) --Information about an EC2 tag filter.

Key (string) --The tag filter key.

Value (string) --The tag filter value.

Type (string) --The tag filter type:

KEY_ONLY : Key only.
VALUE_ONLY : Value only.
KEY_AND_VALUE : Key and value.






autoScalingGroups (list) --The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.

(string) --


ec2TagSet (dict) --Information about the groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as tagFilters .

ec2TagSetList (list) --A list that contains other lists of EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

(list) --
(dict) --Information about an EC2 tag filter.

Key (string) --The tag filter key.

Value (string) --The tag filter value.

Type (string) --The tag filter type:

KEY_ONLY : Key only.
VALUE_ONLY : Value only.
KEY_AND_VALUE : Key and value.












instanceTerminationWaitTimeStarted (boolean) --Indicates whether the wait period set for the termination of instances in the original environment has started. Status is \'false\' if the KEEP_ALIVE option is specified. Otherwise, \'true\' as soon as the termination wait period starts.

blueGreenDeploymentConfiguration (dict) --Information about blue/green deployment options for this deployment.

terminateBlueInstancesOnDeploymentSuccess (dict) --Information about whether to terminate instances in the original fleet during a blue/green deployment.

action (string) --The action to take on instances in the original environment after a successful blue/green deployment.

TERMINATE : Instances are terminated after a specified wait time.
KEEP_ALIVE : Instances are left running after they are deregistered from the load balancer and removed from the deployment group.


terminationWaitTimeInMinutes (integer) --For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set.
The maximum setting is 2880 minutes (2 days).



deploymentReadyOption (dict) --Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

actionOnTimeout (string) --Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using  ContinueDeployment . If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.


waitTimeInMinutes (integer) --The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout .



greenFleetProvisioningOption (dict) --Information about how instances are provisioned for a replacement environment in a blue/green deployment.

action (string) --The method used to add instances to a replacement environment.

DISCOVER_EXISTING : Use instances that already exist or will be created manually.
COPY_AUTO_SCALING_GROUP : Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.






loadBalancerInfo (dict) --Information about the load balancer used in the deployment.

elbInfoList (list) --An array that contains information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

Note
Adding more than one load balancer to the array is not supported.


(dict) --Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

name (string) --For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





targetGroupInfoList (list) --An array that contains information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

Note
Adding more than one target group to the array is not supported.


(dict) --Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name (string) --For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





targetGroupPairInfoList (list) --The target group pair information. This is an array of TargeGroupPairInfo objects with a maximum size of one.

(dict) --Information about two target groups and how traffic is routed during an Amazon ECS deployment. An optional test traffic route can be specified.

targetGroups (list) --One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete.

(dict) --Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name (string) --For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





prodTrafficRoute (dict) --The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete.

listenerArns (list) --The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string) --




testTrafficRoute (dict) --An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment.

listenerArns (list) --The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string) --










additionalDeploymentStatusInfo (string) --Provides information about the results of a deployment, such as whether instances in the original environment in a blue/green deployment were not terminated.

fileExistsBehavior (string) --Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren\'t part of the previous successful deployment.

DISALLOW : The deployment fails. This is also the default behavior if no option is specified.
OVERWRITE : The version of the file from the application revision currently being deployed replaces the version already on the instance.
RETAIN : The version of the file already on the instance is kept and used as part of the new deployment.


deploymentStatusMessages (list) --Messages that contain information about the status of a deployment.

(string) --


computePlatform (string) --The destination platform type for the deployment (Lambda , Server , or ECS ).

externalId (string) --The unique ID for an external resource (for example, a CloudFormation stack ID) that is linked to this deployment.








Exceptions

CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.DeploymentDoesNotExistException


    :return: {
        'deploymentInfo': {
            'applicationName': 'string',
            'deploymentGroupName': 'string',
            'deploymentConfigName': 'string',
            'deploymentId': 'string',
            'previousRevision': {
                'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                },
                'appSpecContent': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
            'revision': {
                'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                },
                'appSpecContent': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
            'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
            'errorInformation': {
                'code': 'AGENT_ISSUE'|'ALARM_ACTIVE'|'APPLICATION_MISSING'|'AUTOSCALING_VALIDATION_ERROR'|'AUTO_SCALING_CONFIGURATION'|'AUTO_SCALING_IAM_ROLE_PERMISSIONS'|'CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND'|'CUSTOMER_APPLICATION_UNHEALTHY'|'DEPLOYMENT_GROUP_MISSING'|'ECS_UPDATE_ERROR'|'ELASTIC_LOAD_BALANCING_INVALID'|'ELB_INVALID_INSTANCE'|'HEALTH_CONSTRAINTS'|'HEALTH_CONSTRAINTS_INVALID'|'HOOK_EXECUTION_FAILURE'|'IAM_ROLE_MISSING'|'IAM_ROLE_PERMISSIONS'|'INTERNAL_ERROR'|'INVALID_ECS_SERVICE'|'INVALID_LAMBDA_CONFIGURATION'|'INVALID_LAMBDA_FUNCTION'|'INVALID_REVISION'|'MANUAL_STOP'|'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION'|'MISSING_ELB_INFORMATION'|'MISSING_GITHUB_TOKEN'|'NO_EC2_SUBSCRIPTION'|'NO_INSTANCES'|'OVER_MAX_INSTANCES'|'RESOURCE_LIMIT_EXCEEDED'|'REVISION_MISSING'|'THROTTLED'|'TIMEOUT'|'CLOUDFORMATION_STACK_FAILURE',
                'message': 'string'
            },
            'createTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'completeTime': datetime(2015, 1, 1),
            'deploymentOverview': {
                'Pending': 123,
                'InProgress': 123,
                'Succeeded': 123,
                'Failed': 123,
                'Skipped': 123,
                'Ready': 123
            },
            'description': 'string',
            'creator': 'user'|'autoscaling'|'codeDeployRollback'|'CodeDeploy'|'CloudFormation'|'CloudFormationRollback',
            'ignoreApplicationStopFailures': True|False,
            'autoRollbackConfiguration': {
                'enabled': True|False,
                'events': [
                    'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                ]
            },
            'updateOutdatedInstancesOnly': True|False,
            'rollbackInfo': {
                'rollbackDeploymentId': 'string',
                'rollbackTriggeringDeploymentId': 'string',
                'rollbackMessage': 'string'
            },
            'deploymentStyle': {
                'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
            },
            'targetInstances': {
                'tagFilters': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
                'autoScalingGroups': [
                    'string',
                ],
                'ec2TagSet': {
                    'ec2TagSetList': [
                        [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                    ]
                }
            },
            'instanceTerminationWaitTimeStarted': True|False,
            'blueGreenDeploymentConfiguration': {
                'terminateBlueInstancesOnDeploymentSuccess': {
                    'action': 'TERMINATE'|'KEEP_ALIVE',
                    'terminationWaitTimeInMinutes': 123
                },
                'deploymentReadyOption': {
                    'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                    'waitTimeInMinutes': 123
                },
                'greenFleetProvisioningOption': {
                    'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                }
            },
            'loadBalancerInfo': {
                'elbInfoList': [
                    {
                        'name': 'string'
                    },
                ],
                'targetGroupInfoList': [
                    {
                        'name': 'string'
                    },
                ],
                'targetGroupPairInfoList': [
                    {
                        'targetGroups': [
                            {
                                'name': 'string'
                            },
                        ],
                        'prodTrafficRoute': {
                            'listenerArns': [
                                'string',
                            ]
                        },
                        'testTrafficRoute': {
                            'listenerArns': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'additionalDeploymentStatusInfo': 'string',
            'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN',
            'deploymentStatusMessages': [
                'string',
            ],
            'computePlatform': 'Server'|'Lambda'|'ECS',
            'externalId': 'string'
        }
    }
    
    
    :returns: 
    tar : A tar archive file.
    tgz : A compressed tar archive file.
    zip : A zip archive file.
    
    """
    pass

def get_deployment_config(deploymentConfigName=None):
    """
    Gets information about a deployment configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployment_config(
        deploymentConfigName='string'
    )
    
    
    :type deploymentConfigName: string
    :param deploymentConfigName: [REQUIRED]\nThe name of a deployment configuration associated with the IAM user or AWS account.\n

    :rtype: dict
ReturnsResponse Syntax{
    'deploymentConfigInfo': {
        'deploymentConfigId': 'string',
        'deploymentConfigName': 'string',
        'minimumHealthyHosts': {
            'value': 123,
            'type': 'HOST_COUNT'|'FLEET_PERCENT'
        },
        'createTime': datetime(2015, 1, 1),
        'computePlatform': 'Server'|'Lambda'|'ECS',
        'trafficRoutingConfig': {
            'type': 'TimeBasedCanary'|'TimeBasedLinear'|'AllAtOnce',
            'timeBasedCanary': {
                'canaryPercentage': 123,
                'canaryInterval': 123
            },
            'timeBasedLinear': {
                'linearPercentage': 123,
                'linearInterval': 123
            }
        }
    }
}


Response Structure

(dict) --Represents the output of a GetDeploymentConfig operation.

deploymentConfigInfo (dict) --Information about the deployment configuration.

deploymentConfigId (string) --The deployment configuration ID.

deploymentConfigName (string) --The deployment configuration name.

minimumHealthyHosts (dict) --Information about the number or percentage of minimum healthy instance.

value (integer) --The minimum healthy instance value.

type (string) --The minimum healthy instance type:

HOST_COUNT : The minimum number of healthy instances as an absolute value.
FLEET_PERCENT : The minimum number of healthy instances as a percentage of the total number of instances in the deployment.

In an example of nine instances, if a HOST_COUNT of six is specified, deploy to up to three instances at a time. The deployment is successful if six or more instances are deployed to successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to five instances at a time. The deployment is successful if four or more instances are deployed to successfully. Otherwise, the deployment fails.

Note
In a call to the GetDeploymentConfig , CodeDeployDefault.OneAtATime returns a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment is still successful.

For more information, see AWS CodeDeploy Instance Health in the AWS CodeDeploy User Guide .



createTime (datetime) --The time at which the deployment configuration was created.

computePlatform (string) --The destination platform type for the deployment (Lambda , Server , or ECS ).

trafficRoutingConfig (dict) --The configuration that specifies how the deployment traffic is routed. Used for deployments with a Lambda or ECS compute platform only.

type (string) --The type of traffic shifting (TimeBasedCanary or TimeBasedLinear ) used by a deployment configuration.

timeBasedCanary (dict) --A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in two increments. The original and target Lambda function versions or ECS task sets are specified in the deployment\'s AppSpec file.

canaryPercentage (integer) --The percentage of traffic to shift in the first increment of a TimeBasedCanary deployment.

canaryInterval (integer) --The number of minutes between the first and second traffic shifts of a TimeBasedCanary deployment.



timeBasedLinear (dict) --A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions or ECS task sets are specified in the deployment\'s AppSpec file.

linearPercentage (integer) --The percentage of traffic that is shifted at the start of each increment of a TimeBasedLinear deployment.

linearInterval (integer) --The number of minutes between each incremental traffic shift of a TimeBasedLinear deployment.












Exceptions

CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
CodeDeploy.Client.exceptions.DeploymentConfigNameRequiredException
CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
CodeDeploy.Client.exceptions.InvalidComputePlatformException


    :return: {
        'deploymentConfigInfo': {
            'deploymentConfigId': 'string',
            'deploymentConfigName': 'string',
            'minimumHealthyHosts': {
                'value': 123,
                'type': 'HOST_COUNT'|'FLEET_PERCENT'
            },
            'createTime': datetime(2015, 1, 1),
            'computePlatform': 'Server'|'Lambda'|'ECS',
            'trafficRoutingConfig': {
                'type': 'TimeBasedCanary'|'TimeBasedLinear'|'AllAtOnce',
                'timeBasedCanary': {
                    'canaryPercentage': 123,
                    'canaryInterval': 123
                },
                'timeBasedLinear': {
                    'linearPercentage': 123,
                    'linearInterval': 123
                }
            }
        }
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
    CodeDeploy.Client.exceptions.DeploymentConfigNameRequiredException
    CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
    CodeDeploy.Client.exceptions.InvalidComputePlatformException
    
    """
    pass

def get_deployment_group(applicationName=None, deploymentGroupName=None):
    """
    Gets information about a deployment group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployment_group(
        applicationName='string',
        deploymentGroupName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n

    :type deploymentGroupName: string
    :param deploymentGroupName: [REQUIRED]\nThe name of a deployment group for the specified application.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'deploymentGroupInfo': {
        'applicationName': 'string',
        'deploymentGroupId': 'string',
        'deploymentGroupName': 'string',
        'deploymentConfigName': 'string',
        'ec2TagFilters': [
            {
                'Key': 'string',
                'Value': 'string',
                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
            },
        ],
        'onPremisesInstanceTagFilters': [
            {
                'Key': 'string',
                'Value': 'string',
                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
            },
        ],
        'autoScalingGroups': [
            {
                'name': 'string',
                'hook': 'string'
            },
        ],
        'serviceRoleArn': 'string',
        'targetRevision': {
            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            },
            'string': {
                'content': 'string',
                'sha256': 'string'
            },
            'appSpecContent': {
                'content': 'string',
                'sha256': 'string'
            }
        },
        'triggerConfigurations': [
            {
                'triggerName': 'string',
                'triggerTargetArn': 'string',
                'triggerEvents': [
                    'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                ]
            },
        ],
        'alarmConfiguration': {
            'enabled': True|False,
            'ignorePollAlarmFailure': True|False,
            'alarms': [
                {
                    'name': 'string'
                },
            ]
        },
        'autoRollbackConfiguration': {
            'enabled': True|False,
            'events': [
                'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
            ]
        },
        'deploymentStyle': {
            'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
            'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
        },
        'blueGreenDeploymentConfiguration': {
            'terminateBlueInstancesOnDeploymentSuccess': {
                'action': 'TERMINATE'|'KEEP_ALIVE',
                'terminationWaitTimeInMinutes': 123
            },
            'deploymentReadyOption': {
                'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                'waitTimeInMinutes': 123
            },
            'greenFleetProvisioningOption': {
                'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
            }
        },
        'loadBalancerInfo': {
            'elbInfoList': [
                {
                    'name': 'string'
                },
            ],
            'targetGroupInfoList': [
                {
                    'name': 'string'
                },
            ],
            'targetGroupPairInfoList': [
                {
                    'targetGroups': [
                        {
                            'name': 'string'
                        },
                    ],
                    'prodTrafficRoute': {
                        'listenerArns': [
                            'string',
                        ]
                    },
                    'testTrafficRoute': {
                        'listenerArns': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'lastSuccessfulDeployment': {
            'deploymentId': 'string',
            'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
            'endTime': datetime(2015, 1, 1),
            'createTime': datetime(2015, 1, 1)
        },
        'lastAttemptedDeployment': {
            'deploymentId': 'string',
            'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
            'endTime': datetime(2015, 1, 1),
            'createTime': datetime(2015, 1, 1)
        },
        'ec2TagSet': {
            'ec2TagSetList': [
                [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
            ]
        },
        'onPremisesTagSet': {
            'onPremisesTagSetList': [
                [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
            ]
        },
        'computePlatform': 'Server'|'Lambda'|'ECS',
        'ecsServices': [
            {
                'serviceName': 'string',
                'clusterName': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Represents the output of a GetDeploymentGroup operation.

deploymentGroupInfo (dict) --
Information about the deployment group.

applicationName (string) --
The application name.

deploymentGroupId (string) --
The deployment group ID.

deploymentGroupName (string) --
The deployment group name.

deploymentConfigName (string) --
The deployment configuration name.

ec2TagFilters (list) --
The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with any of the specified tags.

(dict) --
Information about an EC2 tag filter.

Key (string) --
The tag filter key.

Value (string) --
The tag filter value.

Type (string) --
The tag filter type:

KEY_ONLY : Key only.
VALUE_ONLY : Value only.
KEY_AND_VALUE : Key and value.






onPremisesInstanceTagFilters (list) --
The on-premises instance tags on which to filter. The deployment group includes on-premises instances with any of the specified tags.

(dict) --
Information about an on-premises instance tag filter.

Key (string) --
The on-premises instance tag filter key.

Value (string) --
The on-premises instance tag filter value.

Type (string) --
The on-premises instance tag filter type:

KEY_ONLY: Key only.
VALUE_ONLY: Value only.
KEY_AND_VALUE: Key and value.






autoScalingGroups (list) --
A list of associated Auto Scaling groups.

(dict) --
Information about an Auto Scaling group.

name (string) --
The Auto Scaling group name.

hook (string) --
An Auto Scaling lifecycle event hook name.





serviceRoleArn (string) --
A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls to AWS services on your behalf. For more information, see Create a Service Role for AWS CodeDeploy in the AWS CodeDeploy User Guide .

targetRevision (dict) --
Information about the deployment group\'s target revision, including type and location.

revisionType (string) --
The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location (dict) --
Information about the location of a revision stored in Amazon S3.

bucket (string) --
The name of the Amazon S3 bucket where the application revision is stored.

key (string) --
The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType (string) --
The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version (string) --
A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag (string) --
The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.



gitHubLocation (dict) --
Information about the location of application artifacts stored in GitHub.

repository (string) --
The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId (string) --
The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.



string (dict) --
Information about the location of an AWS Lambda deployment revision stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 (string) --
The SHA256 hash value of the revision content.



appSpecContent (dict) --
The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 (string) --
The SHA256 hash value of the revision content.





triggerConfigurations (list) --
Information about triggers associated with the deployment group.

(dict) --
Information about notification triggers for the deployment group.

triggerName (string) --
The name of the notification trigger.

triggerTargetArn (string) --
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.

triggerEvents (list) --
The event type or types for which notifications are triggered.

(string) --






alarmConfiguration (dict) --
A list of alarms associated with the deployment group.

enabled (boolean) --
Indicates whether the alarm configuration is enabled.

ignorePollAlarmFailure (boolean) --
Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

true : The deployment proceeds even if alarm status information can\'t be retrieved from Amazon CloudWatch.
false : The deployment stops if alarm status information can\'t be retrieved from Amazon CloudWatch.


alarms (list) --
A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.

(dict) --
Information about an alarm.

name (string) --
The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.







autoRollbackConfiguration (dict) --
Information about the automatic rollback configuration associated with the deployment group.

enabled (boolean) --
Indicates whether a defined automatic rollback configuration is currently enabled.

events (list) --
The event type or types that trigger a rollback.

(string) --




deploymentStyle (dict) --
Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

deploymentType (string) --
Indicates whether to run an in-place deployment or a blue/green deployment.

deploymentOption (string) --
Indicates whether to route deployment traffic behind a load balancer.



blueGreenDeploymentConfiguration (dict) --
Information about blue/green deployment options for a deployment group.

terminateBlueInstancesOnDeploymentSuccess (dict) --
Information about whether to terminate instances in the original fleet during a blue/green deployment.

action (string) --
The action to take on instances in the original environment after a successful blue/green deployment.

TERMINATE : Instances are terminated after a specified wait time.
KEEP_ALIVE : Instances are left running after they are deregistered from the load balancer and removed from the deployment group.


terminationWaitTimeInMinutes (integer) --
For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set.
The maximum setting is 2880 minutes (2 days).



deploymentReadyOption (dict) --
Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

actionOnTimeout (string) --
Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using  ContinueDeployment . If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.


waitTimeInMinutes (integer) --
The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout .



greenFleetProvisioningOption (dict) --
Information about how instances are provisioned for a replacement environment in a blue/green deployment.

action (string) --
The method used to add instances to a replacement environment.

DISCOVER_EXISTING : Use instances that already exist or will be created manually.
COPY_AUTO_SCALING_GROUP : Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.






loadBalancerInfo (dict) --
Information about the load balancer to use in a deployment.

elbInfoList (list) --
An array that contains information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.

Note
Adding more than one load balancer to the array is not supported.


(dict) --
Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.

name (string) --
For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





targetGroupInfoList (list) --
An array that contains information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.

Note
Adding more than one target group to the array is not supported.


(dict) --
Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name (string) --
For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





targetGroupPairInfoList (list) --
The target group pair information. This is an array of TargeGroupPairInfo objects with a maximum size of one.

(dict) --
Information about two target groups and how traffic is routed during an Amazon ECS deployment. An optional test traffic route can be specified.

targetGroups (list) --
One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete.

(dict) --
Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.

name (string) --
For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.





prodTrafficRoute (dict) --
The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete.

listenerArns (list) --
The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string) --




testTrafficRoute (dict) --
An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment.

listenerArns (list) --
The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.

(string) --










lastSuccessfulDeployment (dict) --
Information about the most recent successful deployment to the deployment group.

deploymentId (string) --
The unique ID of a deployment.

status (string) --
The status of the most recent deployment.

endTime (datetime) --
A timestamp that indicates when the most recent deployment to the deployment group was complete.

createTime (datetime) --
A timestamp that indicates when the most recent deployment to the deployment group started.



lastAttemptedDeployment (dict) --
Information about the most recent attempted deployment to the deployment group.

deploymentId (string) --
The unique ID of a deployment.

status (string) --
The status of the most recent deployment.

endTime (datetime) --
A timestamp that indicates when the most recent deployment to the deployment group was complete.

createTime (datetime) --
A timestamp that indicates when the most recent deployment to the deployment group started.



ec2TagSet (dict) --
Information about groups of tags applied to an EC2 instance. The deployment group includes only EC2 instances identified by all of the tag groups. Cannot be used in the same call as ec2TagFilters.

ec2TagSetList (list) --
A list that contains other lists of EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

(list) --

(dict) --
Information about an EC2 tag filter.

Key (string) --
The tag filter key.

Value (string) --
The tag filter value.

Type (string) --
The tag filter type:

KEY_ONLY : Key only.
VALUE_ONLY : Value only.
KEY_AND_VALUE : Key and value.










onPremisesTagSet (dict) --
Information about groups of tags applied to an on-premises instance. The deployment group includes only on-premises instances identified by all the tag groups. Cannot be used in the same call as onPremisesInstanceTagFilters.

onPremisesTagSetList (list) --
A list that contains other lists of on-premises instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

(list) --

(dict) --
Information about an on-premises instance tag filter.

Key (string) --
The on-premises instance tag filter key.

Value (string) --
The on-premises instance tag filter value.

Type (string) --
The on-premises instance tag filter type:

KEY_ONLY: Key only.
VALUE_ONLY: Value only.
KEY_AND_VALUE: Key and value.










computePlatform (string) --
The destination platform type for the deployment (Lambda , Server , or ECS ).

ecsServices (list) --
The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <clustername>:<servicename> .

(dict) --
Contains the service and cluster names used to identify an Amazon ECS deployment\'s target.

serviceName (string) --
The name of the target Amazon ECS service.

clusterName (string) --
The name of the cluster that the Amazon ECS service is associated with.













Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
CodeDeploy.Client.exceptions.DeploymentGroupDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException


    :return: {
        'deploymentGroupInfo': {
            'applicationName': 'string',
            'deploymentGroupId': 'string',
            'deploymentGroupName': 'string',
            'deploymentConfigName': 'string',
            'ec2TagFilters': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                },
            ],
            'onPremisesInstanceTagFilters': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                },
            ],
            'autoScalingGroups': [
                {
                    'name': 'string',
                    'hook': 'string'
                },
            ],
            'serviceRoleArn': 'string',
            'targetRevision': {
                'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                },
                'appSpecContent': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
            'triggerConfigurations': [
                {
                    'triggerName': 'string',
                    'triggerTargetArn': 'string',
                    'triggerEvents': [
                        'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                    ]
                },
            ],
            'alarmConfiguration': {
                'enabled': True|False,
                'ignorePollAlarmFailure': True|False,
                'alarms': [
                    {
                        'name': 'string'
                    },
                ]
            },
            'autoRollbackConfiguration': {
                'enabled': True|False,
                'events': [
                    'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                ]
            },
            'deploymentStyle': {
                'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
            },
            'blueGreenDeploymentConfiguration': {
                'terminateBlueInstancesOnDeploymentSuccess': {
                    'action': 'TERMINATE'|'KEEP_ALIVE',
                    'terminationWaitTimeInMinutes': 123
                },
                'deploymentReadyOption': {
                    'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                    'waitTimeInMinutes': 123
                },
                'greenFleetProvisioningOption': {
                    'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                }
            },
            'loadBalancerInfo': {
                'elbInfoList': [
                    {
                        'name': 'string'
                    },
                ],
                'targetGroupInfoList': [
                    {
                        'name': 'string'
                    },
                ],
                'targetGroupPairInfoList': [
                    {
                        'targetGroups': [
                            {
                                'name': 'string'
                            },
                        ],
                        'prodTrafficRoute': {
                            'listenerArns': [
                                'string',
                            ]
                        },
                        'testTrafficRoute': {
                            'listenerArns': [
                                'string',
                            ]
                        }
                    },
                ]
            },
            'lastSuccessfulDeployment': {
                'deploymentId': 'string',
                'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                'endTime': datetime(2015, 1, 1),
                'createTime': datetime(2015, 1, 1)
            },
            'lastAttemptedDeployment': {
                'deploymentId': 'string',
                'status': 'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                'endTime': datetime(2015, 1, 1),
                'createTime': datetime(2015, 1, 1)
            },
            'ec2TagSet': {
                'ec2TagSetList': [
                    [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                ]
            },
            'onPremisesTagSet': {
                'onPremisesTagSetList': [
                    [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                ]
            },
            'computePlatform': 'Server'|'Lambda'|'ECS',
            'ecsServices': [
                {
                    'serviceName': 'string',
                    'clusterName': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    KEY_ONLY : Key only.
    VALUE_ONLY : Value only.
    KEY_AND_VALUE : Key and value.
    
    """
    pass

def get_deployment_instance(deploymentId=None, instanceId=None):
    """
    Gets information about an instance as part of a deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployment_instance(
        deploymentId='string',
        instanceId='string'
    )
    
    
    :type deploymentId: string
    :param deploymentId: [REQUIRED]\nThe unique ID of a deployment.\n

    :type instanceId: string
    :param instanceId: [REQUIRED]\nThe unique ID of an instance in the deployment group.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'instanceSummary': {
        'deploymentId': 'string',
        'instanceId': 'string',
        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
        'lastUpdatedAt': datetime(2015, 1, 1),
        'lifecycleEvents': [
            {
                'lifecycleEventName': 'string',
                'diagnostics': {
                    'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                    'scriptName': 'string',
                    'message': 'string',
                    'logTail': 'string'
                },
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
            },
        ],
        'instanceType': 'Blue'|'Green'
    }
}


Response Structure

(dict) --
Represents the output of a GetDeploymentInstance operation.

instanceSummary (dict) --
Information about the instance.

deploymentId (string) --
The unique ID of a deployment.

instanceId (string) --
The instance ID.

status (string) --
The deployment status for this instance:

Pending : The deployment is pending for this instance.
In Progress : The deployment is in progress for this instance.
Succeeded : The deployment has succeeded for this instance.
Failed : The deployment has failed for this instance.
Skipped : The deployment has been skipped for this instance.
Unknown : The deployment status is unknown for this instance.


lastUpdatedAt (datetime) --
A timestamp that indicates when the instance information was last updated.

lifecycleEvents (list) --
A list of lifecycle events for this instance.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






instanceType (string) --
Information about which environment an instance belongs to in a blue/green deployment.

BLUE: The instance is part of the original environment.
GREEN: The instance is part of the replacement environment.










Exceptions

CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
CodeDeploy.Client.exceptions.InstanceIdRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.InstanceDoesNotExistException
CodeDeploy.Client.exceptions.InvalidInstanceNameException
CodeDeploy.Client.exceptions.InvalidComputePlatformException


    :return: {
        'instanceSummary': {
            'deploymentId': 'string',
            'instanceId': 'string',
            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'lifecycleEvents': [
                {
                    'lifecycleEventName': 'string',
                    'diagnostics': {
                        'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                        'scriptName': 'string',
                        'message': 'string',
                        'logTail': 'string'
                    },
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                },
            ],
            'instanceType': 'Blue'|'Green'
        }
    }
    
    
    :returns: 
    Pending : The deployment is pending for this instance.
    In Progress : The deployment is in progress for this instance.
    Succeeded : The deployment has succeeded for this instance.
    Failed : The deployment has failed for this instance.
    Skipped : The deployment has been skipped for this instance.
    Unknown : The deployment status is unknown for this instance.
    
    """
    pass

def get_deployment_target(deploymentId=None, targetId=None):
    """
    Returns information about a deployment target.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployment_target(
        deploymentId='string',
        targetId='string'
    )
    
    
    :type deploymentId: string
    :param deploymentId: The unique ID of a deployment.

    :type targetId: string
    :param targetId: The unique ID of a deployment target.

    :rtype: dict

ReturnsResponse Syntax
{
    'deploymentTarget': {
        'deploymentTargetType': 'InstanceTarget'|'LambdaTarget'|'ECSTarget'|'CloudFormationTarget',
        'instanceTarget': {
            'deploymentId': 'string',
            'targetId': 'string',
            'targetArn': 'string',
            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'lifecycleEvents': [
                {
                    'lifecycleEventName': 'string',
                    'diagnostics': {
                        'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                        'scriptName': 'string',
                        'message': 'string',
                        'logTail': 'string'
                    },
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                },
            ],
            'instanceLabel': 'Blue'|'Green'
        },
        'lambdaTarget': {
            'deploymentId': 'string',
            'targetId': 'string',
            'targetArn': 'string',
            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'lifecycleEvents': [
                {
                    'lifecycleEventName': 'string',
                    'diagnostics': {
                        'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                        'scriptName': 'string',
                        'message': 'string',
                        'logTail': 'string'
                    },
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                },
            ],
            'lambdaFunctionInfo': {
                'functionName': 'string',
                'functionAlias': 'string',
                'currentVersion': 'string',
                'targetVersion': 'string',
                'targetVersionWeight': 123.0
            }
        },
        'ecsTarget': {
            'deploymentId': 'string',
            'targetId': 'string',
            'targetArn': 'string',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'lifecycleEvents': [
                {
                    'lifecycleEventName': 'string',
                    'diagnostics': {
                        'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                        'scriptName': 'string',
                        'message': 'string',
                        'logTail': 'string'
                    },
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                },
            ],
            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
            'taskSetsInfo': [
                {
                    'identifer': 'string',
                    'desiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'status': 'string',
                    'trafficWeight': 123.0,
                    'targetGroup': {
                        'name': 'string'
                    },
                    'taskSetLabel': 'Blue'|'Green'
                },
            ]
        },
        'cloudFormationTarget': {
            'deploymentId': 'string',
            'targetId': 'string',
            'lastUpdatedAt': datetime(2015, 1, 1),
            'lifecycleEvents': [
                {
                    'lifecycleEventName': 'string',
                    'diagnostics': {
                        'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                        'scriptName': 'string',
                        'message': 'string',
                        'logTail': 'string'
                    },
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                },
            ],
            'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
            'resourceType': 'string',
            'targetVersionWeight': 123.0
        }
    }
}


Response Structure

(dict) --

deploymentTarget (dict) --
A deployment target that contains information about a deployment such as its status, lifecycle events, and when it was last updated. It also contains metadata about the deployment target. The deployment target metadata depends on the deployment target\'s type (instanceTarget , lambdaTarget , or ecsTarget ).

deploymentTargetType (string) --
The deployment type that is specific to the deployment\'s compute platform or deployments initiated by a CloudFormation stack update.

instanceTarget (dict) --
Information about the target for a deployment that uses the EC2/On-premises compute platform.

deploymentId (string) --
The unique ID of a deployment.

targetId (string) --
The unique ID of a deployment target that has a type of instanceTarget .

targetArn (string) --
The Amazon Resource Name (ARN) of the target.

status (string) --
The status an EC2/On-premises deployment\'s target instance.

lastUpdatedAt (datetime) --
The date and time when the target instance was updated by a deployment.

lifecycleEvents (list) --
The lifecycle events of the deployment to this target instance.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






instanceLabel (string) --
A label that identifies whether the instance is an original target (BLUE ) or a replacement target (GREEN ).



lambdaTarget (dict) --
Information about the target for a deployment that uses the AWS Lambda compute platform.

deploymentId (string) --
The unique ID of a deployment.

targetId (string) --
The unique ID of a deployment target that has a type of lambdaTarget .

targetArn (string) --
The Amazon Resource Name (ARN) of the target.

status (string) --
The status an AWS Lambda deployment\'s target Lambda function.

lastUpdatedAt (datetime) --
The date and time when the target Lambda function was updated by a deployment.

lifecycleEvents (list) --
The lifecycle events of the deployment to this target Lambda function.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






lambdaFunctionInfo (dict) --
A LambdaFunctionInfo object that describes a target Lambda function.

functionName (string) --
The name of a Lambda function.

functionAlias (string) --
The alias of a Lambda function. For more information, see AWS Lambda Function Aliases in the AWS Lambda Developer Guide .

currentVersion (string) --
The version of a Lambda function that production traffic points to.

targetVersion (string) --
The version of a Lambda function that production traffic points to after the Lambda function is deployed.

targetVersionWeight (float) --
The percentage of production traffic that the target version of a Lambda function receives.





ecsTarget (dict) --
Information about the target for a deployment that uses the Amazon ECS compute platform.

deploymentId (string) --
The unique ID of a deployment.

targetId (string) --
The unique ID of a deployment target that has a type of ecsTarget .

targetArn (string) --
The Amazon Resource Name (ARN) of the target.

lastUpdatedAt (datetime) --
The date and time when the target Amazon ECS application was updated by a deployment.

lifecycleEvents (list) --
The lifecycle events of the deployment to this target Amazon ECS application.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






status (string) --
The status an Amazon ECS deployment\'s target ECS application.

taskSetsInfo (list) --
The ECSTaskSet objects associated with the ECS target.

(dict) --
Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic. An AWS CodeDeploy application that uses the Amazon ECS compute platform deploys a containerized application in an Amazon ECS service as a task set.

identifer (string) --
A unique ID of an ECSTaskSet .

desiredCount (integer) --
The number of tasks in a task set. During a deployment that uses the Amazon ECS compute type, CodeDeploy instructs Amazon ECS to create a new task set and uses this value to determine how many tasks to create. After the updated task set is created, CodeDeploy shifts traffic to the new task set.

pendingCount (integer) --
The number of tasks in the task set that are in the PENDING status during an Amazon ECS deployment. A task in the PENDING state is preparing to enter the RUNNING state. A task set enters the PENDING status when it launches for the first time, or when it is restarted after being in the STOPPED state.

runningCount (integer) --
The number of tasks in the task set that are in the RUNNING status during an Amazon ECS deployment. A task in the RUNNING state is running and ready for use.

status (string) --
The status of the task set. There are three valid task set statuses:

PRIMARY : Indicates the task set is serving production traffic.
ACTIVE : Indicates the task set is not serving production traffic.
DRAINING : Indicates the tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.


trafficWeight (float) --
The percentage of traffic served by this task set.

targetGroup (dict) --
The target group associated with the task set. The target group is used by AWS CodeDeploy to manage traffic to a task set.

name (string) --
For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.



taskSetLabel (string) --
A label that identifies whether the ECS task set is an original target (BLUE ) or a replacement target (GREEN ).







cloudFormationTarget (dict) --
Information about the target to be updated by an AWS CloudFormation blue/green deployment. This target type is used for all deployments initiated by a CloudFormation stack update.

deploymentId (string) --
The unique ID of an AWS CloudFormation blue/green deployment.

targetId (string) --
The unique ID of a deployment target that has a type of CloudFormationTarget .

lastUpdatedAt (datetime) --
The date and time when the target application was updated by an AWS CloudFormation blue/green deployment.

lifecycleEvents (list) --
The lifecycle events of the AWS CloudFormation blue/green deployment to this target application.

(dict) --
Information about a deployment lifecycle event.

lifecycleEventName (string) --
The deployment lifecycle event name, such as ApplicationStop , BeforeInstall , AfterInstall , ApplicationStart , or ValidateService .

diagnostics (dict) --
Diagnostic information about the deployment lifecycle event.

errorCode (string) --
The associated error code:

Success: The specified script ran.
ScriptMissing: The specified script was not found in the specified location.
ScriptNotExecutable: The specified script is not a recognized executable file type.
ScriptTimedOut: The specified script did not finish running in the specified time period.
ScriptFailed: The specified script failed to run as expected.
UnknownError: The specified script did not run for an unknown reason.


scriptName (string) --
The name of the script.

message (string) --
The message associated with the error.

logTail (string) --
The last portion of the diagnostic log.
If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic log.



startTime (datetime) --
A timestamp that indicates when the deployment lifecycle event started.

endTime (datetime) --
A timestamp that indicates when the deployment lifecycle event ended.

status (string) --
The deployment lifecycle event status:

Pending: The deployment lifecycle event is pending.
InProgress: The deployment lifecycle event is in progress.
Succeeded: The deployment lifecycle event ran successfully.
Failed: The deployment lifecycle event has failed.
Skipped: The deployment lifecycle event has been skipped.
Unknown: The deployment lifecycle event is unknown.






status (string) --
The status of an AWS CloudFormation blue/green deployment\'s target application.

resourceType (string) --
The resource type for the AWS CloudFormation blue/green deployment.

targetVersionWeight (float) --
The percentage of production traffic that the target version of an AWS CloudFormation blue/green deployment receives.











Exceptions

CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentNotStartedException
CodeDeploy.Client.exceptions.DeploymentTargetIdRequiredException
CodeDeploy.Client.exceptions.InvalidDeploymentTargetIdException
CodeDeploy.Client.exceptions.DeploymentTargetDoesNotExistException
CodeDeploy.Client.exceptions.InvalidInstanceNameException


    :return: {
        'deploymentTarget': {
            'deploymentTargetType': 'InstanceTarget'|'LambdaTarget'|'ECSTarget'|'CloudFormationTarget',
            'instanceTarget': {
                'deploymentId': 'string',
                'targetId': 'string',
                'targetArn': 'string',
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'instanceLabel': 'Blue'|'Green'
            },
            'lambdaTarget': {
                'deploymentId': 'string',
                'targetId': 'string',
                'targetArn': 'string',
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'lambdaFunctionInfo': {
                    'functionName': 'string',
                    'functionAlias': 'string',
                    'currentVersion': 'string',
                    'targetVersion': 'string',
                    'targetVersionWeight': 123.0
                }
            },
            'ecsTarget': {
                'deploymentId': 'string',
                'targetId': 'string',
                'targetArn': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'taskSetsInfo': [
                    {
                        'identifer': 'string',
                        'desiredCount': 123,
                        'pendingCount': 123,
                        'runningCount': 123,
                        'status': 'string',
                        'trafficWeight': 123.0,
                        'targetGroup': {
                            'name': 'string'
                        },
                        'taskSetLabel': 'Blue'|'Green'
                    },
                ]
            },
            'cloudFormationTarget': {
                'deploymentId': 'string',
                'targetId': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'lifecycleEvents': [
                    {
                        'lifecycleEventName': 'string',
                        'diagnostics': {
                            'errorCode': 'Success'|'ScriptMissing'|'ScriptNotExecutable'|'ScriptTimedOut'|'ScriptFailed'|'UnknownError',
                            'scriptName': 'string',
                            'message': 'string',
                            'logTail': 'string'
                        },
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    },
                ],
                'status': 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
                'resourceType': 'string',
                'targetVersionWeight': 123.0
            }
        }
    }
    
    
    :returns: 
    Success: The specified script ran.
    ScriptMissing: The specified script was not found in the specified location.
    ScriptNotExecutable: The specified script is not a recognized executable file type.
    ScriptTimedOut: The specified script did not finish running in the specified time period.
    ScriptFailed: The specified script failed to run as expected.
    UnknownError: The specified script did not run for an unknown reason.
    
    """
    pass

def get_on_premises_instance(instanceName=None):
    """
    Gets information about an on-premises instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_on_premises_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the on-premises instance about which to get information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'instanceInfo': {
        'instanceName': 'string',
        'iamSessionArn': 'string',
        'iamUserArn': 'string',
        'instanceArn': 'string',
        'registerTime': datetime(2015, 1, 1),
        'deregisterTime': datetime(2015, 1, 1),
        'tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --Represents the output of a GetOnPremisesInstance operation.

instanceInfo (dict) --Information about the on-premises instance.

instanceName (string) --The name of the on-premises instance.

iamSessionArn (string) --The ARN of the IAM session associated with the on-premises instance.

iamUserArn (string) --The IAM user ARN associated with the on-premises instance.

instanceArn (string) --The ARN of the on-premises instance.

registerTime (datetime) --The time at which the on-premises instance was registered.

deregisterTime (datetime) --If the on-premises instance was deregistered, the time at which the on-premises instance was deregistered.

tags (list) --The tags currently associated with the on-premises instance.

(dict) --Information about a tag.

Key (string) --The tag\'s key.

Value (string) --The tag\'s value.












Exceptions

CodeDeploy.Client.exceptions.InstanceNameRequiredException
CodeDeploy.Client.exceptions.InstanceNotRegisteredException
CodeDeploy.Client.exceptions.InvalidInstanceNameException


    :return: {
        'instanceInfo': {
            'instanceName': 'string',
            'iamSessionArn': 'string',
            'iamUserArn': 'string',
            'instanceArn': 'string',
            'registerTime': datetime(2015, 1, 1),
            'deregisterTime': datetime(2015, 1, 1),
            'tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
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

def list_application_revisions(applicationName=None, sortBy=None, sortOrder=None, s3Bucket=None, s3KeyPrefix=None, deployed=None, nextToken=None):
    """
    Lists information about revisions for an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_application_revisions(
        applicationName='string',
        sortBy='registerTime'|'firstUsedTime'|'lastUsedTime',
        sortOrder='ascending'|'descending',
        s3Bucket='string',
        s3KeyPrefix='string',
        deployed='include'|'exclude'|'ignore',
        nextToken='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n

    :type sortBy: string
    :param sortBy: The column name to use to sort the list results:\n\nregisterTime : Sort by the time the revisions were registered with AWS CodeDeploy.\nfirstUsedTime : Sort by the time the revisions were first used in a deployment.\nlastUsedTime : Sort by the time the revisions were last used in a deployment.\n\nIf not specified or set to null, the results are returned in an arbitrary order.\n

    :type sortOrder: string
    :param sortOrder: The order in which to sort the list results:\n\nascending : ascending order.\ndescending : descending order.\n\nIf not specified, the results are sorted in ascending order.\nIf set to null, the results are sorted in an arbitrary order.\n

    :type s3Bucket: string
    :param s3Bucket: An Amazon S3 bucket name to limit the search for revisions.\nIf set to null, all of the user\'s buckets are searched.\n

    :type s3KeyPrefix: string
    :param s3KeyPrefix: A key prefix for the set of Amazon S3 objects to limit the search for revisions.

    :type deployed: string
    :param deployed: Whether to list revisions based on whether the revision is the target revision of a deployment group:\n\ninclude : List revisions that are target revisions of a deployment group.\nexclude : Do not list revisions that are target revisions of a deployment group.\nignore : List all revisions.\n\n

    :type nextToken: string
    :param nextToken: An identifier returned from the previous ListApplicationRevisions call. It can be used to return the next set of applications in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'revisions': [
        {
            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            },
            'string': {
                'content': 'string',
                'sha256': 'string'
            },
            'appSpecContent': {
                'content': 'string',
                'sha256': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the output of a ListApplicationRevisions operation.

revisions (list) --
A list of locations that contain the matching revisions.

(dict) --
Information about the location of an application revision.

revisionType (string) --
The type of application revision:

S3: An application revision stored in Amazon S3.
GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.


s3Location (dict) --
Information about the location of a revision stored in Amazon S3.

bucket (string) --
The name of the Amazon S3 bucket where the application revision is stored.

key (string) --
The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType (string) --
The file type of the application revision. Must be one of the following:

tar : A tar archive file.
tgz : A compressed tar archive file.
zip : A zip archive file.


version (string) --
A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.

eTag (string) --
The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.



gitHubLocation (dict) --
Information about the location of application artifacts stored in GitHub.

repository (string) --
The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
Specified as account/repository.

commitId (string) --
The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.



string (dict) --
Information about the location of an AWS Lambda deployment revision stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 (string) --
The SHA256 hash value of the revision content.



appSpecContent (dict) --
The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content (string) --
The YAML-formatted or JSON-formatted revision string.
For an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.
For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.
For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.

sha256 (string) --
The SHA256 hash value of the revision content.







nextToken (string) --
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list application revisions call to return the next set of application revisions in the list.







Exceptions

CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.InvalidSortByException
CodeDeploy.Client.exceptions.InvalidSortOrderException
CodeDeploy.Client.exceptions.InvalidBucketNameFilterException
CodeDeploy.Client.exceptions.InvalidKeyPrefixFilterException
CodeDeploy.Client.exceptions.BucketNameFilterRequiredException
CodeDeploy.Client.exceptions.InvalidDeployedStateFilterException
CodeDeploy.Client.exceptions.InvalidNextTokenException


    :return: {
        'revisions': [
            {
                'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                },
                'string': {
                    'content': 'string',
                    'sha256': 'string'
                },
                'appSpecContent': {
                    'content': 'string',
                    'sha256': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    S3: An application revision stored in Amazon S3.
    GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
    String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
    AppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.
    
    """
    pass

def list_applications(nextToken=None):
    """
    Lists the applications registered with the IAM user or AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_applications(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier returned from the previous list applications call. It can be used to return the next set of applications in the list.

    :rtype: dict
ReturnsResponse Syntax{
    'applications': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --Represents the output of a ListApplications operation.

applications (list) --A list of application names.

(string) --


nextToken (string) --If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list applications call to return the next set of applications in the list.






Exceptions

CodeDeploy.Client.exceptions.InvalidNextTokenException


    :return: {
        'applications': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def list_deployment_configs(nextToken=None):
    """
    Lists the deployment configurations with the IAM user or AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_deployment_configs(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier returned from the previous ListDeploymentConfigs call. It can be used to return the next set of deployment configurations in the list.

    :rtype: dict
ReturnsResponse Syntax{
    'deploymentConfigsList': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --Represents the output of a ListDeploymentConfigs operation.

deploymentConfigsList (list) --A list of deployment configurations, including built-in configurations such as CodeDeployDefault.OneAtATime .

(string) --


nextToken (string) --If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment configurations call to return the next set of deployment configurations in the list.






Exceptions

CodeDeploy.Client.exceptions.InvalidNextTokenException


    :return: {
        'deploymentConfigsList': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def list_deployment_groups(applicationName=None, nextToken=None):
    """
    Lists the deployment groups for an application registered with the IAM user or AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_deployment_groups(
        applicationName='string',
        nextToken='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n

    :type nextToken: string
    :param nextToken: An identifier returned from the previous list deployment groups call. It can be used to return the next set of deployment groups in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'applicationName': 'string',
    'deploymentGroups': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the output of a ListDeploymentGroups operation.

applicationName (string) --
The application name.

deploymentGroups (list) --
A list of deployment group names.

(string) --


nextToken (string) --
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment groups call to return the next set of deployment groups in the list.







Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.InvalidNextTokenException


    :return: {
        'applicationName': 'string',
        'deploymentGroups': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_deployment_instances(deploymentId=None, nextToken=None, instanceStatusFilter=None, instanceTypeFilter=None):
    """
    Lists the instance for a deployment associated with the IAM user or AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_deployment_instances(
        deploymentId='string',
        nextToken='string',
        instanceStatusFilter=[
            'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
        ],
        instanceTypeFilter=[
            'Blue'|'Green',
        ]
    )
    
    
    :type deploymentId: string
    :param deploymentId: [REQUIRED]\nThe unique ID of a deployment.\n

    :type nextToken: string
    :param nextToken: An identifier returned from the previous list deployment instances call. It can be used to return the next set of deployment instances in the list.

    :type instanceStatusFilter: list
    :param instanceStatusFilter: A subset of instances to list by status:\n\nPending : Include those instances with pending deployments.\nInProgress : Include those instances where deployments are still in progress.\nSucceeded : Include those instances with successful deployments.\nFailed : Include those instances with failed deployments.\nSkipped : Include those instances with skipped deployments.\nUnknown : Include those instances with deployments in an unknown state.\n\n\n(string) --\n\n

    :type instanceTypeFilter: list
    :param instanceTypeFilter: The set of instances in a blue/green deployment, either those in the original environment ('BLUE') or those in the replacement environment ('GREEN'), for which you want to view instance information.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'instancesList': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the output of a ListDeploymentInstances operation.

instancesList (list) --
A list of instance IDs.

(string) --


nextToken (string) --
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment instances call to return the next set of deployment instances in the list.







Exceptions

CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentNotStartedException
CodeDeploy.Client.exceptions.InvalidNextTokenException
CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.InvalidInstanceStatusException
CodeDeploy.Client.exceptions.InvalidInstanceTypeException
CodeDeploy.Client.exceptions.InvalidDeploymentInstanceTypeException
CodeDeploy.Client.exceptions.InvalidTargetFilterNameException
CodeDeploy.Client.exceptions.InvalidComputePlatformException


    :return: {
        'instancesList': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_deployment_targets(deploymentId=None, nextToken=None, targetFilters=None):
    """
    Returns an array of target IDs that are associated a deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_deployment_targets(
        deploymentId='string',
        nextToken='string',
        targetFilters={
            'string': [
                'string',
            ]
        }
    )
    
    
    :type deploymentId: string
    :param deploymentId: The unique ID of a deployment.

    :type nextToken: string
    :param nextToken: A token identifier returned from the previous ListDeploymentTargets call. It can be used to return the next set of deployment targets in the list.

    :type targetFilters: dict
    :param targetFilters: A key used to filter the returned targets. The two valid values are:\n\nTargetStatus - A TargetStatus filter string can be Failed , InProgress , Pending , Ready , Skipped , Succeeded , or Unknown .\nServerInstanceLabel - A ServerInstanceLabel filter string can be Blue or Green .\n\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'targetIds': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

targetIds (list) --
The unique IDs of deployment targets.

(string) --


nextToken (string) --
If a large amount of information is returned, a token identifier is also returned. It can be used in a subsequent ListDeploymentTargets call to return the next set of deployment targets in the list.







Exceptions

CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentNotStartedException
CodeDeploy.Client.exceptions.InvalidNextTokenException
CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.InvalidInstanceStatusException
CodeDeploy.Client.exceptions.InvalidInstanceTypeException
CodeDeploy.Client.exceptions.InvalidDeploymentInstanceTypeException


    :return: {
        'targetIds': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_deployments(applicationName=None, deploymentGroupName=None, externalId=None, includeOnlyStatuses=None, createTimeRange=None, nextToken=None):
    """
    Lists the deployments in a deployment group for an application registered with the IAM user or AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_deployments(
        applicationName='string',
        deploymentGroupName='string',
        externalId='string',
        includeOnlyStatuses=[
            'Created'|'Queued'|'InProgress'|'Baking'|'Succeeded'|'Failed'|'Stopped'|'Ready',
        ],
        createTimeRange={
            'start': datetime(2015, 1, 1),
            'end': datetime(2015, 1, 1)
        },
        nextToken='string'
    )
    
    
    :type applicationName: string
    :param applicationName: The name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n\nNote\nIf applicationName is specified, then deploymentGroupName must be specified. If it is not specified, then deploymentGroupName must not be specified.\n\n

    :type deploymentGroupName: string
    :param deploymentGroupName: The name of a deployment group for the specified application.\n\nNote\nIf deploymentGroupName is specified, then applicationName must be specified. If it is not specified, then applicationName must not be specified.\n\n

    :type externalId: string
    :param externalId: The unique ID of an external resource for returning deployments linked to the external resource.

    :type includeOnlyStatuses: list
    :param includeOnlyStatuses: A subset of deployments to list by status:\n\nCreated : Include created deployments in the resulting list.\nQueued : Include queued deployments in the resulting list.\nIn Progress : Include in-progress deployments in the resulting list.\nSucceeded : Include successful deployments in the resulting list.\nFailed : Include failed deployments in the resulting list.\nStopped : Include stopped deployments in the resulting list.\n\n\n(string) --\n\n

    :type createTimeRange: dict
    :param createTimeRange: A time range (start and end) for returning a subset of the list of deployments.\n\nstart (datetime) --The start time of the time range.\n\nNote\nSpecify null to leave the start time open-ended.\n\n\nend (datetime) --The end time of the time range.\n\nNote\nSpecify null to leave the end time open-ended.\n\n\n\n

    :type nextToken: string
    :param nextToken: An identifier returned from the previous list deployments call. It can be used to return the next set of deployments in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'deployments': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the output of a ListDeployments operation.

deployments (list) --
A list of deployment IDs.

(string) --


nextToken (string) --
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployments call to return the next set of deployments in the list.







Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
CodeDeploy.Client.exceptions.DeploymentGroupDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
CodeDeploy.Client.exceptions.InvalidTimeRangeException
CodeDeploy.Client.exceptions.InvalidDeploymentStatusException
CodeDeploy.Client.exceptions.InvalidNextTokenException
CodeDeploy.Client.exceptions.InvalidExternalIdException
CodeDeploy.Client.exceptions.InvalidInputException


    :return: {
        'deployments': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_git_hub_account_token_names(nextToken=None):
    """
    Lists the names of stored connections to GitHub accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_git_hub_account_token_names(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier returned from the previous ListGitHubAccountTokenNames call. It can be used to return the next set of names in the list.

    :rtype: dict
ReturnsResponse Syntax{
    'tokenNameList': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --Represents the output of a ListGitHubAccountTokenNames operation.

tokenNameList (list) --A list of names of connections to GitHub accounts.

(string) --


nextToken (string) --If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent ListGitHubAccountTokenNames call to return the next set of names in the list.






Exceptions

CodeDeploy.Client.exceptions.InvalidNextTokenException
CodeDeploy.Client.exceptions.ResourceValidationException
CodeDeploy.Client.exceptions.OperationNotSupportedException


    :return: {
        'tokenNameList': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.InvalidNextTokenException
    CodeDeploy.Client.exceptions.ResourceValidationException
    CodeDeploy.Client.exceptions.OperationNotSupportedException
    
    """
    pass

def list_on_premises_instances(registrationStatus=None, tagFilters=None, nextToken=None):
    """
    Gets a list of names for one or more on-premises instances.
    Unless otherwise specified, both registered and deregistered on-premises instance names are listed. To list only registered or deregistered on-premises instance names, use the registration status parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_on_premises_instances(
        registrationStatus='Registered'|'Deregistered',
        tagFilters=[
            {
                'Key': 'string',
                'Value': 'string',
                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
            },
        ],
        nextToken='string'
    )
    
    
    :type registrationStatus: string
    :param registrationStatus: The registration status of the on-premises instances:\n\nDeregistered : Include deregistered on-premises instances in the resulting list.\nRegistered : Include registered on-premises instances in the resulting list.\n\n

    :type tagFilters: list
    :param tagFilters: The on-premises instance tags that are used to restrict the on-premises instance names returned.\n\n(dict) --Information about an on-premises instance tag filter.\n\nKey (string) --The on-premises instance tag filter key.\n\nValue (string) --The on-premises instance tag filter value.\n\nType (string) --The on-premises instance tag filter type:\n\nKEY_ONLY: Key only.\nVALUE_ONLY: Value only.\nKEY_AND_VALUE: Key and value.\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: An identifier returned from the previous list on-premises instances call. It can be used to return the next set of on-premises instances in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'instanceNames': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the output of the list on-premises instances operation.

instanceNames (list) --
The list of matching on-premises instance names.

(string) --


nextToken (string) --
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list on-premises instances call to return the next set of on-premises instances in the list.







Exceptions

CodeDeploy.Client.exceptions.InvalidRegistrationStatusException
CodeDeploy.Client.exceptions.InvalidTagFilterException
CodeDeploy.Client.exceptions.InvalidNextTokenException


    :return: {
        'instanceNames': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(ResourceArn=None, NextToken=None):
    """
    Returns a list of tags for the resource identified by a specified Amazon Resource Name (ARN). Tags are used to organize and categorize your CodeDeploy resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string',
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of a CodeDeploy resource. ListTagsForResource returns all the tags associated with the resource that is identified by the ResourceArn .\n

    :type NextToken: string
    :param NextToken: An identifier returned from the previous ListTagsForResource call. It can be used to return the next set of applications in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
A list of tags returned by ListTagsForResource . The tags are associated with the resource identified by the input ResourceArn parameter.

(dict) --
Information about a tag.

Key (string) --
The tag\'s key.

Value (string) --
The tag\'s value.





NextToken (string) --
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list application revisions call to return the next set of application revisions in the list.







Exceptions

CodeDeploy.Client.exceptions.ArnNotSupportedException
CodeDeploy.Client.exceptions.InvalidArnException
CodeDeploy.Client.exceptions.ResourceArnRequiredException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.ArnNotSupportedException
    CodeDeploy.Client.exceptions.InvalidArnException
    CodeDeploy.Client.exceptions.ResourceArnRequiredException
    
    """
    pass

def put_lifecycle_event_hook_execution_status(deploymentId=None, lifecycleEventHookExecutionId=None, status=None):
    """
    Sets the result of a Lambda validation function. The function validates lifecycle hooks during a deployment that uses the AWS Lambda or Amazon ECS compute platform. For AWS Lambda deployments, the available lifecycle hooks are BeforeAllowTraffic and AfterAllowTraffic . For Amazon ECS deployments, the available lifecycle hooks are BeforeInstall , AfterInstall , AfterAllowTestTraffic , BeforeAllowTraffic , and AfterAllowTraffic . Lambda validation functions return Succeeded or Failed . For more information, see AppSpec \'hooks\' Section for an AWS Lambda Deployment and AppSpec \'hooks\' Section for an Amazon ECS Deployment .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_lifecycle_event_hook_execution_status(
        deploymentId='string',
        lifecycleEventHookExecutionId='string',
        status='Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
    )
    
    
    :type deploymentId: string
    :param deploymentId: The unique ID of a deployment. Pass this ID to a Lambda function that validates a deployment lifecycle event.

    :type lifecycleEventHookExecutionId: string
    :param lifecycleEventHookExecutionId: The execution ID of a deployment\'s lifecycle hook. A deployment lifecycle hook is specified in the hooks section of the AppSpec file.

    :type status: string
    :param status: The result of a Lambda function that validates a deployment lifecycle event (Succeeded or Failed ).

    :rtype: dict

ReturnsResponse Syntax
{
    'lifecycleEventHookExecutionId': 'string'
}


Response Structure

(dict) --

lifecycleEventHookExecutionId (string) --
The execution ID of the lifecycle event hook. A hook is specified in the hooks section of the deployment\'s AppSpec file.







Exceptions

CodeDeploy.Client.exceptions.InvalidLifecycleEventHookExecutionStatusException
CodeDeploy.Client.exceptions.InvalidLifecycleEventHookExecutionIdException
CodeDeploy.Client.exceptions.LifecycleEventAlreadyCompletedException
CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.UnsupportedActionForDeploymentTypeException


    :return: {
        'lifecycleEventHookExecutionId': 'string'
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.InvalidLifecycleEventHookExecutionStatusException
    CodeDeploy.Client.exceptions.InvalidLifecycleEventHookExecutionIdException
    CodeDeploy.Client.exceptions.LifecycleEventAlreadyCompletedException
    CodeDeploy.Client.exceptions.DeploymentIdRequiredException
    CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
    CodeDeploy.Client.exceptions.InvalidDeploymentIdException
    CodeDeploy.Client.exceptions.UnsupportedActionForDeploymentTypeException
    
    """
    pass

def register_application_revision(applicationName=None, description=None, revision=None):
    """
    Registers with AWS CodeDeploy a revision for the specified application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_application_revision(
        applicationName='string',
        description='string',
        revision={
            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            },
            'string': {
                'content': 'string',
                'sha256': 'string'
            },
            'appSpecContent': {
                'content': 'string',
                'sha256': 'string'
            }
        }
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe name of an AWS CodeDeploy application associated with the IAM user or AWS account.\n

    :type description: string
    :param description: A comment about the revision.

    :type revision: dict
    :param revision: [REQUIRED]\nInformation about the application revision to register, including type and location.\n\nrevisionType (string) --The type of application revision:\n\nS3: An application revision stored in Amazon S3.\nGitHub: An application revision stored in GitHub (EC2/On-premises deployments only).\nString: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).\nAppSpecContent: An AppSpecContent object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.\n\n\ns3Location (dict) --Information about the location of a revision stored in Amazon S3.\n\nbucket (string) --The name of the Amazon S3 bucket where the application revision is stored.\n\nkey (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.\n\nbundleType (string) --The file type of the application revision. Must be one of the following:\n\ntar : A tar archive file.\ntgz : A compressed tar archive file.\nzip : A zip archive file.\n\n\nversion (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.\nIf the version is not specified, the system uses the most recent version by default.\n\neTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.\nIf the ETag is not specified as an input parameter, ETag validation of the object is skipped.\n\n\n\ngitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.\n\nrepository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.\nSpecified as account/repository.\n\ncommitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.\n\n\n\nstring (dict) --Information about the location of an AWS Lambda deployment revision stored as a RawString.\n\ncontent (string) --The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.\n\nsha256 (string) --The SHA256 hash value of the revision content.\n\n\n\nappSpecContent (dict) --The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.\n\ncontent (string) --The YAML-formatted or JSON-formatted revision string.\nFor an AWS Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.\nFor an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.\nFor both types of deployments, the content can specify Lambda functions that run at specified hooks, such as BeforeInstall , during a deployment.\n\nsha256 (string) --The SHA256 hash value of the revision content.\n\n\n\n\n

    :returns: 
    CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
    CodeDeploy.Client.exceptions.ApplicationNameRequiredException
    CodeDeploy.Client.exceptions.InvalidApplicationNameException
    CodeDeploy.Client.exceptions.DescriptionTooLongException
    CodeDeploy.Client.exceptions.RevisionRequiredException
    CodeDeploy.Client.exceptions.InvalidRevisionException
    
    """
    pass

def register_on_premises_instance(instanceName=None, iamSessionArn=None, iamUserArn=None):
    """
    Registers an on-premises instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_on_premises_instance(
        instanceName='string',
        iamSessionArn='string',
        iamUserArn='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the on-premises instance to register.\n

    :type iamSessionArn: string
    :param iamSessionArn: The ARN of the IAM session to associate with the on-premises instance.

    :type iamUserArn: string
    :param iamUserArn: The ARN of the IAM user to associate with the on-premises instance.

    :returns: 
    CodeDeploy.Client.exceptions.InstanceNameAlreadyRegisteredException
    CodeDeploy.Client.exceptions.IamArnRequiredException
    CodeDeploy.Client.exceptions.IamSessionArnAlreadyRegisteredException
    CodeDeploy.Client.exceptions.IamUserArnAlreadyRegisteredException
    CodeDeploy.Client.exceptions.InstanceNameRequiredException
    CodeDeploy.Client.exceptions.IamUserArnRequiredException
    CodeDeploy.Client.exceptions.InvalidInstanceNameException
    CodeDeploy.Client.exceptions.InvalidIamSessionArnException
    CodeDeploy.Client.exceptions.InvalidIamUserArnException
    CodeDeploy.Client.exceptions.MultipleIamArnsProvidedException
    
    """
    pass

def remove_tags_from_on_premises_instances(tags=None, instanceNames=None):
    """
    Removes one or more tags from one or more on-premises instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_tags_from_on_premises_instances(
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        instanceNames=[
            'string',
        ]
    )
    
    
    :type tags: list
    :param tags: [REQUIRED]\nThe tag key-value pairs to remove from the on-premises instances.\n\n(dict) --Information about a tag.\n\nKey (string) --The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :type instanceNames: list
    :param instanceNames: [REQUIRED]\nThe names of the on-premises instances from which to remove tags.\n\n(string) --\n\n

    :returns: 
    CodeDeploy.Client.exceptions.InstanceNameRequiredException
    CodeDeploy.Client.exceptions.InvalidInstanceNameException
    CodeDeploy.Client.exceptions.TagRequiredException
    CodeDeploy.Client.exceptions.InvalidTagException
    CodeDeploy.Client.exceptions.TagLimitExceededException
    CodeDeploy.Client.exceptions.InstanceLimitExceededException
    CodeDeploy.Client.exceptions.InstanceNotRegisteredException
    
    """
    pass

def skip_wait_time_for_instance_termination(deploymentId=None):
    """
    In a blue/green deployment, overrides any specified wait time and starts terminating instances immediately after the traffic routing is complete.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.skip_wait_time_for_instance_termination(
        deploymentId='string'
    )
    
    
    :type deploymentId: string
    :param deploymentId: The unique ID of a blue/green deployment for which you want to skip the instance termination wait time.

    """
    pass

def stop_deployment(deploymentId=None, autoRollbackEnabled=None):
    """
    Attempts to stop an ongoing deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_deployment(
        deploymentId='string',
        autoRollbackEnabled=True|False
    )
    
    
    :type deploymentId: string
    :param deploymentId: [REQUIRED]\nThe unique ID of a deployment.\n

    :type autoRollbackEnabled: boolean
    :param autoRollbackEnabled: Indicates, when a deployment is stopped, whether instances that have been updated should be rolled back to the previous version of the application revision.

    :rtype: dict

ReturnsResponse Syntax
{
    'status': 'Pending'|'Succeeded',
    'statusMessage': 'string'
}


Response Structure

(dict) --
Represents the output of a StopDeployment operation.

status (string) --
The status of the stop deployment operation:

Pending: The stop operation is pending.
Succeeded: The stop operation was successful.


statusMessage (string) --
An accompanying status message.







Exceptions

CodeDeploy.Client.exceptions.DeploymentIdRequiredException
CodeDeploy.Client.exceptions.DeploymentDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentGroupDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentAlreadyCompletedException
CodeDeploy.Client.exceptions.InvalidDeploymentIdException
CodeDeploy.Client.exceptions.UnsupportedActionForDeploymentTypeException


    :return: {
        'status': 'Pending'|'Succeeded',
        'statusMessage': 'string'
    }
    
    
    :returns: 
    Pending: The stop operation is pending.
    Succeeded: The stop operation was successful.
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Associates the list of tags in the input Tags parameter with the resource identified by the ResourceArn input parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of a resource, such as a CodeDeploy application or deployment group.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA list of tags that TagResource associates with a resource. The resource is identified by the ResourceArn input parameter.\n\n(dict) --Information about a tag.\n\nKey (string) --The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeDeploy.Client.exceptions.ResourceArnRequiredException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentGroupDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
CodeDeploy.Client.exceptions.TagRequiredException
CodeDeploy.Client.exceptions.InvalidTagsToAddException
CodeDeploy.Client.exceptions.ArnNotSupportedException
CodeDeploy.Client.exceptions.InvalidArnException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Disassociates a resource from a list of tags. The resource is identified by the ResourceArn input parameter. The tags are identified by the list of keys in the TagKeys input parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that specifies from which resource to disassociate the tags with the keys in the TagKeys input parameter.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of keys of Tag objects. The Tag objects identified by the keys are disassociated from the resource specified by the ResourceArn input parameter.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeDeploy.Client.exceptions.ResourceArnRequiredException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentGroupDoesNotExistException
CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
CodeDeploy.Client.exceptions.TagRequiredException
CodeDeploy.Client.exceptions.InvalidTagsToAddException
CodeDeploy.Client.exceptions.ArnNotSupportedException
CodeDeploy.Client.exceptions.InvalidArnException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_application(applicationName=None, newApplicationName=None):
    """
    Changes the name of an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_application(
        applicationName='string',
        newApplicationName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: The current name of the application you want to change.

    :type newApplicationName: string
    :param newApplicationName: The new name to give the application.

    :returns: 
    CodeDeploy.Client.exceptions.ApplicationNameRequiredException
    CodeDeploy.Client.exceptions.InvalidApplicationNameException
    CodeDeploy.Client.exceptions.ApplicationAlreadyExistsException
    CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
    
    """
    pass

def update_deployment_group(applicationName=None, currentDeploymentGroupName=None, newDeploymentGroupName=None, deploymentConfigName=None, ec2TagFilters=None, onPremisesInstanceTagFilters=None, autoScalingGroups=None, serviceRoleArn=None, triggerConfigurations=None, alarmConfiguration=None, autoRollbackConfiguration=None, deploymentStyle=None, blueGreenDeploymentConfiguration=None, loadBalancerInfo=None, ec2TagSet=None, ecsServices=None, onPremisesTagSet=None):
    """
    Changes information about a deployment group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_deployment_group(
        applicationName='string',
        currentDeploymentGroupName='string',
        newDeploymentGroupName='string',
        deploymentConfigName='string',
        ec2TagFilters=[
            {
                'Key': 'string',
                'Value': 'string',
                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
            },
        ],
        onPremisesInstanceTagFilters=[
            {
                'Key': 'string',
                'Value': 'string',
                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
            },
        ],
        autoScalingGroups=[
            'string',
        ],
        serviceRoleArn='string',
        triggerConfigurations=[
            {
                'triggerName': 'string',
                'triggerTargetArn': 'string',
                'triggerEvents': [
                    'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'|'InstanceFailure'|'InstanceReady',
                ]
            },
        ],
        alarmConfiguration={
            'enabled': True|False,
            'ignorePollAlarmFailure': True|False,
            'alarms': [
                {
                    'name': 'string'
                },
            ]
        },
        autoRollbackConfiguration={
            'enabled': True|False,
            'events': [
                'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
            ]
        },
        deploymentStyle={
            'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
            'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
        },
        blueGreenDeploymentConfiguration={
            'terminateBlueInstancesOnDeploymentSuccess': {
                'action': 'TERMINATE'|'KEEP_ALIVE',
                'terminationWaitTimeInMinutes': 123
            },
            'deploymentReadyOption': {
                'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                'waitTimeInMinutes': 123
            },
            'greenFleetProvisioningOption': {
                'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
            }
        },
        loadBalancerInfo={
            'elbInfoList': [
                {
                    'name': 'string'
                },
            ],
            'targetGroupInfoList': [
                {
                    'name': 'string'
                },
            ],
            'targetGroupPairInfoList': [
                {
                    'targetGroups': [
                        {
                            'name': 'string'
                        },
                    ],
                    'prodTrafficRoute': {
                        'listenerArns': [
                            'string',
                        ]
                    },
                    'testTrafficRoute': {
                        'listenerArns': [
                            'string',
                        ]
                    }
                },
            ]
        },
        ec2TagSet={
            'ec2TagSetList': [
                [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
            ]
        },
        ecsServices=[
            {
                'serviceName': 'string',
                'clusterName': 'string'
            },
        ],
        onPremisesTagSet={
            'onPremisesTagSetList': [
                [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                    },
                ],
            ]
        }
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]\nThe application name that corresponds to the deployment group to update.\n

    :type currentDeploymentGroupName: string
    :param currentDeploymentGroupName: [REQUIRED]\nThe current name of the deployment group.\n

    :type newDeploymentGroupName: string
    :param newDeploymentGroupName: The new name of the deployment group, if you want to change it.

    :type deploymentConfigName: string
    :param deploymentConfigName: The replacement deployment configuration name to use, if you want to change it.

    :type ec2TagFilters: list
    :param ec2TagFilters: The replacement set of Amazon EC2 tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.\n\n(dict) --Information about an EC2 tag filter.\n\nKey (string) --The tag filter key.\n\nValue (string) --The tag filter value.\n\nType (string) --The tag filter type:\n\nKEY_ONLY : Key only.\nVALUE_ONLY : Value only.\nKEY_AND_VALUE : Key and value.\n\n\n\n\n\n

    :type onPremisesInstanceTagFilters: list
    :param onPremisesInstanceTagFilters: The replacement set of on-premises instance tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.\n\n(dict) --Information about an on-premises instance tag filter.\n\nKey (string) --The on-premises instance tag filter key.\n\nValue (string) --The on-premises instance tag filter value.\n\nType (string) --The on-premises instance tag filter type:\n\nKEY_ONLY: Key only.\nVALUE_ONLY: Value only.\nKEY_AND_VALUE: Key and value.\n\n\n\n\n\n

    :type autoScalingGroups: list
    :param autoScalingGroups: The replacement list of Auto Scaling groups to be included in the deployment group, if you want to change them. To keep the Auto Scaling groups, enter their names. To remove Auto Scaling groups, do not enter any Auto Scaling group names.\n\n(string) --\n\n

    :type serviceRoleArn: string
    :param serviceRoleArn: A replacement ARN for the service role, if you want to change it.

    :type triggerConfigurations: list
    :param triggerConfigurations: Information about triggers to change when the deployment group is updated. For examples, see Edit a Trigger in a CodeDeploy Deployment Group in the AWS CodeDeploy User Guide .\n\n(dict) --Information about notification triggers for the deployment group.\n\ntriggerName (string) --The name of the notification trigger.\n\ntriggerTargetArn (string) --The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.\n\ntriggerEvents (list) --The event type or types for which notifications are triggered.\n\n(string) --\n\n\n\n\n\n

    :type alarmConfiguration: dict
    :param alarmConfiguration: Information to add or change about Amazon CloudWatch alarms when the deployment group is updated.\n\nenabled (boolean) --Indicates whether the alarm configuration is enabled.\n\nignorePollAlarmFailure (boolean) --Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.\n\ntrue : The deployment proceeds even if alarm status information can\'t be retrieved from Amazon CloudWatch.\nfalse : The deployment stops if alarm status information can\'t be retrieved from Amazon CloudWatch.\n\n\nalarms (list) --A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.\n\n(dict) --Information about an alarm.\n\nname (string) --The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.\n\n\n\n\n\n\n

    :type autoRollbackConfiguration: dict
    :param autoRollbackConfiguration: Information for an automatic rollback configuration that is added or changed when a deployment group is updated.\n\nenabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.\n\nevents (list) --The event type or types that trigger a rollback.\n\n(string) --\n\n\n\n

    :type deploymentStyle: dict
    :param deploymentStyle: Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.\n\ndeploymentType (string) --Indicates whether to run an in-place deployment or a blue/green deployment.\n\ndeploymentOption (string) --Indicates whether to route deployment traffic behind a load balancer.\n\n\n

    :type blueGreenDeploymentConfiguration: dict
    :param blueGreenDeploymentConfiguration: Information about blue/green deployment options for a deployment group.\n\nterminateBlueInstancesOnDeploymentSuccess (dict) --Information about whether to terminate instances in the original fleet during a blue/green deployment.\n\naction (string) --The action to take on instances in the original environment after a successful blue/green deployment.\n\nTERMINATE : Instances are terminated after a specified wait time.\nKEEP_ALIVE : Instances are left running after they are deregistered from the load balancer and removed from the deployment group.\n\n\nterminationWaitTimeInMinutes (integer) --For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.\nFor an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set.\nThe maximum setting is 2880 minutes (2 days).\n\n\n\ndeploymentReadyOption (dict) --Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.\n\nactionOnTimeout (string) --Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.\n\nCONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.\nSTOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using ContinueDeployment . If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.\n\n\nwaitTimeInMinutes (integer) --The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout .\n\n\n\ngreenFleetProvisioningOption (dict) --Information about how instances are provisioned for a replacement environment in a blue/green deployment.\n\naction (string) --The method used to add instances to a replacement environment.\n\nDISCOVER_EXISTING : Use instances that already exist or will be created manually.\nCOPY_AUTO_SCALING_GROUP : Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.\n\n\n\n\n\n

    :type loadBalancerInfo: dict
    :param loadBalancerInfo: Information about the load balancer used in a deployment.\n\nelbInfoList (list) --An array that contains information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers.\n\nNote\nAdding more than one load balancer to the array is not supported.\n\n\n(dict) --Information about a load balancer in Elastic Load Balancing to use in a deployment. Instances are registered directly with a load balancer, and traffic is routed to the load balancer.\n\nname (string) --For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.\n\n\n\n\n\ntargetGroupInfoList (list) --An array that contains information about the target group to use for load balancing in a deployment. In Elastic Load Balancing, target groups are used with Application Load Balancers.\n\nNote\nAdding more than one target group to the array is not supported.\n\n\n(dict) --Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.\n\nname (string) --For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.\n\n\n\n\n\ntargetGroupPairInfoList (list) --The target group pair information. This is an array of TargeGroupPairInfo objects with a maximum size of one.\n\n(dict) --Information about two target groups and how traffic is routed during an Amazon ECS deployment. An optional test traffic route can be specified.\n\ntargetGroups (list) --One pair of target groups. One is associated with the original task set. The second is associated with the task set that serves traffic after the deployment is complete.\n\n(dict) --Information about a target group in Elastic Load Balancing to use in a deployment. Instances are registered as targets in a target group, and traffic is routed to the target group.\n\nname (string) --For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.\n\n\n\n\n\nprodTrafficRoute (dict) --The path used by a load balancer to route production traffic when an Amazon ECS deployment is complete.\n\nlistenerArns (list) --The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.\n\n(string) --\n\n\n\n\ntestTrafficRoute (dict) --An optional path used by a load balancer to route test traffic after an Amazon ECS deployment. Validation can occur while test traffic is served during a deployment.\n\nlistenerArns (list) --The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type ec2TagSet: dict
    :param ec2TagSet: Information about groups of tags applied to on-premises instances. The deployment group includes only EC2 instances identified by all the tag groups.\n\nec2TagSetList (list) --A list that contains other lists of EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.\n\n(list) --\n(dict) --Information about an EC2 tag filter.\n\nKey (string) --The tag filter key.\n\nValue (string) --The tag filter value.\n\nType (string) --The tag filter type:\n\nKEY_ONLY : Key only.\nVALUE_ONLY : Value only.\nKEY_AND_VALUE : Key and value.\n\n\n\n\n\n\n\n\n\n

    :type ecsServices: list
    :param ecsServices: The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format <clustername>:<servicename> .\n\n(dict) --Contains the service and cluster names used to identify an Amazon ECS deployment\'s target.\n\nserviceName (string) --The name of the target Amazon ECS service.\n\nclusterName (string) --The name of the cluster that the Amazon ECS service is associated with.\n\n\n\n\n

    :type onPremisesTagSet: dict
    :param onPremisesTagSet: Information about an on-premises instance tag set. The deployment group includes only on-premises instances identified by all the tag groups.\n\nonPremisesTagSetList (list) --A list that contains other lists of on-premises instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.\n\n(list) --\n(dict) --Information about an on-premises instance tag filter.\n\nKey (string) --The on-premises instance tag filter key.\n\nValue (string) --The on-premises instance tag filter value.\n\nType (string) --The on-premises instance tag filter type:\n\nKEY_ONLY: Key only.\nVALUE_ONLY: Value only.\nKEY_AND_VALUE: Key and value.\n\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'hooksNotCleanedUp': [
        {
            'name': 'string',
            'hook': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of an UpdateDeploymentGroup operation.

hooksNotCleanedUp (list) --
If the output contains no data, and the corresponding deployment group contained at least one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling lifecycle event hooks from the AWS account. If the output contains data, AWS CodeDeploy could not remove some Auto Scaling lifecycle event hooks from the AWS account.

(dict) --
Information about an Auto Scaling group.

name (string) --
The Auto Scaling group name.

hook (string) --
An Auto Scaling lifecycle event hook name.











Exceptions

CodeDeploy.Client.exceptions.ApplicationNameRequiredException
CodeDeploy.Client.exceptions.InvalidApplicationNameException
CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
CodeDeploy.Client.exceptions.DeploymentGroupAlreadyExistsException
CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
CodeDeploy.Client.exceptions.DeploymentGroupDoesNotExistException
CodeDeploy.Client.exceptions.InvalidEC2TagException
CodeDeploy.Client.exceptions.InvalidTagException
CodeDeploy.Client.exceptions.InvalidAutoScalingGroupException
CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
CodeDeploy.Client.exceptions.InvalidRoleException
CodeDeploy.Client.exceptions.LifecycleHookLimitExceededException
CodeDeploy.Client.exceptions.InvalidTriggerConfigException
CodeDeploy.Client.exceptions.TriggerTargetsLimitExceededException
CodeDeploy.Client.exceptions.InvalidAlarmConfigException
CodeDeploy.Client.exceptions.AlarmsLimitExceededException
CodeDeploy.Client.exceptions.InvalidAutoRollbackConfigException
CodeDeploy.Client.exceptions.InvalidLoadBalancerInfoException
CodeDeploy.Client.exceptions.InvalidDeploymentStyleException
CodeDeploy.Client.exceptions.InvalidBlueGreenDeploymentConfigurationException
CodeDeploy.Client.exceptions.InvalidEC2TagCombinationException
CodeDeploy.Client.exceptions.InvalidOnPremisesTagCombinationException
CodeDeploy.Client.exceptions.TagSetListLimitExceededException
CodeDeploy.Client.exceptions.InvalidInputException
CodeDeploy.Client.exceptions.ThrottlingException
CodeDeploy.Client.exceptions.InvalidECSServiceException
CodeDeploy.Client.exceptions.InvalidTargetGroupPairException
CodeDeploy.Client.exceptions.ECSServiceMappingLimitExceededException
CodeDeploy.Client.exceptions.InvalidTrafficRoutingConfigurationException


    :return: {
        'hooksNotCleanedUp': [
            {
                'name': 'string',
                'hook': 'string'
            },
        ]
    }
    
    
    :returns: 
    CodeDeploy.Client.exceptions.ApplicationNameRequiredException
    CodeDeploy.Client.exceptions.InvalidApplicationNameException
    CodeDeploy.Client.exceptions.ApplicationDoesNotExistException
    CodeDeploy.Client.exceptions.InvalidDeploymentGroupNameException
    CodeDeploy.Client.exceptions.DeploymentGroupAlreadyExistsException
    CodeDeploy.Client.exceptions.DeploymentGroupNameRequiredException
    CodeDeploy.Client.exceptions.DeploymentGroupDoesNotExistException
    CodeDeploy.Client.exceptions.InvalidEC2TagException
    CodeDeploy.Client.exceptions.InvalidTagException
    CodeDeploy.Client.exceptions.InvalidAutoScalingGroupException
    CodeDeploy.Client.exceptions.InvalidDeploymentConfigNameException
    CodeDeploy.Client.exceptions.DeploymentConfigDoesNotExistException
    CodeDeploy.Client.exceptions.InvalidRoleException
    CodeDeploy.Client.exceptions.LifecycleHookLimitExceededException
    CodeDeploy.Client.exceptions.InvalidTriggerConfigException
    CodeDeploy.Client.exceptions.TriggerTargetsLimitExceededException
    CodeDeploy.Client.exceptions.InvalidAlarmConfigException
    CodeDeploy.Client.exceptions.AlarmsLimitExceededException
    CodeDeploy.Client.exceptions.InvalidAutoRollbackConfigException
    CodeDeploy.Client.exceptions.InvalidLoadBalancerInfoException
    CodeDeploy.Client.exceptions.InvalidDeploymentStyleException
    CodeDeploy.Client.exceptions.InvalidBlueGreenDeploymentConfigurationException
    CodeDeploy.Client.exceptions.InvalidEC2TagCombinationException
    CodeDeploy.Client.exceptions.InvalidOnPremisesTagCombinationException
    CodeDeploy.Client.exceptions.TagSetListLimitExceededException
    CodeDeploy.Client.exceptions.InvalidInputException
    CodeDeploy.Client.exceptions.ThrottlingException
    CodeDeploy.Client.exceptions.InvalidECSServiceException
    CodeDeploy.Client.exceptions.InvalidTargetGroupPairException
    CodeDeploy.Client.exceptions.ECSServiceMappingLimitExceededException
    CodeDeploy.Client.exceptions.InvalidTrafficRoutingConfigurationException
    
    """
    pass

