"""
The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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
"""


def add_tags_to_on_premises_instances(tags=None, instanceNames=None):
    """
    :param tags: [REQUIRED]
            The tag key-value pairs to add to the on-premises instances.
            Keys and values are both required. Keys cannot be null or empty strings. Value-only tags are not allowed.
            (dict) --Information about a tag.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            
    :type tags: list
    :param instanceNames: [REQUIRED]
            The names of the on-premises instances to which to add tags.
            (string) --
            
    :type instanceNames: list
    """
    pass


def batch_get_application_revisions(applicationName=None, revisions=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application about which to get revision information.
            
    :type applicationName: string
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
            
            
    :type revisions: list
    """
    pass


def batch_get_applications(applicationNames=None):
    """
    :param applicationNames: A list of application names separated by spaces.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'applicationsInfo': [
                {
                  'applicationId': 'string',
                  'applicationName': 'string',
                  'createTime': datetime(2015, 1, 1),
                  'linkedToGitHub': True|False
                },
              ]
            }
            Response Structure
            (dict) --Represents the output of a batch get applications operation.
            applicationsInfo (list) --Information about the applications.
            (dict) --Information about an application.
            applicationId (string) --The application ID.
            applicationName (string) --The application name.
            createTime (datetime) --The time at which the application was created.
            linkedToGitHub (boolean) --True if the user has authenticated with GitHub for the specified application; otherwise, false.
            
            
            
    :type applicationNames: list
    """
    pass


def batch_get_deployment_groups(applicationName=None, deploymentGroupNames=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            
    :type applicationName: string
    :param deploymentGroupNames: [REQUIRED]
            The deployment groups' names.
            (string) --
            
    :type deploymentGroupNames: list
    """
    pass


def batch_get_deployment_instances(deploymentId=None, instanceIds=None):
    """
    :param deploymentId: [REQUIRED]
            The unique ID of a deployment.
            
    :type deploymentId: string
    :param instanceIds: [REQUIRED]
            The unique IDs of instances in the deployment group.
            (string) --
            
    :type instanceIds: list
    """
    pass


def batch_get_deployments(deploymentIds=None):
    """
    :param deploymentIds: A list of deployment IDs, separated by spaces.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'deploymentsInfo': [
                {
                  'applicationName': 'string',
                  'deploymentGroupName': 'string',
                  'deploymentConfigName': 'string',
                  'deploymentId': 'string',
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
                  'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped',
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
                    'Skipped': 123
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
                  }
                },
              ]
            }
            Response Structure
            (dict) --Represents the output of a batch get deployments operation.
            deploymentsInfo (list) --Information about the deployments.
            (dict) --Information about a deployment.
            applicationName (string) --The application name.
            deploymentGroupName (string) --The deployment group name.
            deploymentConfigName (string) --The deployment configuration name.
            deploymentId (string) --The deployment ID.
            revision (dict) --Information about the location of stored application artifacts and the service from which to retrieve them.
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
            
            status (string) --The current state of the deployment as a whole.
            errorInformation (dict) --Information about any error associated with this deployment.
            code (string) --The error code:
            APPLICATION_MISSING: The application was missing. This error code will most likely be raised if the application is deleted after the deployment is created but before it is started.
            DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code will most likely be raised if the deployment group is deleted after the deployment is created but before it is started.
            HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified.
            HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the instance health constraints specified.
            IAM_ROLE_MISSING: The service role cannot be accessed.
            IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.
            INTERNAL_ERROR: There was an internal error.
            NO_EC2_SUBSCRIPTION: The calling account is not subscribed to the Amazon EC2 service.
            NO_INSTANCES: No instance were specified, or no instance can be found.
            OVER_MAX_INSTANCES: The maximum number of instance was exceeded.
            THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more AWS services.
            TIMEOUT: The deployment has timed out.
            REVISION_MISSING: The revision ID was missing. This error code will most likely be raised if the revision is deleted after the deployment is created but before it is started.
            message (string) --An accompanying error message.
            createTime (datetime) --A timestamp indicating when the deployment was created.
            startTime (datetime) --A timestamp indicating when the deployment was deployed to the deployment group.
            In some cases, the reported value of the start time may be later than the complete time. This is due to differences in the clock settings of back-end servers that participate in the deployment process.
            completeTime (datetime) --A timestamp indicating when the deployment was complete.
            deploymentOverview (dict) --A summary of the deployment status of the instances in the deployment.
            Pending (integer) --The number of instances in the deployment in a pending state.
            InProgress (integer) --The number of instances in which the deployment is in progress.
            Succeeded (integer) --The number of instances in the deployment to which revisions have been successfully deployed.
            Failed (integer) --The number of instances in the deployment in a failed state.
            Skipped (integer) --The number of instances in the deployment in a skipped state.
            description (string) --A comment about the deployment.
            creator (string) --The means by which the deployment was created:
            user: A user created the deployment.
            autoscaling: Auto Scaling created the deployment.
            codeDeployRollback: A rollback process created the deployment.
            ignoreApplicationStopFailures (boolean) --If true, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will not be considered to have failed at that point and will continue on to the BeforeInstall deployment lifecycle event.
            If false or not specified, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will stop, and the deployment to that instance will be considered to have failed.
            autoRollbackConfiguration (dict) --Information about the automatic rollback configuration associated with the deployment.
            enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.
            events (list) --The event type or types that trigger a rollback.
            (string) --
            
            updateOutdatedInstancesOnly (boolean) --Indicates whether only instances that are not running the latest application revision are to be deployed to.
            rollbackInfo (dict) --Information about a deployment rollback.
            rollbackDeploymentId (string) --The ID of the deployment rollback.
            rollbackTriggeringDeploymentId (string) --The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.
            rollbackMessage (string) --Information describing the status of a deployment rollback; for example, whether the deployment can't be rolled back, is in progress, failed, or succeeded.
            
            
            
            
    :type deploymentIds: list
    """
    pass


