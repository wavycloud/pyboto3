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
    :param tags: [REQUIRED]
            The tag key-value pairs to add to the on-premises instances.
            Keys and values are both required. Keys cannot be null or empty strings. Value-only tags are not allowed.
            (dict) --Information about a tag.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            

    :type instanceNames: list
    :param instanceNames: [REQUIRED]
            The names of the on-premises instances to which to add tags.
            (string) --
            

    """
    pass

def batch_get_application_revisions(applicationName=None, revisions=None):
    """
    Gets information about one or more application revisions.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_application_revisions(
        applicationName='string',
        revisions=[
            {
                'revisionType': 'S3'|'GitHub',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                }
            },
        ]
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application about which to get revision information.
            

    :type revisions: list
    :param revisions: [REQUIRED]
            Information to get about the application revisions, including type and location.
            (dict) --Information about the location of an application revision.
            revisionType (string) --The type of application revision:
            S3: An application revision stored in Amazon S3.
            GitHub: An application revision stored in GitHub.
            s3Location (dict) --Information about the location of application artifacts stored in Amazon S3.
            bucket (string) --The name of the Amazon S3 bucket where the application revision is stored.
            key (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.
            bundleType (string) --The file type of the application revision. Must be one of the following:
            tar: A tar archive file.
            tgz: A compressed tar archive file.
            zip: A zip archive file.
            version (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
            If the version is not specified, the system will use the most recent version by default.
            eTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
            If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.
            gitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.
            repository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
            Specified as account/repository.
            commitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.
            
            

    :rtype: dict
    :return: {
        'applicationName': 'string',
        'errorMessage': 'string',
        'revisions': [
            {
                'revisionLocation': {
                    'revisionType': 'S3'|'GitHub',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
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
    GitHub: An application revision stored in GitHub.
    
    """
    pass

def batch_get_applications(applicationNames=None):
    """
    Gets information about one or more applications.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_applications(
        applicationNames=[
            'string',
        ]
    )
    
    
    :type applicationNames: list
    :param applicationNames: A list of application names separated by spaces.
            (string) --
            

    :rtype: dict
    :return: {
        'applicationsInfo': [
            {
                'applicationId': 'string',
                'applicationName': 'string',
                'createTime': datetime(2015, 1, 1),
                'linkedToGitHub': True|False,
                'gitHubAccountName': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_get_deployment_groups(applicationName=None, deploymentGroupNames=None):
    """
    Gets information about one or more deployment groups.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_deployment_groups(
        applicationName='string',
        deploymentGroupNames=[
            'string',
        ]
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    :type deploymentGroupNames: list
    :param deploymentGroupNames: [REQUIRED]
            The deployment groups' names.
            (string) --
            

    :rtype: dict
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
                    'revisionType': 'S3'|'GitHub',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
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
                    ]
                },
                'lastSuccessfulDeployment': {
                    'deploymentId': 'string',
                    'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                    'endTime': datetime(2015, 1, 1),
                    'createTime': datetime(2015, 1, 1)
                },
                'lastAttemptedDeployment': {
                    'deploymentId': 'string',
                    'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                    'endTime': datetime(2015, 1, 1),
                    'createTime': datetime(2015, 1, 1)
                }
            },
        ],
        'errorMessage': 'string'
    }
    
    
    :returns: 
    KEY_ONLY: Key only.
    VALUE_ONLY: Value only.
    KEY_AND_VALUE: Key and value.
    
    """
    pass

def batch_get_deployment_instances(deploymentId=None, instanceIds=None):
    """
    Gets information about one or more instance that are part of a deployment group.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_deployment_instances(
        deploymentId='string',
        instanceIds=[
            'string',
        ]
    )
    
    
    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            The unique ID of a deployment.
            

    :type instanceIds: list
    :param instanceIds: [REQUIRED]
            The unique IDs of instances in the deployment group.
            (string) --
            

    :rtype: dict
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
    Pending: The deployment is pending for this instance.
    In Progress: The deployment is in progress for this instance.
    Succeeded: The deployment has succeeded for this instance.
    Failed: The deployment has failed for this instance.
    Skipped: The deployment has been skipped for this instance.
    Unknown: The deployment status is unknown for this instance.
    
    """
    pass

def batch_get_deployments(deploymentIds=None):
    """
    Gets information about one or more deployments.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_deployments(
        deploymentIds=[
            'string',
        ]
    )
    
    
    :type deploymentIds: list
    :param deploymentIds: A list of deployment IDs, separated by spaces.
            (string) --
            

    :rtype: dict
    :return: {
        'deploymentsInfo': [
            {
                'applicationName': 'string',
                'deploymentGroupName': 'string',
                'deploymentConfigName': 'string',
                'deploymentId': 'string',
                'previousRevision': {
                    'revisionType': 'S3'|'GitHub',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    }
                },
                'revision': {
                    'revisionType': 'S3'|'GitHub',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    }
                },
                'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                'errorInformation': {
                    'code': 'DEPLOYMENT_GROUP_MISSING'|'APPLICATION_MISSING'|'REVISION_MISSING'|'IAM_ROLE_MISSING'|'IAM_ROLE_PERMISSIONS'|'NO_EC2_SUBSCRIPTION'|'OVER_MAX_INSTANCES'|'NO_INSTANCES'|'TIMEOUT'|'HEALTH_CONSTRAINTS_INVALID'|'HEALTH_CONSTRAINTS'|'INTERNAL_ERROR'|'THROTTLED'|'ALARM_ACTIVE'|'AGENT_ISSUE'|'AUTO_SCALING_IAM_ROLE_PERMISSIONS'|'AUTO_SCALING_CONFIGURATION'|'MANUAL_STOP',
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
                'creator': 'user'|'autoscaling'|'codeDeployRollback',
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
                    ]
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
                    ]
                },
                'additionalDeploymentStatusInfo': 'string',
                'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN'
            },
        ]
    }
    
    
    :returns: 
    S3: An application revision stored in Amazon S3.
    GitHub: An application revision stored in GitHub.
    
    """
    pass

def batch_get_on_premises_instances(instanceNames=None):
    """
    Gets information about one or more on-premises instances.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_on_premises_instances(
        instanceNames=[
            'string',
        ]
    )
    
    
    :type instanceNames: list
    :param instanceNames: The names of the on-premises instances about which to get information.
            (string) --
            

    :rtype: dict
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
    
    
    """
    pass

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

def continue_deployment(deploymentId=None):
    """
    For a blue/green deployment, starts the process of rerouting traffic from instances in the original environment to instances in the replacement environment without waiting for a specified wait time to elapse. (Traffic rerouting, which is achieved by registering instances in the replacement environment with the load balancer, can start as soon as all instances have a status of Ready.)
    See also: AWS API Documentation
    
    
    :example: response = client.continue_deployment(
        deploymentId='string'
    )
    
    
    :type deploymentId: string
    :param deploymentId: The deployment ID of the blue/green deployment for which you want to start rerouting traffic to the replacement environment.

    """
    pass

def create_application(applicationName=None):
    """
    Creates an application.
    See also: AWS API Documentation
    
    
    :example: response = client.create_application(
        applicationName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of the application. This name must be unique with the applicable IAM user or AWS account.
            

    :rtype: dict
    :return: {
        'applicationId': 'string'
    }
    
    
    """
    pass

def create_deployment(applicationName=None, deploymentGroupName=None, revision=None, deploymentConfigName=None, description=None, ignoreApplicationStopFailures=None, targetInstances=None, autoRollbackConfiguration=None, updateOutdatedInstancesOnly=None, fileExistsBehavior=None):
    """
    Deploys an application revision through the specified deployment group.
    See also: AWS API Documentation
    
    
    :example: response = client.create_deployment(
        applicationName='string',
        deploymentGroupName='string',
        revision={
            'revisionType': 'S3'|'GitHub',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
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
            ]
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
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    :type deploymentGroupName: string
    :param deploymentGroupName: The name of the deployment group.

    :type revision: dict
    :param revision: The type and location of the revision to deploy.
            revisionType (string) --The type of application revision:
            S3: An application revision stored in Amazon S3.
            GitHub: An application revision stored in GitHub.
            s3Location (dict) --Information about the location of application artifacts stored in Amazon S3.
            bucket (string) --The name of the Amazon S3 bucket where the application revision is stored.
            key (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.
            bundleType (string) --The file type of the application revision. Must be one of the following:
            tar: A tar archive file.
            tgz: A compressed tar archive file.
            zip: A zip archive file.
            version (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
            If the version is not specified, the system will use the most recent version by default.
            eTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
            If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.
            gitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.
            repository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
            Specified as account/repository.
            commitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.
            
            

    :type deploymentConfigName: string
    :param deploymentConfigName: The name of a deployment configuration associated with the applicable IAM user or AWS account.
            If not specified, the value configured in the deployment group will be used as the default. If the deployment group does not have a deployment configuration associated with it, then CodeDeployDefault.OneAtATime will be used by default.
            

    :type description: string
    :param description: A comment about the deployment.

    :type ignoreApplicationStopFailures: boolean
    :param ignoreApplicationStopFailures: If set to true, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will not be considered to have failed at that point and will continue on to the BeforeInstall deployment lifecycle event.
            If set to false or not specified, then if the deployment causes the ApplicationStop deployment lifecycle event to fail to an instance, the deployment to that instance will stop, and the deployment to that instance will be considered to have failed.
            

    :type targetInstances: dict
    :param targetInstances: Information about the instances that will belong to the replacement environment in a blue/green deployment.
            tagFilters (list) --The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment.
            (dict) --Information about an EC2 tag filter.
            Key (string) --The tag filter key.
            Value (string) --The tag filter value.
            Type (string) --The tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            autoScalingGroups (list) --The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.
            (string) --
            

    :type autoRollbackConfiguration: dict
    :param autoRollbackConfiguration: Configuration information for an automatic rollback that is added when a deployment is created.
            enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.
            events (list) --The event type or types that trigger a rollback.
            (string) --
            

    :type updateOutdatedInstancesOnly: boolean
    :param updateOutdatedInstancesOnly: Indicates whether to deploy to all instances or only to instances that are not running the latest application revision.

    :type fileExistsBehavior: string
    :param fileExistsBehavior: Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment.
            The fileExistsBehavior parameter takes any of the following values:
            DISALLOW: The deployment fails. This is also the default behavior if no option is specified.
            OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance.
            RETAIN: The version of the file already on the instance is kept and used as part of the new deployment.
            

    :rtype: dict
    :return: {
        'deploymentId': 'string'
    }
    
    
    """
    pass

def create_deployment_config(deploymentConfigName=None, minimumHealthyHosts=None):
    """
    Creates a deployment configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.create_deployment_config(
        deploymentConfigName='string',
        minimumHealthyHosts={
            'value': 123,
            'type': 'HOST_COUNT'|'FLEET_PERCENT'
        }
    )
    
    
    :type deploymentConfigName: string
    :param deploymentConfigName: [REQUIRED]
            The name of the deployment configuration to create.
            

    :type minimumHealthyHosts: dict
    :param minimumHealthyHosts: The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.
            The type parameter takes either of the following values:
            HOST_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value.
            FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.
            The value parameter takes an integer.
            For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a value of 95.
            value (integer) --The minimum healthy instance value.
            type (string) --The minimum healthy instance type:
            HOST_COUNT: The minimum number of healthy instance as an absolute value.
            FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total number of instance in the deployment.
            In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to three instances at a time. The deployment will be successful if six or more instances are deployed to successfully; otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to five instance at a time. The deployment will be successful if four or more instance are deployed to successfully; otherwise, the deployment fails.
            Note
            In a call to the get deployment configuration operation, CodeDeployDefault.OneAtATime will return a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy will try to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment still succeeds.
            For more information, see AWS CodeDeploy Instance Health in the AWS CodeDeploy User Guide .
            

    :rtype: dict
    :return: {
        'deploymentConfigId': 'string'
    }
    
    
    """
    pass

def create_deployment_group(applicationName=None, deploymentGroupName=None, deploymentConfigName=None, ec2TagFilters=None, onPremisesInstanceTagFilters=None, autoScalingGroups=None, serviceRoleArn=None, triggerConfigurations=None, alarmConfiguration=None, autoRollbackConfiguration=None, deploymentStyle=None, blueGreenDeploymentConfiguration=None, loadBalancerInfo=None):
    """
    Creates a deployment group to which application revisions will be deployed.
    See also: AWS API Documentation
    
    
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
            ]
        }
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    :type deploymentGroupName: string
    :param deploymentGroupName: [REQUIRED]
            The name of a new deployment group for the specified application.
            

    :type deploymentConfigName: string
    :param deploymentConfigName: If specified, the deployment configuration name can be either one of the predefined configurations provided with AWS CodeDeploy or a custom deployment configuration that you create by calling the create deployment configuration operation.
            CodeDeployDefault.OneAtATime is the default deployment configuration. It is used if a configuration isn't specified for the deployment or the deployment group.
            For more information about the predefined deployment configurations in AWS CodeDeploy, see Working with Deployment Groups in AWS CodeDeploy in the AWS CodeDeploy User Guide.
            

    :type ec2TagFilters: list
    :param ec2TagFilters: The Amazon EC2 tags on which to filter. The deployment group will include EC2 instances with any of the specified tags.
            (dict) --Information about an EC2 tag filter.
            Key (string) --The tag filter key.
            Value (string) --The tag filter value.
            Type (string) --The tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            

    :type onPremisesInstanceTagFilters: list
    :param onPremisesInstanceTagFilters: The on-premises instance tags on which to filter. The deployment group will include on-premises instances with any of the specified tags.
            (dict) --Information about an on-premises instance tag filter.
            Key (string) --The on-premises instance tag filter key.
            Value (string) --The on-premises instance tag filter value.
            Type (string) --The on-premises instance tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            

    :type autoScalingGroups: list
    :param autoScalingGroups: A list of associated Auto Scaling groups.
            (string) --
            

    :type serviceRoleArn: string
    :param serviceRoleArn: [REQUIRED]
            A service role ARN that allows AWS CodeDeploy to act on the user's behalf when interacting with AWS services.
            

    :type triggerConfigurations: list
    :param triggerConfigurations: Information about triggers to create when the deployment group is created. For examples, see Create a Trigger for an AWS CodeDeploy Event in the AWS CodeDeploy User Guide.
            (dict) --Information about notification triggers for the deployment group.
            triggerName (string) --The name of the notification trigger.
            triggerTargetArn (string) --The ARN of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.
            triggerEvents (list) --The event type or types for which notifications are triggered.
            (string) --
            
            

    :type alarmConfiguration: dict
    :param alarmConfiguration: Information to add about Amazon CloudWatch alarms when the deployment group is created.
            enabled (boolean) --Indicates whether the alarm configuration is enabled.
            ignorePollAlarmFailure (boolean) --Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.
            true: The deployment will proceed even if alarm status information can't be retrieved from Amazon CloudWatch.
            false: The deployment will stop if alarm status information can't be retrieved from Amazon CloudWatch.
            alarms (list) --A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.
            (dict) --Information about an alarm.
            name (string) --The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.
            
            

    :type autoRollbackConfiguration: dict
    :param autoRollbackConfiguration: Configuration information for an automatic rollback that is added when a deployment group is created.
            enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.
            events (list) --The event type or types that trigger a rollback.
            (string) --
            

    :type deploymentStyle: dict
    :param deploymentStyle: Information about the type of deployment, in-place or blue/green, that you want to run and whether to route deployment traffic behind a load balancer.
            deploymentType (string) --Indicates whether to run an in-place deployment or a blue/green deployment.
            deploymentOption (string) --Indicates whether to route deployment traffic behind a load balancer.
            

    :type blueGreenDeploymentConfiguration: dict
    :param blueGreenDeploymentConfiguration: Information about blue/green deployment options for a deployment group.
            terminateBlueInstancesOnDeploymentSuccess (dict) --Information about whether to terminate instances in the original fleet during a blue/green deployment.
            action (string) --The action to take on instances in the original environment after a successful blue/green deployment.
            TERMINATE: Instances are terminated after a specified wait time.
            KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
            terminationWaitTimeInMinutes (integer) --The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
            deploymentReadyOption (dict) --Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.
            actionOnTimeout (string) --Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
            CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
            STOP_DEPLOYMENT: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.
            waitTimeInMinutes (integer) --The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout
            greenFleetProvisioningOption (dict) --Information about how instances are provisioned for a replacement environment in a blue/green deployment.
            action (string) --The method used to add instances to a replacement environment.
            DISCOVER_EXISTING: Use instances that already exist or will be created manually.
            COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.
            
            

    :type loadBalancerInfo: dict
    :param loadBalancerInfo: Information about the load balancer used in a deployment.
            elbInfoList (list) --An array containing information about the load balancer in Elastic Load Balancing to use in a deployment.
            (dict) --Information about a load balancer in Elastic Load Balancing to use in a deployment.
            name (string) --For blue/green deployments, the name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.
            
            

    :rtype: dict
    :return: {
        'deploymentGroupId': 'string'
    }
    
    
    """
    pass

def delete_application(applicationName=None):
    """
    Deletes an application.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_application(
        applicationName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    """
    pass

def delete_deployment_config(deploymentConfigName=None):
    """
    Deletes a deployment configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_deployment_config(
        deploymentConfigName='string'
    )
    
    
    :type deploymentConfigName: string
    :param deploymentConfigName: [REQUIRED]
            The name of a deployment configuration associated with the applicable IAM user or AWS account.
            

    """
    pass

def delete_deployment_group(applicationName=None, deploymentGroupName=None):
    """
    Deletes a deployment group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_deployment_group(
        applicationName='string',
        deploymentGroupName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    :type deploymentGroupName: string
    :param deploymentGroupName: [REQUIRED]
            The name of an existing deployment group for the specified application.
            

    :rtype: dict
    :return: {
        'hooksNotCleanedUp': [
            {
                'name': 'string',
                'hook': 'string'
            },
        ]
    }
    
    
    """
    pass

def deregister_on_premises_instance(instanceName=None):
    """
    Deregisters an on-premises instance.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_on_premises_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the on-premises instance to deregister.
            

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

def get_application(applicationName=None):
    """
    Gets information about an application.
    See also: AWS API Documentation
    
    
    :example: response = client.get_application(
        applicationName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    :rtype: dict
    :return: {
        'application': {
            'applicationId': 'string',
            'applicationName': 'string',
            'createTime': datetime(2015, 1, 1),
            'linkedToGitHub': True|False,
            'gitHubAccountName': 'string'
        }
    }
    
    
    """
    pass

def get_application_revision(applicationName=None, revision=None):
    """
    Gets information about an application revision.
    See also: AWS API Documentation
    
    
    :example: response = client.get_application_revision(
        applicationName='string',
        revision={
            'revisionType': 'S3'|'GitHub',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            }
        }
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of the application that corresponds to the revision.
            

    :type revision: dict
    :param revision: [REQUIRED]
            Information about the application revision to get, including type and location.
            revisionType (string) --The type of application revision:
            S3: An application revision stored in Amazon S3.
            GitHub: An application revision stored in GitHub.
            s3Location (dict) --Information about the location of application artifacts stored in Amazon S3.
            bucket (string) --The name of the Amazon S3 bucket where the application revision is stored.
            key (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.
            bundleType (string) --The file type of the application revision. Must be one of the following:
            tar: A tar archive file.
            tgz: A compressed tar archive file.
            zip: A zip archive file.
            version (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
            If the version is not specified, the system will use the most recent version by default.
            eTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
            If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.
            gitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.
            repository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
            Specified as account/repository.
            commitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.
            
            

    :rtype: dict
    :return: {
        'applicationName': 'string',
        'revision': {
            'revisionType': 'S3'|'GitHub',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
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
    GitHub: An application revision stored in GitHub.
    
    """
    pass

def get_deployment(deploymentId=None):
    """
    Gets information about a deployment.
    See also: AWS API Documentation
    
    
    :example: response = client.get_deployment(
        deploymentId='string'
    )
    
    
    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            A deployment ID associated with the applicable IAM user or AWS account.
            

    :rtype: dict
    :return: {
        'deploymentInfo': {
            'applicationName': 'string',
            'deploymentGroupName': 'string',
            'deploymentConfigName': 'string',
            'deploymentId': 'string',
            'previousRevision': {
                'revisionType': 'S3'|'GitHub',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                }
            },
            'revision': {
                'revisionType': 'S3'|'GitHub',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                }
            },
            'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
            'errorInformation': {
                'code': 'DEPLOYMENT_GROUP_MISSING'|'APPLICATION_MISSING'|'REVISION_MISSING'|'IAM_ROLE_MISSING'|'IAM_ROLE_PERMISSIONS'|'NO_EC2_SUBSCRIPTION'|'OVER_MAX_INSTANCES'|'NO_INSTANCES'|'TIMEOUT'|'HEALTH_CONSTRAINTS_INVALID'|'HEALTH_CONSTRAINTS'|'INTERNAL_ERROR'|'THROTTLED'|'ALARM_ACTIVE'|'AGENT_ISSUE'|'AUTO_SCALING_IAM_ROLE_PERMISSIONS'|'AUTO_SCALING_CONFIGURATION'|'MANUAL_STOP',
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
            'creator': 'user'|'autoscaling'|'codeDeployRollback',
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
                ]
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
                ]
            },
            'additionalDeploymentStatusInfo': 'string',
            'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN'
        }
    }
    
    
    :returns: 
    tar: A tar archive file.
    tgz: A compressed tar archive file.
    zip: A zip archive file.
    
    """
    pass

def get_deployment_config(deploymentConfigName=None):
    """
    Gets information about a deployment configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.get_deployment_config(
        deploymentConfigName='string'
    )
    
    
    :type deploymentConfigName: string
    :param deploymentConfigName: [REQUIRED]
            The name of a deployment configuration associated with the applicable IAM user or AWS account.
            

    :rtype: dict
    :return: {
        'deploymentConfigInfo': {
            'deploymentConfigId': 'string',
            'deploymentConfigName': 'string',
            'minimumHealthyHosts': {
                'value': 123,
                'type': 'HOST_COUNT'|'FLEET_PERCENT'
            },
            'createTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_deployment_group(applicationName=None, deploymentGroupName=None):
    """
    Gets information about a deployment group.
    See also: AWS API Documentation
    
    
    :example: response = client.get_deployment_group(
        applicationName='string',
        deploymentGroupName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    :type deploymentGroupName: string
    :param deploymentGroupName: [REQUIRED]
            The name of an existing deployment group for the specified application.
            

    :rtype: dict
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
                'revisionType': 'S3'|'GitHub',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
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
                ]
            },
            'lastSuccessfulDeployment': {
                'deploymentId': 'string',
                'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                'endTime': datetime(2015, 1, 1),
                'createTime': datetime(2015, 1, 1)
            },
            'lastAttemptedDeployment': {
                'deploymentId': 'string',
                'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
                'endTime': datetime(2015, 1, 1),
                'createTime': datetime(2015, 1, 1)
            }
        }
    }
    
    
    :returns: 
    KEY_ONLY: Key only.
    VALUE_ONLY: Value only.
    KEY_AND_VALUE: Key and value.
    
    """
    pass

def get_deployment_instance(deploymentId=None, instanceId=None):
    """
    Gets information about an instance as part of a deployment.
    See also: AWS API Documentation
    
    
    :example: response = client.get_deployment_instance(
        deploymentId='string',
        instanceId='string'
    )
    
    
    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            The unique ID of a deployment.
            

    :type instanceId: string
    :param instanceId: [REQUIRED]
            The unique ID of an instance in the deployment group.
            

    :rtype: dict
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
    Pending: The deployment is pending for this instance.
    In Progress: The deployment is in progress for this instance.
    Succeeded: The deployment has succeeded for this instance.
    Failed: The deployment has failed for this instance.
    Skipped: The deployment has been skipped for this instance.
    Unknown: The deployment status is unknown for this instance.
    
    """
    pass

def get_on_premises_instance(instanceName=None):
    """
    Gets information about an on-premises instance.
    See also: AWS API Documentation
    
    
    :example: response = client.get_on_premises_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the on-premises instance about which to get information.
            

    :rtype: dict
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

def list_application_revisions(applicationName=None, sortBy=None, sortOrder=None, s3Bucket=None, s3KeyPrefix=None, deployed=None, nextToken=None):
    """
    Lists information about revisions for an application.
    See also: AWS API Documentation
    
    
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
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    :type sortBy: string
    :param sortBy: The column name to use to sort the list results:
            registerTime: Sort by the time the revisions were registered with AWS CodeDeploy.
            firstUsedTime: Sort by the time the revisions were first used in a deployment.
            lastUsedTime: Sort by the time the revisions were last used in a deployment.
            If not specified or set to null, the results will be returned in an arbitrary order.
            

    :type sortOrder: string
    :param sortOrder: The order in which to sort the list results:
            ascending: ascending order.
            descending: descending order.
            If not specified, the results will be sorted in ascending order.
            If set to null, the results will be sorted in an arbitrary order.
            

    :type s3Bucket: string
    :param s3Bucket: An Amazon S3 bucket name to limit the search for revisions.
            If set to null, all of the user's buckets will be searched.
            

    :type s3KeyPrefix: string
    :param s3KeyPrefix: A key prefix for the set of Amazon S3 objects to limit the search for revisions.

    :type deployed: string
    :param deployed: Whether to list revisions based on whether the revision is the target revision of an deployment group:
            include: List revisions that are target revisions of a deployment group.
            exclude: Do not list revisions that are target revisions of a deployment group.
            ignore: List all revisions.
            

    :type nextToken: string
    :param nextToken: An identifier returned from the previous list application revisions call. It can be used to return the next set of applications in the list.

    :rtype: dict
    :return: {
        'revisions': [
            {
                'revisionType': 'S3'|'GitHub',
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'bundleType': 'tar'|'tgz'|'zip',
                    'version': 'string',
                    'eTag': 'string'
                },
                'gitHubLocation': {
                    'repository': 'string',
                    'commitId': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    S3: An application revision stored in Amazon S3.
    GitHub: An application revision stored in GitHub.
    
    """
    pass

def list_applications(nextToken=None):
    """
    Lists the applications registered with the applicable IAM user or AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_applications(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier returned from the previous list applications call. It can be used to return the next set of applications in the list.

    :rtype: dict
    :return: {
        'applications': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_deployment_configs(nextToken=None):
    """
    Lists the deployment configurations with the applicable IAM user or AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_deployment_configs(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier returned from the previous list deployment configurations call. It can be used to return the next set of deployment configurations in the list.

    :rtype: dict
    :return: {
        'deploymentConfigsList': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_deployment_groups(applicationName=None, nextToken=None):
    """
    Lists the deployment groups for an application registered with the applicable IAM user or AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_deployment_groups(
        applicationName='string',
        nextToken='string'
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    :type nextToken: string
    :param nextToken: An identifier returned from the previous list deployment groups call. It can be used to return the next set of deployment groups in the list.

    :rtype: dict
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
    Lists the instance for a deployment associated with the applicable IAM user or AWS account.
    See also: AWS API Documentation
    
    
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
    :param deploymentId: [REQUIRED]
            The unique ID of a deployment.
            

    :type nextToken: string
    :param nextToken: An identifier returned from the previous list deployment instances call. It can be used to return the next set of deployment instances in the list.

    :type instanceStatusFilter: list
    :param instanceStatusFilter: A subset of instances to list by status:
            Pending: Include those instance with pending deployments.
            InProgress: Include those instance where deployments are still in progress.
            Succeeded: Include those instances with successful deployments.
            Failed: Include those instance with failed deployments.
            Skipped: Include those instance with skipped deployments.
            Unknown: Include those instance with deployments in an unknown state.
            (string) --
            

    :type instanceTypeFilter: list
    :param instanceTypeFilter: The set of instances in a blue/green deployment, either those in the original environment ('BLUE') or those in the replacement environment ('GREEN'), for which you want to view instance information.
            (string) --
            

    :rtype: dict
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

def list_deployments(applicationName=None, deploymentGroupName=None, includeOnlyStatuses=None, createTimeRange=None, nextToken=None):
    """
    Lists the deployments in a deployment group for an application registered with the applicable IAM user or AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_deployments(
        applicationName='string',
        deploymentGroupName='string',
        includeOnlyStatuses=[
            'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
        ],
        createTimeRange={
            'start': datetime(2015, 1, 1),
            'end': datetime(2015, 1, 1)
        },
        nextToken='string'
    )
    
    
    :type applicationName: string
    :param applicationName: The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.

    :type deploymentGroupName: string
    :param deploymentGroupName: The name of an existing deployment group for the specified application.

    :type includeOnlyStatuses: list
    :param includeOnlyStatuses: A subset of deployments to list by status:
            Created: Include created deployments in the resulting list.
            Queued: Include queued deployments in the resulting list.
            In Progress: Include in-progress deployments in the resulting list.
            Succeeded: Include successful deployments in the resulting list.
            Failed: Include failed deployments in the resulting list.
            Stopped: Include stopped deployments in the resulting list.
            (string) --
            

    :type createTimeRange: dict
    :param createTimeRange: A time range (start and end) for returning a subset of the list of deployments.
            start (datetime) --The start time of the time range.
            Note
            Specify null to leave the start time open-ended.
            end (datetime) --The end time of the time range.
            Note
            Specify null to leave the end time open-ended.
            

    :type nextToken: string
    :param nextToken: An identifier returned from the previous list deployments call. It can be used to return the next set of deployments in the list.

    :rtype: dict
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
    
    
    :example: response = client.list_git_hub_account_token_names(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier returned from the previous ListGitHubAccountTokenNames call. It can be used to return the next set of names in the list.

    :rtype: dict
    :return: {
        'tokenNameList': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_on_premises_instances(registrationStatus=None, tagFilters=None, nextToken=None):
    """
    Gets a list of names for one or more on-premises instances.
    Unless otherwise specified, both registered and deregistered on-premises instance names will be listed. To list only registered or deregistered on-premises instance names, use the registration status parameter.
    See also: AWS API Documentation
    
    
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
    :param registrationStatus: The registration status of the on-premises instances:
            Deregistered: Include deregistered on-premises instances in the resulting list.
            Registered: Include registered on-premises instances in the resulting list.
            

    :type tagFilters: list
    :param tagFilters: The on-premises instance tags that will be used to restrict the corresponding on-premises instance names returned.
            (dict) --Information about an on-premises instance tag filter.
            Key (string) --The on-premises instance tag filter key.
            Value (string) --The on-premises instance tag filter value.
            Type (string) --The on-premises instance tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            

    :type nextToken: string
    :param nextToken: An identifier returned from the previous list on-premises instances call. It can be used to return the next set of on-premises instances in the list.

    :rtype: dict
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

def register_application_revision(applicationName=None, description=None, revision=None):
    """
    Registers with AWS CodeDeploy a revision for the specified application.
    See also: AWS API Documentation
    
    
    :example: response = client.register_application_revision(
        applicationName='string',
        description='string',
        revision={
            'revisionType': 'S3'|'GitHub',
            's3Location': {
                'bucket': 'string',
                'key': 'string',
                'bundleType': 'tar'|'tgz'|'zip',
                'version': 'string',
                'eTag': 'string'
            },
            'gitHubLocation': {
                'repository': 'string',
                'commitId': 'string'
            }
        }
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            

    :type description: string
    :param description: A comment about the revision.

    :type revision: dict
    :param revision: [REQUIRED]
            Information about the application revision to register, including type and location.
            revisionType (string) --The type of application revision:
            S3: An application revision stored in Amazon S3.
            GitHub: An application revision stored in GitHub.
            s3Location (dict) --Information about the location of application artifacts stored in Amazon S3.
            bucket (string) --The name of the Amazon S3 bucket where the application revision is stored.
            key (string) --The name of the Amazon S3 object that represents the bundled artifacts for the application revision.
            bundleType (string) --The file type of the application revision. Must be one of the following:
            tar: A tar archive file.
            tgz: A compressed tar archive file.
            zip: A zip archive file.
            version (string) --A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
            If the version is not specified, the system will use the most recent version by default.
            eTag (string) --The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
            If the ETag is not specified as an input parameter, ETag validation of the object will be skipped.
            gitHubLocation (dict) --Information about the location of application artifacts stored in GitHub.
            repository (string) --The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.
            Specified as account/repository.
            commitId (string) --The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.
            
            

    """
    pass

def register_on_premises_instance(instanceName=None, iamSessionArn=None, iamUserArn=None):
    """
    Registers an on-premises instance.
    See also: AWS API Documentation
    
    
    :example: response = client.register_on_premises_instance(
        instanceName='string',
        iamSessionArn='string',
        iamUserArn='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the on-premises instance to register.
            

    :type iamSessionArn: string
    :param iamSessionArn: The ARN of the IAM session to associate with the on-premises instance.

    :type iamUserArn: string
    :param iamUserArn: The ARN of the IAM user to associate with the on-premises instance.

    """
    pass

def remove_tags_from_on_premises_instances(tags=None, instanceNames=None):
    """
    Removes one or more tags from one or more on-premises instances.
    See also: AWS API Documentation
    
    
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
    :param tags: [REQUIRED]
            The tag key-value pairs to remove from the on-premises instances.
            (dict) --Information about a tag.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            

    :type instanceNames: list
    :param instanceNames: [REQUIRED]
            The names of the on-premises instances from which to remove tags.
            (string) --
            

    """
    pass

def skip_wait_time_for_instance_termination(deploymentId=None):
    """
    In a blue/green deployment, overrides any specified wait time and starts terminating instances immediately after the traffic routing is completed.
    See also: AWS API Documentation
    
    
    :example: response = client.skip_wait_time_for_instance_termination(
        deploymentId='string'
    )
    
    
    :type deploymentId: string
    :param deploymentId: The ID of the blue/green deployment for which you want to skip the instance termination wait time.

    """
    pass

def stop_deployment(deploymentId=None, autoRollbackEnabled=None):
    """
    Attempts to stop an ongoing deployment.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_deployment(
        deploymentId='string',
        autoRollbackEnabled=True|False
    )
    
    
    :type deploymentId: string
    :param deploymentId: [REQUIRED]
            The unique ID of a deployment.
            

    :type autoRollbackEnabled: boolean
    :param autoRollbackEnabled: Indicates, when a deployment is stopped, whether instances that have been updated should be rolled back to the previous version of the application revision.

    :rtype: dict
    :return: {
        'status': 'Pending'|'Succeeded',
        'statusMessage': 'string'
    }
    
    
    :returns: 
    Pending: The stop operation is pending.
    Succeeded: The stop operation was successful.
    
    """
    pass

def update_application(applicationName=None, newApplicationName=None):
    """
    Changes the name of an application.
    See also: AWS API Documentation
    
    
    :example: response = client.update_application(
        applicationName='string',
        newApplicationName='string'
    )
    
    
    :type applicationName: string
    :param applicationName: The current name of the application you want to change.

    :type newApplicationName: string
    :param newApplicationName: The new name to give the application.

    """
    pass

def update_deployment_group(applicationName=None, currentDeploymentGroupName=None, newDeploymentGroupName=None, deploymentConfigName=None, ec2TagFilters=None, onPremisesInstanceTagFilters=None, autoScalingGroups=None, serviceRoleArn=None, triggerConfigurations=None, alarmConfiguration=None, autoRollbackConfiguration=None, deploymentStyle=None, blueGreenDeploymentConfiguration=None, loadBalancerInfo=None):
    """
    Changes information about a deployment group.
    See also: AWS API Documentation
    
    
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
            ]
        }
    )
    
    
    :type applicationName: string
    :param applicationName: [REQUIRED]
            The application name corresponding to the deployment group to update.
            

    :type currentDeploymentGroupName: string
    :param currentDeploymentGroupName: [REQUIRED]
            The current name of the deployment group.
            

    :type newDeploymentGroupName: string
    :param newDeploymentGroupName: The new name of the deployment group, if you want to change it.

    :type deploymentConfigName: string
    :param deploymentConfigName: The replacement deployment configuration name to use, if you want to change it.

    :type ec2TagFilters: list
    :param ec2TagFilters: The replacement set of Amazon EC2 tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.
            (dict) --Information about an EC2 tag filter.
            Key (string) --The tag filter key.
            Value (string) --The tag filter value.
            Type (string) --The tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            

    :type onPremisesInstanceTagFilters: list
    :param onPremisesInstanceTagFilters: The replacement set of on-premises instance tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.
            (dict) --Information about an on-premises instance tag filter.
            Key (string) --The on-premises instance tag filter key.
            Value (string) --The on-premises instance tag filter value.
            Type (string) --The on-premises instance tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            

    :type autoScalingGroups: list
    :param autoScalingGroups: The replacement list of Auto Scaling groups to be included in the deployment group, if you want to change them. To keep the Auto Scaling groups, enter their names. To remove Auto Scaling groups, do not enter any Auto Scaling group names.
            (string) --
            

    :type serviceRoleArn: string
    :param serviceRoleArn: A replacement ARN for the service role, if you want to change it.

    :type triggerConfigurations: list
    :param triggerConfigurations: Information about triggers to change when the deployment group is updated. For examples, see Modify Triggers in an AWS CodeDeploy Deployment Group in the AWS CodeDeploy User Guide.
            (dict) --Information about notification triggers for the deployment group.
            triggerName (string) --The name of the notification trigger.
            triggerTargetArn (string) --The ARN of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.
            triggerEvents (list) --The event type or types for which notifications are triggered.
            (string) --
            
            

    :type alarmConfiguration: dict
    :param alarmConfiguration: Information to add or change about Amazon CloudWatch alarms when the deployment group is updated.
            enabled (boolean) --Indicates whether the alarm configuration is enabled.
            ignorePollAlarmFailure (boolean) --Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.
            true: The deployment will proceed even if alarm status information can't be retrieved from Amazon CloudWatch.
            false: The deployment will stop if alarm status information can't be retrieved from Amazon CloudWatch.
            alarms (list) --A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.
            (dict) --Information about an alarm.
            name (string) --The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.
            
            

    :type autoRollbackConfiguration: dict
    :param autoRollbackConfiguration: Information for an automatic rollback configuration that is added or changed when a deployment group is updated.
            enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.
            events (list) --The event type or types that trigger a rollback.
            (string) --
            

    :type deploymentStyle: dict
    :param deploymentStyle: Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.
            deploymentType (string) --Indicates whether to run an in-place deployment or a blue/green deployment.
            deploymentOption (string) --Indicates whether to route deployment traffic behind a load balancer.
            

    :type blueGreenDeploymentConfiguration: dict
    :param blueGreenDeploymentConfiguration: Information about blue/green deployment options for a deployment group.
            terminateBlueInstancesOnDeploymentSuccess (dict) --Information about whether to terminate instances in the original fleet during a blue/green deployment.
            action (string) --The action to take on instances in the original environment after a successful blue/green deployment.
            TERMINATE: Instances are terminated after a specified wait time.
            KEEP_ALIVE: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
            terminationWaitTimeInMinutes (integer) --The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
            deploymentReadyOption (dict) --Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.
            actionOnTimeout (string) --Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
            CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
            STOP_DEPLOYMENT: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.
            waitTimeInMinutes (integer) --The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT option for actionOnTimeout
            greenFleetProvisioningOption (dict) --Information about how instances are provisioned for a replacement environment in a blue/green deployment.
            action (string) --The method used to add instances to a replacement environment.
            DISCOVER_EXISTING: Use instances that already exist or will be created manually.
            COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.
            
            

    :type loadBalancerInfo: dict
    :param loadBalancerInfo: Information about the load balancer used in a deployment.
            elbInfoList (list) --An array containing information about the load balancer in Elastic Load Balancing to use in a deployment.
            (dict) --Information about a load balancer in Elastic Load Balancing to use in a deployment.
            name (string) --For blue/green deployments, the name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.
            
            

    :rtype: dict
    :return: {
        'hooksNotCleanedUp': [
            {
                'name': 'string',
                'hook': 'string'
            },
        ]
    }
    
    
    """
    pass