def batch_get_on_premises_instances(instanceNames=None):
    """
    :param instanceNames: The names of the on-premises instances about which to get information.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'instanceInfos': [
                {
                  'instanceName': 'string',
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
            (dict) --Represents the output of a batch get on-premises instances operation.
            instanceInfos (list) --Information about the on-premises instances.
            (dict) --Information about an on-premises instance.
            instanceName (string) --The name of the on-premises instance.
            iamUserArn (string) --The IAM user ARN associated with the on-premises instance.
            instanceArn (string) --The ARN of the on-premises instance.
            registerTime (datetime) --The time at which the on-premises instance was registered.
            deregisterTime (datetime) --If the on-premises instance was deregistered, the time at which the on-premises instance was deregistered.
            tags (list) --The tags currently associated with the on-premises instance.
            (dict) --Information about a tag.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            
            
            
    :type instanceNames: list
    """
    pass


def can_paginate(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
    :type operation_name: string
    """
    pass


def create_application(applicationName=None):
    """
    :param applicationName: [REQUIRED]
            The name of the application. This name must be unique with the applicable IAM user or AWS account.
            Return typedict
            ReturnsResponse Syntax{
              'applicationId': 'string'
            }
            Response Structure
            (dict) --Represents the output of a create application operation.
            applicationId (string) --A unique application ID.
            
            
    :type applicationName: string
    """
    pass


def create_deployment(applicationName=None, deploymentGroupName=None, revision=None, deploymentConfigName=None,
                      description=None, ignoreApplicationStopFailures=None, autoRollbackConfiguration=None,
                      updateOutdatedInstancesOnly=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            
    :type applicationName: string
    :param deploymentGroupName: The name of the deployment group.
    :type deploymentGroupName: string
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
            
            
    :type revision: dict
    :param deploymentConfigName: The name of a deployment configuration associated with the applicable IAM user or AWS account.
            If not specified, the value configured in the deployment group will be used as the default. If the deployment group does not have a deployment configuration associated with it, then CodeDeployDefault.OneAtATime will be used by default.
            
    :type deploymentConfigName: string
    :param description: A comment about the deployment.
    :type description: string
    :param ignoreApplicationStopFailures: If set to true, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will not be considered to have failed at that point and will continue on to the BeforeInstall deployment lifecycle event.
            If set to false or not specified, then if the deployment causes the ApplicationStop deployment lifecycle event to fail to an instance, the deployment to that instance will stop, and the deployment to that instance will be considered to have failed.
            
    :type ignoreApplicationStopFailures: boolean
    :param autoRollbackConfiguration: Configuration information for an automatic rollback that is added when a deployment is created.
            enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.
            events (list) --The event type or types that trigger a rollback.
            (string) --
            
    :type autoRollbackConfiguration: dict
    :param updateOutdatedInstancesOnly: Indicates whether to deploy to all instances or only to instances that are not running the latest application revision.
    :type updateOutdatedInstancesOnly: boolean
    """
    pass


def create_deployment_config(deploymentConfigName=None, minimumHealthyHosts=None):
    """
    :param deploymentConfigName: [REQUIRED]
            The name of the deployment configuration to create.
            
    :type deploymentConfigName: string
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
            
    :type minimumHealthyHosts: dict
    """
    pass


def create_deployment_group(applicationName=None, deploymentGroupName=None, deploymentConfigName=None,
                            ec2TagFilters=None, onPremisesInstanceTagFilters=None, autoScalingGroups=None,
                            serviceRoleArn=None, triggerConfigurations=None, alarmConfiguration=None,
                            autoRollbackConfiguration=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            
    :type applicationName: string
    :param deploymentGroupName: [REQUIRED]
            The name of a new deployment group for the specified application.
            
    :type deploymentGroupName: string
    :param deploymentConfigName: If specified, the deployment configuration name can be either one of the predefined configurations provided with AWS CodeDeploy or a custom deployment configuration that you create by calling the create deployment configuration operation.
            Note
            CodeDeployDefault.OneAtATime is the default deployment configuration. It is used if a configuration isn't specified for the deployment or the deployment group.
            The predefined deployment configurations include the following:
            CodeDeployDefault.AllAtOnce attempts to deploy an application revision to as many instances as possible at once. The status of the overall deployment will be displayed as Succeeded if the application revision is deployed to one or more of the instances. The status of the overall deployment will be displayed as Failed if the application revision is not deployed to any of the instances. Using an example of nine instances, CodeDeployDefault.AllAtOnce will attempt to deploy to all nine instances at once. The overall deployment will succeed if deployment to even a single instance is successful; it will fail only if deployments to all nine instances fail.
            CodeDeployDefault.HalfAtATime deploys to up to half of the instances at a time (with fractions rounded down). The overall deployment succeeds if the application revision is deployed to at least half of the instances (with fractions rounded up); otherwise, the deployment fails. In the example of nine instances, it will deploy to up to four instances at a time. The overall deployment succeeds if deployment to five or more instances succeed; otherwise, the deployment fails. The deployment may be successfully deployed to some instances even if the overall deployment fails.
            CodeDeployDefault.OneAtATime deploys the application revision to only one instance at a time. For deployment groups that contain more than one instance:
            The overall deployment succeeds if the application revision is deployed to all of the instances. The exception to this rule is if deployment to the last instance fails, the overall deployment still succeeds. This is because AWS CodeDeploy allows only one instance at a time to be taken offline with the CodeDeployDefault.OneAtATime configuration.
            The overall deployment fails as soon as the application revision fails to be deployed to any but the last instance. The deployment may be successfully deployed to some instances even if the overall deployment fails.
            In an example using nine instances, it will deploy to one instance at a time. The overall deployment succeeds if deployment to the first eight instances is successful; the overall deployment fails if deployment to any of the first eight instances fails.
            For deployment groups that contain only one instance, the overall deployment is successful only if deployment to the single instance is successful
            
    :type deploymentConfigName: string
    :param ec2TagFilters: The Amazon EC2 tags on which to filter.
            (dict) --Information about a tag filter.
            Key (string) --The tag filter key.
            Value (string) --The tag filter value.
            Type (string) --The tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            
    :type ec2TagFilters: list
    :param onPremisesInstanceTagFilters: The on-premises instance tags on which to filter.
            (dict) --Information about an on-premises instance tag filter.
            Key (string) --The on-premises instance tag filter key.
            Value (string) --The on-premises instance tag filter value.
            Type (string) --The on-premises instance tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            
    :type onPremisesInstanceTagFilters: list
    :param autoScalingGroups: A list of associated Auto Scaling groups.
            (string) --
            
    :type autoScalingGroups: list
    :param serviceRoleArn: [REQUIRED]
            A service role ARN that allows AWS CodeDeploy to act on the user's behalf when interacting with AWS services.
            
    :type serviceRoleArn: string
    :param triggerConfigurations: Information about triggers to create when the deployment group is created. For examples, see Create a Trigger for an AWS CodeDeploy Event in the AWS CodeDeploy User Guide.
            (dict) --Information about notification triggers for the deployment group.
            triggerName (string) --The name of the notification trigger.
            triggerTargetArn (string) --The ARN of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.
            triggerEvents (list) --The event type or types for which notifications are triggered.
            (string) --
            
            
    :type triggerConfigurations: list
    :param alarmConfiguration: Information to add about Amazon CloudWatch alarms when the deployment group is created.
            enabled (boolean) --Indicates whether the alarm configuration is enabled.
            ignorePollAlarmFailure (boolean) --Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.
            true: The deployment will proceed even if alarm status information can't be retrieved from Amazon CloudWatch.
            false: The deployment will stop if alarm status information can't be retrieved from Amazon CloudWatch.
            alarms (list) --A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.
            (dict) --Information about an alarm.
            name (string) --The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.
            
            
    :type alarmConfiguration: dict
    :param autoRollbackConfiguration: Configuration information for an automatic rollback that is added when a deployment group is created.
            enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.
            events (list) --The event type or types that trigger a rollback.
            (string) --
            
    :type autoRollbackConfiguration: dict
    """
    pass


def delete_application(applicationName=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            ReturnsNone
            
    :type applicationName: string
    """
    pass


def delete_deployment_config(deploymentConfigName=None):
    """
    :param deploymentConfigName: [REQUIRED]
            The name of a deployment configuration associated with the applicable IAM user or AWS account.
            ReturnsNone
            
    :type deploymentConfigName: string
    """
    pass


def delete_deployment_group(applicationName=None, deploymentGroupName=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            
    :type applicationName: string
    :param deploymentGroupName: [REQUIRED]
            The name of an existing deployment group for the specified application.
            
    :type deploymentGroupName: string
    """
    pass


def deregister_on_premises_instance(instanceName=None):
    """
    :param instanceName: [REQUIRED]
            The name of the on-premises instance to deregister.
            ReturnsNone
            
    :type instanceName: string
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    :param ClientMethod: The client method to presign for
    :type ClientMethod: string
    :param Params: The parameters normally passed to
            ClientMethod.
    :type Params: dict
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
    :type ExpiresIn: int
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
    :type HttpMethod: string
    """
    pass


def get_application(applicationName=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            Return typedict
            ReturnsResponse Syntax{
              'application': {
                'applicationId': 'string',
                'applicationName': 'string',
                'createTime': datetime(2015, 1, 1),
                'linkedToGitHub': True|False
              }
            }
            Response Structure
            (dict) --Represents the output of a get application operation.
            application (dict) --Information about the application.
            applicationId (string) --The application ID.
            applicationName (string) --The application name.
            createTime (datetime) --The time at which the application was created.
            linkedToGitHub (boolean) --True if the user has authenticated with GitHub for the specified application; otherwise, false.
            
            
            
    :type applicationName: string
    """
    pass


def get_application_revision(applicationName=None, revision=None):
    """
    :param applicationName: [REQUIRED]
            The name of the application that corresponds to the revision.
            
    :type applicationName: string
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
            
            
    :type revision: dict
    """
    pass


def get_deployment(deploymentId=None):
    """
    :param deploymentId: [REQUIRED]
            A deployment ID associated with the applicable IAM user or AWS account.
            Return typedict
            ReturnsResponse Syntax{
              'deploymentInfo': {
                'applicationName': 'string',
                'deploymentGroupName': 'string',
                'deploymentConfigName': 'string',
                'deploymentId': 'string',
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
                'status': 'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped',
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
                  'Skipped': 123
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
                }
              }
            }
            Response Structure
            (dict) --Represents the output of a get deployment operation.
            deploymentInfo (dict) --Information about the deployment.
            applicationName (string) --The application name.
            deploymentGroupName (string) --The deployment group name.
            deploymentConfigName (string) --The deployment configuration name.
            deploymentId (string) --The deployment ID.
            revision (dict) --Information about the location of stored application artifacts and the service from which to retrieve them.
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
            
            status (string) --The current state of the deployment as a whole.
            errorInformation (dict) --Information about any error associated with this deployment.
            code (string) --The error code:
            APPLICATION_MISSING: The application was missing. This error code will most likely be raised if the application is deleted after the deployment is created but before it is started.
            DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code will most likely be raised if the deployment group is deleted after the deployment is created but before it is started.
            HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified.
            HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the instance health constraints specified.
            IAM_ROLE_MISSING: The service role cannot be accessed.
            IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.
            INTERNAL_ERROR: There was an internal error.
            NO_EC2_SUBSCRIPTION: The calling account is not subscribed to the Amazon EC2 service.
            NO_INSTANCES: No instance were specified, or no instance can be found.
            OVER_MAX_INSTANCES: The maximum number of instance was exceeded.
            THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more AWS services.
            TIMEOUT: The deployment has timed out.
            REVISION_MISSING: The revision ID was missing. This error code will most likely be raised if the revision is deleted after the deployment is created but before it is started.
            message (string) --An accompanying error message.
            createTime (datetime) --A timestamp indicating when the deployment was created.
            startTime (datetime) --A timestamp indicating when the deployment was deployed to the deployment group.
            In some cases, the reported value of the start time may be later than the complete time. This is due to differences in the clock settings of back-end servers that participate in the deployment process.
            completeTime (datetime) --A timestamp indicating when the deployment was complete.
            deploymentOverview (dict) --A summary of the deployment status of the instances in the deployment.
            Pending (integer) --The number of instances in the deployment in a pending state.
            InProgress (integer) --The number of instances in which the deployment is in progress.
            Succeeded (integer) --The number of instances in the deployment to which revisions have been successfully deployed.
            Failed (integer) --The number of instances in the deployment in a failed state.
            Skipped (integer) --The number of instances in the deployment in a skipped state.
            description (string) --A comment about the deployment.
            creator (string) --The means by which the deployment was created:
            user: A user created the deployment.
            autoscaling: Auto Scaling created the deployment.
            codeDeployRollback: A rollback process created the deployment.
            ignoreApplicationStopFailures (boolean) --If true, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will not be considered to have failed at that point and will continue on to the BeforeInstall deployment lifecycle event.
            If false or not specified, then if the deployment causes the ApplicationStop deployment lifecycle event to an instance to fail, the deployment to that instance will stop, and the deployment to that instance will be considered to have failed.
            autoRollbackConfiguration (dict) --Information about the automatic rollback configuration associated with the deployment.
            enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.
            events (list) --The event type or types that trigger a rollback.
            (string) --
            
            updateOutdatedInstancesOnly (boolean) --Indicates whether only instances that are not running the latest application revision are to be deployed to.
            rollbackInfo (dict) --Information about a deployment rollback.
            rollbackDeploymentId (string) --The ID of the deployment rollback.
            rollbackTriggeringDeploymentId (string) --The deployment ID of the deployment that was underway and triggered a rollback deployment because it failed or was stopped.
            rollbackMessage (string) --Information describing the status of a deployment rollback; for example, whether the deployment can't be rolled back, is in progress, failed, or succeeded.
            
            
            
    :type deploymentId: string
    """
    pass


def get_deployment_config(deploymentConfigName=None):
    """
    :param deploymentConfigName: [REQUIRED]
            The name of a deployment configuration associated with the applicable IAM user or AWS account.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the output of a get deployment configuration operation.
            deploymentConfigInfo (dict) --Information about the deployment configuration.
            deploymentConfigId (string) --The deployment configuration ID.
            deploymentConfigName (string) --The deployment configuration name.
            minimumHealthyHosts (dict) --Information about the number or percentage of minimum healthy instance.
            value (integer) --The minimum healthy instance value.
            type (string) --The minimum healthy instance type:
            HOST_COUNT: The minimum number of healthy instance as an absolute value.
            FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total number of instance in the deployment.
            In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to three instances at a time. The deployment will be successful if six or more instances are deployed to successfully; otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to five instance at a time. The deployment will be successful if four or more instance are deployed to successfully; otherwise, the deployment fails.
            Note
            In a call to the get deployment configuration operation, CodeDeployDefault.OneAtATime will return a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy will try to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment still succeeds.
            
            createTime (datetime) --The time at which the deployment configuration was created.
            
            
            
    :type deploymentConfigName: string
    """
    pass


def get_deployment_group(applicationName=None, deploymentGroupName=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            
    :type applicationName: string
    :param deploymentGroupName: [REQUIRED]
            The name of an existing deployment group for the specified application.
            
    :type deploymentGroupName: string
    """
    pass


def get_deployment_instance(deploymentId=None, instanceId=None):
    """
    :param deploymentId: [REQUIRED]
            The unique ID of a deployment.
            
    :type deploymentId: string
    :param instanceId: [REQUIRED]
            The unique ID of an instance in the deployment group.
            
    :type instanceId: string
    """
    pass


def get_on_premises_instance(instanceName=None):
    """
    :param instanceName: [REQUIRED]
            The name of the on-premises instance about which to get information.
            Return typedict
            ReturnsResponse Syntax{
              'instanceInfo': {
                'instanceName': 'string',
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
            (dict) --Represents the output of a get on-premises instance operation.
            instanceInfo (dict) --Information about the on-premises instance.
            instanceName (string) --The name of the on-premises instance.
            iamUserArn (string) --The IAM user ARN associated with the on-premises instance.
            instanceArn (string) --The ARN of the on-premises instance.
            registerTime (datetime) --The time at which the on-premises instance was registered.
            deregisterTime (datetime) --If the on-premises instance was deregistered, the time at which the on-premises instance was deregistered.
            tags (list) --The tags currently associated with the on-premises instance.
            (dict) --Information about a tag.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            
            
            
    :type instanceName: string
    """
    pass


def get_paginator(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
    :type operation_name: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_application_revisions(applicationName=None, sortBy=None, sortOrder=None, s3Bucket=None, s3KeyPrefix=None,
                               deployed=None, nextToken=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            
    :type applicationName: string
    :param sortBy: The column name to use to sort the list results:
            registerTime: Sort by the time the revisions were registered with AWS CodeDeploy.
            firstUsedTime: Sort by the time the revisions were first used in a deployment.
            lastUsedTime: Sort by the time the revisions were last used in a deployment.
            If not specified or set to null, the results will be returned in an arbitrary order.
            
    :type sortBy: string
    :param sortOrder: The order in which to sort the list results:
            ascending: ascending order.
            descending: descending order.
            If not specified, the results will be sorted in ascending order.
            If set to null, the results will be sorted in an arbitrary order.
            
    :type sortOrder: string
    :param s3Bucket: An Amazon S3 bucket name to limit the search for revisions.
            If set to null, all of the user's buckets will be searched.
            
    :type s3Bucket: string
    :param s3KeyPrefix: A key prefix for the set of Amazon S3 objects to limit the search for revisions.
    :type s3KeyPrefix: string
    :param deployed: Whether to list revisions based on whether the revision is the target revision of an deployment group:
            include: List revisions that are target revisions of a deployment group.
            exclude: Do not list revisions that are target revisions of a deployment group.
            ignore: List all revisions.
            
    :type deployed: string
    :param nextToken: An identifier returned from the previous list application revisions call. It can be used to return the next set of applications in the list.
    :type nextToken: string
    """
    pass


def list_applications(nextToken=None):
    """
    :param nextToken: An identifier returned from the previous list applications call. It can be used to return the next set of applications in the list.
            Return typedict
            ReturnsResponse Syntax{
              'applications': [
                'string',
              ],
              'nextToken': 'string'
            }
            Response Structure
            (dict) --Represents the output of a list applications operation.
            applications (list) --A list of application names.
            (string) --
            nextToken (string) --If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list applications call to return the next set of applications, will also be returned. in the list.
            
            
    :type nextToken: string
    """
    pass


def list_deployment_configs(nextToken=None):
    """
    :param nextToken: An identifier returned from the previous list deployment configurations call. It can be used to return the next set of deployment configurations in the list.
            Return typedict
            ReturnsResponse Syntax{
              'deploymentConfigsList': [
                'string',
              ],
              'nextToken': 'string'
            }
            Response Structure
            (dict) --Represents the output of a list deployment configurations operation.
            deploymentConfigsList (list) --A list of deployment configurations, including built-in configurations such as CodeDeployDefault.OneAtATime.
            (string) --
            nextToken (string) --If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment configurations call to return the next set of deployment configurations in the list.
            
            
    :type nextToken: string
    """
    pass


def list_deployment_groups(applicationName=None, nextToken=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            
    :type applicationName: string
    :param nextToken: An identifier returned from the previous list deployment groups call. It can be used to return the next set of deployment groups in the list.
    :type nextToken: string
    """
    pass


def list_deployment_instances(deploymentId=None, nextToken=None, instanceStatusFilter=None):
    """
    :param deploymentId: [REQUIRED]
            The unique ID of a deployment.
            
    :type deploymentId: string
    :param nextToken: An identifier returned from the previous list deployment instances call. It can be used to return the next set of deployment instances in the list.
    :type nextToken: string
    :param instanceStatusFilter: A subset of instances to list by status:
            Pending: Include those instance with pending deployments.
            InProgress: Include those instance where deployments are still in progress.
            Succeeded: Include those instances with successful deployments.
            Failed: Include those instance with failed deployments.
            Skipped: Include those instance with skipped deployments.
            Unknown: Include those instance with deployments in an unknown state.
            (string) --
            
    :type instanceStatusFilter: list
    """
    pass


def list_deployments(applicationName=None, deploymentGroupName=None, includeOnlyStatuses=None, createTimeRange=None,
                     nextToken=None):
    """
    :param applicationName: The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
    :type applicationName: string
    :param deploymentGroupName: The name of an existing deployment group for the specified application.
    :type deploymentGroupName: string
    :param includeOnlyStatuses: A subset of deployments to list by status:
            Created: Include created deployments in the resulting list.
            Queued: Include queued deployments in the resulting list.
            In Progress: Include in-progress deployments in the resulting list.
            Succeeded: Include successful deployments in the resulting list.
            Failed: Include failed deployments in the resulting list.
            Stopped: Include stopped deployments in the resulting list.
            (string) --
            
    :type includeOnlyStatuses: list
    :param createTimeRange: A time range (start and end) for returning a subset of the list of deployments.
            start (datetime) --The start time of the time range.
            Note
            Specify null to leave the start time open-ended.
            end (datetime) --The end time of the time range.
            Note
            Specify null to leave the end time open-ended.
            
    :type createTimeRange: dict
    :param nextToken: An identifier returned from the previous list deployments call. It can be used to return the next set of deployments in the list.
    :type nextToken: string
    """
    pass


def list_on_premises_instances(registrationStatus=None, tagFilters=None, nextToken=None):
    """
    :param registrationStatus: The registration status of the on-premises instances:
            Deregistered: Include deregistered on-premises instances in the resulting list.
            Registered: Include registered on-premises instances in the resulting list.
            
    :type registrationStatus: string
    :param tagFilters: The on-premises instance tags that will be used to restrict the corresponding on-premises instance names returned.
            (dict) --Information about an on-premises instance tag filter.
            Key (string) --The on-premises instance tag filter key.
            Value (string) --The on-premises instance tag filter value.
            Type (string) --The on-premises instance tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            
    :type tagFilters: list
    :param nextToken: An identifier returned from the previous list on-premises instances call. It can be used to return the next set of on-premises instances in the list.
    :type nextToken: string
    """
    pass


def register_application_revision(applicationName=None, description=None, revision=None):
    """
    :param applicationName: [REQUIRED]
            The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
            
    :type applicationName: string
    :param description: A comment about the revision.
    :type description: string
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
            
            
    :type revision: dict
    """
    pass


def register_on_premises_instance(instanceName=None, iamUserArn=None):
    """
    :param instanceName: [REQUIRED]
            The name of the on-premises instance to register.
            
    :type instanceName: string
    :param iamUserArn: [REQUIRED]
            The ARN of the IAM user to associate with the on-premises instance.
            
    :type iamUserArn: string
    """
    pass


def remove_tags_from_on_premises_instances(tags=None, instanceNames=None):
    """
    :param tags: [REQUIRED]
            The tag key-value pairs to remove from the on-premises instances.
            (dict) --Information about a tag.
            Key (string) --The tag's key.
            Value (string) --The tag's value.
            
            
    :type tags: list
    :param instanceNames: [REQUIRED]
            The names of the on-premises instances from which to remove tags.
            (string) --
            
    :type instanceNames: list
    """
    pass


def stop_deployment(deploymentId=None, autoRollbackEnabled=None):
    """
    :param deploymentId: [REQUIRED]
            The unique ID of a deployment.
            
    :type deploymentId: string
    :param autoRollbackEnabled: Indicates, when a deployment is stopped, whether instances that have been updated should be rolled back to the previous version of the application revision.
    :type autoRollbackEnabled: boolean
    """
    pass


def update_application(applicationName=None, newApplicationName=None):
    """
    :param applicationName: The current name of the application you want to change.
    :type applicationName: string
    :param newApplicationName: The new name to give the application.
    :type newApplicationName: string
    """
    pass


def update_deployment_group(applicationName=None, currentDeploymentGroupName=None, newDeploymentGroupName=None,
                            deploymentConfigName=None, ec2TagFilters=None, onPremisesInstanceTagFilters=None,
                            autoScalingGroups=None, serviceRoleArn=None, triggerConfigurations=None,
                            alarmConfiguration=None, autoRollbackConfiguration=None):
    """
    :param applicationName: [REQUIRED]
            The application name corresponding to the deployment group to update.
            
    :type applicationName: string
    :param currentDeploymentGroupName: [REQUIRED]
            The current name of the deployment group.
            
    :type currentDeploymentGroupName: string
    :param newDeploymentGroupName: The new name of the deployment group, if you want to change it.
    :type newDeploymentGroupName: string
    :param deploymentConfigName: The replacement deployment configuration name to use, if you want to change it.
    :type deploymentConfigName: string
    :param ec2TagFilters: The replacement set of Amazon EC2 tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.
            (dict) --Information about a tag filter.
            Key (string) --The tag filter key.
            Value (string) --The tag filter value.
            Type (string) --The tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            
    :type ec2TagFilters: list
    :param onPremisesInstanceTagFilters: The replacement set of on-premises instance tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.
            (dict) --Information about an on-premises instance tag filter.
            Key (string) --The on-premises instance tag filter key.
            Value (string) --The on-premises instance tag filter value.
            Type (string) --The on-premises instance tag filter type:
            KEY_ONLY: Key only.
            VALUE_ONLY: Value only.
            KEY_AND_VALUE: Key and value.
            
            
    :type onPremisesInstanceTagFilters: list
    :param autoScalingGroups: The replacement list of Auto Scaling groups to be included in the deployment group, if you want to change them. To keep the Auto Scaling groups, enter their names. To remove Auto Scaling groups, do not enter any Auto Scaling group names.
            (string) --
            
    :type autoScalingGroups: list
    :param serviceRoleArn: A replacement ARN for the service role, if you want to change it.
    :type serviceRoleArn: string
    :param triggerConfigurations: Information about triggers to change when the deployment group is updated. For examples, see Modify Triggers in an AWS CodeDeploy Deployment Group in the AWS CodeDeploy User Guide.
            (dict) --Information about notification triggers for the deployment group.
            triggerName (string) --The name of the notification trigger.
            triggerTargetArn (string) --The ARN of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.
            triggerEvents (list) --The event type or types for which notifications are triggered.
            (string) --
            
            
    :type triggerConfigurations: list
    :param alarmConfiguration: Information to add or change about Amazon CloudWatch alarms when the deployment group is updated.
            enabled (boolean) --Indicates whether the alarm configuration is enabled.
            ignorePollAlarmFailure (boolean) --Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.
            true: The deployment will proceed even if alarm status information can't be retrieved from Amazon CloudWatch.
            false: The deployment will stop if alarm status information can't be retrieved from Amazon CloudWatch.
            alarms (list) --A list of alarms configured for the deployment group. A maximum of 10 alarms can be added to a deployment group.
            (dict) --Information about an alarm.
            name (string) --The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.
            
            
    :type alarmConfiguration: dict
    :param autoRollbackConfiguration: Information for an automatic rollback configuration that is added or changed when a deployment group is updated.
            enabled (boolean) --Indicates whether a defined automatic rollback configuration is currently enabled.
            events (list) --The event type or types that trigger a rollback.
            (string) --
            
    :type autoRollbackConfiguration: dict
    """
    pass
